# MEXC API Reference

> Probed directly from API.

## Endpoints

| Purpose | URL | Auth |
|---------|-----|------|
| **Products** | `GET https://api.mexc.com/api/v3/exchangeInfo` | None |
| **REST Trades** | `GET https://api.mexc.com/api/v3/trades?symbol=BTCUSDT&limit=200` | None |
| **WebSocket** | `wss://wbs-api.mexc.com/ws` | None |

## Products API (`/api/v3/exchangeInfo`)

`GET /api/v3/exchangeInfo`

```json
{
  "timezone": "CST",
  "serverTime": 1700000000000,
  "rateLimits": [],
  "symbols": [
    {
      "symbol": "METALUSDT",
      "status": "1",
      "baseAsset": "METAL",
      "quoteAsset": "USDT",
      "permissions": ["SPOT"]
    }
  ]
}
```

## REST Trades API (`/api/v3/trades`)

`GET /api/v3/trades?symbol=BTCUSDT&limit=2` -> JSON Array

```json
[
  {
    "id": null,
    "price": "64516.87",
    "qty": "0.00001859",
    "quoteQty": "1.1993686133",
    "time": 1771880412751,
    "isBuyerMaker": true,
    "isBestMatch": true,
    "tradeType": "ASK"
  },
  {
    "id": null,
    "price": "64519.41",
    "qty": "0.00002634",
    "quoteQty": "1.6994412594",
    "time": 1771880412096,
    "isBuyerMaker": false,
    "isBestMatch": true,
    "tradeType": "BID"
  }
]
```

## WebSocket

EnsoX handles MEXC via `Enso.DedicatedWorkers.Mexc` which subscribes to protobuf encoded streams:
- `spot@public.aggre.deals.v3.api.pb@100ms@BTCUSDT`
- `spot@public.aggre.depth.v3.api.pb@100ms@BTCUSDT`

The dedicated worker parses protobuf and emits normalized JSON:
`{"e": "trade", "s": symbol, "p": price, "q": quantity, "T": time, "m": side}`
`{"e": "depth", "s": symbol, "b": bids, "a": asks, "T": time}`

Therefore, `mexc.json` must map these normalized fields using `discriminator: "e"`.
