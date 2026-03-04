#Introduction

We designed our zondacrypto API to provide our users with a convenient interface allowing access to service database, fetching data and performing various operations on third-party software. API allows users to create dynamic charts for various markets and to design autonomous trading apps.
If you by any chance have noticed an error while using API documentation or you would like to share with us your ideas and suggestions regarding new functionalities or future upgrades, please contact us using our Contact form.

The API is available under the following link: https://api.zondacrypto.exchange/rest

Calling a given method, e.g. ticker (method to be explained in more detail in further paragraphs) looks as follows: https://api.zondacrypto.exchange/rest/trading/ticker

All time format data returned by API follows UNIX timestamp format with milisecond precision.
Every request must contains Content-type: application/json header.

Responses return status code “200 OK”, therefore each method returns it’s execution status.
In case of failed execution, method returns status “Fail” and appropriate error message.

In order to offer the best service, operations are limited by the number of queries available per minute.

Action

Max. number of queries per minute

Place order

200

Cancel order

200

Get the list of placed order

200

Get list of transactions

100

Get market configuration

100

Change market configuration

20

Exchange on FIAT Cantor

30

Get FIAT Cantor history

30

Get FIAT Cantor rates

70

Others

60

Error messages
In case of unsuccessful request execution a Fail status will be returned along with appropriate error message. List of common error messages is presented below; those not listed are related to specific method category which they are part of.

Error message

Description

PERMISSIONS_NOT_SUFFICIENT

API Key permissions are not sufficient to perform given action.

INVALID_HASH_SIGNATURE

API-Hash signature is not valid.

RESPONSE_TIMEOUT

Response time was exceeded.

TIMEOUT

Invalid: parameters / request type / path.

ACTION_BLOCKED

Action was blocked on user account.

ACTION_LIMIT_EXCEEDED

Action limit was exceeded. You need to wait one minute before making another request.

UNDER_MAINTENANCE

The exchange is currently under maintenance. You will get also additional field: estimatedTime in Unix Timestamp and it is the time when works will be done.

Ticker
get
https://api.zondacrypto.exchange/rest/trading/ticker/{trading_pair}


The Ticker provides a general overview of the configuration and statistics of all markets or just a selected one - to do this, simply add the market code in the address. It shows the value of the smallest transaction we can make and the precision of the amount, rate and price. The precision of the amount (amountPrecision) determines how accurately we can determine the quantity of the first currency to buy or sell, the precision of the price (pricePrecision) determines the number of decimal places to which the result of our transaction will be rounded or how accurately we can determine the quantity of the second currency, the precision of the rate (ratePrecision) determines the number of decimal places of the rate with which we want to place an offer. Rate precision can vary over time depending on the exchange rate for a particular currency market. The precisions of amount (amountPrecision) and price (pricePrecision) stay unchanged. The Ticker also returns the current best bid and ask, as well as the last and the previous transaction price.

Path Params	
trading_pair
string
Optional: symbol of trading pair you want information about.

BTC-PLN
📘
If you want to get information from specific market just use below path:
https://api.zondacrypto.exchange/rest/trading/ticker/BTC-PLN
Response details

Key

Type

Description

ticker

array

code

string

Currency pair for request

amountPrecision

integer

Number of decimal places of the first currency.

pricePrecision

integer

Number of decimal places of the transaction price or second currency.

ratePrecision

integer

Number of decimal places of the rate.

first / second

array

Arrays of data from first and second currency pair

currency
string

Currency shortcut

minOffer
decimal

Minimal value of currency that you can provide to order

scale
integer

Decimal precision

This field will be removed in the future.

time

Unix Timestamp

Time of execute on server. For this time all values are actual

highestBid

decimal

The best price of buy order at the moment

lowestAsk

decimal

The best price of sell order at the moment

rate

decimal

Rate of the last transaction

previousRate

decimal

Rate of the penultimate transaction.

Response

200
200

Response body

object

Fail

Market statistics
get
https://api.zondacrypto.exchange/rest/trading/stats/{trading_pair}


This method shows market statistics from last 24 hours: highest/lowest order and volume. Applies to selected market or all markets if market code parameter is left blank.

Path Params	
trading_pair
string
Optional: symbol of trading pair you want information about.

BTC-PLN
📘
If you want to get information from specific market just use below path:
https://api.zondacrypto.exchange/rest/trading/stats/BTC-PLN
Response details

Key

Type

Description

stats

array

m
string

Currency pair of the market

h
decimal

