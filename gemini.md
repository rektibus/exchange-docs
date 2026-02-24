# Gemini API Documentation

Source: https://docs.gemini.com/rest-api/ and https://docs.gemini.com/websocket/

## REST API — Market Data (v1.0.0)

Base URL: `https://api.gemini.com`

### List Symbols
`GET /v1/symbols`

Returns an array of all available symbols for trading (flat strings).

```json
["btcusd", "ethbtc", "ethusd", ...]
```

---

### Get Symbol Details
`GET /v1/symbols/details/:symbol`

Returns detail on supported symbols: minimum order size, tick size, quote increment, product type.

**Path Parameters:**
- `symbol` — Trading pair symbol (e.g. `BTCUSD`)

**Response:**
| Field | Description |
|-------|-------------|
| `symbol` | The requested symbol |
| `base_currency` | CCY1 (e.g. BTC in BTCUSD) |
| `quote_currency` | CCY2 (e.g. USD in BTCUSD) |
| `tick_size` | Decimal places in base_currency (e.g. 1e-8) |
| `quote_increment` | Decimal places in quote_currency (e.g. 0.01) |
| `min_order_size` | Minimum order size in base_currency units |
| `status` | `open`, `closed`, `cancel_only`, `post_only`, `limit_only` |
| `wrap_enabled` | Whether symbol can be wrapped |
| `product_type` | `spot` or `swap` (swap = perpetual swap) |
| `contract_type` | `vanilla` (spot), `linear` (perp), `inverse` (inverse perp) |
| `contract_price_currency` | Quote currency or collateral currency for perps |

```json
{
  "symbol": "BTCUSD",
  "base_currency": "BTC",
  "quote_currency": "USD",
  "tick_size": 1e-8,
  "quote_increment": 0.01,
  "min_order_size": "0.00001",
  "status": "open",
  "wrap_enabled": false,
  "product_type": "spot",
  "contract_type": "vanilla",
  "contract_price_currency": "USD"
}
```

---

### Get Ticker (v1)
`GET /v1/pubticker/:symbol`

**Response:**
| Field | Description |
|-------|-------------|
| `bid` | Highest bid currently available |
| `ask` | Lowest ask currently available |
| `last` | Price of last executed trade |
| `volume` | Object with 24h volume: `{BTC: "...", USD: "...", timestamp: ...}` |

---

### Get Ticker V2
`GET /v2/ticker/:symbol`

Returns recent trading activity (recommended over v1).

**Response:**
| Field | Description |
|-------|-------------|
| `symbol` | Trading pair symbol |
| `open` | Open price from 24 hours ago |
| `high` | High price from 24 hours ago |
| `low` | Low price from 24 hours ago |
| `close` | Close price (most recent trade) |
| `changes` | Hourly prices descending for past 24 hours |
| `bid` | Current best bid |
| `ask` | Current best offer |

**Note: No OI (open interest) field in ticker.**

---

### Get Current Order Book
`GET /v1/book/:symbol`

Returns the current order book as two arrays (bids/asks). Quantities and prices are **strings** (exact, not rounded).

**Query Parameters:**
| Param | Description |
|-------|-------------|
| `limit_bids` | Limit bid levels returned. Default 50. May be 0 for full book. |
| `limit_asks` | Limit ask levels returned. Default 50. May be 0 for full book. |

**Response:**
```json
{
  "bids": [{"price": "3607.85", "amount": "6.643373", "timestamp": "1547147541"}],
  "asks": [{"price": "3607.86", "amount": "14.68205084", "timestamp": "1547147541"}]
}
```

---

### List Trades
`GET /v1/trades/:symbol`

Returns trades executed since the specified timestamp. Max 500 records per request.

**Query Parameters:**
| Param | Description |
|-------|-------------|
| `timestamp` | Only return trades after this timestamp (seconds or ms). **90-day hard limit.** |
| `since` | Alias for `timestamp`. Milliseconds. |
| `since_tid` | Only return trades after this trade ID. Trumps `timestamp`. Set to 0 for earliest. |
| `limit_trades` | Max trades to return. Default 50, max 500. |
| `include_breaks` | Show broken trades. Default false. Can be `1` or `true`. |

