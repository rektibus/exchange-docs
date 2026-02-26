Ticker (Level 1)
CHANNEL
wss://ws.kraken.com/v2
ticker
The ticker channel streams level 1 market data, i.e. top of the book (best bid/offer) and recent trade data.

The feed accepts a list symbols for subscription and the updates are generated on trade events.

Subscribe Request
Subscribe Schema
Subscribe Ack Schema
Example: Subscribe
Example: Subscribe Ack
MESSAGE BODY
method
string
required
Value: subscribe
params
object
channel
string
required
Value: ticker
symbol
array of strings
required
Example: ["BTC/USD", "MATIC/GBP"]
A list of currency pairs.
event_trigger
string
Possible values: [bbo, trades]
Default value: trades
The book event that causes a new ticker update to be published on the channel.

bbo: on a change in the best-bid-offer price levels.
trades: on every trade.
snapshot
boolean
Possible values: [true, false]
Default value: true
Request a snapshot after subscribing.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.
Snapshot / Update Response
The snapshot and update responses share the same schema. An update message is streamed on a trade event.

Snapshot / Update Schema
Example: Snapshot
Example: Update
MESSAGE BODY
channel
string
Value: ticker
type
string
Possible values: [snapshot, update]
data
array [
[0] ticker
object
The ticker element is always the first and only item in the data payload.
ask
float
Best ask price.
ask_qty
float
Best ask quantity.
bid
float
Best bid price.
bid_qty
float
Best bid quantity.
change
float
24-hour price change (in quote currency).
change_pct
float
24-hour price change (in percentage points).
high
float
24-hour highest trade price.
last
float
Last traded price (only guaranteed if traded within the past 24 hours).
low
float
24-hour lowest trade price.
symbol
string
Example: "BTC/USD"
The symbol of the currency pair.
timestamp
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456Z
The ticker data timestamp.
volume
float
24-hour traded volume (in base currency terms).
vwap
float
24-hour volume weighted average price.

]
Unsubscribe Request
Unsubscribe Schema
Unsubscribe Ack Schema
Example: Unsubscribe
Example: Unsubscribe Ack
MESSAGE BODY
method
string
required
Value: unsubscribe
params
object
channel
string
required
Value: ticker
symbol
array of strings
required
Example: ["BTC/USD", "MATIC/GBP"]
A list of currency pairs.
event_trigger
string
Possible values: [bbo, trades]
Default value: trades
The book event that causes a new ticker update to be published on the channel.

bbo: on a change in the best-bid-offer price levels.
trades: on every trade.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.



Book (Level 2)
CHANNEL
wss://ws.kraken.com/v2
book
The book channel streams level 2 (L2) order book. It describes the individual price levels in the book with aggregated order quantities at each level.

Subscriptions to this channel can be made for multiple symbols at once by specifying a list of pairs in the symbol.

For more detail on maintaining the order book and generating a checksum, see guide.

Subscribe Request
Subscribe Schema
Subscribe Ack Schema
Example: Subscribe
Example: Subscribe Ack
MESSAGE BODY
method
string
required
Value: subscribe
params
object
channel
string
required
Value: book
symbol
array of strings
required
Example: ["BTC/USD", "MATIC/GBP"]
A list of currency pairs.
depth
integer
Possible values: [10, 25, 100, 500, 1000]
Default value: 10
The number of price levels to be received.
snapshot
boolean
Possible values: [true, false]
Default value: true
Request a snapshot after subscribing.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.
Snapshot Response
Snapshot Schema
Example
The returned snapshot data contains the specified number of bids and asks for the symbol including a CRC32 checksum of the top 10 bids and asks.

MESSAGE BODY
channel
string
Value: book
type
string
Value: snapshot
data
array [
[0] book
object
The book element is always the first and only item in the data payload.

asks
array [
[many] level
object
price
float
The ask price.
qty
float
The ask quantity.
]
bids
array [
[many] level
object
price
float
The bid price.
qty
float
The bid quantity.
]
checksum
integer
CRC32 checksum for the top 10 bids and asks.
symbol
string
Example: "BTC/USD"
The symbol of the currency pair.
timestamp
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456Z
The timestamp of the order book snapshot.
]
Update Response
The data contains the updates of the bids and asks for the relevant symbol including a CRC32 checksum of the top 10 bids and asks.

