# Bitunix Spot API Documentation

Source: https://api-doc.bitunix.com/en_us/

## API Domain
- REST: `https://fapi.bitunix.com` (same domain for both spot and futures, different paths)
- WebSocket: `wss://openapi.bitunix.com:443/ws-api/v1`

## REST API - Public Interface

### 1. Get Latest Price
```
GET /api/spot/v1/market/last_price
```
| Name | Type | Required | Notes |
|------|------|----------|-------|
| symbol | string | Y | Pair |

### 2. Get Depth Data
```
GET /api/spot/v1/market/depth
```
| Name | Type | Required | Notes |
|------|------|----------|-------|
| symbol | string | Y | Trading pair |
| precision | number | Y | Token precision |

Response: `{ asks: [{price, volume}], bids: [{price, volume}], ts }`

### 3. Get K-Line Data
```
GET /api/spot/v1/market/kline
```
| Name | Type | Required | Notes |
|------|------|----------|-------|
| symbol | string | Y | Trading Pair |
| interval | string | Y | kline interval (1,3,5,15,30,60,120,240,360,720,D,M,W) |

### 4. Get K-Line History Data
```
GET /api/spot/v1/market/kline/history
```
| Name | Type | Required | Notes |
|------|------|----------|-------|
| symbol | string | Y | Trading Pair |
| interval | string | N | Default 1min |
| endTime | string | N | End timestamp (seconds) |
| limit | string | N | 1-500, default 200 |

### 5. Query Trading Pair Data
```
GET /api/spot/v1/common/coin_pair/list
```
No parameters required.

Response data array:
| Name | Type | Notes |
|------|------|-------|
| id | string | id |
| base | string | Base token |
| quote | string | Quote token |
| basePrecision | string | Base token precision |
| quotePrecision | string | Quote token precision |
| minPrice | string | Minimum trading amount |
| minVolume | string | Minimum trading volume |
| isOpen | string | Whether pair is open |
| isHot | string | Whether pair is trending |
| isRecommend | string | Whether pair is recommended |
| isShow | string | Whether pair is visible |
| tradeArea | string | Trading categories |
| sort | string | Sorting order |
| openTime | string | Trading pair open time |
| precisions | string[] | Precision of the trading pair |

### 6. Query Rate Data
```
GET /api/spot/v1/common/rate/list
```
Response: `[{ baseSymbol, quoteSymbol, rate }]`

### 7. Query Token Data
```
GET /api/spot/v1/common/coin/coin_network/list
```
Response: token info with network details (chain, contractAddress, deposit/withdraw status, etc.)

## WebSocket API

### Connection
- URL: `wss://openapi.bitunix.com:443/ws-api/v1`
- Connections valid for 24 hours
- All requests require authentication (apiKey, timestamp, nonce, sign)

### Request Format
```json
{
  "id": "unique-request-id",
  "method": "market.last_price",
  "params": {
    "symbol": "BTC",
    "nonce": "17832",
    "timestamp": 1724285700000,
    "apiKey": "your-api-key",
    "sign": "--signature--"
  }
}
```

### Response Format
```json
{
  "id": "unique-request-id",
  "code": "0",
  "msg": "success",
  "data": "10000.00"
}
```
Code "0" = success, others = error codes.

### Ping/Keepalive
```json
{
  "id": "unique-request-id",
  "method": "ping",
  "params": {
    "nonce": "17832",
    "timestamp": "1724285700000",
    "apiKey": "your-api-key",
    "sign": "--signature--"
  }
}
```

### Available WS Methods
- `market.last_price` - Get latest price (params: symbol)
- `market.depth` - Get depth data (params: symbol, precision)
- `market.kline` - Get K-Line data (params: symbol, interval)
- `common.coin_pair.list` - Query trading pair data
- `common.rate.list` - Query rate data
- `common.coin.coin_network.list` - Query token data

## Futures API (separate docs)

Source: https://openapidoc.bitunix.com/doc/common/introduction.html

- REST: `https://fapi.bitunix.com`
- Products endpoint: `GET /api/v1/futures/market/trading_pairs`
- WebSocket: `wss://fapi.bitunix.com/public/`
