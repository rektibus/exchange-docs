# WOO X API Documentation (V3)

Source: https://docs.woox.io/v3/overview/introduction

## REST API
Base URL: `https://api.woox.io` (production)
Staging: `https://api.staging.woox.io`

### Public Endpoints
- `GET /v3/public/info` — Exchange information
- `GET /v3/public/info/{symbol}` — Available symbols
- `GET /v3/public/market_trades` — Market trades
- `GET /v3/public/market_trades_history` — Market trades history
- `GET /v3/public/orderbook/{symbol}` — Orderbook snapshot
- `GET /v3/public/kline` — Kline (candlestick)
- `GET /v3/public/kline_history` — Kline historical data
- `GET /v3/public/token` — Available tokens
- `GET /v3/public/token_network` — Token network info
- `GET /v3/public/funding_rates` — Predicted funding rate for all markets
- `GET /v3/public/funding_rate/{symbol}` — Predicted funding rate for one market
- `GET /v3/public/funding_rate_history/{symbol}` — Funding rate history
- `GET /v3/public/futures` — Futures info for all markets
- `GET /v3/public/futures/{symbol}` — Futures for one market

### Private Endpoints (Trading)
- `POST /v3/order` — Send order
- `DELETE /v3/order` — Cancel order
- `DELETE /v3/orders` — Cancel orders (batch)
- `DELETE /v3/orders/pending` — Cancel all pending orders
- `GET /v3/order/{oid}` — Get order
- `GET /v3/orders` — Get orders
- `PUT /v3/order` — Edit order
- `POST /v3/algo/order` — Send algo order
- `GET /v3/algo/order/{oid}` — Get algo order
- `GET /v3/algo/orders` — Get algo orders
- `GET /v3/trade/{tid}` — Get trade
- `GET /v3/trades` — Get trades
- `GET /v3/trade_history` — Get trade history

### Account
- `GET /v3/balances` — Get current holding
- `GET /v3/accountinfo` — Get account information
- `GET /v3/token_history` — Get token history
- `GET /v3/positions` — Get all position info
- `GET /v3/position/{symbol}` — Get one position info

## WebSocket API V2
URL: `wss://wss.woox.io/ws/stream/{app_id}`
Auth URL: `wss://wss.woox.io/ws/stream/{app_id}`

### Public Channels
- `orderbook` — Full orderbook snapshot
- `orderbookupdate` — Orderbook delta updates
- `trade` — Individual trades
- `trades` — Batch trades
- `ticker` — 24h ticker
- `tickers` — All 24h tickers
- `bbo` — Best bid/offer
- `bbos` — All BBOs
- `kline` — K-line candlestick
- `indexprice` — Index price
- `markprice` / `markprices` — Mark prices
- `estfundingrate` — Estimated funding rate
- `openinterests` — Open interests

### Private Channels
- `balance` — Account balance updates
- `executionreport` — Order execution updates
- `algoexecutionreportv2` — Algo order execution
- `position` — Position updates

### Ping/Pong
Send `{"event":"ping"}` → receive `{"event":"pong"}`

## Authentication
- REST: HMAC-SHA256 signature with API key, timestamp, and request body
- WS: Auth message with key + signature
