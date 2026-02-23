Get Server Time
GET /capi/v2/market/time
Weight(IP): 1

Request parameters

NONE

Request example

curl "https://api-contract.weex.com/capi/v2/market/time"


Response parameters

Parameter	Type	Description
epoch	String	Unix timestamp in UTC time zone, represented as a decimal number of seconds
iso	String	ISO 8601 standard time format
timestamp	Long	Server time
Unix millisecond timestamp
Response example

{
    "epoch": "1716710918.113",
    "iso": "2024-05-26T08:08:38.113Z",
    "timestamp": 1716710918113
}

Previous
Change Log




Get Futures Information
GET /capi/v2/market/contracts
Weight(IP): 10

Request parameters

Parameter	Type	Required?	Description
symbol	String	No	Trading pair
Request example

curl "https://api-contract.weex.com/capi/v2/market/contracts?symbol=cmt_btcusdt"


Response parameters

Parameter	Type	Description
symbol	String	Trading pair
underlying_index	String	Futures crypto
quote_currency	String	Quote currency
coin	String	Margin token
contract_val	String	Futures face value
delivery	Array	Settlement times
size_increment	String	Decimal places of the quantity
tick_size	String	Decimal places of the price
forwardContractFlag	Boolean	Whether it is USDT-M futures
priceEndStep	BigDecimal	Step size of the last decimal digit in the price
minLeverage	Integer	Minimum leverage (default: 1)
maxLeverage	Integer	Maximum leverage (default: 100)
buyLimitPriceRatio	String	Ratio of bid price to limit price
sellLimitPriceRatio	String	Ratio of ask price to limit price
makerFeeRate	String	Maker rate
takerFeeRate	String	Taker rate
minOrderSize	String	Minimum order size (base currency)
maxOrderSize	String	Maximum order size (base currency)
maxPositionSize	String	Maximum position size (base currency)
marketOpenLimitSize	String	Market Order Opening Position Single Limit (base currency)
Response example

[
  {
    "symbol": "cmt_btcusdt",
    "underlying_index": "BTC",
    "quote_currency": "USDT",
    "coin": "USDT",
    "contract_val": "0",
    "delivery": [
      "00:00:00",
      "08:00:00",
      "16:00:00"
    ],
    "size_increment": "5",
    "tick_size": "1",
    "forwardContractFlag": true,
    "priceEndStep": 1,
    "minLeverage": 1,
    "maxLeverage": 500,
    "buyLimitPriceRatio": "0.015",
    "sellLimitPriceRatio": "0.015",
    "makerFeeRate": "0.0002",
    "takerFeeRate": "0.0006",
    "minOrderSize": "0.0001",
    "maxOrderSize": "100000",
    "maxPositionSize": "1000000"
  }
]

Get OrderBook Depth
GET /capi/v2/market/depth
Weight(IP): 1

Request parameters

Parameter	Parameter type	Required?	Description
symbol	String	Yes	Trading pair
limit	Integer	No	Fixed gear enumeration value: 15/200, the default gear is 15
Request example

curl "https://api-contract.weex.com/capi/v2/market/depth?symbol=cmt_btcusdt&limit=15"


Response parameters

Parameter	Type	Description
asks	List	Sell side depth data
Format: [price, quantity] where quantity is in base currency
Index 0	String	Price
Index 1	String	Quantity
bids	List	Buy side depth data
Format: [price, quantity] where quantity is in base currency
Index 0	String	Price
Index 1	String	Quantity
timestamp	String	Timestamp
Unix millisecond timestamp
Response example

{
   "asks":[
         [
            "8858.0", //price
            "19299"//quantity
        ]   
     ],
   "bids":[
         [
            "7466.0", //price
            "499"  //quantity
        ],
         [
            "4995.0",
            "12500"
        ]
     ],
   "timestamp":"1591237821479" 
}

Previous
Get Futures Information




Get All Ticker
GET /capi/v2/market/tickers
Weight(IP): 40

Request parameters

NONE

Request example

curl "https://api-contract.weex.com/capi/v2/market/tickers"


Response parameters

Parameter	Type	Description
symbol	String	Trading pair
last	String	Latest execution price
best_ask	String	Ask price
best_bid	String	Bid price
high_24h	String	Highest price in the last 24 hours
low_24h	String	Lowest price in the last 24 hours
volume_24h	String	Trading volume of quote currency
timestamp	String	System timestamp
Unix millisecond timestamp
priceChangePercent	String	Price increase or decrease (24 hours)
base_volume	String	Trading volume of quote currency
markPrice	String	Mark price
indexPrice	String	Index price
Response example

