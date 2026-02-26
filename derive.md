# Derive (formerly Lyra) — API Reference

Source: https://docs.derive.xyz/reference
Scraped: 2026-02-26

## General

- **Protocol**: JSON-RPC 2.0 over WebSocket
- **WS Endpoint**: `wss://api.lyra.finance/ws`
- **REST Base**: `https://api.lyra.finance`
- **Auth**: Public endpoints require no authentication
- **Rate Limits**: See https://docs.derive.xyz/reference/rate-limits

## REST API

### POST /public/get_all_instruments

Request Parameters (JSON Body):
- `instrument_type` (string, required): `erc20`, `option`, or `perp`
- `expired` (boolean): Filter expired instruments (default false)

Response: `result.instruments[]`
```json
{
    "instrument_type": "perp",
    "instrument_name": "BTC-PERP",
    "is_active": true,
    "tick_size": "0.1",
    "minimum_amount": "0.001",
    "maximum_amount": "1000",
    "amount_step": "0.001",
    "maker_fee_rate": "0.0001",
    "taker_fee_rate": "0.0003",
    "base_currency": "BTC",
    "quote_currency": "USD",
    "perp_details": {
        "index": "BTC-USD",
        "max_rate_per_hour": "0.004",
        "min_rate_per_hour": "-0.004",
        "static_interest_rate": "0.0000125",
        "aggregate_funding": "...",
        "funding_rate": "0.0000125"
    }
}
```

### POST /public/get_trade_history

Request Parameters (JSON Body):

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `instrument_name` | string \| null | null | Filter by instrument (e.g. `BTC-PERP`) |
| `instrument_type` | string \| null | null | `erc20`, `option`, or `perp` |
| `currency` | string \| null | null | Filter by base currency (e.g. `BTC`) |
| `page` | integer | 1 | Page number |
| `page_size` | integer | 100 | Items per page (max 1000) |
| `from_timestamp` | integer | 0 | Start timestamp in ms |
| `to_timestamp` | integer | now | End timestamp in ms |

Response: `result.trades[]`, `result.pagination`

Pagination: `{ "count": total_items, "num_pages": total_pages }`

Trade object fields:
```json
{
    "trade_id": "5259aa4f-5a18-48d3-9272-051bd28d8f4b",
    "instrument_name": "BTC-PERP",
    "timestamp": 1772061040943,
    "trade_price": "68569.8",
    "trade_amount": "0.1404",
    "mark_price": "68600.203370711344177835",
    "index_price": "68578.54935101992",
    "direction": "buy",
    "quote_id": null,
    "rfq_id": null,
    "wallet": "0x3aAa2bB57a0eFeA8F6f89423A923f7107c33471B",
    "subaccount_id": 56939,
    "tx_status": "settled",
    "tx_hash": "0x784a983b...",
    "trade_fee": "0",
    "expected_rebate": "0.962842832888319677",
    "liquidity_role": "maker",
    "realized_pnl": "-35.80687923767475096",
    "realized_pnl_excl_fees": "-35.80687923767475096",
    "extra_fee": "0"
}
```

**NOTE**: Pagination is page-based (`page` + `page_size`), NOT cursor-based. Time filtering uses `from_timestamp` / `to_timestamp` in ms.

### POST /public/get_ticker

Request Parameters:
- `instrument_name` (string, required): Instrument name

Response: `result`
- Contains `funding_rate`, `open_interest`, `best_bid_price`, `best_ask_price`, `timestamp`, etc.

### POST /public/get_funding_rate_history

Request Parameters (JSON Body):

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `instrument_name` | string | required | Instrument name (e.g. `BTC-PERP`) |
| `start_timestamp` | integer | 0 | Start time in ms |
| `end_timestamp` | integer | now | End time in ms |
| `period` | string | `3600` | Frequency. Allowed: `900`, `3600`, `14400`, `28800`, `86400` |

