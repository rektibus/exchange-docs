Spot API documentation
Export
v3.3
Overview
Migration from v3.2 to v3.3
We are updating several order-related API endpoints to improve consistency and clarity in size-related fields. Please review the following changes carefully, as some existing fields will be deprecated and replaced with new ones.

Updated Fields for Order Actions
For the following endpoints, the fields size, fillSize, originalSize and remainingSize will be deprecated and replaced with the following:

originalOrderBaseSize
originalOrderQuoteSize
currentOrderBaseSize
currentOrderQuoteSize
remainingOrderBaseSize
remainingOrderQuoteSize
filledBaseSize
totalFilledBaseSize
orderCurrency ("base" or "quote")
Affected Endpoints

Create New Order
Both POST /api/v3.3/order and POST /api/v3.3/order/peg
Amend Order
Cancel Order
Updated Fields for Order Query Endpoints
To improve data structure clarity and consistency, the following legacy fields will be deprecated:

size
filledSize
remainingSize
In some endpoints: fillSize as well
They will be replaced with the following enhanced fields:

originalOrderBaseSize
originalOrderQuoteSize
currentOrderBaseSize
currentOrderQuoteSize
remainingOrderBaseSize
remainingOrderQuoteSize
totalFilledBaseSize
orderCurrency ("base" or "quote")
Affected Endpoints

Query Order - Replacing size, filledSize, remainingSize
Query Open Orders - Replacing size, fillSize, filledSize, remainingSize
Generating API Key
You will need to create an API key on the platform before you can use authenticated APIs. To create API keys, you can follow the steps below:

Login with your username / email and password into the website
Click on Account on the top right hand corner
Select the API tab
Click on New API button to create an API key and passphrase. (Note: the passphrase will only appear once)
Use your API key and passphrase to construct a signature.
Authentication
API Key (request-api)
Parameter Name: request-api, in: header. API key is obtained from platform as a string
API Key (request-nonce)
Parameter Name: request-nonce, in: header. Representation of current timestamp (epoch milliseconds) in long format
API Key (request-sign)
Parameter Name: request-sign, in: header. A composite signature produced based on the following algorithm: Signature=HMAC.Sha384 (secretKey, (path + request-nonce + body)) (note: body = '' when no data):
Example 1: Query Open Order

Endpoint to query open order is /api/v3.2/user/open_orders
Assume we have the values as follows (notice: the query parameters are excluded from encrypted text):
request-nonce: 1677663813822
request-api:49e9d289fb926ed26aaa971ed4edabc93b675d2b316a7b22d76567a3c5c9f0a6
secret:848db84ac252b6726e5f6e7a711d9c96d9fd77d020151b45839a5b59c37203bx
path: /api/v3.2/user/open_orders
body: (empty)
encrypted text:/api/v3.2/user/open_orders1677663813822
Generated signature will be:
request-sign:5affbcc0813540cb325c05ae632bf31ab7425b0744f3904719093d2cdbcebe7456aaa26c99659b3c7243edd32091a827
cURL example:
curl --location --request GET 'https://api.altex.mn/spot/api/v3.2/user/open_orders?symbol=BTC-USD' \
--header 'request-api: 49e9d289fb926ed26aaa971ed4edabc93b675d2b316a7b22d76567a3c5c9f0a6' \
--header 'request-nonce: 1677663813822' \
--header 'request-sign: 5affbcc0813540cb325c05ae632bf31ab7425b0744f3904719093d2cdbcebe7456aaa26c99659b3c7243edd32091a827'
Example 2: Place an order

Endpoint to place an order is /api/v3.2/order
Assume we have the values as follows (notice: the parameters in the request are case-sensitive):
request-nonce: 1677662848553
request-api:49e9d289fb926ed26aaa971ed4edabc93b675d2b316a7b22d76567a3c5c9f0a6
secret:848db84ac252b6726e5f6e7a711d9c96d9fd77d020151b45839a5b59c37203bx
path: /api/v3.2/order
body: {"postOnly":false,"price":8500.0,"side":"BUY","size":0.002,"stopPrice":0.0,"symbol":"BTC-USD","time_in_force":"GTC","trailValue":0.0,"triggerPrice":0.0,"txType":"LIMIT","type":"LIMIT"}
encrypted text:/api/v3.2/order1677662848553{"postOnly":false,"price":8500,"side":"BUY","size":0.002,"stopPrice":0,"symbol":"BTC-USD","time_in_force":"GTC","trailValue":0,"triggerPrice":0,"txType":"LIMIT","type":"LIMIT"}
Generated signature will be:
request-sign:b38ae8415eb1b008daf60234675c2d1e9992e26e18b1f193f055d870d5c158fc8f17e37c616b3307abc939a72a8867cf
cURL example:
curl --location --request POST 'https://api.altex.mn/spot/api/v3.2/order' \
--header 'request-api: 49e9d289fb926ed26aaa971ed4edabc93b675d2b316a7b22d76567a3c5c9f0a6' \
--header 'request-nonce: 1677662848553' \
--header 'request-sign: b38ae8415eb1b008daf60234675c2d1e9992e26e18b1f193f055d870d5c158fc8f17e37c616b3307abc939a72a8867cf' \
--header 'Content-Type: application/json' \
--data-raw '{"postOnly":false,"price":8500,"side":"BUY","size":0.002,"stopPrice":0,"symbol":"BTC-USD","time_in_force":"GTC","trailValue":0,"triggerPrice":0,"txType":"LIMIT","type":"LIMIT"}'
Rate Limits
The following rate limits are enforced:
Rate limits for the platform is as follows:

Query

Per API: 15 requests/second
Per User: 30 requests/second
Orders

Per API: 75 requests/second
Per User: 75 requests/second
API Status Codes
Each API will return one of the following HTTP status:

Code	Description
200	API request was successful, refer to the specific API response for expected payload
400	Bad Request. Server will not process this request. This is usually due to invalid parameters sent in request
401	Unauthorized request. Server will not process this request as it does not have valid authentication credentials
403	Forbidden request. Credentials were provided but they were insufficient to perform the request
404	Not found. Indicates that the server understood the request but could not find a correct representation for the target resource
405	Method not allowed. Indicates that the request method is not known to the requested server
408	Request timeout. Indicates that the server did not complete the request. API timeouts are set at 30secs
429	Too many requests. Indicates that the client has exceeded the rates limits set by the server. Refer to Rate Limits for more details
500	Internal server error. Indicates that the server encountered an unexpected condition resulting in not being able to fulfill the request
API Enum
When connecting up the API, you will come across number codes that represents different states or status types in platform. The following section provides a list of codes that you are expecting to see.

Code	Description
1	MARKET_UNAVAILABLE = Futures market is unavailable
2	ORDER_INSERTED = Order is inserted successfully
4	ORDER_FULLY_TRANSACTED = Order is fully transacted
5	ORDER_PARTIALLY_TRANSACTED = Order is partially transacted
6	ORDER_CANCELLED = ExecuteOrder/placeOrder/matchOrder fail.
When user send an spot postOnly order and received reject status, maybe:
- Insert order to orderBook fail, because order will transact before insert to orderBook. (postOnly meanings insert first)
- FoK order execute fail, because FoK not allow partially transacted. Order transact with user self, because order not allow self trade.
When user send an futures postOnly order and received reject status. maybe:
- Insert order to orderBook fail, because order will transact before insert to orderBook. (postOnly meanings insert first)
- Insert order to orderBook fail, because order will belong to spam order. (postOnly not allow with spam order)
- FoK order execute fail, because FoK not allow partially transacted. Order transact with user self, because order not allow self trade.
7	ORDER_REFUNDED = Turn user money back to user coin wallet market order without any transacted will get refund. or self traded
8	INSUFFICIENT_BALANCE = Insufficient balance in account
9	TRIGGER_INSERTED = Trigger Order is inserted successfully
10	TRIGGER_ACTIVATED = Trigger Order is activated successfully
11	ERROR_INVALID_CURRENCY
12	ERROR_UPDATE_RISK_LIMIT = Error in updating risk limit
13	ERROR_INVALID_LEVERAGE
15	ORDER_REJECTED = PreCheck fail, then reject.
When user amendOrder and received reject status, maybe:
- Update order price fail, because order not fund.
- Update trigger price fail, because order not fund.
- Update order amount fail, because order not fund. ...
When user cancelOrder and received reject status, maybe:
- Market not fund. ...
When user placeOrder and received reject status, maybe:
- Internal timeout. user try to use same clOrderId with different order at same time.
- Update order amount fail, because order not fund. send closePositionOrder but without any position.
16	ORDER_NOTFOUND = Order is not found with the order ID or clOrderID provided
17	REQUEST_FAILED = Failed to complete the request, please check order status
21	FREEZE_SUCCESSFUL
27	TRANSFER_SUCCESSFUL = Transfer funds between futures and spot is successful
28	TRANSFER_UNSUCCESSFUL = Transfer funds between spot and futures is unsuccessful
29	QUERY_GET_ORDERS
31	QUERY_GET_POSITIONS
33	QUERY_GET_ALL_POSITIONS_ORDERS
34	QUERY_WALLET
36	QUERY_FUTURES_MARGIN
41	ERROR_INVALID_RISK_LIMIT = Invalid risk limit was specified
51	QUERY_GET_ORDERS_WITH_LIMIT
64	STATUS_LIQUIDATION = Account is undergoing liquidation
65	ORDER_ACTIVE = Order is active
66	MODE_BUY
76	ORDER_TYPE_LIMIT = Limit order
77	ORDER_TYPE_MARKET = Market order
80	ORDER_TYPE_PEG = Peg/Algo order
81	ORDER_TYPE_OTC = Otc order
83	MODE_SELL
85	ORDER_PROCESSING = Order is inactive
88	ORDER_INACTIVE = Order is inactive
101	FUTURES_ORDER_PRICE_OUTSIDE_LIQUIDATION_PRICE = Futures order is outside of liquidation price
110	FUTURES_FUNDING
123	AMEND_ORDER = Order amended
124	UNFREEZE_SUCCESSFUL
300	ERROR_MAX_ORDER_SIZE_EXCEEDED
301	ERROR_INVALID_ORDER_SIZE
302	ERROR_INVALID_ORDER_PRICE
303	ERROR_RATE_LIMITS_EXCEEDED
304	ERROR_MAX_OPEN_ORDER_EXCEEDED
1003	ORDER_LIQUIDATION = Order is undergoing liquidation
1004	ORDER_ADL = Order is undergoing ADL
30000	OTC_ORDER_QUERY
30001	OTC_ORDER_QUOTE
30007	OTC_ORDER_COMPLETE_SUCCESS
30410	BLOCK_TRADE_COMPLETE_SUCCESS
Error Code
When the request encounter exception ,it will return one of the following error code.

