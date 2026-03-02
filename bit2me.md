# Bit2Me Pro (Trading Spot) API Reference

> Source: Official OpenAPI spec at `https://api.bit2me.com/openapi/trading-spot-websockets.json`
> and GitHub samples at `https://github.com/bit2me-devs/trading-spot-samples`
> Verified: 2026-03-01

## Base URLs

| Type | URL |
|------|-----|
| REST API | `https://gateway.bit2me.com` |
| WebSocket | `wss://ws.bit2me.com/v1/trading` |

## Authentication

- REST market data endpoints: **No auth required**
- REST trading endpoints: API Key (`X-API-KEY`), nonce (`x-nonce`), HMAC-SHA512 signature (`api-signature`)
- WS public channels: **No auth required**
- WS private channels: Requires token from `POST /v1/signin/apikey`, then `{"event":"authenticate","token":"<token>"}`

## Rate Limits

### REST (per IP)

| Tier | Max RPM |
|------|---------|
| Starter | 600 |
| Medium | 800 |
| Pro | 1000 |

**Per-endpoint limits (per user account):**

| Endpoint | Limit |
|----------|-------|
| GET /v1/trading/candle | 5/sec |
| GET /v1/trading/order | 5/sec |
| GET /v1/trading/trade | 5/sec |
| POST /v1/trading/order | 15/sec |
| DELETE /v1/trading/order/{id} | 15/sec |
| DELETE /v1/trading/order (batch) | 1/sec |

Exceeding limits → HTTP 429. Repeated abuse → HTTP 418 (IP ban).

### WebSocket

| Rule | Value |
|------|-------|
| Max concurrent connections per IP | 50 |
| Max messages per second per connection | 50 |
| Subscribe/Unsubscribe rate | 50 msg/sec |
| Authenticate rate | 1 msg/sec |

Connection closed with code 4001 if message rate exceeded.
Connection rejected with 429 handshake error if max concurrent connections exceeded.

---

## REST Endpoints

### Products — GET /v1/trading/market-config

Returns all trading pairs. **No auth required.**

```
GET https://gateway.bit2me.com/v1/trading/market-config
```

Response (array):
```json
[
  {
    "id": "f50a7eac-01e7-42d3-b6d1-0eebf4cc6b10",
    "symbol": "1INCH/EUR",
    "feeMakerPercentage": 0,
    "feeTakerPercentage": 0,
    "minAmount": 20,
    "maxAmount": 60000,
    "minPrice": 0.01,
    "maxPrice": 100,
    "minOrderSize": 1,
    "tickSize": 0.001,
    "pricePrecision": 4,
    "amountPrecision": 8,
    "marketEnabled": "enabled"
  }
]
```

Symbol format: `BASE/QUOTE` (e.g. `BTC/EUR`, `ETH/USDC`)

### Last Trades — GET /v1/trading/trade/last

Returns last 50 trades for a symbol. **No auth required. No pagination.**

```
GET https://gateway.bit2me.com/v1/trading/trade/last?symbol=BTC/EUR
```

Response (array of arrays):
```json
[
  ["buy", 55997.1, 0.0008929, 1772393885969],
  ["sell", 55998.0, 0.00357155, 1772393868861]
]
```

Format: `[side, price, quantity, timestamp_ms]`

- Fixed 50 results per call
- `limit` parameter has no effect
- No cursor/offset pagination
- Newest trades first

### Order Book — GET /v2/trading/order-book

Returns L2 order book (100 levels each side). **No auth required.**

```
GET https://gateway.bit2me.com/v2/trading/order-book?symbol=BTC/EUR
```

Response:
```json
{
  "bids": [[55986.3, 0.82658669], [55984.7, 0.306722]],
  "asks": [[55988.1, 0.37373861], [55992.4, 0.04095684]],
  "timestamp": "2026-03-01T19:38:00.000Z",
  "datetime": "2026-03-01T19:38:00.000Z",
  "nonce": 1772393944405,
  "symbol": "BTC/EUR"
}
```

