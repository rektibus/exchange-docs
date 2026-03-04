# Gopax WebSocket API

Source: https://gopax.github.io/API + local gopax.md (2026-03-04)

## Connection
- Endpoint: `wss://wsapi.gopax.co.kr`
- Auth: apiKey, timestamp, signature as query string params
- Public APIs (orderbook, tickers) work without auth — just connect without query string
- Primus heartbeat: server sends `"primus::ping::TIMESTAMP"`, client replies `"primus::pong::TIMESTAMP"` within 30s
- Max 24h connection age
- Max 20 concurrent connections per API key
- Rate limit: max 20 connection attempts/s

## Subscribe Commands

### SubscribeToTradingPair (PUBLIC — gives trades + orderbook)
```json
{"n": "SubscribeToTradingPair", "o": {"tradingPairName": "BTC-KRW"}}
```
Response: initial orderbook snapshot, then `OrderBookEvent` deltas + `PublicTradeEvent` pushes.

### SubscribeToOrderBook (PUBLIC — orderbook only)
```json
{"n": "SubscribeToOrderBook", "o": {"tradingPairName": "BTC-KRW"}}
```

### SubscribeToTickers (PUBLIC — all tickers)
```json
{"n": "SubscribeToTickers", "o": {}}
```

## Message Formats

### PublicTradeEvent (from SubscribeToTradingPair)
```json
{
  "i": -1,
  "n": "PublicTradeEvent",
  "o": {
    "tradeId": 75021,
    "baseAmount": 0.01,
    "quoteAmount": 1,
    "price": 100,
    "isBuy": true,
    "occurredAt": 1609756772,
    "tradingPairName": "BCH-KRW"
  }
}
```
| Field | Type | Description |
|-------|------|-------------|
| tradeId | int | Public trade ID |
| baseAmount | number | Filled base asset amount |
| quoteAmount | number | Filled quote asset amount |
| price | number | Trade price |
| isBuy | boolean | true=buy, false=sell |
| occurredAt | int | Unix timestamp (seconds) |
| tradingPairName | string | Trading pair name |

### OrderBookEvent (delta from SubscribeToTradingPair/OrderBook)
```json
{
  "i": -1,
  "n": "OrderBookEvent",
  "o": {
    "ask": [{"entryId": 51, "price": 5000000, "volume": 0, "updatedAt": 1599089169.282}],
    "bid": [{"entryId": 52, "price": 4500000, "volume": 1.3, "updatedAt": 1599089169.282}],
    "tradingPairName": "BCH-KRW"
  }
}
```
| Field | Type | Description |
|-------|------|-------------|
| entryId | int | Order book entry sequence |
| price | number | Price level |
| volume | number | Volume (0 = remove entry) |
| updatedAt | number | Last update time (float seconds) |

## REST Public Trade Format
GET /trading-pairs/<TradingPair>/trades
```json
[{"time": "2020-09-25T11:10:29.000Z", "date": 1601032229, "id": 21876490, "price": 12353000, "amount": 0.2951, "side": "sell"}]
```

## REST Order Book Format
GET /trading-pairs/<TradingPair>/book
```json
{"sequence": 110815766, "ask": [["seq", price, volume, "lastUpdateTs"]], "bid": [...]}
```