Code	Description
-8103	ORDER_BELONGS_TO_VENDOR = The order belongs to the vendor
-7017	NOT_READY_TO_SELL = Not ready to sell
-7016	COIN_FUNCTION_SWITCH_IS_OFF = This coin function is disabled
-7006	COIN_PAIR_IS_NOT_EXISTS_ERROR = Coin pair does not exist
-2023	UNKNOWN_CURRENCY = Unknown currency
4503	TRADE_CREATE_ORDER_ERROR = Create order failed
80001	API_MARKET_NOT_EXISTS = Market does not exist
80003	API_PARAMETER_ORDER_TAG_WRONG = 'tag' is invalid, must be alphanumeric
80004	API_PARAMETER_ORDER_TIME_IN_FORCE_WRONG = 'time_in_force' is invalid
80005	API_PARAMETER_ORDER_PRODUCT_ID_WRONG = 'product_id' is invalid
80006	API_PARAMETER_ORDER_TYPE_WRONG = order type is invalid
80007	API_PARAMETER_ORDER_SIDE_WRONG = parameter 'side' invalid
80009	API_PARAMETER_ORDER_PRODUCT_ID_NULL = parameter 'product_id' is required
80010	API_PARAMETER_ORDER_PRICE_AMOUNT_NULL = parameter 'price' and 'amount' are both required
80011	API_PARAMETER_ORDER_SIDE_NULL = parameter 'side' is required
80012	API_PARAMETER_ORDER_PRICE_NULL = parameter 'price' is required
80013	API_PARAMETER_ORDER_AMOUNT_NULL = parameter 'amount' is required
80014	API_PARAMETER_TIME_PERIOD_WRONG = parameter 'timePeriod' only accept 60 to 86400
80016	API_PARAMETER_MAX_SPREAD_WRONG = parameter 'maxSpread' only accept 0 to 1
80017	API_PARAMETER_MAX_DISTANCE_THROUGH_BOOK_WRONG = parameter 'maxDistanceThroughBook' only accept 0 to 1










Market Summary
get
https://api.altex.mn/spot/api/v3.3/market_summary
Gets market summary information. If no symbol parameter is sent, then all markets will be retrieved.

Request
Query Parameters
symbol
string
market symbol

Responses
200
Body

application/json

application/json
responses
/
200
/
[]
.
futures
array of:
symbol
string
Market symbol

last
number
Last price

lowestAsk
number
Lowest ask price in the orderbook

highestBid
number
Highest bid price in the orderbook

percentageChange
number
Percentage change against the price within the last 24hours

volume
number
Transacted volume

high24Hr
number
Highest price over the last 24hours

low24Hr
number
Lowest price over the last 24hours

base
string
Base currency

quote
string
Quote currency

active
boolean
Indicator if market is active

size
number
Transacted size

minValidPrice
number
Minimum valid price

minPriceIncrement
number
Price increment

minOrderSize
number
Minimum tick size

maxOrderSize
number
Maximum order size

minSizeIncrement
number
Tick size

openInterest
number
openInterestUSD
number
contractStart
number
contractEnd
number
timeBasedContract
boolean
openTime
number
Market opening time

closeTime
number
Market closing time

startMatching
number
Matching start time

inactiveTime
number
Time where market is inactive

fundingRate
number
contractSize
number
maxPosition
number
minRiskLimit
number
maxRiskLimit
number
availableSettlement
array
futures
boolean
Indicator if symbol is a futures contract





Charting Data
get
https://api.altex.mn/spot/api/v3.3/ohlcv
Gets candle stick charting data. Default of 300 data points will be returned at any one time.

Request
Query Parameters
resolution
integer
required
Supported resolution is:
1: 1min
5: 5 minutes
15: 15 minutes
30: 30 minutes
60: 60 minutes
240: 4 hours
360: 6 hours
1440: 1 day
10080: 1 week
43200: 1 month

Default:
1
symbol
string
required
market symbol

Default:
BTC-USD
end
integer
ending time (eg. 1624987283000)

start
integer
starting time (eg. 1624987283000)

Responses
200
Body

application/json

application/json
array[array]
number
0: Unix Time
1: Open Price
2: High Price
3: Low Price
4: Closing Price
5: Volume (Notional value by quote currency, e.g. USD)

resolution*
:
1
symbol*
:
BTC-USD
end
:
integer
start
:
integer
Send API Request
curl --request GET \
  --url 'https://api.altex.mn/spot/api/v3.3/ohlcv?symbol=BTC-USD&resolution=1' \
  --header 'Accept: application/json'
[
  [
    1624987380,
    36477,
    36477,
    36473.5,
    36473.5,
    693.049
  ],
  [
    1624987320,
    36476.5,
    36481.5,
    36466,
    36466,
    2370.8095
  ]
]










Query Market price
get
https://api.altex.mn/spot/api/v3.3/price
Retrieve current prices on the platform. If no symbol specified, all symbols will be returned.

Request
Query Parameters
symbol
string
required
Market symbol

Default:
BTC-USD
Responses
200
Body

application/json

application/json
array of:
symbol
string
Market symbol

indexPrice
number
Index price

lastPrice
number
Last transacted price

markPrice
number
Not valid for spot

symbol*
:
BTC-USD
Send API Request
curl --request GET \
  --url 'https://api.altex.mn/spot/api/v3.3/price?symbol=BTC-USD' \
  --header 'Accept: application/json'
[
  {
    "symbol": "BTC-USD",
    "indexPrice": 36288.949684967,
    "lastPrice": 36286.5,
    "markPrice": 0
  }
]





Orderbook (By grouping)
get
https://api.altex.mn/spot/api/v3.3/orderbook
Retrieves a Level 2 snapshot of the orderbook and allows you to specify grouping and also bid / asks depth

Request
Query Parameters
symbol
string
required
Market symbol

Default:
BTC-USD
group
string
Orderbook grouping. Valid values are:
0-9 where 0 indicates level 0 grouping (eg. for BTC, it will be 0.5) Level 1 grouping for BTC would be 1

limit_asks
string
Orderbook depth on the ask side

limit_bids
string
Orderbook depth on the bid side

Responses
200
Body

application/json

application/json
symbol
string
required
Market symbol

buyQuote
array[object]
required
Array of Buy quotes

price
number
required
order price

size
number
required
order size

sellQuote
array[object]
required
Array of Sell quotes

price
number
required
order price

size
number
required
order size

timestamp
number
required
Timestamp of orderbook

symbol*
:
BTC-USD
group
:
string
limit_asks
:
string
limit_bids
:
string
Send API Request
curl --request GET \
  --url 'https://api.altex.mn/spot/api/v3.3/orderbook?symbol=BTC-USD' \
  --header 'Accept: application/json'
{
  "symbol": "BTC-USD",
  "buyQuote": [
    {
      "price": "36371.0",
      "size": "0.01485"
    }
  ],
  "sellQuote": [
    {
      "price": "36380.5",
      "size": "0.01782"
    }
  ],
  "timestamp": 1624989459489
}







Orderbook
get
https://api.altex.mn/spot/api/v3.3/orderbook/L2
Retrieves a Level 2 snapshot of the orderbook and allows you to specify grouping and also bid / asks depth

Request
Query Parameters
symbol
string
required
Market symbol

Default:
BTC-USD
depth
integer
Orderbook depth

Responses
200
Body

application/json

application/json
symbol
string
Market symbol

buyQuote
array[object]
Array of Buy quotes

price
string
order price

size
string
order size

timestamp
integer
Timestamp of orderbook

depth
integer
Order depth

symbol*
:
BTC-USD
depth
:
integer
Send API Request
curl --request GET \
  --url 'https://api.altex.mn/spot/api/v3.3/orderbook/L2?symbol=BTC-USD' \
  --header 'Accept: application/json'
{
  "symbol": "BTC-USD",
  "buyQuote": [
    {
      "price": "19209.6",
      "size": "1.40000"
    },
    {
      "price": "19208.6",
      "size": "2.30000"
    }
  ],
  "timestamp": 1666163719195,
  "depth": 0
}







Query Trades Fills
get
https://api.altex.mn/spot/api/v3.3/trades
Get trade fills for the market specified by `symbol`

