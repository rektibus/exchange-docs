# BingX API Documentation

> All timestamps in **milliseconds**. All WS connections use **gzip compression**. String numbers common.

## Connection & Heartbeat

| Variant | WS URL | Ping/Pong | Interval |
|---------|--------|-----------|----------|
| **Spot** | `wss://open-api-ws.bingx.com/market` | Server sends `Ping` text → client responds `Pong` text | ~5s |
| **Futures** | `wss://open-api-swap.bingx.com/swap-market` | Server sends `Ping` text → client responds `Pong` text | ~5s |
| **Inverse** | `wss://open-api-cswap-ws.bingx.com/market` | Native ping/pong frames + `{"ping":"..."}` ACK | ~5s |

- Max streams per connection: **200**
- Subscription delay: **100ms** between subscribes
- ACK on subscribe: `{"code": "0"}`

## Rate Limits

| Type | Limit |
|------|-------|
| REST (general) | 100ms between requests (config: `rate_limit_ms: 100`) |
| Spot trades | `limit` param max: **100** |
| Futures historicalTrades | `limit` param max: **1000** (requires auth: `timestamp` signed) |
| Inverse historicalTrades | **NOT AVAILABLE** (returns 404) |

---

## BINGX (Spot)

Base URL: `https://open-api.bingx.com`

### Products — `GET /openApi/spot/v1/common/symbols`

Response: `{"code":0, "data":{"symbols":[...]}}`

```json
{
  "symbol": "BTC-USDT",
  "tickSize": "0.01",
  "stepSize": "0.000001",
  "status": 1
}
```

- `symbol`: Dash-separated (e.g. `POWR-USDT`). **No separate `base`/`quote` fields** — split on `-`
- `status`: `1` = active
- `tickSize`: Price precision step
- `stepSize`: Quantity precision step

### REST Trades — `GET /openApi/spot/v1/market/trades`

Params: `symbol` (required), `limit` (max **100**, default 100). **Public, no auth.**

```json
{"code":0, "data":[
  {"id":196334872, "price":67786.29, "qty":0.031968, "time":1771328339312, "buyerMaker":true}
]}
```

| Field | Type | Description |
|-------|------|-------------|
| `id` | int | Trade ID |
| `price` | number | Trade price |
| `qty` | number | Quantity |
| `time` | int | Timestamp (ms) |
| `buyerMaker` | bool | `true`=sell, `false`=buy |

### REST Depth — `GET /openApi/spot/v2/market/depth`

Params: `symbol` (required), `limit` (5/10/20/50/100), `type` (required: `step0`=no merge, `step1`..`step5`=merge levels).

```json
{"code":0, "data":{
  "bids": [["67791.35","0.005666"], ...],
  "asks": [["67791.37","0.005366"], ...],
  "ts": 1771328510017
}}
```

Levels: `[price_string, qty_string]` indexed format.

### WS Trade

Subscribe: `{"id":"{{id}}","reqType":"sub","dataType":"{{symbol}}@trade"}`

Discriminator: `dataType` value contains `@trade`.

```json
{"dataType":"BTC-USDT@trade", "data":[
  {"s":"BTC-USDT", "p":"67800", "q":"0.001", "T":1234567890123, "m":true}
]}
```

| Field | Type | Description |
|-------|------|-------------|
| `s` | string | Symbol |
| `p` | string | Price |
| `q` | string | Quantity |
| `T` | int | Timestamp (ms) |
| `m` | bool | buyerMaker: `true`=sell |

### WS Depth

Subscribe: `{"id":"{{id}}","reqType":"sub","dataType":"{{symbol}}@depth20@100ms"}`

Indexed levels: `[price, qty]`. Fields: `bids`, `asks`.

---

## BINGX_FUTURES (Perp / USDT-M Swap)

Base URL: `https://open-api.bingx.com`

### Products — `GET /openApi/swap/v2/quote/contracts`

Response: `{"code":0, "data":[...]}`

```json
{
  "contractId": "100",
  "symbol": "BTC-USDT",
  "size": "0.0001",
  "quantityPrecision": 4,
  "pricePrecision": 1,
  "feeRate": 0.0005,
  "makerFeeRate": 0.0002,
  "takerFeeRate": 0.0005,
  "currency": "USDT",
  "asset": "BTC",
  "status": 1,
  "displayName": "BTC-USDT"
}
```

