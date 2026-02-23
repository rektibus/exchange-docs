# Basic Info

RESTful endpoint URL: **`https://api.pionex.com`**

### General API information

* **`timestamp`** parameter in **`query string`**, **`PIONEX-KEY`** and **`PIONEX-SIGNATURE`** parameters in headers, are required in all **`PRIVATE`** request

<table><thead><tr><th width="158.3390479700392"></th><th width="150"></th><th width="150"></th><th width="280.7463297179188"></th></tr></thead><tbody><tr><td>Parameter</td><td>Field</td><td>Type</td><td>Description</td></tr><tr><td>timestamp</td><td>query</td><td>number</td><td>Request timestamp in millisecond.<br>Any timestamp older than 20,000 milliseconds or in the future is invalid</td></tr><tr><td>PIONEX-KEY</td><td>header</td><td>string</td><td>Account API Key.</td></tr><tr><td>PIONEX-SIGNATURE</td><td>header</td><td>string</td><td>Signature.<br><strong><code>GET</code></strong> : <strong><code>METHOD + PATH_URL + QUERY + TIMESTAMP</code></strong><br><strong><code>POST</code></strong> and <strong><code>DELETE</code></strong> :  <strong><code>METHOD + PATH_URL + QUERY + TIMESTAMP + body</code></strong><br>For further information, please refer to  Authentication section</td></tr></tbody></table>

* For **`GET`** endpoint, additional parameter must be sent in **`query string`**
* For **`POST`** and **`DELETE`** endpoints, additional parameter must be sent in **`request body`**, **`content-type`** should be **`application/json`**
* 0 value of all **`number`** type parameters will be ignored.

### Response Message

* Responses of all RESTful endpoints are JSON data, which contains

Parameters

<table data-header-hidden><thead><tr><th width="204.77279692149847"></th><th width="150"></th><th width="318.00563669665246"></th></tr></thead><tbody><tr><td>Name</td><td>Type</td><td>Description</td></tr><tr><td>result</td><td>boolean</td><td><strong><code>true</code></strong> for success，<strong><code>false</code></strong> otherwise</td></tr><tr><td>timestamp</td><td>number</td><td>Response timestamp (millisecond)</td></tr></tbody></table>

* A successful response will contain business data

| Name | Type   | Description    |
| ---- | ------ | -------------- |
| data | object | Business data. |

Example:

```
{
  "result": true,
  "data": {
    "orderId":  123456789
  },
  "timestamp":  1566691672311
}
```

* Failed response contains

| Name    | Type   | Description                  |
| ------- | ------ | ---------------------------- |
| code    | string | Error code (See description) |
| message | string | Error message                |

Example:

```
{
  "result": false,
  "code": "TRADE_INVAILD_SYMBOL",
  "message":  "Invalid symbol",
  "timestamp":  1566691672311
}
```

### Error Code

* APIKEY\_LOST&#x20;
* SIGNATURE\_LOST
* I&#x50;*\_*&#x4E;O&#x54;*\_*&#x57;HITELISTED
* INVALIE\_APIKEY
* INVALID\_SIGNATURE
* APIKEY\_EXPIRED
* INVALID\_TIMESTAMP
* PERMISSION\_DENIED

# Basic Info

RESTful endpoint URL: **`https://api.pionex.com`**

### General API information

* **`timestamp`** parameter in **`query string`**, **`PIONEX-KEY`** and **`PIONEX-SIGNATURE`** parameters in headers, are required in all **`PRIVATE`** request

<table><thead><tr><th width="158.3390479700392"></th><th width="150"></th><th width="150"></th><th width="280.7463297179188"></th></tr></thead><tbody><tr><td>Parameter</td><td>Field</td><td>Type</td><td>Description</td></tr><tr><td>timestamp</td><td>query</td><td>number</td><td>Request timestamp in millisecond.<br>Any timestamp older than 20,000 milliseconds or in the future is invalid</td></tr><tr><td>PIONEX-KEY</td><td>header</td><td>string</td><td>Account API Key.</td></tr><tr><td>PIONEX-SIGNATURE</td><td>header</td><td>string</td><td>Signature.<br><strong><code>GET</code></strong> : <strong><code>METHOD + PATH_URL + QUERY + TIMESTAMP</code></strong><br><strong><code>POST</code></strong> and <strong><code>DELETE</code></strong> :  <strong><code>METHOD + PATH_URL + QUERY + TIMESTAMP + body</code></strong><br>For further information, please refer to  Authentication section</td></tr></tbody></table>

