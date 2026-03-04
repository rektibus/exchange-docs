<!-- KEYWORDS: liquidation! force order! liquidationOrder! PFO! funding rate! open interest! depth! orderbook! -->
<!-- LIQUIDATION: WS topic "liquidationOrder" (PFO). Fields: I=symbol, D=side(0=buy,1=sell), P=price, V=volume, T=timestamp_seconds. Broadcast topic, no symbol filter needed. NO REST liquidation endpoint. -->
<!-- FUNDING: REST live: /deepcoin/trade/fund-rate/current-funding-rate?instType=SwapU (bulk, instrumentId+fundingRate, wrapper=data.current_fund_rates). REST history: /deepcoin/trade/fund-rate/history?instId={{symbol}}&size=100 (paged, wrapper=data.list, fields: instrumentID+rate+CreateTime_seconds). Needs _funding handler with history_value=rate, history_ts=CreateTime for recovery. -->
<!-- OI: NOT AVAILABLE — no endpoint or WS field -->
<!-- LS RATIO: NOT AVAILABLE -->
<!-- PROTOCOL: V2 required (?platform=api&version=v2). Subscribe: {"Action":"1","Symbol":"BTCUSDT","LocalNo":N,"ResumeNo":-1,"Topic":"trade"}. Ack: {"a":"RecvTopicAction","m":"Success"}. Side: D="0"=buy, D="1"=sell (VERIFIED LIVE). Timestamp in seconds. Ping: text "ping" → "pong", 30s interval. -->
<!-- SYMBOL FORMAT: Products: BTC-USDT-SWAP. WS V2: BTCUSDT (ws_symbol_transform: strip_suffix:-SWAP,strip_dashes). Spot: BTC-USDT → BTC/USDT (replace_separator:/). REST trades use product format (instId=BTC-USDT-SWAP). -->
<!-- REST TRADES: No pagination (after/before params silently ignored). Max 500 recent trades. Side: "buy"/"sell" strings. Timestamp: ms. Rate limit: 5/1s for market endpoints. -->
Access Guide
Access Guide
Python DEMO
Golang DEMO
Java DEMO
Telegram API Discussion Group
Request Authentication
API URL https://api.deepcoin.com

Generate APIKey
Before signing any request, you must create an APIKey through the trading website. After creating the APIKey, you will receive 3 pieces of information that must be remembered:

APIKey
SecretKey
Passphrase
The APIKey and SecretKey will be randomly generated and provided by the platform, while the Passphrase will be provided by you to ensure API access security. The platform will store the encrypted hash of the Passphrase for verification, but if you forget the Passphrase, it cannot be recovered. Please generate a new APIKey through the trading website.

Each APIKey can be bound to a maximum of 20 IP addresses; APIKeys with trading or withdrawal permissions that are not bound to an IP will be automatically deleted after 30 days of inactivity.

Making Requests
All REST private request headers must include the following:

DC-ACCESS-KEY APIKey as string type.
DC-ACCESS-SIGN Hash value obtained using HMAC SHA256 hash function, then encoded with Base-64 (see Signature).
DC-ACCESS-TIMESTAMP Time of request initiation (UTC), e.g.: 2020-12-08T09:08:57.715Z
DC-ACCESS-PASSPHRASE The Passphrase you specified when creating the API key.
All requests will be formatted as application/json type requests and contain valid JSON.

Signature
The DC-ACCESS-SIGN request header is obtained by encrypting the string timestamp + method + requestPath + body (+ represents string concatenation) and the SecretKey using the HMAC SHA256 method, then encoding through Base-64.

For example:

sign = CryptoJS.enc.Base64.stringify(
  CryptoJS.HmacSHA256(timestamp + 'GET' + '/users/self/verify', SecretKey)
)

Where timestamp value is the same as the DC-ACCESS-TIMESTAMP request header, in ISO format, such as 2020-12-08T09:08:57.715Z.

method is the request method, all letters in uppercase: GET or POST. requestPath is the request interface path, for example: /deepcoin/account/balance. body is the string of the request body, if the request has no body (usually for GET requests) then body can be omitted. For example:

{ "instId": "BTC-USDT", "lever": "5", "mgnMode": "isolated" }

GET request parameters are considered part of requestPath, not body

SecretKey is generated when the user applies for an APIKey. For example: 22582BD0CFF14C41EDBF1AB98506286D






Error Codes
Error Codes
Error Message	HTTP Status Code	Error Code
API has been frozen, please contact customer service	400	50100
APIKey does not match the current environment	401	50101
Request timestamp has expired	401	50102
Request header "DC-ACCESS-KEY" cannot be empty	401	50103
Request header "DC-ACCESS-PASSPHRASE" cannot be empty	401	50104
Request header "DC-ACCESS-PASSPHRASE" is incorrect	401	50105
Request header "DC-ACCESS-SIGN" cannot be empty	401	50106
Request header "DC-ACCESS-TIMESTAMP" cannot be empty	401	50107
Broker ID does not exist	401	50108
Broker domain does not exist	401	50109
Invalid IP	401	50110
Invalid DC-ACCESS-KEY	401	50113
Invalid DC-ACCESS-TIMESTAMP	401	50112
Invalid signature	401	50111
Invalid authorization	401	50114
Invalid request type	405	50115





Get Order Book
Get Order Book
Get order book depth

Rate limit: IP

Request frequency limit: 5/1s

Request URL
GET /deepcoin/market/books

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
sz	true	integer	Number of depth levels, maximum 400
Response Parameters
Field Name	Type	Description
bids	array	Buy orders collection, format: [[price1, size1], ...]
asks	array	Sell orders collection, format: [[price1, size1], ...]
Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "bids": [
            [
                "97515.7",
                "14.507"
            ]
        ],
        "asks": [
            [
                "97516",
                "9.303"
            ]
        ]
    }
}





Get K-line Data
Get K-line Data
Get K-line data for trading products. The return array values are: [timestamp, open price, highest price, lowest price, close price, trading volume (in base currency), trading volume (in quote currency)]

Rate limit: IP

Request frequency limit: 5/1s

Request URL
GET /deepcoin/market/candles

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
bar	false	string	Time granularity
Default: 1m
1 minute: 1m
5 minutes: 5m
15 minutes: 15m
30 minutes: 30m
1 hour: 1H
4 hours: 4H
12 hours: 12H
1 day: 1D
1 week: 1W
1 month: 1M
1 year: 1Y
after	false	integer	Request content before this timestamp (older data), value should be the ts from the response
limit	false	integer	Maximum number of results per page is 300
Default: 100
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        [
            "1739157660000",  // Timestamp
            "95900.5",        // Open price
            "95932.2",        // Highest price
            "95850.4",        // Lowest price
            "95913.4",        // Close price
            "20084",          // Volume (base currency)
            "1925967.4841"    // Volume (quote currency)
        ],
        [
            "1739157600000",
            "95963.3",
            "95983.2",
            "95898.2",
            "95900.5",
            "5472",
            "524979.2415"
        ]
    ]
}



Get Product Info
Get Product Info
Get information list of all tradable products

Rate limit: IP

Request frequency limit: 5/1s

Request URL
GET /deepcoin/market/instruments

Request Parameters
Field Name	Required	Type	Description
instType	true	string	Product type
Spot: SPOT
Contract: SWAP
uly	false	string	Index symbol, only applicable to perpetual
instId	false	string	Product ID
Response Parameters
Field Name	Type	Description
instType	string	Product type
instId	string	Product ID
uly	string	Index symbol, only applicable to perpetual
baseCcy	string	Base currency, only applicable to spot
quoteCcy	string	Quote currency, only applicable to spot
ctVal	string	Contract value, only applicable to perpetual
ctValCcy	string	Contract value currency, only applicable to perpetual
listTime	string	Listing time, Unix timestamp in milliseconds
lever	string	Maximum leverage supported by the instId, not applicable to spot/options
tickSz	string	Order price precision
lotSz	string	Order size precision
minSz	string	Minimum order size
ctType	string	Contract type
linear: Linear contract
inverse: Inverse contract
Only for perpetual
alias	string	Contract alias
this_week: Current week
next_week: Next week
quarter: Quarter
next_quarter: Next quarter
Only for delivery
state	string	Product status
live: Trading
suspend: Suspended
preopen: Pre-launch
settlement: Funding fee settlement
maxLmtSz	string	Maximum order size for limit orders
maxMktSz	string	Maximum order size for market orders
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "uly": "",
            "baseCcy": "BTC",
            "quoteCcy": "USDT",
            "ctVal": "0.001",
            "ctValCcy": "",
            "listTime": "0",
            "lever": "125",
            "tickSz": "0.1",
            "lotSz": "1",
            "minSz": "1",
            "ctType": "",
            "alias": "",
            "state": "live",
            "maxLmtSz": "200000",
            "maxMktSz": "200000"
        }
    ]
}



Get Market Tickers
Get Market Tickers
Get market tickers information

Rate limit: IP

Request frequency limit: 5/1s

Request URL
GET /deepcoin/market/tickers

Request Parameters
Field Name	Required	Type	Description
instType	true	string	Product type
Spot: SPOT
Contract: SWAP
uly	false	string	Index symbol, only applicable to perpetual
Response Parameters
Field Name	Type	Description
instType	string	Product type
instId	string	Product ID
last	string	Last traded price
lastSz	string	Last traded size
askPx	string	Best ask price
askSz	string	Best ask size
bidPx	string	Best bid price
bidSz	string	Best bid size
open24h	string	24-hour opening price
high24h	string	24-hour highest price
low24h	string	24-hour lowest price
volCcy24h	string	24-hour volume in quote currency
vol24h	string	24-hour volume in base currency
sodUtc0	string	Opening price at UTC 0
sodUtc8	string	Opening price at UTC+8
ts	string	Ticker data generation time, Unix timestamp in milliseconds
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        {
            "instType": "SWAP",
            "instId": "BTC-USD-SWAP",
            "last": "96127.5",
            "lastSz": "",
            "askPx": "96127.8",
            "askSz": "179208",
            "bidPx": "96127.3",
            "bidSz": "2951",
            "open24h": "95596.6",
            "high24h": "96531.5",
            "low24h": "95247",
            "volCcy24h": "55.814169",
            "vol24h": "5350671",
            "sodUtc0": "",
            "sodUtc8": "",
            "ts": "1739242026000"
        }
    ]
}


Get index K-line Data
Get Index price K-line Data
Get Index price K-line data for trading products. The return array values are: [timestamp, open price, highest price, lowest price, close price, trading volume (0), trading volume (0)]

Rate limit: IP

Request frequency limit: 5/1s

Request URL
GET /deepcoin/market/index-candles

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
bar	false	string	Time granularity
Default: 1m
1 minute: 1m
5 minutes: 5m
15 minutes: 15m
30 minutes: 30m
1 hour: 1H
4 hours: 4H
12 hours: 12H
1 day: 1D
1 week: 1W
1 month: 1M
1 year: 1Y
after	false	integer	Request content before this timestamp (older data), value should be the ts from the response
limit	false	integer	Maximum number of results per page is 300
Default: 100
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        [
            "1739157660000",  // Timestamp
            "95900.5",        // Open price
            "95932.2",        // Highest price
            "95850.4",        // Lowest price
            "95913.4",        // Close price
            "0",          // Volume (base currency)
            "0"    // Volume (quote currency)
        ],
        [
            "1739157600000",
            "95963.3",
            "95983.2",
            "95898.2",
            "95900.5",
            "0",
            "0"
        ]
    ]
}




Get Trades
Retrieve the recent transactions for a specific instrument.

Request URL
GET /deepcoin/market/trades

Request Parameters
Parameter	Type	Required	Description	Example
instId	String	Yes	Instrument ID	BTC-USDT
productGroup	String	Yes	Product group Spot:Spot trading Swap:Coin-margined SwapU:USDT-margined	Spot
limit	integer	No	Number of results per request, maximum 500, default 100	100
Response Parameters
Parameter	Type	Description	Example
instId	String	Instrument ID	BTC-USDT
tradeId	String	Trade ID	T1234567890
px	String	Price	38715.7
sz	String	Size For spot trading, the unit is base currency; For futures, swap and options, the unit is contract	0.1
side	String	Taker side buy:buy sell:sell	buy
ts	String	Trade time, Unix timestamp format in milliseconds	1597026383085
Response Example
{
  "code": 0,
  "msg": "success",
  "data": [
    {
      "instId": "BTC-USDT",
      "tradeId": "T1234567890",
      "px": "38715.7",
      "sz": "0.1",
      "side": "buy",
      "ts": "1597026383085"
    },
    {
      "instId": "BTC-USDT",
      "tradeId": "T1234567891",
      "px": "38710.2",
      "sz": "0.5",
      "side": "sell",
      "ts": "1597026383086"
    }
  ]
}



Get mark price K-line Data
Get K-line Data
Get mark price K-line data for trading products. The return array values are: [timestamp, open price, highest price, lowest price, close price, trading volume (0), trading volume (0)]

Rate limit: IP

Request frequency limit: 5/1s

Request URL
GET /deepcoin/market/mark-price-candles

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
bar	false	string	Time granularity
Default: 1m
1 minute: 1m
5 minutes: 5m
15 minutes: 15m
30 minutes: 30m
1 hour: 1H
4 hours: 4H
12 hours: 12H
1 day: 1D
1 week: 1W
1 month: 1M
1 year: 1Y
after	false	integer	Request content before this timestamp (older data), value should be the ts from the response
limit	false	integer	Maximum number of results per page is 300
Default: 100
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        [
            "1739157660000",  // Timestamp
            "95900.5",        // Open price
            "95932.2",        // Highest price
            "95850.4",        // Lowest price
            "95913.4",        // Close price
            "0",          // Volume (base currency)
            "0"    // Volume (quote currency)
        ],
        [
            "1739157600000",
            "95963.3",
            "95983.2",
            "95898.2",
            "95900.5",
            "0",
            "0"
        ]
    ]
}



Get step margin data
Get Step margin data
Get step margin data for trading products.

Rate limit: IP

Request frequency limit: 1/1s

Request URL
GET /deepcoin/market/step-margin

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID,only support SWAP
Response Parameters
Field Name	Type	Description
grade	int	grade
leverage	string	leverage
maxContractValue	float64	max value
maintenanceMarginRate	string	maintenance MarginRate
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
      {
        "grade": 1,
        "leverage": "125",
        "maxContractValue": 12000,
        "maintenanceMarginRate": "0.004"
      },
      {
        "grade": 2,
        "leverage": "76.923077",
        "maxContractValue": 18000,
        "maintenanceMarginRate": "0.0065"
      },
      {
        "grade": 3,
        "leverage": "55.555556",
        "maxContractValue": 24000,
        "maintenanceMarginRate": "0.009"
      }
    ]
}

Get book spread data
Get book spread data
Get book spread data for trading products.

Rate limit: IP

Request frequency limit: 1/1s

