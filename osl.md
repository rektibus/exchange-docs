OSL API Introduction
Welcome to the OSL API reference documentation. Here you will find a single, consolidated library for all application programming interfaces (API) offered by OSL’s platform.

This document provides the details required to use OSL's REST, WebSocket and FIX protocols which are organized into our key business functions.

Please direct any questions or feedback to support@osl.com.

📘
The REST API / WebSocket API / FIX API access
A premium feature available exclusively to Corporate, Institutional, Professional Investor (PI), and omnibus clients. Retail users are not eligible for API functionality.

What you can do with OSL API
Business Functions
OSL operates a brokerage platform, an exchange venue and a custody solution.

Through our digital asset markets business, we deliver a world-class digital asset offering for professional clients which includes brokerage, exchange and custody, all of which are supported by industry-leading customer service.

Brokerage
Through OSL's brokerage offering, clients can access institutional-size liquidity with tight spreads on principal basis. Trades can be executed over-the-counter with our global sales trading team, or electronically through our E-Trade (Electronic Trade) or RFQ (Request for Quote) capabilities.

Exchange
OSL's exchange provides institutional-grade access to spot markets using an aggregated Central Limit Order Book (CLOB) model which provides shared liquidity access with OSL’s global SaaS partners. The OSL exchange has an ultra-low latency matching engine and is accessible directly via API (FIX, REST & WebSocket), native browser GUI and other OMS/EMS vendor partners. Finally, participants are protected by the integration of a full suite of compliance tools including market surveillance and transaction monitoring.

Custody
OSL provides industry leading insured custody for digital assets, including comprehensive protection of customer assets for cold wallets and insurance for loss, damage, destruction, or theft of private keys.







API Summary
Supported API Methods
REST
REST API’s are available for our OSL Exchange users and OSL Brokerage users. Both APIs are expressive and offer a variety of functionality in line with the latest crypto industry standards.

WebSocket
WebSocket API offers market data streams in an easy to process JSON format for both our OSL Exchange users and our OSL Brokerage users.

FIX
OSL supports order entry, market data and drop copy using the FIX 4.4 protocol for OSL Exchange users. Connectivity options to our FIX gateway is described in more detail in the FIX section of this library.

❗
Example codes are for demonstration purposes only.
Some aspects may have been simplified for clarity, while some other codes may have been generated automatically. Please ensure you follow established production rollout guidelines before you run your application.

Overview of API Availability
Function	Available Site	REST V3	REST V4	WebSocket	FIX
Brokerage (RFQ)	HK	✅			
Brokerage (E-Trade)				✅	
Exchange	HK	✅	✅	✅ (Market Data)	✅
General	HK	✅			



Environments
To cater for our geographically distributed clients we offer 3 base URLs for both Production and Sandbox environments.

Sandbox
The OSL Sandbox environment provides full exchange and brokerage capabilities allowing you to try them out with test funds.

Please note that your experience in the sandbox environments may differ slightly from that of the current production implementation.

Activity Simulation: In the Sandbox environment, we have an activity simulation script running to simulate market activity for testing purposes. This ensures a realistic market environment for your testing needs.

Before you start contact us at support@osl.com and request your sandbox account.

Once your sandbox account has been set up please use the Base URL that is most suitable for your geographical location or the one which your account manager has advised you to use:

Hong Kong: trade-hk.oslsandbox.com
Australia: trade-au.oslsandbox.com
🚧
​​We will be using the Hong Kong sandbox base URL from this point forward trade-hk.oslsandbox.com unless otherwise specified.
Production
Once your production account has been set up please use the base URL that is most suitable for your geographical location or the one which your account manager has advised you to use:

Hong Kong: trade-hk.osl.com
Australia: trade-au.osl.com
Once your account is live and you have made a note of your base URL the next step is to authenticate.



Rate Limits
To prevent abuse, OSL imposes rate limits on incoming requests.

📘
REST API rate limits are controlled by IP.
They are not applied per user profile or per API key.

REST V3
For V3 endpoints, we limit requests to 30 requests per second for each IP. For trading API entry points, we limit requests to 100 requests per second for each IP.

