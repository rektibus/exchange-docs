# Zonda (ZondaCrypto) API Documentation

Official Docs: https://docs.zondacrypto.exchange/

## Public REST Endpoints

Base URL: `https://api.zondacrypto.exchange/rest`

| Endpoint | Description |
|----------|-------------|
| `GET /trading/ticker/{market}` | Ticker data |
| `GET /trading/stats/{market}` | Market statistics |
| `GET /trading/orderbook/{market}` | Full orderbook |
| `GET /trading/orderbook-limited/{market}/{limit}` | Limited orderbook |
| `GET /trading/transactions/{market}` | Last transactions (trades) |
| `GET /trading/candle/history/{market}/{resolution}` | Candlestick chart data |

### Last Transactions (Trades)

Shows the list of most recent transactions for a given market. Default: 10 most recent.

**Endpoint**: `GET /rest/trading/transactions/{market}`

**Parameters**:
- `market` (path): Trading pair, e.g. `BTC-PLN`
- `limit` (query, optional): Number of transactions to return

**Response**: Array of transaction objects with fields:
- `id` — Transaction ID
- `t` — Timestamp (ISO or epoch)
- `a` — Amount
- `r` — Rate (price)
- `ty` — Transaction type (Buy/Sell)

## Public WebSocket

Base URL: `wss://api.zondacrypto.exchange/websocket`

### Channels
- **Ticker** — Real-time ticker updates
- **Market statistics** — Aggregated market stats
- **Orderbook** — Full orderbook snapshots/deltas
- **Orderbook limited** — Depth-limited orderbook
- **Last transactions** — Real-time trade stream

### Subscription
Subscribe by sending JSON with `action: "subscribe-public"` and specifying the channel and market.

## Rate Limits
See https://docs.zondacrypto.exchange/reference/limits

## Symbol Format
Markets use dash separator: `BTC-PLN`, `ETH-PLN`, `BTC-EUR`