maximum days of history records:
Time Interval	Maximum Days	Explanation
startTime / endTime	30	Maximum 30 days within the specified interval
startTime / -	3	If the end time is not specified, then 3 days after the start time
- / endTime	3	If the start time is not specified, then 3 days before the end time
- / -	3	If neither start nor end time is specified, then 3 days before the current time
Request
Query Parameters
symbol
string
required
Market symbol

Default:
BTC-USD
count
integer
Number of records to return, defaults to 10

endTime
integer
Ending time (eg. 1624987283000)

startTime
integer
Starting time (eg. 1624987283000)

Responses
200
Body

application/json

application/json
array of:
price
number
Transacted price

size
number
Transacted size

side
string
Trade side. Values are: [BUY, SELL]

symbol
string
Market symbol

serialId
number
Serial Id, running sequence number

timestamp
number
Transacted timestamp

symbol*
:
BTC-USD
count
:
integer
endTime
:
integer
startTime
:
integer
Send API Request
curl --request GET \
  --url 'https://api.altex.mn/spot/api/v3.3/trades?symbol=BTC-USD' \
  --header 'Accept: application/json'
[
  {
    "price": 36164,
    "size": 0.035,
    "side": "SELL",
    "symbol": "BTC-USD",
    "serialId": "<Serial ID>",
    "timestamp": 1624990097000
  }
]



Query Server Time
get
https://api.altex.mn/spot/api/v3.3/time
Gets server time

Responses
200
Body

application/json

application/json
iso
number
required
Time in YYYY-MM-DDTHH24:MI:SS.Z format

epoch
number
required
Returns epoch timestamp

Send API Request
curl --request GET \
  --url https://api.altex.mn/spot/api/v3.3/time \
  --header 'Accept: application/json'
{
  "iso": "2021-06-29T18:14:30.886Z",
  "epoch": 1624990470
}












Web Socket API documentation 1.0.0
Overview
Generating API Key
You will need to create an API key on the platform before you can use authenticated APIs. To create API keys, you can follow the steps below:

Login with your username / email and password into the website
Click on Account on the top right hand corner
Select the API tab
Click on New API button to create an API key and passphrase. (Note: the passphrase will only appear once)
Use your API key and passphrase to construct a signature.
Endpoints - wss://ws.altex.mn
Authentication
The WS Auth requires to send a payload with the Auth data in the Args key after doing the connection and before sending any other data. see Spot Authentication and Futures Authentication for details.

Status Code = 400
You might get 400 status code due to abnormal usage and we will block you for 10 minutes.

Ping/Pong handling
For connectivity checking, we will send a ping frame message every 3 minutes and you will need to respond pong frame message to us for checking, if the pong frame message doesn't correctly respond to us in 10 minutes, we will force to disconnect the connection.

#Spot
#Spot Orderbook Streaming
#Futures
#Futures Orderbook Streaming
#OTC
#Streaming
Operations
SUB Subscription
Endpoint: /ws/spot

Subscribe to a topic

#Spot
Accepts the following message:

Spot-Subscription
To subscribe to a websocket feed

PayloadExpand all
object oneOfuid: subscription
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "topic-name"
  ]
}
#2 Example - Response
Response Contents

{
  "event": "subscribe",
  "channel": [
    "topic-name"
  ]
}
#3 Example - Failed Response
Response Contents

{
  "event": "subscribe",
  "channel": []
}
SUB Public Trade Fills
Public Trade Fills

Endpoint: /ws/spot

#Spot
Accepts the following message:

Spot-Public-Trade-Fills
Subscribe to recent trade feed for a market. The topic will be tradeHistoryApi:<market> where <market> is the market symbol.
*** response content ***

PayloadExpand all
object oneOfuid: publicTradeFills
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "tradeHistoryApi:BTC-USD"
  ]
}
#2 Example - Response
Response Contents

{
  "topic": "tradeHistoryApi:BTC-USD",
  "data": [
    {
      "symbol": "BTC-USD",
      "side": "SELL",
      "size": 0.007,
      "price": 5302.8,
      "tradeId": "<Trade Sequence ID>",
      "timestamp": 1584446020295
    }
  ]
}
SUB Authentication
Spot Authentication

Endpoint: /ws/spot

#Spot
Accepts the following message:

Spot-Authentication
Authenticate the websocket session to subscribe to authenticated websocket topics. Assume we have values as follows:
- request-nonce: 1624985375123
- request-api:4e9536c79f0fdd72bf04f2430982d3f61d9d76c996f0175bbba470d69d59816x
- secret:848db84ac252b6726e5f6e7a711d9c96d9fd77d020151b45839a5b59c37203bx

Our subscription request will be:

Request Parameters
Below details the arguments needed to be sent in.

Generating a signature
echo -n "/ws/spot1624985375123" | openssl dgst -sha384 -hmac "848db84ac252b6726e5f6e7a711d9c96d9fd77d020151b45839a5b59c37203bx"
(stdin)=c410d38c681579adb335885800cff24c66171b7cc8376cfe43da1408c581748156b89bcc5a115bb496413bda481139fb


PayloadExpand all
object oneOfuid: authentication
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "login",
  "args": [
    "4e9536c79f0fdd72bf04f2430982d3f61d9d76c996f0175bbba470d69d59816x",
    "1624985375123",
    "c410d38c681579adb335885800cff24c66171b7cc8376cfe43da1408c581748156b89bcc5a115bb496413bda481139fb"
  ]
}
#2 Example - Response
Response Contents

{
  "event": "login",
  "success": true
}
SUB Notifications
Spot Notifications

Endpoint: /ws/spot

#Spot
Accepts the following message:

Spot-Notifications
Receive trade notifications by subscribing to the topic notificationApiV3. The websocket feed will push trade level notifications to the subscriber. If topic is subscribed without being authenticated, no messages will be sent.
*** response content ***

PayloadExpand all
object oneOfuid: notification
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "notificationApiV3"
  ]
}
#2 Example - Response
Response Contents

{
  "topic": "notificationApiV3",
  "data": [
    {
      "symbol": "Market Symbol (eg. BTC-USD)",
      "orderID": "internal order ID",
      "side": "BUY",
      "orderType": null,
      "price": "Order price or transacted price",
      "originalOrderBaseSize": 1,
      "originalOrderQuoteSize": 1,
      "currentOrderBaseSize": 1,
      "currentOrderQuoteSize": 1,
      "filledBaseSize": 1,
      "totalFilledBaseSize": 1,
      "remainingBaseSize": 1,
      "remainingQuoteSize": 1,
      "orderCurrency": "base",
      "avgFilledPrice": 35000,
      "status": "<Refer to Status description on the left>",
      "clOrderID": "<Client order ID>",
      "maker": "<Maker flag, if true indicates that trade is a maker trade>",
      "stealth": 1,
      "timestamp": 1624985375123,
      "pegPriceDeviation": "Indicate the deviation percentage. Valid for only algo orders.",
      "remainingSize": "<Remaining size on the order>",
      "time_in_force": "<Time where this order is valid>",
      "txType": 0,
      "triggerPrice": "Trade Trigger Price"
    }
  ]
}
SUB User Trade Fills
Spot User Trade Fills

Endpoint: /ws/spot

#Spot
Accepts the following message:

Spot-User-Trade-Fills
When a trade has been transacted, this topic will send the trade information back to the subscriber.

PayloadExpand all
object oneOfuid: userTradeFills
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "fills"
  ]
}
#2 Example - Response
Response Contents

{
  "topic": "fills",
  "data": [
    {
      "orderId": "<Order Id>",
      "serialId": "<Serial ID After Insertion into DB>",
      "clOrderId": "<Client order ID>",
      "type": "order type",
      "symbol": "ex: BTC-USD",
      "side": "BUY|SELL",
      "price": "filled price",
      "size": "filled size",
      "feeAmount": "Fees charged to user, value to be String on API",
      "feeCurrency": "Fee currency, eg. Buy would be BTC, Sell would be USD",
      "base": "Base currency, eg. BTC",
      "quote": "Quote currency eg. USD",
      "maker": "maker or taker",
      "timestamp": "Time trade was matched in the engine",
      "tradeId": "<Trade Unique ID>"
    }
  ]
}
SUB OSS L1 Snapshot
OSS Level 1 Orderbook Snapshot

Endpoint: /ws/oss/spot
The format to subscribe to will be symbol. The L1 orderbook will be pushed immediately when orderbook changes.

symbol indicates the market symbol.
#Spot Orderbook Streaming
Accepts the following message:

Spot-OSS-L1-Snapshot

*** response content ***

PayloadExpand all
object oneOfuid: OSSL1SnapshotByGrouping
Examples
Payload
#1 Example - Request-Subscribe
Request Contents

{
  "op": "subscribe",
  "args": [
    "snapshotL1:BTC-USD"
  ]
}
#2 Example - Request-Unsubscribe
Request Contents

{
  "op": "unsubscribe",
  "args": [
    "snapshotL1:BTC-USD"
  ]
}
#3 Example - Response-Subscribe
Response-Subscribe Contents

{
  "topic": "snapshotL1:BTC-USD",
  "data": {
    "bids": [
      [
        "28016.7",
        "1.48063"
      ]
    ],
    "asks": [
      [
        "28033.6",
        "1.34133"
      ]
    ],
    "type": "snapshotL1",
    "symbol": "BTC-USD",
    "timestamp": 1680750154232
  }
}
SUB Orderbook Incremental Updates
Orderbook Incremental Updates

