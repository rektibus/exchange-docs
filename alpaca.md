# Alpaca Crypto Exchange API Documentation

> Source: Official docs from `docs.alpaca.markets` (Feb 2026)
> Covers: Crypto Spot WebSocket, REST Historical/Latest, Products
> Alpaca executes crypto orders in its own exchange + supports Kraken as secondary source

---

## Key Facts

| Property | Value |
|----------|-------|
| **WS URL** | `wss://stream.data.alpaca.markets/v1beta3/crypto/us` |
| **REST Base URL** | `https://data.alpaca.markets` |
| **Products URL** | `https://api.alpaca.markets/v2/assets?asset_class=crypto` |
| **WS Auth** | HTTP headers `APCA-API-KEY-ID` + `APCA-API-SECRET-KEY` OR message `{"action":"auth","key":"KEY","secret":"SECRET"}` |
| **REST Auth** | Headers `Apca-Api-Key-Id` + `Apca-Api-Secret-Key` (required for WS; REST market data works without auth) |
| **WS Discriminator** | `T` field (string) |
| **Message format** | Array-wrapped: `[{...}, {...}]` |
| **Symbol format** | `BTC/USD` (slash separator) |
| **Timestamps** | RFC-3339 / ISO 8601, nanosecond precision |
| **Connection limit** | 1 active stream per subscription |
| **Auth timeout** | 10 seconds after connect |

---

## WS Locations

| `{loc}` | Source |
|---------|--------|
| `us` | Alpaca US (own exchange) |
| `us-1` | Kraken US |
| `eu-1` | Kraken EU |

Sandbox: `wss://stream.data.sandbox.alpaca.markets/v1beta3/crypto/{loc}`

---

## WS Connection Flow

```
→ Connect to wss://stream.data.alpaca.markets/v1beta3/crypto/us
  (with headers: APCA-API-KEY-ID: KEY, APCA-API-SECRET-KEY: SECRET)
← [{"T":"success","msg":"connected"}]
← [{"T":"success","msg":"authenticated"}]   (auto if headers used)
→ {"action":"subscribe","trades":["BTC/USD"],"orderbooks":["BTC/USD"]}
← [{"T":"subscription","trades":["BTC/USD"],"quotes":[],"orderbooks":["BTC/USD"],"bars":[],"updatedBars":[],"dailyBars":[]}]
← [{"T":"t","S":"BTC/USD","p":65614.929,"s":0.000038,"t":"2026-02-23T15:57:33.393Z","i":8160237406270933078,"tks":"S"}]
```

Alternative auth (via message, within 10s of connect):
```json
{"action": "auth", "key": "KEY_ID", "secret": "SECRET"}
```

---

## WS Discriminator Values

| `T` value | Type |
|-----------|------|
| `t` | Trade |
| `q` | Quote (BBO) |
| `b` | Bar (minute) |
| `o` | Orderbook |
| `success` | Ack (connected/authenticated) |
| `error` | Error |
| `subscription` | Subscription confirmation |

---

## WS Channel: Trades (`T: "t"`)

**Subscribe**: `{"action":"subscribe","trades":["BTC/USD"]}`

| Field | Type | Description |
|-------|------|-------------|
| `T` | string | `"t"` |
| `S` | string | Symbol (e.g. `"BTC/USD"`) |
| `p` | float | Price |
| `s` | float | Size (quantity) |
| `t` | string | Timestamp (RFC-3339, nanosecond) |
| `i` | int | Trade ID |
| `tks` | string | Taker side: `"B"` = buyer, `"S"` = seller |

```json
{"T":"t","S":"AVAX/USD","p":47.299,"s":29.205707815,"t":"2024-03-12T10:27:48.858228144Z","i":3447222699101865076,"tks":"S"}
```

---

## WS Channel: Orderbooks (`T: "o"`)

**Subscribe**: `{"action":"subscribe","orderbooks":["BTC/USD"]}`

| Field | Type | Description |
|-------|------|-------------|
| `T` | string | `"o"` |
| `S` | string | Symbol |
| `t` | string | Timestamp (RFC-3339) |
| `b` | array | Bids: `[{"p": price, "s": size}, ...]` |
| `a` | array | Asks: `[{"p": price, "s": size}, ...]` |
| `r` | boolean | Reset flag: `true` = full snapshot, absent/false = delta |