[
  {
    "symbol": "cmt_btcusdt",
    "last": "90755.3",
    "best_ask": "90755.4",
    "best_bid": "90755.3",
    "high_24h": "91130.0",
    "low_24h": "90097.3",
    "volume_24h": "2321170547.37995",
    "timestamp": "1764482511864",
    "priceChangePercent": "0.000474",
    "base_volume": "25615.0755",
    "markPrice": "90755.2",
    "indexPrice": "90797.161"
  }
]




Get Single Ticker
GET /capi/v2/market/ticker
Weight(IP): 1

Request parameters

Parameter	Type	Required?	Description
symbol	String	Yes	Trading pair
Request example

curl "https://api-contract.weex.com/capi/v2/market/ticker?symbol=cmt_btcusdt"


Response parameters

Parameter	Type	Description
symbol	String	Trading pair
last	String	Latest execution price
best_ask	String	Ask price
best_bid	String	Bid price
high_24h	String	Highest price in the last 24 hours
low_24h	String	Lowest price in the last 24 hours
volume_24h	String	Trading volume of quote currency
timestamp	String	System timestamp
Unix millisecond timestamp
priceChangePercent	String	Price increase or decrease (24 hours)
base_volume	String	Trading volume of quote currency
markPrice	String	Mark price
indexPrice	String	Index price
Response example

{
  "symbol": "cmt_btcusdt",
  "last": "90755.3",
  "best_ask": "90755.4",
  "best_bid": "90755.3",
  "high_24h": "91130.0",
  "low_24h": "90097.3",
  "volume_24h": "2321170547.37995",
  "timestamp": "1764482511864",
  "priceChangePercent": "0.000474",
  "base_volume": "25615.0755",
  "markPrice": "90755.2",
  "indexPrice": "90797.161"
}



Get Trades
GET /capi/v2/market/trades
Weight(IP): 5

Request parameters

Parameter	Type	Required?	Description
symbol	String	Yes	Trading pair
limit	Integer	No	The size of the data ranges from 1 to 1000, with a default of 100
Request example

curl "https://api-contract.weex.com/capi/v2/market/trades?symbol=cmt_btcusdt&limit=100"


Response parameters

Parameter	Type	Description
ticketId	String	Filled order ID
time	Long	The time at which the order was filled
Unix millisecond timestamp
price	String	The price at which the order was filled
size	String	The quantity that was filled (base currency)
value	String	Filled amount (quote currency)
symbol	String	Trading pair
isBestMatch	Boolean	Was the trade the best price match?
isBuyerMaker	Boolean	Was the buyer the maker?
contractVal	String	Futures face value (unit: contracts)
Response example

[
    {
        "ticketId": "124b129e-3999-4d14-a4b5-9bdda68e5e26",
        "time": 1716604853286,
        "price": "68734.8",
        "size": "0.001",
        "value": "68.7348",
        "symbol": "cmt_btcusdt",
        "isBestMatch": true,
        "isBuyerMaker": true,
        "contractVal": "0.000001"
    }
]



Get Historical Candlestick
Description
Query all historical K-line data and return a maximum of 100 pieces of data.
When either startTime or endTime is invalid, the K-line data for the latest time period will be returned.
When both startTime and endTime are provided, the endTime will take precedence and the startTime will be ignored.

GET /capi/v2/market/historyCandles
Weight(IP): 5

Request parameters

Parameter	Type	Required?	Description
symbol	String	Yes	Trading pair
granularity	String	Yes	Candlestick interval[1m,5m,15m,30m,1h,4h,12h,1d,1w]
startTime	Long	No	The start time is to query the k-lines after this time
Unix millisecond timestamp
endTime	Long	No	The end time is to query the k-lines before this time
Unix millisecond timestamp
limit	Integer	No	The size of the data ranges from 1 to 100, with a default of 100
priceType	String	No	Price Type : LAST latest market price; MARK mark; INDEX index;
LAST by default
Request example

curl "https://api-contract.weex.com/capi/v2/market/historyCandles?symbol=cmt_bchusdt&granularity=1m"


Response parameters

Parameter	Type	Description
index[0]	String	Candlestick time
Unix millisecond timestamp
index[1]	String	Opening price
index[2]	String	Highest price
index[3]	String	Lowest price
index[4]	String	Closing price
index[5]	String	Trading volume of the base coin
index[6]	String	Trading volume of quote currency
Response example

