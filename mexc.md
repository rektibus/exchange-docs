# MEXC API Reference

> Source: https://mexcdevelop.github.io/apidocs/spot_v3_en/ (spot)
> Source: https://mexcdevelop.github.io/apidocs/contract_v1_en/ (futures)
> Proto definitions: https://github.com/mexcdevelop/websocket-proto

---

## Spot — WebSocket (Protobuf)

**URL**: `wss://wbs-api.mexc.com/ws`

All spot WS streams use **Protocol Buffers** serialization via `PushDataV3ApiWrapper`.

### Connection Limits & Lifecycle

- **Max 30 subscriptions** per WS connection
- **Connection valid for max 24 hours** — handle reconnection
- **WS rate limit**: 100 messages/second — exceeding → disconnect, repeat → IP ban
- **No valid subscription within 30s** → server disconnects
- **Subscribed but no data flow for 60s** → server disconnects (client ping keeps alive)
- **REST rate limit**: 500 requests per 10s per endpoint (by IP or UID)
- **429 response** → back off. `Retry-After` header gives wait seconds. Repeated violations → IP ban (2min to 3 days)

### Keepalive (Client-Initiated Ping — Archetype D)

Client sends `{"method": "PING"}`, server responds `{"id": 0, "code": 0, "msg": "PONG"}`. No server-initiated heartbeat. Recommended interval: 20s.

### PushDataV3ApiWrapper (outer proto envelope)

```protobuf
message PushDataV3ApiWrapper {
  string channel = 1;            // e.g. "spot@public.aggre.deals.v3.api.pb@100ms@BTCUSDT"
  oneof body {
    PublicDealsV3Api publicDeals = 301;
    PublicIncreaseDepthsV3Api publicIncreaseDepths = 302;
    PublicLimitDepthsV3Api publicLimitDepths = 303;
    // ... (304-312 = private/kline/ticker)
    PublicAggreDepthsV3Api publicAggreDepths = 313;
    PublicAggreDealsV3Api publicAggreDeals = 314;
    PublicAggreBookTickerV3Api publicAggreBookTicker = 315;
  }
  optional string symbol = 3;    // Trading pair (e.g. "BTCUSDT")
  optional string symbolId = 4;
  optional int64 createTime = 5;
  optional int64 sendTime = 6;
}
```

### Subscribe / Unsubscribe / Ping

```json
// Subscribe
{"method": "SUBSCRIPTION", "params": ["spot@public.aggre.deals.v3.api.pb@100ms@BTCUSDT"]}

// Unsubscribe
{"method": "UNSUBSCRIPTION", "params": ["spot@public.aggre.deals.v3.api.pb@100ms@BTCUSDT"]}

// Ping
{"method": "PING"}
```

**Subscribe ack**: `{"id": 0, "code": 0, "msg": "spot@public.aggre.deals.v3.api.pb@100ms@BTCUSDT"}`
**Pong**: `{"id": 0, "code": 0, "msg": "PONG"}`

### Trade Streams (Aggregated — container 314)

Channel: `spot@public.aggre.deals.v3.api.pb@(100ms|10ms)@<symbol>`

```protobuf
message PublicAggreDealsV3Api {
  repeated PublicAggreDealsV3ApiItem deals = 1;
  string eventType = 2;
}
message PublicAggreDealsV3ApiItem {
  string price = 1;
  string quantity = 2;
  int32 tradeType = 3;   // 1 = Buy, 2 = Sell
  int64 time = 4;         // ms timestamp
}
```

JSON representation (after deserialization):
```json
{
  "channel": "spot@public.aggre.deals.v3.api.pb@100ms@BTCUSDT",
  "publicdeals": {
    "dealsList": [
      {"price": "93220.00", "quantity": "0.04438243", "tradetype": 2, "time": 1736409765051}
    ],
    "eventtype": "spot@public.aggre.deals.v3.api.pb@100ms"
  },
  "symbol": "BTCUSDT",
  "sendtime": 1736409765052
}
```

### Trade Streams (Non-aggregated — container 301)

Channel: `spot@public.deals.v3.api.pb@<symbol>`

