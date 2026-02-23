# BigONE API Documentation

> Two distinct APIs: **Spot** (Protobuf WS, Viabtc-style engine) and **Futures** (JSON WS, per-symbol URL).
> Spot base: `https://big.one` | Futures base: `https://api.big.one/api/contract/v2`

---

## BIGONE (Spot)

### REST API — Base URL: `https://big.one`

#### Products — `GET /api/v3/asset_pairs`

**Response**: `{code: 0, data: [...]}`

```json
{
  "id": "550b34db-...",
  "name": "BTC-USDT",
  "quote_scale": 2,
  "quote_asset": {"id": "...", "symbol": "USDT", "name": "TetherUS"},
  "base_asset": {"id": "...", "symbol": "BTC", "name": "Bitcoin"},
  "base_scale": 6,
  "min_quote_value": "10",
  "max_quote_value": "1000000"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Symbol (e.g. "BTC-USDT"), separator `-` |
| `base_asset.symbol` | string | Base currency |
| `quote_asset.symbol` | string | Quote currency |
| `quote_scale` | integer | Price precision (decimal places) |
| `base_scale` | integer | Quantity precision (decimal places) |

#### Trades — `GET /api/v3/asset_pairs/{pair}/trades?limit=N`

Symbol in URL path (e.g. `BTC-USDT`). Default and max returns ~150 trades (limit param accepted but capped at ~150).

**Response**: `{code: 0, data: [...]}`

```json
{
  "id": 5601695069,
  "price": "68428.33",
  "amount": "0.003374",
  "taker_side": "ASK",
  "inserted_at": "2026-02-17T04:44:50.165Z",
  "created_at": "2026-02-17T04:44:50.165Z"
}
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | integer | Trade ID |
| `price` | string | Trade price |
| `amount` | string | Trade quantity |
| `taker_side` | string | "BID" (buy) / "ASK" (sell) |
| `inserted_at` | string | ISO 8601 timestamp |
| `created_at` | string | ISO 8601 timestamp |

#### Depth (Orderbook Snapshot) — `GET /api/v3/asset_pairs/{pair}/depth?limit=N`

Symbol in URL path. Supports `limit` param (max **200** levels per side, default 50).

**Response**: `{code: 0, data: {asset_pair_name, bids: [...], asks: [...]}}`

```json
{
  "asset_pair_name": "BTC-USDT",
  "bids": [
    {"price": "67801.27", "order_count": 1, "quantity": "0.001429"},
    {"price": "67791.10", "order_count": 1, "quantity": "0.02"}
  ],
  "asks": [
    {"price": "67808.06", "order_count": 1, "quantity": "0.001844"},
    {"price": "67818.23", "order_count": 1, "quantity": "0.02"}
  ]
}
```

| Field | Type | Description |
|-------|------|-------------|
| `asset_pair_name` | string | Symbol |
| `bids[].price` | string | Bid price |
| `bids[].quantity` | string | Bid quantity |
| `bids[].order_count` | integer | Number of orders at this level |
| `asks[].price` | string | Ask price |
| `asks[].quantity` | string | Ask quantity |

**Level format**: Named fields (`price`, `quantity`). Matches config `level_format: "named"`, `price_field: "price"`, `size_field: "quantity"`.

#### Ticker — `GET /api/v3/asset_pairs/{pair}/ticker`

**Response**: `{code: 0, data: {asset_pair_name, bid, ask, open, high, low, close, volume, daily_change}}`

```json
{
  "asset_pair_name": "BTC-USDT",
  "bid": {"price": "67801.27", "order_count": 1, "quantity": "0.001429"},
  "ask": {"price": "67808.06", "order_count": 1, "quantity": "0.001844"},
  "open": "68621.75",
  "high": "70097.88",
  "low": "67298.01",
  "close": "67804.67",
  "volume": "1855.733078",
  "daily_change": "-817.08"
}
```

#### REST API Summary (Spot)

| Endpoint | Status | Response Wrapper |
|----------|--------|-----------------|
| `/api/v3/asset_pairs` | ✅ | `{code:0, data:[]}` |
| `/api/v3/asset_pairs/{pair}/trades` | ✅ ~150 trades (no pagination) | `{code:0, data:[]}` |
| `/api/v3/asset_pairs/{pair}/depth` | ✅ max 200 levels | `{code:0, data:{}}` |
| `/api/v3/asset_pairs/{pair}/ticker` | ✅ | `{code:0, data:{}}` |
| `/api/v3/asset_pairs/{pair}/order_book` | ❌ 404 | — |