[
  [
    "1716707460000",//Candlestick time
    "69174.3",//Opening price
    "69174.4",//Highest price
    "69174.1",//Lowest price
    "69174.3",//Closing price
    "0", //Trading volume of the base coin 
    "0.011" //Trading volume of quote currency
  ]
]



Get Candlestick Data
GET /capi/v2/market/candles
Weight(IP): 1

Request parameters

Parameter	Type	Required?	Description
symbol	String	Yes	Trading pair
granularity	String	Yes	Candlestick interval[1m,5m,15m,30m,1h,4h,12h,1d,1w]
limit	Integer	No	The size of the data ranges from 1 to 1000, with a default of 100
priceType	String	No	Price Type : LAST latest market price; MARK mark; INDEX index;
LAST by default
Request example

curl "https://api-contract.weex.com/capi/v2/market/candles?symbol=cmt_bchusdt&granularity=1m"


Response parameters

Parameter	Type	Description
index[0]	String	Candlestick time
Unix millisecond timestamp
index[1]	String	Opening price
index[2]	String	Highest price
index[3]	String	Lowest price
index[4]	String	Closing price
index[5]	String	Trading volume of the base coin
index[6]	String	Trading volume of quote currency
Response example

[
    [
        "1716707460000",//Candlestick time
        "69174.3",//Opening price
        "69174.4",//Highest price
        "69174.1",//Lowest price
        "69174.3",//Closing price
        "0", //Trading volume of the base coin 
        "0.011" //Trading volume of quote currency
    ]
]





Get Cryptocurrency Index
GET /capi/v2/market/index
Weight(IP): 1

Request parameters

Parameter	Type	Required?	Description
symbol	String	Yes	Trading pair
priceType	String	No	Price Type : MARK mark; INDEX index;
INDEX by default
Request example

curl "https://api-contract.weex.com/capi/v2/market/index?symbol=cmt_bchusdt&priceType=INDEX"


Response parameters

Parameter	Type	Description
symbol	String	Trading pair
index	String	Index
timestamp	String	Timestamp
Unix millisecond timestamp
Response example

{
    "symbol": "cmt_btcusdt",
    "index": "333.627857143",
    "timestamp": "1716604853286"
}



Get Open Interest
GET /capi/v2/market/open_interest
Weight(IP): 2

Request parameters

Parameter	Type	Required?	Description
symbol	String	Yes	Trading pair
Request example

curl "https://api-contract.weex.com/capi/v2/market/open_interest?symbol=cmt_1000satsusdt"


Response parameters

Parameter	Type	Description
symbol	String	Trading pair
base_volume	String	Total open interest of the platform Specific coins
target_volume	String	Quote Currency Holdings
timestamp	String	Timestamp
Unix millisecond timestamp
Response example

[
    {
        "symbol": "cmt_1000satsusdt",
        "base_volume": "0",
        "target_volume": "0",
        "timestamp": "1716709712753"
    }
]

Get Next Funding Time
Weight(IP): 1

GET /capi/v2/market/funding_time
Request parameters

Parameter	Type	Required?	Description
symbol	String	Yes	Trading pair
Request example

curl "https://api-contract.weex.com/capi/v2/market/funding_time?symbol=cmt_bchusdt"


Response parameters

Parameter	Type	Description
symbol	String	Trading pair
fundingTime	Long	Settlement time
Unix millisecond timestamp
Response example

{
  "symbol": "cmt_btcusdt",
  "fundingTime": 1716595200000
}

Previous
Get Open Interest

Get Historical Funding Rates
GET /capi/v2/market/getHistoryFundRate
Weight(IP): 5

Request parameters

Parameter	Type	Required?	Description
symbol	String	Yes	Trading pair
limit	Integer	No	The size of the data ranges from 1 to 100, with a default of 10
Request example

curl "https://api-contract.weex.com/capi/v2/market/getHistoryFundRate?symbol=cmt_bchusdt&limit=100"


Response parameters

Parameter	Type	Description
symbol	string	Trading pair
fundingRate	string	Funding rate
fundingTime	long	Funding fee settlement time
Unix millisecond timestamp
Response example

[
    {
        "symbol": "cmt_btcusdt",
        "fundingRate": "0.0001028",
        "fundingTime": 1716595200000
    }
]



