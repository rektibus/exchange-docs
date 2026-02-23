Introduction
Zoomex V3 Open API allow users to select different collections to build their API model.

Copy Trade: You must be Master Trader to use this API.
Authentication
info
Please visit Zoomex's testnet or mainnet to generate an API key

info
The authentication of the v1 interface is different from v3. Please pay attention to using the corresponding signature method when calling, and refer to the call demo of each API for the corresponding method.

REST API Base Endpoint:

Testnet:
https://openapi-testnet.zoomex.com
Mainnet:
https://openapi.zoomex.com
caution
All requests made to private endpoints MUST be authenticated.
Requests made to public endpoints DO NOT require additional authentication.
Parameters for Authenticated Endpoints
The following parameters must be used for authentication:

api_key - api key
timestamp - UTC timestamp in milliseconds
sign - a signature derived from the request's parameters
We also provide recv_window (unit in millisecond and default value is 5,000) to specify how long an HTTP request is valid. It is also used to prevent replay attacks.

A smaller recv_window is more secure, but your request may fail if the transmission time is greater than your recv_window.

caution
Please make sure that the timestamp parameter adheres to the following rule:
server_time - recv_window <= timestamp < server_time + 1000
server_time stands for Zoomex server time, which can be queried via the Server Time endpoint.

Create A Request
tip
To assist in diagnosing advanced network problems, you may consider adding cdn-request-id to your request headers. Its value should be unique for each request.

Basic steps:

timestamp + API key + (recv_window) + (queryString | jsonBodyString)

Use the HMAC_SHA256 or RSA_SHA256 algorithm to sign the string in step 1, and convert it to a hex string (HMAC_SHA256) / base64 (RSA_SHA256) to obtain the sign parameter.

Append the sign parameter to request header, and send the HTTP request. Note: the plain text for GET and POST requests is different. Please refer to blew examples.

Demo

import requests
import time
import hashlib
import hmac
import uuid

api_key='XXXXXXXX'
secret_key='XXXXXXXX'
httpClient=requests.Session()
recv_window=str(5000)
url="https://openapi-testnet.zoomex.com"

def HTTP_Request(endPoint,method,payload,Info):
   global time_stamp
   time_stamp=str(int(time.time() * 10 ** 3))
   signature=genSignature(payload)
   headers = {
       'X-BAPI-API-KEY': api_key,
       'X-BAPI-SIGN': signature,
       'X-BAPI-SIGN-TYPE': '2',
       'X-BAPI-TIMESTAMP': time_stamp,
       'X-BAPI-RECV-WINDOW': recv_window,
       'Content-Type': 'application/json'
   }
   if(method=="POST"):
       response = httpClient.request(method, url+endPoint, headers=headers, data=payload)
   else:
       response = httpClient.request(method, url+endPoint+"?"+payload, headers=headers)
   print(response.text)
   print(Info + " Elapsed Time : " + str(response.elapsed))
def genSignature(payload):
   param_str= time_stamp+ api_key + recv_window + payload
   hash = hmac.new(bytes(secret_key, "utf-8"), param_str.encode("utf-8"),hashlib.sha256)
   signature = hash.hexdigest()
   return signature

#POST Create Order
endpoint="/cloud/trade/v3/order/create"
method="POST"
orderLinkId=uuid.uuid4().hex
params='{"category":"linear","symbol": "BTCUSDT","side": "Buy","positionIdx": 0,"orderType": "Market","qty": "0.001","price": "","timeInForce": "GTC","orderLinkId": "' + orderLinkId + '"}'
HTTP_Request(endpoint,method,params,"Create")

#GET history Orders
endpoint="/cloud/trade/v3/order/history"
method="GET"
params='category=linear&symbol=BTCUSDT'
HTTP_Request(endpoint,method,params,"history")


Common response parameters
Parameter	Type	Comments
retCode	number	Success/Error code
retMsg	string	Success/Error msg. Can be OK,success,Success for Success message
result	Object	Business data result
retExtInfo	Object	Extend info. Most of time, it is {}
time	number	Current timestamp (ms)
{
    "retCode": 0,
    "retMsg": "success",
    "result": {},
    "retExtInfo": {},
    "time": 1690180896378
}

tip
Due to historical reasons, the attributes returned in the list object of the result object in the response body of the [Get Open Orders(real-time)] (./order/open order/#) start with uppercase letters. Please be careful when docking!



Get Zoomex Server Time
HTTP Request
GET /cloud/trade/v3/market/time

Request Parameters
None

Response Parameters
Parameter	Type	Comments
timeSecond	string	Zoomex server timestamp (sec)
timeNano	string	Zoomex server timestamp (nano)
Request Example
GET /cloud/trade/v3/market/time HTTP/1.1
Host: openapi.zoomex.com

Response Example
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "timeSecond": "1688639403",
        "timeNano": "1688639403423213947"
    },
    "retExtInfo": {},
    "time": 1688639403423
}



Get Kline
Query for historical klines (also known as candles/candlesticks). Charts are returned in groups based on the requested interval.

Covers: Spot / USDT perpetual / Inverse contract

HTTP Request
GET /cloud/trade/v3/market/kline

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type. spot,linear,inverse
symbol	true	string	Symbol name
interval	true	string	Kline interval. 1,3,5,15,30,60,120,240,360,720,D,M,W
start	false	integer	The start timestamp (ms)
end	false	integer	The end timestamp (ms)
limit	false	integer	Limit for data size per page. [1, 1000]. Default: 200
Response Parameters
Parameter	Type	Comments
category	string	Product type
symbol	string	Symbol name
list	array	
An string array of individual candle
Sort in reverse by startTime
> list[0]: startTime	string	Start time of the candle (ms)
> list[1]: openPrice	string	Open price
> list[2]: highPrice	string	Highest price
> list[3]: lowPrice	string	Lowest price
> list[4]: closePrice	string	Close price. Is the last traded price when the candle is not closed
> list[5]: volume	string	Trade volume. Unit of contract: pieces of contract.
> list[6]: turnover	string	Turnover. Unit of figure: quantity of quota coin
Request Example
GET /cloud/trade/v3/market/kline?category=inverse&symbol=BTCUSD&interval=60&start=1670601600000&end=1670608800000 HTTP/1.1
Host: openapi-testnet.zoomex.com


Response Example
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "symbol": "BTCUSD",
        "category": "inverse",
        "list": [
            [
                "1670608800000",
                "17071",
                "17073",
                "17027",
                "17055.5",
                "268611",
                "15.74462667"
            ],
            [
                "1670605200000",
                "17071.5",
                "17071.5",
                "17061",
                "17071",
                "4177",
                "0.24469757"
            ],
            [
                "1670601600000",
                "17086.5",
                "17088",
                "16978",
                "17071.5",
                "6356",
                "0.37288112"
            ]
        ]
    },
    "retExtInfo": {},
    "time": 1672025956592
}



Get Mark Price Kline
Query for historical mark price klines. Charts are returned in groups based on the requested interval.

Covers: USDT perpetual / Inverse contract

HTTP Request
GET /cloud/trade/v3/market/mark-price-kline

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type. linear,inverse
symbol	true	string	Symbol name
interval	true	string	Kline interval. 1,3,5,15,30,60,120,240,360,720,D,M,W
start	false	integer	The start timestamp (ms)
end	false	integer	The end timestamp (ms)
limit	false	integer	Limit for data size per page. [1, 1000]. Default: 200
Response Parameters
Parameter	Type	Comments
category	string	Product type
symbol	string	Symbol name
list	array	
An string array of individual candle
Sort in reverse by startTime
> list[0]: startTime	string	Start time of the candle (ms)
> list[1]: openPrice	string	Open price
> list[2]: highPrice	string	Highest price
> list[3]: lowPrice	string	Lowest price
> list[4]: closePrice	string	Close price. Is the last traded price when the candle is not closed
Request Example
GET /cloud/trade/v3/market/mark-price-kline?category=linear&symbol=BTCUSDT&interval=15&start=1670601600000&end=1670608800000&limit=1 HTTP/1.1
Host: openapi-testnet.zoomex.com


