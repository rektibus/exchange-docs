# Bithumb Pro WebSocket API

Source: https://github.com/bithumb-pro/bithumb.pro-official-api-docs/blob/master/ws-api.md

## Connection
- Endpoint: `wss://global-api.bithumb.pro/message/realtime`
- Subscribe via URL query: `?subscribe=TRADE:BTC-USDT,ORDERBOOK:BTC-USDT`
- Or via command: `{"cmd":"subscribe","args":["TRADE:BTC-USDT","ORDERBOOK:BTC-USDT"]}`

## Subscribe/Unsubscribe Commands

```json
{"cmd": "subscribe", "args": ["TRADE:BTC-USDT", "ORDERBOOK:BTC-USDT"]}
{"cmd": "unSubscribe", "args": ["TRADE:BTC-USDT"]}
```

## Topics

### TRADE — Spot Trade Messages

| Field  | Description   | Type   |
|--------|---------------|--------|
| p      | deal price    | String |
| s      | trade type    | String ("buy" or "sell") |
| v      | deal quantity  | String |
| t      | trade time    | String |
| symbol |               | String |
| ver    | version number | String |

Example:
```json
{
  "code": 4,
  "data": {
    "p": "4003.5",
    "s": "buy",
    "v": "0.1",
    "t": "",
    "symbol": "TBTCUSD",
    "ver": "375"
  },
  "timestamp": 1553235407,
  "topic": "TRADE"
}
```

### ORDERBOOK — Spot Orderbook

| Field  | Description | Type |
|--------|-------------|------|
| b      | bids        | String[2] [price, quantity] |
| s      | asks        | String[2] [price, quantity] |
| symbol |             | String |
| ver    | version     | String |

Example:
```json
{
  "code": 4,
  "data": {
    "b": [["4003.5","1"],["4001.5","890"]],
    "s": [["4005","100"],["4006","107"]],
    "symbol": "TBTCUSD",
    "ver": "375"
  },
  "timestamp": 1553235407,
  "topic": "ORDERBOOK"
}
```

### CONTRACT_TICKER — Futures Ticker (includes funding + OI)

| Field | Description |
|-------|-------------|
| fundRate0 | Next funding rate |
| fundTime0 | Next funding time |
| lastPrice | Last deal price |
| openValue | Open position value |
| openInterest | Open interest |
| symbol | |

### CONTRACT_ORDERBOOK — Futures Orderbook

Same format as ORDERBOOK but topic is `CONTRACT_ORDERBOOK`

### code values
- 4: data message
- 00006: full orderbook snapshot
- 00007: orderbook incremental update
