# Bitget API Documentation (Spot)

Source: https://bitgetlimited.github.io/apidoc/en/spot/

## REST API (Public)
Base URL: `https://api.bitget.com`

- `GET /api/spot/v1/public/time` — Get server time
- `GET /api/spot/v1/public/currencies` — Get coin list
- `GET /api/spot/v1/public/products` — Get symbols (all trading pairs)
- `GET /api/spot/v1/public/product?symbol=BTCUSDT_SPBL` — Get single symbol

## WebSocket API
Connection limit: 100 connections per IP
Subscription limit: 240 times per hour

### Ping / Pong
1. Set a timer of 30 seconds.
2. If the timer is triggered, send the String `ping`.
3. Expect a `pong` as a response. If not received within 30 seconds, reconnect.

### Format
Subscribe Example:
```json
{
  "op": "subscribe",
  "args": [{
    "instType": "SP",
    "channel": "ticker",
    "instId": "BTCUSDT"
  }]
}
```

### Public Channels
- **Tickers Channel**: `channel: "ticker"` (Retrieve last traded price, bid/ask, 24h vol. Pushed every 200ms)
- **Candlesticks Channel**: `channel: "candle1m"` (1W, 1D, 12H, 4H, 1H, 30m, 15m, 5m, 1m)
- **Depth Channel**: `channel: "books"` (full snapshot + incremental), `"books5"`, `"books15"`
- **Trades Channel**: `channel: "trade"` (Retrieve recent trading data. Pushed whenever there is a trade)

*Note: The official documentation at `https://www.bitget.com/api-doc/` is blocked by Cloudflare for automated scrapers. See the Kraken API Notices section for a similar example of exchanges tracking IP addresses and headers.*