Response Example
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "symbol": "BTCUSDT",
        "category": "linear",
        "list": [
            [
            "1670608800000",
            "17164.16",
            "17164.16",
            "17121.5",
            "17131.64"
            ]
        ]
    },
    "retExtInfo": {},
    "time": 1672026361839
}


Get Index Price Kline
Query for historical index price klines. Charts are returned in groups based on the requested interval.

Covers: USDT perpetual / Inverse contract

HTTP Request
GET /cloud/trade/v3/market/index-price-kline

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type. linear,inverse
symbol	true	string	Symbol name
interval	true	string	Kline interval. 1,3,5,15,30,60,120,240,360,720,D,M,W
start	false	integer	The start timestamp (ms)
end	false	integer	The end timestamp (ms)
limit	false	integer	Limit for data size per page. [1, 1000]. Default: 200
Response Parameters
Parameter	Type	Comments
category	string	Product type
symbol	string	Symbol name
list	array	
An string array of individual candle
Sort in reverse by startTime
> list[0]: startTime	string	Start time of the candle (ms)
> list[1]: openPrice	string	Open price
> list[2]: highPrice	string	Highest price
> list[3]: lowPrice	string	Lowest price
> list[4]: closePrice	string	Close price. Is the last traded price when the candle is not closed
Request Example
GET /cloud/trade/v3/market/index-price-kline?category=inverse&symbol=BTCUSDT&interval=1&start=1670601600000&end=1670608800000&limit=2 HTTP/1.1
Host: openapi-testnet.zoomex.com


Response Example
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "symbol": "BTCUSDT",
        "category": "linear",
        "list": [
            [
                "1670608800000",
                "17167.00",
                "17167.00",
                "17161.90",
                "17163.07"
            ],
            [
                "1670608740000",
                "17166.54",
                "17167.69",
                "17165.42",
                "17167.00"
            ]
        ]
    },
    "retExtInfo": {},
    "time": 1672026471128
}



Get Premium Index Price Kline
Query for historical premium index klines. Charts are returned in groups based on the requested interval.

Covers: USDT perpetual and Inverse contract

HTTP Request
GET /cloud/trade/v3/market/premium-index-price-kline

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type. linear
symbol	true	string	Symbol name
interval	true	string	Kline interval
start	false	integer	The start timestamp (ms)
end	false	integer	The end timestamp (ms)
limit	false	integer	Limit for data size per page. [1, 1000]. Default: 200
Response Parameters
Parameter	Type	Comments
category	string	Product type
symbol	string	Symbol name
list	array	
An string array of individual candle
Sort in reverse by start
> list[0]	string	Start time of the candle (ms)
> list[1]	string	Open price
> list[2]	string	Highest price
> list[3]	string	Lowest price
> list[4]	string	Close price. Is the last traded price when the candle is not closed
Request Example
GET /cloud/trade/v3/market/premium-index-price-kline?category=linear&symbol=BTCUSDT&interval=D&start=1652112000000&end=1652544000000 HTTP/1.1
Host: openapi-testnet.zoomex.com


Response Example
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "symbol": "BTCUSDT",
        "category": "linear",
        "list": [
            [
                "1652486400000",
                "-0.000587",
                "-0.000344",
                "-0.000480",
                "-0.000344"
            ],
            [
                "1652400000000",
                "-0.000989",
                "-0.000561",
                "-0.000587",
                "-0.000587"
            ]
        ]
    },
    "retExtInfo": {},
    "time": 1672765216291
}


Get Instruments Info
Query for the instrument specification of online trading pairs.

Covers: Spot / USDT perpetual / Inverse contract

caution
When query by baseCoin, regardless of category=linear or inverse, the result will have USDT perpetual and Inverse contract symbols.
HTTP Request
GET /cloud/trade/v3/market/instruments-info

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type. spot,linear,inverse
symbol	false	string	Symbol name
status	false	string	Symbol status filter
linear/inverse has Trading only
baseCoin	false	string	Base coin.
Only valid for linear and inverse
limit	false	integer	Limit for data size per page. [1, 1000]. Default: 500
cursor	false	string	Cursor. Use the nextPageCursor token from the response to retrieve the next page of the result set
Response Parameters
Linear/Inverse
Spot
Parameter	Type	Comments
category	string	Product type
nextPageCursor	string	Cursor. Used to pagination
list	array	Object
> symbol	string	Symbol name
> contractType	string	Contract type
> status	string	Instrument status
> baseCoin	string	Base coin
> quoteCoin	string	Quote coin
> launchTime	string	Launch timestamp (ms)
> priceScale	string	Price scale
> leverageFilter	Object	Leverage attributes
>> minLeverage	string	Minimum leverage
>> maxLeverage	string	Maximum leverage
>> leverageStep	string	The step to increase/reduce leverage
> priceFilter	Object	Price attributes
>> minPrice	string	Minimum order price
>> maxPrice	string	Maximum order price
>> tickSize	string	The step to increase/reduce order price
> lotSizeFilter	Object	Size attributes
>> maxOrderQty	string	Maximum order quantity for a single price limit order
>> maxMktOrderQty	string	Maximum quantity for Market order
>> minOrderQty	string	Minimum order quantity
>> minNotionalValue	string	Minimum order notional Value
>> qtyStep	string	The step to increase/reduce order quantity
>> postOnlyMaxOrderQty	string	Depreciated, please use maxOrderQty
> fundingInterval	integer	Funding interval (minute)
> settleCoin	string	Settle coin
Request Example
Linear
Spot
HTTP
GET /cloud/trade/v3/market/instruments-info?category=linear&symbol=BTCUSDT HTTP/1.1
Host: openapi-testnet.zoomex.com


Response Example
Linear
Spot
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "category": "linear",
        "list": [
            {
                "symbol": "BTCUSDT",
                "contractType": "LinearPerpetual",
                "status": "Trading",
                "baseCoin": "BTC",
                "quoteCoin": "USDT",
                "launchTime": "1585526400000",
                "deliveryTime": "0",
                "deliveryFeeRate": "",
                "priceScale": "2",
                "leverageFilter": {
                    "minLeverage": "1",
                    "maxLeverage": "100.00",
                    "leverageStep": "0.01"
                },
                "priceFilter": {
                    "minPrice": "0.50",
                    "maxPrice": "999999.00",
                    "tickSize": "0.50"
                },
                "lotSizeFilter": {
                    "maxOrderQty": "100.000",
                    "minOrderQty": "0.001",
                    "qtyStep": "0.001",
                    "postOnlyMaxOrderQty": "1000.000"
                    "maxMktOrderQty": "1000.000"
                },
                "unifiedMarginTrade": true,
                "fundingInterval": 480,
                "settleCoin": "USDT"
            }
        ],
        "nextPageCursor": ""
    },
    "retExtInfo": {},
    "time": 1672712495660
}



Get Orderbook
Query for orderbook depth data.

Covers: Spot / USDT perpetual / Inverse contract

future: 500-level of orderbook data
Spot: 200-level of orderbook data
tip
The response is in the snapshot format.

HTTP Request
GET /cloud/trade/v3/market/orderbook

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type. spot, linear, inverse
symbol	true	string	Symbol name
limit	false	integer	Limit size for each bid and ask
spot: [1, 200]. Default: 1.
linear&inverse: [1, 500]. Default: 25.
Response Parameters
Parameter	Type	Comments
s	string	Symbol name
b	array	Bid, buyer. Sort by price desc
> b[0]	string	Bid price
> b[1]	string	Bid size
a	array	Ask, seller. Order by price asc
> a[0]	string	Ask price
> a[1]	string	Ask size
ts	integer	The timestamp (ms) that the system generates the data
u	integer	Update ID, is always in sequence
For future, it is corresponding to u in the wss 500-level orderbook
For spot, it is corresponding to u in the wss 200-level orderbook
Request Example
GET /cloud/trade/v3/market/orderbook?category=linear&symbol=BTCUSDT HTTP/1.1
Host: openapi-testnet.zoomex.com


Response Example
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "s": "BTCUSDT",
        "a": [
            [
                "16638.64",
                "0.008479"
            ]
        ],
        "b": [
            [
                "16638.27",
                "0.305749"
            ]
        ],
        "ts": 1672765737733,
        "u": 5277055
    },
    "retExtInfo": {},
    "time": 1672765737734
}



