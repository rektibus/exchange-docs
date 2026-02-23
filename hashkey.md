# HashKey Global API Documentation (Reference)

## Endpoints

- **REST Base URL**: `https://api-glb.hashkey.com`
- **WebSocket URL**: `wss://stream-glb.hashkey.com/quote/ws/v2`

## 1. Market Data (REST)

### Exchange Information (Products)
- **Endpoint**: `GET /api/v1/exchangeInfo`
- **Fields**:
  - `symbols`: Array of products
  - `symbol`: e.g. `BTCUSDT` (Spot), `BTCUSDT-PERPETUAL` (Futures)
  - `baseAsset`, `quoteAsset`
  - `filters`: `PRICE_FILTER` (`tickSize`), `LOT_SIZE` (`stepSize`)

### Recent Trades
- **Endpoint**: `GET /quote/v1/trades`
- **Params**: `symbol` (e.g. `BTCUSDT`), `limit` (max 100)
- **Fields**:
  - `t`: Timestamp (ms)
  - `p`: Price
  - `q`: Quantity
  - `ibm`: Is buyer maker (Boolean)

### Order Book
- **Endpoint**: `GET /quote/v1/depth`
- **Params**: `symbol`, `limit` (max 200)
- **Fields**:
  - `t`: Timestamp (ms)
  - `b`: Bids `[[p, q]]`
  - `a`: Asks `[[p, q]]`

### Funding Rate
- **Current**: `GET /api/v1/futures/fundingRate`
- **History**: `GET /api/v1/futures/historyFundingRate`
- **Params**: `symbol`, `limit` (max 1000 for history)
- **Fields**:
  - `fundingRate`: Rate
  - `fundingTime`: Timestamp (ms)

## 2. WebSocket Streams (v2)

- **Subscription Format**:
```json
{
  "symbol": "BTCUSDT",
  "topic": "topic_name",
  "event": "sub",
  "params": {
    "binary": false
  }
}
```

### Trade Stream
- **Topic**: `trade`
- **Fields**:
  - `t`: Timestamp (ms)
  - `p`: Price
  - `q`: Quantity
  - `m`: Is buyer maker (Boolean)

### Depth Stream
- **Topic**: `depth`
- **Fields**:
  - `t`: Timestamp (ms)
  - `b`: Bids `[[p, q]]`
  - `a`: Asks `[[p, q]]`

## 3. General Notes
- **Timestamps**: Milliseconds (Unix epoch)
- **Symbol Formats**:
  - Spot: `BTCUSDT`
  - Futures: `BTCUSDT-PERPETUAL`
- **Rate Limits**: 10 requests per second for public endpoints (estimated).
