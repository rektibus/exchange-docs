Change Log (2025-05-09)
2025-05-09
Deprecate the allOpenOrders interface

Deprecate the allOpenOrders interface and provide a single order cancellation interface, allowing users to implement batch order cancellations by themselves
2024-08-08
WebSocket Market Data

Added real-time candlestick charts and historical candlestick data
Recent transaction data and other related market information
This needs to be multiplied by the Contract SizeThis needs to be multiplied by the Contract Size
You can click the following link to go directly to the relevant section: WebSocket Market Data

2023-06-14
OpenApi V2.0

The MARKDOWN documentation is as follows: V2 interface please refer to the document: https://github.com/Bitrue-exchange/USDT-M-Future-open-api-docs/tree/main/v2 V1 interface please refer to the document: https://github.com/Bitrue-exchange/USDT-M-Future-open-api-docs

General Info
SDK and Code Demonstration
Disclaimer:

The following SDKs are provided by partners and users, and are not officially produced. They are only used to help users become familiar with the API endpoint. Please use it with caution and expand R&D according to your own situation.
Bitrue does not make any commitment to the safety and performance of the SDKs, nor will be liable for the risks or even losses caused by using the SDKs.
Java

To get the provided SDK for Bitrue Futures,

please visit https://github.com/Bitrue-exchange/Bitrue-future-SDK
or use the command below: git clone https://github.com/Bitrue-exchange/Bitrue-future-SDK.git
python

To get the provided SDK for Bitrue Futures,

please visit https://github.com/Bitrue-exchange/Bitrue-future-SDK
or use the command below: git clone https://github.com/Bitrue-exchange/Bitrue-future-SDK.git
General API Information
Some endpoints will require an API Key. Please refer to this page
The base endpoint is: https://fapi.bitrue.com
All endpoints return either a JSON object or array.
Data is returned in ascending order. Oldest first, newest last.
All time and timestamp related fields are in milliseconds.
All data types adopt definition in JAVA.
HTTP Error Codes
HTTP 4XX return codes are used for malformed requests; the issue is on the sender's side.
HTTP 429 return code is used when breaking a request rate limit.
HTTP 418 return code is used when an IP has been auto-banned for continuing to send requests after receiving 429 codes.
HTTP 5XX return codes are used for internal errors
HTTP 504 return code is used when the API successfully sent the message but not get a response within the timeout period. It is important to NOT treat this as a failure operation; the execution status is UNKNOWN and could have been a success.
All endpoints can possibly return an ERROR, the error payload is as follows:
Error Codes and Messages
{
  "code": -1121,
  "msg": "Invalid symbol."
}
Any endpoint can return an ERROR
Specific error codes and messages defined in Error Codes.
General Information on Endpoints
All requests are based on the Https protocol, and the Content-Type in the request header information needs to be uniformly set to:'application/json'
For the interface of the GET method, the parameters must be sent in the query string
The interface of the POST method, the parameters must be sent in the request body
Parameters may be sent in any order.
LIMITS
There will be a limited frequency description below each interface.
A 429 will be returned when either rate limit is violated.
Endpoint Security Type
Each endpoint has a security type that determines the how you will interact with it.
API-keys are passed into the Rest API via the X-CH-APIKEY header.
API-keys and secret-keys are case sensitive.
Security Type	Description
NONE	Endpoint can be accessed freely.
TRADE	Endpoint requires sending a valid API-Key and signature.
USER_DATA	Endpoint requires sending a valid API-Key and signature.
USER_STREAM	Endpoint requires sending a valid API-Key.
MARKET_DATA	Endpoint requires sending a valid API-Key.
SIGNED (TRADE and USER_DATA) Endpoint Security
When calling the TRADE or USER_DATA interface, the signature parameter should be passed in the X-CH-SIGN field in the HTTP header.
The signature uses the HMAC SHA256 algorithm. The API-Secret corresponding to the API-KEY is used as the HMAC SHA256 key.
The request header of X-CH-SIGN is based on timestamp + method + requestPath + body string (+ means string connection) as the operation object
The value of timestamp is the same as the X-CH-TS request header, method is the request method, and the letters are all uppercase: GET/POST
requestPath is the request interface path For example: /sapi/v1/order
body is the string of the request body (post only)
The signature is not case sensitive
Timing Security
The signature interface needs to pass the timestamp in the X-CH-TS field in the HTTP header, and its value should be the unix timestamp of the request sending time e.g. 1528394129373
An additional parameter, recvWindow, may be sent to specify the number of milliseconds after timestamp the request is valid for. If recvWindow is not sent, it defaults to 5000.
In addition, if the server calculates that the client's timestamp is more than one second ‘in the future’ of the server’s time, it will also reject the request.
The logic is as follows:
if (timestamp < (serverTime + 1000) && (serverTime - timestamp) <= recvWindow) {
  // process request
} else {
  // reject request
}
Serious trading is about timing. Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With recvWindow, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.

It recommended to use a small recvWindow of 5000 or less!

SIGNED Endpoint Examples for POST /fapi/v1/order - HMAC Keys
Signature example body:

{"symbol":"BTCUSDT","price":"9300","volume":"1","side":"BUY","type":"LIMIT"}
HMAC SHA256 Signature:

[linux]$ echo -n "1588591856950POST/sapi/v1/order/test{\"symbol\":\"BTCUSDT\",\"price\":\"9300\",\"volume\":\"1\",\"side\":\"BUY\",\"type\":\"LIMIT\"}" | openssl dgst -sha256 -hmac "902ae3cb34ecee2779aa4d3e1d226686"
(stdin)= c50d0a74bb9427a9a03933d0eded03af9bf50115dc5b706882a4fcf07a26b761
Curl command :

  [linux]$ curl -H "X-CH-APIKEY: c3b165fd5218cdd2c2874c65da468b1e" -H "X-CH-SIGN: c50d0a74bb9427a9a03933d0eded03af9bf50115dc5b706882a4fcf07a26b761" -H "X-CH-TS: 1588591856950" -H "Content-Type:application/json" -X POST 'http://localhost:30000/sapi/v1/order/test' -d '{"symbol":"BTCUSDT","price":"9300","quantity":"1","side":"BUY","type":"LIMIT"}'
Key	Value
apiKey	vmPUZE6mv9SD5V5e14y7Ju91duEh8A
secretKey	902ae3cb34ecee2779aa4d3e1d226686
Parameter	Value
symbol	BTCUSDT
side	BUY
type	LIMIT
volume	1
price	9300
Market Data Endpoints
Test Connectivity
curl -X GET -i /fapi/v1/ping
The above command returns JSON structured like this:

{}
URL: /fapi/v1/ping

Type: GET

Content-Type: application/json

Description: Test Connectivity PING

Check Server Time
curl -X GET -i /fapi/v1/time
The above command returns JSON structured like this:

{}
URL: /fapi/v1/time

Type: GET

Content-Type: application/json

Description: Check Server Time

Response-fields:

Field	Type	Description
any object	object	any object.
Current open contract
curl -X GET -i /fapi/v1/contracts
The above command returns JSON structured like this:

[
  {
    "symbol": "H-HT-USDT",
    "pricePrecision": 8,
    "side": 1,
    "maxMarketVolume": 100000,
    "multiplier": 6,
    "minOrderVolume": 1,
    "maxMarketMoney": 10000000,
    "type": "H",
    "maxLimitVolume": 1000000,
    "maxValidOrder": 20,
    "multiplierCoin": "HT",
    "minOrderMoney": 0.001,
    "maxLimitMoney": 1000000,
    "status": 1
  }
]
URL: /fapi/v1/contracts

Type: GET

Content-Type: application/json

Description: Current open contract

Response-fields:

