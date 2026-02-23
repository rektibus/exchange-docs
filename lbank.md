 # Marketing REST API

## Getting Start    
REST (Representational State Transfer) is the most popular internet software architecture nowadays. It is clear in structure, easy to understand, and convenient to expand. More and more companies therefore apply the structures in their websites. It has following advantages:

>- In a RESTful architecture, each URL represents a resource
>- Between the client and the server, a certain presentation layer of such resources passed
>- The client uses the four HTTP commands to operate on the server-side resources to achieve “state transition of the presentation layer.”

We suggested that user should use the REST API for trading and/or asset operations (such as deposite and withdrawals)
    
## Requesting Interaction
The base `URL` of REST requests is `https://api.lbkex.com/`

All requests are based on `HTTPS` protocol, and `contentType` in request header should be 
assigned to: `application/x-www-form-urlencoded`

The interaction requests
1.Request parameter: Proceed parameter encapsulation based on the interface request parameter. 
2.Submitting the request parameter: Through `POST` or `GET` method, the encapsulated requested parameter would be submitted to the server. 
3.Server response: Server executes security authentication to the user’s request data, and responded data would be returned to the user, according to the business logic. in JSON format after the authentication.
4.Data processing: process the data as it responds to the server. 


## API Reference
### Marketing API

1. 
1. Query current Market Data  

> URL: `https://api.lbkex.com/v1/ticker.do`

Parameters	

|Name|	Type|	Required|	Description|
| :-----    | :-----   | :-----    | :-----   |
|symbol|String|Yes|Pair <br>Such as: `eth_btc`、`zec_btc`、 `all`|


> Set `all` to `symbol` to get data of all trading pairs.


Example 1:	

```javascript
# Request
GET https://api.lbkex.com/v1/ticker.do
{
  "symbol"："all"
}
# Response
[
  {
    "symbol"："eth_btc",
    "timestamp"："1410431279000",
    "ticker"：{
      "change"："4.21",
      "high"："7722.58",
      "latest"："7682.29",
      "low"："7348.30",
      "turnover"："0.00",
      "vol"："1316.3235"
    }
  },
  {
    "symbol"："sc_btc",
    "timestamp"："1410431279000",
    "ticker"：{
      "change"："4.21",
      "high"："7722.58",
      "latest"："7682.29",
      "low"："7348.30",
      "turnover"："0.00",
      "vol"："1316.3235"
    }
  }
]
```
Example 2

```javascript
# RequestGET https://api.lbkex.com/v1/ticker.do
{
  "symbol"："eth_btc"
}
# Response
{
  "timestamp"："1410431279000",
  "ticker"：{
    "change"："4.21",
    "high"："7722.58",
    "latest"："7682.29",
    "low"："7348.30",
    "turnover"："0.00",
    "vol"："1316.3235"
  }
}
```

Returns	


|Field|Description|
|-|-|
|vol|24 hr trading volume|
|high|24 hr highest price|
|low|24 hr lowest price|
|change|Fluctuation (%) in 24 hr|
|turnover|Total Turn over in 24 hr|
|latest|Latest Price|
|timestamp|Timestamp of latest transaction|



2. Available trading pairs

> URL: `https://api.lbkex.com/v1/currencyPairs.do`	

Paramters: `None`

Example

```javascript
# Request
GET https://api.lbkex.com/v1/currencyPairs.do

# Response[
  "bcc_eth","etc_btc","dbc_neo","eth_btc",
  "zec_btc","qtum_btc","sc_btc","ven_btc",
  "ven_eth","sc_eth","zec_eth"
]
```

Returns
> All available trading pairs


3. Market Depth

URL: `https://api.lbkex.com/v1/depth.do`	

Parameters	

|Name|	Type|	Required|	Description|
| :-----    | :-----   | :-----    | :-----   |
|symbol|String|Yes|Trading Pair. Such as `eth_btc`|
|size|Integer|No(Default is 60)|The count of returned items.(1-60)|
|merge|Integer|No(Default is 0)|Depth: 0,1|

Example
```javascript
# Request
GET https://api.lbkex.com/v1/depth.do
{
  "symbol"："eth_btc",
  "size"："60",
  "merge"："1"
}
# Response
{
  "asks"：[
    [5370.4, 0.32],
    [5369.5, 0.28],
    [5369.24, 0.05],
    [5368.2, 0.079],
    [5367.9, 0.023]
  ],
  "bids"：[
    [5367.24, 0.32],
    [5367.16, 1.31],
    [5366.18, 0.56],
    [5366.03, 1.42],
    [5365.77, 2.64]
  ]
}
```

Returns:
```
asks :Depth of asks (Sellers')
bids :Depth of bids (Buyers')
```

