# Kraken API Documentation



--------------------------------
# URL: https://docs.kraken.com/api/docs/category/rest-api/earn/
--------------------------------
class="margin-top--lg">
## 📄️ Allocate Earn Funds

Allocate funds to the Strategy.

--------------------------------
# URL: https://docs.kraken.com/api/docs/category/rest-api/funding/
--------------------------------
class="margin-top--lg">
## 📄️ Get Deposit Methods

Retrieve methods available for depositing a particular asset.

--------------------------------
# URL: https://docs.kraken.com/api/docs/category/rest-api/market-data/
--------------------------------
class="margin-top--lg">
## 📄️ Get Server Time

Get the server's time.

--------------------------------
# URL: https://docs.kraken.com/api/docs/category/rest-api/subaccounts/
--------------------------------
class="margin-top--lg">
## 📄️ Create Subaccount

Create a trading subaccount. **Note:** `CreateSubaccount` must be called using an API key from the master account.

--------------------------------
# URL: https://docs.kraken.com/api/docs/category/rest-api/trading/
--------------------------------
class="margin-top--lg">
## 📄️ Add Order

Place a new order.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/account-transfer/
--------------------------------
>
# Account Transfer

POST 
## /private/AccountTransfer

Transfer funds to and from master and subaccounts. Note:  must be called using an API key from the master account.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Funds transferred between accounts.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/add-export/
--------------------------------
>
# Request Export Report

POST 
## /private/AddExport

Request export of trades or ledgers.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Export request made

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/add-order-batch/
--------------------------------
>
# Add Order Batch

POST 
## /private/AddOrderBatch

Sends a collection of orders (minimum of 2 and maximum 15):

- Validation is performed on the whole batch prior to submission to the engine. If an order fails validation, the whole batch will be rejected.

- On submission to the engine, if an order fails pre-match checks (i.e. funding), then the individual order will be rejected and remainder of the batch will be processed.

- All orders in batch are limited to a single pair.

Note: See the AssetPairs endpoint for details on the available trading pairs, their price and quantity precisions, order minimums, available leverage, etc.

API Key Permissions Required:  and 

## Request​

## Responses​
- 200

The order of returned  in the response array is the same as the order of the order list sent in request.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/add-order/
--------------------------------
>
# Add Order

POST 
## /private/AddOrder

Place a new order.

Note: See the AssetPairs endpoint for details on the available trading pairs, their price and quantity precisions, order minimums, available leverage, etc.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Order added.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/allocate-strategy/
--------------------------------
>
# Allocate Earn Funds

POST 
## /private/Earn/Allocate

Allocate funds to the Strategy.

Requires the  API key permission.
The amount must always be defined.

This method is asynchronous. A couple of preflight checks are
performed synchronously on behalf of the method before it is dispatched
further. The client is required to poll
the result using the  endpoint.

There can be only one (de)allocation request in progress for given user and
strategy at any time. While the operation is in progress:

-  attribute in  response for the strategy
indicates that funds are being allocated,

-  attribute in  response will be true.

Following specific errors within  class can be returned by this
method:

- Minimum allocation: 

- Allocation in progress: 

- Service temporarily unavailable: . Try again in a few minutes.

- User tier verification: 

- Strategy not found: 

## Request​

## Responses​
- 200

Response

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/amend-order/
--------------------------------
>
# Amend Order

POST 
## /private/AmendOrder

The amend request enables clients to modify the order parameters in-place without the need to cancel the existing order and create a new one.

- The order identifiers assigned by Kraken and/or client will stay the same.

- Queue priority in the order book will be maintained where possible.

- If an amend request will reduce the order quantity below the existing filled quantity, the remaining quantity will be cancelled.

For more detail, see amend transaction guide.

API Key Permissions Required:  or 

## Request​

## Responses​
- 200

A successful amend request will return the unique Kraken amend identifier.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/cancel-order-batch/
--------------------------------
>
# Cancel Order Batch

POST 
## /private/CancelOrderBatch

Cancel multiple open orders  by ,  or (maximum 50 total unique IDs/references)

API Key Permissions Required:  or 

## Request​

## Responses​
- 200

Open order cancelled.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/cancel-order/
--------------------------------
>
# Cancel Order

POST 
## /private/CancelOrder

Cancel a particular open order (or set of open orders) by ,  or 

API Key Permissions Required:  or 

## Request​

## Responses​
- 200

Open order cancelled.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/create-subaccount/
--------------------------------
>
# Create Subaccount

POST 
## /private/CreateSubaccount

Create a trading subaccount. Note:  must be called using an API key from the master account.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Subaccount created.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/deallocate-strategy/
--------------------------------
>
# Deallocate Earn Funds

POST 
## /private/Earn/Deallocate

Deallocate funds from a strategy.

Requires the  API key permission.
The amount must always be defined.

This method is asynchronous. A couple of preflight checks are
performed synchronously on behalf of the method before it is dispatched
further. If the method returns HTTP 202 code, the client is required to poll
the result using the  endpoint.

There can be only one (de)allocation request in progress for given user and
strategy.  While the operation is in progress:

-  attribute in  response for the strategy will hold
the amount that is being deallocated (negative amount)

-  attribute in  response will be true.

Following specific errors within  class can be returned by this
method:

- Minimum allocation: 
allowed

- Allocation in progress: 

- Strategy not found: 

## Request​

## Responses​
- 200

Response

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/edit-order/
--------------------------------
>
# Edit Order

POST 
## /private/EditOrder

Sends a request to edit the order parameters of a live order. When an order has been successfully modified, the original order will be cancelled and a new order will be
created with the adjusted parameters a new  will be returned in the response.

> [note]
> 
The new AmendOrder endpoint resolves the caveats listed below and has additional performance gains.

There are a number of caveats for :

- triggered stop loss or profit take profit orders are not supported.

- orders with conditional close terms attached are not supported.

- orders where the executed volume is greater than the newly supplied volume will be rejected.

-  is not supported.

- existing executions will are associated with the original order and not copied to the amended order.

- queue position will not be maintained.

API Key Permissions Required:  and 

## Request​

## Responses​
- 200

Order edited.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/export-status/
--------------------------------
>
# Get Export Report Status

POST 
## /private/ExportStatus

Get status of requested data exports.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Export status retrieved

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-account-balance/
--------------------------------
>
# Get Account Balance

POST 
## /private/Balance

Retrieve all cash balances, net of pending withdrawals.

Note on Staking/Earn assets: We have begun to migrate assets from our legacy Staking system over to a new Earn system. As such, the following assets may appear in your balances and ledger. Please see our Support article for more details. Note that these assets are "read-only", to interact with your balances in them please use the base asset (e.g.  to transact with your  and  balances).

Symbol Extensions:

- : balances in new yield-bearing products, similar to  (staked) and  (opt-in rewards) balances

- : balances earning automatically in Kraken Rewards

- : tokenized assets.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Account balances retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-allocate-strategy-status/
--------------------------------
>
# Get Allocation Status

POST 
## /private/Earn/AllocateStatus

Get the status of the last allocation request.

Requires either the  or  API key permission.

(De)allocation operations are asynchronous and this endpoint allows client
to retrieve the status of the last dispatched operation. There can be only
one (de)allocation request in progress for given user and strategy.

The  attribute in the response indicates if the previously
dispatched operation is still in progress (true) or has successfully
completed (false).  If the dispatched request failed with an error, then
HTTP error is returned to the client as if it belonged to the original
request.

Following specific errors within  class can be returned by this
method:

- Insufficient funds: 

- User cap exceeded: 

- Total cap exceeded: 

- Minimum allocation: 

## Request​

## Responses​
- 200

Response

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-asset-info/
--------------------------------
>
# Get Asset Info

GET 
## /public/Assets

Get information about the assets that are available for deposit, withdrawal, trading and earn.

## Request​

## Responses​
- 200

Asset info retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-closed-orders/
--------------------------------
>
# Get Closed Orders

POST 
## /private/ClosedOrders

Retrieve information about orders that have been closed (filled or cancelled). 50 results are returned at a time, the most recent by default.

Note: If an order's tx ID is given for  or  time, the order's opening time () is used

API Key Permissions Required: 

## Request​

## Responses​
- 200

Closed orders info retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-deallocate-strategy-status/
--------------------------------
>
# Get Deallocation Status

POST 
## /private/Earn/DeallocateStatus

Get the status of the last deallocation request.

Requires either the  or  API key permission.

(De)allocation operations are asynchronous and this endpoint allows client
to retrieve the status of the last dispatched operation. There can be only
one (de)allocation request in progress for given user and strategy.

The  attribute in the response indicates if the previously
dispatched operation is still in progress (true) or has successfully
completed (false).  If the dispatched request failed with an error, then
HTTP error is returned to the client as if it belonged to the original
request.

Following specific errors within  class can be returned by this
method:

- Insufficient funds: 

- Minimum allocation: 

## Request​

## Responses​
- 200

Response

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-deposit-addresses/
--------------------------------
>
# Get Deposit Addresses

POST 
## /private/DepositAddresses

Retrieve (or generate a new) deposit addresses for a particular asset and method.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Deposit addresses retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-deposit-methods/
--------------------------------
>
# Get Deposit Methods

POST 
## /private/DepositMethods

Retrieve methods available for depositing a particular asset.

API Key Permissions Required:  and 

## Request​

## Responses​
- 200

Deposit methods retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-ledgers-info/
--------------------------------
>
# Query Ledgers

POST 
## /private/QueryLedgers

Retrieve information about specific ledger entries.

Note on Staking/Earn assets: We have begun to migrate assets from our legacy Staking system over to a new Earn system. As such, the following assets may appear in your balances and ledger. Please see our Support article for more details. Note that these assets are "read-only", to interact with your balances in them please use the base asset (e.g.  to transact with your  and  balances).

