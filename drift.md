# Drift Protocol — DLOB + Data API Documentation

Source: https://drift-labs.github.io/v2-teacher/ (`drift_api.html`)
OpenAPI: https://data.api.drift.trade/playground/json

## Endpoints

| Service | URL |
|---------|-----|
| DLOB REST (mainnet) | `https://dlob.drift.trade/` |
| DLOB WS (mainnet) | `wss://dlob.drift.trade/ws` |
| Data API (mainnet) | `https://data.api.drift.trade` |
| Data API Playground | `https://data.api.drift.trade/playground` |

## Rate Limiting
- REST API is rate limited (exact limit varies by endpoint + load)
- 429 = too many requests, exponential backoff recommended
- Responses may be cached for seconds to minutes

---

## DLOB WebSocket

### Subscribe Messages

Per-market subscribe. Channels: `trades`, `fills`, `orderbook`.

```json
{"type": "subscribe", "marketType": "perp", "channel": "trades", "market": "SOL-PERP"}
{"type": "subscribe", "marketType": "perp", "channel": "orderbook", "market": "SOL-PERP"}
```

### Heartbeat / Keepalive

- Server sends `{"channel": "heartbeat"}` every 5 seconds
- No server ping messages — unsolicited pings get pongs back
- Server stops sending if client has >50 unprocessed messages in buffer (backpressure)
- `ping_type: "native"` (WS-level PING/PONG) is sufficient for keepalive

### Orderbook Messages

Channel value in response: `orderbook_perp_0` (includes market type + index).
Update frequency: every 400ms. Full L2 snapshot each time.

**Envelope:**
```json
{"channel": "orderbook_perp_0", "data": "<double-encoded JSON string>"}
```

**Inner `data` fields:**

| Field | Type | Description |
|-------|------|-------------|
| `bids` | array | `[{price, size, sources}, ...]` — bid orders |
| `asks` | array | `[{price, size, sources}, ...]` — ask orders |
| `marketName` | string | e.g. `"SOL-PERP"` |
| `marketType` | string | `"perp"` or `"spot"` |
| `marketIndex` | int | Numeric market ID |
| `slot` | int | Solana slot |
| `oracle` | string | Oracle price |

**Level format**: Named objects `{price, size, sources}`. Sources: `"vamm"`, `"dlob"`, `"phoenix"`, `"serum"`.

**Note**: `data` field is a **double-encoded JSON string** — needs two JSON decodes.

### Trade Messages

Channel value in response: `trades_perp_0`.

**Inner `data` fields (perp):**

| Field | Type | Description |
|-------|------|-------------|
| `ts` | int | Unix timestamp (seconds) |
| `marketIndex` | int | Market numeric ID |
| `marketType` | string | `"perp"` |
| `filler` | string | Filler address |
| `takerFee` | string | Taker fee |
| `makerFee` | string | Maker fee |
| `baseAssetAmountFilled` | string | Base qty filled (human-readable) |
| `quoteAssetAmountFilled` | string | Quote qty filled |
| `takerOrderDirection` | string | `"long"` or `"short"` |
| `oraclePrice` | string | Oracle price at time of trade (human-readable) |
| `txSig` | string | Transaction signature |
| `slot` | int | Solana slot |
| `action` | string | `"fill"` |
| `actionExplanation` | string | See below |
| `symbol` | string | `"SOL-PERP"` (in REST trades) |

**`actionExplanation` values** (from real data):
- `orderFilledWithMatch` — limit order matched with another limit order
- `orderFilledWithMatchJit` — JIT maker filled
- `orderFilledWithAmm` — filled against AMM
- `orderFilledWithAmmJit` — AMM JIT fill
- `liquidation` — **liquidation fill** (from SDK: `liquidate_perp`, `liquidate_borrow`, `liquidate_perp_pnl_for_deposit`, `liquidate_borrow_for_perp_pnl`)

**Side derivation**: `takerOrderDirection` — `"long"` = buy, `"short"` = sell.

---

## DLOB REST Endpoints

### GET /l2

L2 orderbook snapshot.

**Parameters**: `marketIndex` (int), `marketType` (`"perp"` or `"spot"`), `depth` (optional)