4. Query historical transactions

URL: `https://api.lbkex.com/v1/trades.do`	

Parameters	

|Name|	Type|	Required|	Description|
| :-----    | :-----   | :-----    | :-----   |
|symbol|String|Yes| Trading pair. <br>Such as `eth_btc`|
|size|Integer|Yes|The count of returned items.(1-600)|
|time|String|No|Start transaction timestamp of the querying. Return latest records if it is not provided. |

Example
```javascript
# Request
GET https://api.lbkex.com/v1/trades.do
{
  "symbol"："eth_btc",
  "size"："600",
  "time"："1482311600000"
}
# Response[
  {
    "date_ms"：1482311500000,
    "amount"：1.4422,
    "price"：5242.66,
    "type"："buy",
    "tid"："a4aie34"
  },
  {
    "date_ms"：1482311400000,
    "amount"：51.3454,
    "price"：5412.24,
    "type"："sell",
    "tid"："iodsio1934"
  },
  {
    "date_ms"：1482311300000,
    "amount"：4.2355,
    "price"：5124.22,
    "type"："buy",
    "tid"："di124kq"
  }
]
```

Returns:

|Field|Description|
|-|-|
|date_ms|Transaction Time|
|amount|Transaction Volume|
|price|Transaction Price|
|type|buy or sell|
|tid|Transaction ID|


5. Query K Bar Data

URL: `https://api.lbkex.com/v1/kline.do`	

Parameters	

|Name|	Type|	Required|	Description|
| :-----    | :-----   | :-----    | :-----   |
|symbol|String|Yes|Trading Pair `eth_btc`|
|size|Integer|Yes|Count of the bars (1-2880)|
|type|String|Yes|`minute1`：1 minute<br>`minute5`：5 minutes<br> `minute15`：15minutes<br>`minute30`：30 minutes<br>`hour1`：1 hour<br>`hour4`：4 hours<br>`hour8`：8 hours<br>`hour12`：12 hours<br>`day1`：1 day<br>`week1`：1 week<br>`month1`：1 month<br> |
|time|String|Yes|Timestamp (of Seconds)|

Example
```javascript
# Request
GET https://api.lbkex.com/v1/kline.do
{
  "symbol"："eth_btc",
  "size"："600",
  "type"："minute1",
  "time"："1482311600"
}
# Response
[
  [
    1482311500,
    5423.23,
    5472.80,
    5516.09,
    5462,
    234.3250
  ],
  [
    1482311400,
    5432.52,
    5459.87,
    5414.30,
    5428.23,
    213.7329
  ]
]
```

Returns:

|Field|Description|
|-|-|
|1482311500|Timestamp|
|5423.23|Open Price|
|5472.80|Highest Price|
|5516.09|Lowest Price|
|5462|Close Price|
|234.3250|Trading Volume|
# Trading REST API

## Getting Start

REST (Representational State Transfer) is the most popular 
internet software architecture nowadays. It is clear in 
structure, easy to understand, and convenient to expand. 
More and more companies therefore apply the structures 
in their websites. It has following advantages:

>- In a `RESTful` architecture, each `URL` represents a resource
>- Between the client and the server, a certain presentation layer of such resources passed
>- The client uses the four `HTTP` commands to operate on the server-side resources to achieve “state transition of the presentation layer.”

We suggested that user should use the REST API for trading and/or asset operations (such as deposite and withdrawals)

## Requesting Interaction
The base `URL` of REST requests is `https://api.lbkex.com/`

All requests are based on `HTTPS` protocol, and `contentType` in request header should be 
assigned to: `application/x-www-form-urlencoded`

The interaction requests
1.Request parameter: Proceed parameter encapsulation based on the interface request parameter. 
2.Submitting the request parameter: Through `POST` or `GET` method, the encapsulated requested parameter would be submitted to the server. 
3.Server response: Server executes security authentication to the user’s request data, and responded data would be returned to the user, according to the business logic. in JSON format after the authentication.
4.Data processing: process the data as it responds to the server. 


## API Reference

### Trading API

#### 1. Acquiring Users' Asset Information


Parameters	

| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|Yes|User's `api_key`|
|sign|String|Yes|signature of the request|

Example:

```javascript
# RequestPOST https://api.lbkex.com/v1/user_info.do
{
  "api_key"："16702619-0bc8-446d-a3d0-62fb67a8985e",
  "sign"："0E0872AD955C0E715B43C78F24B3053A",
}
# Response
{
  "result"："true",
  "info":{
    "freeze"：{
    "btc"：1.0000,
    "zec"：0.0000,
    "cny"：80000.00
  },
  "asset"：{
    "net"：95678.25
  },
  "free"：{
    "btc"：2.0000,
    "zec"：0.0000,
    "cny"：34.00
  }
}
```