- , which represents balances in new yield-bearing products, similar to  (staked) and  (opt-in rewards) balances

- , which represents balances earning automatically in Kraken Rewards

API Key Permissions Required: 

## Request​

## Responses​
- 200

Ledgers info retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-ledgers/
--------------------------------
>
# Get Ledgers Info

POST 
## /private/Ledgers

Retrieve information about ledger entries. 50 results are returned at a time, the most recent by default.

Note on Staking/Earn assets: We have begun to migrate assets from our legacy Staking system over to a new Earn system. As such, the following assets may appear in your balances and ledger. Please see our Support article for more details. Note that these assets are "read-only", to interact with your balances in them please use the base asset (e.g.  to transact with your  and  balances).

- , which represents balances in new yield-bearing products, similar to  (staked) and  (opt-in rewards) balances

- , which represents balances earning automatically in Kraken Rewards

API Key Permissions Required: 

## Request​

## Responses​
- 200

Ledgers info retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-ohlc-data/
--------------------------------
>
# Get OHLC Data

GET 
## /public/OHLC

Retrieve OHLC market data.
The last entry in the OHLC array is for the current, not-yet-committed timeframe, and will always be present, regardless of the value of .
Returns up to 720 of the most recent entries (older data cannot be retrieved, regardless of the value of ).

## Request​

## Responses​
- 200

OHLC data retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-open-orders/
--------------------------------
>
# Get Open Orders

POST 
## /private/OpenOrders

Retrieve information about currently open orders.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Open orders info retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-open-positions/
--------------------------------
>
# Get Open Positions

POST 
## /private/OpenPositions

Get information about open margin positions.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Open positions info retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-order-amends/
--------------------------------
>
# Get Order Amends

POST 
## /private/OrderAmends

Retrieves an audit trail of amend transactions on the specified order. The list is ordered by ascending amend timestamp.

API Key Permissions Required:  or , depending on status of order.

## Request​

## Responses​
- 200

The first entry contains the original order parameters and has amend_type of .

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-order-book/
--------------------------------
>
# Get Order Book

GET 
## /public/Depth

Returns level 2 (L2) order book, which describes the individual price levels in the book with aggregated order quantities at each level.

## Request​

## Responses​
- 200

Order book entries retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-orders-info/
--------------------------------
>
# Query Orders Info

POST 
## /private/QueryOrders

Retrieve information about specific orders.

API Key Permissions Required:  or , depending on status of order

## Request​

## Responses​
- 200

Orders info retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-recent-spreads/
--------------------------------
>
# Get Recent Spreads

GET 
## /public/Spread

Returns the last ~200 top-of-book spreads for a given pair

## Request​

## Responses​
- 200

Spread data retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-recent-trades/
--------------------------------
>
# Get Recent Trades

GET 
## /public/Trades

Returns the last 1000 trades by default

## Request​

## Responses​
- 200

Trade data retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-server-time/
--------------------------------
>
# Get Server Time

GET 
## /public/Time

Get the server's time.

## Responses​
- 200

Success response

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-status-recent-deposits/
--------------------------------
>
# Get Status of Recent Deposits

POST 
## /private/DepositStatus

Retrieve information about recent deposits. Results are sorted by recency, use the  parameter to iterate through list of deposits (page size equal to value of ) from newest to oldest.
API Key Permissions Required: 

## Request​

## Responses​
- 200

Recent deposits retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-status-recent-withdrawals/
--------------------------------
>
# Get Status of Recent Withdrawals

POST 
## /private/WithdrawStatus

Retrieve information about recent withdrawals. Results are sorted by recency, use the  parameter to iterate through list of withdrawals (page size equal to value of ) from newest to oldest.

API Key Permissions Required:  or 

## Request​

## Responses​
- 200

Recent withdrawals retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-system-status/
--------------------------------
>
# Get System Status

GET 
## /public/SystemStatus

Get the current system status or trading mode.

## Responses​
- 200

Success response

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-ticker-information/
--------------------------------
>
# Get Ticker Information

GET 
## /public/Ticker

Get ticker information for all or requested markets. To clarify usage, note that

- Today's prices start at midnight UTC

- Leaving the pair parameter blank will return tickers for all tradeable assets on Kraken

## Request​

## Responses​
- 200

Ticker info retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-tradable-asset-pairs/
--------------------------------
>
# Get Tradable Asset Pairs

GET 
## /public/AssetPairs

Get tradable asset pairs

## Request​

## Responses​
- 200

Tradable asset pairs retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-trade-balance/
--------------------------------
>
# Get Trade Balance

POST 
## /private/TradeBalance

Retrieve a summary of collateral balances, margin position valuations, equity and margin level.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Trade balances retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-trade-history/
--------------------------------
>
# Get Trades History

POST 
## /private/TradesHistory

Retrieve information about trades/fills. 50 results are returned at a time, the most recent by default.

- Unless otherwise stated, costs, fees, prices, and volumes are specified with the precision for the asset pair ( and ), not the individual assets' precision ().

API Key Permissions Required: 

## Request​

## Responses​
- 200

Trade history retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-trade-volume/
--------------------------------
>
# Get Trade Volume

POST 
## /private/TradeVolume

Returns 30 day USD trading volume and resulting fee schedule for any asset pair(s) provided. Fees will not be included if  is not specified as Kraken fees differ by asset pair.
Note: If an asset pair is on a maker/taker fee schedule, the taker side is given in  and maker side in . For pairs not on maker/taker, they will only be given in .

API Key Permissions Required: 

## Request​

## Responses​
- 200

Trade Volume retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-trades-info/
--------------------------------
>
# Query Trades Info

POST 
## /private/QueryTrades

Retrieve information about specific trades/fills.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Trades info retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-websockets-token/
--------------------------------
>
# Get Websockets Token

POST 
## /private/GetWebSocketsToken

An authentication token must be requested via this REST API endpoint in order to connect to and authenticate with our Websockets API. The token should be used within 15 minutes of creation, but it does not expire once a successful Websockets connection and private subscription has been made and is maintained.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Websockets token retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-withdrawal-addresses/
--------------------------------
>
# Get Withdrawal Addresses

POST 
## /private/WithdrawAddresses

Retrieve a list of withdrawal addresses available for the user.

API Key Permissions Required:  and 

## Request​

## Responses​
- 200

Withdrawal addresses retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-withdrawal-information/
--------------------------------
>
# Get Withdrawal Information

POST 
## /private/WithdrawInfo

Retrieve fee information about potential withdrawals for a particular asset, key and amount.

API Key Permissions Required:  and 

## Request​

## Responses​
- 200

Withdrawal information retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/get-withdrawal-methods/
--------------------------------
>
# Get Withdrawal Methods

POST 
## /private/WithdrawMethods

Retrieve a list of withdrawal methods available for the user.

API Key Permissions Required:  and 

## Request​

## Responses​
- 200

Withdrawal methods retrieved.

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/list-allocations/
--------------------------------
>
# List Earn Allocations

POST 
## /private/Earn/Allocations

List all allocations for the user.

Requires the  API key permission.

By default all allocations are returned, even for strategies that have been
used in the past and have zero balance now. That is so that the user can see
how much was earned with given strategy in the past.
 parameter can be used to remove zero balance entries
from the output.  Paging hasn't been implemented for this method as we don't
expect the result for a particular user to be overwhelmingly large.

All amounts in the output can be denominated in a currency of user's choice
(the  parameter).

Information about when the next reward will be paid to the client is also
provided in the output.

Allocated funds can be in up to 4 states:

- bonding

- allocated

- exit_queue (ETH only)

- unbonding

Any funds in  not in / are simply allocated and
earning rewards. Depending on the strategy funds in the other 3 states can
also be earning rewards. Consult the output of  to know
whether / earn rewards.  in  still
earns rewards.

Note that for , when the funds are in the  state, the
 time given is the time when the funds will have finished
unbonding, not when they go from exit queue to unbonding.

(Un)bonding time estimate can be inaccurate right after having (de)allocated the
funds. Wait 1-2 minutes after (de)allocating to get an accurate result.

## Request​

## Responses​
- 200

Response

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/list-strategies/
--------------------------------
>
# List Earn Strategies

POST 
## /private/Earn/Strategies

List earn strategies along with their parameters.

Requires a valid API key but not specific permission is required.

Returns only strategies that are available to the user
based on geographic region.

When the user does not meet the tier restriction,  will be
false and  indicates  as the restriction
reason. Earn products generally require Intermediate tier. Get your account verified
to access earn.

A note about :

- : can be deallocated without an unbonding period. This is called flexible in the UI.

- : has an unbonding period. Deallocation will not happen until this period has passed.

- : "Kraken rewards". This is earning on your spot balances where eligible. It's turned on account wide
from the UI and you cannot manually allocate to these strategies.

Paging isn't yet implemented, so the endpoint always returns all
data in the first page.

## Request​

## Responses​
- 200

Response

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/remove-export/
--------------------------------
>
# Delete Export Report

POST 
## /private/RemoveExport

Delete exported trades/ledgers report

API Key Permissions Required: 

## Request​

## Responses​
- 200

Export report deleted or cancelled

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/retrieve-export/
--------------------------------
>
# Retrieve Data Export

POST 
## /private/RetrieveExport

Retrieve a processed data export

API Key Permissions Required: 

## Request​

## Responses​
- 200

Data export report retrieved

--------------------------------
# URL: https://docs.kraken.com/api/docs/rest-api/withdraw-funds/
--------------------------------
>
# Withdraw Funds

POST 
## /private/Withdraw

Make a withdrawal request.

API Key Permissions Required: 

## Request​

## Responses​
- 200

Withdrawal created.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/add_order/
--------------------------------
>
# Add Order