* For **`GET`** endpoint, additional parameter must be sent in **`query string`**
* For **`POST`** and **`DELETE`** endpoints, additional parameter must be sent in **`request body`**, **`content-type`** should be **`application/json`**
* 0 value of all **`number`** type parameters will be ignored.

### Response Message

* Responses of all RESTful endpoints are JSON data, which contains

Parameters

<table data-header-hidden><thead><tr><th width="204.77279692149847"></th><th width="150"></th><th width="318.00563669665246"></th></tr></thead><tbody><tr><td>Name</td><td>Type</td><td>Description</td></tr><tr><td>result</td><td>boolean</td><td><strong><code>true</code></strong> for success，<strong><code>false</code></strong> otherwise</td></tr><tr><td>timestamp</td><td>number</td><td>Response timestamp (millisecond)</td></tr></tbody></table>

* A successful response will contain business data

| Name | Type   | Description    |
| ---- | ------ | -------------- |
| data | object | Business data. |

Example:

```
{
  "result": true,
  "data": {
    "orderId":  123456789
  },
  "timestamp":  1566691672311
}
```

* Failed response contains

| Name    | Type   | Description                  |
| ------- | ------ | ---------------------------- |
| code    | string | Error code (See description) |
| message | string | Error message                |

Example:

```
{
  "result": false,
  "code": "TRADE_INVAILD_SYMBOL",
  "message":  "Invalid symbol",
  "timestamp":  1566691672311
}
```

### Error Code

* APIKEY\_LOST&#x20;
* SIGNATURE\_LOST
* I&#x50;*\_*&#x4E;O&#x54;*\_*&#x57;HITELISTED
* INVALIE\_APIKEY
* INVALID\_SIGNATURE
* APIKEY\_EXPIRED
* INVALID\_TIMESTAMP
* PERMISSION\_DENIED
# Authentication

### Signature Description

There is a high risk of API requests being tampered with during transmission over the internet. Except for public endpoints (base information, market data), private endpoints must be signed and authenticated with your API Key to verify that parameters or values have not been modified in transit.

Endpoints are marked their corresponding weight value and permission.&#x20;

Newly created API Key needs to be assigned permissions. Each API Key requires the appropriate permission(s) to access the corresponding endpoint. Please check required permission types before using the endpoints, and make sure your API Key has the appropriate permissions.

### Signing

1. Get current millisecond **`timestamp`**.
2. Set query parameters as key-value pairs: **`key=value`** (signature related value must not be URL-encoded).
3. Sort the key-value pairs in ascending ASCII order by key and concatenate with **`&`** (include **`timestamp`**).
4. Concatenate above result after **`PATH`** with **`?`** to generate **`PATH_URL`**.
5. Concatenate **`METHOD`** and **`PATH_URL`**.
6. Concatenate related entity body of **`POST`** and **`DELETE`** after step 5. Skip this step if there is no entity body.
7. Use **`API Secret`** and the above result to generate **`HMAC SHA256`** code, then convert it to hexadecimal.
8. Assign the hex result to **`PIONEX-SIGNATURE`**, add it to **`Header`** and send request.

Example:

User's **`API Secret`** and **`timestamp`** are:

```
Secret： NFqv4MB3hB0SOiEsJNDP9e0jDdKPWbDqS_Z1dbU4

timestamp： 1655896754515
```

The base part of request to query the order list is:

```
GET /api/v1/trade/allOrders?symbol=BTC_USDT&limit=1
```

Step 1, get current timestamp

```
timestamp=1655896754515
```