```protobuf
message PublicDealsV3Api {
  repeated PublicDealsV3ApiItem deals = 1;
  string eventType = 2;
}
message PublicDealsV3ApiItem {
  string price = 1;
  string quantity = 2;
  int32 tradeType = 3;    // 1 = Buy, 2 = Sell
  int64 time = 4;          // ms timestamp
}
```

### Diff.Depth Stream (Aggregated — container 313)

Channel: `spot@public.aggre.depth.v3.api.pb@(100ms|10ms)@<symbol>`

This is an **incremental/delta** stream. Quantity=0 means remove the level.

```protobuf
message PublicAggreDepthsV3Api {
  repeated PublicAggreDepthV3ApiItem asks = 1;
  repeated PublicAggreDepthV3ApiItem bids = 2;
  string eventType = 3;
  string fromVersion = 4;    // Version range start (for gap detection)
  string toVersion = 5;      // Version range end
}
message PublicAggreDepthV3ApiItem {
  string price = 1;
  string quantity = 2;
}
```

```json
{
  "channel": "spot@public.aggre.depth.v3.api.pb@100ms@BTCUSDT",
  "publicincreasedepths": {
    "asksList": [],                    // asks: Sell orders
    "bidsList": [                      // bids: Buy orders
      {
        "price": "92877.58",           // Price level of change
        "quantity": "0.00000000"       // Quantity (0 = remove level)
      }
    ],
    "eventtype": "spot@public.aggre.depth.v3.api.pb@100ms",
    "fromVersion": "10589632359",      // Version range start
    "toVersion": "10589632359"         // Version range end
  },
  "symbol": "BTCUSDT",
  "sendtime": 1736411507002
}
```

**Response Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `price` | string | Price level of change |
| `quantity` | string | Quantity (0 = remove level) |
| `eventtype` | string | Event type |
| `fromVersion` | string | Version range start |
| `toVersion` | string | Version range end |
| `symbol` | string | Trading pair |
| `sendtime` | long | Event time (ms) |

### Diff.Depth Stream (Non-aggregated — container 302)

Channel: `spot@public.increase.depth.v3.api.pb@<symbol>`

```protobuf
message PublicIncreaseDepthsV3Api {
  repeated PublicIncreaseDepthV3ApiItem asks = 1;
  repeated PublicIncreaseDepthV3ApiItem bids = 2;
  string eventType = 3;
  string version = 4;      // Single version number
}
message PublicIncreaseDepthV3ApiItem {
  string price = 1;
  string quantity = 2;
}
```

### Partial Book Depth Streams (Snapshot — container 303)

Channel: `spot@public.limit.depth.v3.api.pb@<symbol>@<level>` (level: 5, 10, 20)

```protobuf
message PublicLimitDepthsV3Api {
  repeated PublicLimitDepthV3ApiItem asks = 1;
  repeated PublicLimitDepthV3ApiItem bids = 2;
  string eventType = 3;
  string version = 4;
}
```

```json
{
  "channel": "spot@public.limit.depth.v3.api.pb@BTCUSDT@5",
  "publiclimitdepths": {
    "asksList": [
      {"price": "93180.18", "quantity": "0.21976424"}
    ],
    "bidsList": [
      {"price": "93179.98", "quantity": "2.82651000"}
    ],
    "eventtype": "spot@public.limit.depth.v3.api.pb",
    "version": "36913565463"
  },
  "symbol": "BTCUSDT",
  "sendtime": 1736411838730
}
```

**Response Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `price` | string | Price level |
| `quantity` | string | Quantity at level |
| `eventtype` | string | Event type |
| `version` | string | Version number |
| `symbol` | string | Trading pair |
| `sendtime` | long | Event time (ms) |

### Individual Symbol Book Ticker Streams

Pushes any update to the best bid or ask's price or quantity in real-time.

Channel: `spot@public.aggre.bookTicker.v3.api.pb@(100ms|10ms)@<symbol>`