Returns

|Field|Note|
|-|-|
|result | `true` means success and `false` means failed. |
|asset |Total balance of the asset |
|freeze |Frozen balance of the asset |
|free |Available balance of the account|


#### 2. Place Order

Parameters:


| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|Yes|User's `api_key`|
|symbol|String|Yes|Trading Pair<br>`eth_btc`:Etherum over bitcoin； `zec_btc`:zcoin over bitcoin |
|type|String|Yes|trade type: `buy/sell`|
|price|String|Yes|Price<br> `Greater than 0`|
|amount|String|Yes|Volume <br>More than `0.001` `BTC` |
|sign|String|Yes|signature of the request|

Example

```javascript
# Request
POST https://api.lbkex.com/v1/create_order.do
{
  "api_key"："16702619-0bc8-446d-a3d0-62fb67a8985e",
  "symbol"："eth_btc",
  "type"："buy",
  "price"："5323.42",
  "amount"："3",
  "sign"："16702619-0bc8-446d-a3d0-62fb67a8985e",
}
# Response
{
  "result"："true",
  "order_id"："16702619-0bc8-446d"
}
```


Returns

|Field|Note|
|-|-|
|result|`true` on success or `false` on failure |
|order_id|Order ID| 


#### 3. Cancel the Order

Parameters:

| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|Yes|User's `api_key`|
|symbol|String|Yes|Trading Pair<br>`eth_btc`:Etherum over bitcoin； `zec_btc`:zcoin over bitcoin |
|order_id|String|Yes|Order ID<br> Use comma to join the multiply orders. `order_id1,order_id2`, No more than 3 orders in one order.|
|sign|String|Yes|signature of the request|

Example


```javascript
# Request
POST https://api.lbkex.com/v1/cancel_order.do
{
  "api_key"："16702619-0bc8-446d-a3d0-62fb67a8985e",
  "symbol"："eth_btc",
  "order_id"："24f7ce27-af1d-4dca-a8c1-ef1cbeec1b23",
  "sign"："16702619-0bc8-446d-a3d0-62fb67a8985e",
}
# Response
{
  "result"："true",
  "order_id"："*****",
  "success"："*****,*****,*****",
  "error"："*****,*****"
}
```

Returns