Request URL
GET /deepcoin/market/book-spread

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
value	true	float	baseCcy or quoteCcy
vType	false	string	0:quoteCcy,USDT ,1:baseCcy BCT,ETH ... default 0
Response Parameters
Field Name	Type	Description
instId	string	Product ID
askSpreadValue	string	spread of asks books
bidSpreadValue	string	spread of bids books
Response Example
{
  "code": "0",
  "msg": "",
  "data": {
    "instId": "BTC-USDT-SWAP",
    "askSpreadValue": "0.000550",
    "bidSpreadValue": "0.000661"
  }
}


Get information of system
Get information of system
Get information of system

Rate limit: IP

Request frequency limit: 1/1s

Get system time
GET /deepcoin/market/time

Request Parameters
None

Response Parameters
Field Name	Type	Description
ts	int64	current time (milliseconds)
Response Example
{
  "code": "0",
  "msg": "",
  "data": {
    "ts": 1762414261346
  }
}

System connectivity
GET /deepcoin/market/ping

Request Parameters
None

Response Parameters
None

Response Example
{
  "code": "0",
  "msg": "",
  "data": {}
}

Handicap History Kline 1m
Query historical 1m kline data for a symbol within a time range.

Request URL
GET /deepcoin/market/handicap-kline1m

Request Parameters
Parameter	Type	Required	Description	Example
symbol	String	Yes	Trading symbol	BTC-USDT-SWAP
stime	integer	Yes	Start timestamp (seconds)	1700000000
etime	integer	No	End timestamp (seconds)	1800000000
limit	integer	Yes	Result size, between 1 and 2000	60
Response Parameters
Parameter	Type	Description	Example
etime	integer	Response end timestamp	1700003600
data	Array<Array<String>>	Kline data rows (unified from upstream dataV2)	...
errmsg	String	Error message (if any)	
Response Example
{
  "code": "0",
  "msg": "",
  "data": {
    "etime": 1766757360,
    "data": [
      [
        "1766757360",      // Timestamp
        "89021.2",         // Open price
        "89025.9",         // High price
        "89021.2",         // Low price
        "89025.9",         // Close price
        "0.00640052",      // Quantity
        "569.80413281"     // Turnover
      ]
    ],
    "errmsg": ""
  }
}


Handicap History Trades
Query historical trade data for a symbol within a time range.

Request URL
GET /deepcoin/market/handicap-trade

Request Parameters
Parameter	Type	Required	Description	Example
symbol	String	Yes	Trading symbol	BTC-USDT-SWAP
stime	integer	Yes	Start timestamp (seconds)	1700000000
etime	integer	No	End timestamp (seconds)	1800000000
limit	integer	Yes	Result size, between 1 and 2000	60
Response Parameters
Parameter	Type	Description	Example
etime	integer	Response end timestamp	1700003600
data	Array<Array<String>>	Trade data rows (unified from upstream dataV2)	...
errmsg	String	Error message (if any)	
Response Example
{
  "code": "0",
  "msg": "",
  "data": {
    "etime": 1766759271,
    "data": [
      [
        "1766759271",          // Timestamp
        "1000299140908139",    // Trade ID
        "1",                   // Side flag
        "88948.8",             // Trade price
        ""                     // Reserved field (currently empty)
      ]
    ],
    "errmsg": ""
  }
}


Handicap History Orderbook
Query historical orderbook data for a symbol within a time range.

Request URL
GET /deepcoin/market/handicap-orderbook

Request Parameters
Parameter	Type	Required	Description	Example
symbol	String	Yes	Trading symbol	BTC-USDT-SWAP
stime	integer	Yes	Start timestamp (seconds)	1700000000
etime	integer	No	End timestamp (seconds)	1800000000
limit	integer	Yes	Result size, between 1 and 2000	60
Response Parameters
Parameter	Type	Description	Example
etime	integer	Response end timestamp	1700003600
data	Array<Object>	Orderbook snapshot list (unified from upstream dataV2)	...
errmsg	String	Error message (if any)	
Response Example
{
  "code": "0",
  "msg": "",
  "data": {
    "etime": 1766758170,
    "data": [
      {
        "timestamp": 1766758170,  // Timestamp
        "buy_order_list": [       // Bid levels: [price, quantity]
          [104600, 43],
          [99999.9, 3],
          [98200.1, 10],
          [98000, 2],
          [96500, 8],
          [96000, 102],
          [95888, 55],
          [95800, 5],
          [95421.9, 3],
          [95000, 207],
          [94888, 165],
          [94800, 37],
          [94777, 21],
          [94700, 112],
          [94500, 1472],
          [94457, 2307],
          [94300, 803],
          [94299.7, 42],
          [94200, 300],
          [94000, 57],
          [93800, 112],
          [93600, 100],
          [93500, 32],
          [93462, 1],
          [93290, 10]
        ],
        "ask_order_list": [       // Ask levels: [price, quantity]
          [1, 1000],
          [8400, 30],
          [26555.9, 99],
          [61800, 56],
          [62000, 92],
          [63000, 1252],
          [63315, 12],
          [63888, 364],
          [64000, 90],
          [64300, 179],
          [64588, 1310],
          [66680.9, 36],
          [70005, 100],
          [71000, 958],
          [72000, 40],
          [72200, 815],
          [73200, 849],
          [73500, 50],
          [74200, 884],
          [74500, 64],
          [74531, 2],
          [74588, 1],
          [75000, 334],
          [75200, 683],
          [75446, 1]
        ]
      }
    ],
    "errmsg": ""
  }
}







Place Order
Place Order
Place an order when your account has sufficient funds

Request frequency limit: 1/1s

Request URL
POST /deepcoin/trade/order

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
tdMode	true	string	Trading mode
Isolated: isolated
Cross: cross
ccy	false	string	Margin currency, only applicable to cross margin orders in single-currency margin mode
clOrdId	false	string	Custom order ID, combination of letters (case-sensitive) and numbers, length between 1-32. Parameter not supported currently
tag	false	string	Order tag, combination of letters (case-sensitive) and numbers, length between 1-16. Parameter not supported currently
side	true	string	Order side
Buy: buy
Sell: sell
posSide	false	string	Position side
Required when product type is SWAP
Long: long
Short: short
mrgPosition	false	string	Position mode
Required when product type is SWAP
Merged: merge
Split: split
closePosId	false	string	Position ID to close, required in split mode
ordType	true	string	Order type
Market order: market
Limit order: limit
Post only: post_only
Immediate or cancel: ioc
sz	true	string	Order size, get minimum order size (minSz) through Get Product Info API
px	false	string	Order price, get price precision (tickSz) through Get Product Info API
Only applicable to limit and post_only orders
reduceOnly	false	boolean	Reduce only,true or false
Default: false
Only applicable to margin trading and futures/perpetual in long/short mode
tgtCcy	false	string	Market order quantity type, only applicable to spot orders
Base currency: base_ccy
Quote currency: quote_ccy
tpTriggerPx	false	string	Take profit trigger price, only applicable to take profit and stop loss orders
slTriggerPx	false	string	Stop loss trigger price, only applicable to take profit and stop loss orders
Request Example
{
  "instId": "BTC-USDT",
  "tdMode": "cash",
  "ccy": "USDT",
  "clOrdId": "string",
  "tag": "string",
  "side": "buy",
  "posSide": "long",
  "mrgPosition": "merge",
  "closePosId": "1001063717138767",
  "ordType": "limit",
  "sz": "0.0004",
  "px": "0.01",
  "reduceOnly": "boolean",
  "tgtCcy": "string",
  "tpTriggerPx": "10000.1",
  "slTriggerPx": "9000.1"
}



// Market Buy, Open Long
{
    "instId": "BTC-USDT-SWAP",
    "tdMode": "cross",
    "side": "buy",
    "ordType": "market",
    "sz": "5",
    "posSide": "long",
    "mrgPosition": "merge",
}

// Market Sell, Close Long
{
    "instId": "BTC-USDT-SWAP",
    "tdMode": "cross",
    "side": "sell",
    "ordType": "market",
    "sz": "5",
    "posSide": "long",
    "mrgPosition": "merge",
}

// Market Sell, Open Short
{
    "instId": "BTC-USDT-SWAP",
    "tdMode": "cross",
    "side": "sell",
    "ordType": "market",
    "sz": "1",
    "posSide": "short",
    "mrgPosition": "merge",
}

// Market Buy, Close Short
{
    "instId": "BTC-USDT-SWAP",
    "tdMode": "cross",
    "side": "buy",
    "ordType": "market",
    "sz": "1",
    "posSide": "short",
    "mrgPosition": "merge",
}

// Limit Buy, Open Long
{
    "instId": "BTC-USDT-SWAP",
    "tdMode": "cross",
    "side": "buy",
    "ordType": "limit",
    "sz": "1",
    "px": "23000",
    "posSide": "long",
    "mrgPosition": "merge",
}

// Limit Sell, Open Short 
{
    "instId": "BTC-USDT-SWAP",
    "tdMode": "cross",
    "side": "sell",
    "ordType": "limit",
    "sz": "1",
    "px": "35000",
    "posSide": "short",
    "mrgPosition": "merge",
}

Response Parameters
Field Name	Type	Description
ordId	string	Order ID
clOrdId	string	Custom order ID
tag	string	Order tag
sCode	string	Status code of execution result, 0: Success
sMsg	string	Error message if execution fails
Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "ordId": "1000587866646229",
        "clOrdId": "",
        "tag": "",
        "sCode": "0",
        "sMsg": ""
    }
}



Amend Order
Amend Order
Modify the price and quantity of a specified order

Request frequency limit: 1/1s

Request URL
POST /deepcoin/trade/replace-order

Request Parameters
Field Name	Required	Type	Description
OrderSysID	true	string	Order ID
price	false	float	Price
volume	false	integer	Quantity, unit:contracts
Request Example
{
  "OrderSysID": "'12345'",
  "price": 6000.5,
  "volume": 5
}

Response Parameters
Field Name	Type	Description
errorCode	integer	Error code
errorMsg	string	Error message
ordId	string	Order ID
Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "errorCode": 0,
        "errorMsg": "",
        "ordId": "1000587867035933"
    }
}


Cancel Order
Cancel Order
Cancel a pending order

Request frequency limit: 1/1s

Request URL
POST /deepcoin/trade/cancel-order

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
ordId	true	string	Order ID
Request Example
{
    "instId": "BTC-USDT-SWAP",
    "ordId": "1000587866272245"
}

Response Parameters
Field Name	Type	Description
ordId	string	Order ID
clOrdId	string	Custom order ID
sCode	string	Status code of execution result, 0: Success
sMsg	string	Error message if execution fails
Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "ordId": "1000587866272245",
        "clOrdId": "",
        "sCode": "0",
        "sMsg": ""
    }
}


Batch Cancel Orders
Batch Cancel Orders
Cancel multiple limit orders in batch, maximum 50 limit orders per batch

Request frequency limit: 1/1s

Request URL
POST /deepcoin/trade/batch-cancel-order

Request Parameters
Field Name	Required	Type	Description
OrderSysIDs	true	string[]	Specified limit order IDs
Request Example
{
    "orderSysIDs": [
        "1000587865918838",
        "1000587865914949"
    ]
}

Response Parameters
Field Name	Type	Description
errorList	string[]	Cancel failure types
> memberId	string	User ID
> accountId	string	Account ID
>orderSysId	string	Order ID
> errorCode	integer	Error code
> errorMsg	string	Error message
Response Example
// no errors
{
    "code": "0",
    "msg": "",
    "data": {
        "errorList": [

    ]
    }
}

// Partial order cancellation failed.
{
    "code": "0",
    "msg": "",
    "data": {
        "errorList": [
            {
                "memberId": "36006290",
                "accountId": "36006290",
                "orderSysId": "1000587865918838",
                "errorCode": 24,
                "errorMsg": "OrderNotFound:1000587865918838"
            },
            {
                "memberId": "36006290",
                "accountId": "36006290",
                "orderSysId": "1000587865914949",
                "errorCode": 24,
                "errorMsg": "OrderNotFound:1000587865914949"
            }
        ]
    }
}


Cancel Trigger Order
Cancel Trigger Order
Cancel an incomplete trigger order

Request frequency limit: 60/2s

Rate limit rule:

Request URL
POST /deepcoin/trade/cancel-trigger-order

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
ordId	true	string	Trigger Order ID
clOrdId	false	string	Client Order ID (currently not supported)
Request Example
{
    "instId": "BTC-USDT-SWAP",
    "ordId": "1001063717138767"
}

Response Parameters
Field Name	Type	Description
ordId	string	Order ID
clOrdId	string	Client Order ID as assigned by the client
sCode	string	Status code of execution result, 0: Success
sMsg	string	Rejection message if the request is unsuccessful
Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "ordId": "1001063717138767",
        "clOrdId": "",
        "sCode": "0",
        "sMsg": ""
    }
}

Error Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "ordId": "",
        "clOrdId": "",
        "sCode": "1033201232",
        "sMsg": "Order not found"
    }
}

Notes
Only incomplete trigger orders can be cancelled
Both spot and derivatives trigger orders are supported
The order must belong to the authenticated user
Rate limiting is applied per user and instrument type


Cancel All Orders
Cancel All Orders
Cancel all limit orders, maximum one request per second (only for contracts)

Request frequency limit: 1/1s

Request URL
POST /deepcoin/trade/swap/cancel-all

Request Parameters
Field Name	Required	Type	Description
InstrumentID	true	string	Trading pair
ProductGroup	true	string	Product type

Contract (Coin-margined: Swap)
Contract (USDT-margined: SwapU)
IsCrossMargin	true	integer	Margin type
Cross: 1
Isolated: 0
IsMergeMode	true	integer	Position mode
Merged: 1
Split: 0
Request Example
{
  "InstrumentID": "BTCUSDT",
  "ProductGroup": "SwapU",
  "IsCrossMargin": 1,
  "IsMergeMode": 0
}

Response Parameters
Field Name	Type	Description
errorList	string[]	Cancel failure types
> memberId	string	User ID
> accountId	string	Account ID
> orderSysId	string	Order ID
> errorCode	integer	Error code
> errorMsg	string	Error message
Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "errorList": []
    }
}


Cancel All Trigger Orders
Cancel All Trigger Orders
Cancel all contract trigger orders, maximum one request per second (only for contracts)

Request frequency limit: 1/1s

Request URL
POST /deepcoin/trade/swap/cancel-trigger-all

Request Parameters
Body (JSON)

Field Name	Required	Type	Description
ProductGroup	true	string	Swap or SwapU
InstrumentID	false	string	Trading pair, cancel all if omitted
IsCrossMargin	false	integer	Margin mode
Cross: 1
Isolated: 0
-1 no filter (default)
IsMergeMode	false	integer	Position mode
Merged: 1
Split: 0
-1 no filter (default)
Request Example
{
  "ProductGroup": "SwapU",
  "InstrumentID": "BTCUSDT",
  "IsCrossMargin": -1,
  "IsMergeMode": -1
}

Response Parameters
Field Name	Type	Description
errorList	string[]	Cancel failure types
> memberId	string	User ID
> accountId	string	Account ID
> orderSysId	string	Order ID
> errorCode	integer	Error code
> errorMsg	string	Error message
Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "errorList": []
    }
}


Trade Details
Get Trade Details
Get trade execution details

