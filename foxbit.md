Foxbit WebSocket API (3.0)
Follow our Status Page for real-time updates on system performance and maintenance schedules. You can also subscribe to receive notifications about any incidents or scheduled maintenance that may affect the API's availability.
For support with the Foxbit API, please visit our Help Center.

Introduction
Welcome to the official Foxbit's trader and developer documentation! Here, you'll find everything you need to know to integrate and utilize our services effectively. Whether you're a seasoned trader or just starting out, our comprehensive documentation provides clear guidance on how to make the most out of our API.

We also have a full API usage examples repository demonstrating how to integrate and utilize our API, and in Javascript for the WebSocket example: Example Repository


Features
Robust Functionality: Explore the wide range of functionalities our websocket offers, including fetching real-time market data, receive updates about orders, trades and much more.
Detailed Guides: Step-by-step guides and tutorials help you get started quickly and navigate complex features effortlessly.
Comprehensive Reference: Dive deep into our API endpoints, parameters, and response structures with our detailed reference documentation.
This API provides both public and private channels, each accessible through specific URLs:

Public WebSocket: wss://api.foxbit.com.br/ws/v3/public
Private WebSocket: wss://api.foxbit.com.br/ws/v3/private
You can view the full list of available channels for both public and private subscriptions in the navigation menu.

Start Exploring
Ready to get started? Dive into our documentation and unleash the full potential of our Exchange API. Whether you're building trading automation, conducting research, or developing innovative solutions, our API provides the tools you need to succeed.

Happy coding! 🚀

Need More?
If you don't find something here, you can check our others API's documentation:

See all available APIs

Rate Limit
The Rate Limit is divided into five topics, these being connection, concurrent connection, subscriptions by message, subscriptions by connections and messages by period.
Note: Rate limits for public connections are controlled by IP Address.

If a channel does not have rate limit information in its documentation, it will use our global rate limit values:

#	Public	Private
Connections per period	10 connection per 2 seconds	10 connection per 2 seconds
Messages per period	10 messages per 2 seconds	10 messages per 2 seconds
Concurrent connections	30 concurrent connections	30 concurrent connections
Subscriptions per message	25 subscriptions per message	25 subscriptions per message
Subscriptions per connections	50 subscriptions per connection	-
Authentication
Secure access to private WebSocket functionality requires authentication. This section explains the end-to-end flow, signature generation, recommended client practices, and common troubleshooting hints to help you get connected quickly and reliably.

How It Works
Authentication is performed on the private WebSocket by sending a login message that includes a timestamp and an HMAC-SHA256 signature. The signature is generated with your private API key by concatenating the timestamp with the literal string login and hashing the result. If the signature is valid and within the allowed time window, the server responds with a success event and the connection becomes authorized to subscribe to private channels.

Time Window and Clock Skew
The server validates that the provided timestamp is recent. For stable connectivity, keep your client clock synchronized (e.g., via NTP) and generate the timestamp as close as possible to the moment you send the message. Large clock skews can cause the request to be rejected.

Message Payload
To create the signature, you can use the following code:

import CryptoJS from 'crypto-js';

const timestamp = Date.now();
const signature = CryptoJS.HmacSHA256(`${timestamp}login`, privateKey).toString();
Example in Python:

import hmac, hashlib, time

timestamp = str(int(time.time() * 1000))
payload = f"{timestamp}login".encode()
signature = hmac.new(private_key.encode(), payload, hashlib.sha256).hexdigest()
Recommended Client Flow
Open a connection to the private WebSocket.
Immediately send the authentication message using a fresh timestamp and corresponding signature.
Wait for the authentication success event before subscribing to any private channels.
If authentication fails, handle the error gracefully (see the troubleshooting section) and retry only after verifying keys and time synchronization.
Security Best Practices
Store API keys securely and never expose them in client-side logs or UIs.
Rotate keys periodically and revoke unused credentials.
Use environment variables or a secure secrets manager for deployments.
Prefer short-lived processes to reduce the attack surface of long-running sessions.
Troubleshooting Tips
Verify the exact string being signed is ${timestamp}login (no spaces, encoding issues, or extra characters).
Log the computed timestamp and signature in a secure, redacted way during development.
Ensure you send the auth message before any private subscriptions.
Keep your system clock synchronized (NTP) to avoid time-based rejections.
Ping
The Ping channel enables users to verify their connection to the server. When a ping is sent, the server will respond with a "success" event message if the connection is active.

Additionally, the Ping channel can be used to keep the connection alive. If the connection remains idle for too long, the server will close it. Regularly sending pings prevents this from happening. This functionality is available for both public and private connections. Recommendation: It is recommended to send a ping message every 20 seconds for each open connection to maintain optimal connection health and prevent automatic disconnection due to inactivity.

Message Payload
To send a ping, use the following message format:

type	
string
Value: "message"
The desired event to be executed