**Example**: `https://dlob.drift.trade/l2?marketIndex=0&marketType=perp`

**Real response** (raw precision — divide price by 10^6, size by 10^9):
```json
{
  "bids": [
    {"price": "88251000", "size": "38900000000", "sources": {"dlob": "38900000000"}}
  ],
  "asks": [
    {"price": "88300000", "size": "10000000000", "sources": {"dlob": "10000000000"}}
  ]
}
```

---

## Data API — REST Endpoints (Complete List from OpenAPI)

All under `https://data.api.drift.trade`.

### Products & Markets

| Endpoint | Purpose |
|----------|---------|
| `GET /stats/markets` | All perp and spot markets (products catalog) |
| `GET /stats/markets/prices` | Current market prices |
| `GET /stats/markets/volume` | Volume stats |
| `GET /stats/markets/volume/{interval}` | Volume by interval |
| `GET /contracts` | Contract info — current funding + OI for all perps (CoinGecko format) |

### Historical Trades ✅

| Endpoint | Purpose |
|----------|---------|
| `GET /market/{symbol}/trades` | **Recent trades, paginated via cursor** |
| `GET /market/{symbol}/trades/{year}/{month}/{day}` | Daily CSV trade records |

**Real response** from `/market/SOL-PERP/trades`:
```json
{
  "records": [
    {
      "ts": 1772785819,
      "txSig": "66tNKLGr...",
      "baseAssetAmountFilled": "0.260000000",
      "quoteAssetAmountFilled": "22.975420",
      "oraclePrice": "88.377245",
      "action": "fill",
      "actionExplanation": "orderFilledWithAmmJit",
      "takerOrderDirection": "long",
      "symbol": "SOL-PERP",
      "marketIndex": 0
    }
  ],
  "meta": {
    "nextPage": "eyJwayI6Ik1..."
  }
}
```

**Key fields for recovery**: `ts` (unix seconds), `oraclePrice` (human-readable), `baseAssetAmountFilled` (human-readable), `takerOrderDirection` (`long`/`short`), `symbol`.

**Pagination**: Cursor-based via `meta.nextPage`. Pass as `?page={nextPage}`.

**Liquidation detection**: `actionExplanation` contains `"liquidation"` for liquidation fills.

### Funding Rates ✅

| Endpoint | Purpose |
|----------|---------|
| `GET /market/{symbol}/fundingRates` | Recent funding rates (last 30 days) |
| `GET /market/{symbol}/fundingRates/{year}/{month}/{day}` | Daily CSV |
| `GET /stats/fundingRates` | Aggregate funding stats |

**Real response** from `/market/SOL-PERP/fundingRates`:
```json
{
  "fundingRates": [
    {
      "ts": "1770195607",
      "fundingRate": "-3095708",
      "oraclePriceTwap": "97493700",
      "markPriceTwap": "97399905",
      "marketIndex": 0
    }
  ]
}
```

**Precision**: `fundingRate` raw (÷1e9). `oraclePriceTwap` raw (÷1e6). Percentage: `(fundingRate/1e9) / (oraclePriceTwap/1e6)`.

**Note**: The older `GET /fundingRates?marketName=X` also works but the new path format is `/market/{symbol}/fundingRates`.

### Liquidations ✅

| Endpoint | Purpose |
|----------|---------|
| `GET /stats/liquidations` | **Global liquidation records** |

**Real response**:
```json
{
  "success": true,
  "stats": {"24h": {"count": "19", "amount": "32969.54"}, "30d": {"count": "33770", "amount": "26011636.98"}},
  "records": [
    {
      "ts": 1772772066,
      "liquidationType": "liquidatePerpPnlForDeposit",
      "user": "3uf8DhdR...",
      "liquidator": "42vtDSVn...",
      "totalCollateral": "-391.051618",
      "marginFreed": "36.459404",
      "liquidatePerp_marketIndex": 0,
      "liquidatePerp_oraclePrice": "0.000000",
      "liquidatePerp_baseAssetAmount": "0.000000000"
    }
  ]
}
```

