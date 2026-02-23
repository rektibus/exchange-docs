# Bit2Me Pro (Trading Spot) API Reference

> Source: https://gateway.bit2me.com OpenAPI spec (OAS 3.1.0)
> Base URL: `https://gateway.bit2me.com`
> WS URL: `wss://ws.bit2me.com/v1/trading`
> Market type: **Spot only** (no futures/perps/inverse)

## Authentication

- Header: `X-API-KEY: <key>`, `x-nonce: <unix_timestamp_utc>`, `api-signature: <sig>`
- Signature: HMAC-SHA512 of SHA256(`{nonce}:{path}:{body}`)
- Nonce valid window: 5 seconds
- **Market data endpoints do NOT require auth**
- **Trading/funding endpoints require auth**

## Rate Limits

| Tier | Max RPM |
|------|---------|
| Starter | 600 |
| Medium | 800 |
| Pro | 1000 |

**Per-endpoint limits (by user account):**

| Endpoint | Description | Max RPS |
|----------|-------------|---------|
| `POST /v1/trading/order` | Create order | 15/sec |
| `DELETE /v1/trading/order/{id}` | Cancel order | 15/sec |
| `DELETE /v1/trading/order` | Cancel many | 1/sec |
| `GET /v1/trading/order` | List orders | 5/sec |
| `GET /v1/trading/trade` | **Get trades (AUTH REQUIRED)** | 5/sec |
| `GET /v1/trading/wallet/balance` | Balance | 5/sec |

**Per-IP limits:**

| Endpoint | Description | Max RPS |
|----------|-------------|---------|
| `GET /v1/trading/candle` | OHLCV data | 5/sec |

**WS limits:**
- Max 50 concurrent connections per IP
- Max 50 messages/sec per connection (close code 4001 if exceeded)
- Subscribe/Unsubscribe: 50 msg/sec
- Authenticate: 1 msg/sec

## Products / Market Config

**Endpoint:** `GET /v1/trading/market-config` (PUBLIC, no auth)

**Response:** Bare JSON array (no wrapper)

```json
[
  {
    "id": "5daf7851-c883-4e34-ad1a-52a8bb7651e3",
    "symbol": "BTC/EUR",
    "feeMakerPercentage": 0,
    "feeTakerPercentage": 0,
    "minAmount": 0.00005,
    "maxAmount": 20,
    "minPrice": 1000,
    "maxPrice": 200000,
    "minOrderSize": 3,
    "tickSize": 0.1,
    "pricePrecision": 1,
    "amountPrecision": 8,
    "initialPrice": 0,
    "marketEnabled": "enabled",
    "marketEnabledAt": null
  }
]
```

**Symbol format:** `BASE/QUOTE` (slash-separated, uppercase)
- Examples: `BTC/EUR`, `ETH/USDC`, `SOL/EUR`, `B2M/EUR`
- Base = left of `/`, Quote = right of `/`
- **No contract size / multiplier** — spot only, all amounts are in base currency units

**Quote currencies observed:** EUR, EURCV, EUROD, EUROP, EURR, USDC, USDCV, USDR, USDQ, EURQ

**Key fields for config:**
- `symbol` → wire symbol (used as-is for WS subscribe)
- `minAmount` / `maxAmount` → order size bounds (in base currency)
- `minOrderSize` → minimum order value (in quote currency)
- `tickSize` → price increment
- `pricePrecision` → decimal places for price
- `amountPrecision` → decimal places for amount
- `marketEnabled` → `"enabled"` or `"enabled_at"` (with `marketEnabledAt` timestamp)

**products_fields mapping:**
```json
{
  "symbol": "symbol",
  "base": "symbol|/|0",
  "quote": "symbol|/|1"
}
```

## REST Trade History

**Endpoint:** `GET /v1/trading/trade`
- **⚠️ REQUIRES AUTHENTICATION** (private endpoint, 5/sec rate limit)
- **NOT usable for public trade recovery**
- No public trade history endpoint exists