Step 2, set query parameters as key-value pairs: **`key=value`**

```
symbol=BTC_USDT
limit=1
timestamp=1655896754515
```

Step 3, Sort the key-value pairs in ascending ASCII order by key and concatenate with **`&`**

```
limit=1&symbol=BTC_USDT&timestamp=1655896754515
```

Step 4, concatenate above result after **`PATH`** with **`?`** to generate **`PATH_URL`**.

```
/api/v1/trade/allOrders?limit=1&symbol=BTC_USDT&timestamp=1655896754515
```

Step 5, concatenate **`METHOD`** and **`PATH_URL`**.

```
GET/api/v1/trade/allOrders?limit=1&symbol=BTC_USDT&timestamp=1655896754515
```

Step 6, Concatenate related entity body of **`POST`** and **`DELETE`** after step 5. Skip this step if there is no entity body.

```
b'GET/api/v1/trade/allOrders?limit=1&symbol=BTC_USDT&timestamp=1655896754515{"symbol": "BTC_USDT"}'
```

Step 7, Use **`API Secret`** and the above result to generate **`HMAC SHA256`** code, then convert it to hexadecimal.

```
ec83d21e1237cbe7e0172f79c0e3a4741c86f6b201ba762f21149bf195519be1    //PIONEX-SIGNATURE
```
# Authentication

### Signature Description

There is a high risk of API requests being tampered with during transmission over the internet. Except for public endpoints (base information, market data), private endpoints must be signed and authenticated with your API Key to verify that parameters or values have not been modified in transit.

Endpoints are marked their corresponding weight value and permission.&#x20;

Newly created API Key needs to be assigned permissions. Each API Key requires the appropriate permission(s) to access the corresponding endpoint. Please check required permission types before using the endpoints, and make sure your API Key has the appropriate permissions.

### Signing

1. Get current millisecond **`timestamp`**.
2. Set query parameters as key-value pairs: **`key=value`** (signature related value must not be URL-encoded).
3. Sort the key-value pairs in ascending ASCII order by key and concatenate with **`&`** (include **`timestamp`**).
4. Concatenate above result after **`PATH`** with **`?`** to generate **`PATH_URL`**.
5. Concatenate **`METHOD`** and **`PATH_URL`**.
6. Concatenate related entity body of **`POST`** and **`DELETE`** after step 5. Skip this step if there is no entity body.
7. Use **`API Secret`** and the above result to generate **`HMAC SHA256`** code, then convert it to hexadecimal.
8. Assign the hex result to **`PIONEX-SIGNATURE`**, add it to **`Header`** and send request.

Example:

User's **`API Secret`** and **`timestamp`** are:

```
Secret： NFqv4MB3hB0SOiEsJNDP9e0jDdKPWbDqS_Z1dbU4

timestamp： 1655896754515
```

The base part of request to query the order list is:

```
GET /api/v1/trade/allOrders?symbol=BTC_USDT&limit=1
```

Step 1, get current timestamp

```
timestamp=1655896754515
```

Step 2, set query parameters as key-value pairs: **`key=value`**

```
symbol=BTC_USDT
limit=1
timestamp=1655896754515
```

Step 3, Sort the key-value pairs in ascending ASCII order by key and concatenate with **`&`**

```
limit=1&symbol=BTC_USDT&timestamp=1655896754515
```

Step 4, concatenate above result after **`PATH`** with **`?`** to generate **`PATH_URL`**.

```
/api/v1/trade/allOrders?limit=1&symbol=BTC_USDT&timestamp=1655896754515
```

Step 5, concatenate **`METHOD`** and **`PATH_URL`**.

```
GET/api/v1/trade/allOrders?limit=1&symbol=BTC_USDT&timestamp=1655896754515
```

Step 6, Concatenate related entity body of **`POST`** and **`DELETE`** after step 5. Skip this step if there is no entity body.

```
b'GET/api/v1/trade/allOrders?limit=1&symbol=BTC_USDT&timestamp=1655896754515{"symbol": "BTC_USDT"}'
```

