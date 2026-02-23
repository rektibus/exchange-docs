Bullish Trading API 1.0.0
Bullish Help Center: support@bullish.com URL: https://support.bullish.com
Overview
Welcome to the Bullish Trading API documentation!

This documentation provides resource descriptions and endpoints usage instructions for the API.

CoinDesk Trading services are provided by Bullish via regulated subsidiaries in select locations. The features and functionality detailed in this Bullish API documentation also apply to CoinDesk Trading users. The base URLs api.exchange.bullish.com and api.trade.coindesk.com are interchangeable.

The API:

follows REST conventions
has the base URL api.exchange.bullish.com or api.trade.coindesk.com (unless one of the sandbox environments is being used)
has endpoints under the below categories:
Authenticated endpoints for private client data e.g. Get Orders endpoint
Non-authenticated endpoints for public data e.g. Get Markets endpoint
uses bearer-based authentication
enforces a blanket rate limit across all requests
may add new fields to existing response payloads. Please do not use strict deserialisation as it may cause compatibility issues.
Additional Links
Code examples - Bullish Github Repository
Deprecated features & APIs - Deprecated Features Documentation
Help center - Bullish Help Center
Comprehensive guide for new Institutional users - Institutional User Guide
Various order/custody status codes - Error & Rejection Codes
Operational status of our exchange - official status page
Connectivity Options
In GCP, generally our most optimal connection is to operate within asia-southeast1-a Availability Zone. Please note, this may change at any given moment and without warning to another Availability Zone within asia-southeast1 for operational reasons. For AWS or GCP connectivity details, please contact your sales representative

FIX API
The FIX API is available to institutional clients and is only accessible through a AWS or GCP private connection:

AWS PrivateLink
It provides private connectivity between VPCs, AWS service without exposing your traffic to the public internet. Bullish will provide the published service IDs for this service. You will be able to connect to our FIX service endpoint once the connection has been successfully established.
GCP Private Service Connect
It allows customers to access managed services privately from inside their VPC network. Bullish will provide the published service IDs for this service. You will be able to connect to our FIX service endpoint once the connection has been successfully established.
For more details please refer to the full specification:

Bullish FIX Protocol Specification
Bullish FIX Protocol Dictionary
Bullish FIX CRT Certificate
Exchange Time
All timestamps are specified in EPOCH time.

Pagination Support
If specified in the API documentation, an endpoint may return cursor paginated responses. Default page size is 25.

There are 4 special query parameters used to control the pagination behaviour.

_pageSize can be one of 5, 25, 50, 100, default value is 25
_metaData can be false/true, if false the links are NOT part of the response. explicitly set _metaData=true to guarantee links are returned.
_nextPage cursor to the next page. It is provided in the paginated response when _metaData=true.
_previousPage cursor to the previous page. It is provided in the paginated response when _metaData=true.
The paginated data is returned in the following wrapped format with generated links to the previous and next pages:

{
  "data": [
    {
      "averageFillPrice": null,
      "baseFee": "0.00000000",
      "createdAtDatetime": "2018-11-18T00:00:00.000Z",
      "createdAtTimestamp": "1639464207402",
      "handle": null,
      "margin": false,
      "orderId": "390755652232282113",
      "price": "8520.7000",
      "quantity": "1.00000000",
      "quantityFilled": "0.00000000",
      "quoteAmount": "0.0000",
      "quoteFee": "0.0003",
      "side": "BUY",
      "status": "OPEN",
      "statusReason": "Open",
      "statusReasonCode": "6001",
      "stopPrice": null,
      "symbol": "BTCUSD",
      "timeInForce": "GTC",
      "type": "LMT"
    },
    ...
  ],
  "links": {
    "next": "/trading-api/v1/orders?_pageSize=5&symbol=BTCUSD&_nextPage=Mjk3NzM1MzQ5NDI0NjIwMDMy",
    "previous": "/trading-api/v1/orders?_pageSize=5&symbol=BTCUSD&_previousPage=Mjk3NzM1Mzg3NzQ3OTc1Njgw"
  }
}
Filtering Support
If specified in the API documentation, an endpoint may support filters on specific fields and values e.g. GET /orders?status=OPEN
Only fields returned in an API response may be used as filter parameters. What you see is what you query on and by.
For the fields in the API response usable as filter parameters, please consult the API endpoint of interest.
Datetime and timestamp filters require additional keywords from this list - [ gte, lte, gt, lt ]. A few examples are provided below.
/trading-api/v1/trades?createdAtTimestamp[gte]=1686447835000 queries for trades with createdAtTimestamp greater than or equal to 1686447835000.
/trading-api/v1/trades?createdAtDatetime[gte]=2023-04-06T00:00:00.000Z&createdAtDatetime[lte]=2023-06-07T00:00:00.000Z queries for trades with createdAtDatetime greater than or equal to 2023-04-06T00:00:00.000Z but less than or equal to 2023-06-07T00:00:00.000Z
By design, pagination query parameters start with an underscore. This differentiates them from filter query parameters e.g. GET /orders?status=OPEN&_pageSize=25
Rate Limits
Public Endpoints
The below mentioned public endpoints will be rate limited. For more information please reach out to your Bullish customer support.

/trading-api/v1/markets and subpaths
/trading-api/v1/market-data and subpaths
/trading-api/v1/history/markets and subpaths
/trading-api/v1/assets and subpaths
/trading-api/v1/index-prices and subpaths
/trading-api/v1/index-data and subpaths
Private Endpoints
API endpoints denoted by Ratelimited: True in the description are also subject to rate limits. e.g. Create Order. The API endpoints fall under the below categories. The rate limit for each category is independently applied.

Unauthenticated endpoints, rate limited at 50 requests per second.
Authenticated /orders endpoints, rate limited at 10 requests per second.
Other Authenticated endpoints, rate limited at 50 requests per second.
Rate Limits per IP address
Each IP address is subject to a blanket rate limit of 500 requests per 10 seconds (approximately 50 requests per second). If an IP address is rate limited, the http response status code will be 429 Too Many Requests and the IP address is blocked from making any requests for 60 seconds.

Global Rate Limit
The global rate limit is an additional rate limit specific to the exchange. It is used to help limit the flow of orders into the exchange. It affects all clients fairly. When the global rate limit is breached the x-ratelimit-global-breach header value will be set to true else false.

Rate Limits Info
When rate limits are not exceeded, the http response header of the API endpoint called will contain the below:

x-ratelimit-limit: Maximum number of requests allowed for the specific API category within time period.
x-ratelimit-remaining: Remaining number of requests allowed for the specific API category within time period.
x-ratelimit-reset: The next time period in which x-ratelimit-remaining is reset back to the maximum allowed for the specific API category.
x-ratelimit-global-breach: true/false, indicating whether the global limit has been breached.
Exceeding Rate Limits
When rate limits are exceeded, the API endpoint will return the http response status code 429 Too Many Requests and the http response body will be:

  {
    "errorCode": 96000,
    "errorCodeName": "RATE_LIMIT_EXCEEDED",
    "message": "Rate limit exceeded"
  }
Exceeding The Global Rate Limit
When the global rate limit is exceeded, the API endpoint will return the http response status code 429 Too Many Requests and the http response body will be:

  {
    "errorCode": 96001,
    "errorCodeName": "GLOBAL_RATE_LIMIT_EXCEEDED",
    "message": "Global rate limit exceeded"
  }
Increasing Rate Limits
For more information on increasing your rate limits, please reach out to your sales representative.

Obtaining Your Rate Limit Token
Each trading account has a unique rate limit token that can be obtained by querying Get Trading Accounts. The rate limit token must be provided in the HTTP request header BX-RATELIMIT-TOKEN to enjoy higher tiers of rate limits else the default of 50 msgs/sec is applied.

Price And Quantity Precision
A market consists of two assets, namely base asset and quote asset. For instance, the BTCUSD market has BTC as base asset and USD as quote asset. The price of a market is denominated in the quote asset, while the quantity is denominated in the base asset. For instance, the price in BTCUSD market is in USD while the quantity is in BTC. Each asset has its own precision. For this, the below asset APIs can be queried.

The Get Assets API endpoint for all supported asset symbols
The Get Asset By Symbol API endpoint for a specific asset symbol
The precision of an asset is the number of decimal places used to express its value in. For instance, the quantity in the market BTCUSD is in BTC. As BTC has a precision of 8, the quantity in BTCUSD has 8 decimal places. It follows that in order to express a quantity of 1 BTC in BTCUSD market, it has to be 1.00000000 BTC.

Alternatively, the below market APIs can also be queried to obtain the price and quantity precisions for different markets.

The Get Markets API endpoint for all supported market symbols
The Get Market By Symbol API endpoint for a specific market symbol
Following the logic outlined above,

The precision for quantity is defined by the basePrecision
The precision for price is defined by quotePrecision
Numeric Identifier Contraints
Numeric (i64) identifiers such as nonce and handle should not have leading zero's. For example 009990822212000000 is invalid but 9990822212000000 is valid.

Order timeInForce
The order timeInForce can be set to the following values:

GTC - good until cancelled - the order is open forever unless fully filled or cancelled
FOK - fill or kill - if the order cannot immediately be filled in full it is cancelled
IOC - immediate or cancel - the order is immediately filled in full or in part and any remainder is cancelled
Error & Rejection Codes
Details of statusReasonCode and statusReason can be referenced from Error & Rejection Codes

Authentication
The API uses bearer based authentication. A JWT token is valid for 24 hours only. To generate a JWT token see - Generate A JWT Token

How To Send Authenticated Requests
To send an authenticated request, you must follow these steps:

Generate An API Key
Add Authenticated Request Header
Generate A JWT Token
Construct The BX-NONCE Header
Construct The Command You Want To Send
Construct The BX-SIGNATURE Header
Fetch Trading Account Ids
Send The HTTP Authenticated Request
How To Ensure The Order Of Create Order or Cancel Order Requests
How do EMS/Brokers Flag Their Executions Sent To Bullish
Generate An API Key
A prerequisite to generate API keys is to have a Bullish account. To generate an API key follow these steps:

Log in into your Bullish account
Click on your account initials at the upper right corner and then click Settings
Click API Keys and then click Add API Key
Select the API Key type, either ECDSA or HMAC
Enter a key name in the Key Name field
Adding an IP whitelist is optional. Should an IP whitelist be added, login requests must be from within the IP whitelist range.
Click Generate API Key
HMAC API Key Notes
A HMAC API Key is a shared secret key that is used for HMAC based signing of trading API requests
Always store your HMAC secret in a secure medium as they are used to sign your requests. Do not share your HMAC secret in any publicly accessible areas such as code repositories, client side code, or other vulnerable areas and make sure the keys are not shipped with your mobile or web apps.
You do not need the metadata string to extract your userId like you would a Bullish API Key
HMAC API Keys can only be used for Trading on Bullish; the JWT generated using an HMAC API Key is only valid for trading endpoints.
ECDSA API Key Notes
An ECDSA API key is a public/private key pair used for ECDSA based signing of trading and custody API requests
The private key is what you will use to sign your requests. Always store your private keys in a secure medium as they are used to sign your requests. Do not share your private keys in any publicly accessible areas such as code repositories, client side code, or other vulnerable areas and make sure the keys are not shipped with your mobile or web apps.
From here on the:
public key will be referred to as PUBLIC_KEY
private key will be referred to as PRIVATE_KEY
Key and signature format details:
Curve: ECDSA R1 (prime256v1/secp256r1/P-256)
Signature encoding: DER
Hashing Algorithm: SHA256
Key format: X.509 SubjectPublicKeyInfo format, PEM encoded
An ECDSA API key additionally has a metadata string associated with it which is displayed along side the key. You must base64 decode the metadata to extract your userId (example follows). You will need the userId in the next step.

echo eyJwdWJsaWNLZXkiOiJQVUJfUjFfNWNpVW52TW5rVThMOVBCWnZaa1BGcjhqdkRnUHpzcHhWNGlqOThIN1JqM1FSNzJyMkEiLCJhY2NvdW50SWQiOjIyMjAwMDAwMDAwMDAwNCwiY3JlZGVudGlhbElkIjoiMTAifQ== | base64 --decode
{"publicKey":"PUB_R1_5ciUnvMnkU8L9PBZvZkPFr8jvDgPzspxV4ij98H7Rj3QR72r2A","userId":"12345","accountId":"12345","credentialId":"10"}
Add Authenticated Request Header
Each authenticated request must include a Authorization header:

Authorization: Bearer <JWT_TOKEN>
The JWT is valid for 24 hours.

Generate a JWT Token
Bullish API Key
Deprecated [more info]: Existing Bullish API key will no longer be usable as of 28 June, 2024
To generate/get a JWT token for a Bullish API Key you will need to perform the following request:

POST /trading-api/v2/users/login
Body
publicKey - bullish account public key
userId - bullish user id corresponding to the metadata
signature - signed JSON string encoding of loginPayload, see the code sample for how to get it
expirationTime - epoch timestamp in seconds that is 5 minutes in the future
nonce - epoch timestamp in seconds; note this login API nonce has no connection to the orders API nonce
biometricsUsed - set to false
sessionKey - set to null
{
  "publicKey": "<PUBLIC_KEY>",
  "signature": "<SIGNATURE>",
  "loginPayload": {
    "userId": "100008771"
    "nonce": 1638776636,
    "expirationTime": 1638776936,
    "biometricsUsed": false,
    "sessionKey": null
  }
}
Response
{
  "authorizer": "<AUTHORIZER>",
  "token": "<JWT_TOKEN>"
}
See generate JWT for sample Python scripts.

HMAC API Key
To generate/get a JWT token for a HMAC API Key you will need to perform the following request:

GET /trading-api/v1/users/hmac/login
Response
{
  "authorizer": "<AUTHORIZER>",
  "token": "<JWT_TOKEN>"
}
You will need to provide a series of headers along with the request in order to successfully generate a JWT token.

BX-TIMESTAMP - number of milliseconds since EPOCH
BX-NONCE - client side incremented 64-bit unsigned integer
BX-PUBLIC-KEY - Public key for the HMAC Key being used to generate the JWT
BX-SIGNATURE - The signed message related to the login request. Outlined below
To sign the login request for an HMAC API Key login we will need to construct a string that concatenates the following fields:

timestamp - value provided for the BX-TIMESTAMP header
nonce - value provided for the BX-NONCE
request method - GET
request path - /trading-api/v1/users/hmac/login
See generate JWT for a sample Python script.

ECDSA API Key
To generate/get a JWT token for a ECDSA API Key you will need to perform the following request:

POST /trading-api/v2/users/login
Body
publicKey - ECDSA public key; new line characters should be UNIX encoded (\n, not \r\n or \r)
userId - bullish user id corresponding to the metadata
signature - signed JSON string encoding of loginPayload, see the code sample for how to get it
expirationTime - epoch timestamp in seconds that is 5 minutes in the future
nonce - epoch timestamp in seconds; note this login API nonce has no connection to the orders API nonce
biometricsUsed - set to false
sessionKey - set to null
{
  "publicKey": "<PUBLIC_KEY>",
  "signature": "<SIGNATURE>",
  "loginPayload": {
    "userId": "100008771"
    "nonce": 1638776636,
    "expirationTime": 1638776936,
    "biometricsUsed": false,
    "sessionKey": null
  }
}
Response
{
  "authorizer": "<AUTHORIZER>",
  "token": "<JWT_TOKEN>"
}
See generate JWT for a sample Python script.

Logout using a JWT Token
Users can better manage their sessions by logging out of unused sessions. This can be done by calling the GET /trading-api/v1/users/logout endpoint with the JWT Token in the header - see Add Authenticated Request Header.

Construct The BX-NONCE Header
The header BX-NONCE value is a unique client-side 64-bit unsigned integer. It has the following characteristics:

Each request the client sends how have incrementing BX-NONCE value
To prevent a client to send the max value of a 64-bit unsigned integer and thus immediately exhaust all unique nonces the exchange will only accept a nonce within a specified range
The lower and upper bounds of the current nonce range are specified by nonce endpoint e.g. GET /nonce
The nonce range is updated daily
The nonce lowerBound is the start of day EPOCH timestamp in micro seconds
The nonce upperBound is the end of day EPOCH timestamp in micro seconds
Construct The Command You Want To Send
Each authenticated request contains a <COMMAND> to be executed by the API. A <COMMAND> has the following properties:

A <COMMAND> is JSON encoded
Every field in the JSON payload must have a value. Use null to represent the absence of a value
The fields must be specified and encoded in the order presented in this documentation
Find below two <COMMAND> examples:

Create Spot Order
Create Margin Order
Cancel Order
Create Spot Order Example
To create a Spot buy limit order:

for the BTCUSD market
at a price of 55071.5000
for a quantity of 1.87000000
with a time-in-force of GTC (good till cancelled)
The COMMAND would be constructed like below:

{
  "timestamp": "<TIMESTAMP>",
  "nonce": "<NONCE>",
  "authorizer": "<AUTHORIZER>",
  "command": {
    "commandType": "V2CreateOrder",
    "handle": null,
    "symbol": "BTCUSD",
    "type": "LMT",
    "side": "BUY",
    "price": "55071.5000",
    "stopPrice": null,
    "quantity": "1.87000000",
    "timeInForce": "GTC",
    "allowMargin": false,
    "tradingAccountId": "111234567890" 
  }
}
Create Margin Order Example
With reference to the same payload in Create Spot Order, setting the field allowMargin to true will make it a margin order.

Documentation is available here on what happens in the event of liquidation.

Cancel Order Example
To cancel a buy limit order:

for the BTCUSD market
where the orderId is 390755251743358977
The COMMAND would be constructed like below:

{
  "timestamp": "<TIMESTAMP>",
  "nonce": "<NONCE>",
  "authorizer": "<AUTHORIZER>"
  "command": {
    "commandType": "V2CancelOrder",
    "orderId": "390755251743358977",
    "handle": null,
    "symbol": "BTCUSD",
    "tradingAccountId": "111234567890"
  }
}
Add Amm instruction
{
  "timestamp": "1621490985000",
  "nonce": "123456789",
  "authorizer": "03E02367E8C900000500000000000000",
  "command": {
    "commandType": "V2AddLiquidity",
    "symbol": "BTCUSD",
    "baseQuantity": "0.00000000",
    "quoteQuantity": "0.00000000",
    "upperBound": "14000.0000",
    "lowerBound": "12000.0000",
    "feeTierId": "1",
    "tradingAccountId": "111234567890"
  }
}
Remove Amm instruction
{
  "timestamp": "<TIMESTAMP>",
  "nonce": "<NONCE>",
  "authorizer": "<AUTHORIZER>"
  "command": {
    "commandType": "V2RemoveLiquidity",
    "liquidityId": "557839859386417160",
    "symbol": "BTCUSD",
    "tradingAccountId": "111234567890"
  }
}
Command for Transfer Asset
POST /trading-api/v1/command?commandType=V1TransferAsset

{
  "timestamp": "<TIMESTAMP>",
  "nonce": "<NONCE>",
  "authorizer": "<AUTHORIZER>"
  "command": {
    "commandType": "V1TransferAsset",
    "assetSymbol": "USD",
    "quantity": "7.0000",
    "fromTradingAccountId": "11123456789",
    "toTradingAccountId": "11198765432"
  }
}
Construct The BX-SIGNATURE Header
The following signing formats demonstrates how to obtain the BX-SIGNATURE header.

Signing Format
This signing format works with /trading-api/v2/orders, /trading-api/v2/amm-instructions, /trading-api/v2/command and Custody APIs. This signing format has the following benefits:

Null fields need not be included in the HTTP request body
Fields need not be strictly ordered in the HTTP request body
Construct a string that concatenates the following fields:

timestamp - value provided for the BX-TIMESTAMP header
nonce - value provided for the BX-NONCE
request method - e.g. POST
request path - e.g. /trading-api/v2/orders
request JSON string, removing any spaces and newline characters.
Note that the same request JSON string used in signing must be sent as the HTTP request body.

How To Sign - ECDSA API Key
Hash the above string using a SHA-256 hash function and sign the resulting hexdigest with your ECDSA <PRIVATE_KEY>.
DER encode the signature, and base64 encode the DER encoded signature.
See sign a request with ECDSA for a sample Python script.

