# Bithumb API Documentation (v1 — Upbit-compatible)

> **Base URL**: `https://api.bithumb.com`
> **Market format**: `KRW-BTC` (quote-base)
> **Note**: Bithumb migrated from old API (`/public/`) to new Upbit-compatible v1 API. Old endpoints still work but new ones are canonical.

---

## REST API

### Market Code Inquiry (Products)

```
GET /v1/market/all?isDetails=false
```

**Public**. Returns list of all tradable markets.

**Response** (array):

| Field | Type | Description |
|-------|------|-------------|
| `market` | String | Market code, e.g. `KRW-BTC` |
| `korean_name` | String | Korean name |
| `english_name` | String | English name |
| `market_warning` | String | `NONE` or `CAUTION` |

```json
[
  {
    "market": "KRW-BTC",
    "korean_name": "비트코인",
    "english_name": "Bitcoin"
  }
]
```

---

### Ticker (Current Price)

```
GET /v1/ticker?markets=KRW-BTC
```

**Public**. Snapshot at request time. `markets` param: comma-separated market codes.

**Response** (array):

| Field | Type | Description |
|-------|------|-------------|
| `market` | String | Market code |
| `trade_date` | String | Last trade date UTC `yyyyMMdd` |
| `trade_time` | String | Last trade time UTC `HHmmss` |
| `trade_timestamp` | Long | Last trade timestamp (ms) |
| `opening_price` | Double | Open price |
| `high_price` | Double | High price |
| `low_price` | Double | Low price |
| `trade_price` | Double | Last trade price (close) |
| `prev_closing_price` | Double | Previous day close (00:00 KST) |
| `change` | String | `EVEN` / `RISE` / `FALL` |
| `change_price` | Double | Absolute change |
| `change_rate` | Double | Absolute change rate |
| `signed_change_price` | Double | Signed change |
| `signed_change_rate` | Double | Signed change rate |
| `trade_volume` | Double | Most recent trade volume |
| `acc_trade_price` | Double | Cumulative trade amount (00:00 KST) |
| `acc_trade_price_24h` | Double | 24h cumulative trade amount |
| `acc_trade_volume` | Double | Cumulative trade volume (00:00 KST) |
| `acc_trade_volume_24h` | Double | 24h cumulative trade volume |
| `highest_52_week_price` | Double | 52-week high |
| `highest_52_week_date` | String | `yyyy-MM-dd` |
| `lowest_52_week_price` | Double | 52-week low |
| `lowest_52_week_date` | String | `yyyy-MM-dd` |
| `timestamp` | Long | Timestamp (ms) |

```json
[
  {
    "market": "KRW-BTC",
    "trade_date": "20180418",
    "trade_time": "102340",
    "trade_timestamp": 1524047020000,
    "opening_price": 8450000,
    "high_price": 8679000,
    "low_price": 8445000,
    "trade_price": 8621000,
    "prev_closing_price": 8450000,
    "change": "RISE",
    "change_price": 171000,
    "change_rate": 0.0202366864,
    "signed_change_price": 171000,
    "signed_change_rate": 0.0202366864,
    "trade_volume": 0.02467802,
    "acc_trade_price": 108024804862.58253,
    "acc_trade_price_24h": 232702901371.09308,
    "acc_trade_volume": 12603.53386105,
    "acc_trade_volume_24h": 27181.31137002,
    "highest_52_week_price": 28885000,
    "highest_52_week_date": "2018-01-06",
    "lowest_52_week_price": 4175000,
    "lowest_52_week_date": "2017-09-25",
    "timestamp": 1524047026072
  }
]
```

---

### Minute Candles

```
GET /v1/candles/minutes/{unit}?market=KRW-BTC&count=1
```

**Public**. `unit`: 1, 3, 5, 10, 15, 30, 60, 240.

**Params**:

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `unit` | int | Yes (path) | Minute interval |
| `market` | String | Yes | Market code |
| `to` | String | No | Last candle time (exclusive), ISO8601. Default: most recent |
| `count` | int | No | Number of candles (max 200, default 1) |

**Response** (array):

| Field | Type | Description |
|-------|------|-------------|
| `market` | String | Market code |
| `candle_date_time_utc` | String | Candle time UTC `yyyy-MM-dd'T'HH:mm:ss` |
| `candle_date_time_kst` | String | Candle time KST |
| `opening_price` | Double | Open |
| `high_price` | Double | High |
| `low_price` | Double | Low |
| `trade_price` | Double | Close |
| `timestamp` | Long | Candle close timestamp (ms) |
| `candle_acc_trade_price` | Double | Cumulative trade amount |
| `candle_acc_trade_volume` | Double | Cumulative trade volume |
| `unit` | int | Minutes unit |

