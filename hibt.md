Spot Trading
API for spot trading by regular users

Preparation for Access
Trading Pairs
A trading pair consists of a base currency and a quote currency. For example, in the trading pair BTC/USDT, BTC is the base currency and USDT is the quote currency.

Applying for an API Key
To apply for an API Key, access the Hibt app on your mobile device, go to the personal settings page, and find the API management section. After successful creation, be sure to note the following information:

Access Key: The API access key

Secret Key: The key used for signature authentication and encryption (only visible during application)

API Authentication
Public APIs are used for retrieving basic information and market data. Public APIs do not require authentication to be called.

Private APIs are used for trading and account management. Each private request must be signed using your API Secret Key for verification.

REST API
https://api.hibt0.com/user-open-api

Signature Authentication
Private interfaces, except for public ones (such as basic information and market data), must use your API Key for encryption to verify whether the parameters or parameter values have been altered during transmission. Each API Key needs to have the appropriate permissions to access the corresponding interfaces. Every newly created API Key must be assigned permissions. Before using an interface, make sure your API Key has the required permissions.

The contents required for a valid request are as follows:

Method request URL: For example, https://api.hibt0.com/open-api/v1/trade/order.

API access key (X-ACCESS-KEY): The Access Key from the API Key you applied for.

Request timestamp (X-TIMESTAMP): The millisecond timestamp at the time of the request, used during the signature process.

Required and optional parameters: Each method has a set of required and optional parameters that define the API call. You can view these parameters and their meanings in the description of each method.

Signature: The value calculated via encryption to ensure the signature is valid and has not been tampered with. For the security of your API Key, the signature for parameters expires 5 minutes after generation.

Signature Required Parameter: For interfaces requiring signature authentication, the reqTime parameter must be included (its value is the latest server time, which can be obtained via the **/v1/common/systemTime** interface).

Encryption Method
To calculate the signature, the request must be normalized first, because when using HMAC for signature calculation, the result will be completely different for different contents. Therefore, before performing the signature calculation, please normalize the request. The following is an example of a request to query the details of an order:

Order request URL:


Copy
https://api.hibt0.com/user-open-api/v1/trade/order?amount=0.12&direction=ASK&price=7126.4285&symbol=BTC/USDT&reqTime=1672502400000
Sort the parameters in ASCII order and include the request timestamp timestamp:


Copy
amount=0.12&direction=ASK&price=7126.4285&reqTime=1672502400000&symbol=BTC/USDT&timestamp=1672502400000
Use the secretKey to encrypt the sorted request parameters using HMAC SHA256, resulting in:


Copy
550ac73ace8c34372e0e1dd6631e890c7bd16697af8bb4e2908e966b50aba4e0
Constructing HTTP Requests

Use X-ACCESS-KEY to store the access key information and pass it in the header as a parameter.

Use X-SIGNATURE to store the generated signature and pass it in the header as a parameter.

Use X-TIMESTAMP to store the request timestamp and pass it in the header as a parameter.

Request Methods

Currently, there are only two methods: GET and POST.

GET requests: All parameters are included in the path parameters.

POST requests: All parameters are sent in the request body in form-data format.

Response Format

All APIs return data in JSON format. At the top level of the JSON response, there are three fields: message, code, and data. The first two fields represent the request status and information, while the actual business data is contained in the data field.


Copy
{
  "message": "success",
  "code": "0",
  "data": ""
}
Common Error Codes
1xxx (Access Failure)
2xxx (Business Failure)
Error Code
Description
0

Success

1001

API request rate limit exceeded

1101

API Key authentication failed

1102

Secret key decryption failed

1103

Access IP not in the whitelist

2001

Parameter is empty

2002

Time range error

2003

Request time parameter is empty

2004

Request time expired

2101

Account does not exist

2102

API Key does not exist

2103

Trading pair does not exist

2201

User API Key disabled

2202

IP disabled

2203

API expired

2204

Insufficient API permissions

9999

Other exceptions, refer to message

Spot API
Basic Information API
Server Time

HTTP Request

GET /v1/common/systemTime

Authentication: No

Rate Limit: 100 requests/second

Request Parameters

This endpoint does not accept any parameters.

Response Fields

Field Name
Data Type
Description
data

long

Server timestamp


Copy
{
  "message": "success",
  "code": "0",
  "data": 1672502400000
}
All Trading Pair Information
HTTP Request