How To Sign - HMAC API Key
Hash the above string using a SHA-256 hash function and take the hexdigest.
Sign the hexdigest from step 2 with your HMAC Secret Key.
See sign a request with HMAC for a sample Python script.

Fetch Trading Account Ids
Trading Account Ids may be required by some endpoints. They can be fetched from Get All Trading Accounts.

See an API example Here.

Send The HTTP Authenticated Request
See create an order for a sample Python script.

How To Ensure The Order Of Create Order or Cancel Order Requests
To ensure the order of the create order or cancel order requests, you must wait for an acknowledgement response which will contain the orderId generated on the server side. Also remember that the nonce parameter, for these two requests, must be a unique increasing integer value.

For example, let us assume the following:

You sent 10 create order requests in a row without waiting for an orderId
The nonce increases with each request sent and thus
The nonce is unique for each request
Because the requests received by the Bullish exchange are processed in parallel the following two possible scenarios can happen:

happy scenario which has a small chance to occur: all 10 requests are processed in the exact order sent by the client, no error, all great and you are happy
unhappy scenario which has a higher chance to occur: the requests are not processed in the exact order sent by you, because the requests might arrive at the bullish processing server at different times and thus the validations of the nonce for each request take place at random times. Because of that all the requests that are validated and have the nonce higher than the latest valid nonce will be accepted as valid and the ones which have the nonce smaller than the last valid nonce will be considered invalid and dropped. In the worse case scenario the request with the highest nonce, the 10th request you sent, is validated first, and the rest of the 9 requests will fail the validation because they have the nonce smaller than the 10th. Also if some requests are failing because of some other errors, e.g. incorrect inputs or internal error, you will not know because you did not wait for the acknowledgement from the server side for each request you sent.
If you wait the acknowledgement from the server side you ensure the order of the requests you sent and you can also verify the status of the order(s) you created or cancelled.

How To Enable Out-Of-Order Processing of Order Requests
The header BX-NONCE-WINDOW-ENABLED is a string representation of a boolean value which enables out-of-order processing of Create Order or Cancel Order requests up to a window size of 100 from the highest previously used nonce value (inclusive).

The nonce parameter is required to be both unique and incremental, but setting BX-NONCE-WINDOW-ENABLED to true loosens this requirement such that the nonce is only required to be unique. For example, the client is able to send nonce values from 1...100 in any order and all the values will be valid.

How do EMS/Brokers Flag Their Executions Sent To Bullish
The header BX-REFERRER value is a unique identifier that can be used by EMS/brokers to flag their executions sent to Bullish.

This referrer header is applicable to the below mentioned authenticated endpoints:

Create Order
Create OTC Trade
For more details, please reach out to your relationship manager to understand which referrer you are assigned.

WebSockets
Connection request to the web-socket uses JWT_COOKIE based authentication. To generate a JWT token see - Generate A JWT Token. Each web-socket exposes a set of topics that can be subscribed to.

Servers
wss://api.exchange.bullish.com - PRODUCTION
wss://registered.api.exchange.bullish.com - PRODUCTION
wss://prod.access.bullish.com - PRODUCTION (Direct Connect)
wss://api.simnext.bullish-test.com - SANDBOX
wss://registered.api.simnext.bullish-test.com - SANDBOX
wss://simnext.access.bullish.com - SANDBOX (Direct Connect)
Max Open WebSocket Connections
Each WebSocket category has a maximum number of open connections. Once it is reached, new WebSocket requests will be rejected. The WebSocket connections fall under the below categories.

Unauthenticated WebSockets, maximum of 100 open connections per IP address.
Authenticated WebSockets, maximum of 10 open connections per API key.
Send A Message Over The WebSocket
Messages sent by the client to the server over a web-socket follows the JSON-RPC 2.0 Specification. The server then returns a response following the same JSON-RPC 2.0 format. The id field sent by the client will be included in the response, allowing the client to map the server's responses to the messages sent by the client. The client ensures the uniqueness of the id field.

Find below the message types accepted by the web-socket:

Subscription Message
Keepalive Ping Message
Subscribe To A Topic
Subscribe to receive a snapshot of your existing data and subsequently receive updates.

Two types of subscription:

Subscribe by <TOPIC>
Subscribe by <TOPIC> and <SYMBOL> plus optional fields (if any)
Message fields:

<TOPIC>: subscription topic
<SYMBOL>: market symbol
<COMMAND_ID>: unique unsigned long value
The subscription message would be constructed like below:

Subscribe by <TOPIC>

{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "subscribe",
  "params": {
      "topic": "<TOPIC>",
  },
  "id": "<COMMAND_ID>"
}
Subscribe by <TOPIC> and <SYMBOL>

{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "subscribe",
  "params": {
      "topic": "<TOPIC>",
      "symbol": "<SYMBOL>",
  },
  "id": "<COMMAND_ID>"
}
Sample subscription messages:

Orders
{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "subscribe",
  "params": {
      "topic": "orders"
  },
  "id": "1611082473000"
}
L1 Order Book
{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "subscribe",
  "params": {
      "topic": "l1Orderbook"
      "symbol": "BTCUSD"
  },
  "id": "1611082473000"
}
Find below the available <TOPIC>:

Multi-OrderBook Data WebSocket (/trading-api/v1/market-data/orderbook)
Unified Anonymous Trades WebSocket (/trading-api/v1/market-data/trades)
Anonymous Market Data WebSocket (/trading-api/v1/market-data/tick/{symbol})
Index Data WebSocket (/trading-api/v1/index-data)
Private Data WebSocket
Unsubscribe To A Topic
Unsubscribe to stop receive updates.

One type of unsubscription for Day 1:

Unsubscribe from one <TOPIC> and <SYMBOL>
Find below the available <TOPIC> for Day 1:

Unified Anonymous Trades WebSocket (/trading-api/v1/market-data/trades)
Message fields:

<TOPIC>: subscription topic
<SYMBOL>: market symbol
<COMMAND_ID>: unique unsigned long value
The unsubscription message would be constructed like below:

Subscribe by <TOPIC> and <SYMBOL>

{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "unsubscribe",
  "params": {
      "topic": "<TOPIC>",
      "symbol": "<SYMBOL>",
  },
  "id": "<COMMAND_ID>"
}
Sample subscription messages:

unified anonymous trade subscription
{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "unsubscribe",
  "params": {
      "topic": "anonymousTrades",
      "symbol": "BTCUSDC",
  },
  "id": "1611082473000"
}
Keep WebSocket Open
Keep the web-socket connection open by sending keepalive ping messages periodically. The web-socket closes automatically after 5 minutes.

The keepalive ping message would be constructed like below:

{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "keepalivePing",
  "params": {},
  "id": "<COMMAND_ID>"
}
Receive A Message From The WebSocket
JSON-RPC responses are of the following format:

Success responses

{
  "jsonrpc": "2.0",
  "id": "1650865877698",
  "result": {
    "responseCode": "200",
    "responseCodeName": "OK",
    "message": "Successfully subscribed"
  }
}
Error responses

{
  "jsonrpc": "2.0",
  "id": "1650865877698",
  "error": {
    "code": "-32602",
    "errorCode": "29013",
    "errorCodeName": "INVALID_TOPIC_ERROR",
    "message": "'a-random-topic' is not a valid topic"
}
code: JSON-RPC 2.0 error code
responseCode/errorCode: unique ID for response/error code
responseCodeName/errorCodeName: unique name for response/error code
message: textual description of the responseCode/errorCode
Snapshot responses are of the following format:

{
  "type": "snapshot",
  "dataType": "<DATA_TYPE>",
  "data": [ { <TOPIC_RESPONSE> } ]
}
Update responses are of the following format:

{
  "type": "update",
  "dataType": "<DATA_TYPE>",
  "data": { <TOPIC_RESPONSE> }
}
Error responses are of the following format:

{
  "type": "error",
  "dataType": "V1TAErrorResponse",
  "data": {
    "errorCode": <ERROR_CODE>,
    "errorCodeName": "<ERROR_CODE_NAME>"
  }
}
Heartbeat
this is a beta/experimental feature that is currently being tested
the heart beat message is periodically sent approximately every 30 seconds on the heartbeat topic for the Private Data WebSocket API and Multi-OrderBook WebSocket) API
the heat beat serves to validate end to end communication between the exchange and the client
if 3 heart beats are missed, then it is advisable to check the official status page for any announcements on the degradation of the exchanges features
if no announcements have been made, it is advisable to disconnect and reconnect the websocket API given the issue may be isolated to a specific gateway
Multi-OrderBook WebSocket (unauthenticated)
Route

/trading-api/v1/market-data/orderbook
This allows simultaneous subscriptions to multiple L1 and L2 orderbooks of different markets:

It also provides a heartbeat topic which sends heartbeat every 30s as an indicator of platform healthiness. Please refer to the heartbeat session for the details.

Multi-Orderbook Subscription
The orderbooks of different markets to be subscribed are controlled by the parameters in the subscription message listed below:

Parameters	Type	Description
topic	String	l1 orderbook: l1Orderbook
l2 orderbook: l2Orderbook
heartbeat: heartbeat
symbol	String	market symbol
L1 Subscription Message Sample:

{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "subscribe",
  "params": {
      "topic": "l1Orderbook",
      "symbol": "BTCUSD"
  },
  "id": "1611082473000"
}
L2 Subscription Message Sample:

{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "subscribe",
  "params": {
      "topic": "l2Orderbook",
      "symbol": "BTCUSD"
  },
  "id": "1611082473000"
}
Heartbeat Subscription Message Sample:

{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "subscribe",
  "params": {
      "topic": "heartbeat"
  },
  "id": "1611082473000"
}
Multi-Orderbook Response
L1 Snapshot and Update Response
Name	Type	Description
type	String	"snapshot" or "update" - the first message after the subscription is always a snapshot of the L1-orderbook
sequenceNumber	String	incrementing, unique, unsigned integer that identifies a state of the L1-orderbook
symbol	String	market symbol
timestamp	String	denotes the time the update was created
bid	Array	nested array containing price and quantity of highest bid
ask	Array	nested array containing price and quantity of lowest ask
On subscription, the snapshot is received immediately.

{
  "type": "snapshot",
  "dataType": "V1TALevel1",
  "data": {
    "symbol": "BTCUSD",
    "bid": [
      "5190.5000",
      "61.94995262"
    ],
    "ask": [
      "5191.6000",
      "96.79626782"
    ],
    "sequenceNumber": "7",
    "datetime": "2020-06-29T06:28:55.000Z",
    "timestamp": "1593412135000"
  }
}
Updates follow as and when the orderbook changes.

{
  "type": "update",
  "dataType": "V1TALevel1",
  "data": {
    "symbol": "BTCUSD",
    "bid": [
      "5199.5000",
      "61.95995262"
    ],
    "ask": [
      "5199.6000",
      "96.59626782"
    ],
    "sequenceNumber": "8",
    "datetime": "2020-06-29T06:28:55.500Z",
    "timestamp": "1593412135500"
  }
}
L2 Snapshot Response
Name	Type	Description
symbol	String	market symbol
bids	Array	array of size 200 where even indices denote price, odd indices denote absolute quantities
asks	Array	array of size 200 where even indices denote price, odd indices denote absolute quantities
sequenceNumberRange	Array	array of size 2 where first element denotes lower bound, second element denotes upper bound of sequence numbers
lower and upper bound are equal for initial snapshot; this may differ for subsequent snapshots
datetime	String	denotes the time the update was created by the engine, ISO 8601 with millisecond as string
timestamp	String	denotes the time the update was created by the engine
publishedAtTimestamp	String	denotes the time the update was broadcasted to connected websockets
{
  "type": "snapshot",
  "dataType": "V1TALevel2",
  "data": {
    "symbol": "BTCUSDC",
    "bids": [
      "5199.5000",
      "110.92467647",
      "5199.4000",
      "20.92470365",
      "5199.3000",
      "0.92473034",
      "5199.2000",
      "0.92475701",
      "5199.1000",
      "0.92478369",
      "5199.0000",
      "0.92481038",
      "5198.9000",
      "0.92483705",
      "5198.8000",
      "0.92486375",
      "5198.7000",
      "0.92489042",
      "5198.6000",
      "0.92491712"
    ],
    "asks": [
      "5199.6000",
      "96.37848193",
      "5199.7000",
      "0.92465082",
      "5199.8000",
      "11.04464563",
      "5199.9000",
      "0.92459696",
      "5200.0000",
      "0.92457029",
      "5200.1000",
      "0.92454362",
      "5200.2000",
      "0.92451695",
      "5200.3000",
      "0.92449028",
      "5200.4000",
      "0.92446361",
      "5200.5000",
      "0.92443695"
    ],
    "sequenceNumberRange": [
        1370055970,
        1370055970
    ],
    "datetime": "2025-02-14T07:15:33.797Z",
    "timestamp": "1739517333797",
    "publishedAtTimestamp": "1739517333798"
  }
}
See connect to multi-orderbook web-socket for a sample Python script.

Unified Anonymous Trades WebSocket (unauthenticated)
Route

/trading-api/v1/market-data/trades
This allows simultaneous trade subscriptions to multiple markets. Additionally, instead of sending trades one by one, trades are sent in batches.

Upon subscribing to a market, the client will first receive a snapshot of the latest 100 trades, followed by batches of trade updates.

Unified Anonymous Trade Subscription
Anonymous trades from different markets to be subscribed to are controlled by the parameters in the subscription message listed below:

Parameters	Type	Description
topic	String	anonymousTrades
symbol	String	market symbol
Trade Subscription Message Sample:

{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "subscribe",
  "params": {
      "topic": "anonymousTrades",
      "symbol": "BTCUSDC"
  },
  "id": "1611082473000"
}
Trade Response Fields
Each trade in a snapshot or update contains the following fields:

Name	Type	Description
tradeId	String	unique trade ID
symbol	String	market symbol
price	String	price, see asset value format
quantity	String	quantity, see asset value format
side	String	order side
isTaker	Boolean	denotes whether this is a taker's trade
otcMatchId	String	unique OTC match id
otcTradeId	String	unique Bullish OTC trade id
clientOtcTradeId	String	unique client OTC trade id
createdAtTimestamp	String	denotes the time the order was ACK'd by the exchange
createdAtDatetime	String	denotes the time the order was ACK'd by the exchange, ISO 8601 with millisecond as string
publishedAtTimestamp	String	denotes the time the update was broadcasted to connected websockets
Unified Anonymous Trade Snapshot Response
The client will receive a trade snapshot with the latest 100 trades upon subscription.

Sample:

{
  "type": "snapshot",
  "dataType": "V1TAAnonymousTradeUpdate",
  "data": {
    "trades": [
      {
        "tradeId": "100069000000063765",
        "isTaker": true,
        "price": "23404.8636",
        "createdAtTimestamp": "1721879160353",
        "quantity": "0.00029411",
        "publishedAtTimestamp": "1721879162124",
        "side": "SELL",
        "createdAtDatetime": "2024-07-25T03:46:00.353Z",
        "symbol": "BTCUSDC",
        "otcMatchId": "1",
        "otcTradeId": "200069000000063765",
        "clientOtcTradeId": "300069000000063765"
      },
      {
        "tradeId": "100069000000063764",
        "isTaker": true,
        "price": "23405.3380",
        "createdAtTimestamp": "1721879155351",
        "quantity": "0.00029411",
        "publishedAtTimestamp": "1721879162124",
        "side": "SELL",
        "createdAtDatetime": "2024-07-25T03:45:55.351Z",
        "symbol": "BTCUSDC",
        "otcMatchId": "2",
        "otcTradeId": "200069000000063764",
        "clientOtcTradeId": "300069000000063764"
      },
      ...
      {
          "tradeId": "100069000000063666",
          "isTaker": true,
          "price": "23001.8708",
          "createdAtTimestamp": "1721879028067",
          "quantity": "0.00029411",
          "publishedAtTimestamp": "1721879162124",
          "side": "SELL",
          "createdAtDatetime": "2024-07-25T03:43:48.067Z",
          "symbol": "BTCUSDC"
      }
    ],
    "createdAtTimestamp": "1721879160353",
    "publishedAtTimestamp": "1721879162125",
    "symbol": "BTCUSDC"
  }
}
Unified Anonymous Trade Update Response
After receiving the snapshot, the client will receive subsequent trade updates in batches.

Sample:

{
  "type": "update",
  "dataType": "V1TAAnonymousTradeUpdate",
  "data": {
    "trades": [
      {
        "tradeId": "100028000018887830",
        "isTaker": true,
        "price": "111.8940",
        "createdAtTimestamp": "1722408780738",
        "quantity": "0.00100000",
        "publishedAtTimestamp": "1722408780790",
        "side": "BUY",
        "createdAtDatetime": "2024-07-31T06:53:00.738Z",
        "symbol": "BTCUSDC"
      },
      {
        "tradeId": "100028000018887837",
        "isTaker": false,
        "price": "111.8716",
        "createdAtTimestamp": "1722408780738",
        "quantity": "0.00009595",
        "publishedAtTimestamp": "1722408780790",
        "side": "SELL",
        "createdAtDatetime": "2024-07-31T06:53:00.738Z",
        "symbol": "BTCUSDC",
        "otcMatchId": "10",
        "otcTradeId": "200028000018887837",
        "clientOtcTradeId": "300028000018887837"
      },
      ...
      {
        "tradeId": "100028000018887992",
        "isTaker": true,
        "price": "112.2896",
        "createdAtTimestamp": "1722408780786",
        "quantity": "0.00100000",
        "publishedAtTimestamp": "1722408780790",
        "side": "BUY",
        "createdAtDatetime": "2024-07-31T06:53:00.786Z",
        "symbol": "BTCUSDC",
        "otcMatchId": "11",
        "otcTradeId": "200028000018887992",
        "clientOtcTradeId": "300028000018887992"
      }
    ],
    "createdAtTimestamp": "1722408780786",
    "publishedAtTimestamp": "1722408780790",
    "symbol": "BTCUSDC"
  }
}
Unified Anonymous Trade Unsubscription
Upon unsubscribing from a market, the client will stop receiving trade updates. Anonymous trades from different markets to be unsubscribed from are controlled by the parameters in the unsubscription message listed below:

Parameters	Type	Description
topic	String	anonymousTrades
symbol	String	market symbol
Trade Unsubscription Message Sample:

{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "unsubscribe",
  "params": {
      "topic": "anonymousTrades",
      "symbol": "BTCUSDC"
  },
  "id": "1611082473000"
}
Unified Anonymous Tick WebSocket (unauthenticated)
Route

/trading-api/v1/market-data/tick
This allows simultaneous tick subscriptions to multiple markets.

Upon subscribing to a market, the client will first receive a snapshot of latest ticker, followed by updates. See the data model: Get Market Tick

Unified Anonymous Tick Subscription
Tick of different markets to be subscribed to, are controlled by parameters in the subscription message listed below:

Parameters	Type	Description
topic	String	tick
symbol	String	market symbol such as BTCUSDC
Tick Subscription Message Sample:
{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "subscribe",
  "params": {
      "topic": "tick",
      "symbol": "BTCUSD"
  },
  "id": "1611082473000"
}
Keepalive Message Sample:
{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "keepalivePing",
  "params": {},
  "id": "1611082473001"
}
Tick response example
{
  "type": "snapshot",
  "dataType": "V1TATickerResponse",
  "data": {
    "askVolume": "3.56000000",
    "average": "5200.0400",
    "baseVolume": "1.00000000",
    "bestAsk": "6543.0000",
    "bestBid": "2345.0000",
    "bidVolume": "2.00000000",
    "change": "0.0000",
    "close": "5200.0400",
    "createdAtTimestamp": "1591058897000",
    "publishedAtTimestamp": "1591058898000",
    "high": "5200.0400",
    "last": "5200.0400",
    "lastTradeDatetime": "2020-06-02T00:40:39.500Z",
    "lastTradeSize": "1.00000000",
    "low": "5200.0400",
    "open": "5200.0400",
    "percentage": "0.00",
    "quoteVolume": "5200.0400",
    "symbol": "BTC-USDC-PERP",
    "type": "ticker",
    "vwap": "5200.0400",
    "currentPrice": "0.0007",
    "ammData": [
      {
        "feeTierId": "1",
        "currentPrice": "0.0007",
        "tierPrice": "0.000703038503",
        "baseReservesQuantity": "96153.00000000",
        "quoteReservesQuantity": "500005200.0400",
        "bidSpreadFee": "0.00000005",
        "askSpreadFee": "0.00000006"
      },
      {
        "feeTierId": "2",
        "currentPrice": "0.0017",
        "tierPrice": "0.001703038503",
        "baseReservesQuantity": "96153.00000000",
        "quoteReservesQuantity": "500005200.0400",
        "bidSpreadFee": "0.00000015",
        "askSpreadFee": "0.00000016"
      }
    ],
    "createdAtDatetime": "2020-06-02T00:48:17.000Z",
    "markPrice": "26000.0000",
    "fundingRate": "0.114100",
    "openInterest": "9.00000000"
  }
}
Anonymous Market Data Price Tick (unauthenticated)
Route