Endpoint: /ws/oss/spot
Subscribe to Orderbook incremental updates through the endpoint /ws/oss/spot. The topic to subscribe to will be update specifying the symbol (eg. update:BTC-USD). The first response received will be a snapshot of the current orderbook (this is indicated in the type field) and 50 levels will be returned. Incremental updates will be sent in subsequent packets with type delta.
Bids and asks will be sent in price and size tuples. The size sent will be the new updated size for the price. If a value of 0 is sent, the price should be removed from the local copy of the orderbook.
To ensure that the updates are received in sequence, seqNum indicates the current sequence and prevSeqNum refers to the packet before. seqNum will always be one after the prevSeqNum. If the sequence is out of order, you will need to unsubscribe and re-subscribe to the topic again.
Also if crossed orderbook ever occurs when the best bid higher or equal to the best ask, please unsubscribe and re-subscribe to the topic again.
*** response content ***

#Spot Orderbook Streaming
Accepts the following message:

Spot-Orderbook-Incremental-Updates

*** response content ***

PayloadExpand all
object oneOfuid: orderbookIncrementalUpdates
Examples
Payload
#1 Example - Request-Subscribe
Request Contents

{
  "op": "subscribe",
  "args": [
    "update:BTC-USD"
  ]
}
#2 Example - Request-Unsubscribe
Request Contents

{
  "op": "unsubscribe",
  "args": [
    "update:BTC-USD"
  ]
}
#3 Example - Response-Subscribe
Response-Subscribe Contents

{
  "topic": "update:BTC-USD",
  "data": {
    "bids": [
      [
        "59252.5",
        "0.06865"
      ],
      [
        "59249.0",
        "0.24000"
      ],
      [
        "59235.5",
        "0.16073"
      ],
      [
        "59235.0",
        "0.26626"
      ],
      [
        "59233.0",
        "0.50000"
      ]
    ],
    "asks": [
      [
        "59292.0",
        "0.50000"
      ],
      [
        "59285.5",
        "0.24000"
      ],
      [
        "59285.0",
        "0.15598"
      ],
      [
        "59282.5",
        "0.06829"
      ],
      [
        "59278.5",
        "0.01472"
      ]
    ],
    "seqNum": 628282,
    "prevSeqNum": 628281,
    "type": "snapshot",
    "timestamp": 1565135165600,
    "symbol": "BTC-USD"
  }
}
#4 Example - Response-Unsubscribe
Response-Unsubscribe Contents

{
  "topic": "update:BTC-USD",
  "data": {
    "bids": [],
    "asks": [
      [
        "59367.5",
        "2.15622"
      ],
      [
        "59325.5",
        "0"
      ]
    ],
    "seqNum": 628283,
    "prevSeqNum": 628282,
    "type": "delta",
    "timestamp": 1565135165600,
    "symbol": "BTC-USD"
  }
}
SUB Subscription
Futures Subscription

Endpoint: /ws/futures

#Futures
Accepts the following message:

Futures-Subscription
To subscribe to a websocket feed

PayloadExpand all
object oneOfuid: subscription
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "topic-name"
  ]
}
#2 Example - Response
Response Contents

{
  "event": "subscribe",
  "channel": [
    "topic-name"
  ]
}
#3 Example - Failed Response
Response Contents

{
  "event": "subscribe",
  "channel": []
}
SUB Public Trade Fills
Futures Public Trade Fills

Endpoint: /ws/futures

#Futures
Accepts the following message:

Futures-Public-Trade-Fills
Subscribe to recent trade feed for a market. The topic will be tradeHistoryApiV2:<market> where <market> is the market symbol.
*** response content ***

PayloadExpand all
object oneOfuid: publicTradeFills
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "tradeHistoryApiV2:BTC-PERP"
  ]
}
#2 Example - Response
Response Contents

{
  "topic": "tradeHistoryApiV2:BTC-PERP",
  "data": [
    {
      "symbol": "BTC-PERP",
      "side": "SELL",
      "size": 0.007,
      "price": 5302.8,
      "tradeId": "<Trade Sequence ID>",
      "timestamp": 1584446020295
    }
  ]
}
SUB Authentication
Futures Authentication

Endpoint: /ws/futures

#Futures
Accepts the following message:

Futures-Authentication
Authenticate the websocket session to subscribe to authenticated websocket topics. Assume we have values as follows:
- request-nonce: 1624985375123
- request-api:4e9536c79f0fdd72bf04f2430982d3f61d9d76c996f0175bbba470d69d59816x
- secret:848db84ac252b6726e5f6e7a711d9c96d9fd77d020151b45839a5b59c37203bx

Our subscription request will be:

Request Parameters
Below details the arguments needed to be sent in.

Generating a signature
echo -n "/ws/futures1624985375123" | openssl dgst -sha384 -hmac "848db84ac252b6726e5f6e7a711d9c96d9fd77d020151b45839a5b59c37203bx"
(stdin)=bd8afb8bee58ba0a2c67f84dcfe6e64d0274f55d064bb26ea84a0fe6dd8c621b541b511982fb0c0b8c244e9521a80ea1


PayloadExpand all
object oneOfuid: authentication
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "login",
  "args": [
    "4e9536c79f0fdd72bf04f2430982d3f61d9d76c996f0175bbba470d69d59816x",
    "1624985375123",
    "bd8afb8bee58ba0a2c67f84dcfe6e64d0274f55d064bb26ea84a0fe6dd8c621b541b511982fb0c0b8c244e9521a80ea1"
  ]
}
#2 Example - Response
Response Contents

{
  "event": "login",
  "success": true
}
SUB Notifications
Futures Notifications

Endpoint: /ws/futures

#Futures
Accepts the following message:

Futures-Notifications
Receive trade notifications by subscribing to the topic notificationApiV4. The websocket feed will push trade level notifications to the subscriber. If topic is subscribed without being authenticated, no messages will be sent.
*** response content ***

PayloadExpand all
object oneOfuid: notification
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "notificationApiV4"
  ]
}
#2 Example - Response
Response Contents

{
  "topic": "notificationApiV4",
  "data": [
    {
      "symbol": "Market Symbol (eg. BTC-PERP)",
      "orderID": "internal order ID",
      "side": "BUY",
      "type": "76",
      "txType": 0,
      "price": "Order price or transacted price",
      "triggerPrice": "Trade Trigger Price",
      "pegPriceDeviation": "Indicate the deviation percentage. Valid for only algo orders.",
      "stealth": 1,
      "status": "<Refer to Status description on the left>",
      "timestamp": 1624985375123,
      "avgFillPrice": 35000,
      "clOrderID": "<Client order ID>",
      "originalOrderSize": 1,
      "currentOrderSize": 1,
      "filledSize": 1,
      "totalFilledSize": 1,
      "maker": "<Maker flag, if true indicates that trade is a maker trade>",
      "remainingSize": "<Remaining size on the order>",
      "time_in_force": "<Time where this order is valid>"
    }
  ]
}
SUB User Trade Fills
Futures User Trade Fills

Endpoint: /ws/futures

#Futures
Accepts the following message:

Futures-User-Trade-Fills
When a trade has been transacted, this topic will send the trade information back to the subscriber.

PayloadExpand all
object oneOfuid: userTradeFills
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "fillsV2"
  ]
}
#2 Example - Response
Response Contents

{
  "topic": "fillsV2",
  "data": [
    {
      "orderId": "a67c7d42-f3a0-42c5-9da0-26e0afdf5c01",
      "serialId": 9311338,
      "clOrderId": "_mrdngcbe1677815334917",
      "type": "76",
      "symbol": "BTC-PERP",
      "side": "BUY",
      "price": "22366.4",
      "size": "1.0",
      "freeAmount": "0.0111832",
      "feeCurrency": "USD",
      "base": "BTC-PERP",
      "quote": "USD",
      "maker": false,
      "timestamp": 1677815334928,
      "tradeId": "d3b776ff-900f-4457-9275-3abf1aeef6f5"
    }
  ]
}
SUB All Position
Futures All Position

Endpoint: /ws/futures

#Futures
Accepts the following message:

All-Position
All futures positions will be pushed periodically (per 5 secs) via this topic.
Response Content

PayloadExpand all
object oneOfuid: allPosition
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "allPositionV3"
  ]
}
#2 Example - Response
Response Contents

