# MEXC WebSocket API Documentation

> Source: Official MEXC API documentation, February 2026

## Connection

- **Base endpoint**: `wss://wbs-api.mexc.com/ws`
- Max connection lifetime: 24 hours
- All symbol names must be **UPPERCASE**
- If no valid subscription within 30s → server disconnects
- If subscription OK but no data flow within 60s → server disconnects
- Client can send PING to keep alive
- Max **30 subscriptions** per connection

## PING/PONG

**Request:**
```json
{"method": "PING"}
```

**Response:**
```json
{"id": 0, "code": 0, "msg": "PONG"}
```

## Subscribe / Unsubscribe

**Subscribe:**
```json
{"method": "SUBSCRIPTION", "params": ["spot@public.aggre.deals.v3.api.pb@100ms@BTCUSDT"]}
```

**Unsubscribe:**
```json
{"method": "UNSUBSCRIPTION", "params": ["spot@public.aggre.deals.v3.api.pb@100ms@BTCUSDT"]}
```

**Success response:** `msg` matches the subscribed channel name.

## Protocol Buffers

All data is pushed in **protobuf** format. Proto definitions: https://github.com/mexcdevelop/websocket-proto

Wrapper message: `PushDataV3ApiWrapper` with fields:
- `channel` (string, field 1)
- `symbol` (string, field 3)
- `sendTime` (int64, field 6)
- `oneof body` with field numbers for each channel type

## Channels

### Trade Streams (Aggregated)

**Channel**: `spot@public.aggre.deals.v3.api.pb@(100ms|10ms)@<SYMBOL>`

**Proto field**: 314 (`PublicAggreDealsV3Api`)

| Parameter | Type | Description |
|-----------|------|-------------|
| dealsList | array | Trade list |
| price | string | Trade price |
| quantity | string | Trade quantity |
| tradetype | int | 1=Buy, 2=Sell |
| time | long | Trade time (ms) |

### Diff Depth Stream (Aggregated)

**Channel**: `spot@public.aggre.depth.v3.api.pb@(100ms|10ms)@<SYMBOL>`

**Proto field**: 313 (`PublicAggreDepthsV3Api`)

| Parameter | Type | Description |
|-----------|------|-------------|
| asksList | array | Sell orders |
| bidsList | array | Buy orders |
| price | string | Price level |
| quantity | string | Quantity (0 = remove) |
| fromVersion | string | From version |
| toVersion | string | To version |

### Partial Book Depth

**Channel**: `spot@public.limit.depth.v3.api.pb@<SYMBOL>@<level>` (level: 5, 10, 20)

**Proto field**: 303 (`PublicLimitDepthsV3Api`)

### Individual Symbol Book Ticker

**Channel**: `spot@public.aggre.bookTicker.v3.api.pb@(100ms|10ms)@<SYMBOL>`

**Proto field**: 315 (`PublicAggreBookTickerV3Api`)

### K-line Streams

**Channel**: `spot@public.kline.v3.api.pb@<SYMBOL>@<interval>`

Intervals: Min1, Min5, Min15, Min30, Min60, Hour4, Hour8, Day1, Week1, Month1

**Proto field**: 308 (`PublicSpotKlineV3Api`)

## Order Book Maintenance

1. Subscribe to `spot@public.aggre.depth.v3.api.pb@(100ms|10ms)@{symbol}`
2. Cache incremental updates, record `fromVersion` of first update
3. Fetch snapshot: `GET https://api.mexc.com/api/v3/depth?symbol={symbol}&limit=5000`, record `lastUpdateId`
4. If `lastUpdateId < fromVersion` of first cached update → re-fetch snapshot
5. Discard cached updates where `toVersion <= lastUpdateId`
6. If first remaining update's `fromVersion > lastUpdateId + 1` → data discontinuous, re-fetch
7. Apply remaining updates sequentially; after each, set local version = `toVersion`
8. Each update must satisfy: `fromVersion == previous toVersion + 1`, otherwise reinitialize

---

## REST API V3

### General Info

- **Base endpoint**: `https://api.mexc.com`
- HTTP 4XX = client error, 429 = rate limit, 5XX = server error
- Accepts GET, POST, DELETE
- For GET: params as query string
- For POST/DELETE: params as query string or JSON body

### Authentication (SIGNED)

**Header:**

| Key | Description |
|-----|-------------|
| X-MEXC-APIKEY | Access key |
| Content-Type | application/json |

