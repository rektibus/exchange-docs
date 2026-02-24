# Bitnomial Exchange API Reference

> **Type**: CFTC-regulated derivatives exchange (DCM + DCO + FCM)
> **Products**: BTC/ETH/SOL/XRP/LINK/DOGE/ADA/DOT/LTC/AVAX/XLM/SUI/XTZ/HBAR futures, 1 BTC perp, 1 BTC spot, options, spreads
> **REST base URL**: `https://bitnomial.com/exchange/api/v1/prod/`
> **WS URL**: `wss://bitnomial.com/exchange/ws`
> **Sandbox WS**: `wss://bitnomial.com/exchange/sandbox/ws`
> **Rate limit**: 200 requests / 5 minutes (REST). HTTP 403 on exceed.
> **Timestamps**: ISO 8601 with nanosecond precision (e.g. `2022-09-28T16:06:39.022836179Z`)
> **API probed**: 2026-02-18 ✅

---

## Products

### GET `/product/specs/`
Returns **flat array** of all product specs. No pagination wrapper.

**Query params**: `active=true`, `base_symbol=BUS`, `day=YYYY-MM-DD`

**Response** (flat array):
```json
[
  {
    "type": "future",
    "product_id": 1281,
    "product_name": "Bitcoin US Dollar Future",
    "symbol": "BUSH26",
    "base_symbol": "BUS",
    "contract_size": 1,
    "contract_size_unit": "BTC",
    "price_increment": 1,
    "price_quotation_unit": "USD per BTC",
    "margin_unit": "USD",
    "settlement_method": "Deliverable",
    "max_order_quantity": 100,
    "min_block_size": 5,
    "month": 3,
    "year": 2026,
    "first_trading_day": "2025-03-31",
    "final_settle_time": "2026-03-27T15:00:00Z",
    "daily_open_time": "19:00:00",
    "daily_settle_time": "16:00:00",
    "product_status": "active",
    "cqg_symbol": "BBUSH26",
    "price_band_variation": 1000,
    "price_limit_percentage": 0.5
  }
]
```

**Product types**: `future`, `perpetual`, `spot`, `spread`, `option`

### GET `/product/data/`
Returns **flat array** of live product data (OHLCV, OI, settlement).

**Response** (flat array):
```json
[
  {
    "product_id": 1281,
    "last_price": 87150,
    "last_price_time": "2026-02-17T21:05:00.037575Z",
    "settlement_price": 87150,
    "settlement_time": "2026-02-17T21:05:00.037575Z",
    "open_price": null,
    "high_price": null,
    "low_price": null,
    "close_price": null,
    "price_change": 3.27,
    "volume": 45,
    "notional_volume": 3921750.0,
    "block_volume": 0,
    "notional_block_volume": 0.0,
    "open_interest": 392,
    "open_interest_change": 10,
    "price_limit_upper": 134000,
    "price_limit_lower": 40000
  }
]
```

> **Price units**: All prices in ticks. `price_in_usd = price × price_increment`
> **Notional volume**: In cents. `usd = notional_volume / 100`

### Active Product Catalog (probed 2026-02-18)