Step 7, Use **`API Secret`** and the above result to generate **`HMAC SHA256`** code, then convert it to hexadecimal.

```
ec83d21e1237cbe7e0172f79c0e3a4741c86f6b201ba762f21149bf195519be1    //PIONEX-SIGNATURE
```
# Get Trades

```
GET /api/v1/market/trades
```

Weight: 1

Request parameters

<table data-header-hidden><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th><th width="234.84615384615384"></th></tr></thead><tbody><tr><td>Name</td><td>Type</td><td>Mandatory</td><td>Description</td></tr><tr><td>symbol</td><td>string</td><td>YES</td><td>Symbol.</td></tr><tr><td>limit</td><td>number</td><td>NO</td><td>Default: 100. <br>Range: 10 - 500</td></tr></tbody></table>

Response format

<table data-header-hidden><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th><th width="253.84615384615384"></th></tr></thead><tbody><tr><td>Name</td><td></td><td>Type</td><td>Description</td></tr><tr><td>trades</td><td></td><td>array</td><td>Collection of latest real-time transaction, sorted by timestamp in descending order.</td></tr><tr><td></td><td>symbol</td><td>string</td><td>Symbol.</td></tr><tr><td></td><td>tradeId</td><td>string</td><td>Trade id.</td></tr><tr><td></td><td>price</td><td>string</td><td>Price of the trade.</td></tr><tr><td></td><td>size</td><td>string</td><td>Quantity of the trade.</td></tr><tr><td></td><td>side</td><td>string</td><td>BUY / SELL</td></tr><tr><td></td><td>timestamp</td><td>string</td><td>Filled timestamp in millisecond.</td></tr></tbody></table>

Caution: The direction of BUY or SELL is from the liquidity TAKER’s perspective.

Error code

* MARKET\_INVALID\_SYMBOL     Invalid symbol.
* MARKET\_PARAMETER\_ERROR     Parameter error

Request example

```
GET https://{site}/api/v1/market/trades?symbol=BTC_USDT&limit=5
```

Response example

```
{ 
  "data": {
    "trades": [
      {
        "symbol": "BTC_USDT",
        "tradeId": "600848671",
        "price": "7962.62",
        "size": "0.0122",
        "side": "BUY",
        "timestamp": 1566691672311
      },
      {
        "symbol": "BTC_USDT",
        "tradeId": "600848670",
        "price": "7960.12",
        "size": "0.0198",
        "side": "BUY",
        "timestamp": 1566691672311
      }
    ]
  },
  "result": true,
  "timestamp": 1566691672311
}
```
# Get Depth

```
GET /api/v1/market/depth
```

Weight: 1

Request parameters

<table data-header-hidden><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th><th width="257.8461538461538"></th></tr></thead><tbody><tr><td>Name</td><td>Type</td><td>Mandatory</td><td>Description</td></tr><tr><td>symbol</td><td>string</td><td>YES</td><td>Symbol.</td></tr><tr><td>limit</td><td>number</td><td>NO</td><td>Default:20. <br>Range: 1 - 1000</td></tr></tbody></table>

Response format

<table data-header-hidden><thead><tr><th width="165.28594096793304"></th><th width="150"></th><th width="326.79888105235915"></th></tr></thead><tbody><tr><td>Name</td><td>Type</td><td>Description</td></tr><tr><td>bids</td><td>array</td><td>Collection of bid order [price, quantity], sorted by price in descending order.</td></tr><tr><td>asks</td><td>array</td><td>Collection of ask order (price, quantity), sorted by price in ascending order.</td></tr><tr><td>updateTime</td><td>number</td><td>Update timestamp in millisecond.</td></tr></tbody></table>

Error code

* MARKET\_INVALID\_SYMBOL     Invalid symbol.
* MARKET\_PARAMETER\_ERROR     Parameter error.

Request example

```
GET https://{site}/api/v1/market/depth?symbol=BTC_USDT&limit=5
```

Response example

