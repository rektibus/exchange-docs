Overview
Spot API Overview¶
This document lists the base URL for the API endpoints: https://sapi.asterdex.com
All API responses are in JSON format.
All times and timestamps are in UNIX time, in milliseconds.
API Key settings¶
Many endpoints require an API Key to access.
When setting the API Key, for security reasons it is recommended to set an IP access whitelist.
Never reveal your API key/secret to anyone.
If an API Key is accidentally exposed, immediately delete that Key and generate a new one.

Attention¶
TESTUSDT or any other symbols starting with TEST are symbols used for Aster’s INTERNAL TESTING ONLY. Please DO NOT trade on these symbols starting with TEST. Aster does not hold any accountability for loss of funds due to trading on these symbols. However, if you run into issues, you may contact support about this any time, we will try to help you recover your funds.
HTTP return codes¶
HTTP 4XX status codes are used to indicate errors in the request content, behavior, or format. The problem lies with the requester.
HTTP 403 status code indicates a violation of WAF restrictions (Web Application Firewall).
HTTP 429 error code indicates a warning that the access frequency limit has been exceeded and the IP is about to be blocked.
HTTP 418 indicates that after receiving a 429 you continued to access, so the IP has been blocked.
HTTP 5XX error codes are used to indicate issues on the Aster service side.
API error codes¶
When using the endpoint /api/v1, any endpoint may throw exceptions;
The API error codes are returned in the following format:


{
  "code": -1121,
  "msg": "Invalid symbol."
}
Basic information about the endpoint¶
Endpoints with the GET method must send parameters in the query string.
For POST, PUT, and DELETE endpoints, parameters can be sent in the query string with content type application/x-www-form-urlencoded , or in the request body.
The order of parameters is not required.
Access restrictions¶
Basic information on access restrictions¶
The rateLimits array in /api/v1/exchangeInfo contains objects related to REQUEST_WEIGHT and ORDERS rate limits for trading. These are further defined in the enum definitions section under rateLimitType.
A 429 will be returned when any of the rate limits are violated.
IP access limits¶
Each request will include a header named X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter) that contains the used weight of all requests from the current IP.
Each endpoint has a corresponding weight, and some endpoints may have different weights depending on their parameters. The more resources an endpoint consumes, the higher its weight will be.
Upon receiving a 429, you are responsible for stopping requests and must not abuse the API.
If you continue to violate access limits after receiving a 429, your IP will be banned and you will receive a 418 error code.
Repeated violations of the limits will result in progressively longer bans, from a minimum of 2 minutes up to a maximum of 3 days.
The Retry-After header will be sent with responses bearing 418 or 429, and will give the wait time in seconds (if 429) to avoid the ban, or, if 418, until the ban ends.
Access restrictions are based on IP, not API Key
You are advised to use WebSocket messages to obtain the corresponding data as much as possible to reduce the load and rate-limit pressure from requests.

Order rate limits¶
Each successful order response will include a X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter) header containing the number of order limit units currently used by the account.
When the number of orders exceeds the limit, you will receive a response with status 429 but without the Retry-After header. Please check the order rate limits in GET api/v1/exchangeInfo (rateLimitType \= ORDERS) and wait until the ban period ends.
Rejected or unsuccessful orders are not guaranteed to include the above header in the response.
Order placement rate limits are counted per account.
WebSocket connection limits¶
The WebSocket server accepts a maximum of 5 messages per second. Messages include:
PING frame
PONG frame
Messages in JSON format, such as subscribe and unsubscribe.
If a user sends messages that exceed the limit, the connection will be terminated. IPs that are repeatedly disconnected may be blocked by the server.
A single connection can subscribe to up to 1024 Streams.
API authentication types¶
Each API has its own authentication type, which determines what kind of authentication should be performed when accessing it.
The authentication type will be indicated next to each endpoint name in this document; if not specifically stated, it defaults to NONE.
If API keys are required, they should be passed in the HTTP header using the X-MBX-APIKEY field.
API keys and secret keys are case-sensitive.
By default, API keys have access to all authenticated routes.
Authentication type	Description
NONE	APIs that do not require authentication
TRADE	A valid API-Key and signature are required
USER_DATA	A valid API-Key and signature are required
USER_STREAM	A valid API-Key is required
MARKET_DATA	A valid API-Key is required
The TRADE and USER_DATA endpoints are signed (SIGNED) endpoints.
SIGNED (TRADE AND USER_DATA) Endpoint security¶
When calling a SIGNED endpoint, in addition to the parameters required by the endpoint itself, you must also pass a signature parameter in the query string or request body.
The signature uses the HMAC SHA256 algorithm. The API-Secret corresponding to the API-KEY is used as the key for HMAC SHA256, and all other parameters are used as the data for the HMAC SHA256 operation; the output is the signature.
The signature is case-insensitive.
"totalParams" is defined as the "query string" concatenated with the "request body".
Time synchronization safety¶
Signed endpoints must include the timestamp parameter, whose value should be the unix timestamp (milliseconds) at the moment the request is sent.
When the server receives a request it will check the timestamp; if it was sent more than 5,000 milliseconds earlier, the request will be considered invalid. This time window value can be defined by sending the optional recvWindow parameter.
The logical pseudocode is as follows:


  if (timestamp < (serverTime + 1000) && (serverTime - timestamp) <= recvWindow)
  {
    // process request
  } 
  else 
  {
    // reject request
  }