```json
{
  "channel": "spot@public.aggre.bookTicker.v3.api.pb@100ms@BTCUSDT",
  "publicbookticker": {
    "bidprice": "93387.28",      // Best bid price
    "bidquantity": "3.73485",    // Best bid quantity
    "askprice": "93387.29",      // Best ask price
    "askquantity": "7.669875"    // Best ask quantity
  },
  "symbol": "BTCUSDT",
  "sendtime": 1736412092433
}
```

**Response Parameters:**

| Parameter | Type | Description |
|-----------|------|-------------|
| `bidprice` | string | Best bid price |
| `bidquantity` | string | Best bid quantity |
| `askprice` | string | Best ask price |
| `askquantity` | string | Best ask quantity |
| `symbol` | string | Trading pair |
| `sendtime` | long | Event time (ms) |

### How to Maintain Local Order Book

1. Subscribe to `spot@public.aggre.depth.v3.api.pb@(100ms|10ms)@SYMBOL`
2. GET REST snapshot: `https://api.mexc.com/api/v3/depth?symbol=SYMBOL&limit=1000`
3. `fromVersion` of each push = `toVersion + 1` of previous. Otherwise → packet loss → reinit from step 2.
4. Quantity is **absolute** (not relative change).
5. If push `toVersion < snapshot.version` → ignore (outdated).
6. If push `fromVersion > snapshot.version` → reinit.
7. When snapshot.version falls in [fromVersion, toVersion]:
   - Price exists → update quantity
   - Price doesn't exist → insert
   - Quantity = 0 → remove

> **Note:** Since depth snapshot has a level limit, levels outside the initial snapshot that haven't changed won't appear in incremental pushes. The 5000-depth limit is sufficient for most use cases.

---

## Spot — REST

**Base URL**: `https://api.mexc.com`

### Products

`GET /api/v3/exchangeInfo`

```json
{
  "symbols": [
    {
      "symbol": "BTCUSDT",
      "status": "1",
      "baseAsset": "BTC",
      "quoteAsset": "USDT",
      "permissions": ["SPOT"]
    }
  ]
}
```

Filter: `status: "1"` for active pairs. Note: some docs show `"ENABLED"` but API returns `"1"`.

### Recent Trades (no pagination)

`GET /api/v3/trades?symbol=BTCUSDT&limit=1000`

Returns most recent trades. **No time-range params** — recent-only, cannot page back.

```json
[
  {
    "id": null,
    "price": "68208.01",
    "qty": "0.00001568",
    "quoteQty": "1.0695015968",
    "time": 1772817966311,
    "isBuyerMaker": false,
    "isBestMatch": true,
    "tradeType": "BID"
  }
]
```

**Side**: `tradeType` = `"BID"` (buy) / `"ASK"` (sell).

### Aggregate Trades (paginated — used for recovery)

`GET /api/v3/aggTrades?symbol=BTCUSDT&startTime={{start_ms}}&endTime={{end_ms}}&limit=1000`

Supports `startTime` + `endTime` (ms) for time-range pagination. **This is the endpoint used for gap recovery.**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbol` | string | YES | Trading pair |
| `startTime` | long | NO | Start time (ms) — must be used with `endTime` |
| `endTime` | long | NO | End time (ms) — must be used with `startTime` |
| `limit` | int | NO | Max 1000 (default 500) |

```json
[
  {
    "a": null,
    "f": null,
    "l": null,
    "p": "68259.58",       // price
    "q": "2.50084549",     // quantity
    "T": 1772817984000,    // timestamp (ms)
    "m": true,             // isBuyerMaker (true=sell, false=buy)
    "M": true
  }
]
```

**Side**: `m` = isBuyerMaker boolean. `true` → seller was maker → trade is a SELL. `false` → buyer was maker → trade is a BUY. Same convention as Binance.

### Order Book (REST Snapshot)

`GET /api/v3/depth?symbol=BTCUSDT&limit=1000`

```json
{
  "lastUpdateId": 1112416,
  "bids": [["15.00000", "49999.00000"]],
  "asks": [["14.0000", "1.0000"]]
}
```

`lastUpdateId` corresponds to the `version` field in WS depth streams for synchronization.

---

## Futures — WebSocket (JSON)

**URL**: `wss://contract.mexc.com/edge`