```
{ 
  "data": {
    "bids": [
        ["29658.37", "0.0123"],
        ["29658.35", "1.1234"],
        ["29657.99", "2.2345"],
        ["29657.56", "6.3456"],
        ["29656.13", "8.4567"]
    ],
    "asks": [
        ["29658.47", "0.0345"],
        ["29658.65", "1.0456"],
        ["29658.89", "3.5567"],
        ["29659.43", "5.2678"],
        ["29659.98", "1.9789"]
    ]，
    "updateTime": 1566676132311
  },
  "result": true,
  "timestamp": 1566691672311
}
```
# Get 24hr Ticker

```
GET /api/v1/market/tickers
```

Weight: 1

Request parameters

<table data-header-hidden><thead><tr><th width="136.50901977830907"></th><th width="128"></th><th width="150"></th><th width="257.8461538461538"></th></tr></thead><tbody><tr><td>Name</td><td>Type</td><td>Mandatory</td><td>Description</td></tr><tr><td>symbol</td><td>string</td><td>No</td><td>Symbol.</td></tr><tr><td>type</td><td>string</td><td>No</td><td>Type, if the symbol is specified, the type is irrelevant. If the symbol is not specified, the default is SPOT, with the possible values being SPOT / PERP.</td></tr></tbody></table>

Response format

<table data-header-hidden><thead><tr><th width="119.28594096793304"></th><th width="122"></th><th width="150"></th><th width="333.79888105235915"></th></tr></thead><tbody><tr><td>Name</td><td></td><td>Type</td><td>Description</td></tr><tr><td>tickers</td><td></td><td>array</td><td>Collection of tickers.</td></tr><tr><td></td><td>symbol</td><td>string</td><td>Symbol.</td></tr><tr><td></td><td>time</td><td>number</td><td>Timestamp in millisecond.</td></tr><tr><td></td><td>open</td><td>string</td><td>Open price.</td></tr><tr><td></td><td>close</td><td>string</td><td>Close price.</td></tr><tr><td></td><td>high</td><td>string</td><td>Highest price.</td></tr><tr><td></td><td>low</td><td>string</td><td>Lowest price.</td></tr><tr><td></td><td>volume</td><td>string</td><td>24-hour total trading volume</td></tr><tr><td></td><td>amount</td><td>string</td><td>24-hour total trading amount</td></tr><tr><td></td><td>count</td><td>string</td><td>24-hour total trading count</td></tr></tbody></table>

Error code

* MARKET\_INVALID\_SYMBOL     Invalid symbol.
* MARKET\_PARAMETER\_ERROR     Parameter error.

Request example

```
GET https://{site}/api/v1/market/tickers
```

Response example

```
{ 
  "data": {
    "tickers": [
      {
        "symbol": "BTC_USDT",
        "time": 1545291675000,
        "open": "7962.62",
        "close": "7952.32",
        "high": "7971.61",
        "low": "7950.29",
        "volume": "1.537",
        "amount": "12032.56",
        "count": 271585
      },
      {
        "symbol": "ETH_USDT",
        "time": 1545291675000,
        "open": "1963.62",
        "close": "1852.22",
        "high": "1971.11",
        "low": "1850.23",
        "volume": "100.532",
        "amount": "112012.51",
        "count": 432211
      }  
    ]
  },
  "result": true,
  "timestamp": 1566691672311
}
```
# Get Book Ticker

```
GET /api/v1/market/bookTickers
```

Weight: 1

Request parameters

<table data-header-hidden><thead><tr><th width="136.50901977830907"></th><th width="128"></th><th width="150"></th><th width="257.8461538461538"></th></tr></thead><tbody><tr><td>Name</td><td>Type</td><td>Mandatory</td><td>Description</td></tr><tr><td>symbol</td><td>string</td><td>No</td><td>Symbol.</td></tr><tr><td>type</td><td>string</td><td>No</td><td>Type, if the symbol is specified, the type is irrelevant. If the symbol is not specified, the default is PERP, with the possible values being SPOT / PERP.</td></tr></tbody></table>

Response format

