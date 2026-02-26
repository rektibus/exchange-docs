# Poloniex API Reference

> Source: Probed directly from API due to docs.poloniex.com relying on SPA scripts (2026-02-23)

## Endpoints

| Purpose | URL | Auth |
|---------|-----|------|
| **Products** | `GET https://api.poloniex.com/markets` | None |
| **REST Trades** | `GET https://api.poloniex.com/markets/{symbol}/trades?limit=200` | None |
| **WebSocket** | `wss://ws.poloniex.com/ws/public` | None |

## Products API

`GET /markets` → Bare JSON array

```json
[
  {
    "symbol": "DASH_BTC",
    "baseCurrencyName": "DASH",
    "quoteCurrencyName": "BTC",
    "displayName": "DASH/BTC",
    "state": "NORMAL",
    "symbolTradeLimit": {
      "symbol": "DASH_BTC",
      "priceScale": 6,
      "quantityScale": 2,
      "amountScale": 6,
      "minQuantity": "0.01",
      "minAmount": "0.00001",
      "maxQuantity": "0",
      "maxAmount": "0",
      "highestBid": "0",
      "lowestAsk": "0"
    }
  }
]
```

## REST Trades API

`GET /markets/BTC_USDT/trades` → Bare JSON array

```json
[
  {
    "id": "193498016",
    "price": "64427.33",
    "quantity": "0.040355",
    "amount": "2599.96490215",
    "takerSide": "BUY",
    "ts": 1771880201966,
    "createTime": 1771880201958
  }
]
```

## WebSocket

### Subscribe
```json
{
  "event": "subscribe",
  "channel": ["trades"],
  "symbols": ["BTC_USDT"]
}
```

### Ack
- `{"event": "subscribe", "channel": "trades", "symbols": ["BTC_USDT"]}`

### Ping
`{"event": "ping"}` → Responses with `{"event": "pong"}`

### Trade Channel (`channel: "trades"`)
Trade payloads are wrapped in a `data` array.

```json
{
  "channel": "trades",
  "data": [
    {
      "symbol": "BTC_USDT",
      "amount": "1668.89652446",
      "quantity": "0.025894",
      "takerSide": "sell",
      "createTime": 1771880291116,
      "price": "64451.09",
      "id": "193498143",
      "ts": 1771880291129
    }
  ]
}
```

### Orderbook Channel (`channel: "book_lv2"`)
Book payloads are wrapped in a `data` array. The first message contains a full book, subsequent messages contain deltas (size ``"0"`` means remove).

```json
{
  "channel": "book_lv2",
  "data": [
    {
      "symbol": "BTC_USDT",
      "createTime": 1771880224555,
      "asks": [],
      "bids": [
        ["64356.7", "0"],
        ["64276.58", "0.072092"]
      ],
      "lastId": 5961104423,
      "id": 5961104424,
      "ts": 1771880224575
    }
  ]
}
```