Request frequency limit: 1/1s

Request URL
GET /deepcoin/trade/fills

Request Parameters
Field Name	Required	Type	Description
instType	true	string	Product type
Spot: SPOT
Contract: SWAP
instId	false	string	Product ID
ordId	false	string	Order ID
after	false	string	Pagination of data before this ID (older data), value should be billId from the response
before	false	string	Pagination of data after this ID (newer data), value should be billId from the response
begin	false	integer	Request trade details after this timestamp, Unix timestamp in milliseconds
end	false	integer	Request trade details before this timestamp, Unix timestamp in milliseconds
limit	false	integer	Number of results per page, maximum 100, default 100
Response Parameters
Field Name	Type	Description
instType	string	Product type
instId	string	Product ID
tradeId	string	Latest trade ID
ordId	string	Order ID
clOrdId	string	Custom order ID
billId	string	Bill ID
tag	string	Order tag
fillPx	string	Latest fill price
fillSz	string	Latest fill size
side	string	Order side
Buy: buy
Sell: sell
posSide	string	Position side
Long: long
Short: short
execType	string	Execution type
Taker: T
Maker: M
feeCcy	string	Fee currency or rebate currency
fee	string	Trading fee
ts	string	Trade details generation time, Unix timestamp in milliseconds
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "tradeId": "1000169956494218",
            "ordId": "1000587866072658",
            "clOrdId": "",
            "billId": "10001699564942181",
            "tag": "",
            "fillPx": "98230.5",
            "fillSz": "200",
            "side": "sell",
            "posSide": "short",
            "execType": "T",
            "feeCcy": "USDT",
            "fee": "5.89383",
            "ts": "1739261250000"
        },
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "tradeId": "1000169956494217",
            "ordId": "1000587866072658",
            "clOrdId": "",
            "billId": "10001699564942171",
            "tag": "",
            "fillPx": "98230.5",
            "fillSz": "50",
            "side": "sell",
            "posSide": "short",
            "execType": "T",
            "feeCcy": "USDT",
            "fee": "1.4734575",
            "ts": "1739261250000"
        }
    ]
}



Get Order by ID
Get Order by ID
Get order information by ID

Request frequency limit: 1/1s

Request URL
GET /deepcoin/trade/orderByID

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
ordId	true	string	Order ID
Request Example
{
  "instId": "BTC-USDT-SWAP",
  "ordId": "1001063720100637"
}

Response Parameters
Field Name	Type	Description
instType	string	Product type
instId	string	Product ID
tgtCcy	string	Market order quantity type
Base currency: base_ccy
Quote currency: quote_ccy, only applicable to spot orders
ccy	string	Margin currency, only applicable to cross margin orders in single-currency margin mode
ordId	string	Order ID
clOrdId	string	Custom order ID
tag	string	Order tag
px	string	Order price
sz	string	Order size
pnl	string	Profit and loss
ordType	string	Order type
Market order: market
Limit order: limit
Post only: post_only
side	string	Order side
Buy: buy
Sell: sell
posSide	string	Position side
tdMode	string	Trading mode
accFillSz	string	Accumulated fill size
fillPx	string	Latest fill price
tradeId	string	Latest trade ID
fillSz	string	Latest fill size
fillTime	string	Latest fill time
avgPx	string	Average fill price
state	string	Order state
Pending: live
Partially filled: partially_filled
lever	string	Leverage between 0.01 and 125, only applicable to margin/perpetual trading
tpTriggerPx	string	Take profit trigger price
tpTriggerPxType	string	Take profit trigger price type
Last price: last
Index price: index
Mark price: mark
tpOrdPx	string	Take profit order price
slTriggerPx	string	Stop loss trigger price
slTriggerPxType	string	Stop loss trigger price type
Last price: last
Index price: index
Mark price: mark
slOrdPx	string	Stop loss order price
feeCcy	string	Fee currency
fee	string	Trading fee
rebateCcy	string	Rebate currency
source	string	Order source
rebate	string	Rebate amount. Platform pays maker rebates to users who reach specified trading levels. Empty string if no rebate. Positive number for fee rebate, e.g., 0.01
category	string	Order category
uTime	string	Order update time, Unix timestamp in milliseconds
cTime	string	Order creation time, Unix timestamp in milliseconds
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "tgtCcy": "",
            "ccy": "",
            "ordId": "1000587866808715",
            "clOrdId": "",
            "tag": "",
            "px": "1.000000",
            "sz": "95000.000000",
            "pnl": "0.000000",
            "ordType": "limit",
            "side": "buy",
            "posSide": "long",
            "tdMode": "cross",
            "accFillSz": "0.000000",
            "fillPx": "",
            "tradeId": "",
            "fillSz": "0.000000",
            "fillTime": "1739263130000",
            "avgPx": "",
            "state": "live",
            "lever": "1.000000",
            "tpTriggerPx": "",
            "tpTriggerPxType": "",
            "tpOrdPx": "",
            "slTriggerPx": "",
            "slTriggerPxType": "",
            "slOrdPx": "",
            "feeCcy": "USDT",
            "fee": "0.000000",
            "rebateCcy": "",
            "source": "",
            "rebate": "",
            "category": "normal",
            "uTime": "1739263130000",
            "cTime": "1739263130000"
        }
    ]
}



Get Historical Order by ID
Get Historical Order by ID
Get historical order information by ID

Request frequency limit: 1/1s

Request URL
GET /deepcoin/trade/finishOrderByID

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
ordId	true	string	Order ID
Response Parameters
Field Name	Type	Description
instType	string	Product type
instId	string	Product ID
tgtCcy	string	Market order quantity type
Base currency: base_ccy
Quote currency: quote_ccy, only applicable to spot orders
ccy	string	Margin currency, only applicable to cross margin orders in single-currency margin mode
ordId	string	Order ID
clOrdId	string	Custom order ID
tag	string	Order tag
px	string	Order price
sz	string	Order size
pnl	string	Profit and loss
ordType	string	Order type
Market order: market
Limit order: limit
Post only: post_only
side	string	Order side
Buy: buy
Sell: sell
posSide	string	Position side
tdMode	string	Trading mode
accFillSz	string	Accumulated fill size
fillPx	string	Latest fill price
tradeId	string	Latest trade ID
fillSz	string	Latest fill size
fillTime	string	Latest fill time
avgPx	string	Average fill price
state	string	Order state
Pending: live
Partially filled: partially_filled
lever	string	Leverage between 0.01 and 125, only applicable to margin/futures/perpetual trading
tpTriggerPx	string	Take profit trigger price
tpTriggerPxType	string	Take profit trigger price type
Last price: last
Index price: index
Mark price: mark
tpOrdPx	string	Take profit order price
slTriggerPx	string	Stop loss trigger price
slTriggerPxType	string	Stop loss trigger price type
Last price: last
Index price: index
Mark price: mark
slOrdPx	string	Stop loss order price
feeCcy	string	Fee currency
fee	string	Trading fee
rebateCcy	string	Rebate currency
source	string	Order source
Web: web
Mobile: app
API: api
System: system
rebate	string	Rebate amount. Platform pays maker rebates to users who reach specified trading levels. Empty string if no rebate. Positive number for fee rebate, e.g., 0.01
category	string	Order category, normal: Normal order
uTime	string	Order update time, Unix timestamp in milliseconds
cTime	string	Order creation time, Unix timestamp in milliseconds
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "tgtCcy": "",
            "ccy": "",
            "ordId": "1000587866272245",
            "clOrdId": "",
            "tag": "",
            "px": "1.000000",
            "sz": "95000.000000",
            "pnl": "0.000000",
            "ordType": "limit",
            "side": "buy",
            "posSide": "long",
            "tdMode": "cross",
            "accFillSz": "0.000000",
            "fillPx": "",
            "tradeId": "",
            "fillSz": "0.000000",
            "fillTime": "1739261771000",
            "avgPx": "",
            "state": "canceled",
            "lever": "1.000000",
            "tpTriggerPx": "",
            "tpTriggerPxType": "",
            "tpOrdPx": "",
            "slTriggerPx": "",
            "slTriggerPxType": "",
            "slOrdPx": "",
            "feeCcy": "USDT",
            "fee": "0.000000",
            "rebateCcy": "",
            "source": "",
            "rebate": "",
            "category": "normal",
            "uTime": "1739261771000",
            "cTime": "1739261762000"
        }
    ]
}


Order History
Order History
Get historical order records

Request frequency limit: 1/1s

Request URL
GET /deepcoin/trade/orders-history

Request Parameters
Field Name	Required	Type	Description
instType	true	string	Product type
Spot: SPOT
Contract: SWAP
instId	false	string	Product ID
ordType	false	string	Order type
Market order: market
Limit order: limit
Post only: post_only
state	false	string	Order state
Canceled: canceled
Filled: filled
after	false	string	Pagination of data before this ID (older data), value should be ordId from the response
before	false	string	Pagination of data after this ID (newer data), value should be ordId from the response
limit	false	integer	Number of results per page, maximum 100, default 100
ordId	false	string	Order ID
Response Parameters
Field Name	Type	Description
instType	string	Product type
instId	string	Product ID
tgtCcy	string	Market order quantity type
Base currency: base_ccy
Quote currency: quote_ccy, only applicable to spot orders
ccy	string	Margin currency, only applicable to cross margin orders in single-currency margin mode
ordId	string	Order ID
clOrdId	string	Custom order ID
tag	string	Order tag
px	string	Order price
sz	string	Order size
pnl	string	Profit and loss
ordType	string	Order type
Market order: market
Limit order: limit
Post only: post_only
side	string	Order side
Buy: buy
Sell: sell
posSide	string	Position side
tdMode	string	Trading mode
accFillSz	string	Accumulated fill size
fillPx	string	Latest fill price
tradeId	string	Latest trade ID
fillSz	string	Latest fill size
fillTime	string	Latest fill time
avgPx	string	Average fill price
state	string	Order state
Pending: live
Partially filled: partially_filled
lever	string	Leverage between 0.01 and 125, only applicable to margin/futures/perpetual trading
tpTriggerPx	string	Take profit trigger price
tpTriggerPxType	string	Take profit trigger price type
Last price: last
Index price: index
Mark price: mark
tpOrdPx	string	Take profit order price
slTriggerPx	string	Stop loss trigger price
slTriggerPxType	string	Stop loss trigger price type
Last price: last
Index price: index
Mark price: mark
slOrdPx	string	Stop loss order price
feeCcy	string	Fee currency
fee	string	Trading fee
rebateCcy	string	Rebate currency
source	string	Order source, 13: Limit order generated after strategy order is triggered
rebate	string	Rebate amount. Platform pays maker rebates to users who reach specified trading levels. Empty string if no rebate. Positive number for fee rebate, e.g., 0.01
category	string	Order category
uTime	string	Order update time, Unix timestamp in milliseconds
cTime	string	Order creation time, Unix timestamp in milliseconds
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "tgtCcy": "",
            "ccy": "",
            "ordId": "1000587866072658",
            "clOrdId": "",
            "tag": "",
            "px": "90000",
            "sz": "300",
            "pnl": "0",
            "ordType": "limit",
            "side": "sell",
            "posSide": "short",
            "tdMode": "cross",
            "accFillSz": "300",
            "fillPx": "98230.5",
            "tradeId": "",
            "fillSz": "300",
            "fillTime": "1739261250000",
            "avgPx": "98230.5",
            "state": "filled",
            "lever": "1",
            "tpTriggerPx": "",
            "tpTriggerPxType": "",
            "tpOrdPx": "",
            "slTriggerPx": "",
            "slTriggerPxType": "",
            "slOrdPx": "",
            "feeCcy": "USDT",
            "fee": "8.840745",
            "rebateCcy": "",
            "source": "",
            "rebate": "",
            "category": "normal",
            "uTime": "1739261250000",
            "cTime": "1739261250000"
        }
    ]
}

Pending Orders
Get All Pending Orders
Get all pending orders for the current account

Request frequency limit: 1/1s

Request URL
GET /deepcoin/trade/v2/orders-pending

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
index	true	integer	Page number
limit	false	integer	Number of results per page, maximum 100, default 30
ordId	false	string	Order ID
Response Parameters
Field Name	Type	Description
instType	string	Product type
instId	string	Product ID
tgtCcy	string	Market order quantity type
Base currency: base_ccy
Quote currency: quote_ccy, only applicable to spot orders
ccy	string	Margin currency, only applicable to cross margin orders in single-currency margin mode
ordId	string	Order ID
clOrdId	string	Custom order ID
tag	string	Order tag
px	string	Order price
sz	string	Order size
pnl	string	Profit and loss
ordType	string	Order type
Market order: market
Limit order: limit
Post only: post_only
side	string	Order side
Buy: buy
Sell: sell
posSide	string	Position side
tdMode	string	Trading mode
accFillSz	string	Accumulated fill size
fillPx	string	Latest fill price
tradeId	string	Latest trade ID
fillSz	string	Latest fill size
fillTime	string	Latest fill time
avgPx	string	Average fill price
state	string	Order state
Pending: live
Partially filled: partially_filled
lever	string	Leverage between 0.01 and 125, only applicable to margin/futures/perpetual trading
tpTriggerPx	string	Take profit trigger price
tpTriggerPxType	string	Take profit trigger price type
Last price: last
Index price: index
Mark price: mark
tpOrdPx	string	Take profit order price
slTriggerPx	string	Stop loss trigger price
slTriggerPxType	string	Stop loss trigger price type
Last price: last
Index price: index
Mark price: mark
slOrdPx	string	Stop loss order price
feeCcy	string	Fee currency
fee	string	Trading fee
rebateCcy	string	Rebate currency
source	string	Order source, 13: Limit order generated after strategy order is triggered
rebate	string	Rebate amount. Platform pays maker rebates to users who reach specified trading levels. Empty string if no rebate. Positive number for fee rebate, e.g., 0.01
category	string	Order category
uTime	string	Order update time, Unix timestamp in milliseconds
cTime	string	Order creation time, Unix timestamp in milliseconds
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "tgtCcy": "",
            "ccy": "",
            "ordId": "1000587866072658",
            "clOrdId": "",
            "tag": "",
            "px": "90000",
            "sz": "300",
            "pnl": "0",
            "ordType": "limit",
            "side": "sell",
            "posSide": "short",
            "tdMode": "cross",
            "accFillSz": "300",
            "fillPx": "98230.5",
            "tradeId": "",
            "fillSz": "300",
            "fillTime": "1739261250000",
            "avgPx": "98230.5",
            "state": "filled",
            "lever": "1",
            "tpTriggerPx": "",
            "tpTriggerPxType": "",
            "tpOrdPx": "",
            "slTriggerPx": "",
            "slTriggerPxType": "",
            "slOrdPx": "",
            "feeCcy": "USDT",
            "fee": "8.840745",
            "rebateCcy": "",
            "source": "",
            "rebate": "",
            "category": "normal",
            "uTime": "1739261250000",
            "cTime": "1739261250000"
        }
    ]
}

Funding Rate
Get Funding Rate
Get contract trading pair funding rate settlement cycle

Request frequency limit: 1/1s

