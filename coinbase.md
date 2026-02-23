# Coinbase API Ecosystem

Coinbase operates **4 separate APIs** that partially overlap. Three separate configs needed.

## The 4 APIs

| API | REST Base | WS Endpoint | WS Auth | Products |
|-----|-----------|-------------|---------|----------|
| **Advanced Trade** | `api.coinbase.com` | `wss://advanced-trade-ws.coinbase.com` | **Public** | ~876 spot + 81 FCM + 208 INTX perps |
| **Exchange** | `api.exchange.coinbase.com` | `wss://ws-feed.exchange.coinbase.com` | **Public** | 789 spot (same engine as AT) |
| **INTX** | `api.international.coinbase.com` | `wss://ws-md.international.coinbase.com` | **HMAC auth** | 218 perps + 42 spot |
| **Derivatives (CDE)** | separate FCM API | N/A | N/A | FCM contracts = same as AT futures |

## Matching Engine Analysis

**Exchange API = Advanced Trade API = SAME matching engine.** Confirmed: sequential `trade_id` values
(Exchange: `963723331–963723335`, AT: `963723360–963723364`). Identical trades, different field formatting.

**INTX = SEPARATE matching engine** with separate trade IDs, but INTX products are surfaced through
the Advanced Trade API (both REST products and WS trades) using `BTC-PERP-INTX` style product IDs.

**Derivatives (CDE) = SAME products as Advanced Trade futures.** FCM nano contracts.

## 3 Configs

| Config | Exchange | Products Filter | WS | REST Recovery | Products |
|--------|---------|----------------|-----|---------------|----------|
| `coinbase.json` | `COINBASE` | `product_type=SPOT` | AT WS | **Exchange API** (1000 trades, pagination) | 876 spot |
| `coinbase_futures.json` | `COINBASE_FUTURES` | `product_type=FUTURE` | AT WS | AT ticker (100 max, no pagination) | 81 FCM |
| `coinbase_intx_futures.json` | `COINBASE_INTX_FUTURES` | `contract_expiry_type=PERPETUAL` | AT WS | AT ticker (100 max, no pagination) | 208 INTX perps |

### Volume Comparison (24h, BTC)

| Venue | Instrument | 24h Notional |
|-------|-----------|-------------|
| AT Spot | `BTC-USD` | **$579M** |
| FCM Futures | `BIP-20DEC30-CDE` | **$405M** |
| INTX Perps | `BTC-PERP-INTX` | **$2,367M** |

Zero product overlap verified across all 3 configs.

---

## Exchange Quirks

### 1. Dual REST Hosts (Spot Recovery)
Spot products come from `api.coinbase.com` (Advanced Trade) but recovery uses `api.exchange.coinbase.com`
(Exchange API) for better pagination. Uses `history_base_url` field in config to override `base_url` for recovery only.

### 2. FCM/INTX Recovery Limitation
Exchange API returns `NotFound` for FCM (`BIP-20DEC30-CDE`) and INTX (`BTC-PERP-INTX`) products.
Recovery for these uses Advanced Trade ticker endpoint: **max 100 trades, no pagination cursor.**
100 trades ≈ 19 seconds of BTC data. Only short disconnections can be recovered.

### 3. INTX WS is Auth-Gated
`wss://ws-md.international.coinbase.com` connects and subscribes successfully, then immediately returns
`Unauthorized User` (close code 3000). All INTX market data must come through the Advanced Trade WS.

### 4. INTX Products Need Special Query
`product_type=FUTURE` alone returns only 81 FCM products. INTX perpetuals require the additional
`contract_expiry_type=PERPETUAL` parameter, returning 208 products on `INTX` venue.

### 5. FCM Futures Symbol Format
FCM products use contract-code symbols (`BIP-20DEC30-CDE`) not clean perp symbols.
`base_currency_id` is **empty** — must use `future_product_details.contract_root_unit` for base coin.
Contract sizes are nano: BTC=0.01, ETH=0.1, SOL=5, XRP=500, SHIB=10000.
Includes commodities: Gold (`CDEGLD`), Silver (`CDESIL`), Oil (`CDEOIL`), Copper (`CDECU`).

### 6. WS Depth Uses Mixed Named Format
L2 depth combines bids and offers in single `updates` array. Each level has `side: "bid"|"offer"`,
`price_level`, `new_quantity`. Engine uses `level_format: mixed_named`. Snapshots are ~1,184 levels
(~622 bids, ~562 offers). Delta rate: ~19 updates/sec for BTC.

### 7. Exchange API vs Advanced Trade Field Differences
Same trades, different formatting:
- **Exchange**: `side: "sell"` (lowercase), `price: "67146.63000000"` (trailing zeros), raw array response
- **Advanced Trade**: `side: "SELL"` (uppercase), cleaner prices, response wrapped in `trades` key

### 8. FIX API (INTX)
FIX Market Data available at `tcp+ssl://fix.international.coinbase.com:6120` but requires
FIX session-level auth (Logon with credentials). Not usable without institutional account.

---

## Advanced Trade WS Message Formats

### Trade (`market_trades` channel)
```json
{
  "channel": "market_trades",
  "events": [{
    "type": "update",
    "trades": [{
      "trade_id": "963696120", "product_id": "BTC-USD",
      "price": "67231.87", "size": "0.003",
      "time": "2026-02-18T16:42:26.685302Z", "side": "BUY"
    }]
  }]
}
```

### Depth (`level2` → `l2_data` channel)
```json
{
  "channel": "l2_data",
  "events": [{
    "type": "snapshot",
    "product_id": "BTC-USD",
    "updates": [
      {"side":"bid","event_time":"...","price_level":"67217.09","new_quantity":"0.0000967"},
      {"side":"offer","event_time":"...","price_level":"67300.00","new_quantity":"0.5"}
    ]
  }]
}
```

### Exchange API REST Trades (Recovery — spot only)
```json
[
  {"trade_id": 963733649, "side": "buy", "size": "0.00010604",
   "price": "67143.18000000", "time": "2026-02-18T17:58:39.395740Z"}
]
```
Raw array (no wrapper). Pagination: `cb-before`/`cb-after` headers. Max `limit=1000`.

### Advanced Trade REST Trades (Recovery — futures/INTX)
```json
{
  "trades": [
    {"trade_id": "547093680289218579", "product_id": "BTC-PERP-INTX",
     "price": "67077.9", "size": "0.0997",
     "time": "2026-02-18T17:54:57.890519Z", "side": "BUY"}
  ],
  "best_bid": "...", "best_ask": "..."
}
```
Wrapped in `trades` key → needs `history_json_path: "trades"`. Max `limit=100`. No pagination.
