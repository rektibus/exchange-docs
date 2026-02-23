# Bitunix Futures API Documentation

Source: https://openapidoc.bitunix.com/doc/common/introduction.html
GitHub Demo: https://github.com/BitunixOfficial/open-api

## API Domain
- REST: `https://fapi.bitunix.com`
- WebSocket Public: `wss://fapi.bitunix.com/public/`
- WebSocket Private: `wss://fapi.bitunix.com/private/`

## REST API — Market Endpoints

### Get Trading Pairs
```
GET /api/v1/futures/market/trading_pairs
```
No parameters required.

Response:
```json
{
  "code": 0,
  "data": [
    {
      "symbol": "BTCUSDT",
      "base": "BTC",
      "quote": "USDT",
      "minTradeVolume": "0.0001",
      "minBuyPriceOffset": "-0.5",
      "maxSellPriceOffset": "100",
      "maxLimitOrderVolume": "1000",
      "maxMarketOrderVolume": "120",
      "basePrecision": 4,
      "quotePrecision": 1,
      "maxLeverage": 200,
      "minLeverage": 1,
      "defaultLeverage": 20,
      "defaultMarginMode": "2",
      "priceProtectScope": "0.01",
      "symbolStatus": "OPEN"
    }
  ],
  "msg": "Success"
}
```

### Get Depth
```
GET /api/v1/futures/market/depth?symbol=BTCUSDT&limit=max
```
| Param | Type | Required | Notes |
|-------|------|----------|-------|
| symbol | string | Y | Trading pair |
| limit | string | N | Number of levels or "max" |

Response:
```json
{"code":0,"data":{"asks":[[0.1001,0.1],[0.1002,10]],"bids":[[0.1,1],[0.0999,10.23]]},"msg":"Success"}
```

### Get Funding Rate
```
GET /api/v1/futures/market/funding_rate?symbol=BTCUSDT
```
| Param | Type | Required | Notes |
|-------|------|----------|-------|
| symbol | string | Y | Trading pair |

Response:
```json
{
  "code": 0,
  "data": {
    "symbol": "BTCUSDT",
    "markPrice": "67419.7",
    "lastPrice": "67412.7",
    "fundingRate": "0.00072",
    "fundingInterval": 8,
    "nextFundingTime": "1771430400000"
  },
  "msg": "Success"
}
```

### Get Funding Rate Batch
```
GET /api/v1/futures/market/funding_rate_batch
```
No parameters — returns funding for all symbols.

### Get Tickers
```
GET /api/v1/futures/market/tickers?symbols=BTCUSDT,ETHUSDT
```
| Param | Type | Required | Notes |
|-------|------|----------|-------|
| symbols | string | N | Comma-separated. Omit for all |

Response:
```json
{
  "code": 0,
  "data": [
    {"symbol":"BTCUSDT","markPrice":"57892.1","lastPrice":"57891.2","open":"6.31","last":"6.31","quoteVol":"0","baseVol":"0","high":"6.31","low":"6.31"}
  ],
  "msg": "Success"
}
```

### Get Kline
```
GET /api/v1/futures/market/kline?symbol=BTCUSDT&klineType=1min&startTime=...&endTime=...
```
| Param | Type | Required | Notes |
|-------|------|----------|-------|
| symbol | string | Y | Trading pair |
| klineType | string | Y | 1min,5min,15min,30min,1h,4h,1d,1w,1M |
| startTime | string | N | Start timestamp (ms) |
| endTime | string | N | End timestamp (ms) |

### NOTE: No Public Trades Endpoint
The futures REST API does NOT have a public recent-trades endpoint.
Available market endpoints: trading_pairs, depth, funding_rate, funding_rate_batch, tickers, kline.
No trades → recovery via REST is not possible for this exchange.

### NOTE: No Open Interest Endpoint
The futures REST API does NOT have a public open interest endpoint.

---

## WebSocket API

### Connection
- Public URL: `wss://fapi.bitunix.com/public/`
- Max 300 channel subscriptions per connection
- No auth required for public channels

### Ping/Pong
Request:
```json
{"op":"ping","ping":1732519687}
```
Response:
```json
{"op":"ping","pong":1732519687,"ping":1732519690}
```

### Connect Ack
On connection, server sends:
```json
{"op":"connect","data":{"result":true}}
```

### Subscribe
```json
{"op":"subscribe","args":[{"symbol":"BTCUSDT","ch":"trade"},{"symbol":"BTCUSDT","ch":"depth_books"}]}
```

### Subscribe Ack
```json
{"op":"subscribe","ch":"trade","symbol":"BTCUSDT","data":{"result":true}}
```

### Unsubscribe
```json
{"op":"unsubscribe","args":[{"symbol":"BTCUSDT","channel":"market_kline_1min"}]}
```

---

## WS Public Channels

### Trade Channel
Subscribe: `{"op":"subscribe","args":[{"symbol":"BTCUSDT","ch":"trade"}]}`

Push data:
```json
{
  "ch": "trade",
  "symbol": "BTCUSDT",
  "ts": 1732178884994,
  "data": [
    {"t": "2024-12-04T11:36:47.959908526Z", "p": "27000.5", "v": "0.001", "s": "buy"},
    {"t": "2024-12-04T11:36:47.959908526Z", "p": "27000.0", "v": "0.001", "s": "sell"}
  ]
}
```
Fields: `t` = ISO timestamp, `p` = price (string), `v` = volume (string), `s` = side (buy/sell)

### Depth Channel
Channel names:
- `depth_books` — full snapshot first, then deltas (changed levels only)
- `depth_book1` — 1 level pushed every time
- `depth_book5` — 5 levels pushed every time
- `depth_book15` — 15 levels pushed every time

Subscribe: `{"op":"subscribe","args":[{"symbol":"BTCUSDT","ch":"depth_book5"}]}`

Push data:
```json
{
  "ch": "depth_book5",
  "symbol": "BTCUSDT",
  "ts": 1732178884994,
  "data": {
    "b": [["7403.89", "0.002"]],
    "a": [["7405.96", "3.340"]]
  }
}
```
Fields: `b` = bids `[[price, qty]]`, `a` = asks `[[price, qty]]`, `ts` = milliseconds at top level

### MarketPrice Channel
Subscribe: `{"op":"subscribe","args":[{"symbol":"BTCUSDT","ch":"market_price"}]}`

### Ticker Channel
Subscribe: `{"op":"subscribe","args":[{"symbol":"BTCUSDT","ch":"ticker"}]}`

### Tickers Channel
Subscribe: `{"op":"subscribe","args":[{"ch":"tickers"}]}`
(All symbols, no symbol param needed)

### Kline Channel
Subscribe: `{"op":"subscribe","args":[{"symbol":"BTCUSDT","ch":"market_kline_1min"}]}`

---

## Key Notes
- All REST responses wrapped in `{"code":0,"data":...,"msg":"Success"}`
- Code 0 = success, code 2 = parameter error
- Product symbols are UPPERCASE (e.g. BTCUSDT)
- WS trade timestamps are ISO format (e.g. "2024-12-04T11:36:47.959908526Z")
- WS depth timestamps are milliseconds (top-level `ts` field)
- WS prices/quantities are strings
- No public REST trades endpoint — no recovery possible
- No public REST open interest endpoint
- `depth_books` channel sends snapshot+delta, `depth_book{N}` sends full N levels each time
