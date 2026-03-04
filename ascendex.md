AscendEx Pro API Documentation
AscendEx Pro API is the latest release of APIs allowing our users to access the exchange programmatically. It is a major revision of the older releases. The AscendEx team re-implemented the entire backend system in support for the AscendEx Pro API. It is designed to be fast, flexible, stable, and comprehensive.

What's New
Dynamic subscription/unsubscription to private and public data channels via WebSocket.
Synchronized/Asynchronized API calls. When placing/cancelling orders, you may use synchronized method to get the order result in a single API call. You may also use asynchronized method to achieve minimum latency.
Simplified API schemas. For instance, we simplified the cancel order logic, now you can track the entire order life cycle with only one indentifier (orderId).
More detailed error message.
Market Making Incentive Program
AscendEX offers a Market Making Incentive Program for professional liquidity providers. Key benefits of this program include:

Favorable fee structure.
Monthly bonus pending satisfying KPI.
Direct Market Access and Co-location service.
Users with good maker strategies and significant trading volume are welcome to participate in this long-term program. If your account has a trading volume of more than 150,000,000 USDT in the last 30 days on any exchange, please send the following information via email to institution@ascendex.com, with the subject "Market Maker Incentive Application":

One AscendEX account ID.
A brief explanation of your market making method (NO detail is needed), as well as estimation of maker orders' percentage.
SDKs and Client Libraries
Official SDK
CCXT is our authorized SDK provider and you may access the AscendEX API through CCXT. For more information, please visit: https://ccxt.trade

Demo Code
We provide comprehensive demos (currently available in python). We provide two types of demo codes:

Short, self contained demo scripts that you can plugin to you larger system.
Large, complex demo scripts to show you how to design a trading strategy using APIs from this document.
See https://github.com/ascendex/ascendex-pro-api-demo for more details.

Got Questions?
Join our official telegram channel: https://t.me/AscendEX_Official_API

Release Note
2022-05-19

Limit Info API is deprecated, use Limit Info API v2 to get ban info and message threshold.

2022-02-28

Added the Limit Info API to get ban info and risk limit info.
2022-02-25

Update the List all Products API to different endpoints by account type: for cash /api/pro/v1/cash/products, for margin /api/pro/v1/margin/products.
2021-12-02

Update the Balance Snapshot API and Order and Balance Detail API to different endpoints by account type: api/pro/data/v1/cash/balance/snapshot for cash and api/pro/data/v1/margin/balance/snapshot for margin balance;api/pro/data/v1/cash/balance/history for cash and api/pro/data/v1/margin/balance/history for margin balance or order fill detail.
Redirect the Order Hist v2 API to new endpoint api/pro/data/v2/order/hist (No group in the endpoint anymore), and change prehash string to data/v2/order/hist. Original way through <group>/api/pro/v2/order/hist is still supported, but will be removed in the future.
2021-11-22

Replaced the ticker API GET api/pro/v1/ticker with GET api/pro/v1/spot/ticker to include only spot symbols. The old API will still be available but will be removed in the future.
Added the VIP fee schedule API and the Fee Schedule by Symbol API.
2021-07-16

Introduced the experimental Balance Snapshot and Order and Balance Detail api.
2021-06-15

Introduced the List all Assets (version v2) api. The version v1 api will remain available. However, you are highly recommended to upgrade.
2021-06-08

Added balance transfer between sub account.
2020-08-10

We have deprecated list history orders API and replace it with list history orders v2 API.
2020-08-06

Added expireTime and allowedIps to account info
2020-07-17

Added API to query deposit addresses.
Added API to query wallet transaction history
2019-12-26

Added execution instruction to order messages (place new order, list open/historical orders). This field indicates if the order is Post-Only (Post) or forced liquidation (Liquidation). It is named execInst in RESTful responses and ei in websocket messages.
REST APIs
We always respond with json include code field to indicate request result. 0 usually means success response, and you could find data in json format in field data; any code other than 0 indicate failure during the request process. For failure response, usually you could find detailed error in fields message, reason, and possibly extra info.

For private data, such as open order, balance, we usually include accountId, and accountCategory value in top level of response.

Authenticate a RESTful Request
Create Request
To access private data via RESTful APIs, you must include the following headers:

x-auth-key - required, the api key as a string.
x-auth-timestamp - required, the UTC timestamp in milliseconds of your request
x-auth-signature - required, the request signature (see Sign a Request)
The timestamp in the header will be checked against server time. If the difference is greater than 30 seconds, the request will be rejected.

Sign a Request
Signing a RESTful Request

# bash 
APIPATH=info
APIKEY=CEcrjGyipqt0OflgdQQSRGdrDXdDUY2x
SECRET=hV8FgjyJtpvVeAcMAgzgAFQCN36wmbWuN7o3WPcYcYhFd8qvE43gzFGVsFcCqMNk
TIMESTAMP=`date +%s%N | cut -c -13` # 1608133910000
MESSAGE=$TIMESTAMP+$APIPATH
SIGNATURE=`echo -n $MESSAGE | openssl dgst -sha256 -hmac $SECRET -binary | base64`
echo $SIGNATURE  # /pwaAgWZQ1Xd/J4yZ4ReHSPQxd3ORP/YR8TvAttqqYM=

curl -X GET -i \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "x-auth-key: $APIKEY" \
  -H "x-auth-signature: $SIGNATURE" \
  -H "x-auth-timestamp: $TIMESTAMP" \
  https://ascendex.com/api/pro/v1/info
To query APIs with private data, you must include a signature using base64 encoded HMAC sha256 algorithm. The prehash string is <timestamp>+<api-path>. The timestamp is the UTC timestamp in milliseconds.

See the code demos in bash on the right. For other programming languages, please refer to https://github.com/ascendex/ascendex-pro-api-demo/tree/main/signature_demo.

Market Data (Public)
You don't need to sign the request to access public market data.

List all Assets
List all Assets

curl -X GET "https://ascendex.com/api/pro/v2/assets"
Sample Response

{
    "code": 0,
    "data": [
        {
            "assetCode":      "USDT",
            "assetName":      "Tether",
            "precisionScale":  9,
            "nativeScale":     4,
            "blockChain": [
                {
                    "chainName":        "Omni",
                    "withdrawFee":      "30.0",
                    "allowDeposit":      true,
                    "allowWithdraw":     true,
                    "minDepositAmt":    "0.0",
                    "minWithdrawal":    "50.0",
                    "numConfirmations":  3
                },
                {
                    "chainName":        "ERC20",
                    "withdrawFee":      "10.0",
                    "allowDeposit":      true,
                    "allowWithdraw":     true,
                    "minDepositAmt":    "0.0",
                    "minWithdrawal":    "20.0",
                    "numConfirmations":  12
                }
            ]
        }
    ]
}
HTTP Request
GET /api/pro/v2/assets

You can obtain a list of all assets listed on the exchange through this API.

Response Content
Name	Type	Description
assetCode	String	asset code. e.g. "BTC"
assetname	String	full name of the asset, e.g. "Bitcoin"
precisionScale	Int	scale used in internal position keeping.
nativeScale	Int	scale used in deposit/withdraw transaction from/to chain.
blockChain	List	block chain specific details
Blockchain specific details

Name	Type	Description
chainName	String	name of the blockchain
withdrawFee	String	fee charged for each withdrawal request. e.g. "0.01"
allowDepoist	Boolean	allow deposit
allowWithdraw	Boolean	allow withdrawal
minDepositAmt	String	minimum amount required for the deposit request e.g. "0.0"
minWithdrawalAmt	String	minimum amount required for the withdrawal request e.g. "50"
numConfirmations	Int	number of confirmations needed for the exchange to recoganize a deposit
List all Products
List all Products

curl -X GET "https://ascendex.com/api/pro/v1/cash/products"
curl -X GET "https://ascendex.com/api/pro/v1/margin/products"
Sample Response

{
    "code": 0,
    "data": [
        {
          "symbol": "BTC/USDT",
          "displayName": "BTC/USDT",
          "domain": "USDS",
          "tradingStartTime": 1546300800000,
          "collapseDecimals": "1,0.1,0.01",
          "minQty": "0.000000001",
          "maxQty": "1000000000",
          "minNotional": "5",
          "maxNotional": "400000",
          "statusCode": "Normal",
          "statusMessage": "",
          "tickSize": "0.01",
          "useTick": false,
          "lotSize": "0.00001",
          "useLot": false,
          "commissionType": "Quote",
          "commissionReserveRate": "0.001",
          "qtyScale": 5,
          "priceScale": 2,
          "notionalScale": 4
        },
    ]
}
HTTP Request
GET /api/pro/v1/{accountCategory}/products

Response Content
You can obtain a list of all products traded on the exchange through this API.

The response contains the following general fields:

Name	Type	Description
symbol	String	e.g. "ASD/USDT"
baseAsset	String	e.g. "ASD"
quoteAsset	String	e.g. "USDT"
status	String	"Normal"
The response also contains criteria for new order request.

Name	Type	Description
symbol	String	Symbol like BTC/USDT
displayName	String	Symbol's display Name
domain	String	Symbol's Tradins Domain USDS / ETH / BTC
tradingStartTime	Number	Trading Start Time
collapseDecimals	String	Trading Start Time
minQty	String	minimum quantity of an order
maxQty	String	minimum quantity of an order
minNotional	String	minimum notional of an order
maxNotional	String	maximum notional of an order
statusCode	String	Symbol's status code
statusMessage	String	Symbol's status message
tickSize	String	tick size of order price
useTick	Boolean	
lotSize	String	lot size of order quantity
useLot	Boolean	
commissionType	String	"Base", "Quote", "Received"
commissionReserveRate	String	e.g. "0.001", see below.
qtyScale	Number	Quantity Scale
notionalScale	Number	Notional Scale
When placing orders, you should comply with all criteria above. More details can be found in the Order Request Criteria section.

Ticker
Ticker for one trading pair

// curl -X GET 'https://ascendex.com/api/pro/v1/spot/ticker?symbol=ASD/USDT'
{
    "code": 0,
    "data": {
        "symbol": "ASD/USDT",
        "open":   "0.06777",
        "close":  "0.06809",
        "high":   "0.06899",
        "low":    "0.06708",
        "volume": "19823722",
        "ask": [
            "0.0681",
            "43641"
        ],
        "bid": [
            "0.0676",
            "443"
        ]
    }
}
List of Tickers for one or multiple trading pairs

// curl -X GET "https://ascendex.com/api/pro/v1/spot/ticker?symbol=ASD/USDT,"
{
    "code": 0,
    "data": [
        {
            "symbol": "ASD/USDT",
            "open":   "0.06777",
            "close":  "0.06809",
            "high":   "0.06809",
            "low":    "0.06809",
            "volume": "19825870",
            "ask": [
                "0.0681",
                "43641"
            ],
            "bid": [
                "0.0676",
                "443"
            ]
        }
    ]
}
HTTP Request
GET api/pro/v1/spot/ticker

You can get summary statistics of one or multiple symbols (spot market) with this API.

Request Parameters
Name	Type	Required	Value Range	Description
symbol	String	No		you may specify one, multiple, or all symbols of interest. See below.
This API endpoint accepts one optional string field symbol:

If you do not specify symbol, the API will responde with tickers of all symbols in a list.
If you set symbol to be a single symbol, such as ASD/USDT, the API will respond with the ticker of the target symbol as an object. If you want to wrap the object in a one-element list, append a comma to the symbol, e.g. ASD/USDT,.
You shall specify symbol as a comma separated symbol list, e.g. ASD/USDT,BTC/USDT. The API will respond with a list of tickers.
Respond Content
The API will respond with a ticker object or a list of ticker objects, depending on how you set the symbol parameter.

Each ticker object contains the following fields:

