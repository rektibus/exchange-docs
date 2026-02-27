INTRODUCTION
Welcome to Tothemoon trader and developer documentation. These documents outline exchange functionality, market details, and APIs.

APIs are separated into two categories: trading and feed. Access to APIs requires authentication and provides access for placing orders, provides market data and other account information.

By accessing the Tothemoon Data API, you agree to the Exchange Terms & Conditions and Contracts Terms & Conditions

To access the Trading API server, add an access/secret key pair on Account / API section of Tothemoon website. You can generate one or more key pairs.

GENERAL INFORMATION
Matching Orders
Tothemoon market operates a first come-first serve order matching. Orders are executed as received by the matching engine, from the older to newer received orders.

Self-Trade Prevention
To discourage wash trading, Tothemoon exchange cancels smaller order and decreases larger order size by the smaller order size when two orders from the same client cross. Yet Tothemoon charges taker fee for the smaller order. If the two orders are the same size, both will be canceled, yet Tothemoon will charge taker fee for one order.

Rate Limit
Currently Tothemoon has a rate limit of 10 requests per second for WebSocket API and 1 request per second for HTTPS API. If you reach this limit you will receive a message with THROTTLING response type and overflow_level param which must be used for waiting for overflow_level milliseconds.

Unfair Price Prevention for spot trading
We prevent order placement with a price different from the market price by more than 10%. For example, if current best ask is 1000, you can't make Buy order with a price greater than 1100. And if the current best bid is 1000, you can't make Sell order with a price lower than 900.

Decimal Precision
Each amounts and a prices on Tothemoon have 8 decimal places.

Order Lifecycle
Valid orders sent to the matching engine are confirmed immediately and are in the received state. If an order executes against another order immediately, the order is considered done. An order can execute in part or whole. Any part of an order not filled immediately, will be considered open. Orders will stay in the open state until canceled or subsequently filled by new orders. Orders that are no longer eligible for matching (filled or canceled) are in the done state.

Currently Spot WS API supports the following limit orders types: fill or kill (FOK) orders, immediate or cancel (IOK) orders, good 'til canceled (GTC) orders, and good 'til day (GTD) orders. Contracts WS API supports only good 'til canceled (GTC) orders (default type).

A fill or kill (FOK) is a type of time-in-force designation used in securities trading that instructs an exchange to execute a transaction immediately and completely or not at all. The order must be filled in its entirety or canceled (killed).

An immediate or cancel order (IOC) is an order to buy or sell a security that must be immediately filled. Any unfilled portion of the order is canceled.

A good ’til canceled (GTC) describes an order a trader may place to buy or sell a security that remains active until either the order is filled or the trader cancels it.

A good 'til day order is an order which will be canceled at the time preset by a trader if it is not executed or cancelled until this time. A GTD order contains the Time To Live (TTL) instruction. Time To Live is a special instruction which shows the time in which an order will be automatically canceled.

Fees
FAQ

Data Centers
Tothemoon data centers are in the Amazon EU region.

Sandbox
A public sandbox is available for testing API connectivity and web trading. The sandbox provides all of the functionality of the production exchange but allows you to add fake funds for testing.

Login sessions and API keys are separate from production. We will issue some testing keys for you, to use them in the sandbox web interface and the sandbox environment.

To add funds, use the web interface deposit and withdraw buttons as you would on the production web interface.

Sandbox URLs: When testing your API connectivity, make sure to use the following URLs.

HTTPS API: https://api-sandbox.tothemoon.com

Contracts API: wss://contracts-api-sandbox.tothemoon.com/v1/trading

Octopus API: wss://octopus-sandbox.tothemoon.com/v1/connect

Website:

https://sandbox.tothemoon.com

Production
Production URLs: For production use the following URLs.

HTTPS API: https://api.tothemoon.com (Active)

Contracts API: wss://octopus.cryptology.com/v1/connect (Bridge URL - docs.tothemoon.com listed subdomains are NXDOMAIN)

Octopus API: wss://octopus.cryptology.com/v1/connect (Active Bridge URL)

Website:

https://tothemoon.com

Contracts Trading protocol
Tothemoon API operates over the WebSocket protocol (for details about WebSocket protocol, read RFC 6455).

Authentication
To make a request with authorization you need send your access key in Access-Key header and your secret key in Secret-Key header.

If authentication is successfully complete you are receive the following message:

Welcome to Tothemoon Contracts platform
If authentication failed you are received the following message:

{
  "type": "CommonError",
  "code": "INVALID_KEY",
  "message": "invalid access or secret key"
}
Requests
Request example

{
  "@type": "CancelOrder",
  "order_id": "dcfd4f24-9d50-4b76-82e5-47b6a58e4dad",
  "instrument_id": "BTC_PERPETUAL"
}
Responses
Response example:

{
  "message_id": "12345:3",
  "type": "OrderCancelled",
  "time": 1584374824023984764,
  "payload": {
    "reason": "manual",
    "order_id": "21f650e1-f99d-49f4-9d6c-b4d449bb945e",
    "cancelling_time": 1584374824.013984764,
    "instrument_id": "BTC_PERPETUAL",
    "remaining_volume": "1270"
  }
}
Params:

Name	Type	Description	Required	Constraints
type	enum	Message type	Yes	One of documented message types
message_id	string	Is an unique value indicating message order on server and used by the client to skip processed events on reconnect. You can start messages receiving from specific id by sending Msg-Id header with authentication request	Yes	
time	int	Time of operation performed	Yes	Valid timestamp, nanoseconds
payload	json	Body of message	Yes	
Server messages
Order lifecycle
OrderPlaced : order was received and executed.
OrderPlaced

