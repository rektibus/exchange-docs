Get public execution events
GET
https://futures.kraken.com/api/history/v3/market/:tradeable/executions
Lists trades for a market.

Request
Path Parameters
tradeable
string
required
Query Parameters
since
timestamp-milliseconds
Timestamp in milliseconds.

before
timestamp-milliseconds
Timestamp in milliseconds.

sort
string
Possible values: [asc, desc]

Determines the order of events in response(s).

asc = chronological
desc = reverse-chronological
Default value: desc
continuation_token
base64
Opaque token from the Next-Continuation-Token header used to continue listing events. The sort parameter must be the same as in the previous request to continue listing in the same direction.

count
int64
Possible values: >= 1

The maximum number of results to return. The upper bound is determined by a global limit.

Responses
200
Schema
Schema
len
integer<uint64>
required
elements
object[]
required
Array [
uid
string
required
timestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
event
object
required
Execution
object
required
execution
object
required
uid
string<uuid>
required
makerOrder
object
required
uid
string<uuid>
required
tradeable
string
required
direction
string
required
Possible values: [Buy, Sell]

quantity
string<decimal>
required
Example: 1234.56789
timestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
limitPrice
string<decimal>
required
Example: 1234.56789
orderType
string
required
reduceOnly
boolean
required
lastUpdateTimestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
takerOrder
object
required
uid
string<uuid>
required
tradeable
string
required
direction
string
required
Possible values: [Buy, Sell]

quantity
string<decimal>
required
Example: 1234.56789
timestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
limitPrice
string<decimal>
required
Example: 1234.56789
orderType
string
required
reduceOnly
boolean
required
lastUpdateTimestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
timestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
quantity
string<decimal>
required
Example: 1234.56789
price
string<decimal>
required
Example: 1234.56789
markPrice
string<decimal>
required
Example: 1234.56789
limitFilled
boolean
required
oldTakerOrder
object
uid
string<uuid>
required
tradeable
string
required
direction
string
required
Possible values: [Buy, Sell]

quantity
string<decimal>
required
Example: 1234.56789
timestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
limitPrice
string<decimal>
required
Example: 1234.56789
orderType
string
required
reduceOnly
boolean
required
lastUpdateTimestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
usdValue
string<decimal>
required
Example: 1234.56789
takerReducedQuantity
string
required
sometimes empty string

]
continuationToken
string<base64>
Opaque token to pass to the next request to continue listing events. The sort parameter must be the same as in the previous request to continue listing in the same direction.

curl
python
go
nodejs
CURL
curl -L 'https://futures.kraken.com/api/history/v3/market/:tradeable/executions' \
-H 'Accept: application/json'



Request
Collapse all
Base URL
https://futures.kraken.com/api/history/v3
Parameters
tradeable — pathrequired
tradeable
Build URL



Get public order events
GET
https://futures.kraken.com/api/history/v3/market/:tradeable/orders
Lists order events for a market.

Request
Path Parameters
tradeable
string
required
Query Parameters
since
timestamp-milliseconds
Timestamp in milliseconds.

before
timestamp-milliseconds
Timestamp in milliseconds.

sort
string
Possible values: [asc, desc]

Determines the order of events in response(s).

asc = chronological
desc = reverse-chronological
Default value: desc
continuation_token
base64
Opaque token from the Next-Continuation-Token header used to continue listing events. The sort parameter must be the same as in the previous request to continue listing in the same direction.

count
int64
Possible values: >= 1

The maximum number of results to return. The upper bound is determined by a global limit.

Responses
200
Schema
Schema
len
integer<uint64>
required
elements
object[]
required
Array [
uid
string
required
timestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
event
object
required
oneOf
MOD1
MOD2
MOD3
OrderPlaced
object
required
order
object
required
uid
string<uuid>
required
tradeable
string
required
direction
string
required
Possible values: [Buy, Sell]

quantity
string<decimal>
required
Example: 1234.56789
timestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
limitPrice
string<decimal>
required
Example: 1234.56789
orderType
string
required
reduceOnly
boolean
required
lastUpdateTimestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
reason
string
required
reducedQuantity
string
required
always empty string

]
continuationToken
string<base64>
Opaque token to pass to the next request to continue listing events. The sort parameter must be the same as in the previous request to continue listing in the same direction.

curl
python
go
nodejs
CURL
curl -L 'https://futures.kraken.com/api/history/v3/market/:tradeable/orders' \
-H 'Accept: application/json'



