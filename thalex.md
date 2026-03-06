halex API Description
API description
API RPC requests have a method name and a parameter block. Parameters are specific to a method. The result in case of success is a JSON-encoded value, where the type depends on the method. In case of error, the result is a JSON-encoded mapping containing {"code":<integer>,"message":<text>}.

Method names start either with private/ or public/. Private methods relate to a trading account, and must be authenticated.

OpenAPI spec
You can download this document in the OpenAPI format here.

Endpoints
HTTP
Exchange: https://thalex.com/api/v2

Testnet: https://testnet.thalex.com/api/v2

Websocket
Exchange: wss://thalex.com/ws/api/v2

Testnet: wss://testnet.thalex.com/ws/api/v2

Types
Prices and amounts
Unlike in some other exchanges, prices and amounts are transmitted as plain numbers. JSON itself does not specify any precision limits, but in practice, most implementations use double precision binary floating point numbers.

Not every price or amount can be precisely captured in a binary floating point number, e.g. numbers like 3.1 or 0.17. However they generally print just fine in JSON. In order to get around little problems on your side, we will round all prices and amounts to 8 digits, before checking tick size. So if you send an amount of 3.0999999999999999 (as printed in JSON), we'll interpret that as 3.1 without complaining.

Very large numbers that we send to you may lack some precision, e.g. P&L in the millions may not properly contain all 8 digits we track to accrue perpetual funding.

Note that this binary floating point issue exists only in the JSON interface. We use decimal numbers throughout the entire system. As prices and amounts must always click to some tick size, there is never a rounding problem.

Timestamps
Timestamps that we send are always numeric, and denote seconds since 1970-1-1 00:00:00+00 (the UNIX epoch). This is the number as you'd retrieve it from

Python: time.time()
Golang: float64(time.Now().UnixNano()) * 1e-9
JavaScript: Date.now() * 1e-3
C: clock_gettime(CLOCK_REALTIME, &ts), ts.tv_nsec * 1e-9 + ts.tv_sec
Timestamps are not precise and subject to arbitrary rounding. They should not be used for keying.

Labels
For your protection, labels on orders etc. are restricted to 64 characters in the set [A-Za-z0-9<>|_-].

HTTP API
HTTP API calls take the form of:

POST https://<api_endpoint>/api/v2/<method_name>

where the parameter block is a JSON-encoded name/value mapping. Only JSON input is accepted, and the "Content-Type" header is ignored.

Some query methods accept GET as well. In that case, parameters may be sent as a url-encoded query string.

If the input is syntactically valid, all required parameters are present and of the correct type, and proper authorization is supplied, then the HTTP result will always be 200 OK, regardless of the outcome of the request. The output will then always be a JSON-encoded object.

In case of success, the output will be a JSON object: {"result":<value>}. In case of error, the output will be a JSON object: {"error":{"code":<integer>,"message":<text>}}.

Methods starting with private/ require authentication. The HTTP request must carry a header:

Authorization: Bearer <token>

See later in this document on how to generate a token.

For HTTP requests an account can be selected by providing the following HTTP header:

X-Thalex-Account: <account number>

If this header is not provided, default account configured for the API key is selected.

Providing invalid account number in this header results in an invalid request error.

Every response to an authenticated trading account related HTTP request carries a header identifying the account:

X-Thalex-Account: <account number>

Websocket API
To use the WebSocket API, make a WebSocket connection to:

wss://<api_endpoint>/ws/api/v2

API calls then take the form of (JSON encoded):

{
    "method": <method_name>,
    "id": <your request id, optional>,
    "params": { <parameter block> }
}
where the parameter block is a name/value mapping. The parameter block is not optional; if a method does not have parameters, pass an empty object.

Every call has a single result, and the result always contains the user-supplied request ID. In case of success, the result looks like:

{
    "id": <your request id, or null if not supplied>,
    "result": <value>
}
In case of error, the result looks like:

{
    "id": <your request id, or null if not supplied>,
    "error": {"code":<integer>,"message":<text>}
}
WebSocket API calls may be pipelined. Note that in case of pipelining, the ordering of the results is not necessarily the same as the ordering of requests (we only guarantee that multiple matching engine requests on the same instrument will be handled in-order -- but even then, only successful results will be in the same order). If you use pipelining, you can use the id field to match results to requests.

WebSocket connections may also receive asynchronous notifications, as the result of earlier subscriptions. Notifications take the form of:

{
    "channel_name": <channel name as in subscription>,
    "notification": <channel-specific content>
    "snapshot": true
}
The snapshot flag is present only if true, and only for 'stateful' feeds that transmit an initial state and subsequent updates (book, instruments, account.orders, session.orders, account.portfolio).

Before private methods can be used, the connection must be authenticated once:

{
    "method":"public/login",
    "id":<your request id>,
    "params":{
        "token":<auth token>
    }
}
In some cases, for example during exchange maintenance, WebSocket connections can be gracefully closed by the server. In this case the server will send a reconnect system event at least 10 seconds prior to closing the connection. This gives you some time to clean up if needed (e.g. delete non-persistent orders). To receive the reconnect system event you need to be subscribed to the system channel.

WebSocket connections will get closed by the server if no messages are received for extended periods of time. Clients are expected to send ping messages periodically to signal that the connection is still alive. Idle unauthenticated connections that do not have any subscriptions and did not send any valid requests for a while might be closed by the server even if they get the ping messages.

Open orders amount limitations
There is a limit on total amount of open orders per account.

There are limits on total cash size of open orders per account per underlying per side (buy/sell), separate for delta-1 instruments (perpetual, futures) and options. Combination instruments are accounted for each leg separately. Cash size is calculated as a sum of all open order sizes multiplied by underlying price.

Please check Thalex trading information pages for the actual limit values.

For specific cases, e.g. on market maker accounts, higher limits can be in effect. Please contact Thalex support team if you require limit adjustments.

Open order limits are not applied to mass quotes.

Note that open orders are also taken into account for required margin calculations.

Persistent and non-persistent orders and sessions
Orders may be persistent or non-persistent. Non-persistent orders are those that were inserted with a WebSocket connection that was set to cancel_on_disconnect (aka non-persistent sessions). Persistent orders are all others.

The difference between persistent and non-persistent orders are:

Non-persistent orders will be automatically deleted in various cases:

when the creating websocket session is disconnected or times out;
in case of a gateway failure;
in case of a matching engine failover.
Non-persistent orders that were canceled on client request and have no fills are not added to the order history.

The maximum message rate of non-persistent sessions is higher.

Authentication
HTTP private calls must carry a bearer token. The same sort of token is used for the WebSocket public/login call.

Authentication tokens are created from an API key. An API key consists of two parts:

key name (e.g. 'K123456789')
private key, an RSA key
New API keys may be created from the website (account settings, generate API key). Be aware that the RSA private key is only displayed once, upon generation. It is not stored in the Thalex systems (we store the RSA public key used for verification).

A token is a JSON Web Token (JWT) with the following properties:

The signing algorithm is RS256, RS384, or RS512;
The header contains field kid with the key name as value;
The content contains the field iat with the current time (as UNIX timestamp);
The token is signed with the RSA private key.
The timestamp in the iat field must not be "off" for more than 30 seconds. Furthermore, each token on the same key must have a timestamp that is different (later) than any previously used token. This means that each HTTP request must carry a newly generated token. Note that the iat field may be fractional, this may mitigate problems with overlap.

Trading
Orders can be identified in three ways:

Every order has an order_id assigned by the system. This ID is known only when the reply comes back.
Orders also have a client_order_id, which is unique to the session through which the order is inserted. The client order ID may be specified on insert, with a value between 0 and 4294967295. The client order ID may be used to send an amend or cancel even while an insert is still pending, but only on the session that sent the insert. This mechanism may only be used for non-persistent orders.
Orders optionally have a label. Labels may be used to transfer arbitrary information, or as bulk delete group ID. Labels must not exceed 32 bytes in length (UTF8-encoded).
Conditional orders
Conditional orders are stop loss orders and similar. They are not visible in the public order book. Conditional orders also don't show up in open_orders, and can not be manipulated with cancel_all.

Mass quoting and market maker protection
Mass quoting is available on non-persistent sessions only, and only for specific market making accounts.

With mass quoting, orders are managed on a per session/instrument/side basis rather than using order IDs. Mass quoting allows multiple quotes in a single message, in a compact form. Quotes will atomically replace previous quotes, without a danger of accidental self-crossing and without a possibility to end up with multiple orders on one side. Quotes are always good-till-cancel limit orders.

Unlike order amends, quote replacements are not "volume-safe", i.e. the amount set in the quote will become visible in the order book, regardless of any trades on the quote that was replaced. Quote replacements will retain priority only when replacing a quote with the same price and size. Every quote is effectively a new order (and will show up as such in subscription feeds).

Mass quotes are not checked against price collars.

Quotes may be streamed continuously, without waiting for responses. It is not possible to somehow lose track of quotes -- eventually, the last-sent version will take effect.

Mass quotes are always subject to market maker protection. Market maker protection is configured on a per-session per-product basis, and this must be done before any quotes are sent on the respective session and product. A product is e.g. OBTCUSD (BTC options) or FBTCUSD (BTC futures).

Market maker protection is configured by setting some maximum trade and quote amounts for a product. Once that trade amount has traded, all remaining quotes for the product are cancelled automatically, as will any new quotes. Protection can be 'refilled' by sending another configuration request. No quotes may be sent with an amount exceeding the most recent quote amount.

A protection group is the market maker protection set for a product group within a session.

Configuration requests are not additive -- if multiple requests are sent for the same product, the last one will take effect.

When quoting the same product in multiple parallel sessions (WebSocket connections), it is important to keep in mind that the market maker protection configuration for each session is independent. This means that the maximum amount setting on a session only applies to the quotes submitted in that particular session. Traded amount is counted only for the quotes that are sent in the session. Only those quotes will be cancelled if the amount is exhausted, quotes managed over other connections will not be.

Market maker protection is evaluated by the matching engine after every new order request. It will not prevent multiple quotes in a single instrument from being hit/lifted by a single aggressor order, or quotes on different futures when these futures are linked through a roll.

In case a quote is amended through an order-amend request (private/amend), and if such an amend would lead to executions, then market maker protection is not evaluated for that order, only for the passively executed quotes.

Note that market maker protection is only applied to the orders that are managed with mass quotes. Regular orders are not part of the market maker protection and are not be cancelled when the configured maximum amount is exhausted.

Notifications
Notifications are directed to users and API keys, those users and API keys must be explicitly configured to receive notifications.

Notification categories
The following notification categories are defined:

system_announcement - system-wide notifications regarding technical matters, e.g. scheduled downtime notifications etc.

exchange_announcement - global exchange-related notifications, e.g. new strikes announcements etc.

deposit - notifications about deposits.

withdrawal - notifications about withdrawals.

new_password - notifications sent when user's password is changed or reset.

new_phone_number - notifications sent when user's phone number is changed.

new_email - notifications sent when user's e-mail address changes.

margin_call - margin call notifications sent when an account breaches initial margin requirements.

liquidation - notifications sent when an account breaches maintenance margin requirements and is liquidated.

new_signin_client_info - notifications sent when a web sign-in is detected from a new combination of device and IP address.

Message rates
The maximum number of matching engine messages (buy, sell, amend, etc.) per connection per second is 10. When the connection is set to non-persistent (private/set_cancel_on_disconnect), this limit is raised to 50.

The maximum number of cancel requests per connection per second is 1000.

The message rate limit is both the burst limit and the sustained frequency limit. Upon reaching the limit, all subsequent messages will fail for some time.

Self trade prevention
The self trade prevention mechanism prevents traders from matching their own orders in the order book.

There are three possible levels for this mechanism:

Customer (default) - A taker order is checked against all orders of all the accounts of a customer.

Account - A taker order is checked against all the orders of the account.

Disabled - Self trades are permitted.

And there are two possible actions when a self trade is detected:

Partial fill (default) - Cancel the taker order after partially filling from the top-of-book up until self-trade level.

No fill - Cancel the taker order with no fill.

Self trades are checked only on taker orders that have enabled self trade prevention.

By default all customers have self trade prevention enabled at a customer level with partial fill action.

The level and action can be overridden per order (eg. see stp_level and stp_action on private/insert), but only if self trade prevention configuration is enabled for the customer.

Market data
Active instruments

get
/public/instruments


Exchange: https://thalex.com/api/v2/public/instruments

Testnet: https://testnet.thalex.com/api/v2/public/instruments

Retrieves the list of currently active instruments.

Responses
200
Response Schema: application/json
One of SuccessError
result	
Array of objects (Instrument)
List of currently active instruments.

Array 
instrument_name	
string
product	
string
E.g. "FBTCUSD", "OBTCUSD".

tick_size	
number
Price alignment.

volume_tick_size	
number
Amount alignment.

min_order_amount	
number
Minimum order amount for this instrument. This value is always greater or equal to volume_tick_size.

If this value is greater than volume_tick_size, it is not possible to insert an order of a smaller amount, or amend an existing order to a smaller amount. However, orders in the books can have smaller remaining amounts as they get partially filled, down to the minimum of volume_tick_size.

underlying	
string
Related index, e.g. "BTCUSD".

type	
string
Enum: "perpetual" "future" "option" "combination"
option_type	
string
Enum: "call" "put"
expiry_date	
string
Expiration date in ISO format (YYYY-mm-dd).

expiration_timestamp	
integer
Expiration time as Unix timestamp (seconds).

strike_price	
number
Strike price of option.

base_currency	
string
Base currency for pricing (i.e. USD).

legs	
Array of objects
For combinations, array of objects with instrument_name and quantity.

Array 
instrument_name	
string
quantity	
integer
create_time	
number
Creation time (Unix timestamp).

settlement_price	
number
For expired instruments, the final settlement price.

settlement_index_price	
number
For expired instruments, the underlying delivery price.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
{
"instrument_name": "BTC-10SEP21-70000-C",
"product": "OBTCUSD",
"tick_size": 5,
"volume_tick_size": 0.1,
"min_order_amount": 0.1,
"underlying": "BTCUSD",
"type": "option",
"option_type": "call",
"expiry_date": "2021-09-10",
"expiration_timestamp": 1631260800,
"strike_price": 70000,
"base_currency": "USD",
"create_time": 1631250800.103645
}
]
}
All instruments

get
/public/all_instruments


Exchange: https://thalex.com/api/v2/public/all_instruments

Testnet: https://testnet.thalex.com/api/v2/public/all_instruments

Retrieves the list of all instruments that were active in the specified time interval.

Note that the time interval cannot be larger than 3 days.

You can also use public/instrument call to retrieve information about a specific instrument.

query Parameters
time_low	
number
Start time (Unix timestamp) defaults to time_high - 3 days.

time_high	
number
End time (Unix timestamp) defaults to now.

Responses
200
Response Schema: application/json
One of SuccessError
result	
Array of objects (Instrument)
List of all instruments that have not or only recently expired.

Array 
instrument_name	
string
product	
string
E.g. "FBTCUSD", "OBTCUSD".

tick_size	
number
Price alignment.

volume_tick_size	
number
Amount alignment.

min_order_amount	
number
Minimum order amount for this instrument. This value is always greater or equal to volume_tick_size.

If this value is greater than volume_tick_size, it is not possible to insert an order of a smaller amount, or amend an existing order to a smaller amount. However, orders in the books can have smaller remaining amounts as they get partially filled, down to the minimum of volume_tick_size.

underlying	
string
Related index, e.g. "BTCUSD".

type	
string
Enum: "perpetual" "future" "option" "combination"
option_type	
string
Enum: "call" "put"
expiry_date	
string
Expiration date in ISO format (YYYY-mm-dd).

expiration_timestamp	
integer
Expiration time as Unix timestamp (seconds).

strike_price	
number
Strike price of option.

base_currency	
string
Base currency for pricing (i.e. USD).

legs	
Array of objects
For combinations, array of objects with instrument_name and quantity.

Array 
instrument_name	
string
quantity	
integer
create_time	
number
Creation time (Unix timestamp).

settlement_price	
number
For expired instruments, the final settlement price.

settlement_index_price	
number
For expired instruments, the underlying delivery price.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
{
"instrument_name": "BTC-10SEP21-70000-C",
"product": "OBTCUSD",
"tick_size": 5,
"volume_tick_size": 0.1,
"min_order_amount": 0.1,
"underlying": "BTCUSD",
"type": "option",
"option_type": "call",
"expiry_date": "2021-09-10",
"expiration_timestamp": 1631260800,
"strike_price": 70000,
"base_currency": "USD",
"create_time": 1631250800.103645
}
]
}
Single instrument

get
/public/instrument


Exchange: https://thalex.com/api/v2/public/instrument

Testnet: https://testnet.thalex.com/api/v2/public/instrument

Retrieves a singe instrument.

Unlike public/all_instruments, this API endpoint allows retrieving information about instruments that have expired long time ago.

query Parameters
instrument_name
required
string
Name of the instrument to query.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (Instrument)
instrument_name	
string
product	
string
E.g. "FBTCUSD", "OBTCUSD".

tick_size	
number
Price alignment.

volume_tick_size	
number
Amount alignment.

min_order_amount	
number
Minimum order amount for this instrument. This value is always greater or equal to volume_tick_size.

If this value is greater than volume_tick_size, it is not possible to insert an order of a smaller amount, or amend an existing order to a smaller amount. However, orders in the books can have smaller remaining amounts as they get partially filled, down to the minimum of volume_tick_size.

underlying	
string
Related index, e.g. "BTCUSD".

type	
string
Enum: "perpetual" "future" "option" "combination"
option_type	
string
Enum: "call" "put"
expiry_date	
string
Expiration date in ISO format (YYYY-mm-dd).

expiration_timestamp	
integer
Expiration time as Unix timestamp (seconds).

strike_price	
number
Strike price of option.

base_currency	
string
Base currency for pricing (i.e. USD).

legs	
Array of objects
For combinations, array of objects with instrument_name and quantity.

Array 
instrument_name	
string
quantity	
integer
create_time	
number
Creation time (Unix timestamp).

settlement_price	
number
For expired instruments, the final settlement price.

settlement_index_price	
number
For expired instruments, the underlying delivery price.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"instrument_name": "BTC-10SEP21-70000-C",
"product": "OBTCUSD",
"tick_size": 5,
"volume_tick_size": 0.1,
"min_order_amount": 0.1,
"underlying": "BTCUSD",
"type": "option",
"option_type": "call",
"expiry_date": "2021-09-10",
"expiration_timestamp": 1631260800,
"strike_price": 70000,
"base_currency": "USD",
"create_time": 1631250800.103645
}
}
Single ticker value

get
/public/ticker


Exchange: https://thalex.com/api/v2/public/ticker

Testnet: https://testnet.thalex.com/api/v2/public/ticker

Retrieves a single ticker for a single instrument. Please do not use this to repeatedly poll for data -- a websocket subscription is much more useful.

query Parameters
instrument_name
required
string
Name of the instrument to query.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (Ticker)
best_bid_price	
number
Price of the best (highest) bid in the orderbook, or null if the orderbook is empty.

best_bid_amount	
number
Size of best bid, or null if the orderbook is empty.

best_ask_price	
number
Price of best (lowest) ask in the orderbook, or null if the orderbook is empty.

best_ask_amount	
number
Size of best ask, or null if the orderbook is empty.

last_price	
number
Price of last trade, or null if no trades have been registered yet.

Not included for combinations.

mark_price	
number
Current mark price.

mark_timestamp	
number
The unix timestamp when the price was marked.

iv	
number
Implied volatility calculated at time of marking.

Only included for options. Not included for combinations.

delta	
number
Delta calculated at time of marking.

Not included for combinations.

index	
number
Index price at time of marking.

forward	
number
Forward price at time of marking.

Only included for options.

volume_24h	
number
Total volume traded over the last 24 hours.

Not included for combinations.

value_24h	
number
Total value traded over the last 24 hours.

Not included for combinations.

low_price_24h	
number
Lowest price in the last 24 hours.

Not included for combinations.

high_price_24h	
number
Highest price in the last 24 hours.

Not included for combinations.

change_24h	
number
Difference in price between the first and the last trades in the last 24 hours, null if there were no trades.

Not included for combinations.

collar_low	
number
Current price collar low (checks new asks)

collar_high	
number
Current price collar high (checks new bids)

open_interest	
number
Total number of outstanding unsettled contracts.

Not included for combinations.

funding_rate	
number
Current rate at which long position pays and short position earns, in funding interval.

Only included for perpetuals.

funding_mark	
number
Funding value of a single contract long position since last settlement.

Only included for perpetuals.

realised_funding_24h	
number
Total funding accumulated for a single contract long position over the last 24 hours.

Only included for perpetuals.

average_funding_rate_24h	
number
Average funding rate for the last 24 hours.

Only included for perpetuals.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"mark_price": 47238.64143906124,
"mark_timestamp": 946684800,
"best_bid_price": 47240,
"best_bid_amount": 0.4,
"best_ask_price": 47260,
"best_ask_amount": 1,
"delta": 1,
"volume_24h": 0,
"value_24h": 0,
"open_interest": 123.456
}
}
Single index value

get
/public/index


Exchange: https://thalex.com/api/v2/public/index

Testnet: https://testnet.thalex.com/api/v2/public/index

Retrieves the index price for a single underlying. If needed repeatedly, please use the price_index.<underlying> websocket subscription.

query Parameters
underlying
required
string
The underlying (e.g. BTCUSD).

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (Index)
index_name
required
string
price
required
number
timestamp
required
number
The unix timestamp when the index price was recorded in the database.

expiration_print_average	
number
The average price so far over the current expiration, if any.

expiration_progress	
number
A number between 0.0 and 1.0 indicating the progress of the current expiration.

expected_expiration_price	
number
If expiration is in progress, and the index price will not change any more, this is the expiration price. Equals expiration_progress * expiration_print_average + (1 - expiration_progress) * price.

previous_settlement_price	
number
The last known settlement price (expiration price, underlying delivery price).

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"index_name": "BTCUSD",
"price": 47389.10833333334,
"timestamp": 946684800
}
}
Single order book

get
/public/book


Exchange: https://thalex.com/api/v2/public/book

Testnet: https://testnet.thalex.com/api/v2/public/book

Retrieves aggregated price depth for a single instrument, with a maximum of 5 levels. Please do not use this to poll for data -- a websocket subscription is more flexible and more useful.

query Parameters
instrument_name
required
string
Name of the instrument to query.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
bids
required
Array of numbers[ items ]
Bids (list of price, amount, outright-amount)

asks
required
Array of numbers[ items ]
Asks (list of price, amount, outright-amount)

last	
number
Last traded price

time
required
number
Time of the last recorded update to this order book (Unix timestamp).

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"result": {
"bids": [
[]
],
"asks": [ ],
"last": 26500,
"time": 1683901717.209106
}
}
}
Trading
Insert order

post
/private/insert


Exchange: https://thalex.com/api/v2/private/insert

Testnet: https://testnet.thalex.com/api/v2/private/insert

Insert an order

Request Body schema: application/json
direction
required
string
Enum: "buy" "sell"
client_order_id	
integer
Session-local identifier for this order. Only valid for websocket sessions. If set, must be an integer between 0 and 2^64-1, inclusive. When using numbers larger than 2^32, please beware of implicit floating point conversions in some JSON libraries.

instrument_name	
string
Name of the instrument to trade.

This field must not be present when inserting a combination order. Use legs field instead.

legs	
Array of objects
List of legs for a combination order.

There must be at least two and at most four legs specified. All leg instruments must be distinct.

Other constraints apply, please check trading information page on combination orders.

This field must not be present when inserting single-leg orders. Use instrument_name field instead.

Array 
instrument_name
required
string
Name of the instrument to trade on this leg.

quantity
required
number
Quantity of this leg in a unit of the combination. Must be integer. Must not be zero. Use a negative number for short legs.

Result of multiplication of quantity and order amount must be aligned to tick size for every leg.

price	
number
Limit price; required for limit orders.

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Amount of currency to trade (e.g. BTC for futures).

For combination orders this specifies the amount of units of the combination to trade.

label	
string
order_type	
string
Default: "limit"
Enum: "limit" "market"
time_in_force	
string
Enum: "good_till_cancelled" "immediate_or_cancel"
Note that for limit orders, the default time_in_force is good_till_cancelled, while for market orders, the default is immediate_or_cancel. It is illegal to send a GTC market order, or an IOC post order.

For combination orders time_in_force must always be set to immediate_or_cancel.

post_only	
boolean
If the order price is in cross with the current best price on the opposite side in the order book, then the price is adjusted to one tick away from that price, ensuring that the order will never trade on insert. If the adjusted price of a buy order falls at or below zero where not allowed, then the order is cancelled with delete reason 'immediate_cancel'.

This flag is not supported for combination orders.

reject_post_only	
boolean
This flag is only effective in combination with post_only. If set, then instead of adjusting the order price, the order will be cancelled with delete reason 'immediate_cancel'. The combination of post_only and reject_post_only is effectively a book-or-cancel order.

This flag is not supported for combination orders.

reduce_only	
boolean
An order marked reduce_only will have its amount reduced to the open position. If there is no open position, or if the order direction would cause an increase of the open position, the order is rejected. If the order is placed in the book, it will be subsequently monitored, and reduced to the open position if the position changes through other means (best effort). Multiple reduce-only orders will all be reduced individually.

This flag is not supported for combination orders.

collar	
string
Enum: "ignore" "reject" "clamp"
If the instrument has a safety price collar set, and the limit price of the order (infinite for market orders) is in cross with (more aggressive than) this collar, how to handle. If set to ignore, the order will proceed as requested. If reject, the order fails early. If clamp, the price is adjusted to the collar.

The default is clamp for market orders and reject for everything else.

Collar ignore is forbidden for market orders.

Price collars are applied to combination orders. Price collar for a combination is a linear combination of the leg collars with their corresponding quantities as coefficients.

stp_level	
string
Enum: "customer" "account" "disabled"
The self trade prevention level override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is customer and not configurable.

stp_action	
string
Enum: "cancel_aggressive_partial_fill" "cancel_aggressive_no_fill"
The self trade prevention action override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is cancel_aggressive_partial_fill and not configurable.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (OrderStatus)
Order status.

order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
{
"direction": "buy",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit"
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "buy",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
}
Insert buy order

post
/private/buy


Exchange: https://thalex.com/api/v2/private/buy

Testnet: https://testnet.thalex.com/api/v2/private/buy

Insert buy order

Request Body schema: application/json
client_order_id	
integer
Session-local identifier for this order. Only valid for websocket sessions. If set, must be an integer between 0 and 2^64-1, inclusive. When using numbers larger than 2^32, please beware of implicit floating point conversions in some JSON libraries.

instrument_name	
string
Name of the instrument to trade.

This field must not be present when inserting a combination order. Use legs field instead.

legs	
Array of objects
List of legs for a combination order.

There must be at least two and at most four legs specified. All leg instruments must be distinct.

Other constraints apply, please check trading information page on combination orders.

This field must not be present when inserting single-leg orders. Use instrument_name field instead.

Array 
instrument_name
required
string
Name of the instrument to trade on this leg.

quantity
required
number
Quantity of this leg in a unit of the combination. Must be integer. Must not be zero. Use a negative number for short legs.

Result of multiplication of quantity and order amount must be aligned to tick size for every leg.

price	
number
Limit price; required for limit orders.

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Amount of currency to trade (e.g. BTC for futures).

For combination orders this specifies the amount of units of the combination to trade.

label	
string
order_type	
string
Default: "limit"
Enum: "limit" "market"
time_in_force	
string
Enum: "good_till_cancelled" "immediate_or_cancel"
Note that for limit orders, the default time_in_force is good_till_cancelled, while for market orders, the default is immediate_or_cancel. It is illegal to send a GTC market order, or an IOC post order.

For combination orders time_in_force must always be set to immediate_or_cancel.

post_only	
boolean
If the order price is in cross with the current best price on the opposite side in the order book, then the price is adjusted to one tick away from that price, ensuring that the order will never trade on insert. If the adjusted price of a buy order falls at or below zero where not allowed, then the order is cancelled with delete reason 'immediate_cancel'.

This flag is not supported for combination orders.

reject_post_only	
boolean
This flag is only effective in combination with post_only. If set, then instead of adjusting the order price, the order will be cancelled with delete reason 'immediate_cancel'. The combination of post_only and reject_post_only is effectively a book-or-cancel order.

This flag is not supported for combination orders.

reduce_only	
boolean
An order marked reduce_only will have its amount reduced to the open position. If there is no open position, or if the order direction would cause an increase of the open position, the order is rejected. If the order is placed in the book, it will be subsequently monitored, and reduced to the open position if the position changes through other means (best effort). Multiple reduce-only orders will all be reduced individually.

This flag is not supported for combination orders.

collar	
string
Enum: "ignore" "reject" "clamp"
If the instrument has a safety price collar set, and the limit price of the order (infinite for market orders) is in cross with (more aggressive than) this collar, how to handle. If set to ignore, the order will proceed as requested. If reject, the order fails early. If clamp, the price is adjusted to the collar.

The default is clamp for market orders and reject for everything else.

Collar ignore is forbidden for market orders.

Price collars are applied to combination orders. Price collar for a combination is a linear combination of the leg collars with their corresponding quantities as coefficients.

stp_level	
string
Enum: "customer" "account" "disabled"
The self trade prevention level override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is customer and not configurable.

stp_action	
string
Enum: "cancel_aggressive_partial_fill" "cancel_aggressive_no_fill"
The self trade prevention action override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is cancel_aggressive_partial_fill and not configurable.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (OrderStatus)
Order status.

order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
{
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit"
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "buy",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
}
Insert sell order

post
/private/sell


Exchange: https://thalex.com/api/v2/private/sell

Testnet: https://testnet.thalex.com/api/v2/private/sell

Insert sell order

Request Body schema: application/json
client_order_id	
integer
Session-local identifier for this order. Only valid for websocket sessions. If set, must be an integer between 0 and 2^64-1, inclusive. When using numbers larger than 2^32, please beware of implicit floating point conversions in some JSON libraries.

instrument_name	
string
Name of the instrument to trade.

This field must not be present when inserting a combination order. Use legs field instead.

legs	
Array of objects
List of legs for a combination order.

There must be at least two and at most four legs specified. All leg instruments must be distinct.

Other constraints apply, please check trading information page on combination orders.

This field must not be present when inserting single-leg orders. Use instrument_name field instead.

Array 
instrument_name
required
string
Name of the instrument to trade on this leg.

quantity
required
number
Quantity of this leg in a unit of the combination. Must be integer. Must not be zero. Use a negative number for short legs.

Result of multiplication of quantity and order amount must be aligned to tick size for every leg.

price	
number
Limit price; required for limit orders.

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Amount of currency to trade (e.g. BTC for futures).

For combination orders this specifies the amount of units of the combination to trade.

label	
string
order_type	
string
Default: "limit"
Enum: "limit" "market"
time_in_force	
string
Enum: "good_till_cancelled" "immediate_or_cancel"
Note that for limit orders, the default time_in_force is good_till_cancelled, while for market orders, the default is immediate_or_cancel. It is illegal to send a GTC market order, or an IOC post order.

For combination orders time_in_force must always be set to immediate_or_cancel.

post_only	
boolean
If the order price is in cross with the current best price on the opposite side in the order book, then the price is adjusted to one tick away from that price, ensuring that the order will never trade on insert. If the adjusted price of a buy order falls at or below zero where not allowed, then the order is cancelled with delete reason 'immediate_cancel'.

This flag is not supported for combination orders.

reject_post_only	
boolean
This flag is only effective in combination with post_only. If set, then instead of adjusting the order price, the order will be cancelled with delete reason 'immediate_cancel'. The combination of post_only and reject_post_only is effectively a book-or-cancel order.

This flag is not supported for combination orders.

reduce_only	
boolean
An order marked reduce_only will have its amount reduced to the open position. If there is no open position, or if the order direction would cause an increase of the open position, the order is rejected. If the order is placed in the book, it will be subsequently monitored, and reduced to the open position if the position changes through other means (best effort). Multiple reduce-only orders will all be reduced individually.

This flag is not supported for combination orders.

collar	
string
Enum: "ignore" "reject" "clamp"
If the instrument has a safety price collar set, and the limit price of the order (infinite for market orders) is in cross with (more aggressive than) this collar, how to handle. If set to ignore, the order will proceed as requested. If reject, the order fails early. If clamp, the price is adjusted to the collar.

The default is clamp for market orders and reject for everything else.

Collar ignore is forbidden for market orders.

Price collars are applied to combination orders. Price collar for a combination is a linear combination of the leg collars with their corresponding quantities as coefficients.

stp_level	
string
Enum: "customer" "account" "disabled"
The self trade prevention level override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is customer and not configurable.

stp_action	
string
Enum: "cancel_aggressive_partial_fill" "cancel_aggressive_no_fill"
The self trade prevention action override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is cancel_aggressive_partial_fill and not configurable.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (OrderStatus)
Order status.

order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
{
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit"
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "sell",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
}
Amend order

post
/private/amend


Exchange: https://thalex.com/api/v2/private/amend

Testnet: https://testnet.thalex.com/api/v2/private/amend

Note that amount designates the new "original" amount, i.e. the amend is volume-safe. If the specified amount is lower than the already executed amount, the order is deleted.