Field	Type	Description
symbol	string	Contract name
status	number	status (0:cannot trade, 1:can trade)
type	string	contract type, E: perpetual contract, S: test contract, others are mixed contract
side	number	Contract direction(backwards：0，1：forward)
multiplier	number	Contract face value
multiplierCoin	string	Contract face value unit
pricePrecision	number	Precision of the price
minOrderVolume	number	Minimum order volume
minOrderMoney	number	Minimum order value
maxMarketVolume	number	Market price order maximum volume
maxMarketMoney	number	Market price order maximum value
maxLimitVolume	number	Limit price order maximum volume
maxValidOrder	number	Maximum valid order quantity
Order Book
curl -X GET -i /fapi/v1/depth
The above command returns JSON structured like this:

{
  "bids": [
    [
      "3.90000000",
      // price
      "431.00000000"
      // quantity
    ],
    [
      "4.00000000",
      "431.00000000"
    ]
  ],
  "asks": [
    [
      "4.00000200",
      // price
      "12.00000000"
      // quantity
    ],
    [
      "5.10000000",
      "28.00000000"
    ]
  ]
}
URL: /fapi/v1/depth

Type: GET

Content-Type: application/json

Description: Order Book

Query-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract Name E.g. E-BTC-USDT
limit	string	integer	Default 100, Max 100
Response-fields:

name	type	example	description
time	long	1595563624731	Current Timestamp (ms)
bids	list	Look below	Order book purchase info
asks	list	Look below	Order book selling info
The fields bids and asks are lists of order book price level entries, sorted from best to worst.

name	type	example	description
' '	float	131.1	price level
' '	float	2.3	Total order quantity for this price level
ticker
curl -X GET -i /fapi/v1/ticker
The above command returns JSON structured like this:

{
  "high": "9279.0301",
  "vol": "1302",
  "last": "9200",
  "low": "9279.0301",
  "rose": "0",
  "time": 1595563624731
}
24 hour price change statistics:

{
  "high": "9279.0301",
  "vol": "1302",
  "last": "9200",
  "low": "9279.0301",
  "rose": "0",
  "time": 1595563624731
}
URL: /fapi/v1/ticker

Type: GET

Content-Type: application/json

Description: ticker

Parameter	Type	Required	Description
contractName	string	true	Contract Name E.g. E-BTC-USDT
Response-fields:

Field	Type	Description
time	long	Open time
high	float	Higher price
low	float	Lower price
last	float	Newest price
vol	float	Trade volume
rose	string	Price variation
Kline/Candlestick Data
curl -X GET -i /fapi/v1/klines
The above command returns JSON structured like this:

[
  {
    "high": "6228.77",
    "vol": "111",
    "low": "6228.77",
    "idx": 1594640340,
    "close": "6228.77",
    "open": "6228.77"
  },
  {
    "high": "6228.77",
    "vol": "222",
    "low": "6228.77",
    "idx": 1587632160,
    "close": "6228.77",
    "open": "6228.77"
  },
  {
    "high": "6228.77",
    "vol": "333",
    "low": "6228.77",
    "idx": 1587632100,
    "close": "6228.77",
    "open": "6228.77"
  }
]
URL: /fapi/v1/klines

Type: GET

Content-Type: application/json

Description: Kline/Candlestick Data

Parameter	Type	Required	Description
contractName	string	true	Contract Name E.g. E-BTC-USDT
interval	string	true	identifies the sent value as: 1min,5min,15min,30min,60min,2h,4h,1day,1week,1month
limit	integer	false	Default 100, Max 300
Response-fields:

Field	Type	Description
idx	long	Start timestamp(ms)
high	float	Higher price
low	float	Lower price
close	float	close price
vol	float	Trade volume
order
Account Trade List (USER_DATA)(HMAC SHA256)
curl -X GET -i /fapi/v2/myTrades?contractName=E-SAND-USDT&fromId=&limit=10&startTime=&endTime=
The above command returns JSON structured like this:

{
    "code":"0",
    "msg":"Success",
    "data":[
        {
            "tradeId":12,
            "price":0.9,
            "qty":1,
            "amount":9,
            "contractName":"E-SAND-USDT",
            "side":"BUY",
            "fee":"0.0018",
            "bidId":1558124009467904992,
            "askId":1558124043827644908,
            "bidUserId":10294,
            "askUserId":10467,
            "isBuyer":true,
            "isMaker":true,
            "ctime":1678426306000
        }
    ]
}
URL: /fapi/v2/myTrades

Type: GET

Content-Type: application/json

Description: Account Trade List (USER_DATA)(HMAC SHA256)

Query-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract name E.g. E-BTC-USDT
fromId	long	false	Trade id to fetch from. Default gets most recent trades.
limit	int	false	Default 100; max 1000.
startTime	long	false	start time
endTime	long	false	end time
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	array	return data
└─tradeId	long	trade id
└─price	bigdecimal	Order price
└─qty	int	Order quantity
└─amount	bigdecimal	Order amount
└─contractName	string	contract name
└─cTime	long	create time
└─side	string	Order direction. Possible values can only be：BUY（buy long）and SELL（sell short）
└─fee	string	Trading fees
└─bidId	long	bid id
└─askId	long	ask id
└─bidUserId	int	bid User Id
└─askUserId	int	ask User Id
└─isBuyer	boolean	is buy
└─isMaker	boolean	is maker
Modify Isolated Position Margin (TRADE)(HMAC SHA256)
curl -X POST -H 'Content-Type: application/json' -i /fapi/v2/positionMargin --data '{
  'contractName': 'E-SAND-USDT',
  'positionMargin': 10
}'
The above command returns JSON structured like this:

{
    "code": 0,
    "msg": "success"
    "data": null
}
URL: /fapi/v2/positionMargin

Type: POST

Content-Type: application/json

Description: Modify Isolated Position Margin (TRADE)(HMAC SHA256)

Body-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract name E.g. E-BTC-USDT
amount	bigdecimal	true	amount
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	object	return data
Change Initial Leverage (TRADE)(HMAC SHA256)
curl -X POST -H 'Content-Type: application/json' -i /fapi/v2/level_edit --data '{
  'contractName': 'E-BTC-USDT',
  'leverage': 10
}'
The above command returns JSON structured like this:

{
    "code": 0,
    "msg": "success",
    "data": null
}
URL: /fapi/v2/level_edit

Type: POST

Content-Type: application/json

Description: Change Initial Leverage (TRADE)(HMAC SHA256)

Body-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract name E.g. E-BTC-USDT
leverage	int	true	target initial leverage: int from 1 to 125
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	object	return data
Current All Open Orders (USER_DATA)(HMAC SHA256)
curl -X GET -i /fapi/v2/openOrders?contractName=E-SAND-USDT
The above command returns JSON structured like this:

{
  "code": "0",
  "msg": "Success",
  "data": [{
    "orderId": 1917641,
    "clientOrderId": "2488514315",
    "price": 100,
    "origQty": 10,
    "origAmount": 10,
    "executedQty": 1,
    "avgPrice": 12451,
    "status": "INIT",
    "type": "LIMIT",
    "side": "BUY",
    "action": "OPEN",
    "transactTime": 1686717303975,
    "triggerPrice": 100.00,
    "triggerType": 1,
    "triggerOrderType": 1,
    "conditionOrder": true,
    "childOrders": [
      {
        "orderId":1917641,
        "price":100,
        "origQty":10,
        "origAmount":10,
        "executedQty":1,
        "avgPrice":10000,
        "status":"INIT",
        "type":"LIMIT",
        "side":"BUY",
        "action":"OPEN",
        "transactTime":1686716571425,
        "clientOrderId":4949299210,
        "triggerPrice": 100.00,
        "triggerType": 1,
        "triggerOrderType": 1,
        "conditionOrder": true
      }
    ]
  }
  ]
}
URL: /fapi/v2/openOrders