Highest rate of the last 24 hours

l
decimal

Lowest rate of the last 24 hours

v
decimal

Volume of the last 24 hours

r24h
decimal

Opening rate of the 24-hour time window.

Response

200
200

Response body

object

Fail
object
status
string
errors
array of strings
Updated 9 months ago

Ticker
Orderbook
Language

JavaScript

Ruby

Python

PHP
Request
composer require guzzlehttp/guzzle
1
<?php
2
require_once('vendor/autoload.php');
3
​
4
$client = new \GuzzleHttp\Client();
5
​
6
$response = $client->request('GET', 'https://api.zondacrypto.exchange/rest/trading/stats/trading_pair', [
7
  'headers' => [
8
    'accept' => 'application/json',
9
  ],
10
]);
11
​
12
echo $response->getBody();


1
{
2
  "status": "Ok",
3
  "stats": {
4
    "m": "BTC-PLN",
5
    "h": "32841.02",
6
    "l": "31173.99",
7
    "v": "2538.53749287",
8
    "r24h": "31155.76"
9
  }
10
}

Orderbook
get
https://api.zondacrypto.exchange/rest/trading/orderbook/{trading_pair}


Returns 300 of highest bid orders and 300 of lowest ask orders.

Response details

Key

Type

Description

sell / buy

array

ra
decimal

Rate of the order

ca
decimal

Current amount of cryptocurrency in the order

sa
decimal

Starting amount of cryptocurrency in the order

pa
decimal

Amount of cryptocurrency before the last change

co
integer

Amount of orders in the position at specific rate

timestamp

Unix Timestamp

Time of execution on server. For this time all above values are actual

seqNo

integer

Sequence number. Allows you to keep the order of received data.

Path Params
trading_pair
string
required
Defaults to BTC-PLN
Symbol of trading pair you want information about.

BTC-PLN
Response

200
200

Response body

object

Fail
Updated 9 months ago

Market statistics
Orderbook limited
Language

JavaScript

Ruby

Python

PHP
Request
composer require guzzlehttp/guzzle
1
<?php
2
require_once('vendor/autoload.php');
3
​
4
$client = new \GuzzleHttp\Client();
5
​
6
$response = $client->request('GET', 'https://api.zondacrypto.exchange/rest/trading/orderbook/BTC-PLN', [
7
  'headers' => [
8
    'accept' => 'application/json',
9
  ],
10
]);
11
​
12
echo $response->getBody();


1
{
2
  "status": "Ok",
3
  "sell": [
4
    {
5
      "ra": "25285.31",
6
      "ca": "0.02839638",
7
      "sa": "0.02839638",
8
      "pa": "0.02839638",
9
      "co": 1
10
    }
11
  ],
12
  "buy": [
13
    {
14
      "ra": "25280",
15
      "ca": "0.82618498",
16
      "sa": "3.59999",
17
      "pa": "0.82618498",
18
      "co": 1
19
    }
20
  ],
21
  "timestamp": "1529512856512",
22
  "seqNo": "139098"
23
}



Orderbook limited
get
https://api.zondacrypto.exchange/rest/trading/orderbook-limited/{trading_pair}/{limit}


Returns 10 / 50 / 100 of the highest bid orders and the lowest ask orders.

Response details

Key

Type

Description

sell / buy

array

ra
decimal

Rate of the order

ca
decimal

Current amount of cryptocurrency in the order

sa
decimal

Starting amount of cryptocurrency in the order

pa
decimal

Amount of cryptocurrency before the last change

co
integer

Amount of orders in the position at specific rate

timestamp

Unix Timestamp

Time of execution on server. For this time all above values are actual

seqNo

integer

Sequence number. Allows you to keep the order of received data.

Path Params
trading_pair
string
required
Defaults to BTC-PLN
Symbol of trading pair you want information about.

BTC-PLN
limit
int32
required
Limit of records. Available values: 10 / 50 / 100.

Response

200
200

Response body

object

Fail
object
status
string
errors
array of strings
Updated 9 months ago

Orderbook
Last transactions
Language

JavaScript

Ruby

Python

PHP
Request
composer require guzzlehttp/guzzle
1
<?php
2
require_once('vendor/autoload.php');
3
​
4
$client = new \GuzzleHttp\Client();
5
​
6
$response = $client->request('GET', 'https://api.zondacrypto.exchange/rest/trading/orderbook-limited/BTC-PLN/limit', [
7
  'headers' => [
8
    'accept' => 'application/json',
9
  ],
10
]);
11
​
12
echo $response->getBody();