About trade timeliness Internet conditions are not completely stable or reliable, so the latency from your client to Aster's servers will experience jitter. This is why we provide recvWindow; if you engage in high-frequency trading and have strict requirements for timeliness, you can adjust recvWindow flexibly to meet your needs.

It is recommended to use a recvWindow of under 5 seconds. It must not exceed 60 seconds.

Example of POST /api/v1/order¶
Below is an example of placing an order by calling the API using echo, openssl, and curl tools in a Linux bash environment. The apiKey and secretKey are for demonstration only.

Key	Value
apiKey	4452d7e2ed4da80b74105e02d06328c71a34488c9fdd60a5a0900d42d584b795
secretKey	fdde510a2b71fa43a43bff3e3cf7819c8c66df34633d338050f4f59664b3b313
Parameters	Values
symbol	BNBUSDT
side	BUY
type	LIMIT
timeInForce	GTC
quantity	5
price	1.1
recvWindow	5000
timestamp	1756187806000
Example 1: All parameters are sent through the request body¶
Example 1 HMAC SHA256 signature:


    $ echo -n "symbol=BNBUSDT&side=BUY&type=LIMIT&timeInForce=GTC&quantity=5&price=1.1&recvWindow=5000&timestamp=1756187806000" | openssl dgst -sha256 -hmac "fdde510a2b71fa43a43bff3e3cf7819c8c66df34633d338050f4f59664b3b313"
    (stdin)= e09169bf6c02ec4b29fa1bdc3a967f92c8c6cfcde0551ba1d477b2d3cf4c51b0
curl command:


    (HMAC SHA256)
    $ curl -H "X-MBX-APIKEY: 4452d7e2ed4da80b74105e02d06328c71a34488c9fdd60a5a0900d42d584b795" -X POST 'https://sapi.asterdex.com/api/v1/order' -d 'symbol=BNBUSDT&side=BUY&type=LIMIT&timeInForce=GTC&quantity=5&price=1.1&recvWindow=5000&timestamp=1756187806000&signature=e09169bf6c02ec4b29fa1bdc3a967f92c8c6cfcde0551ba1d477b2d3cf4c51b0'
requestBody:
symbol=BNBUSDT \&side=BUY \&type=LIMIT \&timeInForce=GTC \&quantity=5 \&price=1.1 \&recvWindow=5000 \&timestamp=1756187806000

Example 2: All parameters sent through the query string¶
Example 2 HMAC SHA256 signature:


    $ echo -n "symbol=BNBUSDT&side=BUY&type=LIMIT&timeInForce=GTC&quantity=5&price=1.1&recvWindow=5000&timestamp=1756187806000" | openssl dgst -sha256 -hmac "fdde510a2b71fa43a43bff3e3cf7819c8c66df34633d338050f4f59664b3b313"
    (stdin)= e09169bf6c02ec4b29fa1bdc3a967f92c8c6cfcde0551ba1d477b2d3cf4c51b0 
curl command:


    (HMAC SHA256)
   $ curl -H "X-MBX-APIKEY: 4452d7e2ed4da80b74105e02d06328c71a34488c9fdd60a5a0900d42d584b795" -X POST 'https://sapi.asterdex.com/api/v1/order?symbol=BNBUSDT&side=BUY&type=LIMIT&timeInForce=GTC&quantity=5&price=1.1&recvWindow=5000&timestamp=1756187806000&signature=e09169bf6c02ec4b29fa1bdc3a967f92c8c6cfcde0551ba1d477b2d3cf4c51b0'
queryString:
symbol=BNBUSDT \&side=BUY \&type=LIMIT \&timeInForce=GTC \&quantity=5 \&price=1.1 \&recvWindow=5000 \&timestamp=1756187806000

Public API parameters¶
Terminology¶
The terminology in this section applies throughout the document. New users are encouraged to read it carefully for better understanding.