{
  "topic": "allPositionV3",
  "data": [
    {
      "requestId": "<Request Id>",
      "username": "<User Name>",
      "marketName": "BTC-PERP-USD",
      "orderType": 90,
      "orderMode": 66,
      "originalAmount": 0.001,
      "maxPriceHeld": 0,
      "pegPriceMin": 0,
      "stealth": 1,
      "orderID": null,
      "maxStealthDisplayAmount": 0,
      "sellExchangeRate": 0,
      "triggerPrice": 0,
      "closeOrder": true,
      "liquidationInProgress": false,
      "marginType": 91,
      "entryPrice": 47303.404761929,
      "liquidationPrice": 0,
      "markedPrice": 47293.949862586,
      "unrealizedProfitLoss": -0.13236859,
      "totalMaintenanceMargin": 3.484381756,
      "totalContracts": 14,
      "isolatedLeverage": 0,
      "totalFees": 0,
      "totalValue": 662.115298076,
      "adlScoreBucket": 2,
      "orderTypeName": "TYPE_FUTURES_POSITION",
      "orderModeName": "MODE_BUY",
      "marginTypeName": "FUTURES_MARGIN_CROSS",
      "currentLeverage": 0.02,
      "avgFillPrice": 0,
      "positionId": "BTC-PERP-USD|SHORT",
      "positionMode": "HEDGE",
      "positionDirection": "SHORT",
      "settleWithNonUSDAsset": "BTC",
      "takeProfitOrder": {
        "orderId": "4820b20a-e41b-4273-b3ad-4b19920aeeb5",
        "side": "SELL",
        "triggerPrice": 31000,
        "triggerUseLastPrice": false
      },
      "stopLossOrder": {
        "orderId": "eff2b232-e2ce-4562-b0b4-0bd3713c11ec",
        "side": "SELL",
        "triggerPrice": 27000,
        "triggerUseLastPrice": true
      },
      "contractSize": 0.001
    },
    {
      "requestId": 0,
      "username": "user",
      "userCurrency": null,
      "marketName": "LTC-PERP-USD",
      "orderType": 90,
      "orderMode": 83,
      "originalAmount": 0.01,
      "maxPriceHeld": 0,
      "pegPriceMin": 0,
      "stealth": 1,
      "orderID": null,
      "maxStealthDisplayAmount": 0,
      "sellexchangeRate": 0,
      "triggerPrice": 0,
      "closeOrder": false,
      "liquidationInProgress": false,
      "marginType": 91,
      "entryPrice": 69.9,
      "liquidationPrice": 29684.3743872669,
      "markedPrice": 70.062346733,
      "unrealizedProfitLoss": -0.04870402,
      "totalMaintenanceMargin": 0.319484301,
      "totalContracts": 30,
      "isolatedLeverage": 0,
      "totalFees": 0,
      "totalValue": -21.01870402,
      "adlScoreBucket": 1,
      "booleanVar1": false,
      "orderTypeName": "TYPE_FUTURES_POSITION",
      "orderModeName": "MODE_SELL",
      "marginTypeName": "FUTURES_MARGIN_CROSS",
      "currentLeverage": 0.1116510969,
      "takeProfitOrder": null,
      "stopLossOrder": null,
      "settleWithNonUSDAsset": "USDT",
      "positionId": "LTC-PERP-USD|SHORT",
      "positionMode": "HEDGE",
      "positionDirection": "SHORT",
      "contractSize": 0.001
    }
  ]
}
SUB Positions
Futures Positions

Endpoint: /ws/futures

#Futures
Accepts the following message:

Positions
Publish user's current position per 5 secs. When no symbol is specified, positions for all markets will be returned.
You will receive a record with price equals to zero when position is closed. (All-Position won't have this record)

PayloadExpand all
object oneOfuid: allPosition
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "positionsV2"
  ]
}
#2 Example - Response
Response Contents

{
  "topic": "positionsV2",
  "data": [
    {
      "requestId": "<Request Id>",
      "username": "<User Name>",
      "marketName": "BTC-PERP-USD",
      "orderType": 90,
      "orderMode": 66,
      "originalAmount": 0.001,
      "maxPriceHeld": 0,
      "pegPriceMin": 0,
      "stealth": 1,
      "orderID": null,
      "maxStealthDisplayAmount": 0,
      "sellExchangeRate": 0,
      "triggerPrice": 0,
      "closeOrder": true,
      "liquidationInProgress": false,
      "marginType": 91,
      "entryPrice": 47303.404761929,
      "liquidationPrice": 0,
      "markedPrice": 47293.949862586,
      "unrealizedProfitLoss": -0.13236859,
      "totalMaintenanceMargin": 3.484381756,
      "totalContracts": 14,
      "isolatedLeverage": 0,
      "totalFees": 0,
      "totalValue": 662.115298076,
      "adlScoreBucket": 2,
      "orderTypeName": "TYPE_FUTURES_POSITION",
      "orderModeName": "MODE_BUY",
      "marginTypeName": "FUTURES_MARGIN_CROSS",
      "currentLeverage": 0.02,
      "avgFillPrice": 0,
      "positionId": "BTC-PERP-USD|SHORT",
      "positionMode": "HEDGE",
      "positionDirection": "SHORT",
      "settleWithNonUSDAsset": "BTC",
      "takeProfitOrder": {
        "orderId": "4820b20a-e41b-4273-b3ad-4b19920aeeb5",
        "side": "SELL",
        "triggerPrice": 31000,
        "triggerUseLastPrice": false
      },
      "stopLossOrder": {
        "orderId": "eff2b232-e2ce-4562-b0b4-0bd3713c11ec",
        "side": "SELL",
        "triggerPrice": 27000,
        "triggerUseLastPrice": true
      },
      "contractSize": 0.001
    },
    {
      "requestId": 0,
      "username": "user",
      "userCurrency": null,
      "marketName": "LTC-PERP-USD",
      "orderType": 90,
      "orderMode": 83,
      "originalAmount": 0.01,
      "maxPriceHeld": 0,
      "pegPriceMin": 0,
      "stealth": 1,
      "orderID": null,
      "maxStealthDisplayAmount": 0,
      "sellexchangeRate": 0,
      "triggerPrice": 0,
      "closeOrder": false,
      "liquidationInProgress": false,
      "marginType": 91,
      "entryPrice": 69.9,
      "liquidationPrice": 29684.3743872669,
      "markedPrice": 70.062346733,
      "unrealizedProfitLoss": -0.04870402,
      "totalMaintenanceMargin": 0.319484301,
      "totalContracts": 30,
      "isolatedLeverage": 0,
      "totalFees": 0,
      "totalValue": -21.01870402,
      "adlScoreBucket": 1,
      "booleanVar1": false,
      "orderTypeName": "TYPE_FUTURES_POSITION",
      "orderModeName": "MODE_SELL",
      "marginTypeName": "FUTURES_MARGIN_CROSS",
      "currentLeverage": 0.1116510969,
      "takeProfitOrder": null,
      "stopLossOrder": null,
      "settleWithNonUSDAsset": "USDT",
      "positionId": "LTC-PERP-USD|SHORT",
      "positionMode": "HEDGE",
      "positionDirection": "SHORT",
      "contractSize": 0.001
    }
  ]
}
SUB Open Orders
Futures Open Orders

Endpoint: /ws/futures

#Futures
Accepts the following message:

Futures-Open-Order
Offer user's current open orders
if subscribed, websocket will responsd at the time:

after subscription

after order placed, amended, cancelled, filled (notification received)

Only after subscribed, websocket will return SNAPSHOT, otherwise, only return UPDATE data. (check type column)
So that, clients should maintain their own open order snapshot.
For UPDATE data, if the amount is 0, that means the order is cancelled or fully filled, otherwise, order is inserted, amended or partially filled.
The serialId should be continuous. If a client receives non-continuous serialId, it has better to subscribe again since UPDATE datas are missed.
PayloadExpand all
object oneOfuid: FuturesOpenOrder
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "subscribe",
  "args": [
    "open-order:BTC-PERP-USD"
  ]
}
#2 Example - Response
After subscribed

{
  "topic": "open-order:BTC-PERP-USD",
  "serialId": 1,
  "type": "SNAPSHOT",
  "data": [
    {
      "orderID": "52ee0278-f137-4dc5-8393-a7a9ca0696e0",
      "orderType": 76,
      "orderMode": 66,
      "orderModeName": "MODE_BUY",
      "marketName": "BTC-PERP-USD",
      "amount": 10,
      "originalAmount": 10,
      "price": 1,
      "displayPrice": 1,
      "triggerOrder": false,
      "triggerOrderType": 0,
      "triggerPrice": 0,
      "vendorName": null,
      "createTimestamp": 1689303771677,
      "triggered": false
    }
  ]
}
#3 Example - Response
After placing an order

{
  "topic": "open-order:BTC-PERP-USD",
  "serialId": 2,
  "type": "UPDATE",
  "data": [
    {
      "orderID": "a4af4fdf-aaea-452e-93e5-0cd1aa70cfae",
      "orderType": 76,
      "orderMode": 66,
      "orderModeName": "MODE_BUY",
      "marketName": "BTC-PERP-USD",
      "amount": 10,
      "originalAmount": 10,
      "price": 1,
      "displayPrice": 1,
      "triggerOrder": false,
      "triggerOrderType": 0,
      "triggerPrice": 0,
      "vendorName": null,
      "createTimestamp": 1689305697451,
      "triggered": false
    }
  ]
}
#4 Example - Response
After amending the order price

{
  "topic": "open-order:BTC-PERP-USD",
  "serialId": 3,
  "type": "UPDATE",
  "data": [
    {
      "orderID": "a4af4fdf-aaea-452e-93e5-0cd1aa70cfae",
      "orderType": 76,
      "orderMode": 66,
      "orderModeName": "MODE_BUY",
      "marketName": "BTC-PERP-USD",
      "amount": 10,
      "originalAmount": 10,
      "price": 2,
      "displayPrice": 1,
      "triggerOrder": false,
      "triggerOrderType": 0,
      "triggerPrice": 0,
      "vendorName": null,
      "createTimestamp": 1689305697451,
      "triggered": false
    }
  ]
}
#5 Example - Response
After cancelling the order

{
  "topic": "open-order:BTC-PERP-USD",
  "serialId": 4,
  "type": "UPDATE",
  "data": [
    {
      "orderID": "a4af4fdf-aaea-452e-93e5-0cd1aa70cfae",
      "orderType": 0,
      "orderMode": 0,
      "orderModeName": null,
      "marketName": null,
      "amount": 0,
      "originalAmount": 0,
      "price": 0,
      "displayPrice": 0,
      "triggerOrder": false,
      "triggerOrderType": 0,
      "triggerPrice": 0,
      "vendorName": null,
      "createTimestamp": 0,
      "triggered": false
    }
  ]
}
SUB OSS L1 Snapshot
OSS Level 1 Orderbook Snapshot