Get Tickers
Query for the latest price snapshot, best bid/ask price, and trading volume in the last 24 hours.

Covers: Spot / USDT perpetual / Inverse contract

HTTP Request
GET /cloud/trade/v3/market/tickers

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type. spot,linear,inverse
symbol	false	string	Symbol name
Response Parameters
Linear/Inverse
Spot
Parameter	Type	Comments
category	string	Product type
list	array	Object
> symbol	string	Symbol name
> lastPrice	string	Last price
> indexPrice	string	Index price
> markPrice	string	Mark price
> prevPrice24h	string	Market price 24 hours ago
> price24hPcnt	string	Percentage change of market price relative to 24h
> highPrice24h	string	The highest price in the last 24 hours
> lowPrice24h	string	The lowest price in the last 24 hours
> prevPrice1h	string	Market price an hour ago
> openInterest	string	Open interest size in Base
> openInterestValue	string	Open interest value in Quote
> turnover24h	string	Turnover for 24h
> volume24h	string	Volume for 24h
> fundingRate	string	Funding rate
> nextFundingTime	string	Next funding time (ms)
> ask1Size	string	Best ask size
> bid1Price	string	Best bid price
> ask1Price	string	Best ask price
> bid1Size	string	Best bid size
Request Example
GET /cloud/trade/v3/market/tickers?category=linear&symbol=BTCUSD HTTP/1.1
Host: openapi-testnet.zoomex.com


Response Example
Linear
Spot
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
    "category": "inverse",
    "list": [
{
    "symbol": "BTCUSD",
    "lastPrice": "16597.00",
    "indexPrice": "16598.54",
    "markPrice": "16596.00",
    "prevPrice24h": "16464.50",
    "price24hPcnt": "0.008047",
    "highPrice24h": "30912.50",
    "lowPrice24h": "15700.00",
    "prevPrice1h": "16595.50",
    "openInterest": "373504107",
    "openInterestValue": "22505.67",
    "turnover24h": "2352.94950046",
    "volume24h": "49337318",
    "fundingRate": "-0.001034",
    "nextFundingTime": "1672387200000",
    "predictedDeliveryPrice": "",
    "basisRate": "",
    "deliveryFeeRate": "",
    "deliveryTime": "0",
    "ask1Size": "1",
    "bid1Price": "16596.00",
    "ask1Price": "16597.50",
    "bid1Size": "1",
    "basis": ""
}
    ]
},
    "retExtInfo": {},
    "time": 1672376496682
}


Get Funding Rate History
Query for historical funding rates. Each symbol has a different funding interval. For example, if the interval is 8 hours and the current time is UTC 12, then it returns the last funding rate, which settled at UTC 8.

To query the funding rate interval, please refer to the instruments-info endpoint.

Covers: USDT perpetual / Inverse perpetual

tip
Passing only startTime returns an error.
Passing only endTime returns 200 records up till endTime.
Passing neither returns 200 records up till the current time.
HTTP Request
GET /cloud/trade/v3/market/funding/history

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type. linear,inverse
symbol	true	string	Symbol name
startTime	false	integer	The start timestamp (ms)
endTime	false	integer	The end timestamp (ms)
limit	false	integer	Limit for data size per page. [1, 200]. Default: 200
Response Parameters
Parameter	Type	Comments
category	string	Product type
list	array	Object
> symbol	string	Symbol name
> fundingRate	string	Funding rate
> fundingRateTimestamp	string	Funding rate timestamp (ms)
Request Example
GET /cloud/trade/v3/market/funding/history?category=linear&symbol=ETHUSDT&limit=1 HTTP/1.1
Host: openapi-testnet.zoomex.com


Response Example
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "category": "linear",
        "list": [
            {
                "symbol": "ETHUSDT",
                "fundingRate": "0.0001",
                "fundingRateTimestamp": "1672041600000"
            }
        ]
    },
    "retExtInfo": {},
    "time": 1672051897447
}


et Public Trading History
Query recent public trading data in Zoomex.

Covers: Spot / USDT perpetual/ Inverse contract

You can download archived historical trades here:

USDT Perpetual
Inverse Perpetual
HTTP Request
GET /cloud/trade/v3/market/recent-trade

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type. spot,linear,inverse
symbol	false	string	Symbol name
required for spot/linear/inverse
limit	false	integer	Limit for data size per page.
[1,1000], default: 500
Response Parameters
Parameter	Type	Comments
category	string	Products category
list	array	Object
> execId	string	Execution ID
> symbol	string	Symbol name
> price	string	Trade price
> size	string	Trade size
> side	string	Side of taker Buy, Sell
> time	string	Trade time (ms)
Request Example
GET /cloud/trade/v3/market/recent-trade?category=linear&symbol=BTCUSDT&limit=1 HTTP/1.1
Host: openapi-testnet.zoomex.com


Response Example
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "category": "linear",
        "list": [
            {
                "execId": "2100000000007764263",
                "symbol": "BTCUSDT",
                "price": "16618.49",
                "size": "0.00012",
                "side": "Buy",
                "time": "1672052955758"
            }
        ]
    },
    "retExtInfo": {},
    "time": 1672053054358
}


Get Risk Limit
Query for the risk limit.

Covers: USDT perpetual / Inverse contract

HTTP Request
GET /cloud/trade/v3/market/risk-limit

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type. linear,inverse
symbol	false	string	Symbol name
Response Parameters
Parameter	Type	Comments
category	string	Product type
list	array	Object
> id	integer	Risk ID
> symbol	string	Symbol name
> riskLimitValue	string	Position limit
> maintenanceMargin	number	Maintain margin rate
> initialMargin	number	Initial margin rate
> isLowestRisk	integer	1: true, 0: false
> maxLeverage	string	Allowed max leverage
Request Example
GET /cloud/trade/v3/market/risk-limit?category=inverse&symbol=BTCUSD HTTP/1.1
Host: openapi-testnet.zoomex.com


Response Example
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "category": "inverse",
        "list": [
            {
                "id": 1,
                "symbol": "BTCUSD",
                "riskLimitValue": "150",
                "maintenanceMargin": "0.5",
                "initialMargin": "1",
                "isLowestRisk": 1,
                "maxLeverage": "100.00"
            },
        ....
        ]
    },
    "retExtInfo": {},
    "time": 1672054488010
}


Get Pre-upgrade Order History
After the account is upgraded to a Unified account, you can get the orders which occurred before the upgrade.

