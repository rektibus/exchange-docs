# Binance API Documentation

> Three separate venues: **BINANCE** (spot), **BINANCE_FUTURES** (USDT-margined perps), **BINANCE_INVERSE** (coin-margined perps).
> Official docs: https://developers.binance.com/docs/
> Full spot spec cloned: `docs/external/binance-spot-api-docs/` (GitHub: `binance/binance-spot-api-docs`)

---

## Table of Contents

1. [Base URLs & Endpoints](#base-urls--endpoints)
2. [Rate Limits (REST)](#rate-limits-rest)
3. [WebSocket Connection Limits](#websocket-connection-limits)
4. [WebSocket Subscription Methods](#websocket-subscription-methods)
5. [WebSocket Streams — Spot](#websocket-streams--spot)
6. [WebSocket Streams — Futures (USDT-M + COIN-M)](#websocket-streams--futures-usdt-m--coin-m)
7. [REST API — Products / Exchange Info](#rest-api--products--exchange-info)
8. [REST API — Market Data](#rest-api--market-data)
9. [REST API — Futures-Only Endpoints](#rest-api--futures-only-endpoints)
10. [Orderbook Management](#orderbook-management)
11. [Filters](#filters)
12. [Config Differences: Spot vs Futures vs Inverse](#config-differences-spot-vs-futures-vs-inverse)
13. [Side Interpretation](#side-interpretation)
14. [Timestamps](#timestamps)

---

## Base URLs & Endpoints

### REST API

| Venue | Base URL(s) | Purpose |
|-------|-------------|---------|
| **Spot** | `https://api.binance.com` | Primary |
| | `https://api-gcp.binance.com` | GCP endpoint |
| | `https://api1.binance.com` | Better perf, less stable |
| | `https://api2.binance.com` | Better perf, less stable |
| | `https://api3.binance.com` | Better perf, less stable |
| | `https://api4.binance.com` | Better perf, less stable |
| | **`https://data-api.binance.vision`** | **Market data ONLY** (no auth endpoints) |
| **Futures (USDT-M)** | `https://fapi.binance.com` | All endpoints |
| **Inverse (COIN-M)** | `https://dapi.binance.com` | All endpoints |

> **`data-api.binance.vision`**: use for public market data (exchangeInfo, depth, aggTrades, klines, ticker) without requiring auth. No user data, no trading.

### WebSocket

| Venue | URL | Alt Port | Market-Data-Only |
|-------|-----|----------|------------------|
| **Spot** | `wss://stream.binance.com:9443/ws` | `wss://stream.binance.com:443/ws` | `wss://data-stream.binance.vision/ws` |
| **Futures (USDT-M)** | `wss://fstream.binance.com/ws` | — | — |
| **Inverse (COIN-M)** | `wss://dstream.binance.com/ws` | — | — |

**Spot WS access patterns:**
- **Raw stream**: `/ws/<streamName>` — single stream, events come unwrapped
- **Combined stream**: `/stream?streams=<s1>/<s2>/<s3>` — multiple streams, events wrapped: `{"stream":"<name>","data":<payload>}`

> **`data-stream.binance.vision`**: market data streams ONLY. User data stream is NOT available.

---

## Rate Limits (REST)

### Spot

| Limit Type | Value | Interval | Scope |
|-----------|-------|----------|-------|
| `REQUEST_WEIGHT` | **6000** | per 1 minute | per IP |
| `RAW_REQUESTS` | **61000** | per 5 minutes | per IP |
| Unfilled order count | varies per symbol | varies | per account |

> Limits tracked via response headers: `X-MBX-USED-WEIGHT-<intervalNum><intervalLetter>`

### Futures (USDT-M)

| Limit Type | Value | Interval |
|-----------|-------|----------|
| `REQUEST_WEIGHT` | **2400** | per 1 minute |
| `ORDERS` | **1200** | per 1 minute |

### Inverse (COIN-M)

| Limit Type | Value | Interval |
|-----------|-------|----------|
| `REQUEST_WEIGHT` | **2400** | per 1 minute |
| `ORDERS` | **1200** | per 1 minute |

### HTTP Status Codes

| Code | Meaning |
|------|---------|
| `429` | Rate limit exceeded — back off, obey `Retry-After` header |
| `418` | Auto-banned IP (kept sending after 429) — ban scales from 2min to 3 days |
| `403` | WAF rule violated (possible security block) |
| `5XX` | Internal server error — status UNKNOWN, could have succeeded |

### EnsoX Recovery Rate Limits

| Venue | `rate_limit_ms` | Effective |
|-------|----------------|-----------|
| Spot | 500ms | 2 req/s |
| Futures | 500ms | 2 req/s |
| Inverse | 1000ms | 1 req/s |

---

## WebSocket Connection Limits

### Spot

| Limit | Value |
|-------|-------|
| **Max streams per connection** | **1024** |
| **Max incoming messages per second** | **5** (ping, pong, subscribe/unsubscribe) |
| **Max new connections** | **300 per 5 minutes per IP** |
| **Connection lifetime** | **24 hours** (auto-disconnect) |
| **Server ping interval** | Every **20 seconds** |
| **Pong deadline** | Must respond within **60 seconds** |

### Futures (USDT-M + COIN-M)

| Limit | Value |
|-------|-------|
| **Max streams per connection** | **200** |
| **Connection lifetime** | **24 hours** |
| **Ping** | Native WebSocket ping/pong |

### `timeUnit` Parameter (Spot only)

Add `timeUnit=MICROSECOND` to WS URL for microsecond timestamps:
```
/stream?streams=btcusdt@trade&timeUnit=MICROSECOND
```

REST equivalent: header `X-MBX-TIME-UNIT:MICROSECOND`

---

## WebSocket Subscription Methods

### Method 1: URL-Based (Static)

Connect to a specific stream directly:
```
wss://stream.binance.com:9443/ws/btcusdt@aggTrade
```

Or multiple via combined stream:
```
wss://stream.binance.com:9443/stream?streams=btcusdt@aggTrade/btcusdt@depth@100ms/ethusdt@aggTrade
```

### Method 2: Dynamic Subscribe/Unsubscribe (JSON messages)

After connecting to `/ws` or `/stream`, send JSON messages to manage subscriptions:

**Subscribe:**
```json
{
  "method": "SUBSCRIBE",
  "params": ["btcusdt@aggTrade", "btcusdt@depth@100ms"],
  "id": 1
}
```

**Unsubscribe:**
```json
{
  "method": "UNSUBSCRIBE",
  "params": ["btcusdt@depth@100ms"],
  "id": 312
}
```

**List subscriptions:**
```json
{"method": "LIST_SUBSCRIPTIONS", "id": 3}
```
→ Response: `{"result": ["btcusdt@aggTrade"], "id": 3}`

**Set property (combined mode):**
```json
{"method": "SET_PROPERTY", "params": ["combined", true], "id": 5}
```

**Get property:**
```json
{"method": "GET_PROPERTY", "params": ["combined"], "id": 2}
```

**Ack response (all venues):**
```json
{"result": null, "id": 1}
```

### Method 3: Batch Subscribe (EnsoX pattern)

EnsoX uses batch subscribe — collect all stream names into one SUBSCRIBE message:
```json
{"method": "SUBSCRIBE", "params": ["btcusdt@aggTrade", "ethusdt@aggTrade", "btcusdt@depth@100ms", "ethusdt@depth@100ms"], "id": 1}
```

Config: `"subscribe_batch": "{\"method\":\"SUBSCRIBE\",\"params\":[{{params}}],\"id\":1}"`

### Method 4: Combined Stream URL (bulk)

```
wss://stream.binance.com:9443/stream?streams=btcusdt@aggTrade/ethusdt@aggTrade/btcusdt@depth@100ms
```

Events wrapped: `{"stream": "btcusdt@aggTrade", "data": {...}}`

### Available WS Methods

| Method | Description |
|--------|-------------|
| `SUBSCRIBE` | Subscribe to stream(s) |
| `UNSUBSCRIBE` | Unsubscribe from stream(s) |
| `LIST_SUBSCRIPTIONS` | List current subscriptions |
| `SET_PROPERTY` | Set connection property (only `combined` supported) |
| `GET_PROPERTY` | Get connection property |

### WS `id` Field

Accepts: 64-bit signed integer, alphanumeric string (max 36 chars), or `null`.

---

## WebSocket Streams — Spot

**Discriminator field: `"e"`** (event type)

### `<symbol>@trade` — Raw Trade Stream

**Speed:** Real-time

```json
{
  "e": "trade",
  "E": 1672515782136,
  "s": "BNBBTC",
  "t": 12345,
  "p": "0.001",
  "q": "100",
  "T": 1672515782136,
  "m": true,
  "M": true
}
```

| Field | Description |
|-------|-------------|
| `e` | Event type: `"trade"` |
| `E` | Event time (ms) |
| `s` | Symbol |
| `t` | Trade ID |
| `p` | Price (string) |
| `q` | Quantity (string) |
| `T` | Trade time (ms) |
| `m` | Is buyer the market maker? |

### `<symbol>@aggTrade` — Aggregate Trade Stream

**Speed:** Real-time

```json
{
  "e": "aggTrade",
  "E": 1672515782136,
  "s": "BNBBTC",
  "a": 12345,
  "p": "0.001",
  "q": "100",
  "f": 100,
  "l": 105,
  "T": 1672515782136,
  "m": true,
  "M": true
}
```

| Field | Description |
|-------|-------------|
| `a` | Aggregate trade ID |
| `f` | First trade ID |
| `l` | Last trade ID |

### `<symbol>@depth` / `<symbol>@depth@100ms` — Diff. Depth Stream

**Speed:** 1000ms or 100ms

```json
{
  "e": "depthUpdate",
  "E": 1672515782136,
  "s": "BNBBTC",
  "U": 157,
  "u": 160,
  "b": [["0.0024", "10"]],
  "a": [["0.0026", "100"]]
}
```

| Field | Description |
|-------|-------------|
| `U` | First update ID in event |
| `u` | Final update ID in event |
| `b` | Bids: `[price, qty]` arrays |
| `a` | Asks: `[price, qty]` arrays |

### `<symbol>@depth<levels>` / `<symbol>@depth<levels>@100ms` — Partial Book Depth

**Levels:** 5, 10, or 20 | **Speed:** 1000ms or 100ms

```json
{
  "lastUpdateId": 160,
  "bids": [["0.0024", "10"]],
  "asks": [["0.0026", "100"]]
}
```

> **Note:** No `"e"` discriminator — these are NOT wrapped in event type envelope.

### `<symbol>@kline_<interval>` — Kline/Candlestick Stream

**Speed:** 1s for `1s`, 2s for others

**Intervals:** `1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M`

With timezone: `<symbol>@kline_<interval>@+08:00`

```json
{
  "e": "kline",
  "E": 1672515782136,
  "s": "BNBBTC",
  "k": {
    "t": 1672515780000, "T": 1672515839999,
    "s": "BNBBTC", "i": "1m",
    "f": 100, "L": 200,
    "o": "0.0010", "c": "0.0020", "h": "0.0025", "l": "0.0015",
    "v": "1000", "n": 100, "x": false,
    "q": "1.0000", "V": "500", "Q": "0.500"
  }
}
```

### `<symbol>@miniTicker` — Individual Symbol Mini Ticker

**Speed:** 1000ms | Disc: `"24hrMiniTicker"`

### `!miniTicker@arr` — All Market Mini Tickers

**Speed:** 1000ms | Array of mini ticker objects

### `<symbol>@ticker` — Individual Symbol Ticker (24hr)

**Speed:** 1000ms | Disc: `"24hrTicker"`

Full 24hr stats: price change, VWAP, OHLC, volume, trade count, best bid/ask.

### `<symbol>@ticker_<window>` — Rolling Window Statistics

**Windows:** `1h, 4h, 1d` | **Speed:** 1000ms | Disc: `"1hTicker"` etc.

### `!ticker_<window>@arr` — All Market Rolling Window

Array of rolling window tickers.

### `<symbol>@bookTicker` — Best Bid/Ask

**Speed:** Real-time (no disc field — no `"e"`)

```json
{
  "u": 400900217,
  "s": "BNBUSDT",
  "b": "25.35190000",
  "B": "31.21000000",
  "a": "25.36520000",
  "A": "40.66000000"
}
```

### `<symbol>@avgPrice` — Average Price

**Speed:** 1000ms | Disc: `"avgPrice"`

---

## WebSocket Streams — Futures (USDT-M + COIN-M)

### `<symbol>@aggTrade` — Aggregate Trade Stream

Same as spot but with extra field:
- `"nq"` — normal quantity (excluding RPI orders, futures only)

### `<symbol>@depth@100ms` — Diff. Depth Stream

**Extra fields vs spot:**

```json
{
  "e": "depthUpdate",
  "E": 123456789,
  "T": 123456788,
  "s": "BTCUSDT",
  "U": 157,
  "u": 160,
  "pu": 149,
  "b": [["0.0024", "10"]],
  "a": [["0.0026", "100"]]
}
```

| Field | Description |
|-------|-------------|
| `T` | Transaction time (ms) |
| `pu` | **Previous final update ID** (for continuity check — spot does NOT have this) |

Available speeds: `@depth@250ms`, `@depth@500ms`, `@depth@100ms`, `@depth` (250ms default)

### `<symbol>@depth<levels>` — Partial Book Depth

Same levels (5, 10, 20) but with `@100ms`/`@250ms`/`@500ms` speed options.

### `<symbol>@markPrice` / `<symbol>@markPrice@1s` — Mark Price + Funding Rate

**Speed:** 3s default, 1s with `@1s` suffix

```json
{
  "e": "markPriceUpdate",
  "E": 1562305380000,
  "s": "BTCUSDT",
  "p": "11794.15000000",
  "i": "11784.62659091",
  "P": "11784.25641265",
  "r": "0.00038167",
  "T": 1562306400000
}
```

| Field | Description |
|-------|-------------|
| `p` | Mark price |
| `i` | Index price |
| `P` | Estimated settle price |
| `r` | **Funding rate** |
| `T` | Next funding time (ms) |

### `<symbol>@forceOrder` — Liquidation Order Stream

**Speed:** 1000ms (latest per 1s window)

```json
{
  "e": "forceOrder",
  "E": 1568014460893,
  "o": {
    "s": "BTCUSDT",
    "S": "SELL",
    "o": "LIMIT",
    "f": "IOC",
    "q": "0.014",
    "p": "9910",
    "ap": "9910",
    "X": "FILLED",
    "l": "0.014",
    "z": "0.014",
    "T": 1568014460893
  }
}
```

Config reads: `o.s` (symbol), `o.p` (price), `o.q` (quantity), `o.T` (timestamp), `o.S` (side).

### `<symbol>@kline_<interval>` — Kline Stream

Same as spot, same intervals.

### `<symbol>@bookTicker` — Book Ticker

Same as spot.

### `!markPrice@arr` / `!markPrice@arr@1s` — All Market Mark Price (Futures)

Array of all symbols' mark prices + funding rates.

### `<symbol>@compositeIndex` — Composite Index (Futures)

Price components for composite index symbols.

---

## REST API — Products / Exchange Info

### Spot — `GET /api/v3/exchangeInfo`

**Weight:** 20 | **Base:** any spot endpoint or `data-api.binance.vision`

**Params:** `symbol` (string), `symbols` (array), `permissions` (enum), `symbolStatus` (TRADING/HALT/BREAK), `showPermissionSets` (bool)

Response includes: `rateLimits[]`, `exchangeFilters[]`, `symbols[]` (with `status`, `baseAsset`, `quoteAsset`, `filters[]`, `orderTypes[]`, `permissionSets[]`), optionally `sors[]`.

### Futures — `GET /fapi/v1/exchangeInfo`

**Weight:** 1

Response includes: `rateLimits[]`, `assets[]` (marginAvailable, autoAssetExchange), `symbols[]` (with `contractType`, `status`, `pricePrecision`, `quantityPrecision`, `filters[]`, `liquidationFee`, `marketTakeBound`).

### Inverse — `GET /dapi/v1/exchangeInfo`

**Weight:** 1

Same as futures plus `contractSize`, `contractStatus` (vs `status`).

---

## REST API — Market Data

### Order Book — `GET /api/v3/depth` (Spot) / `/fapi/v1/depth` (Futures) / `/dapi/v1/depth` (Inverse)

**Spot weight by limit:**

| Limit | Weight |
|-------|--------|
| 1-100 | 5 |
| 101-500 | 25 |
| 501-1000 | 50 |
| 1001-5000 | 250 |

**Default:** 100 | **Max:** 5000 (spot), 1000 (futures/inverse)

**Spot params:** `symbol` (required), `limit`, `symbolStatus`

**Response:**
```json
{
  "lastUpdateId": 1027024,
  "bids": [["4.00000000", "431.00000000"]],
  "asks": [["4.00000200", "12.00000000"]]
}
```

Futures/inverse add: `"E"` (message time), `"T"` (transaction time).

---

### Recent Trades — `GET /api/v3/trades` (Spot only)

**Weight:** 25 | **Default:** 500 | **Max:** 1000

```json
[
  {
    "id": 28457,
    "price": "4.00000100",
    "qty": "12.00000000",
    "quoteQty": "48.000012",
    "time": 1499865549590,
    "isBuyerMaker": true,
    "isBestMatch": true
  }
]
```

---

### Old Trade Lookup — `GET /api/v3/historicalTrades` (Spot only)

**Weight:** 25 | **Params:** `symbol`, `limit` (max 1000), `fromId`

Same response as recent trades.

---

### Compressed/Aggregate Trades — `GET /api/v3/aggTrades` (Spot) / `/fapi/v1/aggTrades` (Futures) / `/dapi/v1/aggTrades` (Inverse)

| Venue | Weight | Default Limit | Max Limit |
|-------|--------|---------------|-----------|
| Spot | 4 | 500 | 1000 |
| Futures | 20 | 500 | 1000 |
| Inverse | 20 | 500 | 1000 |

**Params:** `symbol` (required), `fromId`, `startTime`, `endTime`, `limit`

**Constraints:**
- Futures: trades not older than **1 year**
- Futures: if both `startTime` AND `endTime` sent, window must be **< 1 hour**
- Don't send both `fromId` and `startTime`/`endTime` together (timeout risk)
- Without params: returns most recent

**Response (bare array, all venues):**
```json
[
  {
    "a": 26129,
    "p": "0.01633102",
    "q": "4.70443515",
    "f": 27781,
    "l": 27781,
    "T": 1498793709153,
    "m": true,
    "M": true
  }
]
```

| Field | Meaning |
|-------|---------|
| `a` | Aggregate trade ID |
| `p` | Price (string) |
| `q` | Quantity (string) |
| `f` | First trade ID |
| `l` | Last trade ID |
| `T` | Timestamp (ms) |
| `m` | Is buyer the market maker? |

---

### Kline/Candlestick — `GET /api/v3/klines` (Spot) / `/fapi/v1/klines` (Futures) / `/dapi/v1/klines` (Inverse)

**Weight:** 2 (spot) | **Default:** 500 | **Max:** 1000

**Params:** `symbol`, `interval`, `startTime`, `endTime`, `timeZone` (spot), `limit`

**Intervals:** `1s, 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M`

**Response (array of arrays):**
```json
[
  [
    1499040000000,      // Open time
    "0.01634790",       // Open
    "0.80000000",       // High
    "0.01575800",       // Low
    "0.01577100",       // Close
    "148976.11427815",  // Volume
    1499644799999,      // Close time
    "2434.19055334",    // Quote volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base volume
    "28.46694368",      // Taker buy quote volume
    "0"                 // Ignore
  ]
]
```

### UIKlines — `GET /api/v3/uiKlines` (Spot only)

Same as klines but optimized for candlestick chart display. Same params, same response.

---

### Current Average Price — `GET /api/v3/avgPrice` (Spot only)

**Weight:** 2

```json
{"mins": 5, "price": "9.35751834", "closeTime": 1694061154503}
```

---

### 24hr Ticker — `GET /api/v3/ticker/24hr` (Spot) / `/fapi/v1/ticker/24hr` (Futures)

Full 24hr rolling window stats.

---

### Symbol Price Ticker — `GET /api/v3/ticker/price` (Spot)

**Weight:** 2 (single) / 4 (all)

---

### Symbol Book Ticker — `GET /api/v3/ticker/bookTicker` (Spot)

**Weight:** 2 (single) / 4 (all)

---

### Test Connectivity — `GET /api/v3/ping` (Spot) / `GET /fapi/v1/ping` (Futures)

**Weight:** 1

---

### Server Time — `GET /api/v3/time` (Spot) / `GET /fapi/v1/time` (Futures)

**Weight:** 1

---

## REST API — Futures-Only Endpoints

### Open Interest — `GET /fapi/v1/openInterest` (Futures) / `GET /dapi/v1/openInterest` (Inverse)

**Weight:** 1

**Param:** `symbol` (required)

```json
{
  "openInterest": "10659.509",
  "symbol": "BTCUSDT",
  "time": 1589437530011
}
```

Config: `open_interest_endpoint: /fapi/v1/openInterest?symbol={{symbol}}`

---

### Mark Price / Premium Index — `GET /fapi/v1/premiumIndex` (Futures) / `GET /dapi/v1/premiumIndex` (Inverse)

Current mark price + funding rate:

```json
{
  "symbol": "BTCUSDT",
  "markPrice": "11012.80409769",
  "indexPrice": "11005.09520000",
  "estimatedSettlePrice": "11005.09520000",
  "lastFundingRate": "0.00038167",
  "nextFundingTime": 1597392000000,
  "interestRate": "0.00010000",
  "time": 1597370495002
}
```

Config: `funding_rate_endpoint: /fapi/v1/premiumIndex?symbol={{symbol}}`

---

### Funding Rate History — `GET /fapi/v1/fundingRate` (Futures)

**Weight:** shared 500/5min/IP with `/fapi/v1/fundingInfo`

**Params:** `symbol`, `startTime`, `endTime`, `limit` (default 100, max 1000)

```json
[
  {
    "symbol": "BTCUSDT",
    "fundingRate": "-0.03750000",
    "fundingTime": 1570608000000,
    "markPrice": "34287.54619963"
  }
]
```

---

### All Force Orders (Liquidations) — `GET /fapi/v1/allForceOrders`

Returns recent liquidation orders across all symbols.

Config: `liquidation_endpoint: /fapi/v1/allForceOrders`

---

## Orderbook Management

### Spot — How to Manage a Local Order Book

1. Open WS: `wss://stream.binance.com:9443/ws/bnbbtc@depth`
2. Buffer events. Note `U` of first event
3. Snapshot: `GET https://api.binance.com/api/v3/depth?symbol=BNBBTC&limit=5000`
4. If snapshot `lastUpdateId` < first event `U` → get snapshot again
5. Discard buffered events where `u` <= snapshot `lastUpdateId`
6. First remaining event: `lastUpdateId` within `[U, u]` range
7. Apply: if `u` < local updateId → ignore. If `U` > local updateId + 1 → restart
8. Normally: `U` of next event = `u + 1` of previous
9. For each level: set qty, or remove if qty = 0
10. Set local updateId = `u`

> Snapshot max: 5000 levels per side. Levels outside won't be known until they change.

### Futures/Inverse — How to Manage a Local Order Book

1. Open WS: `wss://fstream.binance.com/stream?streams=btcusdt@depth`
2. Buffer events
3. Snapshot: `GET https://fapi.binance.com/fapi/v1/depth?symbol=BTCUSDT&limit=1000`
4. Drop events where `u` < snapshot `lastUpdateId`
5. First event: `U` <= `lastUpdateId` AND `u` >= `lastUpdateId`
6. **Each subsequent event's `pu` must equal previous event's `u`** — if not, restart from step 3
7. Qty = 0 means remove level. Receiving removal of non-existent level is normal

> **Key difference:** Futures has `pu` (previous update ID) for continuity. Spot does not.

---

## Filters

Filters define trading rules per symbol and per exchange. Source: `exchangeInfo` response.

### Symbol Filters

| Filter | Description | Key Fields |
|--------|-------------|------------|
| `PRICE_FILTER` | Min/max price, tick size | `minPrice`, `maxPrice`, `tickSize` |
| `PERCENT_PRICE` | Price within % of avg | `multiplierUp`, `multiplierDown`, `avgPriceMins` |
| `PERCENT_PRICE_BY_SIDE` | % by buy/sell side | `bidMultiplierUp/Down`, `askMultiplierUp/Down` |
| `LOT_SIZE` | Min/max qty, step size | `minQty`, `maxQty`, `stepSize` |
| `MIN_NOTIONAL` | Min order value (price×qty) | `minNotional`, `applyToMarket` |
| `NOTIONAL` | Min + max notional | `minNotional`, `maxNotional` |
| `ICEBERG_PARTS` | Max iceberg parts | `limit` |
| `MARKET_LOT_SIZE` | Market order qty limits | `minQty`, `maxQty`, `stepSize` |
| `MAX_NUM_ORDERS` | Max open orders per symbol | `maxNumOrders` |
| `MAX_NUM_ALGO_ORDERS` | Max algo orders | `maxNumAlgoOrders` |
| `MAX_NUM_ICEBERG_ORDERS` | Max iceberg orders | `maxNumIcebergOrders` |
| `MAX_POSITION` | Max position (base asset) | `maxPosition` |
| `TRAILING_DELTA` | Trailing stop constraints | `minTrailingAboveDelta`, `maxTrailingAboveDelta` |
| `MAX_NUM_ORDER_AMENDS` | Max amendments per order | `maxNumOrderAmends` |
| `MAX_NUM_ORDER_LISTS` | Max open order lists | `maxNumOrderLists` |

### Exchange Filters

| Filter | Key |
|--------|-----|
| `EXCHANGE_MAX_NUM_ORDERS` | `maxNumOrders` (1000) |
| `EXCHANGE_MAX_NUM_ALGO_ORDERS` | `maxNumAlgoOrders` (200) |
| `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` | `maxNumIcebergOrders` (10000) |
| `EXCHANGE_MAX_NUM_ORDER_LISTS` | `maxNumOrderLists` (20) |

### Futures Filters

| Filter | Key |
|--------|-----|
| `PRICE_FILTER` | `tickSize` |
| `LOT_SIZE` | `stepSize`, `minQty`, `maxQty` |
| `MARKET_LOT_SIZE` | `stepSize`, `maxQty` |
| `MAX_NUM_ORDERS` | `limit` (200) |
| `MIN_NOTIONAL` | `notional` ("5.0") |
| `PERCENT_PRICE` | `multiplierUp`, `multiplierDown` |

---

## Config Differences: Spot vs Futures vs Inverse

| Aspect | BINANCE (Spot) | BINANCE_FUTURES (USDT-M) | BINANCE_INVERSE (COIN-M) |
|--------|---------------|-------------------------|-------------------------|
| **REST base** | `data-api.binance.vision` | `fapi.binance.com` | `dapi.binance.com` |
| **WS URL** | `stream.binance.com:9443` | `fstream.binance.com` | `dstream.binance.com` |
| **WS alt URL** | `:443` or `data-stream.binance.vision` | — | — |
| **Max streams/conn** | 1024 | 200 | 200 |
| **Trade stream** | `@trade` (raw) | `@aggTrade` | `@aggTrade` |
| **Trade disc.** | `"trade"` | `"aggTrade"` | `"aggTrade"` |
| **Trade ID field** | `t` | `a` | `a` |
| **Depth disc.** | `"depthUpdate"` | `"depthUpdate"` | `"depthUpdate"` |
| **Depth `pu`** | No | Yes | Yes |
| **Depth timestamp** | `E` | `E` | `E` |
| **Depth speeds** | `@100ms`, `@1000ms` | `@100ms/250ms/500ms` | `@100ms/250ms/500ms` |
| **Depth snapshot max** | 5000 | 1000 | 1000 |
| **Funding stream** | N/A | `@markPrice@1s` | `@markPrice` |
| **Liquidation stream** | N/A | `@forceOrder` | `@forceOrder` |
| **OI REST** | N/A | `/fapi/v1/openInterest` | `/dapi/v1/openInterest` |
| **Funding REST** | N/A | `/fapi/v1/premiumIndex` | `/dapi/v1/premiumIndex` |
| **Products path** | `/api/v3/exchangeInfo` | `/fapi/v1/exchangeInfo` | `/dapi/v1/exchangeInfo` |
| **Products weight** | 20 | 1 | 1 |
| **History path** | `/api/v3/aggTrades` | `/fapi/v1/aggTrades` | `/dapi/v1/aggTrades` |
| **History weight** | 4 | 20 | 20 |
| **History max age** | unlimited | 1 year | 1 year |
| **Products filter** | `status: TRADING` | `status: TRADING` | `contractType: PERPETUAL` + `contractStatus: TRADING` |
| **Contract size** | N/A | N/A | `contractSize` field |
| **Ping interval** | 30s | 30s | 60s |
| **Rate limit (recovery)** | 500ms | 500ms | 1000ms |
| **REST weight limit** | 6000/min | 2400/min | 2400/min |
| **WS msg limit** | 5/s | — | — |
| **Polling interval** | N/A | 20s | 20s |
| **Side field** | `m` (is buyer maker) | `m` (is buyer maker) | `m` (is buyer maker) |
| **String numbers** | yes | yes | yes |

---

## Side Interpretation

All venues use `"m"` (is buyer the market maker):
- `m: true` → seller is the taker → **SELL**
- `m: false` → buyer is the taker → **BUY**

For liquidations (`forceOrder`), field `o.S`: `"BUY"` or `"SELL"` (uppercase string).

```json
"side_map": {
  "true": "sell",
  "false": "buy",
  "BUY": "buy",
  "SELL": "sell",
  "buy": "buy",
  "sell": "sell",
  "Buy": "buy",
  "Sell": "sell"
}
```

---

## Timestamps

**All timestamps are milliseconds** (epoch ms) across all venues and endpoints.

| Field | Unit | Context |
|-------|------|---------|
| `E` (event time) | ms | All WS events |
| `T` (trade/transaction time) | ms | All WS events |
| `time` | ms | REST responses |
| `fundingTime` / `nextFundingTime` | ms | Funding REST |
| `startTime` / `endTime` params | ms | All REST queries |
| `timestamp` (SIGNED requests) | ms or µs | Auth requests |

**Microsecond option (spot only):**
- WS: `timeUnit=MICROSECOND` URL param
- REST: `X-MBX-TIME-UNIT:MICROSECOND` header

---

## Full Spec Reference

The complete Binance spot API specification is available locally at:
- `docs/external/binance-spot-api-docs/rest-api.md` (4787 lines, 172KB — ALL REST endpoints)
- `docs/external/binance-spot-api-docs/web-socket-streams.md` (597 lines — ALL WS streams)
- `docs/external/binance-spot-api-docs/web-socket-api.md` (271KB — WebSocket-based API for trading)
- `docs/external/binance-spot-api-docs/fix-api.md` (168KB — FIX protocol)
- `docs/external/binance-spot-api-docs/sbe/` (SBE binary protocol)
- `docs/external/binance-spot-api-docs/filters.md` (356 lines — all filters)
- `docs/external/binance-spot-api-docs/errors.md` (error codes)
- `docs/external/binance-spot-api-docs/enums.md` (enums)
- `docs/external/binance-spot-api-docs/user-data-stream.md` (user data stream)
- `docs/external/binance-spot-api-docs/CHANGELOG.md` (117KB — full changelog)

No official GitHub repo for futures/inverse API docs. Futures reference: https://developers.binance.com/docs/derivatives/usds-margined-futures/
