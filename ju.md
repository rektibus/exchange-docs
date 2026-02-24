# JU Exchange API Documentation

Official Docs: https://www.ju.com/en/api-doc

> Note: JU is the rebranded XT exchange. It shares the exact same API structure.

## Overview

- REST Base URL: `https://api.ju.com`
- Public WebSocket: `wss://sws.ju.com/public`

## Public REST Endpoints

### 1. Market Configuration / Symbol Info
**Endpoint**: `GET /v1/spot/public/symbol`

Returns configuration, precision limits, and trading status for markets.

### 2. Market Depth (Orderbook)
**Endpoint**: `GET /v1/spot/public/depth`
**Parameters**: `symbol` 
**Limit**: 1 req/s per IP

```json
{
  "code": 200,
  "msg": "SUCCESS",
  "data": {
    "timestamp": 1662445330524,
    "lastUpdateId": 137333589606963580,
    "bids": [
      ["200.0000", "0.996000"], // [price, quantity]
      ["100.0000", "0.001000"]
    ],
    "asks": []
  }
}
```

### 3. Recent Trades
**Endpoint**: `GET /v1/spot/public/trade/recent` 
**Parameters**: `symbol`
**Limit**: 10 req/s per IP

```json
{
  "data": [
    {
      "i": 0, // id
      "t": 0, // timestamp (ms)
      "p": "string", // price
      "q": "string", // quantity
      "v": "string", // volume
      "b": true // is buyerMaker
    }
  ]
}
```

### 4. Historical Trades
**Endpoint**: `GET /v1/spot/public/trade/history`
**Parameters**: `symbol`
**Limit**: 10 req/s per IP

Same response format as Recent Trades.

### 5. Tickers
- **Full**: `GET /v1/spot/public/ticker`
- **Latest Price**: `GET /v1/spot/public/ticker/price`
- **Best Book**: `GET /v1/spot/public/ticker/book`
- **24h Stats**: `GET /v1/spot/public/ticker/24h`

## Public WebSocket

**Endpoint**: `wss://sws.ju.com/public`
**Headers**: `Sec-Websocket-Extensions: permessage-deflate` (server compresses via Deflate)

### Subscription Format
Format: `{topic}@{symbol}` (e.g., `trade@btc_usdt`)

To subscribe, send the subscription message containing the topic + symbol combinations.

### 1. Trades (`trade@{symbol}`)

Stream of real-time trades.

```json
{
  "topic": "trade",
  "event": "trade@btc_usdt",
  "data": {
    "s": "btc_usdt", // symbol
    "i": 6316559590087222000, // tradeId
    "t": 1655992403617, // time
    "oi": 6616559590087222666, // orderId
    "p": "43000", // price
    "q": "0.21", // quantity
    "v": "9030", // quoteQty
    "b": true // is buyerMaker
  }
}
```

### 2. Incremental Depth (`depth_update@{symbol}`)

Pushes orderbook deltas at 100ms intervals.

```json
{
  "topic": "depth_update",
  "event": "depth_update@btc_usdt",
  "data": {
    "s": "btc_usdt", // symbol
    "fi": 121, // firstUpdateId
    "i": 123, // lastUpdateId
    "a": [ // asks (sell orders)
      ["34000", "1.2"], // [price, quantity]
      ["34001", "2.3"]
    ],
    "b": [ // bids (buy orders)
      ["32000", "0.2"],
      ["31000", "0.5"]
    ]
  }
}
```

### Heartbeat
Client must periodically send `"ping"` string, and the server replies with `"pong"`.

---

## Private Endpoints

Private interactions (Order, Balance, Info) use authentication via signing.

- **Balances**: `GET /v1/spot/balance` and `GET /v1/spot/balances`
- **Orders**: `POST /v1/spot/order`, `DELETE /v1/spot/order`
- **Private WS**: `wss://sws.ju.com/private`