info
can get all status in 7 days
can only get filled orders beyond 7 days
HTTP Request
GET /cloud/trade/v3/pre-upgrade/order/history

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type
Trading account: linear, inverse, spot
symbol	false	string	Symbol name
orderId	false	string	Order ID
orderLinkId	false	string	User customised order ID
orderFilter	false	string	Order: active order, StopOrder: conditional order
Others: all kinds of orders by default
orderStatus	false	string	
Classic spot: not supported
Others: return all status orders if not passed
startTime	false	integer	The start timestamp (ms)
startTime and endTime must be passed together
If not passed, query the past 7 days data by default
For each request, startTime and endTime interval should be less then 7 days
endTime	false	integer	The end timestamp (ms)
For each request, startTime and endTime interval should be less then 7 days
limit	false	integer	Limit for data size per page. [1, 50]. Default: 20
cursor	false	string	Cursor. Use the nextPageCursor token from the response to retrieve the next page of the result set
Response Parameters
Parameter	Type	Comments
category	string	Product type
list	array	Object
> orderId	string	Order ID
> orderLinkId	string	User customised order ID
> symbol	string	Symbol name
> price	string	Order price
> qty	string	Order qty
> side	string	Side. Buy,Sell
> positionIdx	integer	Position index. Used to identify positions in different position modes
> orderStatus	string	Order status
> cancelType	string	Cancel type
> rejectReason	string	Reject reason.
> avgPrice	string	Average filled price. If unfilled, it is "", and also for those orders have partilly filled but cancelled at the end
> leavesQty	string	The remaining qty not executed.
> leavesValue	string	The estimated value not executed.
> cumExecQty	string	Cumulative executed order qty
> cumExecValue	string	Cumulative executed order value.
> cumExecFee	string	Cumulative executed trading fee.
> timeInForce	string	Time in force
> orderType	string	Order type. Market,Limit. For TP/SL order, it means the order type after triggered
> stopOrderType	string	Stop order type
> orderIv	string	Implied volatility
> triggerPrice	string	Trigger price. If stopOrderType=TrailingStop, it is activate price. Otherwise, it is trigger price
> takeProfit	string	Take profit price
> stopLoss	string	Stop loss price
> tpslMode	string	TP/SL mode, Full: entire position for TP/SL. Partial: partial position tp/sl.
> tpLimitPrice	string	The limit order price when take profit price is triggered
> slLimitPrice	string	The limit order price when stop loss price is triggered
> tpTriggerBy	string	The price type to trigger take profit
> slTriggerBy	string	The price type to trigger stop loss
> triggerDirection	integer	Trigger direction. 1: rise, 2: fall
> triggerBy	string	The price type of trigger price
> lastPriceOnCreated	string	Last price when place the order
> reduceOnly	boolean	Reduce only. true means reduce position size
> closeOnTrigger	boolean	Close on trigger.
> createdTime	string	Order created timestamp (ms)
> updatedTime	string	Order updated timestamp (ms)
nextPageCursor	string	Refer to the cursor request parameter
Request Example
GET /cloud/trade/v3/pre-upgrade/order/history?category=linear&limit=1 HTTP/1.1
Host: openapi-testnet.zoomex.com
X-BAPI-SIGN: XXXXX
X-BAPI-API-KEY: XXXXX
X-BAPI-TIMESTAMP: 1672221263407
X-BAPI-RECV-WINDOW: 5000


Response Example
{
    "retCode": 0,
    "retMsg": "OK",
    "result": {
        "list": [
            {
                "orderId": "14bad3a1-6454-43d8-bcf2-5345896cf74d",
                "orderLinkId": "YLxaWKMiHU",
                "symbol": "BTCUSDT",
                "price": "26864.40",
                "qty": "0.003",
                "side": "Buy",
                "isLeverage": "",
                "positionIdx": 1,
                "orderStatus": "Cancelled",
                "cancelType": "UNKNOWN",
                "rejectReason": "EC_PostOnlyWillTakeLiquidity",
                "avgPrice": "0",
                "leavesQty": "0.000",
                "leavesValue": "0",
                "cumExecQty": "0.000",
                "cumExecValue": "0",
                "cumExecFee": "0",
                "timeInForce": "PostOnly",
                "orderType": "Limit",
                "stopOrderType": "UNKNOWN",
                "orderIv": "",
                "triggerPrice": "0.00",
                "takeProfit": "0.00",
                "stopLoss": "0.00",
                "tpTriggerBy": "UNKNOWN",
                "slTriggerBy": "UNKNOWN",
                "triggerDirection": 0,
                "triggerBy": "UNKNOWN",
                "lastPriceOnCreated": "0.00",
                "reduceOnly": false,
                "closeOnTrigger": false,
                "tpslMode": "",
                "tpLimitPrice": "",
                "slLimitPrice": "",
                "createdTime": "1684476068369",
                "updatedTime": "1684476068372"
            }
        ],
        "nextPageCursor": "page_token%3D39380%26",
        "category": "linear"
    },
    "retExtInfo": {},
    "time": 1684766282976
}


Get Pre-upgrade Trade History
Get users' execution records which occurred before you upgraded the account to a Unified account, sorted by execTime in descending order

HTTP Request
GET /cloud/trade/v3/pre-upgrade/execution/list

Request Parameters
Parameter	Required	Type	Comments
category	true	string	Product type
Trading account: spot, linear, inverse
symbol	false	string	Symbol name
startTime	false	integer	The start timestamp (ms)
startTime and endTime are not passed, return 7 days by default
Only startTime is passed, return range between startTime and startTime+7 days
Only endTime is passed, return range between endTime-7 days and endTime
If both are passed, the rule is endTime - startTime <= 7 days
endTime	false	integer	The end timestamp (ms)
execType	false	string	Execution type. Classic spot is not supported
limit	false	integer	Limit for data size per page. [1, 100]. Default: 50
cursor	false	string	Cursor. Use the nextPageCursor token from the response to retrieve the next page of the result set
Response Parameters
Parameter	Type	Comments
category	string	Product type
list	array	Object
> symbol	string	Symbol name
> orderId	string	Order ID
> side	string	Side. Buy,Sell
> orderPrice	string	Order price
> orderQty	string	Order qty
> leavesQty	string	Create an unexecuted order quantity, spot trading is not supported
> orderType	string	Order type. Market,Limit
> stopOrderType	string	Stop order type. If the order is not stop order, it either returns UNKNOWN or "". spot is not supported
> execFee	string	Executed trading fee. You can get spot fee currency instruction here
> execId	string	Execution ID
> execPrice	string	Execution price
> execQty	string	Execution qty
> execType	string	Executed type. spot is not supported
> execValue	string	Executed order value. spot is not supported
> execTime	string	Executed timestamp（ms）
> isMaker	boolean	Is maker order. true: maker, false: taker
> feeRate	string	Trading fee rate. spot is not supported
> markPrice	string	The mark price of the symbol when executing. spot is not supported
> closedSize	string	Closed position size
nextPageCursor	string	Refer to the cursor request parameter
請求示例
GET /cloud/trade/v3/pre-upgrade/execution/list?category=spot&symbol=BTCUSDT HTTP/1.1
Host: openapi-testnet.zoomex.com
X-BAPI-SIGN: XXXXX
X-BAPI-API-KEY: XXXXX
X-BAPI-TIMESTAMP: 1672221263407
X-BAPI-RECV-WINDOW: 5000


響應示例
{
  "result": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "orderId": "1896284562024596224",
        "side": "Buy",
        "orderPrice": "",
        "orderQty": "",
        "leavesQty": "",
        "orderType": "Market",
        "stopOrderType": "",
        "execFee": "0.0000000198",
        "execId": "2100000000136808695",
        "execPrice": "83877.09",
        "execType": "",
        "execValue": "",
        "execTime": "1740790735426",
        "isMaker": false,
        "feeRate": "",
        "markPrice": "",
        "closedSize": 0,
      },
      {
        "symbol": "BTCUSDT",
        "orderId": "1893483376007480064",
        "side": "Buy",
        "orderPrice": "",
        "orderQty": "",
        "leavesQty": "",
        "orderType": "Market",
        "stopOrderType": "",
        "execFee": "0.0000000198",
        "execId": "2100000000135856467",
        "execPrice": "90800",
        "execType": "",
        "execValue": "",
        "execTime": "1740456808031",
        "isMaker": false,
        "feeRate": "",
        "markPrice": "",
        "closedSize": 0,
      }
    ],
    "nextPageCursor": "2100000000135856467",
    "category": "spot"
  },
  "retCode": 0,
  "retExtInfo": {},
  "retMsg": "OK",
  "time": 1740966707907
}



Connect
caution
The V3 version of the public channel push is expected to go offline on September 23, 2025
please complete the switch as soon as possible(Private channel v3 Unchanged)
Please note: The following fields: tickDirection，price24hPcnt，fundingRate，bid1Price，bid1Size，ask1Price，ask1Size，V3 Even if there is no change, it will be pushed. V5 only pushes when there is a change
WebSocket public channel:

Mainnet:
Spot: wss://stream.zoomex.com/v5/public/spot
USDT perpetual: wss://stream.zoomex.com/v5/public/linear
Inverse contract: wss://stream.zoomex.com/v5/public/inverse

Testnet:
Spot: wss://stream-testnet.zoomex.com/v5/public/spot
USDT perpetual: wss://stream-testnet.zoomex.com/v5/public/linear
Inverse contract: wss://stream-testnet.zoomex.com/v5/public/inverse

WebSocket private channel:

Mainnet:
wss://stream.zoomex.com/v3/private

Testnet:
wss://stream-testnet.zoomex.com/v3/private