/trading-api/v1/market-data/tick/{symbol}
Note: This endpoint does not require subscriptions.

On connection, the client receives current Tick by Market Symbol. See the data model: Get Market Tick

Tick response example
{
  "type": "snapshot",
  "dataType": "V1TATickerResponse",
  "data": {
    "askVolume": "3.56000000",
    "average": "5200.0400",
    "baseVolume": "1.00000000",
    "bestAsk": "6543.0000",
    "bestBid": "2345.0000",
    "bidVolume": "2.00000000",
    "change": "0.0000",
    "close": "5200.0400",
    "createdAtTimestamp": "1591058897000",
    "publishedAtTimestamp": "1591058898000",
    "high": "5200.0400",
    "last": "5200.0400",
    "lastTradeDatetime": "2020-06-02T00:40:39.500Z",
    "lastTradeSize": "1.00000000",
    "low": "5200.0400",
    "open": "5200.0400",
    "percentage": "0.00",
    "quoteVolume": "5200.0400",
    "symbol": "BTC-USDC-PERP",
    "type": "ticker",
    "vwap": "5200.0400",
    "currentPrice": "0.0007",
    "ammData": [
      {
        "feeTierId": "1",
        "currentPrice": "0.0007",
        "tierPrice": "0.001703038503",
        "baseReservesQuantity": "96153.00000000",
        "quoteReservesQuantity": "500005200.0400",
        "bidSpreadFee": "0.00000005",
        "askSpreadFee": "0.00000006"
      },
      {
        "feeTierId": "2",
        "currentPrice": "0.0017",
        "tierPrice": "0.001703038503",
        "baseReservesQuantity": "96153.00000000",
        "quoteReservesQuantity": "500005200.0400",
        "bidSpreadFee": "0.00000015",
        "askSpreadFee": "0.00000016"
      }
    ],
    "createdAtDatetime": "2020-06-02T00:48:17.000Z",
    "markPrice": "26000.0000",
    "fundingRate": "0.114100",
    "openInterest": "9.00000000"
  }
}
Index Data websocket (unauthenticated)
Route

/trading-api/v1/index-data
Index Price Subscription
The index price of different assets to be subscribed are controlled by the parameters in the subscription message listed below:

Parameters	Type	Description
topic	String	Index Price: indexPrice
assetSymbol	String	Asset symbol, such as BTC or USDC
Index Price Subscription Sample:

{
  "jsonrpc": "2.0",
  "type": "command",
  "method": "subscribe",
  "params": {
      "topic": "indexPrice",
      "assetSymbol": "USDC"
  },
  "id": "1611082473000"
}
IndexPrice Response
On successful subscription for an assetSymbol, the client receives a snapshot with the current index price, and updates after.

Name	Type	Description
assetSymbol	String	asset symbol
price	String	price in USD, see asset value format
updatedAtDatetime	String	denotes the time the index price was updated by the exchange, in ISO 8601 format
updatedAtTimestamp	String	denotes the epoch millisecond time the index price was updated by the exchange
{
  "type": "update",
  "dataType": "V1TAIndexPrice",
  "data": {
    "assetSymbol": "USDC",
    "price": "1.0000",
    "updatedAtDatetime": "2024-06-29T06:29:50.500Z",
    "updatedAtTimestamp": "1719642590000"
  }
}
Private Data WebSocket (authenticated)
All private data updates are realtime.
Establishing a websocket connection

Getting private data from a single trading account.
Connect to /trading-api/v1/private-data?tradingAccountId=<Id of the Trading Account>
For example, to subscribe to the orders topic, the following subscription message is sent:
  {
      "jsonrpc": "2.0",
      "type": "command",
      "method": "subscribe",
      "params": {
          "topic": "orders"
      },
      "id": "1611082473000"
  }
It is possible to subscribe to multiple topics with a single subscription message. For example, a topic of assetAccounts+derivativesPositionsV2 would subscribe to both assetAccounts and derivativesPositionsV2
Getting private data from multiple trading accounts.
Connect to /trading-api/v1/private-data
For example, to subscribe to the orders topic for each of your trading accounts, the following subscription message is sent for each trading account you wish to subscribe to:
  {
      "jsonrpc": "2.0",
      "type": "command",
      "method": "subscribe",
      "params": {
          "topic": "orders",
          "tradingAccountId": "<Id of the Trading Account>"
      },
      "id": "1611082473000"
  }
Topic	Description	Data Type	Subscription Type
orders	Provides snapshot and updates on your orders. The snapshot will contain all open orders and the 20 most recent closed orders.	V1TAOrder	By <TOPIC>
trades	Provides snapshot and updates on your trades. The snapshot will contain the 20 most recent trades.	V1TATrade	By <TOPIC>
spotAccounts	Deprecated[more info] Provides snapshot and updates on assets in your account.	V1TASpotAccount	By <TOPIC>
assetAccounts	Provides snapshot and updates on assets in your account.	V1TAAssetAccount	By <TOPIC>
tradingAccounts	Provides snapshot and updates on your trading account summary.	V1TATradingAccount	By <TOPIC>
heartbeat	Provides heartbeat updates for healthcheck.	V1TAHeartbeat	By <TOPIC>
derivativesPositions	Deprecated[Replaced by: derivativesPositionsV2] Provides derivative position information on your trading account.	V1TAPerpetualPosition	By <TOPIC>
derivativesPositionsV2	Provides derivative position information on your trading account.	V1TADerivativesPosition	By <TOPIC>
ammInstructions	Provides amm instructions update on your trading account.	V1TAAmmInstruction	By <TOPIC>
mmpTrigger	Provides snapshot and updates on your market maker protection trigger events.	V1TAMMPTrigger	By <TOPIC>
mmpRequest	Provides snapshot and updates on your market maker protection configurations.	V1TAMMPConfigRequest	By <TOPIC>
orders response
Name	Type	Description
handle	String	unique numeric (i64) identifier generated on the client side expressed as a string value

Deprecatedto be remove towards the end of Q3 2024.
Replaced by: clientOrderId
clientOrderId	String	unique numeric (i64) identifier generated on the client side expressed as a string value
orderId	String	unique order ID
symbol	String	market symbol
price	String	price, see asset value format
averageFillPrice	String	average fill price, see asset value format
stopPrice	String	stop price, see asset value format
margin	Boolean	indicates if the order was allowed to borrow (does not indicate that borrowing occurred)

Deprecatedto be remove towards the end of Q3 2024.
Replaced by: allowBorrow
allowBorrow	Boolean	indicates if the order was allowed to borrow (does not indicate that borrowing occurred)
quantity	String	quantity, see asset value format
quoteAmount	String	quote quantity deducted from asset account, see asset value format
quantityFilled	String	quantity filled, see asset value format
baseFee	String	base fee rate that will be charged upon trade execution, see asset value format
quoteFee	String	quote fee rate that will be charged upon trade execution, see asset value format
borrowedQuantity	String	quantity borrowed, see asset value format - BUY order borrows quote, SELL order borrows base

Deprecatedto be remove towards the end of Q3 2024.
Replaced by: borrowedBaseQuantity & borrowedQuoteQuantity
borrowedBaseQuantity	String	base quantity borrowed, see asset value format
borrowedQuoteQuantity	String	quote quantity borrowed, see asset value format
isLiquidation	Boolean	indicates if the order was executed as a liquidation order
side	String	order side
type	String	order type
timeInForce	String	time in force
status	String	order status
statusReason	String	status reason, describes why the order is in a specific state
statusReasonCode	Integer	status reason code, see details
createdAtDatetime	String	denotes the time the order was ACK'd by the exchange, ISO 8601 with millisecond as string
createdAtTimestamp	String	denotes the time the order was ACK'd by the exchange
publishedAtTimestamp	String	denotes the time the update was broadcasted to connected websockets
{
  "tradingAccountId": "1111",
  "type": "snapshot",
  "dataType": "V1TAOrder",
  "data": [
    {
      "handle": null,
      "orderId": "392883006043848705",
      "symbol": "BTCUSD",
      "price": "66858.2000",
      "averageFillPrice": "66858.2000",
      "stopPrice": null,
      "margin": false,
      "quantity": "2.00000000",
      "quantityFilled": "2.00000000",
      "quoteAmount": "23000.0000",
      "baseFee": "0.00000000",
      "quoteFee": "0.0005",
      "side": "BUY",
      "borrowedQuantity": "0.0010",
      "isLiquidation": false,
      "type": "LMT",
      "timeInForce": "GTC",
      "status": "CLOSED",
      "statusReason": "Executed",
      "statusReasonCode": 6002,
      "createdAtDatetime": "2021-12-30T07:36:35.918Z",
      "createdAtTimestamp": "1640849795918",
      "publishedAtTimestamp": "1640849795920"
    }
  ]
}
trades response
Name	Type	Description
tradeId	String	unique trade ID
orderId	String	unique order ID
handle	String	unique numeric identifier (i64) generated on the client side expressed as a string value
symbol	String	market symbol
price	String	price, see asset value format
quantity	String	quantity, see asset value format
quoteAmount	String	quote quantity deducted from asset account, see asset value format
baseFee	String	base fee, see asset value format
quoteFee	String	quote fee, see asset value format
side	String	order side
tradeRebateAmount	String	amount of rebate that is credited to the user as part of the trade
tradeRebateAssetSymbol	String	symbol of the asset in which the rebate is paid
isTaker	Boolean	denotes whether this is a taker's trade
otcMatchId	String	unique OTC match id
otcTradeId	String	unique Bullish OTC trade id
clientOtcTradeId	String	unique client OTC trade id
createdAtDatetime	String	denotes the time the trade was executed by the exchange, ISO 8601 with millisecond as string
createdAtTimestamp	String	denotes the time the trade was executed by the exchange
publishedAtTimestamp	String	denotes the time the update was broadcasted to connected websockets
{
  "tradingAccountId": "1111",
  "type": "snapshot",
  "dataType": "V1TATrade",
  "data": [
    {
      "tradeId": "100014000000000118",
      "orderId": "392883006043848705",
      "handle": "123456",
      "symbol": "BTCUSD",
      "price": "66858.2000",
      "quantity": "2.00000000",
      "quoteAmount": "23000.0000",
      "baseFee": "0.00000000",
      "quoteFee": "66.8582",
      "side": "BUY",
      "isTaker": false,
      "tradeRebateAmount": "3.0000",
      "tradeRebateAssetSymbol": "USDC",
      "otcMatchId": "15",
      "otcTradeId": "200014000000000118",
      "clientOtcTradeId": "300014000000000118",
      "createdAtDatetime": "2021-12-30T07:36:35.918Z",
      "createdAtTimestamp": "1640849795918",
      "publishedAtTimestamp": "1640849795920"
    }
  ]
}
assetAccounts response
V1TAAssetAccount provides a more granular view of the assets in your trading account compared to V1TASpotAccount.
Name	Type	Description
tradingAccountId	String	id of the trading account
assetId	String	asset ID
assetSymbol	String	asset symbol
availableQuantity	String	the assets that are available to use on the account, see asset value format
borrowedQuantity	String	the assets on the account that are borrowed, see asset value format
lockedQuantity	String	the assets on the account that are locked in orders, loans and AMM instructions, see asset value format
loanedQuantity	String	the assets on the account that are being loaned, see asset value format
updatedAtDatetime	String	denotes the time the asset account was updated by the exchange, ISO 8601 with millisecond as string
updatedAtTimestamp	String	denotes the time the asset account was updated by the exchange
publishedAtTimestamp	String	denotes the time the update was broadcasted to connected websockets
{
  "tradingAccountId": "1111",
  "type": "snapshot",
  "dataType": "V1TAAssetAccount",
  "data": [
    {
      "tradingAccountId": "1111",
      "assetId": "1",
      "assetSymbol": "BTC",
      "availableQuantity": "4.00000000",
      "borrowedQuantity": "20.00000000",
      "lockedQuantity": "0.00000000",
      "loanedQuantity": "10.00000000",
      "updatedAtDatetime": "2021-12-30T07:36:35.918Z",
      "updatedAtTimestamp": "1640849795918",
      "publishedAtTimestamp": "1640849795920"
    },
    {
      "tradingAccountId": "1111",
      "assetId": "2",
      "assetSymbol": "USD",
      "availableQuantity": "229016.0734",
      "borrowedQuantity": "20000.0000",
      "lockedQuantity": "0.0000",
      "loanedQuantity": "10000.0000",
      "updatedAtDatetime": "2021-12-30T07:36:35.918Z",
      "updatedAtTimestamp": "1640849795918",
      "publishedAtTimestamp": "1640849795920"
    }
  ]
}
tradingAccounts response
Provides a summary of the total borrowed and total collateral values on the specific trading account ID. totalBorrowedQuantity and totalCollateralQuantity do not represent the absolute quantity of the borrowed assets and are notional values represented in the reference asset.
snapshot contains a list with a single entry corresponding to the trading account ID specified in the tradingAccountId query parameter when opening the websocket connection.
Name	Type	Description
tradingAccountId	String	id of the trading account
totalBorrowedQuantity	String	total borrowed across all assets in this trading account displayed in the reference asset
totalCollateralQuantity	String	total collateral across all assets in this trading account displayed in the reference asset
totalBorrowedUSD	String	total borrowed across all assets in this trading account displayed in USD
totalCollateralUSD	String	total collateral across all assets in this trading account displayed in USD
initialMarginUSD	String	The minimum margin one must maintain in order to be able to purposefully increase risk
warningMarginUSD	String	The minimum margin when the customer will receive warning via email/notifications over UI
liquidationMarginUSD	String	The minimum value of margin one must maintain in order to avoid liquidation
fullLiquidationMarginUSD	String	The value of margin when full liquidation occurs
endCustomerId	String	The end customer id used for self trade prevention (default is institution id, max 32 characters)
defaultedMarginUSD	String	The value of margin when this trading account will be moved into a Defaulted state
riskLimitUSD	String	The maximum allowed initial margin requirement for this trading account displayed in USD
totalLiabilitiesUSD	String	The total liabilities for this trading account displayed in USD
maxInitialLeverage	String	The maximum initial leverage
isPrimaryAccount	String	Whether this trading account is the primary account
isBorrowing	String	Whether this trading account is borrowing any asset
isLending	String	Whether this trading account has any open loan offers
isDefaulted	String	Whether this trading account is in a defaulted state
takerFee	String	Deprecated and no longer accurate. See tradeFeeRate at Get Trading Account instead
makerFee	String	Deprecated and no longer accurate. See tradeFeeRate at Get Trading Account instead
referenceAssetSymbol	String	asset symbol
liquidityAddonUSD	String	Expected market impact of unwinding the portfolio in the case of a liquidation event
marketRiskUSD	String	The worst possible loss on the portfolio based on scenario analysis
marginProfile	Object	Contains the market risk multipliers applied to a trading account to derive the five individual Margin Requirement values
initialMarketRiskMultiplierPct	String	Market risk multiplier used to calculate initial margin requirement of the account
warningMarketRiskMultiplierPct	String	Market risk multiplier used to calculate warning margin requirement of the account
liquidationMarketRiskMultiplierPct	String	Market risk multiplier used to calculate liquidation margin requirement of the account
fullLiquidationMarketRiskMultiplierPct	String	Market risk multiplier used to calculate full liquidation margin requirement of the account
defaultedMarketRiskMultiplierPct	String	Market risk multiplier used to calculate defaulted margin requirement of the account
updatedAtDatetime	String	denotes the time the trading account was updated by the exchange, ISO 8601 with millisecond as string
updatedAtTimestamp	String	denotes the time the trading account was updated by the exchange
publishedAtTimestamp	String	denotes the time the update was broadcasted to connected websockets
{
  "tradingAccountId": "1111",
  "type": "snapshot",
  "dataType": "V1TATradingAccount",
  "data": [
    {
      "tradingAccountId": "1111",
      "totalBorrowedQuantity": "12000.0000",
      "totalCollateralQuantity": "13000.0000",
      "totalBorrowedUSD": "12000.0000",
      "totalCollateralUSD": "13000.0000",
      "referenceAssetSymbol": "USD",
      "initialMarginUSD": "900000.0000",
      "warningMarginUSD": "700000.0000",
      "liquidationMarginUSD": "600000.0000",
      "fullLiquidationMarginUSD": "500000.0000",
      "endCustomerId" : "PrimeBroker",
      "defaultedMarginUSD": "300000.0000",
      "riskLimitUSD": "1000000.0000",
      "totalLiabilitiesUSD": "13000.0000",
      "maxInitialLeverage": "3",
      "isPrimaryAccount": true,
      "isBorrowing": true,
      "isLending": false,
      "isDefaulted": false,
      "takerFee": null,
      "makerFee": null,
      "liquidityAddonUSD": "100.0000",
      "marketRiskUSD": "200.0000",
      "marginProfile": {
        "initialMarketRiskMultiplierPct": "200.00",
        "warningMarketRiskMultiplierPct": "150.00",
        "liquidationMarketRiskMultiplierPct": "100.00",
        "fullLiquidationMarketRiskMultiplierPct": "75.00",
        "defaultedMarketRiskMultiplierPct": "50.00"
      },
      "updatedAtDatetime": "2021-12-30T07:36:35.918Z",
      "updatedAtTimestamp": "1640849795918",
      "publishedAtTimestamp": "1640849795920"
    }
  ]
}
heartbeat response
Provides heartbeat update every 30s as an indicator of platform healthiness. Please refer to the heartbeat session for the details.
Name	Type	Description
sequenceNumber	String	sequence number of the heartbeat
createdAtTimestamp	String	time at which the heartbeat is generated
{
  "type": "update",
  "dataType": "V1TAHeartbeat",
  "data": [
    {
      "sequenceNumber": "3",
      "createdAtTimestamp": "1611082473000"
    }
  ]
}
Derivative position response
Deprecated: Topic derivativesPosition will be replaced by derivativesPositionV2