{
  "message_id": "1098635:4",
  "type": "OrderPlaced",
  "time": 1584374824023984764,
  "payload": {
    "order_id": "21f650e1-f99d-49f4-9d6c-b4d449bb945e",
    "request_id": "d5c10dec-0fa6-4d50-9d1d-2ae69d83cb1a",
    "created_at": 1584370854013984760,
    "instrument_id": "BTC_PERPETUAL",
    "order_side": "buy",
    "price": "10201.5",
    "volume": "120"
  }
}
OrderCancelled : order was canceled (manual), end of order lifecycle
OrderCancelled

{
  "message_id": "222:56",
  "type": "OrderCancelled",
  "time": 1584374824023984764,
  "payload": {
    "reason": "manual",
    "order_id": "21f650e1-f99d-49f4-9d6c-b4d449bb945e",
    "cancelling_time": 1584374824.013984764,
    "instrument_id": "BTC_PERPETUAL",
    "remaining_volume": "1270"
  }
}
OrderClosed : order was fully executed, end of order lifecycle
OrderClosed

{
  "message_id": "17000230021:9",
  "type": "OrderClosed",
  "time": 1584374824023984764,
  "payload": {
    "order_id": "21f650e1-f99d-49f4-9d6c-b4d449bb945e",
    "instrument_id": "BTC_PERPETUAL"
  }
}
OrderRejected : order was rejected by exchange by the following reasons: LEADS_TO_LIQUIDATION, LIQUIDATION_AVOIDING, EXPIRATION, this message indicate end of order lifecycle
OrderRejected

{
  "message_id": "222:56",
  "type": "OrderRejected",
  "time": 1584374824023984764,
  "payload": {
    "reason": "LIQUIDATION_AVOIDING",
    "order_id": "c0396c86-ed85-4bb1-b3d2-e313712d50f8",
    "rejecting_time": 1584374824.013984764,
    "instrument_id": "BTC_PERPETUAL",
    "remaining_volume": "5000"
  }
}
AllOrdersCancelled : CancelAllOrders request successfully complete. OrderCancelled will be returned earlier for each order
AllOrdersCancelled

{
  "message_id": "2203432:4",
  "type": "AllOrdersCancelled",
  "time": 1584374824023984764,
  "payload": {
    "reason": "manual",
    "order_ids": [
      "21f650e1-f99d-49f4-9d6c-b4d449bb945e",
      "d5eaa66d-cdf7-4400-96f8-3d54b5dc6e2b"
    ],
    "cancelling_time": 1584374829.013984764,
    "instrument_id": "BTC_PERPETUAL"
  }
}
Errors
OrderPlacingError : order was received, but not executed because error was occurred.
OrderPlacingError

{
  "message_id": "1598635:40",
  "type": "OrderPlacingError",
  "time": 1584374824026984764,
  "payload": {
    "order_id": "21f650e1-f99d-49f4-9d6c-b4d449bb945e",
    "request_id": "d5c10dec-0fa6-4d50-9d1d-2ae69d83cb1a",
    "error_code": "INSUFFICIENT_FUNDS"
  }
}
OrderCancellingError : order cancelling request was failed.
OrderCancellingError

{
  "message_id": "1298635:4",
  "type": "OrderCancellingError",
  "time": 1584374924023984764,
  "payload": {
    "order_id": "41f650e1-f99d-49f4-9d6c-b4d449bb945e",
    "request_id": "d5c10dec-0fa6-4d50-9d1d-2ae69d83cb1a",
    "error_code": "ORDER_NOT_FOUND"
  }
}
AllOrdersCancellingError : all orders cancelling request was failed.
AllOrdersCancellingError

{
  "message_id": "1108635:4",
  "type": "AllOrdersCancellingError",
  "time": 1584374024023984764,
  "payload": {
    "error_code": "INSTRUMENT_IS_NOT_ACTIVE"
  }
}
CommonError : common error.
CommonError

{
  "message_id": "116788635:4",
  "type": "CommonError",
  "code": "INTERNAL_SERVER_ERROR",
  "request_id": "d5c10dec-a7a6-4d50-9d1d-2ae69d83cb1a"
}
Info messages
AllOrders : contain list of all placed and not finished orders in order book retrieved by user request.
AllOrders

{
  "message_id": "222000:46",
  "type": "AllOrdersCancelled",
  "time": 1584374824023984764,
  "payload": {
    "instrument_id": "BTC_PERPETUAL",
    "orders": [
      {
        "id": "21f650e1-f99d-49f4-9d6c-b4d449bb945e",
        "placing_time": 1584370854013984760,
        "side": "sell",
        "price": "9800.5",
        "avg_price": "9810",
        "volume": "3500",
        "initial_volume": "4000"
      },
      {
        "id": "b61298b6-e9e3-4edb-a9fa-ad573f694726",
        "placing_time": 1584370874013984760,
        "side": "buy",
        "price": "9750",
        "avg_price": "9750",
        "volume": "2000",
        "initial_volume": "2000"
      }
    ]
  }
}
Position : contain current user position. Can be retrieved due user request
Position

{
  "message_id": "223060:46",
  "type": "Position",
  "time": 1584374814223974734,
  "payload": {
    "instrument_id": "BTC_PERPETUAL",
    "position": {
      "avg_price": "10000",
      "value": "5000",
      "type": "long",
      "base_volume": "0.5",
      "base_remainder": "0.5",
      "realised_pnl": "0"
    }
  }
}
Trade : contain user trade.
Trade

{
  "message_id": "233060:0",
  "type": "Trade",
  "time": 1584374814223974734,
  "payload": {
    "instrument_id": "BTC_PERPETUAL",
    "order_id": "c0396c86-ed85-abb1-b3d2-e313712d50f8",
    "order_new_volume": "11998",
    "fee": "0.00000015",
    "volume": "2",
    "price": "10000",
    "is_self_trade": false
  }
}
SystemInfo : contain information about system status.
SystemInfo