| Field | Description |
|-------|-------------|
| `asset` | Base currency (e.g. `BTC`) |
| `currency` | Quote currency (e.g. `USDT`) |
| `size` | Contract size (e.g. `0.0001` BTC) |
| `quantityPrecision` | Decimal places for quantity |
| `pricePrecision` | Decimal places for price |
| `status` | `1` = active |

### REST Historical Trades — `GET /openApi/swap/v1/market/historicalTrades`

**Requires auth** (signed `timestamp` param). Params: `symbol`, `limit` (max **1000**).

**No public recent trades endpoint** (`/openApi/swap/v2/quote/recentTrades` returns 404).

Fields: `fillId` (trade ID — NOT `id` like spot), `price`, `qty`, `time` (ms), `buyerMaker` (bool).

### REST Depth — `GET /openApi/swap/v2/quote/depth`

Params: `symbol` (required), `limit` (5/10/20/50/100/500/1000).

```json
{"code":0, "data":{
  "T": 1771328498069,
  "bids": [["67750.5","0.0147"], ...],
  "asks": [["67751.5","0.0034"], ...],
  "bidsCoin": [["67750.5","0.0147"], ...],
  "asksCoin": [["67751.5","0.0034"], ...]
}}
```

Indexed levels: `[price_string, qty_string]`. `T` = timestamp (ms).

### Funding Rate — `GET /openApi/swap/v2/quote/premiumIndex`

Params: `symbol={{symbol}}`. **Public, no auth.**

```json
{"code":0, "data":{
  "symbol": "BTC-USDT",
  "markPrice": "67754.1",
  "indexPrice": "67780.8",
  "lastFundingRate": "0.00004580",
  "nextFundingTime": 1771344000000
}}
```

| Field | Type | Description |
|-------|------|-------------|
| `lastFundingRate` | string | Current funding rate |
| `nextFundingTime` | int | Next funding settlement (ms) |
| `markPrice` | string | Mark price |
| `indexPrice` | string | Index price |

Config: `rest_value: "data.lastFundingRate"`, `rest_timestamp: "data.nextFundingTime"`

### Open Interest — `GET /openApi/swap/v2/quote/openInterest`

Params: `symbol={{symbol}}`. **Public, no auth.**

```json
{"code":0, "data":{
  "openInterest": "1209228397.9",
  "symbol": "BTC-USDT",
  "time": 1771328499199
}}
```

Config: `rest_value: "data.openInterest"`, `rest_timestamp: "data.time"`

### WS Trade

Subscribe: `{"id":"1","reqType":"sub","dataType":"{{symbol}}@trade"}`

Array in `data`. Fields: `s` (symbol), `p` (price), `q` (qty), `T` (timestamp ms), `m` (buyerMaker).

### WS Depth

Subscribe: `{"id":"3","reqType":"sub","dataType":"{{symbol}}@depth20@100ms"}`

Array indexed levels: `[price_string, qty_string]`. Fields: `bids`, `asks`, `T` (timestamp ms), `s` (symbol).

### WS Liquidation (forceOrder)

Subscribe: `{"id":"2","reqType":"sub","dataType":"{{symbol}}@forceOrder"}`

Fields: `s` (symbol), `p` (price), `q` (quantity), `T` (timestamp ms), `S` (side: `Buy`/`Sell`).

> **Note**: Side field is `S` (uppercase), not `s` (which is symbol).

### Historical Funding Rate — `GET /openApi/swap/v2/quote/fundingRate`

Params: `symbol`, `startTime` (ms), `limit`. **Public, no auth.**

```json
{"code":0, "data":[
  {"symbol": "BTC-USDT", "fundingRate": "0.0001", "fundingTime": 1585684800000}
]}
```

Supports pagination via `startTime`. CCXT paginates in 8h increments.

### WS Funding / WS Open Interest

No WS streams for funding or OI. Both are **REST-only** with polling at 20s interval.

---

## CCXT Cross-Reference Analysis