REST V4
For all V4 endpoints, we limit requests to 200 requests per second for each IP.

WebSocket
The publication frequency and depth of prices are set by OSL and are currently set to 1 updates per second at a maximum depth of 25 levels per side.

FIX
For FIX protocol, we limit requests to 500 requests per second for each session.




Response / Error Code Reference
📘
Only common response codes are listed here. For endpoint specific codes, please check individual endpoint pages.
REST
Quote Response errorCode Code Table
Code	Description
p200021	No fallback pricing
p500005	Internal error (please check with support)
p500019	Internal error (please check with support)
s200003	Base currency is not supported
s200004	Quote currency is not supported
s200015	Merchant configuration cannot be found
s300001	Invalid exchange rates
s500018	Internal error (please check with support)
s300019	Exchange rates are not available
s500024	Internal error (please check with support)
s500025	Internal error (please check with support)
Trade Response errorCode Code Table
Code	Description
s200003	Base currency is not supported
s200004	Quote currency is not supported
s300001	Invalid exchange rates
s100002	Invalid quote ID
s100005	Trade already exists for the quote ID
s100006	Quote expired
s100026	Quote expired
s400010	Internal error (please check with support)
s400011	Internal error (please check with support)
s400012	Debit account not found
s400013	Debit account have insufficient fund
s400024	Internal error (please check with support)
s400025	Internal error (please check with support)
resultCode Code Table
Code	Description
ORDER_REQUEST_SUBMITTED	Order request submitted. It is generally considered a successful response
INSUFFICIENT_AVAILABLE_BALANCE	Order submission failed as insufficient available balance
TOO_MANY_OPEN_ORDERS	Order submission failed as too many open orders on the exchange
TOO_SMALL	Order submission failed as the order value is too small
SIMPLE_TRADE_DISABLED	RFQ function has been disabled for the account
USER_NOT_VERIFIED	Order submission failed as the account has not been verified for trading
USER_ACTIVITY_RESTRICTED	Account has been restricted to perform a certain action
INVALID_PARAMETERS	Action failed due to invalid parameter(s), including wrong currency pair, order amount/rate too big, too many decimal places, etc
SYSTEM_ERROR	General error
ordStatus Code Table (V4)
Code	Description
New	The order is active and unexecuted on the exchange
PartiallyFilled	The order is active and partially filled on the exchange
Filled	The order is fully filled and no longer active on the exchange
Cancelled	The order is cancelled and no longer active on the exchange
Replaced	The order is amended
Rejected	The order is rejected and no longer active on the exchange
Suspended	The order is suspended
Expired	The order is expired and no longer active on the exchange
Withdrawn	The order is withdrawn to prevent self trade orders
orderState Code Table (V3)
Code	Description
ACTIVE	The order is active and unexecuted on the exchange
PARTIAL_FILL	The order is active and partially filled on the exchange
FULL_FILL	The order is fully filled and no longer active on the exchange
EXPIRED	The order is expired (past expiry date / time) and no longer active on the exchange
PENDING_SUBMISSION	The order is pending processing by the exchange. Need to call an order enquiry to get the latest state
WebSocket
orderStatus Code Table
Code	Description
SUCCESS	The order has been successfully executed
INDETERMINATE	The order is in an undetermined state
FAILED	The order failed to execute
FIX
FIX Error Codes
Code	Error Name	Description
1002	SystemSuspended	System is suspended
1106	UsermanagerSuspended	User is suspended
1192	SessionError	Session error
19087	InvalidOrder	Order is invalid
20002	OrderInvalidSide	Order get rejected with invalid side
20003	OrderInvalidType	Order get rejected with invalid type
20004	OrderInvalidPrice	Order get rejected with invalid price
20005	OrderInvalidQuantity	Order get rejected with invalid quantity
20007	OrderInvalidExpiryDate	Order get rejected with invalid expiry date
20008	OrderInvalidExpiryTime	Order get rejected with invalid expiry time
20009	OrderInvalidPriceStep	Order get rejected with invalid price step
20015	OrderUserSuspended	Order get rejected with user being suspended
20024	OrderInsufficientHoldings	Order get rejected with insufficient holdings
20025	OrderNoHoldings	Order get rejected with no holdings
20026	OrderQuantityTooSmall	Order get rejected with quantity smaller than the minimum quantity
20027	OrderQuantityTooLarge	Order get rejected with quantity larger than the maximum quantity
20031	OrderInsufficientCash	Order get rejected with insufficient Cash
20032	OrderInvalidCurrency	Order get rejected with invalid currency
20033	OrderInvalidSettlementCurrency	Order get rejected with invalid settlement currency
20062	OrderValueTooSmall	Order value cannot be too small
20063	OrderValueTooLarge	Order value cannot be too large
20066	OrderInvalidQuantityStep	Order get rejected with invalid quantity step
20088	OrderInstrumentmarketClosed	Order get rejected because instrument market is closed
20115	OrderPriceZero	Order price cannot be zero
20116	OrderPriceNegative	Order price cannot be negative
20117	OrderPriceTooLow	Order price cannot be too low
20118	OrderPriceTooHigh	Order price cannot be too high
20132	OrderNotMatched	Order get rejected with no other orders to match against
22213	OrderStatusSetNoCancelMatched	Order matched, cancel not allowed
22215	OrderStatusSetNoCancelCancelled	Order cancelled, cancel not allowed
22301	OrderAmendNotAvailable	Failed to amend an order which has already filled