REQUEST
## wss://ws-auth.kraken.com/v2
add_orderAuthentication RequiredSends a single, new order into the exchange. A range of order types, Time-In-Force (TIF) and order flags can be specified by the parameters below.

For triggered order types (, , ), the  section contains the parameters for price tracking and trigger thresholds.

For One-Triggers-Other (OTO) orders, the  section contains the parameters to add a secondary close order to the primary order.

## Request​
- Request Schema
- Example: Limit
- Example: Stop Loss
- Example: OTO

### MESSAGE BODY
method string requiredValue:  params object order_type string requiredPossible values: [, , , , , , , , , ] 
The execution model of the order.
- : The full order quantity executes immediately at the best available price in the order book.
- : The full order quantity is placed immediately with a limit price restriction to only trade at this price or better. 
- : A market order is triggered when the reference price reaches the stop price (from an unfavourable direction).
- : A limit order is triggered when the reference price reaches the stop price (from an unfavourable direction).
- : A market order is triggered when the reference price reaches the stop price (from an favourable direction).
- : A limit order is triggered when the reference price reaches the stop price (from an favourable direction).
- : A market order is triggered when the market reverts a specified distance from the peak price.
- : A limit order is triggered when the market reverts a specified distance from the peak price.
- : Hides the full order size by only showing your chosen display size in the book at your limit price.
side string requiredPossible values: [, ]  Side of the order.order_qty float required Order quantity in terms of the base asset.symbol string requiredExample: "BTC/USD"The symbol of the currency pair.limit_price float Limit price for order types that support limit price restriction.limit_price_type string conditionalCondition:  Only available on trailing-stop-limit orders. Possible values: [, , ] Default value: 
The units for the limit price.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price

Note, for  order type, the value represents offset from the trigger price. 0 would set a limit price the same as the trigger price.
triggers object conditionalCondition:  Required for triggered order types only. 
The parameters for setting the trigger price conditions.
reference string Possible values: [, ] Default value: 
The reference price to track for triggering orders.
- : the index price in the broader market (for this pair). Note, to keep triggers serviceable during connectivity issues with external index feeds, the last price will be used as the reference price.
- : the last traded price in the Kraken order book (for this pair).
price float required
Specifies the amount for the trigger price - it supports both static market prices and relative prices.
This field is used in combination with the  field below to determine the effective trigger price.
Examples:
- To trigger at 29000.5 BTC/USD, use price=29000.5, price_type=static.
- To trigger when price rises by 5%, use price=5, price_type=pct.
- To trigger when price drops by 150 USD, use price=-150, price_type=quote.
price_type string Possible values: [, , ] Default value: 
The units for the trigger price.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price

Note, for  and  order types, the price represents the reversion from the peak. It is always a positive value with  or  offset.
time_in_force string Possible values: [, , ] Default value: 
Time-in-force specifies how long an order remains in effect before being expired.
- : Good Till Canceled - until user has cancelled.
- : Good Till Date - until  parameter.
- : Immediate Or Cancel - immediately cancels back any quantity that cannot be filled on arrival.
margin boolean Possible values: [, ] Default value: Funds the order on margin using the maximum leverage for the pair (maximum is leverage of 5).post_only boolean conditionalCondition:  Orders with limit price only. Possible values: [, ] Default value: 
Cancels the order if it will take liquidity on arrival. Post only orders will always be posted passively in the book.
reduce_only boolean Possible values: [, ] Default value: 
Reduces an existing margin position without opening an opposite long or short position worth more than the current value of your leveraged assets.
effective_time string Format: RFC3339Example: 2022-12-25T09:30:59ZScheduled start time (precision to seconds).expire_time string conditionalCondition:  GTD orders only. Format: RFC3339Example: 2022-12-25T09:30:59ZExpiration time of the order (precision to seconds). GTD orders can have an expiry time up to one month in future.deadline string Format: RFC3339Example: 2022-12-25T09:30:59.123Z
Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond.
The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.
cl_ord_id string 

Adds a alphanumeric client order identifier which uniquely identifies an open order for each client. This field is mutually exclusive with  parameter.

The  parameter can be one of the following formats:

- Long UUID:  32 hex characters separated with 4 dashes.
- Short UUID:  32 hex characters with no dashes.
- Free text:  Free format ascii text up to 18 characters.
order_userref integer 

This is an optional non-unique, numeric identifier which can associated with a number of orders by the client. This field is mutually exclusive with  parameter.

Many clients choose a unique integer value generated by their systems (i.e. a timestamp). However, because we don't enforce uniqueness on our side, it can also be used to easily tag a group of orders for querying or cancelling.

conditional object 
The conditional parameters are used as a template for generating the secondary close orders when the primary order fills. Each fill on the primary order will generate a new secondary order.
The size of the secondary order will be the same size as the executed quantity and have the opposite side.
order_type string Possible values: [, , , , , , ] 
Defines the order type of the secondary close orders which will be created on each fill.
limit_price float 
Defines the limit price on the secondary close orders. Only required on secondary order types that support limit price: , , .
limit_price_type string conditionalCondition:  Only available on trailing-stop-limit orders. Possible values: [, , ] Default value: 
The units for the limit price on the secondary order.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price

Note, for  order type, the value represents offset from the trigger price. 0 would set a limit price the same as the trigger price.
trigger_price float 
Specifies the amount for the trigger price - it supports both static market prices and relative prices.
This field is used in combination with the  field below to determine the effective trigger price.
Examples:
- To trigger at 29000.5 BTC/USD, use price=29000.5, price_type=static.
- To trigger when price rises by 5%, use price=5, price_type=pct.
- To trigger when price drops by 150 USD, use price=-150, price_type=quote.

Note, for  and  order types, the price represents the reversion from the peak. It is always a positive offset value.
trigger_price_type string Possible values: [, , ] Default value: 
The units for the trigger price.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price
stop_price float deprecatedDeprecated Usage: Use trigger_price
Defines the trigger price on the secondary close orders. Only required on triggered secondary order types: , , , .
display_qty float conditionalCondition:  iceberg orders only. 
Defines the quantity to show in the book while the rest of order quantity remains hidden.
Minimum value is 1 / 15 of .
fee_preference string Possible values: [, ] 
Fee preference base or quote currency.  is the default for buy orders,  is the default for sell orders.
no_mpp boolean deprecatedDeprecated Usage: If supplied, the flag is accepted but ignored.Possible values: [, ] Default value: 
Disables Market Price Protection (MPP) if set to . MPP is a feature that protects market orders from filling at a bad price due to price slippage in an illiquid or volatile market. See MPP support article.
stp_type string Possible values: [, , ] Default value: 
Self Trade Prevention (STP) is a protection feature to prevent users from inadvertently or deliberately trading against themselves.
To prevent a self-match, one of the following STP modes can be used to define which order(s) will be expired:
- : arriving order will be canceled.
- : resting order will be canceled.
- : both arriving and resting orders will be canceled.
cash_order_qty float conditionalCondition:  Buy market orders without margin funding. Order volume expressed in quote currency.validate boolean Possible values: [, ] Default value: 
If set to  the order will be validated only, it will not trade in the matching engine.
sender_sub_id string conditionalCondition:  For institutional accounts with enhanced Self Trade Prevention (STP) 

Adds a alphanumeric sub-account/trader identifier which enables STP to be performed at a more granular level.

The  parameter can be one of the following formats:

- Long UUID:  32 hex characters separated with 4 dashes.
- Short UUID:  32 hex characters with no dashes.
- Free text:  Free format ascii text up to 18 characters.
stop_price float deprecatedDeprecated Usage: Use 'triggers' object. The stop price for trigger order types.trigger string deprecatedDeprecated Usage: Use 'triggers' object.Possible values: [, ] Default value: 
The reference price to trigger the order.
- : the index price for the broader market for this symbol.
- : the last traded price in the order book for this symbol.
token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
Create a simple buy order with a limit price.

Create a sell stop-loss order to trigger when the market drops 2% from last price.

A more detailed example, create a limit price order to buy 1.2 BTC at 28440 USD and create a secondary stop-loss order
to sell 1.2 BTC when the price drops below 28410 USD. The stop-loss order has a limit price restriction to not trade below 28400 USD.

## Response​
- Response Schema
- Example

### MESSAGE BODY
method string Value:  result object conditionalCondition:  On successful requests only order_id string Unique order identifier generated by Kraken.cl_ord_id string An optional, alphanumeric identifier specified by the client in the  parameters.order_userref integer An optional non-unique, numeric identifier specified by the client in the  parameters.warnings array of strings An advisory message, highlighting deprecated fields or upcoming changes to the request.error string conditionalCondition:  On unsuccessful requests only The error message for a rejected request.success boolean Possible values: [, ] Indicates if the request was successfully processed by the engine.req_id integer Optional client originated request identifier sent as acknowledgment in the response.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the request was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the response was sent on the wire, just prior to transmitting data.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/amend_order/
--------------------------------
>
# Amend Order

REQUEST
## wss://ws-auth.kraken.com/v2
amend_orderAuthentication RequiredThe amend request enables clients to modify the order parameters in-place without the need to cancel the existing order and create a new one.

- The order identifiers assigned by Kraken and/or client will stay the same.

- Queue priority in the order book will be maintained where possible.

- If an amend request will reduce the order quantity below the existing filled quantity, the remaining quantity will be cancelled.

For more detail, see amend transaction guide.

## Request​
- Request Schema
- Example: Basic
- Example: Advanced