GET /v1/common/symbols

Authentication: No

Rate Limit: 5 requests/second

Request Parameters

This endpoint does not accept any parameters.

Response Fields

Field Name
Data Type
Description
symbol

string

Trading pair

baseCoinScale

integer

Precision for the quoted currency

coinScale

integer

Precision for the base currency

priceScale

integer

Price precision

baseSymbol

string

Base currency

coinSymbol

string

Quote currency

minTurnover

decimal

Minimum order transaction amount

minVolume

decimal

Minimum order quantity

maxVolume

decimal

Maximum order quantity

enable

integer

Whether trading is supported (0-No; 1-Yes)

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "symbol": "BTC/USDT", // Trading pair
      "baseCoinScale": 4, // Precision of quote currency amount
      "coinScale": 4, // Precision of base currency amount
      "priceScale": 2, // Price precision
      "baseSymbol": "USDT", // Quote currency
      "coinSymbol": "BTC", // Base currency
      "minTurnover": 10, // Minimum order value
      "minVolume": 0.001, // Minimum order quantity
      "maxVolume": 50, // Maximum order quantity
      "enable": 1 // Whether it is enabled
    },
    {
      "symbol": "ETH/USDT",
      "baseCoinScale": 4,
      "coinScale": 4,
      "baseSymbol": "USDT",
      "coinSymbol": "ETH",
      "minTurnover": 10,
      "minVolume": 0.01,
      "maxVolume": 500,
      "enable": 1
    }
  ]
}
Latest Trade Price
This endpoint provides the latest trade price for a trading pair.

HTTP Request

GET /v1/market/ticker/price

Authentication: No

Rate Limit: 10 requests/second

Request Parameters

Parameter
Data Type
Required
Description
symbol

string

Yes

Trading pair

Response Fields

Field Name
Data Type
Description
tickerPrice

decimal

Latest trade price

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": {
    "tickerPrice": 40000
  }
}
K-Line Data
HTTP Request

POST /v1/market/kline

Authentication: No

Rate Limit: 5 requests/second

Request Parameters

Parameter
Data Type
Required
Description
symbol

string

true

Trading pair

period

string

true

Time intervals: "1min", "5min", "15min", "30min", "60min", "4hour", "1day", "1week", "1mon", "1year"

size

int

false

Number of data points to retrieve, default is 100, max is 500

from

long

true

Start time (ms)

to

long

true

End time (ms)

Response Fields

Field Name
Data Type
Description
openPrice

decimal

Opening price

highestPrice

decimal

Highest price

lowestPrice

decimal

Lowest price

closePrice

decimal

Closing price

time

long

K-line timestamp (ms)

volume

decimal

Trading volume

turnover

decimal

Trading turnover

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "openPrice": "123456",
      "highestPrice": "45678",
      "lowestPrice": 0.5,
      "closePrice": 0.1,
      "volume": 0.1,
      "time": 1672502400000,
      "turnover": 1.2
    }
  ]
}
Order Book Depth Data
This endpoint returns the current order book depth data for a specified trading pair.

HTTP Request

GET /v1/market/depth

Authentication: No

Rate Limit: 10 requests/second

Request Parameters

Parameter
Data Type
Required
Description
Value Range
symbol

string

Yes

Trading pair

depth

integer

Yes

Number of depth levels to return

Maximum 50 levels

Response Fields

Field Name
Data Type
Description
symbol

string

Trading pair

bids

array

Buy order book depth list

asks

array

Sell order book depth list

timestamp

datetime

Time

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": {
      "symbol" : "BTC/USDT",
      "timestamp" : "1723199363658",
      "bids" : [ [ "36074.99", "0.27225537" ], [ "36074.81", "0.00967628" ] ],
      "asks" : [ [ "36075.06", "0.55858424" ], [ "36075.24", "0.22475193" ] ]
  }
}
Account Balance
This endpoint returns the balance information for a specified currency.

HTTP Request

POST /v1/account/balance

Authentication: Yes

Rate Limit: 5 requests/second

Request Parameters

Parameter
Data Type
Required
Description
coin

string

No

Currency

Response Fields

Field Name
Data Type
Description
coin

string

Currency

balance

decimal

Available balance

frozenBalance

decimal

Frozen balance

isLock

string

