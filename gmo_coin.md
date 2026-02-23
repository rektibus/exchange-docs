# GMO Coin API Documentation

## General
**Public REST Base**: `https://api.coin.z.com/public`
**Public WS Endpoint**: `wss://api.coin.z.com/ws/public/v1`
**Private REST Base**: `https://api.coin.z.com/private`
**Private WS Endpoint**: `wss://api.coin.z.com/ws/private/v1`

## Market Data (REST)
- **Ticker**: `GET /v1/ticker` (params: `symbol`)
- **Order Books**: `GET /v1/orderbooks` (params: `symbol`)
- **Trade History**: `GET /v1/trades` (params: `symbol`, `page`, `count`)
- **KLine Data**: `GET /v1/klines` (params: `symbol`, `interval`)
- **Trade Rules**: `GET /v1/symbols`

## Public WebSocket API
### Channels
- `ticker` — Real-time ticker updates
- `orderbooks` — Real-time order book
- `trades` — Real-time trade stream

### Subscription Format
```json
{
  "command": "subscribe",
  "channel": "trades",
  "symbol": "BTC"
}
```

### Notes
- Ping sent from server once per minute; 3 missed pongs = disconnect
- Rate limit: 1 subscribe/unsubscribe per second per IP
- Symbols are bare (e.g., `BTC`, `ETH`, not pairs)