Note, it is possible to have multiple updates to the same price level in a single update message. Updates should always be processed in sequence.

Update Schema
Example
MESSAGE BODY
channel
string
Value: book
type
string
Value: update
data
array [
[0] book
object
The book element is always the first and only item in the data payload.

asks
array [
[many] level
object
price
float
The ask price.
qty
float
The ask quantity.
]
bids
array [
[many] level
object
price
float
The bid price.
qty
float
The bid quantity.
]
checksum
integer
CRC32 checksum for the top 10 bids and asks.
symbol
string
Example: "BTC/USD"
The symbol of the currency pair.
timestamp
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456Z
The book order update timestamp.
]
Unsubscribe Request
Unsubscribe Schema
Unsubscribe Ack Schema
Example: Unsubscribe
Example: Unsubscribe Ack
MESSAGE BODY
method
string
required
Value: unsubscribe
params
object
channel
string
required
Value: book
symbol
array of strings
required
Example: ["BTC/USD", "MATIC/GBP"]
A list of currency pairs.
depth
integer
Possible values: [10, 25, 100, 500, 1000]
The number of price levels to be unsubscribed.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.




Orders (Level 3)
CHANNEL
wss://ws-l3.kraken.com/v2
level3
Authentication Required
Summary
The level3 channel has an additional level of granularity over the book channel, it provides visibility of individual orders in the book.

L3 shows orders resting in the visible order book and it will never be crossed (i.e. no overlapping buy and sell orders). This feed excludes:

In-flight orders.
Unmatched market orders.
Untriggered stop-loss and take-profit orders.
Hidden quantity of iceberg orders.
For more detail on maintaining the order book and generating a checksum, see guide.

Subscription limits
The level3 channel is authenticated (i.e. it requires an API token to subscribe) and there are restrictions of the number of symbols and the subscription rate.

The total number of symbols per websocket connection is 200. A client can open multiple websockets connections to increase symbol coverage.
The subscription rate determined by client tier and order book depth. Standard rate count limit per second is 200 and the pro limit is 500.
The counter increase per book depth subscription is given in the table below.
Order Book Depth	Rate Counter Increase per Symbol
10	5
100	25
1000	100
**Example: ** Pro client can subscribe to 100 symbols of 10 depth every second.

Subscribe Request
Only one subscription to one depth level per symbol is supported, i.e. cannot subscribe to 10 levels and 1000 levels of "BTC/USD".

Subscribe Schema
Subscribe Ack Schema
Example: Subscribe
Example: Subscribe Ack
MESSAGE BODY
method
string
required
Value: subscribe
params
object
channel
string
required
Value: level3
symbol
array of strings
required
Example: ["BTC/USD", "MATIC/GBP"]
A list of currency pairs.
depth
integer
Possible values: [10, 100, 1000]
Default value: 10
The number of price levels to be received.
snapshot
boolean
Possible values: [true, false]
Default value: true
Request a snapshot after subscribing.
token
string
required
This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.
Snapshot Response
Snapshot Response
Example: Snapshot
MESSAGE BODY
channel
string
Value: level3
type
string
Value: snapshot
data
array [
[0] book
object
The book element is always the first and only item in the data payload.
symbol
string
Example: "BTC/USD"
The symbol of the currency pair.

bids
array [
A list of buy orders posted in the book.

[many] order
object
order_id
string
The Kraken order identifier of the order in the book
limit_price
float
Limit price of the order
order_qty
float
The remaining order quantity visible in the book
timestamp
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456789Z
The time the order was inserted or amended.
]
asks
array [
A list of sell orders posted in the book.

[many] order
object
order_id
string
The Kraken order identifier of the order in the book
limit_price
float
Limit price of the order
order_qty
float
The remaining order quantity visible in the book
timestamp
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456789Z
The time the order was inserted or amended.
]
checksum
integer
CRC32 checksum for the top 10 price levels on both sides.
timestamp
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456789Z
The time this market data message was generated in the matching engine.
]
Update Response
The updates will be streamed following the initial snapshot, no sequencing is required.
The L3 channel is not throttled, updates will be provided in the real-time.
If a price level is removed from the subscribed levels (i.e. result of trades/cancels) then all orders in the next available level will generate an add event.
Maintaining the book
After each update, the book should be truncated to your subscribed depth, there will be no delete event for price levels that fall out of scope. In other words, if you are subscribed with depth of 10 and an insert into the book results in 11 bids, you must remove the 11th worst bid.