If the price of the order is the same as the previous price, and the amount is less than the previous amount, book priority is preserved.

If the amount is amended to a value at or below the executed amount, the order is cancelled.

Request Body schema: application/json
client_order_id	
integer
Exactly one of client_order_id or order_id must be specified.

order_id	
string
Exactly one of client_order_id or order_id must be specified.

price
required
number
amount
required
number
collar	
string
Enum: "ignore" "reject" "clamp"
If the instrument has a safety price collar set, and the new limit price is in cross with (more aggressive than) this collar, how to handle. If set to ignore, the amend will proceed as requested. If reject, the request fails early. If clamp, the price is adjusted to the collar.

The default is reject.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (OrderStatus)
Order status.

order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
{
"order_id": "1728379719872",
"price": 40000,
"amount": 1.1
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 40000,
"amount": 1.1,
"order_type": "limit",
"direction": "sell",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "amend",
"insert_reason": "client_request"
}
}
Cancel order

post
/private/cancel


Exchange: https://thalex.com/api/v2/private/cancel

Testnet: https://testnet.thalex.com/api/v2/private/cancel

Cancel order

Request Body schema: application/json
client_order_id	
integer
Exactly one of client_order_id or order_id must be specified.

order_id	
string
Exactly one of client_order_id or order_id must be specified.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (OrderStatus)
Order status.

order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
{
"order_id": "1728379719872"
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 40000,
"amount": 1.1,
"order_type": "limit",
"direction": "sell",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "cancelled",
"fills": [ ],
"change_reason": "cancel",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"close_time": 1702583649.379417
}
}
Bulk cancel all orders

post
/private/cancel_all


Exchange: https://thalex.com/api/v2/private/cancel_all

Testnet: https://testnet.thalex.com/api/v2/private/cancel_all

Cancels all orders for the account. This may not match new orders in flight (see private/cancel_session).

Request Body schema: application/json
object (EmptyObject)
Empty object.

Responses
200
Response Schema: application/json
One of SuccessError
result	
number
The number of orders successfully deleted.

Request samples
Payload
Content type
application/json

Copy
{ }
Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": 42
}
Request for Quote
Create a request for quote

post
/private/create_rfq


Exchange: https://thalex.com/api/v2/private/create_rfq

Testnet: https://testnet.thalex.com/api/v2/private/create_rfq

Creates a new RFQ. You do not have to indicate upfront whether you want to buy or sell this package. Indicate the full size of the package.

Request Body schema: application/json
legs
required
Array of objects
Specify any number of legs that you'd like to trade in a single package. Leg amounts may be positive (long) or negative (short), and must adhere to the regular volume tick size for the respective instrument. At least one leg must be long.

Array 
instrument_name
required
string
The leg instrument. Must be an outright instrument, not a combination.

amount
required
number
Amount to trade for this leg. Negative for short.

label	
string
User label for this RFQ, which will be reflected in eventual trades.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (Rfq)
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"legs": [
{
"instrument_name": "string",
"amount": 0
}
]
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [
{
"instrument_name": "string",
"quantity": 0,
"fee_quantity": 0
}
],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {
"price": 0,
"amount": 0
},
"quoted_ask": {
"price": 0,
"amount": 0
},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
}
Cancel an RFQ

post
/private/cancel_rfq


Exchange: https://thalex.com/api/v2/private/cancel_rfq

Testnet: https://testnet.thalex.com/api/v2/private/cancel_rfq

Cancels the indicated RFQ.

Request Body schema: application/json
rfq_id
required
string
The ID of the RFQ to be cancelled

Responses
200
Response Schema: application/json
One of SuccessError
result	
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
{
"rfq_id": "string"
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": null
}
Trade an RFQ

post
/private/trade_rfq


Exchange: https://thalex.com/api/v2/private/trade_rfq

Testnet: https://testnet.thalex.com/api/v2/private/trade_rfq

Trade on the quotes given. The requested amount is that of the original request.

Request Body schema: application/json
rfq_id
required
string
The ID of the RFQ

direction
required
string
Enum: "buy" "sell"
Whether to buy or sell. Important: this relates to the combination as created by the system, not the package as originally requested (although they should be equal).

limit_price
required
number
The maximum (for buy) or minimum (for sell) price to trade at. This is the price for one combination, not for the entire package.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
rfq_id
required
string
The RFQ traded.

direction
required
string
Enum: "buy" "sell"
The direction of the trade as requested.

price
required
number
The trade price per combination.

amount
required
number
The number of combinations traded.

legs
required
Array of objects
The trades on the individual legs.

Array 
instrument_name
required
string
direction
required
string
Enum: "buy" "sell"
The trade direction for this leg.

amount
required
number
The total amount traded on this leg.

Request samples
Payload
Content type
application/json

Copy
{
"rfq_id": "string",
"direction": "buy",
"limit_price": 0
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"rfq_id": "string",
"direction": "buy",
"price": 0,
"amount": 0,
"legs": [
{
"instrument_name": "string",
"direction": "buy",
"amount": 0
}
]
}
}
Open RFQs

get
/private/open_rfqs


Exchange: https://thalex.com/api/v2/private/open_rfqs

Testnet: https://testnet.thalex.com/api/v2/private/open_rfqs

Retrieves a list of open RFQs created by this account.

Responses
200
Response Schema: application/json
One of SuccessError
result	
Array of objects (Rfq)
List of open RFQs.

Array 
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
{
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [
{}
],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {
"price": 0,
"amount": 0
},
"quoted_ask": {
"price": 0,
"amount": 0
},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
]
}
Request for Quote (MM)
Open RFQs

get
/private/mm_rfqs


Exchange: https://thalex.com/api/v2/private/mm_rfqs

Testnet: https://testnet.thalex.com/api/v2/private/mm_rfqs

Retrieves a list of open RFQs that this account has access to.

Responses
200
Response Schema: application/json
One of SuccessError
result	
Array of objects (Rfq)
List of open RFQs.

Array 
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
{
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [
{}
],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {
"price": 0,
"amount": 0
},
"quoted_ask": {
"price": 0,
"amount": 0
},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
]
}
Quote on an RFQ

post
/private/mm_rfq_insert_quote


Exchange: https://thalex.com/api/v2/private/mm_rfq_insert_quote

Testnet: https://testnet.thalex.com/api/v2/private/mm_rfq_insert_quote

Sends a new quote on the indicated RFQ. This does not remove any previous quote: any number of quotes may be active on either side. Note that if the session was set to non-persistent (cancel-on-disconnect), then this quote will also be non-persistent.

Request Body schema: application/json
rfq_id
required
string
The ID of the RFQ this quote is for.

client_order_id	
integer
Session-local identifier for this order. Only valid for websocket sessions. If set, must be a number between 0 and 2^64-1, inclusive. When using numbers larger than 2^32, please beware of implicit floating point conversions in some JSON libraries.

direction
required
string
Enum: "buy" "sell"
The side of the quote.

price
required
number
Limit price for the quote (for one combination).

amount
required
number
Number of combinations to quote. Anything over the requested amount will not be visible to the requester.

label	
string
A label to attach to eventual trades.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (RfqOrder)
rfq_id
required
string
Identifier of the RFQ.

order_id
required
string
Identifier of the individual quote.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

direction
required
string
Enum: "buy" "sell"
price
required
number
amount
required
number
label	
string
trade_price	
number
the price at which this order traded.

trade_amount	
number
the number of combinations that traded.

delete_reason	
string
Enum: "client_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled"
Detailed reason of order deletion.

event	
string
Enum: "Inserted" "Amended" "Cancelled" "Filled" "Existing"
This field is set only on subscriptions.

Request samples
Payload
Content type
application/json

Copy
{
"rfq_id": "string",
"direction": "buy",
"price": 0,
"amount": 0
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"rfq_id": "string",
"order_id": "string",
"client_order_id": 0,
"direction": "buy",
"price": 0,
"amount": 0,
"label": "string",
"trade_price": 0,
"trade_amount": 0,
"delete_reason": "client_cancel",
"event": "Inserted"
}
}
Amend quote

post
/private/mm_rfq_amend_quote


Exchange: https://thalex.com/api/v2/private/mm_rfq_amend_quote

Testnet: https://testnet.thalex.com/api/v2/private/mm_rfq_amend_quote

Change the amount and price of an existing quote.

Request Body schema: application/json
client_order_id	
integer
Exactly one of client_order_id or order_id must be specified.

order_id	
string
Exactly one of client_order_id or order_id must be specified.

price
required
number
Limit price for the quote (for one combination).

amount
required
number
Number of combinations to quote. Anything over the requested amount will not be visible to the requester.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (RfqOrder)
rfq_id
required
string
Identifier of the RFQ.

order_id
required
string
Identifier of the individual quote.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

direction
required
string
Enum: "buy" "sell"
price
required
number
amount
required
number
label	
string
trade_price	
number
the price at which this order traded.

trade_amount	
number
the number of combinations that traded.

delete_reason	
string
Enum: "client_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled"
Detailed reason of order deletion.

event	
string
Enum: "Inserted" "Amended" "Cancelled" "Filled" "Existing"
This field is set only on subscriptions.

Request samples
Payload
Content type
application/json

Copy
{
"price": 0,
"amount": 0
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"rfq_id": "string",
"order_id": "string",
"client_order_id": 0,
"direction": "buy",
"price": 0,
"amount": 0,
"label": "string",
"trade_price": 0,
"trade_amount": 0,
"delete_reason": "client_cancel",
"event": "Inserted"
}
}
Delete quote

post
/private/mm_rfq_delete_quote


Exchange: https://thalex.com/api/v2/private/mm_rfq_delete_quote

Testnet: https://testnet.thalex.com/api/v2/private/mm_rfq_delete_quote

Deletes the indicated RFQ quote.

Request Body schema: application/json
client_order_id	
integer
Exactly one of client_order_id or order_id must be specified.

order_id	
string
Exactly one of client_order_id or order_id must be specified.

Responses
200
Response Schema: application/json
One of SuccessError
result	
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
{ }
Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": null
}
List of active quotes

get
/private/mm_rfq_quotes


Exchange: https://thalex.com/api/v2/private/mm_rfq_quotes

Testnet: https://testnet.thalex.com/api/v2/private/mm_rfq_quotes

Retrieves a list of open RFQ quotes across all RFQs.

Responses
200
Response Schema: application/json
One of SuccessError
result	
Array of objects (RfqOrder)
Array 
rfq_id
required
string
Identifier of the RFQ.

order_id
required
string
Identifier of the individual quote.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

direction
required
string
Enum: "buy" "sell"
price
required
number
amount
required
number
label	
string
trade_price	
number
the price at which this order traded.

trade_amount	
number
the number of combinations that traded.

delete_reason	
string
Enum: "client_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled"
Detailed reason of order deletion.

event	
string
Enum: "Inserted" "Amended" "Cancelled" "Filled" "Existing"
This field is set only on subscriptions.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
{
"rfq_id": "string",
"order_id": "string",
"client_order_id": 0,
"direction": "buy",
"price": 0,
"amount": 0,
"label": "string",
"trade_price": 0,
"trade_amount": 0,
"delete_reason": "client_cancel",
"event": "Inserted"
}
]
}
Accounting
Portfolio

get
/private/portfolio


Exchange: https://thalex.com/api/v2/private/portfolio

Testnet: https://testnet.thalex.com/api/v2/private/portfolio

Get account portfolio

Responses
200
Response Schema: application/json
One of SuccessError
result	
Array of objects (PortfolioEntry)
Portfolio positions.

Array 
instrument_name	
string
Instrument name.

position	
number
Amount of this contract currently held; short positions are negative.

mark_price	
number
Current mark price for the instrument.

iv	
number
Implied volatility calculated at time of marking.

index	
number
Index price at time of marking.

start_price	
number
Average price paid to obtain position.

Note: for instruments that are subject to daily futures-style settlement, the start price is reset to the mark price at the end of each session and all the unrealized P&L is thus realized. Use private/daily_mark_history API endpoint to get information about daily settlements.

average_price	
number
Average price paid to obtain position. Doesn't reset at settlement.

unrealised_pnl	
number
Unrealised P&L in the current session for this position based on current mark price, equal to (mark_price - start_price) * position.

Note: for instruments that are subject to daily futures-style settlement, the start price is reset to the mark price at the end of each session and all the unrealized P&L is thus realized. Use private/daily_mark_history API endpoint to get information about daily settlements.

realised_pnl	
number
Realized P&L in the current session.

Realized P&L is settled into a settlement asset at the end of each session.

entry_value	
number
Total entry value, equal to start_price * position.

perpetual_funding_entry_value	
number
Entry mark value for perpetual funding. Unrealised perpetual funding is (current perp funding mark * position) - perpetual funding entry value. Not included if zero.

unrealised_perpetual_funding	
number
For perpetual positions, current unrealized perpetual funding.

The funding is realized as P&L and settled into settlement asset at the end of each session.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
{
"instrument_name": "BTC-PERPETUAL",
"position": 1,
"mark_price": 47299.741264339274,
"start_price": 47260,
"average_price": 47260,
"unrealised_pnl": 39.75859976453942,
"realised_pnl": 0,
"entry_value": 47260,
"perpetual_funding_entry_value": -0.13040705,
"unrealised_perpetual_funding": 0.017335425264924917
}
]
}
Open orders

get
/private/open_orders


Exchange: https://thalex.com/api/v2/private/open_orders

Testnet: https://testnet.thalex.com/api/v2/private/open_orders

Get open orders

Responses
200
Response Schema: application/json
One of SuccessError
result	
Array of objects (OrderStatus)
All currently open orders for the account.

Array 
order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
{
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "buy",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
]
}
Order history

get
/private/order_history


Exchange: https://thalex.com/api/v2/private/order_history

Testnet: https://testnet.thalex.com/api/v2/private/order_history

Retrieves a list of past orders (i.e. orders that are not active anymore) since the last 90 days. Allows sorting and filtering by instrument name.

Unfilled market maker orders are not included.

Orders are like order status updates, without the remaining_amount field (always 0), and with a close_time timestamp. Note that, for technical reasons, the 'fills' field in the order is limited to a length of 8. For a full list of trades, refer to trade history.

Note that it is not real-time, data might appear with a slight delay.

query Parameters
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to 90 days ago.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

sort	
string
Enum: "ascending" "descending"
Sort direction by order close_time. Defaults to descending (i.e. newest items first).

instrument_names	
string
Comma-separated list of instrument names to request order history for. If omitted, order history for all instruments is returned.

bot_ids	
string
Optional comma-separated list of bot IDs to request order history history for.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
orders	
Array of objects (OrderHistory)
List of historical orders.

Array 
order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
All fills for this order.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

delete_reason
required
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

self_trade_prevention: The order was cancelled by the self trade prevention mechanism.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time
required
number
Time when this order was closed or canceled (Unix timestamp).

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"orders": [
{
"order_id": "001BF14D00000003",
"instrument_name": "BTC-16DEC23-46000-C",
"direction": "sell",
"price": "10.0,",
"amount": "0.2,",
"filled_amount": "0.2,",
"status": "filled",
"fills": [],
"create_time": "1702583649.379417,",
"close_time": "1702583649.379417,",
"insert_reason": "client_request",
"delete_reason": "filled",
"order_type": "limit"
}
],
"bookmark": "string"
}
}
Conditional order history

get
/private/conditional_order_history


Exchange: https://thalex.com/api/v2/private/conditional_order_history

Testnet: https://testnet.thalex.com/api/v2/private/conditional_order_history

Retrieves a list of past conditional orders (i.e. orders that are not active anymore). Allows sorting and filtering by instrument name.

Note that it is not real-time, data might appear with a slight delay.

query Parameters
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to 90 days ago.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

sort	
string
Enum: "ascending" "descending"
Sort direction by order create_time. Defaults to descending (i.e. newest items first).

instrument_names	
string
Comma-separated list of instrument names to request order history for. If omitted, order history for all instruments is returned.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
orders	
Array of objects (ConditionalOrder)
List of historical conditional orders.

Array 
order_id
required
string
Unique ID, use to identify in cancel

instrument_name
required
string
direction
required
string
Enum: "buy" "sell"
amount
required
number
Size of the order when activated

target
required
string
Enum: "last" "mark" "index"
The trigger type that stop_price and bracket_price will refer to.

stop_price
required
number
Trigger price at which the order will be activated

limit_price	
number
For stop limit order, the price at which the order will be placed

bracket_price	
number
For bracket order, the price at which profit will be taken (upper activation price)

trailing_stop_callback_rate	
number
For trailing stop loss, the callback rate as a ratio (e.g. 0.05 for 5%)

label	
string
Optional user label

status
required
string
Enum: "created" "active" "converted" "rejected" "cancel requested" "cancelled"
create_time
required
number
update_time
required
number
Time of last update (conversion or change of trailing stop price)

convert_time	
number
Time of trigger

converted_order_id	
string
System order ID of the created order.

reject_reason	
string
If conversion failed, the reason

reduce_only
required
boolean
bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"orders": [
{
"order_id": "00011E570000004B",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"amount": 1,
"stop_price": 50000,
"limit_price": 45000,
"status": "created",
"create_time": 1630062311.3324597,
"update_time": 1630062311.3324597,
"reduce_only": false,
"target": "mark"
}
],
"bookmark": "string"
}
}
Trade history

get
/private/trade_history


Exchange: https://thalex.com/api/v2/private/trade_history

Testnet: https://testnet.thalex.com/api/v2/private/trade_history

Retrieves trades for the last 90 days. Allows sorting and filtering by instrument name. Note that it is not real-time, trades might appear with a slight delay.

query Parameters
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to 90 days ago.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

sort	
string
Enum: "ascending" "descending"
Sort direction by trade time. Defaults to descending (i.e. newest trades first).

instrument_names	
string
Comma-separated list of instrument names to request trade history for. If omitted, trades for all instruments are returned.

bot_ids	
string
Optional comma-separated list of bot IDs to request trade history for.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
trades	
Array of objects (Trade)
List of trades.

Array 
trade_type	
string
Enum: "normal" "block" "combo" "amend" "delete" "internal_transfer" "expiration" "daily_mark" "rfq" "liquidation"
Type of the trade.

Note: as of API v2.31.0 we have stopped representing futures-style settlements as trades of daily_mark type. You might still get such trades in the history, but no new trades of daily_mark type will be created. To get information about daily marks, use private/daily_mark_history API endpoint.

trade_id	
string
order_id	
string
instrument_name	
string
direction	
string
Enum: "buy" "sell"
price	
number
Trade price.

amount	
number
Traded amount.

label	
string
User label.

time	
number
Time of trade (Unix timestamp).

position_after	
number
Position in this instrument right after the trade.

session_realised_after	
number
Session realised P&L for this instrument right after the trade.

position_pnl	
number
If trade closed a position, the positional P&L that was realised.

perpetual_funding_pnl	
number
If trade closed a position in a perpetual, the funding P&L that was realised.

fee	
number
The fee paid for this trade.

The fee for a trade is calculated as fee_basis * fee_rate * amount, and is then subject to clamping to minimum and maximum fee. Depending on the instrument, fee_basis can be different (e.g. it can be equal to the underlying index, trade price or combo mark price). Please refer to trading information pages for more details.

index	
number
The relevant index at time of trade.

fee_rate	
number
The fee rate applied to calculate the fee.

fee_basis	
number
The fee basis on which the fee is calculated.

funding_mark	
number
The perpetual funding mark as applied to the trade (see Ticker).

liquidation_fee	
number
Fee paid in case of liquidation.

client_order_id	
number
Client order reference as set in related order.

maker_taker	
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

bot_id	
string
If the trade was made by a bot, the ID of that bot. Otherwise omitted.

leg_index	
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"trades": [
{
"order_id": "00011E570000004A",
"trade_id": "0080000000000000169F22D05B785A2B",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"price": 47280,
"amount": 0.1,
"label": "",
"time": 1630059868.4145653,
"position_after": 1.1,
"trade_type": "normal",
"leg_index": 0
},
{
"order_id": "00011E570000004B",
"trade_id": "0080000000000000169F20CE441AD986",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"price": 47260,
"amount": 1,
"label": "",
"time": 1630057660.409371,
"position_after": 1,
"trade_type": "normal",
"leg_index": 0
}
]
}
}
Trading volume historical data.

get
/private/trade_value_history


Exchange: https://thalex.com/api/v2/private/trade_value_history

Testnet: https://testnet.thalex.com/api/v2/private/trade_value_history

Returns historical trading volume in the specified interval and resolution.

query Parameters
time_low
required
number
Start time (Unix timestamp) (inclusive).

time_high
required
number
End time (Unix timestamp) (inclusive).

resolution
required
string
Enum: "1d" "1w" "1mo"
Each trade value is aggregated per time resolution, underlying and category.

limit	
number
Default: 1000
The maximum number of primary items to return per page. Due to resolution grouping rules, a page may include additional items beyond the limit to ensure that all items sharing the same date_time_bucket as the last item within the limit are included.

bookmark	
string
Set to bookmark from previous call to get next page.

sort	
string
Enum: "ascending" "descending"
Responses
200
Response Schema: application/json
One of SuccessError
result	
object
trade_values	
Array of objects (TradeValue)
Array of trade value objects.

Array 
underlying
required
string
Underlying name.

trade_volume
required
number
Total trading volume for the underlying instrument category.

trade_value
required
number
The total value traded for the underlying instrument category.

category
required
string
Enum: "options" "futures" "perpetual"
Instrument category.

date_time_bucket
required
any
Start time of the aggregation interval (day, week, or month).

bookmark	
string
Set when additional data exists within or before the requested time interval.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"trade_values": [
{
"account_id": 861918865,
"underlying": "BTCUSD",
"trade_volume": 10,
"trade_value": 20,
"category": "options",
"date_time_bucket": "1704700800000000000"
}
],
"bookmark": "string"
}
}
Daily mark history

get
/private/daily_mark_history


Exchange: https://thalex.com/api/v2/private/daily_mark_history

Testnet: https://testnet.thalex.com/api/v2/private/daily_mark_history

For instruments that are subject to futures-style settlement we perform daily settlement at the mark price. The settlement procedure realizes the positional and perpetual funding profits/losses accumulated during the session, and resets the start price of the position to the mark price.

This API endpoint returns a historical log of settled profits/losses (daily marks).

query Parameters
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to zero.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
daily_marks	
Array of objects (DailyMark)
List of daily marks.

Array 
time
required
number
Time of settlement (Unix timestamp).

instrument_name
required
string
Instrument name.

position
required
number
Position in the instrument.

mark_price
required
number
Mark price used for settlement.

realized_position_pnl
required
number
Realized profit or loss for this position.

realized_funding_pnl	
number
Realized perpetual funding. Only present for perpetuals.

bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"daily_marks": [
{
"time": 1630059868.4145653,
"instrument_name": "BTC-PERPETUAL",
"mark_price": 47280,
"position": 0.1,
"realized_position_pnl": 1220,
"realized_funding_pnl": 10
},
{
"time": 1630059868.4145653,
"instrument_name": "BTC-27DEC24",
"mark_price": 48100,
"position": -0.5,
"realized_position_pnl": -405
}
]
}
}
Transaction history

get
/private/transaction_history


Exchange: https://thalex.com/api/v2/private/transaction_history

Testnet: https://testnet.thalex.com/api/v2/private/transaction_history

Get transaction history

query Parameters
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to zero.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
transactions
required
Array of objects
List of transactions.

Array 
time
required
number
Timestamp when the transaction was performed.

For actions that produce multiple transactions (e.g. asset swaps, internal transfers), all transactions will have the same timestamp.

asset
required
string
Asset name.

amount
required
number
Amount credited (positive number) or debited (negative number).

instrument_name	
string
Instrument name this transaction relates to. For example, settlement transactions are per instrument.

Not included for transactions that don't relate to an instrument.

transaction_type	
string
Enum: "credit" "deposit" "withdrawal" "withdrawal fee" "session settlement" "perpetual funding" "internal transfer" "asset swap" "referral program payment" "market velocity program payment" "market quality program payment" "daily interest"
Transaction type. Can be one of the following values:

credit - Asset credits or debits.
deposit - Deposits.
withdrawal - Withdrawals.
withdrawal fee - Withdrawal fees.
session settlement - Settled session PNL.
perpetual funding - Settled perpetual funding.
internal transfer - Transfer of assets between sub-accounts. One transaction in each sub-account per asset per transfer.
asset swap - Swap between assets. One transaction for each side of the asset pair per swap.
referral program payment - Referral program rewards.
market velocity program payment - MVP program rewards.
market quality program payment - MQP program rewards.
daily interest - Daily penalty charge for negative balance. Not applied anymore, but can be found in historical transactions.
description
required
string
Description of this transaction.

Note that this field is not supposed to be machine-readable and the the format is not guaranteed to remain unchanged.

balance_after	
number
Account balance in this asset right after transaction.

bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"transactions": [
{
"asset": "USDT",
"time": 1629964800.012722,
"amount": -643.70276425,
"description": "daily settlement USD -643.83220000 @ 1.000201",
"transaction_type": "session settlement",
"instrument_name": "BTC-PERPETUAL",
"balance_after": 1000000004483.9625
}
]
}
}
RFQ history

get
/private/rfq_history


Exchange: https://thalex.com/api/v2/private/rfq_history

Testnet: https://testnet.thalex.com/api/v2/private/rfq_history

Retrieves a list of past RFQs for the account. Open RFQs are not incuded.

query Parameters
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to zero.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
rfqs	
Array of objects (Rfq)
List of RFQs.

Array 
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.

bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"rfqs": [
{
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {},
"quoted_ask": {},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
],
"bookmark": "string"
}
}
Account breakdown

get
/private/account_breakdown


Exchange: https://thalex.com/api/v2/private/account_breakdown

Testnet: https://testnet.thalex.com/api/v2/private/account_breakdown

Get account breakdown

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
account_number
required
string
Account number

unrealised_pnl
required
number
Total unrealised profit or loss.

cash_collateral
required
number
Total margin based on cash holdings.

margin
required
number
Total margin from unrealised P&L and cash holdings.

required_margin
required
number
Required margin based on current position.

remaining_margin
required
number
Difference between margin and required margin.

session_realised_pnl
required
number
Total realised profit or loss in current session.

realised_position_pnl
required
number
Position profit or loss in current session.

realised_perpetual_funding
required
number
Realised perpetual funding profit or loss in current session.

session_fees
required
number
Fees paid in current session.

portfolio
required
Array of objects
List of positions each with unrealised P&L.

Array 
instrument_name
required
string
position
required
number
mark_price	
number
start_price	
number
average_price	
number
unrealised_pnl_positional
required
number
unrealised_pnl_perpetual	
number
unrealised_pnl
required
number
realised_position_pnl
required
number
open_buy_amount
required
number
open_sell_amount
required
number
session_realised_pnl
required
number
realised_perpetual_funding
required
number
session_fees
required
number
cash
required
Array of objects
List of cash holdings, for each relevant currency, and how they contribute to margin.

Array 
currency
required
string
Currency name.

balance
required
number
Current balance in this currency.

collateral_factor
required
number
The collateral quality of the asset i.e. the fraction of the asset that can be used as a collateral.

collateral_index_price	
number
Index price used to calculate collateral effect of this position. Can be null for assets that are not converted using an index, e.g. for stable coins.

applied_collateral
required
number
Total collateral effect of this position.

transactable
required
boolean
If this flag is true, this currency can be deposited and withdrawn.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"account_number": "A123456789",
"portfolio": [
{
"instrument_name": "BTC-PERPETUAL",
"position": 1.1,
"mark_price": 47708.13763778502,
"start_price": 47261.81818181818,
"average_price": 47261.81818181818,
"unrealised_pnl_positional": 490.95140156352136,
"unrealised_pnl_perpetual": 0.05837153649983011,
"unrealised_pnl": 491.00977310002116,
"open_buy_amount": 0,
"open_sell_amount": 0,
"session_realised_pnl": -1.18,
"realised_position_pnl": 0,
"realised_perpetual_funding": 0,
"session_fees": 1.18
}
],
"cash": [
{
"currency": "USDT",
"balance": 1000000004483.9625,
"collateral_factor": 1,
"collateral_index_price": null,
"applied_collateral": 1000000004483.9625,
"transactable": true
}
],
"unrealised_pnl": 491.00977310002116,
"session_realised_pnl": -1.18,
"realised_position_pnl": 0,
"realised_perpetual_funding": 0,
"session_fees": 1.18,
"cash_collateral": 1000000004483.9625,
"margin": 1000000004994.1586,
"required_margin": 13123.880458333333,
"remaining_margin": 999999991870.2781
}
}
Account summary

get
/private/account_summary


Exchange: https://thalex.com/api/v2/private/account_summary

Testnet: https://testnet.thalex.com/api/v2/private/account_summary

Get account summary

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (AccountSummary)
unrealised_pnl
required
number
Total unrealised profit or loss.

cash_collateral
required
number
Total margin based on cash holdings.

margin
required
number
Total margin from unrealised P&L and cash holdings.

required_margin
required
number
Required margin based on current position.

remaining_margin
required
number
Difference between margin and required margin.

session_realised_pnl
required
number
Realised profit or loss in current session.

cash
required
Array of objects
List of cash holdings, for each relevant currency, and how they contribute to margin.

Array 
currency
required
string
Currency name.

balance
required
number
Current balance in this currency.

collateral_factor
required
number
The collateral quality of the asset i.e. the fraction of the asset that can be used as a collateral.

collateral_index_price	
number
Index price used to calculate collateral effect of this position. Can be null for assets that are not converted using an index, e.g. for stable coins.

transactable
required
boolean
If this flag is true, this currency can be deposited and withdrawn.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"cash": [
{
"currency": "USDT",
"balance": 1000000004483.9625,
"collateral_factor": 1,
"collateral_index_price": null,
"transactable": true
}
],
"unrealised_pnl": 491.00977310002116,
"session_realised_pnl": 0,
"cash_collateral": 1000000004483.9625,
"margin": 1000000004994.1586,
"required_margin": 13123.880458333333,
"remaining_margin": 999999991870.2781
}
}
Margin breakdown

get
/private/required_margin_breakdown


Exchange: https://thalex.com/api/v2/private/required_margin_breakdown

Testnet: https://testnet.thalex.com/api/v2/private/required_margin_breakdown

Get margin breakdown

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (PortfolioMarginBreakdown)
Required margin breakdown for accounts that use portfolio margin.

portfolio	
object
required_margin	
number
Total required margin for account.

underlyings	
Array of objects
Array 
underlying	
string
Underlying index name.

required_margin	
number
Total margin required for positions with this underlying.

scenario_margin	
number
Deprecated. Same value as loss_margin.

loss_margin	
number
Margin based on scenario loss coverage.

d1_roll_cash_position	
number
Delta one roll position x index price in this underlying.

options_roll_cash_position	
number
Options roll position x index price in this underlying.

roll_cash_position	
number
Roll position x index price in this underlying.

d1_roll_contingency_margin	
number
Margin based on delta one roll position.

options_roll_contingency_margin	
number
Margin based on options roll position.

roll_contingency_margin	
number
Margin based on roll position.

options_short_cash_position	
number
Total short options position x index price in this underlying.

options_contingency_margin	
number
Margin based on options short position.

scenario_used	
integer
Index of the scenario in the scenarios array that was used to calculate total margin requirements for this underlying.

scenarios	
Array of objects
Scenarios that were simulated.

Array 
underlying_change_pct	
number
Simulated underlying change, %

vol_change_pct_point	
number
Simulated volatility change, %

pnl	
number
P&L resulting from this scenario.

coverage_factor	
number
Effect factor of P&L on the loss margin.

required_margin	
number
Total required margin in this scenario.

loss_margin	
number
Margin based on scenario loss coverage.

roll_cash_position	
number
Roll position x index price in this underlying.

roll_contingency_margin	
number
Margin based on roll position.

d1_roll_cash_position	
number
Delta one roll position x index price in this underlying.

d1_roll_contingency_margin	
number
Margin based on delta one roll position.

options_roll_cash_position	
number
Options roll position x index price in this underlying.

options_roll_contingency_margin	
number
Margin based on options roll position.

options_short_cash_position	
number
Total short options position x index price in this underlying.

options_contingency_margin	
number
Margin based on options short position.

positions	
Array of objects
Array 
instrument_name	
string
Instrument feedcode.

position	
number
Position/order size in contracts.

instrument_pnl	
number
P&L for a single contract of this instrument.

pnl	
number
Total P&L for the position/order in this instrument.

current_price	
number
The price at the moment of scenario calculation.

For positions this is set to the current mark price.

For open orders this is the order limit price.

scenario_price	
number
The price simulated for the scenario.

open_order	
boolean
Indicates whether this position is implied from an open order.

assumed_filled	
boolean
Indicates whether this order was assumed to be filled in this scenario.

Orders are assumed to be filled if they, for the particular scenario, generate an immediate loss if filled at the limit price.

Only orders that are assumed to be filled are taken into account for the loss, roll contingency and option contingency margin requirements.

This field is only present if open_order is true.

assets	
Array of objects
Results of scenario simulations on affected asset positions.

Array 
asset_name	
string
Asset name

position	
number
underlying_pnl	
number
P&L for a single unit of this asset.

pnl	
number
Total P&L for the position in this asset.

collateral_factor	
number
The collateral quality of the asset i.e. the fraction of the asset that can be used as a collateral.

