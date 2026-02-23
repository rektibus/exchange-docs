# Hyperliquid API Reference (Local)

> Saved 2026-02-22. Source: https://hyperliquid.gitbook.io/hyperliquid-docs/

## SDK Repos (cloned to docs/external/)
- `hyperliquid-python-sdk/` — Python SDK
- `hyperliquid-ts-sdk/` — TypeScript SDK (nktkas)
- `hyperliquid-rust-sdk/` — Rust SDK

## Architecture

Hyperliquid is a DEX (L1 blockchain). Single API endpoint for ALL REST: `POST https://api.hyperliquid.xyz/info`.
Single WS endpoint: `wss://api.hyperliquid.xyz/ws`. Both perps AND spot share the same endpoints.

**Key difference from CEXes**: No separate base URLs for spot vs futures. The `type` field in the POST body determines the response. Spot symbols use pair names (`PURR/USDC` or `@{index}`), futures use coin names (`BTC`, `ETH`).

## Products

### Futures (Perpetuals)
- **Request**: `POST /info` with `{"type":"meta"}`
- **Response**: `{universe: [{szDecimals, name, maxLeverage, marginTableId}], marginTables, collateralToken}`
- **Symbol format**: Just the coin name: `BTC`, `ETH`, `ATOM`
- **Count**: ~229 perps
- **All linear (USD-margined)**, no inverse contracts
- **contract_size**: Always 1 (native units)

### Spot
- **Request**: `POST /info` with `{"type":"spotMeta"}`
- **Response**: `{universe: [{tokens: [base_idx, quote_idx], name, index, isCanonical}], tokens: [{name, szDecimals, ...}]}`
- **Symbol format**: 
  - Canonical pairs: `PURR/USDC` (only PURR is canonical)
  - All other pairs: `@{index}` (e.g. `@1`, `@107`)
  - The `name` field from universe IS the WS subscribe symbol
- **Quote token**: Always token index 0 = USDC
- **Base/Quote resolution**: Must join `universe[i].tokens[0]` → `tokens[base_idx].name` for base, `tokens[quote_idx].name` for quote
- **Count**: ~275 spot pairs

### Asset Contexts (Funding + OI)
- **Request**: `POST /info` with `{"type":"metaAndAssetCtxs"}`
- **Response**: Array of 2 elements:
  - `[0]`: Same as `meta` response (universe + marginTables)
  - `[1]`: Array of per-asset contexts (same order as universe), each:
    ```json
    {"funding": "0.0000055847", "openInterest": "21012.3622", "prevDayPx": "68256.0",
     "dayNtlVlm": "830487590.42", "premium": "-0.0005040397", "oraclePx": "67455.0",
     "markPx": "67422.0", "midPx": "67420.5", "impactPxs": ["67420.0", "67421.0"]}
    ```
  - ALL values are strings
  - `string_numbers: true` required

### Historical Funding Rates
- **Request**: `POST /info` with `{"type":"fundingHistory","coin":"BTC","startTime":ms,"endTime":ms}`
- **Response**: Array of `{coin, fundingRate, premium, time}`
- Pagination: 500 elements max, use last `time` as next `startTime`

## WebSocket

### Connection
- URL: `wss://api.hyperliquid.xyz/ws`
- Subscribe: `{"method":"subscribe","subscription":{"type":"<type>","coin":"<coin>"}}`
- Ack: `{"channel":"subscriptionResponse","data":{...}}`
- Ping: `{"method":"ping"}` → responds with `{"channel":"pong"}`

### Trades
- Subscribe: `{"method":"subscribe","subscription":{"type":"trades","coin":"BTC"}}`
- Channel: `trades`
- Data format: Array of trades in `data` field:
  ```json
  {"coin":"BTC","side":"B","px":"67423.0","sz":"0.00003","time":1771794660102,
   "hash":"0x109dd...","tid":375940249318652,"users":["0x...","0x..."]}
  ```
- **side**: `"B"` = buy, `"A"` = sell
- **time**: milliseconds
- **All values are strings** (px, sz)
- **Spot**: subscribe with pair name: `{"type":"trades","coin":"PURR/USDC"}` or `{"type":"trades","coin":"@107"}`

