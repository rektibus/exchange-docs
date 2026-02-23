# Deribit API Documentation

## General
- **Base URL**: `https://www.deribit.com`
- **WS URL**: `wss://www.deribit.com/ws/api/v2`
- **Protocol**: JSON-RPC 2.0

## Products
**Endpoint**: `GET /api/v2/public/get_instruments`
**Params**: `currency` (BTC|ETH|USDC|USDT|EURR|any), `kind` (future|option|spot|future_combo|option_combo)
**Response**: `result[]` — **Rate limit**: 1 req/sec

### Instrument Fields
| Field | Description | Example |
|-------|-------------|---------|
| `instrument_name` | Unique ID | `BTC-PERPETUAL`, `BTC_USDC` |
| `instrument_type` | `reversed` or `linear` | |
| `contract_size` | Contracts per unit | `10` (BTC perp), `0.0001` (spot) |
| `base_currency` | Base | `BTC`, `ETH` |
| `quote_currency` | Quote | `USD`, `USDC` |
| `settlement_currency` | Settlement | `BTC` (inverse), `USDT` (linear) |
| `settlement_period` | `perpetual`, `month`, `week` | |
| `kind` | `future`, `option`, `spot` | |
| `is_active` | Boolean | |
| `tick_size` | Min price increment | |
| `min_trade_amount` | Min order size | |

### Known Instruments
**Perpetuals (20)**: BTC-PERPETUAL (inverse, cs=10 USD), ETH-PERPETUAL (inverse, cs=1 USD), plus 18 linear USDC pairs
**Spot (18)**: BTC_USDC, BTC_USDT, ETH_USDC, ETH_USDT, ETH_BTC, etc.

## REST Trades
**Endpoint**: `GET /api/v2/public/get_last_trades_by_instrument_and_time`
**Params**: `instrument_name`, `start_timestamp` (ms), `end_timestamp` (ms), `count` (1-1000, default 10)
**Response**: `result.trades[]`, `result.has_more`

### Trade Fields
| Field | Description |
|-------|-------------|
| `price` | Trade price |
| `amount` | USD for inverse/perp, base for linear/spot |
| `direction` | `buy` or `sell` (taker side) |
| `timestamp` | ms since epoch |
| `instrument_name` | Instrument |
| `trade_id` | Unique per currency |
| `trade_seq` | Sequence within instrument |
| `contracts` | Optional, size in contract units |
| `liquidation` | Optional: `M`/`T`/`MT` |

## WebSocket Channels

### Notifications Envelope
```json
{
  "jsonrpc": "2.0",
  "method": "subscription",
  "params": {
    "channel": "trades.BTC-PERPETUAL.100ms",
    "data": [...]
  }
}
```
**Discriminator**: `params.channel` (prefix match)

### trades.{instrument}.{interval}
- interval: `raw` (auth only), `100ms`, `agg2`
- `params.data[]` = array of trades
- Trade fields: same as REST (`price`, `amount`, `direction`, `timestamp`, `instrument_name`, `trade_id`, `liquidation`)

### ticker.{instrument}.{interval}
- `params.data` = object with:
  - `current_funding` — funding rate
  - `funding_8h` — 8hr funding
  - `open_interest` — OI value
  - `timestamp`, `instrument_name`
  - `last_price`, `mark_price`, `index_price`
  - `best_bid_price`, `best_ask_price`, `best_bid_amount`, `best_ask_amount`
  - `stats.volume`, `stats.volume_usd`, `stats.high`, `stats.low`

### book.{instrument}.{group}.{depth}.{interval}
- `params.data` = object with:
  - `bids` — `[[price, amount], ...]`
  - `asks` — `[[price, amount], ...]`
  - `timestamp`, `instrument_name`, `change_id`
- group: `none`, `1`, `2`, `5`, `10` (BTC); `none`, `5`, `10`, `25`, `100`, `250` (ETH)
- depth: `1`, `10`, `20`
- interval: `raw`, `100ms`, `agg2`
- Amount units: USD for inverse/perp, base for linear/spot

### Subscribe
```json
{"method": "public/subscribe", "params": {"channels": ["trades.BTC-PERPETUAL.100ms"]}, "jsonrpc": "2.0", "id": 1}
```
**Rate limit**: ~3.3 req/sec for subscribe. Max 300 channels per connection.

### Batch Subscribe
All channels in one `channels` array. Config uses `subscribe_batch` template.

## REST Funding / OI
**Endpoint**: `GET /api/v2/public/get_book_summary_by_instrument?instrument_name={symbol}`
**Response**: `result[0]` → `current_funding`, `open_interest`, `creation_timestamp`

## REST Orderbook
**Endpoint**: `GET /api/v2/public/get_order_book?instrument_name={symbol}&depth=20`