Whether locked

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "coin": "USDT",
      "balance": 1000,
      "frozenBalance": 1000,
      "isLock": "IS_FALSE"
    },{
      "coin": BTC,
      "balance": 1,
      "frozenBalance": 0.01,
      "isLock": "IS_TRUE"
    }
  ]
}
Bill List
This endpoint returns the bill list data for a specified currency.

HTTP Request

POST /v1/account/bill

Authentication: Yes

Rate Limit: 5 requests/second

Request Parameters

Parameter
Data Type
Required
Description
coin

string

Yes

Currency

startTime

long

Yes

Start time (ms)

endTime

long

Yes

End time (ms)

Response Fields

Field Name
Data Type
Description
uid

long

User UID

firstLevelBillType

string

Primary bill type, e.g., 2 for trades

secondLevelBillType

string

Secondary bill type name, e.g., 1 for deposit, 4 for spot buy, 5 for spot sell

tradeType

int

Trade type; e.g., 1 for spot trading

amount

decimal

Amount

coinUnit

string

Currency

createTime

long

Creation time (ms)

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "uid": "123456",
      "firstLevelBillType": 2,
      "secondLevelBillType: 4,
      "tradeType: 1,
      "amount: 15.00,
      "coinUnit": "USDT",
      "createTime": 1672502400000
    }
  ]
}
Current Orders
HTTP Request

POST /v1/trade/openOrder

Authentication: Yes

Rate Limit: 10 requests/second

Request Parameters

Parameter
Data Type
Required
Description
symbol

string

Yes

Trading pair

direction

integer

Yes

Order direction (0-Buy; 1-Sell)

Response Fields

Field Name
Data Type
Description
orderId

string

Order ID

price

decimal

Order price

avgPrice

decimal

Average trade price

amount

decimal

Order quantity

tradedAmount

decimal

Quantity traded

turnover

decimal

Trade amount (traded quantity * trade price)

symbol

string

Trading pair

baseSymbol

string

Quote currency

coinSymbol

string

Base currency

direction

integer

Direction (0-Buy; 1-Sell)

status

integer

Status (0-Pending; 1-Completed; 2-Canceled; 3-Expired; 4-Partially Filled)

type

integer

Type (0-Market; 1-Limit)

completedTime

long

Order completion time

canceledTime

long

Order cancellation time

time

long

Order creation time

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "orderId": "E1677194831589408768",
      "clOrdId": "1677AAA",
      "price": 35000,
      "avgPrice": 0,
      "amount": 0.1,
      "tradedAmount": 0,
      "turnover": 0,
      "symbol": "BTC/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "BTC",
      "direction": 0,
      "status": 0,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    },{
      "orderId": "E1677269378757951488",
      "clOrdId": "1677AAA",
      "price": 2000,
      "avgPrice": 0,
      "amount": 1,
      "tradedAmount": 0,
      "turnover": 0,
      "symbol": "ETH/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "ETH",
      "direction": 1,
      "status": 0,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    }
  ]
}
Historical Orders (Within 3 Months)
HTTP Request

POST /v1/trade/history

Authentication: Yes

Rate Limit: 10 requests/second

Request Parameters

Parameter
Data Type
Required
Description
symbol

string

Yes

Trading pair

startTime

long

Yes

Start time (ms)

endTime

long

Yes

End time (ms)

Response Fields

Field Name
Data Type
Description
orderId

string

Order ID

price

decimal

Order price

avgPrice

decimal

Average trade price

amount

decimal

Order quantity

tradedAmount

decimal

Quantity traded

turnover

decimal

Trade amount (traded quantity * trade price)

symbol

string

Trading pair

baseSymbol

string

Quote currency

coinSymbol

string

Base currency

direction

integer

Direction (0-Buy; 1-Sell)

status

integer

Status (0-Pending; 1-Completed; 2-Canceled; 3-Expired; 4-Partially Filled)

type

integer

Type (0-Market; 1-Limit)

completedTime

long

Order completion time

canceledTime

long

Order cancellation time

time

long

Order creation time

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "orderId": "E1677226372826791936",
      "price": 35000,
      "avgPrice": 35000,
      "amount": 0.1,
      "tradedAmount": 0.1,
      "turnover": 3500,
      "symbol": "BTC/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "BTC",
      "direction": 0,
      "status": 1,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    },{
      "orderId": "E1677261905426776064",
      "price": 2000,
      "avgPrice": 2000,
      "amount": 1,
      "tradedAmount": 1,
      "turnover": 2000,
      "symbol": "ETH/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "ETH",
      "direction": 1,
      "status": 1,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    }
  ]
}
Spot Order Placement
HTTP Request

