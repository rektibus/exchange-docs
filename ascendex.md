# AscendEx (ASD) API Reference
Source: https://ascendex.github.io/ascendex-pro-api/

## REST API

Base URL: `https://ascendex.com`

### Products (Spot)
`GET /api/pro/v1/products`
Response: `{"code": 0, "data": [{"symbol": "BTC/USDT", ...}]}`

### Products (Futures)
`GET /api/pro/v2/futures/contract`
Response: `{"code": 0, "data": [{"symbol": "BTC-PERP", ...}]}`

Key fields per contract:
| Field | Example | Description |
|-------|---------|-------------|
| symbol | "BTC-PERP" | Contract symbol |
| status | "Normal" / "NoTrading" | Trading status |
| displayName | "BTCUSDT" | Display name |
| settlementAsset | "USDT" | Quote/settlement currency |
| underlying | "BTC/USDT" | Underlying pair |
| priceFilter.tickSize | "0.1" | Min price increment |
| lotSizeFilter.lotSize | "0.0001" | Min qty increment |
| lotSizeFilter.minQty | "0.0001" | Min order qty |

**Contract type**: Linear perpetual. Quantity is in underlying coin units (no contract multiplier).
`lotSize` is step size, NOT contract size. `contract_size = 1.0` for all pairs.

### Market Trades (Spot)
`GET /api/pro/v1/trades?symbol=BTC/USDT&n=100`

Params: `symbol` (required), `n` (limit, optional)

Response:
```json
{"code": 0, "data": {
  "m": "trades", "symbol": "BTC/USDT",
  "data": [
    {"seqnum": 144115191800016553, "p": "69192.4", "q": "0.13855", "ts": 1771294515656, "bm": false}
  ]
}}
```

| Field | Type | Description |
|-------|------|-------------|
| seqnum | Long | Trade sequence number |
| p | String | Price |
| q | String | Quantity |
| ts | Long | Timestamp (ms) |
| bm | Boolean | Is buyer maker? (true=sell, false=buy) |

### Order Book (Spot)
`GET /api/pro/v1/depth?symbol=BTC/USDT`

Response:
```json
{"code": 0, "data": {
  "m": "depth-snapshot", "symbol": "BTC/USDT",
  "data": {
    "seqnum": 5068757, "ts": 1573165838976,
    "asks": [["0.06848", "4084.2"]], "bids": [["0.06703", "13500"]]
  }
}}
```

### Ticker (Spot)
`GET /api/pro/v1/ticker?symbol=BTC/USDT`

### Futures Pricing Data (Funding + OI)
`GET /api/pro/v2/futures/pricing-data`
Response wrapper: `data.contracts` — contains `fundingRate`, `openInterest`, `nextFundingTime` per symbol.

## WebSocket API

### Spot WS URL
`wss://ascendex.com/0/api/pro/v1/stream`

### Futures WS URL
`wss://ascendex.com/0/api/pro/v2/stream`

### Ping/Pong
Send: `{"op": "ping"}`
Response: `{"m": "pong", "hp": 1}` or `{"m": "ping"}`

### Subscribe Format
```json
{"op": "sub", "ch": "CHANNEL:SYMBOL"}
```

### Channel: Market Trades
Subscribe: `{"op": "sub", "ch": "trades:BTC/USDT"}`

Response:
```json
{"m": "trades", "symbol": "BTC/USDT",
 "data": [{"p": "0.068600", "q": "100.000", "ts": 1573069903254, "bm": false, "seqnum": 144115188077966308}]}
```
- Discriminator: `"m"` field
- `data` is an array (may aggregate consecutive same-price trades)
- `bm`: true = buyer is maker (= sell side), false = buyer is taker (= buy side)

### Channel: Level 2 Order Book (Depth)
Subscribe: `{"op": "sub", "ch": "depth:BTC/USDT"}`

Response:
```json
{"m": "depth", "symbol": "BTC/USDT",
 "data": {"ts": 1573069021376, "seqnum": 2097965,
   "asks": [["0.06844", "10760"]], "bids": [["0.06777", "562.4"]]}}
```
- Levels: `[price_string, size_string]` — indexed format, price_index=0, size_index=1
- Size=0 means delete the level

### Channel: BBO (Best Bid/Offer)
Subscribe: `{"op": "sub", "ch": "bbo:BTC/USDT"}`

Response:
```json
{"m": "bbo", "symbol": "BTC/USDT",
 "data": {"ts": 1573068442532, "bid": ["9309.11", "0.0197172"], "ask": ["9309.12", "0.8851266"]}}
```

### Ack Messages
- Connected: `{"m": "connected", ...}`
- Subscribe ack: `{"m": "sub", ...}`
- Pong: `{"m": "pong", ...}`
