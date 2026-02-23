API Introduction
Welcome to use DigiFinex ApiKey.

This is DigiFinex official API document, and will be continue updating, please follow us to get latest news.

You can switch different language by clicking language button in the top right.

Market Making Program
It is very welcome for market maker who has good market making strategy and large trading volume. Market maker who is willing to cooperate with Digifinex will get support for commission discount on trading fees(rebate), API limit rate, server resources and so on.

If you are willing to be DigiFinex market maker, you can send your email to: vip@digifinex.com

For the (spot / leverage) market maker application, provide below details:

1.UID (not linked to any rebate program in any Market Datas).

2.Screenshot of trading volume in other transaction platform (such as trading volume within 30 days, or VIP status).

3.A brief description of your market-making strategy.

Contact us
If you have any other questions on API, you can contact us by below ways:

Official Telegram: https://t.me/digifinex_api

E-mail: cooperation@digifinex.com

Quick Start
Digifinex API Trading Rules
In order to provide a better API trading environment, avoid malicious manipulation and disruption of the market integrity, DigiFinex hereby publish risk-control quantitative indicators and anti-manipulation rules.

Quantitative Indicators
The indicators record and calculated by all orders on certain trading pair within one time period.

Filling Ratio（FR） FR = Total number of Filled Orders / Total Number of Orders
Filling Weight（FW） FW = Totall Filled Amount / Total Order Amount
Cancellation Ratio（CR） CR = Total Number of Fully-Cancelled Orders / Total Number of Orders In which the Fully-Cancelled Orders indicate orders with zero-filled amount and cancelled within 5 seconds after order placement.
Trigger Conditions
Indicator	Trigger Value	Trigger Condition	Calculating Cycle
Filling Ratio（FR）	<0.01	Number of Orders > 99	10 minutes
Filling Weight（FW）	<0.01	Number of Orders > 49	10 minutes
Cancellation Ratio（CR）	>0.95	Number of Orders > 99	10 minutes
Risk Control and API Ban
API Users violated any anti-manipulation rules will be banned for API trading for 30 minutes. The time will extend to 24 hours after third ban within 3 hours. During that time, banned user cannot place new order through API or creat new API key, order placement and cancellation will not be affected whatsoever.

Trading Interface List
Interface List
Permission Type	Content Type	Context	Request Type	Description	Authorization
Reading	Common	/ping	GET	Server ping	False
Reading	Common	/time	GET	Server timestamp	False
Reading	Market Data	/markets	GET	All the market description	False
Reading	Market Data	/ticker	GET	ticker price	False
Reading	Market Data	/order_book	GET	Get orderbook	False
Reading	Market Data	/trades	GET	Get recent trades	False
Reading	Market Data	/kline	GET	Get candles data	False
Reading	Market Data	/spot/symbols	GET	Spot trading pair symbol	False
Reading	Market Data	/margin/currencies	GET	Currencies which support margin trading	False
Reading	Market Data	/margin/symbols	GET	Margin trading pair symbol	False
Reading	Market interface	/trades/symbols	GET	Whether is API trading enabled for the trading pair	false
Trading	Account	/{market}/financelog	GET	Spot, margin, OTC financial logs	True
Trading	Account	/{market}/order	GET	Get order status	True
Trading	Account	​/{market}​/order​/detail	GET	Get order trades details	True
Trading	Account	/{market}/order/current	GET	Current active orders	True
Trading	Account	/{market}/order/history	GET	Get all orders (including history orders)	True
Trading	Account	/{market}/mytrades	GET	Customer's trades	True
Trading	Account	/spot/assets	GET	Spot account assets	True
Trading	Account	​/margin​/positions	GET	Margin positions	True
Trading	Account	​/margin​/assets	GET	Margin assets	True
Trading	Account	/{market}/order/new	POST	Create new order	True
Trading	Account	​/{market}​/order​/batch_new	POST	Create multiple order	True
Trading	Account	/{market}/order/cancel	POST	Cancel order	True
Trading	Account	/transfer	POST	Transfer assets among accounts	True
Trading	Account	/margin/position/close	POST	Close positions	True
Address
Address	Applicable Sites	Applicable Functions	Applicable Trading Pairs
https://openapi.digifinex.com/v3	digifinex	API	digifinex Trading Pairs
Signature Authentication & Verification
You could create API Key in "Account - API setting".

API Key consists of the following two parts.

"Access Key", the Key used to visit API.

"Secret Key", the Key used to do Signature authentication and verification (visible during application period).

Both Access Key and Secret Key are closely related with account security, please do not disclose them to others for any reasons anytime.

API Endpoints Description:
The field contentType in request header should be: application/x-www-form-urlencoded

The parameters can be passed in query string or request body, priority in query string if passed in both.

All endpoints are classified as two ranks:

public Public endpoints, no signature or timestamp needed

private Private endpoints, need signature and timestamp

All sign required endpoints must be requested with header:

ACCESS-KEY User's API-KEY

ACCESS-SIGN Signature

ACCESS-TIMESTAMP Timestamp in seconds

The request will be considered invalid if the timestamp passed to server was behind more than 5 seconds (the time window can be customized with ACCESS-RECV-WINDOW parameter in the request header). Also, any request with timestamp ahead of server more than 1 second would be considered invalid.

For all the request will cosume server resources, there is a weight for every endpoint base on load balance considerations. Sum of weights for any [IP|API-KEY|User] must not exceed 1200, or the [IP|API-KEY|User] will be banned for 2 minutes for the first 3 times within 24 hours, 10 minutes if exceed more than 3 times, 30 times if exceed more than 6 times.

Signature Algorithm
The HMAC SHA256 is used for signature.

The API-Secret of specific API-KEY will be the secret key of HMAC SHA256, other parameters as the HMAC SHA256 encrypting object, the outcome string is the signature.

The signature is not case sensitive.

When query string and request body are both passed with parameters, the input of HMAC SHA256 must be composed with query string and request body concat with '&' and the query string must be in front.

The signature of specific ACCESS-KEY must be passed in the request header by ACCESS-SIGN parameter.

Authentication
Overview
The API request may be tampered during internet, therefore all private API must be signed by your API Key (Secrete Key).

Each API Key has permission property, please check the API permission, and make sure your API key has proper permission.

Signature Method：

The signature may be different if the request text is different, therefore the request should be normalized before signing. Below signing steps take the Create New Order as an example:

Create new order Parameters.
{'symbol': 'trx_usdt', 'price': 0.01, 'amount': 1, 'type': 'buy'}

The parameters are URL encoded, and ordered based on ASCII
symbol=trx_usdt&price=0.01&amount=1&type=buy

Use the pre-signed text and your Secret Key to generate a signature（Example: Secret:01234567890123456789abcd）:
7e2d0636cab21fd41c828b8c6ce8f77e643febecdeaeab0771c01dc4d7dbef38

Put ACCESS-KEY，ACCESS-TIMESTAMP，ACCESS-SIGN（Get last step） into header.
{'ACCESS-KEY': '0123456789abcd', 'ACCESS-TIMESTAMP': '1589872188', 'ACCESS-SIGN': '7e2d0636cab21fd41c828b8c6ce8f77e643febecdeaeab0771c01dc4d7dbef38'}

Request Create new order url.
Method: Post

url: https://openapi.digifinex.com/v3/spot/order/new

headers: {'ACCESS-KEY': '0123456789abcd', 'ACCESS-TIMESTAMP': '1589872188', 'ACCESS-SIGN': '7e2d0636cab21fd41c828b8c6ce8f77e643febecdeaeab0771c01dc4d7dbef38'}

body: {'symbol': 'trx_usdt', 'price': 0.01, 'amount': 1, 'type': 'buy'}

Error codes
code	Description
0	Success
10001	Wrong request method, please check it's a GET or POST request
10002	Invalid ApiKey
10003	Sign doesn't match
10004	Illegal request parameters
10005	Request frequency exceeds the limit
10006	Unauthorized to execute this request
10007	IP address Unauthorized
10008	Timestamp for this request is invalid
10009	Unexist endpoint or misses ACCESS-KEY, please check endpoint URL
10011	ApiKey expired. Please go to client side to re-create an ApiKey.
20002	Trade of this trading pair is suspended
20007	Price precision error
20008	Amount precision error
20009	Amount is less than the minimum requirement
20010	Cash Amount is less than the minimum requirement
20011	Insufficient balance
20012	Invalid trade type (valid value: buy/sell)
20013	No order info found
20014	Invalid date (Valid format: 2018-07-25)
20015	Date exceeds the limit
20018	Your have been banned for API trading by the system
20019	Wrong trading pair symbol, correct format:"base_quote", e.g. "btc_usdt"
20020	You have violated the API trading rules and temporarily banned for trading. At present, we have certain restrictions on the user's transaction rate and withdrawal rate.
20021	Invalid currency
20022	The ending timestamp must be larger than the starting timestamp
20023	Invalid transfer type
20024	Invalid amount
20025	This currency is not transferable at the moment
20026	Transfer amount exceed your balance
20027	Abnormal account status
20028	Blacklist for transfer
20029	Transfer amount exceed your daily limit
20030	You have no position on this trading pair
20032	Withdrawal limited
20033	Wrong Withdrawal ID
20034	Withdrawal service of this crypto has been closed
20035	Withdrawal limit
20036	Withdrawal cancellation failed
20037	The withdrawal address, Tag or chain type is not included in the withdrawal management list
20038	The withdrawal address is not on the white list
20039	Can't be canceled in current status
20040	Withdraw too frequently; limitation: 3 times a minute, 100 times a day
20041	Beyond the daily withdrawal limit
20042	Current trading pair does not support API trading
50000	Exception error
Common
Server ping
HTTP Request
GET https://openapi.digifinex.com/v3/ping
Request Parameters
No parameter is available for this endpoint.

Response:


{
    "msg": "pong",
    "code": 0
}

Response Content
Field	Mandatory	Request Type	Description
msg	true	string	Response
code	true	int	Status
Server timestamp
HTTP Request
GET https://openapi.digifinex.com/v3/time
Request Parameters
No parameter is available for this endpoint.

Response:


{
    "server_time": 1589873762,
    "code": 0
}

Response Content
Field	Mandatory	Request Type	Description
server_time	true	int	Server timestamp
code	true	int	Status
Market Data
All the market description
HTTP Request
GET https://openapi.digifinex.com/v3/markets
Request Parameters
No parameter is available for this endpoint.

Response:


{
    "data": [{
        "volume_precision": 4,
        "price_precision": 2,
        "market": "btc_usdt",
        "min_amount": 2,
        "min_volume": 0.0001
    }],
    "date": 1589873858,
    "code": 0
}

Response Content
Field	Mandatory	Request Type	Description
data	true	object	Trading Pair Information
volume_precision	true	int	Volume Precision
price_precision	true	int	Price Precision
market	true	string	Symbol Name
min_amount	true	float	Minimum Trading Amount
min_volume	true	float	Minimum Trading Volume
date	true	int	Timestamp
code	true	int	Status
ticker price
HTTP Request
GET https://openapi.digifinex.com/v3/ticker
Request Parameters
Field	Request Type	Mandatory	Description
symbol	string	false	"btc_usdt"
Response:


{
    "ticker": [{
        "vol": 40717.4461,
        "change": -1.91,
        "base_vol": 392447999.65374,
        "sell": 9592.23,
        "last": 9592.22,
        "symbol": "btc_usdt",
        "low": 9476.24,
        "buy": 9592.03,
        "high": 9793.87
    }],
    "date": 1589874294,
    "code": 0
}

Response Content
Field	Mandatory	Request Type	Description
ticker	true	object	Trading Pair Information
vol	true	float	24h Volume
change	true	float	24h Change
base_vol	true	float	24h Amount
sell	true	float	Ask1 Price
last	true	float	Last Price
symbol	true	string	Symbol Name
low	true	float	24h Low Price
buy	true	float	Bid1 Price
high	true	float	24h High Price
date	true	int	Timestamp
code	true	int	Status
Get orderbook
HTTP Request
GET https://openapi.digifinex.com/v3/order_book
Request Parameters
Field	Request Type	Mandatory	Description
symbol	string	true	"btc_usdt"
limit	int	false	Limit of depth, default 10, maximum 150
Response:


