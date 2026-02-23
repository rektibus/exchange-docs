# Bitstamp API Documentation

See bitstamp_openapi.json and bitstamp_v2_openapi.json for full OpenAPI specs.

Source: https://www.bitstamp.net/api/

## REST API
Base URL: https://www.bitstamp.net/api/v2/

### Public Endpoints
- GET /api/v2/ticker/{currency_pair}/ — Ticker
- GET /api/v2/order_book/{currency_pair}/ — Order book
- GET /api/v2/transactions/{currency_pair}/ — Transactions
- GET /api/v2/trading-pairs-info/ — Trading pairs info

### Authenticated Endpoints
- POST /api/v2/balance/ — Account balance
- POST /api/v2/buy/{currency_pair}/ — Buy
- POST /api/v2/sell/{currency_pair}/ — Sell

## WebSocket API
URL: wss://ws.bitstamp.net

### Channels
- live_trades_{currency_pair} — Live trades
- order_book_{currency_pair} — Order book
- diff_order_book_{currency_pair} — Diff order book
- live_orders_{currency_pair} — Live orders

### Heartbeat
Server sends heartbeat every 10s. No client ping needed.