1
{
2
  "status": "Ok",
3
  "sell": [
4
    {
5
      "ra": "25285.31",
6
      "ca": "0.02839638",
7
      "sa": "0.02839638",
8
      "pa": "0.02839638",
9
      "co": 1
10
    }
11
  ],
12
  "buy": [
13
    {
14
      "ra": "25280",
15
      "ca": "0.82618498",
16
      "sa": "3.59999",
17
      "pa": "0.82618498",
18
      "co": 1
19
    }
20
  ],
21
  "timestamp": "1529512856512",
22
  "seqNo": "139098"
23
}



Last transactions
get
https://api.zondacrypto.exchange/rest/trading/transactions/{trading_pair}


Shows the list of most recent transactions for given market. By default returns list of 10 most recent transactions.

Response details

Key

Type

Description

items

array

id
UUID

UUID of transaction

t
Unix Timestamp

Transaction time

a
decimal

Amount of cryptocurrency in the transaction

r
decimal

Rate of the transaction

ty
string

Transaction type: buy / sell

Path Params
trading_pair
string
required
Defaults to BTC-PLN
Symbol of trading pair you want information about.

BTC-PLN
Query Params
limit
int32
Limit of requested transactions. Maximum: 300.

fromTime
date-time
Time from transactions will be get.

sort
string
Defaults to desc
Sort the query results

desc
Response

200
200

Response body

object

Fail
Updated 9 months ago

Orderbook limited
Candlestick chart
Language

JavaScript

Ruby

Python

PHP
Request
composer require guzzlehttp/guzzle
1
<?php
2
require_once('vendor/autoload.php');
3
​
4
$client = new \GuzzleHttp\Client();
5
​
6
$response = $client->request('GET', 'https://api.zondacrypto.exchange/rest/trading/transactions/BTC-PLN', [
7
  'headers' => [
8
    'accept' => 'application/json',
9
  ],
10
]);
11
​
12
echo $response->getBody();


1
{
2
  "status": "Ok",
3
  "items": [
4
    {
5
      "id": "f9ff807c-ec8d-4654-b12a-aa3f6fdcf94c",
6
      "t": "1529515852759",
7
      "a": "0.04016101",
8
      "r": "25111.14",
9
      "ty": "Sell"
10
    },
11
    {
12
      "id": "952d5907-f6db-4fc1-a01a-d39371233115",
13
      "t": "1529515819014",
14
      "a": "0.01491232",
15
      "r": "25147",
16
      "ty": "Buy"
17
    }
18
  ]
19
}


Candlestick chart
get
https://api.zondacrypto.exchange/rest/trading/candle/history/{trading_pair}/{resolution}


Returns candle statistics for user defined time parameters.

Available resolutions:

Resolution

Value

1 minute

60

3 minutes

180

5 minutes

300

15 minutes

900

30 minutes

1800

1 hour

3600

2 hours

7200

4 hours

14400

6 hours

21600

12 hours

43200

1 day

86400

3 days

259200

1 week

604800

Response details

Key

Type

Description

timestamp (ms)

Time of candle generation

o

decimal

Opening price

c

decimal

Closing price

h

decimal

Highest price

l

decimal

Lowest price

v

decimal

Volume

Path Params
trading_pair
string
required
Defaults to BTC-PLN
Symbol of trading pair you want information about.

BTC-PLN
resolution
int32
required
Size of single candle (in seconds). You can find a list of available resolutions below.

Query Params
from
date-time
Get candles from specific time (milliseconds timestamp)

to
date-time
Get candles to specific time (milliseconds timestamp)

Response

200
200

Response body

object

Fail
Updated 9 months ago

Last transactions
Authentication
Language

JavaScript

Ruby

Python

PHP
Request
composer require guzzlehttp/guzzle
1
<?php
2
require_once('vendor/autoload.php');
3
​
4
$client = new \GuzzleHttp\Client();
5
​
6
$response = $client->request('GET', 'https://api.zondacrypto.exchange/rest/trading/candle/history/BTC-PLN/resolution', [
7
  'headers' => [
8
    'accept' => 'application/json',
9
  ],
10
]);
11
​
12
echo $response->getBody();