### MESSAGE BODY
method string requiredValue:  params object order_id string requiredExample: OFGKYQ-FHPCQ-HUQFEK
The Kraken identifier for the order to be amended. Either  or  is required.
cl_ord_id string Example: 6d1b345e-2821-40e2-ad83-4ecb18a06876
The client identifier for the order to be amended. Either  or  is required.
order_qty float requiredThe new order quantity in terms of the base asset.display_qty float conditionalCondition:  iceberg orders only. 
Defines the new quantity to show in the book while the rest of order quantity remains hidden.
Minimum value is 1 / 15 of remaining order quantity.
limit_price float conditionalCondition:  For order types that support limit price only. 
The new limit price restriction on the order, used in combination with the  parameter.
limit_price_type string conditionalCondition:  Currently only available on trailing-stop-limit orders. Possible values: [, , ] 
The units for :
- : a static market price for the asset, i.e. limit price at 29000.5 BTC/USD, use price=29000.5 and price_type=static.
- : a percentage offset from the reference price, i.e. limit price when market rises by 5%, use price=5 and price_type=pct.
- : a notional offset from the reference price in the quote currency, i.e, limit price when market drops by 150 USD, use price=-150 and price_type=quote.

 is the default for all order types except for  which has the default  offset.
post_only boolean conditionalCondition:  Optional parameter for limit price amends. Possible values: [, ] Default value: 
If , the limit price change will be rejected if the order cannot be posted passively in the book.
trigger_price float conditionalCondition:  For triggered order types only 
The new trigger price to activate the order, used in combination with the  parameter.
trigger_price_type string conditionalCondition:  For triggered order types only Possible values: [, , ] Default value: 
The units for :
- : a static market price for the asset, i.e. to trigger at 29000.5 BTC/USD, use price=29000.5 and price_type=static.
- : a percentage offset from the reference price, i.e. to trigger when price rises by 5%, use price=5 and price_type=pct.
- : a notional offset from the reference price in the quote currency, i.e, to trigger when price drops by 150 USD, use price=-150 and price_type=quote.
deadline string Format: RFC3339Example: 2022-12-25T09:30:59.123Z
Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond.
The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.
symbol string Example: TSLAx/USD
The  is required on amends for non-crypto pairs, i.e. provide the pair symbol for xstocks.
token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
Example: amend the limit price and the quantity on an order using a UUID client order identifier.

Amends the price on an order using the Kraken order identifier.

-  indicates the transaction will be rejected if the new limit price will take liquidity immediately.

-  indicates this amend request is latency sensitive, rejected the amend reject if not processed before the time.

## Response​
- Response Schema
- Example

A successful amend request will return the unique Kraken amend identifier.

### MESSAGE BODY
method string Value:  result object conditionalCondition:  On successful requests only amend_id string The unique Kraken identifier generated for this amend transaction.order_id string The Kraken identifier, if populated in the request.cl_ord_id string The client identifier, if populated in the request.warnings array of strings An advisory message, highlighting deprecated fields or upcoming changes to the request.error string conditionalCondition:  On unsuccessful requests only The error message for a rejected request.success boolean Possible values: [, ] Indicates if the request was successfully processed by the engine.req_id integer Optional client originated request identifier sent as acknowledgment in the response.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the request was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the response was sent on the wire, just prior to transmitting data.
Example: response for an order successfully amended with a client order identifier.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/balances/
--------------------------------
>
# Balances

CHANNEL
## wss://ws-auth.kraken.com/v2
balancesAuthentication RequiredThe  channel streams client asset balances and transactions from the account ledger.

This channel contains account specific data, an authentication token is required in the request.

## Subscribe Request​
- Subscribe Schema
- Subscribe Ack Schema
- Example: Subscribe
- Example: Subscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  snapshot boolean Possible values: [, ] Default value: Request a snapshot after subscribing.token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.rebased boolean conditionalCondition:  Effective for viewing xstocks only. Possible values: [, ] Default value: 
If , display in terms of underlying equity, otherwise display in terms of SPV tokens.
users string conditionalCondition:  Available on master accounts only. Value:  
If , events for master and subaccounts are streamed, otherwise only master account events are published. No snapshot is provided.

### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  snapshot boolean Possible values: [, ] Indicates if a snapshot is requested.warnings array of strings  An advisory message, highlighting deprecated fields or upcoming changes to the channel.success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Snapshot Response​

The snapshot provides the value of each asset held in this account.
- Snapshot Schema
- Example: Snapshot

### MESSAGE BODY
channel string Value:  type string Value:  data array [ 
A list of assets held on account.
[many] asset object asset string The asset symbol code.asset_class string Value:  The asset class. A placeholder for future expansion.balance float The total amount of asset held across all wallet types.wallets array [ 
A list of wallets for each asset.
[many] wallet object balance float Balance of asset in wallet.type string Possible values: [, ] Wallet type.id string Possible values: [, , , , , , ] Wallet identifier.]]sequence integer The subscription message sequence number.

## Update Response​

An update will be streamed on each completed transaction to the client account.
- Update Schema
- Example: Deposit Update
- Example: Trade Update

### MESSAGE BODY
channel string Value:  type string Value:  data array [ 
A list of account ledger transactions for each asset.
[many] ledger_transaction object asset string The asset symbol code.asset_class string Value:  The asset class. A placeholder for future expansion.amount float The amount of asset change in this event.balance float The total amount of this asset held in account.fee float The fee paid on the transaction.ledger_id string The identifier for this account ledger entry.ref_id string A reference identifier in the context of this balance event. For example,  will be the  for a trade event.timestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe time of the balance change.type string Possible values: [, , , , , , , , , , , , , , , ] The broad type of the balance event.subtype string Possible values: [, , , , , ] The specific subtype of the balance event.category string Possible values: [, , , , , , , , , , , , , , , , ] The categorization of the balance event.wallet_type string Possible values: [, ] Wallet type.wallet_id string Possible values: [, , , , ] 

The following combinations of wallet types and wallet identifiers are available:

Wallet type :

- : Primary spot pairs trading wallet.

Wallet type :
- : earn on-chain product with lockup period.
- : earn product without lockup period.
- : kraken rewards program, see support center.
- : earn product (may or may not have a lockup period).
user string conditionalCondition:  Published when request parameters have 'users=all'. Example: AA96N74GCGEFN8KIThe Kraken generated identifier for a user / sub-account.]sequence integer The subscription message sequence number.

An example of selling 0.005 BTC/USD, two events are streamed with a shared . The  refers to the  in this scenario:

- BTC debit of -0.005.

- USD credit of 132.9995.

## Unsubscribe Request​
- Unsubscribe Schema
- Unsubscribe Ack Schema
- Example: Unsubscribe
- Example: Unsubscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/batch_add/
--------------------------------
>
# Batch Add

REQUEST
## wss://ws-auth.kraken.com/v2
batch_addAuthentication RequiredSends a collection of orders (minimum of 2 and maximum 15):

- Validation is performed on the whole batch prior to submission to the engine. If an order fails validation, the whole batch will be rejected.

- On submission to the engine, if an order fails pre-match checks (i.e. funding), then the individual order will be rejected and remainder of the batch will be processed.

- All orders in batch are limited to a single pair.

## Request​
- Request Schema
- Example