base asset refers to the asset being traded in a trading pair, i.e., the asset name written first; for example, in BTCUSDT, BTC is the base asset.
quote asset refers to the pricing asset of a trading pair, i.e., the asset name written at the latter part; for example, in BTCUSDT, USDT is the quote asset.
Enumeration definition¶
Trading pair status (status):

TRADING - after trade
Trading pair type:

SPOT - spot
Order status (status):

Status	Description
NEW	Order accepted by the matching engine
PARTIALLY_FILLED	Part of the order was filled
FILLED	The order was fully filled
CANCELED	The user canceled the order
REJECTED	The order was not accepted by the matching engine and was not processed
EXPIRED	Order canceled by the trading engine, for example: Limit FOK order not filled, Market order not fully filled, orders canceled during exchange maintenance
Order types (orderTypes, type):

LIMIT - Limit Order
MARKET - Market Order
STOP - Limit Stop Order
TAKE_PROFIT - Limit Take-Profit Order
STOP_MARKET - Market Stop Order
TAKE_PROFIT_MARKET - Market Take-Profit Order
Order response type (newOrderRespType):

ACK
RESULT
FULL
Order direction (direction side):

BUY - Buy
SELL - Sell
Valid types (timeInForce):

This defines how long an order can remain valid before expiring.

Status	Description
GTC (Good ‘Til Canceled)	The order remains active until it is fully executed or manually canceled.
IOC (Immediate or Cancel)	The order will execute immediately for any amount available. Any unfilled portion is automatically canceled.
FOK (Fill or Kill)	The order must be fully executed immediately. If it cannot be filled in full, it is canceled right away.
GTX (Good till crossing, Post only)	The post-only limit order will only be placed if it can be added as a maker order and not as a taker order.
K-line interval:

m (minutes), h (hours), d (days), w (weeks), M (months)

1m
3m
5m
15m
30m
1h
2h
4h
6h
8h
12h
1d
3d
1w
1M
Rate limit type (rateLimitType)

REQUEST_WEIGHT


    {
      "rateLimitType": "REQUEST_WEIGHT",
      "interval": "MINUTE",
      "intervalNum": 1,
      "limit": 1200
    }
ORDERS


    {
      "rateLimitType": "ORDERS",
      "interval": "MINUTE",
      "intervalNum": 1,
      "limit": 100
    }
REQUEST_WEIGHT - The maximum sum of request weights allowed within a unit time

ORDERS - Order placement frequency limit per time unit

Interval restriction (interval)

MINUTE - Minute
Filters¶
Filters, i.e. Filter, define a set of trading rules. There are two types: filters for trading pairs symbol filters, and filters for the entire exchange exchange filters (not supported yet)

Trading pair filters¶
PRICE_FILTER Price filter¶
Format in the /exchangeInfo response:


  {                     
    "minPrice": "556.72",
    "maxPrice": "4529764",
    "filterType": "PRICE_FILTER",
    "tickSize": "0.01"   
  }
The Price Filter checks the validity of the price parameter in an order. It consists of the following three parts:

minPrice defines the minimum allowed value for price/stopPrice.
maxPrice defines the maximum allowed value for price/stopPrice.
tickSize defines the step interval for price/stopPrice, meaning the price must equal minPrice plus an integer multiple of tickSize.
Each of the above items can be 0; when 0 it means that item is not constrained.

The logical pseudocode is as follows:

price >= minPrice
price \<= maxPrice
(price-minPrice) % tickSize \== 0
PERCENT_PRICE price amplitude filter¶
Format in the /exchangeInfo response:


  {                    
    "multiplierDown": "0.9500",
    "multiplierUp": "1.0500",
    "multiplierDecimal": "4",
    "filterType": "PERCENT_PRICE"
  }
The PERCENT_PRICE filter defines the valid range of prices based on the index price.

For the "price percentage" to apply, the "price" must meet the following conditions:

price \<=indexPrice *multiplierUp
price> \=indexPrice *multiplierDown
LOT_SIZE order size¶
Format in the /exchangeInfo response:


  {
    "stepSize": "0.00100000",
    "filterType": "LOT_SIZE",
    "maxQty": "100000.00000000",
    "minQty": "0.00100000"
  }
Lots is an auction term. The LOT_SIZE filter validates the quantity (i.e., the amount) parameter in orders. It consists of three parts:

minQty indicates the minimum allowed value for quantity.
maxQty denotes the maximum allowed value for quantity.
stepSize denotes the allowed step increment for quantity.
The logical pseudocode is as follows:

quantity >= minQty
quantity \<= maxQty
(quantity-minQty) % stepSize \== 0
MARKET_LOT_SIZE - Market order size¶
*/exchangeInfo response format:


  {
    "stepSize": "0.00100000",
    "filterType": "MARKET_LOT_SIZE"
    "maxQty": "100000.00000000",
    "minQty": "0.00100000"
  }
The MARKET_LOT_SIZE filter defines the quantity (i.e., the "lots" in an auction) rules for MARKET orders on a trading pair. There are three parts:

minQty defines the minimum allowed quantity.
maxQty defines the maximum allowed quantity.
stepSize defines the increments by which the quantity can be increased or decreased.
In order to comply with the market lot size, the quantity must satisfy the following conditions:

quantity >= minQty
quantity \<= maxQty
(quantity-minQty) % stepSize \== 0





Market Data
Test server connectivity¶
Response


{}
GET /api/v1/ping

Test whether the REST API can be reached.

Weight: 1

Parameters: NONE

Get server time¶
Response


{
  "serverTime": 1499827319559
}
GET /api/v1/time

Test if the REST API can be reached and retrieve the server time.

Weight: 1

Parameters: NONE

Trading specification information¶
Response


{
    "timezone": "UTC",
    "serverTime": 1756197279679,
    "rateLimits": [{
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 300
        }
    ],
    "exchangeFilters": [],
    "assets": [{
            "asset": "USD"
        }, {
            "asset": "USDT"
        },
        {
            "asset": "BNB"
        }
    ],
    "symbols": [{
        "status": "TRADING",
        "baseAsset": "BNB",
        "quoteAsset": "USDT",
        "pricePrecision": 8,
        "quantityPrecision": 8,
        "baseAssetPrecision": 8,
        "quotePrecision": 8,
        "filters": [{
                "minPrice": "0.01000000",
                "maxPrice": "100000",
                "filterType": "PRICE_FILTER",
                "tickSize": "0.01000000"
            },
            {
                "stepSize": "0.00100000",
                "filterType": "LOT_SIZE",
                "maxQty": "1000",
                "minQty": "1"
            },
            {
                "stepSize": "0.00100000",
                "filterType": "MARKET_LOT_SIZE",
                "maxQty": "900000",
                "minQty": "0.00100000"
            },
            {
                "limit": 200,
                "filterType": "MAX_NUM_ORDERS"
            },
            {
                "minNotional": "5",
                "filterType": "MIN_NOTIONAL"
            },
            {
                "maxNotional": "100",
                "filterType": "MAX_NOTIONAL"
            },
            {
                "maxNotional": "100",
                "minNotional": "5",
                "avgPriceMins": 5,
                "applyMinToMarket": true,
                "filterType": "NOTIONAL",
                "applyMaxToMarket": true
            },
            {
                "multiplierDown": "0",
                "multiplierUp": "5",
                "multiplierDecimal": "0",
                "filterType": "PERCENT_PRICE"
            },
            {
                "bidMultiplierUp": "5",
                "askMultiplierUp": "5",
                "bidMultiplierDown": "0",
                "avgPriceMins": 5,
                "multiplierDecimal": "0",
                "filterType": "PERCENT_PRICE_BY_SIDE",
                "askMultiplierDown": "0"
            }
        ],
        "orderTypes": [
            "LIMIT",
            "MARKET",
            "STOP",
            "STOP_MARKET",
            "TAKE_PROFIT",
            "TAKE_PROFIT_MARKET"
        ],
        "timeInForce": [
            "GTC",
            "IOC",
            "FOK",
            "GTX"
        ],
        "symbol": "BNBUSDT",
        "ocoAllowed": false
    }]
}
GET /api/v1/exchangeInfo

Retrieve trading rules and trading pair information.

Weight: 1

Parameters: None

Depth information¶
Response


{
  "lastUpdateId": 1027024,
  "E":1589436922972, //  Message output time
  "T":1589436922959, //  Transaction time
  "bids": [
    [
      "4.00000000", // PRICE
      "431.00000000" // QTY
    ]
  ],
  "asks": [
    [
      "4.00000200",
      "12.00000000"
    ]
  ]
}
GET /api/v1/depth

Weight:

Based on limit adjustments:

Limitations	Weight
5, 10, 20, 50	2
100	5
500	10
1000	20
Parameters:

Name	Type	Is it required?	Description
symbol	STRING	YES	
limit	INT	NO	Default 100. Optional values: [5, 10, 20, 50, 100, 500, 1000]
Recent trades list¶
Response


[
 {
    "id": 657,
    "price": "1.01000000",
    "qty": "5.00000000",
    "baseQty": "4.95049505",
    "time": 1755156533943,
    "isBuyerMaker": false
  }
]
GET /api/v1/trades