1
{
2
  "status": "Ok",
3
  "items": [
4
    [
5
      "1530742800000",
6
      {
7
        "o": "25045.87",
8
        "c": "25046.03",
9
        "h": "25130.93",
10
        "l": "25043.59",
11
        "v": "0.22349329"
12
      }
13
    ],
14
    [
15
      "1530743100000",
16
      {
17
        "o": "25003.51",
18
        "c": "25125",
19
        "h": "25125",
20
        "l": "24960.81",
21
        "v": "0.15407649"
22
      }
23
    ]
24
  ]
25
}










Subscription
🚧
ConnectionClosed
We are using external proxy service called CloudFlare. To deliver best and reliable services our provider is changing routing policy few times per day. This might cause instantaneous lost of connection on WebSocket channel. We recommend to consider and solve such situations at the beginning of developing own application.

📘
Secured Websocket URI:
wss://api.zondacrypto.exchange/websocket/
To perform a public subscription, you need to send: action subscribe-public, module and path to endpoint. Required format is JSON. This type of connection do not require any additional parameters.
To cancell subscription - just send action unsubscribe with previous module and path. This will close all active channels.

Subscribe
Unsubscribe

{
 "action": "subscribe-public",
 "module": "trading",
 "path": "ticker"
}
Response details
The first response will always return confirmation of subscription for specific channel. Each subsequent one is called push which contains target data.

Example push
Subscribe confirm

{
  "action": "push",
  "topic": "trading/orderbook/btc-pln",
  "message": {
    "changes": [
      {
        "marketCode": "BTC-PLN",
        "entryType": "Buy",
        "rate": "27601.35",
        "action": "update",
        "state": {
          "ra": "27601.35",
          "ca": "0.46205049",
          "sa": "0.46205049",
          "pa": "0.46205049",
          "co": 4
        }
      }
    ],
    "timestamp": "1576847016253"
  },
  "timestamp": "1576847016253",
  "seqNo": 40018807
}
Parameters action, topic, message, timestamp and seqNo are returned for each channel.

📘
Implementation example of the seqNo
To keep the order of receiving pushes and data consistency should be implemented the following mechanism:

Connect to the channel and save every push on temporary list.
Get the current snapshot of previous connected channel and save whole response to the target structure.
Update structure with temporary list, starting with 1 value greater of seqNo than downloaded snapshot.
For each update - check if seqNo is 1 more greater than previous message and clear temporary list after each successful update on structure.
If temporary list will not be clearing it will be the fault of lost push and need to repeat the whole process from the beginning.
Values of the seqNo are individual for each limits: 10 / 50 / 100 and are consistent for snapshot and websocket channel.

Key

Type

Description

action

String

Type of action: push / subscribe-public-error / subscribe-private-error / subscribe-private-confirm / subscribe-public-confirm / proxy-response / pong / json-error.

topic

String

Full path of current channel.

message

Object

Push message with changes.
Different for each of channel.

timestamp

Unix Timestamp

Time of update on server side.

seqNo

integer

Sequence number. Helps keep the order.

Snapshot
All of the presented public endpoints allows to catch a snapshot.
It is performed by action proxy to REST API endpoint. All of the REST API endpoints of type GET could be snapshotted. In this type of request you need to sent additional parameter: requestID, which is disposable UUID of the request.

Snapshot
Result

{
	"requestId": "78539fe0-e9b0-4e4e-8c86-70b36aa93d4f",
	"action": "proxy",
	"module": "trading",
	"path": "ticker/eth-pln"
}




Ping
Using this one you can implement a heartbeat system to check if the connection is still alive.

Request
Response

{
  "action": "ping"
}


Approximate rate
Subscription informs you of changes in the approximate rate for a given currency pair.

Request
Push

{
 "action": "subscribe-public",
 "module": "cantor_service",
 "path": "rates/{source_currency}/{destination_currrency}"
}
Response details:

Key

Type

Description

rate

decimal

Approximate rate.

rateCurrency

string

Currency rate.



Ticker
The subscription shows the general setup and statistics of the market. It shows the value of the smallest transaction we can make and the precision of the amount, rate and price. The precision of the amount (amountPrecision) determines how accurately we can determine the quantity of the first currency to buy or sell, the precision of the price (pricePrecision) determines the number of decimal places to which the result of our transaction will be rounded or how accurately we can determine the quantity of the second currency, the precision of the rate (ratePrecision) determines the number of decimal places of the rate with which we want to place an offer. Rate precision can vary over time depending on the exchange rate for a particular currency market. The precisions of amount (amountPrecision) and price (pricePrecision) stay unchanged. The Ticker also returns the current best bid and ask, as well as the last and the previous transaction price.

