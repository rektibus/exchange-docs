Access Guide
Access Guide
Python DEMO
Golang DEMO
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






DeepCoinMarket
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



Get Trades
Retrieve the recent transactions for a specific instrument.

Rate Limit: 1 request per 1 second

Rate Limit Rule: IP

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





Handicap History Trades
Query historical trade data for a symbol within a time range.

Rate Limit: 1 request per 1 second

Rate Limit Rule: IP

Request URL
GET /deepcoin/market/handicap-trade

Request Parameters
Parameter	Type	Required	Description	Example
symbol	String	Yes	Trading symbol	BTCUSDT
stime	integer	Yes	Start timestamp (seconds)	1700000000
etime	integer	No	End timestamp (seconds)	1800000000
limit	integer	Yes	Result size, between 1 and 2000 (default: 60)	60
Response Parameters
Parameter	Type	Description	Example
etime	integer	Response end timestamp	1700003600
data	String	Data payload (string)	...
errmsg	String	Error message (if any)	
Response Example
{
  "code": "0",
  "msg": "",
  "data": {
    "etime": 1766759271,
    "data": [
      {
        "trade_id": "1000299140908139",
        "direction": "1",
        "coin_market": "BTCUSDT",
        "price": 88948.8,
        "platform": "deepcoin",
        "timestamp": 1766759271
      }
    ],
    "errmsg": ""
  }
}





Handicap History Orderbook
Query historical orderbook data for a symbol within a time range.

Rate Limit: 1 request per 1 second

Rate Limit Rule: IP

Request URL
GET /deepcoin/market/handicap-orderbook

Request Parameters
Parameter	Type	Required	Description	Example
symbol	String	Yes	Trading symbol	BTCUSDT
stime	integer	Yes	Start timestamp (seconds)	1700000000
etime	integer	No	End timestamp (seconds)	1800000000
limit	integer	Yes	Result size, between 1 and 2000 (default: 60)	60
Response Parameters
Parameter	Type	Description	Example
etime	integer	Response end timestamp	1700003600
data	String	Data payload (string)	...
errmsg	String	Error message (if any)	
Response Example
{
  "code": "0",
  "msg": "",
  "data": {
    "etime": 1766758170,
    "data": [
      {
        "platform": "deepcoin",
        "coin_market": "BTCUSDT",
        "timestamp": 1766758170,
        "buy_order_list": [
          [104600, 43],
          [99999.9, 3],
          [98000, 2],
          [96000, 102],
          [95000, 207]
        ],
        "ask_order_list": [
          [61800, 56],
          [62000, 92],
          [63000, 1252],
          [64000, 90],
          [64588, 1310]
        ]
      }
    ],
    "errmsg": ""
  }
}







Public WebSocket
Mainnet
Contracts: wss://stream.deepcoin.com/streamlet/trade/public/swap?platform=api

Spot: wss://stream.deepcoin.com/streamlet/trade/public/spot?platform=api

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





The Latest Market Data
The-latest-market-data
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












Last Transactions
Last-transactions
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






K-Lines (only support 1 minute)
K-Lines currently only support 1 minute
ResumeNo： -1 means the latest record,-30 means the latest 30 historical records.

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






25-Level Incremental Market Data
25-level-incremental-market-data
Notification push frequency: 200 ms/time

Request
Spot Request
{
  "SendTopicAction": {
    "Action": "1",
    "FilterValue": "DeepCoin_BTC/USDT_0.1",
    "LocalNo": 6,
    "ResumeNo": -1,
    "TopicID": "25"
  }
}

Contracts Request
{
  "SendTopicAction": {
    "Action": "1",
    "FilterValue": "DeepCoin_BTCUSDT_0.1",
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