Get recent trades

Weight: 1

Parameters:

Name	Type	Is it required?	Description
symbol	STRING	YES	
limit	INT	NO	Default 500; maximum 1000
Query historical trades (MARKET_DATA)¶
Response


[
 {
    "id": 1140,
    "price": "1.10000000",
    "qty": "7.27200000",
    "baseQty": "6.61090909",
    "time": 1756094288700,
    "isBuyerMaker": false
 }
]
GET /api/v1/historicalTrades

Retrieve historical trades

Weight: 20

Parameters:

Name	Type	Is it required?	Description
symbol	STRING	YES	
limit	INT	NO	Default 500; maximum 1000.
fromId	LONG	NO	Return starting from which trade id. Defaults to returning the most recent trade records.
Recent trades (aggregated)¶
Response


[
  {
    "a": 26129, // Aggregate tradeId
    "p": "0.01633102", // Price
    "q": "4.70443515", // Quantity
    "f": 27781, // First tradeId
    "l": 27781, // Last tradeId
    "T": 1498793709153, // Timestamp
    "m": true, // Was the buyer the maker?
  }
]
GET /api/v1/aggTrades

The difference between aggregated trades and individual trades is that trades with the same price, same side, and same time are combined into a single entry.

Weight: 20

Parameters:

Name	Type	Is it required?	Description
symbol	STRING	YES	
fromId	LONG	NO	Return results starting from the trade ID that includes fromId
startTime	LONG	NO	Return results starting from trades after that time
endTime	LONG	NO	Return the trade records up to that moment
limit	INT	NO	Default 500; maximum 1000.
If you send startTime and endTime, the interval must be less than one hour.
If no filter parameters (fromId, startTime, endTime) are sent, the most recent trade records are returned by default
K-line data¶
Response


[
  [
    1499040000000, // Open time
    "0.01634790", // Open
    "0.80000000", // High
    "0.01575800", // Low
    "0.01577100", // Close
    "148976.11427815", // Volume
    1499644799999, // Close time
    "2434.19055334", // Quote asset volume
    308, // Number of trades
    "1756.87402397", // Taker buy base asset volume
    "28.46694368", // Taker buy quote asset volume
  ]
]
GET /api/v1/klines

Each K-line represents a trading pair. The open time of each K-line can be regarded as a unique ID.

Parameters:

Name	Type	Is it required?	Description
symbol	STRING	YES	
interval	ENUM	YES	See the enumeration definition: K-line interval
startTime	LONG	NO	
endTime	LONG	NO	
limit	INT	NO	Default 500; maximum 1500.
If startTime and endTime are not sent, the most recent trades are returned by default
24h price change¶
Response


{
  "symbol": "BTCUSDT",              //symbol
  "priceChange": "-94.99999800",    //price change
  "priceChangePercent": "-95.960",  //price change percent
  "weightedAvgPrice": "0.29628482", //weighted avgPrice
  "prevClosePrice": "3.89000000",   //prev close price
  "lastPrice": "4.00000200",        //last price
  "lastQty": "200.00000000",        //last qty
  "bidPrice": "866.66000000",       //first bid price
  "bidQty": "72.05100000",          //first bid qty
  "askPrice": "866.73000000",       //first ask price
  "askQty": "1.21700000",           //first ask qty
  "openPrice": "99.00000000",       //open price
  "highPrice": "100.00000000",      //high price
  "lowPrice": "0.10000000",         //low price
  "volume": "8913.30000000",        //volume
  "quoteVolume": "15.30000000",     //quote volume
  "openTime": 1499783499040,        //open time
  "closeTime": 1499869899040,       //close time
  "firstId": 28385,   // first id
  "lastId": 28460,    // last id
  "count": 76,         // count
  "baseAsset": "BTC",   //base asset
  "quoteAsset": "USDT"  //quote asset
}
GET /api/v1/ticker/24hr

24-hour rolling window price change data. Please note that omitting the symbol parameter will return data for all trading pairs; in that case the returned data is an example array for the respective pairs, which is not only large in volume but also has a very high weight.

Weight: 1 \= single trading pair; 40 \= When the trading pair parameter is missing (returns all trading pairs)

Parameters:

Name	Type	Is it required?	Description
symbol	STRING	NO	
Please note that omitting the symbol parameter will return data for all trading pairs
Latest price¶
Response


{
   "symbol": "ADAUSDT",
   "price": "1.30000000",
   "time": 1649666690902
}  
OR


[     
  {
     "symbol": "ADAUSDT",
     "price": "1.30000000",
     "time": 1649666690902
  }
]
GET /api/v1/ticker/price