### MESSAGE BODY
method string requiredValue:  params object deadline string Format: RFC3339Example: 2022-12-25T09:30:59.123Z
Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds. The precision of this parameter is to the millisecond.
The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.
symbol string requiredExample: "BTC/USD"The symbol of the currency pair.validate boolean Possible values: [, ] Default value: 
If set to  the order will be validated only, it will not trade in the matching engine.
token string requiredThis is a authenticated request, a session token is required.orders array [ 
A list of orders in the batch.
[many] order object cash_order_qty float conditionalCondition:  market orders only. Order volume expressed in quote currency.conditional object 
The conditional parameters are used as a template for generating the secondary close orders when the primary order fills. Each fill on the primary order will generate a new secondary order.
The size of the secondary order will be the same size as the executed quantity and have the opposite side.
order_type string Possible values: [, , , , , , ] 
Defines the order type of the secondary close orders which will be created on each fill.
limit_price float 
Defines the limit price on the secondary close orders. Only required on secondary order types that support limit price: , , .
limit_price_type string conditionalCondition:  Only available on trailing-stop-limit orders. Possible values: [, , ] Default value: 
The units for the limit price on the secondary order.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price

Note, for  order type, the value represents offset from the trigger price. 0 would set a limit price the same as the trigger price.
trigger_price float 
Specifies the amount for the trigger price - it supports both static market prices and relative prices.
This field is used in combination with the  field below to determine the effective trigger price.
Examples:
- To trigger at 29000.5 BTC/USD, use price=29000.5, price_type=static.
- To trigger when price rises by 5%, use price=5, price_type=pct.
- To trigger when price drops by 150 USD, use price=-150, price_type=quote.

Note, for  and  order types, the price represents the reversion from the peak. It is always a positive offset value.
trigger_price_type string Possible values: [, , ] Default value: 
The units for the trigger price.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price
stop_price float deprecatedDeprecated Usage: Use trigger_price
Defines the trigger price on the secondary close orders. Only required on triggered secondary order types: , , , .
display_qty float conditionalCondition:  iceberg orders only. 
Defines the quantity to show in the book while the rest of order quantity remains hidden.
Minimum value is 1 / 15 of .
effective_time string Format: RFC3339Example: 2022-12-25T09:30:59ZScheduled start time (precision to seconds).expire_time string conditionalCondition:  GTD orders only. Format: RFC3339Example: 2022-12-25T09:30:59ZExpiration time of the order  (precision to seconds). GTD orders can have an expiry time up to one month in future.fee_preference string Possible values: [, ] 
Fee preference base or quote currency.  is the default for buy orders,  is the default for sell orders.
limit_price float Limit price for order types that support limit price restriction.limit_price_type string conditionalCondition:  Only available on trailing-stop orders. Possible values: [, , ] Default value: The units for the limit price.margin boolean Possible values: [, ] Default value: Funds the order on margin using the maximum leverage for the pair (maximum is leverage of 5).no_mpp boolean deprecatedDeprecated Usage: If supplied, the flag is accepted but ignored.Possible values: [, ] Default value: 
Disables Market Price Protection (MPP) if set to . MPP is a feature that protects market orders from filling at a bad price due to price slippage in an illiquid or volatile market. See MPP support article.
cl_ord_id string 

Adds a alphanumeric client order identifier which uniquely identifies an open order for each client. This field is mutually exclusive with  parameter.

The  parameter can be one of the following formats:

- Long UUID:  32 hex characters separated with 4 dashes.
- Short UUID:  32 hex characters with no dashes.
- Free text:  Free format ascii text up to 18 characters.
order_userref integer 

This is an optional non-unique, numeric identifier which can associated with a number of orders by the client. This field is mutually exclusive with  parameter.

Many clients choose a unique integer value generated by their systems (i.e. a timestamp). However, because we don't enforce uniqueness on our side, it can also be used to easily tag a group of orders for querying or cancelling.

order_qty float required Order quantity in terms of the base asset.order_type string requiredPossible values: [, , , , , , , , , ]  The execution model of the order.post_only boolean conditionalCondition:  Orders with limit price only. Possible values: [, ] Default value: 
Cancels the order if it will take liquidity on arrival. Post only orders will always be posted passively in the book.
reduce_only boolean Possible values: [, ] Default value: 
Reduces an existing margin position without opening an opposite long or short position worth more than the current value of your leveraged assets.
side string requiredPossible values: [, ]  Side of the order.stp_type string Possible values: [, , ] Default value: 
Self Trade Prevention (STP) is a protection feature to prevent users from inadvertently or deliberately trading against themselves.
To prevent a self-match, one of the following STP modes can be used to define which order(s) will be expired:
- : arriving order will be canceled.
- : resting order will be canceled.
- : both arriving and resting orders will be canceled.
time_in_force string Possible values: [, , ] Default value: 
Time-in-force specifies how long an order remains in effect before being expired.
- : Good Till Canceled - until user has cancelled.
- : Good Till Date - until  parameter.
- : Immediate Or Cancel - immediately cancels back any quantity that cannot be filled on arrival.
triggers object conditionalCondition:  Required for triggered order types only. 
The parameters for setting the trigger price conditions.
reference string Possible values: [, ] Default value: 
The reference price to track for triggering orders.
- : the index price in the broader market (for this pair). Note, to keep triggers serviceable during connectivity issues with external index feeds, the last price will be used as the reference price.
- : the last traded price in the Kraken order book (for this pair).
price float required
Specifies the amount for the trigger price - it supports both static market prices and relative prices.
This field is used in combination with the  field below to determine the effective trigger price.
Examples:
- To trigger at 29000.5 BTC/USD, use price=29000.5, price_type=static.
- To trigger when price rises by 5%, use price=5, price_type=pct.
- To trigger when price drops by 150 USD, use price=-150, price_type=quote.

Note, for  and  order types, the price represents the reversion from the peak. It is always a positive offset value.
price_type string Possible values: [, , ] Default value: 
The units for the trigger price.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price
sender_sub_id string conditionalCondition:  For institutional accounts with enhanced Self Trade Prevention (STP) 

Adds a alphanumeric sub-account/trader identifier which enables STP to be performed at a more granular level.

The  parameter can be one of the following formats:

- Long UUID:  32 hex characters separated with 4 dashes.
- Short UUID:  32 hex characters with no dashes.
- Free text:  Free format ascii text up to 18 characters.
stop_price float deprecatedDeprecated Usage: Use 'triggers' object. The stop price for trigger order types.trigger string deprecatedDeprecated Usage: Use 'triggers' object.Possible values: [, ] Default value: 
The reference price to trigger the order.
- : the index price for the broader market for this symbol.
- : the last traded price in the order book for this symbol.
]token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Response​
- Response Schema
- Example

The order of returned txid's in the response array is the same as the order of the order list sent in request.

### MESSAGE BODY
method string Value:  result array of objects conditionalCondition:  On successful requests only order_id string Unique order identifier generated by Kraken.cl_ord_id string An optional, alphanumeric identifier specified by the client in the  parameters.order_userref integer An optional order identifier specified by the client in the  parameters.warnings array of strings An advisory message, highlighting deprecated fields or upcoming changes to the request.error string conditionalCondition:  On unsuccessful requests only The error message for a rejected request.success boolean Possible values: [, ] Indicates if the request was successfully processed by the engine.req_id integer Optional client originated request identifier sent as acknowledgment in the response.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the request was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the response was sent on the wire, just prior to transmitting data.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/batch_cancel/
--------------------------------
>
# Batch Cancel

REQUEST
## wss://ws-auth.kraken.com/v2
batch_cancelAuthentication RequiredThe  request enables multiple orders to be cancelled in a single request by a range of identifiers (minimum of 2 and maximum 50 in each batch).

## Request​
- Request Schema
- Example

### MESSAGE BODY
method string requiredValue:  params object orders array of string requiredA list containing either client  or Kraken  identifiers.cl_ord_id array of string A list of client  identifiers.token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Response​
- Response Schema
- Example

### MESSAGE BODY
method string Value:  result object conditionalCondition:  On successful requests only count integer Number of orders cancelled.warnings array of strings An advisory message, highlighting deprecated fields or upcoming changes to the request.error string conditionalCondition:  On unsuccessful requests only The error message for a rejected request.success boolean Possible values: [, ] Indicates if the request was successfully processed by the engine.req_id integer Optional client originated request identifier sent as acknowledgment in the response.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the request was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the response was sent on the wire, just prior to transmitting data.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/book/
--------------------------------
>
# Book (Level 2)

CHANNEL
## wss://ws.kraken.com/v2
bookThe  channel streams level 2 (L2) order book. It describes the individual price levels in the book with aggregated order quantities at each level.

Subscriptions to this channel can be made for multiple symbols at once by specifying a list of pairs in the .

For more detail on maintaining the order book and generating a checksum, see guide.

## Subscribe Request​
- Subscribe Schema
- Subscribe Ack Schema
- Example: Subscribe
- Example: Subscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  symbol array of strings requiredExample: ["BTC/USD", "MATIC/GBP"]A list of currency pairs.depth integer Possible values: [, , , , ] Default value: The number of price levels to be received.snapshot boolean Possible values: [, ] Default value: Request a snapshot after subscribing.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
There is an separate acknowledgement response for each symbol in the subscription list.

### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  symbol string requiredExample: "BTC/USD"The currency pair associated with this subscription.depth integer Possible values: [, , , , ] Specifies the number of price levels (in each side of the book) to be received.snapshot boolean Possible values: [, ] Indicates if a snapshot is requested.warnings array of strings  An advisory message, highlighting deprecated fields or upcoming changes to the channel.success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Snapshot Response​
- Snapshot Schema
- Example

The returned snapshot data contains the specified number of bids and asks for the symbol including a CRC32 checksum of the top 10 bids and asks.

### MESSAGE BODY
channel string Value:  type string Value:  data array [ [0] book object 
The book element is always the first and only item in the data payload.
asks array [ [many] level object price float The ask price.qty float The ask quantity.]bids array [ [many] level object price float The bid price.qty float The bid quantity.]checksum integer CRC32 checksum for the top 10 bids and asks.symbol string Example: "BTC/USD"The symbol of the currency pair.timestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp of the order book snapshot.]

## Update Response​

The data contains the updates of the bids and asks for the relevant symbol including a CRC32 checksum of the top 10 bids and asks.

Note, it is possible to have multiple updates to the same price level in a single update message. Updates should always be processed in sequence.
- Update Schema
- Example

### MESSAGE BODY
channel string Value:  type string Value:  data array [ [0] book object 
The book element is always the first and only item in the data payload.
asks array [ [many] level object price float The ask price.qty float The ask quantity.]bids array [ [many] level object price float The bid price.qty float The bid quantity.]checksum integer CRC32 checksum for the top 10 bids and asks.symbol string Example: "BTC/USD"The symbol of the currency pair.timestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe book order update timestamp.]

## Unsubscribe Request​
- Unsubscribe Schema
- Unsubscribe Ack Schema
- Example: Unsubscribe
- Example: Unsubscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  symbol array of strings requiredExample: ["BTC/USD", "MATIC/GBP"]A list of currency pairs.depth integer Possible values: [, , , , ] The number of price levels to be unsubscribed.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
There is an separate acknowledgement response for each symbol in the unsubscription list.

### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  symbol string requiredExample: "BTC/USD"The currency pair associated with this subscription.depth integer Possible values: [, , , , ] Specifies the number of price levels (in each side of the book) to be unsubscribed.success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/cancel_after/
--------------------------------
>
# Cancel on Disconnect

REQUEST
## wss://ws-auth.kraken.com/v2
cancel_all_orders_afterAuthentication Required provides a "Dead Man's Switch" mechanism to protect from network malfunction, extreme latency or unexpected matching
engine downtime.

- The client sends request with a timeout (in seconds), that will start a countdown timer in the trading engine which will cancel all client orders when the timer expires.

- The client must keep sending new requests to reset the trigger time, or deactivate the mechanism by specifying a timeout of 0.

- If the timer expires, all orders in the account are cancelled and the feature is disabled until the next  request.

- The recommended use is to make a call every 15 to 30 seconds, providing a timeout of 60 seconds. This allows the client to keep the orders in place in case of a brief
disconnection or transient delay, while keeping them safe in case of a network breakdown.

> [info]
> 
It is recommended to disable the timer ahead of scheduled trading engine maintenance (if the timer is enabled, all orders will be cancelled when the trading engine comes back from downtime).

## Request​
- Request Schema
- Example