params	
Array of objects
An array of channels intended for action execution


Copy
Expand allCollapse all
{
"type": "message",
"params": [
{}
]
}
Success
This message will be sent when user was successfully pinged

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted

data	
object
The data returned by the server


Copy
Expand allCollapse all
{
"type": "message",
"event": "success",
"params": {
"channel": "ping"
},
"data": {
"message": "pong"
}
}
Ticker
Provides a summary data for a market, including the latest traded price, volume, and price changes over 24hr. Users will receive updates every 1000ms until they send an unsubscribe call.

Message Payload
To subscribe or unsubscribe from WebSocket channels, use the following message format: The type field determines the action ("subscribe" or "unsubscribe"), while params specifies the target channels and markets.

One of SubscribeTickerUnsubscribeTicker
type	
string
The desired event to be executed

Value: "subscribe"
params	
Array of objects
An array of channels intended for action execution

Example

SubscribeTicker
SubscribeTicker

Copy
Expand allCollapse all
{
"type": "subscribe",
"params": [
{}
]
}
Subscribe success
This message will be sent when user was successfully subscribed to the channel with specified market data

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "success",
"params": {
"channel": "ticker",
"market_symbol": "btcbrl"
}
}
Unsubscribe success
This message will be sent when user was successfully unsubscribed from the channel with specified market data

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted


Copy
Expand allCollapse all
{
"type": "unsubscribe",
"event": "success",
"params": {
"channel": "ticker",
"market_symbol": "btcbrl"
}
}
Invalid market response
This message will be sent when user sent invalid payload, the connection will be closed automatically when errors occurs

type	
string
The executed event

event	
string
The event emitted by the server

message	
string
Subscription error


Copy
{
"type": "subscribe",
"event": "error",
"message": "Invalid market 'invalid-market' for channel 'channel'"
}
Ticker update event
This message will be sent at every market change if user have successfully subscribed

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted

data	
object
Update data emitted by the channel


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "update",
"params": {
"channel": "ticker",
"market_symbol": "btcbrl"
},
"data": {
"best": {},
"last_traded": {},
"rolling_24h": {},
"ts": 1717788720000
}
}
Orderbook
Streams the current bid and ask orders in the market, showing price levels and available quantities. Users will receive updates every 1000ms by default, unless a different interval is specified, until they send an unsubscribe call.

Available intervals:

100ms
250ms
500ms
1000ms (default)
Message Payload
To subscribe or unsubscribe from WebSocket channels, use the following message format: The type field determines the action ("subscribe" or "unsubscribe"), while params specifies the target channels and markets.

One of SubscribeOrderbookUnsubscribeOrderbook
type	
string
The desired event to be executed

Value: "subscribe"
params	
Array of objects
An array of channels intended for action execution

Example

SubscribeOrderbook
SubscribeOrderbook

Copy
Expand allCollapse all
{
"type": "subscribe",
"params": [
{}
]
}
Subscribe success
This message will be sent when user was successfully subscribed to the channel with specified market data

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "success",
"params": {
"channel": "orderbook-1000",
"market_symbol": "btcbrl"
}
}
Unsubscribe success
This message will be sent when user was successfully unsubscribed from the channel with specified market data

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted


Copy
Expand allCollapse all
{
"type": "unsubscribe",
"event": "success",
"params": {
"channel": "orderbook-100",
"market_symbol": "btcbrl"
}
}
Orderbook snapshot event
This message provides a snapshot of the current orderbook state when you first subscribe to the orderbook channel. The snapshot is essential for initializing your local orderbook copy and serves as the foundation for maintaining an accurate, real-time orderbook in memory.

Depth: The orderbook snapshot returns the top 300 levels for both buy and sell sides.

Purpose and Usage:

Initial State: The snapshot gives you the current state of buy and sell orders at the moment of subscription
Memory Management: Use this data to build your initial in-memory orderbook structure before processing incremental updates
Synchronization: The snapshot includes a sequence_id which is crucial for maintaining data consistency
Sequential Processing: After receiving the snapshot, all subsequent orderbook update events will be sequential and incremental. Each update event includes first_sequence_id and last_sequence_id to ensure you don't miss any orderbook changes and can maintain a perfectly synchronized local copy.

Implementation Strategy:

Subscribe to the orderbook channel with snapshot param as true
Receive and process the complete snapshot to build your initial orderbook state
Store the sequence_id from the snapshot
Process all subsequent update events sequentially using their first_sequence_id and last_sequence_id to maintain your local orderbook
Example Implementation: For a complete example of how to manage the orderbook in memory using JavaScript, check out our sample implementation: JavaScript Orderbook Management Example

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted

data	
object
Update data emitted by the channel


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "snapshot",
"params": {
"channel": "orderbook",
"market_symbol": "btcbrl"
},
"data": {
"sequence_id": 123321,
"asks": [],
"bids": []
}
}
Invalid market response
This message will be sent when user sent invalid payload, the connection will be closed automatically when errors occurs