**`liquidationType` values**: `liquidatePerp`, `liquidateBorrow`, `liquidateBorrowForPerpPnl`, `liquidatePerpPnlForDeposit`.

### Open Interest

| Endpoint | Purpose |
|----------|---------|
| `GET /contracts` | Current OI per market (`open_interest` field, human-readable) |
| `GET /amm/openInterest` | AMM-specific OI (needs params) |

### Candles

| Endpoint | Purpose |
|----------|---------|
| `GET /market/{symbol}/candles/{resolution}` | OHLCV candles |

**Resolutions**: 1 (1m), 15 (15m), 60 (1h), 240 (4h), D (1d), W (1w).

### Other Endpoints

| Endpoint | Purpose |
|----------|---------|
| `GET /amm/bidAskPrice` | AMM bid/ask prices |
| `GET /amm/oraclePrice` | Current oracle prices |
| `GET /amm/position` | AMM position info |
| `GET /amm/spreads` | AMM spreads |
| `GET /stats/bankruptcies` | Bankruptcy records |
| `GET /stats/leaderboard` | Trading leaderboard |
| `GET /stats/insuranceFund` | Insurance fund stats |

---

## Numerical Precisions

| Value | Context | Raw Unit | Divisor | Example |
|-------|---------|----------|---------|---------|
| Price | DLOB REST `/l2` | integer | 10^6 | `88251000` → `88.251` |
| Size/Qty | DLOB REST `/l2` | integer | 10^9 | `38900000000` → `38.9` |
| Price | Data API `/trades` | string | 1 (human-readable) | `"88.377245"` |
| Size/Qty | Data API `/trades` | string | 1 (human-readable) | `"0.260000000"` |
| Funding Rate | `/fundingRates` | integer | 10^9 | `-3095708` → `-0.003096` |
| Oracle TWAP | `/fundingRates` | integer | 10^6 | `97493700` → `97.4937` |
| Funding Rate | `/contracts` | string | 1 (human-readable) | `"-0.001338082"` |
| OI | `/contracts` | string | 1 (human-readable) | `"852580.600000000"` |

---

## Historical Data Availability Summary

| Metric | REST Endpoint | Pagination | Timestamp |
|--------|--------------|------------|-----------|
| **Trades** | `/market/{symbol}/trades` | Cursor (`meta.nextPage`) | `ts` = unix seconds |
| **Trades (daily)** | `/market/{symbol}/trades/{y}/{m}/{d}` | N/A (CSV) | — |
| **Funding** | `/market/{symbol}/fundingRates` | Last 30 days | `ts` = unix seconds (string) |
| **Funding (daily)** | `/market/{symbol}/fundingRates/{y}/{m}/{d}` | N/A (CSV) | — |
| **Liquidations** | `/stats/liquidations` | Records array | `ts` = unix seconds |
| **OI (live)** | `/contracts` | All markets bulk | — |

---

## `GET /stats/markets` — Products Response

```json
{
  "success": true,
  "markets": [
    {
      "symbol": "SOL-PERP",
      "marketIndex": 0,
      "marketType": "perp",
      "baseAsset": "SOL",
      "quoteAsset": "USDC",
      "status": "active",
      "precision": 9,
      "oraclePrice": "88.379472",
      "openInterest": {"long": "424391.18", "short": "-428628.49"},
      "fundingRate": {"long": "0.001242", "short": "-0.001242"}
    }
  ]
}
```

## `GET /contracts` — Contract Info Response

```json
{
  "contracts": [
    {
      "contract_index": 0,
      "ticker_id": "SOL-PERP",
      "base_currency": "SOL",
      "quote_currency": "USDC",
      "product_type": "PERP",
      "open_interest": "852580.600000000",
      "funding_rate": "-0.001338082",
      "next_funding_rate": "-0.001321",
      "next_funding_rate_timestamp": "1772787604000"
    }
  ]
}
```

**Note**: `/contracts` uses `ticker_id` for symbol (not `symbol`). `open_interest` and `funding_rate` are human-readable.

## Market Index → Symbol Mapping

Subscribe uses `market: "SOL-PERP"` but responses return `marketIndex: 0`. The adapter fetches `/stats/markets` at startup to build the `marketIndex → symbol` map.