Get Current Funding Rate
GET /capi/v2/market/currentFundRate
Weight(IP): 1

Request parameters

Parameter	Type	Required?	Description
symbol	String	No	Trading pair
Request example

curl "https://api-contract.weex.com/capi/v2/market/currentFundRate?symbol=cmt_bchusdt"


Response parameters

Parameter	Type	Description
symbol	String	Trading pair
fundingRate	String	Current funding rates
collectCycle	Long	Funding rate settlement cycle
Unit: minute
timestamp	Long	Funding fee settlement time
Unix millisecond timestamp
Response example

[
  {
    "symbol": "cmt_btcusdt",
    "fundingRate": "-0.0001036",
    "collectCycle": 480,
    "timestamp": 1750383726052
  }
]


argin Mode
Field	Value	Field Description
UNKNOWN_MARGIN_MODE	0	None
SHARED	1	Cross Mode
ISOLATED	3	Isolated Mode
Previous
Modify TP/SL Order
Next
Separated Mode
Separated Mode
Field	Value	Field Description
UNKNOWN_SEPARATED_MODE	0	None
COMBINED	1	Combined mode
SEPARATED	2	Separated mode
Previous
Margin Mode
Next
Position Mode
Position Mode
Field	Value	Field Description
UNKNOWN_POSITION_MODE	0	None
HEDGE	2	Bidirectional mod




WebSocket API
Overview
WebSocket is a new protocol in HTML5 that enables full-duplex communication between clients and servers, allowing rapid bidirectional data transmission. Through a simple handshake, a connection can be established between client and server, enabling the server to actively push information to the client based on business rules. Its advantages include:

Small header size (~2 bytes) during data transmission between client and server
Both client and server can actively send data
Eliminates the need for repeated TCP connection setup/teardown, conserving bandwidth and server resources
Strongly recommended for developers to obtain market data, order book depth, and other information
Domain	WebSocket API	Recommended Use
Public Channel	wss://ws-contract.weex.com/v2/ws/public	Primary domain, public channels
Private Channel	wss://ws-contract.weex.com/v2/ws/private	Primary domain, private channels
Connection
Connection Specifications:

Connection limit: 300 connection requests/IP/5 minutes, maximum 100 concurrent connections per IP

Subscription limit: 240 operations/hour/connection, maximum 100 channels per connection

Public channel requirement: Public channel connections require header authentication(User-Agent)

Private channel requirement: Private channel connections require header authentication

To maintain stable and effective connections, we recommend:

After successful WebSocket connection establishment, the server will periodically send Ping messages to the client in the format: {"event":"ping","time":"1693208170000"}, where "time" represents the server's timestamp. Upon receiving this message, the client should respond with a Pong message: {"event":"pong","time":"1693208170000"}. The server will actively terminate connections that fail to respond more than 5 times.

Header Authentication for Private Channels
User-Agent:Client identification

ACCESS-KEY: Unique identifier for API user authentication (requires application)

ACCESS-PASSPHRASE: Password for the API Key

ACCESS-TIMESTAMP: Unix Epoch timestamp in milliseconds (expires after 30 seconds, must match signature timestamp)

ACCESS-SIGN: Signature string generated as follows:

The message (string to be signed) consists of: timestamp + requestPath

Example timestamp (in milliseconds): const timestamp = '' + Date.now()

Where requestPath is /v2/ws/private

Signature Generation Process

Encrypt the message string using HMAC SHA256 with the secret key:
Signature = hmac_sha256(secretkey, Message)
Encode the Signature using Base64:
Signature = base64.encode(Signature)
Subscription
Subscription Specification:

{
  "event": "subscribe",
  "channel": "channel_name"
}

Unsubscription
Unsubscription Specification:

{
   "event": "unsubscribe",
   "channel": "channel_name"
}


Market Channel
Description
Retrieves real-time market data including latest price, best bid/ask prices, and 24-hour trading volume. Updates occur within 100-300ms when changes occur (trades, bid/ask updates).

Request Parameters

Parameter	Type	Required	Description
event	String	Yes	Operation: subscribe / unsubscribe
channel	String	Yes	Channel name.format: ticker.{contractId}
Example: ticker.cmt_btcusdt
Request Example

{  
  "event": "subscribe",  
  "channel": "ticker.cmt_btcusdt"  
}

Response Parameters

Field	Type	Description
event	String	Operation: subscribed / unsubscribed
channel	String	Channel name (e.g. ticker.cmt_btcusdt)
Subscription Response Example