---

### WebSocket API — `wss://api.big.one/ws/v2`

**Protocols**: JSON (default) or Binary protobuf (set `Sec-WebSocket-Protocol: proto` header).
**Proto definitions**: https://github.com/bigone-eng/websocket-proto
**Heartbeat**: Custom heartbeat message or native WebSocket ping.
**Max streams**: 50 symbols per connection.
**Dedicated adapter**: `bigone.ex` — handles protobuf encode/decode in Elixir, emits normalized JSON to Zig.

#### Protocol Selection

| Protocol | How | Format |
|----------|-----|--------|
| **JSON** (default) | Connect without special header | Text frames |
| **Protobuf** | Set `Sec-WebSocket-Protocol: proto` | Binary frames, decode with `websocket.proto` |

Protobuf recommended for production — 10x smaller messages, lower latency.

#### Request/Response Format

All requests use a `requestId` field for correlation. Responses include `requestId` matching the original request.

**Response field numbers (protobuf)**:

| Field | Type |
|-------|------|
| 98 | Success ack |
| 99 | Error (code=1, message=2) |
| 100 | Pong |
| 103 | TradesSnapshot (repeated Trade at field 1) |
| 104 | TradeUpdate (Trade at field 1) |
| 105 | DepthSnapshot (Depth at field 1, change_id at field 2) |
| 106 | DepthUpdate (Depth at field 1, change_id at field 2, prev_id at field 3) |
| 109 | CandlesSnapshot |
| 110 | CandleUpdate |
| 200 | Heartbeat |

#### WS Market Trades

**Subscribe (JSON)**:
```json
{"requestId": "1", "subscribeMarketTradesRequest": {"market": "BTC-USDT", "limit": 20}}
```

**Unsubscribe (JSON)**:
```json
{"requestId": "1", "unsubscribeMarketTradesRequest": {"market": "BTC-USDT"}}
```

**Subscribe (Protobuf)**: Request field 102 = SubscribeMarketTradesRequest (market=1, limit=2)

**Response**: TradesSnapshot (initial batch), then TradeUpdate for each new trade.

**Trade message fields**:

| Field # | Name | Type | Description |
|---------|------|------|-------------|
| 1 | id | uint64 | Trade ID |
| 2 | price | string | Trade price |
| 3 | amount | string | Trade quantity |
| 4 | market | string | Symbol (e.g. "BTC-USDT") |
| 7 | created_at | google.protobuf.Timestamp | seconds=1, nanos=2 |
| 11 | taker_side | enum | BID=0 (buy), ASK=1 (sell) |

> Note: In public trade streams, `makerOrder` and `takerOrder` fields are always null.

#### WS Market Depth (Order Book) ✅

BigONE spot **does** provide WebSocket depth via both JSON and protobuf protocols.

**Subscribe (JSON)**:
```json
{"requestId": "1", "subscribeMarketDepthRequest": {"market": "BTC-USDT"}}
```

**Unsubscribe (JSON)**:
```json
{"requestId": "1", "unsubscribeMarketDepthRequest": {"market": "BTC-USDT"}}
```

**Subscribe (Protobuf)**: Request field 103 = SubscribeMarketDepthRequest (market=1)

**Response flow**:
1. **DepthSnapshot** — full orderbook on subscribe
2. **DepthUpdate** — incremental changes after snapshot

**DepthSnapshot (proto field 105)**:

| Field # | Name | Type | Description |
|---------|------|------|-------------|
| 1 | depth | Depth | Full orderbook |
| 2 | change_id | uint64 | Sequence ID for this snapshot |

**DepthUpdate (proto field 106)**:

| Field # | Name | Type | Description |
|---------|------|------|-------------|
| 1 | depth | Depth | Changed levels only |
| 2 | change_id | uint64 | Current sequence ID |
| 3 | prev_id | uint64 | Previous sequence ID (for continuity check) |

**Depth message**:

| Field # | Name | Type | Description |
|---------|------|------|-------------|
| 1 | market | string | Symbol (e.g. "BTC-USDT") |
| 2 | asks | repeated PriceLevel | Ask levels |
| 3 | bids | repeated PriceLevel | Bid levels |

