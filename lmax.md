AX Digital
Broker
Service
Target IP Port Targ
et
URL/
IP
Port
FIX 4.4 Order
placement
185.122.246.
1
5000
0
fix-order.london-digital.lmax.com 443
FIX 4.4 Market Data 185.122.246.
2
5000
0
fix-marketdata.londondigital.lmax.com
443
Web based API 185.122.246.
5
443 web-api.london-digital.lmax.com 443
Web based trading
UI
185.122.246.
5
443 web-order.london-digital.lmax.com 443
5.1.2 LMAX Digital Exchange Services
London
Professional
LMAX
Proximity
Public
Intern
et
LMAX Digital
Exchang
e Service
Target IP Port Target
URL/I
P
Port
Prime Broker Portal N/A N/A mtf-primebroker.londondigital.lmax.com
443
FIX 4.2 Market Data 185.122.246.
4
5200
0
mtf-marketdata.londondigital.lmax.com
443
FIX 4.2 Order
placement
185.122.246.
0
5000
0
mtf-order.london-digital.lmax.com 443
FIX 4.4 Trade
Reporting
185.122.246.
3
5000
0
mtf-dropcopy.londondigital.lmax.com
443







Public Data API (0.1)
Open API Specification Download

Introduction
The Public Data API is a freely available API that provides instrument information and prices from the exchange. This API reference provides information on the available REST endpoints and websocket connectivity.

API Changes
The API may undergo incremental changes and any code consuming this API should be developed to accept:

the addition of new API endpoints
the addition of optional parameters to existing API requests
the addition of fields to existing API responses
Connection details
The Public Data API is available at the following endpoints:

Demo Environment
https://public-data-api.london-demo.lmax.com

LMAX Digital
https://public-data-api.london-digital.lmax.com

Rate Limiting
One HTTP(S) request per IP address will be allowed per second. Exceeding the limit will result in subsequent requests being rejected with a 429 status code for up to 1 hour.

Price Updates
Price data provided by the ticker rest endpoint and websocket subscription are limited to one update per second, for each order book.

API Responses
The responses to our REST and WebSocket APIs conform to the JSON specification.

HTTP status codes are used to indicate success / failure

2xx : success
4xx : client error
5xx : server error
Error responses will include a message:

{
    "error_message": "Not found"
}
The API returns numeric values with a scale of:

6 digits to the right of the decimal point for prices;
5 digits to the right of the decimal point for costs;
4 digits to the right of the decimal point for quantities;
2 digits to the right of the decimal point for basis points.
REST Endpoints
REST endpoints are available for instrument reference data and order book pricing

Get Order Book

get
/v1/orderbook/{instrument_id}
Get prices for a requested instrument currently on the platform. The prices are updated once per second. Once a day, most of our instruments close for 5 minutes. A closing price is determined at this time and this will be reflected in the price until the instrument reopens.

path Parameters
instrument_id
required
string
Example: eur-usd
Instrument identifier

Responses
200 Order book snapshot
404 Instrument not found
503 The service is currently unavailable
Request samples
curl

Copy
curl -i -X GET "https://public-data-api.london-demo.lmax.com/v1/orderbook/eur-usd"
Response samples
200404503
Content type
application/json

Copy
Expand allCollapse all
{
"instrument_id": "eur-usd",
"timestamp": "2024-10-13T22:53:26.748Z",
"status": "OPEN",
"bids": [
{
"price": "1.181060",
"quantity": "500000.0000"
},
{
"price": "1.181050",
"quantity": "200000.0000"
}
],
"asks": [
{
"price": "1.181100",
"quantity": "250000.0000"
},
{
"price": "1.181110",
"quantity": "350000.0000"
}
]
}
Get Ticker

get
/v1/ticker/{instrument_id}
Get the latest ticker information for an instrument.

path Parameters
instrument_id
required
string
Example: eur-usd
Instrument identifier

Responses
200 Ticker
204 No ticker information available
404 Instrument not found
503 The service is currently unavailable
Request samples
curl

Copy
curl -i -X GET "https://public-data-api.london-demo.lmax.com/v1/ticker/eur-usd"
Response samples
200404503
Content type
application/json

