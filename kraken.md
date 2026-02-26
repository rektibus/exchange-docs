# Kraken API Documentation (Consolidated)

> Sources: kraken spot rest api.md, kraken futures rest api.rb, Spot WS paste, kraken_futures.md
> Covers: Spot + Futures, REST + WebSocket, all market data endpoints

---

## Base URLs

| Purpose | URL |
|---------|-----|
| Spot REST | `https://api.kraken.com/0` |
| Spot WS v2 | `wss://ws.kraken.com/v2` |
| Futures REST (v3 legacy) | `https://futures.kraken.com/derivatives/api/v3` |
| Futures REST (history) | `https://futures.kraken.com/api/history/v3` |
| Futures REST (charts) | `https://futures.kraken.com/api/charts/v1` |
| Futures WS v1 | `wss://futures.kraken.com/ws/v1` |

---

# SPOT REST API

All spot public endpoints are under `https://api.kraken.com/0/public/`. Auth: **None**.

## Get Server Time

`GET /public/Time`

```json
{"error": [], "result": {"unixtime": 1709000000, "rfc1123": "Wed, 26 Feb 2026 12:00:00 +0000"}}
```

## Get System Status

`GET /public/SystemStatus`

```json
{"error": [], "result": {"status": "online", "timestamp": "2026-02-26T11:09:53Z"}}
```

Status values: `online`, `maintenance`, `cancel_only`, `post_only`.

## Get Asset Info

`GET /public/Assets?asset=XBT,ETH`

| Param | Type | Description |
|-------|------|-------------|
| `asset` | string | Comma-delimited assets (optional, default all) |
| `aclass` | string | `currency` or `tokenized_asset` (default: currency) |

Response: `result` → object keyed by asset name, each with `aclass`, `altname`, `decimals`, `display_decimals`, `collateral_value`, `status`.

## Get Tradable Asset Pairs

`GET /public/AssetPairs?pair=BTC/USD,ETH/BTC`

| Param | Type | Description |
|-------|------|-------------|
| `pair` | string | Asset pairs (optional) |
| `info` | string | `info`/`leverage`/`fees`/`margin` (default: info) |

Response: `result` → object keyed by pair name, each with:
- `altname`, `wsname` (WS pair name), `base`, `quote`
- `pair_decimals`, `lot_decimals`, `lot_multiplier`
- `leverage_buy[]`, `leverage_sell[]`
- `fees[]`, `fees_maker[]` ([volume, percent] tuples)
- `ordermin`, `costmin`, `tick_size`, `status`

## Get Ticker Information

`GET /public/Ticker?pair=XBTUSD`

Returns: `a` (ask [price, whole_lot_volume, lot_volume]), `b` (bid), `c` (close), `v` (volume), `p` (vwap), `t` (trades count), `l` (low), `h` (high), `o` (open).

## Get OHLC Data

`GET /public/OHLC?pair=XBTUSD&interval=1`

| Param | Type | Description |
|-------|------|-------------|
| `pair` | string | Required |
| `interval` | int | 1, 5, 15, 30, 60, 240, 1440, 10080, 21600 (minutes) |
| `since` | int | Return committed OHLC data since given ID |

Returns up to 720 entries. Each: `[time, open, high, low, close, vwap, volume, count]`.

## Get Order Book

`GET /public/Depth?pair=XBTUSD&count=10`

| Param | Type | Description |
|-------|------|-------------|
| `pair` | string | Required |
| `count` | int | Max price levels (1-500, default 100) |

Response: `asks[]` and `bids[]`, each `[price, volume, timestamp]`.

## Get Recent Trades

`GET /public/Trades?pair=XBTUSD&since=TRADE_ID`

Returns last 1000 trades. Each: `[price, volume, time, buy/sell, market/limit, miscellaneous, trade_id]`.

`since` = trade ID for pagination. Response includes `last` = ID for next pagination call.

## Get Recent Spreads

`GET /public/Spread?pair=XBTUSD&since=TIMESTAMP`

Returns ~200 spread entries: `[time, bid, ask]`.

---

# FUTURES REST API

## Get Instruments (Products)

`GET https://futures.kraken.com/derivatives/api/v3/instruments`

Auth: **None**

```json
{
  "result": "success",
  "instruments": [
    {
      "symbol": "PI_XBTUSD",
      "type": "futures_inverse",
      "underlying": "rr_xbtusd",
      "tickSize": 0.5,
      "contractSize": 1,
      "tradeable": true,
      "base": "BTC",
      "quote": "USD",
      "pair": "BTC:USD"
    },
    {
      "symbol": "PF_BTCUSD",
      "type": "flexible_futures",
      "underlying": "rr_xbtusd",
      "tickSize": 0.5,
      "contractSize": 1,
      "tradeable": true,
      "base": "BTC",
      "quote": "USD",
      "pair": "BTC:USD"
    }
  ]
}
```