**PriceLevel**:

| Field # | Name | Type | Description |
|---------|------|------|-------------|
| 1 | price | string | Price level |
| 2 | amount | string | Quantity at this level |
| 3 | order_count | int64 | Number of orders at this level |

**Level format**: Named fields (`price`, `amount`). Amount = 0 means remove level.

**Continuity check**: `change_id` of current message must equal `prev_id` of next message. If mismatch, re-subscribe to get a fresh snapshot.

#### WS Market Candles (K-Line)

**Subscribe (JSON)**:
```json
{"requestId": "2", "subscribeMarketCandlesRequest": {"market": "BTC-USDT", "period": "MIN5", "limit": "20"}}
```

**Periods**: MIN1, MIN5, MIN15, MIN30, HOUR1, HOUR3, HOUR4, HOUR6, HOUR12, DAY1, WEEK1

#### WS Market Ticker

**Subscribe (JSON)**:
```json
{"requestId": "3", "subscribeMarketsTickerRequest": {"markets": ["BTC-USDT", "ETH-USDT"]}}
```

> Note: Can subscribe to multiple markets in one request (array).

#### WS Available Channels Summary

| Channel | Subscribe Request | Snapshot | Update |
|---------|------------------|----------|--------|
| **Trades** | `subscribeMarketTradesRequest` | TradesSnapshot | TradeUpdate |
| **Depth** | `subscribeMarketDepthRequest` | DepthSnapshot | DepthUpdate |
| **Candles** | `subscribeMarketCandlesRequest` | CandlesSnapshot | CandleUpdate |
| **Ticker** | `subscribeMarketsTickerRequest` | TickersSnapshot | TickerUpdate |

#### Side Map (Spot)

| Wire Value | Meaning |
|------------|---------|
| BID / 0 | Buy (taker buys) |
| ASK / 1 | Sell (taker sells) |

---

## BIGONE_FUTURES (Perp)

> Official docs: https://open.big.one/docs/contract/introduction
> OpenAPI spec cloned: `docs/external/bigone-openapi-specs/contract_rest.yml` (40KB)

### REST API — Base URL: `https://api.big.one/api/contract/v2`

#### Contract Specs — `GET /symbols`

**Response**: Bare JSON array `[...]` (no wrapper).

```json
{
  "symbol": "BTCUSDT",
  "baseCurrency": "BTC",
  "quoteCurrency": "USDT",
  "multiplier": 0.001,
  "priceStep": 0.5,
  "pricePrecision": 1,
  "valuePrecision": 4,
  "enable": true,
  "isInverse": false,
  "initialMargin": 0.01,
  "maintenanceMargin": 0.005,
  "settleCurrency": "USDT",
  "maxRiskLimit": 10000000,
  "minRiskLimit": 1000000,
  "riskLimit": 1000000,
  "riskStep": 10000,
  "priceMin": 0.5,
  "priceMax": 1000000
}
```

| Field | Type | Description |
|-------|------|-------------|
| `symbol` | string | Contract symbol (e.g. "BTCUSDT") — no separator |
| `baseCurrency` | string | Base asset |
| `quoteCurrency` | string | Quote asset |
| `multiplier` | number | Contract size (e.g. 0.001 BTC per contract) |
| `priceStep` | number | Tick size |
| `pricePrecision` | integer | Price decimal places |
| `valuePrecision` | integer | Quantity decimal places |
| `enable` | boolean | Whether contract is active |
| `isInverse` | boolean | true for coin-margined (BTCUSD, ETHUSD), false for USDT-margined |
| `settleCurrency` | string | Settlement currency |

**Note**: Both linear (USDT-margined) and inverse (coin-margined) contracts are returned. Config filters with `enable: true` + `isInverse: false` for linear only.

#### Instruments (Funding + OI + Market Data) — `GET /instruments`

**Response**: Bare JSON array `[...]` — returns ALL contracts in one call (bulk endpoint).

```json
{
  "symbol": "BTCUSD",
  "fundingRate": 0.0001974,
  "nextFundingRate": 0.0001,
  "openInterest": 1376246,
  "markPrice": 87422.65,
  "latestPrice": 87391,
  "indexPrice": 87413.1,
  "btcPrice": 87413.1,
  "ethPrice": 2921.36,
  "usdtPrice": 0.99929568,
  "nextFundingTime": 1766685600000,
  "volume24h": 3889971,
  "volume24hInUsd": 3891564.21,
  "turnover24h": 44.5192334698948,
  "last24hPriceChange": 0.0041,
  "last24hMaxPrice": 87997.5,
  "last24hMinPrice": 86313.5,
  "openValue": 29.7443056608277
}
```