Request URL
GET /deepcoin/trade/funding-rate

Request Parameters
Field Name	Required	Type	Description
instType	true	string	Contract type
USDT-margined: SwapU
Coin-margined: Swap
instId	false	string	Query specific trading pair funding rate cycle if not empty, query all if empty
Response Parameters
Field Name	Type	Description
data	array	
>settleInterval	integer	Funding fee interval
>instrumentID	string	Trading pair
>nextSettleTime	integer	Next settlement time
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        {
            "settleInterval": 28800,
            "instrumentID": "1000BABYDOGEUSDT",
            "nextSettleTime": 1739289600
        },
        {
            "settleInterval": 14400,
            "instrumentID": "1000CATUSDT",
            "nextSettleTime": 1739275200
        }
    ]
}


Trigger Order
Trigger Order
A trigger order is an order type where the system automatically places an order when the market price reaches a preset trigger price.

Rate limit: 1 request per second

Request URL
POST /deepcoin/trade/trigger-order

Request Parameters
Field	Required	Type	Description
instId	Yes	string	Product ID
productGroup	Yes	string	Trading type
Spot: Spot
Perpetual: Swap
sz	Yes	string	Order quantity
side	Yes	string	Order side
Buy: buy
Sell: sell
posSide	No	string	Position side
Required when product type is SWAP
Long: long
Short: short
price	No	string	Limit order price
Required for limit orders, not needed for market orders
isCrossMargin	Yes	string	Cross margin mode
Isolated: 0
Cross: 1
orderType	Yes	string	Order price type
Limit: limit
Market: market
triggerPrice	Yes	string	Trigger price
The order will be triggered when the market price reaches this price
triggerPxType	No	string	Trigger price type
Last price: last
Index price: index
Mark price: mark
Default: last
mrgPosition	No	string	Merge position
Required when product type is SWAP
Merge: merge
Split: split
closePosId	No	string	Position ID for closing position. Supports cross and isolated margin modes (required in split mode)
tdMode	Yes	string	Trading mode
Non-margin: cash
Cross margin: cross
Isolated margin: isolated
tpTriggerPx	No	number	Take profit trigger price
Automatically sets TP order after position is opened
tpTriggerPxType	No	string	Take profit trigger price type
Last price: last
Index price: index
Mark price: mark
Default: last
tpOrdPx	No	number	Take profit order price
-1 means market price
slTriggerPx	No	number	Stop loss trigger price
Automatically sets SL order after position is opened
slTriggerPxType	No	string	Stop loss trigger price type
Last price: last
Index price: index
Mark price: mark
Default: last
slOrdPx	No	number	Stop loss order price
-1 means market price
Request Examples
// Scenario 1: Cross margin merge position, open position trigger market order
triggerOrder = &triggerOrderRequest{
    InstId:        "BTC-USDT-SWAP",
    ProductGroup:  "Swap",
    Sz:            "1",
    Side:          "buy",
    PosSide:       "long",
    IsCrossMargin: "1",
    OrderType:     "market", // Market order
    TriggerPrice:  "150000",
    MrgPosition:   "merge",
    TdMode:        "cross",
}

// Scenario 2: Cross margin merge position, open position trigger limit order
triggerOrder = &triggerOrderRequest{
    InstId:        "BTC-USDT-SWAP",
    ProductGroup:  "Swap",
    Sz:            "1",
    Side:          "buy",
    PosSide:       "long",
    Price:         "140000",
    IsCrossMargin: "1",
    OrderType:     "limit", // Limit order
    TriggerPrice:  "150000",
    MrgPosition:   "merge",
    TdMode:        "cross",
}

// Scenario 3: Cross margin split position, open position trigger market order
triggerOrder = &triggerOrderRequest{
    InstId:        "BTC-USDT-SWAP",
    ProductGroup:  "Swap",
    Sz:            "1",
    Side:          "buy",
    PosSide:       "long",
    IsCrossMargin: "1",
    OrderType:     "market", // Market order
    TriggerPrice:  "150000",
    MrgPosition:   "split",
    TdMode:        "cross",
}

// Scenario 4: Cross margin split position, open position trigger limit order
triggerOrder = &triggerOrderRequest{
    InstId:        "BTC-USDT-SWAP",
    ProductGroup:  "Swap",
    Sz:            "1",
    Side:          "buy",
    PosSide:       "long",
    Price:         "140000",
    IsCrossMargin: "1",
    OrderType:     "limit", // Limit order
    TriggerPrice:  "150000",
    MrgPosition:   "split",
    TdMode:        "cross",
}

// Scenario 5: Isolated margin merge position, open position trigger market order
triggerOrder = &triggerOrderRequest{
    InstId:        "BTC-USDT-SWAP",
    ProductGroup:  "Swap",
    Sz:            "1",
    Side:          "buy",
    PosSide:       "long",
    IsCrossMargin: "0",
    OrderType:     "market", // Market order
    TriggerPrice:  "150000",
    MrgPosition:   "merge",
    TdMode:        "isolated",
}

// Scenario 6: Isolated margin merge position, open position trigger limit order
triggerOrder = &triggerOrderRequest{
    InstId:        "BTC-USDT-SWAP",
    ProductGroup:  "Swap",
    Sz:            "1",
    Side:          "buy",
    PosSide:       "long",
    Price:         "140000",
    IsCrossMargin: "0",
    OrderType:     "limit", // Limit order
    TriggerPrice:  "150000",
    MrgPosition:   "merge",
    TdMode:        "isolated",
}

// Scenario 7: Isolated margin split position, open position trigger market order
triggerOrder = &triggerOrderRequest{
    InstId:        "BTC-USDT-SWAP",
    ProductGroup:  "Swap",
    Sz:            "1",
    Side:          "buy",
    PosSide:       "long",
    IsCrossMargin: "0",
    OrderType:     "market", // Market order
    TriggerPrice:  "150000",
    MrgPosition:   "split",
    TdMode:        "isolated",
}

// Scenario 8: Isolated margin split position, open position trigger limit order
triggerOrder = &triggerOrderRequest{
    InstId:        "BTC-USDT-SWAP",
    ProductGroup:  "Swap",
    Sz:            "1",
    Side:          "buy",
    PosSide:       "long",
    Price:         "140000",
    IsCrossMargin: "0",
    OrderType:     "limit", // Limit order
    TriggerPrice:  "150000",
    MrgPosition:   "split",
    TdMode:        "isolated",
}

// Scenario 9: Trigger order with take profit and stop loss (SWAP)
triggerOrder = &triggerOrderRequest{
    InstId:          "BTC-USDT-SWAP",
    ProductGroup:    "Swap",
    Sz:              "1",
    Side:            "buy",
    PosSide:         "long",
    IsCrossMargin:   "1",
    OrderType:       "market",
    TriggerPrice:    "95000",
    TriggerPxType:   "last",
    MrgPosition:     "merge",
    TdMode:          "cross",
    TpTriggerPx:     100000,      // Take profit trigger price
    TpTriggerPxType: "last",      // Take profit trigger price type
    TpOrdPx:         -1,          // Take profit order price (market)
    SlTriggerPx:     90000,       // Stop loss trigger price
    SlTriggerPxType: "last",      // Stop loss trigger price type
    SlOrdPx:         -1,          // Stop loss order price (market)
}

// Scenario 10: Trigger order with take profit and stop loss (SPOT)
triggerOrder = &triggerOrderRequest{
    InstId:          "BTC-USDT",
    ProductGroup:    "Spot",
    Sz:              "0.001",
    Side:            "buy",
    IsCrossMargin:   "1",
    OrderType:       "market",
    TriggerPrice:    "95000",
    TriggerPxType:   "last",
    TdMode:          "cash",
    TpTriggerPx:     100000,
    TpTriggerPxType: "last",
    TpOrdPx:         -1,
    SlTriggerPx:     90000,
    SlTriggerPxType: "last",
    SlOrdPx:         -1,
}

// Scenario 11: Trigger order with take profit only
triggerOrder = &triggerOrderRequest{
    InstId:          "BTC-USDT-SWAP",
    ProductGroup:    "Swap",
    Sz:              "1",
    Side:            "buy",
    PosSide:         "long",
    IsCrossMargin:   "1",
    OrderType:       "market",
    TriggerPrice:    "95000",
    MrgPosition:     "merge",
    TdMode:          "cross",
    TpTriggerPx:     100000,
    TpTriggerPxType: "last",
    TpOrdPx:         -1,
}

// Scenario 12: Trigger order with stop loss only
triggerOrder = &triggerOrderRequest{
    InstId:          "BTC-USDT-SWAP",
    ProductGroup:    "Swap",
    Sz:              "1",
    Side:            "sell",
    PosSide:         "short",
    IsCrossMargin:   "1",
    OrderType:       "market",
    TriggerPrice:    "95000",
    MrgPosition:     "merge",
    TdMode:          "cross",
    SlTriggerPx:     100000,
    SlTriggerPxType: "last",
    SlOrdPx:         -1,
}

// Scenario 13: Close specific position with trigger order (split position mode)
triggerOrder = &triggerOrderRequest{
    InstId:        "BTC-USDT-SWAP",
    ProductGroup:  "Swap",
    Sz:            "1",
    Side:          "sell",
    PosSide:       "long",
    IsCrossMargin: "1",
    OrderType:     "market",
    TriggerPrice:  "105000",
    MrgPosition:   "split",
    TdMode:        "cross",
    ClosePosId:    "1001063717138767",  // Specify position ID to close
}

Response Parameters
Field	Type	Description
ordId	string	Order ID
clOrdId	string	Client-defined order ID
tag	string	Order tag
sCode	string	Event execution result status code 0: Success
sMsg	string	Message when event execution fails
Response Example
{
  "code": "0",
  "msg": "",
  "data": {
    "ordId": "1000595855275418",
    "clOrdId": "",
    "tag": "",
    "sCode": "0",
    "sMsg": "Success"
  }
}

Take Profit and Stop Loss Feature
Overview
When placing a trigger order, you can optionally set take profit (TP) and/or stop loss (SL) parameters. After the trigger order is executed and a position is opened, the system will automatically create TP/SL orders for that position.

Workflow
1. User places trigger order with TP/SL parameters
   ↓
2. Market price reaches trigger price
   ↓
3. Trigger order executes and opens position
   ↓
4. System automatically creates TP/SL orders for the new position

TP/SL Parameters
Take Profit Parameters:

tpTriggerPx: Take profit trigger price (required if setting TP)
tpTriggerPxType: Trigger price type (last, index, or mark). Default: last
tpOrdPx: Order price when TP is triggered. -1 means market order
Stop Loss Parameters:

slTriggerPx: Stop loss trigger price (required if setting SL)
slTriggerPxType: Trigger price type (last, index, or mark). Default: last
slOrdPx: Order price when SL is triggered. -1 means market order
Usage Notes
Optional Feature: TP/SL parameters are optional. You can:

Set both TP and SL
Set only TP
Set only SL
Set neither (standard trigger order)
Price Relationships:

For long positions: TP trigger price > trigger price > SL trigger price
For short positions: SL trigger price > trigger price > TP trigger price
Trigger Timing: TP/SL orders are created AFTER the trigger order executes and opens a position, not immediately when placing the trigger order

Market vs Limit Orders:

Set tpOrdPx or slOrdPx to -1 for market orders
Set specific price for limit orders
Trigger Price Types:

last: Latest traded price (default)
index: Index price
mark: Mark price
Supported Markets: Both SPOT and SWAP markets support TP/SL on trigger orders

Examples
Example 1: Long position with full TP/SL protection

{
  "instId": "BTC-USDT-SWAP",
  "productGroup": "Swap",
  "sz": "1",
  "side": "buy",
  "posSide": "long",
  "orderType": "market",
  "triggerPrice": "95000",
  "mrgPosition": "merge",
  "tdMode": "cross",
  "tpTriggerPx": 100000,
  "tpTriggerPxType": "last",
  "tpOrdPx": -1,
  "slTriggerPx": 90000,
  "slTriggerPxType": "last",
  "slOrdPx": -1
}

Example 2: Spot buy with TP only

{
  "instId": "BTC-USDT",
  "productGroup": "Spot",
  "sz": "0.001",
  "side": "buy",
  "orderType": "market",
  "triggerPrice": "95000",
  "tdMode": "cash",
  "tpTriggerPx": 100000,
  "tpTriggerPxType": "last",
  "tpOrdPx": -1
}

Example 3: Short position with SL only

{
  "instId": "BTC-USDT-SWAP",
  "productGroup": "Swap",
  "sz": "1",
  "side": "sell",
  "posSide": "short",
  "orderType": "market",
  "triggerPrice": "95000",
  "mrgPosition": "merge",
  "tdMode": "cross",
  "slTriggerPx": 100000,
  "slTriggerPxType": "last",
  "slOrdPx": -1
}

Related APIs
Set Position TP/SL: /deepcoin/trade/set-position-sltp - Set TP/SL for existing positions
Modify Position TP/SL: /deepcoin/trade/modify-position-sltp - Modify existing TP/SL orders
Cancel Position TP/SL: /deepcoin/trade/cancel-position-sltp - Cancel TP/SL orders
Query Pending Trigger Orders: /deepcoin/trade/trigger-orders-pending - Query existing trigger orders


Batch Close Position
Batch Close Position
Batch close all positions for a specified product, supporting spot, coin-margined contracts, and USDT-margined contracts

Request frequency limit: 1/1s

Request URL
POST /deepcoin/trade/batch-close-position

Request Parameters
Field Name	Required	Type	Description
productGroup	true	string	Product group
Spot: Spot
Coin-margined: Swap
USDT-margined: SwapU
instId	true	string	Product ID
Request Example
// Batch close spot positions
{
  "productGroup": "Spot",
  "instId": "BTC-USDT"
}

// Batch close coin-margined contract positions
{
  "productGroup": "Swap",
  "instId": "BTC-USD-SWAP"
}

// Batch close USDT-margined contract positions
{
  "productGroup": "SwapU",
  "instId": "BTC-USDT-SWAP"
}

Response Parameters
Field Name	Type	Description
errorList	array	Error list containing detailed information of failed closures
ClosePositionErrorItem Structure in errorList
Field Name	Type	Description
memberId	string	Member ID
accountId	string	Account ID
tradeUnitId	string	Trade unit ID
instId	string	Product ID
posiDirection	string	Position direction
errorCode	int	Error code
errorMsg	string	Error message
Response Example
// Successful response (all positions closed successfully)
{
  "code": "0",
  "msg": "",
  "data": {
    "errorList": []
  }
}

// Partial failure response
{
  "code": "0",
  "msg": "",
  "data": {
    "errorList": [
      {
        "memberId": "10001",
        "accountId": "100001234",
        "tradeUnitId": "TU001",
        "instId": "BTC-USDT-SWAP",
        "posiDirection": "long",
        "errorCode": 51020,
        "errorMsg": "Insufficient position"
      },
      {
        "memberId": "10001",
        "accountId": "100001234",
        "tradeUnitId": "TU002",
        "instId": "BTC-USDT-SWAP",
        "posiDirection": "short",
        "errorCode": 51008,
        "errorMsg": "Order does not exist"
      }
    ]
  }
}