type	
string
The executed event

event	
string
The event emitted by the server

message	
string
Subscription error


Copy
{
"type": "subscribe",
"event": "error",
"message": "Invalid market 'invalid-market' for channel 'channel'"
}
Orderbook update event
This message will be sent at every market change if user have successfully subscribed

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted

data	
object
Update data emitted by the channel


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "update",
"params": {
"channel": "orderbook-100",
"market_symbol": "btcbrl"
},
"data": {
"ts": 1661538954309,
"first_sequence_id": 1,
"last_sequence_id": 10,
"asks": [],
"bids": []
}
}
Candle
Streams aggregated market data over fixed time intervals (e.g., 1m, 5m, 1h), including open, high, low, close prices, and traded volume. Users will receive updates at the end of each interval until they send an unsubscribe call.

Available intervals:

time	1m	5m	15m	30m	1h	2h	4h	6h	12h	1d	1w	2w
seconds	60	300	900	1800	3600	7200	14400	21600	43200	86400	604800	1209600
Message Payload
To subscribe or unsubscribe from WebSocket channels, use the following message format: The type field determines the action ("subscribe" or "unsubscribe"), while params specifies the target channels and markets.

One of SubscribeCandleUnsubscribeCandle
type	
string
The desired event to be executed

Value: "subscribe"
params	
Array of objects
An array of channels intended for action execution

Example

SubscribeCandle
SubscribeCandle

Copy
Expand allCollapse all
{
"type": "subscribe",
"params": [
{}
]
}
Subscribe success
This message will be sent when user was successfully subscribed to the channel with specified market data

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "success",
"params": {
"channel": "candle-60",
"market_symbol": "btcbrl"
}
}
Unsubscribe success
This message will be sent when user was successfully unsubscribed from the channel with specified market data

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted


Copy
Expand allCollapse all
{
"type": "unsubscribe",
"event": "success",
"params": {
"channel": "candle-60",
"market_symbol": "btcbrl"
}
}
Invalid market response
This message will be sent when user sent invalid payload, the connection will be closed automatically when errors occurs

type	
string
The executed event

event	
string
The event emitted by the server

message	
string
Subscription error


Copy
{
"type": "subscribe",
"event": "error",
"message": "Invalid market 'invalid-market' for channel 'channel'"
}
Candle update event
This message will be sent at every market change if user have successfully subscribed

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted

data	
Array of objects[ items ]
Update data emitted by the channel


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "update",
"params": {
"channel": "candle-60",
"market_symbol": "btcbrl"
},
"data": [
1685019840000,
"133294.4051",
"131389.5942",
"133294.405",
"131389.5942",
"0.0172"
]
}
Trades
Provides a real-time feed of executed trades, showing each transaction’s price, quantity, timestamp and taker sides. Users will receive updates as trades occur until they send an unsubscribe call.

Message Payload
To subscribe or unsubscribe from WebSocket channels, use the following message format: The type field determines the action ("subscribe" or "unsubscribe"), while params specifies the target channels and markets.

One of SubscribeTradesUnsubscribeTrades
type	
string
The desired event to be executed

Value: "subscribe"
params	
Array of objects
An array of channels intended for action execution

Example

SubscribeTrades
SubscribeTrades

Copy
Expand allCollapse all
{
"type": "subscribe",
"params": [
{}
]
}
Subscribe success
This message will be sent when user was successfully subscribed to the channel with specified market data

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "success",
"params": {
"channel": "trades",
"market_symbol": "btcbrl"
}
}
Unsubscribe success
This message will be sent when user was successfully unsubscribed from the channel with specified market data

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted


Copy
Expand allCollapse all
{
"type": "unsubscribe",
"event": "success",
"params": {
"channel": "trades",
"market_symbol": "btcbrl"
}
}
Invalid market response
This message will be sent when user sent invalid payload, the connection will be closed automatically when errors occurs

type	
string
The executed event

event	
string
The event emitted by the server

message	
string
Subscription error


Copy
{
"type": "subscribe",
"event": "error",
"message": "Invalid market 'invalid-market' for channel 'channel'"
}
Trade update event
This message will be sent at every market change if user have successfully subscribed

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted

data	
Array of objects
Update data emitted by the channel


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "update",
"params": {
"channel": "trade",
"market_symbol": "btcbrl"
},
"data": [
{}
]
}
Login
The Login channel is used to authenticate and authorize a user on the Private WebSocket connection. By sending a login message with a valid timestamp and signature, users can gain access to private channels that provide real-time updates about their account activities, such as orders, trades, and balances.
For more information about the signature generation, please refer to the Authentication section.

Message Payload
To authenticate, send a login message with the following format:

type	
string
Value: "login"
The desired event to be executed

params	
object
An object with authentication data


Copy
Expand allCollapse all
{
"type": "login",
"params": {
"timestamp": 1717788720000,
"api_key": "your-api-key",
"signature": "generated-signature"
}
}
Success
This message will be sent when the user was successfully authenticated. After receiving it, you can safely subscribe to private channels.

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
An object with authentication data

data	
object
The data returned by the server


Copy
Expand allCollapse all
{
"type": "login",
"event": "success",
"params": {
"timestamp": 1717788720000,
"api_key": "your-api-key",
"signature": "generated-signature"
},
"data": {
"authenticated": true
}
}
Invalid
If the signature is invalid, the timestamp is too old, or the key has been revoked, the server will respond with an error. Typical causes include:

Incorrect private key or misconfigured environment variables.
Client clock skew beyond the allowed window.
Truncated payload or incorrect concatenation when building the string to sign.
Using a stale timestamp when retrying.
The following failure schema describes the error response:

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
An object with authentication data

data	
object
The data returned by the server


Copy
Expand allCollapse all
{
"type": "message",
"event": "error",
"params": {
"timestamp": 1717788720000,
"api_key": "your-api-key",
"signature": "generated-signature"
},
"data": {
"authenticated": true,
"message": "Invalid signature"
}
}
Account Events
The Account Events channel provides real-time notifications about all activities in your trading account. This channel is essential for monitoring your portfolio, tracking order execution, and building automated trading strategies. Users will receive updates continuously until they send an unsubscribe call.

Note: This channel requires authentication on the Private WebSocket connection. Ensure you have successfully authenticated before attempting to subscribe.

Available event types:

Balance: Notifies when available or locked balance changes for any currency
Order: Provides updates on order lifecycle (created, filled, partially filled, cancelled, rejected)
Trade: Sent when your orders are matched and executed in the market
Common use cases:

Real-time portfolio tracking and balance monitoring
Automated trading bots that react to order fills
Order management systems with live status updates
Risk management and position monitoring
Message Payload
To subscribe to account events, send a subscription message through your authenticated WebSocket connection. Unlike public channels, account events don't require market symbols as they cover all activity across your account.

type	
string
Enum: "subscribe" "unsubscribe"
The desired event to be executed

params	
Array of objects
An array of channels intended for action execution


Copy
Expand allCollapse all
{
"type": "subscribe",
"params": [
{}
]
}
Success subscription
This message will be sent when you have successfully subscribed to the Account Events channel. From this point, you will receive real-time updates for all balance, order, and trade events as they occur in your account.

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "success",
"params": {
"channel": "accounts",
"type": "BALANCE"
}
}
Balance update event
This message will be sent whenever your account balance changes, including when funds are locked for orders, unlocked from cancellations, or updated due to deposits, withdrawals, or trade executions. Each event includes both available and locked amounts for the affected currency.

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted

data	
object
Update data emitted by the channel


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "update",
"params": {
"channel": "accounts",
"type": "BALANCE"
},
"data": {
"currency_symbol": "btc",
"available": "12.345",
"hold": "0.000",
"ts": 1717788720000
}
}
Order update event
This message will be sent at every stage of your order lifecycle, including when orders are created, partially filled, fully filled, cancelled, or rejected. The event provides complete order details including status, filled quantity, remaining quantity, and timestamps.

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted

data	
object
Update data emitted by the channel


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "update",
"params": {
"channel": "accounts",
"type": "ORDER"
},
"data": {
"id": 123456,
"client_order_id": 654321,
"market_symbol": "btcbrl",
"side": "BUY",
"instante_amount": "10.000",
"instant_amount_executed": "5.000",
"quantity": "0.005",
"quantity_executed": "0.0025",
"price": "20000.00",
"avg_price": "19999.99",
"state": "FILLED",
"error_message": "Insufficient funds",
"cancellation_reason": 100,
"ts": 1717788720000
}
}
Trade update event
This message will be sent each time one of your orders is matched and executed in the market. A single order may generate multiple trade events if it's filled incrementally by matching with different orders in the book. Each event includes execution price, quantity, fees, and whether you were the maker or taker.

type	
string
The executed event

event	
string
The event emitted by the server

params	
object
Channel data on which the event was emitted

data	
object
Update data emitted by the channel


Copy
Expand allCollapse all
{
"type": "subscribe",
"event": "update",
"params": {
"channel": "accounts",
"type": "TRADE"
},
"data": {
"id": 123456,
"order": {},
"price": "20000.00",
"quantity": "0.005",
"fee": "0.0001",
"fee_currency_symbol": "btc",
"role": "MAKER",
"ts": 1717788720000
}
}

















