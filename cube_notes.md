# Cube Exchange — EnsoX Integration Notes

## What Makes Cube Unusual

Cube is a **hybrid spot/perpetual DEX** with a centralized matching engine (200k ops/s, 200µs latency) and **non-custodial on-chain settlement**. All assets remain in the user's MPC wallet — the exchange never takes custody.

> **Note**: As of March 2026, the perpetual futures feature is documented but **NOT live in the API**. All 141 markets are spot. The products endpoint returns only `Crypto` and `Fiat` asset types, zero `Perpetual` or `Option`. Proto routes for funding/OI (containers 11/13) are in place and will activate when perps go live.

### Unified Spot + Perps Model
- **There is no separate "spot" vs "futures" venue.** Both trade on the same CLOB.
- Spot and perps share margin via cross-margined subaccounts.
- **Implied matching**: orders in one market (e.g. ETH/BTC) can be filled by crossing two other markets (ETH/USDC × BTC/USDC) if it yields a better price. This creates synthetic liquidity.

### Lot-Count Pricing (uint64)
All prices and quantities on WS are **uint64 lot counts**, NOT decimal values. Conversion requires per-market `baseLotSize` and `quoteLotSize` plus per-asset `decimals`:

```
real_price = ws_price × quoteLotSize / baseLotSize × 10^(base_decimals - quote_decimals)
real_qty   = ws_qty × baseLotSize / 10^base_decimals
```

Our `lot_scale_fields` in `resolve_assets` pre-computes `price_scale` and `quantity_scale` per-constituent at product fetch time. These flow into `generated_config.zig` → `COMPOSITION[slot].price_scale/quantity_scale` and are applied at comptime in the proto pipeline.

**REST parsed endpoints** (`/md/v0/parsed/...`) return already-converted decimal prices — no lot conversion needed for recovery.

## Protocol Architecture

### WebSocket — Per-Market Protobuf
- **URL**: `wss://api.cube.exchange/md/book/{market_id}` — one connection per market
- **Format**: Protobuf binary. All messages wrapped in `MdMessages` (repeated `MdMessage`)
- **Heartbeat**: App-level protobuf echo every 30s. Server disconnects after 1 missed interval. Our adapter handles via `peek_field` + echo reply.
- **Config message**: Client sends protobuf `Config` on connect to enable MBP + trades feeds

### MdMessage Field Map (proto oneof)

| Field # | Type | Our Handling |
|---------|------|-------------|
| 1 | Heartbeat | Adapter echo (not ACK'd — intercepted before Zig) |
| 2 | Summary (24h stats) | ACK'd |
| 3 | **Trades** | → proto route: repeated Trade, fields: price=2, qty=5, side=3, ts=6 |
| 4 | MBO Snapshot | ACK'd (we use MBP not MBO) |
| 5 | MBO Diff | ACK'd |
| 6 | **MBP Snapshot** | → proto route: depth, levels field=1, side_field=3 |
| 7 | **MBP Diff** | → proto route: depth, same field layout as snapshot |
| 8 | Kline | ACK'd |
| 9 | MarketStatus | ACK'd (field 10 in ack_fields — but actually proto field 9) |
| 10 | — | ACK'd |
| 11 | **FundingCalculation** | → funding_oi route: funding_rate_field=2, scale=1e-9 |
| 12 | FundingApplication | ACK'd |
| 13 | **ContractStatistics** | → funding_oi route: oi_field=2 |
| 14 | ContractPrice | ACK'd |
| 15 | market_id (optional) | Not a message type, just a field on MdMessage |

### Trade Fields
- `aggressing_side`: enum 0=BID(buy), 1=ASK(sell), 2=IMPLIED_BID, 3=IMPLIED_ASK
- Our `side_map` maps 0→buy, 1→sell. Implied sides (2,3) would need mapping if we want to distinguish — currently they'd be unmatched.
- `transact_time`: nanoseconds
- `fill_quantity` and `price` are uint64 lot counts

### Depth (MBP)
- **Snapshot** (field 6): Full book as repeated `Level` {price, quantity, side}. Side enum: BID=0, ASK=0.
- **Diff** (field 7): Incremental updates as repeated `Diff` {price, quantity, side, op}. Op: ADD=0, REMOVE=1, REPLACE=2.
- Both use `depth_side_field: 3` for mixed bid/ask in single array.
- Varint prices — same lot-count scaling as trades.

## Perpetual Futures

### Contract Specs
- All perps are **linear** (USDC-denominated and collateralized)
- Cross-margined — all positions share the same margin balance
- Leverage up to 100x (tiered by position notional)
- Contract `decimals` field is **negative** (e.g. -5 for BTC = each unit is 1e-5 BTC = 1000 satoshis)

### Funding
- 8-hour funding intervals
- `predicted_funding_rate` (field 2 of FundingCalculation) expressed with **9 decimals** (multiply by 1e-9)
- Funding = `open_contracts × index_price × funding_rate × interval/period`
- Premium index derived from impact bid/ask sampling

### Liquidation
- Multi-step: open order cancel → market close → ADL (auto-deleverage) → insurance fund → socialized loss
- Liquidations appear as **regular trades** on the market data feed (forced market orders). CancelOrderAck reason=8 (LIQUIDATION) is on the order entry WS only.
- **No separate liquidation message type in market data.** We cannot distinguish liquidation trades from normal trades on the MD feed.

### Open Interest
- `ContractStatistics` (field 13): `open_interest` (field 2) is int64 = total open contracts (both long+short counted)

## REST API

### Products: `GET /ir/v0/markets`
- Response: `result.markets[]` and `result.assets[]`
- Markets: `marketId`, `symbol` (e.g. "BTCUSDC"), `baseLotSize`, `quoteLotSize`, `baseAssetId`, `quoteAssetId`, `status` (1=active, 2=cancel-only, 3=retired)
- Assets: `assetId`, `symbol`, `decimals`

### Recent Trades: `GET /md/v0/parsed/book/{symbol}/recent-trades`
- Symbol = market symbol (e.g. "BTCUSDC")
- Response: `result.trades[]` → `{id, p, q, side, ts}`
- Side is string: "Bid"/"Ask" (NOT numeric)
- Timestamp in milliseconds
- Prices are already decimal (parsed endpoint)
- No time-range pagination — recent-only (last ~200 trades)

### Book Snapshot: `GET /md/v0/parsed/book/{symbol}/snapshot`
- Response: `result.{bids, asks}` → arrays of `[price, qty]`
- Decimal prices (parsed)

### Rate Limits
- **Aggressive IP-based throttle**: burst of ~5 rapid requests → 403 Forbidden
- **Ban duration**: ~30 seconds (no `Retry-After` header, silent ban)
- **Safe interval**: `rate_limit_ms: 2000` (0.5 req/s)
- With 79 active symbols, full recovery sweep = 79 × 2s = ~158 seconds
- Each request returns ~200 trades (~25s of history at 8 trades/s)