{
    "bids": [
        [9559.45, 1.3766],
        [9559.04, 0.0127],
        ..
    ],
    "asks": [
        [9563.45, 0.6312],
        [9563.34, 0.0087],
        ..
    ],
    "date": 1589874953,
    "code": 0
}

Response Content
Field	Mandatory	Request Type	Description
bids	true	object	Bids [price, size]
asks	true	object	Asks [price, size]
date	true	int	Timestamp
code	true	int	Status
Get recent trades
HTTP Request
GET https://openapi.digifinex.com/v3/trades
Request Parameters
Field	Request Type	Mandatory	Description
symbol	string	true	"btc_usdt"
limit	int	false	Limit of trades returned, default 100, maximum 500
Response:


{
    "data": [{
        "date": 1589875415,
        "id": 2989995478,
        "amount": 0.001,
        "type": "buy",
        "price": 9661.05
    }, {
        "date": 1589875415,
        "id": 2989995473,
        "amount": 0.0005,
        "type": "buy",
        "price": 9659.99
    },
    ...
    ],
    "date": 1589875415,
    "code": 0
}

Response Content
Field	Mandatory	Request Type	Description
data	true	object	Customer's trades
date	true	int	Timestamp
id	true	int	Trading ID
amount	true	float	Volume
type	true	str	Trading Type
price	true	float	Trading Price
code	true	int	Status
Get candles data
HTTP Request
GET https://openapi.digifinex.com/v3/kline
Request Parameters
Field	Request Type	Mandatory	Description
symbol	string	true	"btc_usdt"
period	str	true	Candle timeframe type: 1,5,15,30,60,240,720,1D,1W
start_time	int	false	Candle starting time in timestamp, default 200 period befor end_time
end_time	int	false	Candle ending time in timestamp, default current timestamp
Get candles data by symbol, up to 500 at one time.

Response:


{
    "data": [
        [1589426100, 621.4565, 9342.7, 9349.99, 9305.86, 9307.96],
        [1589427000, 378.1678, 9333.71, 9344.25, 9318.26, 9342.23],
        ...,
    ],
    "code": 0
}

Response Content
Field	Mandatory	Request Type	Description
data	true	object	Candles Data[timestamp,vol,close,high,low,open],last one is most recent data
code	true	int	Status
Spot trading pair symbol
HTTP Request
GET https://openapi.digifinex.com/v3/spot/symbols
Request Parameters
No parameter is available for this endpoint.

Response:


{
  "code": 0,
  "symbol_list": [
    {
      "status": "TRADING",
      "symbol": "LTC_USDT",
      "quote_asset": "USDT",
      "base_asset": "LTC",
      "amount_precision": 4,
      "price_precision": 2,
      "minimum_amount": 0.001,
      "minimum_value": 2,
      "zone": "MAIN",
      "order_types": [
        "LIMIT",
        "MARKET"
      ]
    }
  ]
}

Response Content
Field	Mandatory	Request Type	Description
symbol_list	true	object	Trading Pair Information
order_types	true	list	Trading Type
quote_asset	true	str	Quote Asset
minimum_value	true	int	Minimum Value
amount_precision	true	int	Volume Precision
status	true	str	Status
minimum_amount	true	float	Minmum Amount
symbol	true	str	Symbol Name
zone	true	str	Zone
base_asset	true	str	Base Asset
price_precision	true	int	Price Precision
code	true	int	Status
Currencies which support margin trading
HTTP Request
GET https://openapi.digifinex.com/v3/margin/currencies
Request Parameters
No parameter is available for this endpoint.

Response:


{
  "code": 0,
  "funding_time": "GMT+8 10:00:00",
  "currencys": [
    "BTC",
    "USDT",
    "ETH",
    "XRP"
  ],
  "margin_fees": [
    {
      "currency_mark": "USDT",
      "level": 2,
      "range": "[8-14]",
      "loan_fees": 0.001
    }
  ]
}

Response Content
Field	Mandatory	Request Type	Description
currencys	true	list	Currencys List
margin_fees	true	object	Margin Fees
currency_mark	true	str	Currency
loan_fees	true	float	Loan Fees
range	true	str	Range
level	true	int	Level
code	true	int	Status
funding_time	true	str	Funding Time
Margin trading pair symbol
HTTP Request
GET https://openapi.digifinex.com/v3/margin/symbols
Request Parameters
No parameter is available for this endpoint.

Response:


{
  "code": 0,
  "symbol_list": [
    {
      "status": "TRADING",
      "symbol": "LTC_USDT",
      "quote_asset": "USDT",
      "base_asset": "LTC",
      "amount_precision": 4,
      "price_precision": 2,
      "minimum_amount": 0.001,
      "minimum_value": 2,
      "zone": "MAIN",
      "liquidation_rate": 0.3,
      "order_types": [
        "LIMIT",
        "MARKET"
      ]
    }
  ]
}

Response Content
Field	Mandatory	Request Type	Description
symbol_list	true	object	Margin trading pair symbol
order_types	true	list	Trading Type
quote_asset	true	str	Quote Asset
minimum_value	true	int	Minimum Value
amount_precision	true	int	Volume Precision
status	true	str	Status
minimum_amount	true	float	Minmum Amount
liquidation_rate	true	float	Liquidation Rate
symbol	true	str	Symbol Name
zone	true	str	Zone
base_asset	true	str	Base Asset
price_precision	true	int	Price Precision
code	true	int	Status
Whether is API trading enabled for the trading pair
HTTP request
GET https://openapi.digifinex.com/v3/trades/symbols
Request parameters
This interface does not accept any parameters.

Response:


{
  "code": 0,
  "symbol_list": [
    {
      "status": "TRADING",
      "symbol": "LTC_USDT",
      "quote_asset": "USDT",
      "base_asset": "LTC",
      "amount_precision": 4,
      "price_precision": 2,
      "minimum_amount": 0.001,
      "minimum_value": 2,
      "zone": "MAIN",
      "is_allow": 1,
      "order_types": [
        "LIMIT",
        "MARKET"
      ]
    }
  ]
}

Return parameters
Parameters	Required	Type	Description
symbol_list	true	object	symbol list
order_types	true	list	order types
quote_asset	true	str	quote asset
minimum_value	true	int	minimum value
amount_precision	true	int	amount precision
status	true	str	status
minimum_amount	true	float	minimum_amount
symbol	true	str	symbol
zone	true	str	zone
base_asset	true	str	base asset
price_precision	true	int	price precision
code	true	int	status
is_allow	true	int	1 true 0 false
Get currency deposit and withdrawal information
Search for crypto information, including deposit and withrawal service, withdrawal fees and minimum deposit amount etc.

HTTP Request
GET https://openapi.digifinex.com/v3/currencies
Request Parameters
Name of parameter	If necessary	Type	Description	Default	Value range
currency	false	string	cryptocurrency	By default, the default value is null and returns to all crptos	btc, ltc, bch, eth, etc ...
Response:

{
  "code": 200,
  "data":
    [
      {
        "currency": "xrp",
        "chain":"",
        "min_deposit_amount": 0.01,
        "min_withdraw_amount": 0.02,
        "deposit_status":1,
        "withdraw_status":1,
        "withdraw_fee_currency":"eth",
        "min_withdraw_fee":0.006,
        "withdraw_fee_rate":0.02,
      },
      ...
    ]
}
Response Content
Name of parameter	If necessary	Data type	Description	Value range
currency	true	string	currency	
chain	true	string	chain name	The chain name is empty by default, and USDT has two chains: ERC20 and OMNI
min_deposit_amount	true	float	minimum deposit	
min_withdraw_amount	true	float	minimum withdrawal	
deposit_status	true	int	deposit status: 1 is on, 0 is off	
withdraw_status	true	int	withdrawal status: 1 is on, 0 is off	
withdraw_fee_currency	true	string	The currency of withdrawal fee	
min_withdraw_fee	true	float	Minimum withdrawal fee	
withdraw_fee_rate	true	float	Percentage of withdrawal fee. Note: if the actual fee is less than the minimum fee, it will be charged according to minimum fee; Otherwise, it will be charged according to the actual fee.	
Status code
Status code	error message	Error scenario description
200	success	success
Account
Spot account assets
HTTP Request
GET https://openapi.digifinex.com/v3/spot/assets
Request Parameters
No parameter is available for this endpoint.

Response:


{
  "code": 0,
  "list": [
    {
      "currency": "BTC",
      "free": 4723846.89208129,
      "total": 0
    }
  ]
}

Response Content
Field	Mandatory	Request Type	Description
list	true	object	Account List
currency	true	string	Currency Name
free	true	float	Free
total	true	float	Total
code	true	int	Status
Margin assets
HTTP Request
GET https://openapi.digifinex.com/v3/margin​/assets
Request Parameters
No parameter is available for this endpoint.

Response:


{
  "code": 0,
  "total": 0,
  "free": 0,
  "unrealized_pnl": 0,
  "list": [
    {
      "currency": "BTC",
      "valuation_rate": 1,
      "free": 4723846.89208129,
      "total": 0
    }
  ]
}

Response Content
Field	Mandatory	Request Type	Description
list	true	object	Account List
currency	true	string	Currency Name
free	true	float	Free
total	true	float	Total
code	true	int	Status
valuation_rate	true	float	valuation rate
Spot, margin, OTC financial logs
HTTP Request
GET https://openapi.digifinex.com/v3/{market}/financelog
Request Parameters
market：spot, margin

Field	Request Type	Mandatory	Description
market	str	true	"spot","margin"
currency_mark	str	false	
start_time	int	false	
end_time	int	false	
limit	int	false	Default 100, maximum 1000
Response:


{
    "data": {
        "finance": [
            {
                "time": 1743936061,
                "num": 0.0001,
                "balance": 3.471289738,
                "currency_mark": "USDT",
                "type": 119
            },
        ],
        "total": "196"
    },
    "code": 0
}  
Response Content
Field	Mandatory	Request Type	Description
time | true | int | time |
num | true | float | num | balance | true | float | balance | currency_mark | true | str | currency mark | type | true | int | type | total | true | str | Total |
code | true | int | Status |

Get order status
HTTP Request
GET https://openapi.digifinex.com/v3/{market}/order
Request Parameters
market：spot, margin

Field	Request Type	Mandatory	Description
market	str	true	"spot","margin"
order_id	str	true	Order ID list, separated by commas, limit of 20
Response:


{
  "code": 0,
  "data": [
    {
      "symbol": "BTC_USDT",
      "order_id": "dd3164b333a4afa9d5730bb87f6db8b3",
      "created_date": 1562303547,
      "finished_date": 0,
      "price": 0.1,
      "amount": 1,
      "cash_amount": 1,
      "executed_amount": 0,
      "avg_price": 0,
      "status": 1,
      "type": "buy",
      "kind": "margin"
    }
  ]
}

Response Content
Field	Mandatory	Request Type	Description
data	true	object	Order Status List
symbol	true	string	Symbol Name
order_id	true	string	Order ID
created_date	true	int	Created Time
finished_date	true	int	Finished Time
price	true	float	Price
amount	true	float	Volume
cash_amount	true	float	Cash amount of orders, 0 for none order
executed_amount	true	float	Amount been executed
avg_price	true	float	Average price of amount been executed
status	true	int	Order status, 0 for none executed, 1 for partially executed, 2 for fully executed, 3 for cancelled with none executed, 4 for cancelled with partially executed
type	true	string	buy for limit buy order, sell for limit sell order, buy_market for market buy order, sell_market for market sell order
kind	true	string	spot, margin
code	true	int	Status
Get order trades details
HTTP Request
GET https://openapi.digifinex.com/v3/{market}​/order​/detail
Request Parameters
market：spot, margin