```json { "type": "SystemInfo", "maintenance_mode_enabled": "false", "instruments_maintenance_mode": { "BTC_PERPETUAL": false, "GRAM_BTC": false } }

```

Balance : contain current user balances (available and on hold). Sent every time when changed.
Balance

{
  "message_id": "233060:0",
  "type": "Balance",
  "time": 1584354814223974734,
  "payload": {
    "currency": "BTC",
    "available": "9.97"
  }
}
MaintenanceModeChanged : contain information about new maintenance mode status.
MaintenanceModeChanged for instrument

{
  "message_id": "233460:0",
  "type": "MaintenanceModeChanged",
  "time": 1584353814223974734,
  "payload": {
    "enabled": true,
    "instrument_id": "BTC_PERPETUAL"
  }
}
MaintenanceModeChanged for system

{
  "message_id": "2253460:0",
  "type": "MaintenanceModeChanged",
  "time": 1584353814223974734,
  "payload": {
    "enabled": true
  }
}
Client messages
Orders management
PlaceOrder : execute order. The result will be a message with type OrderPlaced or OrderPlacingError
PlaceOrder

{
  "@type": "PlaceOrder",
  "instrument_id": "BTC_PERPETUAL",
  "side": "sell",
  "type": "limit",
  "price": "5440.5",
  "volume": "10000",
  "request_id": "35f658e1-fa9d-49f4-9d6c-b4d449bb945e"
}
CancelOrder : cancel order. The result will be a message with type OrderCancelled or OrderCancellingError
CancelOrder

{
  "@type": "CancelOrder",
  "order_id": "35f058e1-fa9d-49f4-9d6c-b4a449bb945e",
  "instrument_id": "BTC_PERPETUAL"
}
CancelAllOrders : cancel all orders which is not finished. The result will be a message AllOrdersCancelled or AllOrdersCancellingError
CancelAllOrders

{
  "@type": "CancelAllOrders",
  "instrument_id": "BTC_PERPETUAL"
}
Info messages
GetPosition : request to retrieve current user position. The result will be a message with type Position
GetPosition

{
  "@type": "GetPosition",
  "instrument_id": "BTC_PERPETUAL"
}
GetAllOrders : request to retrieve all orders which is not finished.
GetAllOrders

{
  "@type": "GetAllOrders",
  "instrument_id": "BTC_PERPETUAL"
}
Octopus market data protocol
Octopus is a new market data server by which you can subscribe to spot market data and contracts market data.

With Octopus you can subscribe to channel with data on which you want to receive updates. Currently available the next channels:

Spot platform:

spotTrades - all new trades
spotTickers - ticker updates on Spot platform
Contracts platform

contractsTrades - trades on Contracts platform
contractsTickers - ticker updates on Contracts platform
contractsOrderbookVolumes - order book volumes updates
Subscription management
After connection to Octopus via WSS you will receive welcomeMessage.

welcomeMessage example

{
  "server_timestamp": 1569319371576,
  "type": "welcomeMessage",
  "payload": {
    "connection_id": "36e662db-880e-4fff-8c05-aede97e975c7",
    "message": "Welcome to Tothemoon!"
  }
}
Next you can subscribe to data updates. For this you need send subscribe message in the following format:

subscribe

{
  "type": "subscribe",
  "channel": "contractsTrades.BTC_PERPETUAL",
  "request_id": "my_unique_request_id_for_contractsTrades.BTC_PERPETUAL_3"
}
Name	Type	Description	Required	Constraints
type	enum	Message type (subscribe, unsubscribe, unsubscribeAll, getSubscriptions)	Yes	One of documented message types
channel	string	Contain name of supported channel, dot (.) and name of instrument	Yes	
request_id	string	Identifier of subscription	Yes	Unique for channel
If you are subscribed successfully, you will receive subscribedSuccessful message.

subscribedSuccessful

{
  "server_timestamp": 1568800623123,
  "type": "subscribedSuccessful",
  "request_id": "my_unique_request_id_for_contractsTrades.BTC_PERPETUAL_3",
  "payload": {
    "channel": "contractsTrades.BTC_PERPETUAL"
  }
}
If subscription fails you will receive errorMessage.

errorMessage

{
  "server_timestamp": 1568801651123,
  "type": "errorMessage",
  "payload": {
    "code": "COMMON_ERROR",
    "message": "invalid request params: request_id is required field"
  }
}
You can unsubscribe from channel with unsubscribe message and request_id of previously created subscription.

unsubscribe

{
  "type": "unsubscribe",
  "request_id": "my_unique_request_id_for_contractsTrades.BTC_PERPETUAL_3"
}
If you have previously subscribed you will receive unsubscribedSuccessful message

unsubscribedSuccessful

{
  "server_timestamp": 1568802316123,
  "type": "unsubscribedSuccessful",
  "request_id": "my_unique_request_id_for_contractsTrades.BTC_PERPETUAL_3",
  "payload": {}
}
else you will receive errorMessage

errorMessage

{
  "server_timestamp": 1568802378123,
  "type": "errorMessage",
  "request_id": "my_unique_request_id_for_turboTrades.BTC_PERPETUAL_4",
  "payload": {
    "code": "COMMON_ERROR",
    "message": "can't unsubscribe: connection ea8e27e2-469a-42a9-88ef-1aa6dfd908e4 is not subscribed with id my_unique_request_id_for_turboTrades.BTC_PERPETUAL_4"
  }
}
You can unsubscribe from all subscriptions by sending unsubscribeAll request