**Level format**: Named objects with `p` (price), `s` (size). Size `0` = remove level.

**Initial full orderbook** (`r: true`):
```json
{"T":"o","S":"BTC/USD","t":"2024-03-12T10:38:50.796Z",
 "b":[{"p":71859.53,"s":0.27994},{"p":71849.4,"s":0.553986}],
 "a":[{"p":71939.7,"s":0.83953},{"p":71940.4,"s":0.28025}],
 "r":true}
```

**Delta update** (no `r` field or `r: false`):
```json
{"T":"o","S":"MKR/USD","t":"2024-03-12T10:39:39.445Z",
 "b":[],"a":[{"p":2614.587,"s":12.5308}]}
```

**Remove level** (size = 0):
```json
{"T":"o","S":"CRV/USD","t":"2024-03-12T10:39:40.501Z",
 "b":[{"p":0.7904,"s":0}],"a":[]}
```

---

## WS Channel: Quotes (`T: "q"`)

**Subscribe**: `{"action":"subscribe","quotes":["BTC/USD"]}`

| Field | Type | Description |
|-------|------|-------------|
| `T` | string | `"q"` |
| `S` | string | Symbol |
| `bp` | float | Best bid price |
| `bs` | float | Best bid size |
| `ap` | float | Best ask price |
| `as` | float | Best ask size |
| `t` | string | Timestamp (RFC-3339) |

---

## WS Channel: Bars (`T: "b"`)

**Subscribe**: `{"action":"subscribe","bars":["BTC/USD"]}` (also `dailyBars`, `updatedBars`)

| Field | Type | Description |
|-------|------|-------------|
| `T` | string | `"b"` |
| `S` | string | Symbol |
| `o` | float | Open |
| `h` | float | High |
| `l` | float | Low |
| `c` | float | Close |
| `v` | float | Volume |
| `t` | string | Timestamp (RFC-3339) |
| `n` | int | Trade count |
| `vw` | float | VWAP |

---

## REST: Historical Trades

`GET /v1beta3/crypto/{loc}/trades`

| Parameter | Type | Required | Default | Max | Description |
|-----------|------|----------|---------|-----|-------------|
| `symbols` | string | yes | | | Comma-separated (e.g. `BTC/USD,ETH/USD`) |
| `start` | date-time | no | start of day | | RFC-3339 or YYYY-MM-DD |
| `end` | date-time | no | now | | RFC-3339 |
| `limit` | integer | no | 1000 | 10000 | Max per page |
| `sort` | enum | no | `asc` | | `asc`, `desc` |
| `page_token` | string | no | | | Pagination token |

**Response**: `trades.{SYMBOL}` → array of trades

```json
{
  "trades": {
    "BTC/USD": [
      {"t":"2026-02-23T00:00:48.646Z","p":67655.2,"s":0.000072,"tks":"B","i":4888505089891583889},
      {"t":"2026-02-23T00:01:28.827Z","p":67614.189,"s":0.015652686,"tks":"S","i":8886124547701098859}
    ]
  },
  "next_page_token": "QlRDL1VTR..."
}
```

**Trade fields**: `t` (timestamp RFC-3339), `p` (price), `s` (size), `tks` (taker side: `B`/`S`), `i` (trade ID)

**NOTE**: REST market data works WITHOUT auth headers. WS requires auth.

---

## REST: Latest Trades

`GET /v1beta3/crypto/{loc}/latest/trades`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbols` | string | yes | Comma-separated |

**Response**: `trades.{SYMBOL}` → single trade object (NOT array)

---

## REST: Latest Orderbooks

`GET /v1beta3/crypto/{loc}/latest/orderbooks`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbols` | string | yes | Comma-separated |

**Response**: `orderbooks.{SYMBOL}` → orderbook object

```json
{
  "orderbooks": {
    "BTC/USD": {
      "t": "2022-06-24T08:00:14.137Z",
      "b": [{"p": 20846, "s": 0.1902}],
      "a": [{"p": 20902, "s": 0.0097}]
    }
  }
}
```

---

## REST: Historical Bars