REST V4


REST V4

Get Currency-Pairs
get
Create New Order
post
Cancel Order(s)
del
Cancel All Orders
del
Get Orders
get
Get Executions
get
Get Executions of an Order
get
Get Order Book
get
Get Exchange Wallet
get
Get Exchange Trade List
get
REST V3

WebSocket

FIX - Overview

FIX - Session Management

FIX - Order Management

FIX - Drop Copy Management
FIX - Market Data Management

Custody
REST

Public
REST

Account
REST

Powered by 

Get Currency-Pairs
get
https://trade-hk.oslsandbox.com/api/v4/instrument

Get the currency-pair information. All available currency-pairs for retail users will be returned by default. PI can also implement API key to get all currency-pairs supported for PI.

Response Body
Field

Description

symbol

Currency pair, i.e. BTCUSD

currency

Currency of the asset for the quoted market price

settlCurrency

Currency in which the price is settled in

highPrice

Highest traded price of the pair within the prior rolling 24 hour window

lowPrice

Lowest traded price of the currency pair within the prior rolling 24 hour window

bidPrice

Current bid price

askPrice

Current ask price

lastPrice

Last traded price

minPrice

Minimum price allowed to order for this currency pair

maxPrice

Maximum price allowed to order for this currency pair

minOrderQty

Minimum quantity allowed to order for this currency pair (in currency)

maxOrderQty

Maximum quantity allowed to order for this currency pair (in currency)

minValue

Minimum allowed order value (in settlement currency)
i.e. order value = order qty x price

maxValue

Maximum allowed order value (in settlement currency)
i.e. order value = order qty x price

prevClosePrice

Last price traded in the previous trading cycle

volume

The traded volume of the currency pair in the prior rolling 24 hour window

tickSize

The minimum price movement of the currency pair.

stepSize

The minimum quantity movement of the currency pair.

priceDecimals

The number of decimal places used to display the price.

quantityDecimals

The number of decimal places used to display the quantity.

updateTime

The last trade time

Query Params
symbol
string
Defaults to BTCUSD
Currency-pair. If empty, all currency-pairs are returned.

BTCUSD
Responses

200
200


400
400


403
403


404
404


REST V4

Get Currency-Pairs
get
Create New Order
post
Cancel Order(s)
del
Cancel All Orders
del
Get Orders
get
Get Executions
get
Get Executions of an Order
get
Get Order Book
get
Get Exchange Wallet
get
Get Exchange Trade List
get
REST V3

WebSocket

FIX - Overview

FIX - Session Management

FIX - Order Management

FIX - Drop Copy Management
FIX - Market Data Management

Custody
REST