unsubscribeAll

{
  "type": "unsubscribeAll"
}
as result you will receive unsubscribeAllSuccessfull message

unsubscribeAllSuccessfull

{
  "server_timestamp": 1568802459123,
  "type": "unsubscribedAllSuccessful",
  "payload": {
    "subscriptions": {
      "my_unique_request_id_for_contractsTrades.BTC_PERPETUAL": "contractsTrades.BTC_PERPETUAL",
      "my_unique_request_id_for_contractsTrades.BTC_PERPETUAL_2": "contractsTrades.BTC_PERPETUAL"
    }
  }
}
If you want to get your all subscriptions, you need to send getSubscriptions request

getSubscriptions

{
  "type": "getSubscriptions"
}
as result you will receive subscriptionList message

subscriptionList

{
  "server_timestamp": 1568802459143,
  "type": "subscriptionList",
  "payload": {
    "subscriptions": {
      "my_unique_request_id_for_contractsTrades.BTC_PERPETUAL": "contractsTrades.BTC_PERPETUAL",
      "my_unique_request_id_for_contractsTrades.BTC_PERPETUAL_2": "contractsTrades.BTC_PERPETUAL"
    }
  }
}
Data format definition
Contracts ticker update (contractsTickers channel)
Name	Type	Description	Required
offset	int	Unique update identifier	Yes
instrument_id	string	Instrument identifier	Yes
mark_price	decimal	Mark price	No
fair_price	decimal	Fair price	No
last_trade_price	decimal	Price of last trade	No
index_price	decimal	Price of underlying index	No
last_funding_time	int	Unix time of last funding, milliseconds	No
funding_rate	decimal	Current funding rate	No
funding_interval	int	Interval between funding, milliseconds	No
premium_index	decimal	Current premium index value	No
interest_rate	decimal	Interest rate	No
1d_high	decimal	Maximum price per last day	No
1d_low	decimal	Minimum price per last day	No
1d_volume	decimal	One day volume	No
best_bid	decimal	Best bid price in order book	No
best_ask	decimal	Best ask price in order book	No
price_change	decimal	Change of price for last 24 hours	No
Spot ticker update (spotTickers channel)
Name	Type	Description	Required
offset	int	Unique update identifier	Yes
trade_pair	string	Trade pair identifier	Yes
last_trade_price	decimal	Price of last trade	No
best_bid	decimal	Best bid price in order book	No
best_ask	decimal	Best ask price in order book	No
price_change	decimal	Change of price for last 24 hours	No
Trade on Contracts platform (contractsTrades channel)
Name	Type	Description	Required
offset	int	Unique update identifier	Yes
instrument_id	string	Instrument identifier	Yes
created_at	int	Unix timestamp of trade execution, milliseconds	Yes
taker_order_type	string	Type of taker order (BUY or SELL)	Yes
volume	decimal	Deal volume	Yes
price	decimal	Deal price	Yes
Trade on Spot (spotTrades channel)
Name	Type	Description	Required
offset	int	Unique update identifier	Yes
trade_pair	string	Trade pair identifier	Yes
created_at	int	Unix timestamp of trade execution, milliseconds	Yes
maker_buy	bool	True if maker have a buy side in deal	Yes
amount	decimal	Deal amount	Yes
price	decimal	Deal price	Yes
Contracts platform order book volume update (contractsOrderbookVolumes channel)
Name	Type	Description	Required
offset	int	Unique update identifier	Yes
instrument_id	string	Instrument identifier	Yes
volumes	map	Bids and asks volumes on prices	Yes
timestamp	int	Unix timestamp of change	Yes
Rate limit
If you want to limit incoming stream of data, you can send rate_limit parameter with subscribing (only for contractsTickers and spotTickers)

Rate limit example

{
  "type": "subscribe",
  "channel": "contractsTickers.GRAM_BTC_PERPETUAL",
  "request_id": "my-req-id-5",
  "params": {
    "rate_limit": 10
  }
}
rate_limit 10 means than you will receive maximum 10 updates per second.

HTTPS API
Tothemoon HTTPS API allows requests with JSON request body for POST endpoints and empty request body for GET endpoints.

Request Format
All POST requests must contain valid JSON body. All required params must be sent on JSON fields via POST or on URL params via GET.

POST request body example:

{
  "trade_pair": "BTC_USD"
}
GET request example:

GET https://api.tothemoon.com/v1/public/get-trades?trade_pair=BTC_USD
Response Format
Every endpoint returns a 200 HTTPS response code and JSON response body.

Successful response

Successful response has "OK" status and "data" JSON field.

{
  "status": "OK",
  "data": {},
  "error": null
}
Where "data" contains the result of request.

Error response

If request finishes with an error, response contains an "ERROR" status and "error" JSON field.

{
  "status": "ERROR",
  "error": { "code": "INSUFFICIENT_FUND", "message": null },
  "data": null
}
Where "error" contains "code" of the error and optionally contains an error "message".

Error Codes
Param name	Description
INSUFFICIENT_FUND	You don't have enough money for operation
INVALID_REQUEST	Invalid request arguments
INVALID_KEY	You need to send correct Access-Key and Secret-Key headers
INVALID_TIMESTAMP	Your timestamp must be within 30 seconds from the api server time. We can use the /public/time endpoint to query for the API server time.
PERMISSION_DENIED	Your API key does not have permissions for this request.
TOO_MANY_REQUESTS	You have reached the rate limit.
DUPLICATE_CLIENT_ORDER_ID	You can't create two orders with the same client_order_id
UNKNOWN_ERROR	Any other error
Types
Order nature

BUY
SELL
Order status