|Field|Note|
|-|-|
|result|`true` on success or `false` on failure (For single order)|
|order_id|Order ID (For single order)| 
|success|Order IDs cancelled sucessfully. (For multiply orders）| 
|error|Order IDs failed to cancel.（For multiply orders）




#### 4. Query Order 

Parameters:


| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|Yes|User's `api_key`|
|symbol|String|Yes|Trading Pair<br>`eth_btc`:Etherum over bitcoin； `zec_btc`:zcoin over bitcoin |
|order_id|String|Yes|Order ID<br> Use comma to join the multiply orders. `order_id1,order_id2`, No more than 3 orders in one order.|
|sign|String|Yes|signature of the request|


Example
```javascript
# Request
POST https://api.lbkex.com/v1/orders_info.do
{
  "api_key"："16702619-0bc8-446d-a3d0-62fb67a8985e",
  "symbol"："eth_btc",
  "order_id"："24f7ce27-af1d-4dca-a8c1-ef1cbeec1b23,57a80854-cf31-489a-93b3-d25a2d4c12f2",
  "sign"："16702619-0bc8-446d-a3d0-62fb67a8985e",
}
# Response
{
  "result"："true",
  "orders"：[
    {
      "symbol"："eth_btc",
      "amount"：10.000000,
      "create_time"：1484289832081,
      "price"：5000.000000,
      "avg_price"：5277.301200,
      "type"："sell",
      "order_id"："ab704110-af0d-48fd-a083-c218f19a4a55",
      "deal_amount"：10.000000,
      "status"：2
    },
    {
      "symbol"："eth_btc",
      "amount"：10.000000,
      "create_time"：1484287197233,
      "price"：6000.000000,
      "avg_price"：0.000000,
      "type"："sell",
      "order_id"："57a80854-cf31-489a-93b3-d25a2d4c12f2",
      "deal_amount"：0.000000,
      "status"：-1
    }
  ]
}
```

Returns

|Field|Note|
|-|-|
|result|`true` on success or `false` on failure (For single order)|
|order_id|Order ID (For single order)| 
|orders|A list of querying orders| 
|symbol|Trading Pair，`eth_btc`：Etherum， `zec_btc`：ZCash|
|amount|required volume|
|create_time|order time|
|price|price|
|avg_price|Average strike price|
|type|`buy`：Buy<br>`sell`：Sell
|deal_amount|filled volume|
|status|Status<br>`-1`：Cancelled <br>`0`：on trading <br>`1`： filled partially <br> `2`：Filled totally <br>`4`：Cancelling|




#### 5. Query history order (Only the records in recent seven days are available)

Parameters:


| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|Yes|User's `api_key`|
|symbol|String|Yes|Trading Pair<br>`eth_btc`:Etherum over bitcoin； `zec_btc`:zcoin over bitcoin |
|current_page|String|Yes|Current Page|
|page_length|String|Yes|The records in a page. No more than 200.|
|sign|String|Yes|signature of the request|
|status|String|No|the status of order|

Example

```javascript
# Request
POST https://api.lbkex.com/v1/orders_info_history.do
{
  "api_key"："16702619-0bc8-446d-a3d0-62fb67a8985e",
  "symbol"："eth_btc",
  "current_page"："1",
  "page_length"："100",
  "sign"："16702619-0bc8-446d-a3d0-62fb67a8985e",
}
# Response
{
  "result"："true",
  "total"："1",
  "page_length"："20",
  "orders"：[
    {
      "symbol"："eth_btc",
      "amount"：5.0000,
      "create_time"：1484716198613,
      "price"：6666.0000,
      "avg_price"：0.0000,
      "type"："sell",
      "order_id"："c3f9c478-5b06-4e1e-9df9-9f84f57a446c",
      "deal_amount"：0.0000,
      "status"：0
    },
    {
      "symbol"："eth_btc",
      "amount"：10.0000,
      "create_time"：1484716151390,
      "price"：6000.0000,
      "avg_price"：6136.3895,
      "type"："sell",
      "order_id"："9ead39f5-701a-400b-b635-d7349eb0f6b4",
      "deal_amount"：10.0000,
      "status"：2
    }
  ],
  "current_page"："1",
}
```

Returns

|Field|Note|
|-|-|
|result|`true` on success or `false` on failure (For single order)|
|symbol|Trading Pair，`eth_btc`：Etherum， `zec_btc`：ZCash|
|order_id|Order ID (For single order)| 
|orders|A list of querying orders| 
|amount|required volume|
|create_time|order time|
|price|price|
|avg_price|Average strike price|
|type|`buy`：Buy<br>`sell`：Sell
|deal_amount|filled volume|
|status|Status<br>`-1`：Cancelled <br>`0`：on trading <br>`1`： filled partially <br> `2`：Filled totally <br> `3`：filled partially and cancelled   <br>`4`：Cancelling|
|current_page|Current Page|
|page_length|The page size|
|total|Total number of records.|


#### 6.Search order transaction details

Parameters:	


| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|sign|String|Yes|signature of the request|
|api_key|String|Yes|User's `api_key`|
|symbol|String|Yes|Trading Pair，`eth_btc`：Etherum， `zec_btc`：ZCash|
|order_id|String|Yes|Order ID|

Example

```javascript
# Request
POST https://www.lbkex.net/v1/order_transaction_detail.do
{
  "api_key"："16702619-0bc*********0-62fb67a8985e",
  "symbol"："eth_btc",
  "order_id"："24f7ce27-af1d-4dca-a8c1-ef1cbeec1b23",
  "sign"："16702619-0bc8-446d***********-a3d0-62fb67a8985e",
}
# Response
{
  "result"："true",
  "transaction"：[
    {
      "txUuid": "ae926ba8f6f44cae8d347a4b7ac90135",
      "orderUuid": "24f7ce27-af1d-4dca-a8c1-ef1cbeec1b23",
      "tradeType": "sell",
      "dealTime": 1562553793113,
      "dealPrice": 0.0200000000,
      "dealQuantity": 0.0001000000,
      "dealVolumePrice": 0.0000020000,
      "tradeFee": 0.0000010000,
      "tradeFeeRate": 0.000001
    }
  ]
}
```
Returns


|Field|Note|
|-|-|
|result|`true` on success or `false` on failure|
|txUuid|Trading ID|
|orderUuid|Order ID| 
|tradeType|`buy`：Buy<br>`sell`：Sell
|dealTime|Trading time| 
|dealPrice|Trading price| 
|dealQuantity|Trading volume|
|dealVolumePrice|Aggregated trading value|
|tradeFee|Transaction fee|
|tradeFeeRate|Transaction fee ratio|


#### 7.Past transaction details

Parameters:


| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|sign|String|Yes|signature of the request|
|api_key|String|Yes|User's `api_key`|
|symbol|String|Yes|Trading Pair，`eth_btc`：Etherum， `zec_btc`：ZCash|
|type|String|No|Order type sell, buy|
|start_date|String|No|Start time yyyy-mm-dd, the maximum is today, the default is yesterday|
|end_date|String|No|Finish time yyyy-mm-dd, the maximum is today, the default is today<br>The start and end date of the query window is up to 2 days|
|from|String|No|Initial transaction number inquiring|
|direct|String|No|inquire direction,The default is the 'next' which  is the positive sequence of dealing time，the 'prev' is inverted order of dealing time|
|size|String|No|Query the number of defaults to 100|

Example

```javascript
# Request
POST https://www.lbkex.net/v1/transaction_history.do
{
  "api_key"："16702619-0bc*********0-62fb67a8985e",
  "symbol"："eth_btc",
  "sign"："16702619-0bc8-446d***********-a3d0-62fb67a8985e",
}
# Response
{
  "result"："true",
  "transaction"：[
    {
      "txUuid": "ae926ba8f6f44cae8d347a4b7ac90135",
      "orderUuid": "5976ed05-6141-4fea-bcd5-179fa7a1fa56",
      "tradeType": "sell",
      "dealTime": 1562553793113,
      "dealPrice": 0.0200000000,
      "dealQuantity": 0.0001000000,
      "dealVolumePrice": 0.0000020000,
      "tradeFee": 0.0000010000,
      "tradeFeeRate": 0.000001
    },
    {
      "txUuid": "ae926ba8f6f44cae8d347a4b7ac90135",
      "orderUuid": "d65d4302-a4ff-4578-aa6b-6717758fb8c2",
      "tradeType": "buy",
      "dealTime": 1562553793113,
      "dealPrice": 0.0200000000,
      "dealQuantity": 0.0001000000,
      "dealVolumePrice": 0.0000020000,
      "tradeFee": 0.0000010000,
      "tradeFeeRate": 0.000002
    },
    {
      "txUuid": "bebadd0f953747d88d1e3181bba36f12",
      "orderUuid": "e0465949-12c2-4b87-87fa-12847a324a09",
      "tradeType": "sell",
      "dealTime": 1562575780302,
      "dealPrice": 0.0200000000,
      "dealQuantity": 0.0001000000,
      "dealVolumePrice": 0.0000020000,
      "tradeFee": 0.0000010000,
      "tradeFeeRate": 0.000001
    }
  ]
}
```
Returns	


|Field|Note|
|-|-|
|result|`true` on success or `false` on failure|
|txUuid|Trading ID|
|orderUuid|Order ID| 
|tradeType|`buy`：Buy<br>`sell`：Sell
|dealTime|Trading time| 
|dealPrice|Trading price| 
|dealQuantity|Trading volume|
|dealVolumePrice|Aggregated trading value|
|tradeFee|Transaction fee|
|tradeFeeRate|Transaction fee ratio|


#### 8. Acquiring the basic information of all trading pairs

Parameters:
None

Example


```javascript
# Request
GET https://api.lbkex.com/v1/accuracy.do

# Response
[
  {
    "priceAccuracy": "2",
    "quantityAccuracy": "4",
    "symbol": "pch_usdt"
  }
]
```

Returns

|Field|Note|
|-|-|
|symbol|Trading Pair，`eth_btc`：Etherum， `zec_btc`：ZCash|
|priceAccuracy|Price Accuracy|
|quantityAccuracy|Quantity Accuracy|

#### 9. Acquiring openning orders

Parameters:


| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|Yes|User's `api_key`|
|symbol|String|Yes|Trading Pair<br>`eth_btc`:Etherum over bitcoin； `zec_btc`:zcoin over bitcoin |
|current_page|String|Yes|Current Page|
|page_length|String|Yes|The records in a page. No more than 200.|
|sign|String|Yes|signature of the request|

Example


```javascript
# Request
POST https://api.lbkex.com/v1/orders_info_no_deal.do
{
  "api_key": "sijnvsvodnvow928492fh2938fh92348f",
  "symbol": "eth_btc",
  "current_page":"1",
  "page_length":"100",
  "sign":"iuhviuviuhviuerh92834fheifhw98f39r8g3rhf"
}


# Response
{
  'page_length': 100, 
  'current_page': 1, 
  'total': 1, 
  'result': true,
  'orders': [
    {
      'status': 0,
      'custom_id': None, 
      'order_id': 'a7de8dae-16a3-416b-8fc9-e3bb88e0d819', 
      'price': 0.015, 
      'amount': 100.0, 
      'create_time': 1527498699770, 
      'avg_price': 0.0, 
      'type': 'sell',
      'symbol': 'eth_btc', 
      'deal_amount': 0.0
    }
  ]
}
```

Returns

|Field|Note|
|-|-|
|result|`true` on success or `false` on failure (For single order)|
|symbol|Trading Pair，`eth_btc`：Etherum， `zec_btc`：ZCash|
|order_id|Order ID (For single order)| 
|orders|A list of querying orders| 
|amount|required volume|
|create_time|order time|
|price|price|
|avg_price|Average strike price|
|type|`buy`：Buy<br>`sell`：Sell
|deal_amount|filled volume|
|status|Status<br>`0`：on trading <br>`1`： filled partially|
|current_page|Current Page|
|page_length|The page size|
|total|Total number of records.|


#### 10. Exchange rate of USD/RMB (Update on 00:00 everyday)

Parameters

None

```javascript
# Request
GET https://api.lbkex.com/v1/usdToCny.do

# Response
{"USD2CNY":"6.4801"}
```

Returns

|Field|Note|
|-|-|
|USD2CNY |Exchange rate of USD/RMB|

#### 11. Withdraw configurations

Parameters

| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|assetCode|String|No|Code of the asset|

Example
```javascript
# Request
GET https://api.lbkex.com/v1/withdrawConfigs.do

# Response
[{'assetCode': 'eth', 'min': '0.01', 'canWithDraw': True, 'fee': '0.01'}]
```

|Field|Note|
|-|-|
|USD2CNY |Exchange rate of USD/RMB|
|assetCode |Code of token|
|min |Minimum amount to withdraw|
|canWithDraw |Whether the currency can be withdrawn|
|fee |Charged fee for withdrawal（amount）|


#### 12. Withdraw (IP binding is required.)

Parameters

| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|Yes|User's `api_key`|
|account|String|Yes|Address,if internal,this is email or mobile account|
|assetCode|String|Yes|Asset Code|
|amount|String|Yes| Amount（Must be integer for NEO）|
|memo|String|No|Required for BTS and/or DCT|
|mark|String|No|User's memo.(length <= 255)|
|sign|String|Yes|signature of the request|
|type|String|No|withdraw type，1:internal，2：normal|

Example

```javascript
# Request
POST https://api.lbkex.com/v1/withdraw.do

# Response
{'result': 'true', 'withdrawId': 90082, 'fee':0.001}
```

Returns

|Field|Note|
|-|-|
|result |true：success，false：failed|
|withdrawId |Current withdrawal ID|
|fee |Withdrawal fee（amount）|



#### 13. Revoke Withdraw (IP binding is required.)

Parameters

| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|Yes|User's `api_key`|
|withdrawId |Current withdrawal ID|
|sign|String|Yes|signature of the request|


Example

```javascript
# Request
POST https://api.lbkex.com/v1/withdrawCancel.do

# Response
{'result': 'true', 'withdrawId': '90083'}
```

Returns

|Field|Note|
|-|-|
|result |true：success，false：failed|
|withdrawId |Current withdrawal ID|


#### 14. Withdrawal record (IP binding is required.)


| Parameter|	Type|	Required|	Note|
| :-----    | :-----   | :-----    | :-----   |
|api_key|String|Yes|User's `api_key`|
|assetCode|String|Yes| |
|status|String|Yes|Status: <br> 0: All, 1: applying. 2. Revoked. 3. Failed. 4. Completed )|
|pageNo|String|Yes|Current Page. Default 1.|
|pageSize|String|Yes|The records in a page. No more than 100. Default 20|
|sign|String|Yes|signature of the request|