POST /v1/trade/order

Authentication: Yes

Rate Limit: 20 requests/second

Request Parameters

Parameter
Data Type
Required
Description
symbol

string

Yes

Trading pair

price

decimal

Yes

Price (set to 0 for market orders)

amount

decimal

Yes

Quantity (Market Buy: amount in quote currency, e.g., USDT; Market Sell: quantity of base currency to sell)

direction

integer

Yes

Direction (0-Buy; 1-Sell)

type

integer

Yes

Type (0-Market; 1-Limit)

Response Fields

Field Name
Data Type
Description
data

string

Order ID

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": "E1677226372826791936"
}
Cancel Order
HTTP Request

POST /v1/trade/cancel

Authentication: Yes

Rate Limit: 20 requests/second

Request Parameters

Parameter
Data Type
Required
Description
orderId

string

Yes

Order ID

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": ""
}
Rebate List
HTTP Request

POST /v1/account/rebateInfo

Authentication: Yes

Rate Limit: 5 requests/second

Request Parameters

Response Fields

Field Name
Data Type
Description
invitedUID

long

Invited user's UID

parentUID

long

Inviter's (parent) UID

createTime

long

Creation time (ms)

coin

string

Rebate coin type

rebateAmount

decimal

Rebate amount

rebateUsdtAmount

decimal

Rebate amount in equivalent USDT

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "invitedUID": "123456",
      "parentUID": "45678",
      "coin": "BTC",
      "rebateAmount": 0.1,
      "rebateUsdtAmount": 0.1,
      "createTime": 1672502400000
    }
  ]
}
User Information
HTTP Request

POST /v1/account/uInfo

Authentication: Yes

Rate Limit: 5 requests/second

Request Parameters

Response Fields

Field Name
Data Type
Description
uid

long

User UID

email

string

Email address

mobile

string

Mobile number

parentUid

long

Inviter's UID

Response Example


Copy
{
  "message": "success",
  "code": "0",
  "data": 
    {
      "uid": "123456",
      "email": "45678@qq.com",
      "mobile": 13800138000,
      "parentUid": 45678
    }
}






Spot Trading (Market Maker)
Market Maker User's Spot Trading API

API Introduction
Access preparation
Trading pairs
A trading pair consists of a base currency and a quote currency. Taking the trading pair BTC/USDT as an example, BTC is the base currency, and USDT is the quote currency.

Apply for API Key
After successful creation, please be sure to remember the following information:

Access Key API Access Key

Secret Key Key used for signature authentication encryption (visible only during application)

Interface Authentication 

Public interfaces can be used to obtain basic information and market data. Public interfaces can be called without authentication. 

Private interfaces can be used for trade management and account management. Each private request must be signed and verified using your API Key.

Access URLs
REST API

https://api.hibt0.com/open-api

Signature Authentication
API requests are susceptible to tampering during transmission over the internet. To ensure that the request has not been altered, private interfaces, excluding public interfaces (basic information, market data), must use your API Key for encryption to verify whether parameters or parameter values have changed during transmission. Each API Key needs appropriate permissions to access the corresponding interfaces, and each newly created API Key requires assignment of permissions. Before using an interface, please check the permission type for each interface and confirm that your API Key has the necessary permissions.

What is required for a legitimate request:

Method request address:  That is, the access server address https://api.hibt0.co/open-api。

API Access Key (X-ACCESS-KEY) : The Access Key in the API Key you applied for.

Required and Optional Parameters: Each method has a set of required and optional parameters for defining API calls. You can review these parameters and their meanings in the documentation for each method.

Signature: The value calculated by encryption, used to ensure that the signature is valid and has not been tampered with,  For the security of your API Key, a parameter signature will expire after 5 minutes.

Signature Required Parameters ** : For interfaces that require signature authentication, the reqTime parameter must be added (the value passed is the latest server time, which can be obtained through the/v1/common/systemTime interface).

Encryption
Standardize the Request for Signature Calculation: Because using HMAC for signature calculation results in completely different outcomes for different content, it's essential to standardize the request before performing signature calculation. The following example illustrates the process using a request to query details for a specific order:

Order Request URL