Futures uses **plain JSON** (NOT protobuf).

### Connection Limits & Keepalive

- **No ping within 60s** → server disconnects
- **Recommended ping interval**: 10–20s
- **Client-initiated only** (Archetype D)

```json
// Client sends:
{"method": "ping"}
// Server responds:
{"channel": "pong", "data": 1587453241453}
```

### Transaction (Trades)

Subscribe: `{"method": "sub.deal", "param": {"symbol": "BTC_USDT"}}`
Unsubscribe: `{"method": "unsub.deal", "param": {"symbol": "BTC_USDT"}}`
Channel: `push.deal`

```json
{
  "channel": "push.deal",
  "data": {
    "M": 1,         // maker flag (1=maker, 2=taker)
    "O": 1,         // open type (1=open, 2=close, 3=both)
    "T": 1,         // side: 1 = buy, 2 = sell
    "p": 6866.5,    // price
    "t": 1587442049632, // timestamp ms
    "v": 2096       // volume (contracts)
  },
  "symbol": "BTC_USDT",
  "ts": 1587442022003
}
```

| Field | Type | Description |
|-------|------|-------------|
| `p` | decimal | Price |
| `v` | int | Volume (contracts) |
| `T` | int | Side: 1=buy, 2=sell |
| `O` | int | Open type |
| `M` | int | Maker flag |
| `t` | long | Timestamp (ms) |

Subscribe ack: `{"channel": "rs.sub.deal", ...}`

### Depth (Incremental)

Subscribe: `{"method": "sub.depth", "param": {"symbol": "BTC_USDT"}}`
Unsubscribe: `{"method": "unsub.depth", "param": {"symbol": "BTC_USDT"}}`
Channel: `push.depth`

Updates pushed every **200ms**.

```json
{
  "channel": "push.depth",
  "data": {
    "asks": [[6859.5, 3251, 1]],
    "bids": [],
    "version": 96801927
  },
  "symbol": "BTC_USDT",
  "ts": 1587442022003
}
```

**Level format**: `[price, contracts_at_level, order_count]` — 3 elements.
- Index 0 = price
- Index 1 = total contracts at this level (**this is what `size_index: 1` maps to**)
- Index 2 = number of distinct orders

| Field | Type | Description |
|-------|------|-------------|
| `asks` | `List<[price, contracts, orders]>` | Ask depth levels |
| `bids` | `List<[price, contracts, orders]>` | Bid depth levels |
| `version` | long | Incremental version number |

Full snapshot subscribe: `{"method": "sub.depth.full", "param": {"symbol": "BTC_USDT", "limit": 20}}`

### How to Maintain Futures Local Order Book

1. **Get full depth snapshot**: `GET /api/v1/contract/depth/{symbol}?limit=1000`
   - Save `version` as `localLastVersion`

2. **Subscribe to `push.depth`** on WebSocket

3. **Apply updates**:
   - If `version > localLastVersion`: cache or apply (updates override for same price)
   - Normal: `version == localLastVersion + 1` → apply directly
   - `quantity > 0` → update/insert level
   - `quantity == 0` → remove level

4. **Packet loss recovery**: `GET /api/v1/contract/depth_commits/{symbol}/1000`
   - Returns latest 1000 incremental commits (ascending by version)
   - Skip commits with `version <= localLastVersion`
   - Apply from first commit where `version == localLastVersion + 1`
   - Update `localLastVersion` after each applied commit
   - Apply any cached WS updates (higher version wins)

5. **Resume real-time**: each new event's `version` must equal `previous + 1`. Gap → re-run step 4 or full reinit from step 1.

> **Note**: Quantity in each event is **absolute** (total at that price), not relative.

### Ticker (OI + Funding)

Subscribe: `{"method": "sub.ticker", "param": {"symbol": "BTC_USDT"}}`
Channel: `push.ticker`

```json
{
  "channel": "push.ticker",
  "data": {
    "holdVol": 2284742,          // OI (contracts)
    "fundingRate": 0.0008,       // funding rate
    "lastPrice": 6865.5,
    "symbol": "BTC_USDT",
    "timestamp": 1587442022003
  },
  "symbol": "BTC_USDT",
  "ts": 1587442022003
}
```

