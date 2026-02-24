# Zonda (ZondaCrypto) API Documentation

Official Docs: https://docs.zondacrypto.exchange/
Base URL: `https://api.zondacrypto.exchange`
WebSocket: `wss://api.zondacrypto.exchange/websocket`

## Public REST Endpoints

### GET /rest/trading/ticker
All markets overview (178 markets). Returns market config and current stats.

```json
{
  "status": "Ok",
  "items": {
    "BTC-PLN": {
      "market": {
        "code": "BTC-PLN",
        "first": {"currency": "BTC", "minOffer": "0.00001800", "scale": 8},
        "second": {"currency": "PLN", "minOffer": "5", "scale": 2},
        "amountPrecision": 8,
        "pricePrecision": 2,
        "ratePrecision": 2
      },
      "time": "1771962920836",
      "highestBid": "235000.03",
      "lowestAsk": "239800.02",
      "rate": "239999.95",
      "previousRate": "241205.98"
    }
  }
}
```

### GET /rest/trading/ticker/{market}
Single market ticker (e.g. `BTC-PLN`).

### GET /rest/trading/stats/{market}
Market statistics (24h high/low, volume, etc).

### GET /rest/trading/transactions/{market}
Recent trades. Default 10, configurable via `?limit=N`.

**Parameters**: `limit` (query, optional) — number of transactions

```json
{
  "status": "Ok",
  "items": [
    {
      "id": "2af86665-11b9-11f1-81a9-4ea2d0fa018b",
      "t": "1771962241274",
      "a": "0.00034525",
      "r": "239999.95",
      "ty": "Buy"
    }
  ]
}
```

| Field | Description |
|-------|-------------|
| `id` | Transaction UUID |
| `t` | Timestamp (milliseconds) |
| `a` | Amount (quantity in base currency) |
| `r` | Rate (price) |
| `ty` | Direction: `Buy` or `Sell` |

### GET /rest/trading/orderbook/{market}
Full orderbook — 300 highest bids + 300 lowest asks.

```json
{
  "status": "Ok",
  "sell": [
    {"ra": "239800.02", "ca": "0.00045321", "sa": "0.00045321", "pa": "0.00045321", "co": 1}
  ],
  "buy": [
    {"ra": "235000.03", "ca": "0.00031987", "sa": "0.00031987", "pa": "0.00031987", "co": 1}
  ],
  "timestamp": "1771963041706",
  "seqNo": "3163698081"
}
```

| Field | Description |
|-------|-------------|
| `ra` | Rate (price) |
| `ca` | Current amount at this level |
| `sa` | Starting amount |
| `pa` | Previous amount |
| `co` | Count of orders at this level |

### GET /rest/trading/orderbook-limited/{market}/{limit}
Limited depth orderbook (e.g. `/BTC-PLN/10`).

### GET /rest/trading/candle/history/{market}/{resolution}
Candlestick/OHLCV data.
Resolutions: `60` (1m), `300` (5m), `900` (15m), `1800` (30m), `3600` (1h), `14400` (4h), `86400` (1d)

---

## Private REST Endpoints (Authenticated)

Authentication: API key + HMAC-SHA512 signature
Headers: `API-Key`, `API-Hash`, `operation-id`, `Request-Timestamp`

### POST /rest/trading/offer/{market}
Place a new order.

### DELETE /rest/trading/offer/{market}/{offerId}/{offerType}/{price}
Cancel an order.

### GET /rest/trading/history/transactions
Get trade history for account.

### GET /rest/trading/offer
Get active orders.

### GET /rest/trading/stop/offer
Get active stop orders.

### POST /rest/trading/stop/offer/{market}
Place a stop order.

### DELETE /rest/trading/stop/offer/{market}/{offerId}
Cancel a stop order.

### GET /rest/balances/BITBAY/balance
Get account balances.

### POST /rest/balances/BITBAY/balance/{currency}/transfer/{wallet}
Transfer between wallets.

### GET /rest/payments/deposit/crypto/addresses
Get deposit addresses.

### POST /rest/payments/withdrawal/crypto
Request crypto withdrawal.

### GET /rest/payments/history
Get payment/transfer history.

---

## Public WebSocket

### Connection
Connect to `wss://api.zondacrypto.exchange/websocket`

### Subscribe
```json
{"action": "subscribe-public", "module": "trading", "path": "transactions/btc-pln"}
```

### Channels

#### Ticker (`ticker/{market}`)
Real-time price/config updates.

#### Last Transactions (`transactions/{market}`)
Real-time trade stream. Same format as REST but pushed in real-time.

```json
{
  "action": "push",
  "topic": "trading/transactions/btc-pln",
  "message": {
    "transactions": [
      {"id": "uuid", "t": "1771962241274", "a": "0.00034525", "r": "239999.95", "ty": "Buy"}
    ]
  }
}
```

#### Orderbook (`orderbook/{market}`)
Full orderbook snapshots pushed on change.

#### Orderbook Limited (`orderbook-limited/{market}/{limit}`)
Depth-limited orderbook.

#### Market Statistics (`stats/{market}`)
Aggregated 24h market stats.

---

## Private WebSocket (Authenticated)

### Connection
Same URL. Authenticate after connecting.

```json
{"action": "subscribe-private", "module": "trading", "path": "offer", "hashKey": "<API-Key>", "hash": "<HMAC-SHA512>", "requestTimestamp": 1234567890}
```

### Private Channels

#### Active Offers (`offer`)
Real-time updates on user's active orders.

#### Transactions (`transactions`)
Real-time notifications of user's completed trades.

#### Balances (`balances`)
Real-time balance updates.

---

## Symbol Format
Markets use dash separator: `BTC-PLN`, `ETH-PLN`, `BTC-EUR`, `ETH-EUR`
Lowercase in WebSocket paths: `btc-pln`

## Rate Limits
- Public: 180 requests per minute
- Private: 60 requests per minute
- WebSocket: no explicit rate limit documented