**Symbol prefixes**: `PF_` = flexible_futures (linear perps), `PI_` = futures_inverse, `FI_` = expiring futures.

## Get Trade History (Legacy v3)

`GET https://futures.kraken.com/derivatives/api/v3/history?symbol=PI_XBTUSD`

Auth: **None**

```json
{
  "result": "success",
  "history": [
    {
      "time": "2026-02-23T20:51:56.455Z",
      "trade_id": 100,
      "price": 64373.5,
      "size": 119,
      "side": "buy",
      "type": "fill",
      "uid": "84284ea3-1ca3-44c9-a89d-a05d7aa29240"
    }
  ]
}
```

## Get Executions (History v3, paginated)

`GET https://futures.kraken.com/api/history/v3/market/{tradeable}/executions`

Auth: **None**

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `since` | timestamp-ms | No | Start time in milliseconds |
| `before` | timestamp-ms | No | End time in milliseconds |
| `sort` | string | No | `asc`/`desc` (default: desc) |
| `count` | int64 | No | Max results |
| `continuation_token` | base64 | No | Pagination token |

```json
{
  "len": 100,
  "elements": [
    {
      "uid": "...",
      "timestamp": 1604937694000,
      "event": {
        "Execution": {
          "execution": {
            "uid": "uuid",
            "takerOrder": {
              "tradeable": "PF_XBTUSD",
              "direction": "Buy",
              "quantity": "1234.56789",
              "timestamp": 1604937694000
            },
            "timestamp": 1604937694000,
            "quantity": "1234.56789",
            "price": "1234.56789",
            "markPrice": "1234.56789"
          }
        }
      }
    }
  ],
  "continuationToken": "base64..."
}
```

## Get Tickers (Current OI + Funding Rate)

`GET https://futures.kraken.com/derivatives/api/v3/tickers`

Auth: **None**

```json
{
  "result": "success",
  "tickers": [
    {
      "symbol": "PI_XBTUSD",
      "last": 64540,
      "lastTime": "2026-02-23T21:39:34.088946Z",
      "tag": "perpetual",
      "pair": "XBT:USD",
      "markPrice": 64535.022,
      "openInterest": 5177736.0,
      "fundingRate": 5.0536283e-11
    }
  ]
}
```

> **Note**: Only returns **current** funding rate. No historical funding rate endpoint exists.

## Get Market Analytics (Historical OI, LS Ratio, etc.)

`GET https://futures.kraken.com/api/charts/v1/analytics/{symbol}/{analytics_type}`

Auth: **None**

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `symbol` | string (path) | Yes | e.g. `PF_XBTUSD` |
| `analytics_type` | string (path) | Yes | See below |
| `since` | int64 (query) | Yes | Epoch **seconds** |
| `interval` | int (query) | Yes | 60, 300, 900, 1800, 3600, 14400, 43200, 86400, 604800 |
| `to` | int (query) | No | Epoch seconds (default: now) |

**Analytics types**: `open-interest`, `long-short-ratio`, `long-short-info`, `aggressor-differential`, `trade-volume`, `trade-count`, `liquidation-volume`, `rolling-volatility`, `cvd`, `top-traders`, `orderbook`, `spreads`, `liquidity`, `slippage`, `future-basis`

```json
{
  "result": {
    "timestamp": [1620816960, 1620817020],
    "more": false,
    "data": {"open_interest": [1234.56, 1235.78]}
  },
  "errors": []
}
```

## Get Market Candles

`GET https://futures.kraken.com/api/charts/v1/{tick_type}/{symbol}/{resolution}`

| Param | Type | Values |
|-------|------|--------|
| `tick_type` | path | `spot`, `mark`, `trade` |
| `symbol` | path | Market symbol |
| `resolution` | path | `1m`, `5m`, `15m`, `30m`, `1h`, `4h`, `12h`, `1d`, `1w` |
| `from` | query | Epoch seconds |
| `to` | query | Epoch seconds |
| `count` | query | Number of candles |

```json
{
  "candles": [
    {"time": 1620816960000, "open": "56294.0", "high": "56475.0", "low": "55935.0", "close": "56250.0", "volume": 10824}
  ],
  "more_candles": true
}
```

## Tick Types & Markets

- `GET /api/charts/v1/` → `["mark", "spot", "trade"]`
- `GET /api/charts/v1/{tick_type}` → list of market symbols
- `GET /api/charts/v1/{tick_type}/{symbol}` → available resolutions

## Get Public Order Events

`GET https://futures.kraken.com/api/history/v3/market/{tradeable}/orders`