Get the latest price for a trading pair

Weight: 1 \= Single trading pair; 2 \= No symbol parameter (returns all pairs)

Parameters:

Name	Type	Is it required?	Description
symbol	STRING	NO	
If no trading pair parameter is sent, information for all trading pairs will be returned
Current best order¶
Response


{
  "symbol": "LTCBTC",
  "bidPrice": "4.00000000",
  "bidQty": "431.00000000",
  "askPrice": "4.00000200",
  "askQty": "9.00000000"
  "time": 1589437530011   // Timestamp
}
OR


[
  {
    "symbol": "LTCBTC",
    "bidPrice": "4.00000000",
    "bidQty": "431.00000000",
    "askPrice": "4.00000200",
    "askQty": "9.00000000",
    "time": 1589437530011   // Timestamp
  }
]
GET /api/v1/ticker/bookTicker

Return the current best orders (highest bid, lowest ask)

Weight: 1 \= Single trading pair; 2 \= No symbol parameter (returns all pairs)

Parameters:

Name	Type	Is it required?	Description
symbol	STRING	NO	
If no trading pair parameter is sent, information for all trading pairs will be returned
Get symbol fees¶
Response


{
   "symbol": "APXUSDT",
   "makerCommissionRate": "0.000200",    
   "takerCommissionRate": "0.000700"
}
GET /api/v1/commissionRate

Get symbol fees

Weight: 20

Parameters:

Name	Type	Is it required?	Description
symbol	STRING	YES	
recvWindow	LONG	NO	The assigned value cannot be greater than 60000
timestamp	LONG	YES	




Error Codes
Error code¶
error JSON payload:


{
  "code":-1121,
  "msg":"Invalid symbol."
}
Errors consist of two parts: an error code and a message. The code is standardized, but the message may vary.