| base_symbol | Type | contract_size | Unit | Count | Sample Symbol |
|-------------|------|---------------|------|-------|---------------|
| **BTCUSD** | spot | 0.00001 | BTC | 1 | `BTCUSD` |
| **BUS** | future | 1 | BTC | 6 | `BUSH26` |
| **BUI** | future | 0.1 | BTC | 6 | `BUIH26` |
| **BUC** | future | 0.01 | BTC | 6 | `BUCH26` |
| **BUC** | perpetual | 0.01 | BTC | 1 | `PBUCZ50` |
| **ETUD** | future | 10 | ETH | 6 | `ETUDH26` |
| **ETUI** | future | 0.1 | ETH | 6 | `ETUIH26` |
| **SOUH** | future | 100 | SOL | 6 | `SOUHH26` |
| **XRUH** | future | 100 | XRP | 6 | `XRUHH26` |
| **XRUY** | future | 10000 | XRP | 6 | `XRUYH26` |
| **CLUK** | future | 1000 | LINK | 6 | `CLUKH26` |
| **DGUN** | future | 100000 | DOGE | 6 | `DGUNH26` |
| **ADUY** | future | 10000 | ADA | 6 | `ADUYH26` |
| **PDUY** | future | 10000 | DOT | 6 | `PDUYH26` |
| **LTUH** | future | 100 | LTC | 6 | `LTUHH26` |
| **ALUK** | future | 1000 | AVAX | 6 | `ALUKH26` |
| **SUUH** | future | 100 | SUI | 6 | `SUUHH26` |
| **HBUN** | future | 100000 | HBAR | 6 | `HBUNH26` |
| **STUN** | future | 100000 | XLM | 6 | `STUNH26` |
| **APUH** | future | 100 | APT | 6 | `APUHH26` |
| **TEUK** | future | 1000 | XTZ | 6 | `TEUKG26` |
| **BCUH** | future | 100 | BCH | 6 | `BCUHH26` |
| **UCUY** | future | 10000 | USDC | 6 | `UCUYH26` |
| **HUP** | future | 30 | pH/s/d | 3 | `HUPG26` |

Plus 536 options and 86 spreads (not relevant for EnsoX).

---

## WebSocket

### Connection
```
wss://bitnomial.com/exchange/ws
```

### Discriminator: `type` field
All messages have a `type` field for classification.

### Subscribe Format
Send JSON with `type: "subscribe"` and product codes:
```json
{"type": "subscribe", "channel": "trade", "product_codes": ["BUS"]}
{"type": "subscribe", "channel": "book", "product_codes": ["BUS"]}
```

Product codes can be:
1. **Exact symbol**: `BUSH26` → only that product
2. **Base symbol**: `BUS` → ALL futures with that base symbol
3. **Options**: `BUSO` → all options with BUS underlying

### Trade Channel
**type**: `"trade"`

```json
{
  "type": "trade",
  "ack_id": "7148460953766461527",
  "price": 19000,
  "quantity": 10,
  "symbol": "BUSZ22",
  "taker_side": "Bid",
  "timestamp": "2022-09-28T16:06:39.022836179Z"
}
```

| Field | Type | Notes |
|-------|------|-------|
| `type` | string | Always `"trade"` |
| `ack_id` | string | Trade ID (numeric string) |
| `price` | number | In ticks (×price_increment for USD) |
| `quantity` | number | In contracts |
| `symbol` | string | Product symbol (e.g. `BUSH26`) |
| `taker_side` | string | `"Bid"` (buy) or `"Ask"` (sell) |
| `timestamp` | string | ISO 8601 with nanosecond precision |

### Book Channel (Snapshot)
**type**: `"book"`

```json
{
  "type": "book",
  "ack_id": "7148460953766461532",
  "asks": [[21000, 10], [22000, 10]],
  "bids": [[19000, 15], [18000, 10]],
  "symbol": "BUSZ22",
  "timestamp": "2022-09-28T16:07:36.93709645Z"
}
```

Asks/bids are `[price, quantity]` tuples, sorted best-first. Level format: **indexed** with `price_index=0, size_index=1`.

### Level Channel (Book Updates)
**type**: `"level"`

```json
{
  "type": "level",
  "ack_id": "7148460953766461522",
  "price": 20000,
  "quantity": 10,
  "side": "Bid",
  "symbol": "BUSZ22",
  "timestamp": "2022-09-28T16:04:32.357586392Z"
}
```

`quantity = 0` means level removed. Apply if `level.ack_id > book.ack_id`.

> **NOTE**: Level updates are NOT in the standard depth array format — each level is a separate message with `price`, `quantity`, `side` fields, not `bids`/`asks` arrays. This requires special handling (not standard `indexed` depth format). Each level update modifies a single price level in the local orderbook.

### Block Trade Channel
**type**: `"block"`

```json
{
  "type": "block",
  "ack_id": "7148466850756558935",
  "leader_side": "Bid",
  "price": 19500,
  "quantity": 10,
  "symbol": "BUSZ22",
  "timestamp": "2022-09-28T16:26:01.440681563Z"
}
```

Same as trade but with `leader_side` instead of `taker_side`.