| Field | Type | Description |
|-------|------|-------------|
| `symbol` | string | Contract symbol |
| `fundingRate` | number | Current funding rate |
| `nextFundingRate` | number | Predicted next funding rate |
| `openInterest` | number | Open interest (in contracts) |
| `markPrice` | number | Mark price |
| `indexPrice` | number | Index price |
| `latestPrice` | number | Last trade price |
| `nextFundingTime` | integer | Next funding timestamp (**milliseconds**) |
| `volume24h` | number | 24h volume (contracts) |
| `volume24hInUsd` | number | 24h volume (USD equivalent) |
| `turnover24h` | number | 24h turnover (settlement currency) |
| `usdtPrice` | number | USDT index price |
| `btcPrice` | number | BTC index price |

#### Depth Snapshot — `GET /depth@{symbol}/snapshot`

**Response**: Object with `bids`/`asks` as **object maps** (price → quantity).

```json
{
  "bids": {"86559": 90688, "86000": 10},
  "asks": {"86928": 86506, "86925.5": 92840},
  "to": 3425679898,
  "from": 0,
  "lastPrice": 86902,
  "bestPrices": {"ask": 86925.5, "bid": 86900.5}
}
```

| Field | Type | Description |
|-------|------|-------------|
| `bids` | object | Map of `{price: quantity}` for buy orders |
| `asks` | object | Map of `{price: quantity}` for sell orders |
| `from` | integer | Starting sequence ID (0 for snapshot) |
| `to` | integer | Ending sequence ID |
| `lastPrice` | number | Most recent trade price |
| `bestPrices` | object | `{ask: number, bid: number}` |

**Level format**: `object_map` — key is price (string), value is quantity (number). Qty = 0 means remove level.

#### Historical Prices (Undocumented) — `GET /instruments/prices`

> **NOT in official docs or OpenAPI spec.** Discovered via CCXT source code (`contractPublicGetInstrumentsPrices`). Matches orphan `PricePoint` schema in `contract_rest.yml`. **Verified live.**

```
GET https://api.big.one/api/contract/v2/instruments/prices
```

**Response**: Object keyed by symbol, each containing array of 48 price points (30-min candle closes, ~24h history):
```json
{
  "BTCUSD": [
    {"time": 1771329600000, "price": 68029.500000000000000000},
    {"time": 1771327800000, "price": 67791.000000000000000000},
    ...
  ],
  "ETHUSDT": [...],
  ...
}
```

| Field | Type | Description |
|-------|------|-------------|
| `time` | integer | **Milliseconds** timestamp (30-min intervals) |
| `price` | number | Close price at that 30-min candle |

**Notes**:
- Always returns ALL symbols (40+), `?symbol=` param is ignored
- 48 data points per symbol = 24 hours at 30-minute intervals
- Values are numbers with 18 decimal places (high precision)
- Some low-liquidity symbols show flat prices (e.g. XINUSDT always 110.0, AUSDT always 0.085)

#### 24h Price Change (Undocumented) — `GET /instruments/difference`

> **NOT in official docs or OpenAPI spec.** Discovered via CCXT source code (`contractPublicGetInstrumentsDifference`). **Verified live.**

```
GET https://api.big.one/api/contract/v2/instruments/difference
```

**Response**: Object keyed by symbol, values are 24h price change ratios (NOT percentage):
```json
{
  "BTCUSD": -0.02369385983166022,
  "ETHUSDT": -0.017032928666194543,
  "SOLUSDT": -0.010566651184393995,
  "MERLUSDT": 0.11802232854864417,
  ...
}
```

**Notes**:
- Negative values = price declined (e.g. -0.024 = -2.4%)
- Always returns ALL symbols, `?symbol=` param is ignored
- Multiply by 100 for percentage

#### REST API Summary (Futures)