```json
[
  {
    "market": "KRW-BTC",
    "candle_date_time_utc": "2018-04-18T10:16:00",
    "candle_date_time_kst": "2018-04-18T19:16:00",
    "opening_price": 8615000,
    "high_price": 8618000,
    "low_price": 8611000,
    "trade_price": 8616000,
    "timestamp": 1524046594584,
    "candle_acc_trade_price": 60018891.90054,
    "candle_acc_trade_volume": 6.96780929,
    "unit": 1
  }
]
```

---

### Recent Trades

```
GET /v1/trades/ticks?market=KRW-BTC&count=3
```

**Public**. Returns recent trade ticks.

**Params**:

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `market` | String | Yes | Market code |
| `to` | String | No | Last trade time (exclusive), `HH:mm:ss` or `HHmmss` |
| `count` | int | No | Number of trades (max 500, default 1) |
| `cursor` | String | No | Pagination cursor (`sequential_id`) |
| `daysAgo` | int | No | Days ago (1-7, default 0 = today) |

**Response** (array):

| Field | Type | Description |
|-------|------|-------------|
| `market` | String | Market code |
| `trade_date_utc` | String | Trade date UTC `yyyy-MM-dd` |
| `trade_time_utc` | String | Trade time UTC `HH:mm:ss` |
| `timestamp` | Long | Timestamp (ms) |
| `trade_price` | Double | Trade price |
| `trade_volume` | Double | Trade volume |
| `prev_closing_price` | Double | Previous day close |
| `change_price` | Double | Price change |
| `ask_bid` | String | `ASK` = sell, `BID` = buy |
| `sequential_id` | Long | Unique sequential ID |

```json
[
  {
    "market": "KRW-BTC",
    "trade_date_utc": "2026-02-17",
    "trade_time_utc": "23:25:27",
    "timestamp": 1771370727772,
    "trade_price": 99990000,
    "trade_volume": 0.00059798,
    "prev_closing_price": 99391000,
    "change_price": 599000,
    "ask_bid": "ASK",
    "sequential_id": 17713707277720000
  }
]
```

> **REST → Canonical field mapping** (for `rest_field_map`):
> - `trade_price` → `price`
> - `trade_volume` → `quantity`
> - `ask_bid` → `side` (side_map: `ASK`=sell, `BID`=buy)
> - `timestamp` → `timestamp`
> - `sequential_id` → `trade_id`

---

### Orderbook

```
GET /v1/orderbook?markets=KRW-BTC
```

**Public**. `markets` param: comma-separated market codes.

Single market → 30 levels. Multiple markets → 15 levels each.

**Response** (array):

| Field | Type | Description |
|-------|------|-------------|
| `market` | String | Market code |
| `timestamp` | Long | Orderbook generation time (ms) |
| `total_ask_size` | Double | Total remaining ask quantity |
| `total_bid_size` | Double | Total remaining bid quantity |
| `orderbook_units` | List | Orderbook levels (see below) |

**orderbook_units** (ordered best→worst):

| Field | Type | Description |
|-------|------|-------------|
| `ask_price` | Double | Ask price |
| `bid_price` | Double | Bid price |
| `ask_size` | Double | Ask size |
| `bid_size` | Double | Bid size |

```json
[
  {
    "market": "KRW-BTC",
    "timestamp": 1529910247984,
    "total_ask_size": 8.83621228,
    "total_bid_size": 2.43976741,
    "orderbook_units": [
      {"ask_price": 6956000, "bid_price": 6954000, "ask_size": 0.24078656, "bid_size": 0.00718341},
      {"ask_price": 6958000, "bid_price": 6953000, "ask_size": 1.12919, "bid_size": 0.11500074},
      {"ask_price": 6960000, "bid_price": 6952000, "ask_size": 0.08614137, "bid_size": 0.19019028}
    ]
  }
]
```

> **Note**: Bids and asks are interleaved in `orderbook_units` — each entry has BOTH a bid and ask level at that depth position. This is different from the typical separate `bids[]`/`asks[]` format.

---

### Market Alert System

```
GET /v1/market/virtual_asset_warning
```

**Public**. Returns list of markets under alert designation.

| Field | Type | Description |
|-------|------|-------------|
| `market` | String | Market code |
| `warning_type` | String | `PRICE_SUDDEN_FLUCTUATION`, `PRICE_DIFFERENCE_HIGH`, `SPECIFIC_ACCOUNT_HIGH_TRANSACTION`, `TRADING_VOLUME_SUDDEN_FLUCTUATION`, `DEPOSIT_AMOUNT_SUDDEN_FLUCTUATION` |
| `warning_step` | String | `CAUTION`, `WARNING`, `DANGER` |
| `end_date` | String | Alert end date KST `yyyy-MM-dd HH:mm:ss` |