index_price	
number
Index price at the moment of scenario calculation.

current_price	
number
The price at the moment of scenario calculation. This is the margin effect of this asset position, i.e. index price multiplied by collateral factor.

scenario_price	
number
The price calculated for the scenario.

highlight	
boolean
true if this scenario was used to calculate total margin requirements for this underlying.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"portfolio": {
"required_margin": -155.90231262790033,
"underlyings": [
{}
]
}
}
}
Margin breakdown with order

get
/private/required_margin_for_order


Exchange: https://thalex.com/api/v2/private/required_margin_for_order

Testnet: https://testnet.thalex.com/api/v2/private/required_margin_for_order

This method returns a lightweight breakdown of the account as it is, and also as if a hypothetical order of a given price and amount would be inserted on either side of the book.

query Parameters
instrument_name	
string
The name of the instrument of this hypothetical order with which the margin is to be broken down with. This field must not be present when requesting margin breakdown for a combination order. Use legs field instead.

legs	
Array of objects
List of legs for a combination order.

There must be at least two and at most four legs specified. All leg instruments must be distinct.

Other constraints apply, please check trading information page on combination orders.

This field must not be present when requesting margin breakdown for single-leg orders. Use instrument_name field instead.

price
required
number
The price of the hypothetical order.

amount
required
number
The amount that would be traded.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (MarginBreakdownWithOrder)
Lightweight margin breakdown without and with an order inserted as buy or sell.

current	
object
required_margin	
number
Total required margin for account.

underlying	
object
underlying	
string
Underlying index name.

required_margin	
number
Total margin required for positions with this underlying.

loss_margin	
number
Margin based on scenario loss coverage.

roll_contingency_margin	
number
Margin based on roll position.

d1_roll_contingency_margin	
number
Margin based on delta one roll position.

options_roll_contingency_margin	
number
Margin based on options roll position.

options_contingency_margin	
number
Margin based on options short position.

with_buy	
object
required_margin	
number
Total required margin for account with the order inserted as buy.

underlying	
object
underlying	
string
Underlying index name.

required_margin	
number
Total margin required for positions with this underlying.

loss_margin	
number
Margin based on scenario loss coverage.

roll_contingency_margin	
number
Margin based on roll position.

d1_roll_contingency_margin	
number
Margin based on delta one roll position.

options_roll_contingency_margin	
number
Margin based on options roll position.

options_contingency_margin	
number
Margin based on options short position.

with_sell	
object
required_margin	
number
Total required margin for account with the order inserted as sell.

underlying	
object
underlying	
string
Underlying index name.

required_margin	
number
Total margin required for positions with this underlying.

loss_margin	
number
Margin based on scenario loss coverage.

roll_contingency_margin	
number
Margin based on roll position.

d1_roll_contingency_margin	
number
Margin based on delta one roll position.

options_roll_contingency_margin	
number
Margin based on options roll position.

options_contingency_margin	
number
Margin based on options short position.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"current": {
"required_margin": -155.90231262790033,
"underlying": {
"required_margin": -155.90231262790033,
"underlying": "BTCUSD",
"loss_margin": -155.90231262790033,
"roll_contingency_margin": 151.54255212726002,
"d1_roll_contingency_margin": 151.54255212726002,
"options_roll_contingency_margin": 151.54255212726002,
"options_contingency_margin": 57.27288000000001
}
},
"with_buy": {
"required_margin": -155.90231262790033,
"underlying": {
"required_margin": -155.90231262790033,
"underlying": "BTCUSD",
"loss_margin": -155.90231262790033,
"roll_contingency_margin": 151.54255212726002,
"d1_roll_contingency_margin": 151.54255212726002,
"options_roll_contingency_margin": 151.54255212726002,
"options_contingency_margin": 57.27288000000001
}
},
"with_sell": {
"required_margin": -155.90231262790033,
"underlying": {
"required_margin": -155.90231262790033,
"underlying": "BTCUSD",
"loss_margin": -155.90231262790033,
"roll_contingency_margin": 151.54255212726002,
"d1_roll_contingency_margin": 151.54255212726002,
"options_roll_contingency_margin": 151.54255212726002,
"options_contingency_margin": 57.27288000000001
}
}
}
}
Conditional orders
Conditional orders

get
/private/conditional_orders


Exchange: https://thalex.com/api/v2/private/conditional_orders

Testnet: https://testnet.thalex.com/api/v2/private/conditional_orders

Get conditional orders

Responses
200
Response Schema: application/json
One of SuccessError
result	
Array of objects (ConditionalOrder)
List of conditional orders, both active and formerly active. After activation, conditional orders may be listed for another few days.

Array 
order_id
required
string
Unique ID, use to identify in cancel

instrument_name
required
string
direction
required
string
Enum: "buy" "sell"
amount
required
number
Size of the order when activated

target
required
string
Enum: "last" "mark" "index"
The trigger type that stop_price and bracket_price will refer to.

stop_price
required
number
Trigger price at which the order will be activated

limit_price	
number
For stop limit order, the price at which the order will be placed

bracket_price	
number
For bracket order, the price at which profit will be taken (upper activation price)

trailing_stop_callback_rate	
number
For trailing stop loss, the callback rate as a ratio (e.g. 0.05 for 5%)

label	
string
Optional user label

status
required
string
Enum: "created" "active" "converted" "rejected" "cancel requested" "cancelled"
create_time
required
number
update_time
required
number
Time of last update (conversion or change of trailing stop price)

convert_time	
number
Time of trigger

converted_order_id	
string
System order ID of the created order.

reject_reason	
string
If conversion failed, the reason

reduce_only
required
boolean
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"result": [
{
"order_id": "00011E570000004B",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"amount": 1,
"stop_price": 50000,
"limit_price": 45000,
"status": "created",
"create_time": 1630062311.3324597,
"update_time": 1630062311.3324597,
"reduce_only": false
}
]
}
}
Create conditional order

post
/private/create_conditional_order


Exchange: https://thalex.com/api/v2/private/create_conditional_order

Testnet: https://testnet.thalex.com/api/v2/private/create_conditional_order

A buy order will activate when a trade/mark/index happens at a price at or higher than the stop price, or at or lower than the bracket price (if set). A sell order will activate when a trigger happens at a price at or lower than the stop price, or at or higher than the bracket price (if set).

When a callback rate is set, the stop price for a buy order will trail down at (trade price * (1 + callback rate)), and for a sell order the stop price will trail up at (trade price * (1 - callback rate)).

A stop limit order will activate to a good-till-cancelled limit order, all other types will activate to a market order.

The last trigger target tracks aggressive trades in the instrument. The mark target tracks the mark price of the instrument, as calculated every second by the Thalex pricing engine. The index trigger target is allowed only for futures (instrument type perpetual or future), and tracks the index price of the respective underlying, as calculated every second by the Thalex pricing engine.

Only the following combinations are possible:

stop order: set only stop price
stop limit order: set stop price and limit price
bracket order: set stop price and bracket price. For a buy order, the bracket price must be under the stop price, and for a sell order the other way around.
trailing stop loss order: set stop price and callback rate.
Request Body schema: application/json
direction
required
string
Enum: "buy" "sell"
instrument_name
required
string
amount
required
number
limit_price	
number
If set, creates a stop limit order

target	
string
Enum: "last" "mark" "index"
The trigger target that stop_price and bracket_price refer to.

stop_price
required
number
Trigger price

bracket_price	
number
If set, creates a bracket order

trailing_stop_callback_rate	
number
If set, creates a trailing stop order

label	
string
Label will be set on the activated order

reduce_only	
boolean
Activated order will be reduce-only

stp_level	
string
Enum: "customer" "account" "disabled"
The self trade prevention level override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is customer and not configurable.

stp_action	
string
Enum: "cancel_aggressive_partial_fill" "cancel_aggressive_no_fill"
The self trade prevention action override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is cancel_aggressive_partial_fill and not configurable.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (ConditionalOrder)
order_id
required
string
Unique ID, use to identify in cancel

instrument_name
required
string
direction
required
string
Enum: "buy" "sell"
amount
required
number
Size of the order when activated

target
required
string
Enum: "last" "mark" "index"
The trigger type that stop_price and bracket_price will refer to.

stop_price
required
number
Trigger price at which the order will be activated

limit_price	
number
For stop limit order, the price at which the order will be placed

bracket_price	
number
For bracket order, the price at which profit will be taken (upper activation price)

trailing_stop_callback_rate	
number
For trailing stop loss, the callback rate as a ratio (e.g. 0.05 for 5%)

label	
string
Optional user label

status
required
string
Enum: "created" "active" "converted" "rejected" "cancel requested" "cancelled"
create_time
required
number
update_time
required
number
Time of last update (conversion or change of trailing stop price)

convert_time	
number
Time of trigger

converted_order_id	
string
System order ID of the created order.

reject_reason	
string
If conversion failed, the reason

reduce_only
required
boolean
Request samples
Payload
Content type
application/json

Copy
{
"direction": "buy",
"instrument_name": "string",
"amount": 0,
"stop_price": 0
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "00011E570000004B",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"amount": 1,
"stop_price": 50000,
"limit_price": 45000,
"status": "created",
"create_time": 1630062311.3324597,
"update_time": 1630062311.3324597,
"reduce_only": false,
"target": "mark"
}
}
Cancel conditional order

post
/private/cancel_conditional_order


Exchange: https://thalex.com/api/v2/private/cancel_conditional_order

Testnet: https://testnet.thalex.com/api/v2/private/cancel_conditional_order

Cancel conditional order

Request Body schema: application/json
order_id
required
string
Responses
200
Response Schema: application/json
One of SuccessError
result	
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
{
"order_id": "00011E570000004B"
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": null
}
Bulk cancel conditional orders

post
/private/cancel_all_conditional_orders


Exchange: https://thalex.com/api/v2/private/cancel_all_conditional_orders

Testnet: https://testnet.thalex.com/api/v2/private/cancel_all_conditional_orders

Cancel all conditional orders of this subaccount

Request Body schema: application/json
object (EmptyObject)
Empty object.

Responses
200
Response Schema: application/json
One of SuccessError
result	
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
{ }
Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": null
}
Bot management
Get bots

get
/private/bots


Exchange: https://thalex.com/api/v2/private/bots

Testnet: https://testnet.thalex.com/api/v2/private/bots

Get bots

Responses
200
Response Schema: application/json
One of SuccessError
result	
Array of SGSL (object) or OCQ (object) or Levels (object) or Grid (object) or DHedge (object) or DFollow (object) (Bot)
List of bots, both active and formerly active. Bots may be listed for another few days after they're stopped.

Array 
One of SGSLOCQLevelsGridDHedgeDFollow
bot_id
required
string
Individually identifies this bot instance. You can use it to cancel this specific one.

status
required
string
Enum: "active" "stopped"
stop_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "end_time" "instrument_deactivated" "margin_breach" "admin_cancel" "conflict" "strategy" "self_trade_prevention"
The reason why the bot stopped executing.

strategy
required
string
equal to "sgsl"

instrument_name
required
string
Name of the instrument.

signal
required
string
Enum: "last" "index" "mark"
entry_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

target_position
required
number
The target position to maintain in the subaccount if signal price is above entry_price. See the bot strategies section for more explanation.

exit_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

exit_position
required
number
The target position to maintain in the subaccount if signal price is below exit_price. See the bot strategies section for more explanation.

max_slippage	
number
Maximum slippage per trade, expressed as % of the traded instruments mark price.

end_time
required
number
Timestamp when the bot stops executing, cancelling its orders and leaving all positions of the subaccount intact.

start_time
required
number
Timestamp indicating when the bot was created.

stop_time	
number
Timestamp indicating when the bot stopped working due to specified stop_reason.

label	
string
A label that the bot will add to all orders for easy identification.

realized_pnl
required
number
Realized P&L made by this bot since the start.

fee
required
number
Trade fees by this bot.

average_price	
number
Average entry price of the position (if any).

position_size	
number
Position size (if any).

mark_price_at_stop	
number
Mark price of the bot instrument at the moment the bot was stopped.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
{
"strategy": "sgsl",
"status": "active",
"bot_id": "0000000035832FDE",
"instrument_name": "BTC-PERPETUAL",
"signal": "index",
"entry_price": 100050,
"target_position": 0.2,
"exit_price": 100000,
"exit_position": 0,
"end_time": 1740064912,
"start_time": 1740064912,
"stop_time": 1740064912
},
{
"strategy": "ocq",
"status": "stopped",
"stop_reason": "client_cancel",
"bot_id": "0000000035832FDF",
"instrument_name": "BTC-PERPETUAL",
"signal": "index",
"bid_offset": -50,
"ask_offset": 120,
"quote_size": 0.1,
"min_position": -0.3,
"max_position": 0.25,
"end_time": 1740064912,
"start_time": 1740064912,
"stop_time": 1740064912
}
]
}
Create a bot

post
/private/create_bot


Exchange: https://thalex.com/api/v2/private/create_bot

Testnet: https://testnet.thalex.com/api/v2/private/create_bot

Instantiate a bot that keeps continually trading in your name according to a predefined strategy. See the bot strategies section for more info on bots. For risk fencing reasons and because of the complex ways manual trades can interact with bot strategies, you might want to consider running bots on a separate/dedicated sub account. Also be aware that you can set up bots with different strategies in a way that they would end up trading with each other.

Request Body schema: application/json
One of SGSLOCQLevelsGridDHedgeDFollow
strategy
required
string
Equal to "sgsl"

instrument_name
required
string
Name of the instrument to run SGSL on.

signal
required
string
Enum: "last" "index" "mark"
entry_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

target_position
required
number
The target position to maintain in the subaccount if signal price is above entry_price. See the bot strategies section for more explanation.

exit_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

exit_position
required
number
The target position to maintain in the subaccount if signal price is below exit_price. See the bot strategies section for more explanation.

max_slippage	
number
Maximum slippage per trade, expressed as % of the traded instruments mark price.

end_time
required
number
Timestamp when the bot should stop executing. When end_time is reached, the bot will leave all positions intact, it will not open/close any of them.

label	
string
A label that the bot will add to all orders for easy identification.

start_time
required
number
Timestamp indicating when the bot was created.

stop_time	
number
Timestamp indicating when the bot stopped working due to specified stop_reason.

Responses
200
Response Schema: application/json
One of SuccessError
result	
SGSL (object) or OCQ (object) or Levels (object) or Grid (object) or DHedge (object) or DFollow (object) (Bot)
One of SGSLOCQLevelsGridDHedgeDFollow
bot_id
required
string
Individually identifies this bot instance. You can use it to cancel this specific one.

status
required
string
Enum: "active" "stopped"
stop_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "end_time" "instrument_deactivated" "margin_breach" "admin_cancel" "conflict" "strategy" "self_trade_prevention"
The reason why the bot stopped executing.

strategy
required
string
equal to "sgsl"

instrument_name
required
string
Name of the instrument.

signal
required
string
Enum: "last" "index" "mark"
entry_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

target_position
required
number
The target position to maintain in the subaccount if signal price is above entry_price. See the bot strategies section for more explanation.

exit_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

exit_position
required
number
The target position to maintain in the subaccount if signal price is below exit_price. See the bot strategies section for more explanation.

max_slippage	
number
Maximum slippage per trade, expressed as % of the traded instruments mark price.

end_time
required
number
Timestamp when the bot stops executing, cancelling its orders and leaving all positions of the subaccount intact.

start_time
required
number
Timestamp indicating when the bot was created.

stop_time	
number
Timestamp indicating when the bot stopped working due to specified stop_reason.

label	
string
A label that the bot will add to all orders for easy identification.

realized_pnl
required
number
Realized P&L made by this bot since the start.

fee
required
number
Trade fees by this bot.

average_price	
number
Average entry price of the position (if any).

position_size	
number
Position size (if any).

mark_price_at_stop	
number
Mark price of the bot instrument at the moment the bot was stopped.

Request samples
Payload
Content type
application/json
Example

SGSL
SGSL

Copy
{
"strategy": "sgsl",
"instrument_name": "BTC-PERPETUAL",
"signal": "index",
"entry_price": 100050,
"target_position": 0.2,
"exit_price": 100000,
"exit_position": 0,
"end_time": 1740064912
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"strategy": "sgsl",
"status": "active",
"bot_id": "0000000035832FDE",
"instrument_name": "BTC-PERPETUAL",
"signal": "index",
"entry_price": 100050,
"target_position": 0.2,
"exit_price": 100000,
"exit_position": 0,
"end_time": 1740064912,
"start_time": 1740064912,
"stop_time": 1740064912
}
}
Cancel a bot

post
/private/cancel_bot


Exchange: https://thalex.com/api/v2/private/cancel_bot

Testnet: https://testnet.thalex.com/api/v2/private/cancel_bot

Cancel a specific bot instance.

Request Body schema: application/json
bot_id
required
string
The bot_id returned when creating the bot, or calling private/bots.

Responses
200
Response Schema: application/json
One of SuccessError
result	
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
{
"bot_id": "string"
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": null
}
Cancel all bots

post
/private/cancel_all_bots


Exchange: https://thalex.com/api/v2/private/cancel_all_bots

Testnet: https://testnet.thalex.com/api/v2/private/cancel_all_bots

Cancel all bots of this subaccount

Request Body schema: application/json
null (Null)
Represents a null value.

Responses
200
Response Schema: application/json
One of SuccessError
result	
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
null
Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": null
}
Notifications
Notifications inbox

get
/private/notifications_inbox


Exchange: https://thalex.com/api/v2/private/notifications_inbox

Testnet: https://testnet.thalex.com/api/v2/private/notifications_inbox