Copy
https://api.hibt0.com/open-api/v1/trade/order?amount=0.12&direction=ASK&price=7126.4285&symbol=BTC_USDT&reqTime=1672502400000
Sort parameters in ASCII order:


Copy
amount=0.12&direction=ASK&price=7126.4285&reqTime=1672502400000&symbol=BTC_USDT
The result obtained by encrypting the sorted request parameters with HMAC SHA256 using secretKey:


Copy
550ac73ace8c34372e0e1dd6631e890c7bd16697af8bb4e2908e966b50aba4e0
Build HTTP request usage
Using X-ACCESS-KEY stores access key information and passes parameters in the header

Using X-Signature stores the generated signature information and passes parameters in the header

Request method
There are currently only two methods available: GET and POST

GET request: All parameters are in the path parameters

POST request: All parameters are sent in form data format in the request body

Response Format
All interfaces are in JSON format. At the top layer of JSON, there are three fields: message, code, and data. The first two fields represent the request status and information, and the actual business data is in the data field.


Copy
{
  "message": "success",
  "code": "0",
  "data": ""
}
Common failure codes
1xxx (access failure class)
2xxx (business failure category)
Failure code
describe
0

 sccuess

1001

Interface request flow limiting

1101

API Key authentication failed

1102

Decryption of the key failed

1103

Access IP is not in the whitelist

2001

The parameter is empty

2002

Time range error

2003

The request time parameter is empty

2004

The request time has expired

2101

Account does not exist

2102

API key does not exist

2103

Trading pair does not exist

2201

User API Key disabled

2202

IP is disabled

9999

Other exception, please refer to the content of the message for details

Spot Interface
Basic Information Interface
Server Time
HTTP Request

GET /v1/common/systemTime

Authentication: No

Rate Limit: 100 requests per second

Request Parameters

This interface does not accept any parameters.

Response Fields

Field Name
Data Type
Description
data

long

Server timestamp


Copy
{
  "message": "success",
  "code": "0",
  "data": 1672502400000
}
All Trading Pair Information
HTTP Request

GET /v1/common/symbols

Authentication: No

Rate Limit: 5 requests per second

Request Parameters

This interface does not accept any parameters.

Response Fields

Field Name
Data Type
Description
symbol

string

Trading Pair

baseCoinScale

integer

Quote Currency Quantity Precision

coinScale

integer

Base Currency Quantity Precision

priceScale

integer

Price Precision

baseSymbol

string

Quote Currency

coinSymbol

string

Base Currency

minTurnover

decimal

Min Order Execution Amount

minVolume

decimal

Min Order Quantity

maxVolume

decimal

Max Order Quantity

enable

integer

Is Trading Supported (0-No; 1-Yes)"


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "symbol": "BTC/USDT", // Trading Pair
      "baseCoinScale": 4, // Quote Currency Quantity Precision
      "coinScale": 4, // Base Currency Quantity Precision
      "priceScale": 2, // Price Precision
      "baseSymbol": "USDT", // Quote Currency
      "coinSymbol":"BTC", // Base Currency
      "minTurnover": 10, // Minimum Order Execution Amount
      "minVolume": 0.001, // Min Order Quantity
      "maxVolume": 50, // Max Order Quantity
      "enable":  1 // Is Trading Supported
    },
    {
      "symbol": "ETH/USDT",
      "baseCoinScale": 4,
      "coinScale": 4,
      "baseSymbol": "USDT",
      "coinSymbol":"ETH",
      "minTurnover": 10,
      "minVolume": 0.01,
      "maxVolume": 500,
      "enable": 1
    }
  ]
}
Market Data Interface
Last Trade Price
    This interface provides the current latest transaction price for the trading pair.

HTTP Request

GET /v1/market/ticker/price

Authentication: No

Rate Limit: 10 requests per second

Request Parameters

Field Name
Data Type
Is required
Description
symbol

string

true

Trading Pair

Response Fields

Field Name
Data Type
Description
tickerPrice

decimal

Last Trade Price


Copy
{
  "message": "success",
  "code": "0",
  "data": {
      "tickerPrice": 40000
    }
}
Order Book Data
    This interface returns the current depth data for the specified trading pair.

HTTP Request

GET /v1/market/depth

Authentication: No

Rate Limit: 10 requests per second

Request Parameters

Field Name
Data Type
Is required
Description
取值范围
symbol

string

true