Foxbit REST API (3.0)
We provide an OpenAPI specification for our REST API, which is a standard way to describe the API's endpoints, request and response formats, authentication methods, and other details. This specification can be downloaded at: OpenAPI Specification.
We also provide a Postman collection and environment to help you get started with our API. The instructions are available in the Integrating with Postman section.
Follow our Status Page for real-time updates on system performance and maintenance schedules. You can also subscribe to receive notifications about any incidents or scheduled maintenance that may affect the API's availability.
For support with the Foxbit API, please visit our Help Center.

Introduction
Welcome to the official Foxbit's trader and developer documentation! Here, you'll find everything you need to know to integrate and utilize our services effectively. Whether you're a seasoned trader or just starting out, our comprehensive documentation provides clear guidance on how to make the most out of our API.

Features
Robust Functionality: Explore the wide range of functionalities our API offers, including fetching real-time market data, placing orders, managing accounts, and much more.
Detailed Guides: Step-by-step guides and tutorials help you get started quickly and navigate complex features effortlessly.
Comprehensive Reference: Dive deep into our API endpoints, parameters, and response structures with our detailed reference documentation.
We also have a full API usage examples repository demonstrating how to integrate and utilize our API in various programming languages:

.NET
Go
Java
JavaScript
TypeScript
PHP
Python
Ruby
Start Exploring
Ready to get started? Dive into our documentation and unleash the full potential of our Exchange API.
Whether you're building trading automations, conducting research, or developing innovative solutions, our API provides the tools you need to succeed.

Happy coding! 🚀

Changelog
A changelog is a record of all notable changes made to this API, including new features, bug fixes and updates. It helps users and developers stay informed about the evolution of the project. For more details, visit our changelog page.

Authentication
Before being able to sign any requests, you must create an API key via the Foxbit platform. After creating a key, you need to write down 2 pieces of information, Key and Secret. The Key and Secret are generated and provided by Foxbit. Please note that the secret key cannot be recovered once lost. If you lost this information, please create a new API key.

Signing a request
All private REST requests must contain the following headers:

X-FB-ACCESS-KEY The API key as a string.
X-FB-ACCESS-TIMESTAMP The current timestamp of your request. Must be in UNIX timestamp format, which represents the number of milliseconds since January 1, 1970 (the UNIX epoch UTC).
X-FB-ACCESS-SIGNATURE The hex-encoded signature. See details below for generating the signature.
Generating the hex-encoded signature
Use your API Secret to encrypt the prehash string using HMAC with the SHA-256 algorithm. The request body is a JSON string and needs to match the parameters passed to the API. Here's an example of how to generate the prehash string:

const preHash = timestamp + httpMethod + requestPath + queryString + rawBody
We provide example implementations for generating the signature in various programming languages, including Javascript, GoLang, Python, and others.

Receive Window
The Receive Window mechanism lets a client specify a time tolerance around the server's clock to protect against replay attacks and drop any requests that arrive too late. By bounding how far “ahead” or “behind” a timestamp may be, the server can reject stale or delayed requests before they reach your API logic. For retry safety, we also support Idempotent Requests to ensure duplicate calls have no unintended side effects.

To define a tolerance window (in milliseconds) around the server's current time, you may include the optional header X-FB-RECEIVE-WINDOW in your request.

Accepted values: 1000 to 60000 (1s-60s).
When set to e.g. 15000, the server will accept requests timestamped up to 15s after the timestamp sent in the request.
Requests with timestamps that fall outside this window will be rejected.
To synchronize your clock, you may call GET /rest/v3/system/time which returns the server's current UNIX timestamp in milliseconds.

Rate Limit
Our rate limit allow a maximum requests (limit) in a time window (ttl).
For public endpoints, we use your IP address as a key. But for private endpoint's, your SN is used as an identifier.

If an endpoint does not have rate limit information in its documentation, then it will be using our global rate limit values:

Limit	Ttl	Block duration
300 req	10 sec.	10 sec.
Endpoints with a specific rate limit (described in their documentation) will override this values.

Idempotent Requests
The API supports idempotency for safely retrying requests without accidentally performing the same operation twice. This is useful when an API call is disrupted in transit and you do not receive a response. For example, if a request to create an order does not respond due to a network connection error, you can retry the request with the same idempotency key to guarantee that no more than one order is created.

To perform an idempotent request, provide an additional X-Idempotent: <key> header to the request.

Foxbit's idempotency works by saving the resulting status code and body of the first request made for any given idempotency key, regardless of whether it succeeded or failed. Subsequent requests with the same key return the same result, including 500 errors.

An idempotency key is a unique value generated by the client which the server uses to recognize subsequent retries of the same request. How you create unique keys is up to you, but we suggest using V4 UUIDs, or another random string with enough entropy to avoid collisions. Idempotency keys can be up to 36 characters long.

Keys are eligible to be removed from the system automatically after they're at least 72 hours old, and a new request is generated if a key is reused after the original has been pruned.

Results are only saved if an API endpoint started executing.