Field	Request Type	Mandatory	Description
market	str	true	"spot","margin"
order_id	str	true	Order ID
Response:


{
  "code": 0,
  "data": {
    "symbol": "BTC_USDT",
    "order_id": "dd3164b333a4afa9d5730bb87f6db8b3",
    "created_date": 1562303547,
    "finished_date": 1574665459,
    "price": 6000,
    "amount": 0.58,
    "cash_amount": 0,
    "executed_amount": 0.58,
    "avg_price": 6000,
    "status": 2,
    "type": "buy",
    "kind": "margin",
    "detail": {
      "tid": "63194988",
      "date": 1574665459,
      "executed_amount": 0.58,
      "executed_price": 6000
    }
  }
}

Response Content
Field	Mandatory	Request Type	Description
data	true	object	Order Status List
symbol	true	string	Symbol Name
order_id	true	string	Order ID
created_date	true	int	Created Time
finished_date	true	int	Finished Time
price	true	float	Price
amount	true	float	Volume
cash_amount	true	float	Cash amount of orders, 0 for none order
executed_amount	true	float	Amount been executed
avg_price	true	float	Average price of amount been executed
status	true	int	Order status, 0 for none executed, 1 for partially executed, 2 for fully executed, 3 for cancelled with none executed, 4 for cancelled with partially executed
type	true	string	buy for limit buy order, sell for limit sell order, buy_market for market buy order, sell_market for market sell order
kind	true	string	spot, margin
detail	true	object	Order Detail
tid	true	string	Trading ID
date	true	int	Trading Time
executed_amount	true	float	Trading Volume
executed_price	true	float	Trading Price格
code	true	int	Status
Current active orders
HTTP Request
GET https://openapi.digifinex.com/v3/{market}/order/current
Request Parameters
market：spot, margin

Field	Request Type	Mandatory	Description
market	str	true	"spot","margin"
symbol	str	false	Symbol Name
Response:


{
  "code": 0,
  "data": [
    {
      "symbol": "BTC_USDT",
      "order_id": "dd3164b333a4afa9d5730bb87f6db8b3",
      "created_date": 1562303547,
      "finished_date": 0,
      "price": 0.1,
      "amount": 1,
      "cash_amount": 1,
      "executed_amount": 0,
      "avg_price": 0,
      "status": 1,
      "type": "buy",
      "kind": "margin"
    }
  ]
}

Response Content
Field	Mandatory	Request Type	Description
data	true	object	Current Active Orders List
symbol	true	string	Symbol Name
order_id	true	string	Order ID
created_date	true	int	Created Time
finished_date	true	int	Finished Time
price	true	float	Price
amount	true	float	Volume
cash_amount	true	float	Cash amount of orders, 0 for none order
executed_amount	true	float	Amount been executed
avg_price	true	float	Average price of amount been executed
status	true	int	Order status, 0 for none executed, 1 for partially executed, 2 for fully executed, 3 for cancelled with none executed, 4 for cancelled with partially executed
type	true	string	buy for limit buy order, sell for limit sell order, buy_market for market buy order, sell_market for market sell order
kind	true	string	spot, margin
code	true	int	Status
Get all orders (including history orders)
HTTP Request
GET https://openapi.digifinex.com/v3/{market}/order/history
Request Parameters
market：spot, margin

Field	Request Type	Mandatory	Description
market	str	true	"spot","margin"
symbol	str	false	Symbol Name
limit	int	false	Default 10, maximum 100
start_time	int	false	Starting time, default 3 days before now, maximum 30 days
end_time	int	false	Ending time, default current timestamp
Response:


{
  "code": 0,
  "data": [
    {
      "symbol": "BTC_USDT",
      "order_id": "dd3164b333a4afa9d5730bb87f6db8b3",
      "created_date": 1562303547,
      "finished_date": 0,
      "price": 0.1,
      "amount": 1,
      "cash_amount": 1,
      "executed_amount": 0,
      "avg_price": 0,
      "status": 1,
      "type": "buy",
      "kind": "margin"
    }
  ]
}

Response Content
Field	Mandatory	Request Type	Description
data	true	object	Order History List
symbol	true	string	Symbol Name
order_id	true	string	Order ID
created_date	true	int	Created Time
finished_date	true	int	Finished Time
price	true	float	Price
amount	true	float	Volume
cash_amount	true	float	Cash amount of orders, 0 for none order
executed_amount	true	float	Amount been executed
avg_price	true	float	Average price of amount been executed
status	true	int	Order status, 0 for none executed, 1 for partially executed, 2 for fully executed, 3 for cancelled with none executed, 4 for cancelled with partially executed
type	true	string	buy for limit buy order, sell for limit sell order, buy_market for market buy order, sell_market for market sell order
kind	true	string	spot, margin
code	true	int	Status
Customer's trades
HTTP Request
GET https://openapi.digifinex.com/v3/{market}/mytrades
Request Parameters
market：spot, margin

Field	Request Type	Mandatory	Description
market	str	true	"spot","margin"
symbol	str	false	Symbol Name
limit	int	false	Default 50, maximum 500
start_time	int	false	Starting time, default 3 days before now, maximum 30 days
end_time	int	false	Ending time, default current timestamp
Response:


{
  "code": 0,
  "list": [
    {
      "symbol": "BTC_USDT",
      "order_id": "6707cbdcda0edfaa7f4ab509e4cbf966",
      "id": "28457",
      "price": 0.1,
      "amount": 0,
      "fee": 0.096,
      "fee_currency": "USDT",
      "timestamp": 1499865549,
      "side": "buy",
      "is_maker": true
    }
  ]
}

Response Content
Field	Mandatory	Request Type	Description
list	true	object	Customer's trades List
symbol	true	string	Symbol Name
order_id	true	string	Order ID
id	true	string	Trading ID
price	true	float	Trading Price
amount	true	float	Volume
fee	true	float	Fee
fee_currency	true	string	Fee Currency
timestamp	true	int	Timestamp
side	true	string	Trading Type，buy,sell,buy_market,sell_market
is_maker	true	bool	maker or taker
code	true	int	Status
Margin positions
HTTP Request
GET https://openapi.digifinex.com/v3/margin​/positions
Request Parameters
Field	Request Type	Mandatory	Description
symbol	str	false	Symbol Name
Response:


{
  "code": 0,
  "margin": "20",
  "margin_rate": "1",
  "unrealized_pnl": "55",
  "positions": [
    {
      "symbol": "BTC_USDT",
      "leverage_ratio": "3.0",
      "side": "long",
      "amount": 3.0,
      "entry_price": 40,
      "unrealized_pnl": 55,
      "liquidation_price": 25.999999999999996,
      "liquidation_rate": 0.3
    }
  ]
}

Response Content
Field	Mandatory	Request Type	Description
margin	true	str	Margin
margin_rate	true	str	Margin Rate
unrealized_pnl	true	str	Unrealized Profit and Loss
positions	true	object	Positions
symbol	true	string	Symbol Name
leverage_ratio	true	float	Leverage Ratio
side	true	string	long, short, empty for none position
amount	true	float	Amount in position
entry_price	true	float	Entrance price of position
unrealized_pnl	true	float	Unrealized Profit and Loss
liquidation_price	true	float	Estimated liquidation price
liquidation_rate	true	float	liquidation leverage ratio
code	true	int	Status
Create new order
HTTP Request
POST https://openapi.digifinex.com/v3/{market}/order/new
Request Parameters
market：spot, margin

Field	Request Type	Mandatory	Description
market	str	true	"spot","margin"
symbol	str	true	Symbol Name
type	str	true	buy for limit buy order, sell for limit sell order, buy_market for market buy order, sell_market for market sell order
amount	float	true	Order amount, value in quote currency for market orders and base currency in other order types
price	float	false	Order price required for limit order
post_only	int	false	Default 0, enabled by 1, if enabled the order will be cancelled if it can be executed immediately, making sure there will be no market taking
Response:


{
  "code": 0,
  "order_id": "198361cecdc65f9c8c9bb2fa68faec40"
}

Response Content
Field	Mandatory	Request Type	Description
order_id	true	str	Order ID
code	true	int	Status
Create multiple order
HTTP Request
POST https://openapi.digifinex.com/v3/{market}​/order​/batch_new
Request Parameters
market：spot, margin up to 10 orders at a time, either all succeed or all fail

Field	Request Type	Mandatory	Description
market	str	true	"spot","margin"
symbol	str	true	Symbol Name
list	str	true	order list, must be json-format, eg:[{"type":"buy","amount":0.1,"price":6000,"post_only":1},{"type":"sell","amount":0.1,"price":6100,"post_only":0}]
Response:


{
  "code": 0,
  "order_ids": [
    "198361cecdc65f9c8c9bb2fa68faec40",
    "3fb0d98e51c18954f10d439a9cf57de0"
  ]
}

Response Content
Field	Mandatory	Request Type	Description
order_ids	true	object	Order ID列表
code	true	int	Status
Cancel order
HTTP Request
POST https://openapi.digifinex.com/v3/{market}/order/cancel
Request Parameters
market：spot, margin

Field	Request Type	Mandatory	Description
market	str	true	"spot","margin"
order_id	str	true	Order ID list, separated by commas
Response:


{
  "code": 0,
  "date": 1744190302,
  "success": [
    "198361cecdc65f9c8c9bb2fa68faec40",
    "3fb0d98e51c18954f10d439a9cf57de0"
  ],
  "error": [
    "78a7104e3c65cc0c5a212a53e76d0205"
  ]
}

Response Content
Field	Mandatory	Request Type	Description
success	true	object	Cancel Success Orders
error	true	object	Cancel Failed Orders
code	true	int	Status
date	true	int	date
Transfer assets among accounts
HTTP Request
POST https://openapi.digifinex.com/v3/transfer
Request Parameters
Transfer assets among, 1 for spot account, 2 for margin account, 3 for OTC account Please be noted transfers between margin account and OTC account is currently not available

Field	Request Type	Mandatory	Description
currency_mark	str	true	Currency
num	str	true	Transfer amount
from	int	true	Transfer from, 1 for spot account, 2 for margin account, 3 for OTC account
to	int	true	Transfer to, 1 for spot account, 2 for margin account, 3 for OTC account
Response:


{
  "code": 0
}

Response Content
Field	Mandatory	Request Type	Description
code	true	int	Status
Close positions
HTTP Request
POST https://openapi.digifinex.com/v3/margin/position/close
Request Parameters
说明：以市场价格平掉仓位

Field	Request Type	Mandatory	Description
symbol	str	true	Symbol Name
Response:


{
  "code": 0
}

Response Content
Field	Mandatory	Request Type	Description
code	true	int	Status
Deposit address inquiry
This node is used to query the address of a specific currency

HTTP request
GET.https://openapi.digifinex.com/v3/deposit/address
curl "https://openapi.digifinex.com/v3/deposit/address?currency=btc"
Request parameters
fieldname	if necessary	types	fieldname	value range
currency	true	string	crypto	btc, ltc, bch, eth, etc ...
Response:

{
    "code": 200,
    "data": [
        {
            "currency": "btc",
            "address": "1PSRjPg53cX7hMRYAXGJnL8mqHtzmQgPUs",
            "addressTag": "",
            "chain": ""
        }
    ]
}
Response data
fieldname	if necessary	data type	field description	value range
currency	true	string	currency	
address	true	string	deposit address	
addressTag	true	string	deposit address lable	
chain	true	string	the chain name is empty by default, and USDT has two chains: ERC20 and OMNI	
Status code
status code	error message	Error scenario description
200	success	success
Deposit history
Query the deposit history

HTTP request
GET.https://openapi.digifinex.com/v3/deposit/history
Request parameters
name of parameter	if necessary	type	description	default value	value range
currency	false	string	currency	By default, the default value is null and returns to all crptos	btc, ltc, bch, eth, etc ...
from	false	int	query initial ID	By default, the default value is direct correlation. When direct is' prev ', from is 1, returning from old to new ascending order; When direct is' next ', from is the ID of the most recent record, returning from the old descending order	
size	false	int	Query record size	100	1-500
direct	false	string	Returns to the sorting direction of the record	By default, it is "prev" (ascending)	"Prev" (ascending) or "next" (descending)
Response:

{
  "code": 200,
  "data":
    [
      {
        "id": 1171,
        "currency": "xrp",
        "hashId": "ed03094b84eafbe4bc16e7ef766ee959885ee5bcb265872baaa9c64e1cf86c2b",
        "chain":"",
        "amount": "7.457467",
        "address": "rae93V8d2mdoUQHwBDBdM4NHCMehRJAsbm",
        "state": 3,
        "created_date": "2020-04-20 11:23:00",
        "update_date": "2020-04-20 13:23:00"
      },
      ...
    ]
}
response data
response Data	if neccesary	data type	description	value range
id	true	long		
currency	true	string	currency	
hashId	true	string	transaction hash	
chain	true	string	chain name	The chain name is empty by default, and USDT has two chains: ERC20 and OMNI
amount	true	string	amount	
address	true	string	address	
state	true	int	state	deposit state includes: 1 (in deposit), 2 (to be confirmed), 3 (successfully deposited), 4 (stopped)
created_date	true	string	created date	
update_date	true	string	update date	
Status code
status code	error message	error scenario description
200	success	success
Withdrawal history
Query the withdrawal history

HTTP request
GET.https://openapi.digifinex.com/v3/withdraw/history
Request parameters
name of parameter	if neccesary	type	description	default value	value range
currency	false	string	currency	By default, the default value is null and returns all currencies	btc, ltc, bch, eth, etc ...
from	false	string	query initial ID	By default, the default value is direct correlation. When direct is' prev ', from is 1, returning from old to new ascending; When direct is' next ', from is the ID of the most recent record, returned from the old descending order	
size	false	string	query record size	100	1-500
direct	false	string	Return to the sorting direction of the record	By default, it is "prev" (ascending)	"Prev" (ascending) or "next" (descending)
Response:

{
  "code": 200,
  "data":
    [
      {
        "id": 1171,
        "currency": "xrp",
        "hashId": "ed03094b84eafbe4bc16e7ef766ee959885ee5bcb265872baaa9c64e1cf86c2b",
        "chain": "",
        "amount": 7.457467,
        "address": "rae93V8d2mdoUQHwBDBdM4NHCMehRJAsbm",
        "memo": "100040",
        "fee": "0.00000000",
        "state": 1,
        "created_date": "2020-04-20 11:23:00",
        "update_date": "2020-04-20 13:23:00"
      },
      ...
    ]
}
Response data
name of parameter	if neccesary	data type	description	value range
id	true	long		
currency	true	string	currency	
hashId	true	string	transaction hash	
chain	true	string	chain name	
amount	true	float	amount	
address	true	string	address	
memo	true	string	address lable	
state	true	int	state	
fee	true	string	fee	Withdrawal status includes: 1 (application in progress), 2 (to be confirmed), 3 (completed),4 (rejected)
created_date	true	string	created date	
update_date	true	string	date of update update	
Status code
status code	error message	error scenario description
200	success	success
Sample Code
PHP

<?php

class digifinex
{
  protected $baseUrl = "https://openapi.digifinex.com/v3";    
  protected $appKey;
  protected $appSecret;

  public function __construct($data) {
      $this->appKey = $data['appKey'];
      $this->appSecret = $data['appSecret'];
  }

  private function calc_sign($data = []) {
      $query = http_build_query($data, '', '&');
      $sign = hash_hmac("sha256", $query, $this->appSecret);
      echo 'query: ' . $query . "\r\n";
      echo 'sign: ' . $sign . "\r\n";
      return $sign;
  }

  public function do_request($method, $path, $data = [], $needSign=false) {
      $curl = curl_init();
      $query = http_build_query($data, '', '&');
      if ($method == "POST") {
          curl_setopt($curl, CURLOPT_URL, $this->baseUrl . $path);
          curl_setopt($curl, CURLOPT_POST, true);
          curl_setopt($curl, CURLOPT_POSTFIELDS, $query);
      } else {
          if(!empty($data)){
              curl_setopt($curl, CURLOPT_URL, $this->baseUrl . $path . '?' . $query);
          } else {
              curl_setopt($curl, CURLOPT_URL, $this->baseUrl . $path);
          }
      }
      if($needSign){
          curl_setopt($curl, CURLOPT_HTTPHEADER, array(
              'ACCESS-KEY: ' . $this->appKey,
              'ACCESS-TIMESTAMP: ' . time(),
              'ACCESS-SIGN: ' . $this->calc_sign($data),
          ));
      }
      curl_setopt($curl, CURLOPT_USERAGENT, "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17");
      curl_setopt($curl, CURLOPT_HEADER, false);
      curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($curl, CURLOPT_TIMEOUT, 10);
      $content = curl_exec($curl) ;
      curl_close($curl);
      return $content;
  }
}

$coin = new digifinex([
  'appKey' => 'your-api-key',
  'appSecret' => 'your-api-secret',
]);

echo 'assets => ' . $coin->do_request('GET', '/margin/assets', [], true) . "\r\n";
echo 'place_order => ' . $coin->do_request('POST', '/margin/order/new', [
  'symbol' => 'btc_usdt',
  'price' => 5000,
  'amount' => 0.01,
  'type' => 'buy',
], true) . "\r\n";

JS

var https = require('https');
var crypto = require('crypto')
var querystring = require('querystring');

const baseUrl = "openapi.digifinex.com"
const appKey = "your-api-key"
const appSecret = "your-api-secret"

calc_sign = function(data) {
  var content = querystring.stringify(data);
  return crypto.createHmac('sha256', appSecret).update(content).digest('hex')
}

do_request = function(method, path, data = {}, needSign = false) {
  var content = querystring.stringify(data);
  var options = {
      hostname: baseUrl,
      port: 443,
      path: '/v3' + path,
      method: method,
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_2) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.52 Safari/537.17',
      }
  };
  if (method == "GET" && content != "") {
      options.path += '?' + content;
  }
  if (needSign) {
      options.headers['ACCESS-KEY'] = appKey;
      options.headers['ACCESS-TIMESTAMP'] = parseInt(Date.now() / 1000);
      options.headers['ACCESS-SIGN'] = calc_sign(data);
  }
  console.log('request: ' + JSON.stringify(options));
  var req = https.request(options, function (res) {
      console.log('STATUS: ' + res.statusCode);
      console.log('HEADERS: ' + JSON.stringify(res.headers));
      res.setEncoding('utf8');
      res.on('data', function (chunk) {
          console.log('BODY: ' + chunk);
      });
  });
  req.on('error', function (e) {
      console.log('problem with request: ' + e.message);
  });
  if (method != 'GET') {
      req.write(content);
  }
  req.end();
}

do_request('GET', '/margin/symbols', {}, false)
do_request('POST', '/margin/order/new', {
  symbol: 'btc_usdt',
  price: 5000,
  amount: 0.01,
  type: 'buy',
}, true)

Python

#!/bin/python
# -*-coding=utf-8-*-

import requests
import time
import hmac
import hashlib
import urllib

baseUrl = "https://openapi.digifinex.com/v3"

class digifinex():
    def __init__(self, data):
        self.appKey = data["appKey"]
        self.appSecret = data["appSecret"]

    def _generate_accesssign(self, data):
        query_string = urllib.urlencode(data)
        m = hmac.new(self.appSecret.encode('utf-8'), query_string.encode('utf-8'), hashlib.sha256)
        s = m.hexdigest()
        print("data-origin:", data)
        print("query_string:", query_string)
        print("sign:", s)
        return s

    def do_request(self, method, path, data, needSign=False):
        if needSign:
            headers = {
                "ACCESS-KEY": self.appKey,
                "ACCESS-TIMESTAMP": str(int(time.time())),
                "ACCESS-SIGN": self._generate_accesssign(data),
            }
        else:
            headers = {}
        if method == "POST":
            response = requests.request(method, baseUrl+path, data=data, headers=headers)
        else:
            response = requests.request(method, baseUrl+path, params=data, headers=headers)
        print('response.text:',response.text)
        print('----------------------------------')

coin = digifinex({"appKey":"your-api-key", "appSecret":"your-api-secret"})
coin.do_request("POST", "/margin/order/new", {
    "symbol": "btc_usdt",
    "price": 5000,
    "amount": 0.01,
    "type": "buy"
}, True)

GO

package main

import (
"crypto/hmac"
"crypto/sha256"
"encoding/hex"
"fmt"
"io/ioutil"
"net/http"
"net/url"
"strconv"
"strings"
"time"
)

const (
dfxRestURI = "https://openapi.digifinex.com/v3"
)

type digifinex struct {
appKey         string
appSecret      string
deafultTimeout time.Duration
}

func parseToString(val interface{}) string {
switch t := val.(type) {
case int, int8, int16, int32, int64:
  return fmt.Sprintf("%d", t)
case uint, uint8, uint16, uint32, uint64:
  return fmt.Sprintf("%d", t)
case float32, float64:
  return fmt.Sprintf("%.8f", t)
case string:
  return t
default:
  panic(fmt.Errorf("invalid value type", t))
}
}

func hmacSha256(key []byte, msg []byte) string {
mac := hmac.New(sha256.New, key)
mac.Write(msg)
return hex.EncodeToString(mac.Sum(nil))
}

func (coin *digifinex) doRequest(method string, path string, params map[string]interface{}, sign bool) (*http.Response, error) {
inputParam := url.Values{}
for key, val := range params {
  inputParam.Add(key, parseToString(val))
}
encodedParams := inputParam.Encode()
var (
  req *http.Request
  err error
)
if method == "GET" {
  if encodedParams != "" {
    req, err = http.NewRequest(method, dfxRestURI+path+"?"+encodedParams, nil)
  } else {
    req, err = http.NewRequest(method, dfxRestURI+path, nil)
  }
} else {
  req, err = http.NewRequest(method, dfxRestURI+path, strings.NewReader(encodedParams))
}
if err != nil {
  return nil, fmt.Errorf("unable to create request " + err.Error())
}
// header
req.Header.Add("ACCESS-TIMESTAMP", strconv.Itoa(int(time.Now().Unix())))
if sign {
  req.Header.Add("ACCESS-KEY", coin.appKey)
  req.Header.Add("ACCESS-SIGN", hmacSha256([]byte(coin.appSecret), []byte(encodedParams)))
  fmt.Println(req.Header.Get("ACCESS-SIGN"))
}
client := &http.Client{
  Transport: &http.Transport{},
  Timeout:   coin.deafultTimeout,
}
resp, err := client.Do(req)
if err != nil {
  return nil, err
}
return resp, nil
}

const (
appKey    = "your-api-key"
appSecret = "your-api-secret"
)

func main() {
app := digifinex{
  appKey:    appKey,
  appSecret: appSecret,
}
response, err := app.doRequest("POST", "/spot/order/new", map[string]interface{}{
  "symbol": "btc_usdt"
  "type": "buy",
  "amount": 1,
  "price": "8100",
  "post_only": 0,
}, true)
if err != nil {
  panic(err)
}
textRes, err := ioutil.ReadAll(response.Body)
if err != nil {
  panic(err)
}
defer response.Body.Close()
if response.StatusCode != 200 {
  panic(fmt.Errorf(string(textRes)))
}
fmt.Println(string(textRes))
}

Websocket
Websoket API
For Websoket API see https://github.com/DigiFinex/api/blob/master/Websocket_API_en.md




URL
wss://openapi.digifinex.com/ws/v1/
Compression algorithm
please use zlib deflate

Catalogue
public

Ping
Time
Trades
Depth
AllTicker
Ticker
private

Auth
order
OrderAlgo
Balance
Public Channel
Ping
method:server.ping

request param

Parameters	Required	Type	Description
method	yes	string	server.ping
id	yes	number	auto-increment request id
request example

