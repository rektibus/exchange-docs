# Bitkub API Documentation

## General
**REST Base URL**: `https://api.bitkub.com`
**WebSocket Endpoint**: `wss://api.bitkub.com/websocket-api/<streamName>`

## Market Data (REST v3)
- **Symbols**: `GET /api/v3/market/symbols`
- **Ticker**: `GET /api/v3/market/ticker`
- **Trades**: `GET /api/v3/market/trades`
- **Bids**: `GET /api/v3/market/bids`
- **Asks**: `GET /api/v3/market/asks`
- **Depth**: `GET /api/v3/market/depth`

## WebSocket API
### Stream Name Format
`<serviceName>.<serviceType>.<symbol>` (case-insensitive)

### Trade Stream
- **Name**: `market.trade.<symbol>` (e.g., `market.trade.thb_btc`)
- **Response**:
```json
{
  "stream": "market.trade.thb_eth",
  "sym": "THB_ETH",
  "txn": "ETHSELL0000074282",
  "rat": "5977.00",
  "amt": 1.556539,
  "bid": "2048451",
  "sid": "2924729",
  "ts": 1542268567
}
```

### Ticker Stream
- **Name**: `market.ticker.<symbol>` (e.g., `market.ticker.thb_btc`)

### Multiple Streams
Connect to multiple streams by joining names with comma:
`wss://api.bitkub.com/websocket-api/market.trade.thb_btc,market.trade.thb_eth`