This method returns a list of latest notifications that were sent to the current user. The list only contains items for which the inbox preference is set` (either in user preferences, or by default).

query Parameters
limit	
integer
Default: 1000
Max results to return.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object (Notifications)
notifications	
Array of objects
List of notifications ordered from newest to oldest.

Array 
id
required
string
Unique notification ID.

time
required
number
Time of notification (Unix timestamp).

category
required
string
Notification category (see API description / Notifications).

title
required
string
Human-readable title for the notification.

message
required
string
Human-readable message for the notification.

display_type
required
string
Enum: "success" "failure" "info" "warning" "critical"
Specifies what style to use for notification display.

read
required
boolean
set to true if notification was marked as read.

account_name	
string
Optional account name, only present if the notification is related to an account.

account_number	
string
Optional account number only present if the notification is related to an account.

popup
required
boolean
User preference - show popup for this notification

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"notifications": [
{
"id": "00000000000000A3",
"time": 1630069885.130461,
"category": "risk",
"title": "Margin Requirements",
"message": "Portfolio of account foo-123 breached initial margin requirements.",
"display_type": "warning",
"read": false,
"account_name": "foo-123",
"account_number": "A123456789",
"popup": true
}
]
}
}
Marking notification as read

post
/private/mark_inbox_notification_as_read


Exchange: https://thalex.com/api/v2/private/mark_inbox_notification_as_read

Testnet: https://testnet.thalex.com/api/v2/private/mark_inbox_notification_as_read

Mark a notification as read

Request Body schema: application/json
notification_id
required
string
ID of the notification to mark.

read	
boolean
Default: true
Set to true to mark as read, false to mark as not read.

Responses
200
Response Schema: application/json
One of SuccessError
result	
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
{
"notification_id": "00000000000000A3"
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": null
}
Wallet
Verify if withdrawal is possible

get
/private/verify_withdrawal


Exchange: https://thalex.com/api/v2/private/verify_withdrawal

Testnet: https://testnet.thalex.com/api/v2/private/verify_withdrawal

This method is subject to withdrawal permissions.

query Parameters
asset_name
required
string
Asset name.

amount
required
number
Amount to withdraw.

target_address
required
string
Target address.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
available_margin
required
number
Projected available margin after the withdrawal.

required_margin
required
number
Projected required margin after the withdrawal.

fee	
number
Amount of fees withheld.

fee_asset	
string
Asset in which the withdrawal fees are withheld.

error	
object
In case such withdrawal is not possible, this object contains an error code and an error message describing why. Otherwise, error is returned as null.

code	
number
Error code.

message	
string
Error message.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"available_margin": 10045,
"required_margin": 5096,
"fee": 25,
"fee_asset": "USDT",
"error": null
}
}
Withdraw assets

post
/private/withdraw


Exchange: https://thalex.com/api/v2/private/withdraw

Testnet: https://testnet.thalex.com/api/v2/private/withdraw

This method is subject to withdrawal permissions.

Request Body schema: application/json
asset_name
required
string
Asset name.

amount
required
number
Amount to withdraw.

target_address
required
string
Target address.

label	
string
Optional label to attach to the withdrawal request.

Responses
200
Response Schema: application/json
One of SuccessError
result	
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
{
"asset_name": "USDT",
"amount": 100,
"target_address": "1234xy2kgdygjrsqtzq2n0yrf2493p83kkfjhx01234",
"label": "For my new yacht"
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": null
}
Withdrawals

get
/private/crypto_withdrawals


Exchange: https://thalex.com/api/v2/private/crypto_withdrawals

Testnet: https://testnet.thalex.com/api/v2/private/crypto_withdrawals

List of withdrawals from the selected account. Includes all withdrawals: pending, executed, rejected etc.

Responses
200
Response Schema: application/json
One of SuccessError
result	
Array of objects
Array 
currency
required
string
Withdrawn currency symbol.

amount
required
number
Amount of currency withdrawn.

target_address
required
string
Target address, specific to blockchain used.

blockchain	
string
Blockchain used or this transaction.

transaction_hash	
string
Transaction hash on the used blockchain.

create_time
required
number
Time when this withdrawal was requested (Unix timestamp).

label	
string
Optional label attached to the withdrawal request.

state
required
string
Enum: "pending" "awaiting_confirmation" "executing" "executed" "rejected"
Withdrawal transaction status.

remark	
string
Remark added by the exchange.

fee	
number
Amount of fees withheld.

fee_asset	
string
Asset in which the withdrawal fees are withheld.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
[
{
"currency": "ETH",
"amount": 0.1,
"target_address": "0x12345767c60fb7867B85aA35F72411234",
"blockchain": "ethereum",
"transaction_hash": "0x123415543674a854df02f4ef8f5dbc04ee01b744ac0bc4123456",
"create_time": 1632732292.7792032,
"label": "It's not much, but it's honest work",
"state": "executed",
"remark": "COMPLETED - CONFIRMED",
"fee": 25,
"fee_asset": "USDT"
}
]
]
}
Deposits

get
/private/crypto_deposits


Exchange: https://thalex.com/api/v2/private/crypto_deposits

Testnet: https://testnet.thalex.com/api/v2/private/crypto_deposits

Pending and confirmed deposits for the selected account.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
confirmed
required
Array of objects (Deposit)
List of confirmed deposits.

Array 
currency
required
string
Deposited currency symbol.

amount
required
number
Amount of currency deposited.

blockchain
required
string
Blockchain used or this transaction.

transaction_hash
required
string
Transaction hash on the used blockchain.

transaction_timestamp
required
number
Time when this transaction was created (Unix timestamp).

status
required
string
Enum: "unconfirmed" "confirmed"
Deposit transaction status.

confirmations	
number
Number of confirmations. Optional, omitted when none.

unconfirmed
required
Array of objects (Deposit)
List of unconfirmed deposits.

Array 
currency
required
string
Deposited currency symbol.

amount
required
number
Amount of currency deposited.

blockchain
required
string
Blockchain used or this transaction.

transaction_hash
required
string
Transaction hash on the used blockchain.

transaction_timestamp
required
number
Time when this transaction was created (Unix timestamp).

status
required
string
Enum: "unconfirmed" "confirmed"
Deposit transaction status.

confirmations	
number
Number of confirmations. Optional, omitted when none.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"confirmed": [
{
"currency": "ETH",
"blockchain": "ethereum",
"transaction_hash": "0x1235467675550cad841c8b410f78e1d1d7cc256b6803234234534534",
"transaction_timestamp": 1632217370,
"amount": 0.059,
"status": "confirmed",
"confirmations": 6
}
],
"unconfirmed": [ ]
}
}
Bitcoin deposit address

get
/private/btc_deposit_address


Exchange: https://thalex.com/api/v2/private/btc_deposit_address

Testnet: https://testnet.thalex.com/api/v2/private/btc_deposit_address

Get Bitcoin deposit address

Responses
200
Response Schema: application/json
One of SuccessError
result	
string
Deposit address for the selected account for Bitcoin.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": "12345yr6zpguy7nrc8md63ykn5h9xr4vryl99r3wpz"
}
Ethereum deposit address

get
/private/eth_deposit_address


Exchange: https://thalex.com/api/v2/private/eth_deposit_address

Testnet: https://testnet.thalex.com/api/v2/private/eth_deposit_address

Get Ethereum deposit address

Responses
200
Response Schema: application/json
One of SuccessError
result	
string
Deposit address for the selected account for coins on Ethereum network.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": "0x1235467675550cad841c8b410f78e1d1d7cc256b6803234234534534"
}
Verify internal transfer

post
/private/verify_internal_transfer


Exchange: https://thalex.com/api/v2/private/verify_internal_transfer

Testnet: https://testnet.thalex.com/api/v2/private/verify_internal_transfer

Verify if internal transfer of assets and/or positions from source (currently selected) to destination account is possible. Does not perform the transfer itself.

Transfers are subject to margin checks.

A transfer cannot result in an account breaching margin requirements. This applies to both source and destination accounts.

If either of the accounts is already in margin breach state, the transfer is only allowed if it results in an increase of available margin on that account. The other account must not breach margin requirement as a result of the transfer. This allows transferring assets and/or positions from an account with enough extra margin to an account that was margin called.

Each transfer can contain multiple asset and position transfers. It is checked for margin requirements as a single transaction. It is possible to specify negative amounts for transferred assets and positions, which results in a reverse direction of transfer (i.e. from destination account to the source one). This allows performing asset/position exchange operations, and is helpful when a leg of such operation alone would result in a margin requirements breach.

Request Body schema: application/json
destination_account_number
required
string
Destination account number.

assets	
Array of objects
Array 
asset_name
required
string
Asset name

amount
required
number
Amount to transfer. Use a negative value to transfer in reverse direction.

positions	
Array of objects
Array 
instrument_name
required
string
Instrument feedcode.

amount
required
number
Amount to transfer. Use a negative value to transfer in reverse direction.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
source_available_margin
required
number
Available margin in the source account after the transfer is performed.

source_required_margin
required
number
Required margin in the source account after the transfer is performed.

destination_available_margin
required
number
Available margin in the destination account after the transfer is performed.

destination_required_margin
required
number
Required margin in the destination account after the transfer is performed.

error	
object
Only present when the transfer is not possible, in which case it describes the error such transfer would result in.

Note: this is different from the top level result/error in the response.

code
required
number
Error code

message
required
string
Error message

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"destination_account_number": "A123456789",
"assets": [
{
"asset_name": "BTC",
"amount": "1"
}
]
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"destination_available_margin": 10040724.221942985,
"destination_required_margin": 13021.147166650373,
"source_available_margin": 11987398962.727953,
"source_required_margin": 179870275.06509292,
"error": {
"code": 27,
"message": "asset 'BTC': insufficient funds for operation"
}
}
}
Internal transfer

post
/private/internal_transfer


Exchange: https://thalex.com/api/v2/private/internal_transfer

Testnet: https://testnet.thalex.com/api/v2/private/internal_transfer

Transfer assets and/or positions from source (currently selected) to destination account.

Transfers are subject to margin checks. Please see private/verify_internal_transfer method description for more information.

Request Body schema: application/json
destination_account_number
required
string
Destination account number.

assets	
Array of objects
Array 
asset_name
required
string
Asset name

amount
required
number
Amount to transfer. Use a negative value to transfer in reverse direction.

positions	
Array of objects
Array 
instrument_name
required
string
Instrument feedcode.

amount
required
number
Amount to transfer. Use a negative value to transfer in reverse direction.

label	
string
Optional label attached to the transfer.

Responses
200
Response Schema: application/json
One of SuccessError
result	
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"destination_account_number": "A123456789",
"assets": [
{
"asset_name": "BTC",
"amount": "1"
}
]
}
Response samples
200
Content type
application/json
Example

Success
Success

Copy
{
"result": null
}
System info
System info

get
/public/system_info


Exchange: https://thalex.com/api/v2/public/system_info

Testnet: https://testnet.thalex.com/api/v2/public/system_info

Get system info

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
environment
required
string
Enum: "testnet" "production"
api_version	
string
Current API version.

banners
required
Array of objects (Banner)
List of banners currently shown.

Banners are 'sticky' notifications visible to all users of the exchange. They are used e.g. for maintenance announcements etc.

Array 
id	
number
The id of this banner.

time
required
number
Time when this banner was posted (Unix timestamp).

severity
required
string
Enum: "info" "warning" "critical"
Severity of the banner message. Used to choose appropriate styling for banner display.

title	
string
Optional title of the banner.

message
required
string
Message text to be displayed in the banner.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"environment": "production",
"api_version": "2.0.0",
"banners": [
{
"id": 1,
"time": 1630059868.4145653,
"severity": "info",
"title": "Important information",
"message": "Starting next week we are lowering our fees by 10%."
}
]
}
}
Historical data
Mark price historical data.

get
/public/mark_price_historical_data


Exchange: https://thalex.com/api/v2/public/mark_price_historical_data

Testnet: https://testnet.thalex.com/api/v2/public/mark_price_historical_data

Returns mark price historical data in the specified interval and resolution in OHLC format.

query Parameters
instrument_name
required
string
Feedcode of the instrument (e.g. BTC-PERPETUAL).

from
required
number
Start time (Unix timestamp).

to
required
number
End time (Unix timestamp) (exclusive).

resolution
required
string
Enum: "1m" "5m" "15m" "30m" "1h" "1d" "1w"
Each data point will be aggregated using OHLC according to the specified resolution.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
instrument_type
required
string
Enum: "perpetual" "future" "combination" "option"
Instrument type the historical data corresponds to.

mark
required
Array of Perpetuals (items) or Array of Futures and combinations (items) or Array of Options (items)
Array of mark price data points. Each mark price data point is an array of mark price data in OHLC format followed by an optional array of top of book data. Top of book data is returned only for 1m resolution and set to null otherwise.

Note that the inner array format depends on the instrument_type flag.

Note also that the top bid and top ask data can be set to null for the 1m resolution if there was no quote at the start of the correspondent minute interval.

One of PerpetualsFutures and combinationsOptions
Array 
[0]	
number
Time (Unix timestamp) of the start of the data point.

[1]	
number
Open (first) value of the data point

[2]	
number
High (max) value of the data point.

[3]	
number
Low (min) value of the data point.

[4]	
number
Close (last) value of the data point.

[5]	
number
Funding payment during the interval represented by the data point.

[6]	
Array of items = 4 items
Top of book data, null for the resolutions other than 1 minute.

[0]	
number
Top bid price, or null if bid order book is empty.

[1]	
number
Top bid size, or null if bid order book is empty.

[2]	
number
Top ask price, or null if ask order book is empty.

[3]	
number
Top ask size, or null if ask order book is empty.

no_data	
boolean
Is set if there is no data for this instrument in or before the requested interval.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"instrument_type": "perpetual",
"mark": [
[
1736363460,
94700,
94701,
94445,
94409,
0.0002
],
[
1736363520,
94409,
94600,
94408,
94500,
-0.00011
]
]
}
}
Index price historical data.

get
/public/index_price_historical_data


Exchange: https://thalex.com/api/v2/public/index_price_historical_data

Testnet: https://testnet.thalex.com/api/v2/public/index_price_historical_data

Returns index price historical data in the specified interval and resolution in OHLC format.

query Parameters
index_name
required
string
Index name (e.g. BTCUSD, ETHUSD).

from
required
number
Start time (Unix timestamp).

to
required
number
End time (Unix timestamp) (exclusive).

resolution
required
string
Enum: "1m" "5m" "15m" "30m" "1h" "1d" "1w"
Each data point will be aggregated using OHLC according to the specified resolution.

Responses
200
Response Schema: application/json
One of SuccessError
result	
object
index
required
Array of items[ items = 6 items ]
Array of arrays of index price data points in OHLC format.

Array 
[0]	
number
Time (Unix timestamp) of the start of the data point.

[1]	
number
Open (first) value of the data point

[2]	
number
High (max) value of the data point.

[3]	
number
Low (min) value of the data point.

[4]	
number
Close (last) value of the data point.

no_data	
boolean
Is set if there is no data for this instrument in or before the requested interval.

Response samples
200
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"index": [
[
1736363460,
94700,
94701,
94445,
94409
],
[
1736363520,
94409,
94600,
94408,
94500
]
]
}
}
Session management
Login

rpc
public/login
See 'Authentication'

Request Body schema: application/json
method
required
string
Value: "public/login"
id	
object
Your request id, optional.

params
required
object
token
required
string
As described in 'Authentication'

account	
string
Number of an account to select for use in this session. Optional, if not specified, default account for the API key is selected.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
account_number
required
string
Account number

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/login",
"params": {
"token": "<JWT token>"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"account_number": "A123456789"
}
}
Set cancel on disconnect

rpc
private/set_cancel_on_disconnect
Sets the session to "non-persistent" mode. All subsequently inserted orders will be non-persistent orders. Furthermore, the session should make sure to send a message at least every timeout_secs seconds or the connection will be considered dead. A WebSocket ping suffices.

Request Body schema: application/json
method
required
string
Value: "private/set_cancel_on_disconnect"
id	
object
Your request id, optional.

params
required
object
timeout_secs
required
integer
Heartbeat interval

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
message_rate
required
integer
Message rate

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/set_cancel_on_disconnect",
"params": {
"timeout_secs": 10
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"message_rate": 50
}
}
Market data
Active instruments

rpc
public/instruments
Retrieves the list of currently active instruments.

Request Body schema: application/json
method
required
string
Value: "public/instruments"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of objects (Instrument)
List of currently active instruments.

Array 
instrument_name	
string
product	
string
E.g. "FBTCUSD", "OBTCUSD".

tick_size	
number
Price alignment.

volume_tick_size	
number
Amount alignment.

min_order_amount	
number
Minimum order amount for this instrument. This value is always greater or equal to volume_tick_size.

If this value is greater than volume_tick_size, it is not possible to insert an order of a smaller amount, or amend an existing order to a smaller amount. However, orders in the books can have smaller remaining amounts as they get partially filled, down to the minimum of volume_tick_size.

underlying	
string
Related index, e.g. "BTCUSD".

type	
string
Enum: "perpetual" "future" "option" "combination"
option_type	
string
Enum: "call" "put"
expiry_date	
string
Expiration date in ISO format (YYYY-mm-dd).

expiration_timestamp	
integer
Expiration time as Unix timestamp (seconds).

strike_price	
number
Strike price of option.

base_currency	
string
Base currency for pricing (i.e. USD).

legs	
Array of objects
For combinations, array of objects with instrument_name and quantity.

Array 
instrument_name	
string
quantity	
integer
create_time	
number
Creation time (Unix timestamp).

settlement_price	
number
For expired instruments, the final settlement price.

settlement_index_price	
number
For expired instruments, the underlying delivery price.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/instruments",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": [
{
"instrument_name": "BTC-10SEP21-70000-C",
"product": "OBTCUSD",
"tick_size": 5,
"volume_tick_size": 0.1,
"min_order_amount": 0.1,
"underlying": "BTCUSD",
"type": "option",
"option_type": "call",
"expiry_date": "2021-09-10",
"expiration_timestamp": 1631260800,
"strike_price": 70000,
"base_currency": "USD",
"create_time": 1631250800.103645
}
]
}
All instruments

rpc
public/all_instruments
Retrieves the list of all instruments that were active in the specified time interval.

Note that the time interval cannot be larger than 3 days.

You can also use public/instrument call to retrieve information about a specific instrument.

Request Body schema: application/json
method
required
string
Value: "public/all_instruments"
id	
object
Your request id, optional.

params
required
object
time_low	
number
Start time (Unix timestamp) defaults to time_high - 3 days.

time_high	
number
End time (Unix timestamp) defaults to now.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of objects (Instrument)
List of all instruments that have not or only recently expired.

Array 
instrument_name	
string
product	
string
E.g. "FBTCUSD", "OBTCUSD".

tick_size	
number
Price alignment.

volume_tick_size	
number
Amount alignment.

min_order_amount	
number
Minimum order amount for this instrument. This value is always greater or equal to volume_tick_size.

If this value is greater than volume_tick_size, it is not possible to insert an order of a smaller amount, or amend an existing order to a smaller amount. However, orders in the books can have smaller remaining amounts as they get partially filled, down to the minimum of volume_tick_size.

underlying	
string
Related index, e.g. "BTCUSD".

type	
string
Enum: "perpetual" "future" "option" "combination"
option_type	
string
Enum: "call" "put"
expiry_date	
string
Expiration date in ISO format (YYYY-mm-dd).

expiration_timestamp	
integer
Expiration time as Unix timestamp (seconds).

strike_price	
number
Strike price of option.

base_currency	
string
Base currency for pricing (i.e. USD).

legs	
Array of objects
For combinations, array of objects with instrument_name and quantity.

Array 
instrument_name	
string
quantity	
integer
create_time	
number
Creation time (Unix timestamp).

settlement_price	
number
For expired instruments, the final settlement price.

settlement_index_price	
number
For expired instruments, the underlying delivery price.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/all_instruments",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": [
{
"instrument_name": "BTC-10SEP21-70000-C",
"product": "OBTCUSD",
"tick_size": 5,
"volume_tick_size": 0.1,
"min_order_amount": 0.1,
"underlying": "BTCUSD",
"type": "option",
"option_type": "call",
"expiry_date": "2021-09-10",
"expiration_timestamp": 1631260800,
"strike_price": 70000,
"base_currency": "USD",
"create_time": 1631250800.103645
}
]
}
Single instrument

rpc
public/instrument
Retrieves a singe instrument.

Unlike public/all_instruments, this API endpoint allows retrieving information about instruments that have expired long time ago.

Request Body schema: application/json
method
required
string
Value: "public/instrument"
id	
object
Your request id, optional.

params
required
object
instrument_name
required
string
Name of the instrument to query.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (Instrument)
instrument_name	
string
product	
string
E.g. "FBTCUSD", "OBTCUSD".

tick_size	
number
Price alignment.

volume_tick_size	
number
Amount alignment.

min_order_amount	
number
Minimum order amount for this instrument. This value is always greater or equal to volume_tick_size.

If this value is greater than volume_tick_size, it is not possible to insert an order of a smaller amount, or amend an existing order to a smaller amount. However, orders in the books can have smaller remaining amounts as they get partially filled, down to the minimum of volume_tick_size.

underlying	
string
Related index, e.g. "BTCUSD".

type	
string
Enum: "perpetual" "future" "option" "combination"
option_type	
string
Enum: "call" "put"
expiry_date	
string
Expiration date in ISO format (YYYY-mm-dd).

expiration_timestamp	
integer
Expiration time as Unix timestamp (seconds).

strike_price	
number
Strike price of option.

base_currency	
string
Base currency for pricing (i.e. USD).

legs	
Array of objects
For combinations, array of objects with instrument_name and quantity.

Array 
instrument_name	
string
quantity	
integer
create_time	
number
Creation time (Unix timestamp).

settlement_price	
number
For expired instruments, the final settlement price.

settlement_index_price	
number
For expired instruments, the underlying delivery price.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/instrument",
"params": {
"instrument_name": "string"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"instrument_name": "BTC-10SEP21-70000-C",
"product": "OBTCUSD",
"tick_size": 5,
"volume_tick_size": 0.1,
"min_order_amount": 0.1,
"underlying": "BTCUSD",
"type": "option",
"option_type": "call",
"expiry_date": "2021-09-10",
"expiration_timestamp": 1631260800,
"strike_price": 70000,
"base_currency": "USD",
"create_time": 1631250800.103645
}
}
Single ticker value

rpc
public/ticker
Retrieves a single ticker for a single instrument. Please do not use this to repeatedly poll for data -- a websocket subscription is much more useful.

Request Body schema: application/json
method
required
string
Value: "public/ticker"
id	
object
Your request id, optional.

params
required
object
instrument_name
required
string
Name of the instrument to query.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (Ticker)
best_bid_price	
number
Price of the best (highest) bid in the orderbook, or null if the orderbook is empty.

best_bid_amount	
number
Size of best bid, or null if the orderbook is empty.

best_ask_price	
number
Price of best (lowest) ask in the orderbook, or null if the orderbook is empty.

best_ask_amount	
number
Size of best ask, or null if the orderbook is empty.

last_price	
number
Price of last trade, or null if no trades have been registered yet.

Not included for combinations.

mark_price	
number
Current mark price.

mark_timestamp	
number
The unix timestamp when the price was marked.

iv	
number
Implied volatility calculated at time of marking.

Only included for options. Not included for combinations.

delta	
number
Delta calculated at time of marking.

Not included for combinations.

index	
number
Index price at time of marking.

forward	
number
Forward price at time of marking.

Only included for options.

volume_24h	
number
Total volume traded over the last 24 hours.

Not included for combinations.

value_24h	
number
Total value traded over the last 24 hours.

Not included for combinations.

low_price_24h	
number
Lowest price in the last 24 hours.

Not included for combinations.

high_price_24h	
number
Highest price in the last 24 hours.

Not included for combinations.

change_24h	
number
Difference in price between the first and the last trades in the last 24 hours, null if there were no trades.

Not included for combinations.

collar_low	
number
Current price collar low (checks new asks)

collar_high	
number
Current price collar high (checks new bids)

open_interest	
number
Total number of outstanding unsettled contracts.

Not included for combinations.

funding_rate	
number
Current rate at which long position pays and short position earns, in funding interval.

Only included for perpetuals.

funding_mark	
number
Funding value of a single contract long position since last settlement.

Only included for perpetuals.

realised_funding_24h	
number
Total funding accumulated for a single contract long position over the last 24 hours.

Only included for perpetuals.

average_funding_rate_24h	
number
Average funding rate for the last 24 hours.

Only included for perpetuals.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/ticker",
"params": {
"instrument_name": "string"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"mark_price": 47238.64143906124,
"mark_timestamp": 946684800,
"best_bid_price": 47240,
"best_bid_amount": 0.4,
"best_ask_price": 47260,
"best_ask_amount": 1,
"delta": 1,
"volume_24h": 0,
"value_24h": 0,
"open_interest": 123.456
}
}
Single index value

rpc
public/index
Retrieves the index price for a single underlying. If needed repeatedly, please use the price_index.<underlying> websocket subscription.

Request Body schema: application/json
method
required
string
Value: "public/index"
id	
object
Your request id, optional.

params
required
object
underlying
required
string
The underlying (e.g. BTCUSD).

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (Index)
index_name
required
string
price
required
number
timestamp
required
number
The unix timestamp when the index price was recorded in the database.

expiration_print_average	
number
The average price so far over the current expiration, if any.

expiration_progress	
number
A number between 0.0 and 1.0 indicating the progress of the current expiration.

expected_expiration_price	
number
If expiration is in progress, and the index price will not change any more, this is the expiration price. Equals expiration_progress * expiration_print_average + (1 - expiration_progress) * price.

previous_settlement_price	
number
The last known settlement price (expiration price, underlying delivery price).

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/index",
"params": {
"underlying": "string"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"index_name": "BTCUSD",
"price": 47389.10833333334,
"timestamp": 946684800
}
}
Single order book

rpc
public/book
Retrieves aggregated price depth for a single instrument, with a maximum of 5 levels. Please do not use this to poll for data -- a websocket subscription is more flexible and more useful.

Request Body schema: application/json
method
required
string
Value: "public/book"
id	
object
Your request id, optional.

params
required
object
instrument_name
required
string
Name of the instrument to query.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
bids
required
Array of numbers[ items ]
Bids (list of price, amount, outright-amount)

asks
required
Array of numbers[ items ]
Asks (list of price, amount, outright-amount)

last	
number
Last traded price

time
required
number
Time of the last recorded update to this order book (Unix timestamp).

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/book",
"params": {
"instrument_name": "string"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"result": {
"bids": [
[]
],
"asks": [ ],
"last": 26500,
"time": 1683901717.209106
}
}
}
Trading
Insert order

rpc
private/insert
Insert an order

Request Body schema: application/json
method
required
string
Value: "private/insert"
id	
object
Your request id, optional.

params
required
object
direction
required
string
Enum: "buy" "sell"
client_order_id	
integer
Session-local identifier for this order. Only valid for websocket sessions. If set, must be an integer between 0 and 2^64-1, inclusive. When using numbers larger than 2^32, please beware of implicit floating point conversions in some JSON libraries.

instrument_name	
string
Name of the instrument to trade.

This field must not be present when inserting a combination order. Use legs field instead.

legs	
Array of objects
List of legs for a combination order.

There must be at least two and at most four legs specified. All leg instruments must be distinct.

Other constraints apply, please check trading information page on combination orders.

This field must not be present when inserting single-leg orders. Use instrument_name field instead.

Array 
instrument_name
required
string
Name of the instrument to trade on this leg.

quantity
required
number
Quantity of this leg in a unit of the combination. Must be integer. Must not be zero. Use a negative number for short legs.

Result of multiplication of quantity and order amount must be aligned to tick size for every leg.

price	
number
Limit price; required for limit orders.

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Amount of currency to trade (e.g. BTC for futures).

For combination orders this specifies the amount of units of the combination to trade.

label	
string
order_type	
string
Default: "limit"
Enum: "limit" "market"
time_in_force	
string
Enum: "good_till_cancelled" "immediate_or_cancel"
Note that for limit orders, the default time_in_force is good_till_cancelled, while for market orders, the default is immediate_or_cancel. It is illegal to send a GTC market order, or an IOC post order.

For combination orders time_in_force must always be set to immediate_or_cancel.

post_only	
boolean
If the order price is in cross with the current best price on the opposite side in the order book, then the price is adjusted to one tick away from that price, ensuring that the order will never trade on insert. If the adjusted price of a buy order falls at or below zero where not allowed, then the order is cancelled with delete reason 'immediate_cancel'.

This flag is not supported for combination orders.

reject_post_only	
boolean
This flag is only effective in combination with post_only. If set, then instead of adjusting the order price, the order will be cancelled with delete reason 'immediate_cancel'. The combination of post_only and reject_post_only is effectively a book-or-cancel order.

This flag is not supported for combination orders.

reduce_only	
boolean
An order marked reduce_only will have its amount reduced to the open position. If there is no open position, or if the order direction would cause an increase of the open position, the order is rejected. If the order is placed in the book, it will be subsequently monitored, and reduced to the open position if the position changes through other means (best effort). Multiple reduce-only orders will all be reduced individually.

This flag is not supported for combination orders.

collar	
string
Enum: "ignore" "reject" "clamp"
If the instrument has a safety price collar set, and the limit price of the order (infinite for market orders) is in cross with (more aggressive than) this collar, how to handle. If set to ignore, the order will proceed as requested. If reject, the order fails early. If clamp, the price is adjusted to the collar.

The default is clamp for market orders and reject for everything else.

Collar ignore is forbidden for market orders.

Price collars are applied to combination orders. Price collar for a combination is a linear combination of the leg collars with their corresponding quantities as coefficients.

stp_level	
string
Enum: "customer" "account" "disabled"
The self trade prevention level override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is customer and not configurable.

stp_action	
string
Enum: "cancel_aggressive_partial_fill" "cancel_aggressive_no_fill"
The self trade prevention action override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is cancel_aggressive_partial_fill and not configurable.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (OrderStatus)
Order status.

order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/insert",
"params": {
"direction": "buy",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "buy",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
}
Insert buy order

rpc
private/buy
Insert buy order

Request Body schema: application/json
method
required
string
Value: "private/buy"
id	
object
Your request id, optional.

params
required
object (InsertRequest)
client_order_id	
integer
Session-local identifier for this order. Only valid for websocket sessions. If set, must be an integer between 0 and 2^64-1, inclusive. When using numbers larger than 2^32, please beware of implicit floating point conversions in some JSON libraries.

instrument_name	
string
Name of the instrument to trade.

This field must not be present when inserting a combination order. Use legs field instead.

legs	
Array of objects
List of legs for a combination order.

There must be at least two and at most four legs specified. All leg instruments must be distinct.

Other constraints apply, please check trading information page on combination orders.

This field must not be present when inserting single-leg orders. Use instrument_name field instead.

Array 
instrument_name
required
string
Name of the instrument to trade on this leg.

quantity
required
number
Quantity of this leg in a unit of the combination. Must be integer. Must not be zero. Use a negative number for short legs.

Result of multiplication of quantity and order amount must be aligned to tick size for every leg.

price	
number
Limit price; required for limit orders.

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Amount of currency to trade (e.g. BTC for futures).

For combination orders this specifies the amount of units of the combination to trade.

label	
string
order_type	
string
Default: "limit"
Enum: "limit" "market"
time_in_force	
string
Enum: "good_till_cancelled" "immediate_or_cancel"
Note that for limit orders, the default time_in_force is good_till_cancelled, while for market orders, the default is immediate_or_cancel. It is illegal to send a GTC market order, or an IOC post order.

For combination orders time_in_force must always be set to immediate_or_cancel.

post_only	
boolean
If the order price is in cross with the current best price on the opposite side in the order book, then the price is adjusted to one tick away from that price, ensuring that the order will never trade on insert. If the adjusted price of a buy order falls at or below zero where not allowed, then the order is cancelled with delete reason 'immediate_cancel'.

This flag is not supported for combination orders.

reject_post_only	
boolean
This flag is only effective in combination with post_only. If set, then instead of adjusting the order price, the order will be cancelled with delete reason 'immediate_cancel'. The combination of post_only and reject_post_only is effectively a book-or-cancel order.

This flag is not supported for combination orders.

reduce_only	
boolean
An order marked reduce_only will have its amount reduced to the open position. If there is no open position, or if the order direction would cause an increase of the open position, the order is rejected. If the order is placed in the book, it will be subsequently monitored, and reduced to the open position if the position changes through other means (best effort). Multiple reduce-only orders will all be reduced individually.

This flag is not supported for combination orders.

collar	
string
Enum: "ignore" "reject" "clamp"
If the instrument has a safety price collar set, and the limit price of the order (infinite for market orders) is in cross with (more aggressive than) this collar, how to handle. If set to ignore, the order will proceed as requested. If reject, the order fails early. If clamp, the price is adjusted to the collar.

The default is clamp for market orders and reject for everything else.

Collar ignore is forbidden for market orders.

Price collars are applied to combination orders. Price collar for a combination is a linear combination of the leg collars with their corresponding quantities as coefficients.

stp_level	
string
Enum: "customer" "account" "disabled"
The self trade prevention level override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is customer and not configurable.

stp_action	
string
Enum: "cancel_aggressive_partial_fill" "cancel_aggressive_no_fill"
The self trade prevention action override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is cancel_aggressive_partial_fill and not configurable.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (OrderStatus)
Order status.

order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/buy",
"params": {
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "buy",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
}
Insert sell order

rpc
private/sell
Insert sell order

Request Body schema: application/json
method
required
string
Value: "private/sell"
id	
object
Your request id, optional.

params
required
object (InsertRequest)
client_order_id	
integer
Session-local identifier for this order. Only valid for websocket sessions. If set, must be an integer between 0 and 2^64-1, inclusive. When using numbers larger than 2^32, please beware of implicit floating point conversions in some JSON libraries.

instrument_name	
string
Name of the instrument to trade.

This field must not be present when inserting a combination order. Use legs field instead.

legs	
Array of objects
List of legs for a combination order.

There must be at least two and at most four legs specified. All leg instruments must be distinct.

Other constraints apply, please check trading information page on combination orders.

This field must not be present when inserting single-leg orders. Use instrument_name field instead.

Array 
instrument_name
required
string
Name of the instrument to trade on this leg.

quantity
required
number
Quantity of this leg in a unit of the combination. Must be integer. Must not be zero. Use a negative number for short legs.

Result of multiplication of quantity and order amount must be aligned to tick size for every leg.

price	
number
Limit price; required for limit orders.

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Amount of currency to trade (e.g. BTC for futures).

For combination orders this specifies the amount of units of the combination to trade.

label	
string
order_type	
string
Default: "limit"
Enum: "limit" "market"
time_in_force	
string
Enum: "good_till_cancelled" "immediate_or_cancel"
Note that for limit orders, the default time_in_force is good_till_cancelled, while for market orders, the default is immediate_or_cancel. It is illegal to send a GTC market order, or an IOC post order.

For combination orders time_in_force must always be set to immediate_or_cancel.

post_only	
boolean
If the order price is in cross with the current best price on the opposite side in the order book, then the price is adjusted to one tick away from that price, ensuring that the order will never trade on insert. If the adjusted price of a buy order falls at or below zero where not allowed, then the order is cancelled with delete reason 'immediate_cancel'.

This flag is not supported for combination orders.

reject_post_only	
boolean
This flag is only effective in combination with post_only. If set, then instead of adjusting the order price, the order will be cancelled with delete reason 'immediate_cancel'. The combination of post_only and reject_post_only is effectively a book-or-cancel order.

This flag is not supported for combination orders.

reduce_only	
boolean
An order marked reduce_only will have its amount reduced to the open position. If there is no open position, or if the order direction would cause an increase of the open position, the order is rejected. If the order is placed in the book, it will be subsequently monitored, and reduced to the open position if the position changes through other means (best effort). Multiple reduce-only orders will all be reduced individually.

This flag is not supported for combination orders.

collar	
string
Enum: "ignore" "reject" "clamp"
If the instrument has a safety price collar set, and the limit price of the order (infinite for market orders) is in cross with (more aggressive than) this collar, how to handle. If set to ignore, the order will proceed as requested. If reject, the order fails early. If clamp, the price is adjusted to the collar.

The default is clamp for market orders and reject for everything else.

Collar ignore is forbidden for market orders.

Price collars are applied to combination orders. Price collar for a combination is a linear combination of the leg collars with their corresponding quantities as coefficients.

stp_level	
string
Enum: "customer" "account" "disabled"
The self trade prevention level override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is customer and not configurable.

stp_action	
string
Enum: "cancel_aggressive_partial_fill" "cancel_aggressive_no_fill"
The self trade prevention action override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is cancel_aggressive_partial_fill and not configurable.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (OrderStatus)
Order status.

order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/sell",
"params": {
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "sell",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
}
Amend order

rpc
private/amend
Note that amount designates the new "original" amount, i.e. the amend is volume-safe. If the specified amount is lower than the already executed amount, the order is deleted.

If the price of the order is the same as the previous price, and the amount is less than the previous amount, book priority is preserved.

If the amount is amended to a value at or below the executed amount, the order is cancelled.

Request Body schema: application/json
method
required
string
Value: "private/amend"
id	
object
Your request id, optional.

params
required
object
client_order_id	
integer
Exactly one of client_order_id or order_id must be specified.

order_id	
string
Exactly one of client_order_id or order_id must be specified.

price
required
number
amount
required
number
collar	
string
Enum: "ignore" "reject" "clamp"
If the instrument has a safety price collar set, and the new limit price is in cross with (more aggressive than) this collar, how to handle. If set to ignore, the amend will proceed as requested. If reject, the request fails early. If clamp, the price is adjusted to the collar.

The default is reject.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (OrderStatus)
Order status.

order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/amend",
"params": {
"order_id": "1728379719872",
"price": 40000,
"amount": 1.1
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 40000,
"amount": 1.1,
"order_type": "limit",
"direction": "sell",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "amend",
"insert_reason": "client_request"
}
}
Cancel order

rpc
private/cancel
Cancel order

Request Body schema: application/json
method
required
string
Value: "private/cancel"
id	
object
Your request id, optional.

params
required
object
client_order_id	
integer
Exactly one of client_order_id or order_id must be specified.

order_id	
string
Exactly one of client_order_id or order_id must be specified.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (OrderStatus)
Order status.

order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/cancel",
"params": {
"order_id": "1728379719872"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 40000,
"amount": 1.1,
"order_type": "limit",
"direction": "sell",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "cancelled",
"fills": [ ],
"change_reason": "cancel",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"close_time": 1702583649.379417
}
}
Bulk cancel all orders

rpc
private/cancel_all
Cancels all orders for the account. This may not match new orders in flight (see private/cancel_session).

Request Body schema: application/json
method
required
string
Value: "private/cancel_all"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
number
The number of orders successfully deleted.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/cancel_all",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
{
"result": 42
}
Bulk cancel all orders in session

rpc
private/cancel_session
Cancels all non-persistent orders in the session. This method is allowed only on sessions that were set to cancel_on_disconnect, and has the same result as closing the connection:

all non-persistent orders are deleted, including those still in flight, with delete reason session_end.
market maker protection groups are reset and must be re-initialised.
Request Body schema: application/json
method
required
string
Value: "private/cancel_session"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/cancel_session",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
Request for Quote
Create a request for quote

rpc
private/create_rfq
Creates a new RFQ. You do not have to indicate upfront whether you want to buy or sell this package. Indicate the full size of the package.

Request Body schema: application/json
method
required
string
Value: "private/create_rfq"
id	
object
Your request id, optional.

params
required
object
legs
required
Array of objects
Specify any number of legs that you'd like to trade in a single package. Leg amounts may be positive (long) or negative (short), and must adhere to the regular volume tick size for the respective instrument. At least one leg must be long.

Array 
instrument_name
required
string
The leg instrument. Must be an outright instrument, not a combination.

amount
required
number
Amount to trade for this leg. Negative for short.

label	
string
User label for this RFQ, which will be reflected in eventual trades.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (Rfq)
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/create_rfq",
"params": {
"legs": [
{
"instrument_name": "string",
"amount": 0
}
]
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [
{
"instrument_name": "string",
"quantity": 0,
"fee_quantity": 0
}
],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {
"price": 0,
"amount": 0
},
"quoted_ask": {
"price": 0,
"amount": 0
},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
}
Cancel an RFQ

rpc
private/cancel_rfq
Cancels the indicated RFQ.

Request Body schema: application/json
method
required
string
Value: "private/cancel_rfq"
id	
object
Your request id, optional.

params
required
object
rfq_id
required
string
The ID of the RFQ to be cancelled

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/cancel_rfq",
"params": {
"rfq_id": "string"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
Trade an RFQ

rpc
private/trade_rfq
Trade on the quotes given. The requested amount is that of the original request.

Request Body schema: application/json
method
required
string
Value: "private/trade_rfq"
id	
object
Your request id, optional.

params
required
object
rfq_id
required
string
The ID of the RFQ

direction
required
string
Enum: "buy" "sell"
Whether to buy or sell. Important: this relates to the combination as created by the system, not the package as originally requested (although they should be equal).

limit_price
required
number
The maximum (for buy) or minimum (for sell) price to trade at. This is the price for one combination, not for the entire package.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
rfq_id
required
string
The RFQ traded.

direction
required
string
Enum: "buy" "sell"
The direction of the trade as requested.

price
required
number
The trade price per combination.

amount
required
number
The number of combinations traded.

legs
required
Array of objects
The trades on the individual legs.

Array 
instrument_name
required
string
direction
required
string
Enum: "buy" "sell"
The trade direction for this leg.

amount
required
number
The total amount traded on this leg.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/trade_rfq",
"params": {
"rfq_id": "string",
"direction": "buy",
"limit_price": 0
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"rfq_id": "string",
"direction": "buy",
"price": 0,
"amount": 0,
"legs": [
{
"instrument_name": "string",
"direction": "buy",
"amount": 0
}
]
}
}
Open RFQs

rpc
private/open_rfqs
Retrieves a list of open RFQs created by this account.

Request Body schema: application/json
method
required
string
Value: "private/open_rfqs"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of objects (Rfq)
List of open RFQs.

Array 
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/open_rfqs",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": [
{
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [
{}
],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {
"price": 0,
"amount": 0
},
"quoted_ask": {
"price": 0,
"amount": 0
},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
]
}
Request for Quote (MM)
Open RFQs

rpc
private/mm_rfqs
Retrieves a list of open RFQs that this account has access to.

Request Body schema: application/json
method
required
string
Value: "private/mm_rfqs"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of objects (Rfq)
List of open RFQs.

Array 
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/mm_rfqs",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": [
{
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [
{}
],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {
"price": 0,
"amount": 0
},
"quoted_ask": {
"price": 0,
"amount": 0
},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
]
}
Quote on an RFQ

rpc
private/mm_rfq_insert_quote
Sends a new quote on the indicated RFQ. This does not remove any previous quote: any number of quotes may be active on either side. Note that if the session was set to non-persistent (cancel-on-disconnect), then this quote will also be non-persistent.

Request Body schema: application/json
method
required
string
Value: "private/mm_rfq_insert_quote"
id	
object
Your request id, optional.

params
required
object
rfq_id
required
string
The ID of the RFQ this quote is for.

client_order_id	
integer
Session-local identifier for this order. Only valid for websocket sessions. If set, must be a number between 0 and 2^64-1, inclusive. When using numbers larger than 2^32, please beware of implicit floating point conversions in some JSON libraries.

direction
required
string
Enum: "buy" "sell"
The side of the quote.

price
required
number
Limit price for the quote (for one combination).

amount
required
number
Number of combinations to quote. Anything over the requested amount will not be visible to the requester.

label	
string
A label to attach to eventual trades.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (RfqOrder)
rfq_id
required
string
Identifier of the RFQ.

order_id
required
string
Identifier of the individual quote.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

direction
required
string
Enum: "buy" "sell"
price
required
number
amount
required
number
label	
string
trade_price	
number
the price at which this order traded.

trade_amount	
number
the number of combinations that traded.

delete_reason	
string
Enum: "client_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled"
Detailed reason of order deletion.

event	
string
Enum: "Inserted" "Amended" "Cancelled" "Filled" "Existing"
This field is set only on subscriptions.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/mm_rfq_insert_quote",
"params": {
"rfq_id": "string",
"direction": "buy",
"price": 0,
"amount": 0
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"rfq_id": "string",
"order_id": "string",
"client_order_id": 0,
"direction": "buy",
"price": 0,
"amount": 0,
"label": "string",
"trade_price": 0,
"trade_amount": 0,
"delete_reason": "client_cancel",
"event": "Inserted"
}
}
Amend quote

rpc
private/mm_rfq_amend_quote
Change the amount and price of an existing quote.

Request Body schema: application/json
method
required
string
Value: "private/mm_rfq_amend_quote"
id	
object
Your request id, optional.

params
required
object
client_order_id	
integer
Exactly one of client_order_id or order_id must be specified.

order_id	
string
Exactly one of client_order_id or order_id must be specified.

price
required
number
Limit price for the quote (for one combination).

amount
required
number
Number of combinations to quote. Anything over the requested amount will not be visible to the requester.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (RfqOrder)
rfq_id
required
string
Identifier of the RFQ.

order_id
required
string
Identifier of the individual quote.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

direction
required
string
Enum: "buy" "sell"
price
required
number
amount
required
number
label	
string
trade_price	
number
the price at which this order traded.

trade_amount	
number
the number of combinations that traded.

delete_reason	
string
Enum: "client_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled"
Detailed reason of order deletion.

event	
string
Enum: "Inserted" "Amended" "Cancelled" "Filled" "Existing"
This field is set only on subscriptions.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/mm_rfq_amend_quote",
"params": {
"price": 0,
"amount": 0
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"rfq_id": "string",
"order_id": "string",
"client_order_id": 0,
"direction": "buy",
"price": 0,
"amount": 0,
"label": "string",
"trade_price": 0,
"trade_amount": 0,
"delete_reason": "client_cancel",
"event": "Inserted"
}
}
Delete quote

rpc
private/mm_rfq_delete_quote
Deletes the indicated RFQ quote.

Request Body schema: application/json
method
required
string
Value: "private/mm_rfq_delete_quote"
id	
object
Your request id, optional.

params
required
object
client_order_id	
integer
Exactly one of client_order_id or order_id must be specified.

order_id	
string
Exactly one of client_order_id or order_id must be specified.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/mm_rfq_delete_quote",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
List of active quotes

rpc
private/mm_rfq_quotes
Retrieves a list of open RFQ quotes across all RFQs.

Request Body schema: application/json
method
required
string
Value: "private/mm_rfq_quotes"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of objects (RfqOrder)
Array 
rfq_id
required
string
Identifier of the RFQ.

order_id
required
string
Identifier of the individual quote.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

direction
required
string
Enum: "buy" "sell"
price
required
number
amount
required
number
label	
string
trade_price	
number
the price at which this order traded.

trade_amount	
number
the number of combinations that traded.

delete_reason	
string
Enum: "client_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled"
Detailed reason of order deletion.

event	
string
Enum: "Inserted" "Amended" "Cancelled" "Filled" "Existing"
This field is set only on subscriptions.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/mm_rfq_quotes",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": [
{
"rfq_id": "string",
"order_id": "string",
"client_order_id": 0,
"direction": "buy",
"price": 0,
"amount": 0,
"label": "string",
"trade_price": 0,
"trade_amount": 0,
"delete_reason": "client_cancel",
"event": "Inserted"
}
]
}
Accounting
Portfolio

rpc
private/portfolio
Get account portfolio

Request Body schema: application/json
method
required
string
Value: "private/portfolio"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of objects (PortfolioEntry)
Portfolio positions.

Array 
instrument_name	
string
Instrument name.

position	
number
Amount of this contract currently held; short positions are negative.

mark_price	
number
Current mark price for the instrument.

iv	
number
Implied volatility calculated at time of marking.

index	
number
Index price at time of marking.

start_price	
number
Average price paid to obtain position.

Note: for instruments that are subject to daily futures-style settlement, the start price is reset to the mark price at the end of each session and all the unrealized P&L is thus realized. Use private/daily_mark_history API endpoint to get information about daily settlements.

average_price	
number
Average price paid to obtain position. Doesn't reset at settlement.

unrealised_pnl	
number
Unrealised P&L in the current session for this position based on current mark price, equal to (mark_price - start_price) * position.

Note: for instruments that are subject to daily futures-style settlement, the start price is reset to the mark price at the end of each session and all the unrealized P&L is thus realized. Use private/daily_mark_history API endpoint to get information about daily settlements.

realised_pnl	
number
Realized P&L in the current session.

Realized P&L is settled into a settlement asset at the end of each session.

entry_value	
number
Total entry value, equal to start_price * position.

perpetual_funding_entry_value	
number
Entry mark value for perpetual funding. Unrealised perpetual funding is (current perp funding mark * position) - perpetual funding entry value. Not included if zero.

unrealised_perpetual_funding	
number
For perpetual positions, current unrealized perpetual funding.

The funding is realized as P&L and settled into settlement asset at the end of each session.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/portfolio",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": [
{
"instrument_name": "BTC-PERPETUAL",
"position": 1,
"mark_price": 47299.741264339274,
"start_price": 47260,
"average_price": 47260,
"unrealised_pnl": 39.75859976453942,
"realised_pnl": 0,
"entry_value": 47260,
"perpetual_funding_entry_value": -0.13040705,
"unrealised_perpetual_funding": 0.017335425264924917
}
]
}
Open orders

rpc
private/open_orders
Get open orders

Request Body schema: application/json
method
required
string
Value: "private/open_orders"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of objects (OrderStatus)
All currently open orders for the account.

Array 
order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/open_orders",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
{
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "buy",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
]
}
Order history

rpc
private/order_history
Retrieves a list of past orders (i.e. orders that are not active anymore) since the last 90 days. Allows sorting and filtering by instrument name.

Unfilled market maker orders are not included.

Orders are like order status updates, without the remaining_amount field (always 0), and with a close_time timestamp. Note that, for technical reasons, the 'fills' field in the order is limited to a length of 8. For a full list of trades, refer to trade history.

Note that it is not real-time, data might appear with a slight delay.

Request Body schema: application/json
method
required
string
Value: "private/order_history"
id	
object
Your request id, optional.

params
required
object
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to 90 days ago.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

sort	
string
Enum: "ascending" "descending"
Sort direction by order close_time. Defaults to descending (i.e. newest items first).

instrument_names	
string
Comma-separated list of instrument names to request order history for. If omitted, order history for all instruments is returned.

bot_ids	
string
Optional comma-separated list of bot IDs to request order history history for.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
orders	
Array of objects (OrderHistory)
List of historical orders.

Array 
order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
All fills for this order.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

delete_reason
required
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

self_trade_prevention: The order was cancelled by the self trade prevention mechanism.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time
required
number
Time when this order was closed or canceled (Unix timestamp).

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/order_history",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"orders": [
{
"order_id": "001BF14D00000003",
"instrument_name": "BTC-16DEC23-46000-C",
"direction": "sell",
"price": "10.0,",
"amount": "0.2,",
"filled_amount": "0.2,",
"status": "filled",
"fills": [],
"create_time": "1702583649.379417,",
"close_time": "1702583649.379417,",
"insert_reason": "client_request",
"delete_reason": "filled",
"order_type": "limit"
}
],
"bookmark": "string"
}
}
Conditional order history

rpc
private/conditional_order_history
Retrieves a list of past conditional orders (i.e. orders that are not active anymore). Allows sorting and filtering by instrument name.

Note that it is not real-time, data might appear with a slight delay.

Request Body schema: application/json
method
required
string
Value: "private/conditional_order_history"
id	
object
Your request id, optional.

params
required
object
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to 90 days ago.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

sort	
string
Enum: "ascending" "descending"
Sort direction by order create_time. Defaults to descending (i.e. newest items first).

instrument_names	
string
Comma-separated list of instrument names to request order history for. If omitted, order history for all instruments is returned.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
orders	
Array of objects (ConditionalOrder)
List of historical conditional orders.

Array 
order_id
required
string
Unique ID, use to identify in cancel

instrument_name
required
string
direction
required
string
Enum: "buy" "sell"
amount
required
number
Size of the order when activated

target
required
string
Enum: "last" "mark" "index"
The trigger type that stop_price and bracket_price will refer to.

stop_price
required
number
Trigger price at which the order will be activated

limit_price	
number
For stop limit order, the price at which the order will be placed

bracket_price	
number
For bracket order, the price at which profit will be taken (upper activation price)

trailing_stop_callback_rate	
number
For trailing stop loss, the callback rate as a ratio (e.g. 0.05 for 5%)

label	
string
Optional user label

status
required
string
Enum: "created" "active" "converted" "rejected" "cancel requested" "cancelled"
create_time
required
number
update_time
required
number
Time of last update (conversion or change of trailing stop price)

convert_time	
number
Time of trigger

converted_order_id	
string
System order ID of the created order.

reject_reason	
string
If conversion failed, the reason

reduce_only
required
boolean
bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/conditional_order_history",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"orders": [
{
"order_id": "00011E570000004B",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"amount": 1,
"stop_price": 50000,
"limit_price": 45000,
"status": "created",
"create_time": 1630062311.3324597,
"update_time": 1630062311.3324597,
"reduce_only": false,
"target": "mark"
}
],
"bookmark": "string"
}
}
Trade history

rpc
private/trade_history
Retrieves trades for the last 90 days. Allows sorting and filtering by instrument name. Note that it is not real-time, trades might appear with a slight delay.

Request Body schema: application/json
method
required
string
Value: "private/trade_history"
id	
object
Your request id, optional.

params
required
object
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to 90 days ago.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

sort	
string
Enum: "ascending" "descending"
Sort direction by trade time. Defaults to descending (i.e. newest trades first).

instrument_names	
string
Comma-separated list of instrument names to request trade history for. If omitted, trades for all instruments are returned.

bot_ids	
string
Optional comma-separated list of bot IDs to request trade history for.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
trades	
Array of objects (Trade)
List of trades.

Array 
trade_type	
string
Enum: "normal" "block" "combo" "amend" "delete" "internal_transfer" "expiration" "daily_mark" "rfq" "liquidation"
Type of the trade.

Note: as of API v2.31.0 we have stopped representing futures-style settlements as trades of daily_mark type. You might still get such trades in the history, but no new trades of daily_mark type will be created. To get information about daily marks, use private/daily_mark_history API endpoint.

trade_id	
string
order_id	
string
instrument_name	
string
direction	
string
Enum: "buy" "sell"
price	
number
Trade price.

amount	
number
Traded amount.

label	
string
User label.

time	
number
Time of trade (Unix timestamp).

position_after	
number
Position in this instrument right after the trade.

session_realised_after	
number
Session realised P&L for this instrument right after the trade.

position_pnl	
number
If trade closed a position, the positional P&L that was realised.

perpetual_funding_pnl	
number
If trade closed a position in a perpetual, the funding P&L that was realised.

fee	
number
The fee paid for this trade.

The fee for a trade is calculated as fee_basis * fee_rate * amount, and is then subject to clamping to minimum and maximum fee. Depending on the instrument, fee_basis can be different (e.g. it can be equal to the underlying index, trade price or combo mark price). Please refer to trading information pages for more details.

index	
number
The relevant index at time of trade.

fee_rate	
number
The fee rate applied to calculate the fee.

fee_basis	
number
The fee basis on which the fee is calculated.

funding_mark	
number
The perpetual funding mark as applied to the trade (see Ticker).

liquidation_fee	
number
Fee paid in case of liquidation.

client_order_id	
number
Client order reference as set in related order.

maker_taker	
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

bot_id	
string
If the trade was made by a bot, the ID of that bot. Otherwise omitted.

leg_index	
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/trade_history",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"trades": [
{
"order_id": "00011E570000004A",
"trade_id": "0080000000000000169F22D05B785A2B",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"price": 47280,
"amount": 0.1,
"label": "",
"time": 1630059868.4145653,
"position_after": 1.1,
"trade_type": "normal",
"leg_index": 0
},
{
"order_id": "00011E570000004B",
"trade_id": "0080000000000000169F20CE441AD986",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"price": 47260,
"amount": 1,
"label": "",
"time": 1630057660.409371,
"position_after": 1,
"trade_type": "normal",
"leg_index": 0
}
]
}
}
Trading volume historical data.

rpc
private/trade_value_history
Returns historical trading volume in the specified interval and resolution.

Request Body schema: application/json
method
required
string
Value: "private/trade_value_history"
id	
object
Your request id, optional.

params
required
object
time_low
required
number
Start time (Unix timestamp) (inclusive).

time_high
required
number
End time (Unix timestamp) (inclusive).

resolution
required
string
Enum: "1d" "1w" "1mo"
Each trade value is aggregated per time resolution, underlying and category.

limit	
number
Default: 1000
The maximum number of primary items to return per page. Due to resolution grouping rules, a page may include additional items beyond the limit to ensure that all items sharing the same date_time_bucket as the last item within the limit are included.

bookmark	
string
Set to bookmark from previous call to get next page.

sort	
string
Enum: "ascending" "descending"
Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
trade_values	
Array of objects (TradeValue)
Array of trade value objects.

Array 
underlying
required
string
Underlying name.

trade_volume
required
number
Total trading volume for the underlying instrument category.

trade_value
required
number
The total value traded for the underlying instrument category.

category
required
string
Enum: "options" "futures" "perpetual"
Instrument category.

date_time_bucket
required
any
Start time of the aggregation interval (day, week, or month).

bookmark	
string
Set when additional data exists within or before the requested time interval.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/trade_value_history",
"params": {
"time_low": 0,
"time_high": 0,
"resolution": "1d"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"trade_values": [
{
"account_id": 861918865,
"underlying": "BTCUSD",
"trade_volume": 10,
"trade_value": 20,
"category": "options",
"date_time_bucket": "1704700800000000000"
}
],
"bookmark": "string"
}
}
Daily mark history

rpc
private/daily_mark_history
For instruments that are subject to futures-style settlement we perform daily settlement at the mark price. The settlement procedure realizes the positional and perpetual funding profits/losses accumulated during the session, and resets the start price of the position to the mark price.

This API endpoint returns a historical log of settled profits/losses (daily marks).

Request Body schema: application/json
method
required
string
Value: "private/daily_mark_history"
id	
object
Your request id, optional.

params
required
object
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to zero.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
daily_marks	
Array of objects (DailyMark)
List of daily marks.

Array 
time
required
number
Time of settlement (Unix timestamp).

instrument_name
required
string
Instrument name.

position
required
number
Position in the instrument.

mark_price
required
number
Mark price used for settlement.

realized_position_pnl
required
number
Realized profit or loss for this position.

realized_funding_pnl	
number
Realized perpetual funding. Only present for perpetuals.

bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/daily_mark_history",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"daily_marks": [
{
"time": 1630059868.4145653,
"instrument_name": "BTC-PERPETUAL",
"mark_price": 47280,
"position": 0.1,
"realized_position_pnl": 1220,
"realized_funding_pnl": 10
},
{
"time": 1630059868.4145653,
"instrument_name": "BTC-27DEC24",
"mark_price": 48100,
"position": -0.5,
"realized_position_pnl": -405
}
]
}
}
Transaction history

rpc
private/transaction_history
Get transaction history

Request Body schema: application/json
method
required
string
Value: "private/transaction_history"
id	
object
Your request id, optional.

params
required
object
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to zero.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
transactions
required
Array of objects
List of transactions.

Array 
time
required
number
Timestamp when the transaction was performed.

For actions that produce multiple transactions (e.g. asset swaps, internal transfers), all transactions will have the same timestamp.

asset
required
string
Asset name.

amount
required
number
Amount credited (positive number) or debited (negative number).

instrument_name	
string
Instrument name this transaction relates to. For example, settlement transactions are per instrument.

Not included for transactions that don't relate to an instrument.

transaction_type	
string
Enum: "credit" "deposit" "withdrawal" "withdrawal fee" "session settlement" "perpetual funding" "internal transfer" "asset swap" "referral program payment" "market velocity program payment" "market quality program payment" "daily interest"
Transaction type. Can be one of the following values:

credit - Asset credits or debits.
deposit - Deposits.
withdrawal - Withdrawals.
withdrawal fee - Withdrawal fees.
session settlement - Settled session PNL.
perpetual funding - Settled perpetual funding.
internal transfer - Transfer of assets between sub-accounts. One transaction in each sub-account per asset per transfer.
asset swap - Swap between assets. One transaction for each side of the asset pair per swap.
referral program payment - Referral program rewards.
market velocity program payment - MVP program rewards.
market quality program payment - MQP program rewards.
daily interest - Daily penalty charge for negative balance. Not applied anymore, but can be found in historical transactions.
description
required
string
Description of this transaction.

Note that this field is not supposed to be machine-readable and the the format is not guaranteed to remain unchanged.

balance_after	
number
Account balance in this asset right after transaction.

bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/transaction_history",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"transactions": [
{
"asset": "USDT",
"time": 1629964800.012722,
"amount": -643.70276425,
"description": "daily settlement USD -643.83220000 @ 1.000201",
"transaction_type": "session settlement",
"instrument_name": "BTC-PERPETUAL",
"balance_after": 1000000004483.9625
}
]
}
}
RFQ history

rpc
private/rfq_history
Retrieves a list of past RFQs for the account. Open RFQs are not incuded.

Request Body schema: application/json
method
required
string
Value: "private/rfq_history"
id	
object
Your request id, optional.

params
required
object
limit	
integer <= 1000
Default: 1000
Max results to return.

time_low	
number
Start time (Unix timestamp) defaults to zero.

time_high	
number
End time (Unix timestamp) defaults to now.

bookmark	
string
Set to bookmark from previous call to get next page.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
rfqs	
Array of objects (Rfq)
List of RFQs.

Array 
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.

bookmark	
string
Bookmark to retrieve next page, or null (no more results).

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/rfq_history",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"rfqs": [
{
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {},
"quoted_ask": {},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
],
"bookmark": "string"
}
}
Account breakdown

rpc
private/account_breakdown
Get account breakdown

Request Body schema: application/json
method
required
string
Value: "private/account_breakdown"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
account_number
required
string
Account number

unrealised_pnl
required
number
Total unrealised profit or loss.

cash_collateral
required
number
Total margin based on cash holdings.

margin
required
number
Total margin from unrealised P&L and cash holdings.

required_margin
required
number
Required margin based on current position.

remaining_margin
required
number
Difference between margin and required margin.

session_realised_pnl
required
number
Total realised profit or loss in current session.

realised_position_pnl
required
number
Position profit or loss in current session.

realised_perpetual_funding
required
number
Realised perpetual funding profit or loss in current session.

session_fees
required
number
Fees paid in current session.

portfolio
required
Array of objects
List of positions each with unrealised P&L.

Array 
instrument_name
required
string
position
required
number
mark_price	
number
start_price	
number
average_price	
number
unrealised_pnl_positional
required
number
unrealised_pnl_perpetual	
number
unrealised_pnl
required
number
realised_position_pnl
required
number
open_buy_amount
required
number
open_sell_amount
required
number
session_realised_pnl
required
number
realised_perpetual_funding
required
number
session_fees
required
number
cash
required
Array of objects
List of cash holdings, for each relevant currency, and how they contribute to margin.

Array 
currency
required
string
Currency name.

balance
required
number
Current balance in this currency.

collateral_factor
required
number
The collateral quality of the asset i.e. the fraction of the asset that can be used as a collateral.

collateral_index_price	
number
Index price used to calculate collateral effect of this position. Can be null for assets that are not converted using an index, e.g. for stable coins.

applied_collateral
required
number
Total collateral effect of this position.

transactable
required
boolean
If this flag is true, this currency can be deposited and withdrawn.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/account_breakdown",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"account_number": "A123456789",
"portfolio": [
{
"instrument_name": "BTC-PERPETUAL",
"position": 1.1,
"mark_price": 47708.13763778502,
"start_price": 47261.81818181818,
"average_price": 47261.81818181818,
"unrealised_pnl_positional": 490.95140156352136,
"unrealised_pnl_perpetual": 0.05837153649983011,
"unrealised_pnl": 491.00977310002116,
"open_buy_amount": 0,
"open_sell_amount": 0,
"session_realised_pnl": -1.18,
"realised_position_pnl": 0,
"realised_perpetual_funding": 0,
"session_fees": 1.18
}
],
"cash": [
{
"currency": "USDT",
"balance": 1000000004483.9625,
"collateral_factor": 1,
"collateral_index_price": null,
"applied_collateral": 1000000004483.9625,
"transactable": true
}
],
"unrealised_pnl": 491.00977310002116,
"session_realised_pnl": -1.18,
"realised_position_pnl": 0,
"realised_perpetual_funding": 0,
"session_fees": 1.18,
"cash_collateral": 1000000004483.9625,
"margin": 1000000004994.1586,
"required_margin": 13123.880458333333,
"remaining_margin": 999999991870.2781
}
}
Account summary

rpc
private/account_summary
Get account summary

Request Body schema: application/json
method
required
string
Value: "private/account_summary"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (AccountSummary)
unrealised_pnl
required
number
Total unrealised profit or loss.

cash_collateral
required
number
Total margin based on cash holdings.

margin
required
number
Total margin from unrealised P&L and cash holdings.

required_margin
required
number
Required margin based on current position.

remaining_margin
required
number
Difference between margin and required margin.

session_realised_pnl
required
number
Realised profit or loss in current session.

cash
required
Array of objects
List of cash holdings, for each relevant currency, and how they contribute to margin.

Array 
currency
required
string
Currency name.

balance
required
number
Current balance in this currency.

collateral_factor
required
number
The collateral quality of the asset i.e. the fraction of the asset that can be used as a collateral.

collateral_index_price	
number
Index price used to calculate collateral effect of this position. Can be null for assets that are not converted using an index, e.g. for stable coins.

transactable
required
boolean
If this flag is true, this currency can be deposited and withdrawn.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/account_summary",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"cash": [
{
"currency": "USDT",
"balance": 1000000004483.9625,
"collateral_factor": 1,
"collateral_index_price": null,
"transactable": true
}
],
"unrealised_pnl": 491.00977310002116,
"session_realised_pnl": 0,
"cash_collateral": 1000000004483.9625,
"margin": 1000000004994.1586,
"required_margin": 13123.880458333333,
"remaining_margin": 999999991870.2781
}
}
Margin breakdown

rpc
private/required_margin_breakdown
Get margin breakdown

Request Body schema: application/json
method
required
string
Value: "private/required_margin_breakdown"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (PortfolioMarginBreakdown)
Required margin breakdown for accounts that use portfolio margin.

portfolio	
object
required_margin	
number
Total required margin for account.

underlyings	
Array of objects
Array 
underlying	
string
Underlying index name.

required_margin	
number
Total margin required for positions with this underlying.

scenario_margin	
number
Deprecated. Same value as loss_margin.

loss_margin	
number
Margin based on scenario loss coverage.

d1_roll_cash_position	
number
Delta one roll position x index price in this underlying.

options_roll_cash_position	
number
Options roll position x index price in this underlying.

roll_cash_position	
number
Roll position x index price in this underlying.

d1_roll_contingency_margin	
number
Margin based on delta one roll position.

options_roll_contingency_margin	
number
Margin based on options roll position.

roll_contingency_margin	
number
Margin based on roll position.

options_short_cash_position	
number
Total short options position x index price in this underlying.

options_contingency_margin	
number
Margin based on options short position.

scenario_used	
integer
Index of the scenario in the scenarios array that was used to calculate total margin requirements for this underlying.

scenarios	
Array of objects
Scenarios that were simulated.

Array 
underlying_change_pct	
number
Simulated underlying change, %

vol_change_pct_point	
number
Simulated volatility change, %

pnl	
number
P&L resulting from this scenario.

coverage_factor	
number
Effect factor of P&L on the loss margin.

required_margin	
number
Total required margin in this scenario.

loss_margin	
number
Margin based on scenario loss coverage.

roll_cash_position	
number
Roll position x index price in this underlying.

roll_contingency_margin	
number
Margin based on roll position.

d1_roll_cash_position	
number
Delta one roll position x index price in this underlying.

d1_roll_contingency_margin	
number
Margin based on delta one roll position.

options_roll_cash_position	
number
Options roll position x index price in this underlying.

options_roll_contingency_margin	
number
Margin based on options roll position.

options_short_cash_position	
number
Total short options position x index price in this underlying.

options_contingency_margin	
number
Margin based on options short position.

positions	
Array of objects
Array 
instrument_name	
string
Instrument feedcode.

position	
number
Position/order size in contracts.

instrument_pnl	
number
P&L for a single contract of this instrument.

pnl	
number
Total P&L for the position/order in this instrument.

current_price	
number
The price at the moment of scenario calculation.

For positions this is set to the current mark price.

For open orders this is the order limit price.

scenario_price	
number
The price simulated for the scenario.

open_order	
boolean
Indicates whether this position is implied from an open order.

assumed_filled	
boolean
Indicates whether this order was assumed to be filled in this scenario.

Orders are assumed to be filled if they, for the particular scenario, generate an immediate loss if filled at the limit price.

Only orders that are assumed to be filled are taken into account for the loss, roll contingency and option contingency margin requirements.

This field is only present if open_order is true.

assets	
Array of objects
Results of scenario simulations on affected asset positions.

Array 
asset_name	
string
Asset name

position	
number
underlying_pnl	
number
P&L for a single unit of this asset.

pnl	
number
Total P&L for the position in this asset.

collateral_factor	
number
The collateral quality of the asset i.e. the fraction of the asset that can be used as a collateral.

index_price	
number
Index price at the moment of scenario calculation.

current_price	
number
The price at the moment of scenario calculation. This is the margin effect of this asset position, i.e. index price multiplied by collateral factor.

scenario_price	
number
The price calculated for the scenario.

highlight	
boolean
true if this scenario was used to calculate total margin requirements for this underlying.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/required_margin_breakdown",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"portfolio": {
"required_margin": -155.90231262790033,
"underlyings": [
{}
]
}
}
}
Margin breakdown with order

rpc
private/required_margin_for_order
This method returns a lightweight breakdown of the account as it is, and also as if a hypothetical order of a given price and amount would be inserted on either side of the book.

Request Body schema: application/json
method
required
string
Value: "private/required_margin_for_order"
id	
object
Your request id, optional.

params
required
object
instrument_name	
string
The name of the instrument of this hypothetical order with which the margin is to be broken down with. This field must not be present when requesting margin breakdown for a combination order. Use legs field instead.

legs	
Array of objects
List of legs for a combination order.

There must be at least two and at most four legs specified. All leg instruments must be distinct.

Other constraints apply, please check trading information page on combination orders.

This field must not be present when requesting margin breakdown for single-leg orders. Use instrument_name field instead.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

price
required
number
The price of the hypothetical order.

amount
required
number
The amount that would be traded.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (MarginBreakdownWithOrder)
Lightweight margin breakdown without and with an order inserted as buy or sell.

current	
object
required_margin	
number
Total required margin for account.

underlying	
object
underlying	
string
Underlying index name.

required_margin	
number
Total margin required for positions with this underlying.

loss_margin	
number
Margin based on scenario loss coverage.

roll_contingency_margin	
number
Margin based on roll position.

d1_roll_contingency_margin	
number
Margin based on delta one roll position.

options_roll_contingency_margin	
number
Margin based on options roll position.

options_contingency_margin	
number
Margin based on options short position.

with_buy	
object
required_margin	
number
Total required margin for account with the order inserted as buy.

underlying	
object
underlying	
string
Underlying index name.

required_margin	
number
Total margin required for positions with this underlying.

loss_margin	
number
Margin based on scenario loss coverage.

roll_contingency_margin	
number
Margin based on roll position.

d1_roll_contingency_margin	
number
Margin based on delta one roll position.

options_roll_contingency_margin	
number
Margin based on options roll position.

options_contingency_margin	
number
Margin based on options short position.

with_sell	
object
required_margin	
number
Total required margin for account with the order inserted as sell.

underlying	
object
underlying	
string
Underlying index name.

required_margin	
number
Total margin required for positions with this underlying.

loss_margin	
number
Margin based on scenario loss coverage.

roll_contingency_margin	
number
Margin based on roll position.

d1_roll_contingency_margin	
number
Margin based on delta one roll position.

options_roll_contingency_margin	
number
Margin based on options roll position.

options_contingency_margin	
number
Margin based on options short position.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/required_margin_for_order",
"params": {
"price": 0,
"amount": 0
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"current": {
"required_margin": -155.90231262790033,
"underlying": {
"required_margin": -155.90231262790033,
"underlying": "BTCUSD",
"loss_margin": -155.90231262790033,
"roll_contingency_margin": 151.54255212726002,
"d1_roll_contingency_margin": 151.54255212726002,
"options_roll_contingency_margin": 151.54255212726002,
"options_contingency_margin": 57.27288000000001
}
},
"with_buy": {
"required_margin": -155.90231262790033,
"underlying": {
"required_margin": -155.90231262790033,
"underlying": "BTCUSD",
"loss_margin": -155.90231262790033,
"roll_contingency_margin": 151.54255212726002,
"d1_roll_contingency_margin": 151.54255212726002,
"options_roll_contingency_margin": 151.54255212726002,
"options_contingency_margin": 57.27288000000001
}
},
"with_sell": {
"required_margin": -155.90231262790033,
"underlying": {
"required_margin": -155.90231262790033,
"underlying": "BTCUSD",
"loss_margin": -155.90231262790033,
"roll_contingency_margin": 151.54255212726002,
"d1_roll_contingency_margin": 151.54255212726002,
"options_roll_contingency_margin": 151.54255212726002,
"options_contingency_margin": 57.27288000000001
}
}
}
}
Subscriptions
Subscribe to private channels

rpc
private/subscribe
Subscribe to private channels

Request Body schema: application/json
method
required
string
Value: "private/subscribe"
id	
object
Your request id, optional.

params
required
object
channels
required
Array of strings
List of channels to subscribe to.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of strings
List of successfully subscribed channels. Note that this method returns successfully even if no channels were valid; check the return value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/subscribe",
"params": {
"channels": [
"account.orders"
]
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
"account.orders"
]
}
Subscribe to public channels

rpc
public/subscribe
Subscribe to public channels

Request Body schema: application/json
method
required
string
Value: "public/subscribe"
id	
object
Your request id, optional.

params
required
object
channels
required
Array of strings
List of channels to subscribe to.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of strings
List of successfully subscribed channels. Note that this method returns successfully even if no channels were valid; check the return value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/subscribe",
"params": {
"channels": [
"instruments"
]
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
"instruments"
]
}
Unsubscribe

rpc
unsubscribe
Unsubscribe from a set of channels

Request Body schema: application/json
method
required
string
Value: "unsubscribe"
id	
object
Your request id, optional.

params
required
object
channels
required
Array of strings
List of channels to unsubscribe from. Public and private channels may be mixed.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of strings
List of successfully unsubscribed channels. Note that this method returns successfully even if no channels were valid; check the return value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "unsubscribe",
"params": {
"channels": [
"account.orders",
"instruments"
]
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
"account.orders",
"instruments"
]
}
Conditional orders
Conditional orders

rpc
private/conditional_orders
Get conditional orders

Request Body schema: application/json
method
required
string
Value: "private/conditional_orders"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of objects (ConditionalOrder)
List of conditional orders, both active and formerly active. After activation, conditional orders may be listed for another few days.

Array 
order_id
required
string
Unique ID, use to identify in cancel

instrument_name
required
string
direction
required
string
Enum: "buy" "sell"
amount
required
number
Size of the order when activated

target
required
string
Enum: "last" "mark" "index"
The trigger type that stop_price and bracket_price will refer to.

stop_price
required
number
Trigger price at which the order will be activated

limit_price	
number
For stop limit order, the price at which the order will be placed

bracket_price	
number
For bracket order, the price at which profit will be taken (upper activation price)

trailing_stop_callback_rate	
number
For trailing stop loss, the callback rate as a ratio (e.g. 0.05 for 5%)

label	
string
Optional user label

status
required
string
Enum: "created" "active" "converted" "rejected" "cancel requested" "cancelled"
create_time
required
number
update_time
required
number
Time of last update (conversion or change of trailing stop price)

convert_time	
number
Time of trigger

converted_order_id	
string
System order ID of the created order.

reject_reason	
string
If conversion failed, the reason

reduce_only
required
boolean
Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/conditional_orders",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"result": [
{
"order_id": "00011E570000004B",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"amount": 1,
"stop_price": 50000,
"limit_price": 45000,
"status": "created",
"create_time": 1630062311.3324597,
"update_time": 1630062311.3324597,
"reduce_only": false
}
]
}
}
Create conditional order

rpc
private/create_conditional_order
A buy order will activate when a trade/mark/index happens at a price at or higher than the stop price, or at or lower than the bracket price (if set). A sell order will activate when a trigger happens at a price at or lower than the stop price, or at or higher than the bracket price (if set).

When a callback rate is set, the stop price for a buy order will trail down at (trade price * (1 + callback rate)), and for a sell order the stop price will trail up at (trade price * (1 - callback rate)).

A stop limit order will activate to a good-till-cancelled limit order, all other types will activate to a market order.

The last trigger target tracks aggressive trades in the instrument. The mark target tracks the mark price of the instrument, as calculated every second by the Thalex pricing engine. The index trigger target is allowed only for futures (instrument type perpetual or future), and tracks the index price of the respective underlying, as calculated every second by the Thalex pricing engine.

Only the following combinations are possible:

stop order: set only stop price
stop limit order: set stop price and limit price
bracket order: set stop price and bracket price. For a buy order, the bracket price must be under the stop price, and for a sell order the other way around.
trailing stop loss order: set stop price and callback rate.
Request Body schema: application/json
method
required
string
Value: "private/create_conditional_order"
id	
object
Your request id, optional.

params
required
object
direction
required
string
Enum: "buy" "sell"
instrument_name
required
string
amount
required
number
limit_price	
number
If set, creates a stop limit order

target	
string
Enum: "last" "mark" "index"
The trigger target that stop_price and bracket_price refer to.

stop_price
required
number
Trigger price

bracket_price	
number
If set, creates a bracket order

trailing_stop_callback_rate	
number
If set, creates a trailing stop order

label	
string
Label will be set on the activated order

reduce_only	
boolean
Activated order will be reduce-only

stp_level	
string
Enum: "customer" "account" "disabled"
The self trade prevention level override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is customer and not configurable.

stp_action	
string
Enum: "cancel_aggressive_partial_fill" "cancel_aggressive_no_fill"
The self trade prevention action override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is cancel_aggressive_partial_fill and not configurable.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (ConditionalOrder)
order_id
required
string
Unique ID, use to identify in cancel

instrument_name
required
string
direction
required
string
Enum: "buy" "sell"
amount
required
number
Size of the order when activated

target
required
string
Enum: "last" "mark" "index"
The trigger type that stop_price and bracket_price will refer to.

stop_price
required
number
Trigger price at which the order will be activated

limit_price	
number
For stop limit order, the price at which the order will be placed

bracket_price	
number
For bracket order, the price at which profit will be taken (upper activation price)

trailing_stop_callback_rate	
number
For trailing stop loss, the callback rate as a ratio (e.g. 0.05 for 5%)

label	
string
Optional user label

status
required
string
Enum: "created" "active" "converted" "rejected" "cancel requested" "cancelled"
create_time
required
number
update_time
required
number
Time of last update (conversion or change of trailing stop price)

convert_time	
number
Time of trigger

converted_order_id	
string
System order ID of the created order.

reject_reason	
string
If conversion failed, the reason

reduce_only
required
boolean
Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/create_conditional_order",
"params": {
"direction": "buy",
"instrument_name": "string",
"amount": 0,
"stop_price": 0
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"order_id": "00011E570000004B",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"amount": 1,
"stop_price": 50000,
"limit_price": 45000,
"status": "created",
"create_time": 1630062311.3324597,
"update_time": 1630062311.3324597,
"reduce_only": false,
"target": "mark"
}
}
Cancel conditional order

rpc
private/cancel_conditional_order
Cancel conditional order

Request Body schema: application/json
method
required
string
Value: "private/cancel_conditional_order"
id	
object
Your request id, optional.

params
required
object
order_id
required
string
Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/cancel_conditional_order",
"params": {
"order_id": "00011E570000004B"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
Bulk cancel conditional orders

rpc
private/cancel_all_conditional_orders
Cancel all conditional orders of this subaccount

Request Body schema: application/json
method
required
string
Value: "private/cancel_all_conditional_orders"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/cancel_all_conditional_orders",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
Bot management
Get bots

rpc
private/bots
Get bots

Request Body schema: application/json
method
required
string
Value: "private/bots"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of SGSL (object) or OCQ (object) or Levels (object) or Grid (object) or DHedge (object) or DFollow (object) (Bot)
List of bots, both active and formerly active. Bots may be listed for another few days after they're stopped.

Array 
One of SGSLOCQLevelsGridDHedgeDFollow
bot_id
required
string
Individually identifies this bot instance. You can use it to cancel this specific one.

status
required
string
Enum: "active" "stopped"
stop_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "end_time" "instrument_deactivated" "margin_breach" "admin_cancel" "conflict" "strategy" "self_trade_prevention"
The reason why the bot stopped executing.

strategy
required
string
equal to "sgsl"

instrument_name
required
string
Name of the instrument.

signal
required
string
Enum: "last" "index" "mark"
entry_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

target_position
required
number
The target position to maintain in the subaccount if signal price is above entry_price. See the bot strategies section for more explanation.

exit_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

exit_position
required
number
The target position to maintain in the subaccount if signal price is below exit_price. See the bot strategies section for more explanation.

max_slippage	
number
Maximum slippage per trade, expressed as % of the traded instruments mark price.

end_time
required
number
Timestamp when the bot stops executing, cancelling its orders and leaving all positions of the subaccount intact.

start_time
required
number
Timestamp indicating when the bot was created.

stop_time	
number
Timestamp indicating when the bot stopped working due to specified stop_reason.

label	
string
A label that the bot will add to all orders for easy identification.

realized_pnl
required
number
Realized P&L made by this bot since the start.

fee
required
number
Trade fees by this bot.

average_price	
number
Average entry price of the position (if any).

position_size	
number
Position size (if any).

mark_price_at_stop	
number
Mark price of the bot instrument at the moment the bot was stopped.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/bots",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": [
{
"strategy": "sgsl",
"status": "active",
"bot_id": "0000000035832FDE",
"instrument_name": "BTC-PERPETUAL",
"signal": "index",
"entry_price": 100050,
"target_position": 0.2,
"exit_price": 100000,
"exit_position": 0,
"end_time": 1740064912,
"start_time": 1740064912,
"stop_time": 1740064912
},
{
"strategy": "ocq",
"status": "stopped",
"stop_reason": "client_cancel",
"bot_id": "0000000035832FDF",
"instrument_name": "BTC-PERPETUAL",
"signal": "index",
"bid_offset": -50,
"ask_offset": 120,
"quote_size": 0.1,
"min_position": -0.3,
"max_position": 0.25,
"end_time": 1740064912,
"start_time": 1740064912,
"stop_time": 1740064912
}
]
}
Create a bot

rpc
private/create_bot
Instantiate a bot that keeps continually trading in your name according to a predefined strategy. See the bot strategies section for more info on bots. For risk fencing reasons and because of the complex ways manual trades can interact with bot strategies, you might want to consider running bots on a separate/dedicated sub account. Also be aware that you can set up bots with different strategies in a way that they would end up trading with each other.

Request Body schema: application/json
method
required
string
Value: "private/create_bot"
id	
object
Your request id, optional.

params
required
SGSL (object) or OCQ (object) or Levels (object) or Grid (object) or DHedge (object) or DFollow (object)
One of SGSLOCQLevelsGridDHedgeDFollow
strategy
required
string
Equal to "sgsl"

instrument_name
required
string
Name of the instrument to run SGSL on.

signal
required
string
Enum: "last" "index" "mark"
entry_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

target_position
required
number
The target position to maintain in the subaccount if signal price is above entry_price. See the bot strategies section for more explanation.

exit_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

exit_position
required
number
The target position to maintain in the subaccount if signal price is below exit_price. See the bot strategies section for more explanation.

max_slippage	
number
Maximum slippage per trade, expressed as % of the traded instruments mark price.

end_time
required
number
Timestamp when the bot should stop executing. When end_time is reached, the bot will leave all positions intact, it will not open/close any of them.

label	
string
A label that the bot will add to all orders for easy identification.

start_time
required
number
Timestamp indicating when the bot was created.

stop_time	
number
Timestamp indicating when the bot stopped working due to specified stop_reason.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
SGSL (object) or OCQ (object) or Levels (object) or Grid (object) or DHedge (object) or DFollow (object) (Bot)
One of SGSLOCQLevelsGridDHedgeDFollow
bot_id
required
string
Individually identifies this bot instance. You can use it to cancel this specific one.

status
required
string
Enum: "active" "stopped"
stop_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "end_time" "instrument_deactivated" "margin_breach" "admin_cancel" "conflict" "strategy" "self_trade_prevention"
The reason why the bot stopped executing.

strategy
required
string
equal to "sgsl"

instrument_name
required
string
Name of the instrument.

signal
required
string
Enum: "last" "index" "mark"
entry_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

target_position
required
number
The target position to maintain in the subaccount if signal price is above entry_price. See the bot strategies section for more explanation.

exit_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

exit_position
required
number
The target position to maintain in the subaccount if signal price is below exit_price. See the bot strategies section for more explanation.

max_slippage	
number
Maximum slippage per trade, expressed as % of the traded instruments mark price.

end_time
required
number
Timestamp when the bot stops executing, cancelling its orders and leaving all positions of the subaccount intact.

start_time
required
number
Timestamp indicating when the bot was created.

stop_time	
number
Timestamp indicating when the bot stopped working due to specified stop_reason.

label	
string
A label that the bot will add to all orders for easy identification.

realized_pnl
required
number
Realized P&L made by this bot since the start.

fee
required
number
Trade fees by this bot.

average_price	
number
Average entry price of the position (if any).

position_size	
number
Position size (if any).

mark_price_at_stop	
number
Mark price of the bot instrument at the moment the bot was stopped.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/create_bot",
"params": {
"strategy": "sgsl",
"instrument_name": "BTC-PERPETUAL",
"signal": "index",
"entry_price": 100050,
"target_position": 0.2,
"exit_price": 100000,
"exit_position": 0,
"end_time": 1740064912
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"strategy": "sgsl",
"status": "active",
"bot_id": "0000000035832FDE",
"instrument_name": "BTC-PERPETUAL",
"signal": "index",
"entry_price": 100050,
"target_position": 0.2,
"exit_price": 100000,
"exit_position": 0,
"end_time": 1740064912,
"start_time": 1740064912,
"stop_time": 1740064912
}
}
Cancel a bot

rpc
private/cancel_bot
Cancel a specific bot instance.

Request Body schema: application/json
method
required
string
Value: "private/cancel_bot"
id	
object
Your request id, optional.

params
required
object
bot_id
required
string
The bot_id returned when creating the bot, or calling private/bots.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/cancel_bot",
"params": {
"bot_id": "string"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
Cancel all bots

rpc
private/cancel_all_bots
Cancel all bots of this subaccount

Request Body schema: application/json
method
required
string
Value: "private/cancel_all_bots"
id	
object
Your request id, optional.

params
required
null (Null)
Represents a null value.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
{
"method": "private/cancel_all_bots",
"params": null
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
Notifications
Notifications inbox

rpc
private/notifications_inbox
This method returns a list of latest notifications that were sent to the current user. The list only contains items for which the inbox preference is set` (either in user preferences, or by default).