Public
REST

Account
REST

Powered by 

Get Order Book
get
https://trade-hk.oslsandbox.com/api/v4/orderBook/L2

Get the order book of a particular coin-pair.

Query Params
symbol
string
required
Currency-pair.

depth
string
Defaults to 25
Order book depth per side. Send 0 for full depth.

25
Responses

200
200


400
400


401
401


404
404




REST V4

Get Currency-Pairs
get
Create New Order
post
Cancel Order(s)
del
Cancel All Orders
del
Get Orders
get
Get Executions
get
Get Executions of an Order
get
Get Order Book
get
Get Exchange Wallet
get
Get Exchange Trade List
get
REST V3

WebSocket

FIX - Overview

FIX - Session Management

FIX - Order Management

FIX - Drop Copy Management
FIX - Market Data Management

Custody
REST

Public
REST

Account
REST

Powered by 

Get Orders
get
https://trade-hk.oslsandbox.com/api/v4/order

Get the list of all orders in chronological order. By default, only open orders are returned. Inactive orders are retrievable only for a limited period of time.

ordStatus Code Table
Code	Description
New	The order is active and unexecuted on the exchange
PartiallyFilled	The order is active and partially filled on the exchange
Filled	The order is fully filled and no longer active on the exchange
Cancelled	The order is cancelled and no longer active on the exchange
Replaced	The order is amended
Rejected	The order is rejected and no longer active on the exchange
Suspended	The order is suspended
Expired	The order is expired and no longer active on the exchange
Withdrawn	The order is withdrawn to prevent self trade orders
Query Params
symbol
string
Currency-pair. If empty, all currency-pairs are returned.

open
boolean
Defaults to true
When true return active/open orders only.


true
orderID
string
Order ID.

clOrdID
string
Client order ID.

start
int32
Defaults to 0
Pagination start point for results. e.g. start=1 skips the first result, start=100 skips the first 100 results. Default is 0.

0
count
int32
Defaults to 100
The number of results to fetch. Must be a positive integer. Supports returning up to 1000 results at maximum, with the default of 100. Pagination may be required if more results are available.

100
reverse
boolean
Defaults to false
TRUE - Reverse chronological order. FALSE - chronological order.


false
startTime
date-time
Filter results based on the start date and time. The timestamp must be ISO-8601 format (YYYY-MM-DDTHH:mm:ss.sssZ) and be in the UTC timezone. e.g. "2023-12-31T23:59:59.999Z".

endTime
date-time
Filter results based on the end date and time. The timestamp must be ISO-8601 format (YYYY-MM-DDTHH:mm:ss.sssZ) and be in the UTC timezone. e.g. "2023-12-31T23:59:59.999Z".

Responses

200
200


400
400


401
401


404
404


REST V4

Get Currency-Pairs
get
Create New Order
post
Cancel Order(s)
del
Cancel All Orders
del
Get Orders
get
Get Executions
get
Get Executions of an Order
get
Get Order Book
get
Get Exchange Wallet
get
Get Exchange Trade List
get
REST V3

WebSocket

FIX - Overview

FIX - Session Management

FIX - Order Management

FIX - Drop Copy Management
FIX - Market Data Management

Custody
REST

Public
REST

Account
REST

Powered by 

Get Executions
get
https://trade-hk.oslsandbox.com/api/v4/execution

Get the list of all executions in chronological order.

Query Params
symbol
string
Currency-pair. If empty, all currency-pairs are returned.

orderID
string
Order ID.

clOrdID
string
Client order ID.

start
int32
Defaults to 0
Pagination start point for results. e.g. start=1 skips the first result, start=100 skips the first 100 results. Default is 0.

0
count
int32
Defaults to 100
The number of results to fetch. Must be a positive integer. Supports returning up to 500 results at maximum, with the default of 100. Pagination may be required if more results are available.

100
reverse
boolean
Defaults to false
TRUE - Reverse chronological order. FALSE - chronological order.


false
startTime
date-time
Filter results based on the start date and time. The timestamp must be ISO-8601 format (YYYY-MM-DDTHH:mm:ss.sssZ) and be in the UTC timezone. e.g. "2023-12-31T23:59:59.999Z".

