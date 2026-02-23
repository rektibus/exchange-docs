# Arkham Exchange API Documentation

> **Base URL**: `https://arkm.com`
> **WS URL**: `wss://arkm.com/ws`
> **Auth**: Public endpoints require no authentication
> **Markets**: Spot + USDT Perpetuals (linear)
> **Symbol format**: `BTC_USDT` (spot), `BTC_USDT_PERP` (perps)
> **OpenAPI spec**: `https://arkm.com/openapi.json` (verified ✅)
> **CCXT Pro source**: `docs/external/ccxt_pro/arkham.py` (verified ✅)
> **Arkham SDK**: `github.com/arkhamintelligence/arkham-sdk-typescript`

## REST Endpoints (Public)

### GET `/api/public/pairs`
Returns all trading pairs (spot + perps).

**Response**: Bare JSON array `[{...}, ...]`

```json
{
  "symbol": "BTC_USDT",
  "baseSymbol": "BTC",
  "quoteSymbol": "USDT",
  "pairType": "spot",          // "spot" or "perpetual"
  "maxLeverage": "0",          // "0" for spot, "10"/"25" for perps
  "status": "listed",          // "listed" or "staged"
  "minTickPrice": "0.01",
  "minLotSize": "0.00001",
  "minNotional": "0.1",
  "maxSize": "9000",
  "marginSchedule": "C"        // perps only
}
```

**Notes**: Futures pairs have `baseSymbol` with `.P` suffix (e.g. `BTC.P`). Must strip via `normalization.base_strip_suffix: ".P"`.

### GET `/api/public/trades`
Returns recent trades for a symbol.

**Params**: `symbol` (required), `limit` (optional, default/max unknown — tested with 1000)

**Response**: Bare JSON array (newest first)

```json
[
  {
    "symbol": "BTC_USDT",
    "revisionId": 25080884544,     // trade ID (integer)
    "size": "0.00721",             // quantity (STRING)
    "price": "68179.46",           // price (STRING)
    "takerSide": "sell",           // "buy" or "sell"
    "time": 1771182819281618       // MICROSECONDS (integer)
  }
]
```

**Key observations**:
- `time` is in **microseconds** (16 digits)
- `size` and `price` are **strings**
- `takerSide` values: `"buy"`, `"sell"` (lowercase)
- `revisionId` is an integer, suitable for `trade_id`

### GET `/api/public/book`
Returns orderbook snapshot for a symbol.

**Params**: `symbol` (required), `group` (optional, price grouping)

**Response**:
```json
{
  "symbol": "BTC_USDT",
  "group": "0.01",
  "asks": [{"price": "68600.00", "size": "0.5"}, ...],
  "bids": [{"price": "68500.00", "size": "1.2"}, ...],
  "lastTime": 1771252442458026          // microseconds
}
```

**Notes**: `asks`/`bids` use **named** format with `price` and `size` fields (NOT indexed arrays).

### GET `/api/public/ticker`
Returns 24h ticker data. For perps, includes funding and OI info.

**Params**: `symbol` (required)

**Response** (perp example):
```json
{
  "symbol": "BTC_USDT_PERP",
  "baseSymbol": "BTC.P",
  "quoteSymbol": "USDT",
  "price": "68578.85",
  "price24hAgo": "68961.72",
  "high24h": "70043.66",
  "low24h": "68336.55",
  "volume24h": "2.14447",
  "quoteVolume24h": "147941.5564152",
  "markPrice": "68544.85",
  "indexPrice": "68544.848171896",
  "fundingRate": "0",
  "nextFundingRate": "0",
  "nextFundingTime": 1771300800000000,   // microseconds
  "productType": "perpetual",
  "openInterest": "0",
  "openInterestUSD": "0",
  "indexCurrency": "USDT",
  "usdVolume24h": "147941.5564152"
}
```

### GET `/api/public/candles`
Returns historical klines.

**Params**: `symbol`, `interval` (1m/5m/15m/30m/1h/6h/24h), `startTime`/`endTime` (microseconds)

