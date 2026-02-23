# MAX Exchange API Reference

> Source: https://maicoin.github.io/max-websocket-docs/ + live probes (2026-02-23)
> GitHub: https://github.com/maicoin/max-websocket-docs

## Endpoints

| Purpose | URL | Auth |
|---------|-----|------|
| **Products** | `GET https://max-api.maicoin.com/api/v2/markets` | None |
| **REST Trades** | `GET https://max-api.maicoin.com/api/v2/trades?market={symbol}&limit=1000` | None |
| **WebSocket** | `wss://max-stream.maicoin.com/ws` | None (public channels) |

## Products API

`GET /api/v2/markets` → bare JSON array (54 markets)

```json
{
  "id": "btcusdt",
  "name": "BTC/USDT",
  "market_status": "active",
  "base_unit": "btc",
  "base_unit_precision": 6,
  "min_base_amount": 0.0001,
  "quote_unit": "usdt",
  "quote_unit_precision": 2,
  "min_quote_amount": 8.0,
  "m_wallet_supported": true
}
```

## REST Trades API

`GET /api/v2/trades?market=btcusdt&limit=2` → bare JSON array

```json
[
  {
    "id": 146489051,
    "price": "63968.6",
    "volume": "0.000189",
    "funds": "12.0900654",
    "market": "btcusdt",
    "market_name": "BTC/USDT",
    "created_at": 1771877706,
    "created_at_in_ms": 1771877706692,
    "side": "bid"
  }
]
```

Side values: `"bid"` = buy, `"ask"` = sell.

## WebSocket

### Key Alias Table (from official docs)

| Abbr | Meaning |
|------|---------|
| `c` | channel |
| `e` | event |
| `M` | market |
| `T` | at / created_at (timestamp ms) |
| `t` | trades (array) |
| `p` | price |
| `v` | volume |
| `tr` | trend (up/down) |
| `a` | asks |
| `b` | bids |
| `fi` | first update ID |
| `li` | last update ID |

### Ping/Keepalive

Native WebSocket ping frames. Server closes after 130s without ping. Recommended interval: 30s.

### Subscribe

```json
{
  "action": "sub",
  "subscriptions": [
    {"channel": "trade", "market": "btcusdt"},
    {"channel": "book", "market": "btcusdt", "depth": 50}
  ]
}
```

Ack: `{"e": "subscribed", "s": [...], "T": 123456789}`

### Trade Channel (`c: "trade"`)

```json
{
  "c": "trade",
  "e": "update",
  "M": "btcusdt",
  "t": [
    {"p": "5337.3", "v": "0.1", "T": 123456789, "tr": "up"}
  ],
  "T": 123456789
}
```

- `tr`: trend — `"up"` = buy (price went up, buyer aggressed), `"down"` = sell
- `t`: array of trade objects (can contain multiple)
- `e`: `"snapshot"` on first message, `"update"` thereafter

### Orderbook Channel (`c: "book"`)

```json
{
  "c": "book",
  "e": "snapshot",
  "M": "btcusdt",
  "a": [["64269.5", "0.099428"]],
  "b": [["64216.77", "0.008314"]],
  "T": 1591869939634,
  "fi": 12141725,
  "li": 12141725
}
```

- Levels: indexed arrays `[price_string, size_string]`
- `e`: `"snapshot"` for full book, `"update"` for deltas
- Size `"0"` means remove that price level
- Supported depths: 1, 5, 10, 20, 50 (default 50)