| Endpoint | Auth | Description |
|----------|------|-------------|
| `GET /symbols` | ❌ Public | Contract specifications |
| `GET /instruments` | ❌ Public | All instruments (funding, OI, prices) |
| `GET /depth@{symbol}/snapshot` | ❌ Public | Orderbook snapshot |
| `GET /instruments/prices` | ❌ Public | **Undocumented** — 24h of 30-min close prices (all symbols) |
| `GET /instruments/difference` | ❌ Public | **Undocumented** — 24h price change ratios (all symbols) |
| `GET /trades` | ✅ Private | User trade history |
| `GET /orders` | ✅ Private | Order list |
| `GET /accounts` | ✅ Private | Balance + positions |

> **No public REST trade history.** `GET /trades` requires authentication. Use WS for public trades.

---

### WebSocket API (JSON, Per-Symbol URL)

> Docs: https://open.big.one/docs/contract/pusher

**Format**: Plain JSON (NOT protobuf — completely different from spot).
**Subscribe**: No subscribe message needed — data streams automatically on connect.
**Heartbeat**: Native WebSocket ping, 30s interval.
**Max streams**: 1 per connection (per-symbol URL pattern).

> **⚠️ Intro doc discrepancy**: The contract introduction page claims WebSocket URL is `wss://api.big.one/ws/v2` (same as spot). **This is WRONG for contract data** — tested live, returns 403. The correct contract WS URL uses per-symbol pattern: `wss://api.big.one/ws/contract/v2/{channel}@{symbol}`.
>
> The intro also claims "Prices and Amounts: Returned as strings." **This is only true for REST/spot.** Contract WS returns `price` and `size` as **numbers** (verified live).

#### WS Trades — `wss://api.big.one/ws/contract/v2/trades@{symbol}`

```
wscat -c wss://api.big.one/ws/contract/v2/trades@BTCUSD
```

**Snapshot** (array of recent trades on connect):
```json
[
  {
    "id": "671ace9b-18c0-0001-0000-00000d858a3b",
    "symbol": "BTCUSD",
    "price": 67680,
    "size": 1018,
    "matchedAt": 1771325516899,
    "side": "SELL"
  }
]
```

**Real-time** (array with single trade):
```json
[
  {
    "id": "671acea3-5600-0001-0000-00000d858a77",
    "symbol": "BTCUSD",
    "price": 67667.5,
    "size": 60,
    "matchedAt": 1771325525336,
    "side": "BUY"
  }
]
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | string | Trade ID (UUID format) |
| `symbol` | string | Contract symbol |
| `price` | **number** | Trade price (NOT string — verified live) |
| `size` | **number** | Trade quantity in contracts (NOT string) |
| `matchedAt` | integer | **Milliseconds** timestamp |
| `side` | string | "BUY" / "SELL" |

#### WS Depth — `wss://api.big.one/ws/contract/v2/depth@{symbol}`

```
wscat -c wss://api.big.one/ws/contract/v2/depth@BTCUSD
```

**Snapshot** (first message):
```json
{
  "bids": {"11192": 35, "11184": 742, "11192.5": 389, "11188": 293},
  "asks": {"11202.5": 1806, "11212.5": 2138, "11211.5": 19308},
  "lastPrice": 11183.5,
  "bestPrices": {"ask": 11202.5, "bid": 11192.5},
  "from": 0,
  "to": 91277134
}
```

**Incremental update**:
```json
{
  "bids": {"11183": 3500},
  "asks": {},
  "lastPrice": 11183.5,
  "bestPrices": {"ask": 11202.5, "bid": 11192.5},
  "from": 91277135,
  "to": 91277135
}
```

| Field | Type | Description |
|-------|------|-------------|
| `bids` | object | `{price: qty}` — bid levels (qty=0 = remove) |
| `asks` | object | `{price: qty}` — ask levels (qty=0 = remove) |
| `from` | integer | Start sequence ID (0 = snapshot) |
| `to` | integer | End sequence ID |
| `lastPrice` | number | Most recent trade price |
| `bestPrices` | object | `{ask, bid}` |

**Level format**: `object_map` — keys are price strings, values are quantity numbers.

**Continuity**: `from` of next message should equal `to + 1` of previous. If gap detected, reconnect.

#### WS Candles — `wss://api.big.one/ws/contract/v2/candlesticks/{period}@{symbol}`

```
wscat -c wss://api.big.one/ws/contract/v2/candlesticks/1MIN@BTCUSD
```

**Periods**: 1MIN, 5MIN, 15MIN, 30MIN, 1H, 4H, 6H, 12H, 1D