endTime
date-time
Filter results based on the end date and time. The timestamp must be ISO-8601 format (YYYY-MM-DDTHH:mm:ss.sssZ) and be in the UTC timezone. e.g. "2023-12-31T23:59:59.999Z".

Responses

200
200


400
400


401
401


404
404


REST V4

Get Currency-Pairs
get
Create New Order
post
Cancel Order(s)
del
Cancel All Orders
del
Get Orders
get
Get Executions
get
Get Executions of an Order
get
Get Order Book
get
Get Exchange Wallet
get
Get Exchange Trade List
get
REST V3

WebSocket

FIX - Overview

FIX - Session Management

FIX - Order Management

FIX - Drop Copy Management
FIX - Market Data Management

Custody
REST

Public
REST

Account
REST

Powered by 

Get Executions of an Order
get
https://trade-hk.oslsandbox.com/api/v4/execution/order

Get all executions of a particular order. This endpoint can only return today's data.

📘
Either orderID or clOrdID array needs to be present in the request, but not both.
ordStatus Code Table
Code	Description
New	The order is active and unexecuted on the exchange
PartiallyFilled	The order is active and partially filled on the exchange
Filled	The order is fully filled and no longer active on the exchange
Cancelled	The order is cancelled and no longer active on the exchange
Replaced	The order is amended
Rejected	The order is rejected and no longer active on the exchange
Suspended	The order is suspended
Expired	The order is expired and no longer active on the exchange
Withdrawn	The order is withdrawn to prevent self trade orders
Query Params
orderID
string
Order ID.

clOrdID
string
Client order ID.

Responses

200
200


400
400


401
401


403
403


404
404


REST V4

Get Currency-Pairs
get
Create New Order
post
Cancel Order(s)
del
Cancel All Orders
del
Get Orders
get
Get Executions
get
Get Executions of an Order
get
Get Order Book
get
Get Exchange Wallet
get
Get Exchange Trade List
get
REST V3

WebSocket

FIX - Overview

FIX - Session Management

FIX - Order Management

FIX - Drop Copy Management
FIX - Market Data Management

Custody
REST

Public
REST

Account
REST

Powered by 

Get Exchange Trade List
get
https://trade-hk.oslsandbox.com/api/v4/trade

Get the list of recent trades on the exchange. Default time slot is 1 hour.

Query Params
symbol
string
Currency-pair. If empty, all currency-pairs are returned.

reverse
boolean
Defaults to false
TRUE - Reverse chronological order. FALSE - chronological order.


false
startTime
date
Filter results based on the start date and time. The timestamp must be ISO-8601 format (YYYY-MM-DDTHH:mm:ss.sssZ) and be in the UTC timezone. e.g. "2023-12-31T23:59:59.999Z".

endTime
date
Filter results based on the end date and time. The timestamp must be ISO-8601 format (YYYY-MM-DDTHH:mm:ss.sssZ) and be in the UTC timezone. e.g. "2023-12-31T23:59:59.999Z".

lastHour
string
Defaults to false
Override startTime and endTime if True. True: Return trade with endTime is last trade time. False: Return trades with endTime is now time.

false
Responses

200
200


400
400


401
401


404
404








Establish Connection
Subscription Endpoint Details
The structure of the URL is:

wss://<root>/ws/v4?subscribe=<instruments>
Each price subscription is of the format orderBook: e.g. orderBook:BTCUSD
Multiple subscriptions can be created on one connection by using a comma separated list of subscriptions e.g. orderBook:BTCUSD,orderBook:LTCUSD
Below shows an example subscription for BTC/USD and LTC/USD on a single connection:

wss://trade-hk.oslsandbox.com/ws/v4?subscribe=orderBook:BTCUSD,orderBook:LTCUSD

📘
The publication frequency and depth are set by OSL and are currently set to 2 updates per second at a maximum depth of 50 levels per side.
If subscription is submitted for an instrument that does not exist the subscription will be rejected with HTTP code 404, if multiple instruments are subscribed to all subscriptions are rejected if one of the instrument does not exist.

