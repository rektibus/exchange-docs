# DeepBook V3 Indexer API

Base URL: `https://deepbook-indexer.mainnet.mystenlabs.com`

All pool endpoints use pool_name format: `SUI_USDC`, `BWETH_USDC`, etc.

## Endpoints

| Endpoint | Method | Description | Response |
|----------|--------|-------------|----------|
| `/get_pools` | GET | List all trading pools with metadata | Array of pool objects |
| `/summary` | GET | 24h summary for all pairs | Array of summary objects |
| `/trades/{pool_name}` | GET | Recent trades for a pool | Array of trade objects |
| `/orderbook/{pool_name}` | GET | Current orderbook bids/asks | `{"bids": [...], "asks": [...]}` |
| `/historical_volume/{pool_name}` | GET | Historical volume (supports time range) | `{"POOL": volume_int}` |
| `/ohlcv/{pool_name}` | GET | Candlestick data (404 as of Feb 2026) | TBD |

## Trade Object

```json
{
  "trade_id": "31879681554928920817783355",
  "price": 0.8641,
  "base_volume": 34.7,
  "quote_volume": 29.98427,
  "type": "buy",
  "timestamp": 1771960566916,
  "taker_is_bid": true,
  "digest": "3PBY8...",
  "maker_fee": 0.0,
  "taker_fee": 0.061731,
  "maker_fee_is_deep": false,
  "taker_fee_is_deep": true
}
```

- `timestamp`: milliseconds
- `type`: "buy" or "sell"
- `base_volume`: quantity in base asset
- `quote_volume`: quantity in quote asset
- No pagination params (no limit, start_time, end_time)

## Pool Object

```json
{
  "pool_id": "0x1109...",
  "pool_name": "BWETH_USDC",
  "base_asset_id": "0xd0e8...::eth::ETH",
  "base_asset_decimals": 8,
  "base_asset_symbol": "BETH",
  "quote_asset_id": "0xdba3...::usdc::USDC",
  "quote_asset_decimals": 6,
  "quote_asset_symbol": "USDC",
  "min_size": 100000,
  "lot_size": 10000,
  "tick_size": 10000
}
```