{  
  "event": "subscribed",  
  "channel": "ticker.cmt_btcusdt"  
}  

Push Data Parameters

Field	Type	Description
event	String	Push action
channel	String	Channel name (e.g. ticker.cmt_btcusdt)
data	List	Market data array
>symbol	String	Product ID
>priceChange	String	Price change amount
>priceChangePercent	String	Price change percentage
>trades	String	24h trade count
>size	String	24h trading volume
>value	String	24h trading value
>high	String	24h highest price
>low	String	24h lowest price
>lastPrice	String	Latest traded price
>markPrice	String	Current mark price
Push Data Example

{  
  "event": "payload",  
  "channel": "ticker.cmt_btcusdt",  
  "data": [  
    {  
      "symbol": "cmt_btcusdt",  
      "priceChange": "-2055.6",  
      "priceChangePercent": "-0.019637",  
      "trades": "28941",  
      "size": "176145.66489",  
      "value": "18115688543.1",  
      "high": "104692.2",  
      "low": "100709.6",  
      "lastPrice": "102623.9",  
      "markPrice": "102623.9"  
    }  
  ]  
}  


Candlestick Channel
Description
Order K-line channel

Request Parameters

Parameter	Type	Required	Description
event	String	Yes	Operation: subscribe / unsubscribe
channel	String	Yes	Channel name.format: kline.{priceType}.{contractId}.{interval}
Example: kline.LAST_PRICE.cmt_btcusdt.MINUTE_1
priceType Parameters

Value	Description
LAST_PRICE	Latest price K-line
MARK_PRICE	Mark price K-line
interval Parameters

Value	Description
MINUTE_1	1-minute
MINUTE_5	5-minute
MINUTE_15	15-minute
MINUTE_30	30-minute
HOUR_1	1-hour
HOUR_2	2-hour
HOUR_4	4-hour
HOUR_6	6-hour
HOUR_8	8-hour
HOUR_12	12-hour
DAY_1	Daily
WEEK_1	Weekly
MONTH_1	Monthly
Request Example

{  
  "event": "subscribe",  
  "channel": "kline.LAST_PRICE.cmt_btcusdt.MINUTE_1"  
}  

Response Parameters

Field	Type	Description
event	String	Operation: subscribed / unsubscribed
channel	String	Channel name
Subscription Response Example

{  
    "event": "subscribed",  
    "channel": "kline.LAST_PRICE.cmt_btcusdt.MINUTE_1"  
}  


Push Data Parameters

Field	Type	Description
event	String	Push action
type	String	Type: change (incremental), snapshot (full)
channel	String	Channel name
data	List	Subscribed data
>symbol	String	Product ID
>klineTime	String	K-line timestamp
>size	String	Trading volume
>value	String	Trading amount
>high	String	Highest price
>low	String	Lowest price
>open	String	Opening price
>close	String	Closing price
Push Data Example

{
  "event": "payload",
  "type": "change",
  "channel": "kline.LAST_PRICE.cmt_btcusdt.MINUTE_1",
  "data": [
    {
      "symbol": "cmt_btcusdt",
      "klineTime": "1747125660000",
      "size": "23.76600",
      "value": "2442678.713400",
      "high": "102784.6",
      "low": "102760.6",
      "open": "102760.6",
      "close": "102764.0"
    }
  ]
}



Depth Channel
Description

Retrieves order book depth data

Upon successful subscription, a full snapshot will be pushed initially (depthType=SNAPSHOT), followed by incremental updates (depthType=CHANGED).

Request Parameters

Parameter	Type	Required	Description
event	String	Yes	Operation: subscribe / unsubscribe
channel	String	Yes	Channel name.format: depth.{contractId}.{depth}
Example: depth.cmt_btcusdt.15
depth Parameters

Value	Description
15	15 levels
200	200 levels
Request Example

{  
  "event": "subscribe",  
  "channel": "depth.cmt_btcusdt.15"  
}  

Response Parameters

Field	Type	Description
event	String	Operation: subscribed / unsubscribed
channel	String	Channel name
Subscription Response Example

{  
  "event": "subscribed",  
  "channel": "depth.cmt_btcusdt.15"  
}  

Push Data Parameters

Field	Type	Description
event	String	Push action
channel	String	Channel name
data	List	Subscribed data
>startVersion	String	Starting order book version
>endVersion	String	Ending order book version
>level	String	Depth level
>depthType	String	Order book depth type
>symbol	String	Product ID
>asks	String	Ask list
>>price	String	Price level
>>size	String	Quantity at price level
>bids	String	Bid list
>>price	String	Price level
>>size	String	Quantity at price level
Push Data Example