Update Schema
Example
MESSAGE BODY
channel
string
Value: level3
type
string
Value: update
data
array [
[0] book
object
The book element is always the first and only item in the data payload.
symbol
string
Example: "BTC/USD"
The symbol of the currency pair.
timestamp
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456789Z
The time this market data message was generated in the matching engine.
checksum
integer
CRC32 checksum for the top 10 price levels on both sides.

bids
array [
A list of order events to the bid side of book.

[many] order_event
object
event
string
Possible values: [add, modify, delete]
The type of order event for this update:
add: A new order added to the book.
modify: The order quantity has been modified, i.e. a fill.
delete: The order has been removed from the book, i.e. full fill or cancel.
order_id
string
The Kraken order identifier of the order in the book
limit_price
float
Limit price of the order
order_qty
float
The remaining order quantity visible in the book
timestamp
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456789Z
The time the order was inserted or amended.
]
asks
array [
A list of order events to the ask side of book.

[many] order_event
object
event
string
Possible values: [add, modify, delete]
The type of order event for this update:
add: A new order added to the book.
modify: The order quantity has been modified, i.e. a fill.
delete: The order has been removed from the book, i.e. full fill or cancel.
order_id
string
The Kraken order identifier of the order in the book
limit_price
float
Limit price of the order
order_qty
float
The remaining order quantity visible in the book
timestamp
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456789Z
The time the order was inserted or amended.
]
]
Unsubscribe Request
Unsubscribe Schema
Unsubscribe Ack Schema
Example: Unsubscribe
Example: Unsubscribe Ack
MESSAGE BODY
method
string
required
Value: unsubscribe
params
object
channel
string
required
Value: level3
symbol
array of strings
required
Example: ["BTC/USD", "MATIC/GBP"]
A list of currency pairs.
depth
integer
Possible values: [10, 100, 1000]
Default value: 10
The number of price levels to be received.
token
string
required
This is a authenticated channel, a session token is required. See guides on how to generate a token via REST.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.



Candles (OHLC)
CHANNEL
wss://ws.kraken.com/v2
ohlc
The ohlc channel streams the Open, High, Low and Close (OHLC) data for the specific interval period.

The feed accepts a list symbols for subscription and the updates are generated on trade events.

Subscribe Request
There is an acknowledgement response for each symbol in the subscription list.

Subscribe Schema
Subscribe Ack Schema
Example: Subscribe
Example: Subscribe Ack
MESSAGE BODY
method
string
required
Value: subscribe
params
object
channel
string
required
Value: ohlc
symbol
array of strings
required
Example: ["BTC/USD", "MATIC/GBP"]
A list of currency pairs.
interval
integer
Possible values: [1, 5, 15, 30, 60, 240, 1440, 10080, 21600]
The interval timeframe in minutes.
snapshot
boolean
Possible values: [true, false]
Default value: true
Request a snapshot after subscribing.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.
Snapshot and Update Response
The snapshot and update responses share the same schema. An update message is streamed on a trade event.