### MESSAGE BODY
method string requiredValue:  params object timeout integer required Duration (in seconds) to set/extend the timer, it should be less than  seconds.token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Response​
- Response Schema
- Example

### MESSAGE BODY
method string Value:  result object conditionalCondition:  On successful requests only currentTime string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe current engine time.triggerTime string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe time the orders will be expired in the engine.warnings array of strings An advisory message, highlighting deprecated fields or upcoming changes to the request.error string conditionalCondition:  On unsuccessful requests only The error message for a rejected request.success boolean Possible values: [, ] Indicates if the request was successfully processed by the engine.req_id integer Optional client originated request identifier sent as acknowledgment in the response.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the request was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the response was sent on the wire, just prior to transmitting data.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/cancel_all/
--------------------------------
>
# Cancel All

REQUEST
## wss://ws-auth.kraken.com/v2
cancel_allAuthentication RequiredCancels all open orders, including untriggered orders and orders resting in the book.

Note, the details of the individual cancelled orders will also be streamed on the  channel.

## Request​
- Request Schema
- Example

### MESSAGE BODY
method string requiredValue:  params object token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Response​
- Response Schema
- Example

### MESSAGE BODY
method string Value:  result object conditionalCondition:  On successful requests only count integer Number of orders cancelled.warnings array of strings An advisory message, highlighting deprecated fields or upcoming changes to the request.error string conditionalCondition:  On unsuccessful requests only The error message for a rejected request.success boolean Possible values: [, ] Indicates if the request was successfully processed by the engine.req_id integer Optional client originated request identifier sent as acknowledgment in the response.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the request was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the response was sent on the wire, just prior to transmitting data.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/cancel_order/
--------------------------------
>
# Cancel Order

REQUEST
## wss://ws-auth.kraken.com/v2
cancel_orderAuthentication RequiredThe  request cancels one or more open orders in a single request. The orders to be cancelled can be identified by a range of client or Kraken identifiers.
Note, the details of the individual cancelled orders will also be streamed on the  channel.

## Request​
- Request Schema
- Example

### MESSAGE BODY
method string requiredValue:  params object order_id array of string A list of Kraken  identifiers.cl_ord_id array of string A list of client  identifiers.order_userref array of integer A list of client  identifiers.token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Response​

When cancelling multiple orders, there will be a stream of individual order responses.
- Response Schema
- Example

### MESSAGE BODY
method string Value:  result object conditionalCondition:  On successful requests only order_id string Kraken identifier of the cancelled order.cl_ord_id string Optional client identifier of the cancelled order.warnings array of strings An advisory message, highlighting deprecated fields or upcoming changes to the request.error string conditionalCondition:  On unsuccessful requests only The error message for a rejected request.success boolean Possible values: [, ] Indicates if the request was successfully processed by the engine.req_id integer Optional client originated request identifier sent as acknowledgment in the response.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the request was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the response was sent on the wire, just prior to transmitting data.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/edit_order/
--------------------------------
>
# Edit Order

REQUEST
## wss://ws-auth.kraken.com/v2
edit_orderAuthentication RequiredSends a request to edit the order parameters of a live order. When an order has been successfully modified, the original order will be cancelled and a new order will be
created with the adjusted parameters a new  will be returned in the response.

> [note]
> 
The new amend_order endpoint resolves the caveats listed below and has additional performance gains.

There are a number of caveats for :

- triggered stop loss or profit take profit orders are not supported.

- orders with conditional close terms attached are not supported.

- orders where the executed volume is greater than the newly supplied volume will be rejected.

-  is not supported.

- existing executions will are associated with the original order and not copied to the amended order.

- queue position will not be maintained.

## Request​
- Request Schema
- Example

### MESSAGE BODY
method string requiredValue:  params object deadline string Format: RFC3339Example: 2022-12-25T09:30:59.123Z
Range of valid offsets (from current time) is 500 milliseconds to 60 seconds, default is 5 seconds.  The precision of this parameter is to the millisecond.
The engine will prevent this order from matching after this time, it provides protection against latency on time sensitive orders.
display_qty float conditionalCondition:  Iceberg orders only. 
Defines the quantity to show in the book while the rest of order quantity remains hidden.
Minimum value is 1 / 15 of .
fee_preference string Possible values: [, ] 
Fee preference base or quote currency.  is the default for buy orders,  is the default for sell orders.
limit_price float Limit price for order types that support limit price restriction.no_mpp boolean deprecatedDeprecated Usage: If supplied, the flag is accepted but ignored.Possible values: [, ] Default value: 
Disables Market Price Protection (MPP) if set to . MPP is a feature that protects market orders from filling at a bad price due to price slippage in an illiquid or volatile market. See MPP support article.
order_id string requiredExample: OFGKYQ-FHPCQ-HUQFEKThe Kraken identifier for the order to be amended.order_qty float  Order quantity in terms of the base asset.order_userref integer User defined reference to be placed on the amended order. It does not identifier the order to be amended, use .post_only boolean conditionalCondition:  Orders with limit price only. Possible values: [, ] Default value: 
Cancels the order if it will take liquidity on arrival. Post only orders will always be posted passively in the book.
reduce_only boolean Possible values: [, ] Default value: 
Reduces an existing margin position without opening an opposite long or short position worth more than the current value of your leveraged assets.
symbol string requiredExample: "BTC/USD"The original symbol identifier for the pair. Note, the  cannot be amended. triggers object conditionalCondition:  Required for triggered order types only. 
The parameters for setting the trigger price conditions.
reference string Possible values: [, ] Default value: 
The reference price to track for triggering orders.
- : the index price in the broader market (for this pair). Note, to keep triggers serviceable during connectivity issues with external index feeds, the last price will be used as the reference price.
- : the last traded price in the Kraken order book (for this pair).
price float 
Specifies the amount for the trigger price - it supports both static market prices and relative prices.
This field is used in combination with the  field below to determine the effective trigger price.
Examples:
- To trigger at 29000.5 BTC/USD, use price=29000.5, price_type=static.
- To trigger when price rises by 5%, use price=5, price_type=pct.
- To trigger when price drops by 150 USD, use price=-150, price_type=quote.

Note, for  and  order types, the price represents the reversion from the peak. It is always a positive offset value.
price_type string Possible values: [, , ] Default value: 
The units for the trigger price.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price
validate boolean Possible values: [, ] Default value: 
If set to  the order will be validated only, it will not trade in the matching engine.
price float deprecatedDeprecated Usage: Use 'limit_price' parameter.trigger string deprecatedDeprecated Usage: Use 'triggers.reference' parameter.stop_price float deprecatedDeprecated Usage: Use 'triggers.price' parameter.token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Response​
- Response Schema
- Example

### MESSAGE BODY
method string Value:  result object conditionalCondition:  On successful requests only order_id string Unique ID of the orderoriginal_order_id string ID of the order that have been editedwarnings array of strings An advisory message, highlighting deprecated fields or upcoming changes to the request.error string conditionalCondition:  On unsuccessful requests only The error message for a rejected request.success boolean Possible values: [, ] Indicates if the request was successfully processed by the engine.req_id integer Optional client originated request identifier sent as acknowledgment in the response.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the request was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the response was sent on the wire, just prior to transmitting data.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/executions/
--------------------------------
>
# Executions

CHANNEL
## wss://ws-auth.kraken.com/v2
executionsAuthentication RequiredThe  channel streams order status and execution events for this account.

It corresponds to a combination of the following Websockets v1 channels:  and .

This channel contains account specific data, an authentication token is required in the request.

## Subscribe Request​
- Subscribe Schema
- Subscribe Ack Schema
- Example: Subscribe
- Example: Subscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  snap_trades boolean Possible values: [, ] Default value: 
If , the last 50 order fills will be included in snapshot.
snap_orders boolean Possible values: [, ] Default value: 
If , open orders will be included in snapshot.
order_status boolean Possible values: [, ] Default value: 
If , all possible status transitions will be sent. Otherwise, only open / close transitions will be streamed: , , , .
rebased boolean conditionalCondition:  Effective for viewing xstocks only. Possible values: [, ] Default value: 
If , display in terms of underlying equity, otherwise display in terms of SPV tokens.
ratecounter boolean Possible values: [, ] Default value: 
If , the rate-limit counter is included in the stream.
users string conditionalCondition:  Available on master accounts only. Value:  
If , events for master and subaccounts are streamed, otherwise only master account events are published. No snapshot is provided.
snapshot_trades boolean deprecatedDeprecated Usage: Use 'snap_trades' field.Possible values: [, ] 
If , snapshot provides only trade events. Otherwise, open orders and trades will be included in snapshot.
snapshot boolean deprecatedDeprecated Usage: Use 'snap_orders' or 'snap_trades' field.Possible values: [, ] Request a snapshot after subscribing.token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  snap_orders boolean Possible values: [, ] Indicates if a snapshot of orders is requested.snap_trades boolean Possible values: [, ] Indicates if a snapshot of trades is requested.maxratecount integer Specifies the max rate counter value for the user transaction rate. It is based on user tier.snapshot boolean deprecatedDeprecated Usage: Use 'snap_trades' and 'snap_orders'.Indicates if a snapshot is requested.warnings array of strings  An advisory message, highlighting deprecated fields or upcoming changes to the channel.success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Snapshot / Update Responses​

The snapshot and update stream share the same data schema, the fields included in the message is dependant on the .

By default, the snapshot response contains all open orders and latest 50 trades.

The snapshot message content can be adjusted with the subscription parameters.
- Snapshot / Update Schema
- Example: Pending
- Example: Live Order
- Example: Execution

