# JU Exchange API Reference

> Probed manually since official documentation was unfindable (2026-02-23)

## Endpoints
| Purpose | URL |
|---------|-----|
| Products | `GET https://api.ju.com/v1/spot/public/symbol` |
| Trades | `GET https://api.ju.com/v1/spot/public/trade/history?symbol=BTCUSDT&direction=PREV` |
| WebSocket | `wss://sws.ju.com/public` |

## Products API
`GET /v1/spot/public/symbol` returns wrapped array in `data.symbols`.
Key fields:
- `symbol` (e.g. `btc_usdt`)
- `baseCurrency`
- `quoteCurrency`

## Trades API
`GET /v1/spot/public/trade/history?symbol=btc_usdt&direction=PREV&limit=100`
Returns `{"data": {"list": [...]}}`.
Each trade: `{"i": 123, "t": 17000000, "p": "50000", "q": "1.5", "b": false/true}`.
`b` indicates is_maker side rule.

## WebSocket
Subscribe: `{"method": "subscribe", "params": ["trade@btc_usdt", "depth@btc_usdt"], "id": "1"}` (Wait, depth specific channel unknown due to disconnects, using 'depth' speculatively).
Payloads are object wrapped in `data`.
```json
{
  "topic": "trade",
  "event": "trade@btc_usdt",
  "data": {
    "s": "btc_usdt",
    "i": "596340245190092608",
    "t": 1771880593933,
    "p": "64545.40",
    "q": "0.00254",
    "b": false
  }
}
```