**Candle endpoint (public):** `GET /v1/trading/candle` — OHLCV data, 5/sec per IP

## WebSocket API

**URL:** `wss://ws.bit2me.com/v1/trading`

### Public Channels (no auth required)

The WS provides public channels for real-time market data:
- **trades** — real-time trade stream
- **orderbook** — order book updates

### Authentication (for private channels)

```json
{"type": "authenticate", "payload": {"apikey": "<key>"}}
```
Or with JWT:
```json
{"type": "authenticate", "payload": {"token": "<jwt>"}}
```

Close codes:
- `4000` — authentication failed
- `4001` — rate limit exceeded

### Subscribe / Unsubscribe

```json
{"event": "subscribe", "channel": "trades", "symbols": ["BTC/EUR"]}
{"event": "unsubscribe", "channel": "trades", "symbols": ["BTC/EUR"]}
```

### Trade Messages

Discriminator field: `event`
Handler value: `trade`

```json
{
  "event": "trade",
  "data": {
    "symbol": "BTC/EUR",
    "price": "95432.10",
    "amount": "0.00150000",
    "side": "buy",
    "timestamp": 1708185600000
  }
}
```

**Field mapping:**
| Field | Path | Type |
|-------|------|------|
| symbol | `data.symbol` → via `array_key: "data"` then `symbol` | string |
| price | `price` (within data) | string number |
| quantity | `amount` (within data) | string number |
| timestamp | `timestamp` (within data) | milliseconds |
| side | `side` (within data) | `"buy"` / `"sell"` |

### Depth (Orderbook) Messages

Discriminator value: `depth`

```json
{
  "event": "depth",
  "data": {
    "symbol": "BTC/EUR",
    "bids": [[95430.0, 0.5], [95429.0, 1.2]],
    "asks": [[95432.0, 0.3], [95433.0, 0.8]],
    "timestamp": 1708185600000
  }
}
```

**Level format:** indexed arrays `[price, size]`
- `price_index: 0`, `size_index: 1`

**Subscribe:**
```json
{"event": "subscribe", "channel": "orderbook", "symbols": ["BTC/EUR"]}
```

## Order Types

- **market** — executes at best available price, immediate, price not guaranteed
- **limit** — buy/sell at fixed price, executes when market reaches price
- **stop-limit** — two prices: stop price triggers → becomes limit order
- Orders expire after **30 days** (auto-cancelled, including partially filled)
- Cancelled market maker orders stored for **7 days** then deleted

**Order limits per user tier:**

| Tier | Max Open Orders/symbol | Max Created+Cancelled/hour/symbol |
|------|----------------------|----------------------------------|
| Standard | 20 | 1000 |
| Advanced (MM/HFT) | 100 | up to 10000 |

## Additional Market Data Endpoints (Public)

| Endpoint | Description |
|----------|-------------|
| `GET /v1/currency/rate` | All exchange rates in USD |
| `GET /v3/currency/ticker/{symbol}` | Crypto data with intervals |
| `GET /v3/currency/market-data/{symbol}` | Market cap, volume, supply |
| `GET /v1/currency/prices` | Crypto prices by interval |
| `GET /v3/currency/chart?ticker=BTC/EUR` | Historical price chart |
| `GET /v2/currency/assets` | All assets with metadata |
| `GET /v1/currency/ohlca/{symbol}` | OHLCA by timeframe (1H-1Y) |

## Key Limitations

1. **No public REST trade history** — `GET /v1/trading/trade` requires authentication
2. **Spot only** — no futures, perps, inverse, or funding rates
3. **No contract size** — all spot, amounts in base currency
4. **No liquidation feed** — spot exchange
5. **No open interest** — spot exchange
6. **No funding rate** — spot exchange
7. **Not in CCXT** — no CCXT integration available
8. **EUR-centric** — primary quote currency is EUR (also supports USDC and stablecoins)