**Response:** Array sorted by timestamp, newest first.
| Field | Description |
|-------|-------------|
| `timestamp` | Unix timestamp (seconds) |
| `timestampms` | Unix timestamp (milliseconds) |
| `tid` | Trade ID number |
| `price` | Execution price (string) |
| `amount` | Amount traded (string) |
| `exchange` | Always "gemini" |
| `type` | `buy` (ask removed by incoming buy) or `sell` (bid removed by incoming sell) |

```json
{
  "timestamp": 1547146811,
  "timestampms": 1547146811357,
  "tid": 5335307668,
  "price": "3610.85",
  "amount": "0.27413495",
  "exchange": "gemini",
  "type": "buy"
}
```

---

### List Prices
`GET /v2/ticker/:symbol`

Hourly prices (same as Ticker V2).

---

### Get Funding Amount (Perpetuals only)
`GET /v1/fundingamount/:symbol`

Returns the current funding amount for a perpetual pair.

**Response:**
| Field | Description |
|-------|-------------|
| `symbol` | e.g. `btcgusdperp` |
| `fundingDateTime` | UTC datetime `yyyy-MM-ddThh:mm:ss.SSSZ` |
| `fundingTimestampMilliSecs` | Current funding epoch time (ms) |
| `nextFundingTimestamp` | Next funding epoch time (ms) |
| `fundingAmount` | Dollar amount for Long 1 position held for funding period (1 hour) |
| `estimatedFundingAmount` | Estimated dollar amount for next funding period |

```json
{
  "symbol": "btcgusdperp",
  "fundingDateTime": "2025-04-22T18:00:00.000Z",
  "fundingTimestampMilliSecs": 1745344800000,
  "nextFundingTimestamp": 1745348400000,
  "fundingAmount": -1.50991,
  "estimatedFundingAmount": -2.10595
}
```

**Note:** `fundingAmount` is a DOLLAR AMOUNT, not a rate. Positive = longs pay, negative = shorts pay.

---

### Get Funding Amount Report File (Perpetuals only)
`GET /v1/fundingamountreport/records.xlsx`

Returns historical funding amounts as Excel/CSV.

**Query Parameters:**
| Param | Description |
|-------|-------------|
| `symbol` | e.g. `BTCGUSDPERP` |
| `fromDate` | Start date (mandatory if `toDate` specified) |
| `toDate` | End date (mandatory if `fromDate` specified) |
| `numRows` | Max records. Default 8760. |

**Examples:**
- `?symbol=BTCGUSDPERP&numRows=1000` — Fetch max 1000 records from now backwards
- `?symbol=BTCGUSDPERP&fromDate=2024-04-10&toDate=2024-04-25` — Date range
- `?symbol=BTCGUSDPERP` — Fetch max 8760 records from now backwards

---

### List Candles (Spot)
`GET /v2/candles/:symbol/:time_frame`

**Time frames:** `1m`, `5m`, `15m`, `30m`, `1hr`, `6hr`, `1day`

**Response:** Array of arrays `[timestamp_ms, open, high, low, close, volume]`

---

### List Derivative Candles (Perpetuals only)
`GET /v2/derivatives/candles/:symbol/:time_frame`

**Time frames:** `1m` (only!)

**Response:** Array of arrays `[timestamp_ms, open, high, low, close, volume]`

---

### FX Rate
`GET /v1/fxrate/:symbol/:fiat_currency`

Returns FX rate for a given symbol and fiat currency.

---

### List Fee Promos
`GET /v1/feepromos`

Returns current fee promotions.

---

### Get Network
`GET /v1/network/:token`

Returns network/transfer details for a given token.

---

## REST API — NOT Available (confirmed)

| Endpoint | Status |
|----------|--------|
| Open Interest | **No public endpoint.** `/v1/openinterest/:symbol` returns `EndpointNotFound`. |
| Liquidations | **No public endpoint.** No documentation reference. |
| Long/Short Ratio | **No public endpoint.** No documentation reference. |
| Historical Funding | Only via `/v1/fundingamountreport/records.xlsx` (Excel/CSV download, not JSON). |

---

