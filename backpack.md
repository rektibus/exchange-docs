# Backpack Exchange API Reference
Source: https://docs.backpack.exchange/

## REST API

Base URL: `https://api.backpack.exchange`

### Products
`GET /api/v1/markets`
Response: bare array `[{symbol, baseSymbol, quoteSymbol, marketType, filters, orderBookState, visible, ...}]`

Key fields:
| Field | Example | Description |
|-------|---------|-------------|
| symbol | "BTC_USDC" / "BTC_USDC_PERP" | Market symbol |
| baseSymbol | "BTC" | Base asset |
| quoteSymbol | "USDC" | Quote asset (always USDC) |
| marketType | "SPOT" / "PERP" | Market type |
| orderBookState | "Open" / "Closed" / "PostOnly" | Trading state |
| visible | true/false | Visibility |
| filters.price.tickSize | "0.1" | Price tick size |
| filters.quantity.stepSize | "0.00001" | Quantity step size |
| fundingInterval | 3600000 | Funding interval ms (perps only, null for spot) |

Note: Spot and perp markets are returned in the same endpoint. Filter by `marketType` or symbol suffix `_PERP`.

### Trades (Spot)
`GET /api/v1/trades?symbol=BTC_USDC&limit=1000`
Response: bare array
```json
[{
  "id": 12128634,
  "isBuyerMaker": true,
  "price": "68118.6",
  "quantity": "0.00276",
  "quoteQuantity": "188.007336",
  "timestamp": 1771334928175
}]
```
- Prices/quantities are strings
- `timestamp` is milliseconds
- `isBuyerMaker`: true = sell, false = buy
- Max limit: 1000

### Trades (Futures)
Same endpoint, same format. Use perp symbol: `?symbol=BTC_USDC_PERP`

### Depth (Orderbook Snapshot)
`GET /api/v1/depth?symbol=BTC_USDC&limit=1000`
Response:
```json
{
  "asks": [["68060.2", "0.14883"], ...],
  "bids": [["68052.9", "0.03673"], ...],
  "lastUpdateId": "2462652442",
  "timestamp": 1771335032038653
}
```
- Levels are `[price_string, quantity_string]`
- `timestamp` is microseconds
- Works for both spot and perp symbols

### Funding Rates
`GET /api/v1/fundingRates?symbol=BTC_USDC_PERP`
Response: bare array (most recent first)
```json
[{
  "fundingRate": "0.0000125",
  "intervalEndTimestamp": "2026-02-17T14:00:00",
  "symbol": "BTC_USDC_PERP"
}]
```
- `fundingRate` is string
- `intervalEndTimestamp` is ISO 8601 string
- Returns ~100 recent funding intervals (hourly)

### Open Interest
`GET /api/v1/openInterest?symbol=BTC_USDC_PERP`
Response: bare array (single element)
```json
[{
  "openInterest": "1380.05922",
  "symbol": "BTC_USDC_PERP",
  "timestamp": 1771334969314
}]
```
- `openInterest` is string (in base asset units)
- `timestamp` is milliseconds

## WebSocket API

Base URL: `wss://ws.backpack.exchange`

### Message Format
All messages are wrapped:
```json
{
  "data": { ... },
  "stream": "trade.BTC_USDC"
}
```
- `stream` field is the discriminator: `trade.SYMBOL`, `depth.SYMBOL`, `ticker.SYMBOL`, `bookTicker.SYMBOL`, `kline.INTERVAL.SYMBOL`
- All data fields are inside `data` object

### Subscribe/Unsubscribe
```json
{"method": "SUBSCRIBE", "params": ["trade.BTC_USDC", "depth.BTC_USDC"]}
{"method": "UNSUBSCRIBE", "params": ["trade.BTC_USDC"]}
```
Ack response: `{"result": null, "id": 1}` (or no `id` field)

### WS Trade
Stream: `trade.SYMBOL`
```json
{
  "data": {
    "E": "1754601477746429",
    "T": "1754601477744000",
    "a": "5121860761",
    "b": "5121861755",
    "e": "trade",
    "m": false,
    "p": "3870.25",
    "q": "0.0008",
    "s": "ETH_USDC_PERP",
    "t": 10782547
  },
  "stream": "trade.ETH_USDC_PERP"
}
```
| Field | Description |
|-------|-------------|
| E | Event time (microseconds) |
| T | Trade time (microseconds) |
| s | Symbol |
| p | Price (string) |
| q | Quantity (string) |
| m | Is buyer maker (bool) |
| t | Trade ID (int) |
| a | Ask order ID |
| b | Bid order ID |

### WS Depth (Delta)
Stream: `depth.SYMBOL`
```json
{
  "data": {
    "E": "1754903057555305",
    "T": "1754903057554352",
    "U": 1345937436,
    "a": [],
    "b": [],
    "e": "depth",
    "s": "ETH_USDC",
    "u": 1345937436
  },
  "stream": "depth.ETH_USDC"
}
```
| Field | Description |
|-------|-------------|
| E | Event time (microseconds) |
| T | Transaction time (microseconds) |
| s | Symbol |
| b | Bids `[[price, qty], ...]` |
| a | Asks `[[price, qty], ...]` |
| U | First update ID |
| u | Last update ID |

- These are DELTA updates, not snapshots
- `is_snapshot: false` — must fetch REST snapshot first
- Price/qty are strings

### WS Ticker
Stream: `ticker.SYMBOL`
```json
{
  "data": {
    "E": "1754176123312507",
    "V": "19419526.742584",
    "c": "3398.57",
    "e": "ticker",
    "h": "3536.65",
    "l": "3371.8",
    "n": 17152,
    "o": "3475.45",
    "s": "ETH_USDC",
    "v": "5573.5827"
  },
  "stream": "bookTicker.ETH_USDC"
}
```

### WS Book Ticker (BBO)
Stream: `bookTicker.SYMBOL`
```json
{
  "data": {
    "A": "0.4087",
    "B": "0.0020",
    "E": "1754517402450016",
    "T": "1754517402449064",
    "a": "3667.50",
    "b": "3667.49",
    "e": "bookTicker",
    "s": "ETH_USDC",
    "u": 1328288557
  },
  "stream": "bookTicker.ETH_USDC"
}
```

## Key Notes
- ALL timestamps in WS are **microseconds** (divide by 1000 for ms)
- REST trade timestamps are **milliseconds**
- REST depth timestamp is **microseconds**
- All prices/quantities are strings in both WS and REST
- Single WS endpoint serves both spot and perp data (same symbols)
- Symbols use underscore separator: `BTC_USDC`, `BTC_USDC_PERP`
- No WS funding or OI streams — REST polling only
- Ping: native WebSocket ping/pong
- Max streams per connection: not documented, tested with 50