In case of concurrent request, only one of them will be process, the other request will return status code 409 and an error, the second request does not get saved by the idempotency.

All POST requests accept idempotency keys. Sending idempotency keys in GET, PUT or DELETE requests has no effect and should be avoided, as these requests are idempotent by definition.

API Codes
This section provides a list of codes that may be returned by the API.

Errors
If there is an error in the execution of the request or response, the payload will have the following format.

{
  "error": {
    "message": "Invalid symbol.",
    "code": 4004,
    "details": [
        "The market or asset symbol is invalid or was not found.",
    ]
  }
}
Some Common Examples
Code	Message	Description
400	Bad request.	An unknown error occurred while processing request parameters.
429	Too many requests.	Request limit exceeded. Try again later.
404	Resource not found.	A resource was not found while processing the request.
500	Internal server error.	An unknown error occurred while processing the request.
2001	Authentication error.	Error authenticating request.
2002	Invalid signature.	The signature for this request is not valid.
2003	Invalid access key.	Access key missing, invalid or not found.
2004	Invalid timestamp.	Invalid or missing timestamp.
2005	IP not allowed.	The IP address {IP_ADDR} isn't on the trusted list for this API key.
3001	Permission denied.	Permission denied for this request.
3002	KYC required.	A greater level of KYC verification is required to proceed with this request.
3003	Member disabled.	This member is disabled. Please get in touch with our support for more information.
4001	Validation error.	A validation error occurred.
4002	Insufficient funds.	Insufficient funds to proceed with this request.
4003	Quantity below the minimum allowed.	Quantity below the minimum allowed to proceed with this request.
4004	Invalid symbol.	The market or asset symbol is invalid or was not found.
4005	Invalid idempotent.	Characters allowed are "a-z", "0-9", "_" or "-", and 36 at max. We recommend UUID v4 in lowercase.
4007	Locked error.	There was an error in your allocated balance, please contact us.
4008	Cannot submit order.	The order cannot be created.
4009	Invalid level.	The sub-member does not have the required level to create the transaction.
4011	Too many open orders.	You have reached the limit of open orders per market/side.
4012	Too many simultaneous account operations.	We are currently unable to process your balance change due to simultaneous operations on your account. Please retry shortly.
4013	Invalid receive window header.	The receive window header is invalid. The value must be between 1000 and 60000.
4014	Timestamp is out of range.	The timestamp is out of range. The request timestamp is outside the allowed time window specified on `X-FB-RECEIVE-WINDOW` header.
4015	Market side disabled.	The market does not allow orders in this side.
5001	Service unavailable.	The requested resource is currently unavailable. Try again later.
5002	Service under maintenance.	The requested resource is currently under maintenance. Try again later.
5003	Market under maintenance.	The market is under maintenance. Try again later.
5004	Market is not deep enough.	The market is not deep enough to complete your request.
5005	Price out of range from market.	The order price is out of range from market to complete your request.
5006	Significant price deviation detected, exceeding acceptable limits.	The order price is exceeding acceptable limits from market to complete your request.
Cancellation Reasons
If an order is cancelled, the code for the reason for cancellation will follow the table below:

Reason from cancellation state:
Code	Description
NULL	Order state is not CANCEL
1	Requested by user
100	Applied by Exchange
101	Applied before failure trade
102	Order Instant with insufficient volume remaining after filled or not matched
103	Order StopMarket with insufficient volume remaining after filled
104	Order matched with counter order from the same member
105	Member without document number on Exchange
200	Limit order with TimeInForce ImmediateorCancel (IOC) doesn't matched
201	Limit order with TimeInForce FillOrKill (FOK) found no trading volume
202	Order PostOnly matched
203	Order Limit or Market with insufficient volume remaining after filled
204	Order Limit price out of range from Market
205	Significant price deviation detected, exceeding acceptable limits during execution. The remaining volume has been canceled due to a breached price limit
206	Order triggered the STP mechanism with EXPIRE_TAKER action
207	Order triggered the STP mechanism with EXPIRE_MAKER action
208	Order triggered the STP mechanism with EXPIRE_BOTH action
209	Order triggered the STP mechanism with DECREMENT action
Tutorials
How to manage a local copy of the order book
Follow the steps below in sequential order
Open a websocket stream to receive order book updates. When the connection opened, the returned data must be buffered. See documentation. The first numeric item (so called ID) in each update refers to an incremental number that represents the current state of the order book.
Get a snapshot of the order book from our REST API. See documentation. The property sequence_id returned refers to an incremental number that represents the current state of the order book.
Update your local copy of the order book each time the ID of an order book update is strictly equals to sequence_id + 1.
Important
While listening to the stream, events can only be processed if their ID remains sequential. If you find a gap between IDs, you need to restart the process from the beginning.
The data at each event contains the most recent quantity for a price level. If this quantity is zero, please, remove the price level.
Integrating with Postman
We provide a Postman collection and environment to help you get started with our API quickly and easily. The collection includes all available endpoints, along with example requests and responses, making it easy to test and explore the API. The environment allows you to set up your API key and secret, so you can make authenticated requests without having to manually enter them each time. The zip containing the Postman collection and environment can be downloaded here: Postman collection