Market Data Message Details
All messages are published in JSON format. Each message contains a field called action which determines how the message should be processed by the client. A message may contain multiple price data elements that always contain a price, a side and conditionally a size.

The combination of price and side is guaranteed unique and in a naive implementation of unordered books this pair could be used as the key to a hash based map.




Subscribe to Market Data
The value of action specifies how the message should be handled; each action type is outlined in following sections with an example message. There are 5 action types.

Partial
Insert
Update
Delete
Heartbeat
Partial Message
Action partial means the message is a new snapshot message, the client should remove the existing view of the order book and replace it with prices and sizes specified in the body of the message.

JSON

{
  "table": "orderBookL2",
  "action": "partial",
  "symbol": "BTCUSD",
  "bookVersionId": 1,
  "sendTime": 1632330416488,
  "keys": [
    "symbol",
    "id",
    "side"
  ],
  "data": [
    {
      "symbol": "BTCUSD",
      "side": "Buy",
      "size": "1.0",
      "price": "43000.0"
    }
  ]
}
Insert Message
Action insert means insert or replace the current value of that price level with the new value; the value is the new absolute position for that price level. Only the size will be changed in the event of an order's price being amended the appropriate combination of insert/append and delete messages will be published to amend the appropriate levels.

JSON

{
  "table": "orderBookL2",
  "action": "insert",
  "symbol": "BTCUSD",
  "bookVersionId": 206,
  "sendTime": 1632335161128,
  "publishTime": 1632335161441,
  "data": [
    {
      "symbol": "BTCUSD",
      "side": "Sell",
      "size": "177.0",
      "price": "47228.0"
    },
    {
      "symbol": "BTCUSD",
      "side": "Sell",
      "size": "102.0",
      "price": "48935.0"
    }
  ]
}
Update Message
Action update means insert or replace the current value of that price level; the value is the new absolute position for that price level.

JSON

{
  "table": "orderBookL2",
  "action": "update",
  "symbol": "BTCUSD",
  "bookVersionId": 207,
  "sendTime": 1632335161128,
  "publishTime": 1632335161441,
  "data": [
    {
      "symbol": "BTCUSD",
      "side": "Sell",
      "size": "177.0",
      "price": "47228.0"
    },
    {
      "symbol": "BTCUSD",
      "side": "Sell",
      "size": "102.0",
      "price": "48935.0"
    }
  ]
}
Delete Message
Action delete means remove the price level; if the price level does not exist the message should be ignored.

JSON

{
  "table": "orderBookL2",
  "action": "delete",
  "symbol": "BTCUSD",
  "bookVersionId": 208,
  "sendTime": 1632335161128,
  "publishTime": 1632335161441,
  "data": [
    {
      "symbol": "BTCUSD",
      "side": "Sell",
      "price": "46823.0"
    }
  ]
}
Heartbeat Message
Action heartbeat is a keep alive message sent every 30 seconds for each instrument if there are no updates in that time interval.

JSON

{
  "table": "orderBookL2",
  "timestamp": 1632334653163,
  "action": "heartbeat",
  "symbol": "BTCUSD"
}




Get Currency Pair
get
https://trade-hk.oslsandbox.com/api/3/currencyStatic

