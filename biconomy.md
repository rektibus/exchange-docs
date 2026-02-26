# Biconomy API Documentation

Source: https://github.com/BiconomyOfficial/APIDocs

## Base URL
`https://api.biconomy.com`

## Rate Limit
10 req/s

## Get Recent Trades
`GET /api/v1/trades`

### Parameters
| Param  | Type   | Required | Description |
|--------|--------|----------|-------------|
| symbol | string | yes      | e.g. BTC_USDT |
| size   | int    | no       | Number of trades |

### Response
```json
[
  {
    "amount": "500",
    "price": "0.401",
    "side": "sell",
    "timestamp": "1535507624521"
  }
]
```

| Field     | Description |
|-----------|-------------|
| amount    | Trade quantity |
| price     | Trade price |
| side      | buy or sell |
| timestamp | Unix timestamp in milliseconds |

**NOTE:** No time-range filtering (startTime/endTime). Only returns recent trades.
No pagination support — only `size` param for count.