### Other Public Endpoints
- `GET /api/public/server-time` — server time
- `GET /api/public/tickers` — all tickers
- `GET /api/public/index-price` — index price
- `GET /api/public/index-prices` — all index prices
- `GET /api/public/margin-schedules` — margin tiers
- `GET /api/public/contracts` — contract specs
- `GET /api/public/chains` — chain info
- `GET /api/public/assets` — asset list

---

## WebSocket API (VERIFIED from CCXT Pro source)

### Connection
- **URL**: `wss://arkm.com/ws`
- **Ping**: Native WebSocket ping, every 30s
- **Compression**: None
- **Same WS URL for spot AND futures**

### Subscription Format
```json
{
  "method": "subscribe",
  "confirmationId": "trade-BTC_USDT",
  "args": {
    "channel": "trades",
    "params": {
      "symbol": "BTC_USDT"
    }
  }
}
```

### Ack Messages
```json
{"channel": "confirmations", "confirmationId": "trade-BTC_USDT"}
```
Also: messages with `"channel": "errors"` are error responses.

### Discriminator
**ALL messages use `"channel"` as the discriminator field** — same for spot and futures.

### Available Channels
| Channel | Type | Subscribe |
|---------|------|-----------|
| `trades` | trade | Yes |
| `l2_updates` | depth | Yes (with `"snapshot": true`) |
| `ticker` | ticker | Yes |
| `candles` | OHLCV | Yes (with `"duration"`) |
| `confirmations` | ack | — |
| `errors` | error | — |
| `balances` | balance (auth) | Yes |
| `positions` | positions (auth) | Yes |
| `order_statuses` | orders (auth) | Yes |
| `trigger_orders` | trigger orders (auth) | Yes |

### Trade Messages (VERIFIED)
Channel: `"trades"` — **SAME format for spot AND futures**

```json
{
  "channel": "trades",
  "type": "update",
  "data": {
    "symbol": "BTC_USDT",
    "revisionId": 2643896903,
    "size": "0.00261",
    "price": "118273.2",
    "takerSide": "buy",
    "time": 1755200320146389
  }
}
```

- **Timestamp**: `data.time` in **microseconds** (16 digits)
- **Side**: `data.takerSide` — `"buy"` or `"sell"`
- **All values are strings** (string_numbers)
- **Trade ID**: `data.revisionId`

### Depth Messages (VERIFIED)
Channel: `"l2_updates"`

**Snapshot** (first message after subscribe with `snapshot: true`):
```json
{
  "channel": "l2_updates",
  "type": "snapshot",
  "data": {
    "symbol": "BTC_USDT",
    "group": "0.01",
    "asks": [{"price": "122722.76", "size": "0.05"}],
    "bids": [{"price": "122700.00", "size": "0.1"}],
    "lastTime": 1755115180608299
  }
}
```

**Update** (incremental):
```json
{
  "channel": "l2_updates",
  "type": "update",
  "data": {
    "symbol": "BTC_USDT",
    "group": "0.01",
    "side": "sell",
    "size": "0.05295",
    "price": "122722.76",
    "revisionId": 2455511217,
    "time": 1755115736475207
  }
}
```

- **Level format**: Named (`price`, `size` fields) — NOT indexed arrays
- **First message is snapshot** (`type: "snapshot"`)
- **Updates are individual levels** with `side` field
- **`size: "0"` means remove** the price level
- **Depths**: configurable via `depth` param (5, 10, 20, 50, 100)
- **Interval**: configurable via `interval` param (100, 200, 500, 1000 ms)

### Ticker Messages
Channel: `"ticker"`

```json
{
  "channel": "ticker",
  "type": "update",
  "data": {
    "symbol": "BTC_USDT",
    "baseSymbol": "BTC",
    "quoteSymbol": "USDT",
    "price": "118962.74",
    "price24hAgo": "118780.42",
    "high24h": "120327.96",
    "low24h": "118217.28",
    "volume24h": "32.89729",
    "quoteVolume24h": "3924438.7146048",
    "markPrice": "0",
    "indexPrice": "118963.080293502",
    "fundingRate": "0",
    "nextFundingRate": "0",
    "nextFundingTime": 0,
    "productType": "spot",
    "openInterest": "0",
    "indexCurrency": "USDT",
    "usdVolume24h": "3924438.7146048",
    "openInterestUSD": "0"
  }
}
```

