# Drift Protocol API Documentation (Consolidated)

> Sources: [Official Docs](https://drift-labs.github.io/v2-teacher/), REST API probes (2026-02-19)
> Drift is a Solana-based DEX with DLOB (Decentralized Limit Order Book)

---

## 1. DLOB WebSocket API

**URL**: `wss://dlob.drift.trade/ws` (mainnet-beta)

### Connection
- No compression
- Native ping/pong
- Heartbeat: server sends `{"channel":"heartbeat"}` every 5s
- Max 50 unprocessed messages in buffer before server stops sending
- No ping messages from server; unsolicited pings get pongs back

### Subscribe Format
```json
{
  "type": "subscribe",
  "marketType": "perp",       // "perp" or "spot"
  "channel": "trades",         // "trades" or "orderbook"
  "market": "SOL-PERP"        // e.g. "SOL-PERP", "BTC-PERP"
}
```

### Ack Response
```json
{"message":"Subscribe received for channel: trades, market: SOL-PERP, marketType: perp"}
```
Discriminator: `message` field present = ack

### Trade Push
```json
{
  "channel": "trades_perp_0",
  "data": "{...}"    // stringified JSON
}
```
Note: `data` is a **stringified JSON string**, not a nested object. Requires `JSON.parse(message.data)`.
The channel name is `trades_{marketType}_{marketIndex}`.

### Orderbook Push
```json
{
  "channel": "orderbook_perp_0_grouped_1",
  "data": "{\"bids\":[{\"size\":61040000000,\"price\":81868100,\"sources\":{\"vamm\":61040000000}},...],\"asks\":[...]}"
}
```
- **Prices**: raw integer (divide by 1e6 for USD price, e.g. `81868100` → `$81.8681`)
- **Sizes**: raw integer (divide by 1e9 for SOL, precision varies per market)
- Updates every 400ms (full snapshot each time)
- `data` is a **stringified JSON string**

### Unsubscribe
```json
{"type":"unsubscribe","marketType":"perp","channel":"orderbook","market":"SOL-PERP"}
```

---

## 2. Data API (REST)

**Base URL**: `https://data.api.drift.trade`

### GET /contracts
Returns contract info for all markets (funding rate + OI).

**Response** (147 items):
```json
{
  "contracts": [
    {
      "contract_index": 0,
      "ticker_id": "SOL-PERP",
      "base_currency": "SOL",
      "quote_currency": "USDC",
      "last_price": "81.644503",
      "base_volume": "385160.620000000",
      "quote_volume": "32232930.657246",
      "high": "86.093400",
      "low": "80.458394",
      "product_type": "PERP",
      "open_interest": "943191.730000000",
      "index_price": "81.683295",
      "funding_rate": "0.000281332",
      "next_funding_rate": "0.000039",
      "next_funding_rate_timestamp": "1771480806000",
      "start_timestamp": "1667560505000",
      "end_timestamp": "1771478151595"
    }
  ]
}
```

### GET /stats/markets
Returns stats for all markets (136 items including spot + perp).

**Response**:
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
      "oraclePrice": "81.889579",
      "markPrice": "81.856150",
      "baseVolume": "389070.700000",
      "quoteVolume": "32153510.020148",
      "openInterest": {
        "long": "471252.73",
        "short": "-471093.53"
      },
      "fundingRate": {
        "long": "-0.000022",
        "short": "0.000022"
      },
      "fundingRate24h": "-0.001100",
      "fundingRateUpdateTs": 1771477206,
      "price": "81.891500",
      "priceChange24h": "-3.054300",
      "priceChange24hPercent": "-3.60"
    }
  ]
}
```

### GET /stats/fundingRates
Aggregated funding rates per market.

**Response** (73 perp markets):
```json
{
  "success": true,
  "markets": [
    {
      "marketIndex": 0,
      "symbol": "SOL-PERP",
      "fundingRates": {
        "24h": "-0.001275543",
        "7d": "-0.001733966",
        "30d": "-0.002012817",
        "1y": "-0.000692263"
      }
    }
  ]
}
```

### GET /fundingRates?marketName={symbol}
Historical funding rates for a specific market (last 30 days).

**Query params**: `marketName=SOL-PERP`

**Response**:
```json
{
  "fundingRates": [
    {
      "txSig": "...",
      "slot": 123456,
      "ts": 1771477206,
      "recordId": 12345,
      "marketIndex": 0,
      "fundingRate": "123456789",
      "oraclePriceTwap": "81889579000",
      "cumulativeFundingRateLong": "...",
      "cumulativeFundingRateShort": "...",
      "markPriceTwap": "...",
      "fundingRateLong": "...",
      "fundingRateShort": "...",
      "periodRevenue": "...",
      "baseAssetAmountWithAmm": "...",
      "baseAssetAmountWithUnsettledLp": "..."
    }
  ]
}
```

**Funding rate calculation**:
```
fundingRatePct = (fundingRate / 1e9) / (oraclePriceTwap / 1e6)
fundingRatePctApr = fundingRatePct * 24 * 365
```

---

## 3. Dedicated Adapter Notes

- Drift uses a **dedicated Elixir adapter** (`drift.ex`) because:
  - WS `data` field contains **stringified JSON** (needs double-parse)
  - Prices/sizes are in Solana precision (1e6 / 1e9) requiring normalization
  - Funding and OI are polled via REST (not available on WS)
  - Trade messages may have a unique format requiring Elixir-side normalization
- Products: available at `/stats/markets` (136 items) or `/contracts` (147 items)
- Products fields: `symbol` ("SOL-PERP"), `baseAsset`/`base_currency` ("SOL"), `quoteAsset`/`quote_currency` ("USDC")
- Trade history: S3 flat files deprecated Jan 2025, Data API is the replacement but no simple paginated REST trades endpoint found

---

## 4. Key Notes for EnsoX Config

| Field | Value |
|-------|-------|
| WS URL | `wss://dlob.drift.trade/ws` |
| WS Discriminator | `channel` field (`trades_perp_*`, `orderbook_perp_*`, `heartbeat`) |
| Subscribe | `{type: "subscribe", channel: "trades"/"orderbook", market: "SOL-PERP", marketType: "perp"}` |
| Ack | `message` field present |
| Heartbeat | `{"channel": "heartbeat"}` every 5s |
| Compression | none |
| Ping/pong | native (unsolicited pings allowed) |
| OI REST | `/contracts` → `contracts[].open_interest` |
| Funding REST | `/contracts` → `contracts[].funding_rate` |
| Funding History | `/fundingRates?marketName=SOL-PERP` → `fundingRates[]` |
| Products | `/stats/markets` → `markets[]` or `/contracts` → `contracts[]` |
| Trade History REST | No paginated endpoint (S3 files deprecated) |
