# Kraken API Documentation

Source: https://docs.kraken.com/api/

## Spot REST API
Base URL: `https://api.kraken.com/0`

### Public Endpoints
- `GET /public/AssetPairs` — Get tradable asset pairs
- `GET /public/Ticker` — Get ticker information (prices start at midnight UTC)
- `GET /public/Trades` — Get recent trades (returns last 1000 by default)
- `GET /public/OHLC` — Get OHLC data
- `GET /public/Depth` — Get order book
- `GET /public/Spread` — Get recent spreads
- `GET /public/Assets` — Get asset info
- `GET /public/SystemStatus` — Get system status
- `GET /public/Time` — Get server time

### Private Endpoints
- `POST /private/Balance` — Get account balance
- `POST /private/TradeBalance` — Get trade balance
- `POST /private/OpenOrders` — Get open orders
- `POST /private/ClosedOrders` — Get closed orders
- `POST /private/QueryOrders` — Query orders info
- `POST /private/TradesHistory` — Get trades history
- `POST /private/AddOrder` — Add order
- `POST /private/CancelOrder` — Cancel order

## Spot WebSocket V2
URL: `wss://ws.kraken.com/v2`
Auth URL: `wss://ws-auth.kraken.com/v2`

### Channels
- `ticker` — Level 1 market data (best bid/offer + recent trades)
- `book` — Order book
- `trade` — Trades
- `ohlc` — OHLC candles
- `instrument` — Instrument status

### Ping/Pong
WebSocket V2 uses native ping/pong frames.

## Futures REST API
Base URL: `https://futures.kraken.com/derivatives/api/v3`

### Public Endpoints
- `GET /api/v3/instruments` — Get instruments
- `GET /api/v3/tickers` — Get tickers
- `GET /api/v3/orderbook` — Get order book
- `GET /api/v3/history` — Get trade history
- `GET /api/v3/feeschedules` — Get fee schedules

## Futures WebSocket
URL: `wss://futures.kraken.com/ws/v1`

### Colocation Endpoints
- Spot WS: `colo-london.vip-ws.kraken.com`
- Futures REST: `colo-london.vip.futures.kraken.com`
- Futures WS: `wss://colo-london.vip.futures.kraken.com/ws/v1`

## Authentication
- REST: HMAC-SHA512 signature
- WS V2: Token-based (obtain token via REST `GetWebSocketsToken`)