PENDING - an order is being prepared for placing at the exchange
NEW - an order is placed at the exchange
FINISHED - an order is fully executed
CANCELLED - an order is canceled
Time in force

GTC stands for a good ’til canceled order
GTD stands for a good 'til day order
FOK stands for a fill or kill order
IOC stands for an immediate or cancel order
Payment status

INITIALIZED - withdrawal is initialized and will be made soon
PENDING - withdrawal is started
COMPLETE - withdrawal is successfully completed
DECLINED - withdrawal is declined
Order book type

AGGREGATED
BEST (currently not supported)
FULL (currently not supported)
Candles interval types

M1 - each candle includes a one-minute interval
M20 - each candle includes a twenty-minute interval
H1 - each candle includes a one-hour interval
H6 - each candle includes a six-hour interval
D1 - each candle includes a one-day interval
Private
Private endpoints are only available for authorized users. To make a request for authorisation you need send your access key in Access-Key header and your secret key in Secret-Key header. Each private request must contain Nonce header. Nonce is a unique five-minute-interval number.

A nonce is an arbitrary number that can be used just once in a cryptographic communication. It is often a random or pseudo-random number issued in an authentication protocol to ensure that old communications cannot be reused in replay attacks.

The easiest way to deal with nonce is to increment nonce on every request you do.

Request headers example

POST /v1/private/get-balances HTTP/1.1
Content-Type: application/json
Accept: application/json
Content-Type: application/json
Content-Length: 235
Access-Key: KJuyg3bdi3ubycvebijckniugvbuibivujb=
Secret-Key: ih74gfyuevcbernivyeucwevbli3h3y4gr74yrgvb37guvbfb483vfy38iv==
Nonce: 23
Orders Management
At Tothemoon exchange you can place and cancel orders, and request for the information regarding the placed, canceled and executed orders.

Create order
Creates an order with the specified parameters

POST /v1/private/create-order
REQUEST PARAMETERS

Param name	Required	Description
trade_pair	Yes	A valid trading pair name
type	Yes	LIMIT or MARKET
side	Yes	BUY/SELL
time_in_force	No	IOC, FOK, GTC or GTD. GTC default
ttl	No	Only for GTD orders
amount	Yes	Decimal amount value
client_order_id	No	A unique integer id of an order
price	No	Decimal price value, required for LIMIT order type
quote_order_qty	No	Decimal, either amount or quote_order_qty must be set for MARKET order type
RESPONSE FIELDS

Param name	Required	Description
order_id	Yes	A number, an internal unique identifier of an order.
Response example

{
  "order_id": 265167535
}
Query for order
Returns the information about an order placed by a trader

GET /v1/private/get-order
REQUEST PARAMETERS

Param name	Required	Description
order_id	Yes	A valid order_id returned by create-order
RESPONSE FIELDS

Param name	Required	Description
order_id	Yes	A number, an internal unique identifier of an order
trade_pair	Yes	A trading pair name
type	Yes	LIMIT or MARKET
side	Yes	BUY/SELL
time_in_force	No	Time In Force of an order. IOC, FOK, GTC or GTD
ttl	No	Only for GTD orders
amount	Yes	Decimal amount value
executed_amount	Yes	A part of an order that is already executed
client_order_id	No	A unique id of an order specified by you at order creation
price	Yes	Decimal price value, specified by you at order creation
status	Yes	Current order status
created_at	Yes	Unix timestamp in UTC. Order creation time
done_at	No	Unix timestamp in UTC. Order completion time. Applicable only to completed orders.
Response data example

{
  "trade_pair": "BTC_USD",
  "side": "BUY",
  "type": "LIMIT",
  "status": "NEW",
  "order_id": 265167535,
  "client_order_id": 543,
  "price": "123.45",
  "amount": "0.21",
  "executed_amount": "0.1",
  "created_at": 1536669674
}
Cancel order
Cancel an order previously created by a user. Only orders with the NEW status can be canceled.

POST /v1/private/cancel-order
REQUEST PARAMETERS

Param name	Required	Description
order_id	Yes	A valid order_id returned by create-order
RESPONSE FIELDS

Param name	Required	Description
cancelled_order	Yes	A number, an internal unique identifier of an order
Response data example

{
  "cancelled_order": 265167535
}
Get all client orders
Returns the list of all user's orders of all statuses, not more than limit at a time

REQUEST PARAMETERS

GET /v1/private/get-orders
Param name	Required	Description
trade_pair	No	Valid trading pair name
status	No	Valid order status
limit	No	Max 500. Default 100
start_created_at	No	Unix timestamp in UTC timezone
ids	No	Comma separated string with order identifiers
RESPONSE FIELDS

The parameters are the same as for /v1/private/get-order

Response data example

[
  {
    "trade_pair": "BTC_USD",
    "side": "SELL",
    "type": "LIMIT",
    "status": "NEW",
    "order_id": 265167539,
    "client_order_id": 544,
    "price": "128.45",
    "amount": "0.5",
    "executed_amount": "0",
    "created_at": 1536669674,
    "time_in_force": "GTC"
  },
  {
    "trade_pair": "BTC_USD",
    "side": "BUY",
    "type": "LIMIT",
    "status": "FINISHED",
    "order_id": 265167540,
    "price": "128.45",
    "amount": "0.5",
    "executed_amount": "0.5",
    "created_at": 1536669695,
    "done_at": 1536669698,
    "time_in_force": "GTC"
  }
]
Cancel all orders
Cancels all orders with the NEW status

POST /v1/private/cancel-all-orders
Returns the list order_id of all canceled orders

Response data example

[265167535, 265167534, 265167015]
Trades
Returns the list of user's trades

List user trades
GET /v1/private/get-trades
REQUEST PARAMETERS