{
  "method":"server.ping",
  "id":1
}
response param

Parameters	Type	Description
id	number	auto-increment request id
result	string	pong if success
error	string	error msg, null if success
response example

{
  "id":1,
  "result": "pong",
  "error": null
}
Time
method:server.time

request param

Parameters	Required	Type	Description
method	yes	string	server.time
id	yes	number	auto-increment request id
request example

{
  "method":"server.time",
  "id":1
}
response param

Parameters	Type	Description
id	number	auto-increment request id
result	string	seconds since UNIX epoch
error	string	error msg, null if success
response example

{
  "id":1,
  "result": 1523348055,
  "error": null
}
Trades
Subscribe
method:trades.subscribe

request param

Parameters	Required	Type	Description
method	yes	string	trades.subscribe
id	yes	number	auto-increment request id
params	yes	array	array of symbols
request example

{
  "method":"trades.subscribe",
  "id":1,
  "params":["ETH_USDT", "BTC_USDT"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
UnSubscribe
method:trades.unsubscribe

request param

Parameters	Required	Type	Description
method	yes	string	trades.unsubscribe
id	yes	number	auto-increment request id
params	yes	array	array of symbols, empty means unsubscribe all symbols
request example

{
  "method":"trades.unsubscribe",
  "id":1,
  "params": ["ETH_USDT", "BTC_USDT"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
Push
push param

Parameters	Type	Description
method	string	trades.update
id	number	null
- params	array	response data
0	bool	true: is complete result false: is last updated result
- 1	array	list of trades
id	number	trade id
time	number	trade time
price	string	trade price
amount	string	trade amount
type	string	trade side: buy or sell
2	string	trade symbol
push example

{
  "method": "trades.update",
  "params":
  [
    true,
    [
      {
        "id": 7172173,
        "time": 1523339279.761838,
        "price": "398.59",
        "amount": "0.027",
        "type": "buy"
      }
    ],
    "ETH_USDT"
  ],
  "id": null
}
Depth
Subscribe
method:depth.subscribe

request param

Parameters	Required	Type	Description
method	yes	string	depth.subscribe
id	yes	number	auto-increment request id
params	yes	array	array of symbols
request example

{
  "method":"depth.subscribe",
  "id":1,
  "params":["ETH_USDT", "BTC_USDT"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
UnSubscribe
method:depth.unsubscribe

request param

Parameters	Required	Type	Description
method	yes	string	depth.unsubscribe
id	yes	number	auto-increment request id
params	yes	array	array of symbols, empty means unsubscribe all symbols
request example

{
  "method":"depth.unsubscribe",
  "id":1,
  "params": ["ETH_USDT", "BTC_USDT"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
Push
push param

Parameters	Type	Description
method	string	depth.update
id	number	null
- params	array	response data
0	bool	true: is complete result false: is last updated result
- 1	object	depth data
- asks	array	ask raws
- 0	string	price
- 1	string	amount
- bids	array	bid raws
- 0	string	price
- 1	string	amount
2	string	trade symbol
push example

{
  "method": "depth.update",
  "params": [
    true,
    {
      "asks": [
        [
          "8000.00",
          "9.6250"
        ]
      ],
      "bids": [
        [
          "8000.00",
          "9.6250"
        ]
      ]
    },
    "EOS_USDT"
  ],
  "id": null
}
All Ticker
Subscribe
method:all_ticker.subscribe

request param

Parameters	Required	Type	Description
method	yes	string	all_ticker.subscribe
id	yes	number	auto-increment request id
request example

{
  "method":"all_ticker.subscribe",
  "id":1
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
UnSubscribe
method:all_ticker.unsubscribe

request param

Parameters	Required	Type	Description
method	yes	string	all_ticker.unsubscribe
id	yes	number	auto-increment request id
request example

{
  "method":"all_ticker.unsubscribe",
  "id":1
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
Push
push param

Parameters	Type	Description
method	string	all_ticker.update
id	number	null
- params	array	array of ticker
symbol	string	trade symbol
open_24h	string	24 hours ago trade price
low_24h	string	lowest trade price since 24 hours ago
base_volume_24h	string	total trade volume since 24 hours ago
quote_volume_24h	string	total trade amount since 24 hours ago
last	string	last trade price
last_qty	string	last trade volume
best_bid	string	best bid price
best_bid_size	string	best bid volume
best_ask	string	best ask price
best_ask_size	string	best ask volume
timestamp	number	milliseconds since UNIX epoch
push example

{
  "method": "all_ticker.update",
  "params": [{
    "symbol": "BTC_USDT",
    "open_24h": "1760",
    "low_24h": "1.00",
    "base_volume_24h": "9.40088557",
    "quote_volume_24h": "21786.30588557",
    "last": "4000",
    "last_qty": "1",
    "best_bid": "3397",
    "best_bid_size": "0.85",
    "best_ask": "4000",
    "best_ask_size": "109.2542",
    "timestamp": 1586762372864
  }],
  "id": null
}
Ticker
Subscribe
method:ticker.subscribe

request param

Parameters	Required	Type	Description
method	yes	string	ticker.subscribe
id	yes	number	auto-increment request id
params	yes	array	array of symbols
request example

{
  "method":"ticker.subscribe",
  "id":1,
  "params":["ETH_USDT", "BTC_USDT"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
UnSubscribe
method:ticker.unsubscribe

request param

Parameters	Required	Type	Description
method	yes	string	ticker.unsubscribe
id	yes	number	auto-increment request id
params	yes	array	array of symbols, empty means unsubscribe all symbols
request example

{
  "method":"ticker.unsubscribe",
  "id":1,
  "params": ["ETH_USDT", "BTC_USDT"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
Push
push param

Parameters	Type	Description
method	string	ticker.update
id	number	null
- params	array	array of ticker
symbol	string	trade symbol
open_24h	string	24 hours ago trade price
low_24h	string	lowest trade price since 24 hours ago
base_volume_24h	string	total trade volume since 24 hours ago
quote_volume_24h	string	total trade amount since 24 hours ago
last	string	last trade price
last_qty	string	last trade volume
best_bid	string	best bid price
best_bid_size	string	best bid volume
best_ask	string	best ask price
best_ask_size	string	best ask volume
timestamp	number	milliseconds since UNIX epoch
push example

{
  "method": "ticker.update",
  "params": [{
    "symbol": "BTC_USDT",
    "open_24h": "1760",
    "low_24h": "1.00",
    "base_volume_24h": "9.40088557",
    "quote_volume_24h": "21786.30588557",
    "last": "4000",
    "last_qty": "1",
    "best_bid": "3397",
    "best_bid_size": "0.85",
    "best_ask": "4000",
    "best_ask_size": "109.2542",
    "timestamp": 1586762372864
  }],
  "id": null
}
Private Channel
Auth
method:server.auth

params = [apikey,timestamp,sign]
apikey: applied apikey
timestamp: millisecond timestamp
sign: CryptoJS.enc.Base64.Stringify(CryptoJS.HmacSHA256(timestamp, secret))
request param

Parameters	Required	Type	Description
method	yes	string	server.auth
id	yes	number	auto-increment request id
- params	yes	array	auth data
0	yes	string	valid apikey
1	yes	string	milliseconds since UNIX epoch
2	yes	string	signature
request example

{
  "method":"server.auth",
  "id":1,
  "params": ["5a8e6b662ddb0","1583135616239","lXU0njGw4F+89g+EMxWtS9cLjKOqvUQ3+vsKK2yda40="]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
Order
Subscribe
method:order.subscribe

request param

Parameters	Required	Type	Description
method	yes	string	order.subscribe
id	yes	number	auto-increment request id
params	yes	array	array of symbols
request example

{
  "method":"order.subscribe",
  "id":1,
  "params":["ETH_USDT", "BTC_USDT"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
UnSubscribe
method:order.unsubscribe

request param

Parameters	Required	Type	Description
method	yes	string	order.unsubscribe
id	yes	number	auto-increment request id
params	yes	array	array of symbols, empty means unsubscribe all symbols
request example

{
  "method":"order.unsubscribe",
  "id":1,
  "params": ["ETH_USDT", "BTC_USDT"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
Push
push param

Parameters	Type	Description
method	string	order.update
id	number	null
- params	array	array of order
amount	string	order amount
filled	string	filled amount
id	string	order id
mode	number	order mode, 1: spot, 2: margin
notional	string	notional amount
price	string	order price
price_avg	string	avg filled price
side	string	order side, buy or sell
status	number	order status, 0: unfilled, 1: partially filled, 2: fully filled, 3: canceled unfilled, 4: canceled partially filled
symbol	string	symbol
type	string	order type, limit or market
timestamp	number	milliseconds since UNIX epoch
push example

{
  "method": "order.update",
  "params": [{
    "amount": "0",
    "filled": "0.9969",
    "id": "31b7f41c81787b4200c75eb074e6edc9",
    "mode": 1,
    "notional": "9713.82",
    "price": "0",
    "price_avg": "9700",
    "side": "buy",
    "status": 2,
    "symbol": "BTC_USDT",
    "timestamp": 1589272547000,
    "type": "market"
  }],
  "id": null
}
Order Algo
Subscribe
method:order_algo.subscribe

request param

Parameters	Required	Type	Description
method	yes	string	order_algo.subscribe
id	yes	number	auto-increment request id
params	yes	array	array of symbols
request example

{
  "method":"order_algo.subscribe",
  "id":1,
  "params":["ETH_USDT", "BTC_USDT"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
UnSubscribe
method:order_algo.unsubscribe

request param

Parameters	Required	Type	Description
method	yes	string	order_algo.unsubscribe
id	yes	number	auto-increment request id
params	yes	array	array of symbols, empty means unsubscribe all symbols
request example

{
  "method":"order_algo.unsubscribe",
  "id":1,
  "params": ["ETH_USDT", "BTC_USDT"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
Push
push param

Parameters	Type	Description
method	string	order_algo.update
id	number	null
- params	array	array of order
algo_price	string	order price
amount	string	order amount
id	string	order id
mode	number	order mode, 1: spot, 2: margin
side	string	order side, buy or sell
status	number	order algo status, -2: fail, -1: canceled, 0: ready to effect, 1: effecting, 2: success
symbol	string	symbol
trigger_price	string	trigger price
timestamp	number	milliseconds since UNIX epoch
push example

{
  "method": "order_algo.update",
  "params": [{
    "algo_price": "4000",
    "amount": "1",
    "id": "ff0738804cc3361fa91cb7c84feb113c",
    "mode": 1,
    "side": "buy",
    "status": 0,
    "symbol": "BTC_USDT",
    "timestamp": 1586767202000,
    "trigger_price": "4000"
  }],
  "id": null
}
Balance
Subscribe
method:balance.subscribe

request param

Parameters	Required	Type	Description
method	yes	string	balance.subscribe
id	yes	number	auto-increment request id
params	yes	array	array of currency
request example

{
  "method":"balance.subscribe",
  "id":1,
  "params":["USDT", "BTC"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
UnSubscribe
method:balance.unsubscribe

request param

Parameters	Required	Type	Description
method	yes	string	balance.unsubscribe
id	yes	number	auto-increment request id
params	yes	array	array of currency, empty means unsubscribe all currency
request example

{
  "method":"balance.unsubscribe",
  "id":1,
  "params": ["USDT", "BTC"]
}
response param

Parameters	Type	Description
id	number	auto-increment request id
error	string	error msg, null if success
- result	object	result data
status	string	success
response example

{
  "error": null,
  "result":
  {
    "status": "success"
  },
  "id": 12312
}
Push
push param

Parameters	Type	Description
method	string	order_algo.update
id	number	null
- params	array	array of order
currency	string	currency
free	string	usable asset
total	string	total asset
used	string	frozen asset
push example

{
  "method": "balance.update",
  "params": [{
    "currency": "USDT",
    "free": "99944652.8478545303601106",
    "total": "99944652.8478545303601106",
    "used": "0.0000000000"
  }],
  "id": null
}





BaseUrl: https://openapi.digifinex.com/swap/v2

Authentication
RateLimit
ErrorCode
Public endpoint

server time
api weight
Instruments
Instrument
OrderBook
RecentTrades
Ticker
Tickers
RecentCandle
CurrentFundingRate
CandleHistory
FundingRateHistory
Private endpoint

account

AccountBalance
AccountTransfer
Positions
PositionMode
PositionMargin
SetLeverage
TradingFee
Bills
Funding Fee
TransferRecord
trade

OrderPlace
CancelOrder
BatchOrder
BatchCancel
OpenOrder
OrderInfo
HistoryOrder
HistoryTrade
copy trading

ExpertSponsorOrder
CloseOrder
CancelCurrentOrder
UserCenterCurrent
UserCenterHistory
ExpertCurrentOpenOrder
AddStopProfitOrderOrStopLossOrder
CancelStopLossOrStopProfitOrder
AccountAvailableBalance
PlanCommissionList
InstrumentList
Authentication
Making Requests
All private REST requests must contain the following headers:

ACCESS-KEY The APIKey as a String.
ACCESS-SIGN The hex-encoded signature (see Signing Messages subsection for details).
ACCESS-TIMESTAMP The milliseconds since UNIX epoch of your request. e.g. 1657522488402
 Request bodies should have content type `application/json` and be in valid JSON format.
Signature
The ACCESS-SIGN header is generated as follows:

Create a prehash string of timestamp + method + requestPath + body (where + represents String concatenation).
Prepare the SecretKey.
Sign the prehash string with the SecretKey using the HMAC SHA256.
Encode the signature in the hex format.
Example: sign=CryptoJS.HmacSHA256(timestamp + 'GET' + '/swap/v2/positions?instrument_id=BTCUSDTPERP', ApiSecret).toString(Hex)
The timestamp value is the same as the ACCESS-TIMESTAMP header with millisecond as a string, e.g. 1657522488402.
The request method should be in UPPERCASE: e.g. GET and POST.
The requestPath is the path of requesting an endpoint. Example: /swap/v2/positions?instrument_id=BTCUSDTPERP
The body refers to the String of the request body. It can be omitted if there is no request body (frequently the case for GET requests).
Example: {"instrument_id":"BTCUSDTPERP","leverage":"20","side":"1"}
The SecretKey is generated when you create an APIKey. Example: ffd4e900015bdfaf5a72aa06f5612290df25c23a78

 `GET` request parameters are counted as requestpath, not body
RateLimit
Public endpoint must observe IP limits rule, private endpoint must observe account and APIKey limits rule.
There has total weight every minute for each IP/account/APIKey, every route has different weight.
When a 429 is received, it's your obligation as an API to back off and not spam the API.
Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (HTTP status 403).
There will be a retry-after field in the response header while over request weight.
IP/account/APIKey bans are tracked and scale in duration for repeat offenders, from 2 minutes to 1 day.
IP Limits
Every public request will contain ip-weight-minute-use in the response headers which has the current used weight for the IP for all request rate limiters defined.
Every public request will contain ip-weight-minute-remain in the response headers which has the current remain weight for the IP for all request rate limiters defined.
Account Limits
Every private request will contain account-weight-minute-use in the response headers which has the current used weight for the account for all request rate limiters defined.
Every private request will contain account-weight-minute-remain in the response headers which has the current remain weight for the account for all request rate limiters defined.
APIKey Limits
Every private request will contain apikey-weight-minute-use in the response headers which has the current used weight for the APIKey for all request rate limiters defined.
Every private request will contain apikey-weight-minute-remain in the response headers which has the current remain weight for the APIKey for all request rate limiters defined.
ErrorCode
code	message	description
0	success	request success
400001	ParamMissing	missing require param
400002	ParamInvalid	param invalid
400003	InvalidIP	unAuthentication ip
400004	InvalidSign	access-sign miss matched
400005	PermissionDeny	permission deny
400006	InvalidApiKey	invalid api key
401001	OrderExist	can not change leverage when exist no finish order
401002	OverMaxOpenLimit	position open value over max limit
401003	NotEnoughMoney	account balance not enough
401004	InstrumentNotTrading	instrument trade is suspended
401005	InstrumentMaintain	instrument under maintain
401006	InstrumentMinSizeLimit	order size less than mini order size
401007	InvalidPricePrecision	price precision invalid
401008	MarketTradingNotSupport	current instrument deny market trade
401009	MarketNoOrder	market order not support when opponent is empty
401010	PriceOverMaxBuyLimit	order price over max buy price
401011	PriceBelowMinSellLimit	order price less than min sell price
401012	NotEnoughClosePosition	not enough position to close
401013	PriceOverLiquidationLimit	order price inferior to liquidation price
401014	OrderCountOverLimit	batch order/cancel count over limit (max 20)
401015	PositionNotIsolated	can not do this when position mode is not isolated
401016	PositionExist	can not do this when position exist
401017	PositionNotExist	can not do this when position not exist
401018	TransferNotAllow	current transfer request not allowed
401019	TransferInRisk	current transfer has entered the risk control process, please contract customer service
403001	FrequencyLimit	request reach frequency limit
403002	RequestForbidden	request forbidden (repeat requests after reach frequency limit)
403003	Disabled	disabled for current user, please contract customer service
404001	FollowExpertLocked	expert is locked, can't open position
404002	FollowSettleLocked	in the contract settlement, it does not support to sponsor orders
404003	FollowInstrumentNotExist	the documentary contract variety is offline or does not exist
404004	FollowOrderChangeHasPosition	existing positions, does not support modification of margin mode or leverage
404005	FollowOrderChangeHasFollow	existing orders, does not support modification of margin mode or leverage
404006	FollowOrderChangeHasOrder	there is already a pending order, which does not support modifying the margin mode or leverage
404007	FollowOrderPriceOffsetOverLimit	the price of the order deviates from the mark price a lot, for the sake of your account risk, please reduce the number of open positions
404008	FollowOrderStopEarnTriggerPriceLarge	the take profit price must be greater than the order price
404009	FollowOrderStopEarnTriggerPriceLess	the take profit price must be less than the order price
404010	FollowOrderStopLossTriggerPriceLess	the stop loss price must be lower than the order price
404011	FollowOrderStopLossTriggerPriceLarge	the stop loss price must be greater than the order price
404012	FollowErrorOrderClosed	the order has been executed to close the position
404013	FollowOrderNotExist	order does not exist
404014	FollowStopProfitExist	take profit already exists
404015	FollowStopLossExist	stop loss already exists
500001	SystemError	system error
500002	SystemException	system exception, pls retry
Public endpoint
Server Time
request URL： GET /swap/v2/public/time

response example

{
  "code":0,
  "data":1657528968992
}
response param

Parameters	Types	Description
code	number	error code
data	number	milliseconds since UNIX epoch
Api Weight
request URL： GET /swap/v2/public/api_weight

response example

{
  "code":0,
  "data":[
    {
      "path":"/swap/v2/api_weight",
      "weight":1
    },
    {
      "path":"/swap/v2/balance",
      "weight":1
    }
  ]
}

response param

Parameters	Types	Description
code	number	error code
- data	object	response data
path	string	route path
weight	number	route weight
Instruments
request URL： GET /swap/v2/public/instruments

request param

Parameters	Required	Type	Description
type	no	number	instrument type 1 simulate 2 real default real
response example

 {
  "code":0,
  "data": [
    {
      "instrument_id":"BTCUSDT2PERP",
      "type":"SIMULATE",
      "contract_type":"PERPETUAL",
      "base_currency":"BTC",
      "quote_currency":"USDT2",
      "clear_currency":"USDT2",
      "contract_value":"0.001",
      "contract_value_currency":"BTC",
      "is_inverse": false,
      "is_trading":true,
      "status":"ONLINE",
      "price_precision":4,
      "tick_size":"0.0001",
      "min_order_amount":1,
      "open_max_limits": [
        {
          "leverage":"20",
          "max_limit":"100000000"
        }
      ]},
    {
      "instrument_id":"EOSUSDT2PERP",
      "type":"SIMULATE",
      "contract_type":"PERPETUAL",
      "base_currency":"EOS",
      "quote_currency":"USDT",
      "clear_currency":"USDT",
      "contract_value":"0.001",
      "contract_value_currency":"EOS",
      "is_inverse": false,
      "is_trading":false,
      "status":"ONLINE",
      "price_precision":4,
      "tick_size":"0.0001",
      "min_order_amount":1,
      "open_max_limits":[]
    }
  ]
}
response param

Parameters	Type	Description
code	number	error code
- data	object	response data
instrument_id	string	instrument id
type	string	instrument type: SIMULATE｜REAL
contract_type	string	contract type: PERPETUAL
base_currency	string	base currency
quote_currency	string	quote currency
clear_currency	string	settlement currency
contract_value	string	contract value for each size
contract_value_currency	string	currency for contract value
is_inverse	boolean	is inverse contract
is_trading	boolean	trading status
status	string	contract status: ONLINE｜OFFLINE｜DELIVERY
price_precision	number	price precision
tick_size	string	mini price step
min_order_amount	number	mini order amount
- - open_max_limits	object	position max open value limit(position leverage bigger than leverage,position value must not more than limit)
leverage	string	leverage
max_limit	string	position max value
Instrument
request URL： GET /swap/v2/public/instrument

request param

Parameters	Required	Type	Description
instrument_id	yes	string	instrument id
response example

 {
  "code":0,
  "data": {
    "instrument_id":"BTCUSDT2PERP",
    "type":"SIMULATE",
    "contract_type":"PERPETUAL",
    "base_currency":"BTC",
    "quote_currency":"USDT2",
    "clear_currency":"USDT2",
    "contract_value":"0.001",
    "contract_value_currency":"BTC",
    "is_inverse": false,
    "is_trading":true,
    "status":"ONLINE",
    "price_precision":4,
    "tick_size":"0.0001",
    "min_order_amount":1,
    "open_max_limits": [
      {
        "leverage":"20",
        "max_limit":"100000000"
      }
    ]
  }
}
response param

Parameters	Type	Description
code	number	error code
- data	object	response data
instrument_id	string	instrument id
type	string	instrument type: SIMULATE｜REAL
contract_type	string	contract type: PERPETUAL
base_currency	string	base currency
quote_currency	string	quote currency
clear_currency	string	settlement currency
contract_value	string	contract value for each size
contract_value_currency	string	currency for contract value
is_inverse	boolean	is inverse contract
is_trading	boolean	trading status
status	string	contract status: ONLINE｜OFFLINE｜DELIVERY
price_precision	number	price precision
tick_size	string	mini price step
min_order_amount	number	mini order amount
- - open_max_limits	object	position max open value limit(position leverage bigger than leverage,position value must not more than limit)
leverage	string	leverage
max_limit	string	position max value
OrderBook
request URL： GET /swap/v2/public/depth

request param

Parameters	Required	Type	Description
instrument_id	yes	string	instrument id
limit	no	number	request level: 1-100, default 20
response example

{
  "code":0,
  "data":{
    "instrument_id":"BTCUSDTPERP",
    "timestamp":1657531507660,
    "asks":[
      ["20609.30",3855],
      ["20616.18",8565],
      ["20616.98",4597],
      ["20617.08",4659],
      ["20617.18",4519],
      ["20617.28",5195],
      ["20617.38",11139],
      ["20617.48",6117],
      ["20617.78",11416],
      ["20617.88",11322]
    ],
    "bids":[
      ["20588.60",5000],
      ["20582.32",4637],
      ["20582.22",4075],
      ["20582.02",4275],
      ["20581.82",4606],
      ["20581.72",3968],
      ["20581.62",4166],
      ["20581.52",4246],
      ["20581.42",4565],
      ["20581.22",3918]
    ]
  }
}
response param

Parameters	Type	Description
code	number	error code
- data	object	response data
instrument_id	string	instrument id
timestamp	number	milliseconds since UNIX epoch
- - asks	object	asks book
0	string	price
1	number	amount
- - bids	object	bids book
0	string	price
1	number	amount
RecentTrades
request URL： GET /swap/v2/public/trades

request param

Parameters	Required	Type	Description
instrument_id	yes	string	instrument id
limit	no	number	request level: 1-100, default 20
response example

{
  "code":0,
  "data":[
    {
      "instrument_id":"BTCUSDTPERP",
      "trade_id":"1546430170401869825",
      "direction":"1",
      "volume":"10000",
      "price":"20541.79",
      "trade_time":1657532658564
    },
    {
      "instrument_id":"BTCUSDTPERP",
      "trade_id":"1546430159257604097",
      "direction":"3",
      "volume":"967",
      "price":"20542.54",
      "trade_time":1657532655907
    }
  ]
}
response param

Parameters	Type	Description
code	number	error code
- data	object	response data
instrument_id	string	instrument id
trade_id	string	trade id
direction	string	order direction 1:Open Long 2:Open Short 3:Close Long 4:Close Short
volume	string	trade volume
price	string	trade price
trade_time	number	milliseconds since UNIX epoch
Ticker
request URL： GET /swap/v2/public/ticker

request param

Parameters	Required	Type	Description
instrument_id	yes	string	instrument id
response example

{
  "code":0,
  "data": {
    "instrument_id":"BTCUSDTPERP",
    "index_price":"20529.49",
    "mark_price":"20533.91",
    "max_buy_price":"25661.54",
    "min_sell_price":"15396.92",
    "best_bid":"20523.73",
    "best_bid_size":"4000",
    "best_ask":"20544.37",
    "best_ask_size":"3080",
    "high_24h":"21351.41",
    "open_24h":"21308.4",
    "low_24h":"20373.31",
    "last":"20528.33",
    "last_qty":"10000",
    "volume_24h":"135526503",
    "price_change_percent":"-0.036608567513281134",
    "open_interest":"12344.55",
    "timestamp":1657533359744
  }
}
response param

Parameters	Type	Description
code	number	error code
- data	object	response data
instrument_id	string	instrument id
index_price	string	index price
mark_price	string	mark price
max_buy_price	string	max buy price
min_sell_price	string	min sell price
best_bid	string	best bid price
best_bid_size	string	best bid volume
best_ask	string	best ask price
best_ask_size	string	best ask volume
high_24h	string	highest trade price since 24 hours ago
open_24h	string	24 hours ago trade price
low_24h	string	lowest trade price since 24 hours ago
last	string	last trade price
last_qty	string	last trade volume
volume_24h	string	total trade volume since 24 hours ago
price_change_percent	string	price change percent from 24 hours ago to now
open_interest	string	open interest
timestamp	number	milliseconds since UNIX epoch
Tickers
request URL： GET /swap/v2/public/tickers

request param

Parameters	Required	Type	Description
type	no	number	instrument type 1 simulate 2 real default real
response example

{
  "code":0,
  "data": [
    {
      "instrument_id":"BTCUSDTPERP",
      "index_price":"20529.49",
      "mark_price":"20533.91",
      "max_buy_price":"25661.54",
      "min_sell_price":"15396.92",
      "best_bid":"20523.73",
      "best_bid_size":"4000",
      "best_ask":"20544.37",
      "best_ask_size":"3080",
      "high_24h":"21351.41",
      "open_24h":"21308.4",
      "low_24h":"20373.31",
      "last":"20528.33",
      "last_qty":"10000",
      "volume_24h":"135526503",
      "price_change_percent":"-0.036608567513281134",
      "open_interest":"-",
      "timestamp":1657533359744
    }
  ]
}
response param

Parameters	Type	Description
code	number	error code
- data	object	response data
instrument_id	string	instrument id
index_price	string	index price
mark_price	string	mark price
max_buy_price	string	max buy price
min_sell_price	string	min sell price
best_bid	string	best bid price
best_bid_size	string	best bid volume
best_ask	string	best ask price
best_ask_size	string	best ask volume
high_24h	string	highest trade price since 24 hours ago
open_24h	string	24 hours ago trade price
low_24h	string	lowest trade price since 24 hours ago
last	string	last trade price
last_qty	string	last trade volume
volume_24h	string	total trade volume since 24 hours ago
price_change_percent	string	price change percent from 24 hours ago to now
open_interest	string	ignore
timestamp	number	milliseconds since UNIX epoch
RecentCandle
request URL： GET /swap/v2/public/candles

request param

Parameters	Required	Type	Description
instrument_id	yes	string	instrument id
granularity	yes	string	candle granularity: 1m 5m 15m 30m 1h 4h 12h 1d 1w
limit	yes	number	return raws: 1-100, default 20
response example

{
  "code":0,
  "data":{
    "instrument_id":"BTCUSDTPERP",
    "granularity":"15m",
    "candles":[
      [1657536300000,"20596.79","20597.39","20564.8","20590.31","559516","559.516"],
      [1657535400000,"20590.36","20598.41","20558.41","20593.17","1638892","1638.892"]
    ]
  }
}
response param

Parameters	Type	Description
code	number	error code
- data	object	response data
instrument_id	string	instrument id
granularity	string	candle granularity: 1m 5m 15m 30m 1h 4h 12h 1d 1w
- - candles	object	candle list
0	number	milliseconds since UNIX epoch (candle start)
1	string	open price
2	string	highest price
3	string	lowest price
4	string	close price
5	string	trade volume
6	string	token trade num
CurrentFundingRate
request URL： GET /swap/v2/public/funding_rate

request param

Parameters	Required	Type	Description
instrument_id	yes	string	instrument id
response example

{
  "code":0,
  "data":{
    "instrument_id":"BTCUSDTPERP",
    "funding_rate":"-0.001",
    "funding_time":1657612800000,
    "next_funding_rate":"-0.001",
    "next_funding_time":1657641600000
  }
}
response param

Parameters	Type	Description
code	number	error code
- data	object	response data
instrument_id	string	instrument id
funding_rate	string	current funding rate
funding_time	number	settlement time,milliseconds since UNIX epoch
next_funding_rate	string	forecasted funding rate for the next period
next_funding_time	number	funding time for the next period, milliseconds since UNIX epoch
CandleHistory
request URL： GET /swap/v2/public/candles_history

request param

Parameters	Required	Type	Description
instrument_id	yes	string	instrument id
granularity	yes	string	candle granularity: 1m 5m 15m 30m 1h 4h 12h 1d 1w
start_timestamp	no	number	query start milliseconds since UNIX epoch
end_timestamp	no	number	query end milliseconds since UNIX epoch
limit	no	number	query raws: 1-100, default 20
response example

{
  "code":0,
  "data":{
    "instrument_id":"BTCUSDTPERP",
    "granularity":"15m",
    "candles":[
      [1653994800000,"31660.34","31749.37","31587.91","31734.43","105048","105.048"],
      [1653995700000,"31736.57","31739.48","31603.44","31603.96","140370","140.37"]
    ]
  }
}
response param

Parameters	Type	Description
code	number	error code
- data	object	response data
instrument_id	string	instrument id
granularity	string	candle granularity: 1m 5m 15m 30m 1h 4h 12h 1d 1w
- - candles	object	candle list
0	number	milliseconds since UNIX epoch (candle start)
1	string	open price
2	string	highest price
3	string	lowest price
4	string	close price
5	string	trade volume
6	string	token trade num
FundingRateHistory
request URL： GET /swap/v2/public/funding_rate_history

request param

Parameters	Required	Type	Description
instrument_id	yes	string	instrument id
start_timestamp	no	number	query start milliseconds since UNIX epoch
end_timestamp	no	number	query end milliseconds since UNIX epoch
limit	no	number	query raws: 1-100, default 20
response example

{
  "code":0,
  "data":{
    "instrument_id":"BTCUSDTPERP",
    "funding_rates":[
      {"rate":"0.0001","time":1598572800000},
      {"rate":"0.0001","time":1598601600000}
    ]
  }
}
response param

Parameters	Type	Description
code	number	error code
- data	object	response data
instrument_id	string	instrument id
- - funding_rates	object	funding rate list
rate	string	funding rate
time	number	settlement time







BaseUrl: wss://openapi.digifinex.com/swap_ws/v2/

Connection
ErrorCode
Public channel

Time
Ping
Ticker
AllTicker
Depth
Trades
CurrentCandle
IndexPrice
MarkPrice
MarkCandle
PriceRange
FundRate
SettlePrice
Private channel

Token
Auth
Account
Position
Order
OrderAlgo
Connection
A single connection is only valid for 24 hours; expect to be disconnected at the 24 hour mark
The connection will break automatically if the subscription is not established or data has not been pushed for more than 60 seconds, to keep the connection stable, you should set a timer less than 60 second and send a ping request when the timer triggered(see Ping).
A single connection can not subscribe over 30 public channels, if you need subscribe more than 30 public channels, you need to build more connection.
All response use zlib deflate to compress data.
deflate example

<script src="https://cdn.bootcss.com/pako/1.0.6/pako.min.js"></script>
<script src="https://static.runoob.com/assets/jquery/2.0.3/jquery.min.js"></script>
<script>
  websocket = function () {
    var ws = new WebSocket("wss://openapi.digifinex.com/swap_ws/v2/");
    ws.onopen = function() {
      console.log("connect success");
      ws.send('{"id":1, "event":"server.ping"}');
    }
    ws.onmessage = function(e) {
      var blob = e.data;
      var reader = new FileReader();
      reader.readAsBinaryString(blob);
      reader.onload = function (evt) {
        var data = pako.inflate(evt.target.result, { to: 'string' })
        console.log("receive binaray message: " + data);
      }
    }
  };
  websocket();
</script>
ErrorCode
code	message	description
1	success	request success
2	ParamInvalid	param invalid
3	AuthFail	auth fail
4	NeedAuth	need auth
5	RepeatSubscribe	repeat subscribe
6	SubscribeFail	subscribe fail
7	UnsubscribeFailed	unsubscribe fail
8	ApiNotActive	api not active
9	RepeatAuth	repeat auth
Public Channel
Time
event:server.time

request param

Parameters	Required	Type	Description
event	yes	string	server.time
id	yes	number	auto-increment request id
request example

{
  "event":"server.time",
  "id":1
}
response param

Parameters	Type	Description
event	string	server.time
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
data	string	milliseconds since UNIX epoch
response example

{
  "event":"server.time",
  "id":1,
  "code":1,
  "msg":"success",
  "data":1662109531891
}
Ping
event:server.ping

request param

Parameters	Required	Type	Description
event	yes	string	server.ping
id	yes	number	auto-increment request id
request example

{
  "event":"server.ping",
  "id":1
}
response param

Parameters	Type	Description
event	string	server.ping
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
data	string	pong if success
response example

{
  "event":"server.ping",
  "id":1,
  "code":1,
  "msg":"success",
  "data":"pong"
}
Ticker
Subscribe
event:ticker.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	ticker.subscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"ticker.subscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"ticker.subscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	ticker.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"ticker.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:ticker.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	ticker.unsubscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
request example

{
  "event":"ticker.unsubscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"ticker.unsubscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	ticker.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"ticker.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	ticker.unsubscribe
- data	object	response data
instrument_id	string	instrument id
best_bid	string	best bid price
best_bid_size	string	best bid volume
best_ask	string	best ask price
best_ask_size	string	best ask volume
high_24h	string	highest trade price since 24 hours ago
open_24h	string	24 hours ago trade price
low_24h	string	lowest trade price since 24 hours ago
last	string	last trade price
last_qty	string	last trade volume
volume_24h	string	total trade volume since 24 hours ago
volume_token_24h	string	total trade token since 24 hours ago
open_interest	string	ignore
timestamp	number	milliseconds since UNIX epoch
push example

{
  "event":"ticker.update",
  "data":{
    "instrument_id":"ETHUSDTPERP",
    "best_bid":"1588.41",
    "best_bid_size":"938",
    "best_ask":"1588.50",
    "best_ask_size":"220",
    "high_24h":"1611.49",
    "open_24h":"1563.83",
    "low_24h":"1513.14",
    "last":"1588.35",
    "last_qty":"130",
    "volume_24h":"81330353",
    "volume_token_24h":"813303.53",
    "open_interest":"-",
    "timestamp":1662116941153
  }
}
All Ticker
Subscribe
event:all_ticker.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	all_ticker.subscribe
id	yes	number	auto-increment request id
request example

{
  "event":"all_ticker.subscribe",
  "id":1
}
response param

Parameters	Type	Description
event	string	all_ticker.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"all_ticker.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:all_ticker.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	all_ticker.unsubscribe
id	yes	number	auto-increment request id
request example

{
  "event":"all_ticker.unsubscribe",
  "id":1
}
response param

Parameters	Type	Description
event	string	all_ticker.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"all_ticker.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	ticker.unsubscribe
- data	object	response data
instrument_id	string	instrument id
best_bid	string	best bid price
best_bid_size	string	best bid volume
best_ask	string	best ask price
best_ask_size	string	best ask volume
high_24h	string	highest trade price since 24 hours ago
open_24h	string	24 hours ago trade price
low_24h	string	lowest trade price since 24 hours ago
last	string	last trade price
last_qty	string	last trade volume
volume_24h	string	total trade volume since 24 hours ago
volume_token_24h	string	total trade token since 24 hours ago
open_interest	string	ignore
timestamp	number	milliseconds since UNIX epoch
push example

[
  {
    "instrument_id":"ETHUSDTPERP",
    "best_bid":"1572.12",
    "best_bid_size":"947",
    "best_ask":"1572.21",
    "best_ask_size":"972",
    "high_24h":"1647.36",
    "open_24h":"1577.20",
    "low_24h":"1546.10",
    "last":"1572.19",
    "last_qty":"51",
    "volume_24h":"87716861",
    "volume_token_24h":"877168.61",
    "open_interest":"-",
    "timestamp":1662169486547
  }
]
Depth
Subscribe
event:depth.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	depth.subscribe
id	yes	number	auto-increment request id
level	yes	number	depth level, valid level: 10 20 100
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"depth.subscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP",
  "level": 10
}
or

{
  "event":"depth.subscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"],
  "level": 10
}
response param

Parameters	Type	Description
event	string	depth.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"depth.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:depth.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	depth.unsubscribe
id	yes	number	auto-increment request id
level	yes	number	depth level, valid level: 10 20 100
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
request example

{
  "event":"depth.unsubscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP",
  "level": 10
}
or

{
  "event":"depth.unsubscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"],
  "level": 10
}
response param

Parameters	Type	Description
event	string	depth.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"depth.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	ticker.unsubscribe
- data	object	response data
instrument_id	string	instrument id
level	number	push depth level
timestamp	number	milliseconds since UNIX epoch
- - asks	object	asks book
0	string	price
1	number	amount
- - bids	object	bids book
0	string	price
1	number	amount
push example

{
  "event":"depth.update",
  "data":{
    "instrument_id":"BTCUSDTPERP",
    "level":10,
    "timestamp":1662173255498,
    "asks":[
      ["19962.75",0],
      ["19964.25",561]
    ],
    "bids":[
      ["19928.54",1001]
    ]
  }
}
Trades
Subscribe
event:trades.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	trades.subscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"trades.subscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"trades.subscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	trades.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"trades.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:trades.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	trades.unsubscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
request example

{
  "event":"trades.unsubscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"trades.unsubscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	trades.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"trades.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	trades.update
- data	object	response data
instrument_id	string	instrument id
trade_id	string	trade id
direction	string	order direction 1:Open Long 2:Open Short 3:Close Long 4:Close Short
volume	string	trade volume
price	string	trade price
trade_time	number	milliseconds since UNIX epoch
response example

{
  "event":"trades.update",
  "data":[
    {
      "instrument_id":"ETHUSDTPERP",
      "trade_id":"1565899918726402049",
      "trade_time":1662174608295,
      "volume":"5417",
      "price":"1557.81",
      "direction":"4"
    },
    {
      "instrument_id":"ETHUSDTPERP",
      "trade_id":"1565899917015126017",
      "trade_time":1662174607887,
      "volume":"111",
      "price":"1557.80",
      "direction":"3"
    }
  ]
}
Cur Candle
Subscribe
event:cur_candle.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	cur_candle.subscribe
id	yes	number	auto-increment request id
granularity	yes	string	candle granularity: 1m 5m 15m 30m 1h 4h 12h 1d 1w
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument with granularity means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"cur_candle.subscribe",
  "id":1,
  "granularity": "1m",
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"cur_candle.subscribe",
  "id":1,
  "granularity": "1m",
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	cur_candle.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"cur_candle.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:cur_candle.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	cur_candle.unsubscribe
id	yes	number	auto-increment request id
granularity	yes	string	candle granularity: 1m 5m 15m 30m 1h 4h 12h 1d 1w
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
request example

{
  "event":"cur_candle.unsubscribe",
  "id":1,
  "granularity": "1m",
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"cur_candle.unsubscribe",
  "id":1,
  "granularity": "1m",
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	cur_candle.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"cur_candle.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	cur_candle.update
- data	object	response data
instrument_id	string	instrument id
granularity	string	candle granularity: 1m 5m 15m 30m 1h 4h 12h 1d 1w
- - candle	object	candle detail
0	number	milliseconds since UNIX epoch (candle start)
1	string	open price
2	string	highest price
3	string	lowest price
4	string	close price
5	string	trade volume
6	string	token trade num
push example

{
  "event":"cur_candle.update",
  "data":{
    "instrument_id":"ETHUSDTPERP",
    "granularity":"1m",
    "candle":[1662338160000,"1573.31","1574.18","1573.13","1574.18","10529","105.29"]
  }
}
Index Price
Subscribe
event:index_price.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	index_price.subscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"index_price.subscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"index_price.subscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	index_price.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"index_price.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:index_price.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	index_price.unsubscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
request example

{
  "event":"index_price.unsubscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"index_price.unsubscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	index_price.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"index_price.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	index_price.update
- data	object	response data
instrument_id	string	instrument id
index_price	string	instrument index price
timestamp	number	milliseconds since UNIX epoch
push example

{
  "event":"index_price.update",
  "data":{
    "instrument_id":"ETHUSDTPERP",
    "index_price":"1573.26",
    "timestamp":1662338890989
  }
}
Mark Price
Subscribe
event:mark_price.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	mark_price.subscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"mark_price.subscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"mark_price.subscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	mark_price.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"mark_price.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:mark_price.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	mark_price.unsubscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"mark_price.unsubscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"mark_price.unsubscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	mark_price.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"mark_price.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	mark_price.update
- data	object	response data
instrument_id	string	instrument id
index_price	string	instrument index price
timestamp	number	milliseconds since UNIX epoch
push example

{
  "event":"mark_price.update",
  "data":{
    "instrument_id":"ETHUSDTPERP",
    "mark_price":"1574.30",
    "timestamp":1662339184099
  }
}
Mark Candle
Subscribe
event:mark_candle.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	mark_candle.subscribe
id	yes	number	auto-increment request id
granularity	yes	string	candle granularity: 1m 5m 15m 30m 1h 4h 12h 1d 1w
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument with granularity means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"mark_candle.subscribe",
  "id":1,
  "granularity": "1m",
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"mark_candle.subscribe",
  "id":1,
  "granularity": "1m",
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	mark_candle.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"mark_candle.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:mark_candle.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	mark_candle.unsubscribe
id	yes	number	auto-increment request id
granularity	yes	string	candle granularity: 1m 5m 15m 30m 1h 4h 12h 1d 1w
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
request example

{
  "event":"mark_candle.unsubscribe",
  "id":1,
  "granularity": "1m",
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"mark_candle.unsubscribe",
  "id":1,
  "granularity": "1m",
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	mark_candle.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"mark_candle.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	cur_candle.update
- data	object	response data
instrument_id	string	instrument id
granularity	string	candle granularity: 1m 5m 15m 30m 1h 4h 12h 1d 1w
- - mark_candle	object	candle detail
0	number	milliseconds since UNIX epoch (candle start)
1	string	open price
2	string	highest price
3	string	lowest price
4	string	close price
5	string	trade volume
6	string	token trade num
push example

{
  "event":"mark_candle.update",
  "data":{
    "instrument_id":"ETHUSDTPERP",
    "granularity":"1m",
    "mark_candle":[1662338160000,"1573.31","1574.18","1573.13","1574.18"]
  }
}
Price Range
Subscribe
event:price_range.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	price_range.subscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"price_range.subscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"price_range.subscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	price_range.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"price_range.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:price_range.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	price_range.unsubscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"price_range.unsubscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"price_range.unsubscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	price_range.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"price_range.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	price_range.update
- data	object	response data
instrument_id	string	instrument id
highest	string	max buy price
lowest	string	min sell price
timestamp	number	milliseconds since UNIX epoch
push example

{
  "event":"price_range.update",
  "data":{
    "instrument_id":"ETHUSDTPERP",
    "highest":"1738.58",
    "lowest":"1422.43",
    "timestamp":1662339996916
  }
}
Fund Rate
Subscribe
event:fund_rate.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	fund_rate.subscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"fund_rate.subscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"fund_rate.subscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	fund_rate.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"fund_rate.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:fund_rate.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	fund_rate.unsubscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
request example

{
  "event":"fund_rate.unsubscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"fund_rate.unsubscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	fund_rate.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"fund_rate.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	fund_rate.update
- data	object	response data
instrument_id	string	instrument id
funding_rate	string	current funding rate
funding_time	number	settlement time,milliseconds since UNIX epoch
next_funding_rate	string	forecasted funding rate for the next period
next_funding_time	number	funding time for the next period, milliseconds since UNIX epoch
push example

{
  "event":"fund_rate.update",
  "data":{
    "instrument_id":"ETHUSDTPERP",
    "funding_rate":"-0.00007",
    "funding_time":1662364800000,
    "next_funding_rate":"-0.00010155724195205366",
    "next_funding_time":1662393600000
  }
}
Settle price
Subscribe
event:estimated_settle_price.subscribe

request param

Parameters	Required	Type	Description
event	yes	string	estimated_settle_price.subscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
 One single instrument means one public channel, a single connection can not subscribe over 30 public channels.
request example

{
  "event":"estimated_settle_price.subscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"estimated_settle_price.subscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	estimated_settle_price.subscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"estimated_settle_price.subscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
UnSubscribe
event:estimated_settle_price.unsubscribe

request param

Parameters	Required	Type	Description
event	yes	string	estimated_settle_price.unsubscribe
id	yes	number	auto-increment request id
instrument_id	options	string	instrument_id
instrument_ids	options	array	array of instrument_id. instrument_id and instrument_ids must not be both empty
request example

{
  "event":"estimated_settle_price.unsubscribe",
  "id":1,
  "instrument_id":"ETHUSDTPERP"
}
or

{
  "event":"estimated_settle_price.unsubscribe",
  "id":1,
  "instrument_ids":["BTCUSDTPERP","ETHUSDTPERP"]
}
response param

Parameters	Type	Description
event	string	estimated_settle_price.unsubscribe
id	number	auto-increment request id
code	number	see ErrorCode
msg	string	error msg
response example

{
  "event":"estimated_settle_price.unsubscribe",
  "id":1,
  "code":1,
  "msg":"success"
}
Push
push param

Parameters	Type	Description
event	string	estimated_settle_price.update
- data	object	response data
instrument_id	string	instrument id
estimated_settle_price	string	current funding rate
timestamp	number	milliseconds since UNIX epoch
push example

{
  "event":"estimated_settle_price.update",
  "data":{
    "instrument_id":"BTC2-MOVE-20220909",
    "estimated_settle_price":"175.3345",
    "timestamp":1662341408594
  }
}