Request Body schema: application/json
method
required
string
Value: "private/notifications_inbox"
id	
object
Your request id, optional.

params
required
object
limit	
integer
Default: 1000
Max results to return.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (Notifications)
notifications	
Array of objects
List of notifications ordered from newest to oldest.

Array 
id
required
string
Unique notification ID.

time
required
number
Time of notification (Unix timestamp).

category
required
string
Notification category (see API description / Notifications).

title
required
string
Human-readable title for the notification.

message
required
string
Human-readable message for the notification.

display_type
required
string
Enum: "success" "failure" "info" "warning" "critical"
Specifies what style to use for notification display.

read
required
boolean
set to true if notification was marked as read.

account_name	
string
Optional account name, only present if the notification is related to an account.

account_number	
string
Optional account number only present if the notification is related to an account.

popup
required
boolean
User preference - show popup for this notification

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/notifications_inbox",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"notifications": [
{
"id": "00000000000000A3",
"time": 1630069885.130461,
"category": "risk",
"title": "Margin Requirements",
"message": "Portfolio of account foo-123 breached initial margin requirements.",
"display_type": "warning",
"read": false,
"account_name": "foo-123",
"account_number": "A123456789",
"popup": true
}
]
}
}
Marking notification as read

rpc
private/mark_inbox_notification_as_read
Mark a notification as read