### Funding Rate

Subscribe: `{"method": "sub.funding.rate", "param": {"symbol": "BTC_USDT"}}`
Channel: `push.funding.rate`

```json
{
  "channel": "push.funding.rate",
  "data": {"rate": 0.001, "symbol": "BTC_USDT"},
  "symbol": "BTC_USDT",
  "ts": 1587442022003
}
```

---

## Futures — REST

**Base URL**: `https://contract.mexc.com`

### Products (Contract Details)

`GET /api/v1/contract/detail`

Response wrapper: `data` array. Filter: `state: 0` for active. All 831 contracts are `futureType: 1` (PERPETUAL).

```json
{
  "symbol": "BTC_USDT",
  "baseCoin": "BTC",
  "quoteCoin": "USDT",
  "contractSize": 0.0001,
  "state": 0,
  "futureType": 1,
  "priceScale": 1,
  "volScale": 0,
  "minVol": 1,
  "maxVol": 400000,
  "maxLeverage": 500
}
```

Key fields for composition: `symbol`, `baseCoin` (→base), `quoteCoin` (→quote), `contractSize`.

### REST Trades

`GET /api/v1/contract/deals/BTC_USDT?limit=100`

Response wrapper: `data` array. Max 100 trades. **No time-range params** — recent-only.

| Field | Type | Description |
|-------|------|-------------|
| `p` | decimal | Price |
| `v` | int | Volume (contracts) |
| `T` | int | Side: 1=buy, 2=sell |
| `t` | long | Timestamp (ms) |
| `i` | string | Trade ID |

### REST Depth Snapshot

`GET /api/v1/contract/depth/{symbol}?limit=1000`

Response wrapper: `data`. Levels: `[price, contracts, order_count]`.

### REST Depth Commits (Recovery)

`GET /api/v1/contract/depth_commits/{symbol}/1000`

Returns latest 1000 incremental depth commits sorted ascending by version. Used for packet loss recovery (see order book maintenance above).

### OI (Ticker)

`GET /api/v1/contract/ticker` — bulk, `response_wrapper: "data"`, `symbol_filter_field: "symbol"`.

Field: `holdVol` (contracts).

### Funding Rate

`GET /api/v1/contract/funding_rate/BTC_USDT` — per-symbol.

Field: `fundingRate`.

### Historical Funding Rate

`GET /api/v1/contract/funding_rate/history?symbol=BTC_USDT&page_num=1&page_size=100`

Rate limit: 20 requests / 2 seconds.

**Page-based pagination ONLY** — no `start_time`/`end_time` params. Recovery can only page through recent records, not targeted gap fill.

| Param | Type | Required | Description |
|-------|------|----------|-------------|
| `symbol` | string | yes | Contract symbol (e.g. `BTC_USDT`) |
| `page_num` | int | yes | Current page, default 1 |
| `page_size` | int | yes | Page size, default 20, max 1000 |

Response path: `data.resultList`. Fields:

| Field | Type | Description |
|-------|------|-------------|
| `fundingRate` | decimal | Funding rate |
| `settleTime` | long | Settlement time (ms) |
| `collectCycle` | int | Funding cycle (hours) |

### Recovery Coverage Matrix

| Metric | Live WS | Live REST | Historical Recovery |
|--------|---------|-----------|---------------------|
| **Trades** | ✅ `push.deal` | ⚠️ Recent-only (100) | ⚠️ Recent-only |
| **Depth** | ✅ `push.depth` (delta) | ✅ Snapshot | N/A |
| **OI** | ✅ `push.ticker` → `holdVol` | ✅ `/api/v1/contract/ticker` | ❌ No historical endpoint |
| **Funding** | ✅ `push.ticker` → `fundingRate` | ✅ `/api/v1/contract/funding_rate/{{symbol}}` | ⚠️ Page-based only |
| **LS Ratio** | ❌ | ❌ | ❌ Not available |
| **Liquidations** | ❌ | ❌ | ❌ Not available |

