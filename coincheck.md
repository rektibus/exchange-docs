# Coincheck API Documentation

Japanese exchange, spot only. 27 pairs, all JPY-denominated.

## Products
**Endpoint**: `GET /api/exchange_status`
**Response**: `{"exchange_status": [{"pair": "btc_jpy", "status": "available", ...}]}`
- 27 pairs, all `_jpy` (BTC, ETH, ETC, LSK, XRP, XEM, LTC, BCH, MONA, XLM, QTUM, BAT, IOST, ENJ, SAND, DOT, CHZ, LINK, MKR, DAI, MATIC, IMX, APE, AXS, WBTC, AVAX, SHIB)
- `products_fields`: `symbol=pair`, `base=pair|_|0`, `quote=pair|_|1`

## REST Trades
**Endpoint**: `GET /api/trades?pair=btc_jpy`
**Response**: `{"success": true, "pagination": {...}, "data": [...]}`
```json
{"id": 301080868, "amount": "0.01", "rate": "10388563.0", "pair": "btc_jpy",
 "order_type": "sell", "created_at": "2026-02-18T18:04:36.000Z"}
```
- **Max limit**: 100 (capped)
- **Pagination**: `last_id` parameter (works)
- **Field map**: `amount→quantity`, `rate→price`, `order_type→side`, `created_at→timestamp`
- **Timestamp unit**: ISO 8601

## REST Orderbook
**Endpoint**: `GET /api/order_books?pair=btc_jpy`
**Response**: `{"asks": [[price, qty], ...], "bids": [[price, qty], ...]}`
- 200 levels each side
- Indexed format: `[price_string, qty_string]`

## WebSocket
**Endpoint**: `wss://ws-api.coincheck.com/`
**Auth**: None (public)
**Subscribe**: `{"type": "subscribe", "channel": "btc_jpy-trades"}`

### Trade Messages
```json
[["1771437916", "301080878", "btc_jpy", "10386396.0", "0.00299892", "buy", "8678267973", "8678267958", null]]
```
Nested array format: `[[timestamp_s, trade_id, pair, price, qty, side, maker_order_id, taker_order_id, null]]`
- Index 0: timestamp (seconds, string)
- Index 1: trade_id (string)
- Index 2: pair (e.g. "btc_jpy")
- Index 3: price (string)
- Index 4: quantity (string)
- Index 5: side ("buy"/"sell")

### Depth Messages
```json
["btc_jpy", {"bids": [["10382780.0", "0.09"], ...], "asks": [["10393421.0", "0.01"], ...], "last_update_at": "1771437913"}]
```
2-element array: `[symbol, {bids, asks, last_update_at}]`
- Delta updates (qty=0 = remove level)
- No explicit snapshot/delta flag
- `last_update_at` = epoch seconds (string)

## Exchange Quirks

### 1. Nested Array Trade Format (REQUIRES DEDICATED ADAPTER)
Trade WS messages are `[[...]]` — nested array with NO object element anywhere.
Engine's array unwrap logic searches for first object in array and panics when none found.
Cannot use generic adapter for trades. Depth works because it contains an object.

### 2. JPY-Only
All 27 pairs are JPY-denominated. No USD/USDT pairs. Likely filtered out by composition
generator's quote whitelist unless JPY is added.

### 3. Low Liquidity
BTC/JPY had ~2 trades in 10 seconds during testing. Small exchange.