### L2 Book (Depth)
- Subscribe: `{"method":"subscribe","subscription":{"type":"l2Book","coin":"BTC"}}`
- Channel: `l2Book`
- Data format:
  ```json
  {"coin":"BTC","time":1771794656744,"levels":[
    [{{"px":"67422.0","sz":"21.38891","n":35}, ...}],  // bids
    [{{"px":"67423.0","sz":"0.5","n":2}, ...}]          // asks
  ]}
  ```
- **`levels[0]` = bids, `levels[1]` = asks**
- **Named format**: `{px, sz, n}` (n = number of orders)
- **IS SNAPSHOT**: Every message is a full book snapshot (verified: all levels present every time, sizes change between messages)
- **`data` wrapper**: depth data is nested under `data` key: `{"channel":"l2Book","data":{"coin":...,"time":...,"levels":...}}`

### L2 Book REST Snapshot
- **Request**: `POST /info` with `{"type":"l2Book","coin":"BTC"}`
- **Response**: `{"coin":"BTC","time":ms,"levels":[[bids],[asks]]}` (max 20 levels per side)
- Same format as WS but top-level (no `data` wrapper)

### Liquidations (Futures only)
- Subscribe: `{"method":"subscribe","subscription":{"type":"liquidations"}}`  
- **Global broadcast** — no `coin` filter, receives ALL liquidations
- Channel: `liquidations`
- **RARELY fires** — waited 30s with 0 liquidations during testing
- Data format (from existing config, needs live verification):
  ```json
  {"channel":"liquidations","data":{"coin":"BTC","side":"B","px":"67000.0","sz":"0.5","time":ms}}
  ```
- Fields nested under `data` (not array)

### ActiveAssetCtx (WS Funding + OI per coin)
- Subscribe: `{"method":"subscribe","subscription":{"type":"activeAssetCtx","coin":"BTC"}}`
- Channel: `activeAssetCtx`
- Data format: `WsActiveAssetCtx` (perps) or `WsActiveSpotAssetCtx` (spot)
- Contains funding, OI, mark price, premium etc. — same data as `metaAndAssetCtxs` but streaming

## REST Trade History

### Recent Trades
- **Request**: `POST /info` with `{"type":"recentTrades","coin":"BTC"}`
- **Response**: Array of 10 trades (FIXED — no `limit` param observed)
- Same format as WS trades: `{coin, side, px, sz, time, hash, tid, users}`
- **Only returns 10 trades** — NOT suitable for gap recovery

### Pagination & Time Range
- Docs say: "Responses that take a time range will only return 500 elements or distinct blocks of data. To query larger ranges, use the last returned timestamp as the next startTime for pagination."
- `recentTrades` does NOT appear to support `startTime`/`endTime`
- **Gap recovery may require candle snapshots instead**

### Candle Snapshot
- **Request**: `POST /info` with `{"type":"candleSnapshot","req":{"coin":"BTC","interval":"1m","startTime":ms,"endTime":ms}}`
- Max 5000 candles
- Supports: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 8h, 12h, 1d, 3d, 1w, 1M

## Rate Limits
- `rate_limit_ms: 50` in existing config
- REST polling recommended at 20s intervals for funding/OI

## Key Quirks

1. **ALL REST is POST** — no GET endpoints. Each "endpoint" is a different `type` in the POST body.
2. **Spot symbols are weird**: Most are `@{index}`, only PURR/USDC is canonical. Base/quote must be resolved via token index lookup.
3. **String numbers everywhere**: All prices, sizes, funding rates are strings.
4. **No trade history pagination for recovery**: `recentTrades` returns only 10 trades with no time-range params. Recovery would need candle snapshots.
5. **Funding/OI via bulk POST**: `metaAndAssetCtxs` returns ALL coins at once as parallel arrays — requires index-based lookup (universe[i] ↔ assetCtxs[i]).
6. **Historical funding rates**: `fundingHistory` endpoint with `startTime`/`endTime` and 500-element pagination.
7. **Liquidations are rare events**: Global broadcast, no per-symbol filter.
8. **Same WS/REST for spot and perps**: Differentiated only by symbol format.