Same pagination params as executions (`since`, `before`, `sort`, `count`, `continuation_token`).

Returns order placed/modified/cancelled events with `direction` (Buy/Sell), `quantity`, `limitPrice`, `orderType`, `timestamp`.

## Get Public Mark Price Events

`GET https://futures.kraken.com/api/history/v3/market/{tradeable}/price`

Same pagination params. Returns `price` per timestamp.

## Liquidity Pool Statistics

`GET https://futures.kraken.com/api/charts/v1/analytics/liquidity-pool`

| Param | Type | Required |
|-------|------|----------|
| `since` | int64 | Yes (epoch seconds) |
| `interval` | int | Yes (60..604800) |
| `to` | int | No (default now) |

---

# SPOT WEBSOCKET API

URL: `wss://ws.kraken.com/v2`

## Connection & Heartbeat

On connect, a `status` message is sent automatically:

```json
{
  "channel": "status",
  "type": "update",
  "data": [{"system": "online", "api_version": "v2", "connection_id": 12345, "version": "2.0.0"}]
}
```

System status values: `online`, `cancel_only`, `maintenance`, `post_only`.

Heartbeats sent ~every second when no other updates:

```json
{"channel": "heartbeat"}
```

## Ping/Pong

Send `{"method": "ping"}` → receive `{"method": "pong"}`.

## Subscribe / Unsubscribe Pattern

All channels follow:
```json
{"method": "subscribe", "params": {"channel": "<name>", "symbol": ["BTC/USD"], ...}, "req_id": 1}
```
Ack:
```json
{"method": "subscribe", "result": {"channel": "<name>", "symbol": "BTC/USD", ...}, "success": true, "req_id": 1}
```
Unsubscribe same pattern with `"method": "unsubscribe"`.

## Trades Channel

Subscribe:
```json
{"method": "subscribe", "params": {"channel": "trade", "symbol": ["BTC/USD"], "snapshot": false}}
```

Payload:
```json
{
  "channel": "trade",
  "type": "update",
  "data": [
    {
      "symbol": "BTC/USD",
      "side": "buy",
      "qty": 0.5,
      "price": 64000.5,
      "ord_type": "market",
      "trade_id": 12345,
      "timestamp": "2022-12-25T09:30:59.123456Z"
    }
  ]
}
```

- `snapshot: true` → first message has last 50 trades, `type: "snapshot"`
- Multiple trades can be batched in one message
- `trade_id` = sequence number, unique per book

## Book Channel (L2)

Subscribe:
```json
{"method": "subscribe", "params": {"channel": "book", "symbol": ["BTC/USD"], "depth": 10, "snapshot": true}}
```

Depth values: `10`, `25`, `100`, `500`, `1000` (default: 10).

Snapshot:
```json
{
  "channel": "book",
  "type": "snapshot",
  "data": [
    {
      "symbol": "BTC/USD",
      "bids": [{"price": 64000.5, "qty": 1.2}],
      "asks": [{"price": 64001.0, "qty": 0.8}],
      "checksum": 123456789,
      "timestamp": "2022-12-25T09:30:59.123456Z"
    }
  ]
}
```

Update:
```json
{
  "channel": "book",
  "type": "update",
  "data": [
    {
      "symbol": "BTC/USD",
      "bids": [{"price": 64000.5, "qty": 0}],
      "asks": [{"price": 64001.5, "qty": 2.0}],
      "checksum": 987654321,
      "timestamp": "2022-12-25T09:30:59.234567Z"
    }
  ]
}
```

- `qty: 0` = remove price level
- Multiple updates to same price level possible in one message — process in sequence
- `checksum` = CRC32 of top 10 bids+asks

## Ticker Channel (L1)

Subscribe:
```json
{"method": "subscribe", "params": {"channel": "ticker", "symbol": ["BTC/USD"], "event_trigger": "trades"}}
```

`event_trigger`: `bbo` (on BBO change) or `trades` (on every trade, default).

```json
{
  "channel": "ticker",
  "type": "update",
  "data": [
    {
      "symbol": "BTC/USD",
      "bid": 64000.5,
      "bid_qty": 1.0,
      "ask": 64001.0,
      "ask_qty": 0.5,
      "last": 64000.5,
      "volume": 1234.5,
      "vwap": 63950.0,
      "high": 65000.0,
      "low": 63000.0,
      "change": 500.0,
      "change_pct": 0.79,
      "timestamp": "2022-12-25T09:30:59.123456Z"
    }
  ]
}
```

## OHLC Channel

Subscribe:
```json
{"method": "subscribe", "params": {"channel": "ohlc", "symbol": ["BTC/USD"], "interval": 1}}
```

Intervals (minutes): `1`, `5`, `15`, `30`, `60`, `240`, `1440`, `10080`, `21600`.