Request Body schema: application/json
method
required
string
Value: "private/mark_inbox_notification_as_read"
id	
object
Your request id, optional.

params
required
object
notification_id
required
string
ID of the notification to mark.

read	
boolean
Default: true
Set to true to mark as read, false to mark as not read.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/mark_inbox_notification_as_read",
"params": {
"notification_id": "00000000000000A3"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
Market making
Send a mass quote

rpc
private/mass_quote
Send multiple quotes, where quotes will replace earlier quotes on the same instrument.

Request Body schema: application/json
method
required
string
Value: "private/mass_quote"
id	
object
Your request id, optional.

params
required
object
quotes
required
Array of objects (DoubleSidedQuote)
List of quotes (maximum 100).

Each item is a double-sided quotes array on a single instrument. A quotes array atomically replaces a previous quotes array. Both bid and ask price may be specified. If either bid or ask is not specified, that side is not replaced or removed. If a double-sided quotes array for an instrument that was specified in an earlier call is omitted from the next call, these quotes are not removed or replaced.

When a side quotes array is specified, any omitted previous quotes will be removed. To remove all quotes on a side, send an empty quotes array.

Sending a quote with the exact same price and amount as in the previous call will not replace the quote, thus preserving the quote's priority.

Mass quoting allows for a maximum of 10 level quotes on each side on the instrument.

Note that market maker protection must have been configured for the instrument's product group, and both bid and ask amount must not exceed the most recent protection configuration amount.

Array 
i
required
string
instrument name

b	
Array of Multi-level quotes (items) or Single-level quote (object) (MassQuoteSingleLevelQuote)
One of Multi-level quotesSingle-level quote
[ 0 .. 10 ] items
Array ([ 0 .. 10 ] items)
[0]	
number
Limit price.

[1]	
number
Amount; set to zero to delete quote.

a	
Array of Multi-level quotes (items) or Single-level quote (object) (MassQuoteSingleLevelQuote)
One of Multi-level quotesSingle-level quote
[ 0 .. 10 ] items
Array ([ 0 .. 10 ] items)
[0]	
number
Limit price.

[1]	
number
Amount; set to zero to delete quote.

label	
string
Optional user label to apply to every quote side.

post_only	
boolean
If set, price may be widened so it will not cross an existing order in the book. If the adjusted price for any bid falls at or below zero where not allowed, then that side will be removed with delete reason 'immediate_cancel'.

reject_post_only	
boolean
This flag is only effective in combination with post_only. If set, then instead of adjusting the order price, the order will be cancelled with delete reason 'immediate_cancel'. The combination of post_only and reject_post_only is effectively a book-or-cancel order.

stp_level	
string
Enum: "customer" "account" "disabled"
The self trade prevention level override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is customer and not configurable.

stp_action	
string
Enum: "cancel_aggressive_partial_fill" "cancel_aggressive_no_fill"
The self trade prevention action override for this order. Needs configuration to be enabled, see the Self trade prevention section for more explanation.

The default is cancel_aggressive_partial_fill and not configurable.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object (DoubleSidedQuoteResult)
n_fail
required
number
The number of individual quote sides failed to insert.

n_success
required
number
The number of individual quote sides successfully replaced or deleted.

errors
required
Array of objects
A collection of errors assembled during execution.

Array 
code	
number
Error code.

message	
string
Error message.

side	
string
Optional quote side.

price	
number
Optional price level.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/mass_quote",
"params": {
"quotes": [
{
"i": "BTC-10SEP21-48000-C",
"b": [],
"a": []
},
{
"i": "BTC-10SEP21-53000-C",
"a": []
}
]
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": {
"n_success": 4,
"n_fail": 0,
"errors": [ ]
}
}
Bulk cancel mass quotes across all sessions

rpc
private/cancel_mass_quote
Cancel mass quotes across all sessions. If a product is set, only the quotes on that product will be cancelled. Otherwise all quotes are cancelled.

Note that market maker protection groups are reset and must be re-initialised.

Request Body schema: application/json
method
required
string
Value: "private/cancel_mass_quote"
id	
object
Your request id, optional.

params
required
object
product	
string
If set, only the mass quotes on this product will be cancelled.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/cancel_mass_quote",
"params": {
"product": "FBTCUSD"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
Market maker protection configuration

rpc
private/set_mm_protection
Set the maximum trading amount for mass quote orders on a particular product in this session. After this amount is executed, the remaining mass quotes on the product in this session are cancelled.

These settings affect only a particular protection group (protection set for a product group within a session).

Note that the amount can be overshot under certain conditions.

See Mass quoting and market maker protection section for more information.

Request Body schema: application/json
method
required
string
Value: "private/set_mm_protection"
id	
object
Your request id, optional.

params
required
object
product
required
string
Product group ('F' + underlying or 'O' + underlying).

trade_amount
required
number
Total amount of mass quote orders (number of contracts) on this protection group that is allowed to be executed before the remaining mass quotes are canceled. The value must be lower or equal to the quote_amount.

quote_amount
required
number
Maximum amount of a single quote on this protection group. Any orders larger than this will be rejected. Mass quote margin requirements are calculated for this amount.

amount	
number
Deprecated. Overwrites 'trade_amount' and 'quote_amount' with this value.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/set_mm_protection",
"params": {
"product": "FBTCUSD",
"amount": 10
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
Wallet
Verify if withdrawal is possible

rpc
private/verify_withdrawal
This method is subject to withdrawal permissions.

Request Body schema: application/json
method
required
string
Value: "private/verify_withdrawal"
id	
object
Your request id, optional.

params
required
object
asset_name
required
string
Asset name.

amount
required
number
Amount to withdraw.

target_address
required
string
Target address.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
available_margin
required
number
Projected available margin after the withdrawal.

required_margin
required
number
Projected required margin after the withdrawal.

fee	
number
Amount of fees withheld.

fee_asset	
string
Asset in which the withdrawal fees are withheld.

error	
object
In case such withdrawal is not possible, this object contains an error code and an error message describing why. Otherwise, error is returned as null.

code	
number
Error code.

message	
string
Error message.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/verify_withdrawal",
"params": {
"asset_name": "USDT",
"amount": 100,
"target_address": "1234xy2kgdygjrsqtzq2n0yrf2493p83kkfjhx01234"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"available_margin": 10045,
"required_margin": 5096,
"fee": 25,
"fee_asset": "USDT",
"error": null
}
}
Withdraw assets

rpc
private/withdraw
This method is subject to withdrawal permissions.

Request Body schema: application/json
method
required
string
Value: "private/withdraw"
id	
object
Your request id, optional.

params
required
object
asset_name
required
string
Asset name.

amount
required
number
Amount to withdraw.

target_address
required
string
Target address.

label	
string
Optional label to attach to the withdrawal request.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/withdraw",
"params": {
"asset_name": "USDT",
"amount": 100,
"target_address": "1234xy2kgdygjrsqtzq2n0yrf2493p83kkfjhx01234",
"label": "For my new yacht"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
Withdrawals

rpc
private/crypto_withdrawals
List of withdrawals from the selected account. Includes all withdrawals: pending, executed, rejected etc.

Request Body schema: application/json
method
required
string
Value: "private/crypto_withdrawals"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
Array of objects
Array 
currency
required
string
Withdrawn currency symbol.

amount
required
number
Amount of currency withdrawn.

target_address
required
string
Target address, specific to blockchain used.

blockchain	
string
Blockchain used or this transaction.

transaction_hash	
string
Transaction hash on the used blockchain.

create_time
required
number
Time when this withdrawal was requested (Unix timestamp).

label	
string
Optional label attached to the withdrawal request.

state
required
string
Enum: "pending" "awaiting_confirmation" "executing" "executed" "rejected"
Withdrawal transaction status.

remark	
string
Remark added by the exchange.

fee	
number
Amount of fees withheld.

fee_asset	
string
Asset in which the withdrawal fees are withheld.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/crypto_withdrawals",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": [
[
{
"currency": "ETH",
"amount": 0.1,
"target_address": "0x12345767c60fb7867B85aA35F72411234",
"blockchain": "ethereum",
"transaction_hash": "0x123415543674a854df02f4ef8f5dbc04ee01b744ac0bc4123456",
"create_time": 1632732292.7792032,
"label": "It's not much, but it's honest work",
"state": "executed",
"remark": "COMPLETED - CONFIRMED",
"fee": 25,
"fee_asset": "USDT"
}
]
]
}
Deposits

rpc
private/crypto_deposits
Pending and confirmed deposits for the selected account.

Request Body schema: application/json
method
required
string
Value: "private/crypto_deposits"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
confirmed
required
Array of objects (Deposit)
List of confirmed deposits.

Array 
currency
required
string
Deposited currency symbol.

amount
required
number
Amount of currency deposited.

blockchain
required
string
Blockchain used or this transaction.

transaction_hash
required
string
Transaction hash on the used blockchain.

transaction_timestamp
required
number
Time when this transaction was created (Unix timestamp).

status
required
string
Enum: "unconfirmed" "confirmed"
Deposit transaction status.

confirmations	
number
Number of confirmations. Optional, omitted when none.

unconfirmed
required
Array of objects (Deposit)
List of unconfirmed deposits.

Array 
currency
required
string
Deposited currency symbol.

amount
required
number
Amount of currency deposited.

blockchain
required
string
Blockchain used or this transaction.

transaction_hash
required
string
Transaction hash on the used blockchain.

transaction_timestamp
required
number
Time when this transaction was created (Unix timestamp).

status
required
string
Enum: "unconfirmed" "confirmed"
Deposit transaction status.

confirmations	
number
Number of confirmations. Optional, omitted when none.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/crypto_deposits",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"confirmed": [
{
"currency": "ETH",
"blockchain": "ethereum",
"transaction_hash": "0x1235467675550cad841c8b410f78e1d1d7cc256b6803234234534534",
"transaction_timestamp": 1632217370,
"amount": 0.059,
"status": "confirmed",
"confirmations": 6
}
],
"unconfirmed": [ ]
}
}
Bitcoin deposit address

rpc
private/btc_deposit_address
Get Bitcoin deposit address

Request Body schema: application/json
method
required
string
Value: "private/btc_deposit_address"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
string
Deposit address for the selected account for Bitcoin.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/btc_deposit_address",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
{
"result": "12345yr6zpguy7nrc8md63ykn5h9xr4vryl99r3wpz"
}
Ethereum deposit address

rpc
private/eth_deposit_address
Get Ethereum deposit address

Request Body schema: application/json
method
required
string
Value: "private/eth_deposit_address"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
string
Deposit address for the selected account for coins on Ethereum network.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/eth_deposit_address",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
{
"result": "0x1235467675550cad841c8b410f78e1d1d7cc256b6803234234534534"
}
Verify internal transfer

rpc
private/verify_internal_transfer
Verify if internal transfer of assets and/or positions from source (currently selected) to destination account is possible. Does not perform the transfer itself.

Transfers are subject to margin checks.

A transfer cannot result in an account breaching margin requirements. This applies to both source and destination accounts.

If either of the accounts is already in margin breach state, the transfer is only allowed if it results in an increase of available margin on that account. The other account must not breach margin requirement as a result of the transfer. This allows transferring assets and/or positions from an account with enough extra margin to an account that was margin called.

Each transfer can contain multiple asset and position transfers. It is checked for margin requirements as a single transaction. It is possible to specify negative amounts for transferred assets and positions, which results in a reverse direction of transfer (i.e. from destination account to the source one). This allows performing asset/position exchange operations, and is helpful when a leg of such operation alone would result in a margin requirements breach.

Request Body schema: application/json
method
required
string
Value: "private/verify_internal_transfer"
id	
object
Your request id, optional.

params
required
object
destination_account_number
required
string
Destination account number.

assets	
Array of objects
Array 
asset_name
required
string
Asset name

amount
required
number
Amount to transfer. Use a negative value to transfer in reverse direction.

positions	
Array of objects
Array 
instrument_name
required
string
Instrument feedcode.

amount
required
number
Amount to transfer. Use a negative value to transfer in reverse direction.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
source_available_margin
required
number
Available margin in the source account after the transfer is performed.

source_required_margin
required
number
Required margin in the source account after the transfer is performed.

destination_available_margin
required
number
Available margin in the destination account after the transfer is performed.

destination_required_margin
required
number
Required margin in the destination account after the transfer is performed.

error	
object
Only present when the transfer is not possible, in which case it describes the error such transfer would result in.

Note: this is different from the top level result/error in the response.

code
required
number
Error code

message
required
string
Error message

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/verify_internal_transfer",
"params": {
"destination_account_number": "A123456789",
"assets": [
{
"asset_name": "BTC",
"amount": "1"
}
]
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"destination_available_margin": 10040724.221942985,
"destination_required_margin": 13021.147166650373,
"source_available_margin": 11987398962.727953,
"source_required_margin": 179870275.06509292,
"error": {
"code": 27,
"message": "asset 'BTC': insufficient funds for operation"
}
}
}
Internal transfer

rpc
private/internal_transfer
Transfer assets and/or positions from source (currently selected) to destination account.

Transfers are subject to margin checks. Please see private/verify_internal_transfer method description for more information.

Request Body schema: application/json
method
required
string
Value: "private/internal_transfer"
id	
object
Your request id, optional.

params
required
object
destination_account_number
required
string
Destination account number.

assets	
Array of objects
Array 
asset_name
required
string
Asset name

amount
required
number
Amount to transfer. Use a negative value to transfer in reverse direction.

positions	
Array of objects
Array 
instrument_name
required
string
Instrument feedcode.

amount
required
number
Amount to transfer. Use a negative value to transfer in reverse direction.

label	
string
Optional label attached to the transfer.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
null (Null)
Represents a null value.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "private/internal_transfer",
"params": {
"destination_account_number": "A123456789",
"assets": [
{
"asset_name": "BTC",
"amount": "1"
}
]
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"id": { },
"result": null
}
System info
System info

rpc
public/system_info
Get system info

Request Body schema: application/json
method
required
string
Value: "public/system_info"
id	
object
Your request id, optional.

params
required
object (EmptyObject)
Empty object.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
environment
required
string
Enum: "testnet" "production"
api_version	
string
Current API version.

banners
required
Array of objects (Banner)
List of banners currently shown.

Banners are 'sticky' notifications visible to all users of the exchange. They are used e.g. for maintenance announcements etc.

Array 
id	
number
The id of this banner.

time
required
number
Time when this banner was posted (Unix timestamp).

severity
required
string
Enum: "info" "warning" "critical"
Severity of the banner message. Used to choose appropriate styling for banner display.

title	
string
Optional title of the banner.

message
required
string
Message text to be displayed in the banner.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/system_info",
"params": { }
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"environment": "production",
"api_version": "2.0.0",
"banners": [
{
"id": 1,
"time": 1630059868.4145653,
"severity": "info",
"title": "Important information",
"message": "Starting next week we are lowering our fees by 10%."
}
]
}
}
Historical data
Mark price historical data.

rpc
public/mark_price_historical_data
Returns mark price historical data in the specified interval and resolution in OHLC format.

Request Body schema: application/json
method
required
string
Value: "public/mark_price_historical_data"
id	
object
Your request id, optional.

params
required
object
instrument_name
required
string
Feedcode of the instrument (e.g. BTC-PERPETUAL).

from
required
number
Start time (Unix timestamp).

to
required
number
End time (Unix timestamp) (exclusive).

resolution
required
string
Enum: "1m" "5m" "15m" "30m" "1h" "1d" "1w"
Each data point will be aggregated using OHLC according to the specified resolution.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
instrument_type
required
string
Enum: "perpetual" "future" "combination" "option"
Instrument type the historical data corresponds to.

mark
required
Array of Perpetuals (items) or Array of Futures and combinations (items) or Array of Options (items)
Array of mark price data points. Each mark price data point is an array of mark price data in OHLC format followed by an optional array of top of book data. Top of book data is returned only for 1m resolution and set to null otherwise.

Note that the inner array format depends on the instrument_type flag.

Note also that the top bid and top ask data can be set to null for the 1m resolution if there was no quote at the start of the correspondent minute interval.

One of PerpetualsFutures and combinationsOptions
Array 
[0]	
number
Time (Unix timestamp) of the start of the data point.

[1]	
number
Open (first) value of the data point

[2]	
number
High (max) value of the data point.

[3]	
number
Low (min) value of the data point.

[4]	
number
Close (last) value of the data point.

[5]	
number
Funding payment during the interval represented by the data point.

[6]	
Array of items = 4 items
Top of book data, null for the resolutions other than 1 minute.

[0]	
number
Top bid price, or null if bid order book is empty.

[1]	
number
Top bid size, or null if bid order book is empty.

[2]	
number
Top ask price, or null if ask order book is empty.

[3]	
number
Top ask size, or null if ask order book is empty.

no_data	
boolean
Is set if there is no data for this instrument in or before the requested interval.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/mark_price_historical_data",
"params": {
"instrument_name": "string",
"from": 0,
"to": 0,
"resolution": "1m"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"instrument_type": "perpetual",
"mark": [
[
1736363460,
94700,
94701,
94445,
94409,
0.0002
],
[
1736363520,
94409,
94600,
94408,
94500,
-0.00011
]
]
}
}
Index price historical data.

rpc
public/index_price_historical_data
Returns index price historical data in the specified interval and resolution in OHLC format.

Request Body schema: application/json
method
required
string
Value: "public/index_price_historical_data"
id	
object
Your request id, optional.

params
required
object
index_name
required
string
Index name (e.g. BTCUSD, ETHUSD).

from
required
number
Start time (Unix timestamp).

to
required
number
End time (Unix timestamp) (exclusive).

resolution
required
string
Enum: "1m" "5m" "15m" "30m" "1h" "1d" "1w"
Each data point will be aggregated using OHLC according to the specified resolution.

Responses
default
Response Schema: application/json
One of SuccessError
id	
object
Your request id, or null if not supplied.

result
required
object
index
required
Array of items[ items = 6 items ]
Array of arrays of index price data points in OHLC format.

Array 
[0]	
number
Time (Unix timestamp) of the start of the data point.

[1]	
number
Open (first) value of the data point

[2]	
number
High (max) value of the data point.

[3]	
number
Low (min) value of the data point.

[4]	
number
Close (last) value of the data point.

no_data	
boolean
Is set if there is no data for this instrument in or before the requested interval.

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"method": "public/index_price_historical_data",
"params": {
"index_name": "string",
"from": 0,
"to": 0,
"resolution": "1m"
}
}
Response samples
default
Content type
application/json
Example

Success
Success

Copy
Expand allCollapse all
{
"result": {
"index": [
[
1736363460,
94700,
94701,
94445,
94409
],
[
1736363520,
94409,
94600,
94408,
94500
]
]
}
}
Market data
Order book
Channel name: book.<instrument>.<grouping>.<nlevels>.<delay>

Subscribes to aggregated book updates and trade ticks on a single instrument or a combination.

Combination order books do not represent combination orders inserted by customers. Instead, each level in the virtual combination order book represents a possible proportional fill at a specific price for the whole combination that can be matched against orders in the outright books that correspond to the combination legs. Combination order books are updated in real time when outright order books they depend on change.

Channel name parameters:

instrument - For single instrument order books this is the instrument name, e.g. "BTC-PERPETUAL".
For combinations, this is a string that specifies combination legs in the following format: [<instrument_name>:<quantity>,<instrument_name>:<quantity>,...].

For example, "[BTC-30MAY25-93000-C:-1,BTC-30MAY25-80000-C:1]".

You can only subscribe to the books of combinations that are allowed for combination orders.

There must be at least two and at most four legs specified. All leg instruments must be distinct. Other constraints apply, please check trading information page on combination orders.

grouping - To group book levels by price, pass a USD value aligned to instrument or combination price tick size. Pass none for no grouping.
nlevels - Number of levels you want to see, or all.
delay - Minimum interval between feeds, possible value is one of 100ms, 200ms, 500ms, 1000ms, 5000ms, 60000ms or raw.
Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "book.<instrument>.<grouping>.<nlevels>.<delay>"
notification
required
object
Channel-specific content

trades	
Array of arrays
List of [price, amount, direction, timestamp, implied_taker]. Note that the snapshot of this feed may contain older trades that happened since the last restart of the gateway.

The implied_taker is a boolean flag, set to true when the actual taker trade happened on another order book, and the maker trade on this book is the result of implied matching.

Trades are not sent for combination order books.

bid_changes	
Array of arrays
List of price level updates (price, amount, outright amount) for buy orders, amount 0 means level is now empty.

For combination order books, price and amount refer to the price and amount per unit of the combination.

ask_changes	
Array of arrays
List of price level updates (price, amount, outright amount) for sell orders, amount 0 means level is now empty.

For combination order books, price and amount refer to the price and amount per unit of the combination.

total_bid_amount	
number
The total amount of bid orders across all levels.

total_ask_amount	
number
The total amount of ask orders across all levels.

time	
number
Time of the last recorded update to this order book (Unix timestamp).


Copy
Expand allCollapse all
{
"channel_name": "book.<instrument>.<grouping>.<nlevels>.<delay>",
"notification": {
"trades": [
[
9120.5,
15,
"buy",
156789.103,
false
],
[
9121,
30,
"buy",
156789.123,
false
]
],
"bid_changes": [
[
9120.5,
0,
0
],
[
9121,
54,
53
]
],
"total_bid_amount": 45,
"total_ask_amount": 30,
"time": 1683901254.785744
}
}
Ticker
Channel name: ticker.<instrument>.<delay>

Subscribes to a ticker feed for a single instrument or a combination.

Mark price of a combination is the quantity-weighted sum of mark prices of the leg instruments.

Best bid and best ask for combinations represent top levels of a corresponding virtual combination order book. Combination order books do not represent combination orders inserted by customers. Instead, each level in the virtual combination order book represents a possible proportional fill at a specific price for the whole combination that can be matched against orders in the outright books that correspond to the combination legs. Combination order books are updated in real time when outright order books they depend on change.

Channel name parameters:

instrument - For single instrument tickers this is the instrument name, e.g. "BTC-PERPETUAL".
For combinations, this is a string that specifies combination legs in the following format: [<instrument_name>:<quantity>,<instrument_name>:<quantity>,...].

For example, "[BTC-30MAY25-93000-C:-1,BTC-30MAY25-80000-C:1]".

You can only subscribe to combinations that are allowed for combination orders.

There must be at least two and at most four legs specified. All leg instruments must be distinct. Other constraints apply, please check trading information page on combination orders.

delay - Minimum interval between feeds, possible value is one of 100ms, 200ms, 500ms, 1000ms, 5000ms, 60000ms or raw.
Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "ticker.<instrument>.<delay>"
notification
required
object (Ticker)
Channel-specific content

best_bid_price	
number
Price of the best (highest) bid in the orderbook, or null if the orderbook is empty.

best_bid_amount	
number
Size of best bid, or null if the orderbook is empty.

best_ask_price	
number
Price of best (lowest) ask in the orderbook, or null if the orderbook is empty.

best_ask_amount	
number
Size of best ask, or null if the orderbook is empty.

last_price	
number
Price of last trade, or null if no trades have been registered yet.

Not included for combinations.

mark_price	
number
Current mark price.

mark_timestamp	
number
The unix timestamp when the price was marked.

iv	
number
Implied volatility calculated at time of marking.

Only included for options. Not included for combinations.

delta	
number
Delta calculated at time of marking.

Not included for combinations.

index	
number
Index price at time of marking.

forward	
number
Forward price at time of marking.

Only included for options.

volume_24h	
number
Total volume traded over the last 24 hours.

Not included for combinations.

value_24h	
number
Total value traded over the last 24 hours.

Not included for combinations.

low_price_24h	
number
Lowest price in the last 24 hours.

Not included for combinations.

high_price_24h	
number
Highest price in the last 24 hours.

Not included for combinations.

change_24h	
number
Difference in price between the first and the last trades in the last 24 hours, null if there were no trades.

Not included for combinations.

collar_low	
number
Current price collar low (checks new asks)

collar_high	
number
Current price collar high (checks new bids)

open_interest	
number
Total number of outstanding unsettled contracts.

Not included for combinations.

funding_rate	
number
Current rate at which long position pays and short position earns, in funding interval.

Only included for perpetuals.

funding_mark	
number
Funding value of a single contract long position since last settlement.

Only included for perpetuals.

realised_funding_24h	
number
Total funding accumulated for a single contract long position over the last 24 hours.

Only included for perpetuals.

average_funding_rate_24h	
number
Average funding rate for the last 24 hours.

Only included for perpetuals.


Copy
Expand allCollapse all
{
"channel_name": "ticker.<instrument>.<delay>",
"notification": {
"mark_price": 47238.64143906124,
"mark_timestamp": 946684800,
"best_bid_price": 47240,
"best_bid_amount": 0.4,
"best_ask_price": 47260,
"best_ask_amount": 1,
"delta": 1,
"volume_24h": 0,
"value_24h": 0,
"open_interest": 123.456
}
}
Ticker (lightweight payload)
Channel name: lwt.<instrument>.<delay>

Similar to ticker.<instrument>.<delay>, but subscribes to a lightweight ticker consisting only of best bid and ask, mark price, volatility and last trade price. Other pricing elements can be derived from the base price feed.

Channel name parameters:

instrument - For single instrument tickers this is the instrument name, e.g. "BTC-PERPETUAL".
For combinations, this is a string that specifies combination legs in the following format: [<instrument_name>:<quantity>,<instrument_name>:<quantity>,...].

For example, "[BTC-30MAY25-93000-C:-1,BTC-30MAY25-80000-C:1]".

You can only subscribe to combinations that are allowed for combination orders.

There must be at least two and at most four legs specified. All leg instruments must be distinct. Other constraints apply, please check trading information page on combination orders.

delay - Minimum interval between feeds, possible value is one of 100ms, 200ms, 500ms, 1000ms, 5000ms, 60000ms or raw.
Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "lwt.<instrument>.<delay>"
notification
required
object
Channel-specific content

b	
Array of items = 3 items
Best bid (if any).

[0]	
number
Price

[1]	
number
Amount

[2]	
number
Outright-only amount

a	
Array of items = 3 items
Best ask (if any).

[0]	
number
Price

[1]	
number
Amount

[2]	
number
Outright-only amount

m	
number
Mark price.

v	
number
Mark volatility.

Only included for options. Not included for combinations.

l	
number
Price of last trade (if any).

Not included for combinations.


