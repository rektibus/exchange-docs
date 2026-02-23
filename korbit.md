# Korbit API Documentation

## General
**REST Base URL**: `https://api.korbit.co.kr`
**Public WS Endpoint**: `wss://ws-api.korbit.co.kr/v2/public`
**Private WS Endpoint**: `wss://ws-api.korbit.co.kr/v2/private`

## Market Data (REST)
- **Tickers**: `GET /v2/tickers` (supports multiple pairs via query)
- **Order Book**: `GET /v2/orderbook` (params: `currency_pair`, `category`)
- **Recent Trades**: `GET /v2/trades` (params: `currency_pair`, `time`, `id`)
- **Candlesticks**: `GET /v2/candles` (params: `currency_pair`, `interval`)
- **Trading Pairs**: `GET /v2/trading-pairs`

## WebSocket API (v2)
### Public Channels
- `ticker` — Real-time current prices for a trading pair
- `orderbook` — Real-time order book data
- `trade` — Real-time trade history

### Subscription Format
```json
{
  "method": "subscribe",
  "type": "ticker",
  "params": {
    "currency_pairs": ["btc_krw"]
  }
}
```

### Notes
- Auth: HMAC-SHA256 or ED25519 signatures
- Ping/pong heartbeat maintained by server