### Side Values
| Wire Value | Meaning |
|-----------|---------|
| `Bid` | Buy |
| `Ask` | Sell |

---

## REST Endpoints

### Funding Rates

#### GET `/funding-rates/`
**Paginated** (`{"data": [...], "pagination": {"cursor": "..."}}`)

**Params**: `product_id`, `base_symbol` (e.g. `PBUC`), `limit`, `begin_time`, `end_time`, `order` (asc/desc), `cursor`

```json
{
  "data": [
    {
      "product_id": 123,
      "price_index": 101234.56,
      "mark_price": 101250.00,
      "interest_rate": 0.0001,
      "funding_rate": 0.000125,
      "interval_start": "2025-12-12T00:00:00Z",
      "interval_end": "2025-12-12T08:00:00Z"
    }
  ],
  "pagination": {"cursor": "eyJsYXN0X2lkIjoxMjM0NX0="}
}
```

Funding intervals: 8h (00:00, 08:00, 16:00 UTC).

#### GET `/funding-rates/estimated/:base_symbol`
Not paginated. Returns estimated current-interval funding rate.

```json
{"funding_rate": 0.000089, "interval_start": "2025-12-12T08:00:00Z", "interval_end": "2025-12-12T16:00:00Z"}
```

### Charts

#### GET `/web/charts/price/:product_id`
**Flat array**. Historical OHLCV.

**Params**: `begin_time`, `end_time`

```json
[
  {
    "date": "2025-12-14",
    "time": "2025-12-14T21:30:00.000000Z",
    "ohlc": {
      "open": "87500.0000000000",
      "high": "88200.0000000000",
      "low": "86800.0000000000",
      "close": "87100.0000000000",
      "volume": 45
    },
    "settlementPrice": "87150.0000000000"
  }
]
```

> Prices here are already in USD (unlike product data which is in ticks).

#### GET `/web/charts/voi`
**Flat array**. Historical Volume + Open Interest.

**Params**: `product_id` (can repeat for multi-product aggregation), `begin_time`, `end_time`

```json
[
  {
    "date": "2025-12-01",
    "productId": 1547,
    "baseSymbol": "PBU",
    "volume": 27,
    "notionalVolume": 2365870,
    "openInterest": 392,
    "notionalOpenInterest": 33806080
  }
]
```

> `notionalVolume` and `notionalOpenInterest` in **cents** (÷100 for USD).

### Market Stats

#### GET `/web/market/stats/trailing/all-products`
**Flat array**. 24h trailing stats.

```json
[{"productId": 1547, "volume": 27, "notionalVolume": 23658}]
```

> `notionalVolume` here is already in USD (NOT cents, unlike VOI charts).

#### GET `/web/market/stats/trailing/:product_id`
Single product trailing stats.

### Block Trades

#### GET `/block-trades/`
Block trade history. Params: `product_id`, `begin_time`, `end_time`, `limit`.

---

## Pagination

All paginated endpoints use:
```json
{"data": [...], "pagination": {"cursor": "base64_encoded_cursor"}}
```

Pass `cursor` query param to get next page. Currently only `CursorInfo` pagination type.

---

## Key Integration Notes

1. **No public REST trades endpoint** — trade history requires authenticated `/fills/` endpoint. Only WS provides live trades.
2. **Prices in ticks** — multiply by `price_increment` from product spec for USD. Exception: `/web/charts/price/` returns prices already in USD.
3. **ISO 8601 timestamps** with nanosecond precision everywhere.
4. **Product symbol format** — symbols include month/year codes: `BUSH26` = BTC USD future, H=March, 26=2026. Perps: `PBUCZ50`.
5. **Single WS connection** — subscribe to multiple channels/products on one connection.
6. **Book updates via individual level messages** — not batched bid/ask arrays like most exchanges.
7. **contract_size varies** — BUS=1 BTC, BUI=0.1, BUC=0.01. For ETH: ETUD=10, ETUI=0.1.
8. **Rate limit** — 200 req/5min is very low. REST probing should be minimal.
9. **Futures expire** — symbols change quarterly. `base_symbol` filter is stable.