```json
[
  {
    "symbol": "BTCUSD",
    "type": "1MIN",
    "time": 1562301000000,
    "open": 11119.5,
    "close": 11109.5,
    "high": 11123.5,
    "low": 11109.5,
    "nTrades": 4,
    "volume": 3427,
    "turnover": 0.30820388075,
    "version": 91383701,
    "nextTs": 1562301060000
  }
]
```

#### WS Instruments — `wss://api.big.one/ws/contract/v2/instruments@{symbol}` or `/instruments`

Real-time funding rate, OI, mark price, index price.

- **Single symbol**: `wss://api.big.one/ws/contract/v2/instruments@BTCUSD`
- **All instruments**: `wss://api.big.one/ws/contract/v2/instruments`

```json
[
  {
    "symbol": "BTCUSD",
    "fundingRate": 0,
    "openInterest": 3412,
    "markPrice": 11255.51,
    "indexPrice": 11255.51,
    "latestPrice": 11290,
    "btcPrice": 11255.51,
    "volume24h": 4000,
    "volume24hInUsd": 4000,
    "turnover24h": 0.354295837,
    "openValue": 0.300825969916003,
    "last24hMaxPrice": 11290,
    "last24hMinPrice": 11290
  }
]
```

> **Funding+OI available via WS!** No need to poll REST `/instruments` — subscribe to `instruments@{symbol}` for real-time updates.

#### WS Available Channels Summary (Futures)

| Channel | URL Pattern | Format | Subscribe |
|---------|------------|--------|-----------|
| **Trades** | `trades@{symbol}` | Array of trades | Auto on connect |
| **Depth** | `depth@{symbol}` | Object map + seq IDs | Auto on connect |
| **Candles** | `candlesticks/{period}@{symbol}` | Array of candles | Auto on connect |
| **Instruments** | `instruments@{symbol}` or `instruments` | Array of instruments | Auto on connect |

#### Side Map (Futures)

| Wire Value | Meaning |
|------------|---------|
| BUY | Buy |
| SELL | Sell |

---

## Key Differences: Spot vs Futures