To import the API collection into Postman, follow these steps:

Download the zip file containing the Postman collection and environment.
Unzip the file to a location on your computer.
Open Postman and click on the "Import" button in the top left corner.
Select the "Import File" tab and choose the unzipped file named rest-v3.collection.json.
Click on the "Import" button to import the collection.
After importing the collection, you will see a new folder named "Foxbit API" in your Postman workspace.
Click on Environments tab in the left sidebar and click on the "Import" button.
Select the "Import File" tab and choose the unzipped file named rest-v3.environment.json.
Click on the "Import" button to import the environment.
After importing the environment, you will see a new environment named "Foxbit RestV3 Environment" in your Postman workspace.
Go to imported environment and fill in the following variables:
Variable	Type	Initial value	Current Value
API_KEY	default		your_api_key_here
API_SECRET	secret		your_api_secret_here
Back to the collection, click on the "Foxbit API" folder to see all available endpoints.
Select an endpoint you want to test and click on it.
Now you can start using our API directly from Postman! If you have any questions or need further assistance, feel free to reach out to our support team.

Market Data
This module provides access to information about available cryptocurrency markets, including trading pairs, price data, volume and other relevant market statistics.

List currencies
To obtain the currency icon, use this URL pattern: https://statics.foxbit.com.br/icons/colored/[CURRENCY_SYMBOL].svg

Cache: 1 minute.
Rate Limit: 6 requests per 1 second.

query Parameters
category	
string
Value: "PREDICTION"
Example: category=PREDICTION
The currency category to filter currencies

Responses
200 A list of currencies was retrieved successfully

get
/rest/v3/currencies

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"data": [
{}
]
}
List markets
Cache: 1 minute.
Rate Limit: 6 requests per 1 second.

query Parameters
category	
string
Example: category=PREDICTION
Filter by market category

Responses
200 A list of markets was retrieved successfully

get
/rest/v3/markets

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"data": [
{}
]
}
Get a market quotation
This endpoint provides a quotation based on market and side. You can specify the amount or the quantity of the quote.

Rate Limit: 2 requests per 2 seconds.

query Parameters
side
required
string
Enum: "buy" "sell"
Example: side=buy
Book side for quote search

base_currency
required
string
Example: base_currency=usdt
The base currency is the currency against which exchange rates are typically quoted. It serves as the reference point for determining the value of other currencies in a currency pair. (e.g. BTC in BTCBRL)

quote_currency
required
string
Example: quote_currency=brl
The quote currency is the second currency in a currency pair. It represents the value of one unit of the base currency in terms of the quote currency. (e.g. BRL in BTCBRL)

Based on quantity or amount
required
QuoteByAmount (object) or QuoteByQuantity (object)
expand for details

Responses
200 A market quotation based on a market and volume basis was retrieved successfully

get
/rest/v3/markets/quotes

Response samples
200
Content type
application/json

Copy
{
"side": "buy|sell",
"market_symbol": "usdtbrl",
"base_amount": "0.00256410",
"quote_amount": "1000.0",
"price": "390000.00"
}
Get order book
This endpoint exports a copy of the order book of a specific market.
See also how to manage a local copy of the order book.

Rate Limit: 10 requests per 2 seconds.

path Parameters
market_symbol
required
string
Example: btcbrl
The symbol of the market from witch the order book data will be exported

query Parameters
depth	
number <= 300
Default: 300
Example: depth=50
The maximum number of asks and bids to be exported

Responses
200 The order book data was retrieved successfully
404 Market not found or not available

get
/rest/v3/markets/{market_symbol}/orderbook

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"sequence_id": 1234567890,
"timestamp": 1713187921336,
"bids": [
[],
[]
],
"asks": [
[],
[]
]
}
Get candlesticks
Retrieve the candlestick charts/data

Rate Limit: 15 requests per 2 seconds.

path Parameters
market_symbol
required
string
Example: btcbrl
The symbol of the market from witch the order book data will be exported

query Parameters
interval
required
string
Enum: "1m" "5m" "15m" "30m" "1h" "2h" "4h" "6h" "12h" "1d" "1w" "2w" "1M"
Examples:
interval=1m - 1 minute interval
interval=5m - 5 minutes interval
interval=15m - 15 minutes interval
interval=1d - 1 day interval
interval=1M - 1 month interval
start_time	
string
Examples:
start_time=2022-07-18T00:00 - Start of day
start_time=2022-08-19T12:10 - Specific time
The earliest date in ticker history, it can be entered with minutes accuracy