### Candles Messages
Channel: `"candles"`

```json
{
  "channel": "candles",
  "type": "update",
  "data": {
    "symbol": "BTC_USDT",
    "time": "1755076380000000",
    "duration": 60000000,
    "open": "120073.01",
    "high": "120073.01",
    "low": "120073.01",
    "close": "120073.01",
    "volume": "0",
    "quoteVolume": "0"
  }
}
```

- `time` is a string in microseconds
- `duration` is in microseconds (60000000 = 1 minute)

---

## Funding / OI (REST-only for perps)
Available via `/api/public/ticker?symbol={{symbol}}`:
- `fundingRate` — current funding rate
- `nextFundingRate` — next funding rate
- `nextFundingTime` — microseconds
- `openInterest` — in base asset
- `openInterestUSD` — in USD

---

## Rate Limits (from OpenAPI spec)

REST rate limits are tier-based (ARKM holdings + 30d volume):
- Default: 20 spot orders/s, 40 perp orders/s, 40 REST requests/s
- WS: 10 messages/s per user
- REST per IP: 5 requests/s (message limit), 150 requests/s (order limit)

---

## Config Notes

### Spot (`arkham.json`)
| Field | Value | Source |
|-------|-------|--------|
| Discriminator | `"channel"` | CCXT Pro ✅ |
| Trade handler key | `"trades"` | CCXT Pro ✅ |
| Trade fields | `data.symbol`, `data.price`, `data.size`, `data.time` (us), `data.takerSide` | CCXT Pro ✅ |
| Depth handler key | `"l2_updates"` | CCXT Pro ✅ |
| Depth fields | `data.bids`, `data.asks`, named `price`/`size` | CCXT Pro ✅ |
| Subscribe format | `{method: subscribe, args: {channel, params}}` | CCXT Pro ✅ |
| Ack channels | `confirmations`, `errors` | CCXT Pro ✅ |
| REST trades | `/api/public/trades` | Verified ✅ |
| REST timestamp | microseconds | Verified ✅ |
| REST field map | `size→quantity`, `takerSide→side`, `time→timestamp`, `revisionId→trade_id` | Verified ✅ |
| REST orderbook | `/api/public/book` | Verified ✅ |
| Products filter | exclude `_PERP$` | Correct |

### Perps (`arkham_futures.json`)
| Field | Value | Source |
|-------|-------|--------|
| Discriminator | `"channel"` | CCXT Pro ✅ |
| Trade handler key | `"trades"` | CCXT Pro ✅ |
| Trade fields | `data.symbol`, `data.price`, `data.size`, `data.time`, `data.takerSide` | CCXT Pro ✅ |
| Depth handler key | `"l2_updates"` | CCXT Pro ✅ |
| Depth fields | `data.bids`, `data.asks`, named `price`/`size` | CCXT Pro ✅ |
| REST trades | `/api/public/trades` | Same as spot |
| Funding rate | via `/api/public/ticker` → `fundingRate` | Verified ✅ |
| Open interest | via `/api/public/ticker` → `openInterestUSD` | Verified ✅ |
| Products filter | include `_PERP` | Correct |
| Normalization | `base_strip_suffix: ".P"` | Verified ✅ |

### Previous Issues (ALL RESOLVED)
1. ~~Spot used `type` discriminator~~ → Fixed to `channel` ✅
2. ~~Spot trade fields were flat~~ → Fixed to nested `data.*` ✅
3. ~~Spot timestamp_unit was `ms`~~ → Fixed to `us` ✅
4. ~~Depth used indexed format~~ → Fixed to named `price`/`size` ✅
5. ~~Depth handler key was `depth`/`book`~~ → Fixed to `l2_updates` ✅
6. ~~Subscribe format was wrong~~ → Fixed to CCXT-verified format ✅