Type: GET

Content-Type: application/json

Description: Current All Open Orders (USER_DATA)(HMAC SHA256)

Query-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract name E.g. E-BTC-USDT
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	array	return data
└─orderId	long	Order ID（system generated）
└─clientOrderId	string	client Order id
└─price	bigdecimal	Order price
└─origQty	bigdecimal	Order quantity
└─origAmount	bigdecimal	Order amount
└─executedQty	bigdecimal	Filled orders quantity
└─avgPrice	bigdecimal	Filled orders average price
└─status	string	Order status. Possible values are：NEW(new order，not filled)、PARTIALLY_FILLED（partially filled）、FILLED（fully filled）、CANCELLED（already cancelled）andREJECTED（order rejected）
└─type	string	Order type. Possible values can only be:LIMIT(limit price) andMARKET（market price）
└─side	string	Order direction. Possible values can only be：BUY（buy long）and SELL（sell short）
└─action	string	OPEN/CLOSE
└─transactTime	long	Order creation time
└─triggerPrice	bigdecimal	triggerPrice
└─triggerType	int	triggerType 1:stop loss 2:take profit
└─triggerOrderType	int	triggerOrderType 0:NORMAL 1:LIMIT 2:MARKET 3:POSITION
└─conditionOrder	bool	conditionOrder
└─childOrders	array	
└─└─	object	like above
Cancel Order (TRADE)(HMAC SHA256)
curl -X POST -H 'Content-Type: application/json' -i /fapi/v2/cancel --data '{
    'contractName': 'E-SAND-USDT', 
    'clientOrderId': "",  
    'orderId': 1690615847831143159, 
    'conditionOrder': true
}
The above command returns JSON structured like this:

{
  "code": "0",
  "msg": "Success",
  "data": {
    "orderId": 1690615847831143159
  }
}
URL: /fapi/v2/cancel

Type: POST

Content-Type: application/json

Description: Cancel Order (TRADE)(HMAC SHA256)

Body-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract name E.g. E-BTC-USDT
clientOrderId	string	false	client Order id(clientOrderId and orderId cannot both be empty)
orderId	long	false	order id(clientOrderId and orderId cannot both be empty)
conditionOrder	bool	false	is conditionOrder
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	object	return data
└─orderId	long	Order ID（system generated）
Query Order (USER_DATA)(HMAC SHA256)
curl -X GET -i /fapi/v2/order?contractName=E-SAND-USDT&orderId=1690615710392189353
The above command returns JSON structured like this:

{
    "code":0,
    "msg":"success",
    "data":[
        {
            "orderId":1917641, 
            "price":100,
            "origQty":10,
            "origAmount":10,
            "executedQty":1,
            "avgPrice":10000,
            "status":"INIT", 
            "type":"LIMIT",
            "side":"BUY",
            "action":"OPEN",
            "transactTime":1686716571425,
            "clientOrderId":4949299210,
            "triggerPrice": 100.00,
            "triggerType": 1,
            "triggerOrderType": 1,
            "conditionOrder": true,
            "childOrders": [
              {
                "orderId":1917641,
                "price":100,
                "origQty":10,
                "origAmount":10,
                "executedQty":1,
                "avgPrice":10000,
                "status":"INIT",
                "type":"LIMIT",
                "side":"BUY",
                "action":"OPEN",
                "transactTime":1686716571425,
                "clientOrderId":4949299210,
                "triggerPrice": 100.00,
                "triggerType": 1,
                "triggerOrderType": 1,
                "conditionOrder": true
              }
            ]          
        }
    ]
}
URL: /fapi/v2/order

Type: GET

Content-Type: application/json

Description: Query Order (USER_DATA)(HMAC SHA256)

Query-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract name E.g. E-BTC-USDT
clientOrderId	string	false	client Order id(clientOrderId and orderId cannot both be empty)
orderId	long	false	order id(clientOrderId and orderId cannot both be empty)
conditionOrder	bool	false	conditionOrder true/false
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	object	return data
└─orderId	long	Order ID（system generated）
└─clientOrderId	string	client Order id
└─price	bigdecimal	Order price
└─origQty	bigdecimal	Order quantity
└─origAmount	bigdecimal	Order amount
└─executedQty	bigdecimal	Filled orders quantity
└─avgPrice	bigdecimal	Filled orders average price
└─status	string	Order status. Possible values are：NEW(new order，not filled)、PARTIALLY_FILLED（partially filled）、FILLED（fully filled）、CANCELLED（already cancelled）andREJECTED（order rejected）
└─type	string	Order type. Possible values can only be:LIMIT(limit price) andMARKET（market price）
└─side	string	Order direction. Possible values can only be：BUY（buy long）and SELL（sell short）
└─action	string	OPEN/CLOSE
└─transactTime	long	Order creation time
└─triggerPrice	bigdecimal	triggerPrice
└─triggerType	int	triggerType 1:stop loss 2:take profit
└─triggerOrderType	int	triggerOrderType 0:NORMAL 1:LIMIT 2:MARKET 3:POSITION
└─conditionOrder	bool	conditionOrder
└─childOrders	array	
└─└─	object	like above
New Order (TRADE)(HMAC SHA256)
curl -X POST -H 'Content-Type: application/json' -i /fapi/v2/order --data '{
    'contractName': 'E-SAND-USDT', 
    'clientOrderId': 7993967859, 
    'side': 'BUY', 
    'type': 'LIMIT', 
    'positionType': 1, 
    'open': 'OPEN', 
    'volume': 100, 
    'amount': 1, 
    'price': 2, 
    'leverage': 5,
    'triggerOrderType': 0,
    'triggerType': 0,
    'triggerPriceType': 0,
    'triggerPrice': 100.00,
    'conditionOrder': true,
    'positionId': 1,
    'triggerOrderCreateParams': [{
        'clientOrderId': 1,
        'triggerType': 0,
        'triggerPriceType': 0,
        'triggerPrice': 100.00,
        'type': 'LIMIT', 
        'price': 100.00
    }]
}'
The above command returns JSON structured like this:

{
  "code": "0",
  "msg": "Success",
  "data": {
    "orderId": 1690615676032452985
  }
}
URL: /fapi/v2/order

Type: POST

Content-Type: application/json

Description: New Order (TRADE)(HMAC SHA256)

Body-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract name E.g. E-BTC-USDT
clientOrderId	string	false	Client order identity, a string with length less than 32 bit
side	string	true	trade direction, BUY/SELL
type	string	true	Order type, LIMIT,MARKET,IOC,FOK,POST_ONLY
positionType	int	true	1 crossed position, 2 isolated position
open	string	true	Open balancing direction, OPEN/CLOSE
volume	bigdecimal	true	Order quantity
amount	bigdecimal	true	Order amount
price	bigdecimal	true	Order price
leverage	bigdecimal	true	target initial leverage: int from 1 to 125
triggerOrderType	int	false	0:NORMAL 1:LIMIT 2:MARKET 3:POSITION
triggerType	int	false	1:stop loss 2:take profit
triggerPriceType	int	false	Trigger Price Type 1:Latest Transaction Prices 2:Marked price
triggerPrice	bigdecimal	false	Trigger Price
conditionOrder	bool	false	conditionOrder true/false
positionId	int	false	positionId
triggerOrderCreateParams	array	false	
└─clientOrderId	string	false	Client order identity, a string with length less than 32 bit
└─triggerType	int	true	1:stop loss 2:take profit
└─triggerPriceType	int	true	Trigger Price Type 1:Latest Transaction Prices 2:Marked price
└─triggerPrice	bigdecimal	true	Trigger Price
└─type	string	true	Order type, LIMIT,MARKET
└─price	bigdecimal	true	Order price
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	object	return data
└─orderId	long	Order ID（system generated）
user
Account Information V2 (USER_DATA)(HMAC SHA256)
curl -X GET -i /fapi/v2/account
The above command returns JSON structured like this:

{
  "code":"0",
  "msg":"Success",
  "data":{
    "account":[
      {
        "marginCoin":"USDT",
        "coinPrecious":4,
        "accountNormal":1010.4043400372839856,
        "accountLock":2.9827889600000006,
        "partPositionNormal":0,
        "totalPositionNormal":0,
        "achievedAmount":0,
        "unrealizedAmount":0,
        "totalMarginRate":0,
        "totalEquity":1010.4043400372839856,
        "partEquity":0,
        "totalCost":0,
        "sumMarginRate":0,
        "sumOpenRealizedAmount":0,
        "canUseTrialFund":0,
        "sumMaintenanceMargin":null,
        "futureModel":null,
        "positionVos":[

        ]
      },
      {
        "marginCoin":"USDT",
        "coinPrecious":8,
        "accountNormal":9999981.6304078411247375,
        "accountLock":1.4950614966,
        "partPositionNormal":0,
        "totalPositionNormal":1.5610615,
        "achievedAmount":0,
        "unrealizedAmount":0,
        "totalMarginRate":128117.7154579628016855,
        "totalEquity":9999981.6304078411247375,
        "partEquity":0,
        "totalCost":1.5610615,
        "sumMarginRate":128117.7346123843289321,
        "sumOpenRealizedAmount":-3.29999999,
        "canUseTrialFund":0,
        "sumMaintenanceMargin":null,
        "futureModel":null,
        "positionVos":[
          {
            "contractId":62,
            "contractName":"E-BTC-USDT",
            "contractSymbol":"BTC-USDT",
            "adlEnabled":false,
            "positions":[
              {
                "id":175633,
                "uid":10294,
                "contractId":62,
                "positionType":1,
                "side":"BUY",
                "volume":30,
                "openPrice":27117.691603,
                "avgPrice":26017.691606,
                "closePrice":0,
                "leverageLevel":50,
                "openAmount":0,
                "holdAmount":1.5610615,
                "closeVolume":0,
                "pendingCloseVolume":0,
                "realizedAmount":0,
                "historyRealizedAmount":-3.47655433,
                "forceLiquidationVolume":0,
                "forceLiquidationPrice":0,
                "tradeFee":-0.02450636,
                "capitalFee":-0.15204798,
                "closeProfit":0,
                "shareAmount":0,
                "freezeLock":0,
                "status":1,
                "ctime":"2023-06-06T09:48:43",
                "mtime":"2023-06-14T04:39:28",
                "brokerId":1000,
                "usingAccountType":0,
                "marginRate":0.0001,
                "reducePrice":-3350051449.6928050669137353,
                "returnRate":-2.1139461825781778,
                "unRealizedAmount":0,
                "openRealizedAmount":-3.29999999,
                "positionBalance":78.05307482,
                "settleProfit":-3.29999999,
                "keepRate":0.004,
                "maxFeeRate":0.001,
                "indexPrice":26017.691606
              }
            ]
          }
        ]
      }
    ]
  }
}
URL: /fapi/v2/account

Type: GET

Content-Type: application/json

Description: Account Information V2 (USER_DATA)(HMAC SHA256)

Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	object	return data
└─account	array	Account V2
     └─marginCoin	string	Margin coin
     └─coinPrecious	int	Currency display precision
     └─accountNormal	bigdecimal	Balance account
     └─accountLock	bigdecimal	Margin frozen account
     └─partPositionNormal	bigdecimal	Restricted position margin balance
     └─totalPositionNormal	bigdecimal	Full position initial margin
     └─achievedAmount	bigdecimal	Profit and losses occurred
     └─unrealizedAmount	bigdecimal	Unfilled profit and losses
     └─totalMarginRate	bigdecimal	Full position margin rate
     └─totalEquity	bigdecimal	Full position equity
     └─partEquity	bigdecimal	Restricted position equity
     └─totalCost	bigdecimal	Full position costs
     └─sumMarginRate	bigdecimal	All accounts margin rate
     └─sumOpenRealizedAmount	bigdecimal	Full account position profit and loss
     └─canUseTrialFund	bigdecimal	Available experience money
     └─sumMaintenanceMargin	bigdecimal	Full position maintenance margin plus handling fee
     └─futureModel	enum	Account type
     └─positionVos	array	Position contract record
          └─contractId	int	Contract id
          └─contractName	string	Contract name
          └─contractSymbol	string	Contract coin pair
          └─adlEnabled	boolean	adl
          └─positions	array	positions
               └─id	int	id
               └─uid	int	user id
               └─contractId	int	contract id
               └─positionType	int	1 crossed position, 2 isolated position
               └─side	string	trade direction, BUY/SELL
               └─volume	bigdecimal	Order quantity
               └─openPrice	bigdecimal	open price
               └─avgPrice	bigdecimal	avg price
               └─closePrice	bigdecimal	Balancing average price
               └─leverageLevel	int	Leverage multiple
               └─openAmount	bigdecimal	Opening margin (including variation)
               └─holdAmount	bigdecimal	Hold position margin
               └─closeVolume	bigdecimal	Balanced quantity
               └─pendingCloseVolume	bigdecimal	The number of pending closing orders
               └─realizedAmount	bigdecimal	Profit and losses occurred
               └─historyRealizedAmount	bigdecimal	Historic accumulated profit and losses
               └─forceLiquidationVolume	bigdecimal	Strong flat quantity
               └─forceLiquidationPrice	bigdecimal	Strong leveling price (average price, trigger price).
               └─tradeFee	bigdecimal	Trading fees
               └─capitalFee	bigdecimal	Capital costs
               └─closeProfit	bigdecimal	Balancing profit and loss
               └─shareAmount	bigdecimal	Amount to share
               └─freezeLock	int	Position freeze status: 0 normal, 1 liquidation freeze, 2 delivery freeze
               └─status	int	Position effectiveness，0 ineffective 1 effective
               └─ctime	string	Creation time
               └─mtime	string	Update time
               └─lockTime	string	liquidation lock time
               └─positionAmount	bigdecimal	Total position value (full) multiplied by face value
               └─positionCloseAmount	bigdecimal	Total closing value (full amount) multiplied by face value
               └─longAccountCount	int	Number of multiple positions
               └─shortAccountCount	int	Number of open positions
               └─sumRealized	bigdecimal	The total realized profit and loss of this settlement cycle
               └─deficitLosses	bigdecimal	Customer account deficit at position settlement
               └─currentMarginRate	bigdecimal	Current margin ratio
               └─realEquity	bigdecimal	Balance occupied by current contracts, excluding realized and unrealized gains and losses
                    └─positionId	int	Location ID, associated with the location list id, primary key
                    └─ctime	string	create time
                    └─mtime	string	update time
Notional and Leverage Brackets (USER_DATA)
curl -X GET -i /fapi/v2/leverageBracket?contractName=E-SAND-USDT
The above command returns JSON structured like this:

{
    "code":"0",
    "msg":"Success",
    "data":{
        "contractName":"E-SAND-USDT",
        "brackets":[
            {
                "bracket":1,
                "initialLeverage":100,
                "maxPositionValue":10000,
                "minPositionValue":0,
                "maintMarginRatio":0.008
            },
            {
                "bracket":2,
                "initialLeverage":75,
                "maxPositionValue":100000,
                "minPositionValue":10000,
                "maintMarginRatio":0.0085
            },
            {
                "bracket":3,
                "initialLeverage":50,
                "maxPositionValue":500000,
                "minPositionValue":100000,
                "maintMarginRatio":0.012
            },
            {
                "bracket":4,
                "initialLeverage":25,
                "maxPositionValue":1000000,
                "minPositionValue":500000,
                "maintMarginRatio":0.022
            },
            {
                "bracket":5,
                "initialLeverage":10,
                "maxPositionValue":2000000,
                "minPositionValue":1000000,
                "maintMarginRatio":0.05
            },
            {
                "bracket":6,
                "initialLeverage":5,
                "maxPositionValue":5000000,
                "minPositionValue":2000000,
                "maintMarginRatio":0.1
            },
            {
                "bracket":7,
                "initialLeverage":4,
                "maxPositionValue":10000000,
                "minPositionValue":5000000,
                "maintMarginRatio":0.125
            },
            {
                "bracket":8,
                "initialLeverage":3,
                "maxPositionValue":20000000,
                "minPositionValue":10000000,
                "maintMarginRatio":0.15
            },
            {
                "bracket":9,
                "initialLeverage":1,
                "maxPositionValue":9999999998,
                "minPositionValue":20000000,
                "maintMarginRatio":0.25
            }
        ]
    }
}
URL: /fapi/v2/leverageBracket

Type: GET

Content-Type: application/json

Description: Notional and Leverage Brackets (USER_DATA)

Query-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract name
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	object	return data
└─contractName	string	Contract name
└─brackets	array	brackets
     └─bracket	int	Notional bracket
     └─initialLeverage	bigdecimal	Max initial leverage for this bracket
     └─maxPositionValue	bigdecimal	Cap notional of this bracket
     └─minPositionValue	bigdecimal	Notional threshold of this bracket
     └─maintMarginRatio	bigdecimal	Maintenance ratio for this bracket
User Commission Rate (USER_DATA)(HMAC SHA256)
curl -X GET -i /fapi/v2/commissionRate?contractName=E-SAND-USDT
The above command returns JSON structured like this:

{
    "code":"0",
    "msg":"Success",
    "data":{
        "contractName":"E-SAND-USDT",
        "openTakerFeeRate":0.0004,
        "openMakerFeeRate":0.0002,
        "closeTakerFeeRate":0.0004,
        "closeMakerFeeRate":0.0002
    }
}
URL: /fapi/v2/commissionRate

Type: GET

Content-Type: application/json

Description: User Commission Rate (USER_DATA)(HMAC SHA256)

Query-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract name
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	object	return data
└─contractName	string	contract name
└─openTakerFeeRate	bigdecimal	open taker fee rate
└─openMakerFeeRate	bigdecimal	open maker fee rate
└─closeTakerFeeRate	bigdecimal	close taker fee rate
└─closeMakerFeeRate	bigdecimal	close maker fee rate
New Future Account Transfer (USER_DATA)(HMAC SHA256)
curl -X POST -H 'Content-Type: application/json' -i /fapi/v2/futures_transfer --data '{
    'coinSymbol': 'USDT',
    'amount': 10,
    'transferType': 'wallet_to_contract'
}'
The above command returns JSON structured like this:

{
    'code': '0',
    'msg': 'Success',
    'data': None
}
URL: /fapi/v2/futures_transfer

Type: POST

Content-Type: application/json

Description: New Future Account Transfer (USER_DATA)(HMAC SHA256)

Body-parameters:

Parameter	Type	Required	Description
coinSymbol	string	true	coin symbol
amount	bigdecimal	true	transfer amount
transferType	string	true	WALLET_TO_CONTRACT,
CONTRACT_TO_WALLET
unionId	string	false	transfer union tag
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	object	return data
Get Future Account transfer History List (USER_DATA)(HMAC SHA256)
curl -X GET -i /fapi/v2/futures_transfer_history?transferType=wallet_to_contract
The above command returns JSON structured like this:

{
    'code': '0',
    'msg': 'Success',
    'data': [{
        'transferType': 'wallet_to_contract',
        'symbol': 'USDT',
        'amount': 1.0,
        'status': 1,
        'ctime': 1685404575000
    }, {
        'transferType': 'wallet_to_contract',
        'symbol': 'USDT',
        'amount': 3.0,
        'status': 1,
        'ctime': 1685495897000
    }, {
        'transferType': 'wallet_to_contract',
        'symbol': 'USDT',
        'amount': 566.0,
        'status': 1,
        'ctime': 1685562991000
    }, {
        'transferType': 'wallet_to_contract',
        'symbol': 'USDT',
        'amount': 66.0,
        'status': 1,
        'ctime': 1685571419000
    }, {
        'transferType': 'wallet_to_contract',
        'symbol': 'USDT',
        'amount': 3.0,
        'status': 1,
        'ctime': 1685573130000
    }]
}
URL: /fapi/v2/futures_transfer_history

Type: GET

Content-Type: application/json

Description: Get Future Account transfer History List (USER_DATA)(HMAC SHA256)

Query-parameters:

Parameter	Type	Required	Description
coinSymbol	string	false	coin symbol
beginTime	long	false	default the recent 30-day data
endTime	long	false	end time
transferType	string	true	WALLET_TO_CONTRACT,
CONTRACT_TO_WALLET
page	int	false	default 1
limit	int	false	Default 10, Max 200
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	array	return data
└─transferType	string	WALLET_TO_CONTRACT,
CONTRACT_TO_WALLET
└─symbol	string	symbol
└─amount	bigdecimal	transfer amount
└─afterAmount	bigdecimal	after transfer amount
└─status	int	Transfer status, 0 payment, 1 success and 2 failure
└─ctime	long	create time
User's Force Orders (USER_DATA)
curl -X GET -i /fapi/v2/forceOrdersHistory?contractName=E-BTC-USDT
The above command returns JSON structured like this:

{
    'code': '0',
    'msg': 'Success',
    'data': [{
        'id': 1690600111070971191,
        'clientId': '0',
        'uid': 11568,
        'positionType': 2,
        'open': 'CLOSE',
        'side': 'SELL',
        'type': 1,
        'leverageLevel': 20,
        'price': 25878.61801778723,
        'volume': 357.0,
        'openTakerFeeRate': 0.0,
        'openMakerFeeRate': 0.0,
        'closeTakerFeeRate': 0.0,
        'closeMakerFeeRate': 0.0,
        'realizedAmount': -44.21710198209588,
        'dealVolume': 357,
        'dealMoney': 923.8666632350041,
        'lockMoney': 0.0,
        'unlockMoney': 0.0,
        'avgPrice': 25878.61801779,
        'tradeFee': 0.0,
        'status': 2,
        'memo': 0,
        'source': 6,
        'ctime': '2023-06-13T20:55:51',
        'mtime': '2023-06-13T12:55:51',
        'brokerId': 1000,
        'usingAccountType': 0,
        'shareRoyaltyRatio': 0.0
    }]
}
URL: /fapi/v2/forceOrdersHistory

Type: GET

Content-Type: application/json

Description: User's Force Orders (USER_DATA)

Query-parameters:

Parameter	Type	Required	Description
contractName	string	true	Contract name E.g. E-BTC-USDT
beginTime	long	false	default the recent 30-day data
endTime	long	false	end time
autoCloseType	string	false	"LIQUIDATION" for liquidation orders, "ADL" for ADL orders.
page	int	false	Default 1
limit	int	false	Default 10, Max 200
Response-fields:

Field	Type	Description
code	string	status code
msg	string	message content
data	array	return data
└─id	int	id
└─clientId	string	false
└─uid	int	user id
└─positionType	int	1 crossed position, 2 isolated position
└─open	string	true
└─side	string	trade direction, BUY/SELL
└─type	string	true
└─leverageLevel	int	Leverage multiple
└─price	bigdecimal	Order price
└─volume	bigdecimal	Order quantity
└─openTakerFeeRate	bigdecimal	open taker fee rate
└─openMakerFeeRate	bigdecimal	open maker fee rate
└─closeTakerFeeRate	bigdecimal	close taker fee rate
└─closeMakerFeeRate	bigdecimal	close maker fee rate
└─realizedAmount	bigdecimal	Profit and losses occurred
└─dealVolume	int	Order deal Volume
└─dealMoney	bigdecimal	Order deal Money
└─lockMoney	bigdecimal	Order lock Money
└─unlockMoney	bigdecimal	Order unlock Money
└─avgPrice	bigdecimal	Order trade price
└─tradeFee	bigdecimal	Order trade fee
└─status	int	Order status. Possible values are：NEW(new order，not filled)、PARTIALLY_FILLED（partially filled）、FILLED（fully filled）、CANCELLED（already cancelled）andREJECTED（order rejected）
└─ctime	string	Creation time
└─mtime	string	Update time
Websocket Market Data
The connection method for Websocket is：

Base Url: wss://fmarket-ws.bitrue.com/kline-api/ws
Data is compressed in binary format except for heartbeat data (users need to decompress using the Gzip algorithm).
All trading pairs are in lowercase.
Each connection has a validity period of no more than 24 hours; please handle reconnects properly.
It is not recommended to subscribe to more than 100 streams per single connection.
If the user's messages exceed the limit, the connection will be terminated. Repeated disconnections from the same IP may result in server blocking.
It is advised not to establish more than 100 connections per IP at the same time.
The WebSocket server sends a Ping message every second.
If the WebSocket server does not receive a Pong message response within N seconds, the connection will be terminated (N=1).
Upon receiving a ping message, the client must promptly reply with a pong message.
Unsolicited pong messages are allowed but do not guarantee that the connection will remain open. Recommended format: {"pong":1721131206}
The volume and amount returned by the interface need to be multiplied by the Contract Size (multiplier) manually.
To get the method, you need to read the Current open contract interface: /fapi/v1/contracts
Subscribe to Depth Updates
Subscribe to this channel to receive real-time depth market data updates.

channel: market_$symbol_depth_step0

Parameter：

Parameter	Data Type	Required	Description	Allowed Values
symbol	string	true	Trading pair	All supported trading pairs. For example: e_btcusdt, e_xrpusdt...
Subscribe to Data

{
  "event": "sub",
  "params": {
    "channel": "market_$symbol_depth_step0",
    "cb_id": ""
  }
}
Unsubscribe

{
  "event": "unsub",
  "params": {
    "channel": "market_$symbol_depth_step0",
    "cb_id": ""
  }
}
Return Parameters:

Field	Data Type	Description
channel	string	The channel to which the data belongs, formatted as: market_$symbol_depth_step0
ts	long	System response timestamp
tick	object	
└─asks	array	Ask orders, sorted in ascending order by price. [price, amount]  (The amount part needs to be multiplied by the Contract Size)
└─buys	array	Bid orders, sorted in descending order by price. [price, amount]  (The amount part needs to be multiplied by the Contract Size) Buy orders, sorted in descending order by price. [price, quantity]
Response: Up to 30 data entries for bid and ask orders.

{
  "event_rep": "",
  "channel": "market_$symbol_depth_step0",
  "ts": 1721716298870,
  "status": "ok",
  "tick": {
    "asks": [
      [
        10000.19,
        0.93
      ],
      [
        10001.21,
        0.2
      ],
      [
        10002.22,
        0.34
      ]
    ],
    "buys": [
      [
        9999.53,
        0.93
      ],
      [
        9998.2,
        0.2
      ],
      [
        9997.19,
        0.21
      ]
    ]
  }
}
Subscribe to Trades
Receive real-time detailed transaction details for the market.

channel: market_$symbol_trade_ticker

Parameter：

Parameter	Data Type	Required	Description	Allowed Values
symbol	string	true	Trading pair	All supported trading pairs. For example: e_btcusdt, e_xrpusdt...
Subscribe to Data

{
  "event": "sub",
  "params": {
    "channel": "market_$symbol_trade_ticker",
    "cb_id": ""
  }
}
Unsubscribe

{
  "event": "unsub",
  "params": {
    "channel": "market_$symbol_trade_ticker",
    "cb_id": ""
  }
}
Response Parameters:

Field	Data Type	Description
channel	string	The channel to which the data belongs, formatted as: market_$symbol_depth_step0
ts	long	System response timestamp
tick	object	
└─data	array	Maximum time in data
└──amount	string	Transaction amount (This needs to be multiplied by the Contract Size)
└──vol	string	Transaction volume (This represents transaction volume; multiply by the contract size to get the number of contracts.)
└──price	string	Transaction price
└──side	string	Trading initiator (order direction of taker): 'BUY' or 'SELL'
└──ts	long	Transaction time
Response

{
  "event_rep": "",
  "channel": "market_$symbol_trade_ticker",
  "tick": {
    "data": [
      {
        "amount": "1666656191.2",
        "ds": "2024-07-23 22:03:11",
        "price": "66008.8",
        "side": "SELL",
        "ts": 1721743391398,
        "vol": "25249"
      }
    ]
  },
  "ts": 1721743391000,
  "status": "ok"
}
Requesting Trade History Data
Supports a single request method to obtain transaction details (up to the most recent 300 transactions)：

channel: market_$symbol_trade_ticker

Parameter：

Parameter	Data Type	Required	Description	Allowed Values
symbol	string	true	Trading pair	All supported trading pairs. For example: e_btcusdt, e_xrpusdt...
Request Parameters：

Parameter	Data Type	Required	Description	Allowed Values
channel	string	true	Subscription channel	
top	integer	false	Number of recent records to retrieve	Up to the most recent 300 transaction records
Request Data

{
  "event": "req",
  "params": {
    "channel": "market_$symbol_trade_ticker",
    "top": 100
  }
}
Response Parameters：

Field	Data Type	Description
channel	string	The channel to which the data belongs, formatted as: market_$symbol_depth_step0
ts	long	System response timestamp
data	array	
└─side	array	Trading initiator (order direction of taker): 'buy' or 'sell'
└─price	float	Transaction price
└─vol	float	Transaction volume (This represents transaction volume; multiply by the contract size to get the number of contracts.)
└─amount	float	Transaction amount (This needs to be multiplied by the Contract Size)
Response

{
  "event_rep": "rep",
  "channel": "market_$symbol_trade_ticker",
  "cb_id": "$symbol",
  "ts": 1506584998239,
  "status": "ok",
  "data": [
    {
      "side": "buy",
      "price": 32.233,
      "vol": 232,
      "amount": 323
    },
    {
      "side": "buy",
      "price": 32.233,
      "vol": 232,
      "amount": 323
    }
  ]
}
Subscribe to Kline Market Data
Once Kline data is generated, the WebSocket server will push updates to the client through this subscription topic:

The Kline stream will push updates for the requested Kline type (latest Kline) every second.

To subscribe to Kline data, you need to provide an interval parameter, ranging from minutes to weeks.

channel: market_$symbol_kline_$interval

Parameter：

Parameter	Data Type	Required	Description	Allowed Values
symbol	string	true	Trading pair	All supported trading pairs. For example: e_btcusdt, e_xrpusdt...
interval	string	true	Kline interval	1min, 5min, 15min, 30min, 60min, 2h, 4h, 1day, 1week
Subscribe Data

{
  "event": "sub",
  "params": {
    "channel": "market_$symbol_kline_$interval",
    "cb_id": ""
  }
}
Unsubscribe Data