10xx - General server or network issues¶
-1000 UNKNOWN¶
An unknown error occurred while processing the request.
-1001 DISCONNECTED¶
Internal error; unable to process your request. Please try again.
-1002 UNAUTHORIZED¶
You are not authorized to execute this request.
-1003 TOO_MANY_REQUESTS¶
Too many requests queued.
Too many requests; please use the WebSocket for live updates.
Too many requests; current limit is %s requests per minute. Please use the WebSocket for live updates to avoid polling the API.
Too many request weights; IP banned until %s. Please use the WebSocket for live updates to avoid bans.
-1004 DUPLICATE_IP¶
This IP is already on the white list.
-1005 NO_SUCH_IP¶
No such IP has been whitelisted.
-1006 UNEXPECTED_RESP¶
An unexpected response was received from the message bus. Execution status unknown.
-1007 TIMEOUT¶
Timeout waiting for response from backend server. Send status unknown; execution status unknown.
-1014 UNKNOWN_ORDER_COMPOSITION¶
The current order parameter combination is not supported.
-1015 TOO_MANY_ORDERS¶
Too many new orders.
Too many new orders; the current limit is %s orders per %s.
-1016 SERVICE_SHUTTING_DOWN¶
This service is no longer available.
-1020 UNSUPPORTED_OPERATION¶
This operation is not supported.
-1021 INVALID_TIMESTAMP¶
Timestamp for this request is outside of the recvWindow.
The timestamp for this request was 1000ms ahead of the server's time.
-1022 INVALID_SIGNATURE¶
The signature for this request is invalid.
-1023 START_TIME_GREATER_THAN_END_TIME¶
The start time in the parameters is after the end time.
11xx - Request issues¶
-1100 ILLEGAL_CHARS¶
Illegal characters found in a parameter.
Illegal characters found in parameter %s; legal range is %s.
-1101 TOO_MANY_PARAMETERS¶
Too many parameters sent for this endpoint.
Too many parameters; expected %s and received %s.
Duplicate values for a parameter detected.
-1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED¶
A mandatory parameter was not sent, was empty/null, or malformed.
Mandatory parameter %s was not sent, was empty/null, or malformed.
Param %s or %s must be sent, but both were empty/null.
-1103 UNKNOWN_PARAM¶
An unknown parameter was sent.
-1104 UNREAD_PARAMETERS¶
Not all sent parameters were read.
Not all sent parameters were read; read %s parameter(s) but %s parameter(s) were sent.
-1105 PARAM_EMPTY¶
A parameter was empty.
Parameter %s was empty.
-1106 PARAM_NOT_REQUIRED¶
A parameter was sent when not required. 
-1111 BAD_PRECISION¶
The precision exceeds the maximum defined for this asset.
-1112 NO_DEPTH¶
No open orders for the trading pair.
-1114 TIF_NOT_REQUIRED¶
TimeInForce parameter sent when not required.
-1115 INVALID_TIF¶
Invalid timeInForce.
-1116 INVALID_ORDER_TYPE¶
Invalid orderType.
-1117 INVALID_SIDE¶
Invalid order side.
-1118 EMPTY_NEW_CL_ORD_ID¶
New client order ID was empty.
-1119 EMPTY_ORG_CL_ORD_ID¶
The client’s custom order ID is empty.
-1120 BAD_INTERVAL¶
Invalid time interval.
-1121 BAD_SYMBOL¶
Invalid trading pair.
-1125 INVALID_LISTEN_KEY¶
This listenKey does not exist.
-1127 MORE_THAN_XX_HOURS¶
The query interval is too large.
More than %s hours between startTime and endTime.
-1128 OPTIONAL_PARAMS_BAD_COMBO¶
Combination of optional parameters invalid. 
-1130 INVALID_PARAMETER¶
The parameter sent contains invalid data.
Data sent for parameter %s is not valid. 
-1136 INVALID_NEW_ORDER_RESP_TYPE¶
Invalid newOrderRespType. 
20xx - Processing Issues¶
-2010 NEW_ORDER_REJECTED¶
New order rejected.
-2011 CANCEL_REJECTED¶
Order cancellation rejected.
-2013 NO_SUCH_ORDER¶
Order does not exist.
-2014 BAD_API_KEY_FMT¶
API-key format invalid.
-2015 REJECTED_MBX_KEY¶
Invalid API key, IP, or permissions for action.
-2016 NO_TRADING_WINDOW¶
No trading window could be found for the symbol. Try ticker/24hrs instead.
-2018 BALANCE_NOT_SUFFICIENT¶
Balance is insufficient.
-2020 UNABLE_TO_FILL¶
Unable to fill.
-2021 ORDER_WOULD_IMMEDIATELY_TRIGGER¶
Order would immediately trigger.
-2022 REDUCE_ONLY_REJECT¶
ReduceOnly Order is rejected.
-2024 POSITION_NOT_SUFFICIENT¶
Position is not sufficient.
-2025 MAX_OPEN_ORDER_EXCEEDED¶
Reached max open order limit.
-2026 REDUCE_ONLY_ORDER_TYPE_NOT_SUPPORTED¶
This OrderType is not supported when reduceOnly.
40xx - Filters and other Issues¶
-4000 INVALID_ORDER_STATUS¶
Invalid order status.
-4001 PRICE_LESS_THAN_ZERO¶
Price less than 0.
-4002 PRICE_GREATER_THAN_MAX_PRICE¶
Price greater than max price.
-4003 QTY_LESS_THAN_ZERO¶
Quantity less than zero.
-4004 QTY_LESS_THAN_MIN_QTY¶
Quantity less than minimum quantity.
-4005 QTY_GREATER_THAN_MAX_QTY¶
Quantity greater than maximum quantity.
-4006 STOP_PRICE_LESS_THAN_ZERO¶
Stop price less than zero.
-4007 STOP_PRICE_GREATER_THAN_MAX_PRICE¶
Stop price greater than max price.
-4008 TICK_SIZE_LESS_THAN_ZERO¶
Tick size less than zero.
-4009 MAX_PRICE_LESS_THAN_MIN_PRICE¶
Max price less than min price.
-4010 MAX_QTY_LESS_THAN_MIN_QTY¶
Maximum quantity less than minimum quantity.
-4011 STEP_SIZE_LESS_THAN_ZERO¶
Step size less than zero.
-4012 MAX_NUM_ORDERS_LESS_THAN_ZERO¶
Maximum order quantity less than 0.
-4013 PRICE_LESS_THAN_MIN_PRICE¶
Price less than minimum price.
-4014 PRICE_NOT_INCREASED_BY_TICK_SIZE¶
Price not increased by tick size.
-4015 INVALID_CL_ORD_ID_LEN¶
Client order ID is not valid.
Client order ID length should not be more than 36 characters.
-4016 PRICE_HIGHTER_THAN_MULTIPLIER_UP¶
Price is higher than mark price multiplier cap.
-4017 MULTIPLIER_UP_LESS_THAN_ZERO¶
Multiplier up less than zero.
-4018 MULTIPLIER_DOWN_LESS_THAN_ZERO¶
Multiplier down less than zero.
-4019 COMPOSITE_SCALE_OVERFLOW¶
Composite scale too large.
-4020 TARGET_STRATEGY_INVALID¶
Target strategy invalid for orderType %s, reduceOnly %b'
-4021 INVALID_DEPTH_LIMIT¶
Invalid depth limit.
%s is not a valid depth limit.
-4022 WRONG_MARKET_STATUS¶
Market status sent is not valid.
-4023 QTY_NOT_INCREASED_BY_STEP_SIZE¶
The increment of the quantity is not a multiple of the step size.
-4024 PRICE_LOWER_THAN_MULTIPLIER_DOWN¶
Price is lower than mark price multiplier floor.
-4025 MULTIPLIER_DECIMAL_LESS_THAN_ZERO¶
Multiplier decimal less than zero.
-4026 COMMISSION_INVALID¶
Commission invalid.
Incorrect profit value.
%s less than zero.
%s absolute value greater than %s.
-4027 INVALID_ACCOUNT_TYPE¶
Invalid account type.
-4029 INVALID_TICK_SIZE_PRECISION¶
Tick size precision is invalid.
Price decimal precision is incorrect.
-4030 INVALID_STEP_SIZE_PRECISION¶
The number of decimal places for the step size is incorrect.
-4031 INVALID_WORKING_TYPE¶
Invalid parameter working type: %s
-4032 EXCEED_MAX_CANCEL_ORDER_SIZE¶
Exceeds the maximum order quantity that can be canceled.
Invalid parameter working type: %s
-4044 INVALID_BALANCE_TYPE¶
The balance type is incorrect.
-4045 MAX_STOP_ORDER_EXCEEDED¶
Reached the stop-loss order limit.
-4055 AMOUNT_MUST_BE_POSITIVE¶
The quantity must be a positive integer.
-4056 INVALID_API_KEY_TYPE¶
The API key type is invalid.
-4057 INVALID_RSA_PUBLIC_KEY¶
The API key is invalid.
-4058 MAX_PRICE_TOO_LARGE¶
maxPrice and priceDecimal too large, please check.
-4060 INVALID_POSITION_SIDE¶
Invalid position side.
-4061 POSITION_SIDE_NOT_MATCH¶
The order's position direction does not match the user’s settings.
-4062 REDUCE_ONLY_CONFLICT¶
Invalid or improper reduceOnly value.
-4084 UPCOMING_METHOD¶
Method is not allowed currently. Coming soon.
-4086 INVALID_PRICE_SPREAD_THRESHOLD¶
Invalid price spread threshold.
-4087 REDUCE_ONLY_ORDER_PERMISSION¶
Users can only place reduce-only orders.
-4088 NO_PLACE_ORDER_PERMISSION¶
User cannot place orders currently.
-4114 INVALID_CLIENT_TRAN_ID_LEN¶
clientTranId is not valid.
The customer's tranId length should be less than 64 characters.
-4115 DUPLICATED_CLIENT_TRAN_ID¶
clientTranId is duplicated.
The client's tranId should be unique within 7 days.
-4118 REDUCE_ONLY_MARGIN_CHECK_FAILED¶
ReduceOnly Order failed. Please check your existing position and open orders
-4131 MARKET_ORDER_REJECT¶
The counterparty's best price does not meet the PERCENT_PRICE filter limit.
-4135 INVALID_ACTIVATION_PRICE¶
Invalid activation price.
-4137 QUANTITY_EXISTS_WITH_CLOSE_POSITION¶
Quantity must be zero when closePosition is true.
-4138 REDUCE_ONLY_MUST_BE_TRUE¶
Reduce only must be true when closePosition is true.
-4139 ORDER_TYPE_CANNOT_BE_MKT¶
Order type cannot be a market order if it cannot be canceled.
-4140 INVALID_OPENING_POSITION_STATUS¶
Invalid symbol status for opening position.
-4141 SYMBOL_ALREADY_CLOSED¶
Trading pair has been delisted.
-4142 STRATEGY_INVALID_TRIGGER_PRICE¶
Rejected: Take Profit or Stop order would be triggered immediately.
-4164 MIN_NOTIONAL¶
Order notional must be at least 5.0 (unless you select Reduce Only)
Order notional must be no smaller than %s (unless you choose Reduce Only)
-4165 INVALID_TIME_INTERVAL¶
Invalid time interval
Maximum time interval is %s days
-4183 PRICE_HIGHTER_THAN_STOP_MULTIPLIER_UP¶
Limit price cannot be higher than the cap of %s.
Take-Profit/Stop-Loss price cannot be higher than the cap of %s.
-4184 PRICE_LOWER_THAN_STOP_MULTIPLIER_DOWN¶
Price is below the stop price limit.
Take-Profit/Stop-Loss price must be above the trigger price × multiplier floor.
Order price (limit or TP/SL) can’t be below %s.
 Back to top
Made with Material for MkDocs