Response Schema
Example: Snapshot
Example: Update
MESSAGE BODY
channel
string
Value: ohlc
type
string
Possible values: [snapshot, update]
data
array [
A list of candle events.

[many] candle
object
symbol
string
Example: "BTC/USD"
The symbol of the currency pair.
open
float
The opening trade price within the interval.
high
float
The highest trade price within the interval.
low
float
The lowest trade price within the interval.
close
float
The last trade price within the interval.
vwap
float
Volume weighted average trade price within the interval.
trades
float
Number of trades within the interval.
volume
float
Total traded volume (in base currency terms) within the interval.
interval_begin
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456Z
The timestamp of start of the interval.
interval
integer
The timeframe from the interval in minutes.
timestamp
string
deprecated
Deprecated Usage: Use 'interval_begin'.
Format: RFC3339
Example: 2022-12-25T09:30:59.123456Z
The timestamp of start of the interval.
]
Unsubscribe Request
There is an acknowledgement response for each symbol in the unsubscribe list.

Unsubscribe Schema
Unsubscribe Ack Schema
Example: Unsubscribe
Example: Unsubscribe Ack
MESSAGE BODY
method
string
required
Value: unsubscribe
params
object
channel
string
required
Value: ohlc
symbol
array of strings
required
Example: ["BTC/USD", "MATIC/GBP"]
A list of currency pairs.
interval
integer
Possible values: [1, 5, 15, 30, 60, 240, 1440, 10080, 21600]
The interval timeframe in minutes.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.



Trades
CHANNEL
wss://ws.kraken.com/v2
trade
The trade channel generates a trade event when orders are matched in the book.

Multiple trades may be batched in a single message but that does not mean that these trades resulted from a single taker order.

The feed accepts a list symbols for subscription.

Subscribe Request
Subscribe Schema
Subscribe Ack Schema
Example: Subscribe
Example: Subscribe Ack
MESSAGE BODY
method
string
required
Value: subscribe
params
object
channel
string
required
Value: trade
symbol
array of strings
required
Example: ["BTC/USD", "MATIC/GBP"]
A list of currency pairs.
snapshot
boolean
Possible values: [true, false]
Default value: false
Request a snapshot after subscribing.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.
Snapshot and Update Response
The snapshot and update responses share the same schema. An update message is streamed on a trade event.

The snapshot reflects the most recent 50 trades.

Response Schema
Example: Snapshot
Example: Update
MESSAGE BODY
channel
string
Value: trade
type
string
Possible values: [snapshot, update]
data
array [
A list of trade events.

[many] trade
object
symbol
string
Example: "BTC/USD"
The symbol of the currency pair.
side
string
The side of the taker order.
qty
float
Size of the trade.
price
float
Average price of the trade.
ord_type
string
Possible values: [limit, market]
The order type of the taker order.
trade_id
integer
Trade identifier is a sequence number, unique per book.
timestamp
string
Format: RFC3339
Example: 2022-12-25T09:30:59.123456Z
The book order update timestamp.
]
Unsubscribe Request
Unsubscribe Schema
Unsubscribe Ack Schema
Example: Unsubscribe
Example: Unsubscribe Ack
MESSAGE BODY
method
string
required
Value: unsubscribe
params
object
channel
string
required
Value: trade
symbol
array of strings
required
Example: ["BTC/USD", "MATIC/GBP"]
A list of currency pairs.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.



Instruments
CHANNEL
wss://ws.kraken.com/v2
instrument
The instrument channel provides a stream of reference data of all active assets and tradeable pairs.

It provides the symbol identifiers, precisions, trading parameters and rules.

Subscribe Request
Subscribe Schema
Example: Subscribe
Subscribe Ack Schema
Example: Subscribe Ack
MESSAGE BODY
method
string
required
Value: subscribe
params
object
channel
string
required
Value: instrument
include_tokenized_assets
boolean
Possible values: [false, true]
Default value: false
If true, include xStocks in the response, otherwise include crypto spot pairs only.

snapshot
boolean
Possible values: [true, false]
Default value: true
Request a snapshot after subscribing.
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.
Snapshot / Update Responses
The snapshot and update responses share the same schema.