Copy
Expand allCollapse all
{
"channel_name": "lwt.<instrument>.<delay>",
"notification": {
"b": [
47240,
0.4,
0.4
],
"a": [
47260,
1,
0.9
],
"l": 47252.64143906124,
"m": 65536.16
}
}
Recent trades
Channel name: recent_trades.<target>.<category>

Subscribes to notifications about recent trades of a specific category. The first notification after subscription contains a snapshot of a certain number of last known trades. Subsequent notifications contain new trades. Note that this subscription has a slight delay compared to order book subscriptions (book.*), but the snapshot functionality is more reliable.

Channel name parameters:

target - Either underlying (e.g. BTCUSD), or instrument name (e.g. BTC-PERPETUAL).
category - Category that serves as a filter for which instruments' trades to include in the feed. Can be one of the following values:
single: single instrument. Only valid for instrument recent trades. I.e. recent_trades.BTC-11MAY22-32400-C.single is valid but recent_trade.BTCUSD.single is not valid.
all: all instruments in underlying. Only valid for underlying recent trades. I.e. recent_trades.BTCUSD.all is valid but recent_trade.BTC-11MAY22-32400-C.all is not valid.
options: all options in underlying. Only valid for underlying recent trades. I.e. recent_trades.BTCUSD.options is valid but recent_trade.BTC-11MAY22-32400-C.options is not valid.
future_rolls: all combination instruments in underlying that represent rolls between two futures or a future and a perpetual. Only valid for underlying recent trades. I.e. recent_trades.BTCUSD.future_rolls is valid but recent_trade.BTC-11MAY22-32400-C.future_rolls is not valid.
Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "recent_trades.<target>.<category>"
notification
required
Array of arrays
Array of trades, each item is an array with the following values: [price, size, side ("buy" or "sell"), timestamp, instrument_name, implied_taker].

The implied_taker is a boolean flag, set to true when the actual taker trade happened on another order book, and the maker trade on this book is the result of implied matching.


Copy
Expand allCollapse all
{
"channel_name": "recent_trades.<target>.<category>",
"notification": [
[
400,
1,
"buy",
1652187265.515,
"BTC-11MAY22-32400-C",
false
]
]
}
Index price
Channel name: price_index.<underlying>

Subscribes to index price stamps.

Channel name parameters:

underlying - Underlying is e.g. BTCUSD.
Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "price_index.<underlying>"
notification
required
object (Index)
Channel-specific content

index_name
required
string
price
required
number
timestamp
required
number
The unix timestamp when the index price was recorded in the database.

expiration_print_average	
number
The average price so far over the current expiration, if any.

expiration_progress	
number
A number between 0.0 and 1.0 indicating the progress of the current expiration.

expected_expiration_price	
number
If expiration is in progress, and the index price will not change any more, this is the expiration price. Equals expiration_progress * expiration_print_average + (1 - expiration_progress) * price.

previous_settlement_price	
number
The last known settlement price (expiration price, underlying delivery price).


Copy
Expand allCollapse all
{
"channel_name": "price_index.<underlying>",
"notification": {
"index_name": "BTCUSD",
"price": 47389.10833333334,
"timestamp": 946684800
}
}
Underlying statistics
Channel name: underlying_statistics.<underlying>

Subscribes to statistics of a single underlying.

Channel name parameters:

underlying - Underlying is e.g. BTCUSD.
Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "underlying_statistics.<underlying>"
notification
required
object
Channel-specific content

trade_volume_24h	
number
Total amount traded in 24 hours, including futures and options.

option_volume_24h	
number
Total amount of options traded in the past 24 hours.

delta_one_volume_24h	
number
Total amount of futures traded in the past 24 hours.

trade_value_24h	
number
Total underlying value traded in 24 hours. This is the sum of (amount * index price at time of trade).

option_value_24h	
number
Total option value traded in 24 hours. This is the sum of (amount * index price at time of trade).

delta_one_value_24h	
number
Total delta one value traded in 24 hours. This is the sum of (amount * index price at time of trade).

open_interest	
object
Total count of outstanding contracts statistics.

expirations	
Array of objects
Total count of outstanding contracts statistics per expiration date.

Array 
expiration_timestamp	
integer
Expiration time as Unix timestamp (seconds).

expiry_date	
string
Expiration date in ISO format (YYYY-mm-dd).

call	
number
Total count of outstanding unsettled call options for the given expiration and underlying.

put	
number
Total count of outstanding unsettled put options for the given expiration and underlying.

option	
number
Total count of outstanding unsettled options for the given expiration and underlying.

future	
number
Total count of outstanding unsettled future contracts for the given expiration and underlying.

totals	
object
call
required
number
Total count of outstanding unsettled call options for the given underlying.

put
required
number
Total count of outstanding unsettled put options for the given underlying.

option
required
number
Total count of outstanding unsettled options for the given underlying.

future
required
number
Total count of outstanding unsettled future contracts for the given underlying.

delta_one
required
number
Total count of outstanding unsettled delta one (future and perpetual) contracts for the given underlying.


Copy
Expand allCollapse all
{
"channel_name": "underlying_statistics.<underlying>",
"notification": {
"trade_volume_24h": 53.159,
"option_volume_24h": 50,
"delta_one_volume_24h": 3.159,
"trade_value_24h": 1554041.6949,
"option_value_24h": 1500000.6,
"delta_one_value_24h": 54041.0949,
"open_interest": {
"expirations": [
{},
{}
],
"totals": {
"call": 357.9,
"put": 113.41,
"option": 471.31,
"future": 555.777,
"delta_one": 811.789
}
}
}
}
Forward price
Channel name: base_price.<underlying>.<expiration>

Subscribes to per-expiration forward prices. If a future exists with this expiration date, the price equals the future's mark price. Otherwise, if one or more options exist with this expiration date, the price will be the interpolated forward price as used in our marking process. If no instrument with this expiration exists, the subscription will fail.

Channel name parameters:

underlying - Underlying is e.g. BTCUSD.
expiration - Expiration date in YYYY-MM-DD format.
Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "base_price.<underlying>.<expiration>"
notification
required
object
Channel-specific content

base_name
required
string
Instrument name of future, or "synthetic".

price
required
number
Forward price of the expiration.

index
required
number
Index price of the underlying of the instrument.

index_delta	
number
Before expiration, Thalex linearly scales the deltas of the expiring instruments to zero, over a time window. This number represents how far into this process the expiration is (i.e. delta used for margining = index_delta * actual delta of the instrument).


Copy
Expand allCollapse all
{
"channel_name": "base_price.<underlying>.<expiration>",
"notification": {
"base_name": "BTC-24SEP21",
"price": 47433.658803891754,
"index": 47172.69166666667,
"index_delta": 1
}
}
Instruments
Channel name: instruments

Subscribes to changes in active instruments.

New instruments may be added when others expire, or intraday when the index price changes significantly. Instruments are removed when they expire.

This subscription immediately responds with a notification for all currently active instruments.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "instruments"
notification
required
Array of objects or objects
Channel-specific content

Array 
One of objectobject
added	
object (Instrument)
instrument_name	
string
product	
string
E.g. "FBTCUSD", "OBTCUSD".

tick_size	
number
Price alignment.

volume_tick_size	
number
Amount alignment.

min_order_amount	
number
Minimum order amount for this instrument. This value is always greater or equal to volume_tick_size.

If this value is greater than volume_tick_size, it is not possible to insert an order of a smaller amount, or amend an existing order to a smaller amount. However, orders in the books can have smaller remaining amounts as they get partially filled, down to the minimum of volume_tick_size.

underlying	
string
Related index, e.g. "BTCUSD".

type	
string
Enum: "perpetual" "future" "option" "combination"
option_type	
string
Enum: "call" "put"
expiry_date	
string
Expiration date in ISO format (YYYY-mm-dd).

expiration_timestamp	
integer
Expiration time as Unix timestamp (seconds).

strike_price	
number
Strike price of option.

base_currency	
string
Base currency for pricing (i.e. USD).

legs	
Array of objects
For combinations, array of objects with instrument_name and quantity.

Array 
instrument_name	
string
quantity	
integer
create_time	
number
Creation time (Unix timestamp).

settlement_price	
number
For expired instruments, the final settlement price.

settlement_index_price	
number
For expired instruments, the underlying delivery price.


Copy
Expand allCollapse all
{
"channel_name": "instruments",
"notification": [
{
"added": {
"instrument_name": "BTC-10SEP21-70000-C",
"product": "OBTCUSD",
"tick_size": 5,
"volume_tick_size": 0.1,
"min_order_amount": 0.1,
"underlying": "BTCUSD",
"type": "option",
"option_type": "call",
"expiry_date": "2021-09-10",
"expiration_timestamp": 1631260800,
"strike_price": 70000,
"base_currency": "USD",
"create_time": 1631250800.103645
}
}
]
}
Traded RFQs
Channel name: rfqs

Subscribed to traded RFQs. When subscribing, a snapshot will be sent containing recently traded RFQs.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "rfqs"
notification
required
Array of objects (Rfq)
Channel-specific content

Array 
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.


