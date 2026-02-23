# Luno API Documentation

## Market Data

### Get Full Order Book
Returns all bids and asks for the currency pair specified.

**Endpoint**: `GET /api/1/orderbook_top` (Note: snippet says orderbook full but path usually implies structure)
Actually, the snippet says: `https://www.luno.com/en/developers/api#tag/Market/operation/GetOrderBookFull`
Warning: This may return a large amount of data.

Response format:
```json
{
  "bids": [...],
  "asks": [...]
}
```

### Get Ticker
Returns the latest ticker indicators for the specified currency pair.

### List Trades
Returns a list of recent trades.
Query parameters:
- `pair`: Currency pair
- `since`: Unix timestamp in milliseconds

## Streaming API (Websockets)

**Endpoint**: `wss://ws.luno.com/api/1/stream/:pair`

### Protocol
The client state consists of:
- sequence number
- set of bid orders
- set of ask orders
- list of trades
- market status

### Messages

**Initial Message** (Order Book Snapshot):
```json
{
  "sequence": "24352",
  "asks": [{ "id": "...", "price": "...", "volume": "..." }],
  "bids": [...],
  "status": "ACTIVE",
  "timestamp": 1528884331021
}
```

**Update Message**:
```json
{
  "sequence": "24353",
  "trade_updates": [],
  "create_update": null,
  "delete_update": null,
  "status_update": null,
  "timestamp": 1469031991
}
```

**Updates Types**:
- `Create`: Add order
- `Delete`: Remove order
- `Trade`: Reduce volume and append trade
- `Status`: Change market status

**Authentication**:
Must send credentials first:
```json
{ "api_key_id": "...", "api_key_secret": "..." }
```