**Signature**: HMAC SHA256 of `totalParams` (query string + request body) using `secretKey`

**Timing**: `timestamp` param required (ms). `recvWindow` optional (default 5000, max 60000).

```
if (timestamp < serverTime + 1000 && serverTime - timestamp <= recvWindow)
  // process
else
  // reject
```

### Rate Limits

- IP-based: 500 requests per 10 seconds per endpoint
- UID-based: 500 requests per 10 seconds per endpoint
- WebSocket: 100 messages/second, max 30 streams per connection
- 429 → back off. Repeated violations → IP ban (2min to 3 days)

### Error Codes

| Code | Description |
|------|-------------|
| -2011 | Unknown order sent |
| 400 | API key required |
| 401 | No authority |
| 403 | Access denied |
| 429 | Too many requests |
| 500 | Internal error |
| 602 | Signature verification failed |
| 10007 | Bad symbol |
| 10072 | Invalid access key |
| 10073 | Invalid Request-Time |
| 10101 | Insufficient balance |
| 30000 | Suspended transaction for symbol |
| 30001 | Direction not allowed |
| 30004 | Insufficient position |
| 30014 | Invalid symbol |
| 30016 | Trading disabled |
| 30019 | API market order disabled |
| 30020 | No permission for symbol |
| 30021 | Invalid symbol |
| 700001 | API-key format invalid |
| 700002 | Signature not valid |
| 700003 | Timestamp outside recvWindow |
| 700006 | IP not in whitelist |
| 700007 | No permission for endpoint |

---

## REST API V3 — Market Data Endpoints

### Historical Market Data

Download kline and trading data for all Spot pairs since 01-01-2023: [Historical Market Data](https://www.mexc.com/support/articles/17827791514841)

### Test Connectivity

`GET /api/v3/ping` — Weight: 1

### Check Server Time

`GET /api/v3/time` — Weight: 1

### Exchange Information

`GET /api/v3/exchangeInfo` — Weight: 10

| Parameter | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| symbol | string | NO | Single symbol |
| symbols | string | NO | Comma-separated symbols |

Key response fields: `symbol`, `status` (1=online, 2=paused, 3=offline), `baseAsset`, `quoteAsset`, `baseAssetPrecision`, `quotePrecision`, `orderTypes`, `baseSizePrecision` (min qty), `quoteAmountPrecision` (min amount), `maxQuoteAmount`, `makerCommission`, `takerCommission`.

### Order Book

`GET /api/v3/depth` — Weight: 1

| Parameter | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| symbol | string | YES | |
| limit | integer | NO | Default 100, max 5000 |

### Recent Trades

`GET /api/v3/trades` — Weight: 5

| Parameter | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| symbol | string | YES | |
| limit | integer | NO | Default 500, max 1000 |

Response: `id`, `price`, `qty`, `quoteQty`, `time`, `isBuyerMaker`, `isBestMatch`

### Compressed/Aggregate Trades

`GET /api/v3/aggTrades` — Weight: 1

| Parameter | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| symbol | string | YES | |
| startTime | long | NO | Must use with endTime |
| endTime | long | NO | Must use with startTime |
| limit | integer | NO | Default 500, max 1000 |

Response: `a` (aggTradeId), `f` (firstTradeId), `l` (lastTradeId), `p` (price), `q` (qty), `T` (timestamp), `m` (isBuyerMaker)

### Kline/Candlestick Data

`GET /api/v3/klines` — Weight: 1

| Parameter | Type | Mandatory | Description |
|-----------|------|-----------|-------------|
| symbol | string | YES | |
| interval | ENUM | YES | 1m,5m,15m,30m,60m,4h,8h,1d,1W,1M |
| startTime | long | NO | |
| endTime | long | NO | |
| limit | integer | NO | Default 500, max 500 |

Response array: [openTime, open, high, low, close, volume, closeTime, quoteAssetVolume]

### 24hr Ticker

`GET /api/v3/ticker/24hr` — Weight: 1 (single), 40 (all)

### Symbol Price Ticker

`GET /api/v3/ticker/price` — Weight: 1 (single), 2 (all)

### Symbol Order Book Ticker

`GET /api/v3/ticker/bookTicker` — Weight: 1

Response: `symbol`, `bidPrice`, `bidQty`, `askPrice`, `askQty`

### Query Offline Symbols

`GET /api/v3/symbol/offline` — Weight: 10

Response: `symbol`, `state` (2=suspended, 3=delisted), `offlineTime`