Copy
Expand allCollapse all
{
"channel_name": "rfqs",
"notification": [
{
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [
{}
],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {
"price": 0,
"amount": 0
},
"quoted_ask": {
"price": 0,
"amount": 0
},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
]
}
Index components
Channel name: index_components.<underlying>

Subscribes to the index price components channel.

Channel name parameters:

underlying - Underlying is e.g. BTCUSD.
Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "index_components.<underlying>"
notification
required
object
Channel-specific content

index_price	
number
Price of the index.

components	
object
Components that were used in calculating the index price. Code name of the source is mapped to its price.


Copy
Expand allCollapse all
{
"channel_name": "index_components.<underlying>",
"notification": {
"index_price": 20000,
"components": {
"coinbase": "19998,",
"bitstamp": 20002
}
}
}
System info
System events
Channel name: system

Subscribes to system and connection related events.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "system"
notification
required
object (SystemEvent)
Channel-specific content

event
required
string
Value: "reconnect"
Type of the system event.

reconnect: you receive this event when the WebSocket connection is about to be closed by the server and you need to open a new one. This can happen, for example, during exchange maintenance windows. The event is sent at least 10 seconds before the connection is closed.

Copy
Expand allCollapse all
{
"channel_name": "system",
"notification": {
"event": "reconnect"
}
}
Banners
Channel name: banners

Subscribes to changes in currently shown banners. Each notification contains full list of banners.

Banners are 'sticky' notifications visible to all users of the exchange. They are used e.g. for maintenance announcements etc.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "banners"
notification
required
Array of objects (Banner)
Channel-specific content

Array 
id	
number
The id of this banner.

time
required
number
Time when this banner was posted (Unix timestamp).

severity
required
string
Enum: "info" "warning" "critical"
Severity of the banner message. Used to choose appropriate styling for banner display.

title	
string
Optional title of the banner.

message
required
string
Message text to be displayed in the banner.


Copy
Expand allCollapse all
{
"channel_name": "banners",
"notification": [
{
"id": 1,
"time": 1630059868.4145653,
"severity": "info",
"title": "Important information",
"message": "Starting next week we are lowering our fees by 10%."
}
]
}
Accounting
Account orders
Channel name: account.orders

Subscribes to all active order changes. Notification value is a list of order status updates. Upon subscription, all current open orders are sent immediately, with status "existing".

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "account.orders"
notification
required
Array of objects (OrderStatus)
Channel-specific content

Array 
order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.


Copy
Expand allCollapse all
{
"channel_name": "account.orders",
"notification": [
{
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "buy",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
]
}
Account orders, persistent only
Channel name: account.persistent_orders

Subscribes to all active order changes on persistent (non-market-maker) orders only. Notification value is a list of order status updates. Upon subscription, all current open orders are sent immediately, with status "existing".

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "account.persistent_orders"
notification
required
Array of objects (OrderStatus)
Channel-specific content

Array 
order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.


Copy
Expand allCollapse all
{
"channel_name": "account.persistent_orders",
"notification": [
{
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "buy",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
]
}
Session orders
Channel name: session.orders

Subscribes to all active order changes, but only for orders that were inserted in the current WebSocket session. Notification value is a list of order status updates. Upon subscription, all current open orders are sent immediately, with status "existing".

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "session.orders"
notification
required
Array of objects (OrderStatus)
Channel-specific content

Array 
order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
time_in_force
required
string
Enum: "good_till_cancelled" "immediate_or_cancel"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

remaining_amount
required
number
Amount on this leg that remains in the book; if 0, order is now inactive.

Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

remaining_amount
required
number
Part of the order that remains in the book; if 0, order is now inactive.

For combination orders this specifies the amount of units of the combination remaining on a book. Note that the only time_in_force for combination orders currently supported is immediate_or_cancel. Therefore, combination orders will never remain on a book, and this field will always be zero.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
These are new fills related to this order status update, except if change_reason is existing, then the list will contain all known fills.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

change_reason
required
string
Enum: "existing" "insert" "amend" "cancel" "fill"
delete_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time	
number
Time when this order was closed or canceled (Unix timestamp). Omitted for orders that are still open.

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.

persistent
required
boolean
True if the order is a persistent order, false otherwise.


Copy
Expand allCollapse all
{
"channel_name": "session.orders",
"notification": [
{
"order_id": "1728379719872",
"time_in_force": "good_till_cancelled",
"instrument_name": "BTC-PERPETUAL",
"price": 45000,
"amount": 1.1,
"order_type": "limit",
"direction": "buy",
"filled_amount": 0,
"remaining_amount": 1.1,
"status": "open",
"fills": [ ],
"change_reason": "insert",
"insert_reason": "client_request"
}
]
}
Account trade history
Channel name: account.trade_history

Subscribes to trade history. Note that this feed is sent only after trades have been fully processed in the central database. For low-latency execution notifications, check the fills field in account.orders.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "account.trade_history"
notification
required
Array of objects (Trade)
Channel-specific content

Array 
trade_type	
string
Enum: "normal" "block" "combo" "amend" "delete" "internal_transfer" "expiration" "daily_mark" "rfq" "liquidation"
Type of the trade.

Note: as of API v2.31.0 we have stopped representing futures-style settlements as trades of daily_mark type. You might still get such trades in the history, but no new trades of daily_mark type will be created. To get information about daily marks, use private/daily_mark_history API endpoint.

trade_id	
string
order_id	
string
instrument_name	
string
direction	
string
Enum: "buy" "sell"
price	
number
Trade price.

amount	
number
Traded amount.

label	
string
User label.

time	
number
Time of trade (Unix timestamp).

position_after	
number
Position in this instrument right after the trade.

session_realised_after	
number
Session realised P&L for this instrument right after the trade.

position_pnl	
number
If trade closed a position, the positional P&L that was realised.

perpetual_funding_pnl	
number
If trade closed a position in a perpetual, the funding P&L that was realised.

fee	
number
The fee paid for this trade.

The fee for a trade is calculated as fee_basis * fee_rate * amount, and is then subject to clamping to minimum and maximum fee. Depending on the instrument, fee_basis can be different (e.g. it can be equal to the underlying index, trade price or combo mark price). Please refer to trading information pages for more details.

index	
number
The relevant index at time of trade.

fee_rate	
number
The fee rate applied to calculate the fee.

fee_basis	
number
The fee basis on which the fee is calculated.

funding_mark	
number
The perpetual funding mark as applied to the trade (see Ticker).

liquidation_fee	
number
Fee paid in case of liquidation.

client_order_id	
number
Client order reference as set in related order.

maker_taker	
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

bot_id	
string
If the trade was made by a bot, the ID of that bot. Otherwise omitted.

leg_index	
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.


Copy
Expand allCollapse all
{
"channel_name": "account.trade_history",
"notification": [
{
"order_id": "00011E570000004A",
"trade_id": "0080000000000000169F22D05B785A2B",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"price": 47280,
"amount": 0.1,
"label": "",
"time": 1630059868.4145653,
"position_after": 1.1,
"trade_type": "normal",
"session_realised_after": 25,
"fee_rate": 0.00025,
"index": 47200,
"fee": 1.18,
"funding_mark": 0.014,
"leg_index": 0
}
]
}
Account order history
Channel name: account.order_history

This subscription notifies when inactive orders are recorded in the central database (i.e. when they would show up in the order_history API call). Unfilled market maker orders are excluded.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "account.order_history"
notification
required
Array of objects (OrderHistory)
Channel-specific content

Array 
order_id
required
string
System order ID, use to identify in amend/cancel, and to match trades.

order_type
required
string
Enum: "limit" "market"
instrument_name	
string
Order instrument name.

Not present for combination orders. Refer to legs field instead.

legs	
Array of objects
List of legs for this combination order.

Not present for single-leg orders. Refer to instrument_name field instead.

Array 
instrument_name
required
string
Leg instrument name.

quantity
required
number
Quantity of this leg in a unit of the combination. A non-zero integer, negative for short legs.

filled_amount
required
number
Amount executed on this leg.

Legs are filled proportionally to their quantities.

direction
required
string
Enum: "buy" "sell"
price	
number
Limit price. May be omitted if no price was supplied (e.g. for a market order).

For combination orders this specifies limit price per unit of the combination.

amount
required
number
Order size (as inserted or amended to).

For combination orders this specifies the amount of units of the combination to trade.

filled_amount
required
number
Part of the order that has been executed.

For combination orders this specifies the amount of units of the combination filled. Legs are filled proportionally to their quantities.

label	
string
Label supplied with insert. Can also be a number. Field is omitted if no label was supplied.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

status
required
string
Enum: "open" "partially_filled" "cancelled" "cancelled_partially_filled" "filled"
fills
required
Array of objects (OrderFill)
All fills for this order.

Array 
trade_id
required
string
Trade ID.

price
required
number
Fill price.

amount
required
number
Filled amount

time	
number
maker_taker
required
string
Enum: "maker" "taker"
Maker (trade on book order) or taker (trade on new order), if applicable.

leg_index
required
number
Index of a leg on which the trade happened for combination orders. Zero for single-leg orders.

For combination orders the direction of the trade is defined by the direction of the order and the sign of the leg quantity.

delete_reason
required
string
Enum: "client_cancel" "client_bulk_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled" "immediate_cancel" "admin_cancel" "replaced" "self_trade_prevention"
Detailed reason of order deletion if the order was deleted, omitted otherwise.

The following reasons are possible:

client_cancel: Order was cancelled by the client, e.g. with a call to private/cancel.

client_bulk_cancel: Order was cancelled by the client with a bulk cancel call, e.g. private/cancel_all.

session_end: Non-persistent order was automatically cancelled when a WebSocket session ended.

instrument_deactivated: Order was automatically cancelled when the order instrument was deactivated, for example after expiration.

mm_protection: Order was automatically cancelled when configured market maker protection amount was exhausted.

failover: Non-persistent order was automatically cancelled on matching engine failover.

margin_breach: Order was automatically cancelled in a response to a margin breach on the account as part of automatic liquidation procedures.

filled: Order was filled in full.

immediate_cancel: The order was submitted as "immediate-or-cancel" and was not filled in full immediately. Note that the order might be partially filled when this delete reason is set.

admin_cancel: The order was cancelled by an exchange admin.

self_trade_prevention: The order was cancelled by the self trade prevention mechanism.

insert_reason
required
string
Enum: "client_request" "conditional_order" "bot" "liquidation"
Detailed reason of order insertion.

conditional_order_id	
string
If the order was triggered by a conditional order (stop order), the ID of that conditional order. Otherwise omitted.

bot_id	
string
If the order was inserted by a bot, the ID of that bot. Otherwise omitted.

create_time
required
number
Creation time (Unix timestamp).

close_time
required
number
Time when this order was closed or canceled (Unix timestamp).

reduce_only	
boolean
True if the order is a reduce only order, omitted otherwise.


Copy
Expand allCollapse all
{
"channel_name": "account.order_history",
"notification": [
{
"order_id": "001BF14D00000003",
"instrument_name": "BTC-16DEC23-46000-C",
"direction": "sell",
"price": "10.0,",
"amount": "0.2,",
"filled_amount": "0.2,",
"status": "filled",
"fills": [
{}
],
"create_time": "1702583649.379417,",
"close_time": "1702583649.379417,",
"insert_reason": "client_request",
"delete_reason": "filled",
"order_type": "limit"
}
]
}
Account portfolio
Channel name: account.portfolio

Subscribes to the total position for the account.

Upon subscription, the full portfolio is sent, but afterwards only updated lines are transmitted (keyed by instrument_name). Lines are retransmitted if the position changes, or if the mark price deviates by more than 1%.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "account.portfolio"
notification
required
Array of objects (PortfolioEntry)
Channel-specific content

Array 
instrument_name	
string
Instrument name.

position	
number
Amount of this contract currently held; short positions are negative.

mark_price	
number
Current mark price for the instrument.

iv	
number
Implied volatility calculated at time of marking.

index	
number
Index price at time of marking.

start_price	
number
Average price paid to obtain position.

Note: for instruments that are subject to daily futures-style settlement, the start price is reset to the mark price at the end of each session and all the unrealized P&L is thus realized. Use private/daily_mark_history API endpoint to get information about daily settlements.

average_price	
number
Average price paid to obtain position. Doesn't reset at settlement.

unrealised_pnl	
number
Unrealised P&L in the current session for this position based on current mark price, equal to (mark_price - start_price) * position.

Note: for instruments that are subject to daily futures-style settlement, the start price is reset to the mark price at the end of each session and all the unrealized P&L is thus realized. Use private/daily_mark_history API endpoint to get information about daily settlements.

realised_pnl	
number
Realized P&L in the current session.

Realized P&L is settled into a settlement asset at the end of each session.

entry_value	
number
Total entry value, equal to start_price * position.

perpetual_funding_entry_value	
number
Entry mark value for perpetual funding. Unrealised perpetual funding is (current perp funding mark * position) - perpetual funding entry value. Not included if zero.

unrealised_perpetual_funding	
number
For perpetual positions, current unrealized perpetual funding.

The funding is realized as P&L and settled into settlement asset at the end of each session.


Copy
Expand allCollapse all
{
"channel_name": "account.portfolio",
"notification": [
{
"instrument_name": "BTC-PERPETUAL",
"position": 1,
"mark_price": 47299.741264339274,
"start_price": 47260,
"average_price": 47260,
"unrealised_pnl": 39.75859976453942,
"realised_pnl": 0,
"entry_value": 47260,
"perpetual_funding_entry_value": -0.13040705,
"unrealised_perpetual_funding": 0.017335425264924917
}
]
}
Account summary
Channel name: account.summary

Periodic updates with current account summary.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "account.summary"
notification
required
object (AccountSummary)
Channel-specific content

unrealised_pnl
required
number
Total unrealised profit or loss.

cash_collateral
required
number
Total margin based on cash holdings.

margin
required
number
Total margin from unrealised P&L and cash holdings.

required_margin
required
number
Required margin based on current position.

remaining_margin
required
number
Difference between margin and required margin.

session_realised_pnl
required
number
Realised profit or loss in current session.

cash
required
Array of objects
List of cash holdings, for each relevant currency, and how they contribute to margin.

Array 
currency
required
string
Currency name.

balance
required
number
Current balance in this currency.

collateral_factor
required
number
The collateral quality of the asset i.e. the fraction of the asset that can be used as a collateral.

collateral_index_price	
number
Index price used to calculate collateral effect of this position. Can be null for assets that are not converted using an index, e.g. for stable coins.

transactable
required
boolean
If this flag is true, this currency can be deposited and withdrawn.


Copy
Expand allCollapse all
{
"channel_name": "account.summary",
"notification": {
"cash": [
{
"currency": "USDT",
"balance": 1000000004483.9625,
"collateral_factor": 1,
"collateral_index_price": null,
"transactable": true
}
],
"unrealised_pnl": 491.00977310002116,
"session_realised_pnl": 0,
"cash_collateral": 1000000004483.9625,
"margin": 1000000004994.1586,
"required_margin": 13123.880458333333,
"remaining_margin": 999999991870.2781
}
}
Account RFQs
Channel name: account.rfqs

Subscribes to RFQ events, for RFQs created by this account. When subscribing, a snapshot will be sent with all currently open requests.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "account.rfqs"
notification
required
Array of objects (Rfq)
Channel-specific content

Array 
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.


Copy
Expand allCollapse all
{
"channel_name": "account.rfqs",
"notification": [
{
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [
{}
],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {
"price": 0,
"amount": 0
},
"quoted_ask": {
"price": 0,
"amount": 0
},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
]
}
Account RFQ history
Channel name: account.rfq_history

Subscribes to RFQ history, for RFQS created by this account. Note that this feed is sent only after RFQs have been fully processed in the central database, and will therefore be slightly behind account.rfqs.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "account.rfq_history"
notification
required
Array of objects (Rfq)
Channel-specific content

Array 
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.


Copy
Expand allCollapse all
{
"channel_name": "account.rfq_history",
"notification": [
{
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [
{}
],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {
"price": 0,
"amount": 0
},
"quoted_ask": {
"price": 0,
"amount": 0
},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
]
}
Conditional orders
Account conditional orders
Channel name: account.conditional_orders

Subscribes to changes in the list of conditional orders. The feed contains a full set of orders every time, including past orders; it is identical to the output of the private/conditional_orders RPC call. No update is sent upon removal of old inactive orders.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "account.conditional_orders"
notification
required
Array of objects (ConditionalOrder)
Channel-specific content

Array 
order_id
required
string
Unique ID, use to identify in cancel

instrument_name
required
string
direction
required
string
Enum: "buy" "sell"
amount
required
number
Size of the order when activated

target
required
string
Enum: "last" "mark" "index"
The trigger type that stop_price and bracket_price will refer to.

stop_price
required
number
Trigger price at which the order will be activated

limit_price	
number
For stop limit order, the price at which the order will be placed

bracket_price	
number
For bracket order, the price at which profit will be taken (upper activation price)

trailing_stop_callback_rate	
number
For trailing stop loss, the callback rate as a ratio (e.g. 0.05 for 5%)

label	
string
Optional user label

status
required
string
Enum: "created" "active" "converted" "rejected" "cancel requested" "cancelled"
create_time
required
number
update_time
required
number
Time of last update (conversion or change of trailing stop price)

convert_time	
number
Time of trigger

converted_order_id	
string
System order ID of the created order.

reject_reason	
string
If conversion failed, the reason

reduce_only
required
boolean

Copy
Expand allCollapse all
{
"channel_name": "account.conditional_orders",
"notification": [
{
"order_id": "00011E570000004B",
"instrument_name": "BTC-PERPETUAL",
"direction": "buy",
"amount": 1,
"stop_price": 50000,
"limit_price": 45000,
"status": "created",
"create_time": 1630062311.3324597,
"update_time": 1630062311.3324597,
"reduce_only": false,
"target": "mark"
}
]
}
Bots
Account bots
Channel name: account.bots

Subscribes to changes in the bots that the subaccount is running. The feed contains a full set of bots every time, including stopped bots.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "account.bots"
notification
required
Array of SGSL (object) or OCQ (object) or Levels (object) or Grid (object) or DHedge (object) or DFollow (object) (Bot)
Channel-specific content

Array 
One of SGSLOCQLevelsGridDHedgeDFollow
bot_id
required
string
Individually identifies this bot instance. You can use it to cancel this specific one.

status
required
string
Enum: "active" "stopped"
stop_reason	
string
Enum: "client_cancel" "client_bulk_cancel" "end_time" "instrument_deactivated" "margin_breach" "admin_cancel" "conflict" "strategy" "self_trade_prevention"
The reason why the bot stopped executing.

strategy
required
string
equal to "sgsl"

instrument_name
required
string
Name of the instrument.

signal
required
string
Enum: "last" "index" "mark"
entry_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

target_position
required
number
The target position to maintain in the subaccount if signal price is above entry_price. See the bot strategies section for more explanation.

exit_price
required
number
Price to compare signal price to, to determine necessary adjustments to the portfolio. See the bot strategies section for more explanation.

exit_position
required
number
The target position to maintain in the subaccount if signal price is below exit_price. See the bot strategies section for more explanation.

max_slippage	
number
Maximum slippage per trade, expressed as % of the traded instruments mark price.

end_time
required
number
Timestamp when the bot stops executing, cancelling its orders and leaving all positions of the subaccount intact.

start_time
required
number
Timestamp indicating when the bot was created.

stop_time	
number
Timestamp indicating when the bot stopped working due to specified stop_reason.

label	
string
A label that the bot will add to all orders for easy identification.

realized_pnl
required
number
Realized P&L made by this bot since the start.

fee
required
number
Trade fees by this bot.

average_price	
number
Average entry price of the position (if any).

position_size	
number
Position size (if any).

mark_price_at_stop	
number
Mark price of the bot instrument at the moment the bot was stopped.


Copy
Expand allCollapse all
{
"channel_name": "account.bots",
"notification": [
{
"strategy": "sgsl",
"status": "active",
"bot_id": "0000000035832FDE",
"instrument_name": "BTC-PERPETUAL",
"signal": "index",
"entry_price": 100050,
"target_position": 0.2,
"exit_price": 100000,
"exit_position": 0,
"end_time": 1740064912,
"start_time": 1740064912,
"stop_time": 1740064912
}
]
}
Notifications
User inbox notifications
Channel name: user.inbox_notifications

This subscription notifies when new notifications are posted or existing notifications are updated (e.g. marked as read) for this user.

The feed includes only the notifications for which inbox preference is set.

Note: this feed only delivers updates that happen after the time of subscription. To get a historical list of notifications use private/notifications_inbox call.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "user.inbox_notifications"
notification
required
object (Notifications)
Channel-specific content

notifications	
Array of objects
List of notifications ordered from newest to oldest.

Array 
id
required
string
Unique notification ID.

time
required
number
Time of notification (Unix timestamp).

category
required
string
Notification category (see API description / Notifications).

title
required
string
Human-readable title for the notification.

message
required
string
Human-readable message for the notification.

display_type
required
string
Enum: "success" "failure" "info" "warning" "critical"
Specifies what style to use for notification display.

read
required
boolean
set to true if notification was marked as read.

account_name	
string
Optional account name, only present if the notification is related to an account.

account_number	
string
Optional account number only present if the notification is related to an account.

popup
required
boolean
User preference - show popup for this notification


Copy
Expand allCollapse all
{
"channel_name": "user.inbox_notifications",
"notification": {
"notifications": [
{
"id": "00000000000000A3",
"time": 1630069885.130461,
"category": "risk",
"title": "Margin Requirements",
"message": "Portfolio of account foo-123 breached initial margin requirements.",
"display_type": "warning",
"read": false,
"account_name": "foo-123",
"account_number": "A123456789",
"popup": true
}
]
}
}
Market maker protection
Session MM protection
Channel name: session.mm_protection

Subscribes to updates in the status of market maker protection groups.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "session.mm_protection"
notification
required
Array of objects
Channel-specific content

Array 
product	
string
remaining_amount	
number
Remaining amount may be less than zero if a single aggressive order has caused an overshoot. If remaining amount is less than or equal to zero, the mass quote orders in the group will have been cancelled, and the group needs refilling.

reason	
string
Enum: "refill" "executions" "client_cancel" "session_end" "failover"
Detailed reason of the protection group status update.

The following reasons are possible:

refill: Remaining amount was updated by the client, e.g. with a call to private/set_mm_protection.

executions: Remaining amount was updated after a trade.

client_cancel: Protection group was deleted by the client, e.g. with a call to private/cancel_mass_quote.

session_end: Protection group was automatically deleted when a WebSocket session ended.

failover: Protection group was automatically deleted on matching engine failover.


Copy
Expand allCollapse all
{
"channel_name": "session.mm_protection",
"notification": [
{
"product": "OBTCUSD",
"remaining_amount": 10,
"reason": "refill"
}
]
}
Request for Quote (MM)
Quote requests
Channel name: mm.rfqs

Subscribes to all RFQs created, for which this account is an eligible counterparty. When subscribing, a snapshot will be sent with all currently open eligible RFQs.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "mm.rfqs"
notification
required
Array of objects (Rfq)
Channel-specific content

Array 
rfq_id
required
string
Identifier for this RFQ.

amount
required
number
Requested amount for this RFQ

create_time
required
number
Timestamp of creation (unix timestamp)

valid_until	
number
Timestamp at which this RFQ will be automatically cancelled (unix timestamp)

legs
required
Array of objects
Combo legs. A minimalised version of the request such that quantities are integer.

Array 
instrument_name
required
string
quantity
required
number
Quantity for this leg. May be negative.

fee_quantity
required
number
Quantity for fee calculations. Anywhere between 0 and abs(quantity).

label	
string
User label set at creation. Not visibible to market makers.

insert_reason	
string
Enum: "client_request" "liquidation"
Detailed reason for creation. Visible only to the requester.

delete_reason	
string
Enum: "client_cancel" "filled"
Reason why this RFQ was removed. Visible only to the requester.

volume_tick_size	
number
The minimum size / size increase for quotes.

quoted_bid	
object
The bid price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
quoted_ask	
object
The ask price/amount quoted so far, if any. Visible only to the requester.

price	
number
amount	
number
trade_price	
number
Combo price for which this RFQ was traded.

trade_amount	
number
Amount in which this RFQ was traded.

close_time	
number
Time at which this RFQ was cancelled or traded.

event	
string
Enum: "Created" "Cancelled" "Traded" "Existing"
This field is set only on the account.rfqs subscription.


Copy
Expand allCollapse all
{
"channel_name": "mm.rfqs",
"notification": [
{
"rfq_id": "string",
"amount": 0,
"create_time": 0,
"valid_until": 0,
"legs": [
{}
],
"label": "string",
"insert_reason": "client_request",
"delete_reason": "client_cancel",
"volume_tick_size": 0,
"quoted_bid": {
"price": 0,
"amount": 0
},
"quoted_ask": {
"price": 0,
"amount": 0
},
"trade_price": 0,
"trade_amount": 0,
"close_time": 0,
"event": "Created"
}
]
}
Open RFQ quotes
Channel name: mm.rfq_quotes

Subscribes to RFQ quote events, including all quotes on all RFQs created by this account. When subscribing, a snapshot will be sent with all currently active quotes.

Notification payload:

channel_name
required
string
Channel name as in subscription.

Value: "mm.rfq_quotes"
notification
required
Array of objects (RfqOrder)
Channel-specific content

Array 
rfq_id
required
string
Identifier of the RFQ.

order_id
required
string
Identifier of the individual quote.

client_order_id	
number
Client-supplied order id. Field is omitted if no client order id was supplied.

direction
required
string
Enum: "buy" "sell"
price
required
number
amount
required
number
label	
string
trade_price	
number
the price at which this order traded.

trade_amount	
number
the number of combinations that traded.

delete_reason	
string
Enum: "client_cancel" "session_end" "instrument_deactivated" "mm_protection" "failover" "margin_breach" "filled"
Detailed reason of order deletion.

event	
string
Enum: "Inserted" "Amended" "Cancelled" "Filled" "Existing"
This field is set only on subscriptions.


Copy
Expand allCollapse all
{
"channel_name": "mm.rfq_quotes",
"notification": [
{
"rfq_id": "string",
"order_id": "string",
"client_order_id": 0,
"direction": "buy",
"price": 0,
"amount": 0,
"label": "string",
"trade_price": 0,
"trade_amount": 0,
"delete_reason": "client_cancel",
"event": "Inserted"
}
]
}
Bot strategies
Bots in general
Margining bots
Running bots in your subaccount doesn't affect your margin requirement directly. Having said that, the bots are going to insert orders in your subaccount, and may enter or exit positions, which will affect your margin requirement. If at any point a bot is not able to insert or amend an order, because of a margin error, it is going to immediately stop executing, cancelling any orders it may have in the book, and leaving all positions of the subaccount intact. Also if your subaccount breaches the initial margin requirement, all bots in the subaccount will be stopped in the same fashion. In these cases, the private/bots endpoint will show the bots with { status: stopped, stop_reason: margin_breach }.

Conflicting bots
In certain cases, creating a bot could lead to a "conflict" with already existing bots, meaning that the two bots, if both were running concurrently under specific circumstances, could try to adjust the portfolio in different directions, or would insert orders in cross with each other's.

To prevent that, one or more of the bots may be stopped, even if they were created successfully. In this case, the private/bots endpoint will show the bots with { status: stopped, stop_reason: conflict }.

Thalex however doesn't guarantee to stop all possible conflicting bots, consider the strategies and their parametrization carefully, especially when creating bots with different strategies on the same or related instruments. Related instruments means for example a combination type instrument and one of its legs, since they may still end up trading with each other via implied matching.

Slippage when taking out orders
Some of the strategies include aggressively taking out orders that are in the book. In order to control slippage, these strategies allow you to define max_slippage, expressed as a percentage of the mark_price of the traded instrument, at the time of inserting the taker order. The actual price the bot will insert the order with, will not be worse than the price defined by max_slippage. However, if there are orders in the book at a worse price level than the collar price of the instrument, and the max_slippage defined allows, the bot will take those out. If max_slippage is not defined, the bots will trade within the collar prices of the instrument. The taker bots will not trade more frequently than 1/s.

Start Gain, Stop Loss
Strategy description
The Start Gain, Stop Loss (SGSL) strategy is about dynamically entering a target position in an instrument, when its price goes above a certain level (start-gain), and dynamically exiting the position when the price falls below that (stop-loss). This allows, among other things, dynamic replication of options using delta-one instruments.

In a classical use case, in order to replicate a long call option, when the underlying price is above the strike price, the trader would place orders to enter a long position in the underlying instrument, and when its price is below the strike price, the trader would place orders to exit the position. Thalex SGSL bot(s) can be parameterized to implement more advanced versions of the strategy, meaning you can also replicate short options, puts and even straddles, or you can have (a replication of) an option on an option.

The parameters that define the strategy are:

signal
entry_price
target_position
exit_price
exit_position
The signal price can be an underlying index price, mark price of an instrument or last trade price of an instrument. The bot is going to listen to this signal, and if it goes above entry_price, the bot will aggressively trade into target_position, and if the signal price falls below the exit_price, the bot will aggressively trade into the exit_position. The values of target_position and exit_position parameters can be positive (to maintain a long position), negative (to maintain a short position), or zero (to close the position).

The relation of target_position and exit_position define whether the bot is going to correct to position up or down when one of the trigger conditions is met.

When creating the bot, you can and have to set an end_time. The bot is going to continuously trade as described above until this end_time is reached, and then the bot simply stops executing, meaning it won't do any more trades. It leaves all positions of the subaccount as they were at the moment of reaching end_time.

The SGSL bot does not perform any per-bot accounting and maintain the the subaccount's total position in the instrument. This means that if you place orders on the same instrument while the bot is active, and the orders get filled, the bot might try to correct the resulting position according to the strategy logic. Consider running the bot on a dedicated sub-account.

Position management
When we say that the bot will aggressively trade into target_position, technically what we mean is that the bot will place taker orders if necessary, in order to maintain a position outside of the (target_position, exit_position] range, in the direction of target_position in the subaccount. Similarly, when "exiting" the position, the bot will place taker orders if necessary, in order to maintain a position outside of the [target_position, exit_position) range, in the direction of exit_position in the subaccount.

This means, that when a trigger condition is met (the signal price goes either above entry_price or below exit_price), and the subaccount's position in the instrument already falls on the correct side of the range, the bot is not going to do anything. This allows you to do two things. First, you can correct the position manually, as long as the correction is not controversial to any trigger conditions currently met, second, you can run multiple SGSL bots on the same instrument "above each other", meaning one of them having an exit_position and an exit_price greater or equal to the target_position and entry_price of the other.

Example 1: long put
Let's assume that BTC is trading around $100k, you're not running any bots, and your subaccount doesn't hold a position in BTC-15MAY25 or BTC-15MAY25-100000-P. Your view is that the BTC-15MAY25-100000-P is overpriced, so you sell 0.1 contracts of the put option, opening a short position, and to hedge the associated risks, you create an SGSL bot with the following parameters:

{
  signal: 'index',
  entry_price: 100500,
  target_position: 0,
  exit_price: 99500,
  exit_position: -0.1,
  instrument_name: 'BTC-15MAY25'
}
This means, that as long as the BTCUSD index price stays above $100k, you simply capture the premium of the option as profit.

If at any point until the bots end_time is reached or the instruments expire, the index price falls below $100k, you would have a potential loss of $100k - index, but if the index falls further, to $99500, the SGSL bot will enter a short position of size 0.1 in BTC-15MAY25, limiting the downside risk to a maximum loss of $500 (plus slippage).

Later if BTC trades at $105k, the hedge no longer being necessary, the bot would trade out of the subaccount's position in BTC-15MAY25.

Your overall profit when executing this strategy is linked to the implied volatility, through the premium of the option you gain, when entering the short option position, and your loss depends on how much volatility is actually realized around the strike price. Notice, that if the option goes deep in the money, or far out of the money, the volatility that the index realizes doesn't matter anymore, since the bot will not need to adjust the portfolio.

Example 2: short straddle
Let's assume that BTC is trading around $100k, you're not running any bots, and your subaccount doesn't hold a position in BTC-PERPETUAL. You decide to replicate a $100k short straddle on BTC with BTC-PERPETUAL, by creating an SGSL bot with the following parameters:

{
  signal: 'index',
  entry_price: 100500,
  target_position: -0.1,
  exit_price: 99500,
  exit_position: 0.1,
  instrument_name: 'BTC-PERPETUAL'
}
Then later the price of BTCUSD index reaches $100500, your entry_price. The bot is going to insert sell orders in cross with the book, until the filled amounts of the orders add up to 0.1, so your subaccount would hold a position of size -0.1, your target_position.

Later, BTC is trading around $110k, and you decide to manually insert a sell order of size 0.05 at $110k, and the order is fully filled. Your subaccount's BTC-PERPETUAL position is now -0.15 contracts.

Then the price of BTC falls to 99500, your exit_price. The bot will then insert buy orders in cross with the book, until the filled amounts of the orders add up to 0.25, trading out of your short position of 0.15 contracts, and opening a long position equal to 0.1, your exit_position.

You would (not taking slippage and fees into account) realize a PNL of 0.1 * 100500 + 0.05 * 110000 - 0.15 * 99500 = 625 when closing the short position.

Example 3: three band option delta replication
Let's assume that BTC is trading around $100k, you're not running any bots, and your subaccount doesn't hold a position in BTC-15MAY25 or BTC-15MAY25-100000-C. Your view is that the BTC-15MAY25-100000-C is overpriced, so you sell 0.1 contracts of the option, opening a short position. You could now start an SGSL bot, entering an equally sized long position in BTC-15MAY25, when the option goes into the money, and exiting it when it goes out of the money, but if volatility is very high, or there is a lot of time until expiry for volatility to realize around the strike price, you could lose more money on trading in and out of the future position, than you gain for selling the option.

In this case, in order to still hedge your short option position, you can set up two SGSL bots, with parameters like:

bot 1

{
  signal: 'index',
  entry_price: 95500,
  target_position: 0.05,
  exit_price: 94500,
  exit_position: 0,
  instrument_name: 'BTC-15MAY25'
}
bot 2

{
  signal: "index",
  entry_price: 105500,
  target_position: 0.1,
  exit_price: 104500,
  exit_position: 0.05,
  instrument_name: 'BTC-15MAY25'
}
Now if BTC is trading around $100k, the option is at the money, so likely it's close to 0.5 delta. Since $100k is above bot 1's entry_price, bot 1 will enter its target_position of 0.05 in BTC-15MAY25, and $100k is under bot 2's exit_price, and the subaccount's portfolio position being already equal to bot 2's exit_position, bot 2 is not going to do anything. In this case, the subaccount's portfolio will be closer to delta neutral, than if you were only running a single SGSL around the option's strike price. Also, the important difference is, that long as the index price stays between bot 1's exit_price and bot 2's entry_price, the bots won't do any further adjustments to the portfolio.

If then the option you sold goes deeper into the money, and the index price raises to $105500, the option is going to gain more deltas, and since bot 2's entry_price will be hit, bot 2 is going to enter a position of 0.1 in BTC-15MAY25, decreasing the overall delta exposure of the subaccount's portfolio.

One Click Quoter
Strategy description
The one click quoter (OCQ) strategy is a market making strategy, that continuously quotes a given instrument based on the underlying index or the mark price of the instrument with a specified size and price offset.

As long as the subaccount's portfolio position in the instrument that the bot is trading is within the (min_position + quote_size, max_position - quote_size) range, the bot will quote both sides of the book with quote_size. Outside of that range, the bot will reduce the quote size, or may even cancel one of the quotes, in order to respect position limits. If the actual portfolio position goes above max_position, the bot will cancel the bid quote, and similarly if the actual portfolio position goes below min_position, the bot will cancel the ask quote. If one of the quotes is cancelled, because one of the position limits is breached, the bot keeps executing, and quotes only the other side of the book. If the position goes back in the (min_position, max_position) range, the bot starts quoting both sides again.

The price of the bid quote is defined by the signal price and the bid_offset like bid = signal + bid_offset, and the price of the ask quote is defined by the signal price and the ask_offset like ask = signal + ask_offset. The quote prices do not depend on the portfolio position.

Note that quotes might affect the mark price, so quoting based on the mark price can become self referential under specific circumstances.

The bot will amend the bid quote if signal price + bid_offset differs at least a set amount of ticks from the quoted price in the book, or if as the result of a fill the size of the bid quote needs to be increased or reduced. The bot will amend the ask quote if signal price + ask_offset differs at least a set amount of ticks from the quoted price in the book, or if as the result of a fill the size of the ask quote needs to be increased or reduced. The amend threshold is 1 price tick for future rolls and 3 price ticks for everything else. Quoting options and rolls is only possible based on their mark prices (so not based on index). Perpetuals and dated futures can be quoted based on their mark prices or based on the underlying index price.

The OCQ bot will always create post_only quotes, meaning they cannot possibly lead to an aggressive execution.

When end_time is reached, the bot stops executing, cancelling all orders it has in the book, leaving all positions of the subaccount intact.

Example 1: dated future
If you want a to quote a dated future $100 above index price, with a $20 spread, and 0.1 size, you would create the bot with parameters like

{
  signal: 'index'
  bid_offset: 90,
  ask_offset: 110,
  quote_size: 0.1,
  min_position: -0.15,
  max_position: 0.15
}
Initially, assuming that your subaccount doesn't hold a position in the given future, and assuming that the index price is $100k, and there are no other quotes in the book, the bot would create a bid quote of size 0.1 and price $100090, and an ask quote of size 0.1 and price $100110.

Then, assuming that the price tick of the chosen future is $1, as long as the index stays in the [99997, 100003] range, the bot will not amend the quotes. If the index moves to $100004, both quote prices will be amended, assuming no fills, the sizes will be left intact. The bid price will become $100094, and the ask price will become $100114.

If then the ask is fully filled, and the index moved to $100005, the bid quote will not be amended, it will still be size 0.1, price $100094. Since your subaccount's position in the future is now -0.1, and the minimum position set when creating the bot was -0.15, there's still 0.05 contracts left to quote on the ask side, with staying within the position limits. The OCQ bot doesn't take the portfolio position into account for pricing, so it will insert a new ask in the book, with size 0.05 and price $100115.

Let's see what happens, if the index price doesn't change, but 0.05 of the bid is filled at this point. Your subaccount's position in the future becomes -0.05, which is within the range where full quote_size can be quoted in both directions. Both quotes are amended, the bid from 0.05 at $100094 to 0.1 at $100095, and the ask to 0.1 at $100115.

If the ask is taken out, and your position then reaches the min_position limit at -0.15, the bot will not insert a new ask quote, only keep the bid in the book unchanged.

Let's assume, that the bid is not filled, but an other market participant inserts a bid quote of size 0.1 at price $100100. You decide to take it out, by inserting a limit order of size 0.1 at price $100100 with time in force: immediate_or_cancel via the trading ui. Let's assume that your manually inserted order is filled, increasing your position to -0.05. At this point, the OCQ bot will leave the bid order in the book unamended, and it will insert a new ask order of size 0.1 at price $100115.

Optionally you can set exit_offset and target_position and the bot will insert a quote when your position changes from target_position. This quote also follows the signal price.

Example 2: option mark
If you want to quote an option with a $200 spread around its mark price, you would create the bot with parameters like

{
  signal: 'mark',
  bid_offset: -100,
  ask_offset: 100`
}
Assuming that the mark price of the option is $3k, the bot would create a bid quote at $2900, and an ask quote at $3100, regardless of the index price. The bot also won't amend the option quotes if the index price moves.

The quotes will be amended, assuming no fills and a price tick of $5, if the mark price of the option moves outside of the [2985, 3015] range.

Example 3: post only
Let's assume you created an OCQ bot with the following parameters on a perpetual future:

{
  signal: 'index'
  bid_offset: -20,
  ask_offset: 80
}
Let's assume, that the index price of the underlying of this perpetual is $100k, and there's a bid quote in the book at $100090. Normally, the OCQ bot would insert an ask quote at $100080 (index + ask offset), but since that's in cross with the book, it would lead to aggressive execution, so the bots actual ask quote in the book will be moved to $100091 (one tick away from best bid).

Similarly, let's assume, you have a bot running on a dated future that you don't have a position in, with parameters:

{
  signal: 'index'
  bid_offset: -50,
  ask_offset: 50,
  quote_size: 0.1,
  min_position: -0.3,
  max_position: 0.3
}
Let's further assume, that the index price of the future's underlying is $100k, so the bot's quotes in the book are a bid of size 0.1 at $99950, and an ask of size 0.1 at $100050. Now if an other market participant inserts a limit sell order of size 0.2 at price $99940, with time in force: good_till_cancelled, it will fill the bots bid at $99950 fully, and 0.1 contracts will remain in the book, at $99940. Now if the index doesn't change, normally the OCQ bot would insert an other bid of size 0.1 at price $99950, but that would be in cross with the best ask now, so the bid price will be lowered to $99939, 1 tick under the best ask.

Example 4: exit quote
Let's assume you created an OCQ bot with the following parameters on a perpetual future:

{
  signal: 'index'
  bid_offset: -100,
  ask_offset: 100,
  exit_offset: 50,
  quote_size: 0.1,
  min_position: -0.2,
  max_position: 0.2,
  target_position: 0
}
Let's assume that the index price of the underlying of this perpetual is $100k, so the bot's quotes in the book are a bid of size 0.1 at $99900 and an ask of size 0.1 at $100100. Now the bid quote is filled and we have a 0.1 position. The bot will create an exit ask quote of size 0.1 at $100050 (index + exit_offset) in order to reach the desired 0 target position. The exit quote price follows the signal price similarly to bid and ask quotes.

Levels
Strategy description
The idea of this strategy is to profit from local volatility, by buying below or selling above a short term mean reversion price, and then exiting the position at the mean reversion price. You can parameterize the strategy by setting the target_mean_price, a set of bid levels, and a set of ask levels. Manually setting the target_mean_price is optional, it defaults to the mark price of the instrument, when starting the bot. Also either the bids, or the asks can be empty, meaning the bot would only open a short/long position. Optionally, you can set exit prices, in case your initial view was incorrect, and the price breaks out. If the mark price of the instrument hits one of these exit prices, the bot cancels the maker orders, aggressively trades into base_position, and then stops executing.

As long as the subaccount's portfolio position in the instrument that the bot is trading is equal to base_position, the quoted bid amount will be number of bids * step_size, and the quoted ask amount will be number of asks * step_size. If the portfolio position becomes greater for whatever reason (so even because of fills on orders other than those of the bots), the bid amount is reduced, if the portfolio position becomes lower, the ask amount is reduced, and in parallel the bot inserts an order at target_mean_price to close the part of the position on top of base_position. Any bid amount is always quoted in step_size levels, starting from the lowest bid level, and any ask amount is always quoted in step_size levels, starting from the highest ask level.

The Levels bot doesn't take index or mark price into account when creating orders, it will always quote at the price levels specified when creating the bot.

The Levels bot inserts good till cancel limit orders, that can lead to aggressive executions.

When end_time is reached, the bot stops executing, meaning it cancels any orders it has in the book. It leaves all positions of the subaccount as they were at the moment of reaching end_time.

Example 1
Let's assume, that a future that you don't hold a position in is traded around $10k, and you created a Levels bot on the instrument with parameters like

{
  bids: [9970, 9980],
  asks: [10040, 10050],
  target_mean_price: 10000,
  downside_exit_price: 9920,
  upside_exit_price: 10100,
  step_size: 0.1,
  base_position: 0
}
The initial quotes of the bot would be 2 bids, sized 0.1 each at $9970 and $9980, and 2 asks sized 0.1 each at $10040 and $10050. Let's see what happens, if an other market participant inserts a 0.15 size market sell order, taking the entire $9980 bid quote, and 0.05 amount of the 9970 bid quote out. Your subaccount's portfolio position in the instrument would become 0.15, making your bid amount 0.05, the remaining part of the $9970 bid quote, which would just stay in the book. The two asks at prices 10040 and 10050 would still be of size 0.1, remaining untouched. The bot would also insert a sell order of size 0.15 at $10000. Now if an other aggressor takes all of your asks out, you close the long position you had open realizing a profit, and open a new, short position of size -0.2. The bot would insert amend the $9970 bid to size 0.1, insert a new bid of size 0.1 at $9980, and one size 0.2 at $10000. The bot wouldn't insert a new ask again, until the portfolio position size is increased.

As long as the mark price of the instrument stays within the [9920, 10100] range, the bot would keep trading in that fashion, until the time reaches the end_time set when creating the bot, in which case the bot would simply stops executing, leaving all positions of the subaccount intact.

If you would now call the private/bots endpoint, the bot would show with { status: stopped, stop_reason: end_time }.

Example 2: no asks
Let's assume, that a future that you don't hold a position in is traded around $10k, and you created a Levels bot on the instrument with parameters like

{
  bids: [9970, 9980],
  asks: [],
  target_mean_price: 10000,
  downside_exit_price: 9920,
  upside_exit_price: 10100,
  step_size: 0.1,
  base_position: 0
}
The bot would quote the bid side only, at levels $9970 and $9980 with quotes sized 0.1 each. Now if both of your bids would be taken out, making your subaccount's portfolio position 0.2, the bot would insert sell order of equivalent size (0.2) at $10000 to close to position for profit.

If the price would never recover, and the mark price would drop all the way to $9920, without the sell order being taken out, the bot would cancel the quote at $10000, aggressively sell the 0.2 you have open, realizing a loss, and then stop executing.

If you would now call the private/bots endpoint, the bot would show with { status: stopped, stop_reason: strategy }.

Example 3
Let's assume, that you have a long perpetual position of size 1, hedged with a future that is traded around $10k. You want to profit from volatility, and you create a Levels bot on the future with parameters like

{
  bids: [9970, 9980],
  asks: [],
  target_mean_price: 10000,
  upside_exit_price: 10100,
  step_size: 0.1,
  base_position: -1
}
The bot would quote the bid side only, at levels $9970 and $9980 with quotes sized 0.1 each. Now if the price breaks out upwards and the mark of the future rises to $10100, without any fills on the bids, the bot simply cancels the bids, doesn't do any trades, leaving the position at -1, and stops executing.

Grid
Strategy description
The idea of this strategy is to profit from local volatility, by buying low and selling high on a specified grid. You can define the grid as a set of price levels, and a short term mean reversion price. This mean reversion price will be the "focus of the grid", above this price the bot will open a short position, and below this the bot will open a long position. The goal of the strategy is to close any position that is opened, on the next level of the grid, in the profitable direction. So any amount filled on buy orders will be quoted on the ask side, one step up the grid.

You can optionally define exit prices around the grid, and if the mark price of the instrument hits one of the exit prices, the bot cancels the maker orders, aggressively trades into base_position, and then stops executing.

As long as the account's portfolio position in the instrument that the bot is trading is equal to base_position, the bot will insert step_size asks on the grid above target_mean_price (one per level), and step_size bids below target_mean_price. If the portfolio position is greater than base_position, then the bid amount is decreased, and the ask amount is increased, if the portfolio position is lower than base_position, then the ask amount is decreased, and the bid amount is increased.

The Grid bot inserts good till cancel limit orders, that can lead to aggressive executions.

When end_time is reached, the bot stops executing, meaning it cancels all orders it has in the book. It leaves all positions of the subaccount as they were at the moment of reaching end_time.

Example 1
Let's assume you created a grid bot on an instrument that your subaccount doesn't hold a position in, with parameters:

{
  base_position: 0,
  grid: [90, 100, 110, 120],
  target_mean_price: 105,
  step_size: 0.1
}
Initially, the bot will insert 4 quotes of size 0.1 each. Two of these quotes will be bids at levels $90 and $100, and two of them asks at $110 and $120. If the $100 bid and half of the $90 bid is filled, the bot will keep the remaining 0.05 of the bid at $90, insert a new ask of size 0.05 at $100, and amend the $110 sell to size 0.2. This way, if the ask quotes are filled, the 0.05 amount that was bought at $90 would be sold at $100, the 0.1 that was bought at $100 would be sold at $110, and having the long position closed, a new, short position would be opened.

Example 2
Let's assume you created a grid bot on an instrument that your subaccount doesn't hold a position in, with parameters:

{
  base_position: 0,
  grid: [90, 100, 110],
  target_mean_price: 120,
  step_size: 0.1
}
Initially, the bot will insert 2 bid quotes at $90 and $100 of size 0.1 each. It would initially not insert a quote at $110, in order to leave some space to take profit if the $100 bid is taken out. If that happens, and both bids are taken out, the quote in the book would be 2 asks of size 0.1 at $110 and $100.

If then the mark price of the instrument goes below downside_exit_price, the bot would cancel all orders in the book, and insert taker orders until it trades out of the subaccount's portfolio position in the instrument, and then stop executing.

If you would now call the private/bots endpoint, the bot would show with { status: stopped, stop_reason: strategy }.

Delta Hedger
Strategy description
This strategy is for managing directional exposure, by trading in an instrument, to target a specific amount of total portfolio deltas in the underlying.

Optionally you can specify a position, and then the bot will be hedging the deltas only from your sub-account's portfolio position in that instrument.

The bot allows the deltas to stay outside of [target_delta - threshold, target_delta + threshold] for period seconds before making any adjustments to the portfolio. The target_delta and threshold are both 0 by default, meaning the bot bot will just make the portfolio delta neutral every period seconds. If the deltas deviate for period-1 seconds and then recover on their own, the bot will not make any adjustments to the portfolio,and the tolerance period also restarts, meaning they need to deviate for a further period seconds before the bot would hedge them again.

The strategy also has the tolerance parameter. If the deltas are outside of [target_delta - tolerance, target_delta + tolerance], the bot will hedge them immediately, without waiting period seconds.

The bot will only take deltas into account from portfolio positions in instruments, with the same underlying as the hedging instrument defined by instrument_name.

Example 1: Entire portfolio
To keep a dynamically changing BTC option portfolio's delta exposure within [-0.1, 0.1], you decide to trade BTC-PERPETUAL every 30 minutes. This is how you would start a bot to do exactly that:

{
  strategy: 'dhedge',
  instrument_name: 'BTC-PERPETUAL',
  period: 1800,
  threshold: 0.1,
}
Example 2: Specific position
One sub-account of yours has 1 BTC deposited as collateral, and you are running an OCQ bot on BTC-26JUN25 in an other sub-account. You decide to trade BTC-PERPETUAL every minute to hedge the position of the sub-account that's running the bot in the dated future, but also account for the spot BTC in the other sub-account. You would need to start a bot in the same sub-account that is running the OCQ bot with the following parameters:

{
  strategy: 'dhedge',
  instrument_name: 'BTC-PERPETUAL',
  position: 'BTC-26JUN25',
  period: 60,
  target_delta: -1
}
Delta Follower
Strategy description
By design this strategy is for replicating the deltas of an option with a delta one instrument, with much greater resolution, than the Start Gain, Stop Loss (SGSL) strategy. You can specify the name of an option (target_instrument), and the amount of contracts to target the deltas of (target_amount). The bot will trade the instrument named instrument_name, so that the deltas from you sub-account's portfolio position in the instrument named instrument_name will be equal to the deltas of (1 contract of) target_instrument * target_amount. The bot allows the deltas to deviate +/- threshold for period seconds before making any adjustments to the portfolio.

The strategy also has the tolerance parameter. If the deltas are outside of [target_delta - tolerance, target_delta + tolerance], the bot will hedge them immediately, without waiting period seconds.

Technically you can also use an option to replicate the deltas of an other option with.

Example: Hedging a short put position
You sold 0.1 contracts of BTC-26JUN25-100000-P in one sub-account manually via the trade ui, and to hedge some of the deltas from it, you decide to replicate the inverse of the position in an other sub-account. To do so, you want to trade BTC-26JUN25 every 10 minutes, so that the deltas from your position in BTC-26JUN25 would be in the +/- 0.05 range of those of from the position in BTC-26JUN25-100000-P. This is how you would parameterize a bot to do that:

{
  instrument_name: 'BTC-26JUN25',
  target_instrument: 'BTC-26JUN25-100000-P',
  target_amount: -0.1,
  period: 600,
  threshold: 0.05,
}
This bot, while running would periodically check the deltas of both positions, and if they deviate more than 0.05 for at least 10 minutes continuously, it'd trade BTC-26JUN25 to push the deviation back under the threshold.

API change log
v2.55.0
Add index_price and collateral_factor to the asset positions breakdown of portfolio margin scenarios in private/required_margin_breakdown API.
v2.54.0
Add private/trade_value_history API to get historical trading volume.
v2.53.0
Add credit transaction type.
v2.52.0
Add self trade prevention.
v2.51.0
Add bots pnl.
v2.50.0
Add fee_basis field to trades API response.
v2.49.0
Add exit_offset and tgt_pos to ocq strategy.
v2.48.0
Add close_time to order payloads.
v2.47.0
Add filtering and sorting by bot_id to the trades API.
v2.46.0
Add filtering by instrument name and bot_id and sorting to order_history.
v2.45.0
Add filtering by instrument name and sorting to trades API.
v2.44.0
Add bot_id to order and order history.
v2.43.0
Add support for bots.
v2.42.0
Support combination orders in the required_margin_for_order API call.
v2.41.0
Ticker subscription channels extended to support combinations.
v2.40.0
Subscription channel for system events ("system") and events for server-initiated WebSocket reconnects.
v2.39.0
Support for inserting combination orders and subscribing to combination order books.
v2.38.0
Extend historical mark price endpoint with the top of book data.
v2.36.0
Add index price historical data endpoint.
v2.35.0
Add mark price historical data endpoint.
v2.34.0
Add average_funding_rate_24h to ticker API/subscription.
v2.33.0
Mass quote requests on exhausted protection groups are rejected.
v2.32.0
Expose order persistence in order responses and subscriptions.
v2.31.0
Add daily marks history endpoint (private/daily_mark_history). Trades of daily_mark type are deprecated.
v2.30.0
Add average_price to positions in portfolio breakdowns.
v2.29.0
Add realised_funding_24h to ticker API/subscription.
v2.28.0
Add implied_taker flag to recent trades subscription notifications and recent trades list in order book subscription notifications.
v2.27.0
Add private/cancel_mass_quote API call to cancel mass quotes across all sessions.
v2.26.0
Add trade_amount and quote_amount to market maker protection settings.
v2.25.0
Added min_order_size field for instruments.
v2.24.0
Add reject_post_only flag to mass quotes.
v2.23.0
Add mark price (m) to the lwt API/subscription.
v2.22.0
Support for non-transactable assets.
v2.21.0
Add total bid and ask amounts to orderbook subscriptions.
v2.20.0
Timestamps for mark and index prices are represented as floating point numbers for higher precision.
v2.19.0
Add roll contingency and cash position for d1 & options in margin breakdown.
v2.18.0
Increased maximum message rate for order cancellation requests over WebSocket.
v2.17.0
Add 'cancel_all_conditional_orders' API call to cancel all conditional orders of a subaccount.
v2.16.0
Unfilled non-persistent orders, that got canceled on the initiative of the exchange (e.g. on connection drop, matching engine failover, instrument deactivation, exchange admin actions) are now visible in the order history.
v2.15.0
Add required_margin_for_order API call to get a lightweight required margin breakdown with a proposed order.
v2.14.0
Add mark_timestamp to the ticker API/subscription, and timestamp to index API / subscription.
v2.13.0
Add id field to banners in public/system_info API call and banners subscription channel payload.
v2.12.0
Add public/instrument API call that allows retrieving information about a single instrument, including long expired ones.
v2.11.0
Add time field to order book API (public/book) and subscription channel payloads.
v2.10.0
Add open interest API.
v2.9.0
Margin breakdown now includes contingency margin requirements per scenario. Roll and short option contingency effect of open orders is now calculated per scenario.
Add collateral_factor to account_summary API.
v2.8.0
Add "single" category to recent trades feed.
Clarify that recent trades feed may be delayed compared to book feed.
Clarify that trade ticks in book feed will be snapshotted, but only as of gateway restart.
Remove documentation of snapshot flag for feeds that have no snapshot.
Added 1 minute (60000ms) to subscription intervals.
Perpetual funding rate value inverted, positive rate now means long pays short.
v2.7.0
Restrict labels to 64 chars and charset.
Remove RFQ counterparty selection.
Add client_order_id to trades.
Add maker_taker to trades and order fill items.
v2.6.0
Add reduce_only field to OrderStatus.
Add open_order flag to margin breakdown position.
Add subscription channel for index_components notifications.
v2.5.0
Subscription interval possible value can be one of 100ms, 200ms, 500ms, 1000ms, 5000ms or raw.
Market orders with collar=ignore are refused.
v2.4.0
Market maker protection must always be configured before mass quoting can take place.
Mass quote size may not exceed market maker protection size.
v2.3.0
The requirement that client_order_id can only be set on non-persistent sessions has been relaxed. Persistent websocket connections now also allow for continuous amend and delete through client_order_id.
RFQ functionality is included.
Introduced subscription channels for recent trades.
v2.2.0
Price collars are now active. By default, limit orders will be rejected if the limit price is in cross with the collar, and market orders will be clamped to the collar. The behaviour can be overridden with the collar field on insert and amend messages.
v2.1.0
Change output of public/all_instruments to include instruments expired up to 3 days ago. For expired instruments, add fields settlement_price and settlement_index_price.
Trade fees are now immediately realised, instead of accounted in entry price.
Expose new fields realised_position_pnl, realised_perpetual_funding, session_fees in portfolio position and account breakdown.
Add field funding_mark to trades.
Add field l (last price) to light-weight ticker.
Add field previous_settlement_price to index price.
Add endpoint public/index for a single index snapshot.
v2.0.0
Initial public release of Thalex APIs.