Request
Collapse all
Base URL
https://futures.kraken.com/api/history/v3
Parameters
tradeable — pathrequired
tradeable
Build URL


Get public mark price events
GET
https://futures.kraken.com/api/history/v3/market/:tradeable/price
Lists price events for a market.

Request
Path Parameters
tradeable
string
required
Query Parameters
since
timestamp-milliseconds
Timestamp in milliseconds.

before
timestamp-milliseconds
Timestamp in milliseconds.

sort
string
Possible values: [asc, desc]

Determines the order of events in response(s).

asc = chronological
desc = reverse-chronological
Default value: desc
continuation_token
base64
Opaque token from the Next-Continuation-Token header used to continue listing events. The sort parameter must be the same as in the previous request to continue listing in the same direction.

count
int64
Possible values: >= 1

The maximum number of results to return. The upper bound is determined by a global limit.

Responses
200
Schema
Schema
len
integer<uint64>
required
elements
object[]
required
Array [
uid
string
required
timestamp
integer<timestamp-milliseconds>
required
Example: 1604937694000
event
object
required
price
string<decimal>
required
Example: 1234.56789
]
continuationToken
string<base64>
Opaque token to pass to the next request to continue listing events. The sort parameter must be the same as in the previous request to continue listing in the same direction.

curl
python
go
nodejs
CURL
curl -L 'https://futures.kraken.com/api/history/v3/market/:tradeable/price' \
-H 'Accept: application/json'



Request
Collapse all
Base URL
https://futures.kraken.com/api/history/v3
Parameters
tradeable — pathrequired
tradeable
Build URL



Tick Types
GET
https://futures.kraken.com/api/charts/v1/
Returns all available tick types to use with the markets endpoint.

Responses
200
Tick types list

Schema
Schema
Array [
Tick Types (string)
Possible values: [spot, mark, trade]

]
curl
python
go
nodejs
CURL
curl -L 'https://futures.kraken.com/api/charts/v1/' \
-H 'Accept: application/json'


Request
Collapse all
Base URL
https://futures.kraken.com/api/charts/v1
Send API Request
Response
Clear
200
Headers
[
  "mark",
  "spot",
  "trade"
]


Previous
Candles


Markets
GET
https://futures.kraken.com/api/charts/v1/:tick_type
Markets available for specified tick type.

List of available tick types can be fetched from the tick types endpoint.

Request
Path Parameters
tick_type
Tick Types
required
Possible values: [spot, mark, trade]

Responses
200
Markets list

Schema
Example
Schema
Array [
string
]
curl
python
go
nodejs
CURL
curl -L 'https://futures.kraken.com/api/charts/v1/:tick_type' \
-H 'Accept: application/json'



Request
Collapse all
Base URL
https://futures.kraken.com/api/charts/v1
Parameters
tick_type — pathrequired

---
This field is required
Send API Request
Response
Clear
Click the Send API Request button above and see the response here!



Resolutions
GET
https://futures.kraken.com/api/charts/v1/:tick_type/:symbol
Candle resolutions available for specified tick type and market.

List of available tick types can be fetched from the tick types endpoint. List of available markets can be fetched from the markets endpoint.

Request
Path Parameters
tick_type
Tick Types
required
Possible values: [spot, mark, trade]

symbol
string
required
Market symbol

Responses
200
All resolutions for the given tick_type and symbol

Schema
Schema
Array [
Resolution (string)
Possible values: [1m, 5m, 15m, 30m, 1h, 4h, 12h, 1d, 1w]

]
curl
python
go
nodejs
CURL
curl -L 'https://futures.kraken.com/api/charts/v1/:tick_type/:symbol' \
-H 'Accept: application/json'



Request
Collapse all
Base URL
https://futures.kraken.com/api/charts/v1
Parameters
tick_type — pathrequired

---
This field is required
symbol — pathrequired
Market symbol
This field is required
Send API Request
Response
Clear
Click the Send API Request button above and see the response here!



Market Candles
GET
https://futures.kraken.com/api/charts/v1/:tick_type/:symbol/:resolution
Candles for specified tick type, market, and resolution.

List of available tick types can be fetched from the tick types endpoint. List of available markets can be fetched from the markets endpoint. List of available resolutions can be fetched from the resolutions endpoint.

Request
Path Parameters
tick_type
Tick Types
required
Possible values: [spot, mark, trade]

symbol
string
required
Market symbol

resolution
Resolution
required
Possible values: [1m, 5m, 15m, 30m, 1h, 4h, 12h, 1d, 1w]

Query Parameters
from
number
From date in epoch seconds