## WebSocket API — Market Data v1

### Connection
`wss://api.gemini.com/v1/marketdata/:symbol`

One connection per symbol (per-symbol URL pattern).

**URL Parameters:**
| Param | Default | Description |
|-------|---------|-------------|
| `heartbeat` | false | Receive `{"type":"heartbeat"}` every 5 seconds |
| `top_of_book` | false | Only top of book (best bid/offer) instead of full depth |
| `bids` | true | Include bid changes in update events |
| `offers` | true | Include ask/offer changes in update events |
| `trades` | false | Include trade events |

If no filtering params, all entry types appear.

### Message Types

**All messages have:**
| Field | Description |
|-------|-------------|
| `type` | `heartbeat` or `update` |
| `socket_sequence` | Zero-indexed, monotonically increasing. Gaps = missed messages. |

### Update Message Structure
```json
{
  "type": "update",
  "eventId": 123456789,
  "timestamp": 1547146811,
  "timestampms": 1547146811357,
  "socket_sequence": 42,
  "events": [...]
}
```

`timestampms` is on the **envelope**, NOT inside individual events.

### Trade Events
```json
{
  "type": "trade",
  "tid": 5335307668,
  "price": "3610.85",
  "amount": "0.27413495",
  "makerSide": "ask"
}
```

| Field | Description |
|-------|-------------|
| `type` | Always `"trade"` |
| `tid` | Trade ID |
| `price` | Execution price (string) |
| `amount` | Amount traded (string) |
| `makerSide` | `"ask"` (taker bought → buy) or `"bid"` (taker sold → sell) |

**Every trade triggers both `trade` and `change` events in the same message.**

### Change (Depth) Events
```json
{
  "type": "change",
  "price": "66630.53",
  "side": "ask",
  "reason": "initial",
  "remaining": "0.01789306",
  "delta": "0.01789306"
}
```

| Field | Description |
|-------|-------------|
| `type` | Always `"change"` |
| `price` | Price level (string) |
| `side` | `"bid"` or `"ask"` |
| `reason` | `"initial"`, `"place"`, `"trade"`, `"cancel"` |
| `remaining` | Quantity remaining at price after change. Zero = level removed. |
| `delta` | Quantity changed. Negative if filled/canceled. For `initial`, delta = remaining. |

### Depth Behavior (CRITICAL)

**Initial message** (first after connect): Contains ALL `change` events with `reason: "initial"` — this IS the full order book snapshot. Observed ~5228 events in first message.

**Subsequent messages**: Individual `change` events with `reason: "place"`, `"trade"`, `"cancel"` — these are DELTAS.

**Classification**: The channel sends **snapshot first, then deltas** → `is_snapshot: false` (delta mode). REST `depth_snapshot_endpoint` required for initial load.

---

## WebSocket API — Fast API (v0.10.7)

URL: `wss://wsapi.fast.gemini.com`
Status: Production Beta

Low-latency (sub-10ms) unified market data + trading. Requires special API key with time-based nonce. Not used by EnsoX (we use v1 marketdata).

**Performance Tiers:**
| Tier | Latency | Description |
|------|---------|-------------|
| Tier 2 (Public Internet) | p99~15ms | Public, connects to AWS us-east-1 |
| Tier 1 (In Region) | p99~10ms | Direct us-east-1 connection |
| Tier 0 (Local Zone) | p99~5ms | Closest to data center |

---

## Summary — Available Data for EnsoX

| Data Type | Spot | Futures | Source |
|-----------|------|---------|--------|
| **Trades** | ✅ WS + REST | ✅ WS + REST | WS: events, REST: `/v1/trades/:symbol` |
| **Depth** | ✅ WS + REST | ✅ WS + REST | WS: change events, REST: `/v1/book/:symbol` |
| **Funding** | — | ✅ REST | `/v1/fundingamount/:symbol` |
| **OI** | — | ❌ | No public endpoint |
| **Liquidations** | — | ❌ | No public endpoint |
| **LS Ratio** | — | ❌ | No public endpoint |
| **Historical Funding** | — | ⚠️ Excel only | `/v1/fundingamountreport/records.xlsx` (not JSON) |