Provide a detail view of the derivative position of each market.
Name	Type	Description
tradingAccountId	String	Id of the trading account
symbol	String	Market symbol, eg. BTC-USDC-PERP
side	String	Side of the position
quantity	String	Current size of the position asset value format
notional	String	Notional value of the current position, calculated using the mark price
entryNotional	String	Notional value of the position, using the average entry price
mtmPnl	String	Sum of all mark-to-market profits and losses plus profits and losses realised from trading, accumulated since the last settlement
reportedMtmPnl	String	The profit/losses from the net price change since the last time the absolute quantity decreased. It is updated with every mark to market and is not updated during settlement or a position size increase
reportedFundingPnl	String	Sum of all funding payments received since the position was opened. This is updated every time funding is paid.
realizedPnl	String	Total profits realized since the trading account first opened this position. This is only updated every time a position’s absolute quantity (aka size) is reduced.
createdAtDatetime	String	denotes the time the position was created by the exchange, ISO 8601 with millisecond as string
createdAtTimestamp	String	denotes the time the position was created by the exchange, number of milliseconds since EPOCH
updatedAtDatetime	String	denotes the time the position was updated by the exchange, ISO 8601 with millisecond as string
updatedAtTimestamp	String	denotes the time the position was updated by the exchange number of milliseconds since EPOCH
publishedAtTimestamp	String	denotes the time the update was broadcasted to connected websockets
{
  "tradingAccountId": "1111",
  "type": "snapshot",
  "dataType": "V1TAPerpetualPosition",
  "data": [
    {
      "tradingAccountId": "111234567890",
      "symbol": "BTC-USDC-PERP",
      "side": "BUY",
      "quantity": "1.00000000",
      "notional": "30000.0000",
      "entryNotional": "30000.0000",
      "mtmPnl": "110.0000",
      "reportedMtmPnl": "120.0000",
      "reportedFundingPnl": "130.0000",
      "realizedPnl": "140.0000",
      "createdAtDatetime": "2020-01-01T00:00:00.000Z",
      "createdAtTimestamp": "1577836800000",
      "updatedAtDatetime": "2020-01-02T00:00:00.000Z",
      "updatedAtTimestamp": "1577923200000",
      "publishedAtTimestamp": "1577923300000"
    }
  ]
}
Derivative position V2 response
Provide a detail view of the derivative position of each market.
Name	Type	Description
tradingAccountId	String	Id of the trading account
symbol	String	Market symbol, eg. BTC-USDC-PERP
side	String	Side of the position
quantity	String	Current size of the position asset value format
notional	String	Notional value of the current position, calculated using the mark price
entryNotional	String	Notional value of the position, using the average entry price
mtmPnl	String	Sum of all mark-to-market profits and losses plus profits and losses realised from trading, accumulated since the last settlement
reportedMtmPnl	String	The profit/losses from the net price change since the last time the absolute quantity decreased. It is updated with every mark to market and is not updated during settlement or a position size increase
reportedFundingPnl	String	Sum of all funding payments received since the position was opened. This is updated every time funding is paid.
realizedPnl	String	Total profits realized since the trading account first opened this position. This is only updated every time a position’s absolute quantity (aka size) is reduced.
settlementAssetSymbol	String	Settlement asset symbol
eventType	String	Derivatives position update event types
createdAtDatetime	String	denotes the time the position was created by the exchange, ISO 8601 with millisecond as string
createdAtTimestamp	String	denotes the time the position was created by the exchange, number of milliseconds since EPOCH
updatedAtDatetime	String	denotes the time the position was updated by the exchange, ISO 8601 with millisecond as string
updatedAtTimestamp	String	denotes the time the position was updated by the exchange number of milliseconds since EPOCH
publishedAtTimestamp	String	denotes the time the update was broadcasted to connected websockets
{
  "tradingAccountId": "1111",
  "type": "snapshot",
  "dataType": "V1TADerivativesPosition",
  "data": [
    {
      "tradingAccountId": "111234567890",
      "symbol": "BTC-USDC-PERP",
      "side": "BUY",
      "quantity": "1.00000000",
      "notional": "30000.0000",
      "entryNotional": "30000.0000",
      "mtmPnl": "110.0000",
      "reportedMtmPnl": "120.0000",
      "reportedFundingPnl": "130.0000",
      "realizedPnl": "140.0000",
      "settlementAssetSymbol": "USDC",
      "eventType": "settlementUpdate",
      "createdAtDatetime": "2020-01-01T00:00:00.000Z",
      "createdAtTimestamp": "1577836800000",
      "updatedAtDatetime": "2020-01-02T00:00:00.000Z",
      "updatedAtTimestamp": "1577923200000",
      "publishedAtTimestamp": "1577923300000"
    }
  ]
}
ammInstruction response
Provides updates of the active AMM instructions on the specific trading account ID.
This topic does not provide snapshot
Name	Type	Description
tradingAccountId	String	id of the trading account
instructionId	String	unique AMM instruction ID
symbol	String	market symbol
baseFee	String	base fee, see asset value format
quoteFee	String	quote fee, see asset value format
status	String	order status
statusReason	String	status reason, describes why the order is in a specific state
statusReasonCode	String	status reason code, see details
createdAtDatetime	String	denotes the time the order was ACK'd by the exchange, ISO 8601 with millisecond as string
createdAtTimestamp	String	denotes the time the order was ACK'd by the exchange
baseCurrentQuantity	String	amount of base asset this AMM instruction currently holds, only for AMM instruction with OPEN status
baseInvestQuantity	String	initial base investment
basePrice	String	current price of base asset
baseWithdrawQuantity	String	amount of base asset returned when AMM instruction is terminated
currentValue	String	value of assets (base and quote) in USD amount that this AMM instruction currently holds
feeTierId	String	unique fee tier ID, see Get Market By Symbol
finalValue	String	value of assets (base and quote) in USD amount when AMM instruction was terminated, only for AMM instruction with CLOSED status
impermanentLoss	String	impermanent loss
liquidity	String	liquidity amount
lastDistributedPrice	String	(Perpetual market only) The price used at the time of settlement for AMM Instructions that can be used to determine mtmPnl and the actual Pnl
lowerBound	String	lower bound of price range, in quote currency
price	String	current price of AMM, see Get Tick By Symbol
quoteCurrentQuantity	String	amount of quote asset this AMM instruction currently holds, only for AMM instruction with OPEN status
quoteInvestQuantity	String	initial quote investment
quotePrice	String	current price of quote asset
quoteWithdrawQuantity	String	amount of quote asset returned when AMM instruction is terminated
requestID	String	unique request ID
updatedAtDatetime	String	denotes the time the AMM instruction was updated by the exchange, ISO 8601 with millisecond as string
updatedAtTimestamp	String	denotes the time the AMM instruction was updated by the exchange
upperBound	String	upper bound of price range, in quote currency
{
  "tradingAccountId": "1111",
  "type": "update",
  "dataType": "V1TAAmmInstruction",
  "data": [
    {
      "instructionId": "100",
      "symbol": "BTCUSDC",
      "baseFee": "1.00000000",
      "quoteFee": "1.0000",
      "status": "OPEN",
      "statusReason": "Ok",
      "statusReasonCode": "1001",
      "createdAtDatetime": "2021-05-20T01:01:01.000Z",
      "createdAtTimestamp": "1621490985000",
      "baseCurrentQuantity": "0.00000000",
      "baseInvestQuantity": "0.00000008",
      "basePrice": "345.67000000",
      "baseWithdrawQuantity": "0.00000010",
      "currentValue": "0.0000",
      "feeTierId": "1",
      "finalValue": "0.0001",
      "impermanentLoss": "0.0000",
      "liquidity": "0.0001",
      "lowerBound": "0.0013",
      "price": "456.7800",
      "quoteCurrentQuantity": "0.0000",
      "quoteInvestQuantity": "0.0009",
      "quotePrice": "1.0000",
      "quoteWithdrawQuantity": "0.0011",
      "lastDistributedPrice": null
      "requestId": "197735387747975680",
      "updatedAtDatetime": "2021-05-20T01:01:01.000Z",
      "updatedAtTimestamp": "1621490985000",
      "upperBound": "14000.0000",
    }
}
mmpTrigger response
Name	Type	Description
tradingAccountId	String	id of the trading account
mmpTriggerId	String	unique MMP trigger ID
underlyingAssetSymbol	String	underlying asset symbol
triggeredBy	String	trigger reason
frozenTimeInSecond	String	duration for which a market maker’s trading activity is temporarily halted after a protective measure is triggered
frozenStartTime	String	start time of the MMP trigger in epoch milliseconds
frozenUntil	String	end time of the MMP trigger in epoch milliseconds
{
  "tradingAccountId": "111000000000000",
  "type": "snapshot",
  "dataType": "V1TAMMPTrigger",
  "data": [
    {
      "mmpTriggerId": "100000000000000"
      "tradingAccountId": "111000000000000",
      "underlyingAssetSymbol": "BTC",
      "triggeredBy": "Delta Limit",
      "frozenTimeInSecond": "10",
      "frozenStartTime": "1611082473000",
      "frozenUntil": "1611082483000"
    }
  ]
}
mmpRequest response
Name	Type	Description
tradingAccountId	String	id of the trading account
requestId	String	id of the request
assetSymbol	String	underlying asset symbol
windowTimeInSecond	String	time window during which the MMP checks are conducted
frozenTimeInSecond	String	duration for which a market maker’s trading activity is temporarily halted after a protective measure is triggered
quantityLimit	String	cap on the total number of contracts that a market maker can trade within windowTimeInSeconds
deltaLimit	String	net delta exposure that a market maker can accumulate within windowTimeInSeconds
status	String	status of the request
statusReason	String	status reason, describes why the request is in a specific state
isReset	String	boolean value that indicates if it was a set or reset MMP configuration request
createdAt	String	denotes the time the request was ACK'd by the exchange
{
  "tradingAccountId": "111000000000000",
  "type": "snapshot",
  "dataType": "V1TAMMPConfigRequest",
  "data": [
    {
      "requestId": "1",
      "tradingAccountId": "111000000000000",
      "assetSymbol": "BTC",
      "windowTimeInSecond": "10",
      "frozenTimeInSecond": "10",
      "quantityLimit": "1000",
      "deltaLimit": "500",
      "status": "CLOSED",
      "statusReason": "Ok",
      "isReset": "false",
      "createdAt": "1611082473000"
    }
  ]
}
See connect to private data web-socket for a sample Python script.

Quickly Try The API
To quickly try the API you can use the TRY green button which you can find on the bottom right side of each endpoint documentation section, next to FILL EXAMPLE and CLEAR buttons.

Try The Non-Authenticated Endpoints
To try the endpoints for which the authentication is not required follow below steps:

Fill in the input parameters, including the request headers
Click the TRY green button
Inspect the results
Try The Authenticated Endpoints
To try the endpoints for which authentication is required follow below steps:

Obtain a bearer token using your API key
Set it in the dedicated api-token field in the Authentication section
Fill in the input parameters
Click the TRY green button
Inspect the results
Test Instruments
Bullish has test instruments which are used for internal testing. Clients can ignore these test instruments.

Test Markets
Bullish currently has 1 test market.

DEMOONEDEMOTWO
Test Assets
Bullish currently has 2 test assets.

DEMOONE
DEMOTWO
API Change Log
2025 Changes
December
updated REST API - Get Unconfirmed OTC Trade NEW fields createdAtDatetime, createdAtTimestamp, expireDatetime and expireTimestamp
November
Removed deprecated fields maxPriceLimit, minPriceLimit, maxCostLimit, minCostLimit, makerFee, takerFee from Get Markets
new REST API - Get Unconfirmed OTC Trade
October
new fields in V1CancelAllOrders - V1CancelAllOrders
September
new REST API - Get Expiry Prices
August
new REST API - Get Option Ladder
updated REST API - Get Markets NEW fields strikePrice
updated REST API - Get Market Tick NEW fields bidIVPercentage, askIVPercentage and greeks
new REST API - OTC
new fields at Get Trades - otcMatchId and otcTradeId
new REST API - Market Maker Protection
new WebSocket API - mmpRequest topic for Private Data WebSocket
new WebSocket API - mmpTrigger topic for Private Data WebSocket
new REST API - Get Market Maker Protection Configuration by Trading Account Id
July
new Websocket API - Unified tick for multiple markets
June
new REST API - Get Historical Trades
new REST API - Get Historical Orders
May
Deprecated Features to be removed June 2025:
Hybrid OrderBook WebSocket (unauthenticated)
Market Data WebSocket (authenticated)
Anonymous Trades WebSocket (unauthenticated)
Support for fee rebates - Get Trades new fields tradeRebateAmount and tradeRebateAssetSymbol
March
updated REST API - Get Trading Account new field tradeFees
updated REST API - Get Trading Account Deprecated fields makerFee and takerFee
updated REST API - Get Markets new field feeGroupId
updated REST API - Get Markets Deprecated fields makerFee and takerFee
Removal of request parameter depth from Get Market Orderbook
Removal of subscription parameter depth from unauthenticated multi-orderbook websocket
updated REST API - Order Amendment Commands new command V1AmendOrder
2024 Changes
December
updated REST API - Get Trading Account new field totalLiabilitiesUSD
updated WebSocket API - /private-data topic - tradingAccounts new field totalLiabilitiesUSD
November
updated REST API - Get Trading Account new fields liquidityAddonUSD, marketRiskUSD and marginProfile
updated WebSocket API - /private-data topic - tradingAccounts new fields liquidityAddonUSD, marketRiskUSD and marginProfile
updated REST API - Get Assets new nested fields underlyingAsset
updated REST API - Get Markets new field expiryDatetime
Deprecated REST API - [Perpetual Settlement History]
New REST API - Derivatives Settlement History
Deprecating REST API - GET /trading-api/v1/history/perpetual-settlement
WebSocket API /private-data new topic - derivativesPositionV2
October
New REST API - Portfolio Margin Simulator
September
New REST API - Funding Rate History
updated REST API - Get Markets deprecated fields maxInitialLeverage, warningLeverage, liquidationLeverage, fullLiquidationLeverage and defaultedLeverage
August
New Unified Anonymous Trade WS API
July
updated REST API - Get Trading Account new field isConcentrationRiskEnabled
updated REST API - Get Markets new fields openInterestUSD, concentrationRiskThresholdUSD and concentrationRiskPercentage
updated REST API - Get Markets new fields roundingCorrectionFactor, makerMinLiquidityAddition, liquidityInvestEnabled and liquidityWithdrawEnabled
New APIs
WebSocket /trading-api/v1/index-data for index price updates
REST - GET /trading-api/v1/index-prices
REST - GET /trading-api/v1/index-prices/{assetSymbol}
June
updated REST API - Get Assets new fields name and collateralBands
updated REST API - Get Assets deprecating field collateralRating
May
WebSocket API /private-data new topic - ammInstructions
April
Moved deprecated items to Deprecated Features & APIs
Bullish Key
Old Signing Format
Hybrid OrderBook WebSocket (unauthenticated)
Market Data WebSocket (authenticated)
V1 Orders APIs
V1 AMM Instructions APIs
REST - GET /accounts/spot
REST - GET /accounts/spot/{symbol}
Removed decommissioned items
REST - POST /trading-api/v1/users/login
March
Added POST_ONLY order type for POST /trading-api/v2/orders
Added POST_ONLY order type for GET /markets
WebSocket API /private-data response models contain new field - tradingAccountId
February
Response model changes for GET /trading-api/assets and GET /trading-api/assets/{symbol}
new fields totalOfferedLoanQuantity and loanBorrowedQuantity
new REST API - GET /trading-api/v1/history/transfer
Updated REST API - Get Trading-Accounts new fields totalBorrowedUSD totalCollateralUSD, initialMarginUSD, warningMarginUSD liquidationMarginUSD, fullLiquidationMarginUSD, defaultedMarginUSD, endCustomerId
Updated WS API - /private-data websocket, tradingAccounts response model updated with new fields
January
Added new field quoteAmount for response models
REST - GET /orders
REST - GET /trades
Websocket - orders and trades topic
2023 Changes
December
History APIs require date/time range to be specified.
Direct Connect connectivity option added.
Deprecation of authenticated L1 websocket in favour of unauthenticated multi-orderbook websocket.
Deprecation of unauthenticated per-market L2 websocket in favour of unauthenticated multi-orderbook websocket.
Added test instruments.
November
New APIs for placing commands into the exchange. Uses signing format and allows non-strict precision on price/quantities.
POST /trading-api/v2/orders for creating orders, GET /trading-api/v2/orders for fetching orders.
POST /trading-api/v2/amm-instructions for creating AMM instructions, GET /trading-api/v2/amm-instructions for fetching AMM instructions.
POST /trading-api/v2/command for all other commands.
Deprecation of following APIs, will be removed towards the end of Q3 2024.
/trading-api/v1/orders
/trading-api/v1/amm-instructions
/trading-api/v1/command
Response model changes for GET /trading-api/v2/orders, GET /trading-api/v1/orders and Private Data WebSocket (authenticated) orders topic.
allowBorrow, borrowedBaseQuantity, borrowedQuoteQuantity, clientOrderId added.
margin, borrowedQuantity, handle deprecated, will be removed towards the end of Q3 2024.
Response model changes for GET /trading-api/v2/amm-instructions and GET /trading-api/v1/amm-instructions
instructionId added.
liquidityId deprecated, will be removed towards the end of Q3 2024.
New Multi-OrderBook WebSocket (unauthenticated) API
new REST API - derivatives positions
new REST API - perpetual settlement
updated REST API - Get Markets new fields marketType and new fields for perpetual market only: contractMultiplier,settlementAssetSymbol, underlyingBaseSymbol, underlyingQuoteSymbol
updated REST API - Get Market Tick new fields markPrice fundingRate, openInterest
updated REST API - Get Trading-Accounts new field riskLimitUSD
updated REST API - Get AMM Instruction new field lastDistributedPrice
New Get Market Tick WebSocket API
Websocket - Updated API Private Data WebSocket new Topic derivativesPositions
Websocket - Updated API Private Data WebSocket Topic tradingAccounts, response model updated.
October
New heartbeat topic for Private Data WebSocket (authenticated)
New ECDSA API Keys and ECDSA based signing
Login API - POST /trading-api/v2/users/login supports ECDSA signatures
BX-SIGNATURE header supports signatures generated via ECDSA
September
New HMAC API Keys and HMAC based signing
Login API - GET /v1/users/hmac/login
BX-SIGNATURE header supports signatures generated via HMAC and EDDSA
New FIX API - The FIX API is available to institutional clients
August - New REST API - GET /history/borrow-interest
New REST API - Cancel All Open Limit Orders after Delay - POST /command?commandType=V1DelayedCancelAllOrders
New REST API - logout session - GET /v1/users/logout
July - Margin related REST and WS changes
borrowedQuantity and isLiquidation fields added to GET /orders and WS /private-data orders topic
Calculation for free and used fields changed in GET /accounts/spot, GET /accounts/spot/{symbol} and WS /private-data spotAccounts topic
New GET /accounts/asset and GET /accounts/asset/{symbol}
New assetAccounts and tradingAccounts topics in WS /private-data
isLending, isBorrowing, isDefaulted, maxInitialLeverage, makerFee and takerFee fields added to GET /accounts/trading-accounts
collateralRating and maxBorrow fields added to /assets
May - add V1CancelAllOrdersByMarket to cancel all open orders by trading account id and market
April - add V1CancelAllOrders to cancel all open limit orders by trading account id
April - add /accounts/trading-accounts endpoint to fetch all trading accounts
April - new hybrid orderbook WebSocket API with greater depth and aggregation factor
Private Data WebSocket /v1/private-data -> New API /v1/private-data?tradingAccountId=111234567890
Get account details Current API -> New API
Get trade details Current API -> New API
Get AMM Instruction by ID Current API -> New API
Get AMM instruction details Current API -> New API
Remove AMM instruction Current API -> New API
Add AMM instruction Current API -> New API
Get order details Current API -> New API
Cancel order Current API -> New API
Create order Current API -> New API
Updated REST API:
New REST API: To transfer asset between two trading accounts
New REST API: To retrieve all the trading account details for current user Gets details for all trading accounts accessible by the API key used in the request. Requires bearer token in authorization header. The trading account's id will be used in all other REST API
March - introduce "trading account Id" to authenticated REST API and websocket
March - add custody SIGNET support, remove SEN support
March - add unsolicited amend status reason code
March - add nonce window to /orders to allow out-of-order order requests to be processed
March - /v1/users/login to be deprecated towards the end of Q2 2023
January - add AMM instructions API
2022 Changes
November - deprecate subscription topics in /private-data - events, positions and marginAccounts
November - deprecate /accounts/margin, /accounts/margin/{symbol}, /positions and /positions/{symbol}
October - add Custody API
August - add anonymous trades WebSocket API
July - deprecate WebSocket API /v1/private and /v1/market-data
July - add hybrid orderbook WebSocket API
June - add handle field to GET /trades and GET /trades/{tradeId}
June - add handle field to V1TATrade for private data WebSocket
June - orderbook default depth of 10 - GET /markets/{symbol}/orderbook/hybrid
May - add events topic to private data WebSocket
April - add market data WebSocket API
April - add private data WebSocket API
March - add optional depth parameter to GET /markets/{symbol}/orderbook/hybrid?depth=10
March - add IOC time-in-force order type
March - add FOK time-in-force order type
March - add order statusReasonCode map to API documentation
March - add historical anonymous trades API - GET /history/markets/{symbol}/trades
February - add filter by status=CANCELLED to GET /orders?status=CANCELLED
January - add pagination support to GET /markets/{symbol}/candle
API SERVER
 https://api.exchange.bullish.com/trading-api - PRODUCTION
 https://api.trade.coindesk.com/trading-api - COINDESK PRODUCTION
 https://registered.api.exchange.bullish.com/trading-api - PRODUCTION
 https://prod.access.bullish.com/trading-api - PRODUCTION (Direct Connect)
 https://api.bugbounty.bullish.com/trading-api - SECURITY SANDBOX
 https://api.simnext.bullish-test.com/trading-api - API SANDBOX
 https://api.trade-simnext.coindesk.com/trading-api - COINDESK API SANDBOX
 https://registered.api.simnext.bullish-test.com/trading-api - API SANDBOX
 https://simnext.access.bullish.com/trading-api - API SANDBOX (Direct Connect)
SELECTED: https://api.exchange.bullish.com/trading-api
AUTHENTICATION
No API key applied
HTTP Bearer
Send Authorization in header containing the word Bearer followed by a space and a Token String.
api-token
 
nonce
Non-authenticated API for getting nonce range information

Get The Current Nonce Range
get /v1/nonce
Get the current nonce range. The lower bound of nonce range is EPOCH start of day in microseconds, and upper bound of nonce range is EPOCH end of day in microseconds.

Ratelimited: False

REQUEST
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"lowerBound": 8455,
"upperBound": 9455
}
orders
Authenticated APIs for interacting with orders

