# Alpaca Market Data API Documentation

> Source: Official OpenAPI spec from `docs.alpaca.markets/openapi/market-data-api.json`
> Local copy: `docs/external/alpaca_market_data_openapi.json` (127KB, 48 endpoints)
> Source: Live WS docs from `docs.alpaca.markets/docs/real-time-crypto-pricing-data`
> Source: Live API verification (Feb 2026)

**Base URL**: `https://data.alpaca.markets`

**Authentication** (required for all endpoints):
- Headers: `Apca-Api-Key-Id` + `Apca-Api-Secret-Key`
- Rate limit headers: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset` (UNIX epoch)

**Pagination**: All historical endpoints support `page_token` + `next_page_token` (null when done).

---

## Table of Contents

1. [Crypto Spot (v1beta3)](#1-crypto-spot-v1beta3)
2. [Crypto Perpetuals (v1beta1)](#2-crypto-perpetuals-v1beta1)
3. [Crypto WebSocket Streaming](#3-crypto-websocket-streaming)
4. [Stocks (v2)](#4-stocks-v2)
5. [News (v1beta1)](#5-news-v1beta1)
6. [Logos (v1beta1)](#6-logos-v1beta1)
7. [Screener (v1beta1)](#7-screener-v1beta1)
8. [Options (v1beta1)](#8-options-v1beta1)
9. [Forex (v1beta1)](#9-forex-v1beta1)
10. [Corporate Actions (v1)](#10-corporate-actions-v1)

---

## 1. Crypto Spot (v1beta3)

All crypto endpoints: `GET /v1beta3/crypto/{loc}/...`

**Path param** `loc` (enum, required): `us` (Alpaca US), `us-1` (Kraken US), `eu-1` (Kraken EU)

### Historical Trades

`GET /v1beta3/crypto/{loc}/trades`

| Parameter    | Type      | Required | Default | Max   | Description |
|-------------|-----------|----------|---------|-------|-------------|
| `symbols`   | string    | yes      |         |       | Comma-separated (e.g. `BTC/USD,ETH/USD`) |
| `start`     | date-time | no       | start of day |  | RFC-3339 or YYYY-MM-DD |
| `end`       | date-time | no       | now     |       | RFC-3339 or YYYY-MM-DD |
| `limit`     | integer   | no       | 1000    | 10000 | Max data points per page |
| `sort`      | enum      | no       | `asc`   |       | `asc`, `desc` |
| `page_token`| string    | no       |         |       | Pagination token |

**Response**: `trades.{SYMBOL}` → array of trades

```json
{
  "trades": {
    "BTC/USD": [
      {"t": "2022-05-18T12:01:00.537052Z", "p": 29791, "s": 0.0016, "tks": "S", "i": 31455289}
    ],
    "ETH/USD": [
      {"t": "2022-05-18T12:01:00.363547Z", "p": 2027.6, "s": 0.06, "tks": "S", "i": 31455287},
      {"t": "2022-05-18T12:01:00.363547Z", "p": 2027.6, "s": 0.136, "tks": "S", "i": 31455288}
    ]
  },
  "next_page_token": null
}
```

**Trade fields**: `t` (timestamp RFC-3339), `p` (price), `s` (size), `tks` (taker side: `B`/`S`), `i` (trade ID)

### Latest Trades

`GET /v1beta3/crypto/{loc}/latest/trades`

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `symbols` | string | yes      | Comma-separated |

**Response**: `trades.{SYMBOL}` → single trade object (NOT array)

```json
{
  "trades": {
    "BTC/USD": {"t": "2022-05-18T12:01:00.537052Z", "p": 29791, "s": 0.0016, "tks": "S", "i": 31455289},
    "ETH/USD": {"t": "2022-05-18T12:01:00.363547Z", "p": 2027.6, "s": 0.06, "tks": "S", "i": 31455287}
  }
}
```

### Historical Bars

`GET /v1beta3/crypto/{loc}/bars`

| Parameter   | Type      | Required | Default | Max   | Description |
|------------|-----------|----------|---------|-------|-------------|
| `symbols`  | string    | yes      |         |       | Comma-separated |
| `timeframe`| string    | yes      |         |       | `[1-59]Min`, `[1-23]Hour`, `1Day`, `1Week`, `[1,2,3,4,6]Month` |
| `start`    | date-time | no       | start of day |  | RFC-3339 or YYYY-MM-DD |
| `end`      | date-time | no       | now     |       | RFC-3339 or YYYY-MM-DD |
| `limit`    | integer   | no       | 1000    | 10000 | Max data points per page |
| `sort`     | enum      | no       | `asc`   |       | `asc`, `desc` |

**Bar fields**: `t` (timestamp), `o` (open), `h` (high), `l` (low), `c` (close), `v` (volume), `n` (trade count), `vw` (VWAP)

### Historical Quotes

`GET /v1beta3/crypto/{loc}/quotes`

Same params as Historical Bars. **Quote fields**: `t`, `bp` (bid price), `bs` (bid size), `ap` (ask price), `as` (ask size)

### Latest Orderbooks

`GET /v1beta3/crypto/{loc}/latest/orderbooks`

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `symbols` | string | yes      | Comma-separated |

**Response**: `orderbooks.{SYMBOL}` → orderbook object

```json
{
  "orderbooks": {
    "BTC/USD": {
      "t": "2022-06-24T08:00:14.137774336Z",
      "b": [{"p": 20846, "s": 0.1902}, {"p": 20350, "s": 0}],
      "a": [{"p": 20902, "s": 0.0097}, {"p": 21444, "s": 0}]
    }
  }
}
```

**Level format**: Named objects with `p` (price) and `s` (size).

### Snapshots

`GET /v1beta3/crypto/{loc}/snapshots`

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `symbols` | string | yes      | Comma-separated |

Returns combined snapshot per symbol: latest trade, latest quote, minute bar, daily bar, previous daily bar.

---

## 2. Crypto Perpetuals (v1beta1)

All perps endpoints: `GET /v1beta1/crypto-perps/{loc}/latest/...`

**Path param** `loc` (enum, required): `global` (only valid value)

> **Auth required** for all perps endpoints (returns 400 without API key headers).
> Not in our local OpenAPI spec (`alpaca_market_data_openapi.json` — spot only).
> Not implemented by CCXT (`swap: False`, `fetchFundingRate: False`, `fetchOpenInterest: False`).
> Source: Alpaca OpenAPI v1.1 via auto-generated Rust crate `alpaca-market-data-client-rs`.

### Latest Perp Trades

`GET /v1beta1/crypto-perps/{loc}/latest/trades`

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `symbols` | string | yes      | Comma-separated |

**Response**: Same structure as crypto spot latest trades (`trades.{SYMBOL}`).

```json
{
  "trades": {
    "BTCUSDT.P": {
      "t": "2022-05-18T12:01:00.537052Z",
      "p": 29791, "s": 0.0016, "tks": "S", "i": 31455289
    },
    "ETHUSDT.P": {
      "t": "2022-05-18T12:01:00.363547Z",
      "p": 2027.6, "s": 0.06, "tks": "S", "i": 31455287
    }
  }
}
```

Fields: `t` timestamp, `p` price, `s` size, `tks` taker side (`B`/`S`), `i` trade ID.

### Latest Perp Orderbooks

`GET /v1beta1/crypto-perps/{loc}/latest/orderbooks`

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `symbols` | string | yes      | Comma-separated |

**Response**: Same structure as crypto spot latest orderbooks (`orderbooks.{SYMBOL}`).

```json
{
  "orderbooks": {
    "BTCUSDT.P": {
      "t": "2022-06-24T08:00:14.137774336Z",
      "b": [
        { "p": 20846, "s": 0.1902 },
        { "p": 20350, "s": 0 }
      ],
      "a": [
        { "p": 20902, "s": 0.0097 },
        { "p": 21444, "s": 0 }
      ]
    }
  }
}
```

Level format: **named** (`p` = price, `s` = size). `s: 0` = remove level (delta update).

### Latest Perp Bars

`GET /v1beta1/crypto-perps/{loc}/latest/bars`

```json
{
  "bars": {
    "BTCUSDT.P": {
      "t": "2022-05-27T10:18:00Z",
      "o": 28999, "h": 29003, "l": 28999, "c": 29003,
      "v": 0.01, "n": 4, "vw": 29001
    }
  }
}
```

Fields: `t` timestamp, `o/h/l/c` OHLC, `v` volume, `n` trade count, `vw` VWAP.

### Latest Perp Quotes

`GET /v1beta1/crypto-perps/{loc}/latest/quotes`

```json
{
  "quotes": {
    "ETHUSDT.P": {
      "t": "2022-05-26T11:47:18.499478272Z",
      "bp": 1817, "bs": 4.76, "ap": 1817.7, "as": 6.137
    },
    "BTCUSDT.P": {
      "t": "2022-05-26T11:47:18.44347136Z",
      "bp": 29058, "bs": 0.3544, "ap": 29059, "as": 3.252
    }
  }
}
```

Fields: `t` timestamp, `bp` bid price, `bs` bid size, `ap` ask price, `as` ask size.

### Latest Perp Pricing (Funding Rate + OI)

`GET /v1beta1/crypto-perps/{loc}/latest/pricing`

| Parameter | Type   | Required | Description |
|-----------|--------|----------|-------------|
| `symbols` | string | yes      | Comma-separated (e.g. `BTCUSDT.P`) |

> **Perps symbol format**: `BTCUSDT.P` — NOT `BTC/USD` like spot crypto. Suffix `.P` = perpetual.

**Response**: `pricing.{SYMBOL}` → `CryptoPerpFuturesPricing` object

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

| Field | JSON Key | Type   | Description |
|-------|----------|--------|-------------|
| Timestamp | `t` | string | RFC-3339, nanosecond precision |
| Next funding time | `ft` | string | RFC-3339, next funding settlement |
| Open interest | `oi` | float | Open interest value |
| Index price | `ip` | float | Index/spot reference price |
| Mark price | `mp` | float | Mark price (for liquidations) |
| Funding rate | `fr` | float | Current funding rate |

### Perps REST Endpoint Summary

| Endpoint | Auth | Response Key | Description |
|----------|------|-------------|-------------|
| `GET /v1beta1/crypto-perps/global/latest/trades` | ✅ Required | `trades.{SYMBOL}` | Latest perp trades |
| `GET /v1beta1/crypto-perps/global/latest/orderbooks` | ✅ Required | `orderbooks.{SYMBOL}` | Latest perp orderbook |
| `GET /v1beta1/crypto-perps/global/latest/bars` | ✅ Required | `bars.{SYMBOL}` | Latest perp bars |
| `GET /v1beta1/crypto-perps/global/latest/quotes` | ✅ Required | `quotes.{SYMBOL}` | Latest perp quotes |
| `GET /v1beta1/crypto-perps/global/latest/pricing` | ✅ Required | `pricing.{SYMBOL}` | **Funding rate + OI + mark/index price** |

> **No WS perps stream documented** — only REST `latest/*` endpoints.
> **No historical perps data** — only `latest/*` (no time range params).
> **No liquidation feed** — not in OpenAPI spec, not in CCXT, no known endpoint.
> **No LS ratio** — not available.

## CCXT & OpenAPI Cross-Reference Analysis

> Analysis based on CCXT library (`ccxt_alpaca.py`, 1860 lines) and local OpenAPI spec (`alpaca_market_data_openapi.json`).

### CCXT Coverage

| Feature | CCXT `has` | Notes |
|---------|-----------|-------|
| `swap` | `False` | CCXT treats Alpaca as spot-only |
| `fetchFundingRate` | `False` | Not implemented |
| `fetchOpenInterest` | `False` | Not implemented |
| `fetchLiquidations` | `False` | Not implemented |
| `fetchLongShortRatio` | `False` | Not implemented |

CCXT `api.market.public` lists only 8 spot endpoints (`v1beta3/crypto/{loc}/...`). **Zero perps endpoints** in CCXT.

### OpenAPI Spec Coverage

Local spec `alpaca_market_data_openapi.json` (127KB, 48 endpoints) covers:
- ✅ Crypto spot (v1beta3)
- ✅ Stocks (v2)
- ✅ Options (v1beta1)
- ✅ Forex (v1beta1)
- ✅ News, Logos, Screener, Corporate Actions
- ❌ **Crypto Perpetuals** — not in this spec

The perps API exists in a **separate, unpublished OpenAPI spec** (version 1.1, confirmed via Rust crate auto-generation metadata).

### Data Source for Perps Fields

The `CryptoPerpFuturesPricing` struct was extracted from the Rust crate `alpaca-market-data-client-rs` v0.1.0, which was auto-generated from Alpaca's OpenAPI v1.1 spec using `openapi-generator`. Source: `docs/external/alpaca-market-data-client-rs-0.1.0/src/models/crypto_perp_futures_pricing.rs`.

## 3. Crypto WebSocket Streaming

### URL

```
wss://stream.data.alpaca.markets/v1beta3/crypto/{loc}
```

Sandbox: `wss://stream.data.sandbox.alpaca.markets/v1beta3/crypto/{loc}`

Locations: `us` (Alpaca US), `us-1` (Kraken US), `eu-1` (Kraken EU)

### Connection Flow

All messages are **array-wrapped**: `[{...}, {...}]`

```
< [{"T":"success","msg":"connected"}]
> {"action": "auth", "key": "***", "secret": "***"}
< [{"T":"success","msg":"authenticated"}]
> {"action":"subscribe", "trades":["BTC/USD"], "orderbooks":["BTC/USD"]}
< [{"T":"subscription","trades":["BTC/USD"],"quotes":[],"orderbooks":["BTC/USD"],"bars":[],"updatedBars":[],"dailyBars":[]}]
```

### Discriminator: `T` field

| Value          | Type              |
|----------------|-------------------|
| `t`            | Trade             |
| `q`            | Quote             |
| `b`            | Bar (minute)      |
| `o`            | Orderbook         |
| `success`      | Ack (success)     |
| `error`        | Ack (error)       |
| `subscription` | Ack (subscription)|

### Channel: Trades (`T: "t"`)

**Subscribe**: `{"action":"subscribe","trades":["BTC/USD"]}`

| Field | Type   | Description |
|-------|--------|-------------|
| `T`   | string | `"t"` |
| `S`   | string | Symbol (e.g. `"BTC/USD"`) |
| `p`   | float  | Price |
| `s`   | float  | Size |
| `t`   | string | Timestamp (RFC-3339, nanosecond precision) |
| `i`   | int    | Trade ID |
| `tks` | string | Taker side: `"B"` = buyer, `"S"` = seller |

```json
{"T": "t", "S": "AVAX/USD", "p": 47.299, "s": 29.205707815, "t": "2024-03-12T10:27:48.858228144Z", "i": 3447222699101865076, "tks": "S"}
```

### Channel: Quotes (`T: "q"`)

**Subscribe**: `{"action":"subscribe","quotes":["ETH/USD"]}`

| Field | Type   | Description |
|-------|--------|-------------|
| `T`   | string | `"q"` |
| `S`   | string | Symbol |
| `bp`  | float  | Best bid price |
| `bs`  | float  | Best bid size |
| `ap`  | float  | Best ask price |
| `as`  | float  | Best ask size |
| `t`   | string | Timestamp (RFC-3339) |

```json
{"T": "q", "S": "BAT/USD", "bp": 0.35718, "bs": 13445.46, "ap": 0.3581, "as": 13561.902, "t": "2024-03-12T10:29:43.111588173Z"}
```

### Channel: Bars (`T: "b"`)

**Subscribe**: `{"action":"subscribe","bars":["BTC/USD"]}` (also `dailyBars`, `updatedBars`)

Crypto bars contain quote mid-prices. If no trade happens, volume=0 but prices use midpoints.

| Field | Type   | Description |
|-------|--------|-------------|
| `T`   | string | `"b"` |
| `S`   | string | Symbol |
| `o`   | float  | Open |
| `h`   | float  | High |
| `l`   | float  | Low |
| `c`   | float  | Close |
| `v`   | float  | Volume |
| `t`   | string | Timestamp (RFC-3339) |
| `n`   | int    | Trade count |
| `vw`  | float  | VWAP |

```json
{"T": "b", "S": "BTC/USD", "o": 71856.14, "h": 71856.14, "l": 71856.14, "c": 71856.14, "v": 0, "t": "2024-03-12T10:37:00Z", "n": 0, "vw": 0}
```

### Channel: Orderbooks (`T: "o"`)

**Subscribe**: `{"action":"subscribe","orderbooks":["BTC/USD"]}`

| Field | Type    | Description |
|-------|---------|-------------|
| `T`   | string  | `"o"` |
| `S`   | string  | Symbol |
| `t`   | string  | Timestamp (RFC-3339) |
| `b`   | array   | Bids: `[{"p": price, "s": size}, ...]` |
| `a`   | array   | Asks: `[{"p": price, "s": size}, ...]` |
| `r`   | boolean | Reset flag: `true` = full snapshot, absent = delta update |

**Level format**: Named objects with `p` (price), `s` (size). Size `0` = remove level.

```json
{"T": "o", "S": "BTC/USD", "t": "2024-03-12T10:38:50.796Z",
 "b": [{"p": 71859.53, "s": 0.27994}, {"p": 71849.4, "s": 0.553986}],
 "a": [{"p": 71939.7, "s": 0.83953}, {"p": 71940.4, "s": 0.28025}],
 "r": true}
```

---

## 4. Stocks (v2)

### Historical Trades

`GET /v2/stocks/trades` (multi) or `GET /v2/stocks/{symbol}/trades` (single)

| Parameter    | Type      | Required | Default | Max   | Description |
|-------------|-----------|----------|---------|-------|-------------|
| `symbols`   | string    | yes (multi) |      |       | Comma-separated (e.g. `AAPL,TSLA`) |
| `start`     | date-time | no       | start of day |  | RFC-3339 or YYYY-MM-DD |
| `end`       | date-time | no       | now     |       | RFC-3339 or YYYY-MM-DD |
| `limit`     | integer   | no       | 1000    | 10000 | Max data points per page |
| `feed`      | enum      | no       | `sip`   |       | `sip`, `iex`, `otc`, `boats` |
| `currency`  | string    | no       | `USD`   |       | ISO 4217 |
| `asof`      | string    | no       |         |       | YYYY-MM-DD |
| `sort`      | enum      | no       | `asc`   |       | `asc`, `desc` |
| `page_token`| string    | no       |         |       | Pagination token |

**Response**: `trades.{SYMBOL}` → array of trades

```json
{
  "trades": {
    "AAPL": [
      {"t": "2022-01-03T09:00:00.086175744Z", "x": "P", "p": 178.26, "s": 246, "c": ["@", "T"], "i": 1, "z": "C"}
    ]
  },
  "next_page_token": "QUFQTHwy...",
  "currency": "USD"
}
```

**Stock trade fields**: `t` (timestamp), `x` (exchange code), `p` (price), `s` (size), `c` (condition codes array), `i` (trade ID), `z` (tape: `A`=NYSE, `B`=NYSE Arca/Bats/IEX, `C`=NASDAQ, `N`=Overnight, `O`=OTC)

### Latest Trades

`GET /v2/stocks/trades/latest` (multi) or `GET /v2/stocks/{symbol}/trades/latest` (single)

| Parameter | Type   | Required | Default | Description |
|-----------|--------|----------|---------|-------------|
| `symbols` | string | yes      |         | Comma-separated |
| `feed`    | enum   | no       | `sip`   | `sip`, `iex`, `delayed_sip`, `boats`, `overnight`, `otc` |
| `currency`| string | no       | `USD`   | ISO 4217 |

**Response**: `trades.{SYMBOL}` → single trade object (NOT array)

### Historical Quotes

`GET /v2/stocks/quotes` (multi) or `GET /v2/stocks/{symbol}/quotes` (single)

Same params as Historical Trades.

**Stock quote fields**: `t` (timestamp), `ax` (ask exchange), `ap` (ask price), `as` (ask size), `bx` (bid exchange), `bp` (bid price), `bs` (bid size), `c` (condition codes), `z` (tape)

```json
{
  "quotes": {
    "AAPL": [
      {"t": "2022-01-03T09:00:00.028Z", "ax": " ", "ap": 0, "as": 0, "bx": "Q", "bp": 177.92, "bs": 4, "c": ["Y"], "z": "C"}
    ]
  }
}
```

### Latest Quotes

`GET /v2/stocks/quotes/latest` (multi) or `GET /v2/stocks/{symbol}/quotes/latest` (single)

Same params as Latest Trades. **Response**: `quotes.{SYMBOL}` → single quote object.

### Historical Bars

`GET /v2/stocks/bars` (multi) or `GET /v2/stocks/{symbol}/bars` (single)

| Parameter    | Type      | Required | Default | Max   | Description |
|-------------|-----------|----------|---------|-------|-------------|
| `symbols`   | string    | yes      |         |       | Comma-separated |
| `timeframe` | string    | yes      |         |       | `[1-59]Min`, `[1-23]Hour`, `1Day`, `1Week`, `[1-12]Month` |
| `start`     | date-time | no       | start of day |  | RFC-3339 or YYYY-MM-DD |
| `end`       | date-time | no       | now     |       | RFC-3339 or YYYY-MM-DD |
| `limit`     | integer   | no       | 1000    | 10000 | Max data points per page |
| `adjustment`| enum      | no       | `raw`   |       | `raw`, `split`, `dividend`, `all` |
| `feed`      | enum      | no       | `sip`   |       | `sip`, `iex`, `otc`, `boats` |
| `currency`  | string    | no       | `USD`   |       | ISO 4217 |
| `sort`      | enum      | no       | `asc`   |       | `asc`, `desc` |

**Bar fields**: `t`, `o`, `h`, `l`, `c`, `v`, `n` (trade count), `vw` (VWAP)

### Snapshots

`GET /v2/stocks/snapshots` (multi) or `GET /v2/stocks/{symbol}/snapshot` (single)

| Parameter | Type   | Required | Default | Description |
|-----------|--------|----------|---------|-------------|
| `symbols` | string | yes      |         | Comma-separated |
| `feed`    | enum   | no       |         | `sip`, `iex`, `delayed_sip`, `boats`, `overnight`, `otc` |
| `currency`| string | no       | `USD`   | ISO 4217 |

Returns per symbol: `latestTrade`, `latestQuote`, `minuteBar`, `dailyBar`, `prevDailyBar`.

### Auctions

`GET /v2/stocks/auctions` (multi) or `GET /v2/stocks/{symbol}/auctions` (single)

Same params as Historical Trades + `feed` only `sip`.

### Meta

`GET /v2/stocks/meta/exchanges` — Exchange code mappings
`GET /v2/stocks/meta/conditions/{ticktype}` — Condition code meanings (`ticktype`: `trade` or `quote`)

---

## 5. News (v1beta1)

`GET /v1beta1/news`

| Parameter            | Type    | Required | Default | Max | Description |
|---------------------|---------|----------|---------|-----|-------------|
| `start`             | date-time| no      | start of day |  | RFC-3339 or YYYY-MM-DD |
| `end`               | date-time| no      | now     |     | RFC-3339 or YYYY-MM-DD |
| `sort`              | enum    | no       | `desc`  |     | `asc`, `desc` |
| `symbols`           | string  | no       |         |     | Comma-separated symbols to filter |
| `limit`             | integer | no       |         | 50  | Max articles per page |
| `include_content`   | boolean | no       |         |     | Include full article content |
| `exclude_contentless`| boolean | no      |         |     | Exclude articles without content |
| `page_token`        | string  | no       |         |     | Pagination token |

**Response**:

```json
{
  "news": [
    {
      "id": 12345678,
      "headline": "Apple Reports Record Revenue",
      "author": "John Doe",
      "created_at": "2024-01-15T14:30:00Z",
      "updated_at": "2024-01-15T14:30:00Z",
      "summary": "Summary text...",
      "content": "Full article content (if requested, may contain HTML)",
      "url": "https://example.com/article",
      "images": [{"size": "large", "url": "https://..."}],
      "symbols": ["AAPL", "MSFT"],
      "source": "Benzinga"
    }
  ],
  "next_page_token": "..."
}
```

**News article fields**:

| Field        | Type     | Required | Description |
|-------------|----------|----------|-------------|
| `id`        | int64    | yes      | Article ID |
| `headline`  | string   | yes      | Title |
| `author`    | string   | yes      | Author |
| `created_at`| date-time| yes      | Created timestamp (RFC-3339) |
| `updated_at`| date-time| yes      | Updated timestamp (RFC-3339) |
| `summary`   | string   | yes      | Summary (may be first sentence) |
| `content`   | string   | yes      | Full content (may contain HTML) |
| `url`       | uri      | no       | Article URL (nullable) |
| `images`    | array    | yes      | Image URLs (may be empty) |
| `symbols`   | array    | yes      | Related ticker symbols |
| `source`    | string   | yes      | Source (e.g. "Benzinga") |

---

## 6. Logos (v1beta1)

`GET /v1beta1/logos/{symbol}`

| Parameter    | Type    | Required | Default | Description |
|-------------|---------|----------|---------|-------------|
| `symbol`    | string  | yes (path) |       | Ticker symbol |
| `placeholder`| boolean| no       | `true`  | Return placeholder if logo not found |

**Response**: `image/png` binary. Direct image URL for embedding.

**Example**: `https://data.alpaca.markets/v1beta1/logos/AAPL` → PNG image

---

## 7. Screener (v1beta1)

### Most Active Stocks

`GET /v1beta1/screener/stocks/most-actives`

| Parameter | Type    | Required | Default  | Max | Description |
|-----------|---------|----------|----------|-----|-------------|
| `by`      | enum    | no       | `volume` |     | `volume`, `trades` |
| `top`     | integer | no       | 10       | 100 | Number of results |

**Response**:

```json
{
  "most_actives": [
    {"symbol": "AAPL", "volume": 122709184, "trade_count": 639626}
  ]
}
```

### Top Market Movers

`GET /v1beta1/screener/{market_type}/movers`

| Parameter     | Type    | Required | Default | Max | Description |
|--------------|---------|----------|---------|-----|-------------|
| `market_type`| enum    | yes (path) |       |     | `stocks`, `crypto` |
| `top`        | integer | no       | 10      | 50  | Number of gainers AND losers |

**Response**:

```json
{
  "gainers": [
    {"symbol": "AGRI", "percent_change": 145.56, "change": 2.46, "price": 4.15}
  ],
  "losers": [
    {"symbol": "XYZ", "percent_change": -45.2, "change": -1.5, "price": 1.82}
  ]
}
```

---

## 8. Options (v1beta1)

### Historical Trades

`GET /v1beta1/options/trades`

| Parameter    | Type      | Required | Default | Max   | Description |
|-------------|-----------|----------|---------|-------|-------------|
| `symbols`   | string    | yes      |         |       | Comma-separated options symbols |
| `start`     | date-time | no       | start of day |  | RFC-3339 or YYYY-MM-DD |
| `end`       | date-time | no       | now     |       | RFC-3339 or YYYY-MM-DD |
| `limit`     | integer   | no       | 1000    | 10000 | Max data points per page |
| `sort`      | enum      | no       | `asc`   |       | `asc`, `desc` |

### Latest Trades

`GET /v1beta1/options/trades/latest`

### Latest Quotes

`GET /v1beta1/options/quotes/latest`

### Historical Bars

`GET /v1beta1/options/bars`

### Snapshots

`GET /v1beta1/options/snapshots` — multi-symbol
`GET /v1beta1/options/snapshots/{underlying_symbol}` — by underlying

### Meta

`GET /v1beta1/options/meta/exchanges`
`GET /v1beta1/options/meta/conditions/{ticktype}`

---

## 9. Forex (v1beta1)

### Historical Rates

`GET /v1beta1/forex/rates`

| Parameter      | Type      | Required | Default | Description |
|---------------|-----------|----------|---------|-------------|
| `currency_pairs`| string  | yes      |         | Comma-separated (e.g. `EURUSD,GBPUSD`) |
| `timeframe`    | string   | yes      |         | `1Min`, `1Hour`, `1Day` etc. |
| `start`        | date-time| no       |         | RFC-3339 or YYYY-MM-DD |
| `end`          | date-time| no       |         | RFC-3339 or YYYY-MM-DD |
| `limit`        | integer  | no       | 1000    | Max per page |

### Latest Rates

`GET /v1beta1/forex/latest/rates`

---

## 10. Corporate Actions (v1)

`GET /v1/corporate-actions`

---

## Key Facts for EnsoX Integration

| Property | Value |
|----------|-------|
| **Crypto WS URL** | `wss://stream.data.alpaca.markets/v1beta3/crypto/us` |
| **WS discriminator** | `T` (string) |
| **WS messages** | Array-wrapped: `[{...}]` |
| **WS auth** | Required (API key + secret) |
| **Trade WS type** | `"t"` |
| **Orderbook WS type** | `"o"` |
| **Depth level format** | Named objects: `{"p": price, "s": size}` |
| **Depth reset field** | `"r"` (boolean, true = snapshot) |
| **Trade subscribe** | `{"action":"subscribe","trades":["{{symbol}}"]}` |
| **Orderbook subscribe** | `{"action":"subscribe","orderbooks":["{{symbol}}"]}` |
| **Timestamps** | ISO 8601 / RFC-3339, nanosecond precision |
| **Side values** | `"B"` (buyer/taker) / `"S"` (seller/taker) |
| **REST base** | `https://data.alpaca.markets` |
| **REST trades path** | `/v1beta3/crypto/us/trades` |
| **REST response nesting** | `trades.{SYMBOL}` (symbol as key) |
| **REST limit** | 1-10000, default 1000 |
| **REST timestamp** | ISO (same as WS) |
| **Pagination** | `next_page_token` / `page_token` param |
| **Symbol format** | `BTC/USD` (with `/` separator) |
| **Stocks base** | Same base URL, `/v2/stocks/...` |
| **Stock trade fields** | Same short names + `x` (exchange), `c` (conditions), `z` (tape) |
| **News limit** | Max 50 per page |
| **Logo URL** | `https://data.alpaca.markets/v1beta1/logos/{SYMBOL}` → PNG |
| **Screener movers** | Supports both `stocks` and `crypto` market types |

## Feed Options

| Feed        | Description |
|-------------|-------------|
| `sip`       | All US exchanges (default for paid) |
| `iex`       | Investors Exchange (default for free) |
| `delayed_sip` | SIP with 15-min delay |
| `boats`     | Blue Ocean ATS (overnight trading) |
| `overnight` | Derived overnight US trading data |
| `otc`       | Over-the-counter exchanges |
