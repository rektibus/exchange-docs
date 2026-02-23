# Zaif API Documentation

## General
**REST Base URL**: `https://api.zaif.jp/tapi`
**Websocket Endpoint**: `wss://ws.zaif.jp:8888/stream?currency_pair={pair}`

## Public API (REST)
- **Ticker**: `GET /api/1/ticker/{pair}`
- **Trades**: `GET /api/1/trades/{pair}`
- **Order Book**: `GET /api/1/depth/{pair}`

## WebSocket API
Connect to the stream with a `currency_pair` (e.g., `btc_jpy`).

### Message Format
Pushes real-time trades and order book changes.
Example endpoint: `wss://ws.zaif.jp:8888/stream?currency_pair=mona_jpy`