Endpoint: /ws/oss/futures
The format to subscribe to will be symbol. The L1 orderbook will be pushed immediately when orderbook changes.

symbol indicates the market symbol.
#Futures Orderbook Streaming
Accepts the following message:

Futures-OSS-L1-Snapshot

*** response content ***

PayloadExpand all
object oneOfuid: OSSL1SnapshotByGrouping
Examples
Payload
#1 Example - Request-Subscribe
Request Contents

{
  "op": "subscribe",
  "args": [
    "snapshotL1:BTC-PERP"
  ]
}
#2 Example - Request-Unsubscribe
Request Contents

{
  "op": "unsubscribe",
  "args": [
    "snapshotL1:BTC-PERP"
  ]
}
#3 Example - Response-Subscribe
Response-Subscribe Contents

{
  "topic": "snapshotL1:BTC-PERP",
  "data": {
    "bids": [
      [
        "28016.7",
        "1.48063"
      ]
    ],
    "asks": [
      [
        "28033.6",
        "1.34133"
      ]
    ],
    "type": "snapshotL1",
    "symbol": "BTC-PERP",
    "timestamp": 1680750154232
  }
}
SUB Orderbook Incremental Updates
Futures Orderbook Incremental Updates

Endpoint: /ws/oss/futures
Subscribe to Orderbook incremental updates. The topic to subscribe to will be update specifying the symbol (eg. update:BTC-PERP). The first response received will be a snapshot of the current orderbook (this is indicated in the type field) and 50 levels will be returned. Incremental updates will be sent in subsequent packets with type delta.
Bids and asks will be sent in price and size tuples. The size sent will be the new updated size for the price. If a value of 0is sent, the price should be removed from the local copy of the orderbook.
To ensure that the updates are received in sequence, seqNum indicates the current sequence and prevSeqNumrefers to the packet before. seqNum will always be one after the prevSeqNum. If the sequence is out of order, you will need to unsubscribe and re-subscribe to the topic again.
Also if crossed orderbook ever occurs when the best bid higher or equal to the best ask, please unsubscribe and re-subscribe to the topic again.

#Futures Orderbook Streaming
Accepts the following message:

Futures-Orderbook-Incremental-Updates

*** response content ***

PayloadExpand all
object oneOfuid: orderbookIncrementalUpdates
Examples
Payload
#1 Example - Request-Subscribe
Request Contents

{
  "op": "subscribe",
  "args": [
    "update:BTC-PERP_0"
  ]
}
#2 Example - Request-Unsubscribe
Request Contents

{
  "op": "unsubscribe",
  "args": [
    "update:BTC-PERP_0"
  ]
}
#3 Example - Response-Subscribe
Response-Subscribe Contents

{
  "topic": "update:BTC-PERP_0",
  "data": {
    "bids": [
      [
        "59252.5",
        "0.06865"
      ],
      [
        "59249.0",
        "0.24000"
      ],
      [
        "59235.5",
        "0.16073"
      ],
      [
        "59235.0",
        "0.26626"
      ],
      [
        "59233.0",
        "0.50000"
      ]
    ],
    "asks": [
      [
        "59292.0",
        "0.50000"
      ],
      [
        "59285.5",
        "0.24000"
      ],
      [
        "59285.0",
        "0.15598"
      ],
      [
        "59282.5",
        "0.06829"
      ],
      [
        "59278.5",
        "0.01472"
      ]
    ],
    "seqNum": 628282,
    "prevSeqNum": 628281,
    "type": "snapshot",
    "timestamp": 1565135165600,
    "symbol": "BTC-PERP"
  }
}
#4 Example - Response-Unsubscribe
Response-Unsubscribe Contents

{
  "topic": "update:BTC-PERP_0",
  "data": {
    "bids": [],
    "asks": [
      [
        "59367.5",
        "2.15622"
      ],
      [
        "59325.5",
        "0"
      ]
    ],
    "seqNum": 628283,
    "prevSeqNum": 628282,
    "type": "delta",
    "timestamp": 1565135165600,
    "symbol": "BTC-PERP"
  }
}
SUB Authentication
OTC Authentication

Endpoint: /ws/otc

#OTC
#Streaming
Accepts the following message:

Authentication
Authenticate the websocket session to subscribe to authenticated websocket topics. Assume we have values as follows:
- request-nonce: 1624985375123
- request-api:4e9536c79f0fdd72bf04f2430982d3f61d9d76c996f0175bbba470d69d59816x
- secret:848db84ac252b6726e5f6e7a711d9c96d9fd77d020151b45839a5b59c37203bx

Our subscription request will be:

Request Parameters
Below details the arguments needed to be sent in.

Generating a signature
echo -n "/ws/otc1624985375123" | openssl dgst -sha384 -hmac "848db84ac252b6726e5f6e7a711d9c96d9fd77d020151b45839a5b59c37203bx"
(stdin)=971798b32585d7e63a1c2cafd261170c56caf17ff1d32a58fc2e9842292fa8ff2dbcf4fda7b4d6aed4a737c3c2930cf1


PayloadExpand all
object oneOfuid: authentication
Examples
Payload
#1 Example - Request
Request Contents

{
  "op": "login",
  "args": [
    "4e9536c79f0fdd72bf04f2430982d3f61d9d76c996f0175bbba470d69d59816x",
    "1624985375123",
    "971798b32585d7e63a1c2cafd261170c56caf17ff1d32a58fc2e9842292fa8ff2dbcf4fda7b4d6aed4a737c3c2930cf1"
  ]
}
#2 Example - Response
Response Contents

{
  "event": "login",
  "success": true
}
SUB Quote Stream
OTC Quote Stream

Endpoint: /ws/otc

#OTC
#Streaming
Accepts the following message:

Quote-Stream
Receive quote streams by subscribing to the quote websocket. The websocket topic will constantly push new prices to the subscriber. To accept the quote, indicate the buy or sell quote Id using the /accept API.

PayloadExpand all
object oneOfuid: quoteStream








Futures API documentation
Export
v2.3
Overview
Migration from v2.2 to v2.3
We are updating several order-related API endpoints to improve consistency and clarity in size-related fields. Please review the following changes carefully, as some existing fields will be deprecated and replaced with new ones.

Updated Fields for Order Actions
For the following endpoints, the fields size, fillSize and originalSize will be deprecated and replaced with the following:

originalOrderSize
currentOrderSize
filledSize
totalFilledSize
Affected Endpoints

Create New Order
Amend Order
Cancel Order
Create New Algo Order
Bind TP/SL
Close Position
Updated Fields for Order Query
For the following endpoints, size and filledSize will be deprecated, and replaced by:

originalOrderSize
currentOrderSize
totalFilledSize
Affected Endpoints

Query Order
Query Open Orders
Updated Fields for Notifications

For Notifications, the fields size, fillSize, originalSize will be deprecated and replaced with:

originalOrderSize
currentOrderSize
filledSize
totalFilledSize
WebSocket Consistency Update
We are also improving consistency across WebSocket topics between subscription requests and data notifications.

Generating API Key
You will need to create an API key on the platform before you can use authenticated APIs. To create API keys, you can follow the steps below:

Login with your username / email and password into the website
Click on Account on the top right hand corner
Select the API tab
Click on New API button to create an API key and passphrase. (Note: the passphrase will only appear once)
Use your API key and passphrase to construct a signature.
Authentication
API Key (request-api)
Parameter Name: request-api, in: header. API key is obtained from the platform as a string
API Key (request-nonce)
Parameter Name: request-nonce, in: header. Representation of current timestamp (epoch milliseconds) in long format
API Key (request-sign)
Parameter Name: request-sign, in: header. A composite signature produced based on the following algorithm: Signature=HMAC.Sha384 (secretKey, (path + request-nonce + body)) (note: body = '' when no data):
Example 1: Query Position

Endpoint to query position is /api/v2.2/user/positions
Assume we have the values as follows (notice: the query parameters are excluded from encrypted text):
request-nonce:1677668593571
request-api: 4e9536c79f0fdd72bf04f2430982d3f61d9d76c996f0175bbba470d69d59816x
secret: 848db84ac252b6726e5f6e7a711d9c96d9fd77d020151b45839a5b59c37203bx
path: /api/v2.2/user/positions
body: (empty)
encrypted text:/api/v2.2/user/positions1677668593571
Generated signature will be:
request-sign: 254949204f2009705eba550b5a158867d678715cd4f6a14d00c6e46390329e57dddc36947542e1a0f03b010b140ca315
cURL example:
curl --location --request GET 'https://api.altex.mn/futures/api/v2.2/user/positions?symbol=BTC-PERP' \
--header 'request-api: 49e9d289fb926ed26aaa971ed4edabc93b675d2b316a7b22d76567a3c5c9f0a6' \
--header 'request-nonce: 1677668593571' \
--header 'request-sign: 254949204f2009705eba550b5a158867d678715cd4f6a14d00c6e46390329e57dddc36947542e1a0f03b010b140ca315'
Example 2: Place an order (notice: the parameters in the request are case-sensitive)