| Aspect | BIGONE (Spot) | BIGONE_FUTURES (Perp) |
|--------|---------------|----------------------|
| **Docs** | `open.big.one/docs/spot/` | `open.big.one/docs/contract/` |
| **WS Protocol** | JSON or Binary protobuf | Plain JSON |
| **WS URL** | Single shared `wss://api.big.one/ws/v2` | Per-symbol `wss://api.big.one/ws/contract/v2/{channel}@{symbol}` (**verified** — intro doc's claim of `ws/v2` returns 403) |
| **WS Header** | `Sec-WebSocket-Protocol: proto` (optional) | None |
| **Subscribe** | JSON/Protobuf message required | No message (auto-stream on connect) |
| **Adapter** | Dedicated `bigone.ex` (protobuf) | Generic WS worker |
| **Symbol format** | `BTC-USDT` (dash separator) | `BTCUSDT` (no separator) |
| **Side values** | BID/ASK (or 0/1 enum) | BUY/SELL |
| **Trade timestamp** | google.protobuf.Timestamp | Milliseconds (integer) |
| **Trade price/size** | String | Number (**verified** — intro doc claims strings, but live WS sends numbers) |
| **REST trades** | ✅ `/api/v3/asset_pairs/{pair}/trades` (no limit param) | ❌ Private only |
| **REST depth** | ✅ `/api/v3/asset_pairs/{pair}/depth` (**max 200** levels, named) | ✅ `/depth@{symbol}/snapshot` (object_map) |
| **Products** | `{code:0, data:[]}` | Bare `[]` array |
| **Depth WS** | ✅ JSON + Protobuf (change_id/prev_id) | ✅ JSON (from/to seq IDs, object_map) |
| **Funding/OI WS** | N/A (spot) | ✅ `instruments@{symbol}` (real-time) |
| **Funding/OI REST** | N/A | ✅ `/instruments` (bulk) |
| **Depth format** | Named: `{price, quantity, order_count}` | Object map: `{price_string: qty_number}` |
| **Liquidations** | N/A (spot) | ❌ No public feed (private `isLiquidate` flag on orders) |
| **L/S Ratio** | N/A | ❌ Not available |
| **Contract types** | — | Linear (USDT) + Inverse (USD) |

## Data Availability for EnsoX

| Data Type | Spot | Futures | Recovery? |
|-----------|------|---------|-----------|
| **Trades (WS)** | ✅ JSON + Protobuf | ✅ JSON (per-symbol URL) | N/A (live) |
| **Trades (REST)** | ✅ Public (no pagination params) | ❌ Private only | ⚠️ Spot only, no time-range |
| **Depth (WS)** | ✅ Snapshot + incremental (change_id/prev_id) | ✅ Snapshot + incremental (from/to seq) | N/A (live) |
| **Depth (REST)** | ✅ Max 200 levels | ✅ Snapshot endpoint | ✅ For OB rebuild on reconnect |
| **Funding rate** | N/A | ✅ REST `/instruments` + WS `instruments@` | Point-in-time (no history endpoint) |
| **Open Interest** | N/A | ✅ REST `/instruments` + WS `instruments@` | Point-in-time (no history endpoint) |
| **Liquidations** | N/A | ❌ No public feed | ❌ |
| **L/S Ratio** | N/A | ❌ Not available | ❌ |
| **Candles** | ✅ REST + WS (12 periods, max 500) | ✅ WS only (9 periods) | REST spot only |

> **Recovery limitations**: No public REST trade history for futures (auth required). Spot REST trades have no pagination/time-range params, so only recent trades retrievable. No historical funding or OI endpoints — only current snapshot. Depth REST snapshot available for both venues (useful for orderbook rebuild on reconnect).

## CCXT & OpenAPI Cross-Reference Analysis

> Analysis based on CCXT library (`ccxt_bigone.py`) and OpenAPI specs (`contract_rest.yml`).

### Undocumented Endpoints

| Endpoint | Found In | Purpose |
|----------|----------|---------|
| `GET /instruments/prices` | CCXT (`contractPublicGetInstrumentsPrices`) | 30-min candle closes (24h) |
| `GET /instruments/difference` | CCXT (`contractPublicGetInstrumentsDifference`) | 24h price change ratios |

Both are **public, unauthenticated**, and return ALL symbols regardless of query params.

### Orphaned Schema: `PricePoint`

The OpenAPI spec `contract_rest.yml` defines a `PricePoint` schema (`time` + `price` fields) that is **not referenced by any documented endpoint**. The `/instruments/prices` response matches this schema exactly — confirming the endpoint exists but was omitted from official documentation.

### Timestamp Discrepancy

| Context | Unit | Example |
|---------|------|---------|
| WS Trades (`instruments@`) | **Seconds** (`1771330247`) | Via confirmed WS testing |
| REST `/instruments` | **Seconds** (same format) | Live API call |
| REST `/instruments/prices` | **Milliseconds** (`1771329600000`) | **Different from all others** |

> ⚠️ The undocumented `/prices` endpoint uses **milliseconds** while all other contract endpoints use **seconds**.

### Liquidation Data Availability

| Source | Finding |
|--------|---------|
| **Official Docs** | ❌ No public liquidation feed documented |
| **CCXT** | `type_enum` in `contracts` market includes: `NORMAL`, `ADL` (auto-deleverage), `FUNDING` |
| **WS Trades** | Trades MAY carry `type` field distinguishing normal vs ADL vs funding — **needs WS confirmation** |
| **REST** | No public endpoint for liquidation history |

### CCXT Contract Trade Support

CCXT explicitly raises `NotSupported` for contract trades: "bigone does not support fetchTrades for contract markets" (`fetch_trades()` line 785). Only spot `fetchTrades()` and `fetchOrderBook()` are implemented for contracts.

### CCXT Confirms Depth Format

`parse_contract_order_book()` confirms depth is `object_map` format:
```python
# CCXT iterates dict entries: key = price, value = quantity
# Consistent with our `/depth@{symbol}/snapshot` testing
```

## Full Spec Reference

- Spot: `docs/external/bigone-openapi-specs/spot_rest.yml` (36KB — all REST endpoints)
- Contract: `docs/external/bigone-openapi-specs/contract_rest.yml` (40KB — all REST endpoints)
- Spot WS: https://open.big.one/docs/spot/pusher
- Contract WS: https://open.big.one/docs/contract/pusher
- Protobuf: https://github.com/bigone-eng/websocket-proto
- CCXT: `docs/external/ccxt_bigone.py` (2268 lines — full exchange implementation)
- OpenAPI specs: https://github.com/bigone-eng/openapi-specs