Copy
{
"instrument_id": "eur-usd",
"timestamp": "2024-10-13T22:53:26.748Z",
"best_bid": "1.180970",
"best_ask": "1.181010",
"trade_id": "0B5WMAAAAAAAAAAS",
"last_quantity": "1000.0000",
"last_price": "1.180970",
"session_open": "1.181070",
"session_low": "1.180590",
"session_high": "1.181390"
}
Current time

get
/v1/time
Get current time.

Responses
200 Current time
Request samples
curl

Copy
curl -i -X GET "https://public-data-api.london-demo.lmax.com/v1/time"
Response samples
200
Content type
application/json

Copy
{
"epoch_millis": "1728860006748",
"timestamp": "2024-10-13T22:53:26.748Z"
}
Get Instrument

get
/v1/instruments/{instrument_id}
Get a requested instrument currently available on the platform.

path Parameters
instrument_id
required
string
Example: eur-usd
Instrument identifier

Responses
200 Instrument
404 Instrument not found
503 The service is currently unavailable
Request samples
curl

Copy
curl -i -X GET "https://public-data-api.london-demo.lmax.com/v1/instruments/eur-usd"
Response samples
200404503
Content type
application/json
Example

Currency
Currency

Copy
{
"instrument_id": "eur-usd",
"symbol": "EUR/USD",
"security_id": "4001",
"currency": "USD",
"unit_of_measure": "EUR",
"asset_class": "CURRENCY",
"quantity_increment": "1000.0000",
"price_increment": "0.000010",
"ticker_enabled": true
}
List Instruments

get
/v1/instruments
List all instruments currently available on the platform.

Responses
200 A list of all instruments
503 The service is currently unavailable
Request samples
curl

Copy
curl -i -X GET "https://public-data-api.london-demo.lmax.com/v1/instruments"
Response samples
200503
Content type
application/json

Copy
Expand allCollapse all
[
{
"instrument_id": "eur-usd",
"symbol": "EUR/USD",
"security_id": "4001",
"currency": "USD",
"unit_of_measure": "EUR",
"asset_class": "CURRENCY",
"quantity_increment": "1000.0000",
"price_increment": "0.000010",
"ticker_enabled": true
},
{
"instrument_id": "gbp-usd",
"symbol": "GBP/USD",
"security_id": "4002",
"currency": "USD",
"unit_of_measure": "GBP",
"asset_class": "CURRENCY",
"quantity_increment": "1000.0000",
"price_increment": "0.000010",
"ticker_enabled": false
}
]
WebSocket
A websocket endpoint is available at /v1/web-socket. This web socket can be used to stream order book snapshots and ticker information for one or multiple instruments. For example:

wss://public-data-api.london-demo.lmax.com/v1/web-socket
Websocket Request Rate Limiting
Websocket requests are rate limited to 1 requests per second. Exceeding this limit will result in an error response with the error code TOO_MANY_REQUESTS While it is technically possible to use multiple web socket connections, we currently recommend to use one websocket connection with multiple subscriptions.

Subscribe
Send a Subscribe message to begin streaming data. The available channels for subscription are:

ORDER_BOOK - A stream of order book updates
TICKER - A ticker (trade information) for an order book
The full list of available instruments can be obtained from List Instruments REST API endpoint.

Subscribe Schema
type
required
string
Value: "SUBSCRIBE"
Message Type

channels
required
Array of objects (Channels)
The list of channels to subscribe to

Subscribe Example

Copy
Expand allCollapse all
{
"type": "SUBSCRIBE",
"channels": [
{
"name": "ORDER_BOOK",
"instruments": []
},
{
"name": "TICKER",
"instruments": []
}
]
}
Unsubscribe
To stop receiving data, send an Unsubscribe message.

Unsubscribe Schema
type
required
string
Value: "UNSUBSCRIBE"
Message Type

channels
required
Array of objects (Channels)
The list of channels to unsubscribe from

Unsubscribe Example

Copy
Expand allCollapse all
{
"type": "UNSUBSCRIBE",
"channels": [
{
"name": "ORDER_BOOK",
"instruments": []
},
{
"name": "TICKER",
"instruments": []
}
]
}
Subscription Responses
On a successful subscription or unsubscription a response will be sent containing all current subscriptions:

Successful Subscription
Subscriptions Schema
type	
string
Value: "SUBSCRIPTIONS"
Message Type

channels	
Array of objects (Channel)
The list of channels to subscribe to

Subscriptions Example

Copy
Expand allCollapse all
{
"type": "SUBSCRIPTIONS",
"channels": [
{
"name": "ORDER_BOOK",
"instruments": []
},
{
"name": "TICKER",
"instruments": []
}
]
}
If a subscription cannot be processed an error response will be sent.

Subscription Error
Subscription Error Schema
type	
string
Value: "ERROR"
Message Type

error_code	
string
Enum: "CHANNEL_UNAVAILABLE" "INSTRUMENT_NOT_FOUND" "INTERNAL_SERVER_ERROR" "PARSING_ERROR" "TOO_MANY_REQUESTS" "BAD_REQUEST"
error_message	
string
Error Example

Copy
{
"type": "ERROR",
"error_code": "INSTRUMENT_NOT_FOUND",
"error_message": "Instrument not found."
}
Order Book Channel
Order book price updates are limited to one update a second for each instrument.

OrderBook Schema
type	
string
Value: "ORDER_BOOK"
Message Type

instrument_id	
string
Instrument identifier

timestamp	
string
ISO8601 timestamp with millisecond resolution

status	
string
Enum: "OPEN" "SUSPENDED" "CLOSED" "SETTLED" "WITHDRAWN"
Current status of the order book

bids	
Array of objects (Price and Quantity)
Bids listed from best to worst price (descending)

asks	
Array of objects (Price and Quantity)
Asks listed from best to worst price (ascending)

Order Book Example

Copy
Expand allCollapse all
{
"type": "ORDER_BOOK",
"instrument_id": "eur-usd",
"timestamp": "2024-10-13T22:53:26.748Z",
"status": "OPEN",
"bids": [
{
"price": "1.181060",
"quantity": "500000.0000"
},
{
"price": "1.181050",
"quantity": "200000.0000"
}
],
"asks": [
{
"price": "1.181100",
"quantity": "250000.0000"
},
{
"price": "1.181110",
"quantity": "350000.0000"
}
]
}
Ticker Channel
Ticker updates are per trade for each instrument.

Ticker Schema
type	
string
Value: "TICKER"
Message Type

instrument_id	
string
Instrument identifier

timestamp	
string <date-time>
ISO8601 timestamp with millisecond resolution

best_bid	
string
Current best bid price

best_ask	
string
Current best ask price

trade_id	
string
Trade identifier

last_quantity	
string
Last quantity traded

last_price	
string
Last price traded

session_open	
string
Session open price

session_low	
string
Session low trade price

session_high	
string
Session high trade price

Ticker Example

Copy
{
"type": "TICKER",
"instrument_id": "eur-usd",
"timestamp": "2024-10-13T22:53:26.748Z",
"best_bid": "1.180970",
"best_ask": "1.181010",
"trade_id": "0B5WMAAAAAAAAAAS",
"last_quantity": "1000.0000",
"last_price": "1.180970",
"session_open": "1.181070",
"session_low": "1.180590",
"session_high": "1.181390"
}
Status
Status messages are sent when the system goes offline.

Status Schema
type	
string
Value: "STATUS"
Message Type

description	
string
Status description

status	
string
Enum: "ONLINE" "MAINTENANCE"
Status

Status Example

Copy
{
"type": "STATUS",
"description": "The service is currently unavailable",
"status": "MAINTENANCE"
}
General considerations
Responding to Public API Pings
The Public API initiates a websocket Ping every three seconds. Websocket connection might be closed with status code 1000 if the client does not respond to websocket Ping messages with a Pong frame - as specified in RFC6455 "The WebSocket Protocol":

Upon receipt of a Ping frame, an endpoint MUST send a Pong frame in response, unless it already received a Close frame. It SHOULD respond with Pong frame as soon as is practical.

Client implementations are expected to handle bursts of websocket messages while still being able to respond to Pings within 1 second.

Pinging the Public API
The Public API complies with RFC6455 5.5.2 and will respond to a Ping frame with a Pong frame. Note that there is a limit of one Ping frame per 30 seconds. Exceeding this limit will result in the websocket being disconnected with a status code of 1008.