<table data-header-hidden><thead><tr><th width="119.28594096793304"></th><th width="122"></th><th width="150"></th><th width="333.79888105235915"></th></tr></thead><tbody><tr><td>Name</td><td></td><td>Type</td><td>Description</td></tr><tr><td>tickers</td><td></td><td>array</td><td>Collection of tickers.</td></tr><tr><td></td><td>symbol</td><td>string</td><td>Symbol.</td></tr><tr><td></td><td>bidPrice</td><td>number</td><td>Best bid price.</td></tr><tr><td></td><td>bidSize</td><td>string</td><td>Volume at the best bid price.</td></tr><tr><td></td><td>askPrice</td><td>string</td><td>Best ask price.</td></tr><tr><td></td><td>askSize</td><td>string</td><td>Volume at the best ask price.</td></tr><tr><td></td><td>timestamp</td><td>string</td><td>Timestamp in millisecond.</td></tr></tbody></table>

Error code

* MARKET\_INVALID\_SYMBOL     Invalid symbol.
* MARKET\_PARAMETER\_ERROR     Parameter error.

Request example

```
GET https://{site}/api/v1/market/bookTicker
```

Response example

```
{ 
  "data": {
    "tickers": [
      
    ]
  },
  "result": true,
  "timestamp": 1566691672311
}
```
# Get Klines

```
GET /api/v1/market/klines
```

Weight: 1

Request parameters

<table data-header-hidden><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th><th width="257.8461538461538"></th></tr></thead><tbody><tr><td>Name</td><td>Type</td><td>Mandatory</td><td>Description</td></tr><tr><td>symbol</td><td>string</td><td>YES</td><td>Symbol.</td></tr><tr><td>interval</td><td>string</td><td>YES</td><td>1M，5M，15M，30M，60M，4H，8H，12H，1D</td></tr><tr><td>endTime</td><td>number</td><td>NO</td><td>End time in millisecond</td></tr><tr><td>limit</td><td>number</td><td>NO</td><td>Default 100, range: 1-500.</td></tr></tbody></table>

Response format

<table data-header-hidden><thead><tr><th width="119.28594096793304"></th><th width="122"></th><th width="150"></th><th width="333.79888105235915"></th></tr></thead><tbody><tr><td>Name</td><td></td><td>Type</td><td>Description</td></tr><tr><td>klines</td><td></td><td>array</td><td>Collection of klines.</td></tr><tr><td></td><td>time</td><td>number</td><td>Timestamp in millisecond.</td></tr><tr><td></td><td>open</td><td>string</td><td>Open price.</td></tr><tr><td></td><td>close</td><td>string</td><td>Close price.</td></tr><tr><td></td><td>high</td><td>string</td><td>Highest price.</td></tr><tr><td></td><td>low</td><td>string</td><td>Lowest price.</td></tr><tr><td></td><td>volume</td><td>string</td><td>Total trading volume</td></tr></tbody></table>

Error code

* MARKET\_INVALID\_TIME    A maximum of 10,000 records can be retrieved, if the specified endTime exceeds the limit, the error will occur

Request example

```
GET https://{site}/api/v1/market/klines
```

Response example

```
{
  "result": true,
  "data": {
    "klines": [
      {
        "time": 1691649240000,
        "open": "1851.27",
        "close": "1851.32",
        "high": "1851.32",
        "low": "1851.27",
        "volume": "0.542"
      }
    ]
  },
  "timestamp": 1691649271544
}
```
# Get Klines

```
GET /api/v1/market/klines
```

Weight: 1

Request parameters

<table data-header-hidden><thead><tr><th width="150"></th><th width="150"></th><th width="150"></th><th width="257.8461538461538"></th></tr></thead><tbody><tr><td>Name</td><td>Type</td><td>Mandatory</td><td>Description</td></tr><tr><td>symbol</td><td>string</td><td>YES</td><td>Symbol.</td></tr><tr><td>interval</td><td>string</td><td>YES</td><td>1M，5M，15M，30M，60M，4H，8H，12H，1D</td></tr><tr><td>endTime</td><td>number</td><td>NO</td><td>End time in millisecond</td></tr><tr><td>limit</td><td>number</td><td>NO</td><td>Default 100, range: 1-500.</td></tr></tbody></table>