`GET /v1beta3/crypto/{loc}/bars`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbols` | string | yes | Comma-separated |
| `timeframe` | string | yes | `[1-59]Min`, `[1-23]Hour`, `1Day`, `1Week`, `[1,2,3,4,6]Month` |
| `start` | date-time | no | start of day |
| `end` | date-time | no | now |
| `limit` | integer | no | 1000 (max 10000) |

**Bar fields**: `t`, `o`, `h`, `l`, `c`, `v`, `n`, `vw`

---

## REST: Snapshots

`GET /v1beta3/crypto/{loc}/snapshots`

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `symbols` | string | yes | Comma-separated |

Returns per symbol: `latestTrade`, `latestQuote`, `minuteBar`, `dailyBar`, `prevDailyBar`.

---

## Products (Assets) Listing

`GET https://api.alpaca.markets/v2/assets?asset_class=crypto`

**Auth required**: `Apca-Api-Key-Id` + `Apca-Api-Secret-Key` headers

**Response**: Array of asset objects

```json
[
  {
    "id": "276e2673-764b-4ab6-a611-caf665ca6340",
    "class": "crypto",
    "exchange": "ALPACA",
    "symbol": "BTC/USD",
    "name": "BTC/USD pair",
    "status": "active",
    "tradable": true,
    "marginable": false,
    "shortable": false,
    "easy_to_borrow": false,
    "fractionable": true,
    "min_order_size": "0.0001",
    "min_trade_increment": "0.0001",
    "price_increment": "1"
  }
]
```

**Key fields**: `symbol` (e.g. `BTC/USD`), `status` (`active`), `class` (`crypto`), `min_order_size`, `price_increment`

56 trading pairs across 20+ unique crypto assets. Pairs based on BTC, USD, USDT, USDC.

**Symbol compatibility**: `BTC/USD` is the current format. Legacy `BTCUSD` is still accepted for backwards compatibility.

---

## Perps (v1beta1) — REST Only

All perps endpoints: `GET /v1beta1/crypto-perps/global/latest/...`

**Auth required**. No WS stream for perps. No historical data (only `latest/*`).

**Symbol format**: `BTCUSDT.P` (suffix `.P` = perpetual)

### Latest Perp Pricing (Funding Rate + OI)

`GET /v1beta1/crypto-perps/global/latest/pricing?symbols=BTCUSDT.P`

```json
{
  "pricing": {
    "BTCUSDT.P": {
      "t": "2022-05-27T10:18:00Z",
      "ft": "2022-05-27T10:18:00Z",
      "oi": 90.7367,
      "ip": 50702.8,
      "mp": 50652.3553,
      "fr": 0.000565699
    }
  }
}
```

| Field | Key | Description |
|-------|-----|-------------|
| Timestamp | `t` | RFC-3339 |
| Next funding time | `ft` | RFC-3339 |
| Open interest | `oi` | float |
| Index price | `ip` | float |
| Mark price | `mp` | float |
| Funding rate | `fr` | float |

### Other Perp Endpoints

| Endpoint | Response Key |
|----------|-------------|
| `/v1beta1/crypto-perps/global/latest/trades` | `trades.{SYMBOL}` |
| `/v1beta1/crypto-perps/global/latest/orderbooks` | `orderbooks.{SYMBOL}` |
| `/v1beta1/crypto-perps/global/latest/bars` | `bars.{SYMBOL}` |
| `/v1beta1/crypto-perps/global/latest/quotes` | `quotes.{SYMBOL}` |

No liquidation feed. No LS ratio. No historical perps data.

---

## Rate Limits

- REST: Rate limit headers `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` (UNIX epoch)
- WS: 200 requests/min per connection, 1000 connections/min
- WS connection limit: 1 active stream per subscription plan

## Pagination

All historical endpoints support `page_token` param + `next_page_token` in response (null when done).

---

## EnsoX Integration Notes

1. **Dedicated adapter required**: Array-wrapped messages, auth headers on connect, custom subscribe format
2. **WS auth via HTTP headers** is the cleanest approach — set `APCA-API-KEY-ID` and `APCA-API-SECRET-KEY` as connection headers
3. **Depth is delta-based**: First message has `r: true` (full snapshot), subsequent are deltas
4. **Side values**: `"B"` = buyer/taker, `"S"` = seller/taker (NOT `"buy"`/`"sell"`)
5. **Timestamp unit**: ISO/RFC-3339 everywhere
6. **Products listing requires auth**: Need API keys for `api.alpaca.markets/v2/assets`
7. **No perps WS stream**: Perps data only via REST polling