Response: `result.funding_rate_history[]`
```json
{
    "funding_rate": "0.0000125",
    "timestamp": 1772060000000
}
```

## WebSocket Channels

### Channel: trades.{instrument_name}

Subscribe to trades for a given instrument name.

Subscribe message:
```json
{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {"channels": ["trades.BTC-PERP"]},
    "id": 1
}
```

Notification data (`params.data[]`):

| Field | Type | Description |
|-------|------|-------------|
| `direction` | string | `buy` or `sell` |
| `index_price` | string | Index price at time of trade |
| `instrument_name` | string | Instrument name |
| `mark_price` | string | Mark price at time of trade |
| `quote_id` | string \| null | Quote ID if applicable |
| `rfq_id` | string \| null | RFQ ID if applicable |
| `timestamp` | integer | Milliseconds since Unix epoch |
| `trade_amount` | string | Trade quantity |
| `trade_id` | string | Unique trade identifier |
| `trade_price` | string | Execution price |

WS notification envelope: `{"jsonrpc":"2.0","method":"subscription","params":{"channel":"trades.BTC-PERP","data":[...]}}`

### Channel: orderbook.{instrument_name}.{group}.{depth}

Periodically publishes bids and asks for an instrument. The 100ms orderbook emits at 1s intervals if not changing, otherwise 100ms.

Parameters:
- `instrument_name`: string, required
- `group`: string, required — price grouping. Allowed: `1`, `10`, `100`
- `depth`: string, required — number of price levels. Allowed: `1`, `10`, `20`, `100`

Subscribe message:
```json
{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {"channels": ["orderbook.BTC-PERP.1.20"]},
    "id": 3
}
```

Notification data (`params.data`):

| Field | Type | Description |
|-------|------|-------------|
| `instrument_name` | string | Instrument name |
| `publish_id` | integer | Monotonically increasing ID |
| `timestamp` | integer | Update timestamp in ms |
| `bids` | array | Array of `[price, amount]` string pairs |
| `asks` | array | Array of `[price, amount]` string pairs |

WS notification envelope: `{"jsonrpc":"2.0","method":"subscription","params":{"channel":"orderbook.BTC-PERP.1.20","data":{...}}}`

### Channel: ticker_slim.{instrument_name}.{interval}

Periodically publishes ticker info for a single instrument. 100ms interval emits at 1s if best bid/ask not changing.

Parameters:
- `instrument_name`: string, required
- `interval`: string, required — frequency in ms. Allowed: `100`, `1000`

Subscribe message:
```json
{
    "jsonrpc": "2.0",
    "method": "subscribe",
    "params": {"channels": ["ticker_slim.BTC-PERP.1000"]},
    "id": 4
}
```

Notification data (`params.data.instrument_ticker`):

| Field | Type | Description |
|-------|------|-------------|
| `a` | string | Best Ask Price |
| `b` | string | Best Bid Price |
| `A` | string | Best Ask Amount |
| `B` | string | Best Bid Amount |
| `I` | string | Index Price |
| `M` | string | Mark Price |
| `f` | string \| null | Current hourly funding rate (perps only) |
| `maxp` | string | Current Max Price |
| `minp` | string | Current Min Price |
| `t` | integer | Creation timestamp |
| `stats` | object | 24h statistics |
| `stats.h` | string | 24h High |
| `stats.l` | string | 24h Low |
| `stats.c` | string | 24h Volume (contracts) |
| `stats.n` | string | 24h Number of Trades |
| `stats.oi` | string | Current Open Interest |

### Channel: auctions.watch

Subscribe to liquidation auction events.

Format: `{state: "ongoing"|"ended", subaccount_id: int, timestamp: ms, details: {estimated_bid_price, subaccount_balances: {instrument_name: amount_string}}}`

**NOTE**: Cannot use standard liquidation handler — requires dedicated adapter. Liquidations are portfolio auctions, not single-instrument trades.