Authentication
info
Public topics do not require authentication. The following section applies to private topics only.
Apply for authentication when establishing a connection.

{
    "req_id": "10001", // optional
    "op": "auth",
    "args": [
        "api_key",
        1662350400000, // expires; is greater than your current timestamp
        "signature"
    ]
}


Successful authentication sample response

{
    "success": true,
    "ret_msg": "",
    "op": "auth",
    "conn_id": "cejreaspqfh3sjdnldmg-p"
}

note
Example signature algorithms as following.

import hmac
import json
import logging
import time


def send_auth():
    key = 'XXXXXXXX'
    secret = 'XXXXXXXX'
    expires = int((time.time() + 1000) * 1000)
    _val = f'GET/realtime{expires}'
    print(_val)
    signature = str(hmac.new(
        bytes(secret, 'utf-8'),
        bytes(_val, 'utf-8'), digestmod='sha256'
    ).hexdigest())
    print(json.dumps({"op": "auth", "args": [key, expires, signature]}))


if __name__ == "__main__":
    send_auth()


caution
Due to network complexity, your may get disconnected at any time. Please follow the instructions below to ensure that you receive WebSocket messages on time:

Keep connection alive by sending the heartbeat packet
Reconnect as soon as possible if disconnected
IP Limits
Do not frequently connect and disconnect the connection.
Do not build over 500 connections in 5 minutes. This is counted separately per WebSocket endpoint.
Public channel - Args limits
For one public connection, you cannot have length of "args" array over 21,000 characters.

How to Send the Heartbeat Packet
How to Send

// req_id is a customised ID, which is optional
ws.send(JSON.stringify({"req_id": "100001", "op": "ping"}));


Pong message example of public channels

{
    "success": true,
    "ret_msg": "pong",
    "conn_id": "465772b1-7630-4fdc-a492-e003e6f0f260",
    "req_id": "",
    "op": "ping"
}

Pong message example of private channels

{
    "req_id": "test",
    "op": "pong",
    "args": [
        "1675418560633"
    ],
    "conn_id": "cfcb4ocsvfriu23r3er0-1b"
}

caution
To avoid network or program issues, we recommend that you send the ping heartbeat packet every 20 seconds to maintain the WebSocket connection.

How to Subscribe to Topics
Understanding WebSocket Filters
How to subscribe with a filter

// Subscribing level 1 orderbook
{
    "req_id": "test", // optional
    "op": "subscribe",
    "args": [
        "orderbook.1.BTCUSDT"
    ]
}

Subscribing with multiple symbols and topics is supported.

{
    "req_id": "test", // optional
    "op": "subscribe",
    "args": [
        "orderbook.1.BTCUSDT",
        "publicTrade.BTCUSDT",
        "orderbook.1.ETHUSDT"
    ]
}

Understanding WebSocket Filters: Unsubscription
You can dynamically subscribe and unsubscribe from topics without unsubscribing from the WebSocket like so:

{
    "op": "unsubscribe",
    "args": [
        "publicTrade.ETHUSD"
    ],
    "req_id": "customised_id"
}

Understanding the Subscription Response
Topic subscription response message example