end_time	
string
Examples:
end_time=2022-08-19T12:00 - Start of hour
end_time=2022-08-19T12:12 - Specific minute
The most current date in ticker history, can be entered with a precision of minutes

limit	
number
Default: 100
Examples:
limit=100 - Default limit
limit=500 - Maximum allowed
The maximum number of ticks to be returned (max 500)

Responses
200 It returns an array nested with another array of strings. All numbers (excluding date value) are represented as a string of decimals.
404 Candlesticks not found or not available.

get
/rest/v3/markets/{market_symbol}/candlesticks

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
[
"1692918000000",
"127772.05150000",
"128467.99980000",
"127750.01000000",
"128353.99990000",
"1692918060000",
"0.17080431",
"21866.35948786",
66,
"0.12073605",
"15466.34096391"
],
[
"1692921600000",
"128353.99990000",
"128353.99990000",
"127922.00030000",
"128339.99990000",
"1692921660000",
"0.12355465",
"15851.30631056",
45,
"0.11030870",
"14156.75206627"
]
]
Get ticker for a specific market
Get last 24 hours ticker information, in real-time, for given market.

Rate Limit: 12 requests per 2 seconds.

path Parameters
market_symbol
required
string
Example: btcbrl
The symbol of the market from witch the book data will be exported

Responses
200 The ticker data was retrieved successfully
404 Market pair not found or not available.

get
/rest/v3/markets/{market_symbol}/ticker/24hr

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"data": [
{}
]
}
Get all markets ticker
Retrieve the ticker data of all markets.
To obtain the currency icon, use this URL pattern: https://statics.foxbit.com.br/icons/colored/[CURRENCY_SYMBOL].svg.

Cache: 10 seconds.
Rate Limit: 2 requests per 4 seconds.

Responses
200 The ticker data was retrieved successfully

get
/rest/v3/markets/ticker/24hr

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"data": [
{}
]
}
Get trades
Retrieve the trades of a specific market
If the start_time and end_time are not sent, the trades returned will be the last trades based on the quantity indicated in the page_size field.

Rate Limit: 5 requests per 2 seconds.

path Parameters
market_symbol
required
string
Example: btcbrl
The market you want to filter

query Parameters
start_time	
string
Examples:
start_time=2024-01-01 - Date only
start_time=2024-01-01T06:25:09 - Date and time
Filter values after this start_time, in the format YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS

end_time	
string
Examples:
end_time=2024-01-01 - Date only
end_time=2024-01-01T06:25:09 - Date and time
Filter values before this end_time, in the format YYYY-MM-DD or YYYY-MM-DDTHH:MM:SS

page	
number
Default: 1
Examples:
page=1 - First page
page=10 - Tenth page
Page to be retrieved from the list

page_size	
number <= 200
Default: 50
Examples:
page_size=50 - Default page size
page_size=100 - Larger page size
The number of entries returned

Responses
200 The trades data was retrieved successfully

get
/rest/v3/markets/{market_symbol}/trades/history

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"data": [
{}
]
}
Get Sparkline
Retrieve the sparkline data for a specific time window and a group of markets

Cache: 10 seconds.
Rate Limit: 3 requests per 2 seconds.

path Parameters
window
required
string
Enum: "hour" "day" "week" "month" "year" "all"
The time window for the sparkline

query Parameters
market_symbols
required
Array of strings <= 20 items
Example: market_symbols=btcbrl,ethbrl,adabrl
Comma-separated list of market symbols

interval	
string
Enum: "1m" "5m" "1h" "2h" "1d" "1w"
Example: interval=1h
Time interval for sparkline data points. Available intervals per window:

Window	Available Intervals
hour	1m
day	5m
week	1h
month	2h
year	1d
all	1w
If not specified, the default interval for the selected window will be used.
Responses
200 Sparkline data retrieved successfully
400 Bad request - Invalid interval for the requested window or too many market symbols

get
/rest/v3/markets/sparkline/{window}

Response samples
200400
Content type
application/json

Copy
Expand allCollapse all
{
"data": [
{}
]
}
Banks
The Banks module facilitates interactions with external financial institutions or payment processors for handling fiat currency deposits, withdrawals and other banking-related operations.

List banks
Cache: 5 minutes.
Rate Limit: 1 request per 1 second.

Responses
200 A list of banks was retrieved successfully

get
/rest/v3/banks

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"data": [
{}
]
}
System
This module provides server information, ensuring optimal performance and reliability of the exchange platform.

Get current time
Returns the API server time in ISO-8601 and UNIX Timestamp formats with milliseconds precision.

Rate Limit: 5 requests per 1 second.

Responses
200 Server time was retrieved successfully

get
/rest/v3/system/time

Response samples
200
Content type
application/json

Copy
{
"iso": "2021-06-15T18:00:00.123Z",
"timestamp": 1637342699407
}





