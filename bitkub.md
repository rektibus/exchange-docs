# bitkub-official-api-docs
Official Documentation for Bitkub APIs

* The documentation described here is official. This means the documentation is officially supported and maintained by Bitkub's own development team.
* The use of any other projects is **not supported**; please make sure you are visiting **bitkub/bitkub-official-api-docs**.


Name | Description
------------ | ------------ 
[restful-api.md](./restful-api.md)       | Details on the RESTful API V3 (/api)
[restful-api-v4.md](./restful-api-v4.md) | Details on the RESTful API V4 (/api)
[websocket-api.md](./websocket-api.md)   | Details on the Websocket API (/websocket-api)

# RESTful API for Bitkub (2025-10-10)

# Announcement
* The following market endpoints will be deprecated on 9 Dec 2025. Please use [v3 endpoints](#non-secure-endpoints-v3) as replacement: [GET /api/market/symbols](#get-apimarketsymbols), [GET /api/market/ticker](#get-apimarketticker), [GET /api/market/trades](#get-apimarkettrades), [GET /api/market/bids](#get-apimarketbids), [GET /api/market/asks](#get-apimarketasks), [GET /api/market/books](#get-apimarketbooks), [GET /api/market/depth](#get-apimarketdepth)
* Page-based pagination will be deprecated on 8 Sep 2025 for [my-order-history](#get-apiv3marketmy-order-history).
* Order history older than 90 days is archived for [my-order-history] (#get-apiv3marketmy-order-history) More details here.
* order_id and txn_id formats of [my-open-orders](#get-apiv3marketmy-open-orders), [my-order-history](#get-apiv3marketmy-order-history), [my-order-info](#get-apiv3marketorder-info), [place-bid](#post-apiv3marketplace-bid), [place-ask](#post-apiv3marketplace-ask), [cancel-order](#post-apiv3marketcancel-order) may change for some symbols due to a system upgrade, See affected symbols and detail : [here](https://support.bitkub.com/en/support/solutions/articles/151000214886-announcement-trading-system-upgrade)
* API Specifications for Crypto Endpoints, please refer to the documentation here: [Crypto Endpoints](restful-api-v4.md)
* Deprecation of Order Hash for [my-open-orders](#get-apiv3marketmy-open-orders), [my-order-history](#get-apiv3marketmy-order-history), [my-order-info](#get-apiv3marketorder-info), [place-bid](#post-apiv3marketplace-bid), [place-ask](#post-apiv3marketplace-ask), [cancel-order](#post-apiv3marketcancel-order) on 28/02/2025 onwards, More details [here](https://support.bitkub.com/en/support/solutions/articles/151000205895-notice-deprecation-of-order-hash-from-public-api-on-28-02-2025-onwards)

# Change log
* 2025-09-08 Update API [my-order-history](#get-apiv3marketmy-order-history) spec
* 2025-01-07 Update FIAT Withdraw error code
* 2025-04-03 Deprecated Crypto Endpoint v3 and Remove from the Document.
* 2024-12-20 Introducing the Enhanced Market Data Endpoint [Ticker, Depth, Bids, Asks, Trades](#non-secure-endpoints-v3)
* 2024-07-25 Deprecated Secure Endpoint V1/V2 and Remove from the Document.
* 2024-07-05 Update rate-limits of place-bid, place-ask, cancel-order, my-open-orders  [Rate-Limits](#rate-limits)
* 2024-07-05 Update rate-limits which will be apply on 17 July 2024 [Rate-Limits](#rate-limits)
* 2024-06-11 Updated API request of [POST /api/v3/crypto/internal-withdraw](#post-apiv3cryptointernal-withdraw) and edited API response of [POST /api/v3/crypto/withdraw-history](#post-apiv3cryptowithdraw-history)
* 2024-06-11 Added new error code 58 - Transaction Not Found
* 2024-05-16 Release: Post-Only Functionality Added to [POST /api/v3/market/place-bid](#post-apiv3marketplace-bid) and [POST /api/v3/market/place-ask](#post-apiv3marketplace-ask)
* 2024-03-06 Edited Request field for [POST /api/v3/crypto/withdraw](#post-apiv3cryptowithdraw)
* 2024-02-15 Edited Endpoint permission [Permission Table](#secure-endpoints-v3)


# Table of contents
* [Base URL](#base-url)
* [Endpoint types](#endpoint-types)
* [Constructing the request](#constructing-the-request)
* [API documentation](#api-documentation)
* [Error codes](#error-codes)
* [Rate limits](#rate-limits)


# Base URL
* The base URL is: https://api.bitkub.com

# Endpoint types
### Non-secure endpoints
Our existing endpoints remain available for use. However, for enhanced security and performance, we strongly recommend utilizing the new [Non-Secure Endpoint V3](#non-secure-endpoints-v3).
* [GET /api/status](#get-apistatus)
* [GET /api/servertime](#get-apiservertime)
* [GET /tradingview/history](#get-tradingviewhistory)
* [GET /api/v3/servertime](#get-apiv3servertime)

### Non-secure endpoints V3
| Market Data Endpoint                                          | Method |
| --------------------------------------------------------------| ------ |
| [GET /api/v3/market/symbols](#get-apiv3marketsymbols)         | GET    |
| [GET /api/v3/market/ticker](#get-apiv3marketticker)           | GET    |
| [GET /api/v3/market/bids](#get-apiv3marketbids)               | GET    |
| [GET /api/v3/market/asks](#get-apiv3marketasks)               | GET    |
| [GET /api/v3/market/depth](#get-apiv3marketdepth)             | GET    |
| [GET /api/v3/market/trades](#get-apiv3markettrades)           | GET    |

| Exchange Information Endpoint                                 | Method |
| --------------------------------------------------------------| ------ |
| [GET /api/v3/servertime](#get-apiv3servertime)                | GET    |


### Secure endpoints V3
All secure endpoints require [authentication](#constructing-the-request).

| User Endpoint                                                             | Method | Trade | Deposit | Withdraw |
| ------------------------------------------------------------------------- | ------ | ----- | ------- | -------- |
| [/api/v3/user/trading-credits](#post-apiv3usertrading-credits)            | POST   |       |         |          |
| [/api/v3/user/limits](#post-apiv3userlimits)                              | POST   |       |         |          |
| [/api/v3/user/coin-convert-history](#get-apiv3usercoin-convert-history)   | GET    |       |         |          |

| Trading Endpoint                                                     | Method | Trade | Deposit | Withdraw |
| ------------------------------------------------------------------- | ------ | ----- | ------- | -------- |
| [/api/v3/market/wallet](#post-apiv3marketwallet)                    | POST   |       |         |          |
| [/api/v3/market/balances](#post-apiv3marketbalances)                | POST   |       |         |          |
| [/api/v3/market/place-bid](#post-apiv3marketplace-bid)              | POST   | ✅     |         |          |
| [/api/v3/market/place-ask](#post-apiv3marketplace-ask)              | POST   | ✅     |         |          |
| [/api/v3/market/cancel-order](#post-apiv3marketcancel-order)        | POST   | ✅     |         |          |
| [/api/v3/market/wstoken](#post-apiv3marketwstoken)                  | POST   | ✅     |         |          |
| [/api/v3/market/my-open-orders](#get-apiv3marketmy-open-orders)     | GET    |        |         |          |
| [/api/v3/market/my-order-history](#get-apiv3marketmy-order-history) | GET    |        |         |          |
| [/api/v3/market/order-info](#get-apiv3marketorder-info)             | GET    |       |         |          |

| Fiat Endpoint                                                    | Method | Trade | Deposit | Withdraw |
| ---------------------------------------------------------------- | ------ | ----- | ------- | -------- |
| [/api/v3/fiat/accounts](#post-apiv3fiataccounts)                 | POST   |       |         | ✅       |
| [/api/v3/fiat/withdraw](#post-apiv3fiatwithdraw)                 | POST   |       |         |          |
| [/api/v3/fiat/deposit-history](#post-apiv3fiatdeposit-history)   | POST   |       |         |          |
| [/api/v3/fiat/withdraw-history](#post-apiv3fiatwithdraw-history) | POST   |       |         |          |

# Constructing the request
### GET/POST request
* GET requests require parameters as **query string** in the URL (e.g. ?sym=THB_BTC&lmt=10). 
* POST requests require JSON payload (application/json).

### Request headers (Secure Endpoints)
Authentication requires API KEY and API SECRET. Every request to the server must contain the following in the request header:
* Accept: application/json
* Content-type: application/json
* X-BTK-APIKEY: {YOUR API KEY}
* X-BTK-TIMESTAMP: {Timestamp i.e. 1699376552354 }
* X-BTK-SIGN: [Signature](#signature)

### Payload (POST)
The payload is always JSON.

### Signature
Generate the signature from the timestamp, the request method, API path, query parameter, and JSON payload using HMAC SHA-256. Use the API Secret as the secret key for generating the HMAC variant of JSON payload. The signature is in **hex**  format. The user has to attach the signature via the Request Header
You must get a new timestamp in millisecond from [/api/v3/servertime](#get-apiv3servertime). The old one is in second.

#### Example string for signing a signature:
```javascript
//Example for Get Method
1699381086593GET/api/v3/market/my-order-history?sym=BTC_THB

// Example for Post Method
1699376552354POST/api/v3/market/place-bid{"sym":"thb_btc","amt": 1000,"rat": 10,"typ": "limit"}
```

#### Example cURL:
```javascript
curl --location 'https://api.bitkub.com/api/v3/market/place-bid' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a' \
--header 'Content-Type: application/json' \
--data '{
  "sym": "thb_btc",
  "amt": 1000,
  "rat": 10,
  "typ": "limit",
}'
```
```javascript
curl --location 'https://api.bitkub.com/api/v3/market/my-open-orders?sym=BTC_THB' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a'

```

# API documentation
Refer to the following for description of each endpoint

### GET /api/status

#### Description:
Get endpoint status. When status is not `ok`, it is highly recommended to wait until the status changes back to `ok`.

#### Query:
- n/a

#### Response:
```javascript
[
  {
    "name": "Non-secure endpoints",
    "status": "ok",
    "message": ""
  },
  {
    "name": "Secure endpoints",
    "status": "ok",
    "message": ""
  }
]
```

### GET /api/servertime

#### Description:
Get server timestamp. This can't use with secure endpoint V3. Please use [/api/v3/servertime](#get-apiv3servertime).

#### Query:
- n/a

#### Response:
```javascript
1707220534359
```

### GET /api/v3/servertime

#### Description:
Get server timestamp.

#### Query:
- n/a

#### Response:
```javascript
1701251212273
```

### GET /api/v3/market/symbols

#### Description:
List all available symbols.

#### Query:
- n/a

#### Response:
```javascript
{
    "error": 0,
    "result": [
        {
            "base_asset": "BTC",
            "base_asset_scale": 8,
            "buy_price_gap_as_percent": 20,
            "created_at": "2017-10-30T22:16:10+07:00",
            "description": "Thai Baht to Bitcoin",
            "freeze_buy": false,
            "freeze_cancel": false,
            "freeze_sell": false,
            "market_segment": "SPOT",
            "min_quote_size": 10,
            "modified_at": "2025-05-20T16:48:04.599+07:00",
            "name": "Bitcoin",
            "pairing_id": 1,
            "price_scale": 2,
            "price_step": "0.01",
            "quantity_scale": 0,
            "quantity_step": "1",
            "quote_asset": "THB",
            "quote_asset_scale": 2,
            "sell_price_gap_as_percent": 20,
            "status": "active",
            "symbol": "BTC_THB",
            "source": "exchange"
        }
    ]
}
```

### GET /tradingview/history
#### Description:
Get historical data for TradingView chart.

#### Query:
* `symbol`		**string**		The symbol (e.g. BTC_THB)
* `resolution`		**string**		Chart resolution (1, 5, 15, 60, 240, 1D)
* `from`		**int**		Timestamp of the starting time (e.g. 1633424427)
* `to`		**int**		Timestamp of the ending time (e.g. 1633427427)

#### Response:
```javascript
{
  "c": [
    1685000,
    1680699.95,
    1688998.99,
    1692222.22
  ],
  "h": [
    1685000,
    1685000,
    1689000,
    1692222.22
  ],
  "l": [
    1680053.22,
    1671000,
    1680000,
    1684995.07
  ],
  "o": [
    1682500,
    1685000,
    1680100,
    1684995.07
  ],
  "s": "ok",
  "t": [
    1633424400,
    1633425300,
    1633426200,
    1633427100
  ],
  "v": [
    4.604352630000001,
    8.530631670000005,
    4.836581560000002,
    2.8510189200000022
  ]
}
```

## Market Data Endpoint

### GET /api/v3/market/ticker

### Description:
Get ticker information.

### Query (URL):
* `sym` **string** The symbol (e.g. btc_thb)

### Response:
```javascript
[
    {
        "symbol": "ADA_THB",
        "base_volume": "1875227.0489781",
        "high_24_hr": "38",
        "highest_bid": "37.33",
        "last": "37.36",
        "low_24_hr": "35.76",
        "lowest_ask": "37.39",
        "percent_change": "2.69",
        "quote_volume": "69080877.73"
    },
    {
        "symbol": "CRV_THB",
        "base_volume": "1811348.93318162",
        "high_24_hr": "39",
        "highest_bid": "38.4",
        "last": "38.42",
        "low_24_hr": "35.51",
        "lowest_ask": "38.42",
        "percent_change": "4.52",
        "quote_volume": "67340316.65"
    }
]
```


### GET /api/v3/market/bids
#### Description:
List open buy orders.

#### Query:
* `sym` **string** The symbol (e.g. btc_thb)
* `lmt` **int** No. of limit to query open buy orders

#### Response:
```javascript
{
  "error": 0,
  "result": [
    {
      "order_id": "365357265",
      "price": "3330100.43",
      "side": "buy",
      "size": "0.87901418",
      "timestamp": 1734714699000,
      "volume": "2927205.5"
    },
    {
      "order_id": "365357190",
      "price": "3330100.13",
      "side": "buy",
      "size": "0.00314952",
      "timestamp": 1734689476000,
      "volume": "10488.24"
    }
  ]
}

```

### GET /api/v3/market/asks


#### Description:
List open sell orders.

#### Query:
* `sym` **string** The symbol (e.g. btc_thb)
* `lmt` **int** No. of limit to query open sell orders

#### Response:
```javascript
{
  "error": 0,
  "result": [
    {
      "order_id": "303536416",
      "price": "3334889",
      "side": "sell",
      "size": "0.01289714",
      "timestamp": 1734689550000,
      "volume": "42903"
    },
    {
      "order_id": "303536239",
      "price": "3334889.31",
      "side": "sell",
      "size": "0.129",
      "timestamp": 1734714713000,
      "volume": "430200.72"
    }
  ]
}
```

### GET /api/v3/market/depth

#### Description:
Get depth information.

#### Query:
* `sym` **string** The symbol (e.g. btc_thb)
* `lmt` **int** Depth size

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "asks": [
      [
       3338932.98, // price
       0.00619979, //size
      ],
      [
       3341006.36, // price
       0.00134854 //size
      ]
    ],
    "bids": [
      [
        3334907.27, // price
        0.00471255 //size
      ],
      [
        3334907.26, // price
        0.36895805 //size
      ]
    ]
  }
}
```

### GET /api/v3/market/trades

#### Description:
List recent trades.

#### Query:
* `sym`		**string** The symbol (e.g. btc_thb)
* `lmt`		**int** No. of limit to query recent trades

#### Response:
```javascript
{
    "error": 0,
    "result": [
        [
            1734661894000,
            3367353.98,
            0.00148484,
            "BUY"
        ],
        [
            1734661893000,
            3367353.98,
            0.00029622,
            "BUY"
        ]
    ]
}
```
## Trading Endpoint V3


### POST /api/v3/market/wallet

#### Description:
Get user available balances (for both available and reserved balances please use [POST /api/v3/market/balances](#post-apiv3marketbalances)).

#### Query:
- n/a

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "THB": 188379.27,
    "BTC": 8.90397323,
    "ETH": 10.1
  }
}
```
### POST /api/v3/user/trading-credits

### Description:
Check trading credit balance.

### Query (URL):
-

### Response:
```javascript
{
   "error": 0,
   "result": 1000
}
```

### POST /api/v3/market/place-bid

#### Description:
Create a buy order.

#### Body:
* `sym`   **string**    The symbol you want to trade (e.g. btc_thb).
* `amt`   **float**   Amount you want to spend with no trailing zero (e.g. 1000.00 is invalid, 1000 is ok)
* `rat`   **float**   Rate you want for the order with no trailing zero (e.g. 1000.00 is invalid, 1000 is ok)
* `typ`   **string**    Order type: limit or market (for market order, please specify rat as 0)
* `client_id` **string**    your id for reference ( not required )
* `post_only`   **bool**    Postonly flag: true or false ( not required )

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "id": "1", // order id
    "typ": "limit", // order type
    "amt": 1000, // spending amount
    "rat": 15000, // rate
    "fee": 2.5, // fee
    "cre": 2.5, // fee credit used
    "rec": 0.06666666, // amount to receive
    "ts": "1707220636" // timestamp
    "ci": "input_client_id" // input id for reference
  }
}
```

### POST /api/v3/market/place-ask

#### Description:
Create a sell order.

#### Body:
* `sym`   **string**    The symbol. The symbol you want to trade (e.g. btc_thb).
* `amt`   **float**   Amount you want to sell with no trailing zero (e.g. 0.10000000 is invalid, 0.1 is ok)
* `rat`   **float**   Rate you want for the order with no trailing zero (e.g. 1000.00 is invalid, 1000 is ok)
* `typ`   **string**    Order type: limit or market (for market order, please specify rat as 0)
* `client_id`   **string**    your id for reference ( not required )
* `post_only`   **bool**    Postonly flag: true or false ( not required )


#### Response:
```javascript
{
  "error": 0,
  "result": {
    "id": "1", // order id
    "typ": "limit", // order type
    "amt": 1.00000000, // selling amount
    "rat": 15000, // rate
    "fee": 37.5, // fee
    "cre": 37.5, // fee credit used
    "rec": 15000, // amount to receive
    "ts": "1533834844" // timestamp
    "ci": "input_client_id" // input id for reference
  }
}
```

### POST /api/v3/market/cancel-order

### Description:
Cancel an open order.

### Body:
* `sym`   **string**    The symbol. ***Please note that the current endpoint requires the symbol thb_btc. However, it will be changed to btc_thb soon and you will need to update the configurations accordingly for uninterrupted API functionality.***
* `id`    **string**   Order id you wish to cancel
* `sd`    **string**    Order side: buy or sell

### Response:
```javascript
{
  "error": 0
}
```
### POST /api/v3/market/balances

#### Description:
Get balances info: this includes both available and reserved balances.

#### Query:
- n/a

#### Response:
```javascript
{
  "error": 0,
  "result": {
    "THB":  {
      "available": 188379.27,
      "reserved": 0
    },
    "BTC": {
      "available": 8.90397323,
      "reserved": 0
    },
    "ETH": {
      "available": 10.1,
      "reserved": 0
    }
  }
}
```
### GET /api/v3/market/my-open-orders

### Description:
List all open orders of the given symbol.

### Query:
* `sym`		**string**		The symbol (e.g. btc_thb)

### Response:
```javascript
{
  "error": 0,
  "result": [
    { // Example of sell order
      "id": "2", // order id
      "side": "sell", // order side
      "type": "limit", // order type
      "rate": "15000", // rate
      "fee": "35.01", // fee
      "credit": "35.01", // credit used
      "amount": "0.93333334", // amount of crypto quantity
      "receive": "14000", // amount of THB 
      "parent_id": "1", // parent order id
      "super_id": "1", // super parent order id
      "client_id": "client_id" // client id
      "ts": 1702543272000 // timestamp
    },
    { // Example of buy order
      "id": "278465822",
      "side": "buy",
      "type": "limit",
      "rate": "10",
      "fee": "0.25",
      "credit": "0",
      "amount": "100", // amount of THB 
      "receive": "9.975", // amount of crypto quantity
      "parent_id": "0",
      "super_id": "0",
      "client_id": "client_id",
      "ts": 1707220636000
    },
  ]
}
```
Note : The ```client_id``` of this API response is the input body field name ```client_id``` , was inputted by the user of APIs 
* [api/v3/market/place-bid](#post-apiv3marketplace-bid)
* [api/v3/market/place-ask](#post-apiv3marketplace-ask)



### GET /api/v3/market/my-order-history

### Description:
List all orders that have already matched.

#### Query:
* `sym` **string** The trading symbol (e.g. BTC_THB)
* `p` **string** Page number for page-based pagination (optional)
* `lmt` **string** Limit per page, default: 10, min: 1 (optional)
* `cursor` **string** Base64 encoded cursor for keyset pagination (optional)
* `start` **string** Start timestamp (optional)
* `end` **string** End timestamp (optional)
* `pagination_type` **string** Pagination type: "page" or "keyset", default: "page" (optional)

#### Validation Rules:
- `sym` is required and must be a valid trading symbol
- `p` and `cursor` cannot be used together
- `p` requires `pagination_type=page` or no pagination_type specified
- `cursor` requires `pagination_type=keyset`
- `lmt` must be a positive integer >= 1
- `start` and `end` must be valid timestamps if provided
- `start` must be less than `end` if both provided

#### Response (Page-based pagination):
```json
{
    "error": 0,
    "result": [
        {
            "txn_id": "68a82566596d482000f4e4edaa05m0",
            "order_id": "68a82566596d482000f4e4edaa05m0",
            "parent_order_id": "68a82566596d482000f4e4edaa05m0",
            "super_order_id": "68a82566596d482000f4e4edaa05m0",
            "client_id": "CLIENT123",
            "taken_by_me": false,
            "is_maker": true,
            "side": "buy",
            "type": "limit",
            "rate": "2500000.00",
            "fee": "25.00",
            "credit": "0.00",
            "amount": "1000.00",
            "ts": 1755850086843,
            "order_closed_at": 1755850086843
        }
    ],
    "pagination": {
        "page": 1,
        "last": 10,
        "next": 2,
        "prev": null
    }
}
```

#### Response (Keyset-based pagination):
```json
{
    "error": 0,
    "result": [
        {
            "txn_id": "68a82566596d482000f4e4edaa05m0",
            "order_id": "68a82566596d482000f4e4edaa05m0",
            "parent_order_id": "68a82566596d482000f4e4edaa05m0",
            "super_order_id": "68a82566596d482000f4e4edaa05m0",
            "client_id": "CLIENT123",
            "taken_by_me": false,
            "is_maker": true,
            "side": "buy",
            "type": "limit",
            "rate": "2500000.00",
            "fee": "25.00",
            "credit": "0.00",
            "amount": "1000.00",
            "ts": 1755850086843,
            "order_closed_at": 1755850086843
        }
    ],
    "pagination": {
        "cursor": "eyJpZCI6Ik9SRDEyMzQ1Njc4OSIsInRzIjoiMTY3MjUzMTIwMCJ9",
        "has_next": true
    }
}
```

#### Response Fields:

**Order Item Fields:**
- `txn_id`: Transaction ID
- `order_id`: Unique order identifier
- `parent_order_id`: Parent order ID (for linked orders)
- `super_order_id`: Super order ID (for grouped orders)
- `client_id`: Client-provided order ID
- `taken_by_me`: Whether the order was taken by the user
- `is_maker`: Whether the order was a maker order
- `side`: Order side ("buy" or "sell")
- `type`: Order type ("limit" or "market")
- `rate`: Order price/rate
- `fee`: Fee paid in THB
- `credit`: Credit used for fee payment
- `amount`: Order amount (quote quantity for buy orders, base quantity for sell orders)
- `ts`: Order close timestamp in millisecond
- `order_closed_at`: Order closure timestamp in millisecond (nullable)

**Pagination Fields (Page-based):**
- `page`: Current page number
- `last`: Total number of pages
- `next`: Next page number (nullable)
- `prev`: Previous page number (nullable)

**Pagination Fields (Keyset-based):**
- `cursor`: Base64 encoded cursor for next page
- `has_next`: Whether there are more records

#### Cursor Encoding Details:

The `cursor` parameter uses Base64 encoding of a JSON object containing pagination state:

**Cursor Structure:**
```json
{
  "id": "ORDER_ID_STRING",
  "ts": "TIMESTAMP_DECIMAL"
}
```

**Encoding Process:**
1. Create JSON object with `id` (order ID) and `ts` (timestamp as decimal)
2. Convert JSON to string
3. Encode string using Base64 standard encoding

**Example:**
```json
// Original cursor object
{
  "id": "ORD123456789", 
  "ts": "1672531200"
}

// JSON string
'{"id":"ORD123456789","ts":"1672531200"}'

// Base64 encoded
"eyJpZCI6Ik9SRDEyMzQ1Njc4OSIsInRzIjoiMTY3MjUzMTIwMCJ9"
```

**Custom Cursor Creation:**
Users can create custom cursors by:
1. Taking the last item's `order_id` and `ts` from previous response
2. Creating JSON: `{"id":"LAST_ORDER_ID","ts":"LAST_TIMESTAMP"}`
3. Base64 encoding the JSON string
4. Using encoded string as `cursor` parameter

**Empty Cursor:**
- Default empty cursor: `e30=` (Base64 of `{}`)
- Used when no cursor is provided in keyset pagination

### GET /api/v3/market/order-info
### Description:
Get information regarding the specified order.

### Query:
* `sym`		**string**		The symbol (e.g. btc_thb)
* `id`		**string**		Order id
* `sd`		**string**		Order side: buy or sell

### Response:
```javascript
{
    "error": 0,
    "result": {
        "id": "289", // order id
        "first": "289", // first order id
        "parent": "0", // parent order id
        "last": "316", // last order id
        "client_id": "", // your id for reference
        "post_only": false, // post_only: true, false
        "amount": "4000", // order amount THB amount if it Buy side. And Crypto Amount if it sell side
        "rate": 291000, // order rate
        "fee": 10, // order fee
        "credit": 10, // order fee credit used
        "filled": 3999.97, // filled amount
        "total": 4000, // total amount
        "status": "filled", // order status: filled, unfilled, cancelled
        "partial_filled": false, // true when order has been partially filled, false when not filled or fully filled
        "remaining": 0, // remaining amount to be executed
        "history": [
            {
                "amount": 98.14848,
                "credit": 0.25,
                "fee": 0.25,
                "id": "289",
                "rate": 291000,
                "timestamp": 1702466375000,
                "txn_id": "BTCBUY0003372258"
            }
        ]
    }
}
```

## Fiat Endpoint

### POST /api/v3/fiat/accounts

### Description:
List all approved bank accounts.

### Query (URL):
* `p` **int** Page (optional)
* `lmt` **int** Limit (optional)

### Response:
```javascript
{
   "error": 0,
   "result": [
      {
         "id": "7262109099",
         "bank": "Kasikorn Bank",
         "name": "Somsak",
         "time": 1570893867
      }
   ],
   "pagination": {
      "page": 1,
      "last": 1
   }
}
```

### POST /api/v3/fiat/withdraw

### Description:
Make a withdrawal to an **approved** bank account.

### Query:
* `id`		**string**	Bank account id
* `amt`		**float**		Amount you want to withdraw

### Response:
```javascript
{
    "error": 0,
    "result": {
        "txn": "THBWD0000012345", // local transaction id
        "acc": "7262109099", // bank account id
        "cur": "THB", // currency
        "amt": 21, // withdraw amount
        "fee": 20, // withdraw fee
        "rec": 1, // amount to receive
        "ts": 1569999999 // timestamp
    }
}
```

### POST /api/v3/fiat/deposit-history

### Description:
List fiat deposit history.

### Query (URL):
* `p` **int** Page (optional)
* `lmt` **int** Limit (optional)

### Response:
```javascript
{
   "error": 0,
   "result": [
      {
         "txn_id": "THBDP0000012345",
         "currency": "THB",
         "amount": 5000.55,
         "status": "complete",
         "time": 1570893867
      }
   ],
   "pagination": {
      "page": 1,
      "last": 1
   }
}
```

### POST /api/v3/fiat/withdraw-history

### Description:
List fiat withdrawal history.

### Query (URL):
* `p` **int** Page (optional)
* `lmt` **int** Limit (optional)

### Response:
```javascript
{
   "error":0,
   "result": [
      {
         "txn_id": "THBWD0000012345",
         "currency": "THB",
         "amount": "21",
         "fee": 20,
         "status": "complete",
         "time": 1570893493
      }
   ],
   "pagination": {
      "page": 1,
      "last": 1
   }
}
```

## User information Endpoint

### POST /api/v3/user/limits

### Description:
Check deposit/withdraw limitations and usage.

### Query (URL):
-

### Response:
```javascript
{
   "error": 0,
   "result": { 
       "limits": { // limitations by kyc level
          "crypto": { 
             "deposit": 0.88971929, // BTC value equivalent
             "withdraw": 0.88971929 // BTC value equivalent
          },
          "fiat": { 
             "deposit": 200000, // THB value equivalent
             "withdraw": 200000 // THB value equivalent
          }
       },
       "usage": { // today's usage
          "crypto": { 
             "deposit": 0, // BTC value equivalent
             "withdraw": 0, // BTC value equivalent
             "deposit_percentage": 0,
             "withdraw_percentage": 0,
             "deposit_thb_equivalent": 0, // THB value equivalent
             "withdraw_thb_equivalent": 0 // THB value equivalent
          },
          "fiat": { 
             "deposit": 0, // THB value equivalent
             "withdraw": 0, // THB value equivalent
             "deposit_percentage": 0,
             "withdraw_percentage": 0
          }
       },
       "rate": 224790 // current THB rate used to calculate
    }
}
```
### GET /api/v3/user/coin-convert-history
### Description:
List all coin convert histories (paginated).

### Query (URL):
* `p` **int** Page default = 1 (optional)
* `lmt` **int** Limit default = 100 (optional)
* `sort` **int** Sort [1, -1] default = 1 (optional)
* `status` **string** Status [success, fail, all] (default = all) (optional)
* `sym` **string** The symbol (optional)
  * e.g. KUB
* `start` **int** Start timestamp (optional)
* `end` **int** End timestamp (optional)


### Response:
```javascript
{
    "error": 0,
    "result": [
        {
            "transaction_id": "67ef4ca7ddb88f34ce16a126",
            "status": "success",
            "amount": "0.0134066",
            "from_currency": "KUB",
            "trading_fee_received": "1.34",
            "timestamp": 1743761171000
        },
        {
            "transaction_id": "6707a7426fb3370035725c03",
            "status": "fail",
            "amount": "0.000006",
            "from_currency": "KUB",
            "trading_fee_received": "0",
            "timestamp": 1728580016000
        }
    ],
    "pagination": {
        "page": 1,
        "last": 12,
        "next": 2
    }
}
```


# Error codes
Refer to the following descriptions:

| Code | Message                | Description                                                |
| ---- | ---------------------- | ---------------------------------------------------------- |
| 0    | | No error                                                           |
| 1    | | Invalid JSON payload                                               |
| 2    | | Missing X-BTK-APIKEY                                               |
| 3    | | Invalid API key                                                    |
| 4    | | API pending for activation                                         |
| 5    | | IP not allowed                                                     |
| 6    | | Missing / invalid signature                                        |
| 7    | | Missing timestamp                                                  |
| 8    | | Invalid timestamp                                                  |
| 9    | | • Invalid user <br> • User not found <br> • Freeze withdrawal <br> • User is not allowed to perform this action within the last 24 hours <br> • User has suspicious withdraw crypto txn |
| 10   | | • Invalid parameter <br> • Invalid response: Code not found in response <br> • Validate params <br> • Default |
| 11   | | Invalid symbol                                                     |
| 12   | | • Invalid amount <br> • Withdrawal amount is below the minimum threshold |
| 13   | | Invalid rate                                                       |
| 14   | | Improper rate                                                      |
| 15   | | Amount too low                                                     |
| 16   | | Failed to get balance                                              |
| 17   | | Wallet is empty                                                    |
| 18   | | Insufficient balance                                               |
| 19   | | Failed to insert order into db                                     |
| 20   | | Failed to deduct balance                                           |
| 21   | | Invalid order for cancellation (Unable to find OrderID or Symbol.) |
| 22   | | Invalid side                                                       |
| 23   | | Failed to update order status                                      |
| 24   | | • Invalid order for lookup <br> • Invalid kyc level |
| 25   | | KYC level 1 is required to proceed                                 |
| 30   | | Limit exceeds                                                      |
| 40   | | Pending withdrawal exists                                          |
| 41   | | Invalid currency for withdrawal                                    |
| 42   | | Address is not in whitelist                                        |
| 43   | | • Failed to deduct crypto <br> • Insufficient balance <br> • Deduct balance failed |
| 44   | | Failed to create withdrawal record                                 |
| 47   | | Withdrawal amount exceeds the maximum limit                                           |
| 48   | | • Invalid bank account <br> • User bank id is not found <br> • User bank is unavailable |
| 49   | | Bank limit exceeds                                                 |
| 50   | | • Pending withdrawal exists <br> • Cannot perform the action due to pending transactions |
| 51   | | Withdrawal is under maintenance                                    |
| 52   | | Invalid permission                                                 |
| 53   | | Invalid internal address                                           |
| 54   | | Address has been deprecated                                        |
| 55   | | Cancel only mode                                                   |
| 56   | | User has been suspended from purchasing                            |
| 57   | | User has been suspended from selling                               |
| 58   | | ~~Transaction not found~~ <br> User bank is not verified           |
| 61   | | This endpoint doesn't support broker coins ('source' = broker). You can check 'source' of each symbol in /api/v3/market/symbols. |
| 90   | | Server error (please contact support)                              |

# Rate limits 
If the request rate exceeds the limit in any endpoints, the request will be blocked for 30 seconds. When blocked, HTTP response is 429 Too Many Requests. The limits apply to individual user accessing the API. ***The rate limit is applied to each endpoint regardless the API version.***

| Endpoint                     | Rate Limit       |
| ---------------------------- | ---------------- |
| /api/v3/market/ticker        | 100 req/sec      |
| /api/v3/market/depth         | 10 req/sec       |
| /api/v3/market/symbols       | 100 req/sec      |
| /api/v3/market/trades        | 100 req/sec      |
| /api/v3/market/bids          | 100 req/sec      |
| /api/v3/market/asks          | 100 req/sec      |
| /api/market/order-info       | 100 req/sec      |
| /api/market/my-open-orders   | 150 req/sec      |
| /api/market/my-order-history | 100 req/sec      |
| /api/market/place-bid        | 150 req/sec       |
| /api/market/place-ask        | 150 req/sec       |
| /api/market/cancel-order     | 200 req/sec      |
| /api/market/balances         | 150 req/sec      |
| /api/market/wallet           | 150 req/sec      |
| /api/servertime              | 2,000 req/10secs |
| /api/status                  | 100 req/sec      |
| /api/fiat/*                  | 20 req/sec       |
| /api/user/*                  | 20 req/sec       |
| /tradingview/*               | 100 req/sec      |
# RESTful API for Bitkub V4 (2025-12-03)

# Announcement

- Deposit history records are available for the last 90 days only for [GET /api/v4/crypto/deposits](#get-apiv4cryptodeposits). Records older than 90 days are archived.
- Introducing the New Public API v4 for Crypto Endpoints

# Change log

- 2025-05-27 Added new Crypto endpoint [GET /api/v4/crypto/compensations](#get-apiv4cryptocompensations) and update api specification for [GET /api/v4/crypto/withdraws](#get-apiv4cryptowithdraws) and [GET /api/v4/crypto/deposits](#get-apiv4cryptodeposits)
- 2025-04-08 Added new error codes: [B1016-CW] Deposit is frozen, [V1015-CW] Coin not found
- 2025-04-03 Added new Crypto endpoint [GET /api/v4/crypto/coins](#get-apiv4cryptocoins)
- 2025-02-03 Introducing Crypto V4 Endpoints

# Table of contents

- [Base URL](#base-url)
- [Endpoint types](#endpoint-types)
- [Constructing the request](#constructing-the-request)
- [API documentation](#api-documentation)
- [Error codes](#error-codes)
- [Rate limits](#rate-limits)

# Base URL

- The base URL is: https://api.bitkub.com

# Endpoint types

### Secure endpoints V4

All secure endpoints require [authentication](#constructing-the-request).

| Crypto V4 Endpoints                                           | Method | Deposit | Withdraw | Trade |
| ------------------------------------------------------------- | ------ | ------- | -------- | ----- |
| [/api/v4/crypto/addresses](#get-apiv4cryptoaddresses)         | GET    |         |          |       |
| [/api/v4/crypto/addresses](#post-apiv4cryptoaddresses)        | POST   | ✅      |          |       |
| [/api/v4/crypto/deposits](#get-apiv4cryptodeposits)           | GET    |         |          |       |
| [/api/v4/crypto/withdraws](#get-apiv4cryptowithdraws)         | GET    |         |          |       |
| [/api/v4/crypto/withdraws](#post-apiv4cryptowithdraws)        | POST   |         | ✅       |       |
| [/api/v4/crypto/coins](#get-apiv4cryptocoins)                 | GET    |         |          |       |
| [/api/v4/crypto/compensations](#get-apiv4cryptocompensations) | GET    |         |          |       |

# Constructing the request

### GET/POST request

- GET requests require parameters as **query string** in the URL (e.g. ?symbol=BTC&limit=10).
- POST requests require JSON payload (application/json).

### Request headers (Secure Endpoints)

Authentication requires API KEY and API SECRET. Every request to the server must contain the following in the request header:

- Accept: application/json
- Content-type: application/json
- X-BTK-APIKEY: {YOUR API KEY}
- X-BTK-TIMESTAMP: {Timestamp i.e. 1699376552354 }
- X-BTK-SIGN: [Signature](#signature)

### Signature

Generate the signature from the timestamp, the request method, API path, query parameter, and JSON payload using HMAC SHA-256. Use the API Secret as the secret key for generating the HMAC variant of JSON payload. The signature is in **hex** format. The user has to attach the signature via the Request Header
You must get a new timestamp in millisecond from [/api/v3/servertime](restful-api.md#get-apiv3servertime). The old one is in second.

#### Example string for signing a signature:

```javascript
//Example for Get Method
1699381086593GET/api/v4/crypto/addresses?symbol=ATOM

// Example for Post Method
1699376552354POST/api/v4/crypto/addresses{"symbol":"ATOM","network": "ATOM"}
```

#### Example cURL:

```javascript
curl --location 'https://api.bitkub.com/api/v4/crypto/addresses?symbol=ATOM' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a'
```

```javascript
curl --location 'https://api.bitkub.com/api/v4/crypto/addresses' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a' \
--header 'Content-Type: application/json' \
--data '{
    "symbol": "ATOM",
    "network": "ATOM",
}'
```

# API documentation

Refer to the following for description of each endpoint

### GET /api/v4/crypto/addresses

#### Description:

List all crypto addresses (paginated).

#### Path Params: -

#### Query Params:

| Key     | Type   | Required | Description                      |
| ------- | ------ | -------- | -------------------------------- |
| page    | int    | false    | Page (default = 1)               |
| limit   | int    | false    | Limit (default = 100, max = 200) |
| symbol  | String | false    | e.g. ATOM                        |
| network | String | false    | e.g. ATOM                        |
| memo    | String | false    | e.g. 107467228685                |

#### Body Params: -

#### Example cURL:

```javascript
curl --location 'https://api.bitkub.com/api/v4/crypto/addresses?symbol=ATOM' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a'
```

#### Response:

```javascript
{
  "code": "0",
  "message": "success",
  "data": {
    "page": 1,
    "total_page": 1,
    "total_item": 2,
    "items": [
      {
        "symbol": "ATOM",
        "network": "ATOM",
        "address": "cosmos1jcslcmz2lpsy7uq5u2ktn459qce2chqapey7gh",
        "memo": "107467228685",
        "created_at": "2022-03-18T05:41:40.199Z"
      },
      {
        "symbol": "ATOM",
        "network": "ATOM",
        "address": "cosmos1jcslcmz2lpsy7uq5u2ktn459qce2chqapey7gh",
        "memo": "104010164476",
        "created_at": "2022-03-18T05:46:34.113Z"
      }
    ]
  }
}
```

### POST /api/v4/crypto/addresses

#### Description:

Generate a new crypto address (if an address exists; will return the existing address).

#### Required Permission: `is_deposit`

#### Path Params: -

#### Query Params: -

#### Body Params:

| Key     | Type   | Required | Description |
| ------- | ------ | -------- | ----------- |
| symbol  | String | true     | e.g. ATOM   |
| network | String | true     | e.g. ATOM   |

#### Example cURL:

```javascript
curl --location 'https://api.bitkub.com/api/v4/crypto/addresses' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a' \
--header 'Content-Type: application/json' \
--data '{
    "symbol": "ETH",
    "network": "ETH",
}'
```

#### Response:

```javascript
{
  "code": "0",
  "message": "success",
  "data": [
    {
      "symbol": "ETH",
      "network": "ETH",
      "address": "0x520165471daa570ab632dd504c6af257bd36edfb",
      "memo": ""
    }
  ]
}
```

### GET /api/v4/crypto/deposits

#### Description:

List crypto deposit history.

#### Note: Only deposit records within the last 90 days will be returned.

#### Path Params: -

#### Query Params:

| Key           | Type   | Required | Description                                                                                                                                                                |
| ------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page          | int    | false    | Page (default = 1)                                                                                                                                                         |
| limit         | int    | false    | Limit (default = 100, max = 200)                                                                                                                                           |
| symbol        | String | false    | Coin Symbol (e.g. BTC, ETH)                                                                                                                                                |
| status        | String | false    | Transaction Deposit Status (pending, rejected, complete)                                                                                                                   |
| created_start | String | false    | The start of the time range for the transaction creation timestamp. Only transactions created on or after this timestamp will be included. (e.g. 2025-01-11T10:00:00.000Z) |
| created_end   | String | false    | The end of the time range for the transaction creation timestamp. Only transactions created on or before this timestamp will be included. (e.g. 2025-01-11T10:00:00.000Z)  |

#### Body Params: -

#### Example cURL:

```javascript
curl --location 'https://api.bitkub.com/api/v4/crypto/deposits?limit=10' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a'
```

#### Response:

```javascript
{
  "code": "0",
  "message": "success",
  "data": {
    "page": 1,
    "total_page": 1,
    "total_item": 1,
    "items": [
     {
        "hash": "XRPWD0000100276",
        "symbol": "XRP",
        "network": "XRP",
        "amount": "5.75111474",
        "from_address": "0xDaCd17d1E77604aaFB6e47F5Ffa1F7E35F83fDa7",
        "to_address": "0x2b0849d47a90e3c4784a5b1130a14305a099d828",
        "confirmations": 1,
        "status": "complete",
        "created_at": "2022-03-18T05:41:40.199Z",
        "completed_at": "2022-03-18T05:45:50.199Z"
      }
    ]
  }
}
```

### GET /api/v4/crypto/withdraws

#### Description:

List crypto withdrawal history.

#### Path Params: -

#### Query Params:

| Key           | Type   | Required | Description                                                                                                                                                                |
| ------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page          | int    | false    | Page (default = 1)                                                                                                                                                         |
| limit         | int    | false    | Limit (default = 100, max = 200)                                                                                                                                           |
| symbol        | String | false    | Coin Symbol (e.g. BTC, ETH)                                                                                                                                                |
| status        | String | false    | Transaction Withdraw Status (pending, processing, reported, rejected, complete)                                                                                            |
| created_start | String | false    | The start of the time range for the transaction creation timestamp. Only transactions created on or after this timestamp will be included. (e.g. 2025-01-11T10:00:00.000Z) |
| created_end   | String | false    | The end of the time range for the transaction creation timestamp. Only transactions created on or before this timestamp will be included. (e.g. 2025-01-11T10:00:00.000Z)  |

#### Body Params: -

#### Example cURL:

```javascript
curl --location 'https://api.bitkub.com/api/v4/crypto/withdraws?limit=10' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a'
```

#### Response:

```javascript
{
  "code": "0",
  "message": "success",
  "data": {
    "page": 1,
    "total_page": 1,
    "total_item": 2,
    "items": [
       {
        "txn_id": "RDNTWD0000804050",
        "external_ref": "XX_1111111111",
        "hash": null,
        "symbol": "RDNT",
        "network": "ARB",
        "amount": "2.00000000",
        "fee": "4.36",
        "address": "0xDaCd17d1E77604aaFB6e47F5Ffa1F7E35F83fDa7",
        "memo": "",
        "status": "processing",
        "created_at": "2024-09-01T10:02:43.211Z",
        "completed_at": "2024-09-01T10:02:45.031Z"
      },
      {
        "txn_id": "BTCWD1321312683",
        "external_ref": "XX_1111111112",
        "hash": "0x8891b79c79f0842c9a654db47745fe0291fba222b290d22cabc93f8ae4490303",
        "symbol": "BTC",
        "network": "BTC",
        "amount": "0.10000000",
        "fee": "0.0025",
        "address": "0xDaCd17d1E77604aaFB6e47F5Ffa1F7E35F83fDa7",
        "memo": "",
        "status": "complete",
        "created_at": "2024-09-01T10:02:43.211Z",
        "completed_at": "2024-09-01T10:02:45.031Z"
      }
    ]
  }
}
```

### POST /api/v4/crypto/withdraws

#### Description:

Make a withdrawal to a trusted address.

#### Required Permission: `is_withdraw`

#### Path Params: -

#### Query Params: -

#### Body Params:

| Key     | Type   | Required | Description                           |
| ------- | ------ | -------- | ------------------------------------- |
| symbol  | String | true     | Symbol for withdrawal (e.g. BTC, ETH) |
| amount  | String | true     | Amount to withdraw                    |
| address | String | true     | Address to withdraw                   |
| memo    | String | false    | Memo or destination tag to withdraw   |
| network | String | true     | Network to withdraw                   |

#### Example cURL:

```javascript
curl --location 'https://api.bitkub.com/api/v4/crypto/withdraws' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a' \
--header 'Content-Type: application/json' \
--data '{
    "symbol": "RDNT",
    "amount": "2.00000000",
    "address": "0xDaCd17d1E77604aaFB6e47F5Ffa1F7E35F83fDa7",
    "network": "ARB"
}'
```

#### Response:

```javascript
{
  "code": "0",
  "message": "success",
  "data": {
    "txn_id": "RDNTWD0000804050",
    "symbol": "RDNT",
    "network": "ARB",
    "amount": "2.00000000",
    "fee": "4.36",
    "address": "0xDaCd17d1E77604aaFB6e47F5Ffa1F7E35F83fDa7",
    "memo": "",
    "created_at": "2024-09-01T10:02:43.211Z"
  }
}
```

### GET /api/v4/crypto/coins

#### Description:

Get all coins (available for deposit and withdraw).

#### Path Params: -

#### Query Params:

| Key     | Type   | Required | Description                 |
| ------- | ------ | -------- | --------------------------- |
| symbol  | String | false    | Coin Symbol (e.g. BTC, ETH) |
| network | String | false    | Network                     |

#### Body Params: -

#### Example cURL:

```javascript
curl --location 'https://api.bitkub.com/api/v4/crypto/coin?symbol=ATOM' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a'
```

#### Response:

```javascript
{
  "code": "0",
  "message": "success",
  "data": {
    "items":[
      {
        "name": "Bitcoin",
        "symbol": "BTC",
        "networks": [
          {
            "name": "Bitcoin",
            "network": "BTC",
            "address_regex": "^[13][a-km-zA-HJ-NP-Z1-9]{26,35}$|^(tb1)[0-9A-Za-z]{39,59}$",
            "memo_regex": "",
            "explorer": "https://www.blockchain.com/btc/tx/",
            "contract_address": "",
            "withdraw_min": "0.0002",
            "withdraw_fee": "0.0001",
            "withdraw_internal_min": "",
            "withdraw_internal_fee": "",
            "withdraw_decimal_places": 8,
            "min_confirm": 3,
            "decimal": 8,
            "deposit_enable": true,
            "withdraw_enable": true,
            "is_memo": false
          }
        ],
        "deposit_enable": true,
        "withdraw_enable": true
      }
    ]
  }
}
```

### GET /api/v4/crypto/compensations

#### Description:

List crypto compensations history.

#### Path Params: -

#### Query Params:

| Key           | Type   | Required | Description                                                                                                                                                                |
| ------------- | ------ | -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| page          | int    | false    | Page (default = 1)                                                                                                                                                         |
| limit         | int    | false    | Limit (default = 100, max = 200)                                                                                                                                           |
| symbol        | String | false    | Coin Symbol (e.g. BTC, ETH)                                                                                                                                                |
| type          | String | false    | Compensation Type (COMPENSATE,DECOMPENSATE)                                                                                                                                |
| status        | String | false    | Transaction Compensation Status (complete)                                                                                                                                 |
| created_start | String | false    | The start of the time range for the transaction creation timestamp. Only transactions created on or after this timestamp will be included. (e.g. 2025-01-11T10:00:00.000Z) |
| created_end   | String | false    | The end of the time range for the transaction creation timestamp. Only transactions created on or before this timestamp will be included. (e.g. 2025-01-11T10:00:00.000Z)  |

#### Body Params: -

#### Example cURL:

```javascript
curl --location 'https://api.bitkub.com/api/v4/crypto/compensations?symbol=ATOM' \
--header 'X-BTK-TIMESTAMP: 1699381086593' \
--header 'X-BTK-APIKEY: e286825bda3497ae2d03aa3a30c420d603060cb4edbdd3ec711910c86966e9ba' \
--header 'X-BTK-SIGN: f5884963865a6e868ddbd58c9fb9ea4bd013076e8a8fa51d38b86c38d707cb8a'
```

#### Response:

```javascript
{
  "code": "0",
  "message": "Success",
  "data": {
    "page": 1,
    "total_page": 1,
    "total_item": 2,
    "items": [
      {
        "txn_id": "XRPCP0000001234",
        "symbol": "XRP",
        "type": "DECOMPENSATE",
        "amount": "-1",
        "status": "complete",
        "created_at": "2024-02-09T12:00:00Z",
        "completed_at": "2024-02-09T13:00:00Z",
        "user_id": "1234"
      },
      {
        "txn_id": "BLUECP0000001234",
        "symbol": "BLUE",
        "type": "COMPENSATE",
        "amount": "20",
        "status": "complete",
        "created_at": "2025-04-09T18:30:04Z",
        "completed_at": "2025-04-09T18:30:04Z",
        "user_id": "1234"
      }
    ]
  }
}
```

## Additional

For the use of coins and networks, please use coin or network symbol for any APIs request. Please be cautious of these cryptocurrency when you specified on the request.\
\
Please refer to the link below for the available coins and networks.\
https://www.bitkub.com/fee/cryptocurrency \
\
Note the following exceptions for the coin and network:

| Currency / Network  | Symbol  |
| ------------------- | ------- |
| Terra Classic(LUNC) | `LUNA`  |
| Terra 2.0 (LUNA)    | `LUNA2` |

# Error codes

The following is the JSON payload for the Response Error:

```javascript
{
   "code": "V1007-CW",
   "message": "Symbol not found",
   "data": {}
 }
```

## Status Codes

#### 200 (OK)

The request was processed as expected.

#### 400 (INVALID_REQUEST)

The request is not well-formed, violates schema, or has incorrect fields.

#### 401 (NOT_AUTHORIZED)

The API key doesn't match the signature or have the necessary permissions to perform the request.

#### 403 (FORBIDDEN)

The API key doesn't have the necessary permissions to complete the request.

#### 404 (NOT_FOUND)

The requested resource doesn't exist.

#### 5XX

Internal Server Error.

| Code     | Status | Message                |
| -------- | ------ | ---------------------- |
| S1000-CW | 500    | Internal service error |

### Business Error

| Code     | Status | Message                        |
| -------- | ------ | ------------------------------ |
| B1000-CW | 400    | User account is suspended      |
| B1001-CW | 400    | Network is disabled            |
| B1002-CW | 400    | CWS Wallet not found           |
| B1003-CW | 400    | Insufficient balance           |
| B1004-CW | 400    | User mismatch condition        |
| B1005-CW | 400    | Duplicate key                  |
| B1006-CW | 400    | Airdrop already transfer       |
| B1007-CW | 400    | Symbol required                |
| B1008-CW | 400    | Event Symbol mismatched        |
| B1009-CW | 400    | Pending withdrawal exists      |
| B1010-CW | 400    | User account is frozen         |
| B1011-CW | 400    | Withdrawal exceeds daily limit |
| B1012-CW | 400    | Address is not trusted         |
| B1013-CW | 400    | Withdrawal is frozen           |
| B1014-CW | 400    | Address is not whitelisted     |
| B1015-CW | 400    | Request is processing          |
| B1016-CW | 400    | Deposit is frozen              |

### Validation Error

| Code     | Status | Message                                   |
| -------- | ------ | ----------------------------------------- |
| V1000-CW | 404    | User not found                            |
| V1001-CW | 404    | Asset not found                           |
| V1002-CW | 404    | Event not found                           |
| V1003-CW | 400    | Invalid signature                         |
| V1004-CW | 401    | Signature has expired                     |
| V1005-CW | 404    | Transaction not found                     |
| V1006-CW | 400    | Invalid parameter                         |
| V1007-CW | 404    | Symbol not found                          |
| V1008-CW | 400    | Address not yet generated for this symbol |
| V1009-CW | 404    | Memo not found for this address           |
| V1010-CW | 404    | Address not found                         |
| V1011-CW | 400    | Address already exists                    |
| V1012-CW | 400    | Destination address not active            |
| V1015-CW | 404    | Coin not found                            |

### Authentication Error

| Code     | Status | Message             |
| -------- | ------ | ------------------- |
| A1000-CW | 401    | Unauthorized Access |
| A1001-CW | 403    | Permission denied   |

# Rate limits

If the request rate exceeds the limit in any endpoints, the request will be blocked for 30 seconds. When blocked, HTTP response is 429 Too Many Requests. The limits apply to individual user accessing the API. **_The rate limit is applied to each endpoint regardless the API version._**

| Endpoint          | Rate Limit        |
| ----------------- | ----------------- |
| /api/v4/crypto/\* | 250 req / 10 secs |
# Websocket API for Bitkub (2023-04-19)

# Changelog
* 2023-04-19 Changed the webSocket
market.trade.symbol. Field ```bid, sid``` changed type from ```Integer to String```.
* 2023-01-16 Update `Live Order Book`, added a new event info.
* 2022-08-31 Deprecated the authentication to `Live Order Book` websocket.
# Table of contents
* [Websocket endpoint](#websocket-endpoint)
* [Stream name](#stream-name)
* [Symbols](#symbols)
* [Websocket API documentation](#web-socket-api-documentation)
* [Stream Demo](#stream-demo)
* [Live Order Book](#live-order-book)

# Websocket endpoint
* The websocket endpoint is: **wss://api.bitkub.com/websocket-api/[\<streamName\>](#stream-name)**

# Stream name
Stream name requires 3 parts: **service name**, **service type**, and **symbol**, delimited by **dot (.)**, and is **case-insensitive**.

#### Stream name format:
```javascript
<serviceName>.<serviceType>.<symbol>
```

#### Stream name example:
```javascript
market.trade.thb_btc
```
Above example stream name provides real-time data from the **market** service, type **trade**, of symbol **THB_BTC**.



### Multiple streams subscription:
You can combine multiple streams by using **comma (,)** as the delimeter.

#### Multiple stream names format:
```javascript
<streamName>,<streamName>,<streamName>
```

#### Multiple stream names example:
```javascript
market.trade.thb_btc,market.ticker.thb_btc,market.trade.thb_eth,market.ticker.thb_eth
```
Above subscription provides real-time data from trade and ticker streams of symbols THB_BTC and THB_ETH.



# Symbols
Refer to [RESTful API](https://github.com/bitkub/bitkub-official-api-docs/blob/master/restful-api.md#get-apimarketsymbols) for all available symbols and symbol ids).



# Websocket API documentation
Refer to the following for description of each stream

### Trade stream
<span style="color:white;background:red;"> ⚠️ After April 18th, 2023 at 18:00PM(GMT+7)</span>

* Response field ```bid, sid``` change type from ```Integer to String```.
* Ref: [Announcement](#announcement)

#### Name:
market.trade.\<symbol\>

#### Description:
The trade stream provides real-time data on matched orders. Each trade contains buy order id and sell order id. Order id is unique by the order side (buy/sell) and symbol.

#### Response:
```javascript
{
  "stream": "market.trade.thb_eth", // stream name
  "sym":"THB_ETH", // symbol
  "txn": "ETHSELL0000074282", // transaction id
  "rat": "5977.00", // rate matched
  "amt": 1.556539, // amount matched
  "bid": 2048451, // buy order id
  "sid": 2924729, // sell order id
  "ts": 1542268567 // trade timestamp
}
```

### Ticker stream
#### Name:
market.ticker.\<symbol\>

#### Description:
The ticker stream provides real-time data on ticker of the specified symbol. Ticker for each symbol is re-calculated on trade order creation, cancellation, and fulfillment.

#### Response:
```javascript
 {
    "stream": "market.ticker.thb_btc",
    "id": 1,
    "last": 2883194.85,
    "lowestAsk": 2883194.9,
    "lowestAskSize": 0.0070947,
    "highestBid": 2881000.31,
    "highestBidSize": 0.00470253,
    "change": 60622.33,
    "percentChange": 2.15,
    "baseVolume": 89.25334259,
    "quoteVolume": 256768588.16,
    "isFrozen": 0,
    "high24hr": 2916959.99,
    "low24hr": 2819009.05,
    "open": 2822572.52,
    "close": 2883194.85
}
```

# Stream Demo
The demo page is available [here](https://api.bitkub.com/websocket-api?streams=) for testing streams subscription.

# Live Order Book
#### Description:
Use symbol id (numeric id) to get real-time data of order book: **wss://api.bitkub.com/websocket-api/orderbook/[\<symbol-id\>](#symbols)**.

#### Message data:
```javascript
{
    "data": (data),
    "event": (event type)
}
```
There are 4 event types: **bidschanged**, **askschanged**, **tradeschanged**, and **global.ticker**
* **bidschanged** occurs when any buy order has changed on the selected symbol (opened/closed/cancelled). Data is array of buy orders after the change (max. 30 orders).
* **askschanged** occurs when any sell order has changed on the selected symbol (opened/closed/cancelled). Data is array of sell orders after the change (max. 30 orders).
* **tradeschanged** occurs when buy and sell orders have been matched on the selected symbol. Data is array containing 3 arrays: array of latest trades, array of buy orders, and array of sell orders (each max. 30 orders). You get this event as the initial data upon successful subscription.
* **ticker** occurs every time when either bidschanged, askschanged, or tradeschanged is fired on the selected symbol.
* **global.ticker** occurs every time when either bidschanged, askschanged, or tradeschanged is fired on any symbol in the exchange.

#### Example response (bidschanged or askschanged):
```javascript
{
   "data":[
      [
         121.82, // vol
         112510.1, // rate
         0.00108283, // amount
         0, // reserved, always 0
         false, // is new order
         false // user is owner (deprecated)
      ]
   ],
   "event":"bidschanged",
   "pairing_id":1
}
```

#### Example response (tradeschanged):
```javascript
{
   "data":[
      [
         [
            1550320593, // timestamp
            113587, // rate
            0.12817027, // amount
            "BUY", // side
            0, // reserved, always 0
            0, // reserved, always 0
            true, // is new order
            false, // user is buyer (available when authenticated)
            false // user is seller (available when authenticated)
         ]
      ],
      [
         [
            121.82, // vol
            112510.1, // bid rate
            0.00108283, // bid amount
            0, // reserved, always 0
            false, // is new order
            false // user is owner (available when authenticated)
         ]
      ],
      [
         [
            51247.13, // vol
            113699, // ask rate
            0.45072632, // ask amount
            0, // reserved, always 0
            false, // is new order
            false // user is owner (available when authenticated)
         ]
      ]
   ],
   "event":"tradeschanged",
   "pairing_id":1
}
```

#### Example response (ticker):
```javascript
{
   "data":{
      "baseVolume":106302.39237032, // amount of crypto
      "change":0.16, // difference of price compare to the latest
      "close":15.9, // close price
      "high24hr":16.72, // the highest bidding price taken in the last 24 hours
      "highestBid":15.81, // the highest bidding price
      "highestBidSize":5640.39911448, // the amount of the highest bidding order
      "id":139, // symbol id
      "isFrozen":0, // symbol trade status
      "last":15.9, // the latest price
      "low24hr":15.7, // the lowest price taken in the last 24 hours
      "lowestAsk":16.22, // the lowest asking price
      "lowestAskSize":1582, // the amount of the lowest asking order
      "open":15.74, // open price
      "percentChange":1.02, // difference of price compare to the latest in percent
      "quoteVolume":1715566.77, //  amount of fiat
      "stream":"market.ticker.thb_1inch" // stream name
   },
   "event":"global.ticker", // event name
   "pairing_id":1
}
```

#### Example response (global.ticker):
```javascript
{
   "data":{
      "baseVolume":106302.39237032, // amount of crypto
      "change":0.16, // difference of price compare to the latest
      "close":15.9, // close price
      "high24hr":16.72, // the highest bidding price taken in the last 24 hours
      "highestBid":15.81, // the highest bidding price
      "highestBidSize":5640.39911448, // the amount of the highest bidding order
      "id":139, // symbol id
      "isFrozen":0, // symbol trade status
      "last":15.9, // the latest price
      "low24hr":15.7, // the lowest price taken in the last 24 hours
      "lowestAsk":16.22, // the lowest asking price
      "lowestAskSize":1582, // the amount of the lowest asking order
      "open":15.74, // open price
      "percentChange":1.02, // difference of price compare to the latest in percent
      "quoteVolume":1715566.77, //  amount of fiat
      "stream":"market.ticker.thb_1inch" // stream name
   },
   "event":"global.ticker" // event name
}
```