Trading Pair

depth

integer

true

Number of Depth Levels Returned

最大 50 档

Response Fields

Field Name
Data Type
Description
symbol

string

Trading Pair

bids

array

Bid Depth List

asks

array

Ask Depth List

timestamp

datetime

Time


Copy
{
  "message": "success",
  "code": "0",
  "data": {
      "symbol" : "BTC/USDT",
      "timestamp" : "2023-11-22 10:00:00",
      "bids" : [ [ "36074.99", "0.27225537" ], [ "36074.81", "0.00967628" ] ],
      "asks" : [ [ "36075.06", "0.55858424" ], [ "36075.24", "0.22475193" ] ]
  }
}
Historical KLines

This endpoint returns the historical candlestick (K-line) data for a specified trading pair.

HTTP Request

GET /v1/market/kline

Authentication: No

Rate Limit: 2 requests per second

Request Parameters

Field Name
Data Type
Is required
Description
Data Range
symbol

string

true

symbol

period

string

true

period

Min:1min;5min;15min;30minxHour:1hour;4hour 天:1day Week:1week Month:1month

from

long

true

start time

Milliseconds

to

long 

false

end time

Milliseconds. If not provided, the current time is used.

limit

integer

false

Number of returned records

If not provided, the default is 500; the maximum is 1000.

Response Fields


Copy
{
  "data": [
    [
      "1765555200000", // Open time
      "89926.2",       // Open price
      "90050.0",       // High price
      "89785.5",       // Low price
      "89959.9",       // Close price
      "30.8345",       // Volume
      "2773034.7896",  // Quote asset volume
      "2209"           // Number of trades
    ],
    [
      "1765555260000",
      "89960",
      "90031.5",
      "89863.9",
      "89911.9",
      "19.8816",
      "1788283.7845",
      "1808"
    ]
  ],
  "code": 0,
  "message": "SUCCESS",
  "success": true
}
Historical Trades
This endpoint returns the trade history of a specified trading pair (queried in reverse chronological order).

HTTP Request

GET /v1/market/historicalTrades

Authentication: No

Rate Limit: 2 requests per second

Request Parameters

Field Name
数据类型
是否必须
描述
说明
symbol

string

true

交易对

beforeId

string

false

查询开始id

查询该id之前的交易记录，不传按最新成交id向前查询

limit

integer

false

返回条数

不填默认100，最大100

Response Fields


Copy
{
  "data": [
    {
      "id": "693d3d73453ac877d3233e55", // Trade ID
      "price": "90487.8",              // Trade price
      "qty": "0.0024",                 // Trade quantity
      "quoteQty": "217.170912",        // Quote asset volume
      "time": 1765621107203,           // Trade time
      "side": "SELL"                   // Trade side: BUY or SELL
    },
    {
      "id": "693d3d72453ac877d3233e14",
      "price": "90487.8",
      "qty": "0.0026976",
      "quoteQty": "244.10013216",
      "time": 1765621106245,
      "side": "BUY"
    }
  ],
  "code": 0,
  "message": "SUCCESS",
  "success": true
}
Account Interface
Account Balance
HTTP Request

POST /v1/account/balance

Authentication: Yes

Rate Limit: 5 requests per second

Request Parameters

Field Name
Data Type
Is required
Description
coin

string

false

Currency

Response Fields

Field Name
Data Type
Description
coin

string

Currency

balance

decimal

Balance

frozenBalance

decimal

Frozen Balance

isLock

string

Lock Status


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "coin": "USDT",
      "balance": 1000,
      "frozenBalance": 1000,
      "isLock": "IS_FALSE"
    },{
      "coin": BTC,
      "balance": 1,
      "frozenBalance": 0.01,
      "isLock": "IS_TRUE"
    }
  ]
}
Trading Interface
Open Orders
HTTP Request

POST /v1/trade/openOrder

Authentication: Yes

Rate Limit: 10 requests per second

Request Parameters

Field Name
Data Type
Is required
Description
symbol

string

true

Trading Pair

direction

integer

true

Direction (0-Buy; 1-Sell)

Response Fields

Field Name
Data Type
Description
orderId

string

Order ID

clOrdId

string

Customer Custom Order ID

price

decimal

Order Price

avgPrice

decimal

Average Transaction Price

amount

decimal

Order Amount

tradedAmount

decimal

Filled Quantity

turnover

decimal