Example

```javascript
# Request
POST https://api.lbkex.com/v1/withdraws.do

# Response
{
	'totalPages': 1,
	'pageSize': 20,
	'pageNo': 1
	'list': [{
		'amount': 20.0,
		'assetCode': 'btc',
		'address': 'erfwergertghrehyrhethyryuj',
		'fee': 0.0,
		'id': 89686,
		'time': 1525750028000,
		'txHash': '',
		'status': '2'
	}, {
		'amount': 335.0,
		'assetCode': 'btc',
		'address': 'erfwergertghrehyrhethyryuj',
		'fee': 0.0,
		'id': 89687,
		'time': 1525767979000,
		'txHash': '',
		'status': '2'
	}
	....]
}
```

Return

|Field|Note|
|-|-|
|totalPage |Total Number of Pages|
|pageNo|Current Page. |
|pageSize|The records in a page. |
|list| List data（id: coin withdrawal ID，assetCode: Asset Code，address: coin withdrawal address，amount：withdrawal amount fee：withdrawal fee，time：wtihdrawal time，txHash：withdrawal hash， status：Coin withdrawal status）|





# WebSocket API (Market Data) 

## Start

WebSocket  protocol which achieves full-duplex communications over a  single TCP connection between client and server is based on a new network protocol of the TCP. Server sends information to client, reducing unnecessary overhead such as frequent authentication. It greatest advantage includes that：