Get Orders
get /v2/orders
Retrieve a list of orders placed by a trading account with specified filters.

Only the last 24 hours of data is available for querying
This endpoint requires authentication and supports pagination. To filter by createdAtDatetime and createdAtTimestamp, additional parameters are required. For detailed instructions, see the Filtering Support section. Additionally, this endpoint is subjected to rate limiting.

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
symbol
string
BTCUSDC
Examples: BTCUSDC
clientOrderId
string
299834741023572480
Unique numeric (i64) identifier generated on the client side expressed as a string value

Examples: 299834741023572480
side
enum
BUY
Allowed: BUY ┃ SELL
order side

Examples: BUY
status
enum
OPEN
Allowed: OPEN ┃ CLOSED ┃ CANCELLED ┃ REJECTED
order status

Examples: OPEN
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"clientOrderId": "299834741023572480",
"orderId": "297735387747975680",
"symbol": "BTCUSDC",
"price": "1.00000000",
"averageFillPrice": "1.00000000",
"stopPrice": "1.00000000",
"allowBorrow": false,
"quantity": "1.00000000",
"quantityFilled": "1.00000000",
"quoteAmount": "1.00000000",
"baseFee": "0.00100000",
"quoteFee": "0.0010",
"borrowedBaseQuantity": "1.00000000",
"borrowedQuoteQuantity": "1.00000000",
"isLiquidation": false,
"side": "BUY",
"type": "LMT",
"timeInForce": "GTC",
"status": "OPEN",
"statusReason": "User cancelled",
"statusReasonCode": "1002",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
]
Create Order
post /v2/orders
Creates an order, requires bearer token in authorization header.

This endpoint uses the signing format which does not require strict field ordering and addition of null fields in the request body. Quantities and prices does not require strict precision. Eg. for asset precision of 4 - 100, 100.0, 100.00, 100.000 and 100.0000 are all accepted.

Ratelimited: True. Higher tiers of rate limits available by providing the BX-RATELIMIT-TOKEN request header.

HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
new order request body

EXAMPLE
SCHEMA