| Data Type | Spot | Futures | Inverse | Source |
|-----------|------|---------|---------|--------|
| **Trades** | ✅ REST public | ✅ REST (auth) | ❌ REST 404 | CCXT `fetchTrades` |
| **Depth** | ✅ REST + WS | ✅ REST + WS | ✅ WS only | Verified |
| **Funding Rate** | N/A | ✅ REST poll | ✅ REST poll | CCXT `fetchFundingRate` |
| **Historical Funding** | N/A | ✅ `/quote/fundingRate` | ❓ Not verified | CCXT `fetchFundingRateHistory: True` |
| **Open Interest** | N/A | ✅ REST poll | ✅ REST poll | CCXT `fetchOpenInterest: True` |
| **Historical OI** | N/A | ❌ | ❌ | Not in CCXT |
| **Liquidations (public)** | N/A | ✅ WS `@forceOrder` | ❌ | CCXT `fetchLiquidations: False` |
| **Liquidations (private)** | N/A | ✅ | ✅ | CCXT `fetchMyLiquidations: True` |
| **LS Ratio** | N/A | ❌ | ❌ | Not in CCXT |

## BINGX_INVERSE (Coin-Margined / CSwap)

Base URL: `https://open-api.bingx.com`

### Products — `GET /openApi/cswap/v1/market/contracts`

**Requires `timestamp` query param.** Response: `{"code":0, "data":[...]}`

Also requires `User-Agent` header (config: `products_headers`).

```json
{
  "symbol": "BTC-USD",
  "pricePrecision": 1,
  "minTickSize": "100",
  "minTradeValue": "100",
  "minQty": "1.00000000",
  "status": 1,
  "displayName": "BTC-USD"
}
```

- **No `base`/`quote` fields** — base derived from symbol, quote always USD
- `pricePrecision`: Decimal places for price
- `minTickSize`: Minimum tick value (USD)
- `status`: `1` = active
- ~23 contracts available (BTC, ETH, SOL, DOGE, XRP, etc.)

### REST Trades — NOT AVAILABLE

`/openApi/cswap/v1/market/historicalTrades` returns `"this api is not exist"`. **`history_supported: false`**.

### Funding Rate — `GET /openApi/cswap/v1/market/premiumIndex`

Params: `symbol={{symbol}}&timestamp={{timestamp}}`. Response wraps in **array**.

```json
{"code":0, "data":[{
  "symbol": "BTC-USD",
  "lastFundingRate": "0.000056",
  "markPrice": "67725.6",
  "indexPrice": "67750.9",
  "nextFundingTime": 1771344000000
}]}
```

Config: `rest_value: "data.0.lastFundingRate"`, `rest_timestamp: "data.0.nextFundingTime"` (array index 0).

### Open Interest — `GET /openApi/cswap/v1/market/openInterest`

Params: `symbol={{symbol}}&timestamp={{timestamp}}`. Response wraps in **array**.

```json
{"code":0, "data":[{
  "symbol": "BTC-USD",
  "openInterest": "804.3204",
  "timestamp": 1771286400000
}]}
```

Config: `rest_value: "data.0.openInterest"`, `rest_timestamp: "data.0.timestamp"` (array index 0).

Polling interval: **20,000ms** (20s).

### WS Trade

Subscribe: `{"id":"1","reqType":"sub","dataType":"{{symbol}}@trade"}`

Array in `data`. Fields: `symbol` (full name, not `s`!), `price`, `q`, `T`, `isBuyerMaker` (not `m`!).

Note: Inverse WS uses **full field names** (`symbol`, `price`, `isBuyerMaker`) unlike futures which uses shorthand (`s`, `p`, `m`).

---

## Side Mapping (All Variants)

| Wire Value | Canonical |
|------------|-----------|
| `true` (buyerMaker/isBuyerMaker) | `sell` |
| `false` | `buy` |
| `"buy"` / `"Buy"` / `"BUY"` | `buy` |
| `"sell"` / `"Sell"` / `"SELL"` | `sell` |

Config: `side_is_maker: true` + `side_map` covers all variants.

## Key Differences Between Variants

| Feature | Spot | Futures | Inverse |
|---------|------|---------|---------|
| WS URL | `open-api-ws.bingx.com/market` | `open-api-swap.bingx.com/swap-market` | `open-api-cswap-ws.bingx.com/market` |
| Products path | `data.symbols` | `data` (bare array) | `data` (bare array) |
| Base/Quote fields | None (split from `symbol`) | `asset` / `currency` | None (split from `symbol`) |
| REST trades | ✅ public, limit 100 | ✅ auth required, limit 1000 | ❌ not available |
| Funding/OI response | N/A | `data.field` (object) | `data.0.field` (array) |
| WS trade fields | `s/p/q/T/m` | `s/p/q/T/m` | `symbol/price/q/T/isBuyerMaker` |
| Ping type | `text` | `text` | `native` |
| Compression | gzip | gzip | gzip |