{  
  "event": "payload",  
  "channel": "depth.cmt_btcusdt.15",  
  "data": [  
    {  
      "startVersion": "3644174246",  
      "endVersion": "3644174270",  
      "level": 15,  
      "depthType": "CHANGED",  
      "symbol": "cmt_btcusdt",  
      "asks": [  
        {  
          "price": "103436.1",  
          "size": "0.91500"  
        },  
        {  
          "price": "103436.3",  
          "size": "1.95800"  
        },  
        {  
          "price": "103436.5",  
          "size": "0"  
        },  
        {  
          "price": "103436.6",  
          "size": "1.08300"  
        },  
        {  
          "price": "103436.7",  
          "size": "7.64700"  
        },  
        {  
          "price": "103436.9",  
          "size": "7.23100"  
        },  
        {  
          "price": "103437.0",  
          "size": "0"  
        },  
        {  
          "price": "103437.2",  
          "size": "0"  
        }  
      ],  
      "bids": [  
        {  
          "price": "103435.9",  
          "size": "2.40500"  
        },  
        {  
          "price": "103435.7",  
          "size": "0"  
        },  
        {  
          "price": "103435.6",  
          "size": "0.32700"  
        },  
        {  
          "price": "103435.5",  
          "size": "0"  
        },  
        {  
          "price": "103435.2",  
          "size": "3.19400"  
        },  
        {  
          "price": "103434.8",  
          "size": "10.25000"  
        },  
        {  
          "price": "103434.5",  
          "size": "11.13900"  
        }  
      ]  
    }  
  ]  
}  


Public Trade Channel
Description

Platform trade channel (taker orders)

Request Parameters

Parameter	Type	Required	Description
event	String	Yes	Operation: subscribe, unsubscribe
channel	String	Yes	Channel name. Product ID
e.g., trades.cmt_btcusdt
Request Example

{  
  "event": "subscribe",  
  "channel": "trades.cmt_btcusdt"  
}  

Response Parameters

Field	Type	Description
event	String	Operation: subscribed, unsubscribed
channel	String	Channel name
Subscription Response Example

{  
  "event": "subscribed",  
  "channel": "trades.cmt_btcusdt"  
}  

Push Data Parameters

Field	Type	Description
event	String	Push data action
channel	String	Channel name
data	List	Subscribed data
>time	String	Trade time
>price	String	Trade price
>size	String	Trade quantity
>value	String	Trade amount
>buyerMaker	String	Market flag (internal/external)
Push Response Example

{
  "event": "payload",
  "channel": "trades.cmt_btcusdt",
  "data": [
    {
      "time": "1747131727502",
      "price": "103337.5",
      "size": "0.01600",
      "value": "1653.400000",
      "buyerMaker": false
    }
  ]
}

Error Code Examples
All APIs may return exceptions.

The following are possible error codes returned by the API

Error Message	Error Code	HTTP Status Code
Header "ACCESS_KEY" is required	40001	400
Header "ACCESS_SIGN" is required	40002	400
Header "ACCESS_TIMESTAMP" is required	40003	400
Invalid ACCESS_TIMESTAMP	40005	400
Invalid ACCESS_KEY	40006	400
Invalid Content_Type, use "application/json" format	40007	400
Request timestamp expired	40008	400
API verification failed	40009	400
Too many requests	429	429
Header "ACCESS_PASSPHRASE" is required	40011	400
Incorrect API key/Passphrase	40012	400
Account frozen	40013	400
Invalid permissions	40014	400
System error	40015	400
Parameter validation failed	40017	400
Invalid IP request	40018	400
Parameter cannot be empty	40019	400
Parameter is invalid	40020	400
API permission disabled	40753	400
Insufficient permissions for this operation	40022	403
Not have permission to trade this pair.	50003	400
Not have permission to access this API.	50004	400
Order does not exist	50005	400
Leverage cannot exceed the limit	50007	400
Error Response Format
All errors return a JSON response in the following format:

{
  "code": "error code",
  "msg": "error description",
  "requestTime": 1765776384556,
  "data": null
}

Example 1: Parameter Error
{
  "code": "40020",
  "msg": "Parameter symbol is invalid",
  "requestTime": 1765776928145,
  "data": null
}