> - Request header is small in size (2 Bytes) .
> - The server no longer passively responses after receiving the client's request, but actively pushes the new data to the client.
> - There is no need to establish and close TCP connection repeatedly, so it saves bandwidth and server resources.



## Request & subscription instruction

* URL: `wss://www.lbkex.net/ws/V2/`

* Hearbeat（ping/pong）

    To prevent botch links and reduce server load, server will send a "Ping" message periodically to client connections. When client recieves the "Ping" message, it should response immediately. If a client responds nothing to macth the "Ping" message in one minute,  server will close the connection to the client. Meanwhile client can also send a "Ping" message to server to check whether the connection is working. After server recieves the "Ping" message, it should response with a "Pong" message to match the "Ping".

    **Eg:**

    ```javascript
    
    # ping
    {
        "action":"ping",
        "ping":"0ca8f854-7ba7-4341-9d86-d3327e52804e"
    }
    # pong
    {
        "action":"pong",
        "pong":"0ca8f854-7ba7-4341-9d86-d3327e52804e"
    }
    ```

    where the value of the key "pong" in the "Pong" message should equal to the value of the key "ping" in correspond "Ping" message.



* Subscription/Unsubscription

    Each subscribed data should include one subscribed field at least which specifies the data type of the subscription. Data types that can be subscribed now includes：kbar, tick, depth, trade. Each subscription needs a pair field to specify the trading pair subscribed, which is concatenated with a underline (_). After successful subscription Websocket client receives the updated message sent from server as soon as the subscribed data is updated. 
    
