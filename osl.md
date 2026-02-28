# OSL API Documentation

Source: https://osl.com/reference/introduction

## Environments

- **Production HK**: trade-hk.osl.com
- **Production AU**: trade-au.osl.com
- **Sandbox HK**: trade-hk.oslsandbox.com
- **Sandbox AU**: trade-au.oslsandbox.com

## Rate Limits

> REST API rate limits are controlled by IP, not per user or API key.

| Channel | Limit |
|---------|-------|
| REST V3 | 30 req/s per IP (trading: 100 req/s) |
| REST V4 | 200 req/s per IP |
| WebSocket | 1 update/s, max 25 levels per side |
| FIX | 500 req/s per session |

## Error Codes (Common)

| Code | Description |
|------|-------------|
| s200003 | Base currency not supported |
| s200004 | Quote currency not supported |
| s300001 | Invalid exchange rates |
| s100002 | Invalid quote ID |
| s100005 | Trade already exists for quote ID |
| s100006 / s100026 | Quote expired |
| INSUFFICIENT_AVAILABLE_BALANCE | Insufficient balance |
| TOO_SMALL | Order value too small |
| INVALID_PARAMETERS | Wrong pair, amount/rate too big, too many decimals |

---

## WebSocket — Establish Connection

### Subscription Endpoint

Structure: `wss://<root>/ws/v4?subscribe=<instruments>`

- Each subscription: `orderBook:<SYMBOL>` (e.g. `orderBook:BTCUSD`)
- Multiple: comma-separated (e.g. `orderBook:BTCUSD,orderBook:LTCUSD`)

Example:
```
wss://trade-hk.osl.com/ws/v4?subscribe=orderBook:BTCUSD,orderBook:LTCUSD
```

> Publication frequency: 2 updates/second, max 50 levels per side.
> If any instrument doesn't exist → HTTP 404 rejects ALL subscriptions.

**NOTE**: This is plain WebSocket, NOT Socket.IO. No subscribe messages needed — subscription is in the URL.

### Market Data Messages

All JSON. Field `action` determines how to handle. Each message has `price`, `side`, and conditionally `size`.

### Action Types

#### `partial` — Full snapshot (replace entire book)
```json
{
  "table": "orderBookL2",
  "action": "partial",
  "symbol": "BTCUSD",
  "bookVersionId": 1,
  "sendTime": 1632330416488,
  "keys": ["symbol", "id", "side"],
  "data": [
    {"symbol": "BTCUSD", "side": "Buy", "size": "1.0", "price": "43000.0"}
  ]
}
```

#### `insert` — Insert/replace price level
```json
{
  "table": "orderBookL2",
  "action": "insert",
  "symbol": "BTCUSD",
  "bookVersionId": 206,
  "sendTime": 1632335161128,
  "publishTime": 1632335161441,
  "data": [
    {"symbol": "BTCUSD", "side": "Sell", "size": "177.0", "price": "47228.0"},
    {"symbol": "BTCUSD", "side": "Sell", "size": "102.0", "price": "48935.0"}
  ]
}
```

#### `update` — Update price level (same format as insert)
```json
{
  "table": "orderBookL2",
  "action": "update",
  "symbol": "BTCUSD",
  "bookVersionId": 207,
  "sendTime": 1632335161128,
  "data": [
    {"symbol": "BTCUSD", "side": "Sell", "size": "177.0", "price": "47228.0"}
  ]
}
```

#### `delete` — Remove price level (no size field)
```json
{
  "table": "orderBookL2",
  "action": "delete",
  "symbol": "BTCUSD",
  "bookVersionId": 208,
  "sendTime": 1632335161128,
  "data": [
    {"symbol": "BTCUSD", "side": "Sell", "price": "46823.0"}
  ]
}
```

#### `heartbeat` — Keep alive (every 30s if no updates)
```json
{
  "table": "orderBookL2",
  "timestamp": 1632334653163,
  "action": "heartbeat",
  "symbol": "BTCUSD"
}
```

#### `ping` — Server ping (must respond with pong or connection drops)
```json
{"action": "ping"}
```