```json
{
  "channel": "ohlc",
  "type": "update",
  "data": [
    {
      "symbol": "BTC/USD",
      "open": 64000.0,
      "high": 64500.0,
      "low": 63900.0,
      "close": 64200.0,
      "vwap": 64100.0,
      "trades": 150,
      "volume": 23.5,
      "interval_begin": "2022-12-25T09:30:00.000000Z",
      "interval": 1
    }
  ]
}
```

## Instruments Channel

Subscribe:
```json
{"method": "subscribe", "params": {"channel": "instrument", "snapshot": true}}
```

Snapshot includes `assets[]` (id, decimals, precision, status, collateral_value, margin_rate) and `pairs[]` (symbol, base, quote, status, price_increment, qty_increment, qty_min, price_precision, qty_precision, marginable, cost_min).

Pair status values: `online`, `cancel_only`, `delisted`, `limit_only`, `maintenance`, `post_only`, `reduce_only`.

---

# FUTURES WEBSOCKET API

URL: `wss://futures.kraken.com/ws/v1`

## Subscription

```json
{"event": "subscribe", "feed": "<feed_name>", "product_ids": ["PI_XBTUSD"]}
```

Ack:
```json
{"event": "subscribed", "feed": "<feed_name>", "product_ids": ["PI_XBTUSD"]}
```

## Trade Feed

Subscribe:
```json
{"event": "subscribe", "feed": "trade", "product_ids": ["PI_XBTUSD"]}
```

Payload:
```json
{
  "feed": "trade",
  "product_id": "PI_XBTUSD",
  "uid": "1fba1dc3-...",
  "side": "sell",
  "type": "fill",
  "seq": 100,
  "time": 1715011200000,
  "qty": 5000,
  "price": 64000.5
}
```

Fields: `feed`, `product_id`, `uid`, `side` (buy/sell), `type` (fill), `seq`, `time` (ms), `qty`, `price`.

## Book Feed (Depth)

Subscribe:
```json
{"event": "subscribe", "feed": "book", "product_ids": ["PI_XBTUSD"]}
```

Snapshot (first message, feed = `book_snapshot`):
```json
{
  "feed": "book_snapshot",
  "product_id": "PI_XBTUSD",
  "timestamp": 1715011200000,
  "seq": 1000,
  "bids": [{"price": 64000.5, "qty": 1000}],
  "asks": [{"price": 64001.0, "qty": 1500}]
}
```

Deltas (feed = `book`):
```json
{
  "feed": "book",
  "product_id": "PI_XBTUSD",
  "timestamp": 1715011200100,
  "seq": 1001,
  "bids": [{"price": 64000.5, "qty": 0}],
  "asks": [{"price": 64001.0, "qty": 2000}]
}
```

`qty: 0` = remove level.

## Ticker Feed

Subscribe:
```json
{"event": "subscribe", "feed": "ticker", "product_ids": ["PI_XBTUSD"]}
```

Returns current mark price, funding rate, open interest, bid/ask, volume, etc.

## Heartbeat

Heartbeats sent periodically:
```json
{"feed": "heartbeat", "time": 1715011200000}
```

---

# NOTES

## Historical Funding Rate

> **No public endpoint exists.** The `/derivatives/api/v3/tickers` only returns the current funding rate.
> The analytics API supports `open-interest` and `long-short-ratio` but NOT funding rate history.
> `https://futures.kraken.com/derivatives/api/v3/historicalfundingrates?symbol=PF_XBTUSD` returns **404**.
>
> **Workaround**: Poll `/tickers` via RestPoller for live funding rate (no recovery possible).

## Error Handling

Spot REST errors in `error[]` array at top level:
```json
{"error": ["EGeneral:Invalid arguments"], "result": {}}
```

Futures REST errors:
```json
{"result": "error", "errors": [{"code": 0, "message": "404 NOT_FOUND"}], "serverTime": "..."}
```

Or success:
```json
{"result": "success", ...}
```

## Symbol Formats

| Market | Product Symbol | WS Symbol | REST Symbol |
|--------|---------------|-----------|-------------|
| Spot | `XXBTZUSD` | `BTC/USD` (v2 WS) | `XBTUSD` or `BTC/USD` |
| Futures Linear | `PF_XBTUSD` | `PF_XBTUSD` | `PF_XBTUSD` |
| Futures Inverse | `PI_XBTUSD` | `PI_XBTUSD` | `PI_XBTUSD` |

## Raw Source Files

Unprocessed raw docs preserved in:
- `docs/external/kraken/kraken spot rest api.md` (spot REST, 1.1MB)
- `docs/external/kraken/kraken futures rest api.rb` (futures REST, 14KB)
- `docs/external/kraken-api-specs/` (official GitHub repo)