1. Subscription of K-line Data
  

**Parameter:**
    
|Parameter|Parameter Type|Required|Description|
| :-----    | :-----   | :-----    | :-----   |
|action|String|Y|Action requested: `subscribe` or `unsubscribe`|
|subscribe|String|Y|`kbar`|
|kbar|String|Y|To subscribe to k-line types<br>`1min`: 1 minute<br>`5min`: 5 minutes<br>`15min`: 15 minutes<br>`30min`: 30 minutes<br>`1hr`: 1 hour<br>`4hr`: 4 hours<br>`day`: 1 day<br>`week`: 1 week<br>`month`: 1 month<br>`year`: 1 year|
|pair|String|Y|Trading pair:`eth_btc`|

**Eg:**
    
```javascript
    
    # Subscription request
    {
        "action":"subscribe",
        "subscribe":"kbar",
        "kbar":"5min",
        "pair":"eth_btc"
    }
    # Push data
    {
        "kbar":{
            "a":64.32991311,
            "c":0.02590293,
            "t":"2019-06-28T17:45:00.000",
            "v":2481.1912,
            "h":0.02601247,
            "slot":"5min",
            "l":0.02587925,
            "n":272,
            "o":0.02595196
        },
        "type":"kbar",
        "pair":"eth_btc",
        "SERVER":"V2",
        "TS":"2019-06-28T17:49:22.722"
    }
```

**Return value specification:**
    
|Parameters|Parameters Type|Description|
| :-----    | :-----  | :-----   |
|t|String|K-line updates the time|
|o|BigDecimal|Open price|
|h|BigDecimal|Highest price|
|l|BigDecimal|Lowest price|
|c|BigDecimal|Close price|
|v|BigDecimal|Trading volume|
|a|BigDecimal|Aggregated turnover (summation of price times volume for each trade)|
|n|BigDecimal|Number of trades|
|slot|String|K-line type|



2. Market Depth
       

**Parameter:**
    
|Parameters|Parameters Type|Required|Description|
| :-----    | :-----   | :-----    | :-----   |
|action|String|Y|Type of action requested:`subscribe`,`unsubscribe`|
|subscribe|String|Y|`depth`|
|depth|String|Y|Pro-choise:10/50/100|
|pair|String|Y|Trading pair:`eth_btc`|

**Eg:**

```javascript
    # Subscription request
    {
        "action":"subscribe",
        "subscribe":"depth",
        "depth":"100",
        "pair":"eth_btc"
    }
    # Push data
    {
        "depth":{
            "asks":[
                [
                    0.0252,
                    0.5833
                ],
                [
                    0.025215,
                    4.377
                ],
                ...
            ],
            "bids":[
                [
                    0.025135,
                    3.962
                ],
                [
                    0.025134,
                    3.46
                ],
                ...
            ]
        },
        "count":100,
        "type":"depth",
        "pair":"eth_btc",
        "SERVER":"V2",
        "TS":"2019-06-28T17:49:22.722"
    }
```

**Return value specification:**

|Parameters|Parameters Type|Description|
| :-----    | :-----  | :-----   |
|asks|List|Selling side: list.get(0): delegated price, list.get(1): delegated quantity|
|bids|List|Buying side|


3. Trade record
  

**Parameter:**
    