Endpoint to place an order is /api/v2.2/order
Assume we have the values as follows (notice: the parameters in the request are case-sensitive):
request-nonce:1677669503458
request-api:4e9536c79f0fdd72bf04f2430982d3f61d9d76c996f0175bbba470d69d59816x
secret:848db84ac252b6726e5f6e7a711d9c96d9fd77d020151b45839a5b59c37203bx
path: /api/v2.2/order
body: {"symbol":"BTC-PERP","price":10000,"size":2,"side":"BUY","time_in_force":"GTC","type":"LIMIT","postOnly":false,"trailValue":0}
encrypted text:/api/v2.2/order1677669503458{"symbol":"BTC-PERP","price":10000,"size":2,"side":"BUY","time_in_force":"GTC","type":"LIMIT","postOnly":false,"trailValue":0}
Generated signature will be:
request-sign: b8a866f7336b4870a2be3fed1a0734599cecca10a3e147957371b64c6cccee5561b7ad34c192572775529fce363c4bb5
cURL example:
curl --location --request POST 'https://api.altex.mn/futures/api/v2.2/order' \
--header 'request-api: 49e9d289fb926ed26aaa971ed4edabc93b675d2b316a7b22d76567a3c5c9f0a6' \
--header 'request-nonce: 1677669503458' \
--header 'request-sign: b8a866f7336b4870a2be3fed1a0734599cecca10a3e147957371b64c6cccee5561b7ad34c192572775529fce363c4bb5' \
--header 'Content-Type: application/json' \
--data-raw '{"symbol":"BTC-PERP","price":10000,"size":2,"side":"BUY","time_in_force":"GTC","type":"LIMIT","postOnly":false,"trailValue":0}'
Rate Limits
The following rate limits are enforced:
Rate limits for platform is as follows:

Query

Per API:15 requests/second
Per User:30 requests/second
Orders

Per API:75 requests/second
Per User:75 requests/second
API Status Codes
Each API will return one of the following HTTP status:

Code	Description
200	API request was successful, refer to the specific API response for expected payload
400	Bad Request. Server will not process this request. This is usually due to invalid parameters sent in request
401	Unauthorized request. Server will not process this request as it does not have valid authentication credentials
403	Forbidden request. Credentials were provided but they were insufficient to perform the request
404	Not found. Indicates that the server understood the request but could not find a correct representation for the target resource
405	Method not allowed. Indicates that the request method is not known to the requested server
408	Request timeout. Indicates that the server did not complete the request. The API timeouts are set at 30secs
429	Too many requests. Indicates that the client has exceeded the rates limits set by the server. Refer to Rate Limits for more details
500	Internal server error. Indicates that the server encountered an unexpected condition resulting in not being able to fulfill the request
503	Service unavailable. Indicates that the server is not ready to handle the request
API Enum
When connecting up the API, you will come across number codes that represents different states or status types in platform. The following section provides a list of codes that you are expecting to see.

Code	Description
1	MARKET_UNAVAILABLE = Futures market is unavailable
2	ORDER_INSERTED = Order is inserted successfully
4	ORDER_FULLY_TRANSACTED = Order is fully transacted
5	ORDER_PARTIALLY_TRANSACTED = Order is partially transacted
6	ORDER_CANCELLED = ExecuteOrder/placeOrder/matchOrder fail.
When user send an spot postOnly order and received reject status, maybe:
- Insert order to orderBook fail, because order will transact before insert to orderBook. (postOnly meanings insert first)
- FoK order execute fail, because FoK not allow partially transacted. Order transact with user self, because order not allow self trade.
When user send an futures postOnly order and received reject status. maybe:
- Insert order to orderBook fail, because order will transact before insert to orderBook. (postOnly meanings insert first)
- Insert order to orderBook fail, because order will belong to spam order. (postOnly not allow with spam order)
- FoK order execute fail, because FoK not allow partially transacted. Order transact with user self, because order not allow self trade.
7	ORDER_REFUNDED = Turn user money back to user coin wallet, market order without any transacted will get refund, or self traded
8	INSUFFICIENT_BALANCE = Insufficient balance in account
9	TRIGGER_INSERTED = Trigger Order is inserted successfully
10	TRIGGER_ACTIVATED = Trigger Order is activated successfully
11	ERROR_INVALID_CURRENCY
12	ERROR_UPDATE_RISK_LIMIT = Error in updating risk limit
13	ERROR_INVALID_LEVERAGE
15	ORDER_REJECTED = PreCheck fail, then reject
When user amendOrder and received reject status, maybe:
- Update order price fail, because order not fund.
- Update trigger price fail, because order not fund.
- Update order amount fail, because order not fund. ...
When user cancelOrder and received reject status, maybe:
- Market not fund. ...
When user placeOrder and received reject status, maybe:
- Internal timeout. user try to use same clOrderId with different order at same time.
- Update order amount fail, because order not fund. send closePositionOrder but without any position.
16	ORDER_NOTFOUND = Order is not found with the order ID or clOrderID provided
17	REQUEST_FAILED = Failed to complete the request, please check order status
21	FREEZE_SUCCESSFUL
27	TRANSFER_SUCCESSFUL = Transfer funds between futures and spot is successful
28	TRANSFER_UNSUCCESSFUL = Transfer funds between spot and futures is unsuccessful
29	QUERY_GET_ORDERS
31	QUERY_GET_POSITIONS
33	QUERY_GET_ALL_POSITIONS_ORDERS
34	QUERY_WALLET
36	QUERY_FUTURES_MARGIN
41	ERROR_INVALID_RISK_LIMIT = Invalid risk limit was specified
51	QUERY_GET_ORDERS_WITH_LIMIT
64	STATUS_LIQUIDATION = Account is undergoing liquidation
65	ORDER_ACTIVE = Order is active
66	MODE_BUY
76	ORDER_TYPE_LIMIT = Limit order
77	ORDER_TYPE_MARKET = Market order
80	ORDER_TYPE_PEG = Peg/Algo order
81	ORDER_TYPE_OTC = Otc order
83	MODE_SELL
85	ORDER_PROCESSING = Order is inactive
88	ORDER_INACTIVE = Order is inactive
101	FUTURES_ORDER_PRICE_OUTSIDE_LIQUIDATION_PRICE = Futures order is outside of liquidation price
110	FUTURES_FUNDING
123	AMEND_ORDER = Order amended
124	UNFREEZE_SUCCESSFUL
129	FUTURES_CONFIG_MODE_CHANGE
300	ERROR_MAX_ORDER_SIZE_EXCEEDED
301	ERROR_INVALID_ORDER_SIZE
302	ERROR_INVALID_ORDER_PRICE
303	ERROR_RATE_LIMITS_EXCEEDED
304	ERROR_MAX_OPEN_ORDER_EXCEEDED
1003	ORDER_LIQUIDATION = Order is undergoing liquidation
1004	ORDER_ADL = Order is undergoing ADL
30000	ORDER_ADL = OTC_ORDER_QUERY
30001	ORDER_ADL = OTC_ORDER_QUOTE
30007	ORDER_ADL = OTC_ORDER_COMPLETE_SUCCESS
30410	ORDER_ADL = BLOCK_TRADE_COMPLETE_SUCCESS
Error Code
When the request encounter exception ,it will return one of the following error code.

Code	Description
-8104	ORDER_BELONGS_TO_VENDOR = The order belongs to vendor
-7006	COIN_PAIR_IS_NOT_EXISTS_ERROR = Coin pair does not exist
-2023	UNKNOWN_CURRENCY = Unknown currency
-1042	USER_CANT_TRADE = User can not trade
-22	COMM_EXCESS_RATE_LIMIT_ERROR = Exceed rate limit
-7	COMM_AUTHENTICATE_ERROR = Authenticate failed
-2	COMM_REQUEST_PARAM_ERROR = Invalid request parameter
-1	COMM_FAILED_ERROR = Failed
10002	USER_TOKEN_EXPIRED = User token has expired
51523	FINANCE_INSUFFICIENT_WALLET_BALANCE_ERROR = Insufficient wallet balance
Spam Orders
Spam orders are large number of small order sizes that are placed into orderbook.In order to ensure that the platform and user's interests are protected from malicious players, we will apply the following rules when users place small sized orders.

Orders with notional value below 5 USDT will be marked as spam orders.
Orders marked as spam always pay the taker fee.
Post-Only API orders marked as spam will be rejected.
Too many spam orders may be grounds to temporarily ban an account from trading.
API accounts placing >= 4 resting orders, with total size less than 20 USDT (notional value) are at risk of being marked as a spam account.
Accounts marked as spam may have limitations placed on the account, including order rate limits, position limits, or have API functions disabled.




Market Summary
get
https://api.altex.mn/futures/api/v2.3/market_summary
Gets market summary information. If no symbol parameter is sent, then all markets will be retrieved.

Request
Query Parameters
listFullAttributes
boolean
True to return all attributes of the market summary

symbol
string
Market symbol

Responses
200
Body

application/json

application/json
responses
/
200
array of:
symbol
string
Market symbol

last
number
Last price

lowestAsk
number
Lowest ask price in the orderbook

highestBid
number
Highest bid price in the orderbook

openInterest
number
Number of open positions in the futures market

openInterestUSD
number
Number of open positions in the futures market in USD notional value

percentageChange
number
Percentage change against the price within the last 24hours

volume
number
Transacted volume

high24Hr
number
Highest price over the last 24hours

low24Hr
number
Lowest price over the last 24hours

base
string
Base currency

quote
string
Quote currency

contractStart
string
Contract start time

contractEnd
string
Contract end time