Transaction Amount (Filled Quantity * Transaction Price)

symbol

string

Trading Pair

baseSymbol

string

Quote Currency

coinSymbol

string

Base Currency

direction

integer

Direction (0-Buy; 1-Sell)

status

integer

Status (0-In Progress; 1-Completed; 2-Canceled; 3-Timeout; 4-Partially Filled)

type

integer

Type (0-Market Order; 1-Limit Order)

completedTime

long

Order Completion Time

canceledTime

long

Order Cancel Time

time

long

Order Create Time


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "orderId": "E1677194831589408768",
      "clOrdId": "1677AAA",
      "price": 35000,
      "avgPrice": 0,
      "amount": 0.1,
      "tradedAmount": 0,
      "turnover": 0,
      "symbol": "BTC/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "BTC",
      "direction": 0,
      "status": 0,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    },{
      "orderId": "E1677269378757951488",
      "clOrdId": "1677AAA",
      "price": 2000,
      "avgPrice": 0,
      "amount": 1,
      "tradedAmount": 0,
      "turnover": 0,
      "symbol": "ETH/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "ETH",
      "direction": 1,
      "status": 0,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    }
  ]
}
Historical Orders (Last 3 Months)
HTTP Request

POST /v1/trade/history

Authentication: Yes

Rate Limit: 10 requests per second

Request Parameters

Field Name
Data Type
Is required
Description
symbol

string

true

Trading Pair

startTime

long

true

Start Time (milliseconds)

endTime

long

true

End Time (milliseconds)

Response Fields

Field Name
Data Type
Description
orderId

string

Order ID

clOrdId

string

Customer Custom Order ID

price

decimal

Order Price

avgPrice

decimal

Average Transaction Price

amount

decimal

Order Amount

tradedAmount

decimal

Filled Quantity

turnover

decimal

Transaction Amount (Filled Quantity * Transaction Price)

symbol

string

Trading Pair

baseSymbol

string

Quote Currency

coinSymbol

string

Base Currency

direction

integer

Direction (0-Buy; 1-Sell)

status

integer

Status (0-In Progress; 1-Completed; 2-Canceled; 3-Timeout; 4-Partially Filled)

type

integer

Type (0-Market Order; 1-Limit Order)

completedTime

long

Order Completion Time

canceledTime

long

Order Cancel Time

time

long

Order Create Time


Copy
{
  "message": "success",
  "code": "0",
  "data": [
    {
      "orderId": "E1677226372826791936",
      "clOrdId": "1677AAA",
      "price": 35000,
      "avgPrice": 35000,
      "amount": 0.1,
      "tradedAmount": 0.1,
      "turnover": 3500,
      "symbol": "BTC/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "BTC",
      "direction": 0,
      "status": 1,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    },{
      "orderId": "E1677261905426776064",
      "clOrdId": "1677AAA",
      "price": 2000,
      "avgPrice": 2000,
      "amount": 1,
      "tradedAmount": 1,
      "turnover": 2000,
      "symbol": "ETH/USDT",
      "baseSymbol": "USDT",
      "coinSymbol": "ETH",
      "direction": 1,
      "status": 1,
      "type": 1,
      "completedTime": 1672502400000,
      "canceledTime": 1672502400000,
      "time": 1672502400000
    }
  ]
}
Create Order
HTTP Request

POST /v1/trade/order

Authentication: Yes

Rate Limit: 20 requests per second

Request Parameters

Field Name
Data Type
Is required
Description
symbol

string

true

Trading Pair

price

decimal

true

Price (Set to 0 for Market Order)

amount

decimal

true

Quantity (For Market Buy Order: Represents the amount to buy in USDT; For Market Sell Order: Represents the quantity of base currency to sell)

direction

integer

true

Direction (0-Buy; 1-Sell)

type

integer

true

Type (0-Market Order; 1-Limit Order)

Response Fields

Field Name
Data Type
Description
data

string

Order ID


Copy
{
  "message": "success",
  "code": "0",
  "data": "E1677226372826791936"
}
Cancel Order
HTTP Request

POST /v1/trade/cancel

Authentication: Yes

Rate Limit: 20 requests per second

Request Parameters

Field Name
Data Type
Is required
Description
symbol

string

true

Trading Pair

orderId

string

true

Order ID

Response Fields


Copy
{
  "message": "success",
  "code": "0",
  "data": ""
}