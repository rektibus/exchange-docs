# XT Exchange API Documentation

Official Docs: https://doc.xt.com
Python SDK: https://pypi.org/project/pyxt/
Java SDK: https://github.com/xt-com/xt4-java-demo
JS SDK: https://www.npmjs.com/package/xt-open-api

> XT and JU (formerly XT rebranded) share the **exact same API structure** (v4, identical response formats and field names). JU docs: see `ju.md`.

## Base URLs

| Service | URL |
|---------|-----|
| Spot REST | `https://sapi.xt.com` |
| Spot WS Public | `wss://stream.xt.com/public` |
| Spot WS Private | `wss://stream.xt.com/private` |
| Futures REST | `https://fapi.xt.com` |

## Response Format

All responses use the same wrapper:
```json
{
  "rc": 0,        // return code (0=success)
  "mc": "SUCCESS", // message code
  "ma": [],        // message arguments
  "result": { ... } // actual data
}
```

---

## Spot REST Endpoints

Base: `https://sapi.xt.com`
Public endpoints start with `/v4/public/` (no auth required).

### GET /v4/public/symbol
Get symbol/market configuration. Returns: `data.symbols[]` with `symbol`, `baseCurrency`, `quoteCurrency`, `pricePrecision`, `quantityPrecision`, `state`, `tradingEnabled`, `filters[]`.

### GET /v4/public/depth
Get orderbook depth.
**Params**: `symbol` (required), `limit` (optional)
**Rate**: 10/s/ip

```json
{
  "rc": 0,
  "result": {
    "timestamp": 1662445330524,
    "lastUpdateId": 137333589606963580,
    "bids": [["200.0000", "0.996000"]], // [price, quantity]
    "asks": []
  }
}
```

### GET /v4/public/kline
Get K-line/OHLCV data.
**Params**: `symbol`, `interval`, `limit`

### GET /v4/public/trade/recent
Query recent trades.
**Params**: `symbol`, `limit`
**Rate**: 10/s/ip

```json
{
  "rc": 0,
  "result": [
    {
      "i": 0,      // trade ID
      "t": 0,      // timestamp (ms)
      "p": "string", // price
      "q": "string", // quantity
      "v": "string", // volume (quote amount)
      "b": true     // is buyer maker
    }
  ]
}
```

### GET /v4/public/trade/history
Query historical trades.
**Params**: `symbol`, `limit`, `direction` (`PREV`|`NEXT`)
**Rate**: 10/s/ip

Same response format as recent trades.

### GET /v4/public/ticker
Full ticker for all markets.

### GET /v4/public/ticker/price
Latest prices ticker.

### GET /v4/public/ticker/book
Best bid/ask ticker.

### GET /v4/public/ticker/24h
24h statistics.

---

## Spot WebSocket (Public)

**URL**: `wss://stream.xt.com/public`
**Required header**: `Sec-WebSocket-Extensions: permessage-deflate`

### Subscription Format
`{topic}@{symbol}` (e.g., `trade@btc_usdt`)

### Trade Stream (`trade@{symbol}`)
```json
{
  "topic": "trade",
  "event": "trade@btc_usdt",
  "data": {
    "s": "btc_usdt",
    "i": 6316559590087222000,
    "t": 1655992403617,
    "p": "43000",
    "q": "0.21",
    "v": "9030",
    "b": true
  }
}
```

### Incremental Depth (`depth_update@{symbol}`)
100ms push rate.
```json
{
  "topic": "depth_update",
  "event": "depth_update@btc_usdt",
  "data": {
    "s": "btc_usdt",
    "fi": 121,
    "i": 123,
    "a": [["34000", "1.2"]],
    "b": [["32000", "0.2"]]
  }
}
```

### Limited Depth (`depth@{symbol},{level}`)
Snapshot depth at specific levels.

### Ticker (`ticker@{symbol}`)
Real-time ticker updates.

### K-line (`kline@{symbol},{interval}`)
Real-time candlestick updates.

### Heartbeat
Send `"ping"`, server replies `"pong"`.

---

## Spot Private Endpoints (Authenticated)

Authentication uses HMAC-SHA256 signature.

### Orders
- `GET /v4/order` — Get single order
- `POST /v4/order` — Submit order
- `DELETE /v4/order/{orderId}` — Cancel order
- `GET /v4/open-order` — Get open orders
- `POST /v4/batch-order` — Submit batch orders

### Trades
- `GET /v4/trade` — Query user's trade history

### Balance
- `GET /v4/balances` — Get all balances
- `GET /v4/balance` — Get single currency balance

### Transfers
- `POST /v4/balance/transfer` — Transfer between systems

---

## Spot WebSocket (Private)

**URL**: `wss://stream.xt.com/private`

### Channels
- **Balance changes**: Real-time balance updates
- **Order changes**: Order status updates
- **Order filled**: Trade fill notifications

---

## Symbol Format
Markets use underscore separator: `btc_usdt`, `eth_usdt`, `xt_usdt`
All lowercase in WS.

## Rate Limits
- Most public endpoints: 10 req/s per IP
- Depth: 10 req/s per IP