Description
Functionality
Batch close all positions for a specified product
Supports spot (Spot), coin-margined contracts (Swap), and USDT-margined contracts (SwapU)
Uses concurrent processing to improve efficiency
Returns an error list containing detailed information about all failed closures
Processing Logic
Calls different services (spot/contracts) based on productGroup
Processes multiple position closures concurrently
Collects all position closure failure error information
Even if some positions fail to close, successful positions will still be closed
Notes
This API will close all positions for the specified product, please use with caution
An empty error list indicates all positions were closed successfully
Failed closures of some positions will not affect the closure operations of other positions




Current Funding Rate
Get Current Funding Rate
Get current contract trading pair funding rate

Request frequency limit: 1/1s

Request URL
GET /deepcoin/trade/fund-rate/current-funding-rate

Request Parameters
Field Name	Required	Type	Description
instType	true	string	Contract type
USDT-margined: SwapU
Coin-margined: Swap
instId	false	string	Query specific trading pair funding rate if not empty, query all if empty
Response Parameters
Field Name	Type	Description
>current_fund_rates	object	
>instrumentID	string	Trading pair
>fundingRate	float64	Funding fee rate
Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "current_fund_rates":[
            {
                "instrumentId":"BTCUSD",
                "fundingRate":0.00011794
                }
            ]
            }
}


Funding Rate History
Get Funding Rate History
Get contract trading pair funding rates list

Request frequency limit: 1/1s

Request URL
GET /deepcoin/trade/fund-rate/history

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Query specific trading pair funding rate cycle
page	false	integer	Page number, default 1
size	false	integer	Number of results per page, maximum 100, default 20
Response Parameters
Field Name	Type	Description
code	integer	Status code
msg	string	Error message
data	array	
>instrumentID	string	Trading pair
>CreateTime	integer	Date
>rate	string	Funding fee rate
>ratePeriodSec	integer	Funding fee rate resolve cycle in seconds
Response Example
{
    "code": "0",
    "msg": "",
    "data": 
        {
            "list":[
            {
                "instrumentID":"BTCUSDT",
                "rate":"-0.00005",
                "CreateTime":1744606800,
                "ratePeriodSec":8
            },
            {
                "instrumentID":"BTCUSDT",
                "rate":"-0.00005",
                "CreateTime":1744606200,
                "ratePeriodSec":8
            },

    ]
}
}


Modify Take Profit and Stop Loss for Open Limit Orders
Modify Take Profit and Stop Loss for Open Limit Orders
Modify take profit and stop loss settings for open limit orders.

Request frequency limit: 1/1s

Request URL
POST /deepcoin/trade/replace-order-sltp

Request Parameters
Field Name	Required	Type	Description
orderSysID	true	string	Limit order ID
tpTriggerPx	false	float	Take profit price, not set or value of 0 means cancel the setting
slTriggerPx	false	float	Stop loss price, not set or value of 0 means cancel the setting
Response Parameters
无

Response Example
// Successful modification
{
    "code": "0",
    "msg": "",
    "data": {

    }
}

// Failed modification
{
    "code": "24",
    "msg": "OrderNotFound:10005881114595391",
    "data": null
}


Close Position By IDs
Close Position By IDs
Close specific positions by specified position ID list, supporting spot, coin-margined contracts, and USDT-margined contracts

Request frequency limit: 1/1s

Request URL
POST /deepcoin/trade/close-position-by-ids

Request Parameters
Field Name	Required	Type	Description
productGroup	true	string	Product group
Spot: Spot
Coin-margined: Swap
USDT-margined: SwapU
instId	true	string	Product ID
positionIds	true	[]string	Position ID list, must contain at least one ID
Request Example
// Close specified spot positions
{
  "productGroup": "Spot",
  "instId": "BTC-USDT",
  "positionIds": ["pos123", "pos456"]
}

// Close specified coin-margined contract positions
{
  "productGroup": "Swap",
  "instId": "BTC-USD-SWAP",
  "positionIds": ["pos789", "pos012", "pos345"]
}

// Close specified USDT-margined contract positions
{
  "productGroup": "SwapU",
  "instId": "BTC-USDT-SWAP",
  "positionIds": ["pos678"]
}

// Close multiple positions
{
  "productGroup": "SwapU",
  "instId": "ETH-USDT-SWAP",
  "positionIds": [
    "1001063717138767",
    "1001063717138768",
    "1001063717138769",
    "1001063717138770"
  ]
}

Response Parameters
Field Name	Type	Description
errorList	array	Error list containing detailed information of failed closures
ClosePositionErrorItem Structure in errorList
Field Name	Type	Description
memberId	string	Member ID
accountId	string	Account ID
tradeUnitId	string	Trade unit ID
instId	string	Product ID
posiDirection	string	Position direction
errorCode	int	Error code
errorMsg	string	Error message
Response Example
// Successful response (all specified positions closed successfully)
{
  "code": "0",
  "msg": "",
  "data": {
    "errorList": []
  }
}

// Partial failure response
{
  "code": "0",
  "msg": "",
  "data": {
    "errorList": [
      {
        "memberId": "10001",
        "accountId": "100001234",
        "tradeUnitId": "TU001",
        "instId": "BTC-USDT-SWAP",
        "posiDirection": "long",
        "errorCode": 51020,
        "errorMsg": "Insufficient position"
      },
      {
        "memberId": "10001",
        "accountId": "100001234",
        "tradeUnitId": "TU002",
        "instId": "BTC-USDT-SWAP",
        "posiDirection": "short",
        "errorCode": 51404,
        "errorMsg": "Position does not exist"
      }
    ]
  }
}

// All failures response
{
  "code": "0",
  "msg": "",
  "data": {
    "errorList": [
      {
        "memberId": "10001",
        "accountId": "100001234",
        "tradeUnitId": "TU001",
        "instId": "BTC-USDT-SWAP",
        "posiDirection": "long",
        "errorCode": 51404,
        "errorMsg": "Position does not exist"
      },
      {
        "memberId": "10001",
        "accountId": "100001234",
        "tradeUnitId": "TU002",
        "instId": "BTC-USDT-SWAP",
        "posiDirection": "short",
        "errorCode": 51404,
        "errorMsg": "Position does not exist"
      }
    ]
  }
}

Description
Functionality
Close specific positions by specified position ID list
Supports spot (Spot), coin-margined contracts (Swap), and USDT-margined contracts (SwapU)
Can close multiple specified positions at once
Uses concurrent processing to improve efficiency
Processing Logic
Internally calls the same doClosePositionInternal method as batch close position
Filters through positionIds parameter to only close positions with specified IDs
Processes multiple position closures concurrently
Collects all position closure failure error information
Notes
positionIds must contain at least one position ID
Only positions specified in the list will be closed, other positions will not be affected
An empty error list indicates all specified positions were closed successfully
Failed closures of some positions will not affect the closure operations of other positions
If a position ID does not exist or has already been closed, corresponding error information will be returned in the error list


et Position Take Profit and Stop Loss
Set Position Take Profit and Stop Loss
Set take profit and stop loss for existing positions, supporting both spot and contract trading.

Request frequency limit: 1/s

Rate limit rule: UserID

Request URL
POST /deepcoin/trade/set-position-sltp

Request Parameters
Field Name	Required	Type	Description
instType	true	string	Product type
Spot: SPOT
Contract: SWAP
instId	true	string	Product ID
e.g., BTC-USDT for spot, BTC-USDT-SWAP for contract
posSide	false	string	Position side (required for contract)
Long: long
Short: short
mrgPosition	false	string	Margin position mode (for contract)
Merged: merge
Split: split
tdMode	false	string	Trade mode (for contract)
Cross margin: cross
Isolated margin: isolated
posId	false	string	Position ID (required when mrgPosition is split)
tpTriggerPx	false	string	Take profit trigger price
At least one of TP or SL must be set
tpTriggerPxType	false	string	Take profit trigger price type
Last price: last
Index price: index
Mark price: mark
Default: last
tpOrdPx	false	string	Take profit order price
-1 means market price
Default: -1
slTriggerPx	false	string	Stop loss trigger price
At least one of TP or SL must be set
slTriggerPxType	false	string	Stop loss trigger price type
Last price: last
Index price: index
Mark price: mark
Default: last
slOrdPx	false	string	Stop loss order price
-1 means market price
Default: -1
sz	false	string	Position size for partial TP/SL
Empty means full position
Notes:

At least one of tpTriggerPx or slTriggerPx must be provided
For contract trading with split position mode (mrgPosition=split), posId is required
For spot trading, posSide, mrgPosition, tdMode, and posId are not applicable
Request Example
Spot - Set both take profit and stop loss:

{
  "instType": "SPOT",
  "instId": "BTC-USDT",
  "tpTriggerPx": "107000",
  "slTriggerPx": "102000"
}

Contract - Set take profit and stop loss for long position (merged mode):

{
  "instType": "SWAP",
  "instId": "BTC-USDT-SWAP",
  "posSide": "long",
  "mrgPosition": "merge",
  "tdMode": "cross",
  "tpTriggerPx": "107000",
  "slTriggerPx": "102000"
}

Contract - Set take profit and stop loss for specific position (split mode):

{
  "instType": "SWAP",
  "instId": "BTC-USDT-SWAP",
  "posSide": "long",
  "mrgPosition": "split",
  "tdMode": "isolated",
  "posId": "1000596063679172",
  "tpTriggerPx": "107000",
  "tpTriggerPxType": "mark",
  "tpOrdPx": "-1",
  "slTriggerPx": "102000",
  "slTriggerPxType": "mark",
  "slOrdPx": "-1"
}

Set only take profit:

{
  "instType": "SPOT",
  "instId": "BTC-USDT",
  "tpTriggerPx": "107000"
}

Set only stop loss:

{
  "instType": "SPOT",
  "instId": "BTC-USDT",
  "slTriggerPx": "102000"
}

Response Parameters
Field Name	Type	Description
ordId	string	SLTP Order ID (use this ID to cancel the order)
sCode	string	Event execution result status code
0: Success
sMsg	string	Rejection message if the request is unsuccessful
Response Example
Successful response:

{
  "code": "0",
  "msg": "",
  "data": {
    "ordId": "1001063717138767",
    "sCode": "0",
    "sMsg": ""
  }
}

Failed response:

{
  "code": "51000",
  "msg": "Parameter error",
  "data": {
    "ordId": "",
    "sCode": "51000",
    "sMsg": "At least one of take profit or stop loss must be set"
  }
}

Description
Functionality
Set take profit and/or stop loss for existing positions
Supports both spot (SPOT) and contract (SWAP) trading
Allows partial position TP/SL by specifying sz parameter
Supports different trigger price types (last, index, mark)
Can set market or limit order price for TP/SL execution
Use Cases
Risk Management: Automatically close positions when price reaches target or stop loss level
Profit Protection: Lock in profits when price reaches desired level
Loss Limitation: Limit potential losses by setting stop loss
Partial Position Management: Set TP/SL for only part of the position
Important Notes
Order ID: Save the returned ordId to cancel or modify the TP/SL order later
Price Precision: Trigger prices must comply with the product's price precision requirements
Position Verification: Ensure you have an existing position before setting TP/SL
Overwriting: Setting new TP/SL may overwrite existing TP/SL orders for the same position
Contract Specifics: For contract trading, specify position side (posSide) and margin mode correctly
Related APIs
Modify Position TP/SL: /deepcoin/trade/modify-position-sltp - Modify existing TP/SL orders
Cancel Position TP/SL: /deepcoin/trade/cancel-position-sltp - Cancel TP/SL orders
Query Pending Trigger Orders: /deepcoin/trade/trigger-orders-pending - Query existing TP/SL orders

Cancel Position Take Profit and Stop Loss
Cancel Position Take Profit and Stop Loss
Cancel existing position take profit and stop loss orders, supporting both spot and contract trading.

Request frequency limit: 1/s

Rate limit rule: UserID

Request URL
POST /deepcoin/trade/cancel-position-sltp

Request Parameters
Field Name	Required	Type	Description
instType	true	string	Product type
Spot: SPOT
Contract: SWAP
instId	true	string	Product ID
e.g., BTC-USDT for spot, BTC-USDT-SWAP for contract
ordId	true	string	SLTP Order ID
Obtained from set-position-sltp API response or trigger order query
Notes:

The ordId is returned when setting position TP/SL via the set-position-sltp API
You can also query pending trigger orders to get the ordId
Request Example
Cancel spot position TP/SL:

{
  "instType": "SPOT",
  "instId": "BTC-USDT",
  "ordId": "1000762096073860"
}

Cancel contract position TP/SL:

{
  "instType": "SWAP",
  "instId": "BTC-USDT-SWAP",
  "ordId": "1000596068909100"
}

Response Parameters
Field Name	Type	Description
ordId	string	Order ID
sCode	string	Event execution result status code
0: Success
sMsg	string	Rejection message if the request is unsuccessful
Response Example
Successful response:

{
  "code": "0",
  "msg": "",
  "data": {
    "ordId": "1000762096073860",
    "sCode": "0",
    "sMsg": ""
  }
}

Failed response (order not found):

{
  "code": "51400",
  "msg": "Order does not exist",
  "data": {
    "ordId": "1000762096073860",
    "sCode": "51400",
    "sMsg": "Order does not exist"
  }
}

Failed response (order already executed):

{
  "code": "51401",
  "msg": "Order already executed",
  "data": {
    "ordId": "1000762096073860",
    "sCode": "51401",
    "sMsg": "Order already executed or canceled"
  }
}

Description
Functionality
Cancel existing position take profit and stop loss orders
Supports both spot (SPOT) and contract (SWAP) trading
Can only cancel pending TP/SL orders (not yet triggered)
Use Cases
Strategy Adjustment: Cancel existing TP/SL to set new levels
Market Change Response: Remove TP/SL when market conditions change
Manual Control: Take manual control of position closing instead of automatic TP/SL
Error Correction: Cancel incorrectly set TP/SL orders
Important Notes
Order ID Required: You must have the ordId from the set-position-sltp response
Order Status: Can only cancel pending orders; already triggered or executed orders cannot be canceled
Query Orders: Use the trigger-orders-pending API to query existing TP/SL orders and get their IDs
Timing: Once a TP/SL order is triggered, it cannot be canceled
Verification: Ensure the order belongs to your account before attempting to cancel
Related APIs
Set Position TP/SL: /deepcoin/trade/set-position-sltp - Set new TP/SL orders
Modify Position TP/SL: /deepcoin/trade/modify-position-sltp - Modify existing TP/SL orders
Query Pending Trigger Orders: /deepcoin/trade/trigger-orders-pending - Query existing TP/SL orders
Query Trigger Order History: /deepcoin/trade/trigger-orders-history - Query historical TP/SL orders

Modify Position Take Profit and Stop Loss
Modify Position Take Profit and Stop Loss
Modify existing position take profit and stop loss orders, supporting both spot and contract trading.

Request frequency limit: 1/s

Rate limit rule: UserID

Request URL
POST /deepcoin/trade/modify-position-sltp

