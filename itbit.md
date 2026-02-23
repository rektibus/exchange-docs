# itBit / Paxos Exchange API Documentation

Source: https://docs.paxos.com/api-reference/websockets/overview

## REST API
Base URL: `https://api.paxos.com/v2`

### Public Endpoints
- `GET /v2/markets` — List available markets
- `GET /v2/markets/{market}/ticker` — Get ticker
- `GET /v2/markets/{market}/order-book` — Get order book
- `GET /v2/markets/{market}/recent-executions` — Get recent trades

### Private Endpoints
- `POST /v2/orders` — Create order
- `DELETE /v2/orders/{id}` — Cancel order
- `GET /v2/orders/{id}` — Get order
- `GET /v2/profiles/{id}/balances` — Get balances

## WebSocket API (Public)

### Server Endpoints
- Production: `wss://ws.paxos.com`
- Sandbox: `wss://ws.sandbox.paxos.com`

### Available Channels
- `/executiondata` — All markets execution data
- `/executiondata/{market}` — Single market execution data
- `/marketdata` — All markets order book data
- `/marketdata/{market}` — Single market order book data
- `/marketdata/stablecoin/{market}` — Stablecoin market price data

### Execution Data Feed
- Initial message: last execution at connection time
- Subsequent messages: each new execution as it occurs
- Idle markets: no messages until new activity
- Reconnection: receives last execution (dedup via `match_number`)

### Market Data Feed
- SNAPSHOT messages: full order book on connection
- UPDATE messages: incremental order book changes

### Connection
- URL format: `wss://ws.paxos.com/executiondata` or `wss://ws.paxos.com/marketdata/{market}`
- No authentication required for public channels
- Ping: native WebSocket ping/pong

## Authentication
- REST: OAuth2 bearer token
- API keys generated from Paxos Dashboard → Settings → API Management
