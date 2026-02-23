# Alpaca API Reference

> Source: https://docs.alpaca.markets/reference/get-v2-assets + live probes (2026-02-23)

## Endpoints

| Purpose | Base URL | Path | Auth |
|---------|----------|------|------|
| **Products (Assets)** | `https://paper-api.alpaca.markets` | `/v2/assets?asset_class=crypto&status=active` | `APCA-API-KEY-ID` + `APCA-API-SECRET-KEY` headers |
| **Crypto Trade History** | `https://data.alpaca.markets` | `/v1beta3/crypto/us/trades` | Same auth headers |
| **WebSocket** | `wss://stream.data.alpaca.markets` | `/v1beta3/crypto/us` | JSON auth message |

> **IMPORTANT**: The Assets API lives on the **Trading API** domain (`paper-api.alpaca.markets` or `api.alpaca.markets`), NOT the Market Data domain (`data.alpaca.markets`). Using `data.alpaca.markets/v2/assets` returns 404.

## Authentication

All REST endpoints require two headers:
```
APCA-API-KEY-ID: <key>
APCA-API-SECRET-KEY: <secret>
```

Environment variables: `ALPACA_API_KEY`, `ALPACA_API_SECRET`

## Products API Response

`GET /v2/assets?asset_class=crypto&status=active`

Returns a bare JSON array (no wrapper). 73 crypto pairs as of 2026-02-23.

```json
[
  {
    "id": "efc42aad-b8ee-4e2f-b0e7-875b6c734956",
    "class": "crypto",
    "exchange": "CRYPTO",
    "symbol": "SOL/USDT",
    "name": "Solana / USD Tether",
    "status": "active",
    "tradable": true,
    "marginable": false,
    "fractionable": true,
    "min_order_size": "0.007782282",
    "min_trade_increment": "0.000000001",
    "price_increment": "0.000000001"
  }
]
```

### Key Fields for ProductCatalog

| Our Field | Alpaca Field | Notes |
|-----------|-------------|-------|
| symbol | `symbol` | e.g. `SOL/USDT` — contains `/` separator |
| base | `symbol\|/\|0` | Split on `/`, take index 0 → `SOL` |
| quote | `symbol\|/\|1` | Split on `/`, take index 1 → `USDT` |

## Trade REST API Response

`GET /v1beta3/crypto/us/trades?symbols=BTC/USD&limit=2`

```json
{
  "next_page_token": "...",
  "trades": {
    "BTC/USD": [
      {
        "i": 4888505089891583889,
        "p": 67655.2,
        "s": 0.000072,
        "t": "2026-02-23T00:00:48.646747308Z",
        "tks": "B"
      }
    ]
  }
}
```

### REST Trade Field Map

| Our Field | Alpaca Field | Notes |
|-----------|-------------|-------|
| price | `p` | float |
| quantity | `s` | float |
| timestamp | `t` | ISO 8601 with nanoseconds |
| side | `tks` | `B` = buy, `S` = sell |
| trade_id | `i` | int64 |

## WebSocket

URL: `wss://stream.data.alpaca.markets/v1beta3/crypto/us`

Auth message: `{"action":"auth","key":"<key>","secret":"<secret>"}`
Subscribe: `{"action":"subscribe","trades":["BTC/USD"],"orderbooks":["BTC/USD"]}`

Discriminator field: `T` (message type)
- `t` = trade
- `o` = orderbook update
- `success` = ack
- `subscription` = ack
- `error` = ack

Trade WS fields: same as REST (`i`, `p`, `s`, `t`, `tks`, `S` for symbol)
Orderbook fields: `S` (symbol), `t` (timestamp), `b` (bids array), `a` (asks array), levels: `{p: price, s: size}`