Snapshot / Update Schema
Example: Snapshot
Example: Update
MESSAGE BODY
channel
string
Value: instrument
type
string
Possible values: [snapshot, update]
data
object
assets
array [
A list of assets.

[many] asset
object
borrowable
boolean
Possible values: [true, false]
Flag if asset is borrowable.
collateral_value
float
Valuation as margin collateral (if applicable).
id
string
Asset identifier.
margin_rate
float
Interest rate to borrow the asset.
precision
integer
Maximum precision for asset ledger, balances.
precision_display
integer
Recommended display precision.
multiplier
float
Multiplier of the tokenised asset. Fixed conversion rate of the token .
status
string
Possible values: [depositonly, disabled, enabled, fundingtemporarilydisabled, withdrawalonly, workinprogress]
Status of asset.
]
pairs
array [
A list of pairs.

[many] pair
object
base
string
Asset identifier of the base currency.
quote
string
Asset identifier of the quote currency.
cost_min
string
Minimum cost (price * qty) for new orders.
cost_precision
integer
Maximum precision used for cost prices.
has_index
boolean
Whether the pair has an index available for example stop-loss triggers.
margin_initial
float
conditional
Condition: On marginable pairs only
Initial margin requirement (in percent).
marginable
boolean
Possible values: [true, false]
Whether the pair can be traded on margin.
position_limit_long
integer
conditional
Condition: On marginable pairs only
Limit for long positions.
position_limit_short
integer
conditional
Condition: On marginable pairs only
Limit for short positions.
price_increment
float
Minimum price increment for new orders.
price_precision
integer
Maximum precision used for order prices.
qty_increment
float
Minimum quantity increment for new orders.
qty_min
float
Minimum quantity (in base currency) for new orders.
qty_precision
integer
Maximum precision used for order quantities.
status
string
Possible values: [cancel_only, delisted, limit_only, maintenance, online, post_only, reduce_only, work_in_progress]
Status of pair.
symbol
string
Example: "BTC/USD"
The symbol of the currency pair.
tick_size
float
deprecated
Deprecated Usage: Use 'price_increment'.
Minimum price increment for new orders.
]
Unsubscribe Request
Unsubscribe Schema
Example: Unsubscribe
Unsubscribe Ack Schema
Example: Unsubscribe Ack
MESSAGE BODY
method
string
required
Value: unsubscribe
params
object
channel
string
required
Value: instrument
req_id
integer
Optional client originated request identifier sent as acknowledgment in the response.



Status
CHANNEL
wss://ws.kraken.com/v2
status
The status channel provides a mechanism to verify exchange status and successful initial connection.

There is no option to directly request a status update, a status will be automatically generated on successful websocket connection and when the trading engine status changes.

Update Response
Update Schema
Example
MESSAGE BODY
channel
string
Value: status
type
string
Value: update
data
array [
[0] status
object
The status element is always the first and only item in the data payload.

system
string
Possible values: [online, cancel_only, maintenance, post_only]
The status of the trading engine.

online: Markets are operating normally - all order types may be submitted and order matching can occur.
maintenance: Markets are offline for scheduled maintenance - new orders cannot be placed and existing orders cannot be cancelled.
cancel_only: Orders can be cancelled but new orders cannot be placed. No order matching will occur.
post_only: Only limit orders using the post_only option can be submitted. Orders can be cancelled. No order matching will occur.
api_version
string
Value: v2
The version of the websockets API.
connection_id
integer
A unique connection identifier (for debugging).
version
string
The version of the websockets service.
]


Heartbeat
CHANNEL
wss://ws.kraken.com/v2
heartbeat
The heartbeat channel provides a mechanism to verify that the connection is alive.

Heartbeat messages are sent approximately once every second in the absence of any other channel updates.

There is no option to directly request a heartbeat subscription, the heartbeats will be automatically generated on subscription to any channel.

Update Response
The channel name is the indicator of a heartbeat, here is no other data in the heartbeat payload.

Update Response
Example
MESSAGE BODY
channel
string
heartbeat




