# Bitfinex V2 API — Field Reference (EnsoX)

> Source: [Bitfinex API V2 Docs](https://docs.bitfinex.com/reference)
> Probed: 2026-02-17

## Symbol Format

| Context | Format | Example | Note |
|---------|--------|---------|------|
| **Spot pairs** | Concatenated (6-char) or colon-separated | `BTCUSD`, `AAVE:USD`, `AVAX:BTC` | No `t` prefix in pair name |
| **Futures pairs** | `{BASE}F0:{QUOTE}F0` | `BTCF0:USTF0`, `ETHF0:USTF0` | `UST` = USDT in Bitfinex notation |
| **WS subscribe** | Prepend `t` to pair | `tBTCUSD`, `tBTCF0:USTF0` | Always uppercase |
| **WS subscribed response** | `pair` field = raw pair (no `t`) | `BTCUSD`, `BTCF0:USTF0` | Used for chanId→symbol mapping |
| **REST trades URL** | `/v2/trades/t{PAIR}/hist` | `/v2/trades/tBTCUSD/hist` | Prepend `t` |
| **REST status URL** | `/v2/status/deriv?keys=t{PAIR}` | `?keys=tBTCF0:USTF0` | Prepend `t` |

### Bitfinex Quote Currency Mapping
| Bitfinex | Canonical |
|----------|-----------|
| `USD` | USD |
| `UST` | USDT |
| `BTC` | BTC |
| `EUR` | EUR |
| `GBP` | GBP |
| `JPY` | JPY |

### Base/Quote Extraction (Spot)

Spot pairs come in **two formats** from `/v2/conf/pub:list:pair:exchange`:
- **6-char concatenated**: `BTCUSD` → base=`BTC`, quote=`USD` (3+3 chars)
- **Colon-separated**: `AAVE:USD` → base=`AAVE`, quote=`USD`

There is **no universal delimiter**. The colon is present for >3 char bases, absent for 3-char bases.
CCXT handles this by maintaining a currency list and trying splits.

### Base/Quote Extraction (Futures)

Futures pairs from `/v2/conf/pub:list:pair:futures`:
- Format: `BTCF0:USTF0` — always colon-separated
- Strip `F0` suffix from both parts: `BTC` + `UST`
- Map `UST` → `USDT`

Normalization config: `{"replace": {"F0": ""}}` handles the F0 stripping.

---

## Products Endpoints

| Type | Endpoint | Response |
|------|----------|----------|
| **Spot pairs** | `/v2/conf/pub:list:pair:exchange` | `[["BTCUSD", "AAVE:USD", ...]]` |
| **Futures pairs** | `/v2/conf/pub:list:pair:futures` | `[["BTCF0:USTF0", ...]]` |
| **All symbols** | `/v2/conf/pub:list:pair` | Combined |

Response is `[[...]]` — array of one array. Use `products_json_path: "$"` to unwrap outer array.

> ⚠️ These are flat string arrays, NOT objects. No `baseCoin`/`quoteCoin` fields.
> Base/quote must be parsed from the pair string itself.

### Configs Endpoint `/v2/conf/pub:{Action}:{Object}:{Detail}`

Flexible endpoint for platform configuration data. Supports multi-requests (comma-separated, no spaces).

**Listing Requests** (products):

| Request | Description | Our Use |
|---------|-------------|---------|
| `pub:list:pair:exchange` | Spot trading pairs | ✅ Spot products |
| `pub:list:pair:futures` | Derivative pairs | ✅ Futures products |
| `pub:list:pair:margin` | Margin trading pairs | — |
| `pub:list:currency` | All currencies | — |

**Mapping Requests** (metadata):

| Request | Description | Our Use |
|---------|-------------|---------|
| `pub:map:currency:undl` | Derivatives → underlying (e.g. `BTCF0` → `BTC`) | Useful for base extraction |
| `pub:map:currency:label` | Symbol → friendly name (e.g. `BTC` → `Bitcoin`) | — |
| `pub:map:currency:sym` | API symbol mapping (e.g. `DSH` → `DASH`) | — |
| `pub:map:currency:pool` | Symbol → network (e.g. `BAT` → `ETH`) | — |

**Info Requests**:

| Request | Description |
|---------|-------------|
| `pub:info:pair` | Per-pair info: `[PAIR, [...MIN_ORDER_SIZE, MAX_ORDER_SIZE...INITIAL_MARGIN, MIN_MARGIN]]` |
| `pub:info:pair:futures` | Same structure for derivatives |

**Multi-request example**: `pub:list:pair:exchange,pub:list:pair:futures` — fetches both in one call.

**Rate Limit**: 90 req/min.

---

## REST Candles `/v2/candles/trade:{timeframe}:{symbol}/hist`

> OHLCV klines. Not used by our system (we build bars from trades).
> Section must be `hist` or `last` (mandatory).

### Request
| Param | Type | Description |
|-------|------|-------------|
| `timeframe` | path | `1m`, `5m`, `15m`, `30m`, `1h`, `3h`, `6h`, `12h`, `1D`, `1W`, `14D`, `1M` |
| `symbol` | path | e.g. `tBTCUSD`, `fUSD:p30` (funding requires period) |
| `limit` | int | Max **10000** |
| `start` | int | Start timestamp (ms), inclusive |
| `end` | int | End timestamp (ms), inclusive |
| `sort` | int | `1` = ascending, `-1` = descending |

### Response
```
// hist: [[MTS, OPEN, CLOSE, HIGH, LOW, VOLUME], ...]
// last: [MTS, OPEN, CLOSE, HIGH, LOW, VOLUME]
```

| Index | Field | Type |
|-------|-------|------|
| 0 | MTS | int |
| 1 | OPEN | float |
| 2 | CLOSE | float |
| 3 | HIGH | float |
| 4 | LOW | float |
| 5 | VOLUME | float |

> ⚠️ Field order is `OCHLV` (Open, **Close**, High, Low) — NOT standard OHLCV!

**Rate Limit**: 30 req/min.

---

## REST Ticker `/v2/ticker/{symbol}`

> Real-time market snapshot for a single symbol.

### Response (Trading Pairs)
```
[
  10645,          // [0] BID
  73.94,          // [1] BID_SIZE (sum of 25 highest bids)
  10647,          // [2] ASK
  75.22,          // [3] ASK_SIZE (sum of 25 lowest asks)
  731.61,         // [4] DAILY_CHANGE
  0.0738,         // [5] DAILY_CHANGE_RELATIVE (×100 for %)
  10644.01,       // [6] LAST_PRICE
  14480.90,       // [7] VOLUME (daily)
  10766,          // [8] HIGH (daily)
  9889.14         // [9] LOW (daily)
]
```

| Index | Field | Type | Description |
|-------|-------|------|-------------|
| 0 | BID | float | Best bid price |
| 1 | BID_SIZE | float | Sum of 25 highest bid sizes |
| 2 | ASK | float | Best ask price |
| 3 | ASK_SIZE | float | Sum of 25 lowest ask sizes |
| 6 | LAST_PRICE | float | Last traded price |
| 7 | VOLUME | float | Daily volume |
| 8 | HIGH | float | Daily high |
| 9 | LOW | float | Daily low |

**Rate Limit**: 90 req/min.

> Not currently used by our system.

---

## REST Tickers History `/v2/tickers/hist`

> Hourly best bid/ask snapshots. **1 year** of history.

### Request
| Param | Type | Description |
|-------|------|-------------|
| `symbols` | string | Comma-separated list or `ALL`. e.g. `tBTCUSD,tETHUSD` |
| `limit` | int | Default **100**, max **250** |
| `start` | int | Start timestamp (ms), inclusive |
| `end` | int | End timestamp (ms), inclusive |
| `sort` | int | `1` = ascending, `-1` = descending (default) |

### Response
```
[
  [
    "tMKRF0:USTF0",  // [0]  SYMBOL
    643.57,           // [1]  BID
    null,             // [2]  —
    648.82,           // [3]  ASK
    null, null, null, null, null, null, null, null,
    1674061204000     // [12] MTS (ms)
  ],
  [...]
]
```

| Index | Field | Type | Description |
|-------|-------|------|-------------|
| 0 | SYMBOL | string | e.g. `tBTCUSD` |
| 1 | BID | float | Best bid price |
| 3 | ASK | float | Best ask price |
| 12 | MTS | int | Timestamp (ms) |

> Not currently used by our system. Funding currencies not supported.

---

## REST Trades `/v2/trades/{symbol}/hist`

### Request
| Param | Type | Description |
|-------|------|-------------|
| `symbol` | path | Required. e.g. `tBTCUSD`, `tBTCF0:USTF0`, `fUSD` |
| `limit` | int | Default **125**, max **10000** |
| `sort` | int | `1` = ascending, `-1` = descending (default: -1) |
| `start` | int | Start timestamp (ms), inclusive |
| `end` | int | End timestamp (ms), inclusive |

### Response (Trading Pairs)
```
[
  [
    388063448,       // [0] ID
    1567526214876,   // [1] MTS (ms)
    1.918524,        // [2] AMOUNT (+ = buy, - = sell)
    10682            // [3] PRICE
  ],
  [...]
]
```

> ⚠️ Field order is `[ID, MTS, AMOUNT, PRICE]` — AMOUNT before PRICE!

### Response (Funding Currencies — `fUSD`, `fBTC`)
```
[[ID, MTS, AMOUNT, RATE, PERIOD], ...]
```

| Index | Field | Type | Description |
|-------|-------|------|-------------|
| 0 | ID | int | Trade ID |
| 1 | MTS | int | Timestamp (ms) |
| 2 | AMOUNT | float | **Signed**: positive = buy, negative = sell |
| 3 | PRICE | float | Execution price (or RATE for funding) |
| 4 | PERIOD | int | *(Funding only)* Period in days |

**Side**: Derived from AMOUNT sign (`side_from_signed_qty: true`).
**Rate limit**: ⚠️ **15 req/min** (strict).

---

## REST Book `/v2/book/{symbol}/{precision}`

### Request
| Param | Type | Description |
|-------|------|-------------|
| `symbol` | path | Required. e.g. `tBTCUSD`, `tBTCF0:USTF0` |
| `precision` | path | `P0` (most granular), `P1`, `P2`, `P3`, `P4`, `R0` (raw orders) |
| `len` | query | Number of levels: `1`, `25`, `100` (default: 25) |

### Response (Trading Pairs — P0-P4)
```
[
  [
    8744.9,       // [0] PRICE
    2,            // [1] COUNT (orders at this level)
    0.45603413    // [2] AMOUNT (+ = bid, - = ask)
  ],
  [...]
]
```

### Response (Raw Books — R0)
```
[
  [
    ORDER_ID,     // [0] Order ID
    PRICE,        // [1] Price
    AMOUNT        // [2] Amount (+ = bid, - = ask)
  ],
  [...]
]
```

| Field | Type | Description |
|-------|------|-------------|
| PRICE | float | Price level |
| COUNT | int | Number of orders at that level |
| AMOUNT | float | **Signed**: positive = bid, negative = ask |

> ⚠️ Side from AMOUNT sign — same convention as WS book and trades.
> COUNT=0 is NOT used in REST snapshots (only in WS updates for level removal).

**Rate Limit**: 240 req/min.

---

## REST Derivatives Status `/v2/status/deriv?keys=t{PAIR}`

### Response
```
[
  [
    "tBTCF0:USTF0",   // [0]  KEY
    1596124822000,     // [1]  MTS (ms)
    null,              // [2]  —
    66868.07,          // [3]  DERIV_PRICE (derivative book mid)
    66836.00,          // [4]  SPOT_PRICE (underlying spot mid)
    null,              // [5]  —
    70821880.00,       // [6]  INSURANCE_FUND_BALANCE
    null,              // [7]  —
    1771344000000,     // [8]  NEXT_FUNDING_EVT_MTS
    0.00043074,        // [9]  NEXT_FUNDING_ACCRUED
    7944,              // [10] NEXT_FUNDING_STEP (counter)
    null,              // [11] —
    0.00010304,        // [12] CURRENT_FUNDING (8h rate)
    null,              // [13] —
    null,              // [14] —
    66812.90,          // [15] MARK_PRICE
    null,              // [16] —
    null,              // [17] —
    8651.43,           // [18] OPEN_INTEREST
    null,              // [19] —
    null,              // [20] —
    null,              // [21] —
    0.0005,            // [22] CLAMP_MIN
    0.0025             // [23] CLAMP_MAX
  ]
]
```

### Field Index Summary (Live)

| Index | Field | Our Use | Config Path |
|-------|-------|---------|-------------|
| **1** | MTS | Timestamp for both OI and funding | `rest_timestamp: "0.1"` |
| **9** | NEXT_FUNDING_ACCRUED | — (accumulating, not applied) | — |
| **12** | CURRENT_FUNDING | **Funding rate** (applied in current 8h) | `rest_value: "0.12"` |
| **18** | OPEN_INTEREST | **OI** (total outstanding contracts) | `rest_value: "0.18"` |

> ⚠️ Both OI and funding use the SAME endpoint. `rest_symbol_transform: "add_prefix:t"` prepends `t`.

---

## REST Derivatives Status History `/v2/status/deriv/{key}/hist`

> ⚠️ **Different URL format from live**: key is a **path param**, not query param.
> `/v2/status/deriv/tBTCF0:USTF0/hist` — NOT `/v2/status/deriv/hist?key=...`

### Request
| Param | Type | Description |
|-------|------|-------------|
| `key` | path | Required. e.g. `tBTCF0:USTF0` |
| `start` | int | Start timestamp (ms), inclusive |
| `end` | int | End timestamp (ms), inclusive |
| `limit` | int | Max **5000** |
| `sort` | int | `1` = ascending, `-1` = descending |

### Response
> ⚠️ **Indices are shifted -1 vs live** — no KEY field in history response!

```
[
  [
    1570578776000,     // [0]  MTS
    null,              // [1]  —
    8194.95,           // [2]  DERIV_PRICE
    8196.95,           // [3]  SPOT_PRICE
    null,              // [4]  —
    101120.80,         // [5]  INSURANCE_FUND_BALANCE
    null,              // [6]  —
    1570579200000,     // [7]  NEXT_FUNDING_EVT_MTS
    0.00021817,        // [8]  NEXT_FUNDING_ACCRUED
    9379,              // [9]  NEXT_FUNDING_STEP
    null,              // [10] —
    0,                 // [11] CURRENT_FUNDING
    null,              // [12] —
    null,              // [13] —
    8192.82,           // [14] MARK_PRICE
    null,              // [15] —
    null,              // [16] —
    5174.01,           // [17] OPEN_INTEREST
    null,              // [18] —
    null,              // [19] —
    null,              // [20] —
    0.0005,            // [21] CLAMP_MIN
    0.0025             // [22] CLAMP_MAX
  ],
  [...]
]
```

### Field Index Comparison: Live vs History

| Field | Live Index | History Index | Note |
|-------|-----------|---------------|------|
| KEY | 0 | — | **Not present** in history |
| MTS | 1 | **0** | |
| DERIV_PRICE | 3 | **2** | |
| SPOT_PRICE | 4 | **3** | |
| INSURANCE_FUND | 6 | **5** | |
| NEXT_FUNDING_TS | 8 | **7** | |
| NEXT_FUNDING_ACCRUED | 9 | **8** | |
| NEXT_FUNDING_STEP | 10 | **9** | |
| CURRENT_FUNDING | 12 | **11** | |
| MARK_PRICE | 15 | **14** | |
| **OPEN_INTEREST** | **18** | **17** | |
| CLAMP_MIN | 22 | **21** | |
| CLAMP_MAX | 23 | **22** | |

**Rate Limit**: 90 req/min.

---

## REST Liquidations `/v2/liquidations/hist`

### Request
| Param | Type | Description |
|-------|------|-------------|
| `start` | int | Start timestamp (ms), inclusive |
| `end` | int | End timestamp (ms), inclusive |
| `limit` | int | Max **500** |
| `sort` | int | `1` = ascending, `-1` = descending |

### Response (triple-nested)
```
[
  [
    [
      "pos",             // [0]  TYPE (always "pos")
      158793100,         // [1]  POS_ID
      1678465351520,     // [2]  MTS (ms)
      null,              // [3]  —
      "tAMPF0:USTF0",   // [4]  SYMBOL
      1e-8,              // [5]  AMOUNT (+ = long liq, - = short liq)
      1.0093,            // [6]  BASE_PRICE (entry price)
      null,              // [7]  —
      0,                 // [8]  IS_MATCH (0=initial trigger, 1=market exec)
      1,                 // [9]  IS_MARKET_SOLD (0=system acquired, 1=market sold)
      null,              // [10] —
      1.0098             // [11] PRICE_ACQUIRED (liquidation price)
    ]
  ],
  [...]
]
```

| Index | Field | Type | Description |
|-------|-------|------|-------------|
| 0 | TYPE | string | Always `"pos"` |
| 1 | POS_ID | int | Position ID |
| 2 | MTS | int | Timestamp (ms) |
| 4 | SYMBOL | string | e.g. `tBTCF0:USTF0` (with `t` prefix) |
| 5 | AMOUNT | float | Signed: positive = long liquidated, negative = short liquidated |
| 6 | BASE_PRICE | float | Price at which user entered the position |
| 8 | IS_MATCH | int | `0` = initial liquidation trigger, `1` = market execution |
| 9 | IS_MARKET_SOLD | int | `0` = position acquired by system, `1` = direct market sell |
| 11 | PRICE_ACQUIRED | float | Price at which the position was actually liquidated |

**Rate limit**: ⚠️ **3 req/min** (very strict). Params: `start`, `end`, `limit`, `sort`.

> Currently NOT configured in our system. Could add as REST-polled liquidation data.
> Note: AMOUNT sign gives side (like trades), PRICE_ACQUIRED is the execution price.

---

## REST Funding Statistics `/v2/funding/stats/{symbol}/hist`

> Funding **market** data (lending side), NOT derivatives funding rate.
> Symbol uses `f` prefix: `fUSD`, `fBTC`, `fETH`.

### Request
| Param | Type | Description |
|-------|------|-------------|
| `symbol` | path | Required. e.g. `fUSD`, `fBTC` |
| `start` | int | Start timestamp (ms), inclusive |
| `end` | int | End timestamp (ms), inclusive |
| `limit` | int | Max **250** |

### Response
```
[
  [
    1678467900000,       // [0]  MTS
    null,                // [1]  —
    null,                // [2]  —
    0.00000187,          // [3]  FRR (1/365th of Flash Return Rate)
    68.88,               // [4]  AVG_PERIOD (days)
    null,                // [5]  —
    null,                // [6]  —
    3230660371.44,       // [7]  FUNDING_AMOUNT (total provided)
    2988430006.46,       // [8]  FUNDING_AMOUNT_USED (used in positions)
    null,                // [9]  —
    null,                // [10] —
    1447938775.57        // [11] FUNDING_BELOW_THRESHOLD (offers < 0.75%)
  ],
  [...]
]
```

| Index | Field | Type | Description |
|-------|-------|------|-------------|
| 0 | MTS | int | Timestamp (ms) |
| 3 | FRR | float | Flash Return Rate / 365. Daily rate = `FRR × 365`. APR% = `FRR × 365 × 365 × 100` |
| 4 | AVG_PERIOD | float | Average funding period (days) |
| 7 | FUNDING_AMOUNT | float | Total funding provided |
| 8 | FUNDING_AMOUNT_USED | float | Funding used in active positions |
| 11 | FUNDING_BELOW_THRESHOLD | float | Sum of open offers below 0.75% |

**Rate Limit**: Not specified (likely 90 req/min default).

---

## REST Stats `/v2/stats1/{key}:{size}:{sym}:{side}/hist`

> ⚠️ **This provides LS ratio data!** `pos.size` with `long`/`short` sides = total longs/shorts.
> Section must be `hist` or `last` (mandatory).

### Response
```
// hist:  [[MTS, VALUE], ...]
// last:  [MTS, VALUE]
```

| Index | Field | Type | Description |
|-------|-------|------|-------------|
| 0 | MTS | int | Timestamp (ms) |
| 1 | VALUE | float | Total amount |

### Available Keys

| Key | Size | Symbol | Side | Description | Example |
|-----|------|--------|------|-------------|---------|
| **`pos.size`** | `1m` | `tBTCUSD` | `long`, `short` | **Total longs/shorts** (base currency) | `pos.size:1m:tBTCF0:USTF0:long/hist` |
| `funding.size` | `1m` | `fUSD` | — | Total active funding | `funding.size:1m:fUSD/hist` |
| `credits.size` | `1m` | `fUSD` | — | Funding used in positions | `credits.size:1m:fUSD/hist` |
| `credits.size.sym` | `1m` | `fUSD` | `tBTCUSD` | Funding used per pair | `credits.size.sym:1m:fUSD:tBTCUSD/hist` |
| `vol.1d/7d/30d` | `30m` | `BFX` | — | Trading volume | `vol.1d:30m:BFX/hist` |
| `vwap` | `1d` | `tBTCUSD` | — | Volume-weighted avg price | `vwap:1d:tBTCUSD/hist` |

### LS Ratio from `pos.size`

To get LS ratio for a derivatives pair:
```
Long:  /v2/stats1/pos.size:1m:tBTCF0:USTF0:long/hist?limit=1
Short: /v2/stats1/pos.size:1m:tBTCF0:USTF0:short/hist?limit=1
Ratio: long_value / short_value
```

**Rate Limit**: 15 req/min. **Max limit**: 10000. Params: `start`, `end`, `limit`, `sort`.

---

## WS Public Channels

### Connection
- **URL**: `wss://api-pub.bitfinex.com/ws/2`
- **Max subscriptions**: 25 channels per connection (the 26th is reserved)
- **Heartbeat**: `[CHAN_ID, "hb"]` every 15 seconds
- **Ping**: JSON `{"event":"ping","cid":1234}` → `{"event":"pong","ts":...,"cid":1234}`
- **Also supports**: Native WS ping frames

### Subscribe
```json
{"event": "subscribe", "channel": "trades", "symbol": "tBTCUSD"}
```

### Subscribe Response
```json
{"event": "subscribed", "channel": "trades", "chanId": 17, "symbol": "tBTCUSD", "pair": "BTCUSD"}
```
> `pair` field = wire symbol WITHOUT `t` prefix. This is what gets stored in chanId→symbol map.

### Trades Channel

**Snapshot** (on subscribe):
```
[CHAN_ID, [[ID, MTS, AMOUNT, PRICE], [ID, MTS, AMOUNT, PRICE], ...]]
```

**Update** (live):
```
[CHAN_ID, "te", [ID, MTS, AMOUNT, PRICE]]
```
or
```
[CHAN_ID, "tu", [ID, MTS, AMOUNT, PRICE]]
```

- `te` = trade executed (real-time)
- `tu` = trade update (with full trade details, arrives shortly after `te`)
- Our worker uses `te` only (avoids duplicates)

| Array Index | Field | Description |
|-------------|-------|-------------|
| 0 | ID | Trade ID |
| 1 | MTS | Timestamp (ms) |
| 2 | AMOUNT | Signed quantity (+ = buy, - = sell) |
| 3 | PRICE | Price |

### Book Channel (Orderbook)

**Subscribe**:
```json
{"event": "subscribe", "channel": "book", "symbol": "tBTCUSD", "prec": "P0", "len": "25"}
```

**Snapshot**:
```
[CHAN_ID, [[PRICE, COUNT, AMOUNT], [PRICE, COUNT, AMOUNT], ...]]
```

**Update**:
```
[CHAN_ID, [PRICE, COUNT, AMOUNT]]
```

| Field | Type | Description |
|-------|------|-------------|
| PRICE | float | Price level |
| COUNT | int | Number of orders at this level. **0 = remove level** |
| AMOUNT | float | **Signed**: positive = bid side, negative = ask side. Absolute = total amount |

> **Side is determined by AMOUNT sign**, not by separate bid/ask arrays.
> The dedicated worker normalizes this into separate `bids`/`asks` arrays before emitting.
> When COUNT=0, the level should be removed (size=0 in our system).

### Status Channel (Derivatives — WS)

**Subscribe**:
```json
{"event": "subscribe", "channel": "status", "key": "deriv:tBTCF0:USTF0"}
```

**Update**: Same array format as REST `/v2/status/deriv`, wrapped in channel:
```
[CHAN_ID, [KEY, MTS, null, DERIV_PRICE, SPOT_PRICE, ..., CURRENT_FUNDING, ..., OPEN_INTEREST, ...]]
```

> ⚠️ Our dedicated worker does NOT currently subscribe to the Status WS channel.
> Funding + OI are REST-polled only via `polling_interval_ms: 20000`.
> Could be improved to use WS for lower latency, but REST works.

---

## Rate Limits

| Endpoint Type | Limit |
|---------------|-------|
| REST Public | 90 req/min |
| WS Connections | 20 connections/min (public) |
| WS Subscriptions | 25 channels/connection |
| WS Auth Connections | 5 connections/15s |

---

## Timestamps

**All timestamps are millisecond epoch UTC.** No timezone suffix issues (unlike some exchanges).

---

## Bitfinex Quirks Summary

| Quirk | Impact | Mitigation |
|-------|--------|------------|
| No universal pair delimiter (spot) | `BTCUSD` has no separator, `AAVE:USD` has `:` | Need currency-aware parser or explicit mapping |
| `UST` = USDT | Quote currency doesn't match canonical | Quote whitelist mapping needed |
| `F0` suffix on futures | `BTCF0:USTF0` → strip F0 for base/quote | `normalization.replace: {"F0": ""}` |
| Signed quantities | Side from AMOUNT sign in trades + book | `side_from_signed_qty: true` |
| Book COUNT=0 → remove | Different from most exchanges (size=0) | Worker handles in normalization |
| Snapshot on subscribe | Both trades and book send snapshots first | Worker discards trade snapshot, processes book snapshot |
| `te` vs `tu` trade events | `te` = instant, `tu` = confirmed update | Worker uses `te` only |
| TEST pairs in products | `TESTBTCF0:TESTUSDTF0` etc. | `normalization.exclude: "^TEST"` |
| Same endpoint for OI + funding | `/v2/status/deriv` returns both | Two handlers, same REST URL |
| Historical deriv status path differs | `/v2/status/deriv/{key}/hist` (path param, not query) — indices shift -1 | Different URL format, limit 5000 |