### MESSAGE BODY
channel string Value:  type string Possible values: [, ] data array [ 
A list of execution reports: order status and fills.
[many] execution_report object amended boolean Possible values: [, ] Indicates if the order has been amended, the modification history can be extracted from the REST  endpoint. This field is present in the snapshot and the ,  event types.avg_price float Order's average fill price.cash_order_qty float Order volume expressed in quote currency (if specified on the original order).cl_ord_id string Optional client identifier associated with the order.contingent object 
The contingent object describes the template for generating the secondary close orders when the primary order fills.
order_type string Possible values: [, , , , , , ] 
Describes the order type of the secondary orders which will be created on each fill.
trigger_price float conditionalCondition:  Only on triggered secondary order types. 
Describes the trigger price amount on the secondary orders.
This field is used in combination with the  field to determine the effective trigger price.
trigger_price_type string conditionalCondition:  Only on triggered secondary order types. Possible values: [, , ] 
Describes trigger price units on the secondary orders.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price
limit_price float conditionalCondition:  Only on secondary order types that support limit price. 
Describes limit price amount on the secondary orders.
This field is used in combination with the  field to determine the effective limit price.
limit_price_type string conditionalCondition:  Only on secondary order types that support limit price. Possible values: [, , ] 
Describes limit price units on the secondary orders.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price
cost float conditionalCondition:  trade events only. Value of an individual execution.cum_cost float The order cumulative value executed.cum_qty float The order  cumulative executed quantity.display_qty float Display quantity for iceberg order types.display_qty_remain float conditionalCondition:  Iceberg Order Indicates next display_qty in Iceberg order.effective_time string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZScheduled start time of the order.exec_id string conditionalCondition:  trade events only. Execution identifier.exec_type string Possible values: [, , , , , , , , ] 
Describes the type of order event and determines the set of fields in the message.
-  : Order request has been received and validated but the order is not live yet.
-  : Order has been created and is live in the engine.
-  : The order has received a fill.
-  : The order has been fully filled.
-  : The order has been cancelled.
-  : Indicates an Iceberg order refill.
-  : The order has expired.
-  : There is a user initiated amend on the order, i.e. limit price change. 
-  : There is a engine initiated amend on the order for maintenance of position or book, see  field, i.e. reduce non-tradable liquidity. 
-  : The order has a status update, i.e. trigger price has been updated.
expire_time string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZScheduled expiration time of the order.ext_ord_id string Format: UUIDAn optional, external partner order identifier shown on order events. ext_exec_id string Format: UUIDAn optional, external partner execution identifier shown on trade events. fees array [ conditionalCondition:  trade events only. 
The fees paid on this trade event. Currently, the fees are expressed in the quote currency only.
[0] fee object asset string The fee currency.qty float The fee amount.]fee_ccy_pref string 
The preferred currency for paying fees.
- : prefer fee in base currency. 
- : prefer fee in quote currency. 
fee_usd_equiv float The total fee paid in USD.limit_price float Limit price for order types that support limit price restriction.liquidated boolean Indicates if the order has been liquidated by the engine.liquidity_ind string Possible values: [, ] The liquidity indicator:  taker,  maker.last_price float conditionalCondition:  trade events only. The average price in this trade event.last_qty float conditionalCondition:  trade events only. The quantity filled in this trade event.margin boolean Indicates if the order can be funded on margin.margin_borrow boolean Indicates if an execution is on margin, i.e. if the trade increased or reduced size of margin borrowing. On trade events only.no_mpp boolean Indicates if the order has market price protection.ord_ref_id string Referral order transaction id that created this order.order_id string Unique order identifier generated by Kraken.order_qty float The client order quantity.order_type string Possible values: [, , , , , , , , , ] The execution model of the order.order_status string 
Describes current state of the order.
-  : Order has been received but not yet created by the engine. 
-  : Order is live but has no fills. 
-  : Order is live and some fills. 
-  : The order has been fully filled. 
-  : The order has been cancelled. 
-  : The order has expired. 
order_userref integer Optional numeric, client identifier associated with one or more orders.post_only boolean Possible values: [, ] Indicates a post only order.position_status string Possible values: [, , ] Indicates status of the position on a margin order.reason string The reason associated with an event, if applicable. reduce_only boolean Possible values: [, ] Indicates a reduce only order.sender_sub_id string For institutional accounts, identifies underlying sub-account/trader for Self Trade Prevention (STP).side string Possible values: [, ] Side of the order.symbol string Example: "BTC/USD"The symbol of the currency pair.time_in_force string Possible values: [, , ] 
Time-in-force specifies how long an order remains in effect before being expired.
- : Good Till Canceled
- : Good Till Date
- : Immediate Or Cancel
timestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZTime of the event.trade_id integer The trade identifier.triggers object 
Describes the parameters and status of the price trigger for triggered order types.

reference string Possible values: [, ] The reference price tracked for triggering orders.

price float 
Specifies the amount for the trigger price - it supports both static market prices and relative prices.
This field is used in combination with the  field below to determine the effective trigger price.
price_type string Possible values: [, , ] 
The units for the trigger price.
- : a static market price for the asset, i.e. 30000 for BTC/USD.
- : a percentage offset from the reference price, i.e. -10% from index price.
- : a notional offset from the reference price in the quote currency, i.e, 150 BTC/USD from last price
actual_price float The current value of the effective trigger price, this is useful if the trigger was entered using a relative price or the trigger price changes over time.peak_price float The peak / trough price on  and  orders.last_price float On trigger activation, the value of the reference last price that triggered the order.status string Possible values: [, ] The status is set to  when the trigger conditions are met and the order becomes active.timestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZOn trigger activation, the timestamp of the trigger event.user string conditionalCondition:  Published when request parameters have 'users=all'. Example: AA96N74GCGEFN8KIThe Kraken generated identifier for a user / sub-account.cancel_reason string deprecatedDeprecated Usage: Use 'reason' field.Cancellation reason.stop_price float deprecatedDeprecated Usage: Use 'triggers' object. The stop price for triggered order types.trigger string deprecatedDeprecated Usage: Use 'triggers' object.Possible values: [, ]  Reference price for triggered order types.triggered_price float deprecatedDeprecated Usage: Use 'triggers' object. Price which triggered the order.]sequence integer The subscription message sequence number.

## Unsubscribe Request​
- Unsubscribe Schema
- Unsubscribe Ack Schema
- Example: Unsubscribe
- Example: Unsubscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/heartbeat/
--------------------------------
>
# Heartbeat

CHANNEL
## wss://ws.kraken.com/v2
heartbeatThe  channel provides a mechanism to verify that the connection is alive.

Heartbeat messages are sent approximately once every second in the absence of any other channel updates.

There is no option to directly request a  subscription, the heartbeats will be automatically generated on subscription to any channel.

## Update Response​

The channel name is the indicator of a heartbeat, here is no other data in the heartbeat payload.
- Update Response
- Example

### MESSAGE BODY
channel string

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/level3/
--------------------------------
>
# Orders (Level 3)

CHANNEL
## wss://ws-l3.kraken.com/v2
level3Authentication Required
## Summary​
The  channel has an additional level of granularity over the  channel, it provides visibility of individual orders in the book.

L3 shows orders resting in the visible order book and it will never be crossed (i.e. no overlapping buy and sell orders). This feed excludes:

- In-flight orders.

- Unmatched market orders.

- Untriggered stop-loss and take-profit orders.

- Hidden quantity of iceberg orders.

For more detail on maintaining the order book and generating a checksum, see guide.

## Subscription limits​

The  channel is authenticated (i.e. it requires an API token to subscribe) and there are restrictions of the number of symbols and the subscription rate.

- The total number of symbols per websocket connection is . A client can open multiple websockets connections to increase symbol coverage.

- The subscription rate determined by client tier and order book depth. Standard rate count limit per second is  and the pro limit is .

- The counter increase per book depth subscription is given in the table below.

Order Book DepthRate Counter Increase per Symbol
| 10 | 5 
| 100 | 25 
| 1000 | 100 
**Example: ** Pro client can subscribe to 100 symbols of 10 depth every second.

## Subscribe Request​

Only one subscription to one depth level per symbol is supported, i.e. cannot subscribe to 10 levels and 1000 levels of "BTC/USD".
- Subscribe Schema
- Subscribe Ack Schema
- Example: Subscribe
- Example: Subscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  symbol array of strings requiredExample: ["BTC/USD", "MATIC/GBP"]A list of currency pairs.depth integer Possible values: [, , ] Default value: The number of price levels to be received.snapshot boolean Possible values: [, ] Default value: Request a snapshot after subscribing.token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
There is an separate acknowledgement response for each symbol in the subscription list.

### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  symbol string requiredExample: "BTC/USD"The currency pair associated with this subscription.depth integer Possible values: [, , ] The number of price levels to be received.snapshot boolean Possible values: [, ] Indicates if a snapshot is requested.warnings array of strings  An advisory message, highlighting deprecated fields or upcoming changes to the channel.success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Snapshot Response​
- Snapshot Response
- Example: Snapshot

### MESSAGE BODY
channel string Value:  type string Value:  data array [ [0] book object 
The book element is always the first and only item in the data payload.

symbol string Example: "BTC/USD"The symbol of the currency pair.

bids array [ 
A list of buy orders posted in the book.
[many] order object order_id string The Kraken order identifier of the order in the booklimit_price float Limit price of the orderorder_qty float The remaining order quantity visible in the booktimestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456789ZThe time the order was inserted or amended.]asks array [ 
A list of sell orders posted in the book.
[many] order object order_id string The Kraken order identifier of the order in the booklimit_price float Limit price of the orderorder_qty float The remaining order quantity visible in the booktimestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456789ZThe time the order was inserted or amended.]checksum integer CRC32 checksum for the top 10 price levels on both sides.timestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456789ZThe time this market data message was generated in the matching engine.]

## Update Response​

- The updates will be streamed following the initial snapshot, no sequencing is required.

- The L3 channel is not throttled, updates will be provided in the real-time.

