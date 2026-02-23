# Biconomy API Documentation

> Spot exchange. Base URL: `https://api.biconomy.com` | WS: `wss://bei.biconomy.com/ws`

## REST API

### Products — `GET /api/v1/exchangeInfo`

Returns a flat JSON array of all trading pairs.

**Response** (array):
```json
[
  {
    "baseAsset": "BTC",
    "quoteAsset": "USDT",
    "baseAssetPrecision": 6,
    "quoteAssetPrecision": 2,
    "symbol": "BTC_USDT",
    "status": "trading",
    "tickSize": "0.01",
    "minQuantity ": "10",
    "PoBaseAssetMin": 0,
    "PoQuoteAssetMin": 0
  }
]
```

Key fields: `baseAsset`, `quoteAsset`, `symbol`, `status` ("trading"), `tickSize`, `baseAssetPrecision` (integer = lot size precision).

### Depth — `GET /api/v1/depth?symbol=BTC_USDT&limit=5`

Returns orderbook snapshot.

**Response**:
```json
{
  "asks": [["68446.12", "0.11772"], ["68446.13", "0.04937"]],
  "bids": [["68446.11", "0.03765"], ["68446.10", "0.01669"]]
}
```

Format: `[[price_string, size_string], ...]`. Asks ascending, bids descending.

### Trades — NOT AVAILABLE

REST trades endpoint (`/api/v1/trades`) returns `{"code":1,"message":"Illegal parameter"}` with any parameter combination tested (`symbol`, `market`, `limit`). **History NOT supported via REST.**

---

## WebSocket API

URL: `wss://bei.biconomy.com/ws`  
Ping: Native WebSocket ping, 30s interval.

### Authentication

None required for public streams.

### Subscribe — Trades

```json
{"method": "deals.subscribe", "params": ["BTC_USDT"], "id": 1}
```

**Ack**:
```json
{"error": null, "result": {"status": "success"}, "id": 1}
```

**Snapshot** (first message after subscribe):
```json
{
  "method": "deals.update",
  "params": [
    "BTC_USDT",
    [
      {
        "market": "BTC_USDT",
        "id": 5584858007,
        "price": "68430.78",
        "amount": "0.05254",
        "time": 1771303183.374657,
        "type": "buy"
      }
    ]
  ]
}
```

**Update** (same format as snapshot):
```json
{
  "method": "deals.update",
  "params": ["BTC_USDT", [{"market": "BTC_USDT", "id": 123, "price": "100", "amount": "1", "time": 1771303183.825, "type": "sell"}]]
}
```

Trade fields:
| Field | Type | Description |
|-------|------|-------------|
| `market` | string | Trading pair (e.g. "BTC_USDT") |
| `id` | integer | Trade ID |
| `price` | string | Trade price |
| `amount` | string | Trade quantity |
| `time` | float | Unix timestamp in **seconds** (with fractional ms) |
| `type` | string | "buy" or "sell" |

### Subscribe — Depth

```json
{"method": "depth.subscribe", "params": ["BTC_USDT", 20, "0.01"], "id": 2}
```

Params: `[symbol, depth_limit, price_interval]`

**Snapshot** (first message, `params[0] = true`):
```json
{
  "method": "depth.update",
  "params": [
    true,
    {
      "asks": [["68430.79", "0.07199"], ["68430.80", "0.03887"]],
      "bids": [["68430.64", "0.04660"], ["68430.63", "0.03100"]]
    }
  ]
}
```

**Delta** (subsequent, `params[0] = false`):
```json
{
  "method": "depth.update",
  "params": [
    false,
    {
      "asks": [["68430.80", "0.14094"]],
      "bids": [["68430.64", "0.04660"]]
    }
  ]
}
```

Depth fields:
| Field | Type | Description |
|-------|------|-------------|
| `params[0]` | boolean | `true` = full snapshot, `false` = delta |
| `params[1].asks` | array | `[[price, size], ...]` ascending |
| `params[1].bids` | array | `[[price, size], ...]` descending |

**No timestamp** in depth messages.  
**No symbol** in depth updates — implicit from subscription.

### Message Discrimination

| `method` value | Type |
|----------------|------|
| `deals.update` | Trade |
| `depth.update` | Depth |

Ack messages have `error: null` and `result.status`.

### Side Map

| Wire Value | Meaning |
|------------|---------|
| `"buy"` | Buy |
| `"sell"` | Sell |