{
  "event": "unsub",
  "params": {
    "channel": "market_$symbol_kline_$interval",
    "cb_id": ""
  }
}
Return Parameters：

Field	Data Type	Description
channel	string	The channel to which the data belongs, formatted as: market_$symbol_kline_$interval
ts	long	System response timestamp
tick	object	
└─id	integer	Unix timestamp, starting time scale
└─amount	float	Transaction amount (This needs to be multiplied by the Contract Size)
└─vol	float	Transaction volume (This represents transaction volume; multiply by the contract size to get the number of contracts.)
└─ds	string	Start time
└─open	float	Opening price
└─close	float	Closing price
└─low	float	Lowest price
└─high	float	Highest price
Response

{
  "channel": "market_$symbol_kline_$interval",
  "data": [],
  "tick": {
    "amount": 396539282326.3,
    "close": 19517.1,
    "ds": "2022-07-13 14:00:00",
    "high": 19556.5,
    "id": 1657692000,
    "low": 19465.1,
    "open": 19507.3,
    "vol": 20325940
  },
  "ts": 1657696418000,
  "status": "ok"
}
Request Historical Kline Data
channel: market_$symbol_kline_$interval

Parameters:

Parameter	Data Type	Required	Description	Allowed Values
symbol	string	true	Trading pair	All supported trading pairs. For example: e_btcusdt, e_xrpusdt...
interval	string	true	Kline interval	1min, 5min, 15min, 30min, 60min, 2h, 4h, 1day, 1week
Request Parameters:

Parameter	Data Type	Required	Description	Allowed Values
channel	string	true	Subscription channel	
endIdx	float	false	Returns data before endIdx	Less than current time
pageSize	float	false	Returns specified number of entries when endIdx is specified	Up to 300
Request Data:

{
  "event": "req",
  "params": {
    "channel": "market_$symbol_kline_$interval",
    "cb_id": "",
    "endIdx": "1506602880",
    "pageSize": 10
  }
}
Response Parameters:

Field	Data Type	Description
channel	string	The channel to which the data belongs, formatted as: market_$symbol_kline_$interval
ts	long	System response timestamp
data	array	
└─id	integer	Unix timestamp, starting time scale
└─amount	float	Transaction amount (This needs to be multiplied by the Contract Size.)
└─vol	float	Transaction volume (This represents transaction volume; multiply by the contract size to get the number of contracts)
└─ds	string	Start time
└─open	float	Opening price
└─close	float	Closing price
└─low	float	Lowest price
└─high	float	Highest price
Response

{
  "event_rep": "rep",
  "channel": "market_$symbol_kline_$interval",
  "data": [
    {
      "amount": 1721334621154,
      "close": 41307,
      "ds": "2021-07-26 00:00:00",
      "high": 356000,
      "id": 1627228800,
      "low": 3000,
      "open": 34145,
      "vol": 43865325
    }
  ],
  "tick": null,
  "ts": 1721744417000,
  "status": "ok"
}
Subscribe to 24h Market Overview
Receive aggregated market overview data.

channel: market_$symbol_ticker

Parameter：

Parameter	Data Type	Required	Description	Allowed Values
symbol	string	true	Trading pair	All supported trading pairs. For example: e_btcusdt, e_xrpusdt...
Subscribe to Data

{
  "event": "sub",
  "params": {
    "channel": "market_$symbol_ticker"
  }
}
Unsubscribe

{
  "event": "unsub",
  "params": {
    "channel": "market_$symbol_ticker",
    "cb_id": ""
  }
}
Return Parameters：

Field	Data Type	Description
channel	string	The channel to which the data belongs, formatted as: market_$symbol_kline_$interval
ts	long	System response timestamp
tick	object	
└─amount	float	Transaction amount (This needs to be multiplied by the Contract Size)
└─vol	float	Transaction volume (This represents transaction volume; multiply by the contract size to get the number of contracts)
└─open	float	Opening price
└─close	float	Closing price
└─low	float	Lowest price
└─high	float	Highest price
└─rose	float	Percentage rise
Response

{
  "channel": "market_$symbol_ticker",
  "ts": 1506584998239,
  "tick": {
    "amount": 123.1221,
    "vol": 1212.12211,
    "open": 2233.22,
    "close": 1221.11,
    "high": 22322.22,
    "low": 2321.22,
    "rose": -0.2922
  },
  "status": "ok"
}
Websocket Account and Order
The base API endpoint is: https://fapiws-auth.bitrue.com
A User Data Stream listenKey is valid for 30 minutes after creation.
API-keys are passed into the API via the X-CH-APIKEY header.
API-keys are passed into the API via the X-CH-SIGN header. It is based on timestamp + method + requestPath + body string (+ means string connection) as the operation object
The value of timestamp is the same as the X-CH-TS request header, method is the request method, and the letters are all uppercase: GET/POST
Doing a PUT on a listenKey will extend its validity for 30 minutes.
Doing a DELETE on a listenKey will close the stream and invalidate the listenKey.
Doing a POST on an account with an active listenKey will return the currently active listenKey and extend its validity for 30 minutes.
A listenKey is a stream.
Users can listen to multiple streams.
The base websocket endpoint is: wss://fapiws.bitrue.com
User Data Streams are accessed at /stream?listenKey=<listenKey>
Signature generation
Timing Security
The signature interface needs to pass the timestamp in the X-CH-TS field in the HTTP header, and its value should be the unix timestamp of the request sending time e.g. 1528394129373
An additional parameter, recvWindow, may be sent to specify the number of milliseconds after timestamp the request is valid for. If recvWindow is not sent, it defaults to 5000.
In addition, if the server calculates that the client's timestamp is more than one second ‘in the future’ of the server’s time, it will also reject the request.
The logic is as follows:
Serious trading is about timing. Networks can be unstable and unreliable, which can lead to requests taking varying amounts of time to reach the servers. With recvWindow, you can specify that the request must be processed within a certain number of milliseconds or be rejected by the server.
It recommended to use a small recvWindow of 5000 or less!

SIGNED Endpoint Examples for POST /sapi/v1/order
Here is a step-by-step example of how to send a vaild signed payload from the Linux command line using echo, openssl, and curl.

Key	Value
apiKey	vmPUZE6mv9SD5V5e14y7Ju91duEh8A
secretKey	902ae3cb34ecee2779aa4d3e1d226686
Parameter	Value
symbol	BTCUSDT
side	BUY
type	LIMIT
volume	1
price	9300
Signature example
body:
{"symbol":"BTCUSDT","price":"9300","volume":"1","side":"BUY","type":"LIMIT"}
HMAC SHA256 Signature:
Curl command : shell [linux]$ curl -H "X-CH-APIKEY: c3b165fd5218cdd2c2874c65da468b1e" -H "X-CH-SIGN: c50d0a74bb9427a9a03933d0eded03af9bf50115dc5b706882a4fcf07a26b761" -H "X-CH-TS: 1588591856950" -H "Content-Type:application/json" -X POST 'http://localhost:30000/sapi/v1/order/test' -d '{"symbol":"BTCUSDT","price":"9300","quantity":"1","side":"BUY","type":"LIMIT"}'
Error Codes
Errors consist of two parts: an error code and a message. Codes are universal, but messages can vary.

code	description	memo
200	SUCCESS	200 for success,others are error codes.
503	SERVICE_ERROR	An unknown error occurred while processing the request.
1022	INVALID_API_KEY	You are not authorized to execute this request.
1102	MANDATORY_PARAM_EMPTY_OR_MALFORMED	A mandatory parameter was not sent, was empty/null, or malformed.
-1150	INVALID_LISTEN_KEY	This listenKey does not exist.
ListenKey
CREATE A LISTENKEY (USER_STREAM)
url
POST /user_stream/api/v1/listenKey