Param name	Required	Description
trade_pair	No	Valid trading pair name
limit	No	Max 500. Default 100
start	No	Unix timestamp in UTC timezone
order_id	No	Order identifier, within which trades are needed to be received
RESPONSE FIELDS

Param name	Required	Description
trade_pair	No	Valid trading pair name
side	Yes	BUY/SELL
order_id	Yes	A number, an internal unique identifier of an order
trade_id	Yes	A number, an internal unique identifier of a trader
price	Yes	Decimal price value, at which a trade has been carried out
amount	Yes	Decimal amount value
time	Yes	Unix timestamp in UTC timezone. Trade execution time
Response data example

[
  {
    "trade_pair": "BTC_USD",
    "side": "SELL",
    "order_id": 265167539,
    "trade_id": 746837892,
    "price": "128.45",
    "amount": "0.5",
    "time": 1536669696
  },
  {
    "trade_pair": "BTC_USD",
    "side": "BUY",
    "order_id": 265167540,
    "trade_id": 746837467,
    "price": "128.45",
    "amount": "0.5",
    "time": 1536669695
  }
]
Account
Get account balances
GET /v1/private/get-balances
Endpoint returns the dictionary, where keys are currencies and values are balances which include both the available amount of funds, and those on hold, which can not be used at the moment.

Response data example

{
  "BTC": { "available": "1.2", "on_hold": "0" },
  "USD": { "available": "342.1", "on_hold": "200" },
  "LTC": { "available": "23.62", "on_hold": "0" }
}
Payments
Payments via HTTPS API are only available for cryptocurrencies.

Generate new deposit address
To top up a cryptocurrency account at Tothemoon you can generate an address of the cryptocurrency wallet

POST /v1/private/create-deposit-address
REQUEST PARAMETERS

Param name	Required	Description
currency	Yes	Valid currency name, e.g.: USDT
network	No	Valid network type, e.g.: ETH, TRX, SOL
RESPONSE FIELDS

Param name	Required	Description
wallet	Yes	Crypto address which can be used for depositing
network	No	Network type of created address
Response data example:

{
  "wallet": "TKHuVq1oKVruCGLvqVexFs6dawKv6fQgFs",
  "network": "TRX"
}
Get already generated deposit address
To top up a cryptocurrency account you can also get an address that was previously generated. If you have not generated it earlier, it will be generated automatically

GET /v1/private/get-deposit-address
REQUEST PARAMETERS

Param name	Required	Description
currency	Yes	Valid currency name, e.g.: USDT
network	No	Valid network type, e.g.: ETH, TRX, SOL
RESPONSE FIELDS

Param name	Required	Description
wallet	Yes	Crypto address which can be used for depositing
network	No	Network type of created address
Response data example

{
  "wallet": "TKHuVq1oKVruCGLvqVexFs6dawKv6fQgFs",
  "network": "TRX"
}
Withdraw
Withdraws user's funds from the account to a specified address

POST /v1/private/create-withdrawal
REQUEST PARAMETERS

Param name	Required	Description
currency	Yes	Valid currency name
amount	Yes	Decimal amount value
wallet	Yes	Valid wallet address
client_payment_id	No	Client payment identifier, unique string
RESPONSE FIELDS

Param name	Required	Description
payment_id	Yes	Is a unique payment identifier.
Response data example

{
  "payment_id": "1d4b2661-35a3-4b73-ae76-121bf38b088c"
}
Get information about withdrawal
Returns the information about a previously made withdrawal

GET /v1/private/get-withdrawal
REQUEST PARAMETERS

Param name	Required	Description
payment_id	Yes	Valid payment id
RESPONSE FIELDS

Param name	Required	Description
status	Yes	Withdrawal status
currency	Yes	Currency name
amount	Yes	Decimal amount value
fee	Yes	Decimal fee value
transaction_info	No	Information about a withdrawal in the blockchain. Applicable only to withdrawals with the COMPLETE status
created_at	Yes	Unix timestamp in UTC. Withdrawal initialization time
completed_at	No	Unix timestamp in UTC. Withdrawal completion time. Applicable only to withdrawals with the COMPLETE status
payment_id	Yes	String identifier of payment
reason	Yes	Reason contains additional status info
to_wallet	Yes	Crypto address
client_payment_id	No	Client payment identifier
Response data example

{
  "payment_id": "1d4b2661-35a3-4b73-ae76-121bf38b088c",
  "status": "DECLINED",
  "amount": "0.23",
  "fee": "0.01",
  "currency": "BTC",
  "created_at": 1536669200,
  "completed_at": 1536669200,
  "transaction_info": {
    "blockchain_tx_ids": [
      "0x124129474b1dcbdb4e39436de49f7e5987f46dc4b8740966655718d7a1da699b"
    ],
    "tx_urls": [
      "https://sepolia.etherscan.io/tx/0x124129474b1dcbdb4e39436de49f7e5987f46dc4b8740966655718d7a1da699b"
    ]
  },
  "to_wallet": "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
  "reason": "insufficient funds"
}
Get information about withdrawals
Returns the information about a previously made withdrawals

GET /v1/private/get-withdrawals
REQUEST PARAMETERS

Param name	Required	Description
payment_id	No	Valid payment id
client_payment_id	No	Valid client payment id
start	No	Unix timestamp in UTC filter
limit	No	Max 500
RESPONSE FIELDS

The parameters are the same as for /v1/private/get-withdrawal

Response data example

