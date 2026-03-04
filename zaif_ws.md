# Zaif WebSocket API

Source: https://zaif-api-document.readthedocs.io/ja/latest/WebSocket_API.html

## Connection
- `wss://ws.zaif.jp/stream?currency_pair={currency_pair}`
- `ws://ws.zaif.jp/stream?currency_pair={currency_pair}`
- Per-symbol URL, auto-streams on connect (no subscribe needed)
- Reconnect limit: ~4 attempts/second per IP

## Response Format

Single combined JSON object per frame with ALL data:

```json
{
  "asks": [[30000.0, 0.1], [30010.0, 0.2]],
  "bids": [[29500.0, 0.5], [29300.0, 0.1]],
  "trades": [
    {
      "currenty_pair": "btc_jpy",
      "trade_type": "ask",
      "price": 30001,
      "tid": 123,
      "amount": 0.02,
      "date": 1427879761
    }
  ],
  "timestamp": "2015-04-01 18:16:01.739990",
  "last_price": {
    "action": "ask",
    "price": 30001
  },
  "currency_pair": "btc_jpy"
}
```

### Field Reference

| Field | Type | Description |
|-------|------|-------------|
| asks | array[[price,qty]] | Ask side orderbook (full snapshot) |
| bids | array[[price,qty]] | Bid side orderbook (full snapshot) |
| trades | array[object] | Recent trades |
| trades[].currenty_pair | string | Currency pair (NOTE: typo in API — "currenty" not "currency") |
| trades[].trade_type | string | "bid" = buy, "ask" = sell |
| trades[].price | number | Trade price |
| trades[].tid | number | Trade ID |
| trades[].amount | number | Trade quantity |
| trades[].date | number | Unix timestamp (seconds) |
| last_price | object | Last executed trade info |
| last_price.action | string | "bid" or "ask" |
| last_price.price | number | Last price |
| currency_pair | string | The currency pair (e.g. "btc_jpy") |
| timestamp | string | Server timestamp |