Request Parameters
Field Name	Required	Type	Description
instType	true	string	Product type
Spot: SPOT
Contract: SWAP
instId	true	string	Product ID
e.g., BTC-USDT for spot, BTC-USDT-SWAP for contract
ordId	true	string	SLTP Order ID (obtained from set-position-sltp response)
posSide	false	string	Position side (required for contract)
Long: long
Short: short
mrgPosition	false	string	Margin position mode (for contract)
Merged: merge
Split: split
tdMode	false	string	Trade mode (for contract)
Cross margin: cross
Isolated margin: isolated
posId	false	string	Position ID (required when mrgPosition is split)
tpTriggerPx	false	string	Take profit trigger price
At least one of TP or SL must be set
tpTriggerPxType	false	string	Take profit trigger price type
Last price: last
Index price: index
Mark price: mark
Default: last
tpOrdPx	false	string	Take profit order price
-1 means market price
Default: -1
slTriggerPx	false	string	Stop loss trigger price
At least one of TP or SL must be set
slTriggerPxType	false	string	Stop loss trigger price type
Last price: last
Index price: index
Mark price: mark
Default: last
slOrdPx	false	string	Stop loss order price
-1 means market price
Default: -1
sz	false	string	Position size for partial TP/SL
Empty means full position
Notes:

ordId is required and must be a valid pending SLTP order ID
At least one of tpTriggerPx or slTriggerPx must be provided
For contract trading with split position mode (mrgPosition=split), posId is required
For spot trading, posSide, mrgPosition, tdMode, and posId are not applicable
The order ID is obtained from the set-position-sltp API response
Request Example
Spot - Modify both take profit and stop loss:

{
  "instType": "SPOT",
  "instId": "BTC-USDT",
  "ordId": "1000762096073860",
  "tpTriggerPx": "110000",
  "slTriggerPx": "103000"
}

Contract - Modify TP/SL for long position (merged mode):

{
  "instType": "SWAP",
  "instId": "BTC-USDT-SWAP",
  "ordId": "1000596069447069",
  "posSide": "long",
  "mrgPosition": "merge",
  "tdMode": "cross",
  "tpTriggerPx": "110000",
  "tpTriggerPxType": "mark",
  "tpOrdPx": "-1",
  "slTriggerPx": "103000",
  "slTriggerPxType": "mark",
  "slOrdPx": "-1"
}

Contract - Modify TP/SL for specific position (split mode):

{
  "instType": "SWAP",
  "instId": "BTC-USDT-SWAP",
  "ordId": "1000596069492933",
  "posSide": "long",
  "mrgPosition": "split",
  "tdMode": "isolated",
  "posId": "1000596069432784",
  "tpTriggerPx": "111000",
  "tpTriggerPxType": "mark",
  "tpOrdPx": "-1",
  "slTriggerPx": "104000",
  "slTriggerPxType": "mark",
  "slOrdPx": "-1",
  "sz": "200"
}

Modify only take profit:

{
  "instType": "SWAP",
  "instId": "BTC-USDT-SWAP",
  "ordId": "1000596069447069",
  "posSide": "long",
  "mrgPosition": "merge",
  "tdMode": "cross",
  "tpTriggerPx": "112000",
  "tpTriggerPxType": "mark",
  "tpOrdPx": "-1"
}

Modify only stop loss:

{
  "instType": "SWAP",
  "instId": "BTC-USDT-SWAP",
  "ordId": "1000596069447069",
  "posSide": "long",
  "mrgPosition": "merge",
  "tdMode": "cross",
  "slTriggerPx": "101000",
  "slTriggerPxType": "mark",
  "slOrdPx": "-1"
}

Response Parameters
Field Name	Type	Description
ordId	string	SLTP Order ID
sCode	string	Event execution result status code
0: Success
sMsg	string	Rejection message if the request is unsuccessful
Response Example
Successful response:

{
  "code": "0",
  "msg": "",
  "data": {
    "ordId": "1000596069447069",
    "sCode": "0",
    "sMsg": ""
  }
}

Failed response:

{
  "code": "51400",
  "msg": "Order not found",
  "data": {
    "ordId": "",
    "sCode": "51400",
    "sMsg": "Order does not exist or has been executed"
  }
}

Description
Functionality
Modify existing position take profit and/or stop loss orders
Supports both spot (SPOT) and contract (SWAP) trading
Allows partial position TP/SL modification by specifying sz parameter
Supports different trigger price types (last, index, mark)
Can modify market or limit order price for TP/SL execution
Can modify only take profit or only stop loss independently
Use Cases
Strategy Adjustment: Adjust TP/SL levels based on market conditions
Risk Management: Tighten or loosen stop loss based on position performance
Profit Optimization: Adjust take profit targets as price moves favorably
Partial Position Management: Modify TP/SL for only part of the position
Important Notes
Order ID Required: Must provide valid ordId from the set-position-sltp response
Order Status: Can only modify pending TP/SL orders (not yet triggered or executed)
Price Precision: Trigger prices must comply with the product's price precision requirements
Parameter Consistency: Parameters like instId, posSide, mrgPosition should match the original order
At Least One: Must modify at least one of take profit or stop loss
Split Mode: For split position mode, posId is required
Query Orders: Use trigger-orders-pending API to query existing TP/SL orders and get their IDs
Related APIs
Set Position TP/SL: /deepcoin/trade/set-position-sltp - Create new TP/SL orders
Cancel Position TP/SL: /deepcoin/trade/cancel-position-sltp - Cancel TP/SL orders
Query Pending Trigger Orders: /deepcoin/trade/trigger-orders-pending - Query existing TP/SL orders
Common Errors
Error Code	Error Message	Solution
51400	Order not found	Check if ordId is correct and order has not been canceled or executed
51000	Parameter error	Verify all required parameters are provided and formatted correctly
51001	At least one of TP or SL must be set	Provide at least tpTriggerPx or slTriggerPx


Get Pending Trigger Orders
Get Pending Trigger Orders
Query all pending trigger orders under the current account

Request URL
GET /deepcoin/trade/trigger-orders-pending

Request Parameters
Field	Required	Type	Description
instType	Yes	string	Instrument type
Spot: SPOT
Swap: SWAP
instId	Yes	string	Instrument ID, e.g.BTC-USDT-SWAP
orderType	No	string	Trigger order type
Limit: limit
Market: market
limit	No	integer	Number of results per request. The maximum is 100; The default is 100. Range: 1-100
Response Parameters
Field	Type	Description
instType	string	Instrument type, e.g.SWAP
instId	string	Instrument ID, e.g.BTC-USDT-SWAP
ordId	string	Order ID
triggerPx	string	Trigger price
ordPx	string	Order price
sz	string	Order size
ordType	string	Order type
Market: market
Limit: limit
side	string	Order side
Buy: buy
Sell: sell
posSide	string	Position side
Long: long
Short: short
tdMode	string	Trade mode
Cross: cross
Isolated: isolated
triggerOrderType	string	Trigger order type
TPSL: Take-profit/Stop-loss
Conditional: Conditional order
Serial: Serial order
Indicator: Indicator order
Complex: Complex indicator
Tracking: Tracking exit
Line: Line drawing order
triggerPxType	string	Trigger price type
Last: last
Index: index
Mark: mark
lever	string	Leverage
slPrice	string	Stop-loss price
slTriggerPrice	string	Stop-loss trigger price
tpPrice	string	Take-profit price
tpTriggerPrice	string	Take-profit trigger price
closeSLTriggerPrice	string	Open position stop-loss price
closeTPTriggerPrice	string	Open position take-profit price
cTime	string	Order creation time, Unix timestamp in milliseconds format
uTime	string	Order status update time, Unix timestamp in milliseconds format
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "ordId": "1000595888037394",
            "triggerPx": "0",
            "ordPx": "0",
            "sz": "0",
            "ordType": "",
            "side": "sell",
            "posSide": "long",
            "tdMode": "cross",
            "triggerOrderType": "TPSL",
            "triggerPxType": "last",
            "lever": "11",
            "slPrice": "0",
            "slTriggerPrice": "110001",
            "tpPrice": "0",
            "tpTriggerPrice": "170001",
            "closeSLTriggerPrice": "",
            "closeTPTriggerPrice": "",
            "cTime": "1758028926000",
            "uTime": "1758028926000"
        },
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "ordId": "1000595888000274",
            "triggerPx": "150001",
            "ordPx": "130001",
            "sz": "201",
            "ordType": "",
            "side": "buy",
            "posSide": "long",
            "tdMode": "cross",
            "triggerOrderType": "Conditional",
            "triggerPxType": "last",
            "lever": "11",
            "slPrice": "130001",
            "slTriggerPrice": "150001",
            "tpPrice": "0",
            "tpTriggerPrice": "0",
            "closeSLTriggerPrice": "",
            "closeTPTriggerPrice": "",
            "cTime": "1758026859000",
            "uTime": "1758026859000"
        },
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "ordId": "1000595887990299",
            "triggerPx": "150000",
            "ordPx": "130000",
            "sz": "200",
            "ordType": "",
            "side": "buy",
            "posSide": "long",
            "tdMode": "cross",
            "triggerOrderType": "Conditional",
            "triggerPxType": "last",
            "lever": "11",
            "slPrice": "",
            "slTriggerPrice": "",
            "tpPrice": "",
            "tpTriggerPrice": "",
            "closeSLTriggerPrice": "110000",
            "closeTPTriggerPrice": "160000",
            "cTime": "1758026306000",
            "uTime": "1758026306000"
        }
    ]
}



Get Triggered Order History
Get Triggered Order History
Query triggered condition order history

Request URL
GET /deepcoin/trade/trigger-orders-history

Request Parameters
Field	Required	Type	Description
instType	Yes	string	Instrument type
Spot: SPOT
Swap: SWAP
instId	Yes	string	Instrument ID, e.g.BTC-USDT-SWAP
OrderType	No	string	Trigger order type
Limit: limit
Market: market
limit	No	integer	Number of results per request. The maximum is 100; The default is 100. Range: 1-100
ordId	No	string	Order ID
Response Parameters
Field	Type	Description
instType	string	Instrument type, e.g.SWAP
instId	string	Instrument ID, e.g.BTC-USDT-SWAP
ordId	string	Order ID
px	string	Order price
sz	string	Order size
triggerPx	string	Trigger price
triggerPxType	string	Trigger price type
Last: last
Index: index
Mark: mark
ordType	string	Trigger order type
TPSL: Take-profit/Stop-loss
Conditional: Conditional order
Serial: Serial order
Indicator: Indicator order
Complex: Complex indicator
Tracking: Tracking exit
Line: Line drawing order
side	string	Order side
Buy: buy
Sell: sell
posSide	string	Position side
Long in open/close mode: long
Short in open/close mode: short
Net mode: net
tdMode	string	Trade mode
Cross: cross
Isolated: isolated
Cash: cash
lever	string	Leverage
triggerTime	string	Trigger time, Unix timestamp in milliseconds format, e.g.1597026383085
Value 0 means not triggered
uTime	string	Order status update time, Unix timestamp in milliseconds format
cTime	string	Order creation time, Unix timestamp in milliseconds format
errorCode	string	Error code
0: Success
4: Invalid operation
errorMsg	string	Error message, e.g.InvalidAction:OrderType=5,CFDPriceIsNull
Response Example
{
    "code": "0",
    "msg": "",
    "data": [
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "ordId": "1000595886219036",
            "px": "140000",
            "sz": "100",
            "triggerPx": "150000",
            "triggerPxType": "last",
            "ordType": "Conditional",
            "side": "buy",
            "posSide": "long",
            "tdMode": "cross",
            "lever": "11",
            "triggerTime": "0",
            "uTime": "1758026276000",
            "cTime": "1757918143",
            "errorCode": "0",
            "errorMsg": ""
        },
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "ordId": "1000595882098321",
            "px": "0",
            "sz": "200",
            "triggerPx": "0",
            "triggerPxType": "last",
            "ordType": "TPSL",
            "side": "sell",
            "posSide": "long",
            "tdMode": "cross",
            "lever": "11",
            "triggerTime": "0",
            "uTime": "1758026278000",
            "cTime": "1757660515",
            "errorCode": "0",
            "errorMsg": ""
        },
        {
            "instType": "SWAP",
            "instId": "BTC-USDT-SWAP",
            "ordId": "1000594091040387",
            "px": "0",
            "sz": "0",
            "triggerPx": "80000",
            "triggerPxType": "last",
            "ordType": "TPSL",
            "side": "sell",
            "posSide": "long",
            "tdMode": "cross",
            "lever": "1",
            "triggerTime": "1751505074",
            "uTime": "1751505074000",
            "cTime": "1749695677",
            "errorCode": "4",
            "errorMsg": "InvalidAction:OrderType=5,CFDPriceIsNull"
        }
    ]
}

Notes
This endpoint returns triggered condition order history, including both successfully triggered and failed triggered orders
triggerTime of 0 indicates the order has not been triggered yet
errorCode of 0 means success, other values indicate failure
px of 0 indicates a market order, non-zero value indicates a limit order
Results are sorted in descending order by update time, with the most recent records first


trace order
trace order
It's supported only when you in Cross Margin Mode and have merge position

Request frequency limit: 1/1s

Request URL
POST /deepcoin/trade/trace-order

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
retracePoint	true	string	pullback spread
triggerPrice	true	string	Activation price, "0": Cancel order, "-1": Activate immediately;
The positive price is for setting an activation order and must maintain a price difference of 0.1% from the latest price; other prices are invalid.
posSide	true	string	Position side
product type must be SWAP
Long: long
Short: short
Request Example
{
  "instId": "BTC-USDT-SWAP",
  "retracePoint": "1000",
  "triggerPrice": "-1",
  "posSide": "long"
}


Response Parameters
None

Response Example
{
    "code": "0",
    "msg": "",
    "data": {}
}

Get pending trace order list
Request frequency limit: 1/1s

Request URL
GET /deepcoin/trade/trace-order-list

Request Parameters
Field Name	Required	Type	Description
instId	true	string	Product ID
Response Parameters
Field Name	Type	Description
retracePoint	string	pullback spread
triggerPrice	string	activation price
breakPrice	string	breakout price
isTriggered	int	activated or not,1:activated,0:not activated
posSide	string	Position side
Long: long
Short: short
createTime	int	created time
Response Example
{ 
  "code":"0",
  "msg":"",
  "data":[
    {
      "triggerPrice":"87195",
      "breakPrice":"87329.8",
      "retracePoint":"1500",
      "isTriggered":1,
      "posSide":"long",
      "createTime":1763954015
    }
  ]
}


Private websocket
Private websocket
Private websocket address
mainnet: wss://stream.deepcoin.com/v1/private

Get listenkey
HTTP Method: GET

HTTP Request: /deepcoin/listenkey/acquire

response:

{
  "code": "0",
  "msg": "",
  "data": {
    "listenkey": "a29e6d260bb2a82478abf49759cb31a9",
    "expire_time": 1691403285
  }
}

Extend expiration time
By sliding window, the expiration time will be extended for another hour

HTTP Method: GET

HTTP Request: /deepcoin/listenkey/extend

