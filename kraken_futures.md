# Kraken Futures API Documentation

Based on live API responses for the `futures.kraken.com` endpoints. Covers flexible_futures and futures_inverse.

## REST Endpoints

### Get Instruments (Products)

`GET https://futures.kraken.com/derivatives/api/v3/instruments`

Returns all trading pairs.

```json
{
  "result": "success",
  "instruments": [
    {
      "symbol": "PI_XBTUSD",
      "type": "futures_inverse",
      "underlying": "rr_xbtusd",
      "tickSize": 0.5,
      "contractSize": 1,
      "tradeable": true,
      "marginLevels": [...],
      "base": "BTC",
      "quote": "USD",
      "pair": "BTC:USD"
    },
    {
      "symbol": "PF_BTCUSD",
      "type": "flexible_futures",
      "underlying": "rr_xbtusd",
      "tickSize": 0.5,
      "contractSize": 1,
      "tradeable": true,
      "base": "BTC",
      "quote": "USD",
      "pair": "BTC:USD"
    }
  ],
  "serverTime": "2026-02-23T21:45:00.000Z"
}
```

### Get Trade History

`GET https://futures.kraken.com/derivatives/api/v3/history?symbol=PI_XBTUSD`

Returns recent trades. Trades are returned in an array of objects.

```json
{
  "result": "success",
  "history": [
    {
      "time": "2026-02-23T20:51:56.455Z",
      "trade_id": 100,
      "price": 64373.5,
      "size": 119,
      "side": "buy",
      "type": "fill",
      "uid": "84284ea3-1ca3-44c9-a89d-a05d7aa29240"
    }
  ],
  "serverTime": "2026-02-23T21:45:00.000Z"
}
```

### Get Tickers

`GET https://futures.kraken.com/derivatives/api/v3/tickers`

Returns funding rate and open interest.

```json
{
  "result": "success",
  "tickers": [
    {
      "symbol": "PI_XBTUSD",
      "last": 64540,
      "lastTime": "2026-02-23T21:39:34.088946Z",
      "tag": "perpetual",
      "pair": "XBT:USD",
      "markPrice": 64535.022,
      "openInterest": 5177736.0,
      "fundingRate": 5.0536283e-11
    }
  ],
  "serverTime": "2026-02-23T21:45:00.000Z"
}
```

## WebSocket API

`wss://futures.kraken.com/ws/v1`

### Trades feed

Subscription: `{"event": "subscribe", "feed": "trade", "product_ids": ["PI_XBTUSD"]}`

Payload:
```json
{
  "feed": "trade",
  "product_id": "PI_XBTUSD",
  "uid": "1fba1dc3-...",
  "side": "sell",
  "type": "fill",
  "seq": 100,
  "time": 1715011200000,
  "qty": 5000,
  "price": 64000.5
}
```

### Book feed (Depth)

Subscription: `{"event": "subscribe", "feed": "book", "product_ids": ["PI_XBTUSD"]}`

First payload (snapshot `book_snapshot`):
```json
{
  "feed": "book_snapshot",
  "product_id": "PI_XBTUSD",
  "timestamp": 1715011200000,
  "seq": 1000,
  "bids": [{"price": 64000.5, "qty": 1000}],
  "asks": [{"price": 64001.0, "qty": 1500}]
}
```

Deltas (`book`):
```json
{
  "feed": "book",
  "product_id": "PI_XBTUSD",
  "timestamp": 1715011200100,
  "seq": 1001,
  "bids": [{"price": 64000.5, "qty": 0}],
  "asks": [{"price": 64001.0, "qty": 2000}]
}
```