Private
Linear/Inverse
{
    "success": true,
    "ret_msg": "",
    "op": "subscribe",
    "conn_id": "cejreassvfrsfvb9v1a0-2m"



    Orderbook
Subscribe to the orderbook stream. Supports different depths.

tip
Once you have subscribed successfully, you will receive a snapshot.
The WebSocket will keep pushing delta messages every time the orderbook changes. If you receive a new snapshot message, you will have to reset your local orderbook.
If there is a problem on Zoomex's end, a snapshot will be re-sent, which is guaranteed to contain the latest data.
info
Linear & inverse level 1 data: if 3 seconds have elapsed without a change in the orderbook, a snapshot message will be pushed again.

Linear & inverse:
Level 1 data, push frequency: 10ms
Level 50 data, push frequency: 20ms
Level 200 data, push frequency: 100ms
Level 1000 data, push frequency: 300ms

Spot:
Level 1 data, push frequency: 10ms
Level 50 data, push frequency: 20ms
Level 200 data, push frequency: 200ms
Level 1000 data, push frequency: 300ms

Topic:
orderbook.{depth}.{symbol} e.g., orderbook.1.BTCUSDT

Response Parameters
Parameter	Type	Comments
topic	string	Topic name
type	string	Data type. snapshot,delta
ts	number	The timestamp (ms) that the system generates the data
data	array	Object
> s	string	Symbol name
> b	array	Bids. For snapshot stream, the element is sorted by price in descending order
>> b[0]	string	Bid price
>> b[1]	string	Bid size
The delta data has size=0, which means that all quotations for this price have been filled or cancelled
> a	array	Asks. For snapshot stream, the element is sorted by price in ascending order
>> a[0]	string	Ask price
>> a[1]	string	Ask size
The delta data has size=0, which means that all quotations for this price have been filled or cancelled
> u	integer	Update ID. Is a sequence. Occasionally, you'll receive "u"=1, which is a snapshot data due to the restart of the service. So please overwrite your local orderbook
> seq	integer	Cross sequence.
You can use this field to compare different levels orderbook data, and for the smaller seq, then it means the data is generated earlier.
cts	number	The timestamp from the match engine when this orderbook data is produced. It can be correlated with T from public trade channel
Subscribe Example
// 创建WebSocket对象
const socket = new WebSocket('wss://stream-testnet.zoomex.com/v5/public/linear');

// 订阅WebSocket
socket.onopen = function() {
  console.log('WebSocket连接已经打开');
  // 发送订阅消息
  const subscribeMsg = {
    "op": "subscribe",
    "args": ["orderbook.50.BTCUSDT"]
  };
  socket.send(JSON.stringify(subscribeMsg));
};

// 监听WebSocket消息
socket.onmessage = function(event) {
  console.log('收到WebSocket消息：', event.data);
};

// 监听WebSocket关闭事件
socket.onclose = function(event) {
  console.log('WebSocket连接已经关闭', event);
};


Response Example
Snapshot
Delta
{
    "topic": "orderbook.50.BTCUSDT",
    "type": "snapshot",
    "ts": 1672304484978,
    "data": {
        "s": "BTCUSDT",
        "b": [
            ...,
            [
                "16493.50",
                "0.006"
            ],
            [
                "16493.00",
                "0.100"
            ]
        ],
        "a": [
            [
                "16611.00",
                "0.029"
            ],
            [
                "16612.00",
                "0.213"
            ],
            ...,
        ],
    "u": 18521288,
    "seq": 7961638724
    }
}




Trade
Subscribe to the recent trades stream.

After subscription, you will be pushed trade messages in real-time.

Push frequency: real-time

Topic:
publicTrade.{symbol}

Response Parameters
Parameter	Type	Comments
id	string	Message id.
topic	string	Topic name
type	string	Data type. snapshot
ts	number	The timestamp (ms) that the system generates the data
data	array	Object. The element in the array is sort by matching time in ascending order
> T	number	The timestamp (ms) that the order is filled
> s	string	Symbol name
> S	string	Side of taker. Buy,Sell
> v	string	Trade size
> p	string	Trade price
> L	string	Direction of price change. Unique field for future
> i	string	Trade ID
Subscribe Example
const socket = new WebSocket('wss://stream-testnet.zoomex.com/v5/public/linear');

socket.onopen = function() {
  const subscribeMsg = {
    "op": "subscribe",
    "args": ["publicTrade.BTCUSDT"]
  };
  socket.send(JSON.stringify(subscribeMsg));
};

socket.onmessage = function(event) {
};

socket.onclose = function(event) {
};


Response Example
{
    "topic": "publicTrade.BTCUSDT",
    "type": "snapshot",
    "ts": 1672304486868,
    "data": [
        {
            "T": 1672304486865,
            "s": "BTCUSDT",
            "S": "Buy",
            "v": "0.001",
            "p": "16578.50",
            "L": "PlusTick",
            "i": "20f43950-d8dd-5b31-9112-a178eb6023af",
            "BT": false
        }
    ]
}


Ticker
Subscribe to the ticker stream.

note
This topic utilises the snapshot field and delta field. If a response param is not found in the message, then its value has not changed.
Push frequency: Derivatives - 100ms, Spot - real-time

Topic:
tickers.{symbol}

Response Parameters
Linear/Inverse
Spot
Parameter	Type	Comments
topic	string	Topic name
type	string	Data type. snapshot,delta
cs	integer	Cross sequence
ts	number	The timestamp (ms) that the system generates the data
data	array	Object
> symbol	string	Symbol name
> tickDirection	string	Tick direction
> price24hPcnt	string	Percentage change of market price in the last 24 hours
> lastPrice	string	Last price
> prevPrice24h	string	Market price 24 hours ago
> highPrice24h	string	The highest price in the last 24 hours
> lowPrice24h	string	The lowest price in the last 24 hours
> prevPrice1h	string	Market price an hour ago
> markPrice	string	Mark price
> indexPrice	string	Index price
> openInterest	string	Open interest size
> openInterestValue	string	Open interest value
> turnover24h	string	Turnover for 24h
> volume24h	string	Volume for 24h
> nextFundingTime	string	Next funding timestamp (ms)
> fundingRate	string	Funding rate
> bid1Price	string	Best bid price
> bid1Size	string	Best bid size
> ask1Price	string	Best ask price
> ask1Size	string	Best ask size
Subscribe Example
const socket = new WebSocket('wss://stream-testnet.zoomex.com/v5/public/linear');

socket.onopen = function() {
  const subscribeMsg = {
    "op": "subscribe",
    "args": ["tickers.BTCUSDT"]
  };
  socket.send(JSON.stringify(subscribeMsg));
};

socket.onmessage = function(event) {
};

socket.onclose = function(event) {
};


Response Example
Linear
```json
{
    "topic": "tickers.BTCUSDT",
    "type": "snapshot",
    "data": {
    "symbol": "BTCUSDT",
    "tickDirection": "PlusTick",
    "price24hPcnt": "0.017103",
    "lastPrice": "17216.00",
    "prevPrice24h": "16926.50",
    "highPrice24h": "17281.50",
    "lowPrice24h": "16915.00",
    "prevPrice1h": "17238.00",
    "markPrice": "17217.33",
    "indexPrice": "17227.36",
    "openInterest": "68744.761",
    "openInterestValue": "1183601235.91",
    "turnover24h": "1570383121.943499",
    "volume24h": "91705.276",
    "nextFundingTime": "1673280000000",
    "fundingRate": "-0.000212",
    "bid1Price": "17215.50",
    "bid1Size": "84.489",
    "ask1Price": "17216.00",
    "ask1Size": "83.020"
},
    "cs": 24987956059,
    "ts": 1673272861686
}
```


Kline
Subscribe to the klines stream.

tip
If confirm=true, this means that the candle has closed. Otherwise, the candle is still open and updating.

Available intervals:

1 3 5 15 30 (min)
60 120 240 360 720 (min)
D (day)
W (week)
M (month)
Push frequency: 1-60s

Topic:
kline.{interval}.{symbol} e.g., kline.30.BTCUSDT

Response Parameters
Parameter	Type	Comments
topic	string	Topic name
type	string	Data type. snapshot
ts	number	The timestamp (ms) that the system generates the data
data	array	Object
> start	number	The start timestamp (ms)
> end	number	The end timestamp (ms)
> interval	string	Kline interval
> open	string	Open price
> close	string	Close price
> high	string	Highest price
> low	string	Lowest price
> volume	string	Trade volume
> turnover	string	Turnover
> confirm	boolean	Weather the tick is ended or not
> timestamp	number	The timestamp (ms) of the last matched order in the candle
Subscribe Example
const socket = new WebSocket('wss://stream-testnet.zoomex.com/v5/public/linear');

socket.onopen = function() {
  const subscribeMsg = {
    "op": "subscribe",
    "args": ["kline.5.BTCUSDT"]
  };
  socket.send(JSON.stringify(subscribeMsg));
};

socket.onmessage = function(event) {
};

socket.onclose = function(event) {
};


Response Example
{
    "topic": "kline.5.BTCUSDT",
    "data": [
        {
            "start": 1672324800000,
            "end": 1672325099999,
            "interval": "5",
            "open": "16649.5",
            "close": "16677",
            "high": "16677",
            "low": "16608",
            "volume": "2.081",
            "turnover": "34666.4005",
            "confirm": false,
            "timestamp": 1672324988882
        }
    ],
    "ts": 1672324988882,
    "type": "snapshot"
}



All Liquidation
Subscribe to the liquidation stream, push all liquidations.

Covers: USDT contract / Inverse contract

Push frequency: 500ms

Topic:
allLiquidation.{symbol} e.g., allLiquidation.BTCUSDT

Response Parameters
Parameter	Type	Comments
topic	string	Topic name
type	string	Data type. snapshot
ts	number	The timestamp (ms) that the system generates the data
data	Object	
> T	number	The updated timestamp (ms)
> s	string	Symbol name
> S	string	Position side. Buy,Sell. When you receive a Buy update, this means that a long position has been liquidated
> v	string	Executed size
> p	string	Bankruptcy price
Subscribe Example
const socket = new WebSocket('wss://stream-testnet.zoomex.com/v5/public/linear');

socket.onopen = function() {
  const subscribeMsg = {
    "op": "subscribe",
    "args": ["allLiquidation.BTCUSDT"]
  };
  socket.send(JSON.stringify(subscribeMsg));
};

socket.onmessage = function(event) {
};

socket.onclose = function(event) {
};


Message Example
{
    "topic": "allLiquidation.BTCUSDT",
    "type": "snapshot",
    "ts": 1739502303204,
    "data": [
        {
            "T": 1739502302929,
            "s": "BTCUSDT",
            "S": "Sell",
            "v": "20000",
            "p": "0.04499"
        }
    ]
}

Previous
Kline


Rate Limit
IP Rate Limit
HTTP IP limit
You are allowed to send 600 requests within a 5-second window per IP by default. This limit applies to all traffic directed to api.zoomex.com. If you encounter the error "403, access too frequent", it indicates that your IP has exceeded the allowed request frequency. In this case, you should terminate all HTTP sessions and wait for at least 10 minutes. The ban will be lifted automatically.

We do not recommend running your application at the very edge of these limits in case abnormal network activity results in an unexpected violation.

Websocket IP limit
Do not establish more than 500 connections within a 5-minute window. This limit applies to all connections directed to stream.zoomex.com as well as local site hostnames such as stream.zoomex.kz. Do not frequently connect and disconnect the connection Do not establish more than 1,000 connections per IP for market data. The connection limits are counted separately for Spot, Linear, and Inverse markets

API Rate Limit
caution
If you receive "ret_msg": "Too many visits!" in the JSON response, you have hit the API rate limit.

The API rate limit is based on the rolling time window per second and UID. In other words, it is per second per UID. Every request to the API returns response header shown in the code panel:

X-Bapi-Limit-Status - your remaining requests for current endpoint
X-Bapi-Limit - your current limit for current endpoint
X-Bapi-Limit-Reset-Timestamp - the timestamp indicating when your request limit resets if you have exceeded your rate_limit. Otherwise, this is just the current timestamp (it may not exactly match timeNow).
Http Response Header Example

▶Response Headers
Content-Type: application/json; charset=utf-8
Content-Length: 141
X-Bapi-Limit: 100
X-Bapi-Limit-Status: 99
X-Bapi-Limit-Reset-Timestamp: 1672738134824

API Rate Limit Table
Trade
Method	Path	linear	inverse	upgradable
POST	/cloud/trade/v3/order/create	10 req/s	10 req/s	Y
/cloud/trade/v3/order/amend	10 req/s	10 req/s	Y
/cloud/trade/v3/order/cancel	10 req/s	10 req/s	Y
/cloud/trade/v3/order/cancel-all	10 req/s	10 req/s	N
GET	/cloud/trade/v3/order/realtime	10 req/s	10 req/s	N
/cloud/trade/v3/order/history	10 req/s	10 req/s	N
Position
Method	Path	linear/inverse	upgradable
GET	/cloud/trade/v3/position/list	10 req/s	N
/cloud/trade/v3/execution/list	10 req/s	N
/cloud/trade/v3/position/closed-pnl	10 req/s	N
POST	/cloud/trade/v3/position/set-leverage	10 req/s	N
/cloud/trade/v3/position/set-tpsl-mode	10 req/s	N
/cloud/trade/v3/position/set-risk-limit	10 req/s	N
/cloud/trade/v3/position/trading-stop	10 req/s	N
Account
Method	Path	Limit	upgradable
GET	/cloud/trade/v3/account/wallet-balance	10 req/s	N
/cloud/trade/v3/account/fee-rate	10 req/s	N
API Rate Limit Rules For VIPs/PROs
info
The values in the table represent the application upper limit of the corresponding level, and do not mean that users at this level will automatically enjoy the corresponding API Rate Limit by default.
instructions for batch endpoints
API for batch create/amend/cancel order, the frequency of the API will be consistent with the current configuration, but the counting consumption will be consumed according to the actual number of orders. (Number of consumption = number of requests * number of orders included in a single request), and the configuration of business lines is independent of each other.

The batch APIs allows 1-20 orders/request. For example, if a batch order request is made once and contains 10 orders, then the request limit will consume 10.

If part of the last batch of orders requested within 1s exceeds the limit, the part that exceeds the limit will fail, and the part that does not exceed the limit will succeed. For example, in the 1 second, the limit is 10, but a batch request containing 15 orders is placed at this time, then the first 10 orders will be successfully placed, and the 11-15th orders will report an error exceeding the limit, and these orders will fail.

Normal account
Level\Product	Futures
Default	10/s
VIP 1	20/s
VIP 2	40/s
VIP 3 - Supreme VIP	60/s
PRO1	100/s
PRO2	150/s
PRO3	200/s
UID level
Level\Product	Futures	Spot
PRO1	200/s	200/s
PRO2	400/s	400/s
PRO3	600/s	600/s
PRO4	800/s	800/s
PRO5	1000/s	1000/s
PRO6	1200/s	1200/s
Master and subaccounts level
Level\Product	Futures	Spot
PRO1	10000/s	10000/s
PRO2	20000/s	20000/s
PRO3	30000/s	30000/s
PRO4	40000/s	40000/s
PRO5	50000/s	50000/s
PRO6	60000/s	60000/s
Set api rate limit
API rate limit: 50 req per second

info
If UID requesting this endpoint is a master account, uids in the input parameter must be subaccounts of the master account.
If UID requesting this endpoint is not a master account, uids in the input parameter must be the UID requesting this endpoint.
UID requesting this endpoint must be an institutional user.
HTTP Request
POST /cloud/trade/v3/apilimit/set

Request Parameters
Parameter	Required	Type	Comments
list	true	array	Object
> uids	true	string	Multiple UIDs, separated by commas
> bizType	true	string	Business type
> rate	true	integer	api rate limit per second
Response Parameters
Parameter	Type	Comments
list	array	Object
> uids	string	Multiple UIDs, separated by commas
> bizType	string	Business type
> rate	integer	api rate limit per second
> success	boolean	success or not
> msg	string	result message
Request Example
POST /cloud/trade/v3/apilimit/set HTTP/1.1
Host: openapi-testnet.zoomex.com
X-BAPI-SIGN: XXXXXXX
X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx
X-BAPI-TIMESTAMP: 1711420489915
X-BAPI-RECV-WINDOW: 5000
Content-Type: application/json

{
    "list": [
        {
            "uids": "106293838",
            "bizType": "DERIVATIVES",
            "rate": 50
        }
    ]
}

Response Example
{
  "retCode": 0,
  "retMsg": "success",
  "result": {
    "result": [
      {
        "uids": "290118",
        "bizType": "SPOT",
        "rate": 600,
        "success": true,
        "msg": "API limit updated successfully"
      }
    ]
  },
  "retExtInfo": {},
  "time": 1754894296913
}

Query api rate limit
API rate limit: 50 req per second

info
A master account can query api rate limit of its own and subaccounts.
A subaccount can only query its own api rate limit.
HTTP Request
GET /cloud/trade/v3/apilimit/query

Request Parameters
Parameter	Required	Type	Comments
uids	true	string	Multiple UIDs, separated by commas
Response Parameters
Parameter	Type	Comments
list	array	Object
> uids	string	Multiple UIDs, separated by commas
> bizType	string	Business type
> rate	integer	api rate limit per second
Request Example
GET /cloud/trade/v3/apilimit/query?uids=290118 HTTP/1.1
Host: openapi-testnet.zoomex.com
X-BAPI-SIGN: XXXXXXX
X-BAPI-API-KEY: xxxxxxxxxxxxxxxxxx
X-BAPI-TIMESTAMP: 1728460942776
X-BAPI-RECV-WINDOW: 5000
Content-Type: application/json
Content-Length: 2


Response Example
{
  "retCode": 0,
  "retMsg": "success",
  "result": {
    "list": [
      {
        "uids": "290118",
        "bizType": "SPOT",
        "rate": 600
      },
      {
        "uids": "290118",
        "bizType": "DERIVATIVES",
        "rate": 400
      }
    ]
  },
  "retExtInfo": {},
  "time": 1754894341984
}

How to increase API Limit
Please contact your client manager or email to support@zoomex.com with the following information. We will reply within 1-4 working days:

Your name and your company details
Your Zoomex UID or registered email, and the assets you are trading
General description of your trading strategy and reasons for higher rate limits
Screenshot of previous monthly trading volume (maker/taker) on other platforms
Optional: your order history in CSV forma



Enums Definitions
locale
de-DE
en-US
es-AR
es-ES
es-MX
fr-FR
kk-KZ
id-ID
uk-UA
ja-JP
ru-RU
th-TH
pt-BR
tr-TR
vi-VN
zh-TW
ar-SA
hi-IN
fil-PH
category
Normal Account

linear USDT perp
inverse Inverse contract, including Inverse perp, Inverse futures
orderStatus
Created order has been accepted by the system but not yet put through the matching engine
New order has been placed successfully
Rejected
PartiallyFilled
Filled
Cancelled In derivatives, orders with this status may have an executed qty
Untriggered
Triggered
Deactivated
Active order has been triggered and the new active order has been successfully placed. Is the final state of a successful conditional order
timeInForce
GTC GoodTillCancel
IOC ImmediateOrCancel
FOK FillOrKill
PostOnly
execType
Trade
AdlTrade Auto-Deleveraging
Funding Funding fee
BustTrade Liquidation
BlockTrade
stopOrderType
TakeProfit
StopLoss
TrailingStop
Stop
PartialTakeProfit
PartialStopLoss
tickDirection
PlusTick price rise
ZeroPlusTick trade occurs at the same price as the previous trade, which occurred at a price higher than that for the trade preceding it
MinusTick price drop
ZeroMinusTick trade occurs at the same price as the previous trade, which occurred at a price lower than that for the trade preceding it
interval
1 3 5 15 30 60 120 240 360 720 minute
D day
W week
M month
positionIdx
0 one-way mode position
1 Buy side of hedge-mode position
2 Sell side of hedge-mode position
positionStatus
Normal
Liq in the liquidation progress
Adl in the auto-deleverage progress
rejectReason
EC_NoError
EC_Others
EC_UnknownMessageType
EC_MissingClOrdID
EC_MissingOrigClOrdID
EC_ClOrdIDOrigClOrdIDAreTheSame
EC_DuplicatedClOrdID
EC_OrigClOrdIDDoesNotExist
EC_TooLateToCancel
EC_UnknownOrderType
EC_UnknownSide
EC_UnknownTimeInForce
EC_WronglyRouted
EC_MarketOrderPriceIsNotZero
EC_LimitOrderInvalidPrice
EC_NoEnoughQtyToFill
EC_NoImmediateQtyToFill
EC_PerCancelRequest
EC_MarketOrderCannotBePostOnly
EC_PostOnlyWillTakeLiquidity
EC_CancelReplaceOrder
EC_InvalidSymbolStatus
accountType
CONTRACT Derivatives Account
SPOT Spot Account
FUND Funding Account
COPYTRADING Copy trade Account
UNIFIED Trading account
transferStatus
SUCCESS
PENDING
FAILED
depositStatus
0 unknown
1 toBeConfirmed
2 processing
3 success
4 deposit failed
withdrawStatus
Pending Review
Pending Transfer
Rejected
Transferred successfully
Cancelled
Fail
triggerBy
LastPrice
IndexPrice
MarkPrice
cancelType
CancelByUser
CancelByReduceOnly
CancelByPrepareLiq CancelAllBeforeLiq Cancelled due to liquidation
CancelByPrepareAdl CancelAllBeforeAdl Cancelled due to ADL
CancelByAdmin
CancelByTpSlTsClear
CancelByPzSideCh
CancelBySmp
period
BTC: 7,14,21,30,60,90,180,270days
ETH: 7,14,21,30,60,90,180,270days
SOL: 7,14,21,30,60,90days
contractType
InversePerpetual
LinearPerpetual
status
PreLaunch
Trading
Settling
Closed
type
TRANSFER_IN
TRANSFER_OUT
TRADE
SETTLEMENT
DELIVERY
LIQUIDATION
BONUS
FEE_REFUND
INTEREST
CURRENCY_BUY
CURRENCY_SELL
unifiedMarginStatus
1 Regular account
ltStatus
1 LT can be purchased and redeemed
2 LT can be purchased, but not redeemed
3 LT can be redeemed, but not purchased
4 LT cannot be purchased nor redeemed
5 Adjusting position
symbol
USDT Perpetual:

BTCUSDT
ETHUSDT
Inverse Perpetual:

BTCUSD
ETHUSD
vipLevel
No VIP
PRO-1
PRO-2
PRO-3
VIP-1
VIP-2
VIP-3
MM-1
MM-2
MM-3
adlRankIndicator
0 default value of empty position
1
2
3
4
5
bizType
SPOT
DERIVATIVES
msg
API limit updated successfully API limit updated successfully
Requested limit exceeds maximum allowed per user Requested limit exceeds maximum allowed per user
No permission to operate these UIDs No permission to operate these UIDs
API cap configuration not found API cap configuration not found
API cap configuration not found for bizType API cap configuration not found for bizType
Requested limit would exceed institutional quota Requested limit would exceed institutional quota



Error Codes
HTTP Code
Code	Description
400	Bad request. Need to send the request with GET / POST (must be capitalized)
401	Invalid request. 1. Need to use the correct key to access; 2. Need to put authentication params in the request header
403	Forbidden request. Possible causes: 1. IP rate limit breached; 2. You send GET request with an empty json body
404	Cannot find path. Possible causes: 1. Wrong path; 2. Category value does not match account mode
Trading account & Futures of Normal Account
Code	Description
0	OK
10000	Server Timeout
10001	Request parameter error
10002	The request time exceeds the time window range.
10003	API key is invalid.
10004	Error sign, please check your signature generation algorithm.
10005	Permission denied, please check your API key permissions.
10006	Too many visits. Exceeded the API Rate Limit.
10007	User authentication failed.
10008	Common banned, please check your account mode
10009	IP has been banned.
10010	Unmatched IP, please check your API key's bound IP addresses.
10014	Invalid duplicate request.
10016	Server error.
10017	Route not found.
10018	Exceeded the IP Rate Limit.
10024	Compliance rules triggered
10027	Transactions are banned.
10029	The requested symbol is invalid, please check symbol whitelist
30150	Current order leverage exceeds the maximum available for your current Risk Limit tier. Please lower leverage before placing an order.
30151	Leverage for Perpetual or Futures contracts cannot exceed the maximum allowed for your Institutional Loan.
30153	Reduce-Only restrictions must be lifted for both Long and Short positions at the same time.
40004	the order is modified during the process of replacing , please check the order status again
110001	Order does not exist
110003	Order price exceeds the allowable range.
110004	Wallet balance is insufficient
110005	position status
110006	The assets are estimated to be unable to cover the position margin
110007	Available balance is insufficient
110008	The order has been completed or cancelled.
110009	The number of stop orders exceeds the maximum allowable limit. You can find references from our Open API doc.
110010	The order has been cancelled
110011	Liquidation will be triggered immediately by this adjustment
110012	Insufficient available balance.
110013	Cannot set leverage due to risk limit level.
110014	Insufficient available balance to add additional margin.
110015	The position is in cross margin mode.
110016	The quantity of contracts requested exceeds the risk limit, please adjust your risk limit level before trying again
110017	Unmatch the ReduceOnly rules.
110018	User ID is illegal.
110019	Order ID is illegal.
110020	Not allowed to have more than 500 active orders.
110021	Not allowed to exceeded position limits due to Open Interest.
110022	Quantity has been restricted and orders cannot be modified to increase the quantity.
110023	Currently you can only reduce your position on this contract. please check our announcement or contact customer service for details.
110024	You have an existing position, so the position mode cannot be switched.
110025	Position mode has not been modified.
110026	Cross/isolated margin mode has not been modified.
110027	Margin has not been modified.
110028	You have existing open orders, so the position mode cannot be switched.
110029	Hedge mode is not supported for this symbol.
110030	Duplicate orderId
110031	Non-existing risk limit info, please check the risk limit rules.
110032	Order is illegal
110033	You can't set margin without an open position
110034	There is no net position
110035	Cancellation of orders was not completed before liquidation
110036	You are not allowed to change leverage due to cross margin mode.
110037	User setting list does not have this symbol
110038	You are not allowed to change leverage due to portfolio margin mode.
110039	Maintenance margin rate is too high. This may trigger liquidation.
110040	The order will trigger a forced liquidation, please re-submit the order.
110041	Skip liquidation is not allowed when a position or maker order exists
110043	Set leverage has not been modified.
110044	Available margin is insufficient.
110045	Wallet balance is insufficient.
110046	Liquidation will be triggered immediately by this adjustment.
110047	Risk limit cannot be adjusted due to insufficient available margin.
110048	Risk limit cannot be adjusted as the current/expected position value exceeds the revised risk limit.
110049	Tick notes can only be numbers
110050	Invalid coin
110051	The user's available balance cannot cover the lowest price of the current market
110052	Your available balance is insufficient to set the price
110053	The user's available balance cannot cover the current market price and upper limit price
110054	This position has at least one take profit link order, so the take profit and stop loss mode cannot be switched
110055	This position has at least one stop loss link order, so the take profit and stop loss mode cannot be switched
110056	This position has at least one trailing stop link order, so the take profit and stop loss mode cannot be switched
110057	Conditional order or limit order contains TP/SL related params
110058	You can't set take profit and stop loss due to insufficient size of remaining position size.
110059	Not allowed to modify the TP/SL of a partially filled open order
110060	Under full TP/SL mode, it is not allowed to modify TP/SL
110061	Not allowed to have more than 20 TP/SLs under Partial tpSlMode
110062	There is no MMP information of the institution found.
110063	Settlement in progress! {{key0}} not available for trading.
110064	The modified contract quantity cannot be less than or equal to the filled quantity.
110066	Trading is currently not allowed.
110068	Leveraged trading is not allowed.
110069	Ins lending customer is not allowed to trade.
110070	ETP symbols cannot be traded.
110071	Sorry, we're revamping the Unified Margin Account! Currently, new upgrades are not supported. If you have any questions, please contact our 24/7 customer support.
110072	OrderLinkedID is duplicate
110073	Set margin mode failed
110075	RiskId not modified
110076	Only isolated mode can set auto-add-margin
110077	Pm mode cannot support
110078	Added margin more than max can reduce margin
110079	The order is processing and can not be operated, please try again later
110094	Order notional Value below the lower limit {{.key}}.
3100197	Temporary banned due to the upgrade to Trading account
3200403	isolated margin can not create order
3400208	You have unclosed hedge mode or isolated mode USDT perpetual positions
3400209	You have USDT perpetual positions, so upgrading is prohibited for 10 minutes before and after the hour every hour
3400210	The risk rate of your Derivatives account is too high
3400211	Once upgraded, the estimated risk rate will be too high
3400054	You have uncancelled USDT perpetual orders
3400214	Server error, please try again later
3400071	The net asset is not satisfied