Level format: `[price, size]`

### Candles — GET /v1/trading/candle

```
GET https://gateway.bit2me.com/v1/trading/candle?symbol=BTC/EUR&timeframe=1h
```

Not tested. Requires auth per docs.

---

## WebSocket API

Endpoint: `wss://ws.bit2me.com/v1/trading`

### Public Channels (no auth)

#### Subscribe to Trades

Request:
```json
{"event":"subscribe","symbol":"BTC/EUR","subscription":{"name":"public-trades"}}
```

Ack:
```json
{"event":"subscribe","symbol":"BTC/EUR","subscription":{"name":"public-trades"},"result":"subscribed"}
```

Trade message:
```json
{
  "event": "public-trades",
  "symbol": "BTC/EUR",
  "data": {
    "side": "buy",
    "price": 55991.5,
    "amount": 0.00512643,
    "timestamp": 1772393913546
  }
}
```

| Field | Path | Type |
|-------|------|------|
| discriminator | `event` | `"public-trades"` |
| symbol | `symbol` | string `"BTC/EUR"` |
| price | `data.price` | float |
| quantity | `data.amount` | float |
| side | `data.side` | `"buy"` / `"sell"` |
| timestamp | `data.timestamp` | int (ms) |

#### Subscribe to Order Book (L2)

Request:
```json
{"event":"subscribe","symbol":"BTC/EUR","subscription":{"name":"order-book"}}
```

Ack:
```json
{"event":"subscribe","symbol":"BTC/EUR","subscription":{"name":"order-book"},"result":"subscribed"}
```

Depth message:
```json
{
  "event": "order-book",
  "symbol": "BTC/EUR",
  "data": {
    "symbol": "BTC/EUR",
    "bids": [[55988.0, 0.05913268], [55984.7, 0.306722]],
    "asks": [[55988.1, 0.37373861], [55992.4, 0.04095684]],
    "nonce": 1772277528283
  }
}
```

| Field | Path | Type |
|-------|------|------|
| discriminator | `event` | `"order-book"` |
| symbol | `symbol` | string `"BTC/EUR"` |
| bids | `data.bids` | array of `[price, size]` |
| asks | `data.asks` | array of `[price, size]` |
| nonce | `data.nonce` | int (ms, use as timestamp) |

100 levels per side.

#### Unsubscribe

```json
{"event":"unsubscribe","symbol":"BTC/EUR","subscription":{"name":"public-trades"}}
{"event":"unsubscribe","symbol":"BTC/EUR","subscription":{"name":"order-book"}}
```

### Private Channels (auth required)

- `my-trades` — executed trades for authenticated user
- `my-orders` — order status updates
- `executions` — combined my-trades + my-orders
- `my-balance` — balance changes

### Private Commands (auth required)

- `add-order` — place order
- `add-orders` — batch orders (max 20)
- `cancel-order` — cancel single order
- `cancel-orders` — batch cancel (max 20)
- `cancel-all-orders` — cancel all orders
- `auto-cancel-orders-on-disconnection` — kill switch

### Error Messages

```json
{"event":"authenticate","error":"jwt expired"}
{"error":"Forbidden"}
```

Error on malformed/unauthorized requests. `Forbidden` occurs when WS connection cannot be established (IP ban, etc.).

---

## EnsoX Config Notes

- **Symbol format**: `BTC/EUR` — no lowercase, separator `/`
- **WS discriminator**: `event` field — values: `public-trades`, `order-book`, `subscribe`
- **text_ack_patterns**: `"event":"subscribe"` catches all subscribe acks, `"error"` catches Forbidden/auth errors
- **REST trade recovery**: Limited to last 50 trades, no pagination — gap recovery is constrained
- **Depth**: Snapshot mode (full L2 each message, not delta updates)
- **No REST auth needed**: Products, trades, and orderbook are all public