CreateLimitOrderCommand
{
  "commandType": "V3CreateOrder",
  "clientOrderId": "1234",
  "symbol": "BTCUSDC",
  "type": "LIMIT",
  "side": "BUY",
  "price": "31000.1",
  "quantity": "1.1",
  "timeInForce": "GTC",
  "allowBorrow": true,
  "tradingAccountId": "111000000000001"
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

BX-NONCE-WINDOW-ENABLED
enum
Default: false
Allowed: false ┃ true
string representation of a boolean value, enables out-of-order order requests to be processed

BX-REFERRER
string
A numeric referrer id if applicable

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. The create order command was successfully acknowledged. To check the current status of the order, query Get Order by ID using the orderId received in the response payload. Please consult the section How To Ensure The Order Of Create Order or Cancel Order Requests for more information.

EXAMPLE
SCHEMA
application/json
Copy
{
"message": "Command acknowledged - CreateOrder",
"requestId": "633910976353665024",
"orderId": "633910775316480001",
"clientOrderId": "1234567"
}
Get Order by ID
get /v2/orders/{orderId}
Retrieve a specific order using its unique identifier.

This endpoint requires authentication and is subjected to rate limiting.

HTTP Bearer
REQUEST
PATH PARAMETERS
* orderId
number
order ID

QUERY-STRING PARAMETERS
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"clientOrderId": "299834741023572480",
"orderId": "297735387747975680",
"symbol": "BTCUSDC",
"price": "1.00000000",
"averageFillPrice": "1.00000000",
"stopPrice": "1.00000000",
"allowBorrow": false,
"quantity": "1.00000000",
"quantityFilled": "1.00000000",
"quoteAmount": "1.00000000",
"baseFee": "0.00100000",
"quoteFee": "0.0010",
"borrowedBaseQuantity": "1.00000000",
"borrowedQuoteQuantity": "1.00000000",
"isLiquidation": false,
"side": "BUY",
"type": "LMT",
"timeInForce": "GTC",
"status": "OPEN",
"statusReason": "User cancelled",
"statusReasonCode": "1002",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
Get Order by clientOrder ID
get /v2/orders/client-order-id/{clientOrderId}
Retrieve a specific order using its unique identifier generated on the client side.

This endpoint requires authentication and is subjected to rate limiting.

HTTP Bearer
REQUEST
PATH PARAMETERS
* clientOrderId
number
unique numeric (i64) identifier generated on the client side

QUERY-STRING PARAMETERS
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"clientOrderId": "299834741023572480",
"orderId": "297735387747975680",
"symbol": "BTCUSDC",
"price": "1.00000000",
"averageFillPrice": "1.00000000",
"stopPrice": "1.00000000",
"allowBorrow": false,
"quantity": "1.00000000",
"quantityFilled": "1.00000000",
"quoteAmount": "1.00000000",
"baseFee": "0.00100000",
"quoteFee": "0.0010",
"borrowedBaseQuantity": "1.00000000",
"borrowedQuoteQuantity": "1.00000000",
"isLiquidation": false,
"side": "BUY",
"type": "LMT",
"timeInForce": "GTC",
"status": "OPEN",
"statusReason": "User cancelled",
"statusReasonCode": "1002",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
Order Cancellation Commands
post /v2/command
Submits a command to the trading engine. A successful response indicates that the command entry was acknowledged but does not indicate that the command was executed. This endpoint uses the signing format which does not require strict field ordering and addition of null fields in the request body. Quantities and prices does not require strict precision. Eg. for asset precision of 4 - 100, 100.0, 100.00, 100.000 and 100.0000 are all accepted.

Command schemas and examples are provided below. Supported commands:

V3CancelOrder
V1CancelAllOrders
V1CancelAllOrdersByMarket
V1DelayedCancelAllOrders
V1UnsetDelayedCancelAllOrders
Requires

bearer token in authorization header
Ratelimited: True. Higher tiers of rate limits available by providing the BX-RATELIMIT-TOKEN request header.

HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
EXAMPLE
SCHEMA

CancelOrderCommand
Only one of orderId or clientOrderId can be used in the cancel order command

{
  "commandType": "V3CancelOrder",
  "orderId": "297735387747975680",
  "symbol": "BTCUSDC",
  "tradingAccountId": "111000000000001"
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

BX-NONCE-WINDOW-ENABLED
enum
Default: false
Allowed: false ┃ true
string representation of a boolean value, enables out-of-order order requests to be processed

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. This means a command was successfully acknowledged.

EXAMPLE
SCHEMA
application/json

CancelOrderResponse
Only one of orderId or clientOrderId present

Copy
{
"message": "Command acknowledged - CancelOrder",
"requestId": "633910976353665024",
"orderId": "633910775316480001"
}
Order Amendment Command
post /v2/command
Ability to amend the price ,quantity and type (i.e. change from Taker Only to Maker only and vice-versa) on Limit orders. It can be applied only to open orders (quantityFilled=0 and status=OPEN).

This submits a command to the trading engine to amend an order. A successful response indicates that the command entry was acknowledged but does not indicate that the command was executed.

This endpoint uses the signing format which does not require strict field ordering and addition of null fields in the request body. Quantities and prices does not require strict precision. Eg. for asset precision of 4 - 100, 100.0, 100.00, 100.000 and 100.0000 are all accepted.

Requires

bearer token in authorization header
Ratelimited: True. Higher tiers of rate limits available by providing the BX-RATELIMIT-TOKEN request header.

HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
EXAMPLE
SCHEMA
{
  "commandType": "V1AmendOrder",
  "orderId": "297735387747975680",
  "symbol": "BTCUSDC",
  "type": "LIMIT",
  "price": "1.00000000",
  "clientOrderId": "633914459442118656",
  "quantity": "1.00000000",
  "tradingAccountId": "111000000000001"
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

BX-NONCE-WINDOW-ENABLED
enum
Default: false
Allowed: false ┃ true
string representation of a boolean value, enables out-of-order order requests to be processed

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. This means a command was successfully acknowledged.

EXAMPLE
SCHEMA
application/json
Copy
{
"message": "Command acknowledged - AmendOrder",
"requestId": "633910976353665024",
"orderId": "633910775316480001",
"clientOrderId": "1234567-1"
}
amm instructions
Authenticated APIs that allow users to Create, View and Terminate AMM instructions.

Please refer to the AMM instruction Overview Doc for more details on how AMM instructions work.

Get AMM Instructions
get /v2/amm-instructions
Gets a list of AMM instructions based on applied filters.

requires bearer token in authorization header
supports pagination
Ratelimited: True

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
symbol
string
BTCUSDC
Examples: BTCUSDC
status
enum
OPEN
Allowed: OPEN ┃ CLOSED
order status

Examples: OPEN
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"instructionId": "297735387747975680",
"symbol": "BTCUSDC",
"baseFee": "1.00000000",
"quoteFee": "1.00000000",
"status": "OPEN",
"statusReason": "Ok",
"statusReasonCode": 1001,
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000",
"24HrApy": "2.3319",
"24HrYieldEarn": "0.00",
"apy": "0.0000",
"baseCurrentQuantity": "0.00000000",
"baseInvestQuantity": "0.00000008",
"basePrice": "345.6700",
"baseWithdrawQuantity": "0.00000010",
"currentValue": "0.0000",
"dislocationEnabled": false,
"feeTierId": "1",
"finalValue": "0.0001",
"impermanentLoss": "0.0000",
"initialBasePrice": "100.0000",
"initialQuotePrice": "0.0100",
"initialValue": "0.0000",
"lowerBound": "0.0013",
"price": "456.7800",
"quoteCurrentQuantity": "0.0000",
"quoteInvestQuantity": "0.0009",
"quotePrice": "1.0000",
"quoteWithdrawQuantity": "0.0011",
"lastDistributedPrice": null
"requestId": "197735387747975680",
"staticSpreadFee": "0.00200000",
"updatedAtDatetime": "2025-05-20T01:01:01.000Z",
"updatedAtTimestamp": "1621490985000",
"upperBound": "14000.0000",
"yieldEarn": "0.00"
}
]
Create AMM Instruction
post /v2/amm-instructions
Creates an AMM instruction, requires bearer token in authorization header.

This endpoint uses the signing format which does not require strict field ordering in the request body. Quantities and prices does not require strict precision. Eg. for asset precision of 4 - 100, 100.0, 100.00, 100.000 and 100.0000 are all accepted.

Ratelimited: True

HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
new AMM instruction

EXAMPLE
SCHEMA
{
  "commandType": "V3CreateAMMInstruction",
  "symbol": "BTCUSDC",
  "baseQuantity": "0",
  "quoteQuantity": "50000.1",
  "upperBound": "25000",
  "lowerBound": "20000",
  "feeTierId": "1",
  "tradingAccountId": "111000000000001"
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. This means a create AMM instruction command was successfully acknowledged. It does not necessarily mean the instruction was created. To check the current status, query Get AMM Instruction by ID using the instructionId received in the response payload.

EXAMPLE
SCHEMA
application/json
Copy
{
"message": "Command acknowledged - CreateAMMInstruction",
"requestId": "633906221577404416",
"instructionId": "633906221577404424"
}
Get AMM Instruction by ID
get /v2/amm-instructions/{instructionId}
Gets a specific AMM instruction based on the instructionId, requires bearer token in authorization header

Ratelimited: True

HTTP Bearer
REQUEST
PATH PARAMETERS
* instructionId
number
unique AMM instruction ID

QUERY-STRING PARAMETERS
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"instructionId": "297735387747975680",
"symbol": "BTCUSDC",
"baseFee": "1.00000000",
"quoteFee": "1.00000000",
"status": "OPEN",
"statusReason": "Ok",
"statusReasonCode": 1001,
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000",
"24HrApy": "2.3319",
"24HrYieldEarn": "0.00",
"apy": "0.0000",
"baseCurrentQuantity": "0.00000000",
"baseInvestQuantity": "0.00000008",
"basePrice": "345.6700",
"baseWithdrawQuantity": "0.00000010",
"currentValue": "0.0000",
"dislocationEnabled": false,
"feeTierId": "1",
"finalValue": "0.0001",
"impermanentLoss": "0.0000",
"initialBasePrice": "100.0000",
"initialQuotePrice": "0.0100",
"initialValue": "0.0000",
"lowerBound": "0.0013",
"price": "456.7800",
"quoteCurrentQuantity": "0.0000",
"quoteInvestQuantity": "0.0009",
"quotePrice": "1.0000",
"quoteWithdrawQuantity": "0.0011",
"lastDistributedPrice": null
"requestId": "197735387747975680",
"staticSpreadFee": "0.00200000",
"updatedAtDatetime": "2025-05-20T01:01:01.000Z",
"updatedAtTimestamp": "1621490985000",
"upperBound": "14000.0000",
"yieldEarn": "0.00"
}
Create Command
post /v2/command
Submits a command to the trading engine. A successful response indicates that the command entry was acknowledged but does not indicate that the command was executed. This endpoint uses the signing format which does not require strict field ordering and addition of null fields in the request body. Quantities and prices does not require strict precision. Eg. for asset precision of 4 - 100, 100.0, 100.00, 100.000 and 100.0000 are all accepted.

Command schemas and examples are provided below. Supported commands:

V3CancelOrder
V1CancelAllOrders
V1CancelAllOrdersByMarket
V1DelayedCancelAllOrders
V1UnsetDelayedCancelAllOrders
V1AmendOrder
V3TerminateAMMInstruction
V2TransferAsset
Requires

bearer token in authorization header
Ratelimited: True. Higher tiers of rate limits available by providing the BX-RATELIMIT-TOKEN request header.

HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
EXAMPLE
SCHEMA

CancelOrderCommand
Only one of orderId or clientOrderId can be used in the cancel order command

{
  "commandType": "V3CancelOrder",
  "orderId": "297735387747975680",
  "symbol": "BTCUSDC",
  "tradingAccountId": "111000000000001"
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

BX-NONCE-WINDOW-ENABLED
enum
Default: false
Allowed: false ┃ true
string representation of a boolean value, enables out-of-order order requests to be processed

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. This means a command was successfully acknowledged.

EXAMPLE
SCHEMA
application/json

CancelOrderResponse
Only one of orderId or clientOrderId present

Copy
{
"message": "Command acknowledged - CancelOrder",
"requestId": "633910976353665024",
"orderId": "633910775316480001"
}
transfers
Authenticated API for initiating asset transfers between trading accounts.

Create Command
post /v2/command
Submits a command to the trading engine. A successful response indicates that the command entry was acknowledged but does not indicate that the command was executed. This endpoint uses the signing format which does not require strict field ordering and addition of null fields in the request body. Quantities and prices does not require strict precision. Eg. for asset precision of 4 - 100, 100.0, 100.00, 100.000 and 100.0000 are all accepted.

Command schemas and examples are provided below. Supported commands:

V3CancelOrder
V1CancelAllOrders
V1CancelAllOrdersByMarket
V1DelayedCancelAllOrders
V1UnsetDelayedCancelAllOrders
V1AmendOrder
V3TerminateAMMInstruction
V2TransferAsset
Requires

bearer token in authorization header
Ratelimited: True. Higher tiers of rate limits available by providing the BX-RATELIMIT-TOKEN request header.

HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
EXAMPLE
SCHEMA

CancelOrderCommand
Only one of orderId or clientOrderId can be used in the cancel order command

{
  "commandType": "V3CancelOrder",
  "orderId": "297735387747975680",
  "symbol": "BTCUSDC",
  "tradingAccountId": "111000000000001"
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

BX-NONCE-WINDOW-ENABLED
enum
Default: false
Allowed: false ┃ true
string representation of a boolean value, enables out-of-order order requests to be processed

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. This means a command was successfully acknowledged.

EXAMPLE
SCHEMA
application/json

CancelOrderResponse
Only one of orderId or clientOrderId present

Copy
{
"message": "Command acknowledged - CancelOrder",
"requestId": "633910976353665024",
"orderId": "633910775316480001"
}
command entry
Authenticated API for submitting commands into the exchange.

Create Command
post /v2/command
Submits a command to the trading engine. A successful response indicates that the command entry was acknowledged but does not indicate that the command was executed. This endpoint uses the signing format which does not require strict field ordering and addition of null fields in the request body. Quantities and prices does not require strict precision. Eg. for asset precision of 4 - 100, 100.0, 100.00, 100.000 and 100.0000 are all accepted.

Command schemas and examples are provided below. Supported commands:

V3CancelOrder
V1CancelAllOrders
V1CancelAllOrdersByMarket
V1DelayedCancelAllOrders
V1UnsetDelayedCancelAllOrders
V1AmendOrder
V3TerminateAMMInstruction
V2TransferAsset
Requires

bearer token in authorization header
Ratelimited: True. Higher tiers of rate limits available by providing the BX-RATELIMIT-TOKEN request header.

HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
EXAMPLE
SCHEMA

CancelOrderCommand
Only one of orderId or clientOrderId can be used in the cancel order command

{
  "commandType": "V3CancelOrder",
  "orderId": "297735387747975680",
  "symbol": "BTCUSDC",
  "tradingAccountId": "111000000000001"
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

BX-NONCE-WINDOW-ENABLED
enum
Default: false
Allowed: false ┃ true
string representation of a boolean value, enables out-of-order order requests to be processed

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. This means a command was successfully acknowledged.

EXAMPLE
SCHEMA
application/json

CancelOrderResponse
Only one of orderId or clientOrderId present

Copy
{
"message": "Command acknowledged - CancelOrder",
"requestId": "633910976353665024",
"orderId": "633910775316480001"
}
custody
Authenticated APIs for custody, Custody Basic Examples

Custody APIs have a limit of 40 requests per IP, per minute. This is combined across all endpoints of type /wallets/*

Get Custody Transaction History
get /v1/wallets/transactions
Get custody transaction history, requires bearer token in authorization header

Please note that Custody endpoints utilize a non-multiplied asset format for long decimal assets like SHIB and PEPE, ensuring consistency with real-world asset representation. This differs from Trading endpoints, which use a multiplied asset format, such as SHIB1M and PEPE1M. For more information, please see help centre

Note on Source Address for Token Transfers (ERC-20, SPL, TRC-20): The source address for tokens following standards like ERC-20, SPL and TRC-20 may not be the originator wallet that broadcasts a transaction. If the transfer is executed by a smart contract or program, the visible source address may represent the account executing the token logic, not the external user who initiated the transfer (Externally Owned Account).

supports pagination
Ratelimited: True - see custody limits

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
createdAtDatetime[gte]
date-time
2025-05-20T01:01:01.000Z
start timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
createdAtDatetime[lte]
date-time
2025-05-20T01:01:01.000Z
end timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
custodyTransactionId
string
DB:9e6304a08c9cc2a33e6bc6429a088eae2a6b940c8e312aede3a3780257b9b979
Custody transaction Id

Examples: DB:9e6304a08c9cc2a33e6bc6429a088eae2a6b940c8e312aede3a3780257b9b979
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"custodyTransactionId": "DB:9e6304a08c9cc2a33e6bc6429a088eae2a6b940c8e312aede3a3780257b9b979",
"direction": "DEPOSIT",
"quantity": "100000.00",
"symbol": "USDC",
"network": "ETH",
"fee": "3.00",
"memo": "925891241",
"createdAtDateTime": "2022-09-16T07:56:15.000Z",
"status": "COMPLETE",
"statusReason": "OK",
"statusReasonCode": 1001,
"transactionDetails": {
"address": "0xb0a64d976972d87b0783eeb1ff88306cd1891f02",
"blockchainTxId": "0xec557f2c7278d2dae2d98a27b9bd43f386789a4209090cbbd11595f1bed4a4c2",
"swiftUetr": "b55aa5cd-baa2-4122-8c17-ae9b856ae36a",
"sources": [
{
"address": "0xb0a64d976972d87b0783eeb1ff88306cd1891f02"
}
]
}
}
]
Get Withdrawal Limits for Symbol
get /v1/wallets/limits/{symbol}
Get withdrawal limits for symbol, requires bearer token in authorization header

Please note that Custody endpoints utilize a non-multiplied asset format for long decimal assets like SHIB and PEPE, ensuring consistency with real-world asset representation. This differs from Trading endpoints, which use a multiplied asset format, such as SHIB1M and PEPE1M. For more information, please see help centre

Ratelimited: True - see custody limits

HTTP Bearer
REQUEST
PATH PARAMETERS
* symbol
string
USDC
Examples: USDC
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"symbol": "USDC",
"available": "20000.0",
"twentyFourHour": "1000000.00"
}
Get Deposit Instructions for Crypto
get /v1/wallets/deposit-instructions/crypto/{symbol}
Get deposit instructions, requires bearer token in authorization header

Please note that Custody endpoints utilize a non-multiplied asset format for long decimal assets like SHIB and PEPE, ensuring consistency with real-world asset representation. This differs from Trading endpoints, which use a multiplied asset format, such as SHIB1M and PEPE1M. For more information, please see help centre

Ratelimited: True - see custody limits

HTTP Bearer
REQUEST
PATH PARAMETERS
* symbol
string
USDC
Examples: USDC
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"network": "ETH",
"symbol": "USDC",
"address": "0xb0a64d976972d87b0783eeb1ff88306cd1891f02",
"minimumDepositAmount": "0.01"
}
]
Get Withdrawal Instructions for Crypto
get /v1/wallets/withdrawal-instructions/crypto/{symbol}
Get crypto withdrawal instructions, requires bearer token in authorization header. Please note that all withdrawal addresses must be whitelisted via the Bullish website before any digital asset withdrawals can be processed.

Please note that Custody endpoints utilize a non-multiplied asset format for long decimal assets like SHIB and PEPE, ensuring consistency with real-world asset representation. This differs from Trading endpoints, which use a multiplied asset format, such as SHIB1M and PEPE1M. For more information, please see help centre

Ratelimited: True - see custody limits

HTTP Bearer
REQUEST
PATH PARAMETERS
* symbol
string
USDC
Examples: USDC
QUERY-STRING PARAMETERS
signed
boolean
true
Examples: true
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"network": "ETH",
"symbol": "USDC",
"address": "0xb0a64d976972d87b0783eeb1ff88306cd1891f02",
"fee": "3.00",
"label": "Our cold wallet",
"destinationId": "1560ec0b406c0d909bb9f5f827dd6aa14a1f638884f33a2a3134878102e78038",
"minimumWithdrawalAmount": "0.01",
"vaspName": "Bullish",
"userWalletType": "HOSTED",
"signed": true
}
]
Get Deposit Instructions for Fiat
get /v1/wallets/deposit-instructions/fiat/{symbol}
Get deposit instructions, requires bearer token in authorization header

Ratelimited: True - see custody limits

HTTP Bearer
REQUEST
PATH PARAMETERS
* symbol
string
USD
Examples: USD
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"network": "SWIFT",
"symbol": "USD",
"accountNumber": "5090022533",
"name": "Bullish (GI) Limited",
"physicalAddress": "26/F, The Centrium, 60 Wyndham Street, Central, Hong Kong",
"memo": "8VZPKSGPA",
"bank": {
"name": "Silvergate Bank",
"physicalAddress": "4250 Executive Square Suite 300 La Jolla, CA 92037",
"routingCode": "322286803"
}
}
]
Get Withdrawal Instructions for Fiat
get /v1/wallets/withdrawal-instructions/fiat/{symbol}
Get withdrawal instructions added by the user, requires bearer token in authorization header. Please note that before withdrawal destinations can be used for withdrawing to, they must be whitelisted on the Bullish website.

Ratelimited: True - see custody limits

HTTP Bearer
REQUEST
PATH PARAMETERS
* symbol
string
USD
Examples: USD
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"destinationId": "1560ec0b406c0d909bb9f5f827dd6aa14a1f638884f33a2a3134878102e78038",
"accountNumber": "9873481227",
"network": "SWIFT",
"symbol": "USD",
"name": "Silvergate Bank",
"physicalAddress": "4250 Executive Square Suite 300 La Jolla, CA 92037",
"fee": "3.00",
"memo": "MZAXEMRXA",
"bank": {
"name": "Silvergate Bank",
"physicalAddress": "4250 Executive Square Suite 300 La Jolla, CA 92037",
"routingCode": "322286803"
},
"intermediaryBank": {
"name": "Middle Bank",
"physicalAddress": "523 Exchange Square, Canary Wharf, E14 2WA",
"routingCode": "321176234"
}
}
]
Initiate Self-Hosted Wallet Verification
post /v1/wallets/self-hosted/initiate
This endpoint is used for initiating wallet verification requests.

Note: users will have 24 hours to complete the wallet verification by sending the exact total amount to the Bullish deposit address provided.

Ratelimited: True - see custody limits

HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
Self hosted wallet verification request

EXAMPLE
SCHEMA
{
  "network": "ETH",
  "symbol": "USDC",
  "address": "0xb0a64d976972d87b0783eeb1ff88306cd1891f02",
  "label": "Our cold wallet",
  "requestedDepositAmount": "12.3456"
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"destinationId": "1560ec0b406c0d909bb9f5f827dd6aa14a1f638884f33a2a3134878102e78038",
"network": "ETH",
"symbol": "USDC",
"depositAddress": "0xb0a64d976972d87b0783eeb1ff88306cd1891f02",
"requestedDepositAmount": "12.3456",
"verificationAmount": "0.0012",
"totalDepositAmount": "12.3468",
"verificationExpiryTime": "2025-05-20T01:01:01.000Z"
}
Get a List of Self-Hosted Wallet Verification Attempts
get /v1/wallets/self-hosted/verification-attempts
This endpoint provides a history of all Wallet Verification attempts, including those that are completed, pending verification and expired.

Ratelimited: True - see custody limits

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
address
string
0xb0a64d976972d87b0783eeb1ff88306cd1891f02
Examples: 0xb0a64d976972d87b0783eeb1ff88306cd1891f02
destinationId
string
1560ec0b406c0d909bb9f5f827dd6aa14a1f638884f33a2a3134878102e78038
Examples: 1560ec0b406c0d909bb9f5f827dd6aa14a1f638884f33a2a3134878102e78038
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"destinationId": "1560ec0b406c0d909bb9f5f827dd6aa14a1f638884f33a2a3134878102e78038",
"network": "ETH",
"symbol": "USDC",
"address": "0xb0a64d976972d87b0783eeb1ff88306cd1891f02",
"verificationStatus": "VERIFIED",
"requestedDepositAmount": "12.3456",
"verificationAmount": "0.0012",
"totalDepositAmount": "12.3468",
"verificationExpiryTime": "2025-05-20T01:01:01.000Z"
}
]
Delete Existing Wallet Address
delete /v1/wallets/withdrawal-instructions/{destinationId}
This endpoint is used for deleting any existing withdrawal addresses.

Ratelimited: True - see custody limits

HTTP Bearer
REQUEST
PATH PARAMETERS
* destinationId
string
1560ec0b406c0d909bb9f5f827dd6aa14a1f638884f33a2a3134878102e78038
Examples: 1560ec0b406c0d909bb9f5f827dd6aa14a1f638884f33a2a3134878102e78038
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

Create Withdrawal
post /v1/wallets/withdrawal
Trigger a withdrawal, requires bearer token in authorization header

The BX-SIGNATURE header should be created by signing the request with an ECDSA API Key as follows:

Construct a string that concatenates the following fields:
timestamp - current epoch milliseconds e.g. 1697008474031
nonce - a UUID identifier to protect against replay attacks e.g. 255241a1-2cde-4954-87b1-13beef547960
request method - e.g. POST
request path - e.g. /trading-api/v1/wallets/withdrawal
request body JSON string, removing any spaces and newline characters
Hash the string using a SHA-256 hash function and sign the resulting hexdigest with your <PRIVATE_KEY>.
DER encode the signature, and BASE64 encode the DER encoded signature.
Bullish requires you to whitelist a withdrawal destination address before submitting a withdrawal request. You may view, approve, and manage your list of destination addresses in Account Settings on the Bullish website. If you attempt a withdrawal without first whitelisting an address in Account Settings, then the withdrawal attempt will fail.

For a full example of using the withdrawal endpoint please see the Custody Withdrawal Example

Please note that Custody endpoints utilize a non-multiplied asset format for long decimal assets like SHIB and PEPE, ensuring consistency with real-world asset representation. This differs from Trading endpoints, which use a multiplied asset format, such as SHIB1M and PEPE1M. For more information, please see help centre

The currently supported precisions for withdrawal quantities are as follows. Please note that fees are always specified in units of the symbol itself, not in smaller denominations (e.g. BTC not Satoshi, ETH not Wei) :

Symbol	Precision	Remarks
USD	2dp	
BTC	8dp	
DOGE	8dp	
ETH	8dp	
LTC	8dp	
XRP	6dp	
AAVE	8dp	
CRV	8dp	
LINK	8dp	
MANA	8dp	
MATIC	8dp	
SUSHI	8dp	
UNI	8dp	
USDC	6dp	
USDT	6dp	
SHIB	2dp	Please ensure to use the non-multiplied asset format (e.g., SHIB, PEPE, BONK) when creating withdrawals, as Custody endpoints align with real-world asset representation
PEPE	2dp	Please ensure to use the non-multiplied asset format (e.g., SHIB, PEPE, BONK) when creating withdrawals, as Custody endpoints align with real-world asset representation
BONK	Round to the nearest ten (e.g., 120 or 130, not 125).	Please ensure to use the non-multiplied asset format (e.g., SHIB, PEPE, BONK) when creating withdrawals, as Custody endpoints align with real-world asset representation
Ratelimited: True - see custody limits

HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
withdrawal request

EXAMPLE
SCHEMA
{
  "timestamp": "1621490985000",
  "nonce": "1628376611",
  "authorizer": "03E02367E8C900000500000000000000",
  "command": {
    "commandType": "V1Withdrawal",
    "destinationId": "1560ec0b406c0d909bb9f5f827dd6aa14a1f638884f33a2a3134878102e78038",
    "symbol": "USDC",
    "network": "ETH",
    "quantity": "100000.000001"
  }
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"statusReason": "Withdrawal accepted",
"statusReasonCode": 1001,
"custodyTransactionId": "DB:9e6304a08c9cc2a33e6bc6429a088eae2a6b940c8e312aede3a3780257b9b979"
}
trades
Authenticated APIs for reading trade data

Get Trades
get /v1/trades
Get a list of trades based on specified filters.

requires bearer token in authorization header
Only the last 24 hours of data is available for querying
supports pagination
filtering on createdAtDatetime, createdAtTimestamp requires additional keywords, see filtering support
Ratelimited: True

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
symbol
string
BTCUSDC
Examples: BTCUSDC
orderId
string
297735387747975680
unique order ID

Examples: 297735387747975680
clientOrderId
string
299834741023572480
unique numeric (i64) identifier generated on the client side, only orderId or clientOrderId can be used

Examples: 299834741023572480
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
otcTradeId
string
200000000000000098
unique Bullish otc trade id

Examples: 200000000000000098
clientOtcTradeId
string
20050900225
unique client otc trade id

Examples: 20050900225
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"tradeId": "100020000000000060",
"orderId": "297735387747975680",
"clientOrderId": "299834741023572480",
"symbol": "BTCUSDC",
"price": "1.00000000",
"quantity": "1.00000000",
"quoteAmount": "1.00000000",
"baseFee": "1.00000000",
"quoteFee": "1.00000000",
"side": "BUY",
"isTaker": true,
"tradeRebateAmount": "1.00000000",
"tradeRebateAssetSymbol": "USDC",
"otcMatchId": "15",
"otcTradeId": "200000000000000098",
"clientOtcTradeId": "20050900225",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
]
Get Trade by ID
get /v1/trades/{tradeId}
Gets a trade by ID, requires bearer token in authorization header

Ratelimited: True

HTTP Bearer
REQUEST
PATH PARAMETERS
* tradeId
number
trade ID

QUERY-STRING PARAMETERS
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"tradeId": "100020000000000060",
"orderId": "297735387747975680",
"clientOrderId": "299834741023572480",
"symbol": "BTCUSDC",
"price": "1.00000000",
"quantity": "1.00000000",
"quoteAmount": "1.00000000",
"baseFee": "1.00000000",
"quoteFee": "1.00000000",
"side": "BUY",
"isTaker": true,
"tradeRebateAmount": "1.00000000",
"tradeRebateAssetSymbol": "USDC",
"otcMatchId": "15",
"otcTradeId": "200000000000000098",
"clientOtcTradeId": "20050900225",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
Get Trades by clientOrder ID
get /v1/trades/client-order-id/{clientOrderId}
Gets trade(s) associated with the clientOrderID, requires bearer token in authorization header

Ratelimited: True

HTTP Bearer
REQUEST
PATH PARAMETERS
* clientOrderId
string
299834741023572480
unique numeric (i64) identifier generated on the client side

Examples: 299834741023572480
QUERY-STRING PARAMETERS
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"tradeId": "100020000000000060",
"orderId": "297735387747975680",
"clientOrderId": "299834741023572480",
"symbol": "BTCUSDC",
"price": "1.00000000",
"quantity": "1.00000000",
"quoteAmount": "1.00000000",
"baseFee": "1.00000000",
"quoteFee": "1.00000000",
"side": "BUY",
"isTaker": true,
"tradeRebateAmount": "1.00000000",
"tradeRebateAssetSymbol": "USDC",
"otcMatchId": "15",
"otcTradeId": "200000000000000098",
"clientOtcTradeId": "20050900225",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
accounts
Authenticated APIs for reading account data

Get Asset Accounts
get /v1/accounts/asset
Gets the asset accounts, requires bearer token in authorization header

Ratelimited: True

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"tradingAccountId": "111000000000001",
"assetId": "1",
"assetSymbol": "BTC",
"availableQuantity": "1.00000000",
"borrowedQuantity": "1.00000000",
"lockedQuantity": "1.00000000",
"loanedQuantity": "1.00000000",
"updatedAtDatetime": "2025-05-20T01:01:01.000Z",
"updatedAtTimestamp": "1621490985000"
}
]
Get Asset Account by Symbol
get /v1/accounts/asset/{symbol}
Gets the asset account by symbol, requires bearer token in authorization header

Ratelimited: True

HTTP Bearer
REQUEST
PATH PARAMETERS
* symbol
string
BTC
Examples: BTC
QUERY-STRING PARAMETERS
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"tradingAccountId": "111000000000001",
"assetId": "1",
"assetSymbol": "BTC",
"availableQuantity": "1.00000000",
"borrowedQuantity": "1.00000000",
"lockedQuantity": "1.00000000",
"loanedQuantity": "1.00000000",
"updatedAtDatetime": "2025-05-20T01:01:01.000Z",
"updatedAtTimestamp": "1621490985000"
}
time
Non-authenticated API for reading time data

Get Exchange Time
get /v1/time
Get Current Exchange Time

REQUEST
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"timestamp": "1621490985000",
"datetime": "2025-05-20T01:01:01.000Z"
}
asset-data
Non-authenticated APIs for accessing general asset data information

Get Assets
get /v1/assets
Get supported assets. Clients can ignore test assets.

REQUEST
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"assetId": "1",
"symbol": "BTC",
"name": "Bitcoin",
"precision": "8",
"minBalanceInterest": "1.00000000",
"minFee": "1.00000000",
"apr": "12.50",
"maxBorrow": "10.00000000",
"totalOfferedLoanQuantity": "5.00000000",
"loanBorrowedQuantity": "3.00000000",
"collateralBands": [
{
"collateralPercentage": "95.00",
"bandLimitUSD": "1000000.0000"
}
],
"underlyingAsset": {
"symbol": "BTC",
"assetId": "1",
"bpmMinReturnStart": "40.0000",
"bpmMinReturnEnd": "20.0000",
"bpmMaxReturnStart": "30.0000",
"bpmMaxReturnEnd": "50.0000",
"marketRiskFloorPctStart": "1.00",
"marketRiskFloorPctEnd": "5.00",
"bpmTransitionDateTimeStart": "2024-08-02T12:00:00.000Z",
"bpmTransitionDateTimeEnd": "2024-08-02T18:00:00.000Z"
}
}
]
Get Asset by Symbol
get /v1/assets/{symbol}
Get Asset by Symbol

REQUEST
PATH PARAMETERS
* symbol
string
BTC
Examples: BTC
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"assetId": "1",
"symbol": "BTC",
"name": "Bitcoin",
"precision": "8",
"minBalanceInterest": "1.00000000",
"minFee": "1.00000000",
"apr": "12.50",
"maxBorrow": "10.00000000",
"totalOfferedLoanQuantity": "5.00000000",
"loanBorrowedQuantity": "3.00000000",
"collateralBands": [
{
"collateralPercentage": "95.00",
"bandLimitUSD": "1000000.0000"
}
],
"underlyingAsset": {
"symbol": "BTC",
"assetId": "1",
"bpmMinReturnStart": "40.0000",
"bpmMinReturnEnd": "20.0000",
"bpmMaxReturnStart": "30.0000",
"bpmMaxReturnEnd": "50.0000",
"marketRiskFloorPctStart": "1.00",
"marketRiskFloorPctEnd": "5.00",
"bpmTransitionDateTimeStart": "2024-08-02T12:00:00.000Z",
"bpmTransitionDateTimeEnd": "2024-08-02T18:00:00.000Z"
}
}
market-data
Non-authenticated APIs for accessing general market data information

Get Markets
get /v1/markets
Get Markets. Clients can ignore test markets.

REQUEST
QUERY-STRING PARAMETERS
marketType
enum
SPOT
Allowed: SPOT ┃ PERPETUAL ┃ DATED_FUTURE ┃ OPTION
Market Types to filter markets against

Examples: SPOT
optionType
enum
CALL
Allowed: CALL ┃ PUT
Option Type to filter markets against. If this is present, only Option Markets will be returned

Examples: CALL
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"marketId": "10000",
"symbol": "BTC-USDC-20241004-70000-C",
"baseSymbol": "BTC",
"underlyingBaseSymbol": null
"quoteSymbol": "BTC",
"underlyingQuoteSymbol": null
"quoteAssetId": "1",
"baseAssetId": "1",
"quotePrecision": 4,
"basePrecision": 8,
"pricePrecision": 8,
"quantityPrecision": 8,
"costPrecision": 8,
"priceBuffer": 0.3,
"minQuantityLimit": "1.00000000",
"maxQuantityLimit": "1.00000000",
"timeZone": "Etc/UTC",
"tickSize": "1.00000000",
"liquidityTickSize": "100.0000",
"liquidityPrecision": 4,
"roundingCorrectionFactor": "0.00000001",
"makerMinLiquidityAddition": "5000",
"orderTypes": [
"LMT"
],
"spotTradingEnabled": true,
"marginTradingEnabled": true,
"marketEnabled": true,
"createOrderEnabled": true,
"cancelOrderEnabled": true,
"liquidityInvestEnabled": true,
"liquidityWithdrawEnabled": true,
"feeGroupId": 1,
"feeTiers": [
{
"feeTierId": "1",
"staticSpreadFee": "0.00040000",
"isDislocationEnabled": true
}
],
"marketType": "SPOT",
"contractMultiplier": null
"settlementAssetSymbol": null
"openInterestUSD": null
"concentrationRiskThresholdUSD": null
"concentrationRiskPercentage": null
"expiryDatetime": "2024-10-04T08:00:00.000Z",
"optionStrikePrice": "70000.0000",
"optionType": "CALL",
"premiumCapRatio": "0.10"
}
]
Get Market by Symbol
get /v1/markets/{symbol}
Get Market by Symbol.

REQUEST
PATH PARAMETERS
* symbol
string
BTCUSDC
Examples: BTCUSDC
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"marketId": "10000",
"symbol": "BTC-USDC-20241004-70000-C",
"baseSymbol": "BTC",
"underlyingBaseSymbol": null
"quoteSymbol": "BTC",
"underlyingQuoteSymbol": null
"quoteAssetId": "1",
"baseAssetId": "1",
"quotePrecision": 4,
"basePrecision": 8,
"pricePrecision": 8,
"quantityPrecision": 8,
"costPrecision": 8,
"priceBuffer": 0.3,
"minQuantityLimit": "1.00000000",
"maxQuantityLimit": "1.00000000",
"timeZone": "Etc/UTC",
"tickSize": "1.00000000",
"liquidityTickSize": "100.0000",
"liquidityPrecision": 4,
"roundingCorrectionFactor": "0.00000001",
"makerMinLiquidityAddition": "5000",
"orderTypes": [
"LMT"
],
"spotTradingEnabled": true,
"marginTradingEnabled": true,
"marketEnabled": true,
"createOrderEnabled": true,
"cancelOrderEnabled": true,
"liquidityInvestEnabled": true,
"liquidityWithdrawEnabled": true,
"feeGroupId": 1,
"feeTiers": [
{
"feeTierId": "1",
"staticSpreadFee": "0.00040000",
"isDislocationEnabled": true
}
],
"marketType": "SPOT",
"contractMultiplier": null
"settlementAssetSymbol": null
"openInterestUSD": null
"concentrationRiskThresholdUSD": null
"concentrationRiskPercentage": null
"expiryDatetime": "2024-10-04T08:00:00.000Z",
"optionStrikePrice": "70000.0000",
"optionType": "CALL",
"premiumCapRatio": "0.10"
}
Get Historical Market by Symbol
get /v1/history/markets/{symbol}
Get Historical Market by Symbol. This endpoint will return specified market even if it is expired. Only applicable for this is applicable only for DATED_FUTURE and OPTION markets.

REQUEST
PATH PARAMETERS
* symbol
string
BTC-USDC-20241004-70000-C
Examples: BTC-USDC-20241004-70000-C
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"marketId": "10000",
"symbol": "BTC-USDC-20241004-70000-C",
"baseSymbol": "BTC",
"underlyingBaseSymbol": null
"quoteSymbol": "BTC",
"underlyingQuoteSymbol": null
"quoteAssetId": "1",
"baseAssetId": "1",
"quotePrecision": 4,
"basePrecision": 8,
"pricePrecision": 8,
"quantityPrecision": 8,
"costPrecision": 8,
"priceBuffer": 0.3,
"minQuantityLimit": "1.00000000",
"maxQuantityLimit": "1.00000000",
"timeZone": "Etc/UTC",
"tickSize": "1.00000000",
"liquidityTickSize": "100.0000",
"liquidityPrecision": 4,
"roundingCorrectionFactor": "0.00000001",
"makerMinLiquidityAddition": "5000",
"orderTypes": [
"LMT"
],
"spotTradingEnabled": true,
"marginTradingEnabled": true,
"marketEnabled": true,
"createOrderEnabled": true,
"cancelOrderEnabled": true,
"liquidityInvestEnabled": true,
"liquidityWithdrawEnabled": true,
"feeGroupId": 1,
"feeTiers": [
{
"feeTierId": "1",
"staticSpreadFee": "0.00040000",
"isDislocationEnabled": true
}
],
"marketType": "SPOT",
"contractMultiplier": null
"settlementAssetSymbol": null
"openInterestUSD": null
"concentrationRiskThresholdUSD": null
"concentrationRiskPercentage": null
"expiryDatetime": "2024-10-04T08:00:00.000Z",
"optionStrikePrice": "70000.0000",
"optionType": "CALL",
"premiumCapRatio": "0.10"
}
Get Market Order Book
get /v1/markets/{symbol}/orderbook/hybrid
Get Order Book by Market Symbol

Ratelimited: False

REQUEST
PATH PARAMETERS
* symbol
string
BTCUSDC
symbol to get

Examples: BTCUSDC
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"bids": [
{
"price": "1.00000000",
"priceLevelQuantity": "1.00000000"
}
],
"asks": [
{
"price": "1.00000000",
"priceLevelQuantity": "1.00000000"
}
],
"datetime": "2025-05-20T01:01:01.000Z",
"timestamp": "1621490985000",
"sequenceNumber": 999
}
Get Latest Market Trades
get /v1/markets/{symbol}/trades
Get Market Trades by Market Symbol.

Only the last 24 hours of data is available for querying
return 100 most recent trades
lookup from local cache
Ratelimited: False

REQUEST
PATH PARAMETERS
* symbol
string
BTCUSDC
symbol to get

Examples: BTCUSDC
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"tradeId": "100020000000000060",
"symbol": "BTCUSDC",
"price": "1.00000000",
"quantity": "1.00000000",
"side": "BUY",
"isTaker": true,
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
]
Get Market Tick
get /v1/markets/{symbol}/tick
Get Current Tick by Market Symbol.

return top 100
Ratelimited: False

REQUEST
PATH PARAMETERS
* symbol
string
BTCUSDC
symbol to get. Only perpetual markets are supported.

Examples: BTCUSDC
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000",
"high": "1.00000000",
"low": "1.00000000",
"bestBid": "1.00000000",
"bidIVPercentage": "99.0",
"bidVolume": "1.00000000",
"bestAsk": "1.00000000",
"askIVPercentage": "99.0",
"askVolume": "1.00000000",
"vwap": "1.00000000",
"open": "1.00000000",
"close": "1.00000000",
"last": "1.00000000",
"change": "1.00000000",
"percentage": "1.00000000",
"average": "1.00000000",
"baseVolume": "1.00000000",
"quoteVolume": "1.00000000",
"bancorPrice": "1.00000000",
"markPrice": "19999.00",
"fundingRate": "0.01",
"openInterest": "100000.32452",
"lastTradeDatetime": "2025-05-20T01:01:01.000Z",
"lastTradeTimestamp": "1621490985000",
"lastTradeQuantity": "1.00000000",
"ammData": [
{
"feeTierId": "1",
"bidSpreadFee": "0.00040000",
"askSpreadFee": "0.00040000",
"baseReservesQuantity": "245.56257825",
"quoteReservesQuantity": "3424383.3629",
"currentPrice": "16856.0000",
"tierPrice": "16856.000100200031"
}
],
"optionStrikePrice": "70000",
"optionType": "CALL",
"expiryDateTime": "2025-05-20T01:01:01.000Z",
"greeks": {
"delta": "0.98",
"gamma": "0.98",
"theta": "-0.17",
"vega": "0.05"
}
}
Get Market Candle
get /v1/markets/{symbol}/candle
Get Current OHLCV Candle by Market Symbol

supports pagination
filtering on createdAtDatetime, createdAtTimestamp requires additional keywords, see filtering support
Ratelimited: False

REQUEST
PATH PARAMETERS
* symbol
string
BTCUSDC
Examples: BTCUSDC
QUERY-STRING PARAMETERS
* createdAtDatetime[gte]
date-time
2025-05-20T01:01:01.000Z
start timestamp of window, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
* createdAtDatetime[lte]
date-time
2025-05-20T01:01:01.000Z
end timestamp of window, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
* timeBucket
enum
1m
Allowed: 1m ┃ 5m ┃ 30m ┃ 1h ┃ 6h ┃ 12h ┃ 1d
time bucket size

Examples: 1m
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"open": "1.00000000",
"high": "1.00000000",
"low": "1.00000000",
"close": "1.00000000",
"volume": "1.00000000",
"createdAtTimestamp": "1621490985000",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"publishedAtTimestamp": "1621490985000"
}
]
sessions
Logout
get /v1/users/logout
Logout of the session associated with the JWT. It requires bearer token in authorization header.

Ratelimited: True

HTTP Bearer
REQUEST
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

Login
post /v2/users/login
Login and generate a new session associated with a JWT. Once you log in from an IP, the same IP must be used for the duration of the session for any subsequent requests.

Ratelimited: True

REQUEST
REQUEST BODY
*
application/json
login request body

EXAMPLE
SCHEMA
{
  "publicKey": "PUB_R1_6PTdfWbXvXWQduhcCiRooGHTVpriu15xMqfr7EDq6sWLDj7NjS",
  "signature": "SIG_R1_K35d5hSY5FbNoJwrCfmH6QvPG7m9XmhL2mgWYcSB7q2hKJ2mv39Luck9WBJroSB635ZAXhdg36TYG7QJX1fTidbsMvyE8N",
  "loginPayload": {
    "userId": "12345",
    "nonce": 1621490985,
    "expirationTime": 1621490985,
    "biometricsUsed": false,
    "sessionKey": null
  }
}
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
returns JWT and the authorizer for signing requests

EXAMPLE
SCHEMA
application/json
Copy
{
"authorizer": "03E02367E8C900000500000000000000",
"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic2FuZGVlcCByYWtocmEifQ.wyVq6PlKaldWXtu-jz2hJCvkGl1lM2S7HUKCH8LnXp0"
}
HMAC Login
get /v1/users/hmac/login
Login and generate a new session associated with a JWT using HMAC. Once you log in from an IP, the same IP must be used for the duration of the session for any subsequent requests.

Ratelimited: True

REQUEST
REQUEST HEADERS
* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

* BX-PUBLIC-KEY
string
public key being used to generate the JWT

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
returns JWT and the authorizer for signing requests

EXAMPLE
SCHEMA
application/json
Copy
{
"authorizer": "03E02367E8C900000500000000000000",
"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoic2FuZGVlcCByYWtocmEifQ.wyVq6PlKaldWXtu-jz2hJCvkGl1lM2S7HUKCH8LnXp0"
}
trading-accounts
Get all trading Accounts details
get /v1/accounts/trading-accounts
Gets details for all trading accounts accessible by the API key used in the request. It requires bearer token in authorization header. The trading account's id will be used in all other REST API

Ratelimited: True

HTTP Bearer
REQUEST
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"isBorrowing": "false",
"isLending": "false",
"maxInitialLeverage": "1",
"tradingAccountId": "111000000000001",
"tradingAccountName": "algo trading account",
"tradingAccountDescription": "algo trading account with experimental strategy",
"isPrimaryAccount": "false",
"rateLimitToken": "97d98951b12fb11f330dd9cb1b807d888c702679ee602edcf1ebc6bac17ad63d",
"isDefaulted": "false",
"tradeFeeRate": [
{
"feeGroupId": 1,
"makerFee": "0.00005000",
"takerFee": "0.00005000"
}
],
"riskLimitUSD": "10000.0000",
"totalLiabilitiesUSD": "14000.0000",
"totalBorrowedUSD": "12000.0000",
"totalCollateralUSD": "13000.0000",
"initialMarginUSD": "0000.0000",
"warningMarginUSD": "0000.0000",
"liquidationMarginUSD": "0000.0000",
"fullLiquidationMarginUSD": "0000.0000",
"defaultedMarginUSD": "0000.0000",
"endCustomerId": "PrimeBroker",
"isConcentrationRiskEnabled": true,
"liquidityAddonUSD": "1000.0000",
"marketRiskUSD": "2000.0000",
"marginProfile": {
"initialMarketRiskMultiplierPct": "200.00",
"warningMarketRiskMultiplierPct": "150.00",
"liquidationMarketRiskMultiplierPct": "100.00",
"fullLiquidationMarketRiskMultiplierPct": "75.00",
"defaultedMarketRiskMultiplierPct": "50.00"
}
}
]
Get trading account details by trading account id
get /v1/accounts/trading-accounts/{tradingAccountId}
Gets details for specific trading account by tradingAccountId and API key used in the request. It requires bearer token in authorization header.

Ratelimited: True

HTTP Bearer
REQUEST
PATH PARAMETERS
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"isBorrowing": "false",
"isLending": "false",
"maxInitialLeverage": "1",
"tradingAccountId": "111000000000001",
"tradingAccountName": "algo trading account",
"tradingAccountDescription": "algo trading account with experimental strategy",
"isPrimaryAccount": "false",
"rateLimitToken": "97d98951b12fb11f330dd9cb1b807d888c702679ee602edcf1ebc6bac17ad63d",
"isDefaulted": "false",
"tradeFeeRate": [
{
"feeGroupId": 1,
"makerFee": "0.00005000",
"takerFee": "0.00005000"
}
],
"riskLimitUSD": "10000.0000",
"totalLiabilitiesUSD": "14000.0000",
"totalBorrowedUSD": "12000.0000",
"totalCollateralUSD": "13000.0000",
"initialMarginUSD": "0000.0000",
"warningMarginUSD": "0000.0000",
"liquidationMarginUSD": "0000.0000",
"fullLiquidationMarginUSD": "0000.0000",
"defaultedMarginUSD": "0000.0000",
"endCustomerId": "PrimeBroker",
"isConcentrationRiskEnabled": true,
"liquidityAddonUSD": "1000.0000",
"marketRiskUSD": "2000.0000",
"marginProfile": {
"initialMarketRiskMultiplierPct": "200.00",
"warningMarketRiskMultiplierPct": "150.00",
"liquidationMarketRiskMultiplierPct": "100.00",
"fullLiquidationMarketRiskMultiplierPct": "75.00",
"defaultedMarketRiskMultiplierPct": "50.00"
}
}
Transfer Asset
post /v1/command
Send command to transfer asset between two trading accounts.

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
* commandType
enum
V1TransferAsset
Allowed: V1TransferAsset
The command type, must be 'V1TransferAsset'

Examples: V1TransferAsset
REQUEST BODY
*
application/json
Command for action

EXAMPLE
SCHEMA
{
  "timestamp": "1621490985000",
  "nonce": "123456789",
  "authorizer": "03E02367E8C900000500000000000000",
  "command": {
    "commandType": "V1TransferAsset",
    "assetSymbol": "BTC",
    "quantity": "100",
    "fromTradingAccountId": "111000000000001",
    "toTradingAccountId": "111000000000001"
  }
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. This means the request was successfully acknowledged. It does not necessarily mean the command was successfully executed.

EXAMPLE
SCHEMA
application/json
Copy
{
"message": "Command acknowledged - TransferAsset",
"requestId": "633909659774222336"
}
derivatives
Get derivatives positions
get /v1/derivatives-positions
Get derivatives positions

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
tradingAccountId
string
111000000000001
Id of the trading account. tradingAccountId is mandatory in the query for users with multiple trading accounts. For users with a single trading account, it can be automatically retrieved from the login.

Examples: 111000000000001
symbol
string
BTC-USDC-PERP
Examples: BTC-USDC-PERP
marketType
enum
DATED_FUTURE
Allowed: SPOT ┃ PERPETUAL ┃ DATED_FUTURE ┃ OPTION
Optional - Filter for results by expiry date

Examples: DATED_FUTURE
optionType
enum
CALL
Allowed: CALL ┃ PUT
Optional - Filter for results by option type

Examples: CALL
sort
enum
optionType
Allowed: marketType ┃ optionType
Optional - Sort results by Market Type or Option Type

Examples: optionType
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Derivatives Position of one market for the trading account

Copy
[
{
"tradingAccountId": "111000000000001",
"symbol": "BTC-USDC-PERP",
"side": "BUY",
"quantity": "1.00000000",
"notional": "1.0000",
"entryNotional": "1.0000",
"mtmPnl": "1.0000",
"reportedMtmPnl": "1.0000",
"reportedFundingPnl": "1.0000",
"realizedPnl": "1.0000",
"settlementAssetSymbol": "USDC",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000",
"updatedAtDatetime": "2025-05-20T01:01:01.000Z",
"updatedAtTimestamp": "1621490985000"
}
]
Get Expiry Prices
get /v1/expiry-prices/{symbol}
Retrieves Expiry Price and Expiry Notional for respective Options and Dated Futures markets.

REQUEST
PATH PARAMETERS
* symbol
string
BTC-USDC-20250919-90000-C
Examples: BTC-USDC-20250919-90000-C
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
Retrieve expiry price and expiry notional for options and dated future.

EXAMPLE
SCHEMA
application/json
Copy
{
"symbol": "BTC-USDC-20250912-95000-C",
"expiryPrice": "115123.2512",
"expiryNotional": "20123.3033",
"expiryDatetime": "2018-11-18T00:00:00.000Z",
"expiryTimestamp": "1672041600000"
}
history
Get Historical Orders
get /v2/history/orders
Retrieve a list of orders placed by a trading account with specified filters.

On a single query request you can retrieve data over a 7 day window, with the data available for the last 90 days
This endpoint requires authentication and supports pagination. To filter by createdAtDatetime and createdAtTimestamp, additional parameters are required. For detailed instructions, see the Filtering Support section. Additionally, this endpoint is subjected to rate limiting.

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
symbol
string
BTCUSDC
Examples: BTCUSDC
orderId
string
297735387747975680
Examples: 297735387747975680
clientOrderId
string
299834741023572480
Unique numeric (i64) identifier generated on the client side expressed as a string value

Examples: 299834741023572480
side
enum
BUY
Allowed: BUY ┃ SELL
order side

Examples: BUY
status
enum
OPEN
Allowed: OPEN ┃ CLOSED ┃ CANCELLED ┃ REJECTED
order status

Examples: OPEN
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
createdAtDatetime[gte]
date-time
2025-05-20T01:01:01.000Z
start timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
createdAtDatetime[lte]
date-time
2025-05-20T01:01:01.000Z
end timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"clientOrderId": "299834741023572480",
"orderId": "297735387747975680",
"symbol": "BTCUSDC",
"price": "1.00000000",
"averageFillPrice": "1.00000000",
"stopPrice": "1.00000000",
"allowBorrow": false,
"quantity": "1.00000000",
"quantityFilled": "1.00000000",
"quoteAmount": "1.00000000",
"baseFee": "0.00100000",
"quoteFee": "0.0010",
"borrowedBaseQuantity": "1.00000000",
"borrowedQuoteQuantity": "1.00000000",
"isLiquidation": false,
"side": "BUY",
"type": "LMT",
"timeInForce": "GTC",
"status": "OPEN",
"statusReason": "User cancelled",
"statusReasonCode": "1002",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
]
Get Historical Trades
get /v1/history/trades
Get a list of trades based on specified filters.

requires bearer token in authorization header
On a single query request you can retrieve data over a 7 day window, with the data available for the last 90 days
supports pagination
filtering on createdAtDatetime, createdAtTimestamp requires additional keywords, see filtering support
Ratelimited: True

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
symbol
string
BTCUSDC
Examples: BTCUSDC
orderId
string
297735387747975680
unique order ID

Examples: 297735387747975680
tradeId
string
100020000000000060
unique trade ID

Examples: 100020000000000060
clientOrderId
string
299834741023572480
unique numeric (i64) identifier generated on the client side, only orderId or clientOrderId can be used

Examples: 299834741023572480
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
createdAtDatetime[gte]
date-time
2025-05-20T01:01:01.000Z
start timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
createdAtDatetime[lte]
date-time
2025-05-20T01:01:01.000Z
end timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
otcTradeId
string
200000000000000098
unique Bullish otc trade id

Examples: 200000000000000098
clientOtcTradeId
string
20050900225
unique client otc trade id

Examples: 20050900225
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"tradeId": "100020000000000060",
"orderId": "297735387747975680",
"clientOrderId": "299834741023572480",
"symbol": "BTCUSDC",
"price": "1.00000000",
"quantity": "1.00000000",
"quoteAmount": "1.00000000",
"baseFee": "1.00000000",
"quoteFee": "1.00000000",
"side": "BUY",
"isTaker": true,
"tradeRebateAmount": "1.00000000",
"tradeRebateAssetSymbol": "USDC",
"otcMatchId": "15",
"otcTradeId": "200000000000000098",
"clientOtcTradeId": "20050900225",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
]
Get Historical Hourly Derivatives Settlement
get /v1/history/derivatives-settlement
Get historical derivatives settlement.

supports pagination
filtering on settlementDatetime requires additional keywords, see filtering support
On a single query request you can retrieve data over a 7 day window, with the data available for the last 90 days. By default the results are returned and sorted in descending order if specific settlement datetime is not specified.
HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
tradingAccountId
string
111000000000001
Id of the trading account. tradingAccountId is mandatory in the query for users with multiple trading accounts. For users with a single trading account, it can be automatically retrieved from the login.

Examples: 111000000000001
symbol
string
BTC-USDC-PERP
Examples: BTC-USDC-PERP
* settlementDatetime[gte]
date-time
2025-05-20T01:01:01.000Z
start timestamp of window, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
* settlementDatetime[lte]
date-time
2025-05-20T01:01:01.000Z
end timestamp of window, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Derivatives Settlement of one market for the trading account

Copy
[
{
"tradingAccountId": "111000000000001",
"symbol": "BTC-USDC-PERP",
"side": "BUY",
"settlementQuantity": "1.00000000",
"deltaTradingQuantity": "1.00000000",
"mtmPnl": "1.0000",
"fundingPnl": "1.0000",
"eventType": "settlementUpdate",
"settlementMarkPrice": "1.0000",
"settlementIndexPrice": "1.0000",
"settlementFundingRate": "10.0",
"settlementDatetime": "2025-05-20T01:01:01.000Z",
"settlementTimestamp": "1621490985000"
}
]
Get Historical Account Transfer
get /v1/history/transfer
Get historical transfers.

supports pagination
filtering on createdAtDatetime and createdAtTimestamp requires additional keywords, see filtering support
On a single query request you can retrieve data over a 7 day window, with the data available for the last 90 days
HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
tradingAccountId
string
111000000000001
Id of the trading account. tradingAccountId is mandatory in the query for users with multiple trading accounts. For users with a single trading account, it can be automatically retrieved from the login.

Examples: 111000000000001
status
string
CLOSED
Default: CLOSED
Status of the transfer request. Defaults to CLOSED

Examples: CLOSED
requestId
string
561287547935260672
Unique identifier of the transfer request

Examples: 561287547935260672
assetSymbol
string
BTC
Asset symbol of the transfer request

Examples: BTC
* createdAtDatetime[gte]
date-time
2025-05-20T01:01:01.000Z
start datetime of window, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
* createdAtDatetime[lte]
date-time
2025-05-20T01:01:01.000Z
end datetime of window, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Get account transfer history

Copy
[
{
"requestId": "1",
"toTradingAccountId": "111000000000001",
"fromTradingAccountId": "121000000000001",
"assetSymbol": "BTC",
"quantity": "1.00000000",
"status": "CLOSED",
"statusReasonCode": "6002",
"statusReason": "Executed",
"createdAtTimestamp": "1621490985000",
"createdAtDatetime": "2025-05-20T01:01:01.000Z"
}
]
Get Historical Market Trades
get /v1/history/markets/{symbol}/trades
Get Historical Market Trades by Market Symbol. Supports querying of up to 7 days of data at a time.

supports pagination
Ratelimited: False

On a single query request you can retrieve data over a 7 day window, with the data available for the last 90 days
REQUEST
PATH PARAMETERS
* symbol
string
BTCUSDC
symbol to get

Examples: BTCUSDC
QUERY-STRING PARAMETERS
createdAtDatetime[gte]
date-time
2025-05-20T01:01:01.000Z
start timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
createdAtDatetime[lte]
date-time
2025-05-20T01:01:01.000Z
end timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"tradeId": "100020000000000060",
"symbol": "BTCUSDC",
"price": "1.00000000",
"quantity": "1.00000000",
"side": "BUY",
"isTaker": true,
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
]
Get Historical Funding Rate
get /v1/history/markets/{symbol}/funding-rate
Get historical hourly funding rate for the requested perpetual market

supports pagination
On a single query request you can retrieve data over a 7 day window, with the data available for the last 90 days
REQUEST
PATH PARAMETERS
* symbol
string
BTC-USDC-PERP
symbol to get

Examples: BTC-USDC-PERP
QUERY-STRING PARAMETERS
updatedAtDatetime[gte]
date-time
2025-05-20T01:01:01.000Z
start timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
updatedAtDatetime[lte]
date-time
2025-05-20T01:01:01.000Z
end timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Hourly Funding Rate History of one market

Copy
[
[
{
"fundingRate": "0.1",
"updatedAtDatetime": "2024-09-16T12:59:59.000Z"
}
]
]
Get Historical Hourly Borrow Interest
get /v1/history/borrow-interest
Get Historical Hourly Borrow Interest. Each entry denotes the hourly quantities for the specific asset. Total borrowed quantity is inclusive of interest. interest = totalBorrowedQuantity - borrowedQuantity which denotes the interest charged in the particular hour for the asset.

supports pagination
filtering createdAtDatetime, createdAtTimestamp requires additional keywords, see filtering support
On a single query request you can retrieve data over a 7 day window, with the data available for the last 90 days
Ratelimited: True

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
tradingAccountId
string
111000000000001
Id of the trading account. tradingAccountId is mandatory in the query for users with multiple trading accounts. For users with a single trading account, it can be automatically retrieved from the login.

Examples: 111000000000001
* assetSymbol
string
BTC
Examples: BTC
* createdAtDatetime[gte]
date-time
2025-05-20T01:01:01.000Z
start timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
* createdAtDatetime[lte]
date-time
2025-05-20T01:01:01.000Z
end timestamp of period, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"assetId": "1",
"assetSymbol": "BTC",
"borrowedQuantity": "1.00000000",
"totalBorrowedQuantity": "1.00000000",
"createdAtDatetime": "2020-08-21T08:00:00.000Z",
"createdAtTimestamp": "1621490985000"
}
]
market-maker-protection(MMP)
Get Market Marker Protection Configuration By Trading Account Id
get /v2/mmp-configuration
Get market maker protection configurations under a trading account id

This endpoint requires authentication. To filter by symbol, additional parameters are required. For detailed instructions, see the Filtering Support section.

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
symbol
string
BTC
The underlying asset id you filter the configurations against. If symbol is provided, this API will only return the market maker protection configuration for this symbol for this trading account.

Examples: BTC
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. This means a command was successfully acknowledged.

EXAMPLE
SCHEMA
application/json
Copy
{
"tradingAccountId": "111000000000001",
"message": null
"mmpConfigurations": [
{
"underlyingAssetSymbol": "BTC",
"windowTimeInSeconds": 60,
"frozenTimeInSeconds": 120,
"quantityLimit": "100",
"deltaLimit": "10",
"isActive": true
}
]
}
Setup Market Maker Protection (MMP)
post /v2/mmp-configuration
MMP configurations are setup per underlying asset symbol for a specific trading Account. While setting up MMP configurations you can specify windowTimeInSeconds, frozenTimeInSeconds, quantityLimit and deltaLimit and use it as best suited. Please reach out to your relationship manager to understand how to enable MMP for your trading accounts.

To get updates on the status of your set / reset MMP configs request for an underlying asset symbol over WS ,please subscribe to mmpRequest TOPIC within the Private Data WebSocket.
To get updates about MMP triggered event over WS ,please subscribe to the mmpTriggered TOPIC within the Private Data WebSocket.
To update/amend your MMP configs, please use the ResetMMPCommandV1 to reset the MMP configurations, followed by setting up a new MMP config via setMMPCommandV1 per underlying asset symbol.

Notes:

MMP is only applicable for Options Orders created with the isMMP flag set to true.
ResetMMPCommandV1 will trigger only when there are no isMMP=true open orders on the account
HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
EXAMPLE
SCHEMA

SetMMPCommandV1
{
  "commandType": "V1SetMMP",
  "tradingAccountId": "123567443543",
  "underlyingAssetSymbol": "BTC",
  "windowTimeInSeconds": "10",
  "frozenTimeInSeconds": "5",
  "quantityLimit": "10",
  "deltaLimit": "1"
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. This means a command was successfully acknowledged.

EXAMPLE
SCHEMA
application/json

SetMMPCommandResponse
Copy
{
"message": "Command acknowledged - SetMMPConfig",
"requestId": "633910976353665025"
}
index-data
Get Index Prices
get /v1/index-prices
Retrieves the index price of all supported assets

REQUEST
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"assetSymbol": "BTC",
"price": "66100.0000",
"updatedAtDatetime": "2025-05-20T01:01:01.000Z",
"updatedAtTimestamp": "1621490985000"
}
]
Get Index Price by Asset Symbol
get /v1/index-prices/{assetSymbol}
Retrieves the index price of a specified asset

REQUEST
PATH PARAMETERS
* assetSymbol
string
BTC
Examples: BTC
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"assetSymbol": "BTC",
"price": "66100.0000",
"updatedAtDatetime": "2025-05-20T01:01:01.000Z",
"updatedAtTimestamp": "1621490985000"
}
option-ladder
Get Option Ladder
get /v1/option-ladder
Returns the available options contracts. This data helps traders quickly assess the available options and their respective prices, implied volatilities, and Greeks (such as delta, gamma, theta, and vega).

REQUEST
QUERY-STRING PARAMETERS
* baseSymbol
string
BTC
symbol to get

Examples: BTC
expiry
date
20250520
Optional - Filter results by expiry date of the option markets

Examples: 20250520
type
enum
CALL
Allowed: CALL ┃ PUT
Optional - Filter results by type (CALL or PUT) of the option markets

Examples: CALL
sort
enum
optionType
Allowed: optionType ┃ expiryDatetime
Optional - Sort results by Option Type or Expiry Datetime

Examples: optionType
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Option Ladder Response

Copy
[
{
"symbol": "BTC-USDC-20241004-70000-C",
"baseSymbol": "BTC",
"settlementAssetSymbol": "USDC",
"bidQuantity": "0.0",
"askQuantity": "0.0",
"bidIVPercentage": "99.0",
"askIVPercentage": "99.0",
"bid": "90000.0000",
"ask": "90000.0000",
"underlyingPrice": "100000.0000",
"optionStrikePrice": "90000",
"markPrice": "100.0000",
"quantity": "1000",
"openInterest": "0.11442400",
"openInterestUSD": "1144240.0000",
"optionType": "CALL",
"expiryDatetime": "2025-05-20T01:01:01.000Z",
"greeks": {
"delta": "0.98",
"gamma": "0.98",
"theta": "-0.17",
"vega": "0.05"
}
}
]
Get Option Ladder for market
get /v1/option-ladder/{symbol}
Returns the for a given baseSymbol, organised by strike prices and expiration dates. This data helps traders quickly assess the available options and their respective prices, implied volatilities, and Greeks (such as delta, gamma, theta, and vega).

REQUEST
PATH PARAMETERS
* symbol
string
BTC-USDC-20241004-70000-C
symbol to get. Only option markets are supported.

Examples: BTC-USDC-20241004-70000-C
API Server
https://api.exchange.bullish.com/trading-api
Authentication
Not Required
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Option Ladder Response

Copy
{
"symbol": "BTC-USDC-20241004-70000-C",
"baseSymbol": "BTC",
"settlementAssetSymbol": "USDC",
"bidQuantity": "0.0",
"askQuantity": "0.0",
"bidIVPercentage": "99.0",
"askIVPercentage": "99.0",
"bid": "90000.0000",
"ask": "90000.0000",
"underlyingPrice": "100000.0000",
"optionStrikePrice": "90000",
"markPrice": "100.0000",
"quantity": "1000",
"openInterest": "0.11442400",
"openInterestUSD": "1144240.0000",
"optionType": "CALL",
"expiryDatetime": "2025-05-20T01:01:01.000Z",
"greeks": {
"delta": "0.98",
"gamma": "0.98",
"theta": "-0.17",
"vega": "0.05"
}
}
portfolio-margin-simulator
Portfolio Margin Simulator
post /v1/simulate-portfolio-margin
Use Portfolio margin simulator to determine your margin requirements and risk levels based on your current portfolio balances. You can also append position details on top of your portfolio specifics to see simulated results.

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
includeExisting
true or false
true
Examples: true
REQUEST BODY
application/json
EXAMPLE
SCHEMA
{
  "tradingAccountId": "111000000000001",
  "positions": [
    {
      "symbol": "BTC-USDC-PERP",
      "quantity": "1.0"
    }
  ],
  "orders": [
    {
      "symbol": "BTCUSDC",
      "quantity": "1.0",
      "limitPrice": "10000.0"
    }
  ],
  "referencePrices": [
    {
      "symbol": "BTC",
      "price": "12000.0"
    }
  ]
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Simulation result

Copy
{
"collateralUSD": "13000.0000",
"borrowedUSD": "12000.0000",
"initialMarginUSD": "14000.0000",
"warningMarginUSD": "15000.0000",
"liquidationMarginUSD": "16000.0000",
"fullLiquidationMarginUSD": "17000.0000",
"defaultedMarginUSD": "18000.0000",
"liquidityAddonUSD": "19000.0000",
"marketRiskUSD": "20000.0000"
}
OTC
The OTC Clearing Facility API (OTC API) is available to customers to book trades negotiated outside of the Bullish Exchange order book to Bullish’s clearing and settlement platform. Customers may agree to an OTC transaction through bilateral negotiations or via a 3rd party RFQ platform. Once the two customers agree on the trade details, they can use the OTC API to book the trade to their Bullish account to benefit from Bullish’s risk and collateral management system. For purposes of clarity, the OTC API is not for trading purposes.

Get OTC Trades
get /v2/otc-trades
Get the otc trade list based on specified filters.

requires bearer token in authorization header
supports pagination
supports filtering on status, tradingAccountId, sharedMatchKey, clientOtcTradeId, createdAtDatetime, createdAtTimestamp
HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
status
enum
MATCHED
Allowed: COUNTERPARTY_PENDING ┃ COUNTERPARTY_PAIRED ┃ RISK_PENDING ┃ MATCHED ┃ CANCELLED ┃ REJECTED
OTC trade status

Examples: MATCHED
* tradingAccountId
string
111000000000001
Examples: 111000000000001
sharedMatchKey
string
cfBtcXrpMatch001
Examples: cfBtcXrpMatch001
clientOtcTradeId
string
20050900225
Examples: 20050900225
createdAtDatetime[ gte ]
date-time
2025-05-20T01:01:01.000Z
Start timestamp of window, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
createdAtDatetime[ lte ]
date-time
2025-05-20T01:01:01.000Z
End timestamp of window, ISO 8601 with millisecond as string

Examples: 2025-05-20T01:01:01.000Z
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
[
{
"otcTradeId": "200000000000000098",
"clientOtcTradeId": "20050900225",
"sharedMatchKey": "cfBtcXrpMatch001",
"status": "MATCHED",
"statusReason": "Ok",
"statusReasonCode": "1002",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000",
"expireDatetime": "2025-05-20T01:01:01.000Z",
"expireTimestamp": "1621490985000",
"remarks": "first otc trade with xyz client",
"trades": [
{
"tradeId": "100020000000000060",
"symbol": "BTC-USDC-PERP",
"price": "1.00000000",
"quantity": "1.00000000",
"quoteAmount": "1.00000000",
"baseFee": "1.00000000",
"quoteFee": "1.00000000",
"tradeRebateAssetSymbol": "BTC-USDC-PERP",
"tradeRebateAmount": "1.00000000",
"side": "BUY",
"isTaker": true,
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
]
}
]
Create OTC Trade
post /v2/otc-trades
Creates an OTC trade, requires bearer token in authorization header.

This endpoint uses the signing format which does not require strict field ordering and addition of null fields in the request body. Prices do not require strict precision. Eg. for asset precision of 4 - 100, 100.0, 100.00, 100.000 and 100.0000 are all accepted.

HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
EXAMPLE
SCHEMA
{
  "commandType": "V1CreateOtcTrade",
  "clientOtcTradeId": "20050900225",
  "sharedMatchKey": "cfBtcXrpMatch001",
  "tradingAccountId": "111000000000001",
  "isTaker": true,
  "remarks": "first otc trade with xyz client",
  "trades": [
    {
      "symbol": "BTC-USDC-PERP",
      "side": "BUY",
      "price": "98213.0000",
      "quantity": "1.50000000"
    },
    {
      "symbol": "XRP-USDC-PERP",
      "side": "SELL",
      "price": "2.6600",
      "quantity": "50.000000"
    }
  ]
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

BX-REFERRER
string
A numeric referrer id if applicable

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. The create OTC trade command was successfully acknowledged. To check the current status of the OTC trade, query Get Trade by ID using otcTradeId or clientOtcTradeId received in the response payload.

EXAMPLE
SCHEMA
application/json
A response for an acknowledged OTC trade creation request

Copy
{
"message": "Command acknowledged - CreateOtcTrade",
"requestId": "197735387747975680",
"otcTradeId": "200000000000000098",
"clientOtcTradeId": "20050900225",
"sharedMatchKey": "cfBtcXrpMatch001"
}
Get OTC Trade by ID
get /v2/otc-trades/{otcTradeId}
Retrieve a specific otc trade using its unique identifier.

HTTP Bearer
REQUEST
PATH PARAMETERS
* otcTradeId
string
Id of the OTC Trade

QUERY-STRING PARAMETERS
* tradingAccountId
string
111000000000001
Id of the trading account

Examples: 111000000000001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
Copy
{
"otcTradeId": "200000000000000098",
"clientOtcTradeId": "20050900225",
"sharedMatchKey": "cfBtcXrpMatch001",
"status": "MATCHED",
"statusReason": "Ok",
"statusReasonCode": "1002",
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000",
"expireDatetime": "2025-05-20T01:01:01.000Z",
"expireTimestamp": "1621490985000",
"remarks": "first otc trade with xyz client",
"trades": [
{
"tradeId": "100020000000000060",
"symbol": "BTC-USDC-PERP",
"price": "1.00000000",
"quantity": "1.00000000",
"quoteAmount": "1.00000000",
"baseFee": "1.00000000",
"quoteFee": "1.00000000",
"tradeRebateAssetSymbol": "BTC-USDC-PERP",
"tradeRebateAmount": "1.00000000",
"side": "BUY",
"isTaker": true,
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000"
}
]
}
Get Unconfirmed OTC Trade
get /v2/otc-trades/unconfirmed-trade
Retrieve the unconfirmed trade details using shared match key.

HTTP Bearer
REQUEST
QUERY-STRING PARAMETERS
* tradingAccountId
string
111000000000001
Id of the trading account for accepting the unconfirmed trade

Examples: 111000000000001
* sharedMatchKey
string
cfBtcXrpMatch001
Provided by your counterparty to identify the trade

Examples: cfBtcXrpMatch001
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
OK

EXAMPLE
SCHEMA
application/json
An unconfirmed OTC trade for booking.

Copy
{
"sharedMatchKey": "cfBtcXrpMatch001",
"isTaker": true,
"createdAtDatetime": "2025-05-20T01:01:01.000Z",
"createdAtTimestamp": "1621490985000",
"expireDatetime": "2025-05-20T01:01:01.000Z",
"expireTimestamp": "1621490985000",
"trades": [
{
"symbol": "BTC-USDC-PERP",
"price": "1.00000000",
"quantity": "1.00000000",
"side": "BUY"
}
]
}
OTC Trade Cancellation Command
post /v2/otc-command
Submits a command to the trading engine. A successful response indicates that the command entry was acknowledged but does not indicate that the command was executed. This endpoint uses the signing format which does not require strict field ordering and addition of null fields in the request body.

Command schemas and examples are provided below. Supported commands:

V1CancelOtcTrade
V1CancelAllOtcTrades
Requires

bearer token in authorization header
HTTP Bearer
REQUEST
REQUEST BODY
*
application/json
EXAMPLE
SCHEMA

CancelOtcTrade
{
  "commandType": "V1CancelOtcTrade",
  "clientOtcTradeId": "20050900225",
  "tradingAccountId": "111000000000001"
}
REQUEST HEADERS
* Authorization
string
authorization header, its value must be 'Bearer ' + token

* BX-SIGNATURE
string
signature obtained using the signing format

* BX-TIMESTAMP
string
timestamp is the number of milliseconds since EPOCH

* BX-NONCE
string
nonce is a client side incremented unsigned 64 bit integer

API Server
https://api.exchange.bullish.com/trading-api
Authentication
Required (None Applied)
RESPONSE
Status OK. This means a command was successfully acknowledged.

EXAMPLE
SCHEMA
application/json

CancelOtcTradeResponse
Copy
{
"message": "Command acknowledged - CancelOtcTrade",
"requestId": "100000000000000147",
"otcTradeId": "200000000000000098",
"tradingAccountId": "111000000000001"
}