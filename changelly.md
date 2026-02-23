# Changelly Pro API Notes

## EnsoX Integration Notes

### API (HitBTC-Compatible)
- **WS**: `wss://api.pro.changelly.com/api/3/ws/public`
- **REST**: `https://api.pro.changelly.com/api/3/public/`
- Changelly Pro uses the **HitBTC API** — same endpoints, same message format.

### WS Trade Format
Channel `trades`, data nested in `update.{SYMBOL}` (HitBTC broadcast pattern):
```json
{"ch":"trades","update":{"BTCUSDT":[{"t":1771432838968,"i":2537448440,"p":"67247.25","q":"0.09386","s":"sell"}]}}
```
Fields: `t` (epoch ms), `i` (trade_id), `p` (price), `q` (quantity), `s` (side: buy/sell).
Uses `array_key: "update.*"` wildcard — symbol extracted from object key.

### WS Orderbook Format (NOT SUPPORTED — data pattern unsupported)
Channel `orderbook/full` (NOT `depth` — that channel returns "Unknown channel" error).
Data nested in `update.{SYMBOL}` / `snapshot.{SYMBOL}`:
```json
{"ch":"orderbook/full","update":{"BTCUSDT":{"t":ms,"s":seqId,"a":[[price,qty]],"b":[[price,qty]]}}}
```
Fields: `a` = asks, `b` = bids, `s` = sequence ID.
**Not supported**: dynamic symbol key in path prevents generic depth extractor from working.

### REST Trade Format
```json
[{"id":2537448440,"price":"67247.25","qty":"0.09386","side":"sell","timestamp":"2026-02-18T16:40:38.968Z"}]
```
Field map: `qty→quantity`, `id→trade_id`. Timestamp is ISO format.

### Products
`GET /api/3/public/symbol` → object keyed by symbol name (361 pairs).
`products_json_path: "$"`, `symbol: "_key"`, `base: "base_currency"`, `quote: "quote_currency"`.
Filter: `type: "spot"`.

### Known Quirks
1. **Very low volume**: ~1 trade per 1-2 minutes on BTC-USD.
2. **Snapshot/update pattern**: all data uses `snapshot.{SYMBOL}` and `update.{SYMBOL}` nesting.
3. **No `depth` channel**: must use `orderbook/full` for orderbooks.