[
  {
    "payment_id": "1d4b2661-35a3-4b73-ae76-121bf38b088c",
    "status": "COMPLETE",
    "amount": "0.23",
    "fee": "0.00000015",
    "currency": "BTC",
    "created_at": 1536669200,
    "completed_at": 1536669200,
    "transaction_info": {
      "blockchain_tx_ids": [
        "0x124129474b1dcbdb4e39436de49f7e5987f46dc4b8740966655718d7a1da699b"
      ],
      "tx_urls": [
        "https://sepolia.etherscan.io/tx/0x124129474b1dcbdb4e39436de49f7e5987f46dc4b8740966655718d7a1da699b"
      ]
    },
    "to_wallet": "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
    "reason": "some meta info string"
  },
  {
    "payment_id": "0411919f-7a02-432c-9138-b15d27fa1d21",
    "status": "COMPLETE",
    "amount": "0.42",
    "fee": "0.00000015",
    "currency": "BTC",
    "created_at": 1536669345,
    "completed_at": 1536669345,
    "transaction_info": {
      "blockchain_tx_ids": [
        "0x124129474b1dcbdb4e39436de49f7e5987f46dc4b87409666523452345234554"
      ],
      "tx_urls": [
        "https://sepolia.etherscan.io/tx/0x124129474b1dcbdb4e39436de49f7e5987f46dc4b87409666523452345234554"
      ]
    },
    "to_wallet": "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
    "reason": "some meta info string"
  }
]
Get information about deposits
Returns the information about a previously made deposits

GET /v1/private/get-deposits
REQUEST PARAMETERS

Param name	Required	Description
payment_id	No	Valid payment id
start	No	Unix timestamp in UTC filter
limit	No	Max 500
currency	No	Valid currency name
to_wallet	No	Crypto address
status	No	Deposit processing status
RESPONSE FIELDS

Param name	Required	Description
payment_id	Yes	String identifier of payment
amount	Yes	Decimal amount value
fee	Yes	Decimal fee value
currency	Yes	Currency name
to_wallet	Yes	Crypto address
status	Yes	Deposit status
blockchain_tx_ids	Yes	Information about a Deposit in the blockchain
tx_urls	Yes	Link to blockchain explorer
created_at	Yes	Unix timestamp in UTC. Withdrawal initialization time
client_payment_id	No	Client payment identifier
reason	Yes	Reason contains additional status info
confirmations	Yes	Confirmations amount in blockchain
needed_confirmations	Yes	Amount of required blockchain confirmations
address_tag	No	Address tag
Response data example

[
  {
    "payment_id": "1d4b2661-35a3-4b73-ae76-121bf38b088c",
    "amount": "42",
    "fee": "0.00000015",
    "currency": "BTC",
    "to_wallet": "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
    "status": "COMPLETE",
    "blockchain_tx_ids": [
      "0x124129474b1dcbdb4e39436de49f7e5987f46dc4b87409666523452345234554"
    ],
    "tx_urls": [
      "https://sepolia.etherscan.io/tx/0x124129474b1dcbdb4e39436de49f7e5987f46dc4b87409666523452345234554"
    ],
    "created_at": 1536669345,
    "reason": "some meta info string",
    "confirmations": 3,
    "needed_confirmations": 2
  },
  {
    "payment_id": "224b2661-15a3-2b73-ae76-121bf38b4823",
    "amount": "0.2",
    "fee": "0.0000000043",
    "currency": "BTC",
    "to_wallet": "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
    "status": "COMPLETE",
    "blockchain_tx_ids": [
      "0x245129474b1dcbdb4e39436de49f7e5987f46dc4b87409666523452345232312"
    ],
    "tx_urls": [
      "https://sepolia.etherscan.io/tx/0x245129474b1dcbdb4e39436de49f7e5987f46dc4b87409666523452345232312"
    ],
    "created_at": 1536669345,
    "reason": "some meta info string",
    "confirmations": 3,
    "needed_confirmations": 2
  }
]
Get information about deposit batch
Returns the information about a previously made deposits

POST /v1/private/get-deposits-batch
REQUEST PARAMETERS

Param name	Required	Description
start	No	Unix timestamp in UTC filter
status	No	Deposit processing status
currency_address_pairs	Yes	Array of currency address pairs
currency_address_pairs.currency	Yes	Currency name
currency_address_pairs.to_wallet	Yes	Crypto address
Request example

{
  "start": 1536669345,
  "status": "NEW",
  "currency_address_pairs": [
    {
      "currency": "BTC",
      "to_wallet": "1BoatSLRHtKNngkdXEeobR76b53LETtpyT"
    }
  ]
}
RESPONSE FIELDS

The parameters are the same as for /v1/private/get-deposits

Response data example

[
  {
    "payment_id": "1d4b2661-35a3-4b73-ae76-121bf38b088c",
    "amount": "42",
    "fee": "0.00000015",
    "currency": "BTC",
    "to_wallet": "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
    "status": "COMPLETE",
    "blockchain_tx_ids": [
      "0x124129474b1dcbdb4e39436de49f7e5987f46dc4b87409666523452345234554"
    ],
    "tx_urls": [
      "https://sepolia.etherscan.io/tx/0x124129474b1dcbdb4e39436de49f7e5987f46dc4b87409666523452345234554"
    ],
    "created_at": 1536669345,
    "reason": "some meta info string",
    "confirmations": 3,
    "needed_confirmations": 2
  },
  {
    "payment_id": "224b2661-15a3-2b73-ae76-121bf38b4823",
    "amount": "0.2",
    "fee": "0.0000000043",
    "currency": "BTC",
    "to_wallet": "1BoatSLRHtKNngkdXEeobR76b53LETtpyT",
    "status": "COMPLETE",
    "blockchain_tx_ids": [
      "0x245129474b1dcbdb4e39436de49f7e5987f46dc4b87409666523452345232312"
    ],
    "tx_urls": [
      "https://sepolia.etherscan.io/tx/0x245129474b1dcbdb4e39436de49f7e5987f46dc4b87409666523452345232312"
    ],
    "created_at": 1651225749,
    "reason": "some meta info string",
    "confirmations": 4,
    "needed_confirmations": 1
  }
]
Create wire withdrawal
Withdraws user's funds from the account to a saved credentials uid