to
number
To date in epoch seconds

count
integer
Possible values: >= 0

Number of candles to return.

Responses
200
OHLC candles

Schema
Schema
candles
object[]
required
OHLC candles

Array [
time
integer<int64>
required
Epoch in ms

Example: 1620816960000
high
string<big-decimal>
required
Example: 56475.00000000000
low
string<big-decimal>
required
Example: 55935.00000000000
open
string<big-decimal>
required
Example: 56294.00000000000
close
string<big-decimal>
required
Example: 56250.00000000000
volume
number<int64>
required
Example: 10824
]
more_candles
boolean
required
True if there are more candles in time range

curl
python
go
nodejs
CURL
curl -L 'https://futures.kraken.com/api/charts/v1/:tick_type/:symbol/:resolution' \
-H 'Accept: application/json'



Request
Collapse all
Base URL
https://futures.kraken.com/api/charts/v1
Parameters
tick_type — pathrequired

---
This field is required
symbol — pathrequired
Market symbol
This field is required
resolution — pathrequired

---
This field is required
Send API RequestBuild URL
Response
Clear
Click the Send API Request button above and see the response here!



Get liquidity pool statistic
GET
https://futures.kraken.com/api/charts/v1/analytics/liquidity-pool
Get liquidity pool statistic including usd value

Request
Query Parameters
since
int64
required
epoch time in seconds

interval
Resolution in seconds
required
Possible values: [60, 300, 900, 1800, 3600, 14400, 43200, 86400, 604800]

to
integer
epoch time in seconds, default now

Responses
200
400
404
Available analytics by type and symbol

Schema
Schema
result
object
required
timestamp
integer[]
required
more
boolean
required
True if there are more candles in time range

data
object
required
oneOf

MOD1
Statistic of long and short positions
Orderbook analytics data
AnalyticsCvdData
AnalyticsTopTradersData
AnalyticsLiquidityPoolData
AnalyticsFutureBasisData

Array [
oneOf
MOD1
MOD2
Ohlc
number
]
errors
object[]
required
Array [
severity
string
required
error_class
string
required
type
string
required
msg
string
value
string
field
string
]
curl
python
go
nodejs
CURL
curl -L 'https://futures.kraken.com/api/charts/v1/analytics/liquidity-pool' \
-H 'Accept: application/json'



Request
Collapse all
Base URL
https://futures.kraken.com/api/charts/v1
Parameters
since — queryrequired
epoch time in seconds
interval — queryrequired

---
Send API RequestBuild URL
Response
Clear
Click the Send API Request button above and see the response here!




Market Analytics
GET
https://futures.kraken.com/api/charts/v1/analytics/:symbol/:analytics_type
Analytics data divided into time buckets

Request
Path Parameters
symbol
string
required
Market symbol

analytics_type
Type of analytics
required
Possible values: [open-interest, aggressor-differential, trade-volume, trade-count, liquidation-volume, rolling-volatility, long-short-ratio, long-short-info, cvd, top-traders, orderbook, spreads, liquidity, slippage, future-basis]

Query Parameters
since
int64
required
epoch time in seconds

interval
Resolution in seconds
required
Possible values: [60, 300, 900, 1800, 3600, 14400, 43200, 86400, 604800]

to
integer
epoch time in seconds, default now

Responses
200
400
404
Available analytics by type and symbol

Schema
Schema
result
object
required
timestamp
integer[]
required
more
boolean
required
True if there are more candles in time range

data
object
required
oneOf

MOD1
Statistic of long and short positions
Orderbook analytics data
AnalyticsCvdData
AnalyticsTopTradersData
AnalyticsLiquidityPoolData
AnalyticsFutureBasisData

Array [
oneOf
MOD1
MOD2
Ohlc
number
]
errors
object[]
required
Array [
severity
string
required
error_class
string
required
type
string
required
msg
string
value
string
field
string
]
curl
python
go
nodejs
CURL
curl -L 'https://futures.kraken.com/api/charts/v1/analytics/:symbol/:analytics_type' \
-H 'Accept: application/json'



Request
Collapse all
Base URL
https://futures.kraken.com/api/charts/v1
Parameters
symbol — pathrequired
Market symbol
This field is required
analytics_type — pathrequired

---
This field is required
since — queryrequired
epoch time in seconds
This field is required
interval — queryrequired

---
This field is required
Send API RequestBuild URL
Response
Clear
Click the Send API Request button above and see the response here!

Previous
Get liquidity pool statistic
Next
Auth