Response Body
Fields	Type	Description
timestamp	string	UNIX timestamp in milliseconds. Example: 1632390252603
resultCode	string	Result code reflecting the success status of the operation. Example: OK
currencyStatic	[currencyStatic]	Contains static details of each currency available from the platform. See Currency static object parameters.
Currency static object parameters
Fields	Type	Description
currencies	[currency]	Map of currency and currency settings. See Currency object parameters.
currencyPairs	[currencyPair]	Map of Currency Pair and Currency Pair Settings. See Currency pair object parameters.
Currency object parameters
Fields	Type	Description
decimals	int	Decimal place used for trading. Example: 8
minOrderSize	decimal	Minimum order size. Example: 0.00020000
maxOrderSize	decimal	Maximum order size. Example: 100000.00000000
minOrderValue	decimal	Minimum order value. Example: 1.0E-7
maxOrderValue	decimal	Minimum order value. Example: 100000000.00000000
maxMarketOrderValue	decimal	Maximum market order value. Example: 10.00000000
maxMarketOrderSize	decimal	Maximum market order size. Example: 10.00000000
displayDenominator	decimal	Display denominator. Example: 1000
summaryDecimals	int	Decimals place used to display summary. Example: 2
displayUnit	string	Currency unit
symbol	string	Symbol of the currency
type	string	CRYPTO or FIAT
confirmationThresholds	decimal	Confirmation thresholds
networkFee	decimal	Standard network fee
engineSettings	[engineSetting]	List of engine settings. See Fund engine setting object parameters.
urlPrefix	string	Url prefix to handle the related coin address
digitalCurrencyType	string	Crypto currency type. Example: RIPPLE, RIPPLE_IOU, ETHEREUM, ETHEREUM_TOKEN
assetId	string	Crypto asset ID
assetName	string	Crypto asset Name
assetDivisibility	string	Crypto asset divisibility
assetIcon	string	Crypto asset icon: location of the asset icon file
Fund engine setting object parameters
Fields	Type	Description
depositsEnabled	boolean	If true deposits are enabled
withdrawalsEnabled	boolean	If true withdrawals are enabled
displayEnabled	boolean	If true the currency is visible on the platform. If false, the user should also reflect this in their application and hide the currency.
mobileAccessEnabled	boolean	If mobile access is enabled
Currency pair object parameters
Fields	Type	Description
priceDecimals	int	Decimals place of price for trading
engineSettings	[engineSetting]	List of order engine settings. See Order engine setting object parameters
minOrderRate	decimal	Minimum order rate
maxOrderRate	decimal	Maximum order rate
displayPriceDecimals	int	Decimals place of price for display
tradedCcy	string	Traded currency
settlementCcy	string	Settlement currency
preferredMarket	string	Preferred market
Order engine setting object parameters
Fields	Type	Description
tradingEnabled	boolean	True if trading enabled
displayEnabled	boolean	True if the currency is visible on the platform web frontend.
cancelOnly	boolean	True if cancel only
verifyRequired	boolean	True if verification required for trading
restrictedBuy	boolean	True if user is restricted from buying the currency pair
restrictedSell	boolean	True if user is restricted from selling the currency pair
Responses

200
200


400
400




Get Currency-Pairs
get
https://trade-hk.oslsandbox.com/api/v4/instrument

Get the currency-pair information. All available currency-pairs for retail users will be returned by default. PI can also implement API key to get all currency-pairs supported for PI.

Response Body
Field

Description

symbol

Currency pair, i.e. BTCUSD

currency

Currency of the asset for the quoted market price

settlCurrency

Currency in which the price is settled in

highPrice

Highest traded price of the pair within the prior rolling 24 hour window

lowPrice

Lowest traded price of the currency pair within the prior rolling 24 hour window

bidPrice

Current bid price

askPrice

Current ask price

lastPrice

Last traded price

minPrice

Minimum price allowed to order for this currency pair

maxPrice

Maximum price allowed to order for this currency pair

minOrderQty

Minimum quantity allowed to order for this currency pair (in currency)

maxOrderQty

Maximum quantity allowed to order for this currency pair (in currency)

minValue

Minimum allowed order value (in settlement currency)
i.e. order value = order qty x price

maxValue

Maximum allowed order value (in settlement currency)
i.e. order value = order qty x price

prevClosePrice

Last price traded in the previous trading cycle

volume

The traded volume of the currency pair in the prior rolling 24 hour window

tickSize

The minimum price movement of the currency pair.

stepSize

The minimum quantity movement of the currency pair.

priceDecimals

The number of decimal places used to display the price.

quantityDecimals

The number of decimal places used to display the quantity.

updateTime

The last trade time

Query Params
symbol
string
Defaults to BTCUSD
Currency-pair. If empty, all currency-pairs are returned.

BTCUSD
Responses

200
200


400
400


403
403


404
404


500
500

