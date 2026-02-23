
Change Log
General Info
Market Data Endpoints 
Test Connectivity
Check Server Time
Ticker Price Statistics
Assets Information
Order Book
Recent Trades List
Market Summary Data
API V2
Change Log
2023-08-06
Update endpoints for All

GET /api/v2/ping: Test connectivity to the Rest API
GET /api/v2/time: Test connectivity to the Rest API and get the current server time.
GET /api/v2/assets: Current exchange trading rules and symbol information
GET /api/v2/depth: Current order book information.
GET /api/v2/trades: Get recent trades information
GET /api/v2/ticker: 24 hour rolling window price change statistics.
General Info
General API Information
The base endpoint is: https://api.bitcointry.com
All endpoints return either a JSON object or array.
All time and timestamp related fields are in milliseconds.
Market Data Endpoint
Test Connectivity
GET /api/v2/ping

Test connectivity to the Rest API and get the current server time.

Parameters:
NONE

Response:
{}
Check Server Time
GET /api/v2/time

Test connectivity to the Rest API and get the current server time.

Parameters:
NONE

Response:
{
  "serverTime": 1611327319559
}
24hr Ticker Price Change Statistics
GET /api/v2/ticker

24 hour rolling window price change statistics.

Parameters:There are 2 possible options:
Options	Example
No parameters	curl -X GET "curl -X GET "https://api.bitcointry.com/api/v2/ticker"
pair	curl -X GET "curl -X GET "https://api.bitcointry.com/api/v2/ticker?pair=BTC_USDT"
Response:
{
    "BTC_USDT: "{
      "base_id": 1,
      "quote_id": 825,
      "last_price": 26804.82,
      "quote_volume": 264935.78620
      "base_volume": 9.89670
      "price_change_percent_24h": "-0.05"
      "highest_price_24h": "26934.99"
      "lowest_price_24h": "26562.60"
      "lowest_ask": 26804.83
      "highest_bid": "26804.82"
      "isFrozen": 0
    }
}
Assets Information
GET /api/v2/assets

Current exchange trading rules and symbol information.

Parameters:There are 2 possible options:
Options	Example
No parameters	curl -X GET "curl -X GET "https://api.bitcointry.com/api/v2/assets"
pair	curl -X GET "curl -X GET "https://api.bitcointry.com/api/v2/assets?symbol=BTC"
Response:
{
    "BTC_USDT: "{
      "name": Bitcoin,
      "unified_cryptoasset_id": 1,
      "can_withdraw": true,
      "can_deposit": true
      "min_withdraw": 0.00010000
      "max_withdraw": "1000.00"
      "maker_fee": "0.2"
      "taker_fee": "0.2"
    }
}
Order Book
GET /api/v2/depth/BTC_USDT

Current order book information.

Parameters:*Default limit: 500 order.
There are 1 possible options:
Options	Example
Symbol	curl -X GET "curl -X GET "https://api.bitcointry.com/api/v2/depth/BTC_USDT"
Limit	curl -X GET "curl -X GET "https://api.bitcointry.com/api/v2/depth/BTC_USDT?limit=100"
Response:
{
  "serverTime": "1667217248454",
  "bids": [
    [
      "26804.99",
      "10.018225"
    ],
    [
      "26804.92",
      "0.0451"
    ],
  ],
  "asks": [
    [
      "26805.02",
      "0.19746"
    ],
    [
      "26805.03",
      "0.000195"
    ],
  ]
}
Order Book (Alternative)
GET /api/v2/orderbook?symbol=BTC_USDT

Current order book information.

Parameters:*Default limit: 500 order.
There are 1 possible options:
Options	Example
Symbol	curl -X GET "curl -X GET "https://api.bitcointry.com/api/v2/orderbook?symbol=BTC_USDT"
Limit	curl -X GET "curl -X GET "https://api.bitcointry.com/api/v2/orderbook?symbol=BTC_USDT&limit=100"
Response:
{
  "serverTime": "1667217248454",
  "bids": [
    [
      "26804.99",
      "10.018225"
    ],
    [
      "26804.92",
      "0.0451"
    ],
  ],
  "asks": [
    [
      "26805.02",
      "0.19746"
    ],
    [
      "26805.03",
      "0.000195"
    ],
  ]
}
Recent Trades List
GET /api/v2/trades

Get recent trades.

Parameters:*Default limit: 100 orders
There are 1 possible options:
Options	Example
Symbol	curl -X GET "curl -X GET "https://api.bitcointry.com/api/v2/trades/BTC_USDT"
Limit	curl -X GET "curl -X GET "https://api.bitcointry.com/api/v2/trades/BTC_USDT?limit=10"
Response:
[
  {
    "price": "19852.02",
    "base_volume": "0.00105",
    "quote_volume": "21.7601055",
    "timestamp": "1667220076241",
    "trade_id": "30108",
    "type": "buy"
  }
]
Summary
GET /api/v2/summary

Overview of market data for all tickers and all markets.

Parameters:
None

Options	Example
No parameters	curl -X GET "curl -X GET https://api.bitcointry.com/api/v2/summary"
Response:
[
  {
      "trading_pairs": "BTC_USDT",
      "base_currency": "BTC",
      "quote_currency": "USDT",
      "last_price": "26811.43"
      "lowest_ask": "26816.98"
      "highest_bid": "26816.97"
      "base_volume": "9.82801"
      "quote_volume": "263093.54526"
      "price_change_percent_24h": "263093.54526"
      "highest_price_24h": "26934.99"
      "lowest_price_24h": "26562.60"
  }
]