body listenkey="f24739a259bc1ac714dad2ac6690c816"

response:

{
  "code": "0",
  "msg": "",
  "data": {
    "listenkey": "a29e6d260bb2a82478abf49759cb31a9",
    "expire_time": 1691403285
  }
}

Subscribe ws
wss://stream.deepcoin.com/v1/private?listenKey=404879eae0a969e199d2bc3f3766faa1

Return parameters
Currently, once the subscription is successful, fund changes, order changes, etc. will be pushed at once.


Private websocket



Order
Order
Response Parameters
Field Name	Type	Example	Short Name	Description
LocalID	string	""	L	Order local identifier
InstrumentID	string	"BTCUSDT"	I	Instrument id
OrderPriceType	string	"9"	OPT	Order price type
Direction	string	"0"	D	Buy/sell direction
OffsetFlag	string	0	o	Open/close flag
Price	float	30027.5	P	Order price
Volume	int	1	V	Volume
OrderType	string	"0"	OT	Order type
IsCrossMargin	int	1	i	Is cross margin
OrderSysID	string	"1000466073187710"	OS	Order ID
Leverage	int	125	l	Leverage
OrderStatus	string	"1"	Or	Order status
VolumeTraded	int	1	v	Traded volume
InsertTime	int	1689727080	IT	DB Insert time
UpdateTime	int	1689727080	U	DB Update time
Turnover	float	30.0275	T	Transaction amount
PosiDirection	string	"0"	p	Position long/short direction
TradePrice	float	30027.5	t	Average transaction price
Response Example
{
  "action": "PushOrder",
  "result": [
    {
      "table": "Order",
      "data": {
        "D": "1",
        "I": "BTCUSDT",
        "IT": 1690804738,
        "L": "1000175061255804",
        "O": "9",
        "OS": "1000175061255804",
        "OT": "0",
        "Or": "1",
        "P": 29365,
        "T": 1616.621,
        "U": 1690804738,
        "V": 55,
        "i": 0,
        "l": 125,
        "o": "0",
        "p": "1",
        "t": 29393.1090909091,
        "v": 55
      }
    }
  ]
}

Asset Notification
Asset
Response Parameters
Field Name	Type	Example	Short Name	Description
AccountID	string	"8644930"	A	Account ID
Currency	string	"BCH"	C	Currency
MemberID	string	"8644930"	M	Member ID
Available	float	1.020878361	a	Available amount
Withdrawable	float	1.020878361	W	Withdrawable amount
Balance	float	1.05827892	B	Balance
UseMargin	float	0.037400559	u	Margin used
CloseProfit	float	0.19237793	CP	Close P/L
FrozenMargin	int	0	FM	Frozen margin
FrozenFee	int	0	FF	Frozen fee
Response Example
{
  "action": "PushAccount",
  "result": [
    {
      "table": "Account",
      "data": {
        "A": "36005550",
        "B": 1998332.7691469,
        "C": "USDT",
        "M": "36005550",
        "W": 1998316.543355371,
        "a": 1998316.543355371,
        "c": 2.02499997,
        "u": 12.932968
      }
    }
  ]
}

osition Notification
Position
Response Parameters
Field Name	Type	Example	Short Name	Description
MemberID	string	455725	M	Member ID
InstrumentID	string	ETHUSD	I	Instrument id
PosiDirection	string	1	p	Position long/short direction
Position	int	40	Po	Position
UseMargin	float	0.108207952	u	Margin used
CloseProfit	int	0	CP	Close P/L
OpenPrice	int	1779.275975	OP	Open price
Leverage	int	2	l	Leverage
AccountID	string	"455725"	A	Account ID
IsCrossMargin	int	0	i	Whether is cross-margin
UpdateTime	int	1683885945	U	DB update time
Response Example
{
  "action": "PushPosition",
  "result": [
    {
      "table": "Position",
      "data": {
        "A": "36005550",
        "I": "BTCUSDT",
        "M": "36005550",
        "OP": 29393.1090909091,
        "Po": 55,
        "U": 1690804738,
        "c": 0,
        "i": 0,
        "l": 125,
        "p": "1",
        "u": 12.932968
      }
    }
  ]
}


Trade Notification
Trade
Response Parameters
Field Name	Type	Example	Short Name	Description
TradeID	string	"1000265430292943"	TI	Trade ID
Direction	string	"0"	D	Buy/sell direction
OrderSysID	string	"1000466047366963"	OS	Order ID
MemberID	string	"9052130"	M	Member ID
AccountID	string	"9052130"	A	Account ID
InstrumentID	string	"ETHUSDT"	I	Instrument id
OffsetFlag	string	"8"	o	Open/close flag
Price	float	1883.23	P	Transaction price
Volume	int	50	V	Volume
TradeTime	int	1689698910	TT	Transaction time
MatchRole	string	"1"	m	Match role
ClearCurrency	string	"USDT"	CC	Clearing currency
Fee	float	5.64969	F	Fee
FeeCurrency	string	"USDT"	f	Fee currency
CloseProfit	float	39.34273504	CP	Close P/L
Turnover	float	9416.15	T	Turnover
Leverage	int	125	l	Leverage
InsertTime	int	1689698910	IT	DB Insert time
Response Example
{
  "action": "PushTrade",
  "result": [
    {
      "table": "Trade",
      "data": {
        "A": "36005550",
        "CC": "USDT",
        "D": "1",
        "F": 0.026451,
        "I": "BTCUSDT",
        "IT": 1690804738,
        "M": "36005550",
        "OS": "1000175061255804",
        "P": 29390,
        "T": 29.39,
        "TI": "1000168389225300",
        "TT": 1690804738,
        "V": 1,
        "c": 0,
        "f": "USDT",
        "l": 125,
        "m": "1",
        "o": "0"
      }
    }
  ]
}


Account Details
Account Details
Response Parameters
Field Name	Type	Example	Short Name	Description
AccountDetailID	string	"1000256882229328"	AD	Account detail ID
MemberID	string	"471114"	M	Member ID
InstrumentID	string	"BCHUSD"	I	Instrument ID
AccountID	string	"471114"	A	Account ID
Currency	string	"BCH"	C	Currency
Amount	float	-0.00009545	Am	Amount
PreBalance	float	5.83568833	PB	Last static balance
Balance	float	5.83559288	B	Static balance
Source	string	"7"	S	Financial transaction type
1: "P/L"
2: "Income and Expenditure"
3: "System Transfer In"
4: "Withdraw to"
5: "Transaction Fee"
7: "Funding Fee"
8: "Settlement"
a: "Liquidation"
g: "Withheld Profits"
h: "Refunded withheld profit share"
i: "Copy trading profit share"
j: "Trial bonus issuance"
k: "Trial money recovery"
i: "Copy trading profit share"
j: "Trial bonus issuance"
k: "Trial money recovery"
Remark	string	""	R	Remark
InsertTime	int	1689696006	IT	DB Insert time
RelatedID	string	""	r	Related ID
Response Example
{
  "action": "PushAccountDetail",
  "result": [
    {
      "table": "AccountDetail",
      "data": {
        "A": "36005550",
        "AD": "1000167140823738",
        "Am": -0.026451,
        "B": 1998332.7691469,
        "C": "USDT",
        "I": "BTCUSDT",
        "IT": 1690804738,
        "M": "36005550",
        "PB": 1998332.7955979,
        "R": "",
        "S": "5",
        "r": "1000168389225300"
      }
    }
  ]
}


Trigger Order Notification
Trigger Order Notification
Response Parameters
Field Name	Type	Example	Short Name	Description
MemberID	string	"8853509"	M	Member ID
TradeUnitID	string	"8853509"	TU	Position ID
AccountID	string	"8853509"	A	Account ID
InstrumentID	string	"BTCUSDT"	I	Instrument ID
OrderPriceType	string	"0"	OPT	Order price type
Direction	string	"1"	D	Buy/sell direction
OffsetFlag	string	"5"	o	Open/close flag
OrderType	string	"0"	OT	Order type
OrderSysID	string	"1000466073338447"	OS	Order ID
Leverage	int	125	l	Leverage
SLPrice	int	31000	SL	Stop loss price
SLTriggerPrice	int	29000	SLT	Stop loss trigger price
TPPrice	int	30010	TP	Take profit price
TPTriggerPrice	int	30000	TPT	Take profit trigger price
TriggerOrderType	string	"1"	TO	Trigger order type
TriggerPriceType	string	"0"	Tr	Trigger price type
TriggerStatus	int	"1"	TS	Trigger status
InsertTime	int	1689727248	IT	DB Insert time
UpdateTime	int	1689727248	U	DB Update time
Response Example
{
  "action": "PushTriggerOrder",
  "result": [
    {
      "table": "TriggerOrder",
      "data": {
        "A": "36005550",
        "D": "0",
        "I": "BTCUSDT",
        "IT": 1690786912,
        "M": "36005550",
        "O": "0",
        "OS": "1000175049516168",
        "OT": "0",
        "TO": "3",
        "TP": 20001,
        "TPT": 20000,
        "TS": "1",
        "TU": "36005550",
        "Tr": "0",
        "U": 1690786912,
        "l": 85,
        "o": "0"
      }
    }
  ]
}


Public WebSocket
Mainnet
Contracts: wss://stream.deepcoin.com/streamlet/trade/public/swap?platform=api

Spot: wss://stream.deepcoin.com/streamlet/trade/public/spot?platform=api

Request parameters for version 2： ?platform=api&version=v2

Access Method
# Send Heartbeat

request:
ping
response:
pong

Request Parameters
Subscribe Parameters
parameter	required	type	description	remark
Action	yes	string	Subscription operation	0:Unsubscribe all;1:Subscribe;2:Unsubscribe;
FilterValue	yes	string	Filter value	Format:$ExchangeID_$InstrumentID_$Period Period range[1m:1 minute;5m:5 minutes;15m:15 minutes;30m:30 minutes;1h:1 hour;4h:4 hours;12h:12 hours;1d:1 day;1w:1 week;1o:1 month;1y:1 year;] Spot uses BASE/QUOTE (e.g. DeepCoin_BTC/USDT), contracts do not use a slash (e.g. DeepCoin_BTCUSDT).
LocalNo	yes	int	Local unique identifier	Greater than 0, string comparison, customized, cannot be repeated in one session
ResumeNo	yes	int	Resume number	0:Start from the beginning;-1:Resume from the latest position on the server;
TopicID	yes	string	Subscription topic ID	2:Transaction details
v2
parameter	required	type	description	remark
Action	yes	string	Subscription operation	0:Unsubscribe all;1:Subscribe;2:Unsubscribe;
Symbol	yes	string	Filter value	Format: $InstrumentID_$Period Period Period range[1m:1 分钟;5m:5 分钟;15m:15 分钟;30m:30 分钟;1h:1 小时;4h:4 小时;12h:12 小时;1d:一天;1w:一个星期;1o:一个月;1y:一年;] Spot uses BASE/QUOTE（e.g. BTC/USDT）， contracts do not use a slash （e.g. BTCUSDT)。
LocalNo	yes	int	Local unique identifier	Greater than 0, string comparison, customized, cannot be repeated in one session
ResumeNo	yes	int	Resume number	0:Start from the beginning;-1:Resume from the latest position on the server;
Topic	yes	string	Subscription topic ID	market-latest tick;trade-recently;kline-k line;book25-25Level Incremental Market Data;liquidationOrder-Liquidation Order


The Latest Market Data
The-latest-market-data
V1
Request
Spot Request
{
  "SendTopicAction": {
    "Action": "1",
    "FilterValue": "DeepCoin_BCH/USDT",
    "LocalNo": 9,
    "ResumeNo": -2,
    "TopicID": "7"
  }
}

Contracts Request
{
  "SendTopicAction": {
    "Action": "1",
    "FilterValue": "DeepCoin_BCHUSDT",
    "LocalNo": 9,
    "ResumeNo": -2,
    "TopicID": "7"
  }
}

Response Parameters
Field	Type	Example	Description
I	string	"BTCUSDT"	Instrument ID
U	int	1757642301089	The latest update time(ms)
PF	int	1756690200	Position fee time
C	double	173183.6	Upper limit price
F	double	57727.9	Lower limit price
D	double	115455.77	Underlying price
M	double	115473.7	Marked price
H	double	116346	The highest price of the day
L	double	114132.8	The lowest price of the day
N	double	115482.9	The latest price
V	double	7688046	Today's volume
T	double	885654450.392686	Today's turnover
O	double	114206.7	Today's open price
PF	double	0.0005251816	Previous position fee rate
Response Example
{
    "a": "PO",
    "m": "Success",
    "tt": 1757642301185,
    "mt": 1757642301185,
    "r": [
        {
            "d": {
                "I": "BTCUSDT",
                "U": 1757642301089,
                "PF": 1756690200,
                "E": 0.0005251816,
                "O": 114206.7,
                "H": 116346,
                "L": 114132.8,
                "V": 7688046,
                "T": 885654450.392686,
                "N": 115482.9,
                "M": 115473.7,
                "D": 115455.77,
                "V2": 19978848,
                "T2": 2288286517.724497,
                "F": 57727.9,
                "C": 173183.6,
                "BP1": 115482.8,
                "AP1": 115482.9
            }
        }
    ]
}

V2
Request
Spot Request
{
  "Action": "1",
  "Symbol": "BTC/USDT",
  "LocalNo": 6,
  "ResumeNo": -1,
  "Topic": "market"
}

Contracts Request
{
  "Action": "1",
  "Symbol": "BTCUSDT",
  "LocalNo": 6,
  "ResumeNo": -1,
  "Topic": "market"
}

Response Parameters
Field	Type	Example	Description
I	string	"BTCUSDT"	Instrument ID
U	int	1757642301089	The latest update time(ms)
PF	int	1756690200	Position fee time
C	double	173183.6	Upper limit price
F	double	57727.9	Lower limit price
D	double	115455.77	Underlying price
M	double	115473.7	Marked price
H	double	116346	The highest price of the day
L	double	114132.8	The lowest price of the day
N	double	115482.9	The latest price
V	double	7688046	Today's volume
T	double	885654450.392686	Today's turnover
O	double	114206.7	Today's open price
PF	double	0.0005251816	Previous position fee rate
Response Example
{
  "a": "PO",
  "m": "Success",
  "tt": 1757642301185,
  "mt": 1757642301185,
  "d": {
    "I": "BTCUSDT",
    "U": 1757642301089,
    "PF": 1756690200,
    "E": 0.0005251816,
    "O": 114206.7,
    "H": 116346,
    "L": 114132.8,
    "V": 7688046,
    "T": 885654450.392686,
    "N": 115482.9,
    "M": 115473.7,
    "D": 115455.77,
    "V2": 19978848,
    "T2": 2288286517.724497,
    "F": 57727.9,
    "C": 173183.6,
    "BP1": 115482.8,
    "AP1": 115482.9
  }
}



Last Transactions
Last-transactions
V1
Request
Spot Request
{
  "SendTopicAction": {
    "Action": "1",
    "FilterValue": "DeepCoin_BTC/USDT",
    "LocalNo": 9,
    "ResumeNo": -2,
    "TopicID": "2"
  }
}

