# Kraken Futures API Reference

## WebSocket API

**Endpoint**: `wss://futures.kraken.com/ws/v1`

---

### Book Feed

**Feed**: `book`

```json
{"event": "subscribe", "feed": "book", "product_ids": ["PI_XBTUSD"]}
```

**Snapshot** (`feed: "book_snapshot"`):

| Field | Type | Description |
|-------|------|-------------|
| product_id | string | Symbol |
| seq | integer | Sequence number |
| timestamp | integer | ms |
| bids | list | `[{qty, price}, ...]` |
| asks | list | `[{qty, price}, ...]` |

**Delta** (`feed: "book"`):

| Field | Type | Description |
|-------|------|-------------|
| product_id | string | Symbol |
| seq | integer | Sequence number |
| timestamp | integer | ms |
| side | string | Side of entry |
| price | float | Price |
| qty | float | Quantity |

---

### Trade Feed

**Feed**: `trade`

```json
{"event": "subscribe", "feed": "trade", "product_ids": ["PI_XBTUSD"]}
```

**Snapshot** (`feed: "trade_snapshot"`): `{trades: [delta fields...]}`

**Delta** (`feed: "trade"`):

| Field | Type | Description |
|-------|------|-------------|
| product_id | string | Symbol |
| uid | string | Unique trade ID |
| side | string | `buy` or `sell` |
| type | string | `fill`, `liquidation`, `termination`, `block` |
| seq | integer | Sequence number |
| time | integer | **ms** |
| qty | float | Quantity |
| price | float | Price |

> **Note**: `type: "liquidation"` — liquidations come from the trade feed, no separate liquidation channel needed.

---

### Heartbeat Feed

**Feed**: `heartbeat`

```json
{"event": "subscribe", "feed": "heartbeat"}
```

Response: `{feed: "heartbeat", time: <ms>}`

---

### Event Types

| Event | Description |
|-------|-------------|
| `subscribed` | Subscription success |
| `subscribed_failed` | Subscription failure |
| `unsubscribed` | Unsubscription success |
| `info` | Server info on connect |
| `pong` | Ping response |
| `error` | Error: `Invalid product id`, `Invalid feed`, `Json Error` |
| `alert` | Undocumented — seen with `"message": "Bad websocket message"` |

---

## REST API

**Base URL**: `https://futures.kraken.com/derivatives/api/v3`

---

### Get Trade History

`GET /history?symbol=PI_XBTUSD&lastTime=<ISO8601>`

Returns most recent 100 trades prior to `lastTime` (up to 7 days or last engine restart).

**Response** (`history[]`):

| Field | Type | Description |
|-------|------|-------------|
| price | number | Fill price |
| side | string | `buy` or `sell` |
| size | string | Fill size (**NOTE: string, not number. And `size` not `qty`**) |
| time | string | ISO8601 timestamp |
| trade_id | integer | Continuous index per contract maturity |
| type | string | `fill`, `liquidation`, `assignment`, `termination`, `block` |
| uid | string | Unique ID |

> **WS uses `qty` (float), REST uses `size` (string)** — different field names for quantity.

---

### Get Orderbook

`GET /orderbook?symbol=PI_XBTUSD`

**Response** (`orderBook`):

| Field | Type | Description |
|-------|------|-------------|
| asks | array | `[[price, size], ...]` sorted ascending |
| bids | array | `[[price, size], ...]` sorted descending |

---

### Get Tickers

`GET /tickers`

Returns all instruments. Key fields for perps:

| Field | Type | Description |
|-------|------|-------------|
| symbol | string | e.g. `PF_BTCUSD` |
| last | number | Last fill price |
| bid / ask | number | Best bid/ask |
| bidSize / askSize | number | Best bid/ask size |
| vol24h | number | 24h volume (contracts) |
| volumeQuote | number | 24h volume (quote) |
| openInterest | number | Open interest |
| fundingRate | number | Current absolute funding rate |
| fundingRatePrediction | number | Estimated next funding rate |
| markPrice | number | Mark price |
| pair | string | e.g. `BTC:USD` |
| suspended | boolean | Market suspended |

---

### Get Historical Funding Rates

`GET /historical-funding-rates?symbol=PF_XBTUSD`

Returns historical funding rates sorted ascending by timestamp.

**Response** (`rates[]`):

| Field | Type | Description |
|-------|------|-------------|
| fundingRate | double | Absolute funding rate |
| relativeFundingRate | double | Relative funding rate |
| timestamp | datetime | Start of period (ISO8601) |

---

### Get Instruments

`GET /instruments`

Key fields:

| Field | Type | Description |
|-------|------|-------------|
| symbol | string | e.g. `PF_BTCUSD` |
| pair | string | e.g. `BTC:USD` |
| tradeable | boolean | Can be traded |
| type | string | `flexible_futures`, `futures_inverse`, `futures_vanilla` |
| tickSize | number | Tick size |
| contractSize | number | Contract size |
| maxPositionSize | number | Max position |