|Parameters|Parameters Type|Required|Description|
| :-----    | :-----   | :-----    | :-----   |
|action|String|Y|Action requested: `subscribe` or `unsubscribe`|
|subscribe|String|Y|`trade`|
|pair|String|Y|Trading pair:`eth_btc`|


**Eg:**
    
```javascript
    
    # Subscription request
    {
        "action":"subscribe",
        "subscribe":"trade",
        "pair":"eth_btc"
    }
    # Push data
    {
        "trade":{
            "volume":6.3607,
            "amount":77148.9303,
            "price":12129,
            "direction":"sell",
            "TS":"2019-06-28T19:55:49.460"
        },
        "type":"trade",
        "pair":"btc_usdt",
        "SERVER":"V2",
        "TS":"2019-06-28T19:55:49.466"
    }
```

**Return value specification:**
    

|Parameters|Parameters Type|Description|
| :-----    | :-----  | :-----   |
|amount|String|Recent trading volume|
|price|Integer|Trade price|
|volumePrice|String|Aggregated turnover|
|direction|String|`sell`,`buy`|
|TS|String|Deal time|



4. Market


**Parameter:**
    
|Parameters|Parameters Type|Required|Description|
| :-----    | :-----   | :-----    | :-----   |
|action|String|Y|Action requested:`subscribe`,`unsubscribe`|
|subscribe|String|Y|`tick`|
|pair|String|Y|Trading pair:`eth_btc`|


**Eg:**
    
```javascript
    
    # Subscription request
    {
        "action":"subscribe",
        "subscribe":"tick",
        "pair":"eth_btc"
    }
    # ush data
    {
        "tick":{
            "to_cny":76643.5,
            "high":0.02719761,
            "vol":497529.7686,
            "low":0.02603071,
            "change":2.54,
            "usd":299.12,
            "to_usd":11083.66,
            "dir":"sell",
            "turnover":13224.0186,
            "latest":0.02698749,
            "cny":2068.41
        },
        "type":"tick",
        "pair":"eth_btc",
        "SERVER":"V2",
        "TS":"2019-07-01T11:33:55.188"
    }
```

**Return value specification:**
    
|Parameters|Parameters Type|Description|
| :-----    | :-----  | :-----   |
|high|BigDecimal|Highest price in last 24 hours|
|low|BigDecimal|Lowest price in last 24 hours|
|latest|BigDecimal|Lastest traded price|
|vol|BigDecimal|Trading volume|
|turnover|BigDecimal|Aggregated turnover (summation of price times volume for each trade)|
|to_cny|BigDecimal|Such as `eth_btc`, convert btc into cny|
|to_usd|BigDecimal|Such as `eth_btc`, convert btc into usd|
|cny|BigDecimal|Such as `eth_btc`, convert eth into cny|
|usd|BigDecimal|Such as `eth_btc`, convert eth into usd|
|dir|String|`sell`, `buy`|
|change|BigDecimal|Price limit in last 24 hours|



**Unsubscribe example:**
    
```javascript
    
    #Unsubscribe from k-line
    {
        "action":"unsubscribe",
        "subscribe":"kbar",
        "kbar":"5min",
        "pair":"eth_btc"
    }
    #Unsubscribe from deep subscription
    {
        "action":"unsubscribe",
        "subscribe":"depth",
        "depth":"100",
        "pair":"eth_btc"
    }
```


* Request data

    One-time request data is supported by Websocket server.

1. One-time request to get k-line needs extra parameters defined in following：

**Parameter:**

|Parameters|Parameters Type|Required|Description|
| :-----    | :-----   | :-----    | :-----   |
|start|String|fasle|Start time. Accept 2 formats, such as `2018-08-03T17:32:00` (beijing time), another timestamp, such as `1533288720` (Accurate to second)|
|end|String|false|Deadline|
|size|String|false|Number of kbars|

2. One-time request to get trade records needs extra parameters defined in following：
       
**Parameter:**
       

|Parameters|Parameters Type|Required|Description|
| :-----    | :-----   | :-----    | :-----   |
|size|String|Y|Number of trades|


**Eg:**
    
```javascript
    
    # Get k-line data Request
    {
        "action":"request",
        "request":"kbar",
        "kbar":"5min",
        "pair":"eth_btc",
        "start":"2018-08-03T17:32:00",
        "end":"2018-08-05T17:32:00",
        "size":"576"
    }
    # Get depth data Request
    {
        "action":"request",
        "request":"depth",
        "depth":"100",
        "pair":"eth_btc"
    }
    # Get transaction data Request
    {
        "action":"request",
        "request":"trade",
        "pair":"eth_btc",
        "size":"100"
    }
    # Get market data Request
    {
        "action":"request",
        "request":"tick",
        "pair":"eth_btc"
    }
```