Contracts Request
{
  "SendTopicAction": {
    "Action": "1",
    "FilterValue": "DeepCoin_BTCUSDT",
    "LocalNo": 9,
    "ResumeNo": -2,
    "TopicID": "2"
  }
}

Response Parameters
Field Name	Type	Example	Description
TradeID	string	"1000170423277947"	Traded ID
I	string	"ETHUSDT"	Instrument ID
D	string	"1"	Direction
P	int	4519.91	Price
V	float	4	Volume
T	int	1757640595	Traded time
Response Example
{
    "a": "PMT",
    "b": 0,
    "tt": 1757640595167,
    "mt": 1757640595167,
    "r": [
        {
            "d": {
                "TradeID": "1000170423277947",
                "I": "ETHUSDT",
                "D": "1",
                "P": 4519.91,
                "V": 4,
                "T": 1757640595
            }
        }
    ]
}

V2
Request
Spot Request
{
  "Action": "1",
  "Symbol": "BTC/USDT",
  "LocalNo": 6,
  "ResumeNo": -1,
  "Topic": "trade"
}

Contracts Request
{
  "Action": "1",
  "Symbol": "BTCUSDT",
  "LocalNo": 6,
  "ResumeNo": -1,
  "Topic": "trade"
}

Response Parameters
Field Name	Type	Example	Description
TradeID	string	"1000170423277947"	Traded ID
i	string	"ETHUSDT"	Instrument ID
D	string	"1"	Direction
P	int	4519.91	Price
V	float	4	Volume
T	int	1757640595	Traded time
Response Example
{
  "a": "PMT",
  "b": 0,
  "i": "ETHUSDT",
  "tt": 1771924508470,
  "mt": 1771924508470,
  "d": [
    {
      "TradeID": "1000300469088080",
      "D": "1",
      "P": 1826.76,
      "V": 1.0,
      "T": 1771924508
    }
  ]
}

K-Lines (only support 1 minute)
K-Lines currently only support 1 minute
ResumeNo： -1 means the latest record,-30 means the latest 30 historical records.

V1
Request
Spot Request
{
  "SendTopicAction": {
    "Action": "1",
    "FilterValue": "DeepCoin_BTC/USDT_1m",
    "LocalNo": 6,
    "ResumeNo": -1,
    "TopicID": "11"
  }
}

Contracts Request
{
  "SendTopicAction": {
    "Action": "1",
    "FilterValue": "DeepCoin_BTCUSDT_1m",
    "LocalNo": 6,
    "ResumeNo": -1,
    "TopicID": "11"
  }
}

Response Parameters
Field Name	Type	Example	Description
I	string	"BTCUSDT"	Instrument ID
P	string	"1m"	Period
B	int	1757640420	Begin time
O	float	115819	Open price
C	float	115788.4	Close price
H	float	115819	The highest price
L	float	115787.6	The lowest price
V	float	4989	Volume
M	float	577697.5531	Turnover
Response Example
{
    "a": "PK",
    "tt": 1757640455199,
    "mt": 1757640455199,
    "r": [
        {
            "d": {
                "I": "BTCUSDT",
                "P": "1m",
                "B": 1757640420,
                "O": 115819,
                "C": 115788.4,
                "H": 115819,
                "L": 115787.6,
                "V": 4989,
                "M": 577697.5531
            },
            "t": "LK"
        }
    ]
}

V2
Request
Spot Request
{
  "Action": "1",
  "Symbol": "BTC/USDT_1m",
  "LocalNo": 6,
  "ResumeNo": -1,
  "Topic": "kline"
}

Contracts Request
{
  "Action": "1",
  "Symbol": "BTCUSDT_1m",
  "LocalNo": 6,
  "ResumeNo": -1,
  "Topic": "kline"
}

Response Parameters
Field Name	Type	Example	Description
tt	int	1757640455199	Trading timestamp
mt	int	1757640455199	Market timestamp
i	string	"BTCUSDT"	Instrument ID
p	string	1m	Period
d	array		data
Response Example
{
  "a": "PK",
  "tt": 1757640455199,
  "mt": 1757640455199,
  "i": "BTCUSDT",
  "p": "1m",
  "d": [
    [
      "1739157660000",  // Timestamp
      "95900.5",        // Open price
      "95932.2",        // Highest price
      "95850.4",        // Lowest price
      "95913.4",        // Close price
      "20084",          // Volume (base currency)
      "1925967.4841"    // Volume (quote currency)
    ]
  ]
}

25-Level Incremental Market Data
25-level-incremental-market-data
Notification push frequency: 200 ms/time

V1
Request
Spot Request
{
  "SendTopicAction": {
    "Action": "1",
    "FilterValue": "DeepCoin_BTC/USDT_0.1",// 0.1 indicates the number of decimal places
    "LocalNo": 6,
    "ResumeNo": -1,
    "TopicID": "25"
  }
}

Contracts Request
{
  "SendTopicAction": {
    "Action": "1",
    "FilterValue": "DeepCoin_BTCUSDT_0.1",// 0.1 indicates the number of decimal places
    "LocalNo": 6,
    "ResumeNo": -1,
    "TopicID": "25"
  }
}

Response Parameters
Field Name	Type	Example	Description
InstrumentID	string	"BTCUSDT"	Instrument ID
Direction	string	"1"	Direction
Price	int	115970.6	Price
Volume	int	6432	Volume
Response Example
{
  "a": "PMO",
  "t": "i",
  "r": [
    {
      "d": {
              "I": "BTCUSDT",
              "D": "0",
              "P": 115970.7,
              "V": 13285.0
          }
      },
      {
          "d": {
              "I": "BTCUSDT",
              "D": "0",
              "P": 115970.6,
              "V": 1272.0
          }
      }
   ]
}

V2
Request
Spot Request
{
  "Action": "1",
  "Symbol": "BTC/USDT_0.1",// 0.1 indicates the number of decimal places
  "LocalNo": 6,
  "ResumeNo": -1,
  "Topic": "book25"
}

Contracts Request
{
  "Action": "1",
  "Symbol": "BTCUSDT_0.1",// 0.1 indicates the number of decimal places
  "LocalNo": 6,
  "ResumeNo": -1,
  "Topic": "book25"
}

Response Parameters
Field Name	Type	Example	Description
i	string	"BTCUSDT"	Instrument ID
a	array		asks
b	array		bids
Response Example
{
  "a": "PMO",
  "t": "i",
  "i": "BTCUSDT_0.1",
  "d": [
    {
      "a": [
        ["8476.98","415"],// Asks price, asks quantity
        ["8477","7"]
      ],
      "b": [
        ["8476.98","415"],// Bids price, bids quantity
        ["8477","7"]
      ]
    }
  ]
}

iquidation Order Subscription
Subscribe to Liquidation Orders
V1
Request Example
{
  "SendTopicAction": {
    "Action": "1",
    "LocalNo": 0,
    "TopicID": "30"
  }
}

Field	Description
Action	Subscription operation. 1 = subscribe, 0 = unsubscribe.
LocalNo	Client-defined identifier. Unique values allow multiple, independent topics.
TopicID	Topic identifier. 30 = Liquidation order topic.
Response Parameters
Field	Description
a	Message type, PFO stands for liquidation order.
c	Channel indicator.
r	Payload array containing table (t) and data (d).
t	Payload table name.
I	Symbol (e.g., BTCUSDT).
D	Direction: 0 = buy, 1 = sell.
P	Liquidation price.
V	Filled volume.
T	Deal timestamp (Unix seconds).
Response Example
{
  "a": "PFO",
  "c": "b",
  "r": [
    {
      "t": "Order",
      "d": {
        "I": "BTCUSDT",
        "D": "1",
        "P": 86339.9,
        "V": 11.0,
        "T": 1765866172
      }
    }
  ]
}

V2
Request Example
{
  "Action": "1",
  "LocalNo": 0,
  "Topic": "liquidationOrder"
}

Field	Description
Action	Subscription operation. 1 = subscribe, 0 = unsubscribe.
LocalNo	Client-defined identifier. Unique values allow multiple, independent topics.
Topic	Topic identifier. liquidationOrder = Liquidation order topic.
Response Parameters
Field	Description
a	Message type, PFO stands for liquidation order.
c	Channel indicator.
r	Payload array containing table (t) and data (d).
t	Payload table name.
I	Symbol (e.g., BTCUSDT).
D	Direction: 0 = buy, 1 = sell.
P	Liquidation price.
V	Filled volume.
T	Deal timestamp (Unix seconds).
Response Example
{
  "a": "PFO",
  "c": "b",
  "d": [
    {
      "I": "BTCUSDT",
      "D": "1",
      "P": 86339.9,
      "V": 11.0,
      "T": 1765866172
    }
  ]
}









Assets Deposit
Assets Deposit
Get user's deposit records

Request frequency limit: 1/1s

Request URL
GET /deepcoin/asset/deposit-list

Request Parameters
Field Name	Required	Type	Description
coin	false	string	Coin
txHash	false	string	Transaction hash
startTime	false	integer	Query start time
endTime	false	integer	Query end time
page	false	integer	Page number
Default: 1
size	false	integer	Items per page
Default: 10
Response Parameters
Field Name	Type	Description
data	array	
>createTime	string	On-chain confirmation time
>txHash	string	Transaction hash
>chainName	string	Chain name
>amount	string	Amount
>coin	string	Coin
>status	string	Status
confirming: Confirming
succeed: Success
count	integer	Total count
page	integer	Current page number
size	integer	Current items per page
Response Example
{
  "code": "0",
  "msg": "",
  "data": {
    "data": [
      {
        "createTime": 1720764939,
        "txHash": "be6a16eb864f4e7d98ed6bbd96405c558099b7a60834b3537901b275b06babff",
        "chainName": "TRC20",
        "amount": "1000000",
        "coin": "USDT",
        "status": "succeed"
      },
      {
        "createTime": 1720764939,
        "txHash": "be6a16eb864f4e7d98ed6bbd96405c558099b7a60834b3537901b275b06babff",
        "chainName": "TRC20",
        "amount": "1000000",
        "coin": "USDT",
        "status": "confirming"
      }
    ],
    "count": 2,
    "page": 1,
    "size": 10
  }
}


Assets Withdraw
Assets Withdraw
Get user's withdraw records

Request frequency limit: 1/1s

Request URL
GET /deepcoin/asset/withdraw-list

Request Parameters
Field Name	Required	Type	Description
coin	false	string	Coin
txHash	false	string	Transaction hash
startTime	false	integer	Query start time
endTime	false	integer	Query end time
page	false	integer	Page number
Default: 1
size	false	integer	Items per page
Default: 10
Response Parameters
Field Name	Type	Description
data	array	
>createTime	string	Withdrawal application time
>txHash	string	Transaction hash
>address	string	Withdrawal address
>amount	string	Amount
>coin	string	Coin
>status	string	Withdrawal status
auditing: Under review
confirming: Confirming
rejected: Platform review rejected
succeed: Success
count	integer	Total count
page	integer	Current page number
size	integer	Current items per page
Response Example
{
  "code": "0",
  "msg": "",
  "data": {
    "data": [
      {
        "createTime": 1719459854,
	"txHash": "xxxxxxxxx",
        "address": "",
        "amount": "100",
        "coin": "USDT",
        "status": "auditing"
      }
    ],
    "count": 4,
    "page": 1,
    "size": 1
  }
}

Recharge Chain List
Recharge Chain List
Get list of supported chains for deposits

Request frequency limit: 1/1s

Request URL
GET /deepcoin/asset/recharge-chain-list

Request Parameters
Field Name	Required	Type	Description
currency_id	true	string	Currency ID
lang	true	string	Language code (e.g., "zh", "en")
Request Example
GET /deepcoin/asset/recharge-chain-list?currency_id=USDT&lang=zh

Response Parameters
Field Name	Type	Description
list	array	List of supported chains
>chain	string	Chain name
>state	integer	Chain state (1: enabled, 0: disabled)
>remind	string	Reminder information
>inNotice	string	Notice information
>actLogo	string	Chain logo URL
>address	string	Deposit address
>hasMemo	boolean	Whether memo is required
>memo	string	Memo information for the chain
>estimatedTime	integer	Estimated confirmation time (minutes)
>fastConfig	object	Fast confirmation configuration
>>fastLimitNum	integer	Fast confirmation limit
>>fastBlock	integer	Fast confirmation blocks
>>realBlock	integer	Real confirmation blocks
addressHideReason	string	Reason for hiding address (if applicable)
Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "list": [
            {
                "chain": "TRC20",
                "state": 1,
                "remind": "",
                "inNotice": "",
                "actLogo": "",
                "address": "TXYZabc123...",
                "hasMemo": false,
                "memo": "",
                "estimatedTime": 10,
                "fastConfig": {
                    "fastLimitNum": 100,
                    "fastBlock": 6,
                    "realBlock": 12
                }
            },
            {
                "chain": "ERC20",
                "state": 1,
                "remind": "",
                "inNotice": "",
                "actLogo": "",
                "address": "0x123abc...",
                "hasMemo": false,
                "memo": "",
                "estimatedTime": 30,
                "fastConfig": {
                    "fastLimitNum": 50,
                    "fastBlock": 12,
                    "realBlock": 24
                }
            }
        ],
        "addressHideReason": ""
    }
}

Notes
This endpoint returns all supported blockchain networks for a specific currency
The memo field contains important information for certain chains (like EOS, XRP)
Check canDeposit and canWithdraw flags before allowing operations
Different chains may have different fees and limits


Asset Transfer
Asset Transfer
Transfer funds between different account types

Request frequency limit: 1/1s

Request URL
POST /deepcoin/asset/transfer

Request Parameters
Field Name	Required	Type	Description
currency_id	true	string	Currency ID
amount	true	string	Transfer amount
from_id	true	integer	Source account ID
1: Spot account
2: Wallet account
3: Rebate account
5: Inverse futures account
7: USDT futures account
10: Demo account
to_id	true	integer	Destination account ID
1: Spot account
2: Wallet account
3: Rebate account
5: Inverse futures account
7: USDT futures account
10: Demo account
uid	true	integer	User ID
Request Example
{
    "currency_id": "USDT",
    "amount": "100.00",
    "from_id": 7,
    "to_id": 1,
    "uid": 36020176
}

Response Parameters
Field Name	Type	Description
retCode	integer	Return code (0: success)
retMsg	string	Return message
retData	object	Return data
Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "retCode": 0,
        "retMsg": "",
        "retData": {}
    }
}

Error Response Example
{
    "code": "0",
    "msg": "",
    "data": {
        "retCode": 100029,
        "retMsg": "Failed.",
        "retData": {}
    }
}

Account Type Reference
Account ID	Account Type	Description
1	Spot account	For spot trading
2	Wallet account	Main wallet
3	Rebate account	Commission rebate account
5	Inverse futures	Coin-margined futures
7	USDT futures	USDT-margined futures
10	Demo account	Demo trading account
Notes
The user ID must match the authenticated API key owner
Ensure sufficient balance in the source account before transfer
Transfers between the same account type are not allowed
Some account types may have restrictions based on user verification level