---

## REST V4 — Get Currency-Pairs

```
GET /api/v4/instrument?symbol=BTCUSD
```

If `symbol` is empty, all currency-pairs are returned.

Response (array):
```json
[
  {
    "symbol": "BTCUSD",
    "currency": "BTC",
    "settlCurrency": "USD",
    "highPrice": "30000.00000",
    "lowPrice": "14000.00000",
    "bidPrice": "18932.00000",
    "askPrice": "19000.00000",
    "lastPrice": "19000.00000",
    "minPrice": "13482.00000",
    "maxPrice": "25038.00000",
    "minOrderQty": "0.00010000",
    "maxOrderQty": "399.39290000",
    "minValue": "10.00000",
    "maxValue": "10000000.00000",
    "prevClosePrice": "19000.00000",
    "volume": null,
    "tickSize": "1.00000",
    "stepSize": "0.00010000",
    "priceDecimals": "5",
    "quantityDecimals": "8",
    "updateTime": "2022-10-22T03:14:48.044Z"
  }
]
```

| Field | Description |
|-------|-------------|
| symbol | Currency pair (e.g. BTCUSD) |
| currency | Base asset |
| settlCurrency | Quote/settlement currency |
| lastPrice | Last traded price |
| volume | 24h traded volume |
| tickSize | Min price movement |
| stepSize | Min quantity movement |

---

## REST V4 — Get Exchange Trade List

```
GET /api/v4/trade?symbol=BTCUSD&reverse=false
```

Default time slot: 1 hour. Timestamps in ISO-8601 UTC.

| Param | Type | Description |
|-------|------|-------------|
| symbol | string | Currency-pair (all if empty) |
| reverse | boolean | true=reverse chrono, false=chrono |
| startTime | date | ISO-8601 filter start |
| endTime | date | ISO-8601 filter end |
| lastHour | string | Override times, use last trade time |

Response (array):
```json
[
  {
    "trdMatchID": "87ZPV",
    "symbol": "BTCUSD",
    "side": "Sell",
    "size": "0.60000000",
    "price": "27592.00000000",
    "grossValue": "16555.20000000",
    "transactTime": "2023-10-10T00:06:04.000Z"
  }
]
```

| Field | Type | Description |
|-------|------|-------------|
| trdMatchID | string | Trade match ID |
| symbol | string | Currency pair |
| side | string | Buy or Sell |
| size | string | Trade quantity |
| price | string | Trade price |
| grossValue | string | size × price |
| transactTime | string | ISO-8601 timestamp |

---

## REST V4 — Get Order Book

```
GET /api/v4/orderBook/L2?symbol=BTCUSD&depth=25
```

Response:
```json
{
  "symbol": "BTCUSD",
  "asks": [["19268", "0.0024"], ["19271", "0.0048"]],
  "bids": [["19253", "0.003"], ["19235", "0.0048"]],
  "updateTime": "2022-10-22T14:05:42.365Z"
}
```

---

## REST V3 — Get Currency Pair (currencyStatic)

```
GET /api/3/currencyStatic
```

Response contains `currencyStatic.currencies` (map) and `currencyStatic.currencyPairs` (map).

Each currency pair has `tradedCcy`, `settlementCcy`, `priceDecimals`, `engineSettings.tradingEnabled`.

```json
{
  "currencyStatic": {
    "currencies": {
      "USD": {
        "decimals": 2, "type": "FIAT", "symbol": "$",
        "engineSettings": {"depositsEnabled": true, "withdrawalsEnabled": true, "displayEnabled": true}
      },
      "BTC": {
        "decimals": 8, "type": "CRYPTO", "symbol": "BTC",
        "engineSettings": {"depositsEnabled": true, "withdrawalsEnabled": true, "displayEnabled": true}
      }
    },
    "currencyPairs": {
      "BTCUSD": {
        "priceDecimals": 5, "tradedCcy": "BTC", "settlementCcy": "USD",
        "engineSettings": {"tradingEnabled": true, "displayEnabled": true}
      }
    }
  }
}
```
