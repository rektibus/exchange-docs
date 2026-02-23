import { ApiEndpoint } from "@/components/api-endpoint";
import { RegionalBaseUrl } from "@/components/regional-base-url";
import { InlineRegionSelector } from "@/components/inline-region-selector";
import { RegionalUrl } from "@/components/regional-url";
import { RegionalBaseUrlText } from "@/components/regional-base-url-text";
import { Code } from "nextra/components";

# Public HTTP API V4

- [Error messages V4 format](#error-messages-v4-format)
  - [Maintenance status](#maintenance-status)
  - [Market Info](#market-info)
  - [Market activity](#market-activity)
  - [Asset status list](#asset-status-list)
  - [Orderbook](#orderbook)
  - [Depth](#depth)
  - [Recent Trades](#recent-trades)
  - [Fee](#fee)
  - [Server Time](#server-time)
  - [Server Status](#server-status)
  - [Collateral Markets List](#collateral-markets-list)
  - [Available Futures Markets List](#available-futures-markets-list)
  - [Funding History](#funding-history)

<InlineRegionSelector className="my-4" />

Endpoint example: <Code><RegionalBaseUrlText />/api/v4/public/{"{endpoint}"}</Code>

All endpoints return time in Unix-time format.

All endpoints return either a **JSON** object or array.

For receiving responses from API calls please use http method **GET**

If an endpoint requires parameters you should send them as `query string`

---

### Error messages V4 format

```json
{
  "success": false,
  "message": "ERROR MESSAGE",
  "params": []
}
```

---

### Maintenance status

<ApiEndpoint method="GET" path="/api/v4/public/platform/status" />

This endpoint retrieves maintenance status

**Response:**

```json
{
  "status": "1"  // 1 - system operational, 0 - system maintenance
}
```

---

### Market Info

<ApiEndpoint method="GET" path="/api/v4/public/markets" />

This endpoint retrieves all information about available spot and futures markets.

**Response is cached for:**
_1 second_

**Parameters:**
NONE

❗ Rate limit 2000 requests/10 sec.

**Response:**

```json
[
    {
      "name": "SON_USD",         // Market pair name
      "stock": "SON",            // Ticker of stock currency
      "money": "USD",            // Ticker of money currency
      "stockPrec": "3",          // Stock currency precision
      "moneyPrec": "2",          // Precision of money currency
      "feePrec": "4",            // Fee precision
      "makerFee": "0.001",       // Default maker fee ratio
      "takerFee": "0.001",       // Default taker fee ratio
      "minAmount": "0.001",      // Minimal amount of stock to trade
      "minTotal": "0.001",       // Minimal amount of money to trade
      "maxTotal": "10000000000", // Maximum total(amount * price) of money to trade
      "tradesEnabled": true,     // Is trading enabled
      "isCollateral": true,      // Is margin trading enabled
      "type": "spot"             // Market type. Possible values: "spot", "futures"
    },
]
```

---

### Market activity

<ApiEndpoint method="GET" path="/api/v4/public/ticker" />

This endpoint retrieves a 24-hour pricing and volume summary for each market pair available on the exchange.

**Response is cached for:**
_1 second_

**Parameters:**
NONE

❗ Rate limit 2000 requests/10 sec.

**Response:**

```json
{
  "BTC_USDT": {
    "base_id": 1,                        // CoinmarketCap Id of base currency; 0 - if unknown
    "quote_id": 825,                     // CoinmarketCap Id of quote currency; 0 - if unknown
    "last_price": "9164.09",             // Last price
    "quote_volume": "43341942.90416876", // Volume in quote currency
    "base_volume": "4723.286463",        // Volume in base currency
    "isFrozen": false,                   // Identifies if trades are closed
    "change": "0.57"                     // Change in percent between open and last prices
  },
}
```

---

### Asset status list

<ApiEndpoint method="GET" path="/api/v4/public/assets" />

This endpoint retrieves the assets status.

**Response is cached for:**
_1 second_

**Parameters:**
NONE

❗ Rate limit 2000 requests/10 sec.

**Response:**

```json
{
  "BTC": {
    "name": "Bitcoin",           // Full name of cryptocurrency.
    "unified_cryptoasset_id": 1, // Unique ID of cryptocurrency assigned by Unified Cryptoasset ID, 0 if unknown
    "can_withdraw": true,        // Identifies whether withdrawals are enabled or disabled.
    "can_deposit": true,         // Identifies whether deposits are enabled or disabled.
    "min_withdraw": "0.001",     // Identifies the single minimum withdrawal amount of a cryptocurrency.
    "max_withdraw": "2",         // Identifies the single maximum withdrawal amount of a cryptocurrency.
    "maker_fee": "0.1",          // Maker fee in percentage
    "taker_fee": "0.1",          // Taker fee in percentage
    "min_deposit": "0.0001",     // Min deposit amount
    "max_deposit": "0",          // Max deposit amount, will not be returned if there is no limit, 0 if unlimited
    "currency_precision": 18,    // Max number of digits to the right of the decimal point
    "is_memo": false,            // Identifies if currency has memo address
    "memo": {                    // Identifies if currency requires memo for deposits/withdraws
      "deposit": false,
      "withdraw": false
    },
    "networks": {                // Currency networks. It might be a list of networks for cryptocurrency networks or just a single item list for simple cryptocurrencies or tokens
      "deposits": [              // Networks available for depositing
        "BTC"
      ],
      "withdraws": [             // Networks available for withdrawing
        "BTC"
      ],
      "default": "BTC"           // Default network for depositing / withdrawing if available
    },
    "limits": {                  // Currency limits by each network
      "deposit": {               // Deposits limits
        "BTC": {                 // Network
          "min": "0.001"         // Min deposit amount
        },
      },
      "withdraw": {              // Withdraws limits
        "BTC": {                 // Network
          "min": "0.002",        // Min withdraw amount
        },
      }
    },
    "confirmations": {           // Deposit confirmations count mapped by network
      "BTC": 2
    }
  },
  "ETH": {
    "name": "Ethereum",
    "unified_cryptoasset_id": 1027,
    "can_withdraw": true,
    "can_deposit": true,
    "min_withdraw": "0.02",
    "max_withdraw": "0",
    "maker_fee": "0.1",
    "taker_fee": "0.1",
    "min_deposit": "0.1",
    "max_deposit": "0",
    "currency_precision": 18,
    "is_memo": false,
    "memo": {            // Identifies if currency requires memo for deposits/withdraws
      "deposit": false,
      "withdraw": false
    },
    "networks": {        // Currency networks. It might be a list of networks for cryptocurrency networks or just a single item list for simple cryptocurrencies or tokens
      "deposits": [      // Networks available for depositing
        "ETH"
      ],
      "withdraws": [     // Networks available for withdrawing
        "ETH"
      ],
      "default": "ETH"   // Default network for depositing / withdrawing if available
    },
    "limits": {          // Currency limits by each network
      "deposit": {       // Deposits limits
        "ETH": {         // Network
          "min": "0.001" // Max deposit amount
        }
      },
      "withdraw": {      // Withdraws limits
        "ETH": {         // Network
          "min": "0.002" // Min withdraw amount
        }
      }
    },
    "confirmations": {
      "ETH": 20
    }
  },
  "USDT": {
    "name": "Tether US",
    "unified_cryptoasset_id": 825,
    "can_withdraw": true,
    "can_deposit": true,
    "min_withdraw": "5",
    "max_withdraw": "0",
    "maker_fee": "0.1",
    "taker_fee": "0.1",
    "min_deposit": "0",
    "max_deposit": "0",
    "currency_precision": 6,
    "is_memo": false,
    "memo": {            // Identifies if currency requires memo for deposits/withdraws
      "deposit": false,
      "withdraw": false
    },
    "networks": {        // Currency networks. It might be a list of networks for cryptocurrency networks or just a single item list for simple cryptocurrencies or tokens
      "deposits": [      // Networks available for depositing
        "ERC20",
        "TRC20",
        "OMNI",
        "BEP20"
      ],
      "withdraws": [     // Networks available for withdrawing
        "ERC20",
        "TRC20",
        "OMNI",
        "BEP20"
      ],
      "default": "ERC20" // Default network for depositing / withdrawing
    },
    "limits": {          // This object will be returned when currency has several networks/providers
      "deposit": {       // Deposits limits
        "ERC20": {       // Network
          "min": "5",    // Min deposit amount
          "max": "1000"  // Max deposit amount
        },
        "TRC20": {
          "min": "5"     // If there is no max limit, it is not returned
        },
      },
      "withdraw": {      // Withdraws limits
        "ERC20": {       // Network
          "min": "10",   // Min withdraw amount
          "max": "1000"  // Max withdraw amount
        },
        "TRC20": {
          "min": "10"    // If there is no max limit, it is not returned
        },
      }
    },
    "confirmations": {
      "ERC20": 20,
      "TRC20": 20
    }
  },
  "UAH": {
    "name": "Hryvnia",
    "unified_cryptoasset_id": 0,
    "can_withdraw": true,
    "can_deposit": true,
    "min_withdraw": "50",
    "max_withdraw": "100000",
    "maker_fee": "0.1",
    "taker_fee": "0.1",
    "min_deposit": "50",
    "max_deposit": "100000",
    "is_memo": false,
    "memo": {             // Identifies if currency requires memo for deposits/withdraws
      "deposit": false,
      "withdraw": false
    },
    "providers": {        // Fiat currency providers
      "deposits": [       // Providers available for depositing
        "VISAMASTER",
        "ADVCASH",
        "GEOPAY"
      ],
      "withdraws": [      // Providers available for withdrawing
        "VISAMASTER",
        "GEOPAY"
      ],
    },
    "limits": {           // This object will be returned when currency has several networks/providers
      "deposit": {        // Deposits limits
        "VISAMASTER": {   // Provider
          "min": "50",    // Min deposit amount
          "max": "50000"  // Max deposit amount
        },
      },
      "withdraw": {      // Withdraws limits
        "VISAMASTER": {  // Provider
          "min": "50",   // Min withdraw amount
          "max": "50000" // Max withdraw amount
        },
      }
    }
  },
}
```

---

### Orderbook

<ApiEndpoint method="GET" path="/api/v4/public/orderbook/{market}?limit=100&level=2" />

This endpoint retrieves the current [order book](./../glossary.md#order-book) as two arrays ([bids](./../glossary.md#bid) / [asks](./../glossary.md#ask)) with additional parameters.

**Response is cached for:**
_100 ms_

❗ Rate limit 600 requests/10 sec.

**Parameters:**

| Name  | Type | Mandatory | Description                                                                                                                                                                                                                                                              |
| ----- | ---- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| limit | int  | **No**    | Orders depth quantity: 0 - 100. Not defined or 0 will return 100 entries.                                                                                                                                                                                                |
| level | int  | **No**    | Optional parameter that allows API user to see different level of aggregation. Level 0 – default level, no aggregation. Starting from level 1 (lowest possible aggregation) and up to level 5 - different levels of aggregated [orderbook](./../glossary.md#order-book). |

**Response:**

```json
{
  "ticker_id": "BTC_PERP", // Market Name
  "timestamp": 1594391413, // Current timestamp
  "asks": [                // Array of ask orders
    [
      "9184.41",           // Price of lowest ask
      "0.773162"           // Amount of lowest ask
    ],
  ],
  "bids": [                // Array of bid orders
    [
      "9181.19",           // Price of highest bid
      "0.010873"           // Amount of highest bid
    ],
  ]
}
```

### Depth

<ApiEndpoint method="GET" path="/api/v4/public/orderbook/depth/{market}" />

This endpoint retrieves depth price levels within ±2% of the market last price.

**Response is cached for:**
_1 sec_

❗ Rate limit 2000 requests/10 sec.

**Parameters:**
NONE

**Response:**

```json
{
  "ticker_id": "BTC_PERP", // Market Name
  "timestamp": 1594391413, // Current timestamp
  "asks": [                // Array of ask orders
    [
      "9184.41",           // Price of lowest ask
      "0.773162"           // Amount of lowest ask
    ],
  ],
  "bids": [                // Array of bid orders
    [
      "9181.19",           // Price of highest bid
      "0.010873"           // Amount of highest bid
    ],
  ]
}
```
---

### Recent Trades

<ApiEndpoint method="GET" path="/api/v4/public/trades/{market}?type=sell" />

This endpoint retrieves the [trades](./../glossary.md#deal-trade) that have been executed recently on the requested [market](./../glossary.md#market).

**Response is cached for:**
_1 second_

❗ Rate limit 2000 requests/10 sec.

**Parameters:**

| Name | Type   | Mandatory | Description        |
| ---- | ------ | --------- | ------------------ |
| type | String | **No**    | Can be buy or sell |

**Response:**

```json
[
  {
    "tradeID": 158056419,          // A unique ID associated with the trade for the currency pair transaction Note: Unix timestamp does not qualify as trade_id.
    "price": "9186.13",            // Transaction price in quote pair volume.
    "quote_volume": "0.0021",      // Transaction amount in quote pair volume.
    "base_volume": "9186.13",      // Transaction amount in base pair volume.
    "trade_timestamp": 1594391747, // Unix timestamp in milliseconds, identifies when the transaction occurred.
    "type": "sell",                // Used to determine whether or not the transaction originated as a buy or sell. Buy – Identifies an ask that was removed from the order book. Sell – Identifies a bid that was removed from the order book.
    "rpi": true                    // Indicates whether the trade involved a Retail Price Improvement (RPI) order
  },
  {
    "tradeID": 158056416,
    "price": "9186.13",
    "base_volume": "9186.13",
    "quote_volume": "0.002751",
    "trade_timestamp": 1594391746,
    "type": "sell",
    "rpi": false
  }
]
```

---

### Fee

<ApiEndpoint method="GET" path="/api/v4/public/fee" />

This endpoint retrieves the list of [fees](./../glossary.md#fee) and min/max amount for deposits and withdraws

**Response is cached for:**
_1 second_

❗ Rate limit 2000 requests/10 sec.

---

**Response:**

```json
{
  "USDT (ERC20)": {
    "ticker": "USDT",                             // currency ticker
    "name": "Tether US",                          // currency ticker
    "providers": [],
    "deposit": {                                  // deposit fees
      "min_amount": "0.0005",                     // min deposit amount. 0 if there is no limitation
      "max_amount": "0.1",                        // max deposit amount. 0 if there is no limitation
      "fixed": "0.0005",                          // fixed fee amount which applies for all transaction
      "flex": {                                   // flex fee only applies for all transactions but according to min/max fee. Nullable if there is no flex fee
        "min_fee": "100",                         // min fee amount
        "max_fee": "1000",                        // max fee amount
        "percent": "10"
      }
    },
    "withdraw": {
      "min_amount": "0.001",
      "max_amount": "0",
      "fixed": null,
      "flex": null
    },
    "is_depositable": true,                       // true if currency can be depositable
    "is_withdrawal": true,                        // true if currency can be withdrawable
    "is_api_withdrawal": true,                    // true if currency can be withdrawable by api
    "is_api_depositable": true                    // true if currency can be depositable by api
  },
  "USD": {
    "ticker": "USD",                              // currency ticker
    "name": "United States Dollar",               // currency ticker
    "providers": [                                // the list of providers. It is uses for fiat currencies. Provider is a payment system with own fees, which process payment operation
      "USD_ADVCASH",
      "USD_CAPITALIST",
      "USD_EPAY_COM",
      "USD_PERFECT_MONEY",
      "USD_VISAMASTER_INTERKASSA"
    ],
    "deposit": {                                  // for currencies with payment providers fee and amounts shows for each provider directly
      "USD_VISAMASTER_INTERKASSA": {
        "min_amount": "10",
        "max_amount": "1500",
        "fixed": null,
        "flex": null,
        "is_depositable": false,
        "is_api_depositable": true,
        "name": "USD Visa/MasterCard Interkassa", // provider name
        "ticker": "USD_VISAMASTER_INTERKASSA"     // provider ticker
      }
    },
    "withdraw": {
      "USD_VISAMASTER_INTERKASSA": {
        "min_amount": "20",
        "max_amount": "1500",
        "fixed": null,
        "flex": null,
        "is_withdrawal": false,
        "is_api_withdrawal": true,
        "name": "USD Visa/MasterCard Interkassa",
        "ticker": "USD_VISAMASTER_INTERKASSA"
      }
    }
  }
}
```

### Server Time

<ApiEndpoint method="GET" path="/api/v4/public/time" />

This endpoint retrieves the current server time.

**Response is cached for:**
_1 second_

❗ Rate limit 2000 requests/10 sec.

**Response:**

```json
{
  "time": 1631451591
}
```

### Server Status

<ApiEndpoint method="GET" path="/api/v4/public/ping" />

This endpoint retrieves the current API life-state.

❗ Rate limit 2000 requests/10 sec.

**Response is cached for:**
_1 second_

**Response:**

```json
["pong"]
```

### Collateral Markets List

<ApiEndpoint method="GET" path="/api/v4/public/collateral/markets" />

This endpoint returns the list of [markets](./../glossary.md#market) that available for [collateral](./../glossary.md#collateral) trading

❗ Rate limit 2000 requests/10 sec.

**Response is cached for:**
_1 second_

**Response:**

```json
[
  "ADA_USDT",
  "BCH_USDT",
  "BTC_USDT",
  "DOGE_USDT",
  "EOS_USDT",
  "ETH_BTC",
  "ETH_USDT",
  "LINK_USDT",
  "LTC_USDT",
  "SHIB_USDT",
  "SOL_USDT",
  "TRX_USDT",
  "USDC_USDT",
  "XLM_USDT",
  "XRP_USDT"
]
```

### Available Futures Markets List

<ApiEndpoint method="GET" path="/api/v4/public/futures" />

This endpoint returns the list of available futures markets.

❗ Rate limit 2000 requests/10 sec.

**Response is cached for:**
_1 second_

**Response:**

```json
{
  "success": true,
  "message": null,
  "result": [
    {
      "ticker_id": "BTC_PERP",                        // Identifier of a ticker with delimiter to separate base/target
      "stock_currency": "BTC",                        // Symbol/currency code of base pair
      "money_currency": "USDT",                       // Symbol/currency code of target pair
      "last_price": "24005.5",                        // Last transacted price of base currency based on given target currency
      "stock_volume": "196965.591",                   // 24 hour trading volume in base pair volume
      "money_volume": "4737879075.7817",              // 24 hour trading volume in target pair volume
      "bid": "24005.4",                               // Current highest bid price
      "ask": "24005.6",                               // Current lowest ask price
      "high": "24295.1",                              // Rolling 24-hours highest transaction price
      "low": "23765.3",                               // Rolling 24-hours lowest transaction price
      "product_type": "Perpetual",                    // What product is this? Futures, Perpetual, Options?
      "open_interest": "6000",                        // The open interest in the last 24 hours in contracts.
      "index_price": "24019.25",                      // Underlying index price
      "index_name": "Bitcoin",                        // Name of the underlying index if any
      "index_currency": "BTC",                        // Underlying currency for index
      "funding_rate": "0.000044889033693137",         // The current funding rate, which may fluctuate due to market conditions.
      "next_funding_rate_timestamp": "1660665600000", // Timestamp of the next funding rate change
      "brackets": {                                   // Brackets
        "1": 0,
        "2": 0,
        "3": 0,
        "5": 0,
        "10": 0,
        "20": 0,
        "50": 20,
        "100": 50
      },
      "max_leverage": 100,                             // Max Leverage
      "funding_interval_minutes": 300                 // Funding interval in minutes
    }
  ]
}
```

### Funding History

<ApiEndpoint method="GET" path="/api/v4/public/funding-history/{market}" />

This endpoint returns the funding rate history for a specified futures market.

❗ Rate limit 2000 requests/10 sec.

**Parameters:**

| Name      | Type   | Mandatory | Description                                                   |
| --------- | ------ | --------- | ------------------------------------------------------------- |
| market    | String | **Yes**   | Market name (e.g., BTC_PERP)                                 |
| startDate | Int    | **No**    | Start timestamp in seconds                                    |
| endDate   | Int    | **No**    | End timestamp in seconds                                     |
| limit     | Int    | **No**    | Number of records to return. Default: 100, Maximum: 1000     |
| offset    | Int    | **No**    | Number of records to skip                                    |

**Response:**

```json
[
  {
    "fundingTime": "1752537600",        // Timestamp when funding was executed
    "fundingRate": "-0.0001229",        // Funding rate value
    "market": "BTC_PERP",               // Market name
    "settlementPrice": "119816.5",      // Price at which funding was settled
    "rateCalculatedTime": "1752508800"  // Timestamp when the funding rate was calculated
  },
  {
    "fundingTime": "1752508800",
    "fundingRate": "-0.0001306",
    "market": "BTC_PERP",
    "settlementPrice": "119873.1",
    "rateCalculatedTime": "1752480000"
  }
]
```

### Mining Pool Overview

<ApiEndpoint method="GET" path="/api/v4/public/mining-pool" />

This endpoint returns an overall information about the current mining pool state.

HashRate info represents in the H units.

❗ Rate limit 1000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**
NONE

**Request BODY raw:**
NONE

**Response:**

Available statuses:

- `Status 200`

```json
{
  "data": [
    {
      "connectionLinks": ["stratum+tcp://1.1.1.1:80", "stratum+tcp://1.1.1.2:80"],
      "location": "global",
      "assets": ["BTC"],
      "rewardSchemes": ["FPPS"],
      "workers": 1846,
      "currentHashRate": "39353570.8006319183174839",
      "last7daysHashRate": [
        {
          "timestamp": 1732579200,
          "hashrate": "184425100325925.9259259259259259",
        }
      ],
      "blocks": [
        {
          "blockFoundAt": 1715339355,
          "blockHeight": 18329
        },
        {
          "blockFoundAt": 1715329275,
          "blockHeight": 18325
        }
      ]
    }
  ]
}
```
import { Tabs } from 'nextra/components'

# Public WebSocket API

- [Service](#service)
- [Ping](#ping)
- [Time](#time)
- [Kline](#kline)
- [Last price](#last-price)
- [Market statistics](#market-statistics)
- [Market statistics for current day UTC](#market-statistics-for-current-day-utc)
- [Market trades](#market-trades)
- [Market depth](#market-depth)
- [Book Ticker](#book-ticker)

- [Playground](#playground)

## WebSocket Connection Management

WebSocket endpoint is **```wss://api.whitebit.com/ws```**

The API is based on [JSON RPC](https://www.jsonrpc.org/specification) of WebSocket protocol.

⚠️️ **Connection Timeout** ⚠️️
- Server closes websocket connection after **60 seconds of inactivity**
- Inactivity is defined as no messages sent by the client

### Maintaining Connection
To keep the websocket connection active:
- Send periodic ping messages every **50 seconds**
- Handle potential connection closures gracefully in your application logic

### Example Implementation

```javascript
// Establish websocket connection
const socket = new WebSocket("wss://api.whitebit.com/ws");

// Set up periodic ping
setInterval(() => {
  if (socket.readyState === WebSocket.OPEN) {
    socket.send(JSON.stringify({
            id: 0,
            method: "ping",
            params: [],
        }));
  }
}, 50000); // Every 50 seconds
```

**❗ Rate limit 1000 ws connections per minute and 200 requests per minute in one connection.❗**

**All endpoints return time in Unix-time format.**

## ⤴️ Request message

JSON Structure of request message:

- `id` - **Integer**. Should be unique to handle response for your request.
- `method` - **String**. Name of request.
- `params` - **Array**. Here you pass params for method.

🚫 WebSocket connection will be closed if invalid JSON was sent.

### Types of request messages

- Query (`ping`, `candles_request`, etc)
- Subscription (`candles_subscribe`, `lastprice_subscribe`, etc). Repeated subscription will be cancelled for the same data type.

## ⤵️ Response message

JSON Structure of response message:

- `id` - **Integer**. Id of request.
- `result` - **Null** for failure, for success - look for responses below
- `error` - **Null** for success, **JSON Object** for failure:
  - `message` - Detailed text
  - `code` - Error code

| Code  | Message             |
| ----- | ------------------- |
| **1** | invalid argument    |
| **2** | internal error      |
| **3** | service unavailable |
| **4** | method not found    |
| **5** | service timeout     |

## Types of response messages

- Query result
- Subscription status (success/failed)
- Update events

---

## Examples

**Example** messages for request with response:

#### ⤴️ Request

```json
{
  "id": 0,
  "method": "ping",
  "params": []
}
```

#### ⤵️ Response

```json
{
  "id": 0,
  "result": "pong",
  "error": null
}
```

**Example** subscription:

#### ⤴️ Request

```json
{
  "id": 0,
  "method": "candles_subscribe",
  "params": []
}
```

#### ⤵️ Response

```json
{
  "id": 0,
  "result": {
    "status": "success"
  },
  "error": null
}
```

#### 🔄 Update events

```json
{
  "id": null,
  "method": "candles_update",
  "params": [] // look below for params
}
```

---

## API

### Service

#### Ping

##### ⤴️ Request

```json
{
  "id": 0,
  "method": "ping",
  "params": []
}
```

##### ⤵️ Response

```json
{
  "id": 0,
  "result": "pong",
  "error": null
}
```

#### Time

##### ⤴️ Request

```json
{
  "id": 1,
  "method": "time",
  "params": []
}
```

##### ⤵️ Response

```json
{
  "id": 1,
  "result": 1493285895,
  "error": null
}
```

---

### Kline

#### Query

The requested interval must meet the following conditions:

- If the number is less than 60, then 60 must be divisible by the requested number without a remainder;
- Less than 3600 (1 hour) - the number must be divisible by 60 without a remainder, and 3600 must be divisible by the requested number without a remainder;
- Less than 86400 (day) - the number must be whitened by 3600 without a remainder, and 86400 must be divisible by the number without a remainder;
- Less than 86400 \* 7 (week) - the number must be divisible by 86400 without a remainder;
- Equal to 86400 \* 7;
- Equal to 86400 \* 30.

##### ⤴️ Request

```json
{
  "id": 2,
  "method": "candles_request",
  "params": [
    "ETH_BTC", // market
    1659569940, // start time
    1660894800, // end time
    3600 // interval in seconds
  ]
}
```

##### ⤵️ Response

```json
{
    "id": 2,
    "result": [
        [
            1580860800,       // time
            "0.020543",       // open
            "0.020553",       // close
            "0.020614",       // highest
            "0.02054",        // lowest
            "7342.597",       // volume in stock
            "151.095481849",  // volume in deal
            "ETH_BTC"         // market
        ],
    ],
    "error": null
}
```

#### Subscribe

Update interval: 0.5 sec

##### ⤴️ Request

```json
{
  "id": 3,
  "method": "candles_subscribe",
  "params": [
    "BTC_USD", // market
    900 // interval in seconds
  ]
}
```

##### ⤵️ Response

```json
{
  "id": 3,
  "result": {
    "status": "success"
  },
  "error": null
}
```

##### 🔄 Update events

```json
{
  "id": null,
  "method": "candles_update",
  "params": [
    [
      1580895000, // time
      "0.020683", // open
      "0.020683", // close
      "0.020683", // high
      "0.020666", // low
      "504.701", // volume in stock
      "10.433600491", // volume in money (deal)
      "ETH_BTC" // market
    ]
  ]
}
```

#### Unsubscribe

##### ⤴️ Request

```json
{
  "id": 4,
  "method": "candles_unsubscribe",
  "params": []
}
```

##### ⤵️ Response

```json
{
  "id": 4,
  "result": {
    "status": "success"
  },
  "error": null
}
```

---

### Last price

#### Query

##### ⤴️ Request

```json
{
  "id": 5,
  "method": "lastprice_request",
  "params": [
    "ETH_BTC" // market
  ]
}
```

##### ⤵️ Response

```json
{
  "id": 5,
  "result": "0.020553",
  "error": null
}
```

#### Subscribe

Update interval: 1 sec

##### ⤴️ Request

```json
{
    "id": 6,
    "method": "lastprice_subscribe",
    "params": [
        "ETH_BTC", // markets
        "BTC_USDT",
    ]
}
```

##### ⤵️ Response

```json
{
  "id": 6,
  "result": {
    "status": "success"
  },
  "error": null
}
```

##### 🔄 Update events

```json
{
  "id": null,
  "method": "lastprice_update",
  "params": [
    "ETH_BTC", // market
    "0.020683" // price
  ]
}
```

#### Unsubscribe

##### ⤴️ Request

```json
{
  "id": 7,
  "method": "lastprice_unsubscribe",
  "params": []
}
```

##### ⤵️ Response

```json
{
  "id": 7,
  "result": {
    "status": "success"
  },
  "error": null
}
```

---

### Market statistics

#### Query

##### ⤴️ Request

```json
{
  "id": 5,
  "method": "market_request",
  "params": [
    "ETH_BTC", // market
    86400 // period in seconds
  ]
}
```

##### ⤵️ Response

```json
{
  "id": 5,
  "result": {
    "period": 86400, // period in seconds
    "last": "0.020981", // last price
    "open": "0.02035", // open price that was at 'now - period' time
    "close": "0.020981", // price that closes this period
    "high": "0.020988", // highest price
    "low": "0.020281", // lowest price
    "volume": "135220.218", // volume in stock
    "deal": "2776.587022649" // volume in money
  },
  "error": null
}
```

#### Subscribe

You can subscribe only for 86400s (24h from now).

Update interval: 1 sec

##### ⤴️ Request

```json
{
    "id": 6,
    "method": "market_subscribe",
    "params": [
        "ETH_BTC", // markets
        "BTC_USDT",
    ]
}
```

##### ⤵️ Response

```json
{
  "id": 6,
  "result": {
    "status": "success"
  },
  "error": null
}
```

##### 🔄 Update events

```json
{
  "id": null,
  "method": "market_update",
  "params": [
    "ETH_BTC", // market
    {
      // response same as 'market_request'
      "period": 86400, // period in seconds
      "last": "0.020964", // last price
      "open": "0.020349", // open price that was at 'now - period' time
      "close": "0.020964", // price that closes this period
      "high": "0.020997", // highest price
      "low": "0.020281", // lowest price
      "volume": "135574.476", // volume in stock
      "deal": "2784.413999488" // volume in money
    }
  ]
}
```

#### Unsubscribe

##### ⤴️ Request

```json
{
  "id": 7,
  "method": "market_unsubscribe",
  "params": []
}
```

##### ⤵️ Response

```json
{
  "id": 7,
  "result": {
    "status": "success"
  },
  "error": null
}
```

---

### Market statistics for current day UTC

#### Query

##### ⤴️ Request

```json
{
  "id": 14,
  "method": "marketToday_query",
  "params": [
    "ETH_BTC" // only one market per request
  ]
}
```

##### ⤵️ Response

```json
{
  "id": 14,
  "result": {
    "last": "0.020981", // last price
    "open": "0.02035", // open price that was at 'now - period' time
    "high": "0.020988", // highest price
    "low": "0.020281", // lowest price
    "volume": "135220.218", // volume in stock
    "deal": "2776.587022649" // volume in money
  },
  "error": null
}
```

#### Subscribe

Update interval: 1 sec

##### ⤴️ Request

```json
{
    "id": 15,
    "method": "marketToday_subscribe",
    "params": [
        "ETH_BTC", // markets
        "BTC_USDT",
    ]
}
```

##### ⤵️ Response

```json
{
  "id": 15,
  "result": {
    "status": "success"
  },
  "error": null
}
```

##### 🔄 Update events

```json
{
  "id": null,
  "method": "marketToday_update",
  "params": [
    "ETH_BTC", // market
    {
      // response same as 'market_request'
      "last": "0.020964", // last price
      "open": "0.020349", // open price that was at 'now - period' time
      "high": "0.020997", // highest price
      "low": "0.020281", // lowest price
      "volume": "135574.476", // volume in stock
      "deal": "2784.413999488" // volume in money
    }
  ]
}
```

#### Unsubscribe

##### ⤴️ Request

```json
{
  "id": 16,
  "method": "marketToday_unsubscribe",
  "params": []
}
```

##### ⤵️ Response

```json
{
  "id": 16,
  "result": {
    "status": "success"
  },
  "error": null
}
```

---

### Market trades

#### Query

##### ⤴️ Request

```json
{
  "id": 8,
  "method": "trades_request",
  "params": [
    "ETH_BTC", // market
    100, // limit
    41358445 // largest id from which you want to request trades
  ]
}
```

##### ⤵️ Response

```json
{
    "id": 8,
    "result": [
        {
            "id": 41358530,           // trade id
            "time": 1580905394.70332, // time in milliseconds
            "price": "0.020857",      // trade price
            "amount": "5.511",        // trade amount
            "type": "sell"            // type of trade (buy/sell)
        },
    ],
    "error": null
}

```

#### Subscribe

Update interval: real-time

❗ For each websocket connection, you can subscribe to either one or several specific markets, or all markets. Every following subscription will replace the existing one.

**Note:** To subscribe to all markets, send the request with an empty `params` array.

##### ⤴️ Request

**Subscribe to specific markets:**

```json
{
    "id": 9,
    "method": "trades_subscribe",
    "params": [
        "ETH_BTC", // markets
        "BTC_USDT",
    ]
}
```

**Subscribe to all markets:**

```json
{
    "id": 9,
    "method": "trades_subscribe",
    "params": []
}
```

##### ⤵️ Response

```json
{
  "id": 9,
  "result": {
    "status": "success"
  },
  "error": null
}
```

##### 🔄 Update events

```json
{
    "id": null,
    "method": "trades_update",
    "params": [
        "ETH_BTC",                         // market
         [                                 // response same as 'market_request'
             {
                 "id": 41358530,           // trade id
                 "time": 1580905394.70332, // time in milliseconds
                 "price": "0.020857",      // trade price
                 "amount": "5.511",        // trade amount
                 "type": "sell",           // type of trade (buy/sell)
                 "rpi": true               // Indicates whether the trade involved a Retail Price Improvement (RPI) order
             }
         ]
    ]
}
```

#### Unsubscribe

##### ⤴️ Request

```json
{
  "id": 10,
  "method": "trades_unsubscribe",
  "params": []
}
```

##### ⤵️ Response

```json
{
  "id": 10,
  "result": {
    "status": "success"
  },
  "error": null
}
```

---

### Market depth

#### Query

This endpoint allows clients to request the current market depth for a specific cryptocurrency pair.

##### ⤴️ Request

```json
{
  "id": 11,
  "method": "depth_request",
  "params": [
    "ETH_BTC", // market
    100, // limit, max value is 100
    "0" // price interval units. "0" - no interval, available values - "0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01", "0.1"
  ]
}
```

##### ⤵️ Response

```json
{
    "id": 11,
    "result": {
        "timestamp": 1689600180.5164471, // timestamp of the update from matchengine
        "asks": [                   // sorted ascending
            ["0.020846", "29.369"], // [price, amount]
        ],
        "bids": [                   // sorted descending
            ["0.02083", "9.598"],   // [price, amount]
        ]
    },
    "error": null
}

```

#### Subscribe

This endpoint allows clients to subscribe to market depth data updates. After successful subscription, the server immediately sends a full snapshot of the current order book as the first `depth_update` message. Subsequent messages are incremental updates containing only changes. The server pushes updates every 100ms to subscribed clients when there are actual changes to the order book.

##### ⤴️ Request

```json
{
  "id": 12,
  "method": "depth_subscribe",
  "params": [
    "ETH_BTC",  // market
    100,        // limit. available values - 1, 5, 10, 20, 30, 50, 100
    "0",        // price interval units. "0" - no interval, available values - "0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01", "0.1"
    true        // multiple subscription flag. true - add, false - unsubscribe from all
  ]
}
```

The fourth parameter - Multiple subscription flag - allows you to subscribe to market depths as many markets as you want. The only restriction is one subscription with specific parameters per market.

INFO: If 10 seconds have elapsed without a change in the depth subscription, a snapshot message will be pushed again

##### ⤵️ Response

```json
{
  "id": 12,
  "result": {
    "status": "success"
  },
  "error": null
}
```

##### 🔄 Update events

Update events provide real-time updates to the subscribed market depth. The first message after subscription is a full snapshot of the order book, while subsequent messages are incremental updates.

**First message (full snapshot):**

```json
{
    "id": null,
    "method": "depth_update",
    "params": [
        true,
        {
            "timestamp": 1689600180.5164471, // timestamp of the update from matchengine
            "update_id": 214403,
            "asks": [                   // sorted ascending - full order book snapshot
                ["0.020846", "29.369"],
                ["0.020850", "15.123"],
                ["0.020855", "8.456"],
            ],
            "bids": [                   // sorted descending - full order book snapshot
                ["0.020844", "5.949"],
                ["0.020840", "12.345"],
                ["0.020835", "20.678"],
            ],
            "event_time": 1749026542.817343
        },
        "ETH_BTC"                       // market pair
    ]
}
```

**Subsequent messages (incremental updates):**

```json
{
    "id": null,
    "method": "depth_update",
    "params": [
        false,
        {
            "timestamp": 1689600180.5164471, // timestamp of the update from matchengine
            "update_id": 214404,
            "past_update_id": 214403, // present in incremental updates
            "asks": [
                ["0.020861", "0"],      // finished orders will be [price, "0"]
                ["0.020900", "2.5"],
            ],
            "bids": [
                ["0.020844", "5.949"],
                ["0.020800", "0"],
            ],
            "event_time": 1749026542.817343
        },
        "ETH_BTC"                       // market pair
    ]
}
```

##### 💻 Code examples

<Tabs items={['Typescript', 'Python', 'Java']}>
<Tabs.Tab>
```typescript showLineNumbers copy
type IDepth = [string, string];

interface OrderBook {
    asks: IDepth[];
    bids: IDepth[];
}

const ws = new WebSocket("wss://api.whitebit.com/ws");
const orderBook: OrderBook = { asks: [], bids: [] };
const LIMIT = 100;

ws.addEventListener("open", () => {
    ws.send(
        JSON.stringify({
            id: 1,
            method: "depth_subscribe",
            params: ["ETH_BTC", LIMIT, "0", true]
        }),
    );
});

ws.addEventListener("message", (event: MessageEvent) => {
    const message = JSON.parse(event.data.toString());

    if (message.method === "depth_update") {
        const updateData = message.params[0] as Partial<OrderBook & { past_update_id?: number }>;
        const isFirstMessage = !updateData.past_update_id;

        if (isFirstMessage) {
            // First message or keepalive snapshot is a full snapshot - replace order book
            orderBook.asks = updateData.asks ?? [];
            orderBook.bids = updateData.bids ?? [];
        } else {
            // Subsequent messages are incremental updates
            applyUpdates(orderBook.asks, updateData.asks, "ask");
            applyUpdates(orderBook.bids, updateData.bids, "bid");
            truncateOrderBook(orderBook.asks);
            truncateOrderBook(orderBook.bids);
        }
    }
});

function applyUpdates(orderBookSide: IDepth[], updates: IDepth[] | undefined, side: "ask" | "bid") {
    if (updates === undefined) return;
    for (const [price, amount] of updates) {
        // Find the index of an entry in orderBookSide that matches the given price.
        const priceIndex = orderBookSide.findIndex((level) => level[0] === price);

        // If the amount is '0', it means this price level should be removed from the orderBookSide.
        if (amount === "0") {
            if (priceIndex !== -1) {
                // Remove the existing price level since the amount is '0'.
                orderBookSide.splice(priceIndex, 1);
            }
        } else {
            // If the amount is not '0', either update the existing price level or add a new one.
            if (priceIndex === -1) {
                // Find the position where the new price level should be inserted.
               const insertIndex = orderBookSide.findIndex((level) =>
                    side === "ask" ? level[0] > price : level[0] < price
                );

                if (insertIndex === -1) {
                    // Add to the end if there's no higher price level.
                    orderBookSide.push([price, amount]);
                } else {
                    // Insert at the correct sorted position.
                    orderBookSide.splice(insertIndex, 0, [price, amount]);
                }
            } else {
                // Update the amount for the existing price level.
                orderBookSide[priceIndex][1] = amount;
            }
        }
    }
}

function truncateOrderBook(orderBookSide: IDepth[]) {
    if (orderBookSide.length > LIMIT) {
        // Only truncate if the length exceeds the LIMIT
        orderBookSide.splice(LIMIT);
    }
}
```
</Tabs.Tab>
<Tabs.Tab>
```python showLineNumbers copy
import asyncio
import json
import websockets

class OrderBook:
    def __init__(self):
        self.asks = []
        self.bids = []

LIMIT = 100

async def depth_subscribe():
    async with websockets.connect('wss://api.whitebit.com/ws') as ws:
        await ws.send(json.dumps({
            'id': 1,
            'method': 'depth_subscribe',
            'params': ['ETH_BTC', LIMIT, '0', True]
        }))

        async for message in ws:
            data = json.loads(message)
            if data.get('method') == 'depth_update':
                handle_depth_update(data['params'])

def handle_depth_update(params):
    update_data = params[0]
    is_first_message = update_data.get('past_update_id') is None

    if is_first_message:
        # First message or keepalive snapshot is a full snapshot - replace order book
        order_book.asks = update_data.get('asks', [])
        order_book.bids = update_data.get('bids', [])
    else:
        # Subsequent messages are incremental updates
        apply_updates(order_book.asks, update_data.get('asks', []), "ask")
        apply_updates(order_book.bids, update_data.get('bids', []), "bid")
        truncate_order_book(order_book.asks)
        truncate_order_book(order_book.bids)

def apply_updates(order_book_side, updates, side):
    for price, amount in updates:
        price = str(price)
        amount = str(amount)

        # Find existing entry
        price_index = next((i for i, level in enumerate(order_book_side) if level[0] == price), -1)

        if amount == '0':
            if price_index != -1:
                # Remove the existing price level since the amount is '0'.
                order_book_side.pop(price_index)
        else:
            if price_index == -1:
                # Find the position where the new price level should be inserted.
                insert_index = next((i for i, level in enumerate(order_book_side)
                                     if (side == "ask" and level[0] > price) or
                                     (side == "bid" and level[0] < price)), -1)
                if insert_index == -1:
                    # Add to the end if there's no higher price level.
                    order_book_side.append([price, amount])
                else:
                    # Insert at the correct sorted position.
                    order_book_side.insert(insert_index, [price, amount])
            else:
                # Update the amount for the existing price level.
                order_book_side[price_index][1] = amount

def truncate_order_book(order_book_side):
    if len(order_book_side) > LIMIT:
        del order_book_side[LIMIT:]

order_book = OrderBook()

asyncio.get_event_loop().run_until_complete(depth_subscribe())
```
</Tabs.Tab>
<Tabs.Tab>
```java showLineNumbers copy
import java.io.ByteArrayInputStream;
import java.net.URI;
import java.net.URISyntaxException;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.TimeUnit;
import javax.json.*;
import javax.websocket.*;

@ClientEndpoint
public class OrderBookClient {
    private static final int LIMIT = 100;
    private static List<IDepth> asks = new ArrayList<>();
    private static List<IDepth> bids = new ArrayList<>();
    private static CountDownLatch latch;

    public static void main(String[] args) throws URISyntaxException, InterruptedException {
        latch = new CountDownLatch(1);
        WebSocketContainer container = ContainerProvider.getWebSocketContainer();
        URI uri = new URI("wss://api.whitebit.com/ws");
        container.connectToServer(OrderBookClient.class, uri);
        latch.await(1, TimeUnit.MINUTES);
    }

    @OnOpen
    public void onOpen(Session session) throws Exception {
        JsonObject message = Json.createObjectBuilder()
                .add("id", 1)
                .add("method", "depth_subscribe")
                .add("params", Json.createArrayBuilder()
                        .add("ETH_BTC")
                        .add(LIMIT)
                        .add("0")
                        .add(true)  // multiple subscription flag
                .build();
        session.getBasicRemote().sendText(message.toString());
    }

    @OnMessage
    public void onMessage(String message, Session session) {
        JsonReader reader = Json.createReader(new ByteArrayInputStream(message.getBytes(StandardCharsets.UTF_8)));
        JsonObject jsonMessage = reader.readObject();

        if ("depth_update".equals(jsonMessage.getString("method"))) {
            JsonArray params = jsonMessage.getJsonArray("params");
            JsonObject updateData = params.getJsonObject(0);
            boolean isFirstMessage = !updateData.containsKey("past_update_id") || 
                                     updateData.isNull("past_update_id");

            if (isFirstMessage) {
                // First message or keepalive snapshot is a full snapshot - replace order book
                asks = parseOrderBookSide(updateData.getJsonArray("asks"));
                bids = parseOrderBookSide(updateData.getJsonArray("bids"));
            } else {
                // Subsequent messages are incremental updates
                applyUpdates(asks, updateData.getJsonArray("asks"), "ask");
                applyUpdates(bids, updateData.getJsonArray("bids"), "bid");
                truncateOrderBook(asks);
                truncateOrderBook(bids);
            }
        }
    }

    @OnClose
    public void onClose(Session session, CloseReason reason) {
        System.out.println("Connection closed: " + reason);
        latch.countDown();
    }

    @OnError
    public void onError(Session session, Throwable throwable) {
        throwable.printStackTrace();
        latch.countDown();
    }

    private static List<IDepth> parseOrderBookSide(JsonArray jsonArray) {
        List<IDepth> orderBookSide = new ArrayList<>();
        for (JsonValue value : jsonArray) {
            JsonArray level = value.asJsonArray();
            String price = level.getString(0);
            String amount = level.getString(1);
            orderBookSide.add(new IDepth(price, amount));
        }
        return orderBookSide;
    }

    private static void applyUpdates(List<IDepth> orderBookSide, JsonArray updates, String side) {
        for (JsonValue value : updates) {
            JsonArray level = value.asJsonArray();
            String price = level.getString(0);
            String amount = level.getString(1);

            int priceIndex = -1;
            for (int i = 0; i < orderBookSide.size(); i++) {
                if (orderBookSide.get(i).getPrice().equals(price)) {
                    priceIndex = i;
                    break;
                }
            }

            if ("0".equals(amount)) {
                if (priceIndex != -1) {
                    orderBookSide.remove(priceIndex);
                }
            } else {
                if (priceIndex == -1) {
                    int insertIndex = -1;
                    for (int i = 0; i < orderBookSide.size(); i++) {
                        if ((side.equals("ask") && orderBookSide.get(i).getPrice().compareTo(price) > 0) ||
                            (side.equals("bid") && orderBookSide.get(i).getPrice().compareTo(price) < 0)) {
                            insertIndex = i;
                            break;
                        }
                    }

                    if (insertIndex == -1) {
                        orderBookSide.add(new IDepth(price, amount));
                    } else {
                        orderBookSide.add(insertIndex, new IDepth(price, amount));
                    }
                } else {
                    orderBookSide.get(priceIndex).setAmount(amount);
                }
            }
        }
    }

    private static void truncateOrderBook(List<IDepth> orderBookSide) {
        if (orderBookSide.size() > LIMIT) {
            orderBookSide.subList(LIMIT, orderBookSide.size()).clear();
        }
    }

    static class IDepth {
        private final String price;
        private String amount;

        public IDepth(String price, String amount) {
            this.price = price;
            this.amount = amount;
        }

        public String getPrice() {
            return price;
        }

        public String getAmount() {
            return amount;
        }

        public void setAmount(String amount) {
            this.amount = amount;
        }
    }
}
```
</Tabs.Tab>
</Tabs>


#### Unsubscribe

This endpoint allows clients to unsubscribe from real-time updates of market depth data.

##### ⤴️ Request

```json
{
  "id": 13,
  "method": "depth_unsubscribe",
  "params": []
}
```

##### ⤵️ Response

```json
{
  "id": 13,
  "result": {
    "status": "success"
  },
  "error": null
}
```

---

### Book Ticker

The Book Ticker stream provides instant snapshot updates to the best bid and ask prices and quantities for a market.

#### Subscribe

Update interval: instant snapshot of the current best bid and ask (BBO), followed by incremental updates.

##### ⤴️ Request

```json
{
    "method": "bookTicker_subscribe",
    "params": [
        "SHIB_PERP" // Optional: market name. If empty, subscribes to all markets
    ],
    "id": 1
}
```

##### ⤵️ Response

```json
{
  "id": 1,
  "result": {
    "status": "success"
  },
  "error": null
}
```

##### 🔄 Update events

```json
{
    "method": "bookTicker_update",
    "params": [
        [
            1751958383.5933869, // transaction_time - timestamp of the update from matchengine
            1751958383.5935569, // message_time - timestamp of the message from websocket
            "SHIB_PERP",        // market
            80670102,           // update_id
            "0.000011751",      // best_bid_price
            "12547000",         // best_bid_amount
            "0.000011776",      // best_ask_price
            "17424000"          // best_ask_amount
        ]
    ],
    "id": null
}
```

#### Unsubscribe

##### ⤴️ Request

```json
{
    "method": "bookTicker_unsubscribe",
    "params": [],
    "id": 2
}
```

##### ⤵️ Response

```json
{
  "id": 2,
  "result": {
    "status": "success"
  },
  "error": null
}
```

---
import { Button } from "@/components/ui/button"
import { PlayCircle } from "lucide-react"

<div className="flex flex-col items-center my-12">
  <Button
    variant="outline"
    size="lg"
    onClick={() => {
      const event = new CustomEvent('open-playground', { detail: { mode: 'websocket' } });
      window.dispatchEvent(event);
    }}
    className="relative group px-8 py-6 shadow-lg bg-gradient-to-b from-white to-zinc-50/50 dark:from-zinc-900 dark:to-zinc-950/50 hover:shadow-xl overflow-hidden transition-all duration-300"
  >
    <div className="absolute inset-0 bg-gradient-to-r from-primary/10 via-blue-500/10 to-primary/10 dark:from-primary/[0.07] dark:via-blue-500/[0.07] dark:to-primary/[0.07] opacity-0 group-hover:opacity-100 transition-opacity duration-500 blur-xl scale-110" />
    <div className="absolute inset-0 bg-gradient-to-r from-primary/10 via-blue-500/10 to-primary/10 dark:from-primary/[0.07] dark:via-blue-500/[0.07] dark:to-primary/[0.07] opacity-0 group-hover:opacity-100 transition-opacity duration-500" />
    <div className="relative flex items-center gap-3">
      <div className="p-2 rounded-full bg-primary/10 dark:bg-primary/[0.15]">
        <PlayCircle className="w-6 h-6 text-primary dark:text-primary" />
      </div>
      <span className="text-lg font-medium bg-gradient-to-br from-primary to-blue-600 dark:from-primary dark:to-blue-400 text-transparent bg-clip-text">
        Open WebSocket Playground
      </span>
    </div>
  </Button>
  <div className="mt-4 flex justify-center">
    <div className="text-sm text-muted-foreground flex items-center gap-2">
      <div className="w-1 h-1 rounded-full bg-muted" />
      Try out WebSocket API directly in the documentation
      <div className="w-1 h-1 rounded-full bg-muted" />
    </div>
  </div>
</div>import { ApiEndpoint } from "@/components/api-endpoint";
import { Alert } from "@/components/alert";
import { ErrorCodeSelector } from "@/components/error-code-selector";
import { RegionalBaseUrl } from "@/components/regional-base-url";
import { InlineRegionSelector } from "@/components/inline-region-selector";
import { RegionalUrl } from "@/components/regional-url";
import { RegionalBaseUrlText } from "@/components/regional-base-url-text";
import { Code } from "nextra/components";

# Private HTTP API V4 for trading

- [Private HTTP API V4 for trading](#private-http-api-v4-for-trading)
  - [Error messages V4 format](#error-messages-v4-format)
  - [Market Fee](#market-fee)
    - [Query Market Fee](#query-market-fee)
    - [Query All Market Fees](#query-all-market-fees)
  - [Spot](#spot)
    - [Trading balance](#trading-balance)
    - [Create limit order](#create-limit-order)
    - [Bulk limit order](#bulk-limit-order)
    - [Create market order](#create-market-order)
    - [Create buy stock market order](#create-buy-stock-market-order)
    - [Create stop-limit order](#create-stop-limit-order)
    - [Create stop-market order](#create-stop-market-order)
    - [Cancel order](#cancel-order)
    - [Cancel all orders](#cancel-all-orders)
    - [Query Active Orders](#query-active-orders)
    - [Query executed order history](#query-executed-order-history)
    - [Query executed order deals](#query-executed-order-deals)
    - [Query executed orders](#query-executed-orders)
    - [Sync kill-switch timer](#sync-kill-switch-timer)
    - [Status kill-switch timer](#status-kill-switch-timer)
    - [Order modify](#modify-order)
  - [Collateral](#collateral)
    - [Collateral Account Balance](#collateral-account-balance)
    - [Collateral Account Balance Summary](#collateral-account-balance-summary)
    - [Collateral Limit Order](#collateral-limit-order)
    - [Collateral bulk limit order](#collateral-bulk-limit-order)
    - [Collateral Market Order](#collateral-market-order)
    - [Collateral Stop-Limit Order](#collateral-stop-limit-order)
    - [Collateral Trigger Market Order](#collateral-trigger-market-order)
    - [Collateral Account Summary](#collateral-account-summary)
    - [Open Positions](#open-positions)
    - [Positions History](#positions-history)
    - [Funding History](#funding-history)
    - [Change Collateral Account Leverage](#change-collateral-account-leverage)
    - [Query Active Conditional Orders](#query-active-conditional-orders)
    - [Query Active OCO Orders](#query-active-oco-orders)
    - [Create collateral OCO order](#create-collateral-oco-order)
    - [Cancel conditional order](#cancel-conditional-order)
    - [Cancel OCO order](#cancel-oco-order)
    - [Cancel OTO order](#cancel-oto-order)
  - [Convert](#convert)
    - [Estimate](#convert-estimate)
    - [Confirm](#convert-confirm)
    - [History](#convert-history)

---

<InlineRegionSelector className="my-4" />

Endpoint example: <Code><RegionalBaseUrlText />/api/v4/{"{endpoint}"}</Code>

All endpoints return time in Unix-time format.

All endpoints return either a **JSON** object or array.

For receiving responses from API calls please use http method **POST**

### Error messages V4 format

---

```json
{
  "code": 0,
  "message": "MESSAGE",
  "errors": {
    "PARAM1": ["MESSAGE"],
    "PARAM2": ["MESSAGE"]
  }
}
```

---

## Market Fee

### Query Market Fee

<ApiEndpoint method="POST" path="/api/v4/market/fee?market=BTC_USDT" />

This endpoint retrieves the maker and taker fees for a specific market. The `taker` and `maker` fields represent spot trading fees, while `futures_taker` and `futures_maker` represent futures trading fees. Futures fees return either the default values or custom values if set by the user.

**Parameters:**

| Name   | Type   | Mandatory | Description                         |
| ------ | ------ | --------- | ----------------------------------- |
| market | String | **Yes**   | Available market. Example: BTC_USDT |

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if validation failed`

```json
{
  "error": null,
  "taker": "0.1",           // Spot taker fee
  "maker": "0.1",           // Spot maker fee
  "futures_taker": "0.05",  // Futures taker fee (default or custom)
  "futures_maker": "0.03"  // Futures maker fee (default or custom)
}
```

### Query All Market Fees

<ApiEndpoint method="POST" path="/api/v4/market/fee" />

This endpoint retrieves the maker and taker fees for all markets, including any custom fees. The `taker` and `maker` fields represent default spot trading fees, while `futures_taker` and `futures_maker` represent futures trading fees (returning default values or custom values if set by the user). The `custom_fee` object contains market-specific custom spot fees.

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if validation failed`

```json
{
  "error": null,
  "taker": "0.1",           // Default spot taker fee
  "maker": "0.1",           // Default spot maker fee
  "futures_taker": "0.05",  // Default or custom futures taker fee
  "futures_maker": "0.03",  // Default or custom futures maker fee
  "custom_fee": {
    "BTC_USDT": ["0.1", "0.2"],
    "ETH_USDT": ["0.1", "0.2"]
  }
}
```

## Spot

### Trading balance

<ApiEndpoint method="POST" path="/api/v4/trade-account/balance" />

This endpoint retrieves the [trade balance](./../glossary.md#balance-spotbalance-trade) by currency [ticker](./../glossary.md#ticker) or all balances.

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name   | Type   | Mandatory | Description                                                |
| ------ | ------ | --------- | ---------------------------------------------------------- |
| ticker | String | **No**    | Currency's [ticker](./../glossary.md#ticker). Example: BTC |

**Request BODY raw:**

```json
{
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 422 if request validation failed`
- `Status 400 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "BTC": {
    "available": "0.123", // Available balance of currency for trading
    "freeze": "1" // Balance of currency that is currently in active orders
  },
  "USDT": {
    "available": "3013",
    "freeze": "100"
  }
}
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "ticker": ["Ticker field should be a string."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "ticker": ["Currency was not found."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>
___

### Create limit order

<ApiEndpoint method="POST" path="/api/v4/order/new" />

This endpoint creates [limit trading order](./../glossary.md#limit-order).

❗ Rate limit 10000 requests/10 sec.

**Parameters:**

| Name          | Type          | Mandatory | Description                                                                                                                                                                                                                                                                                       |
| ------------- | ------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market        | String        | **Yes**   | Available [market](./../glossary.md#market). Example: BTC_USDT                                                                                                                                                                                                                                    |
| side          | String        | **Yes**   | Order type. Variables: 'buy' / 'sell' Example: 'buy'                                                                                                                                                                                                                                              |
| amount        | String/Number | **Yes**   | Amount of [stock](./../glossary.md#stock) currency to buy or sell. Example: '0.001' or 0.001                                                                                                                                                                                                      |
| price         | String/Number | **Yes**   | Price in money currency. Example: '9800' or 9800                                                                                                                                                                                                                                                  |
| clientOrderId | String        | **No**    | Identifier should be unique and contain letters, dashes, numbers, dots or underscores. The identifier must be unique.                                                                                                                                                                             |
| postOnly      | boolean       | **No**    | [Orders](./../glossary.md#orders) are guaranteed to be the [maker](./../glossary.md#maker) order when [executed](./../glossary.md#finished-orders). Variables: 'true' / 'false' Example: 'false'.                                                                                                 |
| ioc           | boolean       | **No**    | An immediate or cancel order (IOC) is an order that attempts to execute all or part immediately and then cancels any unfilled portion of the order. Variables: 'true' / 'false' Example: 'false'.                                                                                                 |
| bboRole       | Integer       | **No**    | When you activate the [BBO](./../glossary.md#bbo) option when placing Limit orders, the system automatically selects the best market prices for executing these orders in one of two ways. Variables: 1 - Queue Method / 2 - Counterparty Method. You can use 2 method with ioc flag. Example: 2. |
| stp           | String        | **No**    | Self trade prevention mode. Variables: 'no / 'cancel_both' / 'cancel_new' /'cancel_old'. Example: 'no'.                                                                                                                                                                                           |
| rpi           | boolean       | **No**    | Retail Price Improvement(RPI) order: Order type designed to offer better prices to retail users. It is post-only and can match only with orders from the Web or Mobile App. RPI orders can be placed only by the designated Market Makers. Example: true                                          |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "side": "buy",
  "amount": "0.01",
  "price": "40000",
  "postOnly": false,
  "ioc": false,
  "clientOrderId": "order1987111",
  "rpi": true,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if request validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "orderId": 4180284841, // order id
  "clientOrderId": "order1987111", // custom client order id; "clientOrderId": "" - if not specified.
  "market": "BTC_USDT", // deal market
  "side": "buy", // order side
  "type": "limit", // order type
  "timestamp": 1595792396.165973, // timestamp of order creation
  "dealMoney": "0", // if order finished - amount in money currency that is finished
  "dealStock": "0", // if order finished - amount in stock currency that is finished
  "amount": "0.01", // amount
  "left": "0.001", // if order not finished - rest of the amount that must be finished
  "dealFee": "0", // fee in money that you pay if order is finished
  "price": "40000", // price
  "postOnly": false, // PostOnly
  "ioc": false, // IOC
  "status": "FILLED", // order status
  "stp": "no", // self trade prevention mode
  "rpi": true // RPI order flag
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed
- `32` - amount validation failed
- `33` - price validation failed
- `36` - clientOrderId validation failed
- `37` - ioc and postOnly flags are both true

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field is required."],
    "market": ["Market field is required."],
    "price": ["Price field is required."],
    "side": ["Side field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "side": ["Side field should contain only 'buy' or 'sell' values."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field should be numeric string or number."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be numeric string or number."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Given amount is less than min amount 0.001",
      "Min amount step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": ["ClientOrderId field should be a string."]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "ClientOrderId field field should contain only latin letters, numbers and dashes."
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "This client order id is already used by the current account."
    ]
  }
}
```

```json
{
  "code": 37,
  "message": "Validation failed",
  "errors": {
    "ioc": ["Either IOC or PostOnly flag in true state is allowed."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "total": ["Total(amount * price) is less than 5.05"]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Min amount step = 0.01" // money/stock precision is not taken into consideration when order was submitted
    ]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be at least 10", "Min price step = 0.000001"]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price should be greater than 0."]
  }
}
```

```json
{
  "code": 35,
  "message": "Validation failed",
  "errors": {
    "maker_fee": ["Incorrect maker fee"]
  }
}
```

```json
{
  "code": 10,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 11,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Amount too small."]
  }
}
```

```json
{
  "code": 13,
  "message": "Inner validation failed",
  "errors": {
    "postOnly": [
      "This order couldn't be executed as a maker order and was canceled."
    ]
  }
}
```

</details>

---

### Bulk limit order

<ApiEndpoint method="POST" path="/api/v4/order/bulk" />

This endpoint creates bulk [limit trading orders](./../glossary.md#limit-order).

❗Limit - From 1 to 20 orders by request.

**Parameters:**

| Name   | Type  | Mandatory | Description                                  |
| ------ | ----- | --------- | -------------------------------------------- |
| orders | Array | **Yes**   | Array of [limit orders](#create-limit-order) |

**Request BODY raw:**

```json
{
  "orders": [
    {
      "side": "buy",
      "amount": "0.02",
      "price": "40000",
      "market": "BTC_USDT",
      "postOnly": false,
      "ioc": false,
      "clientOrderId": "",
      "rpi": true
    },
    {
      "side": "sell",
      "amount": "0.0001",
      "price": "41000",
      "postOnly": false,
      "market": "BTC_USDT",
      "ioc": false,
      "clientOrderId": "",
      "rpi": true
    },
    {
      "side": "sell",
      "amount": "0.02",
      "price": "41000",
      "postOnly": false,
      "market": "BTC_USDT",
      "ioc": false,
      "clientOrderId": "",
      "rpi": true
    }
  ],
  "stopOnFail": true,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if request validation failed`
- `Status 503 if service temporary unavailable`

```json
[
  {
    "result": {
      "orderId": 4326248250, // order id
      "clientOrderId": "", // custom client order id; "clientOrderId": "" - if not specified.
      "market": "BTC_USDT", // deal market
      "side": "buy", // order side
      "type": "limit", // order type
      "timestamp": 1684916268.825564, // timestamp of order creation
      "dealMoney": "641.988", // if order finished - amount in money currency that is finished
      "dealStock": "0.02", // if order finished - amount in stock currency that is finished
      "amount": "0.02", // amount
      "left": "0", // if order not finished - rest of the amount that must be finished
      "dealFee": "1.283976", // fee in money that you pay if order is finished
      "ioc": false, // IOC
      "postOnly": false, // PostOnly
      "price": "40000", // price
      "status": "FILLED", // order status
      "stp": "no", // self trade prevention mode
      "positionSide": "BOTH", // position side
      "rpi": true // RPI order flag
    },
    "error": null
  },
  {
    "result": null,
    "error": {
      "code": 32,
      "message": "Validation failed",
      "errors": {
        "amount": ["Given amount is less than min amount 0.001."]
      }
    }
  },
  {
    "result": {
      "orderId": 4326248250,
      "clientOrderId": "",
      "market": "BTC_USDT",
      "side": "sell",
      "type": "limit",
      "timestamp": 1684916268.825564,
      "dealMoney": "641.988",
      "dealStock": "0.02",
      "amount": "0.02",
      "left": "0",
      "dealFee": "1.283976",
      "ioc": false,
      "postOnly": false,
      "price": "41000",
      "status": "FILLED",
      "stp": "no",
      "positionSide": "BOTH",
      "rpi": true
    },
    "error": null
  }
]
```

<details>

<summary>
  <b>Errors:</b>
</summary>

Error codes:

- `30` - default validation error code

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "orders": ["The orders must be an array."]
  }
}
```

<summary>
  <b>Errors in multiply response:</b>
</summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed
- `32` - amount validation failed
- `33` - price validation failed
- `36` - clientOrderId validation failed
- `37` - ioc and postOnly flags are both true

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field is required."],
    "market": ["Market field is required."],
    "price": ["Price field is required."],
    "side": ["Side field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "side": ["Side field should contain only 'buy' or 'sell' values."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field should be numeric string or number."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be numeric string or number."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Given amount is less than min amount 0.001",
      "Min amount step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": ["ClientOrderId field should be a string."]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "ClientOrderId field field should contain only latin letters, numbers and dashes."
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "This client order id is already used by the current account."
    ]
  }
}
```

```json
{
  "code": 37,
  "message": "Validation failed",
  "errors": {
    "ioc": ["Either IOC or PostOnly flag in true state is allowed."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "total": ["Total(amount * price) is less than 5.05"]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Min amount step = 0.01" // money/stock precision is not taken into consideration when order was submitted
    ]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be at least 10", "Min price step = 0.000001"]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price should be greater than 0."]
  }
}
```

```json
{
  "code": 35,
  "message": "Validation failed",
  "errors": {
    "maker_fee": ["Incorrect maker fee"]
  }
}
```

```json
{
  "code": 10,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 11,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Amount too small."]
  }
}
```

```json
{
  "code": 13,
  "message": "Inner validation failed",
  "errors": {
    "postOnly": [
      "This order couldn't be executed as a maker order and was canceled."
    ]
  }
}
```

</details>

---

### Create market order

<ApiEndpoint method="POST" path="/api/v4/order/market" />

This endpoint creates [market trading order](./../glossary.md#market-order).

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name          | Type          | Mandatory | Description                                                                                                                                                                                               |
| ------------- | ------------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market        | String        | **Yes**   | Available [market](./../glossary.md#market). Example: BTC_USDT                                                                                                                                            |
| side          | String        | **Yes**   | Order type. Variables: 'buy' / 'sell' Example: 'buy'                                                                                                                                                      |
| amount        | String/Number | **Yes**   | ⚠️️ Amount of [money](./../glossary.md#money) currency to buy or amount in [stock](./../glossary.md#stock) currency to sell. Example: '5 USDT' for buy (min total) and '0.001 BTC' for sell (min amount). |
| clientOrderId | String        | **No**    | Identifier should be unique and contain letters, dashes, numbers, dots or underscores. The identifier must be unique.                                                                                     |
| stp           | String        | **No**    | Self trade prevention mode. Variables: 'no / 'cancel_both' / 'cancel_new' /'cancel_old'. Example: 'no'.                                                                                                   |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "side": "buy",
  "amount": "50", // I want to buy BTC for 50 USDT
  "clientOrderId": "order1987111",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

```json
{
  "market": "BTC_USDT",
  "side": "sell",
  "amount": "0.01", // I want to sell 0.01 BTC
  "clientOrderId": "order1987111",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if request validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "orderId": 4180284841, // order id
  "clientOrderId": "order1987111", // custom client order id; "clientOrderId": "" - if not specified.
  "market": "BTC_USDT", // deal market
  "side": "buy", // order side
  "type": "market", // order type
  "timestamp": 1595792396.165973, // timestamp of order creation
  "dealMoney": "0", // amount in money currency that finished
  "dealStock": "0", // amount in stock currency that finished
  "amount": "0.001", // amount
  "left": "0.001", // rest of amount that must be finished
  "dealFee": "0", // fee in money that you pay if order is finished
  "status": "FILLED", // order status
  "stp": "no" // self trade prevention mode
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - [market](./../glossary.md#market) validation failed
- `32` - amount validation failed
- `36` - clientOrderId validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field is required."],
    "market": ["Market field is required."],
    "side": ["Side field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "side": ["Side field should contain only 'buy' or 'sell' values."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field should be numeric string or number."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Given amount is less than min amount 0.001",
      "Min amount step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": ["ClientOrderId field should be a string."]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "ClientOrderId field field should contain only latin letters, numbers and dashes."
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "This client order id is already used by the current account."
    ]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Total amount should be no less than 5.05 + trade fee"]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Min total step = = 0.000001"]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount should be greater than 0."]
  }
}
```

```json
{
  "code": 10,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 11,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Amount too small."]
  }
}
```

</details>

---

### Create buy stock market order

<ApiEndpoint method="POST" path="/api/v4/order/stock_market" />

This endpoint creates buy [stock](./../glossary.md#stock) market trading [order](./../glossary.md#orders).

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name          | Type          | Mandatory | Description                                                                                                           |
| ------------- | ------------- | --------- | --------------------------------------------------------------------------------------------------------------------- |
| market        | String        | **Yes**   | Available market. Example: BTC_USDT                                                                                   |
| side          | String        | **Yes**   | Order type. Available variables: "buy", "sell"                                                                        |
| amount        | String/Number | **Yes**   | ⚠️️ Amount in [stock](./../glossary.md#stock) currency for buy or sell. Example: "0.0001" or 0.0001.                  |
| clientOrderId | String        | **No**    | Identifier should be unique and contain letters, dashes, numbers, dots or underscores. The identifier must be unique. |
| stp           | String        | **No**    | Self trade prevention mode. Variables: 'no / 'cancel_both' / 'cancel_new' /'cancel_old'. Example: 'no'.               |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "side": "buy",
  "amount": "0.001", // I want to buy 0.001 BTC
  "clientOrderId": "order1987111",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if request validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "orderId": 4180284841,           // order id
  "clientOrderId": "order1987111", // custom client order id; "clientOrderId": "" - if not specified.
  "market": "BTC_USDT",            // deal market
  "side": "buy",                   // order side
  "type": "stock market",          // order type
  "timestamp": 1595792396.165973,  // timestamp of order creation
  "dealMoney": "0",                // amount in money currency that finished
  "dealStock": "0",                // amount in stock currency that finished
  "amount": "0.001",               // amount
  "left": "0.001",                 // rest of amount that must be finished
  "dealFee": "0"                   // fee in money that you pay if order is finished
  "status": "FILLED" ,            // order status
  "stp": "no"                      // self trade prevention mode
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed
- `32` - amount validation failed
- `36` - clientOrderId validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field is required."],
    "market": ["Market field is required."],
    "side": ["Side field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "side": ["Side field should contain only 'buy' or 'sell' values."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field should be numeric string or number."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Given amount is less than min amount 0.001",
      "Min amount step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": ["ClientOrderId field should be a string."]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "ClientOrderId field field should contain only latin letters, numbers and dashes."
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "This client order id is already used by the current account."
    ]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount should be greater than 0."]
  }
}
```

```json
{
  "code": 10,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 11,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Amount too small."]
  }
}
```

</details>

---

### Create stop-limit order

<ApiEndpoint method="POST" path="/api/v4/order/stop_limit" />

This endpoint creates [stop-limit trading order](./../glossary.md#stop-limit-order)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name             | Type          | Mandatory | Description                                                                                                                                                                                                                                                                                       |
| ---------------- | ------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market           | String        | **Yes**   | Available market. Example: BTC_USDT                                                                                                                                                                                                                                                               |
| side             | String        | **Yes**   | Order type. Variables: 'buy' / 'sell' Example: 'buy'                                                                                                                                                                                                                                              |
| amount           | String/Number | **Yes**   | Amount of [stock](./../glossary.md#stock) currency to buy or sell. Example: '0.001' or 0.001                                                                                                                                                                                                      |
| price            | String/Number | **Yes**   | Price in [money](./../glossary.md#money) currency. Example: '9800' or 9800                                                                                                                                                                                                                        |
| activation_price | String/Number | **Yes**   | Activation price in [money](./../glossary.md#money) currency. Example: '10000' or 10000                                                                                                                                                                                                           |
| clientOrderId    | String        | **No**    | Identifier should be unique and contain letters, dashes, numbers, dots or underscores. The identifier must be unique.                                                                                                                                                                             |
| bboRole          | Integer       | **No**    | When you activate the [BBO](./../glossary.md#bbo) option when placing Limit orders, the system automatically selects the best market prices for executing these orders in one of two ways. Variables: 1 - Queue Method / 2 - Counterparty Method.                                                 |
| stp              | String        | **No**    | Self trade prevention mode. Variables: 'no / 'cancel_both' / 'cancel_new' /'cancel_old'. Example: 'no'.                                                                                                                                                                                           |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "side": "buy",
  "amount": "0.001",
  "price": "40000",
  "activation_price": "40000",
  "clientOrderId": "order1987111",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if request validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "orderId": 4180284841, // order id
  "clientOrderId": "order1987111", // custom client order id; "clientOrderId": "" - if not specified.
  "market": "BTC_USDT", // deal market
  "side": "buy", // order side
  "type": "stop limit", // order type
  "timestamp": 1595792396.165973, // timestamp of order creation
  "dealMoney": "0", // if order finished - amount in money currency that finished
  "dealStock": "0", // if order finished - amount in stock currency that finished
  "amount": "0.001", // amount
  "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - it will be rounded to zero
  "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - it will be rounded to zero
  "left": "0.001", // if order not finished - rest of amount that must be finished
  "dealFee": "0", // fee in money that you pay if order is finished
  "price": "40000", // price
  "activation_price": "40000", // activation price
  "status": "FILLED", // order status
  "stp": "no" // self trade prevention mode
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed
- `32` - amount validation failed
- `33` - price validation failed
- `36` - clientOrderId validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Activation price field is required."],
    "amount": ["Amount field is required."],
    "market": ["Market field is required."],
    "price": ["Price field is required."],
    "side": ["Side field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "side": ["Side field should contain only 'buy' or 'sell' values."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field should be numeric string or number."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be numeric string or number."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Given amount is less than min amount 0.001",
      "Min amount step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "total": ["Total(amount * price) is less than 5.05"]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": ["ClientOrderId field should be a string."]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "ClientOrderId field field should contain only latin letters, numbers and dashes."
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "This client order id is already used by the current account."
    ]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount should be greater than 0."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be at least 10", "Min price step = 0.000001"]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price should be greater than 0."]
  }
}
```

```json
{
  "code": 35,
  "message": "Validation failed",
  "errors": {
    "maker_fee": ["Incorrect maker fee"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": [
      "Activation price should not be equal to the last price"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Activation price should be numeric string."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Activation price should be greater than 0."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Empty history"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Min activation price = 10"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Min activation price step = 0.00001"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": [
      "Activation price should not be equal to the last price"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "lastPrice": ["internal error"]
  }
}
```

```json
{
  "code": 10,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 11,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Amount too small."]
  }
}
```

</details>

---

### Create stop-market order

<ApiEndpoint method="POST" path="/api/v4/order/stop_market" />

This endpoint creates [stop-market trading order](./../glossary.md#stop-market-order)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name             | Type          | Mandatory | Description                                                                                                                                                                                            |
| ---------------- | ------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| market           | String        | **Yes**   | Available market. Example: BTC_USDT                                                                                                                                                                    |
| side             | String        | **Yes**   | Order type. Variables: 'buy' / 'sell' Example: 'buy'                                                                                                                                                   |
| amount           | String/Number | **Yes**   | ⚠️️Amount of [**`money`**](./../glossary.md#money) currency to **buy** or amount in [**`stock`**](./../glossary.md#stock) currency to **sell**. Example: '0.01' or 0.01 for buy and '0.0001' for sell. |
| activation_price | String/Number | **Yes**   | Activation price in [money](./../glossary.md#money) currency. Example: '10000' or 10000                                                                                                                |
| clientOrderId    | String        | **No**    | Identifier should be unique and contain letters, dashes, numbers, dots or underscores. The identifier must be unique.                                                                                  |
| stp              | String        | **No**    | Self trade prevention mode. Variables: 'no / 'cancel_both' / 'cancel_new' /'cancel_old'. Example: 'no'.                                                                                                |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "side": "buy",
  "amount": "50", // I want to buy for 50 USDT
  "activation_price": "40000",
  "clientOrderId": "order1987111",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

```json
{
  "market": "BTC_USDT",
  "side": "sell",
  "amount": "0.001", // I want to sell 0.01 BTC
  "activation_price": "40000",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "orderId": 4180284841, // order id
  "clientOrderId": "order1987111", // custom order identifier; "clientOrderId": "" - if not specified.
  "market": "BTC_USDT", // deal market
  "side": "buy", // order side
  "type": "stop market", // order type
  "timestamp": 1595792396.165973, // timestamp of order creation
  "dealMoney": "0", // if order finished - amount in money currency that finished
  "dealStock": "0", // if order finished - amount in stock currency that finished
  "amount": "0.001", // amount
  "left": "0.001", // if order not finished - rest of amount that must be finished
  "dealFee": "0", // fee in money that you pay if order is finished
  "activation_price": "40000", // activation price
  "status": "FILLED", // order status
  "stp": "no" // self trade prevention mode
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed
- `32` - amount validation failed
- `36` - clientOrderId validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Activation price field is required."],
    "amount": ["Amount field is required."],
    "market": ["Market field is required."],
    "side": ["Side field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "side": ["Side field should contain only 'buy' or 'sell' values."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field should be numeric string or number."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Given amount is less than min amount 0.001",
      "Min amount step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": ["ClientOrderId field should be a string."]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "ClientOrderId field field should contain only latin letters, numbers and dashes."
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "This client order id is already used by the current account."
    ]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount should be greater than 0."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": [
      "Activation price should not be equal to the last price"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Activation price should be numeric string."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Activation price should be greater than 0."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Empty history"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Min activation price = 10"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Min activation price step = 0.00001"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": [
      "Activation price should not be equal to the last price"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "lastPrice": ["internal error"]
  }
}
```

```json
{
  "code": 10,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 11,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Amount too small."]
  }
}
```

</details>

---

### Cancel order

<ApiEndpoint method="POST" path="/api/v4/order/cancel" />

Cancel existing [order](./../glossary.md#orders)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name          | Type       | Mandatory                      | Description                                                    |
| ------------- | ---------- | ------------------------------ | -------------------------------------------------------------- |
| market        | String     | **Yes**                        | Available [market](./../glossary.md#market). Example: BTC_USDT |
| orderId       | String/Int | **No if clientOrderId is set** | Order Id. Example: 4180284841 or "4180284841"                  |
| clientOrderId | String     | **No if orderId is set**       | Custom client order id. Example: "customId11"                  |

❗ Modification by clientOrderId takes priority over orderId.
❗ The request supports working only with orderId or only with clientOrderId.
❗ You cannot pass both values at the same time.

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "orderId": 4180284841,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "orderId": 4180284841, // order id
  "clientOrderId": "customId11", // custom order identifier; "clientOrderId": "" - if not specified.
  "market": "BTC_USDT", // deal market
  "side": "buy", // order side
  "type": "limit", // order type
  "timestamp": 1595792396.165973, // timestamp of order creation
  "dealMoney": "0", // if order finished - amount in money currency that is finished
  "dealStock": "0", // if order finished - amount in stock currency that is finished
  "amount": "0.001", // amount
  "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - it will be rounded to zero
  "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - it will be rounded to zero
  "left": "0.001", // if order not finished - rest of the amount that must be finished
  "dealFee": "0", // fee in money that you pay if order is finished
  "price": "40000", // price if price isset
  "status": "FILLED", // order status
  "stp": "no", // self trade prevention mode
  "rpi": true // RPI order flag
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field is required."],
    "orderId": ["OrderId field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "orderId": ["OrderId field should be an integer."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": [
      "Market field should be a string.",
      "Market field format is invalid."
    ]
  }
}
```

```json
{
  "code": 2,
  "message": "Inner validation failed",
  "errors": {
    "orderId": ["Unexecuted order was not found."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

---

### Cancel all orders

<ApiEndpoint method="POST" path="/api/v4/order/cancel/all" />

Cancels all orders that meet the conditions [order](./../glossary.md#orders)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name   | Type   | Mandatory | Description                                                    |
| ------ | ------ | --------- | -------------------------------------------------------------- |
| market | String | **No**    | Available [market](./../glossary.md#market). Example: BTC_USDT |
| type   | Array  | **No**    | Order types value. Example: "spot", "margin", "futures"        |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "type": ["Margin", "Futures", "Spot"]
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if validation failed`
- `Status 503 if service temporary unavailable`

```json
[]
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "type": ["The type must be an array."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": [
      "Market field should be a string.",
      "Market field format is invalid."
    ]
  }
}
```

```json
{
  "code": 2,
  "message": "Inner validation failed",
  "errors": {
    "orderId": ["Unexecuted order was not found."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

---

### Query Active Orders

<ApiEndpoint method="POST" path="/api/v4/orders" />

This endpoint retrieves [active orders](./../glossary.md#active-orders) (orders not yet executed).

❗ Rate limit 1000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name          | Type       | Mandatory | Description                                                                                                                                                           |
| ------------- | ---------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market        | String     | **No**    | Available [market](./../glossary.md#market). Example: BTC_USDT                                                                                                        |
| orderId       | String/Int | **No**    | Available orderId. Example: 3134995325                                                                                                                                |
| clientOrderId | String     | **No**    | Available clientOrderId. Example: customId11                                                                                                                          |
| limit         | String/Int | **No**    | LIMIT is a special clause used to limit records a particular query can return. Default: 50, Min: 1, Max: 100                                                          |
| offset        | String/Int | **No**    | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. Default: 0, Min: 0 |

Search across all markets is available only if clientOrderId and orderId are not provided.

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "orderId": "3134995325", //order Id (optional)
  "clientOrderId": "customId11", // custom order id; (optional)
  "offset": 0,
  "limit": 100,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 422 if request validation failed`
- `Status 400 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
[
  {
    "orderId": 3686033640, // unexecuted order ID
    "clientOrderId": "customId11", // custom order id; "clientOrderId": "" - if not specified.
    "market": "BTC_USDT", // currency market
    "side": "buy", // order side
    "type": "limit", // unexecuted order type
    "timestamp": 1594605801.49815, // timestamp of order creation
    "dealMoney": "0", // executed amount in money
    "dealStock": "0", // executed amount in stock
    "amount": "2.241379", // active order amount
    "left": "2.241379", // unexecuted amount in stock
    "dealFee": "0", // executed fee by deal
    "price": "40000", // unexecuted order price
    "status": "FILLED", // order status
    "stp": "no", // self trade prevention mode
    "rpi": true, // RPI order flag
    "oto": {
      // OTO order data - if stopLoss or takeProfit is specified
      "otoId": 29457221, // ID of the OTO
      "stopLoss": "30000", // stop loss order price - if stopLoss is specified
      "takeProfit": "50000" // take profit order price - if takeProfit is specified
    }
  }
]
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["The market field is required."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should be a string."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field format is invalid."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "message": "Validation failed",
  "code": 31,
  "errors": {
    "market": ["Market is not available"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["The limit must be an integer."],
    "offset": ["The offset must be an integer."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["The limit may not be greater than 100."],
    "offset": ["The offset may not be greater than 10000."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["The limit must be at least 1."],
    "offset": ["The offset must be at least 0."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

---

### Query executed order history

<ApiEndpoint method="POST" path="/api/v4/trade-account/executed-history" />

This endpoint retrieves all deals for all markets. Can be filtered by single market if needed.

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name          | Type       | Mandatory | Description                                                                                                                                                           |
| ------------- | ---------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market        | String     | **No**    | Requested market. Example: BTC_USDT                                                                                                                                   |
| clientOrderId | String     | **No**    | Requested clientOrderId. Example: customId11    
| startDate     | Int        | **No**    | Start date in Unix-time format                                                                                                                    |
| endDate       | Int        | **No**    | End date in Unix-time format                                                                                                                         |
| limit         | String/Int | **No**    | LIMIT is a special clause used to limit records a particular query can return. Default: 50, Min: 1, Max: 100                                                          |
| offset        | String/Int | **No**    | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. Default: 0, Min: 0 |

<Alert
  type="warning"
  header="Important Limitations"
  message="This method can retrieve data not older than 6 months from current month. If you need older data - you can use Report on the History page in your account."
/>

**Request BODY raw:**

```json
{
  "clientOrderId": "customId11", // custom order id; (optional)
  "offset": 0,
  "limit": 100,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 422 if request validation failed`
- `Status 400 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "BTC_USDT": [
    {
      "id": 8846967538, // deal ID
      "clientOrderId": "customId11", // custom order id; "clientOrderId": "" - if not specified.
      "time": 1739310711.387599, // Timestamp of the executed deal
      "side": "buy", // Deal side "sell" / "buy"
      "role": 2, // Role - 1 - maker, 2 - taker
      "amount": "2.717", // amount in stock
      "price": "3.3419", // price
      "deal": "9.0799423", // amount in money
      "fee": "0.002717", // paid fee
      "orderId": 1164603916051, // order ID
      "feeAsset": "SUI" // fee asset
    }
  ]
}
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["Limit field should be an integer."],
    "offset": ["Offset field should be an integer."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field format is invalid."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should be a string."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["Limit should not be greater than 100."],
    "offset": ["Offset should not be greater than 10000."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["Limit should be at least 1."],
    "offset": ["Offset should be at least 0."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

---

### Query executed order deals

<ApiEndpoint method="POST" path="/api/v4/trade-account/order" />

This endpoint retrieves deals of a specific order. [deals](./../glossary.md#deal-trade) history details on pending or [executed order](./../glossary.md#finished-orders).

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name    | Type       | Mandatory | Description                                                                                                                                                          |
| ------- | ---------- | --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| orderId | String/Int | **Yes**   | Order ID. Example: 1234                                                                                                                                              |
| limit   | String/Int | **No**    | LIMIT is a special clause used to limit records a particular query can return. Default: 50, Min: 1, Max: 100                                                         |
| offset  | String/Int | **No**    | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. Default: 0, Min: 0 |

<Alert
  type="warning"
  header="Important Limitations"
  message="This method can retrieve data not older than 6 months from current month. If you need older data - you can use Report on the History page in your account."
/>

**Request BODY raw:**

```json
{
  "orderId": 3135554375,
  "offset": 0,
  "limit": 100,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 422 if request validation failed`
- `Status 400 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "records": [
    {
      "time": 1593342324.613711,     // Timestamp of executed order
      "fee": "0.00000419198",        // fee that you pay
      "price": "0.00000701",         // price
      "amount": "598",               // amount in stock
      "id": 149156519,               // deal id
      "dealOrderId": 3134995325,     // completed order Id
      "clientOrderId": "customId11", // custom order id; "clientOrderId": "" - if not specified.
      "role": 2,                     // Role - 1 - maker, 2 - taker
      "deal": "0.00419198",          // amount in money
      "feeAsset": "USDT",            // fee asset
      "rpi": true                    // RPI order flag
    }
  ],
  "offset": 0,
  "limit": 100
}
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "orderId": ["Order was not found."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "orderId": ["OrderId field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "orderId": ["OrderId field should be an integer."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["Limit should not be greater than 100."],
    "offset": ["Offset should not be greater than 10000."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["Limit should be at least 1."],
    "offset": ["Offset should be at least 0."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

---

### Query executed orders

<ApiEndpoint method="POST" path="/api/v4/trade-account/order/history" />

This endpoint retrieves all orders for markets. [executed order](./../glossary.md#finished-orders) history by [market](./../glossary.md#market).

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name          | Type       | Mandatory | Description                                                                                                                                                           |
| ------------- | ---------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market        | String/Int | **No**    | Requested available market. Example: BTC_USDT                                                                                                                         |
| orderId       | String/Int | **No**    | Requested available orderId. Example: 3134995325                                                                                                                      |
| startDate     | Int        | **No**    | Start date in Unix-time format                                                                                                                    |
| endDate       | Int        | **No**    | End date in Unix-time format      
| clientOrderId | String     | **No**    | Requested available clientOrderId. Example: clientOrderId                                                                                                             |
| limit         | String/Int | **No**    | LIMIT is a special clause used to limit records a particular query can return. Default: 50, Min: 1, Max: 100                                                          |
| offset        | String/Int | **No**    | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. Default: 0, Min: 0 |
| status        | String     | **No**    | Possible values: "ALL", "OPEN", "FILLED", "CANCELED", "AUTO_CANCELED_USER_MARGIN", "AUTO_CANCELED_LIQUIDATION", "AUTO_CANCELED_REDUCE_ONLY", "PARTIALLY_FILLED", "CANCELED_STP", "CANCELED_POSITION_SIDE_NOT_MATCH" |

<Alert
  type="warning"
  header="Important Limitations"
  message="This method can retrieve data not older than 6 months from current month. If you need older data - you can use Report on the History page in your account."
/>

**Request BODY raw:**

```json
{
  "market": "BTC_USDT", //optional
  "orderId": "3134995325", //order Id (optional)
  "clientOrderId": "clientOrderId", // custom order id; (optional)
  "startDate": 1597486960, // start date in Unix-time format (optional)
  "endDate": 1597486960, // end date in Unix-time format (optional)
  "offset": 0,
  "limit": 100,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 422 if request validation failed`
- `Status 400 if inner validation failed`
- `Status 503 if service temporary unavailable`

Empty response if order is not yours

```json
{
  "BTC_USDT": [
    {
      "amount": "0.0009", // amount of trade
      "price": "40000", // price
      "type": "limit", // order type
      "id": 4986126152, // order id
      "clientOrderId": "customId11", // custom order identifier; "clientOrderId": "" - if not specified.
      "side": "sell", // order side
      "ctime": 1597486960.311311, // timestamp of order creation
      "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - its rounded to zero
      "ftime": 1597486960.311332, // executed order timestamp
      "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - its rounded to zero
      "dealFee": "0.041258268", // paid fee if order is finished
      "dealStock": "0.0009", // amount in stock currency that finished
      "dealMoney": "41.258268", // amount in money currency that finished
      "postOnly": false, // PostOnly flag
      "ioc": false, // IOC flag
      "status": "CANCELED", // Order status
      "feeAsset": "USDT", // fee asset
      "stp": "no", // self trade prevention mode
      "rpi": false // RPI order flag
    }
  ]
}
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["Limit field should be an integer."],
    "offset": ["Offset field should be an integer."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field format is invalid."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should be a string."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["Limit should not be greater than 100."],
    "offset": ["Offset should not be greater than 10000."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["Limit should be at least 1."],
    "offset": ["Offset should be at least 0."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

### Modify order

<ApiEndpoint method="POST" path="/api/v4/order/modify" />

This endpoint modify existing [order](./../glossary.md#orders)

Supported order types: limit, stop limit, stop market, stop limit

Request must contain one of the following parameters: `amount`, `price`, `activationPrice`

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name            | Type          | Mandatory                      | Description                                                                                  |
| --------------- | ------------- | ------------------------------ | -------------------------------------------------------------------------------------------- |
| orderId         | Integer       | **No if clientOrderId is set** | Active order id [order](./../glossary.md#active-orders). Example: 834506                     |
| clientOrderId   | String        | **No if orderId is set**       | Identifier should be unique and contain letters, dashes, numbers, dots or underscores.       |
| market          | String        | **Yes**                        | Available [market](./../glossary.md#market). Example: BTC_USDT                               |
| amount          | String/Number | **No**                         | Amount of [stock](./../glossary.md#stock) currency to buy or sell. Example: '0.001' or 0.001 |
| total           | String/Number | **No**                         | Total of [money](./../glossary.md#money) currency to buy or sell. Example: '0.001' or 0.001  |
| price           | String/Number | **No**                         | Price in [money](./../glossary.md#money) currency. Example: '9800' or 9800                   |
| activationPrice | String/Number | **No**                         | Activation price in [money](./../glossary.md#money) currency. Example: '10000' or 10000      |

❗ Use total parameter instead of amount for modify buy stop market order.
❗ Modification by clientOrderId takes priority.
❗ The request supports working only with orderId or only with clientOrderId.
❗ You cannot pass both values at the same time.
**Request BODY raw:**

```json
{
  "orderId": 2590468842,
  "market": "BTC_USDT",
  "price": "38635",
  "activationPrice": "123456",
  "amount": "2",
  "clientOrderId": "1a2s3f4g5h6v",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200` - Order successfully modified
- `Status 400` - Bad Request (client errors): Invalid arguments, order not found, quote expired, activation price issues
  - Error codes: 1, 2, 6, 20, 24, 101, 158
- `Status 422` - Unprocessable Entity (business logic validation): Balance insufficient, trading restrictions, order type conflicts, price bands exceeded
  - Error codes: 10, 11, 12, 13, 14, 15, 16, 17, 25, 27, 40, 42, 51, 103, 104, 105, 106, 111, 112, 113, 114, 115, 150, 151, 152, 153, 155, 157, 159, 160, 161, 162, 163, 250, 251, 300, 302, 330
- `Status 503` - Service temporarily unavailable

```json
[
  {
    "orderId": 2590468939,
    "clientOrderId": "1clientOrderId1",
    "market": "BTC_USDT",
    "side": "buy",
    "type": "limit",
    "timestamp": 1706023985.307382,
    "dealMoney": "0",
    "dealStock": "0",
    "amount": "0.001",
    "left": "0.001",
    "dealFee": "0",
    "ioc": false,
    "price": "38635",
    "postOnly": false,
    "status": "FILLED",
    "stp": "no",
    "rpi": true
  }
]
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": [
      "Market field should be a string.",
      "Market field format is invalid."
    ]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field should be numeric string or number."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be numeric string or number."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Given amount is less than min amount 0.001",
      "Min amount step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": ["ClientOrderId field should be a string."]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "ClientOrderId field field should contain only latin letters, numbers and dashes."
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "This client order id is already used by the current account."
    ]
  }
}
```

```json
{
  "code": 37,
  "message": "Validation failed",
  "errors": {
    "ioc": ["Either IOC or PostOnly flag in true state is allowed."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "total": ["Total(amount * price) is less than 5.05"]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Min amount step = 0.01" // money/stock precision is not taken into consideration when order was submitted
    ]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be at least 10", "Min price step = 0.000001"]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price should be greater than 0."]
  }
}
```

```json
{
  "code": 35,
  "message": "Validation failed",
  "errors": {
    "maker_fee": ["Incorrect maker fee"]
  }
}
```

```json
{
  "code": 10,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 11,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount too small."]
  }
}
```

```json
{
  "code": 2,
  "message": "Inner validation failed",
  "errors": {
    "orderId": ["Unexecuted order was not found."]
  }
}
```

```json
{
  "code": 6,
  "message": "Inner validation failed",
  "errors": {
    "orderId": ["Unexecuted order was not found."]
  }
}
```

```json
{
  "code": 7,
  "message": "Validation failed",
  "errors": {
    "orderId": ["order not found."]
  }
}
```

```json
{
  "code": 10,
  "message": "Validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 12,
  "message": "Validation failed",
  "errors": {
    "amount": ["The amount field value, that the API unable to process."]
  }
}
```

```json
{
  "code": 13,
  "message": "Validation failed",
  "errors": {
    "postOnly": ["This order couldn't be executed as a maker order and was canceled."]
  }
}
```

```json
{
  "code": 14,
  "message": "Validation failed",
  "errors": {
    "postOnly": ["This order couldn't be executed as a maker order and was canceled."]
  }
}
```

```json
{
  "code": 15,
  "message": "Validation failed",
  "errors": {
    "error": ["Please try again later."]
  }
}
```

```json
{
  "code": 16,
  "message": "Validation failed",
  "errors": {
    "error": ["Please try again later."]
  }
}
```

```json
{
  "code": 17,
  "message": "Validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 40,
  "message": "Validation failed",
  "errors": {
    "postOnly": ["Limit order is not post only"]
  }
}
```

```json
{
  "code": 42,
  "message": "Validation failed",
  "errors": {
    "stp": ["trading group does not match"]
  }
}
```

```json
{
  "code": 51,
  "message": "Validation failed",
  "errors": {
    "price": ["Trading in the market is not allowed."]
  }
}
```

```json
{
  "code": 101,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Activation price should not be equal to the last price."]
  }
}
```

```json
{
  "code": 103,
  "message": "Validation failed",
  "errors": {
    "error": ["Max. limit of margin stop limit orders have been reached."]
  }
}
```

```json
{
  "code": 104,
  "message": "Validation failed",
  "errors": {
    "positionId": ["position doesn't exist."]
  }
}
```

```json
{
  "code": 105,
  "message": "Validation failed",
  "errors": {
    "takeProfit": ["Wrong activation price for take profit."]
  }
}
```

```json
{
  "code": 106,
  "message": "Validation failed",
  "errors": {
    "stopLoss": ["Wrong activation price for stop loss."]
  }
}
```

```json
{
  "code": 111,
  "message": "Validation failed",
  "errors": {
    "amount": ["margin position too big"]
  }
}
```

```json
{
  "code": 112,
  "message": "Validation failed",
  "errors": {
    "amount": ["margin pending orders value too big"]
  }
}
```

```json
{
  "code": 113,
  "message": "Validation failed",
  "errors": {
    "hedgeMode": ["Position side cannot be changed if there exists futures positions or orders"]
  }
}
```

```json
{
  "code": 114,
  "message": "Validation failed",
  "errors": {
    "hedgeMode": ["Order's position side does not match user's setting"]
  }
}
```

```json
{
  "code": 115,
  "message": "Validation failed",
  "errors": {
    "hedgeMode": ["Order would result in a new position in the opposite direction"]
  }
}
```

```json
{
  "code": 150,
  "message": "Validation failed",
  "errors": {
    "price": ["Can't place limit order."]
  }
}
```

```json
{
  "code": 151,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Wrong activation price for stop loss."]
  }
}
```

```json
{
  "code": 152,
  "message": "Validation failed",
  "errors": {
    "error": ["Max. limit of margin stop limit orders have been reached."]
  }
}
```

```json
{
  "code": 153,
  "message": "Validation failed",
  "errors": {
    "price": ["Not enough balance for limit order."]
  }
}
```

```json
{
  "code": 155,
  "message": "Validation failed",
  "errors": {
    "orderId": ["Can't modify conditional order."]
  }
}
```

```json
{
  "code": 157,
  "message": "Validation failed",
  "errors": {
    "amount": ["Wrong order deal size."]
  }
}
```

```json
{
  "code": 158,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Activation price can't be set for a limit order."]
  }
}
```

```json
{
  "code": 159,
  "message": "Validation failed",
  "errors": {
    "price": ["Limit price can't be set for stop market order."]
  }
}
```

```json
{
  "code": 160,
  "message": "Validation failed",
  "errors": {
    "orderId": ["tpsl orders can't be modified."]
  }
}
```

```json
{
  "code": 161,
  "message": "Validation failed",
  "errors": {
    "price": ["Wrong order conditions"]
  }
}
```

```json
{
  "code": 162,
  "message": "Validation failed",
  "errors": {
    "total": ["Total cannot be specified for this order type"]
  }
}
```

```json
{
  "code": 163,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount cannot be specified for this order type"]
  }
}
```

```json
{
  "code": 250,
  "message": "Validation failed",
  "errors": {
    "price": ["The Price is out of bands"]
  }
}
```

```json
{
  "code": 251,
  "message": "Validation failed",
  "errors": {
    "stopLimitPrice": ["The Price is out of bands"]
  }
}
```

```json
{
  "code": 300,
  "message": "Validation failed",
  "errors": {
    "request": ["fee not found"]
  }
}
```

```json
{
  "code": 302,
  "message": "Validation failed",
  "errors": {
    "amount": ["margin balance update magnitude limit exceeded"]
  }
}
```

```json
{
  "code": 330,
  "message": "Validation failed",
  "errors": {
    "request": ["fee not found"]
  }
}
```

```json
{
  "code": 20,
  "message": "Inner validation failed",
  "errors": {
    "quoteId": ["quote expired"]
  }
}
```

```json
{
  "code": 24,
  "message": "Inner validation failed",
  "errors": {
    "quoteId": ["quote not found."]
  }
}
```

```json
{
  "code": 25,
  "message": "Validation failed",
  "errors": {
    "amount": ["quote amount is too big"]
  }
}
```

```json
{
  "code": 27,
  "message": "Validation failed",
  "errors": {
    "market": ["conversion markets not found"]
  }
}
```

</details>

<ErrorCodeSelector 
  errorCodes={[
    { code: 1, message: "Inner validation failed", field: "amount", description: "Invalid argument." },
    { code: 2, message: "Inner validation failed", field: "orderId", description: "Unexecuted order was not found." },
    { code: 6, message: "Inner validation failed", field: "orderId", description: "Unexecuted order was not found." },
    { code: 7, message: "Validation failed", field: "orderId", description: "order not found." },
    { code: 10, message: "Validation failed", field: "amount", description: "Not enough balance." },
    { code: 11, message: "Validation failed", field: "amount", description: "Amount too small." },
    { code: 12, message: "Validation failed", field: "amount", description: "The amount field value, that the API unable to process." },
    { code: 13, message: "Validation failed", field: "postOnly", description: "This order couldn't be executed as a maker order and was canceled." },
    { code: 14, message: "Validation failed", field: "postOnly", description: "This order couldn't be executed as a maker order and was canceled." },
    { code: 15, message: "Validation failed", field: "error", description: "Please try again later." },
    { code: 16, message: "Validation failed", field: "error", description: "Please try again later." },
    { code: 17, message: "Validation failed", field: "amount", description: "Not enough balance." },
    { code: 20, message: "Inner validation failed", field: "quoteId", description: "quote expired" },
    { code: 24, message: "Inner validation failed", field: "quoteId", description: "quote not found." },
    { code: 25, message: "Validation failed", field: "amount", description: "quote amount is too big" },
    { code: 27, message: "Validation failed", field: "market", description: "conversion markets not found" },
    { code: 40, message: "Validation failed", field: "postOnly", description: "Limit order is not post only" },
    { code: 42, message: "Validation failed", field: "stp", description: "trading group does not match" },
    { code: 51, message: "Validation failed", field: "price", description: "Trading in the market is not allowed." },
    { code: 101, message: "Validation failed", field: "activation_price", description: "Activation price should not be equal to the last price." },
    { code: 103, message: "Validation failed", field: "error", description: "Max. limit of margin stop limit orders have been reached." },
    { code: 104, message: "Validation failed", field: "positionId", description: "position doesn't exist." },
    { code: 105, message: "Validation failed", field: "takeProfit", description: "Wrong activation price for take profit." },
    { code: 106, message: "Validation failed", field: "stopLoss", description: "Wrong activation price for stop loss." },
    { code: 111, message: "Validation failed", field: "amount", description: "margin position too big" },
    { code: 112, message: "Validation failed", field: "amount", description: "margin pending orders value too big" },
    { code: 113, message: "Validation failed", field: "hedgeMode", description: "Position side cannot be changed if there exists futures positions or orders" },
    { code: 114, message: "Validation failed", field: "hedgeMode", description: "Order's position side does not match user's setting" },
    { code: 115, message: "Validation failed", field: "hedgeMode", description: "Order would result in a new position in the opposite direction" },
    { code: 150, message: "Validation failed", field: "price", description: "Can't place limit order." },
    { code: 151, message: "Validation failed", field: "activation_price", description: "Wrong activation price for stop loss." },
    { code: 152, message: "Validation failed", field: "error", description: "Max. limit of margin stop limit orders have been reached." },
    { code: 153, message: "Validation failed", field: "price", description: "Not enough balance for limit order." },
    { code: 155, message: "Validation failed", field: "orderId", description: "Can't modify conditional order." },
    { code: 157, message: "Validation failed", field: "amount", description: "Wrong order deal size." },
    { code: 158, message: "Validation failed", field: "activation_price", description: "Activation price can't be set for a limit order." },
    { code: 159, message: "Validation failed", field: "price", description: "Limit price can't be set for stop market order." },
    { code: 160, message: "Validation failed", field: "orderId", description: "tpsl orders can't be modified." },
    { code: 161, message: "Validation failed", field: "price", description: "Wrong order conditions" },
    { code: 162, message: "Validation failed", field: "total", description: "Total cannot be specified for this order type" },
    { code: 163, message: "Validation failed", field: "amount", description: "Amount cannot be specified for this order type" },
    { code: 250, message: "Validation failed", field: "price", description: "The Price is out of bands" },
    { code: 251, message: "Validation failed", field: "stopLimitPrice", description: "The Price is out of bands" },
    { code: 300, message: "Validation failed", field: "request", description: "fee not found" },
    { code: 302, message: "Validation failed", field: "amount", description: "margin balance update magnitude limit exceeded" },
    { code: 330, message: "Validation failed", field: "request", description: "fee not found" }
  ]}
  title="Modify Order Error Codes"
/>

## Collateral

### Collateral Account Balance

<ApiEndpoint method="POST" path="/api/v4/collateral-account/balance" />

This endpoint returns a current [collateral balance](./../glossary.md#balance-collateral)

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters**

| Name   | Type   | Mandatory | Description                                                       |
| ------ | ------ | --------- | ----------------------------------------------------------------- |
| ticker | String | **No**    | [Asset](./../glossary.md#assets) to be filtered. For example: BTC |

**Request BODY raw:**

```json
{
  "ticker": "BTC",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "BTC": 1,
  "USDT": 1000
}
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "ticker": ["ticker is invalid."]
  }
}
```

</details>

### Collateral Account Balance Summary

<ApiEndpoint method="POST" path="/api/v4/collateral-account/balance-summary" />

This endpoint returns a current [collateral balance](./../glossary.md#balance-collateral) summary

**Parameters**

| Name   | Type   | Mandatory | Description                                 |
| ------ | ------ | --------- | ------------------------------------------- |
| ticker | String | **No**    | Filter by requested asset. For example: BTC |

**Request BODY raw:**

```json
{
  "ticker": "BTC",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
[
  {
    "asset": "BTC",
    "balance": "0",
    "borrow": "0",
    "availableWithoutBorrow": "0",
    "availableWithBorrow": "123.456"
  }
]
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "ticker": ["ticker is invalid."]
  }
}
```

</details>

### Collateral Limit Order

<ApiEndpoint method="POST" path="/api/v4/order/collateral/limit" />

This endpoint creates [limit order](./../glossary.md#limit-order) using [collateral balance](./../glossary.md#balance-collateral)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name          | Type    | Mandatory                        | Description                                                                                                                                                                                                                                                                                       |
| ------------- | ------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market        | String  | **Yes**                          | Available margin market. Example: BTC_USDT                                                                                                                                                                                                                                                        |
| side          | String  | **Yes**                          | Order type. Variables: 'buy' / 'sell' Example: 'buy'. For open long position you have to use **buy**, for short **sell**. Also to close current position you have to place opposite [order](./../glossary.md#orders) with current position amount.                                                |
| amount        | String  | **Yes**                          | ⚠️️Amount of [**`stock`**](./../glossary.md#stock) currency to **buy** or **sell**.                                                                                                                                                                                                               |
| price         | String  | **Yes**                          | Price in [money](./../glossary.md#money) currency. Example: '9800'                                                                                                                                                                                                                                |
| clientOrderId | String  | **No**                           | Identifier should be unique and contain letters, dashes, numbers, dots or underscores. The identifier must be unique.                                                                                                                                                                             |
| stopLoss      | String  | **No**                           | Stop loss price, if exist create [OTO](./../glossary.md#OTO) with stop loss                                                                                                                                                                                                                       |
| takeProfit    | String  | **No**                           | Take profit price, if exist create [OTO](./../glossary.md#OTO) with take profit                                                                                                                                                                                                                   |
| postOnly      | boolean | **No**                           | Orders are guaranteed to be the [maker](./../glossary.md#maker) order when [executed](./../glossary.md#finished-orders). Variables: true / false Example: false.                                                                                                                                  |
| ioc           | boolean | **No**                           | An immediate or cancel order (IOC) is an order that attempts to execute all or part immediately and then cancels any unfilled portion of the order. Variables: 'true' / 'false' Example: 'false'.                                                                                                 |
| bboRole       | Integer | **No**                           | When you activate the [BBO](./../glossary.md#bbo) option when placing Limit orders, the system automatically selects the best market prices for executing these orders in one of two ways. Variables: 1 - Queue Method / 2 - Counterparty Method. You can use 2 method with ioc flag. Example: 1. |
| stp           | String  | **No**                           | Self trade prevention mode. Variables: 'no / 'cancel_both' / 'cancel_new' /'cancel_old'. Example: 'no'.                                                                                                                                                                                           |
| positionSide  | String  | **Yes, when hedge mode enabled** | Defines the position direction. Variables: 'LONG / 'SHORT' / 'BOTH'. Example: 'BOTH'. See [positionSide](./../glossary.md#position-side)                                                                                                                                                          |
| rpi           | boolean | **No**                           | Retail Price Improvement(RPI) order: Order type designed to offer better prices to retail users. It is post-only and can match only with orders from the Web or Mobile App. RPI orders can be placed only by the designated Market Makers. Example: true                                          |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "side": "buy",
  "amount": "0.01",
  "price": "40000",
  "postOnly": false,
  "ioc": false,
  "clientOrderId": "order1987111",
  "stopLoss": "50000",
  "takeProfit": "30000",
  "positionSide": "LONG",
  "rpi": true,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "orderId": 4180284841, // order id
  "clientOrderId": "order1987111", // custom client order id; "clientOrderId": "" - if not specified.
  "market": "BTC_USDT", // deal market
  "side": "buy", // order side
  "type": "limit", // order type
  "timestamp": 1595792396.165973, // timestamp of order creation
  "dealMoney": "0", // if order finished - amount in money currency that is finished
  "dealStock": "0", // if order finished - amount in stock currency that is finished
  "amount": "0.01", // amount
  "left": "0.001", // if order not finished - rest of the amount that must be finished
  "dealFee": "0", // fee in money that you pay if order is finished
  "price": "40000", // price
  "postOnly": false, // PostOnly
  "ioc": false, // IOC
  "status": "FILLED", // order status
  "stp": "no", // self trade prevention mode
  "oto": {
    // OTO order data - if stopLoss or takeProfit is specified
    "otoId": 29457221, // ID of the OTO
    "stopLoss": "30000", // stop loss order price - if stopLoss is specified
    "takeProfit": "50000" // take profit order price - if takeProfit is specified
  },
  "positionSide": "LONG", // position side - LONG or SHORT or BOTH
  "rpi": true // RPI order flag
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `31` - market is disabled for trading
- `32` - incorrect amount (it is less than or equals zero or its precision is too big)
- `33` - incorrect price (it is less than or equals zero or its precision is too big)
- `36` - incorrect clientOrderId (invalid string or not unique id)
- `37` - ioc and postOnly flags are both true

---

</details>

Detailed information about errors response you can find in [Create limit order](#create-limit-order)

---

### Collateral bulk limit order

<ApiEndpoint method="POST" path="/api/v4/order/collateral/bulk" />

This endpoint creates bulk collateral [limit trading orders](./../glossary.md#limit-order).

❗Limit - From 1 to 20 orders by request.

**Parameters:**

| Name   | Type  | Mandatory | Description                                  |
| ------ | ----- | --------- | -------------------------------------------- |
| orders | Array | **Yes**   | Array of [limit orders](#create-limit-order) |

**Request BODY raw:**

```json
{
  "orders": [
    {
      "side": "buy",
      "amount": "0.02",
      "price": "40000",
      "market": "BTC_PERP",
      "postOnly": false,
      "ioc": false,
      "clientOrderId": "",
      "positionSide": "LONG",
      "rpi": true
    },
    {
      "side": "sell",
      "amount": "0.0001",
      "price": "41000",
      "postOnly": false,
      "market": "BTC_USDT",
      "ioc": false,
      "clientOrderId": "",
      "positionSide": "LONG",
      "rpi": true
    },
    {
      "side": "sell",
      "amount": "0.02",
      "price": "0.030",
      "postOnly": false,
      "market": "ETH_BTC",
      "ioc": false,
      "clientOrderId": "",
      "positionSide": "LONG",
      "rpi": true
    }
  ],
  "stopOnFail": true,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if request validation failed`
- `Status 503 if service temporary unavailable`

```json
[
  {
    "result": {
      "orderId": 4326248250, // order id
      "clientOrderId": "", // custom client order id; "clientOrderId": "" - if not specified.
      "market": "BTC_USDT", // deal market
      "side": "buy", // order side
      "type": "limit", // order type
      "timestamp": 1684916268.825564, // timestamp of order creation
      "dealMoney": "641.988", // if order finished - amount in money currency that is finished
      "dealStock": "0.02", // if order finished - amount in stock currency that is finished
      "amount": "0.02", // amount
      "left": "0", // if order not finished - rest of the amount that must be finished
      "dealFee": "1.283976", // fee in money that you pay if order is finished
      "ioc": false, // IOC
      "postOnly": false, // PostOnly
      "price": "40000", // price
      "status": "FILLED", // order status
      "stp": "no", // self trade prevention mode
      "positionSide": "LONG", // position side - LONG or SHORT or BOTH
      "rpi": true // RPI order flag
    },
    "error": null
  },
  {
    "result": null,
    "error": {
      "code": 32,
      "message": "Validation failed",
      "errors": {
        "amount": ["Given amount is less than min amount 0.001."]
      }
    }
  },
  {
    "result": {
      "orderId": 4326248250,
      "clientOrderId": "",
      "market": "BTC_USDT",
      "side": "sell",
      "type": "limit",
      "timestamp": 1684916268.825564,
      "dealMoney": "641.988",
      "dealStock": "0.02",
      "amount": "0.02",
      "left": "0",
      "dealFee": "1.283976",
      "ioc": false,
      "postOnly": false,
      "price": "41000",
      "status": "FILLED", // order status
      "stp": "no", // self trade prevention mode
      "positionSide": "LONG", // position side - LONG or SHORT or BOTH
      "rpi": true // RPI order flag
    },
    "error": null
  }
]
```

<details>

<summary>
  <b>Errors:</b>
</summary>

Error codes:

- `30` - default validation error code

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "orders": ["The orders must be an array."]
  }
}
```

<summary>
  <b>Errors in multiply response:</b>
</summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed
- `32` - amount validation failed
- `33` - price validation failed
- `36` - clientOrderId validation failed
- `37` - ioc and postOnly flags are both true

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field is required."],
    "market": ["Market field is required."],
    "price": ["Price field is required."],
    "side": ["Side field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "side": ["Side field should contain only 'buy' or 'sell' values."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field should be numeric string or number."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be numeric string or number."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Given amount is less than min amount 0.001",
      "Min amount step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": ["ClientOrderId field should be a string."]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "ClientOrderId field field should contain only latin letters, numbers and dashes."
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "This client order id is already used by the current account."
    ]
  }
}
```

```json
{
  "code": 37,
  "message": "Validation failed",
  "errors": {
    "ioc": ["Either IOC or PostOnly flag in true state is allowed."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "total": ["Total(amount * price) is less than 5.05"]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Min amount step = 0.01" // money/stock precision is not taken into consideration when order was submitted
    ]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be at least 10", "Min price step = 0.000001"]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price should be greater than 0."]
  }
}
```

```json
{
  "code": 35,
  "message": "Validation failed",
  "errors": {
    "maker_fee": ["Incorrect maker fee"]
  }
}
```

```json
{
  "code": 10,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 11,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Amount too small."]
  }
}
```

```json
{
  "code": 13,
  "message": "Inner validation failed",
  "errors": {
    "postOnly": [
      "This order couldn't be executed as a maker order and was canceled."
    ]
  }
}
```

</details>

---

### Collateral Market Order

<ApiEndpoint method="POST" path="/api/v4/order/collateral/market" />

This endpoint creates [market trading order](./../glossary.md#market-order).

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name          | Type   | Mandatory                        | Description                                                                                                                                                                                                                                        |
| ------------- | ------ | -------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market        | String | **Yes**                          | Available margin market. Example: BTC_USDT                                                                                                                                                                                                         |
| side          | String | **Yes**                          | Order type. Variables: 'buy' / 'sell' Example: 'buy'. For open long position you have to use **buy**, for short **sell**. Also to close current position you have to place opposite [order](./../glossary.md#orders) with current position amount. |
| amount        | String | **Yes**                          | ⚠️️Amount of [**`stock`**](./../glossary.md#stock) currency to **buy** or **sell**.                                                                                                                                                                |
| clientOrderId | String | **No**                           | Identifier should be unique and contain letters, dashes, numbers, dots or underscores. The identifier must be unique.                                                                                                                              |
| stopLoss      | String | **No**                           | Stop loss price, if exist create [OTO](./../glossary.md#OTO) with stop loss                                                                                                                                                                        |
| takeProfit    | String | **No**                           | Take profit price, if exist create [OTO](./../glossary.md#OTO) with take profit                                                                                                                                                                    |
| stp           | String | **No**                           | Self trade prevention mode. Variables: 'no / 'cancel_both' / 'cancel_new' /'cancel_old'. Example: 'no'.                                                                                                                                            |
| positionSide  | String | **Yes, when hedge mode enabled** | Defines the position direction. Variables: 'LONG / 'SHORT' / 'BOTH'. Example: 'BOTH'. See [positionSide](./../glossary.md#position-side)                                                                                                           |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "side": "buy",
  "amount": "0.01", // I want to buy 0.01 BTC
  "clientOrderId": "order1987111",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

```json
{
  "market": "BTC_PERP",
  "side": "sell",
  "amount": "0.01", // I want to sell 0.01 BTC
  "clientOrderId": "order1987111",
  "stopLoss": "50000",
  "takeProfit": "40000",
  "positionSide": "LONG",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if internal validation failed`
- `Status 503 if service is temporary unavailable`

```json
{
  "orderId": 4180284841, // order id
  "clientOrderId": "order1987111", // custom client order id; "clientOrderId": "" - if not specified.
  "market": "BTC_USDT", // deal market
  "side": "sell", // order side
  "type": "market", // order type
  "timestamp": 1595792396.165973, // timestamp of order creation
  "dealMoney": "0", // amount in money currency that finished
  "dealStock": "0", // amount in stock currency that finished
  "amount": "0.001", // amount
  "left": "0.001", // rest of amount that must be finished
  "dealFee": "0", // fee in money that you pay if order is finished
  "status": "FILLED", // order status
  "stp": "no", // self trade prevention mode
  "oto": {
    // OTO order data - if stopLoss or takeProfit is specified
    "otoId": 29457221, // ID of the OTO
    "stopLoss": "50000", // stop loss order price - if stopLoss is specified
    "takeProfit": "40000" // take profit order price - if takeProfit is specified
  },
  "positionSide": "LONG" // position side - LONG or SHORT or BOTH
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `31` - market is disabled for trading
- `32` - incorrect amount (it is less than or equals zero or its precision is too big)
- `33` - incorrect price (it is less than or equals zero or its precision is too big)
- `36` - incorrect clientOrderId (invalid string or not unique id)

</details>

Detailed information about errors response you can find in [Create market order](#create-market-order)

---

---

### Collateral Stop-Limit Order

<ApiEndpoint method="POST" path="/api/v4/order/collateral/stop-limit" />

This endpoint creates collateral [stop-limit trading order](./../glossary.md#stop-limit-order)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name             | Type          | Mandatory                        | Description                                                                                                                                                                                                                                                                                       |
| ---------------- | ------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market           | String        | **Yes**                          | Available [market](./../glossary.md#market). Example: BTC_USDT                                                                                                                                                                                                                                    |
| side             | String        | **Yes**                          | Order type. Variables: 'buy' / 'sell' Example: 'buy'                                                                                                                                                                                                                                              |
| amount           | String/Number | **Yes**                          | Amount of [stock](./../glossary.md#stock) currency to buy or sell. Example: '0.001' or 0.001                                                                                                                                                                                                      |
| price            | String/Number | **Yes**                          | Price in [money](./../glossary.md#money) currency. Example: '9800' or 9800                                                                                                                                                                                                                        |
| activation_price | String/Number | **Yes**                          | Activation price in [money](./../glossary.md#money) currency. Example: '10000' or 10000                                                                                                                                                                                                           |
| clientOrderId    | String        | **No**                           | Identifier should be unique and contain letters, dashes, numbers, dots or underscores. The identifier must be unique.                                                                                                                                                                             |
| stopLoss         | String/Number | **No**                           | Stop loss price, if exist create [OTO](./../glossary.md#OTO) with stop loss                                                                                                                                                                                                                       |
| takeProfit       | String/Number | **No**                           | Take profit price, if exist create [OTO](./../glossary.md#OTO) with take profit                                                                                                                                                                                                                   |
| bboRole          | Integer       | **No**                           | When you activate the [BBO](./../glossary.md#bbo) option when placing Limit orders, the system automatically selects the best market prices for executing these orders in one of two ways. Variables: 1 - Queue Method / 2 - Counterparty Method.                                                 |
| stp              | String        | **No**                           | Self trade prevention mode. Variables: 'no / 'cancel_both' / 'cancel_new' /'cancel_old'. Example: 'no'.                                                                                                                                                                                           |
| positionSide     | String        | **Yes, when hedge mode enabled** | Defines the position direction. Variables: 'LONG / 'SHORT' / 'BOTH'. Example: 'BOTH'. See [positionSide](./../glossary.md#position-side)                                                                                                                                                          |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "side": "buy",
  "amount": "0.001",
  "price": "40000",
  "activation_price": "40000",
  "stopLoss": "30000",
  "takeProfit": "50000",
  "clientOrderId": "order1987111",
  "positionSide": "LONG",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if request validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "orderId": 4180284841, // order id
  "clientOrderId": "order1987111", // custom client order id; "clientOrderId": "" - if not specified.
  "market": "BTC_USDT", // deal market
  "side": "buy", // order side
  "type": "stop limit", // order type
  "timestamp": 1595792396.165973, // timestamp of order creation
  "dealMoney": "0", // if order finished - amount in money currency that finished
  "dealStock": "0", // if order finished - amount in stock currency that finished
  "amount": "0.001", // amount
  "left": "0.001", // if order not finished - rest of amount that must be finished
  "dealFee": "0", // fee in money that you pay if order is finished
  "price": "40000", // price
  "activation_price": "40000", // activation price
  "status": "FILLED", // order status
  "stp": "no", // self trade prevention mode
  "oto": {
    // OTO order data - if stopLoss or takeProfit is specified
    "otoId": 29457221, // ID of the OTO
    "stopLoss": "30000", // stop loss order price - if stopLoss is specified
    "takeProfit": "50000" // take profit order price - if takeProfit is specified
  },
  "positionSide": "LONG" // position side - LONG or SHORT or BOTH
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed
- `32` - amount validation failed
- `33` - price validation failed
- `36` - clientOrderId validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Activation price field is required."],
    "amount": ["Amount field is required."],
    "market": ["Market field is required."],
    "price": ["Price field is required."],
    "side": ["Side field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "side": ["Side field should contain only 'buy' or 'sell' values."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field should be numeric string or number."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be numeric string or number."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Given amount is less than min amount 0.001",
      "Min amount step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "total": ["Total(amount * price) is less than 5.05"]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": ["ClientOrderId field should be a string."]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "ClientOrderId field field should contain only latin letters, numbers and dashes."
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "This client order id is already used by the current account."
    ]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount should be greater than 0."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be at least 10", "Min price step = 0.000001"]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price should be greater than 0."]
  }
}
```

```json
{
  "code": 35,
  "message": "Validation failed",
  "errors": {
    "maker_fee": ["Incorrect maker fee"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": [
      "Activation price should not be equal to the last price"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Activation price should be numeric string."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Activation price should be greater than 0."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Empty history"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Min activation price = 10"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Min activation price step = 0.00001"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": [
      "Activation price should not be equal to the last price"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "lastPrice": ["internal error"]
  }
}
```

```json
{
  "code": 10,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 11,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Amount too small."]
  }
}
```

</details>

---

### Collateral Trigger Market Order

<ApiEndpoint method="POST" path="/api/v4/order/collateral/trigger-market" />

This endpoint creates margin trigger [market order](./../glossary.md#market-order)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name             | Type   | Mandatory                        | Description                                                                                                                                                                                                             |
| ---------------- | ------ | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market           | String | **Yes**                          | Available margin market. Example: BTC_USDT                                                                                                                                                                              |
| side             | String | **Yes**                          | Order type. Variables: 'buy' / 'sell' Example: 'buy'. For open long position you have to use **buy**, for short **sell**. Also to close current position you have to place opposite order with current position amount. |
| amount           | String | **Yes**                          | ⚠️️Amount of [**`stock`**](./../glossary.md#stock) currency to **buy** or **sell**.                                                                                                                                     |
| activation_price | String | **Yes**                          | Activation price in [money](./../glossary.md#money) currency. Example: '10000'                                                                                                                                          |
| clientOrderId    | String | **No**                           | Identifier should be unique and contain letters, dashes, numbers, dots or underscores. The identifier must be unique.                                                                                                   |
| stopLoss         | String | **No**                           | Stop loss price, if exist create [OTO](./../glossary.md#OTO) with stop loss                                                                                                                                             |
| takeProfit       | String | **No**                           | Take profit price, if exist create [OTO](./../glossary.md#OTO) with take profit                                                                                                                                         |
| stp              | String | **No**                           | Self trade prevention mode. Variables: 'no / 'cancel_both' / 'cancel_new' /'cancel_old'. Example: 'no'.                                                                                                                 |
| positionSide     | String | **Yes, when hedge mode enabled** | Defines the position direction. Variables: 'LONG / 'SHORT' / 'BOTH'. Example: 'BOTH'. See [positionSide](./../glossary.md#position-side)                                                                                |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "side": "buy",
  "amount": "0.01", // I want to buy 0.01 BTC
  "activation_price": "40000",
  "clientOrderId": "order1987111",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

```json
{
  "market": "BTC_PERP",
  "side": "sell",
  "amount": "0.01", // I want to sell 0.01 BTC
  "activation_price": "40000",
  "stopLoss": "50000",
  "takeProfit": "30000",
  "positionSide": "LONG",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "orderId": 4180284841, // order id
  "clientOrderId": "order1987111", // custom order identifier; "clientOrderId": "" - if not specified.
  "market": "BTC_USDT", // deal market
  "side": "sell", // order side
  "type": "stop market", // order type
  "timestamp": 1595792396.165973, // timestamp of order creation
  "dealMoney": "0", // if order finished - amount in money currency that finished
  "dealStock": "0", // if order finished - amount in stock currency that finished
  "amount": "0.001", // amount
  "left": "0.001", // if order not finished - rest of amount that must be finished
  "dealFee": "0", // fee in money that you pay if order is finished
  "activation_price": "40000", // activation price
  "status": "FILLED", // order status
  "stp": "no", // self trade prevention mode
  "oto": {
    // OTO order data - if stopLoss or takeProfit is specified
    "otoId": 29457221, // ID of the OTO
    "stopLoss": "50000", // stop loss order price - if stopLoss is specified
    "takeProfit": "30000" // take profit order price - if takeProfit is specified
  },
  "positionSide": "LONG" // position side - LONG or SHORT or BOTH
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `31` - market is disabled for trading
- `32` - incorrect amount (it is less than or equals zero or its precision is too big)
- `33` - incorrect price (it is less than or equals zero or its precision is too big)
- `36` - incorrect clientOrderId (invalid string or not unique id)

</details>

---

### Collateral Account Summary

<ApiEndpoint method="POST" path="/api/v4/collateral-account/summary" />

This endpoint retrieves summary of [collateral](./../glossary.md#collateral) account

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**Request BODY raw:**

```json
{
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 503 if service temporary unavailable`

```json
{
  "equity": "9817.676478608323", // total equity of collateral balance including lending funds in USDT
  "margin": "3880.64387", // amount of funds in open position USDT
  "freeMargin": "10739.489348608323", // free funds for trading
  "unrealizedFunding": "0", // funding that will be paid on next position stage change (order, liquidation, etc)
  "pnl": "4802.45674", // current profit and loss in USDT
  "leverage": 100, // current leverage of account which affect amount of lending funds
  "marginFraction": "0.0497228995828862", // margin fraction (Note: value of 1000000000000000000000 indicates no positions)
  "maintenanceMarginFraction": "0.0065990118926067", // maintenance margin fraction
  "futuresEquity": "9817.676478608323", // equity value for futures positions in USDT
  "futuresFreeMargin": "10739.489348608323" // free margin available for futures in USDT
}
```

---

### Open Positions

<ApiEndpoint method="POST" path="/api/v4/collateral-account/positions/open" />

This endpoint returns all open positions

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name   | Type   | Mandatory | Description                                                    |
| ------ | ------ | --------- | -------------------------------------------------------------- |
| market | String | **No**    | Requested [market](./../glossary.md#market). Example: BTC_USDT |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
[
  {
    "positionId": 527, // position ID
    "market": "BTC_USDT", // market name
    "openDate": 1651568067.789679, // date of position opening
    "modifyDate": 1651568067.789679, // date of position modifying (this is date of current event)
    "amount": "0.1", // amount of order
    "basePrice": "45658.349", // base price of position
    "liquidationPrice": null, // liquidation price according to current state of position
    "liquidationState": null, // state of liquidation. Possible values: null, margin_call, liquidation
    "pnl": "-168.42", // unrealized profit and loss in money
    "pnlPercent": "-0.43", // unrealized profit and loss in percentage
    "margin": "8316.74", // amount of funds in open position money
    "freeMargin": "619385.67", // free funds for trading
    "funding": "0", // funding that will be paid on next position stage change (order, liquidation, etc)
    "unrealizedFunding": "0.0019142920201966", // funding that will be paid on next position stage change (order, liquidation, etc)
    "tpsl": {
      "takeProfitId": 123, // take profit order ID
      "takeProfit": "50000", // take profit price
      "stopLossId": 124, // stop loss order ID
      "stopLoss": "35000" // stop loss price
    },
    "positionSide": "LONG" // position side - LONG or SHORT or BOTH
  },
  {
    "positionId": 528, // position ID
    "market": "ETH_USDT", // market name
    "openDate": 1651568067.789679, // date of position opening
    "modifyDate": 1651568067.789679, // date of position modifying (this is date of current event)
    "amount": "0.1", // amount of order
    "basePrice": "5658.349", // base price of position
    "liquidationPrice": null, // liquidation price according to current state of position
    "liquidationState": null, // state of liquidation. Possible values: null, margin_call, liquidation
    "pnl": "-168.42", // unrealized profit and loss in money
    "pnlPercent": "-0.43", // unrealized profit and loss in percentage
    "margin": "8316.74", // amount of funds in open position money
    "freeMargin": "19385.67", // free funds for trading
    "funding": "0", // funding that will be paid on next position stage change (order, liquidation, etc)
    "unrealizedFunding": "0.0020142920201966", // funding that will be paid on next position stage change (order, liquidation, etc)
    "tpsl": null,
    "positionSide": "LONG" // position side - LONG or SHORT or BOTH
  }
]
```

- NOTE: In case of position opening using trigger or [limit order](./../glossary.md#limit-order) you can get situation when `basePrice`, `liquidationPrice`, `amount`, `pnl`, `pnlPercent` returns with null value. It happens when funds are lending, and you start to pay funding [fee](./../glossary.md#fee), but position is not completely opened, cos activation price hadn't been triggered yet.
- NOTE: In case of position have take profit or stop loss, you will get `tpsl` object with `takeProfitId`, `takeProfit`, `stopLossId`, `stopLoss` fields else you will get `tpsl` object with `null` value.

---

### Close Position

<ApiEndpoint method="POST" path="/api/v4/collateral-account/position/close" />

This endpoint closes specific position by `positionId` and by `market`.

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name         | Type   | Mandatory | Description                                                                                                                                                        |
| ------------ | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| positionId   | Int    | **Yes**   | Requested position                                                                                                                                                 |
| market       | String | **Yes**   | Requested [market](./../glossary.md#market). Example: BTC_USDT                                                                                                     |
| positionSide | String | **No**    | Defines the position direction when hedge mode is enabled. Variables: 'LONG / 'SHORT' / 'BOTH'. Example: 'BOTH'. See [positionSide](./../glossary.md#PositionSide) |

**Request BODY raw:**

```json
{
  "positionId": 123,
  "positionSide": "LONG",
  "market": "BTC_USDT",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if request validation failed`
- `Status 500 if internal error`
- `Status 503 if service temporary unavailable`

```json
[]
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["The market field is required."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should be a string."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field format is invalid."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "message": "Validation failed",
  "code": 31,
  "errors": {
    "market": ["Market is not available"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "positionId": ["The PositionId must be an integer."]
  }
}
```

```json
{
  "code": 113,
  "message": "Validation failed",
  "errors": {
    "hedgeMode": [
      "Position side cannot be changed if there exists futures positions or orders"
    ]
  }
}
```

```json
{
  "code": 114,
  "message": "Validation failed",
  "errors": {
    "hedgeMode": ["Order's position side does not match user's setting"]
  }
}
```

```json
{
  "code": 115,
  "message": "Validation failed",
  "errors": {
    "hedgeMode": [
      "Order would result in a new position in the opposite direction"
    ]
  }
}
```

</details>

---

### Positions History

<ApiEndpoint
  method="POST"
  path="/api/v4/collateral-account/positions/history"
/>

This endpoint returns past positions history. Each position represented by position states. Each of them means event that shows current position changes such [order](./../glossary.md#orders), position close, liquidation, etc.

If your request has a "positionId" field, you receive data only with this "positionId".
If your request has a "market" field, you receive data only by this "[market](./../glossary.md#market)".

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**"positionId" field has higher priority then "market" field.**

**Parameters:**

| Name       | Type   | Mandatory | Description                                                                                                                                                           |
| ---------- | ------ | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market     | String | **No**    | Requested [market](./../glossary.md#market). Example: BTC_USDT                                                                                                        |
| positionId | Int    | **No**    | Requested position                                                                                                                                                    |
| startDate  | Int    | **No**    | Start date in Unix-time format                                                                                                                                        |
| endDate    | Int    | **No**    | End date in Unix-time format                                                                                                                                          |
| limit      | Int    | **No**    | LIMIT is a special clause used to limit records a particular query can return. Default: 50, Min: 1, Max: 100                                                          |
| offset     | Int    | **No**    | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. Default: 0, Min: 0 |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT", //optional
  "positionId": 1, //optional
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
[
  {
    "positionId": 111, // position ID
    "market": "BTC_USDT", // position market
    "openDate": 1650400589.882613, // date of position opening
    "modifyDate": 1650400589.882613, // date of position modifying (this is date of current event)
    "amount": "0.1", // amount of order
    "basePrice": "45658.349", // base price of position
    "realizedFunding": "0", // funding fee for whole position lifetime till current state
    "liquidationPrice": null, // liquidation price according to current state of position
    "liquidationState": null, // state of liquidation. Possible values: null, margin_call, liquidation
    "orderDetail": {
      // details of order which changes position
      "id": 97067934, // order ID
      "tradeAmount": "0.1", // trade amount of order
      "price": "41507.59", // order's price
      "tradeFee": "415.07", // order's trade fee
      "fundingFee": null, // funding fee which was captured by this position change (order)
      "realizedPnl": null // realized pnl
    },
    "positionSide": "LONG" // position side - LONG or SHORT or BOTH
  }
]
```

---

### Funding History

<ApiEndpoint method="POST" path="/api/v4/collateral-account/funding-history" />

Retrieves the history of realized funding payments for an account.

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name      | Type   | Mandatory | Description                                                                                                                                       |
| --------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| market    | String | **Yes**   | Requested futures [market](./../glossary.md#market). Example: BTC_PERP                                                                            |
| startDate | Int    | **No**    | Start date in Unix-time format                                                                                                                    |
| endDate   | Int    | **No**    | End date in Unix-time format                                                                                                                      |
| limit     | Int    | **No**    | LIMIT is a special clause used to limit records a particular query can return. Default: 100, Min: 1, Max: 100                                     |
| offset    | Int    | **No**    | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. Default: 0 |

**Request BODY raw:**

```json
{
  "market": "BTC_PERP",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "records": [
    {
      "market": "BTC_PERP", // market name
      "fundingTime": "1734451200", // funding time
      "fundingRate": "0.00017674", // funding rate
      "fundingAmount": "-0.171053531892", // funding amount
      "positionAmount": "0.019", // position amount
      "settlementPrice": "50938.2", // settlement price
      "rateCalculatedTime": "1734364800" // rate calculated time
    },
    {
      "market": "BTC_PERP",
      "fundingTime": "1734451200",
      "fundingRate": "-0.000177877800093587",
      "fundingAmount": "-0.0054997859133136",
      "positionAmount": "-0.001",
      "settlementPrice": "30918.9",
      "rateCalculatedTime": "1734364800"
    }
  ],
  "limit": 100,
  "offset": 0
}
```

---

### Change Collateral Account Leverage

<ApiEndpoint method="POST" path="/api/v4/collateral-account/leverage" />

This endpoint changes the current leverage of account.

**Please note**: Leverages of 50x and 100x are applicable only for futures trading. When applied to margin trading, the maximum leverage applied will be 20x. The leverage value is applied to the entire account, so if you choose a new leverage value below 50x, it will be applied to both margin and futures trading.
Additionally, we would like to draw your attention to the fact that calculations for futures positions with 50x and 100x leverage are done considering brackets (see endpoint [futures](./../public/http-v4.md#available-futures-markets-list)). You can familiarize yourself with the bracket mechanics for 50x and 100x leverage on the Trading Rules page.

❗ Rate limit 12000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name     | Type | Mandatory | Description                                                                                                          |
| -------- | ---- | --------- | -------------------------------------------------------------------------------------------------------------------- |
| leverage | Int  | **Yes**   | New [collateral](./../glossary.md#collateral) account leverage value. Acceptable values: 1, 2, 3, 5, 10, 20, 50, 100 |

**Request BODY raw:**

```json
{
  "leverage": 5,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "leverage": 5 // current collateral balance leverage
}
```

---

### Collateral Account Hedge Mode

<ApiEndpoint method="POST" path="/api/v4/collateral-account/hedge-mode" />

This endpoint retrieves the current hedge mode status for a collateral account.

❗ Rate limit 1000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**
None required

**Request BODY raw:**

```json
{
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 500 if internal error`
- `Status 503 if service temporary unavailable`

```json
{
  "hedgeMode": true
}
```

---

### Update Collateral Account Hedge Mode

<ApiEndpoint
  method="POST"
  path="/api/v4/collateral-account/hedge-mode/update"
/>

This endpoint updates the hedge mode status for a collateral account. When hedge mode is enabled, you can hold both long and short positions on the same market simultaneously.

❗ Rate limit 1000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name      | Type    | Mandatory | Description                                              |
| --------- | ------- | --------- | -------------------------------------------------------- |
| hedgeMode | Boolean | **Yes**   | Set to `true` to enable or `false` to disable hedge mode |

**Request BODY raw:**

```json
{
  "hedgeMode": true
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 422 if inner validation failed`
- `Status 500 if internal error`
- `Status 503 if service temporary unavailable`

<details>
<summary><b>Errors:</b></summary>
```json
{
    "code": 113,
    "message": "Validation failed",
    "errors": {
        "hedgeMode": ["Position side cannot be changed if there exists futures positions or orders"],
    }
}
```
The response confirms the updated hedge mode status (`true` for enabled, `false` for disabled) for the collateral account.
</details>

---

### Query Active Conditional Orders

<ApiEndpoint method="POST" path="/api/v4/conditional-orders" />

This endpoint retrieves [active](./../glossary.md#active-orders) [conditional orders](./../glossary.md#conditional-orders) (orders not yet executed).

❗ Rate limit 1000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name   | Type       | Mandatory | Description                                                                                                                                                           |
| ------ | ---------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market | String     | **Yes**   | Available [market](./../glossary.md#market). Example: BTC_USDT                                                                                                        |
| limit  | String/Int | **No**    | LIMIT is a special clause used to limit records a particular query can return. Default: 50, Min: 1, Max: 100                                                          |
| offset | String/Int | **No**    | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. Default: 0, Min: 0 |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "offset": 0,
  "limit": 100,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 422 if request validation failed`
- `Status 400 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "limit": 100,
  "offset": 0,
  "total": 2,
  "records": [
    {
      "id": 117703764513, // conditional order id
      "type": "oco",
      "stop_loss": {
        "orderId": 117703764514, // unexecuted order ID
        "clientOrderId": "", // custom order id; "clientOrderId": "" - if not specified.
        "market": "BTC_USDT", // currency market
        "side": "buy", // order side
        "type": "stop limit", // unexecuted order type
        "timestamp": 1594605801.49815, // timestamp of order creation
        "dealMoney": "0", // executed amount in money
        "dealStock": "0", // executed amount in stock
        "amount": "2.241379", // active order amount
        "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - it will be rounded to zero
        "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - it will be rounded to zero
        "left": "2.241379", // unexecuted amount in stock
        "dealFee": "0", // executed fee by deal
        "post_only": false, // orders are guaranteed to be the maker order when executed.
        "mtime": 1662478154.941582, // timestamp of order modification
        "price": "19928.79", // unexecuted order price
        "activation_price": "29928.79", // activation price
        "activation_condition": "gte", // activation condition
        "activated": 0, // activation status
        "status": "FILLED", // order status
        "stp": "no", // self trade prevention mode
        "positionSide": "LONG" // position side - LONG or SHORT or BOTH
      },
      "take_profit": {
        "orderId": 117703764515, // unexecuted order ID
        "clientOrderId": "", // custom order id; "clientOrderId": "" - if not specified.
        "market": "BTC_USDT", // currency market
        "side": "buy", // order side
        "type": "limit", // unexecuted order type
        "timestamp": 1662478154.941582, // timestamp of order creation
        "dealMoney": "0", // executed amount in money
        "dealStock": "0", // executed amount in stock
        "amount": "0.635709", // active order amount
        "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - it will be rounded to zero
        "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - it will be rounded to zero
        "left": "0.635709", // unexecuted amount in stock
        "dealFee": "0", // executed fee by deal
        "post_only": false, // orders are guaranteed to be the maker order when executed.
        "mtime": 1662478154.941582, // timestamp of order modification
        "price": "9928.79", // unexecuted order price
        "status": "FILLED", // order status
        "stp": "no", // self trade prevention mode
        "positionSide": "LONG" // position side - LONG or SHORT or BOTH
      }
    },
    {
      "id": 29457221, // ID of the conditional
      "type": "oto", // type of the conditional
      "stopLossPrice": "30000", // stop loss order price - if stopLoss is specified
      "takeProfitPrice": "50000", // take profit order price - if takeProfit is specified
      // OTO order data - if stopLoss or takeProfit is specified
      "conditionalOrder": {
        "orderId": 3686033640, // unexecuted order ID
        "clientOrderId": "customId11", // custom order id; "clientOrderId": "" - if not specified.
        "market": "BTC_USDT", // currency market
        "side": "buy", // order side
        "type": "limit", // unexecuted order type
        "timestamp": 1594605801.49815, // timestamp of order creation
        "dealMoney": "0", // executed amount in money
        "dealStock": "0", // executed amount in stock
        "amount": "2.241379", // active order amount
        "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - it will be rounded to zero
        "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - it will be rounded to zero
        "left": "2.241379", // unexecuted amount in stock
        "dealFee": "0", // executed fee by deal
        "price": "40000", // unexecuted order price
        "status": "FILLED", // order status
        "stp": "no", // self trade prevention mode
        "positionSide": "LONG" // position side - LONG or SHORT or BOTH
      }
    }
  ]
}
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["The market field is required."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should be a string."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field format is invalid."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "message": "Validation failed",
  "code": 31,
  "errors": {
    "market": ["Market is not available"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["The limit must be an integer."],
    "offset": ["The offset must be an integer."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["The limit may not be greater than 100."],
    "offset": ["The offset may not be greater than 10000."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["The limit must be at least 1."],
    "offset": ["The offset must be at least 0."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

---

### Query Active OCO Orders

<ApiEndpoint method="POST" path="/api/v4/oco-orders" />

This endpoint retrieves [active](./../glossary.md#active-orders) [OCO orders](./../glossary.md#oco-orders) (orders not yet executed).

❗ Deprecated - use [/api/v4/conditional-orders](#query-active-conditional-orders) instead.
❗ Rate limit 1000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name   | Type       | Mandatory | Description                                                                                                                                                           |
| ------ | ---------- | --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| market | String     | **Yes**   | Available [market](./../glossary.md#market). Example: BTC_USDT                                                                                                        |
| limit  | String/Int | **No**    | LIMIT is a special clause used to limit records a particular query can return. Default: 50, Min: 1, Max: 100                                                          |
| offset | String/Int | **No**    | If you want the request to return entries starting from a particular line, you can use OFFSET clause to tell it where it should start. Default: 0, Min: 0 |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "offset": 0,
  "limit": 100,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 422 if request validation failed`
- `Status 400 if inner validation failed`
- `Status 503 if service temporary unavailable`

```json
[
  {
    "id": 117703764513, // oco order id
    "stop_loss": {
      "orderId": 117703764514, // unexecuted order ID
      "clientOrderId": "", // custom order id; "clientOrderId": "" - if not specified.
      "market": "BTC_USDT", // currency market
      "side": "buy", // order side
      "type": "stop limit", // unexecuted order type
      "timestamp": 1594605801.49815, // timestamp of order creation
      "dealMoney": "0", // executed amount in money
      "dealStock": "0", // executed amount in stock
      "amount": "2.241379", // active order amount
      "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - it will be rounded to zero
      "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - it will be rounded to zero
      "left": "2.241379", // unexecuted amount in stock
      "dealFee": "0", // executed fee by deal
      "post_only": false, // orders are guaranteed to be the maker order when executed.
      "mtime": 1662478154.941582, // timestamp of order modification
      "price": "19928.79", // unexecuted order price
      "activation_price": "29928.79", // activation price
      "activation_condition": "gte", // activation condition
      "activated": 0, // activation status
      "status": "FILLED", // order status
      "stp": "no" // self trade prevention mode
    },
    "take_profit": {
      "orderId": 117703764515, // unexecuted order ID
      "clientOrderId": "", // custom order id; "clientOrderId": "" - if not specified.
      "market": "BTC_USDT", // currency market
      "side": "buy", // order side
      "type": "limit", // unexecuted order type
      "timestamp": 1662478154.941582, // timestamp of order creation
      "dealMoney": "0", // executed amount in money
      "dealStock": "0", // executed amount in stock
      "amount": "0.635709", // active order amount
      "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - it will be rounded to zero
      "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - it will be rounded to zero
      "left": "0.635709", // unexecuted amount in stock
      "dealFee": "0", // executed fee by deal
      "post_only": false, // orders are guaranteed to be the maker order when executed.
      "mtime": 1662478154.941582, // timestamp of order modification
      "price": "9928.79", // unexecuted order price
      "status": "FILLED", // order status
      "stp": "no" // self trade prevention mode
    }
  }
]
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["The market field is required."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should be a string."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field format is invalid."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "message": "Validation failed",
  "code": 31,
  "errors": {
    "market": ["Market is not available"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["The limit must be an integer."],
    "offset": ["The offset must be an integer."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["The limit may not be greater than 100."],
    "offset": ["The offset may not be greater than 10000."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "limit": ["The limit must be at least 1."],
    "offset": ["The offset must be at least 0."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

---

### Create collateral OCO order

<ApiEndpoint method="POST" path="/api/v4/order/collateral/oco" />

This endpoint creates [collateral](./../glossary.md#collateral) trading [OCO order](./../glossary.md#oco-orders)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name             | Type          | Mandatory                        | Description                                                                                                                              |
| ---------------- | ------------- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- |
| market           | String        | **Yes**                          | Available [market](./../glossary.md#market). Example: BTC_USDT                                                                           |
| side             | String        | **Yes**                          | Order type. Variables: 'buy' / 'sell' Example: 'buy'                                                                                     |
| amount           | String/Number | **Yes**                          | Amount of [stock](./../glossary.md#stock) currency to buy or sell. Example: '0.001' or 0.001                                             |
| price            | String/Number | **Yes**                          | Price in [money](./../glossary.md#money) currency for [limit order](./../glossary.md#limit-order). Example: '9800' or 9800               |
| activation_price | String/Number | **Yes**                          | Activation price in [money](./../glossary.md#money) currency. Example: '10000' or 10000                                                  |
| stop_limit_price | String/Number | **Yes**                          | Price in [money](./../glossary.md#money) currency for [stop limit order](./../glossary.md#stop-limit-order). Example: '10100' or 10100   |
| clientOrderId    | String        | **No**                           | Identifier should be unique and contain letters, dashes, numbers, dots or underscores. The identifier must be unique.                    |
| stp              | String        | **No**                           | Self trade prevention mode. Variables: 'no / 'cancel_both' / 'cancel_new' /'cancel_old'. Example: 'no'.                                  |
| positionSide     | String        | **Yes, when hedge mode enabled** | Defines the position direction. Variables: 'LONG / 'SHORT' / 'BOTH'. Example: 'BOTH'. See [positionSide](./../glossary.md#position-side) |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "side": "buy",
  "amount": "0.001",
  "price": "40000",
  "activation_price": "41000",
  "stop_limit_price": "42000",
  "clientOrderId": "order1987111",
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**
Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if request validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "id": 117703764513, // oco order id
  "stop_loss": {
    "orderId": 117703764514, // unexecuted order ID
    "clientOrderId": "", // custom order id; "clientOrderId": "" - if not specified.
    "market": "BTC_USDT", // currency market
    "side": "buy", // order side
    "type": "stop limit", // unexecuted order type
    "timestamp": 1594605801.49815, // timestamp of order creation
    "dealMoney": "0", // executed amount in money
    "dealStock": "0", // executed amount in stock
    "amount": "2.241379", // active order amount
    "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - it will be rounded to zero
    "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - it will be rounded to zero
    "left": "2.241379", // unexecuted amount in stock
    "dealFee": "0", // executed fee by deal
    "post_only": false, // orders are guaranteed to be the maker order when executed.
    "mtime": 1662478154.941582, // timestamp of order modification
    "price": "19928.79", // unexecuted order price
    "activation_price": "29928.79", // activation price
    "activation_condition": "gte", // activation condition
    "activated": 0, // activation status
    "status": "FILLED", // order status
    "stp": "no", // self trade prevention mode
    "positionSide": "LONG" // position side - LONG or SHORT or BOTH
  },
  "take_profit": {
    "orderId": 117703764515, // unexecuted order ID
    "clientOrderId": "", // custom order id; "clientOrderId": "" - if not specified.
    "market": "BTC_USDT", // currency market
    "side": "buy", // order side
    "type": "limit", // unexecuted order type
    "timestamp": 1662478154.941582, // timestamp of order creation
    "dealMoney": "0", // executed amount in money
    "dealStock": "0", // executed amount in stock
    "amount": "0.635709", // active order amount
    "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - it will be rounded to zero
    "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - it will be rounded to zero
    "left": "0.635709", // unexecuted amount in stock
    "dealFee": "0", // executed fee by deal
    "post_only": false, // orders are guaranteed to be the maker order when executed.
    "mtime": 1662478154.941582, // timestamp of order modification
    "price": "9928.79", // unexecuted order price
    "status": "FILLED", // order status
    "stp": "no", // self trade prevention mode
    "positionSide": "LONG" // position side - LONG or SHORT or BOTH
  }
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed
- `32` - amount validation failed
- `33` - price validation failed
- `36` - clientOrderId validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Activation price field is required."],
    "amount": ["Amount field is required."],
    "market": ["Market field is required."],
    "price": ["Price field is required."],
    "side": ["Side field is required."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "side": ["Side field should contain only 'buy' or 'sell' values."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount field should be numeric string or number."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be numeric string or number."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "stop_limit_price": [
      "Stop_limit_price field should be numeric string or number."
    ]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field should not be empty string."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": [
      "Given amount is less than min amount 0.001",
      "Min amount step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "total": ["Total(amount * price) is less than 5.05"]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": ["ClientOrderId field should be a string."]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "ClientOrderId field field should contain only latin letters, numbers and dashes."
    ]
  }
}
```

```json
{
  "code": 36,
  "message": "Validation failed",
  "errors": {
    "clientOrderId": [
      "This client order id is already used by the current account."
    ]
  }
}
```

```json
{
  "code": 32,
  "message": "Validation failed",
  "errors": {
    "amount": ["Amount should be greater than 0."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price field should be at least 10", "Min price step = 0.000001"]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "stop_limit_price": [
      "Stop_limit_price field should be at least 10",
      "Min price step = 0.000001"
    ]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "price": ["Price should be greater than 0."]
  }
}
```

```json
{
  "code": 33,
  "message": "Validation failed",
  "errors": {
    "stop_limit_price": ["Stop_limit_price should be greater than 0."]
  }
}
```

```json
{
  "code": 35,
  "message": "Validation failed",
  "errors": {
    "maker_fee": ["Incorrect maker fee"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": [
      "Activation price should not be equal to the last price"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activation_price": ["Activation price should be numeric string."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Activation price should be greater than 0."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Empty history"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Min activation price = 10"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": ["Min activation price step = 0.00001"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "activationPrice": [
      "Activation price should not be equal to the last price"
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "lastPrice": ["internal error"]
  }
}
```

```json
{
  "code": 10,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Not enough balance."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

```json
{
  "code": 11,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Amount too small."]
  }
}
```

```json
{
  "code": 16,
  "message": "Inner validation failed",
  "errors": {
    "error": ["Please try again later."]
  }
}
```

```json
{
  "code": 15,
  "message": "Inner validation failed",
  "errors": {
    "error": ["Please try again later."]
  }
}
```

```json
{
  "code": 14,
  "message": "Inner validation failed",
  "errors": {
    "postOnly": [
      "This order couldn't be executed as a maker order and was canceled."
    ]
  }
}
```

```json
{
  "code": 153,
  "message": "Inner validation failed",
  "errors": {
    "price": ["Not enough balance for limit order."]
  }
}
```

```json
{
  "code": 150,
  "message": "Inner validation failed",
  "errors": {
    "price": ["Can't place limit order."]
  }
}
```

```json
{
  "code": 151,
  "message": "Inner validation failed",
  "errors": {
    "activation_price": ["Wrong activation price for stop loss."]
  }
}
```

```json
{
  "code": 152,
  "message": "Inner validation failed",
  "errors": {
    "price": ["Not enough balance for stop limit order."]
  }
}
```

</details>

---

### Cancel OCO order

<ApiEndpoint method="POST" path="/api/v4/order/oco-cancel" />

Cancel existing [order](./../glossary.md#orders)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name    | Type       | Mandatory | Description                                                                      |
| ------- | ---------- | --------- | -------------------------------------------------------------------------------- |
| market  | String     | **Yes**   | Available [market](./../glossary.md#market). Example: BTC_USDT                   |
| orderId | String/Int | **Yes**   | [OCO order](./../glossary.md#oco-orders) Id. Example: 4180284841 or "4180284841" |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "orderId": 117703764514,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if validation failed`
- `Status 503 if service temporary unavailable`

```json
{
  "id": 117703764513, // oco order id
  "stop_loss": {
    "orderId": 117703764514, // unexecuted order ID
    "clientOrderId": "", // custom order id; "clientOrderId": "" - if not specified.
    "market": "BTC_USDT", // currency market
    "side": "buy", // order side
    "type": "stop limit", // unexecuted order type
    "timestamp": 1594605801.49815, // timestamp of order creation
    "dealMoney": "0", // executed amount in money
    "dealStock": "0", // executed amount in stock
    "amount": "2.241379", // active order amount
    "takerFee": "0.001", // taker fee ratio. If the number less than 0.0001 - it will be rounded to zero
    "makerFee": "0.001", // maker fee ratio. If the number less than 0.0001 - it will be rounded to zero
    "left": "2.241379", // unexecuted amount in stock
    "dealFee": "0", // executed fee by deal
    "post_only": false, // orders are guaranteed to be the maker order when executed.
    "mtime": 1662478154.941582, // timestamp of order modification
    "price": "19928.79", // unexecuted order price
    "activation_price": "29928.79", // activation price
    "activation_condition": "gte", // activation condition
    "activated": 0, // activation status
    "status": "CANCELED", // order status
    "stp": "no" // self trade prevention mode
  },
  "take_profit": {
    "orderId": 117703764515, // unexecuted order ID
    "clientOrderId": "", // custom order id; "clientOrderId": "" - if not specified.
    "market": "BTC_USDT", // currency market
    "side": "buy", // order side
    "type": "limit", // unexecuted order type
    "timestamp": 1662478154.941582, // timestamp of order creation
    "dealMoney": "0", // executed amount in money
    "dealStock": "0", // executed amount in stock
    "amount": "0.635709", // active order amount
    "left": "0.635709", // unexecuted amount in stock
    "dealFee": "0", // executed fee by deal
    "post_only": false, // orders are guaranteed to be the maker order when executed.
    "mtime": 1662478154.941582, // timestamp of order modification
    "price": "9928.79", // unexecuted order price
    "status": "CANCELED", // order status
    "stp": "no" // self trade prevention mode
  }
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field is required."],
    "orderId": ["OrderId field is required."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "orderId": ["OrderId field should be an integer."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": [
      "Market field should be a string.",
      "Market field format is invalid."
    ]
  }
}
```

```json
{
  "code": 2,
  "message": "Inner validation failed",
  "errors": {
    "orderId": ["Unexecuted order was not found."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

---

### Cancel conditional order

<ApiEndpoint method="POST" path="/api/v4/order/conditional-cancel" />

Cancel existing [order](./../glossary.md#orders)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name   | Type       | Mandatory | Description                                                                         |
| ------ | ---------- | --------- | ----------------------------------------------------------------------------------- |
| market | String     | **Yes**   | Available [market](./../glossary.md#market). Example: BTC_USDT                      |
| id     | String/Int | **Yes**   | [conditional](./../glossary.md#conditional) Id. Example: 4180284841 or "4180284841" |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "id": 117703764514,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if validation failed`
- `Status 503 if service temporary unavailable`

```json
[]
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field is required."],
    "orderId": ["Id field is required."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "orderId": ["Id field should be an integer."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": [
      "Market field should be a string.",
      "Market field format is invalid."
    ]
  }
}
```

```json
{
  "code": 2,
  "message": "Inner validation failed",
  "errors": {
    "orderId": ["Unexecuted order was not found."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

---

### Cancel OTO order

<ApiEndpoint method="POST" path="/api/v4/order/oto-cancel" />

Cancel existing [order](./../glossary.md#orders)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name   | Type       | Mandatory | Description                                                                |
| ------ | ---------- | --------- | -------------------------------------------------------------------------- |
| market | String     | **Yes**   | Available [market](./../glossary.md#market). Example: BTC_USDT             |
| otoId  | String/Int | **Yes**   | [OTO](./../glossary.md#oco-orders) Id. Example: 4180284841 or "4180284841" |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "otoId": 117703764514,
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if validation failed`
- `Status 503 if service temporary unavailable`

```json
[]
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field is required."],
    "orderId": ["OtoId field is required."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "orderId": ["OtoId field should be an integer."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": [
      "Market field should be a string.",
      "Market field format is invalid."
    ]
  }
}
```

```json
{
  "code": 2,
  "message": "Inner validation failed",
  "errors": {
    "orderId": ["Unexecuted order was not found."]
  }
}
```

```json
{
  "code": 1,
  "message": "Inner validation failed",
  "errors": {
    "amount": ["Invalid argument."]
  }
}
```

</details>

---

### Sync kill-switch timer

<ApiEndpoint method="POST" path="/api/v4/order/kill-switch" />

This endpoint creates, updates, deletes [kill-switch timer](./../glossary.md#kill-switch-timer)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name    | Type   | Mandatory | Description                                                     |
| ------- | ------ | --------- | --------------------------------------------------------------- |
| market  | String | **Yes**   | Available [market](./../glossary.md#market). Example: BTC_USDT  |
| timeout | String | **Yes**   | Timer value. Example: "5"-"600" or null                         |
| types   | Array  | **No**    | Order types value. Example: "spot", "margin", "futures" or null |

If timer=null - delete existing timer by [market](./../glossary.md#market).
If types=null - create timer by [market](./../glossary.md#market) for all order types.

**Request BODY raw:**

```json
{
  "market": "BTC_USDT",
  "timeout": "5",
  "types": ["spot", "margin"],
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if validation failed`

```json
{
  "market": "BTC_USDT", // currency market,
  "startTime": 1662478154, // now timestamp,
  "cancellationTime": 1662478154, // now + timer_value,
  "types": ["spot", "margin"]
}
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": ["Market field is required."],
    "timeout": ["Timeout field is required."]
  }
}
```

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "timeout": ["Timeout field should be a string."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": [
      "Market field should be a string.",
      "Market field format is invalid."
    ]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "timeout": ["Timeout should be at least 5."]
  }
}
```

</details>

---

### Status kill-switch timer

<ApiEndpoint method="POST" path="/api/v4/order/kill-switch/status" />

This endpoint retrieves the status of [kill-switch timer](./../glossary.md#kill-switch-timer)

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name   | Type   | Mandatory | Description                                                    |
| ------ | ------ | --------- | -------------------------------------------------------------- |
| market | String | **No**    | Available [market](./../glossary.md#market). Example: BTC_USDT |

**Request BODY raw:**

```json
{
  "market": "BTC_USDT", // optional
  "request": "{{request}}",
  "nonce": "{{nonce}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if validation failed`

```json
[
  {
    "market": "BTC_USDT",
    "startTime": 1686127243,
    "cancellationTime": 1686127343,
    "types": ["spot", "margin"]
  }
]
```

<details>
<summary><b>Errors:</b></summary>

Error codes:

- `30` - default validation error code
- `31` - market validation failed

```json
{
  "code": 31,
  "message": "Validation failed",
  "errors": {
    "market": ["Market is not available."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "market": [
      "Market field should be a string.",
      "Market field format is invalid."
    ]
  }
}
```

</details>

---

## Convert

### Convert Estimate

<ApiEndpoint method="POST" path="/api/v4/convert/estimate" />

This endpoint creates a quote for converting one currency to another. Quote lifetime is 10 seconds, then quote will be expired.

❗ Rate limit 10000 requests/10 sec.

**Parameters:**

| Name      | Type   | Mandatory | Description                                                                                                                                                                                                         |
| --------- | ------ | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| from      | String | **Yes**   | From currency. Example: BTC                                                                                                                                                                                         |
| to        | String | **Yes**   | To currency. Example: USDT                                                                                                                                                                                          |
| direction | String | **Yes**   | Convert amount direction, defines in which currency corresponding "amount" field is populated. Use "to" in case amount is in "to" currency, use "from" if amount is in "from" currency (see use case samples below) |
| amount    | String | **Yes**   | Amount to convert or receive.                                                                                                                                                                                       |

**Request BODY raw:**

Example of 'I would like to estimate convert of BTC to receive 35,103.1 USDT':

```json
{
  "amount": "35,103.1",
  "direction": "to", // enum('from', 'to')
  "from": "BTC",
  "to": "USDT",
  "nonce": "{{nonce}}",
  "request": "{{request}}"
}
```

Example of 'I would like to estimate convert of 1 BTC to USDT':

```json
{
  "amount": "1",
  "direction": "from", // enum('from', 'to')
  "from": "BTC",
  "to": "USDT",
  "nonce": "{{nonce}}",
  "request": "{{request}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if validation failed`

```json
{
  "id": "123",
  "from": "BTC",
  "to": "USDT",
  "give": "50",
  "receive": "1714988.41577452",
  "rate": "34299.76831549",
  "expireAt": 1699016476
}
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 0,
  "message": "Validation failed",
  "errors": {
    "user": ["Terms of exchange are not accepted"]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "direction": ["Direction field does not exist in [from,to]."]
  }
}
```

```json
{
  "code": 0,
  "message": "Validation failed",
  "errors": {
    "from": ["Conversion markets not available"]
  }
}
```

</details>

---

### Convert Confirm

<ApiEndpoint method="POST" path="/api/v4/convert/confirm" />

This endpoint confirms an estimated quote.

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**
| Name | Type | Mandatory | Description |
|---------|--------|-----------|-------------|
| quoteId | String | **Yes** | Quote ID |

**Request BODY raw:**

```json
{
  "quoteId": 4050,
  "nonce": "{{nonce}}",
  "request": "{{request}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if validation failed`

```json
{
  "finalGive": "0.00002901",
  "finalReceive": "1"
}
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 0,
  "message": "Validation failed",
  "errors": {
    "quoteId": ["Quote could not be found"]
  }
}
```

</details>

---

### Convert History

<ApiEndpoint method="POST" path="/api/v4/convert/history" />

This endpoint returns convert history.

❗ Rate limit 10000 requests/10 sec.

**Response is cached for:**
NONE

**Parameters:**

| Name       | Type   | Mandatory | Description                                             |
| ---------- | ------ | --------- | ------------------------------------------------------- |
| fromTicker | String | **No**    | From currency. Example: BTC                             |
| toTicker   | String | **No**    | To currency. Example: USDT                              |
| from       | String | **No**    | From time filter. Example: 1699260637. Default: `now()` |
| to         | String | **No**    | To time filter. Example: 1699260637. Default: `now() +` |
| quoteId    | String | **No**    | Quote Id. Example: 4050                                 |
| limit      | String | **No**    | How many records to receive. Default: 100               |
| offset     | String | **No**    | Amount to convert or receive. Default 0                 |

<Alert
  type="warning"
  header="Important Limitations"
  message="This method can retrieve data not older than 6 months from current month. If you need older data - you can use Report on the History page in your account."
/>

**Request BODY raw:**

```json
{
  "fromTicker": "BTC",
  "nonce": "{{nonce}}",
  "request": "{{request}}"
}
```

**Response:**

Available statuses:

- `Status 200`
- `Status 400 if inner validation failed`
- `Status 422 if validation failed`

```json
{
  "records": [
    {
      "id": "4030",
      "date": 1699020642,
      "give": "0.00002901",
      "receive": "1",
      "rate": "34470.87211306",
      "path": [
        {
          "from": "BTC",
          "to": "USDT",
          "rate": "34470.87211306"
        }
      ]
    }
  ],
  "total": 4,
  "limit": 1,
  "offset": 0
}
```

<details>
<summary><b>Errors:</b></summary>

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "fromTicker": ["fromTicker is invalid."]
  }
}
```

```json
{
  "code": 30,
  "message": "Validation failed",
  "errors": {
    "toTicker": ["toTicker is invalid."]
  }
}
```

</details>

---