📘
If you want to get information from all markets just use path without market symbol:
"path": "ticker"
Request
Push
Snapshot
Proxy response

{
 "action": "subscribe-public",
 "module": "trading",
 "path": "ticker/{market_code}"
}
Response details:

Key

Type

Description

ticker

array

code

string

Currency pair for request.

amountPrecision

integer

Number of decimal places of the first currency.

pricePrecision

integer

Number of decimal places of the transaction price or second currency.

ratePrecision

integer

Number of decimal places of the rate.

first / second

array

Arrays of data from first and second currency pair.

currency
string

Currency symbol.

minOffer
decimal

Minimal value of currency that you could order.

scale
integer

Decimal precision.

This field will be removed in the future.

time

Unix Timestamp

Time of execute on server. For this time all values are actual.

highestBid

decimal

The best price for buy order at the moment.

lowestAsk

decimal

The best price for sell order at the moment.

rate

decimal

Price of the last transaction.

previousRate

decimal

Price of the penultimate transaction.



Market statistics
This subscription is updating market statistics from last 24 hours: highest/lowest order and volume. Applies to selected market or all markets if market code parameter is left blank.

📘
If you want to get information from all markets just use path without market symbol:
"path": "stats"
Request
Push
Snapshot
Proxy response

{
 "action": "subscribe-public",
 "module": "trading",
 "path": "stats/{market_code}"
}
Response details

Key

Type

Description

stats

array

m

string

Currency pair of the market.

h

decimal

Highest price of the last 24 hours.

l

decimal

Lowest price of the last 24 hours.

v

decimal

Volume of the last 24 hours.

r24h

decimal

Average rate of the last 24 hours.


Orderbook
Updates of orders from orderbook.

Request
Push
Snapshot
Proxy response

{
 "action": "subscribe-public",
 "module": "trading",
 "path": "orderbook/{market_code}"
}
Response details

Key

Type

Description

changes

array

mmarketCode

string

Symbol of the market.

entryType

string

Order type: buy / sell.

rate

decimal

Price of the order.

action

string

Type of change: remove / update. If update will occur you are going to get additional array of state.

state

array

Optional array for active orders.

ra
decimal

Price of the order.

ca
decimal

Current amount of cryptocurrency in the order.

sa
decimal

Starting amount of cryptocurrency in the order.

pa
decimal

Amount of cryptocurrency before the last change.

co
decimal

Amount of orders in the order.

timestamp

Unix Timestamp

Time of execute on server. For this time all above values are actual.


Orderbook limited
Updates of first 10 / 50 / 100 orders from orderbook. If one of order will be deleted - the push with existing order will be send to keep constant limit of orders on user's side.

Request
Push
Snapshot
Proxy response

{
  "action": "subscribe-public",
  "module": "trading",
  "path": "orderbook-limited/{market_code}/{limit}"
}
📘
Implementation example
To keep the order of receiving pushes and data consistency should be implemented the following mechanism:

Connect to the channel and save every push on temporary list.
Get the current snapshot of previous connected channel and save whole response to the target structure.
Update structure with temporary list, starting with 1 value greater of seqNo than downloaded snapshot.
For each update - check if seqNo is 1 more greater than previous message and clear temporary list after each successful update on structure.
If temporary list will not be clearing it will be the fault of lost push and need to repeat the whole process from the beginning.
Values of the seqNo are individual for each limits: 10 / 50 / 100 and are consistent for snapshot and websocket channel.

Response details

Key

Type

Description

changes

array

mmarketCode

string

Symbol of the market.

entryType

string

Order type: buy / sell.

rate

decimal

Price of the order.

action

string

Type of change: remove / update. If update will occur you are going to get additional array of state.

state

array

Optional array for active orders.

ra
decimal

Price of the order.

ca
decimal

Current amount of cryptocurrency in the order.

sa
decimal

Starting amount of cryptocurrency in the order.

pa
decimal

Amount of cryptocurrency before the last change.

co
decimal

Amount of orders in the order.

timestamp

Unix Timestamp

Time of execute on server. For this time all above values are actual.



Last transactions
Get current transactions.

Zapytanie
Push
Snapshot
Proxy response

{
 "action": "subscribe-public",
 "module": "trading",
 "path": "transactions/{market_code}"
}
Response details

Key

Type

Description

items

array

id

UUID

UUID of transaction.

t

Unix Timestamp

Transaction time.

a

decimal

Amount of cryptocurrency in the transaction.

r

decimal

Price of the transaction.

ty

string

Transaction type: buy / sell.