Field	Type	Description
symbol	String	
open	String	the traded price 24 hour ago
close	String	the last traded price
high	String	the highest price over the past 24 hours
low	String	the lowest price over the past 24 hours
volume	String	the total traded volume in base asset over the paste 24 hours
ask	[String, String]	the price and size at the current best ask level
bid	[String, String]	the price and size at the current best bid level
Code Sample
Please refer to python code to query ticker info.

Bar Info
Request

curl -X GET "https://ascendex.com/api/pro/v1/barhist/info"
Sample response

{
    "code": 0,
    "data": [
        {
            "name": "1",
            "intervalInMillis": 60000
        },
        {
            "name": "5",
            "intervalInMillis": 300000
        },
        {
            "name": "15",
            "intervalInMillis": 900000
        },
        {
            "name": "30",
            "intervalInMillis": 1800000
        },
        {
            "name": "60",
            "intervalInMillis": 3600000
        },
        {
            "name": "120",
            "intervalInMillis": 7200000
        },
        {
            "name": "240",
            "intervalInMillis": 14400000
        },
        {
            "name": "360",
            "intervalInMillis": 21600000
        },
        {
            "name": "720",
            "intervalInMillis": 43200000
        },
        {
            "name": "1d",
            "intervalInMillis": 86400000
        },
        {
            "name": "1w",
            "intervalInMillis": 604800000
        },
        {
            "name": "1m",
            "intervalInMillis": 2592000000
        }
    ]
}
HTTP Request

GET /api/pro/v1/barhist/info

This API returns a list of all bar intervals supported by the server.

Request Parameters
This API endpoint does not take any parameters.

Resposne
Name	Type	Description
name	String	name of the interval
intervalInMillis	Long	length of the interval
Plesae note that the one-month bar (1m) always resets at the month start. The intervalInMillis value for the one-month bar is only indicative.

The value in the name field should be your input to the Historical Bar Data API.

Historical Bar Data
Request

curl -X GET "https://ascendex.com/api/pro/v1/barhist?symbol=ASD/USDT&interval=1"
Sample response

{
    "code": 0,
    "data": [
        {
            "data": {
                "c": "0.05019",
                "h": "0.05019",
                "i": "1",
                "l": "0.05019",
                "o": "0.05019",
                "ts": 1575409260000,
                "v": "1612"},
           "m": "bar",
           "s": "ASD/USDT"},
        {
            "data": {
                "c": "0.05019",
                "h": "0.05027",
                "i": "1",
                "l": "0.05017",
                "o": "0.05017",
                "ts": 1575409200000,
                "v": "57242"
                },
           "m": "bar",
           "s": "ASD/USDT"},
    ]
}
HTTP Request
GET /api/pro/v1/barhist

This API returns a list of bars, with each contains the open/close/high/low prices of a symbol for a specific time range.

Request Parameters
Name	Type	Required	Description
symbol	String	Yes	e.g. "ASD/USDT"
interval	String	Yes	a string representing the interval type.
to	Long	No	UTC timestamp in milliseconds. If not provided, this field will be set to the current time.
from	Long	No	UTC timestamp in milliseconds.
n	Int	No	default 10, number of bars to be returned, this number will be capped at 500
The requested time range is determined by three parameters - to, from, and n - according to rules below:

from/to each specifies the start timestamp of the first/last bar.
to is always honored. If not provided, this field will be set to the current system time.
For from and to:
if only from is provided, then the request range is determined by [from, to], inclusive. However, if the range is too wide, the server will increase from so the number of bars in the response won't exceed 500.
if only n is provided, then the server will return the most recent n data bars to time to. However, if n is greater than 500, only 500 bars will be returned.
if both from and n are specified, the server will pick one that returns fewer bars.
Response
Name	Type	value	Description
m	String	bar	message type
s	String		symbol
data:ts	Long		bar start time in milliseconds
i	String		interval
o	String		open price
c	String		close price
h	String		high price
l	String		low price
v	String		volume in base asset
Code Sample
Please refer python code to [get bar history]{https://github.com/ascendex/ascendex-pro-api-demo/blob/master/python/query_pub_barhist.py}

Order Book (Depth)
Request for Order Book (Depth) Data

curl -X GET "https://ascendex.com/api/pro/v1/depth?symbol=ASD/USDT"
Order Book (Depth) Data - Sample response

{
    "code": 0,
    "data": {
        "m":      "depth-snapshot",
        "symbol": "ASD/USDT",
        "data": {
            "seqnum":  5068757,
            "ts":      1573165838976,
            "asks": [
                [
                    "0.06848",
                    "4084.2"
                ],
                [
                    "0.0696",
                    "15890.6"
                ]
            ],
            "bids": [
                [
                    "0.06703",
                    "13500"
                ],
                [
                    "0.06615",
                    "24036.9"
                ]
            ]
        }
    }
}
HTTP Request
GET /api/pro/v1/depth

Request Parameters
Name	Type	Required	Value Range	Description
symbol	String	Yes	Valid symbol supported by exchange	
Response Content
data field in response contains depth data and meta info.

Name	Type	Description
m	String	"depth-snapshot"
symbol	String	e.g. "ASD/USDT"
data	Json	actual bid and ask info. See below for detail.
Actual depth data in data section:

Name	Type	Description
seqnum	Long	a sequence number that is guaranteed to increase for each symbol.
ts	Long	UTC timestamp in milliseconds when the message is generated by the server
asks	[String, String]	pair of price and size of ask levels
bids	[String, String]	pair of price and size of bid levels
Demo Sample
Pleas refer to python code to take depth snapshot

Market Trades
Request

curl -X GET "https://ascendex.com/api/pro/v1/trades?symbol=ASD/USDT"
Sample response

{
    "code": 0,
    "data": {
        "m": "trades",
        "symbol": "ASD/USDT",
        "data": [
            {
                "seqnum": 144115191800016553,
                "p": "0.06762",            
                "q": "400",
                "ts": 1573165890854,
                "bm": false               // is buyer maker?
            },
            {
                "seqnum": 144115191800070421,
                "p": "0.06797",
                "q": "341",
                "ts": 1573166037845,
                "bm": true
            }
        ]
    }
}
HTTP Request
GET /api/pro/v1/trades

Request Parameters
Name	Type	Required	Value Range	Description
symbol	String	Yes	Valid symbol supported by exchange	
n	Int	No	any positive integer, capped at 100	number of trades to return.
Response Content
data field in response contains trade data and meta info.

Name | Type | Description m | String | trades symbol | String | trade symbol data | Json | A list of trade record; see below for detail.

Trade record information in data:

Name	Type	Description
seqnum	Long	the sequence number of the trade record. seqnum is always increasing for each symbol, but may not be consecutive
p	String	trade price in string format
q	String	trade size in string format
ts	Long	UTC timestamp in milliseconds
bm	Boolean	If true, the maker of the trade is the buyer.
Code Sample
Please refer to python code to [query trades]{https://github.com/ascendex/ascendex-pro-api-demo/blob/master/python/query_pub_trades.py}




WebSocket
General Message Request/Handling Logic from Client Side
Client usually initiate request with op parameter (followed by other required parameters).
Server usually reply message with m value to indicate message topic, e.g., order, depth, auth.
Private data response usually has accountId field, such as order, balance; public data response usually contains symbol field.
Uniquie id parameter is recommended for your request. We will echo it back for you to track the requests. (The only exception is depth-snapshot, we do not include id)
WebSocket Request
WSS <account-group>/api/pro/v1/stream

In order to authorize the session you must include <account-group> in the URL. Without <account-group>, you can only subscribe to public data.

Code Sample
Please refer to python code for all kinds of [websocket operation]{https://github.com/ascendex/ascendex-pro-api-demo/blob/master/python/client.py} (e.g. authorization, sub/unsub, place/cancel order, and so on)

Keep the Connection Alive via Ping/Pong
In order to keep the websocket connection alive, you have two options, detailed below.

Method 1: Responding to Server ping messages
Method 1. keep the connection alive by responding to Server pushed ping message

<<< { "m": "ping", "hp": 3 }  # Server pushed ping message
>>> { "op": "pong" }   # Client responds with pong
If the server doesn't receive any client message after a while, it will send a ping message to the client. Once the ping message is received, the client should promptly send a pong message to the server. If you missed two consecutive ping messages, the session will be disconnected.

Server Ping Message Schema

Name	Type	Description
op	String	ping
hp	Int	health point: when this value decreases to 0, the session will be disconnected.
Method 2: Sending ping messages to Server
Method 2. keep the connection alive by sending ping message to the server

>>> { "op": "ping" }                                      # Client initiated ping message (every 30 seconds)
<<< { "m":"pong", "code":0, "ts":1574260701259, "hp": 2 } # Server responds to client ping 
You can also send ping message to the server every 15 seconds to keep the connection alive. The server will stop sending ping message for 30 seconds if a client initiated ping message is received.

Server Pong Message Schema

Name	Type	Description
m	String	pong
code	Int	error code, for the pong mesage, the error code is always 0 (success)
ts	Long	server time in UTC miliseconds
hp	Int	health point: when this value decreases to 0, the session will be disconnected.
WebSocket Authentication
You must authenticate the websocket session in order to recieve private data and send account specific requests (e.g. placing new orders).

You have two options to authenticate a websocket session.

by adding authentication data in the request header when connecting to websocket.
by sending an op:auth message to the server after you have connected to websocket.
Once you successfully connect to the websocket, you will receive a connected message:

for authenticated websocket session: {"op":"connected","type":"auth"}
for unauthenticated websocket session: {"op":"connected","type":"unauth"}
If the session is disconnected for some reason, you will receive a disconnected message:

{"m":"disconnected","code":100005,"reason":"INVALID_WS_REQUEST_DATA","info":"Session is disconnected due to missing pong message from the client"}
Method 1 - WebSocket Authentication with Request Headers
Authenticate with Headers

# # Install wscat from Node.js if you haven't
# npm install -g wscat  

APIPATH=stream
APIKEY=BclE7dBGbS1AP3VnOuq6s8fJH0fWbH7r
SECRET=fAZcQRUMxj3eX3DreIjFcPiJ9UR3ZTdgIw8mxddvtcDxLoXvdbXJuFQYadUUsF7q
TIMESTAMP=`date +%s%N | cut -c -13`
MESSAGE=$TIMESTAMP+$APIPATH
SIGNATURE=`echo -n $MESSAGE | openssl dgst -sha256 -hmac $SECRET -binary | base64`

wscat -H "x-auth-key: $APIKEY" \
  -H "x-auth-signature: $SIGNATURE" \
  -H "x-auth-timestamp: $TIMESTAMP" \
  -c wss://ascendex.com/1/api/pro/v1/stream -w 1 -x '{"op":"sub", "id": "abc123", "ch": "order:cshQtyfq8XLAA9kcf19h8bXHbAwwoqDo:ASD/USDT"}'
This is similar to the way you authenticate any RESTful request. You need to add the following header fields to the connection request:

x-auth-key
x-auth-timestamp
x-auth-signature
The server will then check if the data is correctly signed before upgrading the connection protocol to WebSocket.

Note that if you specify these header fields, the server will reject the websocket connection request if authentication fails.

Method 2 - WebSocket Authentication by Sending the Auth Message
Authenticate by Sending the auth Message

# # Install wscat from Node.js if you haven't
# npm install -g wscat  

APIPATH=stream
APIKEY=BclE7dBGbS1AP3VnOuq6s8fJH0fWbH7r
SECRET=fAZcQRUMxj3eX3DreIjFcPiJ9UR3ZTdgIw8mxddvtcDxLoXvdbXJuFQYadUUsF7q
TIMESTAMP=`date +%s%N | cut -c -13`
MESSAGE=$TIMESTAMP+$APIPATH
SIGNATURE=`echo -n $MESSAGE | openssl dgst -sha256 -hmac $SECRET -binary | base64`

wscat -c wss://ascendex.com/1/api/v1/pro/stream -w 1 -x "{\"op\":\"auth\", \"id\": \"abc123\", \"t\": $TIMESTAMP, "key": \"$APIKEY\", \"sig\": \"$SIGNATURE\"}"
You can also authenticate a live websocket session by sending an op:auth message to the server.

Name	Type	Required	Description
op	String	Yes	"auth"
id	String	No	optional id field, you may safely skip it
t	Long	Yes	UTC timestamp in milliseconds, use this timestamp to generate signature
key	String	Yes	your api key
sig	String	Yes	the signature is generated by signing "<timestamp>+stream"
More comprehensive examples can be found at:

Python for websocket auth
Authentication Response
Auth success message

{  
  "m": "auth",
  "id": "abc123",
  "code": 0
}
Auth error message

{
  "m":"auth",
  "id": "abc123",
  "code": 200006,
  "err": "Unable to find User Account Data"
}
You will receive a message for authentication result after you send authentication request.

Field	Type	Description
m	String	"auth"
id	String	echo back the id if you provide one in the request
code	Long	Any code other than 0 indicate an error in authentication
err	Optional[String]	Provide detailed error message if code is not 0
Subscribe to Data Channels
How to Subscribe
Use wscat from Node.js to connect to websocket data.

# # Install wscat from Node.js if you haven't
# npm install -g wscat  
npm install -g wscat

# Connect to websocket
wscat -c wss://ascendex.com/0/api/pro/v1/stream -x '{"op":"sub", "ch": "depth:ASD/USDT"}'
You can also setup authorized session

@ToDo
You can subscribe/unsubscribe to one or multiple data channels.

If the subscription is successful, you will receive at least one ack message confirming the request is successful and you will start receiving data streams.
If the subscription is unsuccessful, you will receive one ack message with text explaining why the subscription failed.
Request Body Schema
The standard messages to subscribe to / unsubscribe from data channels is an JSON object with fields:

Name	Type	Description
op	String	sub to subscribe and unsub to unsubscribe
id	Optional[String]	user specified UUID, if provided, the server will echo back this value in the response message
ch	String	name of the data channel with optional arguments, see below for details
Subscribe to bbo stream for symbol BTC/USDT

{ "op": "sub", "id": "abcd1234", "ch": "bbo:BTC/USDT" }
Subscribe to ref-px stream for symbol BTC

{ "op": "sub", "id": "abcd1234", "ch": "ref-px:BTC" }
Subscribe to trade stream for a list of symbols

{ "op": "sub", "id": "abcd1234", "ch": "trades:BTC/USDT,ETH/USDT,ASD/USDT" }
Unsubscribes from the depth stream for all symbols (method 1)

{ "op": "unsub", "id": "abcd1234", "ch": "depth:*" }
Unsubscribes from the depth stream for all symbols (methond 2)

{ "op": "unsub", "id": "abcd1234", "ch": "depth" }
Unsubscribes from the 1 minute bar streams for all symbols (method 1)

{ "op": "unsub", "id": "abcd1234", "ch": "bar:1:*" }
Unsubscribes from the 1 minute bar streams for all symbols (method 2)

{ "op": "unsub", "id": "abcd1234", "ch": "bar:1" }
Unsubscribes from bar streams of all frequencies for ASD/USDT

{ "op": "unsub", "id": "abcd1234", "ch": "bar:*:ASD/USDT" }
Response for sub multiple symbols in one single message

{"m":"sub","id":"abc23g","ch":"summary:BTC/USDT,ASD/USDT","code":0}
Response for unsub multiple symbols in one single message

{ "m": "unsub", "id": "abcd1234", "ch": "bar:*:ASD/USDT" }
Customize Channel content with ch
You can customize the channel content by setting ch according to the table below:

Type	Value	Description
public	depth:<symbol>	Updates to order book levels.
public	bbo:<symbol>	Price and size at best bid and ask levels on the order book.
public	trades:<symbol>	Market trade data
public	bar:<interval>:<symbol>	Bar data containing O/C/H/L prices and volume for specific time intervals
public	ref-px:<symbol>	Reference prices used by margin risk Calculation.
Private	order:<account>	Order Update Stream: "cash", "margin", or actual accountId for `account.
Symbol in ref-px is single asset symbol(e.g. BTC), not trading pair symbol (e.g. BTC/USDT), which is different from other channels.

#### Unsubscribe with Wildcard Character *

Using the wildcard character *, you can unsubscribe from multiple channels with the same channel name.

Subscribe to single or multiple symbols
Subscribe to a single symbol (e.g. BTC/USDT), or multiple symbols (up to 10) separated by ",", e.g. "BTC/USDT,ETH/USDT".

Sub/Unsub response with multiple symbols
When sub or unsub from multiple symbols, we may ack symbol by symbol, or ack in one single message.

You can subscribe/unsubscribe one channel per subscription message. You can subscribe to multiple data channels by sending multiple subscription messages. However, the exchange limits the total number of data channels per client (NOT per session) according to the following rules:

@ToDo rule: maximum number of channels

Channel: Level 1 Order Book Data (BBO)
Subscribe to ASD/USDT quote stream

{ "op": "sub", "id": "abc123", "ch":"bbo:ASD/USDT" }
Unsubscribe to ASD/USDT quote stream

{ "op": "unsub", "id": "abc123", "ch":"bbo:ASD/USDT" }
BBO Message

{
    "m": "bbo",
    "symbol": "BTC/USDT",
    "data": {
        "ts": 1573068442532,
        "bid": [
            "9309.11",
            "0.0197172"
        ],
        "ask": [
            "9309.12",
            "0.8851266"
        ]
    }
}
You can subscribe to updates of best bid/offer data stream only. Once subscribed, you will receive BBO message whenever the price and/or size changes at the top of the order book.

Each BBO message contains price and size data for exactly one bid level and one ask level.

Channel: Level 2 Order Book Updates
Subscribe to ASD/USDT depth updates stream

{ "op": "sub", "id": "abc123", "ch":"depth:ASD/USDT" }
Unsubscribe to ASD/USDT depth updates stream

{ "op": "unsub", "id": "abc123", "ch":"depth:ASD/USDT" }
The Depth Message

{
    "m": "depth",
    "symbol": "ASD/USDT",
    "data": {
        "ts": 1573069021376,
        "seqnum": 2097965,
        "asks": [
            [
                "0.06844",
                "10760"
            ]
        ],
        "bids": [
            [
                "0.06777",
                "562.4"
            ],
            [
                "0.05",
                "221760.6"
            ]
        ]
    }
}
If you want to keep track of the most recent order book snapshot in its entirety, the most efficient way is to subscribe to the depth channel.

Each depth message contains a bids list and an asks list in its data field. Each list contains a series of [price, size] pairs that you can use to update the order book snapshot. In the message, price is always positive and size is always non-negative.

if size is positive and the price doesn't exist in the current order book, you should add a new level [price, size].
if size is positive and the price exists in the current order book, you should update the existing level to [price, size].
if size is zero, you should delete the level at price.
See Orderbook Snapshot for code examples.

Channel: Market Trades
Subscribe to ASD/USDT market trades stream

{ "op": "sub", "id": "abc123", "ch":"trades:ASD/USDT" }
Unsubscribe to ASD/USDT market trades stream

{ "op": "unsub", "id": "abc123", "ch":"trades:ASD/USDT" }
Trade Message

{
    "m": "trades",
    "symbol": "ASD/USDT",
    "data": [
        {
            "p":      "0.068600",
            "q":      "100.000",
            "ts":      1573069903254,
            "bm":      false,
            "seqnum":  144115188077966308
        }
    ]
}
The data field is a list containing one or more trade objects. The server may combine consecutive trades with the same price and bm value into one aggregated item. Each trade object contains the following fields:

Name	Type	Description
seqnum	Long	the sequence number of the trade record. seqnum is always increasing for each symbol, but may not be consecutive
p	String	the executed price expressed as a string
q	String	the aggregated traded amount expressed as string
ts	Long	the UTC timestamp in milliseconds of the first trade
bm	Boolean	if true, the buyer of the trade is the maker.
Channel: Bar Data
Subscribe to ASD/USDT 1 minute bar stream

{ "op": "sub", "id": "abc123", "ch":"bar:1:ASD/USDT" }
Unsubscribe to ASD/USDT 1 minute bar stream

{ "op": "unsub", "id": "abc123", "ch":"bar:1:ASD/USDT" }

//  Alternatively, you can unsubscribe all bar streams for ASD/USDT
{ "op": "unsub", "id": "abc123", "ch":"bar:*:ASD/USDT" }

// Or unsubscribe all 1 minute bar stream
{ "op": "unsub", "id": "abc123", "ch":"bar:1" }

// Or unsubscribe all bar stream
{ "op": "unsub", "id": "abc123", "ch":"bar" }
Bar Data Message

{
    "m": "bar",
    "s": "ASD/USDT",    
    "data": {
        "i":  "1",
        "ts": 1575398940000,
        "o":  "0.04993",
        "c":  "0.04970",
        "h":  "0.04993",
        "l":  "0.04970",
        "v":  "8052"
    }
}
The data field is a list containing one or more trade objects. The server may combine consecutive trades with the same price and bm value into one aggregated item. Each trade object contains the following fields:

Name	Type	Description
seqnum	Long	the sequence number of the trade record. seqnum is always increasing for each symbol, but may not be consecutive
p	String	the executed price expressed as a string
q	String	the aggregated traded amount expressed as string
ts	Long	the UTC timestamp in milliseconds of the first trade
bm	Boolean	if true, the buyer of the trade is the maker.
Channel: Order (and Balance)
Subscribe to cash account order update stream

{ "op": "sub", "id": "abc123", "ch":"order:cash" }
Subscribe to specific account id cshQtyfq8XLAA9kcf19h8bXHbAwwoqDo account for order update stream

{ "op": "sub", "id": "abc123", "ch":"order:cshQtyfq8XLAA9kcf19h8bXHbAwwoqDo" }
Unsubscribe from cash account order update stream

{ "op": "unsub", "id": "abc123", "ch":"order:cash" }
Order update message

{
    "m": "order", 
    "accountId": "cshQtyfq8XLAA9kcf19h8bXHbAwwoqDo", 
    "ac": "CASH", 
    "data": {
        "s":       "BTC/USDT", 
        "sn":       8159711, 
        "sd":      "Buy", 
        "ap":      "0", 
        "bab":     "2006.5974027", 
        "btb":     "2006.5974027",
        "cf":      "0", 
        "cfq":     "0", 
        "err":     "", 
        "fa":      "USDT",
        "orderId": "s16ef210b1a50866943712bfaf1584b", 
        "ot":      "Market", 
        "p":       "7967.62", 
        "q":       "0.0083", 
        "qab":     "793.23", 
        "qtb":     "860.23", 
        "sp":      "", 
        "st":      "New", 
        "t":        1576019215402,
        "ei":      "NULL_VAL"
    }
}
Balance Update Message (Cash Account)

{
    "m": "balance",
    "accountId": "cshQtyfq8XLAA9kcf19h8bXHbAwwoqDo",
    "ac": "CASH",
    "data": {
        "a" : "USDT",
        "sn": 8159798,
        "tb": "600",
        "ab": "600"
    }
}
Balance Update Message (Margin Account)

{
    "m": "balance",
    "accountId": "marOxpKJV83dxTRx0Eyxpa0gxc4Txt0P",
    "ac": "MARGIN",
    "data": {
        "a"  : "USDT",
        "sn" : 8159802,
        "tb" : "400",
        "ab" : "400",
        "brw": "0",
        "int": "0"
    }
}
Note: once you subscribe to the order channel, you will start receiving messages from the balance channel automatically. If you unsubscribe from the order channel, you will simultaneously unsubscribe from the balance channel.

You need to specify the account when subscribing to the order channel. You could specify account category cash, margin, or specific account id.

Order Messages
You can track the state change of each order thoughout its life cycle with the order update message (m=order). The data field is a single order udpate object. Each order update object contains the following fields:

Name	Type	Description
s	String	symbol
sn	long	sequence number
ap	String	average fill price
bab	String	base asset available balance
btb	String	base asset total balance
cf	String	cumulated commission
cfq	String	cumulated filled qty
err	String	error code; could be empty
fa	String	fee asset
orderId	String	order id
ot	String	order type
p	String	order price
q	String	order quantity
qab	String	quote asset available balance
qtb	String	quote asset total balance
sd	String	order side
sp	String	stop price; could be empty
st	String	order status
t	Long	latest execution timestamp
ei	String	execution instruction
Balance Messages
You will also receive balance update message (m=balance) for the asset balance updates not caused by orders. For instance, when you make wallet deposits/withdrawals, or when you transfer asset from the cash account to the margin account, you will receive balance update message.

For Cash Account Balance Update, the data field contains:

Name	Type	Description
a	String	asset
sn	long	sequence number
tb	String	total balance
ab	String	available balance
For Margin Account Balance Update, the data field contains:

Name	Type	Description
a	String	asset
sn	long	sequence number
tb	String	total balance
ab	String	available balance
brw	String	borrowed amount
int	String	interest amount
Data Query / Order Request
Besides subscript mesages, you could also send request message via websocket. You will receive exactly one message regarding each request message. Here are some use cases:

Place/cancel orders
Request orderbook snapshot data to initialize/rebuild orderbook.
WebSocket Request Schema
All operation or data request follow the same uniform format:

Name	Type	Required	Value	Description
op	String	Yes	req	
id	String	No	digits and numbers	if provided, the server will echo back this value in the response message
action	String	Yes	See below	name of the request action with optional arguments
account	String	NO	cash, margin	the account of the interest, this field is not required for public data request
args	{key:value}	No		each action has different args, please see each action for detail.
Supported action
Name	Description
place-order	Place new order
cancel-order	Cancel exisitng open order
cancel-all	Cancel all open orders on account level
depth-snapshot	Get market depth for symbol up to 500 level
depth-snapshot-top100	Get top 100 depth
market-trades	Get market trades for a symbol
balance	Request balance
open-order	Query open order
margin-risk	Get margin risk
WebSocket Response Schema
We try to provide all data in uniform format.

Ack or Data

Response follow the following schema

Name	Type	Description
m	String	message topic related with request action
id	Optional[String]	user specified UUID, if provided, the server will echo back this value in the response message
action	String	echo action field in request
data or info	Json	detailed data for data request, or info for operation result(e.g. order place/cancel)
Error

Name	Type	Description
m	String	"error"
id	String	Echo back the error
code	Long	
reason	String	simple error message
info	String	detailed error message
Example error response

{
    "m":      "error",
    "id":     "ab123",
    "code":   100005,
    "reason": "INVALID_WS_REQUEST_DATA",
    "info":   "Invalid request action: trade-snapshot"
}
WS: Orderbook Snapshot
Requesting the current order book snapshot

{ "op": "req", "id": "abcdefg", "action": "depth-snapshot", "args": { "symbol": "ASD/USDT" } }
Depth snapshot message

{
    "m": "depth-snapshot",
    "symbol": "ASD/USDT",
    "data": {
        "seqnum": 3167819629,
        "ts": 1573142900389,
        "asks": [
            [
                "0.06758",
                "585"
            ],
            [
                "0.06773",
                "8732"
            ]
        ],
        "bids": [
            [
                "0.06733",
                "667"
            ],
            [
                "0.06732",
                "750"
            ]
        ]
    }
}
You can request the current order book via websocket by an depth-snapshot request.

The args schema:

Name	Data Type	Description
op	String	req
action	String	depth-snapshot
id	String	echo back in case of error
args:symbol	String	Symbol, e.g. ASD/USDT
The response schema:

Name	Data Type	Description
m	String	depth-snapshot
symbol	String	Symbol, e.g. ASD/USDT
data:seqnum	Long	
data:ts	Long	UTC Timestamp in milliseconds
data:asks	[[String, String]]	List of (price, size) pair
data:bids	[[String, String]]	List of (price, size) pair
You can following the steps below to keep track of the the most recent order book:

Connecting to WebSocket Stream
Subscribe to the depth update stream, see Level 2 Order Book Updates.
Send a depth-snapshot request to the server.
Once you obtain the snapshot message from the server, initialize the snapshot.
Using consequent depth messages to update the order book.
Please note that field seqnum should strictly increase by 1 for each new depth update (each symbol maintain its own seqnum). If you see a larger than 1 gap from previous seqnum (for the same symbol), then there might be data loss, you need to repeat above steps to maintain a new order book.

The depth-snapshot message is constructed in a consistent way with all depth message.

Please note that the depth-snapshot API has higher latency. The response time is usually between 1000 - 2000 milliseconds. It is intended to help you initialize the orderbook, not to be used to obtain the timely order book data.

More comprehensive examples can be found at:

Python: websocket orderbook snapshot
WS: Place Order
Request to place new order

{
    "op": "req",
    "action": "place-Order",
    "account": "cash",
    "args": {
        "time":       1573772908483,
        "id":         "11eb9a8355fc41bd9bf5b08bc0d18f6b",
        "symbol":     "EOS/USDT",
        "orderPrice": "3.27255",
        "orderQty":   "30.557210737803853",
        "orderType":  "limit",
        "side":       "buy",
        "postOnly":    false,
        "respInst":   "ACK"
    }
}
Successful ACK message

{
    "m": "order", 
    "accountId": "cshQtyfq8XLAA9kcf19h8bXHbAwwoqDo", 
    "ac": "CASH", 
    "action": "place-order", 
    "status": "Ack", 
    "info": {
        "symbol": "BTC/USDT", 
        "orderType": "Limit", 
        "timestamp": 1576015701441, 
        "id": "17e1f6809122469589ffc991523b505d", 
        "orderId": "s16ef1daefbe08669437121523b505d"
    }
}
Error response message

{
    "m": "order",
    "accountId": "cshQtyfq8XLAA9kcf19h8bXHbAwwoqDo",
    "ac": "CASH", 
    "action": "place-order",
    "status": "Err",
    "info": {
        "id":      "69c482a3f29540a0b0d83e00551bb623",
        "symbol":  "ETH/USDT",
        "code":     300011,
        "message": "Not Enough Account Balance",
        "reason":  "INVALID_BALANCE"
    }
}
Place order via websocket

Request

Make new order request follow the general websocket request rule, with proper place new order parameters as specified in rest api for args field.

see placing order via RESTful API.

Response

Respond with m field as order, and action field as place-order; status field to indicate if this is a successful Ack or failed Err.

ACK

With status field as Ack to indicate this new order request pass some basic sanity check, and has been sent to matching engine.

info field provide some detail: if you provide id in your request, it will be echoed back as id to help you identify; we also provide server side generated orderId, which is the id you should use for future track or action on the order.

ERR

With status field as Err to indicate there is some obvisous errors in your order.

info field provide some detail: if you provide id in your request, it will be echoed back as id to help you identify; we also provide error code, reason, and message detail.





Experimental APIs
Real Time Level 2 Orderbook Updates
WebSocket messages from the default depth channel are throttled with 300 milliseconds throttling intervals. If you want to subscribe to realtime orderbook updates, please refer to this article.

Subscribe to Order Channel with Ready Ack Mode
By default, when you subscribe to the order channel via WebSocket, you automatically enter the New Ack Mode. In this mode, when the order is accepted by the matching engine, you will receive an order message with status st=New. This is true even when the order will immediately change status. For instance, when you place a Post-only order that crosses the book, it will immediately be rejected. However, in the New Ack Mode, you will first receive an order message with st=New, then immediately receive another message with st=Canceled. However, if your order successfully enters the orderbook without crossing with order on the opposite side, you will only receive one message with st=New. This makes it hard for trading bots to decide when to take actions.

To address this issue, we introduced the Ready Ack mode. Follow this link for more details.

Appendex
ENUM: BlockChains
ABBC Coin
Akash
Algorand
ATOM
BandProtocol
BCH-SLP
BEP20
Binance
Bitcoin
Bitcoin ABC
Bitcoin Cash ABC
Bitcoin HD
Bitcoin SV
bytom
Cardano
casper
Dash
Divi
dogechain
e-Money
Elrond eGold
EOS
ERC20
Ether Zero
Ethereum Classic
Filecoin
FIOProtocol
fusion
GO20
Harmony
Hathor
hermez
HPB
insolar
Iost chain
kava
Litecoin
LTONetwork
Matic network
MetaHash
NEO
nervos
Nimiq
Omni
oneledger
Ontology
Own blockchain
Persistence
polkadot
Qtum
Raven
Ripple
Solana
Stafi
Stellar
Tezos
Tron
vechain
wanchain
xDai
XEM
YAP STONE
Zerocash
Zilliqa
Error Message
We structure our error message in three levels: * Error Group provide a broad error category (Error group id = error code / 10000) * Error Reason provide some intuitive information on the error * Error Message explains error detail.

In most situation, we provide simple error in this way: {"code": XYABCDE, "reason": XXXXXXXX}; for complicated scenatio (such as order place/cancel request, websocket request, and so on), we provide rich format error: {"code": XYZBCDE, "reason":XXXXXXXX, "message":YYYYYYYY}.

Rich format error is derived from simple error, so you could get error message with same error code and reason, but different message content.

Error Base Group
We summary the major error group below.

group name	group code	derived code	description
GeneralError	10	10XXXX	Errors applied to general scenario
FormatError	15	15XXXX	Format related error
AuthError	20	20XXXX	Auth related error
OrderError	30	30XXXX	Order action and information related error
MarginError	31	31XXXX	Margin account and trading related error
SystemError	50	50XXXX	System related error
BehaviorError	90	90XXXX	Behavior error
10XXXX - General Error
code	reason	descripion
100001	INVALID_HTTP_INPUT	Http request is invalid
100002	DATA_NOT_AVAILABLE	Some required data is missing
100003	KEY_CONFLICT	The same key exists already
100004	INVALID_REQUEST_DATA	The HTTP request contains invalid field or argument
100005	INVALID_WS_REQUEST_DATA	Websocket request contains invalid field or argument
100006	INVALID_ARGUMENT	The arugment is invalid
100007	ENCRYPTION_ERROR	Something wrong with data encryption
100008	SYMBOL_ERROR	Symbol does not exist or not valid for the request
100009	AUTHORIZATION_NEEDED	Authorization is require for the API access or request
100010	INVALID_OPERATION	The action is invalid or not allowed for the account
100011	INVALID_TIMESTAMP	Not a valid timestamp
100012	INVALID_STR_FORMAT	String format does not
100013	INVALID_NUM_FORMAT	Invalid number input
100101	UNKNOWN_ERROR	Some unknown error
15XXXX - Format Error
code	reason	descripion
150001	INVALID_JSON_FORMAT	Require a valid json object
20XXXX - Auth Error
Auth related errors.

code	reason	descripion
200001	AUTHENTICATION_FAILED	Authorization failed
200002	TOO_MANY_ATTEMPTS	Tried and failed too many times
200003	ACCOUNT_NOT_FOUND	Account not exist
200004	ACCOUNT_NOT_SETUP	Account not setup properly
200005	ACCOUNT_ALREADY_EXIST	Account already exist
200006	ACCOUNT_ERROR	Some error related with error
200007	CODE_NOT_FOUND	
200008	CODE_EXPIRED	Code expired
200009	CODE_MISMATCH	Code does not match
200010	PASSWORD_ERROR	Wrong assword
200011	CODE_GEN_FAILED	Do not generate required code promptly
200012	FAKE_COKE_VERIFY	
200013	SECURITY_ALERT	Provide security alert message
200014	RESTRICTED_ACCOUNT	Account is restricted for certain activity, such as trading, or withdraw.
200015	PERMISSION_DENIED	No enough permission for the operation
30XXXX - Order Error
Order place/cancel/query related errors. We usually provide rich format errors based on these simple ones.

code	reason	descripion
300001	INVALID_PRICE	Order price is invalid
300002	INVALID_QTY	Order size is invalid
300003	INVALID_SIDE	Order side is invalid
300004	INVALID_NOTIONAL	Notional is too small or too large
300005	INVALID_TYPE	Order typs is invalid
300006	INVALID_ORDER_ID	Order id is invalid
300007	INVALID_TIME_IN_FORCE	Time In Force in order request is invalid
300008	INVALID_ORDER_PARAMETER	Some order parameter is invalid
300009	TRADING_VIOLATION	Trading violation on account or asset
300011	INVALID_BALANCE	No enough account or asset balance for the trading
300012	INVALID_PRODUCT	Not a valid product supported by exchange
300013	INVALID_BATCH_ORDER	Some or all orders are invalid in batch order request
300020	TRADING_RESTRICTED	There is some trading restriction on account or asset
300021	TRADING_DISABLED	Trading is disabled on account or asset
300031	NO_MARKET_PRICE	No market price for market type order trading
31XXXX - Margin Error
Margin trading related errors.

code	reason	descripion
310001	INVALID_MARGIN_BALANCE	No enough margin balance
310002	INVALID_MARGIN_ACCOUNT	Not a valid account for margin trading
310003	MARGIN_TOO_RISKY	Leverage is too high
310004	INVALID_MARGIN_ASSET	This asset does not support margin trading
310005	INVALID_REFERENCE_PRICE	There is no valid reference price
50XXXX - System Error
code	reason	descripion
510001	SERVER_ERROR	Something wrong with server.
90XXXX - Behavior Error
code	reason	descripion
900001	HUMAN_CHALLENGE	Human change do not pass



















































Introducing Futures Pro (v2) APIs
General
Mainnet URL: https://ascendex.com

Testnet

Testnet URL: https://api-test.ascendex-sandbox.com

You are free to register one or more accounts in the testnet. You can use the magic code 888888 to bypass all verification code checks (email verification, phone number verification, two-step authentication, etc.).

You accounts will automatically receive initial funding.

Please expect the testnet to be reset every a few days.

Obtain API Keys
Prior to use API, you need to login the website to create API Key with proper permissions. The API key is shared for all instruments in AscendEx including cash, margin and futures.

You can create and manage your API Keys here.

Every user can create up to 10 API Keys, each can be applied with either permission below:

View permission: It is used to query the data, such as order query, trade query.
Trade permission: It is used to place order, cancel order and transfer, etc.
Transfer permission: It is used to create/cancel asset transfer order, etc.
Please remember below information after creation:

Access Key is used in API request
Secret Key is used to generate the signature (only visible once after creation)
The API Key can bind maximum 20 IP addresses (either host IP or network IP), we strongly suggest you bind IP address for security purpose. The API Key without IP binding will be expired after 90 days.
SDKs and Client Libraries
Official SDK

CCXT is our authorized SDK provider and you may access the AscendEX API through CCXT. For more information, please visit: https://ccxt.trade

Demo Code

Python Demo: https://github.com/ascendex/ascendex-futures-api-demo-v2

Market Making Incentive Program
AscendEX offers a Market Making Incentive Program for professional liquidity providers. Key benefits of this program include:

Favorable fee structure.
Monthly bonus pending satisfying KPI.
Direct Market Access and Co-location service.
Users with good maker strategies and significant trading volume are welcome to participate in this long-term program. If your account has a trading volume of more than 150,000,000 USDT in the last 30 days on any exchange, please send the following information via email to institution@ascendex.com, with the subject "Market Maker Incentive Application":

One AscendEX account ID.
A brief explanation of your market making method (NO detail is needed), as well as estimation of maker orders' percentage.
Got Questions?
Join our official telegram channel: https://t.me/AscendEX_Official_API

Change Log
2022-08-16

Funding Payment History added to get account funding payment history.

2022-05-19

Limit Info API is deprecated, use Limit Info API v2 to get ban info and message threshold info.

2022-02-28

Added the Limit Info API to get ban info and risk limit info.
2021-11-22

Added the ticker API for futures contracts.
Added the VIP fee schedule API and the Fee Schedule by Symbol API.
2021-03-18

Added WebSocket Query Open Orders API.
2021-03-03

Fixed bug of cancelling a filled order with empty fields error response.
Added symbol to error response from WebSocket Place Order.
Updated nextFundingTime value in RESTful Futures Pricing Data response.
Updated nextFundingTime f value in WebSocket Futures Pricing Data message.
Added error response demo in Place New Order.
Added error response demo in Place Batch Orders.
Fixed bug in Cancel All Open Orders when no data is passed in request body.
Fixed bug of URL Not Found in Account Info.
Added openInterest in Futures Pricing Data
Added oi (open interest) in Channel: Futures Pricing Data
2021-02-26

Updated respInst field requirement in Place Batch Orders.
Updated respInst field explanation in Place New Order.
2021-02-25

Updated id field requirement in WebSocket Place Order request.
2021-02-23

Removed collapseDecimals field from Futures Contracts Info response.
2021-02-22

Added RESTful Current Order History API.
2021-02-21

Added Order Id Generate Algorithm.
Added RESTful Place Batch Orders API.
Added RESTful Cancel Batch Orders API.
Added RESTful Query Order By ID API.
2021-02-19

Added WebSocket Account Snapshot API.
Added WebSocket Place Order API.
Added WebSocket Cancel Order API.
Added WebSocket Cancel All Orders API.
2021-02-18

Replaced baseAsset and quoteAsset with settlementAsset in Futures Contract Info response.
Updated Account Info API path.
Futures Trading System Specification
Contract Position Notional (CPN)
CPN = abs(position size * mark price) for the contract
CPN is defined for each contract.

Margin Group
The Isolated Group

The isolated group manages a single position with a certain amount of margin moved out of the crossed group. It isolates the risk of the position from other margin groups. Your maximum loss will be limited to the total margin moved into the isolated group.

Each account may have at most one isolated group per contract.

The Crossed Group

The crossed group manages all positions except those in isolated groups.

Total Margin
For the isolated group

Total margin is set by the user. You can find its value in the isolatedMargin field from the Position endpoint.

You can increase / decrease the total margin of the isolated margin group via the Change Margin endpoint.

For the isolated group, we also refer to total margin as isolated margin.

For the crossed group

Total Margin = sum(Asset Balance * Reference Price * Collateral Discount Factor) for each collateral asset
Discount factor can be found in the discountFactor field from the Futures Collateral Asset Info endpoint.

Group Collateral Balance
For the isolated group

Group Collateral Balance = isolated margin + unrealized pnl of the isolated position
For the crossed group

Group Collateral Balance = total margin of the crossed group + total unrealized pnl of all positions in the crossed group
The Group Collateral Balance is important to determine the risk level of the margin group. If it becomes lower than the position maintanence margin, all positions in the margin group are expected to be liquidated.

Position Initial/Maintenance Margin Rate
Initial/Maintenance Margin Rate is system-specified for each position bracket and each contract. You may refer to the marginRequirements section from the Futures Contract Info endpoint for position brackets.

You should compare Contract Position Notional (CPN) with each position bracket to determine your initial and maintenance margin rate.

Position Initial/Maintenance Margin
For the isolated group

Position Initial Margin = CPN * Initial Margin Rate
Position Maintenance Margin = CPN * Maintenance Margin
For the crossed group

Position Initial Margin = sum(CPN * Initial Margin Rate) for each contract in the crossed group
Position Maintenance Margin = sum(CPN * Maintenance Margin Rate) for each contract in the crossed group
Liquidation Price
V = Total Margin + Unrealized Pnl - Maintenance Margin
For long positions

R = abs(position size) * (1 - maintenance margin rate)
Liquidation Price = mark price - V / R
If the calculated liquidation price is negative, the position won't be liquidation even when the price becomes zero.

For short positions

R = abs(position size) * (1 + maintenance margin rate)
Liquidation Price = mark price + V / R
Unrealized PnL
The Unrealized PnL of a position is calculated as:

Unrealized PnL = mark price * position + reference cost
Note that position and reference cost are of opposite signs.

The Unrealized PnL will be rolled (settled) when:

position is closed or flipped side (long becomes short, vice versa)
every 15 minutes AND abs(Unrealized Pnl) >= 10 USDT
Assume your current position is P, the current reference cost if RC, and unrealized PnL is L, after rolling:

position = P
reference cost = RC + L
realized PnL = 0
You should always include the unrealized PnL when calculating the collateral balance.

Realized PnL
Realized Pnl is merely a bookkeeping entry for all profits and losses realized by the current position under the assumption that the position was built on an average cost basis.

If you are mostly concerned about the risk of your positions, you can ignore the realized PnL.

RESTful APIs
Exchange Latency Info
Latency Info

curl -X GET https://ascendex.com/api/pro/v1/exchange-info?requestTime="$(date +%s%N | cut -b1-13)"
Latency Info - Sample response::

{
    "code": 0,
    "data":
    {
        "requestTimeEcho": 1640052379050,
        "requestReceiveAt": 1640052379063,
        "latency": 13
    }
}
HTTP Request

GET /api/pro/v1/exchange-info

Request Parameters
Name	Type	Required	Value Range	Description
requestTime	Long	Yes	milliseconds since UNIX epoch in UTC	the client's local time. The server compare it with the system time to calculate latency.
General Info (Public)
Futures Contracts Info
Response - Futures Contracts Info

{
    "code": 0,
    "data": [
        {
            "symbol"          : "BTC-PERP",
            "status"          : "Normal",
            "displayName"     : "BTCUSDT",    // the name displayed on the webpage
            "settlementAsset" : "USDT",       // settlement asset
            "underlying"      : "BTC/USDT",
            "tradingStartTime": 1579701600000,
            "priceFilter": {
                "minPrice"  : "0.25",     // the order price cannot be smaller than the minPrice
                "maxPrice"  : "1000000",  // the order price cannot be greater than the maxPrice
                "tickSize"  : "0.25"      // the order price must be a multiple of the tickSize
            },
            "lotSizeFilter": {
                "minQty"  : "0.0001",     // the order quantity cannot be smaller than the minQty
                "maxQty"  : "1000000000", // the order quantity cannot be greater than the maxQty
                "lotSize" : "0.0001"      // the order quantity must be a multiple of the lotSize
            },
            "marginRequirements": [
                {
                    "positionNotionalLowerbound": "0",     // position lower bound
                    "positionNotionalUpperbound": "50000", // position upper bound
                    "initialMarginRate"         : "0.01",  // initial margin rate
                    "maintenanceMarginRate"     : "0.006"  // maintenance margin rate
                },
                {
                    "positionNotionalLowerbound": "50000",
                    "positionNotionalUpperbound": "200000",
                    "initialMarginRate"         : "0.02",
                    "maintenanceMarginRate"     : "0.012"
                }
            ]
        }
    ]
}
Get information for all futures contracts.

HTTP Request

GET /api/pro/v2/futures/contract

Response

Futures Collateral Asset Info
Response - Futures Collateral Asset Info

{
    "code": 0,
    "data": [
        {
            "asset"           : "BTC",
            "assetName"       : "Bitcoin",
            "conversionFactor": "0.995",
            "discountFactor"  : "0.98",
            "displayName"     : "BTC",
            "statusCode"      : "Normal"
        },
        {
            "asset"           : "USDT",
            "assetName"       : "Tether",
            "conversionFactor": "1",
            "discountFactor"  : "1",
            "displayName"     : "USDT",
            "statusCode"      : "Normal"
        },
        {
            "asset"           : "USDTR",
            "assetName"       : "Futures Reward Token",
            "conversionFactor": "1",
            "discountFactor"  : "1",
            "displayName"     : "USDTR",
            "statusCode"      : "NoTransaction"
        }
    ]
}
Get information for all futures collateral assets.

HTTP Request

GET /api/pro/v2/futures/collateral

Market Data (Public)
Anyone can access public market data via the API endpoints. No authentication is needed.

Futures Pricing Data
Requesting pricing data for all futures contract

{
    "code": 0,
    "data": {
        "contracts": [
            {
                "symbol"         : "BTC-PERP",          // contract symbol
                "time"           : 1614815005717,       // server time (UTC timestamp in milliseconds)
                "fundingRate"    : "0.000564448",       // funding rate 
                "indexPrice"     : "50657.35",          // index price of the underlying
                "markPrice"      : "50667.130409723",   // mark price of the contract
                "openInterest"   : "90.7366",           // funding rate
                "nextFundingTime": 1614816000000        // next funding time (UTC timestamp in milliseconds)
            }
        ],
        "collaterals": [
            {
                "asset": "USDTR",
                "referencePrice": "1"
            },
            {
                "asset": "USDC",
                "referencePrice": "0.9994"
            },
            {
                "asset": "ETH",
                "referencePrice": "1582.3264074"
            },
            {
                "asset": "PAX",
                "referencePrice": "0.99645"
            },
            {
                "asset": "BTC",
                "referencePrice": "50636.14"
            },
            {
                "asset": "USDT",
                "referencePrice": "1"
            }
        ],
    }
}
Get pricing data for all futures contracts.

HTTP Request

GET /api/pro/v2/futures/pricing-data

Bar Info
Request

curl -X GET "https://ascendex.com/api/pro/v1/barhist/info"
Sample response

{
    "code": 0,
    "data": [
        {
            "name": "1",
            "intervalInMillis": 60000
        },
        {
            "name": "5",
            "intervalInMillis": 300000
        },
        {
            "name": "15",
            "intervalInMillis": 900000
        },
        {
            "name": "30",
            "intervalInMillis": 1800000
        },
        {
            "name": "60",
            "intervalInMillis": 3600000
        },
        {
            "name": "120",
            "intervalInMillis": 7200000
        },
        {
            "name": "240",
            "intervalInMillis": 14400000
        },
        {
            "name": "360",
            "intervalInMillis": 21600000
        },
        {
            "name": "720",
            "intervalInMillis": 43200000
        },
        {
            "name": "1d",
            "intervalInMillis": 86400000
        },
        {
            "name": "1w",
            "intervalInMillis": 604800000
        },
        {
            "name": "1m",
            "intervalInMillis": 2592000000
        }
    ]
}
HTTP Request

GET /api/pro/v1/barhist/info

This API returns a list of all bar intervals supported by the server.

Request Parameters
This API endpoint does not take any parameters.

Resposne
Name	Type	Description
name	String	name of the interval
intervalInMillis	Long	length of the interval
Plesae note that the one-month bar (1m) always resets at the month start. The intervalInMillis value for the one-month bar is only indicative.

The value in the name field should be your input to the Historical Bar Data API.

Historical Bar Data
Request

curl -X GET "https://ascendex.com/api/pro/v1/barhist?symbol=BTC-PERP&interval=1"
Sample response

{
    "code": 0,
    "data":
    [
        {
            "m": "bar",
            "s": "BTC-PERP",
            "data":
            {
                "i": "1",
                "ts": 1637619240000,
                "o": "56263",
                "c": "56260",
                "h": "56263",
                "l": "56239",
                "v": "0.0126"
            }
        },
        {
            "m": "bar",
            "s": "BTC-PERP",
            "data":
            {
                "i": "1",
                "ts": 1637619300000,
                "o": "56243",
                "c": "56243",
                "h": "56243",
                "l": "56243",
                "v": "0.0001"
            }
        }
    ]
}
HTTP Request
GET /api/pro/v1/barhist

This API returns a list of bars, with each contains the open/close/high/low prices of a symbol for a specific time range.

Request Parameters
Name	Type	Required	Description
symbol	String	Yes	e.g. "BTC-PERP"
interval	String	Yes	a string representing the interval type.
to	Long	No	UTC timestamp in milliseconds. If not provided, this field will be set to the current time.
from	Long	No	UTC timestamp in milliseconds.
n	Int	No	default 10, number of bars to be returned, this number will be capped at 500
The requested time range is determined by three parameters - to, from, and n - according to rules below:

from/to each specifies the start timestamp of the first/last bar.
to is always honored. If not provided, this field will be set to the current system time.
For from and to:
if only from is provided, then the request range is determined by [from, to], inclusive. However, if the range is too wide, the server will increase from so the number of bars in the response won't exceed 500.
if only n is provided, then the server will return the most recent n data bars to time to. However, if n is greater than 500, only 500 bars will be returned.
if both from and n are specified, the server will pick one that returns fewer bars.
Response
Name	Type	value	Description
m	String	bar	message type
s	String		symbol
data:ts	Long		bar start time in milliseconds
i	String		interval
o	String		open price
c	String		close price
h	String		high price
l	String		low price
v	String		volume in quote asset
Code Sample
Please refer python code to [get bar history]{https://github.com/ascendex/ascendex-pro-api-demo/blob/main/python/query_pub_barhist.py}

Ticker
Ticker for one trading pair

// curl -X GET 'https://ascendex.com/api/pro/v2/futures/ticker?symbol=BTC-PERP'
{
    "code": 0,
    "data":
    {
        "symbol":  "BTC-PERP",
        "open":    "59488",
        "close":   "56725",
        "high":    "59724",
        "low":     "56672",
        "baseVol": "208.7414",
        "ask":
        [
            "56730",
            "0.0005"
        ],
        "bid":
        [
            "56710",
            "0.0042"
        ]
    }
}
List of Tickers for one or multiple trading pairs

// curl -X GET "https://ascendex.com/api/pro/v2/futures/ticker?symbol=BTC-PERP,"
{
    "code": 0,
    "data":
    [
        {
            "symbol":  "BTC-PERP",
            "open":    "59488",
            "close":   "56716",
            "high":    "59724",
            "low":     "56672",
            "baseVol": "208.7414",
            "ask":
            [
                "56720",
                "0.2315"
            ],
            "bid":
            [
                "56712",
                "0.0024"
            ]
        }
    ]
}
HTTP Request
GET api/pro/v2/futures/ticker

You can get summary statistics of one or multiple symbols (spot market) with this API.

Request Parameters
Name	Type	Required	Value Range	Description
symbol	String	No		you may specify one, multiple, or all symbols of interest. See below.
This API endpoint accepts one optional string field symbol:

If you do not specify symbol, the API will responde with tickers of all symbols in a list.
If you set symbol to be a single symbol, such as ASD/USDT, the API will respond with the ticker of the target symbol as an object. If you want to wrap the object in a one-element list, append a comma to the symbol, e.g. ASD/USDT,.
You shall specify symbol as a comma separated symbol list, e.g. ASD/USDT,BTC/USDT. The API will respond with a list of tickers.
Respond Content
The API will respond with a ticker object or a list of ticker objects, depending on how you set the symbol parameter.

Each ticker object contains the following fields:

Field	Type	Description
symbol	String	
open	String	the traded price 24 hour ago
close	String	the last traded price
high	String	the highest price over the past 24 hours
low	String	the lowest price over the past 24 hours
volume	String	the total traded volume in quote asset over the paste 24 hours
ask	[String, String]	the price and size at the current best ask level
bid	[String, String]	the price and size at the current best bid level
Code Sample
Please refer to python code to [query ticker info]{https://github.com/ascendex/ascendex-pro-api-demo/blob/main/python/query_pub_ticker.py}

Authenticate a RESTful Request
Create Request
To access private data via RESTful APIs, you must include the following headers:

x-auth-key - required, the api key as a string.
x-auth-timestamp - required, the UTC timestamp in milliseconds of your request
x-auth-signature - required, the request signature (see Sign a Request)
The timestamp in the header will be checked against server time. If the difference is greater than 30 seconds, the request will be rejected.

Sign a Request
Signing a RESTful Request

# bash 
APIPATH=info
APIKEY=CEcrjGyipqt0OflgdQQSRGdrDXdDUY2x
SECRET=hV8FgjyJtpvVeAcMAgzgAFQCN36wmbWuN7o3WPcYcYhFd8qvE43gzFGVsFcCqMNk
TIMESTAMP=`date +%s%N | cut -c -13` # 1608133910000
MESSAGE=$TIMESTAMP+$APIPATH
SIGNATURE=`echo -n $MESSAGE | openssl dgst -sha256 -hmac $SECRET -binary | base64`
echo $SIGNATURE  # /pwaAgWZQ1Xd/J4yZ4ReHSPQxd3ORP/YR8TvAttqqYM=

curl -X GET -i \
  -H "Accept: application/json" \
  -H "Content-Type: application/json" \
  -H "x-auth-key: $APIKEY" \
  -H "x-auth-signature: $SIGNATURE" \
  -H "x-auth-timestamp: $TIMESTAMP" \
  https://ascendex.com/api/pro/v1/info
To query APIs with private data, you must include a signature using base64 encoded HMAC sha256 algorithm. The prehash string is <timestamp>+<api-path>. The timestamp is the UTC timestamp in milliseconds. The api-path is provided in each API description.

See the code demos in (bash/python/java) on the right.

WebSocket
How to Connect
Base endpoints:

Testnet:

Public endpoint: wss://api-test.ascendex-sandbox.com:443/api/pro/v2/stream
Private endpoint: wss://api-test.ascendex-sandbox.com:443/<grp>/api/pro/v2/stream
Mainnet:

Public endpoint: wss://ascendex.com:443/api/pro/v2/stream
Private endpoint: wss://ascendex.com:443/<grp>/api/pro/v2/stream You can only authenticate a WebSocket session via a private endpoint.
WebSocket Authentication
You must authenticate the websocket session in order to recieve private data and send account specific requests (e.g. placing new orders).

You have two options to authenticate a websocket session.

by adding authentication data in the request header when connecting to websocket.
by sending an op:auth message to the server after you have connected to websocket.
Once you successfully connect to the websocket, you will receive a connected message:

for authenticated websocket session: {"m":"connected","type":"auth"}
for unauthenticated websocket session: {"m":"connected","type":"unauth"}
If the session is disconnected for some reason, you will receive a disconnected message:

{"m":"disconnected","code":100005,"reason":"INVALID_WS_REQUEST_DATA","info":"Session is disconnected due to missing pong message from the client"}
Method 1 - WebSocket Authentication with Request Headers

Authenticate with Headers

# # Install wscat from Node.js if you haven't
# npm install -g wscat  

APIPATH=v2/stream
APIKEY=BclE7dBGbS1AP3VnOuq6s8fJH0fWbH7r
SECRET=fAZcQRUMxj3eX3DreIjFcPiJ9UR3ZTdgIw8mxddvtcDxLoXvdbXJuFQYadUUsF7q
TIMESTAMP=`date +%s%N | cut -c -13`
MESSAGE=$TIMESTAMP+$APIPATH
SIGNATURE=`echo -n $MESSAGE | openssl dgst -sha256 -hmac $SECRET -binary | base64`

wscat -H "x-auth-key: $APIKEY" \
  -H "x-auth-signature: $SIGNATURE" \
  -H "x-auth-timestamp: $TIMESTAMP" \
  -c wss://api-test.ascendex-sandbox.com:443/api/pro/v2/stream -w 1 -x '{"op":"sub", "id": "abc123", "ch": "order:cshQtyfq8XLAA9kcf19h8bXHbAwwoqDo:ASD/USDT"}'
This is similar to the way you authenticate any RESTful request. You need to add the following header fields to the connection request:

x-auth-key
x-auth-timestamp
x-auth-signature
The server will then check if the data is correctly signed before upgrading the connection protocol to WebSocket.

Note that if you specify these header fields, the server will reject the websocket connection request if authentication fails.

Method 2 - WebSocket Authentication by Sending the Auth Message

Authenticate by Sending the auth Message

# # Install wscat from Node.js if you haven't
# npm install -g wscat  

APIPATH=v2/stream
APIKEY=BclE7dBGbS1AP3VnOuq6s8fJH0fWbH7r
SECRET=fAZcQRUMxj3eX3DreIjFcPiJ9UR3ZTdgIw8mxddvtcDxLoXvdbXJuFQYadUUsF7q
TIMESTAMP=`date +%s%N | cut -c -13`
MESSAGE=$TIMESTAMP+$APIPATH
SIGNATURE=`echo -n $MESSAGE | openssl dgst -sha256 -hmac $SECRET -binary | base64`

wscat -c wss://api-test.ascendex-sandbox.com:443/1/api/pro/v2/stream -w 1 -x "{\"op\":\"auth\", \"id\": \"abc123\", \"t\": $TIMESTAMP, "key": \"$APIKEY\", \"sig\": \"$SIGNATURE\"}"
You can also authenticate a live websocket session by sending an op:auth message to the server.

Name	Type	Required	Description
op	String	Yes	"auth"
id	String	No	optional id field, you may safely skip it
t	Long	Yes	UTC timestamp in milliseconds, use this timestamp to generate signature
key	String	Yes	your api key
sig	String	Yes	the signature is generated by signing "<timestamp>+v2/stream"
More comprehensive examples can be found at:

Python demo for websocket auth
Authentication Response

Auth success message

{  
  "m": "auth",
  "id": "abc123",
  "code": 0
}
Auth error message

{
  "m":"auth",
  "id": "abc123",
  "code": 200006,
  "err": "Unable to find User Account Data"
}
You will receive a message for authentication result after you send authentication request.

Field	Type	Description
m	String	"auth"
id	String	echo back the id if you provide one in the request
code	Long	Any code other than 0 indicate an error in authentication
err	Optional[String]	Provide detailed error message if code is not 0
Keep the Connection Alive
In order to keep the websocket connection alive, you have two options, detailed below.

Method 1: Responding to Server's ping messages
Method 1. keep the connection alive by responding to Server pushed ping message

<<< { "m": "ping", "hp": 3 }  # Server pushed ping message
>>> { "op": "pong" }   # Client responds with pong
If the server doesn't receive any client message after a while, it will send a ping message to the client. Once the ping message is received, the client should promptly send a pong message to the server. If you missed two consecutive ping messages, the session will be disconnected.

Server Ping Message Schema

Name	Type	Description
op	String	ping
hp	Int	health point: when this value decreases to 0, the session will be disconnected.
Method 2: Sending ping messages to Server
Method 2. keep the connection alive by sending ping message to the server

>>> { "op": "ping" }                                    # Client initiated ping message (every 30 seconds)
<<< { "m":"pong", "code":0, "ts":1614164189, "hp": 2 }  # Server responds to client ping 
You can also send ping message to the server every 15 seconds to keep the connection alive. The server will stop sending ping message for 30 seconds if a client initiated ping message is received.

Server Pong Message Schema

Name	Type	Description
m	String	pong
code	Int	error code, for the pong mesage, the error code is always 0 (success)
ts	Long	server time in UTC miliseconds
hp	Int	health point: when this value decreases to 0, the session will be disconnected.
Public Stream Data
Channel: Futures Pricing Data
Sample Futures Pricing Data Message

{
    "m": "futures-pricing-data",
    "con": [  // contracts
        {
            "s" : "BTC-PERP",        // symbol
            "t" : 1614814705716,     // data time
            "ip": "50702.8",         // index price
            "mp": "50652.3553",      // mark price
            "r" : "0.000565699",     // funding rate 
            "oi": "90.7367",         // open interest
            "f" : 1614816000000      // next funding time
        }
    ], 
    "col": [  // collateral assets
        {
            "a": "USDTR",  // asset
            "p": "1"       // reference price (quote in USDT)
        },
        {
            "a": "USDC",
            "p": "0.99935"
        },
        {
            "a": "ETH",
            "p": "1582.505"
        },
        {
            "a": "PAX",
            "p": "0.9964"
        },
        {
            "a": "BTC",
            "p": "50621.795"
        },
        {
            "a": "USDT",
            "p": "1"
        }
    ]
}
Subscribe to the Channel

{"op":"sub", "id":"sample-id", "ch":"futures-pricing-data"}

Channel: Level 1 Order Book Data (BBO)
Subscribe to BTC-PERP quote stream

{ "op": "sub", "id": "abc123", "ch":"bbo:BTC-PERP" }
Unsubscribe to BTC-PERP quote stream

{ "op": "unsub", "id": "abc123", "ch":"bbo:BTC-PERP" }
BBO Message

{
    "m": "bbo",
    "symbol": "BTC-PERP",
    "data": {
        "ts": 1573068442532,
        "bid": [
            "9309.11",
            "0.0197172"
        ],
        "ask": [
            "9309.12",
            "0.8851266"
        ]
    }
}
You can subscribe to updates of best bid/offer data stream only. Once subscribed, you will receive BBO message whenever the price and/or size changes at the top of the order book.

Each BBO message contains price and size data for exactly one bid level and one ask level.

Channel: Level 2 Order Book Updates
Subscribe to BTC-PERP depth updates stream

{ "op": "sub", "id": "abc123", "ch":"depth:BTC-PERP" }
Unsubscribe to BTC-PERP depth updates stream

{ "op": "unsub", "id": "abc123", "ch":"depth:BTC-PERP" }
The Depth Message

{
    "m": "depth",
    "symbol": "BTC-PERP",
    "data": {
        "ts": 1573069021376,
        "seqnum": 2097965,
        "asks": [
            [
                "0.06844",
                "10760"
            ]
        ],
        "bids": [
            [
                "0.06777",
                "562.4"
            ],
            [
                "0.05",
                "221760.6"
            ]
        ]
    }
}
If you want to keep track of the most recent order book snapshot in its entirety, the most efficient way is to subscribe to the depth channel.

Each depth message contains a bids list and an asks list in its data field. Each list contains a series of [price, size] pairs that you can use to update the order book snapshot. In the message, price is always positive and size is always non-negative.

if size is positive and the price doesn't exist in the current order book, you should add a new level [price, size].
if size is positive and the price exists in the current order book, you should update the existing level to [price, size].
if size is zero, you should delete the level at price.
See Orderbook Snapshot for code examples.

Channel: Market Trades
Subscribe to BTC-PERP market trades stream

{ "op": "sub", "id": "abc123", "ch":"trades:BTC-PERP" }
Unsubscribe to BTC-PERP market trades stream

{ "op": "unsub", "id": "abc123", "ch":"trades:BTC-PERP" }
Trade Message

{
    "m": "trades",
    "symbol": "BTC-PERP",
    "data": [
        {
            "p":      "0.068600",
            "q":      "100.000",
            "ts":      1573069903254,
            "bm":      false,
            "seqnum":  144115188077966308
        }
    ]
}
The data field is a list containing one or more trade objects. The server may combine consecutive trades with the same price and bm value into one aggregated item. Each trade object contains the following fields:

Name	Type	Description
seqnum	Long	the sequence number of the trade record. seqnum is always increasing for each symbol, but may not be consecutive
p	String	the executed price expressed as a string
q	String	the aggregated traded amount expressed as string
ts	Long	the UTC timestamp in milliseconds of the first trade
bm	Boolean	if true, the buyer of the trade is the maker.
Channel: Bar Data
Subscribe to BTC-PERP 1 minute bar stream

{ "op": "sub", "id": "abc123", "ch":"bar:1:BTC-PERP" }
Unsubscribe to BTC-PERP 1 minute bar stream

{ "op": "unsub", "id": "abc123", "ch":"bar:1:BTC-PERP" }

//  Alternatively, you can unsubscribe all bar streams for BTC-PERP
{ "op": "unsub", "id": "abc123", "ch":"bar:*:BTC-PERP" }

// Or unsubscribe all 1 minute bar stream
{ "op": "unsub", "id": "abc123", "ch":"bar:1" }

// Or unsubscribe all bar stream
{ "op": "unsub", "id": "abc123", "ch":"bar" }
Bar Data Message

{
    "m": "bar",
    "s": "BTC-PERP",    
    "data": {
        "i":  "1",
        "ts": 1575398940000,
        "o":  "0.04993",
        "c":  "0.04970",
        "h":  "0.04993",
        "l":  "0.04970",
        "v":  "8052"
    }
}
The data field is a list containing one or more trade objects. The server may combine consecutive trades with the same price and bm value into one aggregated item. Each trade object contains the following fields:

Name	Type	Description
seqnum	Long	the sequence number of the trade record. seqnum is always increasing for each symbol, but may not be consecutive
p	String	the executed price expressed as a string
q	String	the aggregated traded amount expressed as string
ts	Long	the UTC timestamp in milliseconds of the first trade
bm	Boolean	if true, the buyer of the trade is the maker.
Private Stream Data
Channel: Order
{
  "m"      : "futures-order",
  "sn"     : 127,                   // sequence number
  "e"      : "ExecutionReport",     // event
  "a"      : "sample-futures-account-id",  // account Id
  "ac"     : "FUTURES",             // account category 
  "t"      : 1606335352348,         // last execution time
  "ct"     : 1606335351541,         // order creation time
  "orderId": "a176010c4957U68469127074abcd1234",  // order Id
  "sd"     : "Buy",                 // side 
  "ot"     : "Limit",               // order type 
  "q"      : "0.1",                 // order quantity (base asset)
  "p"      : "18000",               // order price
  "sp"     : "0",                   // stop price
  "spb"    : "",                    // stop trigger
  "s"      : "BTC-PERP",            // symbol 
  "st"     : "New",                 // order status
  "lp"     : "0",                   // last filled price
  "lq"     : "0",                   // last filled quantity (base asset)
  "ap"     : "0",                   // average filled price
  "cfq"    : "0",                   // cummulative filled quantity (base asset)
  "f"      : "0",                   // commission fee of the current execution
  "cf"     : "0",                   // cumulative commission fee
  "fa"     : "USDT",                // fee asset
  "ei"     : "NULL_VAL",            // execution instruction
  "err"    : ""                     // error message
}
Subscribe to the Channel

{"op":"sub", "id":"sample-id", "ch":"futures-order"}

Channel: Account Update


{
  "m"     : "futures-account-update",            // message
  "e"     : "ExecutionReport",                   // event type
  "t"     : 1612508562129,                       // server time (UTC time in milliseconds)
  "acc"   : "sample-futures-account-id",         // account ID
  "at"    : "FUTURES",                           // account type
  "sn"    : 23128,                               // sequence number, strictly increasing for each account
  "id"    : "r177710001cbU3813942147C5kbFGOan",  // request ID for this account update
  "col": [
    {
      "a": "USDT",               // asset code
      "b": "1000000",            // balance 
      "f": "1"                   // discount factor
    }
  ],
  "pos": [
    {
      "s"   : "BTC-PERP",        // symbol
      "sd"  : "LONG",            // side
      "pos" : "0.011",           // position
      "rc"  : "-385.840455",     // reference cost
      "up"  : "18.436008668",    // unrealized pnl
      "rp"  : "0",               // realized pnl
      "aop" : "35041.363636363", // Average Opening Price
      "boon": "0",               // Buy Open Order Notional
      "soon": "0",               // Sell Open Order Notional
      "mt"  : "crossed",         // margin type: isolated / cross
      "iw"  : "0",               // isolated margin
      "lev" : "10",              // leverage
      "tp"  : "0",               // take profit price (by position exit order)
      "tpt" : "market",          // take profit trigger (by position exit order)
      "sl"  : "0",               // stop loss price (by position exit order)
      "slt" : "market",          // stop loss trigger (by position exit order)
    }
  ]
}
Subscribe to the Channel

{"op":"sub", "id":"sample-id", "ch":"futures-account-update"}

WebSocket - Data Request
WS: Account Snapshot
Requesting Futures Account Snapshot

{
   "op"    : "req",
   "id"    : "abc123456",
   "action": "futures-account-snapshot"
}
Futures Account Snapshot response

{
   "m"  : "futures-account-snapshot",  // message
   "id" : "abc123456",                 // echo back the request Id
   "e"  : "ClientRequest",             // event name
   "t"  : 1613748277356,               // server time in milliseconds (UTC)
   "acc": "futH9N59hR0BMVEjHnBleHLn0mfUl5lo",  // accountId
   "ac" : "FUTURES",                   // account category
   "sn" : 9982,                        // sequence number
   "col":[  // collateral balances
      {
         "a": "ETH",     // collateral asset code
         "b": "500",     // collateral balance
         "f": "0.95"     // discount factor
      },
      {
         "a": "BTC",
         "b": "100",
         "f": "0.98"
      },
      {
         "a": "USDT",
         "b": "1000000",
         "f": "1"
      }
   ],
   "pos":[  // contract positions
      {
         "s"   : "BTC-PERP",  // contract symbol
         "sd"  : "NULL_VAL",  // side: LONG / SHORT / NULL_VAL
         "pos" : "0",         // position
         "rc"  : "0",         // reference cost
         "up"  : "0",         // unrealized pnl
         "rp"  : "0",         // realized pnl
         "aop" : "0",         // average opening price
         "mt"  : "crossed",   // margin type: isolated / cross
         "boon": "0",         // buy open order notional
         "soon": "0",         // sell open order notional
         "lev" : "10",        // leverage
         "iw"  : "0",         // isolated margin
         "tp"  : "0",         // take profit price (by position exit order)
         "tpt" : "market",    // take profit trigger (by position exit order)
         "sl"  : "0",         // stop loss price (by position exit order)
         "slt" : "market"     // stop loss trigger (by position exit order)
      }
   ]
}
You can request the futures account snapshot via websocket by a futures-account-snapshot action.

The request schema:

Name	Data Type	Description
op	String	req
action	String	futures-account-snapshot
id	String	for result match purpose
WS: Place Order
Request to place new order

{
   "op"    : "req",
   "action": "place-order",
   "ac"    : "futures",         // the Account Category
   "id"    : "sampleRequestID", // the server will echo back this id in the ack message. 
   "args":{
      "time"      : 1613753879921,
      "symbol"    : "BTC-PERP",
      "price"     : "30000",
      "orderQty"  : "0.12",
      "orderType" : "limit",
      "side"      : "buy",
      "postOnly"  : false,
      "respInst"  : "ACK"
   }
}
Successful ACK message

{
   "m"     : "order",
   "code"  : 0,
   "id"    : "sampleRequestID",   // echo back the original request Id
   "action": "place-order",
   "ac"    : "FUTURES",
   "info": {
      "orderId": "s177bbb671b7U1234567890leOrderId",
      "symbol" : "BTC-PERP"
   }
}
Error response message

{
   "m"     : "order",
   "code"  : 300001,
   "id"    : "sampleRequestID",  // echo back the original request Id
   "action": "place-order",
   "ac"    : "FUTURES",
   "info": {
      "symbol"  : "BTC-PERP",
      "reason"  : "INVALID_PRICE",
      "errorMsg": "Order price is too low from market price."
   }
}
Place order via websocket

Request

Make new order request follow the general websocket request rule, with proper place new order parameters as specified in rest api for args field.

see placing order via RESTful API.

id

As described in Generate Order Id, the server uses a deterministic algorithm to compute the orderId based on client inputs. For every order request placed via WebSocket, We strongly recommend you put a non-repeatable id.

Response

Respond with m field as order, and action field as place-order; if you provide id in your request, it will be echoed back as id to help you identify; code field to indicate if this is a successful zero or failed non-zero.

code=0

With code field as zero to indicate this new order request pass some basic sanity check, and has been sent to matching engine.

info field provide some detail: if you provide id in your request, it will be echoed back as id to help you identify; we also provide server side generated orderId, which is the id you should use for future track or action on the order.

code=non-zero

With code field as non-zero to indicate there is some obvisous errors in your request.

info field provide some detail: we also provide error reason and errorMsg detail.

WS: Cancel Order
Request to cancel existing open order

{
   "op"    : "req",
   "action": "cancel-order",
   "ac"    : "futures",
   "id"    : "sampleRequestId",    // server will echo back this Id.
   "args":{
      "time":1613744943323,
      "orderId":"s177bab1b474U5051470287bbtcpKiOR",
      "symbol":"BTC-PERP"
   }
}
Successful ACK message

{
   "m"     : "order",
   "action": "cancel-order",
   "ac"    : "FUTURES",
   "id"    : "sampleRequestId", // echo back the original request Id
   "code":0,
   "info":{
      "orderId": "s177bab1b474U5051470287bbtcpKiOR",
      "symbol" : "BTC-PERP"
   }
}
Error response message

{
   "m"     : "order",
   "action": "cancel-order",
   "ac"    : "FUTURES",
   "code"  : 300006,
   "id"    : "sampleRequestId", // echo back the original request Id
   "info":{
      "symbol"  : "BTC-PERP",
      "reason"  : "INVALID_ORDER_ID",
      "errorMsg": "Client Order Id too Long: s177bab1b474U5051470287bbtcpKiOR1"
   }
}
Cancel an existing open order via websocket

Request

Make order cancelling request follow the general websocket request rule by setting action to be cancel-orde, with proper cancel order parameters as specified in rest api for args field.

Response

Respond with m field as order, and action field as cancel-order; code field to indicate if this is a successful zero or failed non-zero.

code=0

With code field as zero to indicate this cancel order request pass some basic sanity check, and has been sent to matching engine.

info field provide some detail: if you provide symbol in your request, it will be echoed back as symbol to help you idintify; we also echo back target orderId to be cancelled.

code=non-zero

With code field as non-zero to indicate there is some obvisous errors in your cancel order request.

info field provide some detail: we also provide error reason and errorMsg detail.

WS: Cancel All Orders
Request to cancel all existing open orders

{
   "op"    : "req",
   "action": "cancel-all",
   "ac"    : "futures",
   "id"    : "sampleRequestId", // server will echo back this Id.
   "args": {   // you can also omit the args field
   }
}
Request to cancel existing open order related to symbol "BTC-PERP"

{
   "op"    : "req",
   "action": "cancel-all",
   "ac"    : "futures",
   "id"    : "sampleRequestId", // server will echo back this Id.
   "args":{ 
        "symbol": "BTC-PERP"     
   }
}
Successful ACK message

{
   "m"     : "order",
   "code"  : 0,
   "action": "cancel-all",
   "ac"    : "FUTURES",
   "id"    : "sampleRequestId", // echo back the original request Id
   "info":{
      "symbol":""
   }
}
Error response message

{
   "m"     : "order",
   "code"  : 300012,
   "action": "cancel-all",
   "ac"    : "FUTURES",
   "id"    : "sampleRequestId", // echo back the original request Id
   "info":{
      "symbol"  : "",
      "reason"  : "INVALID_PRODUCT",
      "errorMsg": "Invalid Product Symbol"
   }
}
Cancel all open orders on account level via websocket with optional symbol.

Request

Make general websocket request with action field as cancel-All and set proper ac value(futures), and provide symbol value in args.

Response

With code field as zero to indicate this cancel all order request has been received by server and sent to matching engine.

info field provide some detail: if you provide symbol in your request to cancel orders.

With code field as non-zero to indicate there is some obvisous errors in your request.

info field provide some detail: we also provide error reason and errorMsg detail.

WS: Query Open Orders
Requesting open orders on symbol BTC-PERP

{
   "op"    : "req",
   "id"    : "abc123456",
   "action": "futures-open-orders",
   "args":{
      "symbol":"BTC-PERP"
   }
}
Open orders response

{
   "m":"futures-open-orders",
   "code":0,
   "id":"abc123456",
   "ac":"FUTURES",
   "data":[
      {
         "ac":"FUTURES",
         "accountId":"sample-futures-account-id",
         "time":1615696544843,
         "orderId":"r1782f04c58aU3792951278sbtcp7EbA",
         "seqNum":13,
         "orderType":"Limit",
         "execInst":"NULL_VAL",
         "side":"Sell",
         "symbol":"BTC-PERP",
         "price"     :"66000",
         "orderQty":"0.0001",
         "stopPrice":"0",
         "stopBy":"market",
         "status":"New",
         "lastExecTime":1615696544851,
         "lastQty":"0",
         "lastPx":"0",
         "avgFilledPx":"0",
         "cumFilledQty":"0",
         "fee":"0",
         "cumFee":"0",
         "feeAsset":"USDT",
         "errorCode":"",
         "posStopLossPrice":"0",
         "posStopLossTrigger":"None",
         "posTakeProfitPrice":"0",
         "posTakeProfitTrigger":"None"
      },
      ...
   ]
}
Error response message

{
   "m":"error",
   "id":"abc123456",
   "code":100005,
   "reason":"INVALID_WS_REQUEST_DATA",
   "info":"Missing required parameter: args"
}
You can request the open order via websocket by a futures-open-orders action.

The request schema:

Name	Data Type	Description
op	String	req
action	String	futures-open-orders
id	String	for result match purpose
args:symbol	Optional[String]	add the (optional) symbol filter, see below for details.
The symbol key in the args map allows you to customize the symbol filter in a flexible way:

to query open orders of the a specific symbol, set symbol to a valid symbol code. For instance, {"symbol": "BTC-PERP"}
to query all open orders, you may simply omit the symbol key ({}).
Appendix
ENUM Definitions
Account Category (ac)
CASH
MARGIN
FUTURES
Order Type (orderType)
Limit
Market
StopLimit
StopMarket
Side (side)
Buy
Sell
Response Type (respInst)
ACK
ACCEPT
DONE
Time in Force (timeInForce)
GTC - good till cancelled
IOC - immediate or cancel
FOK - fill or kill
Execution Instruction (execInst)
Post
Liquidation
InternalPost
StopOnMarket
StopOnMark
StopOnRef
ReduceOnly
PostReduceOnly
PostStopMarket
PostStopMark
PostStopRef
ReduceOnlyMarket
ReduceOnlyMark
ReduceOnlyRef
PostReduceMarket
PostReduceMark
PostReduceRef
OpenStopMkt
OpenStopMark
OpenStopRef
OpenPostStopMkt
OpenPostStopMark
OpenPostStopRef
PosStopMkt
PosStopMark
PosStopRef
Order Status (status)
New
PartiallyFilled
Filled
Canceled
Rejected
PendingNew - a conditional order (stop limit / stop market) that hasn't been triggered yet.
Margin Type (marginType)
crossed
isolated
WebSocket Operations (op)
auth
WebSocket Message Types (m)
auth
sub
unsub
bbo
futures-pricing-data-batch
futures-order
futures-account-update