Response format

<table data-header-hidden><thead><tr><th width="119.28594096793304"></th><th width="122"></th><th width="150"></th><th width="333.79888105235915"></th></tr></thead><tbody><tr><td>Name</td><td></td><td>Type</td><td>Description</td></tr><tr><td>klines</td><td></td><td>array</td><td>Collection of klines.</td></tr><tr><td></td><td>time</td><td>number</td><td>Timestamp in millisecond.</td></tr><tr><td></td><td>open</td><td>string</td><td>Open price.</td></tr><tr><td></td><td>close</td><td>string</td><td>Close price.</td></tr><tr><td></td><td>high</td><td>string</td><td>Highest price.</td></tr><tr><td></td><td>low</td><td>string</td><td>Lowest price.</td></tr><tr><td></td><td>volume</td><td>string</td><td>Total trading volume</td></tr></tbody></table>

Error code

* MARKET\_INVALID\_TIME    A maximum of 10,000 records can be retrieved, if the specified endTime exceeds the limit, the error will occur

Request example

```
GET https://{site}/api/v1/market/klines
```

Response example

```
{
  "result": true,
  "data": {
    "klines": [
      {
        "time": 1691649240000,
        "open": "1851.27",
        "close": "1851.32",
        "high": "1851.32",
        "low": "1851.27",
        "volume": "0.542"
      }
    ]
  },
  "timestamp": 1691649271544
}
```
# Trade

The TRADE topic provides data on all trades in the market. Up to 100 trades per message, sorted by timestamp in descending order.

You can subscribe to it on a public connection by sending

```
{
  "op": "SUBSCRIBE",
  "topic":  "TRADE", 
  "symbol": "BTC_USDT"
}
```

Data field contains

* **`symbol`**: Symbol.
* **`tradeId`**: Trade id.
* **`price`**: Price of the trade.
* **`size`**: Quantity of the trade.
* **`side`**: BUY / SELL. The direction of BUY or SELL of trade are from the liquidity TAKER's perspective.
* **`timestamp`**: Filled timestamp in millisecond.

Message example

```
{
  "topic": "TRADE",
  "symbol": "BTC_USDT"
  "data": [
    {
      "symbol": "BTC_USDT",
      "tradeId": "600848671",
      "price": "7962.62",
      "size": "0.0122",
      "side": "BUY",
      "timestamp": 1566691672311
    },
    {
      "symbol": "BTC_USDT",
      "tradeId": "600848672",
      "price": "7962.62",
      "size": "0.0322",
      "side": "BUY",
      "timestamp": 1566691672311
    },
    {
      "symbol": "BTC_USDT",
      "tradeId": "600848673",
      "price": "7962.62",
      "size": "0.0132",
      "side": "BUY",
      "timestamp": 1566691672311
    }
  ]
  "timestamp":1566691672311
}
```

###
# Depth

The DEPTH topic provides the latest market by price order book.

You can subscribe to it on a public connection by sending

```
{
  "op": "SUBSCRIBE",
  "topic":  "DEPTH", 
  "symbol": "BTC_USDT",
  "limit":  5 // Range: 1-100
}
```

Data field contains

* **`bids`**
* **`asks`**

The `bids` and `asks` are formatted like so: `[[best price, size at price], [next next best price, size at price], ...]`

Message example

```
{
  "topic": "DEPTH",
  "symbol": "BTC_USDT"
  "data": {
    "bids": [
      ["27964.01", "0.0675"],
      ["27963.23", "0.9111"],
      ["27961.52", "0.1022"],
      ["27960.00", "3.8891"],
      ["27958.13", "1.2008"]
    ],
    "asks": [
      ["27979.32", "0.0731"],
      ["27980.97", "1.0294"],
      ["27981.62", "2.5651"],
      ["27986.45", "1.2415"],
      ["27990.16", "1.9978"]
    ]  
  },
  "timestamp": 1566691672311
}
```