Start a new user data stream. The stream will close after 60 minutes unless a keepalive is sent. If the account has an active listenKey, that listenKey will be returned and its validity will be extended for 60 minutes.

Response:
{
  "msg": "succ",
  "code": 200,
  "data":
  {
    "listenKey": "ac3abbc8ac18f7977df42de27ab0c87c1f4ea3919983955d2fb5786468ccdb07"
  }
}
Ping/Keep-alive a ListenKey (USER_STREAM)
url
PUT /user_stream/api/v1/listenKey/{listenKey}

Keep alive a user data stream to prevent a time out. User data streams will close after 60 minutes. It's recommended to send a ping about every 30 minutes.

Response:
{
  "msg": "succ",
  "code": 200
}
Close a ListenKey (USER_STREAM)
url
DELETE /user_stream/api/v1/listenKey/{listenKey}

Close out a user data stream.

Response:
{
  "msg": "succ",
  "code": 200
}
keep-alive(websocket)
you should send pong message after receive a ping message.

ping: json {"event":"ping","ts":"1635221621062"}

pong：

{"event":"pong","ts":"1635221621062"}
User stream
User Account stream subscribe： {"event":"sub","params":{"channel":"user_account_update"}} response：

sub success : {"event":"user_account_update","status":"ok","ts":1689568979259}

payload
order event :
{
    "e": "ORDER_TRADE_UPDATE", // Event type
    "E": 1568879465651, // Event time (timestamp)
    "o": {
        "s": "BTCUSDT", // Trading pair
        "c": "TEST", // Client-provided order ID
        "S": "SELL", // Order direction
        "o": "MARKET", // Order type (MARKET|LIMIT|IOC|POST_ONLY...)
        "q": "0.001", // Original order quantity (multiplied by face value)
        "p": "0", // Original order price
        "ap": "0", // Average order price (price after execution)
        "x": "NEW", // Specific execution type for this event (new, liquidation, trade, cancel, adl)
        "X": "NEW", // Current status of the order (status)
        "i": 8886774, // Order ID
        "l": "0", // Order quantity filled in the current event
        "z": "0", // Cumulative filled order quantity
        "L": "0", // Price at which the order was filled in the current event
        "N": "USDT", // Fee asset type
        "n": "0", // Fee amount (total fee)
        "T": 1568879465650, // Trade time
        "t": 0, // Trade ID
        "m": false, // Was this trade a maker or taker? (make, take) Reserved field
        "R": false, // Is this a reduce-only order? (default false) Reserved field
        "ps": "LONG", // Position direction (long if present, short if empty)
        "rp": "0" // Realized profit or loss for this trade (current P&L)
    }
}
Orders are updated with the executionReport event.

Execution types(x):

NEW - The order has been accepted into the engine.
CANCELED - The order has been canceled by the user.
TRADE - Part of the order or all of the order's quantity has filled.
LIQUIDATION - force liquidation when the position under
acount event
{
    "e": "ACCOUNT_UPDATE", // Event type
    "E": 1564745798939, // Event time
    "T": 1564745798938, // Matching time (tentative)
    "a": // Account update event
    {
        "m": "ORDER", // Event trigger reason (enum: see table)
        "B": [ // Balance information
            {
                "a": "USDT", // Asset name
                "cw": "122624.12345678", // Cross-margin balance
                "lb": "0.000", // Locked balance
                "iw": "100.12345678", // Isolated margin wallet balance
                "bc": "50.12345678" // Balance change not related to profit and loss or trading fees
            }, // Only send relevant account balances.
            {
                "a": "BUSD",
                "cw": "122624.12345678",
                "lb": "0.0000",
                "iw": "100.12345678",
                "bc": "50.12345678"
            }
        ],
        "P": [{
            "s": "BTCUSDT", // Trading pair
            "pa": "0", // Position amount
            "ep": "0.00000", // Entry price
            "lp": "28343.33", // Last settlement price
            "cr": "200", // Cumulative realized profit and loss (history_realized_amount) including fees
            "up": "0", // Unrealized profit and loss for the position (lp -> current)
            "mt": "1", // Margin type, position type (1 Cross, 2 Isolated)
            "iw": "0.00000000", // If isolated, isolated margin for the position
            "ps": "SHORT|LONG" // Position direction (SHORT|LONG)
        }]
    }
}
Error code list
Error code	Description
0	Success
-1000	Unknown error occurred while processing the request
-1001	Internal error; unable to process your request. Please try again
-1002	You are not authorized to perform this request. The request requires sending an API Key; we recommend attaching X-CH-APIKEY to all request headers
-1003	Request frequency exceeds the limit
-1004	You are not authorized to perform this request; user does not exist
-1006	Received a message that does not conform to the expected format; order status is unknown
-1007	Timeout waiting for backend server response. Sending status is unknown; execution status is unknown
-1014	Unsupported order combination
-1015	Too many orders. Please reduce the number of your orders
-1016	Server offline
-1017	We recommend attaching Content-Type to all request headers and setting it to application/json
-1020	UNSUPPORTED_OPERATION
-1021	Invalid timestamp; time offset is too large
-1022	Invalid signature
-1023	You are not authorized to perform this request. The request requires sending a timestamp; we recommend attaching X-CH-TS to all request headers
-1024	You are not authorized to perform this request. The request requires sending a sign; we recommend attaching X-CH-SIGN to all request headers
-1025	User has not activated the contract
-1100	Illegal characters in the request
-1101	Too many parameters sent
-1102	Required parameter {0} not sent, empty, or in the wrong format
-1103	Unknown parameters sent
-1104	Not all sent parameters have been read
-1105	Parameter {0} is empty
-1106	This parameter does not need to be sent
-1111	Precision exceeds the maximum value defined for this asset
-1112	No orders exist for the trading pair
-1116	Invalid order type
-1117	Invalid buy/sell direction
-1118	New client order ID is empty
-1121	Invalid contract
-1136	Order quantity is less than the minimum value
-1137	Order quantity exceeds the maximum limit
-1138	Order price is out of allowable range
-1139	This trading pair does not support market orders
-1140	Exceeds the maximum position limit
-1141	Duplicate cancellation or invalid order
-1145	Order status does not allow cancellation
-1146	Current contract cannot be traded temporarily
-1147	The current interface does not support coin-margined contracts
-1148	The current interface does not support USDT-margined contracts
-1149	Your isolated position does not exist
-1150	Maximum of {0} decimal places allowed
-1151	Transfer amount exceeds the limit
-1152	Position leverage adjustment failed
-1153	Maximum leverage does not exceed {0}
-1154	Order quantity exceeds the maximum limit
-1155	Order price deviates significantly from the latest trade price
-1156	Closing quantity exceeds the total position quantity
-1157	Position frozen, cannot be operated temporarily
-1158	Total order quantity exceeds the limit
-1159	Maximum of {0} decimal places allowed for order amount
-1160	Minimum order amount is {0}
-1161	Maximum order amount is {0}
-1162	Maximum of {0} decimal places allowed for limit order amount
-1163	There are currently open orders; leverage cannot be modified
-1164	Order quantity must be greater than {0}
-1165	Order type does not match user contract configuration {0}
-1166	Order leverage does not match user contract configuration {0}
-1167	Order book is too large; self-trade prevention failed
-1168	Order book is missing
-2013	Order does not exist
-2014	Invalid API key format
-2015	Invalid API key, IP, or permission
-2016	Trading is frozen
-2017	Insufficient balance
-2100	Parameter issue
-2101	User IP is non-compliant and the country is forcibly banned
-2102	User IP is soft-banned in the country