POST /v1/private/create-wire-withdrawal
REQUEST PARAMETERS

Param name	Required	Description
currency	Yes	Currency name
amount	Yes	Decimal amount value
saved_credentials_uid	Yes	Previously saved bank account uid
Request example

{
  "currency": "USD",
  "amount": "42",
  "saved_credentials_uid": "1d4b2661-35a3-4b73-ae76-121bf38b088c"
}
RESPONSE FIELDS

Param name	Required	Description
payment_id	Yes	Payment ID
Response data example

{
  "payment_id": "1d4b2661-35a3-4b73-ae76-121bf38b088c"
}
Get wire withdrawal statuses
Get statuses of previously made wire withdrawals

GET /v1/private/get-wire-withdrawal
REQUEST PARAMETERS

Param name	Required	Description
payment_id	No	ID of previously made wire payment
creation_date	No	Date filter of wire withdrawal, if empty returns last 24h withdrawals
status	No	Status filter, can accept multiple values
RESPONSE FIELDS

Param name	Required	Description
payment_id	Yes	Wire withdrawal ID
status	Yes	Wire withdrawal status
Response data example

[
  {
    "payment_id": "29bd4985-1b8e-40ef-9768-77b81d7721cb",
    "status": "COMPLETE"
  },
  {
    "payment_id": "522244ad-cef4-4428-8830-10fffb5d8dcb",
    "status": "PENDING"
  }
]
Public
Public endpoints are available without authorization.

List available trading pairs
Get available trading pairs

GET /v1/public/get-trade-pairs
RESPONSE FIELDS

Param name	Required	Description
trade_pair	Yes	Trading pair name
base_currency	Yes	Base currency
quoted_currency	Yes	Quoted currency
Response data example

[
  {
    "trade_pair": "BTC_USD",
    "base_currency": "BTC",
    "quoted_currency": "USD"
  },
  {
    "trade_pair": "LTC_BTC",
    "base_currency": "LTC",
    "quoted_currency": "BTC"
  }
]
Get order book
Returns the current order book for the specified pair in accordance with the bid and ask in a list format containing pairs "price" and "amount".

GET /v1/public/get-order-book
REQUEST PARAMETERS

Param name	Required	Description
trade_pair	Yes	Valid trading pair name
Response data example

{
  "asks": [
    ["905.95", "0.1"],
    ["906.00", "0.05"],
    ["906.2", "0.2"]
  ],
  "bids": [
    ["905.45", "0.5"],
    ["904.00", "0.9"],
    ["902.00", "0.3"]
  ]
}
List recent trades
GET /v1/public/get-trades
REQUEST PARAMETERS

Param name	Required	Description
trade_pair	Yes	Valid trading pair name
limit	No	Max 500. Default 100
start	No	Unix timestamp in UTC timezone
order_id	No	Integer order identifier
RESPONSE FIELDS

Param name	Required	Description
trade_id	Yes	A number, an internal unique identifier of a trade
price	Yes	Decimal price value, at which a trade was executed
amount	Yes	Decimal amount value
time	Yes	Unix timestamp in UTC timezone. Trade execution time
Response data example:

[
  {
    "trade_id": 45678878,
    "price": "128.45",
    "amount": "0.5",
    "time": 1536669632
  },
  {
    "trade_id": 45678879,
    "price": "128.80",
    "amount": "0.2",
    "time": 1536669632
  }
]
List candles
Returns the list of candles according to the specified parameters. Each candle starts from the time rounded to an interval.

GET /v1/public/get-candles
REQUEST PARAMETERS

Param name	Required	Description
trade_pair	Yes	Valid trading pair name
interval	Yes	Supported candles interval
start	Yes	Start UNIX timestamp
end	Yes	End UNIX timestamp in UTC timezone
Maximum data points that can be requested is 300 candles.

RESPONSE FIELDS

Param name	Required	Description
open	Yes	Decimal price value, at which the first trade was executed within a candle period
high	Yes	Maximum decimal price value, at which a trade was executed within a candle period
low	Yes	Minimum decimal price value, at which a trade was executed within a candle period
close	Yes	Decimal price value, at which the last trade was executed within a candle period
avg	Yes	Average decimal price value of trades executed within a candle period
base_volume	Yes	Trading volume in a base currency within a candle period
time	Yes	Unix timestamp in UTC timezone. Candle start time
Response data example

[
  {
    "time": 1536669600,
    "open": "128.76",
    "high": "135.2",
    "low": "127",
    "close": "127",
    "avg": "132.76",
    "base_volume": "12"
  },
  {
    "time": 1536669660,
    "open": "127",
    "high": "130",
    "low": "127",
    "close": "127",
    "avg": "128.2",
    "base_volume": "3"
  }
]
Get 24 hour statistics
Returns statistics within previous 24 hours.

GET /v1/public/get-24hrs-stat
REQUEST PARAMETERS

Param name	Required	Description
trade_pair	Yes	Valid trading pair name
RESPONSE FIELDS

Param name	Required	Description
open	Yes	Decimal price value, at which the first trade was executed within a candle period
high	Yes	Maximum decimal price value, at which a trade was executed within a candle period
low	Yes	Minimum decimal price value, at which a trade was executed within a candle period
base_volume	Yes	Trading volume in a base currency within a candle period
Response data example

{
  "open": "128.76",
  "high": "135.2",
  "low": "128",
  "base_volume": "765.2"
}
