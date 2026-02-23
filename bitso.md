# Bitso Trading API Documentation

Source: https://docs.bitso.com

## REST API
Base URL: `https://api.bitso.com`

### List Available Books
**GET** `/v3/available_books`

Returns a JSON array of available exchange order books. Each element contains:
- `book` — Order book symbol (e.g. `btc_mxn`)
- `default_chart` — Default chart type
- `fees` — Fee structure with `flat_rate` (maker/taker) and `structure` (volume tiers)
- `margin_enabled` — Whether margin trading is enabled
- `minimum_amount`, `maximum_amount` — Order size limits
- `minimum_price`, `maximum_price` — Price limits
- `minimum_value`, `maximum_value` — Value limits
- `tick_size` — Minimum price increment

### Get Ticker
**GET** `/v3/ticker?book={{symbol}}`

### List Order Book
**GET** `/v3/order_book?book={{symbol}}`

### List Trades (History)
**GET** `/v3/trades?book={{symbol}}`

Query Parameters:
- `book` (required) — Specifies which book to use
- `limit` — Number of trades to return
- `marker` — Pagination marker
- `sort` — Sort direction (`asc` or `desc`)

Response payload is a descending JSON array of transactions:
- `amount` — Trade amount (String)
- `book` — Book symbol
- `created_at` — Timestamp (ISO 8601)
- `maker_side` — Side of the maker (`buy` or `sell`)
- `price` — Trade price (String)
- `tid` — Trade ID (Number)

Example response:
```json
{
  "success": true,
  "payload": [{
    "book": "btc_mxn",
    "created_at": "2016-04-08T17:52:31.000+00:00",
    "amount": "0.02000000",
    "maker_side": "buy",
    "price": "5545.01",
    "tid": 55845
  }]
}
```

## WebSocket API
Endpoint: `wss://ws.bitso.com`

### Available Channels
- **Trades Channel** — Sends a message whenever a new trade executes
- **Orders Channel** — Top 20 asks and bids, updates on change
- **Diff-Orders Channel** — All order book modifications (state changes, new orders)

### Subscription
```json
{
  "action": "subscribe",
  "book": "btc_mxn",
  "type": "trades"
}
```

Server acknowledgment:
```json
{"action": "subscribe", "response": "ok", "time": 1455831538045, "type": "trades"}
```

### Keep-Alive Messages
```json
{"type": "ka"}
```

### Trades Channel Message Format
```json
{
  "type": "trades",
  "book": "btc_mxn",
  "payload": [{
    "i": 77777,
    "a": "0.0035",
    "r": "7190",
    "v": "25.16",
    "mo": "laasdqw1ywYgfYI2",
    "to": "asADW123wedwqeYk",
    "t": 0,
    "x": 1675555546102
  }],
  "sent": 1675555546102
}
```

Field descriptions:
- `a` — Amount (String, Major currency)
- `i` — Trade ID (Number)
- `mo` — Maker Order ID (String)
- `r` — Rate/Price (String, Minor currency)
- `t` — Taker side: 0=buy, 1=sell (Number)
- `to` — Taker Order ID (String)
- `v` — Value (String, Minor currency)
- `x` — Creation timestamp (Number, Milliseconds)

### Message Fields (All Channels)
- `type` — Channel name
- `book` — Order book
- `payload` — Data
- `sent` — Broadcast timestamp (ms)
- `sequence` — (Diff-Orders only) Increasing integer
