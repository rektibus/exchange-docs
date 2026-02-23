# Kucoin API Documentation

## General
**REST Base URL**: `https://api.kucoin.com`
**Public WS Endpoint**: `wss://x-push-spot.kucoin.com` (Requires a token negotiation via REST first: `POST /api/v1/bullet-public`)

## Market Data (REST)
- **Tickers**: `GET /api/v1/symbols`
- **Recent Trades**: `GET /api/v1/market/histories?symbol=BTC-USDT`
  - Kucoin's API states this endpoint returns the **last 100 transaction records** for the specified symbol.
  - The returned data is sorted in descending order by the latest update time.
  - While some documentation mentions time ranges (7-day window, `startAt`, `endAt`), empirical testing shows that these parameters (`startTime`, `startAt`, `since`, `after`) are generally ignored for this specific public endpoint, making it effectively a fixed 100-trade rolling window.

## WebSocket API (Spot)
### Orderbook Level 2
There are multiple streams for depth:
- `increment`: Real-time incremental changes (deltas). Clients must build a local orderbook using a REST snapshot and applying these deltas.
- `depth5`: Top 5 bids and asks, pushed every 100ms.
- `depth50`: Top 50 bids and asks, pushed every 100ms.

Topics:
- Spot Level 2 (incremental): `/market/level2:{symbol}`
- Spot Level 2 (Depth 5): `/spotMarket/level2Depth5:{symbol}`
- Spot Level 2 (Depth 50): `/spotMarket/level2Depth50:{symbol}`

### Trades
- Spot Match: `/market/match:{symbol}`

### Authentication
- Public WS endpoints do not require signatures but do require an initial token fetch (`bullet-public`).