active
boolean
Indicator if market is active

size
number
deprecated
Transacted size

timeBasedContract
boolean
Indicator to indicate if it is a time based contract

openTime
string
Market opening time

closeTime
string
Market closing time

startMatching
string
Matching start time

inactiveTime
string
Time where market is inactive

fundingRate
number
The funding rate

contractSize
number
Size of one contract

maxPosition
number
Maximum position in notional value that each user is allowed to have.

minValidPrice
number
Minimum valid price

minPriceIncrement
number
Price increment

minOrderSize
number
Minimum tick size

maxOrderSize
number
Maximum order size

minRiskLimit
number
Minimum risk limit in notional value

maxRiskLimit
number
Maximum risk limit in notional value

minSizeIncrement
number
Tick size

availableSettlement
array
Currencies available for settlement

futures
boolean
deprecated
Indicator if symbol is a futures contract

fundingIntervalMinutes
integer
Funding interval, only display when param listFullAttributes is true

fundingTime
number
Next funding time, only display when param listFullAttributes is true

listFullAttributes
:
Not SetFalseTrue

select an option
symbol
:
string
Send API Request
curl --request GET \
  --url https://api.altex.mn/futures/api/v2.3/market_summary \
  --header 'Accept: application/json'
[
  {
    "symbol": "BTC-PERP",
    "last": 36365,
    "lowestAsk": 36377,
    "highestBid": 36376,
    "percentageChange": 4.973731309,
    "volume": 172418318.7575521,
    "high24Hr": 36447,
    "low24Hr": 33989.5,
    "base": "BTC",
    "quote": "USDT",
    "active": true,
    "size": 4916.8266,
    "minValidPrice": 0.5,
    "minPriceIncrement": 0.5,
    "minOrderSize": 0.00001,
    "maxOrderSize": 2000,
    "minSizeIncrement": 0.00001,
    "openInterest": 0,
    "openInterestUSD": 0,
    "contractStart": 0,
    "contractEnd": 0,
    "timeBasedContract": false,
    "openTime": 0,
    "closeTime": 0,
    "startMatching": 0,
    "inactiveTime": 0,
    "fundingRate": 0,
    "contractSize": 0,
    "maxPosition": 0,
    "minRiskLimit": 0,
    "maxRiskLimit": 0,
    "availableSettlement": null,
    "futures": false
  }
]


Charting Data
get
https://api.altex.mn/futures/api/v2.3/ohlcv
Gets candle stick charting data. Default of 300 data points will be returned at any one time.

Request
Query Parameters
resolution
string
required
Supported resolution is:
1: 1min
5: 5 minutes
15: 15 minutes
30: 30 minutes
60: 60 minutes
240: 4 hours
360: 6 hours
1440: 1 day
10080: 1 week
43200: 1 month

Default:
1
symbol
string
required
Market symbol

Default:
BTC-PERP
end
string
Ending time (eg. 1624987283000)

start
string
Starting time (eg. 1624987283000)

Responses
200
Body

application/json

application/json
array[array]
number
0: Unix Time
1: Open Price
2: High Price
3: Low Price
4: Closing Price
5: Volume

resolution*
:
1
symbol*
:
BTC-PERP
end
:
string
start
:
string
Send API Request
curl --request GET \
  --url 'https://api.altex.mn/futures/api/v2.3/ohlcv?symbol=BTC-PERP&resolution=1' \
  --header 'Accept: application/json'
[
  [
    1666145400,
    26000,
    26000,
    26000,
    26000,
    0
  ],
  [
    1666145340,
    26000,
    26000,
    26000,
    26000,
    0
  ]
]




Query Market Price
get
https://api.altex.mn/futures/api/v2.3/price
Retrieve current prices on the platform. If no symbol specified, all symbols will be returned.

Request
Query Parameters
symbol
string
Market symbol

Default:
BTC-PERP
Responses
200
Body

application/json

application/json
array of:
symbol
number
Market symbol

indexPrice
number
Index price

lastPrice
number
Last transacted price

markPrice
number
Mark price

symbol
:
defaults to: BTC-PERP
Send API Request
curl --request GET \
  --url https://api.altex.mn/futures/api/v2.3/price \
  --header 'Accept: application/json'
[
  {
    "symbol": "BTC-PERP",
    "indexPrice": 36288.949684967,
    "lastPrice": 36286.5,
    "markPrice": 0
  }
]



Orderbook (By grouping)
get
https://api.altex.mn/futures/api/v2.3/orderbook
Retrieves a snapshot of the orderbook.

Request
Query Parameters
group
integer
Orderbook grouping. Valid values are: 0-8 where 0 indicates level 0 grouping (eg. for BTC-PERP, it will be 0.1) Level 1 grouping for BTC-PERP would be 0.5 Level 2 grouping for BTC-PERP would be 1

symbol
string
Market symbol

Default:
BTC-PERP
Responses
200
Body

application/json

application/json
symbol
string
required
Market symbol

buyQuote
array[object]
required
Array of Buy quotes

price
number
required
order price

size
number
required
order size

sellQuote
array[object]
required
Array of Sell quotes

price
string
required
order price

size
string
required
order size

timestamp
number
required
Timestamp of orderbook

group
:
integer
symbol
:
defaults to: BTC-PERP
Send API Request
curl --request GET \
  --url https://api.altex.mn/futures/api/v2.3/orderbook \
  --header 'Accept: application/json'
{
  "buyQuote": [
    {
      "price": 36371,
      "size": "100"
    }
  ],
  "sellQuote": [
    {
      "price": "36380.5",
      "size": "100"
    }
  ],
  "timestamp": 1624989459489,
  "symbol": "BTC-PERP"
}



Orderbook
get
https://api.altex.mn/futures/api/v2.3/orderbook/L2
Retrieves a Level 2 snapshot of the orderbook

Request
Query Parameters
depth
integer
Orderbook depth

symbol
string
Market symbol

Default:
BTC-PERP
Responses
200
Body

application/json

application/json
symbol
string
Market symbol

buyQuote
array[object]
Array of Buy quotes

price
string
order price

size
string
order size

timestamp
integer
Timestamp of orderbook

depth
integer
Order depth

depth
:
integer
symbol
:
defaults to: BTC-PERP
Send API Request
curl --request GET \
  --url https://api.altex.mn/futures/api/v2.3/orderbook/L2 \
  --header 'Accept: application/json'
{
  "symbol": "BTC-PERP",
  "buyQuote": [
    {
      "price": "18956.5",
      "size": "1676"
    },
    {
      "price": "18954.5",
      "size": "1116"
    }
  ],
  "timestamp": 1666316095340,
  "depth": 10
}





Query Trades Fills
get
https://api.altex.mn/futures/api/v2.3/trades
Get trade fills for the market specified by `symbol`

maximum days of history records:
Time Interval	Maximum Days	Explanation
startTime / endTime	30	Maximum 30 days within the specified interval
startTime / -	3	If the end time is not specified, then 3 days after the start time
- / endTime	3	If the start time is not specified, then 3 days before the end time
- / -	3	If neither start nor end time is specified, then 3 days before the current time
Request
Query Parameters
afterSerialId
string
Condition to retrieve records after the specified serial Id. Used for pagination

beforeSerialId
string
Condition to retrieve records before the specified serial Id. Used for pagination

count
integer
Number of records to return

endTime
string
Ending time (eg. 1624987283000)

includeOld
boolean
Retrieve trade history records past 7 days

startTime
string
Starting time (eg. 1624987283000)

symbol
string
Market symbol

Default:
BTC-PERP
Responses
200
Body

application/json

application/json
array of:
price
number
Transacted price

size
number
Transacted size

side
string
deprecated
Trade side. Values are: [Buy, SELL]

symbol
string
Market symbol

serialId
number
Serial Id, running sequence number

timestamp
integer
Transacted timestamp

afterSerialId
:
string
beforeSerialId
:
string
count
:
integer
endTime
:
string
includeOld
:
Not SetFalseTrue

select an option
startTime
:
string
symbol
:
defaults to: BTC-PERP
Send API Request
curl --request GET \
  --url https://api.altex.mn/futures/api/v2.3/trades \
  --header 'Accept: application/json'
[
  {
    "price": 36164,
    "size": 100,
    "side": "SELL",
    "symbol": "BTC-PERP",
    "serialId": "<Serial Id>",
    "timestamp": 1624990097000
  }
]



Get Funding Rate History
get
https://api.altex.mn/futures/api/v2.3/funding_history
Get funding rate history for certain symbols

Request
Body

application/json

application/json
symbol
string
Market symbol (e.g., BTC-PERP)

count
integer
Number of records to return (mutually exclusive with from/to)

from
number
Starting time in milliseconds (e.g., 1624987283000; mutually exclusive with count)

to
number
Ending time in milliseconds (e.g., 1624987283000; mutually exclusive with count)

Responses
200
Body

application/json

application/json
array of:
symbol
string
Market symbol

time
number
The epoch timestamp in second of the funding rate

rate
number
Funding rate

{
  "symbol": "string",
  "count": 0,
  "from": 0,
  "to": 0
}
{
  "symbol": "string",
  "count": 0,
  "from": 0,
  "to": 0
}
Send API Request
curl --request GET \
  --url https://api.altex.mn/futures/api/v2.3/funding_history \
  --header 'Accept: application/json'
{
  "BTC-PERP": [
    {
      "time": 1706515200,
      "rate": 0.000011405,
      "symbol": "BTC-PERP"
    }
  ]
}