---

## WebSocket API

### Connection

```
Public:  wss://ws-api.bithumb.com/websocket/v1
Private: wss://ws-api.bithumb.com/websocket/v1/private
```

**Rate limit**: 10 connections/sec per IP. Data received after connection is not rate-limited.

**Data types**: `snapshot` (state at request time) and `realtime` (continuous stream). Can request both or one.

**Public channels**: `ticker`, `trade`, `orderbook`
**Private channels**: `myOrder`, `myAsset` (require JWT auth in header)

### Request Format

Requests are JSON arrays with ticket, type, and optional format fields:

```json
[
  {"ticket": "unique-id"},
  {"type": "ticker", "codes": ["KRW-BTC", "BTC-ETH"]},
  {"type": "trade", "codes": ["KRW-BTC"]},
  {"format": "SIMPLE"}
]
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `ticket` | String | Yes | Unique requester ID (use UUID) |
| `type` | String | Yes | Channel: `ticker`, `trade`, `orderbook` |
| `codes` | String[] | Yes | Market codes |
| `is_only_snapshot` | Boolean | No | Only receive snapshot |
| `is_only_realtime` | Boolean | No | Only receive realtime |
| `format` | String | No | `DEFAULT` or `SIMPLE` (abbreviated field names) |

Multiple `type` fields can be specified in one request.

---

### WS Ticker

**DEFAULT format** — discriminator: `"type": "ticker"`

```json
{
  "type": "ticker",
  "code": "KRW-BTC",
  "opening_price": 484500,
  "high_price": 493100,
  "low_price": 472500,
  "trade_price": 493100,
  "prev_closing_price": 484500,
  "change": "RISE",
  "change_price": 8600,
  "signed_change_price": 8600,
  "change_rate": 0.01775026,
  "signed_change_rate": 0.01775026,
  "trade_volume": 3.2529,
  "acc_trade_volume": 220.0447,
  "acc_trade_volume_24h": 13380.57687512,
  "acc_trade_price": 105917424.208256,
  "acc_trade_price_24h": 8227950466.316009,
  "trade_date": "20240910",
  "trade_time": "091617",
  "trade_timestamp": 1725927377174,
  "ask_bid": "BID",
  "highest_52_week_price": 999999000,
  "highest_52_week_date": "2024-06-18",
  "lowest_52_week_price": 1000,
  "lowest_52_week_date": "2024-06-18",
  "market_state": "ACTIVE",
  "is_trading_suspended": false,
  "market_warning": "NONE",
  "timestamp": 1725927377287,
  "stream_type": "SNAPSHOT"
}
```

**SIMPLE format** — discriminator: `"ty": "ticker"`

| DEFAULT | SIMPLE | Description |
|---------|--------|-------------|
| `type` | `ty` | Channel type |
| `code` | `cd` | Market code |
| `opening_price` | `op` | Open |
| `high_price` | `hp` | High |
| `low_price` | `lp` | Low |
| `trade_price` | `tp` | Last trade price |
| `trade_volume` | `tv` | Last trade volume |
| `trade_timestamp` | `ttms` | Trade timestamp (ms) |
| `acc_trade_volume` | `atv` | Cumulative volume |
| `acc_trade_volume_24h` | `atv24h` | 24h volume |
| `acc_trade_price` | `atp` | Cumulative amount |
| `acc_trade_price_24h` | `atp24h` | 24h amount |
| `ask_bid` | `ab` | `ASK` or `BID` |
| `timestamp` | `tms` | Message timestamp (ms) |
| `stream_type` | `st` | `SNAPSHOT` or `REALTIME` |

---

### WS Trade

**Request**: `{"type": "trade", "codes": ["KRW-BTC"]}`

**DEFAULT format** — discriminator: `"type": "trade"`

| DEFAULT | SIMPLE | Type | Description |
|---------|--------|------|-------------|
| `type` | `ty` | String | `trade` |
| `code` | `cd` | String | Market code (e.g. `KRW-BTC`) |
| `trade_price` | `tp` | Double | Trade price |
| `trade_volume` | `tv` | Double | Trade volume |
| `ask_bid` | `ab` | String | `ASK` = sell, `BID` = buy |
| `prev_closing_price` | `pcp` | Double | Previous day close |
| `change` | `c` | String | `RISE`/`EVEN`/`FALL` |
| `change_price` | `cp` | Double | Absolute change |
| `trade_date` | `tdt` | String | Trade date KST `yyyy-MM-dd` |
| `trade_time` | `ttm` | String | Trade time KST `HH:mm:ss` |
| `trade_timestamp` | `ttms` | Long | Trade timestamp (ms) |
| `sequential_id` | `sid` | Long | Unique trade ID (not ordered) |
| `timestamp` | `tms` | Long | Message timestamp (ms) |
| `stream_type` | `st` | String | `SNAPSHOT`/`REALTIME` |

```json
{
  "type": "trade",
  "code": "KRW-BTC",
  "trade_price": 489700,
  "trade_volume": 1.4825,
  "ask_bid": "BID",
  "prev_closing_price": 484500,
  "change": "RISE",
  "change_price": 5200,
  "trade_date": "2024-09-10",
  "trade_time": "09:58:54",
  "trade_timestamp": 1725929934373,
  "sequential_id": 17259299343730000,
  "timestamp": 1725929934483,
  "stream_type": "REALTIME"
}
```

> **Note**: `sequential_id` guarantees uniqueness but NOT order. `ask_bid` = `BID` means buyer-initiated (taker bought), `ASK` = seller-initiated (taker sold).

---

### WS Orderbook

**Request**: `{"type": "orderbook", "codes": ["KRW-BTC"], "level": 1}`

`level` = price grouping unit (default `1` = tick-level). Per-market level via suffix: `"KRW-ETH.3"`.

**DEFAULT format** — discriminator: `"type": "orderbook"`

| DEFAULT | SIMPLE | Type | Description |
|---------|--------|------|-------------|
| `type` | `ty` | String | `orderbook` |
| `code` | `cd` | String | Market code |
| `total_ask_size` | `tas` | Double | Total ask quantity |
| `total_bid_size` | `tbs` | Double | Total bid quantity |
| `orderbook_units` | `obu` | List | Levels (see below) |
| `timestamp` | `tms` | Long | Timestamp (ms) |
| `level` | `lv` | Double | Price grouping unit |

**orderbook_units** (interleaved — each entry has BOTH bid and ask at that depth):

| DEFAULT | SIMPLE | Type | Description |
|---------|--------|------|-------------|
| `ask_price` | `ap` | Double | Ask price |
| `bid_price` | `bp` | Double | Bid price |
| `ask_size` | `as` | Double | Ask size |
| `bid_size` | `bs` | Double | Bid size |

```json
{
  "type": "orderbook",
  "code": "KRW-BTC",
  "total_ask_size": 450.3526,
  "total_bid_size": 63.3006,
  "orderbook_units": [
    {"ask_price": 478800, "bid_price": 478300, "ask_size": 4.3478, "bid_size": 5.6370},
    {"ask_price": 489700, "bid_price": 477900, "ask_size": 2.3642, "bid_size": 0.9705},
    {"ask_price": 493100, "bid_price": 471200, "ask_size": 411.8686, "bid_size": 3.9279}
  ],
  "timestamp": 1725927377287,
  "level": 0,
  "stream_type": "REALTIME"
}
```

> **Note**: Bids and asks are interleaved — NOT separate arrays. Each `orderbook_units` entry contains one ask level and one bid level at that depth position.

---

### Connection Management (PING/PONG)

- **Idle timeout**: ~120 seconds without any data → server closes connection
- **Keep-alive**: Send text `PING` → server responds with `{"status":"UP"}` every 10 seconds
- **RFC 6455**: Standard WebSocket PING/PONG frames also supported
- Most WS libraries have built-in ping support

```
> PING
< {"status":"UP"}
< {"status":"UP"}
...
```

---

### WS Errors

Error response format:
```json
{"error": {"name": "ERROR_TYPE", "message": "description"}}
```

| Error | Description |
|-------|-------------|
| `WRONG_FORMAT` | Invalid JSON format |
| `NO_TICKET` | Missing or invalid ticket |
| `NO_TYPE` | Missing type field |
| `NO_CODES` | Missing codes field |
| `INVALID_PARAM` | Empty codes or unsupported format |

---

## Old API (Legacy — Still Working)

The old Bithumb API at `/public/` is still functional:

- **Products**: `GET /public/ticker/ALL_KRW` → `data` object keyed by symbol
- **Trades**: `GET /public/transaction_history/{symbol}` → `transaction_date` (ISO), `type` (bid/ask), `units_traded`, `price`, `total`
- **Old WS**: `wss://pubwss.bithumb.com/pub/ws` — discriminator `type`, handlers: `transaction` (trades), `depth` (orderbook)

### Old REST Trade Fields

| REST Field | Canonical | Description |
|------------|-----------|-------------|
| `contPrice` | `price` | Trade price |
| `contQty` | `quantity` | Trade quantity |
| `buySellGb` | `side` | `1`=buy, `2`=sell |
| `contDtm` | `timestamp` | Trade datetime (ISO string) |

> **Note**: Bithumb Futures (`bithumbfutures.com`) and Bithumb Pro/Global (`global-api.bithumb.pro`) are both **dead** as of 2026-02. Only Bithumb Korea spot is operational.