- If a price level is removed from the subscribed levels (i.e. result of trades/cancels) then all orders in the next available level will generate an add event.

### Maintaining the book​

After each update, the book should be truncated to your subscribed depth, there will be no  event for price levels that fall out of scope.
In other words, if you are subscribed with  of 10 and an insert into the book results in 11 bids, you must remove the 11th worst bid.
- Update Schema
- Example

### MESSAGE BODY
channel string Value:  type string Value:  data array [ [0] book object 
The book element is always the first and only item in the data payload.

symbol string Example: "BTC/USD"The symbol of the currency pair.
timestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456789ZThe time this market data message was generated in the matching engine.
checksum integer CRC32 checksum for the top 10 price levels on both sides.

bids array [ 
A list of order events to the bid side of book.
[many] order_event object event string Possible values: [, , ] The type of order event for this update:- : A new order added to the book.
- : The order quantity has been modified, i.e. a fill.
- : The order has been removed from the book, i.e. full fill or cancel.
order_id string The Kraken order identifier of the order in the booklimit_price float Limit price of the orderorder_qty float The remaining order quantity visible in the booktimestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456789ZThe time the order was inserted or amended.]asks array [ 
A list of order events to the ask side of book.
[many] order_event object event string Possible values: [, , ] The type of order event for this update:- : A new order added to the book.
- : The order quantity has been modified, i.e. a fill.
- : The order has been removed from the book, i.e. full fill or cancel.
order_id string The Kraken order identifier of the order in the booklimit_price float Limit price of the orderorder_qty float The remaining order quantity visible in the booktimestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456789ZThe time the order was inserted or amended.]]

## Unsubscribe Request​
- Unsubscribe Schema
- Unsubscribe Ack Schema
- Example: Unsubscribe
- Example: Unsubscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  symbol array of strings requiredExample: ["BTC/USD", "MATIC/GBP"]A list of currency pairs.depth integer Possible values: [, , ] Default value: The number of price levels to be received.token string requiredThis is a authenticated channel, a session token is required. See guides on how to generate a token via REST.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
There is an separate acknowledgement response for each symbol in the unsubscribe request list.

### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  symbol string requiredExample: "BTC/USD"The currency pair associated with this subscription.depth integer Possible values: [, , ] The number of price levels to be unsubscribed.success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/ohlc/
--------------------------------
>
# Candles (OHLC)

CHANNEL
## wss://ws.kraken.com/v2
ohlcThe  channel streams the  Open, High, Low and Close (OHLC) data for the specific interval period.

The feed accepts a list symbols for subscription and the updates are generated on trade events.

## Subscribe Request​

There is an acknowledgement response for each symbol in the subscription list.
- Subscribe Schema
- Subscribe Ack Schema
- Example: Subscribe
- Example: Subscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  symbol array of strings requiredExample: ["BTC/USD", "MATIC/GBP"]A list of currency pairs.interval integer Possible values: [, , , , , , , , ] The interval timeframe in minutes.snapshot boolean Possible values: [, ] Default value: Request a snapshot after subscribing.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  symbol string requiredExample: "BTC/USD"The currency pair associated with this subscription.snapshot boolean Possible values: [, ] Indicates if a snapshot is requested.warnings array of strings  An advisory message, highlighting deprecated fields or upcoming changes to the channel.success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Snapshot and Update Response​

The snapshot and update responses share the same schema. An update message is streamed on a trade event.
- Response Schema
- Example: Snapshot
- Example: Update

### MESSAGE BODY
channel string Value:  type string Possible values: [, ] data array [ 
A list of candle events.
[many] candle object symbol string Example: "BTC/USD"The symbol of the currency pair.open float The opening trade price within the interval.high float The highest trade price within the interval.low float The lowest trade price within the interval.close float The last trade price within the interval.vwap float Volume weighted average trade price within the interval.trades float Number of trades within the interval.volume float Total traded volume (in base currency terms) within the interval.interval_begin string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp of start of the interval.interval integer The timeframe from the interval in minutes.timestamp string deprecatedDeprecated Usage: Use 'interval_begin'.Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp of start of the interval.]

## Unsubscribe Request​

There is an acknowledgement response for each symbol in the unsubscribe list.
- Unsubscribe Schema
- Unsubscribe Ack Schema
- Example: Unsubscribe
- Example: Unsubscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  symbol array of strings requiredExample: ["BTC/USD", "MATIC/GBP"]A list of currency pairs.interval integer Possible values: [, , , , , , , , ] The interval timeframe in minutes.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  symbol string requiredExample: "BTC/USD"The currency pair associated with this subscription.success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/ping/
--------------------------------
>
# Ping

REQUEST
## wss://ws.kraken.com/v2
pingClients can ping the server to verify connection is alive and the server will respond with a .

This is an application level ping, distinct from the protocol-level ping in the WebSockets standard.

## Request​
- Request Schema
- Example

### MESSAGE BODY
method string requiredValue:  req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Response​
- Response Schema
- Response Schema

### MESSAGE BODY
method string Value:  result object conditionalCondition:  On successful requests only warnings array of strings An advisory message, highlighting deprecated fields or upcoming changes to the request.error string conditionalCondition:  On unsuccessful requests only The error message for a rejected request.success boolean Possible values: [, ] Indicates if the request was successfully processed by the engine.req_id integer Optional client originated request identifier sent as acknowledgment in the response.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the request was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the response was sent on the wire, just prior to transmitting data.

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/status/
--------------------------------
>
# Status

CHANNEL
## wss://ws.kraken.com/v2
statusThe  channel provides a mechanism to verify exchange status and successful initial connection.

There is no option to directly request a  update, a status will be automatically generated on successful websocket connection and when the trading engine status changes.

## Update Response​
- Update Schema
- Example

### MESSAGE BODY
channel string Value:  type string Value:  data array [ [0] status object 
The status element is always the first and only item in the data payload.
system string Possible values: [, , , ] 
The status of the trading engine.
- : Markets are operating normally - all order types may be submitted and order matching can occur.
- : Markets are offline for scheduled maintenance - new orders cannot be placed and existing orders cannot be cancelled.
- : Orders can be cancelled but new orders cannot be placed. No order matching will occur.
- : Only limit orders using the  option can be submitted. Orders can be cancelled. No order matching will occur.
api_version  string Value:  The version of the websockets API.connection_id  integer A unique connection identifier (for debugging).version  string The version of the websockets service.]

--------------------------------
# URL: https://docs.kraken.com/api/docs/websocket-v2/ticker/
--------------------------------
>
# Ticker (Level 1)

CHANNEL
## wss://ws.kraken.com/v2
tickerThe  channel streams level 1 market data, i.e. top of the book (best bid/offer) and recent trade data.

The feed accepts a list symbols for subscription and the updates are generated on trade events.

## Subscribe Request​
- Subscribe Schema
- Subscribe Ack Schema
- Example: Subscribe
- Example: Subscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  symbol array of strings requiredExample: ["BTC/USD", "MATIC/GBP"]A list of currency pairs.event_trigger string Possible values: [, ] Default value: 
The book event that causes a new ticker update to be published on the channel.
- : on a change in the best-bid-offer price levels.
- : on every trade.
snapshot boolean Possible values: [, ] Default value: Request a snapshot after subscribing.req_id integer Optional client originated request identifier sent as acknowledgment in the response.
### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  symbol string requiredExample: "BTC/USD"The currency pair associated with this subscription.snapshot boolean Possible values: [, ] Indicates if a snapshot is requested.warnings array of strings  An advisory message, highlighting deprecated fields or upcoming changes to the channel.success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.

## Snapshot / Update Response​

The snapshot and update responses share the same schema. An update message is streamed on a trade event.
- Snapshot / Update Schema
- Example: Snapshot
- Example: Update

### MESSAGE BODY
channel string Value:  type string Possible values: [, ] data array [ [0] ticker object 
The ticker element is always the first and only item in the data payload.

ask float Best ask price.
ask_qty float Best ask quantity.
bid float Best bid price.
bid_qty float Best bid quantity.
change float 24-hour price change (in quote currency).
change_pct float 24-hour price change (in percentage points).
high float 24-hour highest trade price.
last float Last traded price (only guaranteed if traded within the past 24 hours).
low float 24-hour lowest trade price.
symbol string Example: "BTC/USD"The symbol of the currency pair.
timestamp string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe ticker data timestamp.
volume float 24-hour traded volume (in base currency terms).
vwap float 24-hour volume weighted average price.

]

## Unsubscribe Request​
- Unsubscribe Schema
- Unsubscribe Ack Schema
- Example: Unsubscribe
- Example: Unsubscribe Ack

### MESSAGE BODY
method string requiredValue:  params object channel string requiredValue:  symbol array of strings requiredExample: ["BTC/USD", "MATIC/GBP"]A list of currency pairs.event_trigger string Possible values: [, ] Default value: 
The book event that causes a new ticker update to be published on the channel.
- : on a change in the best-bid-offer price levels.
- : on every trade.
req_id integer Optional client originated request identifier sent as acknowledgment in the response.
### MESSAGE BODY
method string requiredValue:  result object channel string requiredValue:  symbol string requiredExample: "BTC/USD"The currency pair associated with this subscription.event_trigger string Possible values: [, ] Default value: 
The book event that causes a new ticker update to be published on the channel.
- : on a change in the best-bid-offer price levels.
- : on every trade.
success boolean Possible values: [, ]  Indicates if the request was successfully processed by the engine.error string conditionalCondition:  If success is false.  Error message.time_in string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the subscription was received on the wire, just prior to parsing data.time_out string Format: RFC3339Example: 2022-12-25T09:30:59.123456ZThe timestamp when the acknowledgement was sent on the wire, just prior to transmitting data.req_id integer Optional client originated request identifier sent as acknowledgment in the response.