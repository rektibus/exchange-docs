# Backpack API Documentation

Auto-fetched from 1 page(s)


---

# Source: https://docs.backpack.exchange/

  * Introduction
  * Authentication
    * Signing requests
  * Changelog
    * 2025-11-12
    * 2025-11-10
    * 2025-10-23
    * 2025-09-02
    * 2025-09-01
    * 2025-08-07
    * 2025-06-08
    * 2025-04-22
    * 2025-04-08
    * 2025-03-26
    * 2025-03-19
    * 2025-02-28
    * 2025-02-11
    * 2025-02-07
    * 2025-02-03
    * 2025-01-09
    * 2024-12-03
    * 2024-12-02
    * 2024-11-10
    * 2024-10-15
    * 2024-05-14
    * 2024-05-03
    * 2024-05-02
    * 2024-05-01
    * 2024-03-14
    * 2024-02-28
    * 2024-02-24
    * 2024-01-16
    * 2024-01-11
  * Public Endpoints
    * Assets
      * getGet assets.
      * getGet collateral.
    * Borrow Lend Markets
      * getGet borrow lend markets.
      * getGet borrow lend market history.
      * getGet APY rates for borrow/lend markets and staking.
    * Markets
      * getGet markets.
      * getGet market.
      * getGet ticker.
      * getGet tickers.
      * getGet depth.
      * getGet K-lines.
      * getGet prediction events.
      * getGet prediction tags.
      * getGet mark prices.
      * getGet open interest.
      * getGet funding interval rates.
    * System
      * getGet system status.
      * getPing.
      * getGet system time.
      * getGet wallets.
    * Trades
      * getGet recent trades.
      * getGet historical trades.
  * Authenticated Endpoints
    * Account
      * getGet account.
      * patchUpdate account.
      * getGet max borrow quantity.
      * getGet max order quantity.
      * getGet max withdrawal quantity.
    * Borrow Lend
      * getGet borrow lend positions.
      * getGet estimated liquidation price.
      * postExecute borrow lend.
      * getGet borrow history.
      * getGet interest history.
      * getGet borrow position history.
    * Capital
      * postConvert a dust balance.
      * getGet balances.
      * getGet collateral.
      * getGet deposits.
      * getGet deposit address.
      * getGet withdrawals.
      * postRequest withdrawal.
      * getGet dust conversion history.
      * getGet settlement history.
    * Order
      * getGet open order.
      * postExecute order.
      * delCancel open order.
      * postExecute orders.
      * getGet open orders.
      * delCancel open orders.
      * getGet fill history.
      * getGet order history.
    * Position
      * getGet open positions.
      * getGet funding payments.
      * getGet position history.
    * RFQ
      * postSubmit quote.
      * postSubmit RFQ.
      * postAccept quote.
      * postRefresh RFQ.
      * postCancel RFQ.
      * getGet RFQ history.
      * getGet quote history.
      * getGet RFQ fill history.
      * getGet quote fill history.
    * Strategy
      * getGet open strategy.
      * postCreate strategy.
      * delCancel open strategy.
      * getGet open strategies.
      * delCancel open strategies.
      * getGet strategy history.
  * Websocket
    * Streams
      * Usage
        * Subscribing
        * Timing
        * Keeping the connection alive
      * Private
        * Order update
        * Position update
        * RFQ Update
      * Public
        * Book ticker
        * Depth
        * K-Line
        * Liquidation
        * Mark price
        * Ticker
        * Open interest
        * Trade



[API docs by Redocly](https://redocly.com/redoc/)

# Backpack Exchange API (1.0)

Download OpenAPI specification:

## [](#section/Introduction)Introduction

Welcome to the Backpack Exchange API. This API is for programmatic trade execution. All of the endpoints require requests to be signed with an ED25519 keypair for authentication.

The API is hosted at `https://api.backpack.exchange/` and the WS API is hosted at `wss://ws.backpack.exchange/`.

## [](#section/Authentication)Authentication

## [](#section/Authentication/Signing-requests)Signing requests

Signed requests are required for any API calls that mutate state. Additionally, some read only requests can be performed by signing or via session authentication.

Signed requests require the following additional headers:

  * `X-Timestamp` \- Unix time in milliseconds that the request was sent.
  * `X-Window` \- Time window in milliseconds that the request is valid for, default is `5000` and maximum is `60000`.
  * `X-API-Key` \- Base64 encoded verifying key of the ED25519 keypair.
  * `X-Signature` \- Base64 encoded signature generated according to the instructions below.



### Generate ED25519 Keys

You can generate a private/public ED25519 keypair using this Python one-liner:
    
    
    python3 -c "from cryptography.hazmat.primitives.asymmetric import ed25519; import base64; key = ed25519.Ed25519PrivateKey.generate(); seed = key.private_bytes_raw(); pub = key.public_key().public_bytes_raw(); print(f'Seed: {base64.b64encode(seed).decode()}\nPublic Key: {base64.b64encode(pub).decode()}')"
    

This will output your base64-encoded private key (seed) and public key that can be used for API authentication.

### Signature Generation

To generate a signature perform the following:

  1. The key/values of the request body or query parameters should be ordered alphabetically and then turned into query string format.

  2. Append the header values for the timestamp and receive window to the above generated string in the format `&timestamp=<timestamp>&window=<window>`. If no `X-Window` header is passed the default value of `5000` still needs to be added to the signing string.




Each request also has an instruction type, valid instructions are:
    
    
    accountQuery
    balanceQuery
    borrowLendExecute
    borrowHistoryQueryAll
    collateralQuery
    depositAddressQuery
    depositQueryAll
    fillHistoryQueryAll
    fundingHistoryQueryAll
    interestHistoryQueryAll
    orderCancel
    orderCancelAll
    orderExecute
    orderHistoryQueryAll
    orderQuery
    orderQueryAll
    pnlHistoryQueryAll
    positionHistoryQueryAll
    positionQuery
    quoteSubmit
    strategyCancel
    strategyCancelAll
    strategyCreate
    strategyHistoryQueryAll
    strategyQuery
    strategyQueryAll
    withdraw
    withdrawalQueryAll
    

The correct instruction type should be prefixed to the signing string. The instruction types for each request are documented alongside the request.

For example, an API request to cancel an order with the following body:
    
    
    {
        "orderId": 28
        "symbol": "BTC_USDT",
    }
    

Would require the following to be signed:
    
    
    instruction=orderCancel&orderId=28&symbol=BTC_USDT&timestamp=1614550000000&window=5000
    

Regarding batch order execution (`POST /orders`), for each order in the batch, the order parameters should be ordered alphabetically and then turned into query string format. The orderExecute instruction should then be prefixed to that string. The query strings for the orders should be concatenated with `&` and the timestamp and window appended at the end.

For example, an API request for an order execution batch with the following body:
    
    
    [
        {
            "symbol": "SOL_USDC_PERP",
            "side": "Bid",
            "orderType": "Limit",
            "price": "141",
            "quantity": "12"
        },
        {
            "symbol": "SOL_USDC_PERP",
            "side": "Bid",
            "orderType": "Limit",
            "price": "140",
            "quantity": "11"
        }
    ]
    

Would require the following to be signed:
    
    
    instruction=orderExecute&orderType=Limit&price=141&quantity=12&side=Bid&symbol=SOL_USDC_PERP&instruction=orderExecute&orderType=Limit&price=140&quantity=11&side=Bid&symbol=SOL_USDC_PERP&timestamp=1750793021519&window=5000
    

If the API endpoint requires query parameters instead of a request body, the same procedure should be used on the query parameters. If the API endpoint does not have a request body or query parameters, only the timestamp and receive window need to be signed.

This message should be signed using the private key of the ED25519 keypair that corresponds to the public key in the `X-API-Key` header. The signature should then be base64 encoded and submitted in the `X-Signature` header.

  
  


* * *

## [](#section/Changelog)Changelog

## [](#section/Changelog/2025-11-12)2025-11-12

  * Backstop liquidation fills now include a non-zero `tradeId` field on an on-going basis. Previously such fills had a zero `tradeId`. This applies to the `/fills` endpoint as well as the trade stream.



## [](#section/Changelog/2025-11-10)2025-11-10

  * Add a specific error message for withdrawal attempts to non-2FA exempt withdrawal addresses.
  * Set a default limit of `1000` levels each side of the book for `/depth` endpoint.



## [](#section/Changelog/2025-10-23)2025-10-23

  * Add `j` and `k` fields to the order update stream (take profit limit price and stop loss limit price).



## [](#section/Changelog/2025-09-02)2025-09-02

  * The `/depth` endpoint now returns a limit of 5,000 price levels on each side of the book.



## [](#section/Changelog/2025-09-01)2025-09-01

  * The `cumulativeInterest` response field is being removed from the `/position`endpoint.
  * Estimated liquidation price or `l` is being removed from the position update stream. It will remain as a placeholder and be set to 0. It will be removed in the future, so client's should not rely on its presence.
  * Liquidation price can be queried for a single position using the Positions API `/position` for example `/position?symbol=BTC_USDC_PERP`.



## [](#section/Changelog/2025-08-07)2025-08-07

  * `/history/pnl` has been removed.



## [](#section/Changelog/2025-06-08)2025-06-08

  * The order id format is changing, it is no longer a byte shifted timestamp. It is no longer possible to derive the order timestamp from the order id. This change will take place at Monday June 9th, 01:00 UTC.



## [](#section/Changelog/2025-04-22)2025-04-22

  * The `/fills` endpoint now returns all fills for the account, including fills from system orders as well as client orders. System orders include liquidations, ADLs and collateral conversions. Previously, by default, it only returned fills from client orders. This behavior can be achieved by setting the `fillType` parameter to `User`.



## [](#section/Changelog/2025-04-08)2025-04-08

  * Added funding rate lower and upper bounds to `/markets` and `/market` endpoints.



## [](#section/Changelog/2025-03-26)2025-03-26

  * Add open interest stream `openInterest.<symbol>`.
  * Added the option to query `/history/borrowLend/positions` with a signed request using the instruction `borrowPositionHistoryQueryAll`.



## [](#section/Changelog/2025-03-19)2025-03-19

  * The leverage filter has been removed from `/markets` and `/market` endpoints.
  * Added `/openInterest` now takes `symbol` as an optional parameter. When not set, all markets are returned.
  * `/openInterests` has been deprecated.
  * Add stop loss and take profit fields to `/orders/execute`.
  * Add `I` field to the order update stream (related order id).
  * Add `a` and `b` fields to the order update stream (take profit trigger price and stop loss trigger price).



## [](#section/Changelog/2025-02-28)2025-02-28

  * Added `clientId` to fill history.



## [](#section/Changelog/2025-02-11)2025-02-11

  * An `O` field has been added to the order update stream. It denotes the origin of the update. The possible values are:
    * `USER`: The origin of the update was due to order entry by the user.
    * `LIQUIDATION_AUTOCLOSE`: The origin of the update was due to a liquidation by the liquidation engine.
    * `ADL_AUTOCLOSE`: The origin of the update was due to an ADL (auto-deleveraging) event.
    * `COLLATERAL_CONVERSION`: The origin of the update was due to a collateral conversion to settle debt on the account.
    * `SETTLEMENT_AUTOCLOSE`: The origin of the update was due to the settlement of a position on a dated market.
    * `BACKSTOP_LIQUIDITY_PROVIDER`: The origin of the update was due to a backstop liquidity provider facilitating a liquidation.



## [](#section/Changelog/2025-02-07)2025-02-07

  * Added `r` to denote a reduce only order on the order updates stream.
  * Added `reduceOnly` to the get orders endpoint.



## [](#section/Changelog/2025-02-03)2025-02-03

  * Added `openInterestLimit` to the markets endpoint. Applicable to futures markets only.
  * Added `orderModified` event to the order update stream. A resting reduce only order's quantity can be decreased in order to prevent position side reversal.



## [](#section/Changelog/2025-01-09)2025-01-09

  * Added `marketType` to the markets endpoint.
  * Added an optional `marketType` filter to the fills and the orders endpoints.



## [](#section/Changelog/2024-12-03)2024-12-03

  * Add order expiry reason to order update stream.
  * Add `cumulativeInterest` to borrow lend position.



## [](#section/Changelog/2024-12-02)2024-12-02

  * Add borrow lend history per position endpoint.



## [](#section/Changelog/2024-11-10)2024-11-10

  * Add `timestamp` field denoting the system time in unix-epoch microseconds to the depth endpoint.



## [](#section/Changelog/2024-10-15)2024-10-15

  * Convert all error responses to JSON and add a error code.



## [](#section/Changelog/2024-05-14)2024-05-14

  * Add `executedQuantity` and `executedQuoteQuantity` to order history endpoint.



## [](#section/Changelog/2024-05-03)2024-05-03

  * Add single market order update stream `account.orderUpdate.<symbol>`.



## [](#section/Changelog/2024-05-02)2024-05-02

  * Add optional `from` and `to` timestamp to get withdrawals endpoint.



## [](#section/Changelog/2024-05-01)2024-05-01

  * Add optional `from` and `to` timestamp to get deposits endpoint.



## [](#section/Changelog/2024-03-14)2024-03-14

  * Add optional `orderId` filter to order history endpoint.
  * Add optional `from` and `to` timestamp to order fills endpoint.



## [](#section/Changelog/2024-02-28)2024-02-28

  * Return the withdrawal in request withdrawal response.



## [](#section/Changelog/2024-02-24)2024-02-24

  * An additional field `t` was added to the private order update stream. It is the `trade_id` of the fill that generated the order update.
  * Added a maximum value for the `X-Window` header of `60000`.



## [](#section/Changelog/2024-01-16)2024-01-16

### Breaking

  * A new websocket API is available at `wss://ws.backpack.exchange`. Please see the documentation. The previous API remains on the same endpoint and will be deprecated after a migration period. The new API changes the following:
    * Subscription endpoint is now `wss://ws.backpack.exchange` instead of `wss://ws.backpack.exchange/stream`.
    * Can subscribe and unsubscribe to/from multiple streams by passing more than one in the `params` field.
    * Signature should now be sent in a separate `signature` field.
    * Signature instruction changed from `accountQuery` to `subscribe`.
    * Event and engine timestamps are now in `microseconds` instead of `milliseconds`.
    * Add engine timestamp to `bookTicker`, `depth`, and `order` streams.
    * Add quote asset volume to ticker stream.
    * Add sequential trade id to trade stream.
    * Rename the event type in the depth stream from `depthEvent` to `depth`.
    * Change the format of streams from `<symbol>@<type>` to `<type>.<symbol>` or `kline.<interval>.<symbol>` for K-lines.
    * Flatten the K-Line in the K-line stream so its not nested.



## [](#section/Changelog/2024-01-11)2024-01-11

### Breaking

  * Replaced `identifier` field on deposits with `transaction_hash` and `provider_id`. This aims to provide clearer representation of the field, particularly for fiat deposits.
  * Removed duplicate `pending` values from the `WithdrawalStatus` and `DepositStatus` spec enum.



  
  


* * *

## [](#tag/Assets)Assets

Assets and collateral data.

## [](#tag/Assets/operation/get_assets)Get assets.

### Responses

**200 **

Success.

**500 **

Internal server error.

get/api/v1/assets

https://api.backpack.exchange/api/v1/assets

###  Response samples

  * 200
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "symbol": "BTC",

    * "displayName": "string",

    * "coingeckoId": "string",

    * "tokens": [
      * {
        * "displayName": "string",

        * "blockchain": "0G",

        * "contractAddress": "string",

        * "depositEnabled": true,

        * "minimumDeposit": "string",

        * "withdrawEnabled": true,

        * "minimumWithdrawal": "string",

        * "maximumWithdrawal": "string",

        * "withdrawalFee": "string",

        * "nativeDecimals": 0

}

]

}


]`

## [](#tag/Assets/operation/get_collateral_parameters)Get collateral.

Get collateral parameters for assets.

### Responses

**200 **

Success.

**500 **

Internal server error.

get/api/v1/collateral

https://api.backpack.exchange/api/v1/collateral

###  Response samples

  * 200
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "symbol": "string",

    * "imfFunction": {
      * "type": "sqrt",

      * "base": "string",

      * "factor": "string"

},

    * "mmfFunction": {
      * "type": "sqrt",

      * "base": "string",

      * "factor": "string"

},

    * "haircutFunction": {
      * "weight": "string",

      * "kind": {
        * "type": "identity"

}

}

}


]`

## [](#tag/Borrow-Lend-Markets)Borrow Lend Markets

Borrowing and lending.

## [](#tag/Borrow-Lend-Markets/operation/get_borrow_lend_markets)Get borrow lend markets.

### Responses

**200 **

Success.

**500 **

Internal server error.

**502 **

Bad gateway.

get/api/v1/borrowLend/markets

https://api.backpack.exchange/api/v1/borrowLend/markets

###  Response samples

  * 200
  * 500
  * 502



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "state": "Open",

    * "assetMarkPrice": "string",

    * "borrowInterestRate": "string",

    * "borrowedQuantity": "string",

    * "fee": "string",

    * "lendInterestRate": "string",

    * "lentQuantity": "string",

    * "maxUtilization": "string",

    * "openBorrowLendLimit": "string",

    * "optimalUtilization": "string",

    * "symbol": "BTC",

    * "timestamp": "2019-08-24T14:15:22Z",

    * "throttleUtilizationThreshold": "string",

    * "throttleUtilizationBound": "string",

    * "throttleUpdateFraction": "string",

    * "utilization": "string",

    * "stepSize": "string"

}


]`

## [](#tag/Borrow-Lend-Markets/operation/get_borrow_lend_markets_history)Get borrow lend market history.

##### query Parameters

intervalrequired| string (BorrowLendMarketHistoryInterval)  Enum: "1d" "1w" "1month" "1year" Filter for an interval.  
---|---  
symbol| string Market symbol to query. If not set, all markets are returned.  
  
### Responses

**200 **

Success.

**500 **

Internal server error.

get/api/v1/borrowLend/markets/history

https://api.backpack.exchange/api/v1/borrowLend/markets/history

###  Response samples

  * 200
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "borrowInterestRate": "string",

    * "borrowedQuantity": "string",

    * "lendInterestRate": "string",

    * "lentQuantity": "string",

    * "timestamp": "2019-08-24T14:15:22Z",

    * "utilization": "string"

}


]`

## [](#tag/Borrow-Lend-Markets/operation/get_apy_rates)Get APY rates for borrow/lend markets and staking.

### Responses

**200 **

Success.

**500 **

Internal server error.

get/api/v1/borrowLend/apy

https://api.backpack.exchange/api/v1/borrowLend/apy

###  Response samples

  * 200
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`{

  * "borrowLend": [
    * {
      * "symbol": "BTC",

      * "borrowRate": "string",

      * "lendRate": "string"

}

],

  * "staking": [
    * {
      * "symbol": "string",

      * "dilutionFactor": "string",

      * "stakingRate": "string"

}

]


}`

## [](#tag/Markets)Markets

Public market data.

## [](#tag/Markets/operation/get_markets)Get markets.

Retrieves all the markets that are supported by the exchange.

##### query Parameters

marketType| Array of strings (MarketType) Items Enum: "SPOT" "PERP" "IPERP" "DATED" "PREDICTION" "RFQ" Market type. Defaults to return spot and perp.  
---|---  
  
### Responses

**200 **

Success.

**500 **

Internal server error.

get/api/v1/markets

https://api.backpack.exchange/api/v1/markets

###  Response samples

  * 200
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "symbol": "string",

    * "baseSymbol": "BTC",

    * "quoteSymbol": "BTC",

    * "marketType": "SPOT",

    * "filters": {
      * "price": {
        * "minPrice": "string",

        * "maxPrice": "string",

        * "tickSize": "string",

        * "maxMultiplier": "string",

        * "minMultiplier": "string",

        * "maxImpactMultiplier": "string",

        * "minImpactMultiplier": "string",

        * "meanMarkPriceBand": {
          * "maxMultiplier": "string",

          * "minMultiplier": "string"

},

        * "meanPremiumBand": {
          * "tolerancePct": "string"

},

        * "borrowEntryFeeMaxMultiplier": "string",

        * "borrowEntryFeeMinMultiplier": "string"

},

      * "quantity": {
        * "minQuantity": "string",

        * "maxQuantity": "string",

        * "stepSize": "string"

}

},

    * "imfFunction": {
      * "type": "sqrt",

      * "base": "string",

      * "factor": "string"

},

    * "mmfFunction": {
      * "type": "sqrt",

      * "base": "string",

      * "factor": "string"

},

    * "fundingInterval": 0,

    * "fundingRateUpperBound": "string",

    * "fundingRateLowerBound": "string",

    * "openInterestLimit": "string",

    * "orderBookState": "Open",

    * "createdAt": "string",

    * "visible": true,

    * "positionLimitWeight": "string"

}


]`

## [](#tag/Markets/operation/get_market)Get market.

Retrieves a market supported by the exchange.

##### query Parameters

symbolrequired| string  
---|---  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/market

https://api.backpack.exchange/api/v1/market

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`{

  * "symbol": "string",

  * "baseSymbol": "BTC",

  * "quoteSymbol": "BTC",

  * "marketType": "SPOT",

  * "filters": {
    * "price": {
      * "minPrice": "string",

      * "maxPrice": "string",

      * "tickSize": "string",

      * "maxMultiplier": "string",

      * "minMultiplier": "string",

      * "maxImpactMultiplier": "string",

      * "minImpactMultiplier": "string",

      * "meanMarkPriceBand": {
        * "maxMultiplier": "string",

        * "minMultiplier": "string"

},

      * "meanPremiumBand": {
        * "tolerancePct": "string"

},

      * "borrowEntryFeeMaxMultiplier": "string",

      * "borrowEntryFeeMinMultiplier": "string"

},

    * "quantity": {
      * "minQuantity": "string",

      * "maxQuantity": "string",

      * "stepSize": "string"

}

},

  * "imfFunction": {
    * "type": "sqrt",

    * "base": "string",

    * "factor": "string"

},

  * "mmfFunction": {
    * "type": "sqrt",

    * "base": "string",

    * "factor": "string"

},

  * "fundingInterval": 0,

  * "fundingRateUpperBound": "string",

  * "fundingRateLowerBound": "string",

  * "openInterestLimit": "string",

  * "orderBookState": "Open",

  * "createdAt": "string",

  * "visible": true,

  * "positionLimitWeight": "string"


}`

## [](#tag/Markets/operation/get_ticker)Get ticker.

Retrieves summarised statistics for the last 24 hours for the given market symbol.

##### query Parameters

symbolrequired| string  
---|---  
interval| string (TickerInterval)  Enum: "1d" "1w"  
  
### Responses

**200 **

Success.

**204 **

Not found.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/ticker

https://api.backpack.exchange/api/v1/ticker

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

`{

  * "symbol": "string",

  * "firstPrice": "string",

  * "lastPrice": "string",

  * "priceChange": "string",

  * "priceChangePercent": "string",

  * "high": "string",

  * "low": "string",

  * "volume": "string",

  * "quoteVolume": "string",

  * "trades": "string"


}`

## [](#tag/Markets/operation/get_tickers)Get tickers.

Retrieves summarised statistics for the last 24 hours for all market symbols.

##### query Parameters

interval| string (TickerInterval)  Enum: "1d" "1w"  
---|---  
  
### Responses

**200 **

Success.

**500 **

Internal server error.

get/api/v1/tickers

https://api.backpack.exchange/api/v1/tickers

###  Response samples

  * 200
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "symbol": "string",

    * "firstPrice": "string",

    * "lastPrice": "string",

    * "priceChange": "string",

    * "priceChangePercent": "string",

    * "high": "string",

    * "low": "string",

    * "volume": "string",

    * "quoteVolume": "string",

    * "trades": "string"

}


]`

## [](#tag/Markets/operation/get_depth)Get depth.

Retrieves the order book depth for a given market symbol.

##### query Parameters

symbolrequired| string  
---|---  
limit| string (DepthLimit)  Enum: "5" "10" "20" "50" "100" "500" "1000" Limit on the number of price levels to return on each side. Defaults to `1000`.  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

get/api/v1/depth

https://api.backpack.exchange/api/v1/depth

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`{

  * "asks": [
    * [
      * "21.9",

      * "500.123"

],

    * [
      * "22.1",

      * "2321.11"

]

],

  * "bids": [
    * [
      * "20.12",

      * "255.123"

],

    * [
      * "20.5",

      * "499.555"

]

],

  * "lastUpdateId": "1684026955123",

  * "timestamp": 1684026955123


}`

## [](#tag/Markets/operation/get_klines)Get K-lines.

Get K-Lines for the given market symbol, optionally providing a `startTime` and `endTime`. If no `endTime` is provided, the current time will be used.

The `priceType` parameter can be used to specify the price type of the kline. If not provided, the default is `LastPrice`.

##### query Parameters

symbolrequired| string Market symbol for the kline query, e.g. SOL_USDC.  
---|---  
intervalrequired| string (KlineInterval)  Enum: "1m" "3m" "5m" "15m" "30m" "1h" "2h" "4h" "6h" "8h" "12h" "1d" "3d" "1w" "1month"  
startTimerequired| integer <int64> UTC timestamp in seconds.  
endTime| integer <int64> UTC timestamp in seconds. Set to the current time if not provided.  
priceType| string (KlinePriceType)  Enum: "Last" "Index" "Mark" The price type of the K-line.  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/klines

https://api.backpack.exchange/api/v1/klines

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "start": "string",

    * "end": "string",

    * "open": "string",

    * "high": "string",

    * "low": "string",

    * "close": "string",

    * "volume": "string",

    * "quoteVolume": "string",

    * "trades": "string"

}


]`

## [](#tag/Markets/operation/get_prediction_events)Get prediction events.

Retrieves all the events and associated markets that are supported by the exchange.

##### query Parameters

symbol| string The market symbol for the prediction market.  
---|---  
tagSlug| string The tag slug of the prediction event.  
eventSlug| string The event slug that the prediction market is based on.  
seriesSlug| string The series slug that the prediction event belongs to.  
resolved| boolean Whether the prediction market is resolved.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/prediction

https://api.backpack.exchange/api/v1/prediction

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "slug": "string",

    * "title": "string",

    * "predictionMarkets": [
      * {
        * "marketSymbol": "string",

        * "question": "string",

        * "groupLabel": "string",

        * "yesOutcomeLabel": "string",

        * "noOutcomeLabel": "string",

        * "rules": "string",

        * "resolvedAt": "string",

        * "resolutionPrice": "string",

        * "activePrice": "string",

        * "quoteVolume": "string",

        * "quoteVolumeLifetime": "string",

        * "imgUrl": "string",

        * "resolutionCondition": {
          * "type": "QuantityRange",

          * "greaterThanOrEqual": "string",

          * "lessThan": "string"

},

        * "proposedResolution": true,

        * "proposedResolutionAt": "string"

}

],

    * "tags": [
      * {
        * "slug": "string",

        * "title": "string"

}

],

    * "series": [
      * {
        * "slug": "string",

        * "title": "string",

        * "recurrence": "hourly"

}

],

    * "description": "string",

    * "imgUrl": "string",

    * "quoteVolume": "string",

    * "resolution": {
      * "resolved": true,

      * "startDate": "string",

      * "endDate": "string",

      * "strikePrice": "string",

      * "closePrice": "string",

      * "resolutionSourceEventIdentifier": "string",

      * "resolutionSource": "binance",

      * "outcome": "string"

},

    * "estimatedEndDate": "string",

    * "resolved": true

}


]`

## [](#tag/Markets/operation/get_prediction_tags)Get prediction tags.

Retrieves prediction tags supported by the exchange with pagination.

##### query Parameters

limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
---|---  
offset| integer <uint64> Offset. Default `0`.  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/prediction/tags

https://api.backpack.exchange/api/v1/prediction/tags

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "slug": "string",

    * "title": "string"

}


]`

## [](#tag/Markets/operation/get_mark_prices)Get mark prices.

Retrieves mark prices, index prices, and funding rates for futures products, or a specified symbol.

##### query Parameters

symbol| string  
---|---  
marketType| string (MarketType)  Enum: "SPOT" "PERP" "IPERP" "DATED" "PREDICTION" "RFQ" Market type. Defaults to return perp.  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/markPrices

https://api.backpack.exchange/api/v1/markPrices

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "fundingRate": "string",

    * "indexPrice": "string",

    * "markPrice": "string",

    * "nextFundingTimestamp": 0,

    * "symbol": "string"

}


]`

## [](#tag/Markets/operation/get_open_interest)Get open interest.

Retrieves the current open interest for the given market. If no market is provided, then all markets are returned.

##### query Parameters

symbol| string  
---|---  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/openInterest

https://api.backpack.exchange/api/v1/openInterest

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "symbol": "string",

    * "openInterest": "string",

    * "timestamp": 0

}


]`

## [](#tag/Markets/operation/get_funding_interval_rates)Get funding interval rates.

Funding interval rate history for futures.

##### query Parameters

symbolrequired| string Market symbol to query  
---|---  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `10000`.  
offset| integer <uint64> Offset for pagination. Default `0`.  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/fundingRates

https://api.backpack.exchange/api/v1/fundingRates

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "symbol": "string",

    * "intervalEndTimestamp": "string",

    * "fundingRate": "string"

}


]`

## [](#tag/System)System

Exchange system status.

## [](#tag/System/operation/get_status)Get system status.

### Responses

**200 **

Success.

get/api/v1/status

https://api.backpack.exchange/api/v1/status

###  Response samples

  * 200



Content type

application/json; charset=utf-8

Copy

`{

  * "status": "Ok",

  * "message": "string"


}`

## [](#tag/System/operation/ping)Ping.

Responds with `pong`.

### Responses

**200 **

get/api/v1/ping

https://api.backpack.exchange/api/v1/ping

## [](#tag/System/operation/get_time)Get system time.

Retrieves the current system time.

### Responses

**200 **

get/api/v1/time

https://api.backpack.exchange/api/v1/time

## [](#tag/System/operation/get_wallets)Get wallets.

Returns all configured blockchain wallets and their addresses.

### Responses

**200 **

Success.

get/api/v1/wallets

https://api.backpack.exchange/api/v1/wallets

###  Response samples

  * 200



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "blockchain": "string",

    * "address": "string"

}


]`

## [](#tag/Trades)Trades

Public trade data.

## [](#tag/Trades/operation/get_recent_trades)Get recent trades.

Retrieve the most recent trades for a symbol. This is public data and is not specific to any account.

The maximum available recent trades is `1000`. If you need more than `1000` trades use the historical trades endpoint.

##### query Parameters

symbolrequired| string Market symbol to query fills for.  
---|---  
limit| integer <uint16> Limit the number of fills returned. Default `100`, maximum `1000`.  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal Server Error.

get/api/v1/trades

https://api.backpack.exchange/api/v1/trades

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "id": 0,

    * "price": "string",

    * "quantity": "string",

    * "quoteQuantity": "string",

    * "timestamp": 0,

    * "isBuyerMaker": true

}


]`

## [](#tag/Trades/operation/get_historical_trades)Get historical trades.

Retrieves all historical trades for the given symbol. This is public trade data and is not specific to any account.

##### query Parameters

symbolrequired| string  
---|---  
limit| integer <uint64> Limit the number of trades returned. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal Server Error.

get/api/v1/trades/history

https://api.backpack.exchange/api/v1/trades/history

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "id": 0,

    * "price": "string",

    * "quantity": "string",

    * "quoteQuantity": "string",

    * "timestamp": 0,

    * "isBuyerMaker": true

}


]`

## [](#tag/Account)Account

Account settings and limits.

## [](#tag/Account/operation/get_account)Get account.

**Instruction:** `accountQuery`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/account

https://api.backpack.exchange/api/v1/account

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

`{

  * "autoBorrowSettlements": true,

  * "autoLend": true,

  * "autoRealizePnl": true,

  * "autoRepayBorrows": true,

  * "borrowLimit": "string",

  * "futuresMakerFee": "string",

  * "futuresTakerFee": "string",

  * "leverageLimit": "string",

  * "limitOrders": 0,

  * "liquidating": true,

  * "positionLimit": "string",

  * "spotMakerFee": "string",

  * "spotTakerFee": "string",

  * "triggerOrders": 0


}`

## [](#tag/Account/operation/update_account_settings)Update account.

Update account settings.

**Instruction:** `accountUpdate`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

autoBorrowSettlements| boolean If true, then tries to borrow during collateral reconciliation. Collateral reconciliation is a process in which the system reconciles the negative account debt or positive account equity.  
---|---  
autoLend| boolean Determines if the account should automatically lend.  
autoRepayBorrows| boolean Determines if the account should automatically repay borrows with available balance.  
leverageLimit| string <decimal> Determines the maximum leverage allowed for the main account or subaccount.  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

**503 **

System under maintenance.

patch/api/v1/account

https://api.backpack.exchange/api/v1/account

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "autoBorrowSettlements": true,

  * "autoLend": true,

  * "autoRepayBorrows": true,

  * "leverageLimit": "string"


}`

###  Response samples

  * 400
  * 401
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "code": "ACCOUNT_DEACTIVATED",

  * "message": "string"


}`

## [](#tag/Account/operation/get_max_borrow_quantity)Get max borrow quantity.

Retrieves the maxmimum quantity an account can borrow for a given asset based on the accounts existing exposure and margin requirements

**Instruction:** `maxBorrowQuantity`

##### query Parameters

symbolrequired| string The asset to borrow.  
---|---  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

Service unavailable.

get/api/v1/account/limits/borrow

https://api.backpack.exchange/api/v1/account/limits/borrow

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "maxBorrowQuantity": "string",

  * "symbol": "string"


}`

## [](#tag/Account/operation/get_max_order_quantity)Get max order quantity.

Retrieves the maxmimum quantity an account can trade for a given symbol based on the account's balances, existing exposure and margin requirements.

**Instruction:** `maxOrderQuantity`

##### query Parameters

symbolrequired| string The market symbol to trade.  
---|---  
siderequired| string (Side)  Enum: "Bid" "Ask" The side of the order.  
price| string <decimal> The limit price of the order. Not included for market orders.  
reduceOnly| boolean Whether the order is reduce only.  
autoBorrow| boolean Whether the order uses auto borrow.  
autoBorrowRepay| boolean Whether the order uses auto borrow repay.  
autoLendRedeem| boolean Whether the order uses auto lend redeem.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/account/limits/order

https://api.backpack.exchange/api/v1/account/limits/order

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

`{

  * "autoBorrow": true,

  * "autoBorrowRepay": true,

  * "autoLendRedeem": true,

  * "maxOrderQuantity": "string",

  * "price": "string",

  * "side": "string",

  * "symbol": "string",

  * "reduceOnly": true


}`

## [](#tag/Account/operation/get_max_withdrawal_quantity)Get max withdrawal quantity.

Retrieves the maxmimum quantity an account can withdraw for a given asset based on the accounts existing exposure and margin requirements The response will include the maximum quantity that can be withdrawn and whether the withdrawal is with auto borrow or auto lend redeem enabled.

**Instruction:** `maxWithdrawalQuantity`

##### query Parameters

symbolrequired| string The asset to withdraw.  
---|---  
autoBorrow| boolean Whether the withdrawal is with auto borrow.  
autoLendRedeem| boolean Whether the withdrawal is with auto lend redeem.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/account/limits/withdrawal

https://api.backpack.exchange/api/v1/account/limits/withdrawal

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

`{

  * "autoBorrow": true,

  * "autoLendRedeem": true,

  * "maxWithdrawalQuantity": "string",

  * "symbol": "string"


}`

## [](#tag/Borrow-Lend)Borrow Lend

Borrowing and lending.

## [](#tag/Borrow-Lend/operation/get_borrow_lend_positions)Get borrow lend positions.

Retrieves all the open borrow lending positions for the account.

**Instruction:** `borrowLendPositionQuery`

##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/borrowLend/positions

https://api.backpack.exchange/api/v1/borrowLend/positions

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "cumulativeInterest": "string",

    * "id": "string",

    * "imf": "string",

    * "imfFunction": {
      * "type": "sqrt",

      * "base": "string",

      * "factor": "string"

},

    * "netQuantity": "string",

    * "markPrice": "string",

    * "mmf": "string",

    * "mmfFunction": {
      * "type": "sqrt",

      * "base": "string",

      * "factor": "string"

},

    * "netExposureQuantity": "string",

    * "netExposureNotional": "string",

    * "symbol": "BTC"

}


]`

## [](#tag/Borrow-Lend/operation/get_borrow_lend_estimated_liquidation_price)Get estimated liquidation price.

Retrieves the estimated liquidation price for a potential borrow lend position.

##### query Parameters

subaccountId| integer <uint16> Optional subaccount.  
---|---  
borrowrequired| string Standard base64 encoded json of [`BorrowLendExecutePayload`]  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/api/v1/borrowLend/position/liquidationPrice

https://api.backpack.exchange/api/v1/borrowLend/position/liquidationPrice

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

`{

  * "liquidationPrice": "string",

  * "markPrice": "string"


}`

## [](#tag/Borrow-Lend/operation/execute_borrow_lend)Execute borrow lend.

**Instruction:** `borrowLendExecute`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

quantityrequired| string <decimal> The quantity of the asset to repay.  
---|---  
siderequired| string Enum: "Borrow" "Lend" Side of the borrow lend.  
symbolrequired| string Enum: "BTC" "ETH" "SOL" "USDC" "USDT" "PYTH" "JTO" "BONK" "HNT" "MOBILE" "WIF" "JUP" "RENDER" "WEN" "W" "TNSR" "PRCL" "SHARK" "KMNO" "MEW" "BOME" "RAY" "HONEY" "SHFL" "BODEN" "IO" "DRIFT" "PEPE" "SHIB" "LINK" "UNI" "ONDO" "FTM" "MATIC" "STRK" "BLUR" "WLD" "GALA" "NYAN" "HLG" "MON" "ZKJ" "MANEKI" "HABIBI" "UNA" "ZRO" "ZEX" "AAVE" "LDO" "MOTHER" "CLOUD" "MAX" "POL" "TRUMPWIN" "HARRISWIN" "MOODENG" "DBR" "GOAT" "ACT" "DOGE" "BCH" "LTC" "APE" "ENA" "ME" "EIGEN" "CHILLGUY" "PENGU" "EUR" "SONIC" "J" "TRUMP" "MELANIA" "ANIME" "XRP" "SUI" "VINE" "ADA" "MOVE" "BERA" "IP" "HYPE" "BNB" "KAITO" "kPEPE" "kBONK" "kSHIB" "AVAX" "S" "POINTS" "ROAM" "AI16Z" "LAYER" "FARTCOIN" "NEAR" "PNUT" "ARB" "DOT" "APT" "OP" "PYUSD" "HUMA" "WAL" "DEEP" "CETUS" "SEND" "BLUE" "NS" "HAEDAL" "JPY" "TAO" "VIRTUAL" "TIA" "TRX" "FRAG" "PUMP" "WCT" "ES" "SEI" "CRV" "TON" "BPUSD" "HBAR" "XLM" "ZORA" "WLFI" "BPEUR" "SWTCH" "LINEA" "XPL" "BARD" "FLOCK" "AVNT" "PENDLE" "AERO" "ASTER" "GLXY" "0G" "2Z" "FWDI" "ZEUS" "APEX" "EDEN" "FF" "ORDER" "MNT" "ZEC" "PAXG" "MORPHO" "ATH" "KGEN" "XAUT" "FOGO" "SPX" "ETHFI" "APR" "PIPE" "MET" "MONP" "STABLE" "GUSDT" "BTCD121025" "BTCD121125" "BTCD121225" "SOLWP011526A160" "SOLD121125" "SOLD121225" "BTCW12122590000" "BTCW12122591000" "BTCW12122592000" "BTCW12122593000" "BTCW12122594000" "BTCW12122595000" "BTCW121225100000" "SOLW121225140000" "SOLW121225145000" "SOLW121225150000" "SOLW121225155000" "SOLW121225160000" "SOLW121225165000" "SOLW121225170000" "BTCM1225130000" "BTCM1225140000" "BTCM1225150000" "BTCM1225160000" "BTCM1225170000" "BTCM1225200000" "BTCM1225500000" "BTCM12251000000" "SOLDUD011226" "BTCDUD011326" "SOLDUD011326" "BTCDUD011426" "SOLDUD011426" "BTCDUD011526" "SOLDUD011526" "SOLWP011526U120" "SOLWP011526T120" "SOLWP011526T130" "SOLWP011526T140" "SOLWP011526T150" "DEMS28NEWSOM" "DEMS28AOC" "DEMS28BUTTIGIEG" "DEMS28SHAPIRO" "DEMS28KELLY" "DEMS28OSSOFF" "DEMS28KAMALA" "DEMS28MOORE" "DEMS28PRITZKER" "DEMS28BESHEAR" "DEMS28WHITMER" "DEMS28THEROCK" "DEMS28EMANUEL" "DEMS28MAMDANI" "LIT" "FOMC0126H0" "FOMC0126C25" "FOMC0126C50P" "FOMC0126H25P" "BTCWP011526U84" "BTCWP011526T84" "BTCWP011526T89" "BTCWP011526T94" "BTCWP011526T99" "BTCWP011526A104" "BTCDUD011026" "SOLDUD011026" "BTCDUD011126" "SOLDUD011126" "BTCDUD011226" "WHITEWHALE" "INX" "SKR" "XMR" "BTCWP011626T1" "BTCWP011626T2" "BTCWP011626T3" "BTCWP011626T4" "BTCWP011626T5" "BTCWP011626T6" "BTCWP011626T7" "BTCWP011626T8" "BTCWP011726T1" "BTCWP011726T2" "BTCWP011726T3" "BTCWP011726T4" "BTCWP011726T5" "BTCWP011726T6" "BTCWP011726T7" "BTCWP011726T8" "BTCWP011826T1" "BTCWP011826T2" "BTCWP011826T3" "BTCWP011826T4" "BTCWP011826T5" "BTCWP011826T6" "BTCWP011826T7" "BTCWP011826T8" "BTCWP011926T1" "BTCWP011926T2" "BTCWP011926T3" "BTCWP011926T4" "BTCWP011926T5" "BTCWP011926T6" "BTCWP011926T7" "BTCWP011926T8" "BTCWP012026T1" "BTCWP012026T2" "BTCWP012026T3" "BTCWP012026T4" "BTCWP012026T5" "BTCWP012026T6" "BTCWP012026T7" "BTCWP012026T8" "BTCWP012126T1" "BTCWP012126T2" "BTCWP012126T3" "BTCWP012126T4" "BTCWP012126T5" "BTCWP012126T6" "BTCWP012126T7" "BTCWP012126T8" "BTCWP012226T1" "BTCWP012226T2" "BTCWP012226T3" "BTCWP012226T4" "BTCWP012226T5" "BTCWP012226T6" "BTCWP012226T7" "BTCWP012226T8" "BTCWP012326T1" "BTCWP012326T2" "BTCWP012326T3" "BTCWP012326T4" "BTCWP012326T5" "BTCWP012326T6" "BTCWP012326T7" "BTCWP012326T8" "BTCWMS011626T1" "BTCWMS011626T2" "BTCWMS011626T3" "BTCWMS011626T4" "BTCWMS011626T5" "BTCWMS011626T6" "BTCWMS011626T7" "BTCWMS011626T8" "BTCWMS011726T1" "BTCWMS011726T2" "BTCWMS011726T3" "BTCWMS011726T4" "BTCWMS011726T5" "BTCWMS011726T6" "BTCWMS011726T7" "BTCWMS011726T8" "BTCWMS011826T1" "BTCWMS011826T2" "BTCWMS011826T3" "BTCWMS011826T4" "BTCWMS011826T5" "BTCWMS011826T6" "BTCWMS011826T7" "BTCWMS011826T8" "BTCWMS011926T1" "BTCWMS011926T2" "BTCWMS011926T3" "BTCWMS011926T4" "BTCWMS011926T5" "BTCWMS011926T6" "BTCWMS011926T7" "BTCWMS011926T8" "BTCWMS012026T1" "BTCWMS012026T2" "BTCWMS012026T3" "BTCWMS012026T4" "BTCWMS012026T5" "BTCWMS012026T6" "BTCWMS012026T7" "BTCWMS012026T8" "BTCWMS012126T1" "BTCWMS012126T2" "BTCWMS012126T3" "BTCWMS012126T4" "BTCWMS012126T5" "BTCWMS012126T6" "BTCWMS012126T7" "BTCWMS012126T8" "BTCWMS012226T1" "BTCWMS012226T2" "BTCWMS012226T3" "BTCWMS012226T4" "BTCWMS012226T5" "BTCWMS012226T6" "BTCWMS012226T7" "BTCWMS012226T8" "BTCWMS012326T1" "BTCWMS012326T2" "BTCWMS012326T3" "BTCWMS012326T4" "BTCWMS012326T5" "BTCWMS012326T6" "BTCWMS012326T7" "BTCWMS012326T8" "SOLWP011626T1" "SOLWP011626T2" "SOLWP011626T3" "SOLWP011626T4" "SOLWP011626T5" "SOLWP011726T1" "SOLWP011726T2" "SOLWP011726T3" "SOLWP011726T4" "SOLWP011726T5" "SOLWP011826T1" "SOLWP011826T2" "SOLWP011826T3" "SOLWP011826T4" "SOLWP011826T5" "SOLWP011926T1" "SOLWP011926T2" "SOLWP011926T3" "SOLWP011926T4" "SOLWP011926T5" "SOLWP012026T1" "SOLWP012026T2" "SOLWP012026T3" "SOLWP012026T4" "SOLWP012026T5" "SOLWP012126T1" "SOLWP012126T2" "SOLWP012126T3" "SOLWP012126T4" "SOLWP012126T5" "SOLWP012226T1" "SOLWP012226T2" "SOLWP012226T3" "SOLWP012226T4" "SOLWP012226T5" "SOLWP012326T1" "SOLWP012326T2" "SOLWP012326T3" "SOLWP012326T4" "SOLWP012326T5" "SOLWMS011626T1" "SOLWMS011626T2" "SOLWMS011626T3" "SOLWMS011626T4" "SOLWMS011626T5" "SOLWMS011726T1" "SOLWMS011726T2" "SOLWMS011726T3" "SOLWMS011726T4" "SOLWMS011726T5" "SOLWMS011826T1" "SOLWMS011826T2" "SOLWMS011826T3" "SOLWMS011826T4" "SOLWMS011826T5" "SOLWMS011926T1" "SOLWMS011926T2" "SOLWMS011926T3" "SOLWMS011926T4" "SOLWMS011926T5" "SOLWMS012026T1" "SOLWMS012026T2" "SOLWMS012026T3" "SOLWMS012026T4" "SOLWMS012026T5" "SOLWMS012126T1" "SOLWMS012126T2" "SOLWMS012126T3" "SOLWMS012126T4" "SOLWMS012126T5" "SOLWMS012226T1" "SOLWMS012226T2" "SOLWMS012226T3" "SOLWMS012226T4" "SOLWMS012226T5" "SOLWMS012326T1" "SOLWMS012326T2" "SOLWMS012326T3" "SOLWMS012326T4" "SOLWMS012326T5" "ETHWP011626T1" "ETHWP011626T2" "ETHWP011626T3" "ETHWP011626T4" "ETHWP011626T5" "ETHWP011626T6" "ETHWP011626T7" "ETHWP011626T8" "ETHWP011726T1" "ETHWP011726T2" "ETHWP011726T3" "ETHWP011726T4" "ETHWP011726T5" "ETHWP011726T6" "ETHWP011726T7" "ETHWP011726T8" "ETHWP011826T1" "ETHWP011826T2" "ETHWP011826T3" "ETHWP011826T4" "ETHWP011826T5" "ETHWP011826T6" "ETHWP011826T7" "ETHWP011826T8" "ETHWP011926T1" "ETHWP011926T2" "ETHWP011926T3" "ETHWP011926T4" "ETHWP011926T5" "ETHWP011926T6" "ETHWP011926T7" "ETHWP011926T8" "ETHWP012026T1" "ETHWP012026T2" "ETHWP012026T3" "ETHWP012026T4" "ETHWP012026T5" "ETHWP012026T6" "ETHWP012026T7" "ETHWP012026T8" "ETHWP012126T1" "ETHWP012126T2" "ETHWP012126T3" "ETHWP012126T4" "ETHWP012126T5" "ETHWP012126T6" "ETHWP012126T7" "ETHWP012126T8" "ETHWP012226T1" "ETHWP012226T2" "ETHWP012226T3" "ETHWP012226T4" "ETHWP012226T5" "ETHWP012226T6" "ETHWP012226T7" "ETHWP012226T8" "ETHWP012326T1" "ETHWP012326T2" "ETHWP012326T3" "ETHWP012326T4" "ETHWP012326T5" "ETHWP012326T6" "ETHWP012326T7" "ETHWP012326T8" "ETHWMS011626T1" "ETHWMS011626T2" "ETHWMS011626T3" "ETHWMS011626T4" "ETHWMS011626T5" "ETHWMS011626T6" "ETHWMS011626T7" "ETHWMS011626T8" "ETHWMS011726T1" "ETHWMS011726T2" "ETHWMS011726T3" "ETHWMS011726T4" "ETHWMS011726T5" "ETHWMS011726T6" "ETHWMS011726T7" "ETHWMS011726T8" "ETHWMS011826T1" "ETHWMS011826T2" "ETHWMS011826T3" "ETHWMS011826T4" "ETHWMS011826T5" "ETHWMS011826T6" "ETHWMS011826T7" "ETHWMS011826T8" "ETHWMS011926T1" "ETHWMS011926T2" "ETHWMS011926T3" "ETHWMS011926T4" "ETHWMS011926T5" "ETHWMS011926T6" "ETHWMS011926T7" "ETHWMS011926T8" "ETHWMS012026T1" "ETHWMS012026T2" "ETHWMS012026T3" "ETHWMS012026T4" "ETHWMS012026T5" "ETHWMS012026T6" "ETHWMS012026T7" "ETHWMS012026T8" "ETHWMS012126T1" "ETHWMS012126T2" "ETHWMS012126T3" "ETHWMS012126T4" "ETHWMS012126T5" "ETHWMS012126T6" "ETHWMS012126T7" "ETHWMS012126T8" "ETHWMS012226T1" "ETHWMS012226T2" "ETHWMS012226T3" "ETHWMS012226T4" "ETHWMS012226T5" "ETHWMS012226T6" "ETHWMS012226T7" "ETHWMS012226T8" "ETHWMS012326T1" "ETHWMS012326T2" "ETHWMS012326T3" "ETHWMS012326T4" "ETHWMS012326T5" "ETHWMS012326T6" "ETHWMS012326T7" "ETHWMS012326T8" "BTCDUD011626" "BTCDUD011726" "BTCDUD011826" "BTCDUD011926" "BTCDUD012026" "BTCDUD012126" "BTCDUD012226" "BTCDUD012326" "SOLDUD011626" "SOLDUD011726" "SOLDUD011826" "SOLDUD011926" "SOLDUD012026" "SOLDUD012126" "SOLDUD012226" "SOLDUD012326" "ETHDUD011626" "ETHDUD011726" "ETHDUD011826" "ETHDUD011926" "ETHDUD012026" "ETHDUD012126" "ETHDUD012226" "ETHDUD012326" "FDVEDGEX1B" "FDVEDGEX2B" "FDVEDGEX3B" "FDVEDGEX4B" "FDVEDGEX5B" "FDVEXTD300M" "FDVEXTD500M" "FDVEXTD800M" "FDVEXTD1B" "FDVEXTD2B" "FDVEXTD3B" "FDVPARA300M" "FDVPARA500M" "FDVPARA750M" "FDVPARA1N5B" "FDVPARA3B" "FDVPARA5B" "FDVINX200M" "FDVINX300M" "FDVINX400M" "FDVINX600M" "FDVINX800M" "FDVINX1B" "FDVVAR500M" "FDVVAR800M" "FDVVAR1B" "FDVVAR2B" "FDVVAR3B" "FDVVAR4B" "FDVVAR5B" "NBA26HA012026H" "NBA26HA012026A" "NBA26HA012026HN2" "NBA26HA012026AP2" "NBA26HA012026TTLO222" "NBA26HA012026TTLU222" "NBA26HA012026P1O30" "NBA26HA012026P1U30" "NHL26HA012026H" "NHL26HA012026A" "NHL26HA012026HN2" "NHL26HA012026AP2" "NHL26HA012026TTLO4" "NHL26HA012026TTLU4" "NHL26HA012026P1O2" "NHL26HA012026P1U2" "CC" "DASH" "AXS" "BTCWP012626T1" "BTCWP012626T2" "BTCWP012626T3" "BTCWP012626T4" "BTCWP012626T5" "BTCWP012626T6" "BTCWP012626T7" "BTCWP012626T8" "BTCWP012826T1" "BTCWP012826T2" "BTCWP012826T3" "BTCWP012826T4" "BTCWP012826T5" "BTCWP012826T6" "BTCWP012826T7" "BTCWP012826T8" "BTCWP013026T1" "BTCWP013026T2" "BTCWP013026T3" "BTCWP013026T4" "BTCWP013026T5" "BTCWP013026T6" "BTCWP013026T7" "BTCWP013026T8" "BTCWP020226T1" "BTCWP020226T2" "BTCWP020226T3" "BTCWP020226T4" "BTCWP020226T5" "BTCWP020226T6" "BTCWP020226T7" "BTCWP020226T8" "BTCWP020426T1" "BTCWP020426T2" "BTCWP020426T3" "BTCWP020426T4" "BTCWP020426T5" "BTCWP020426T6" "BTCWP020426T7" "BTCWP020426T8" "BTCWP020626T1" "BTCWP020626T2" "BTCWP020626T3" "BTCWP020626T4" "BTCWP020626T5" "BTCWP020626T6" "BTCWP020626T7" "BTCWP020626T8" "SOLWP012626T1" "SOLWP012626T2" "SOLWP012626T3" "SOLWP012626T4" "SOLWP012626T5" "SOLWP012626T6" "SOLWP012826T1" "SOLWP012826T2" "SOLWP012826T3" "SOLWP012826T4" "SOLWP012826T5" "SOLWP012826T6" "SOLWP013026T1" "SOLWP013026T2" "SOLWP013026T3" "SOLWP013026T4" "SOLWP013026T5" "SOLWP013026T6" "SOLWP020226T1" "SOLWP020226T2" "SOLWP020226T3" "SOLWP020226T4" "SOLWP020226T5" "SOLWP020226T6" "SOLWP020426T1" "SOLWP020426T2" "SOLWP020426T3" "SOLWP020426T4" "SOLWP020426T5" "SOLWP020426T6" "SOLWP020626T1" "SOLWP020626T2" "SOLWP020626T3" "SOLWP020626T4" "SOLWP020626T5" "SOLWP020626T6" "ETHWP012626T1" "ETHWP012626T2" "ETHWP012626T3" "ETHWP012626T4" "ETHWP012626T5" "ETHWP012626T6" "ETHWP012626T7" "ETHWP012626T8" "ETHWP012826T1" "ETHWP012826T2" "ETHWP012826T3" "ETHWP012826T4" "ETHWP012826T5" "ETHWP012826T6" "ETHWP012826T7" "ETHWP012826T8" "ETHWP013026T1" "ETHWP013026T2" "ETHWP013026T3" "ETHWP013026T4" "ETHWP013026T5" "ETHWP013026T6" "ETHWP013026T7" "ETHWP013026T8" "ETHWP020226T1" "ETHWP020226T2" "ETHWP020226T3" "ETHWP020226T4" "ETHWP020226T5" "ETHWP020226T6" "ETHWP020226T7" "ETHWP020226T8" "ETHWP020426T1" "ETHWP020426T2" "ETHWP020426T3" "ETHWP020426T4" "ETHWP020426T5" "ETHWP020426T6" "ETHWP020426T7" "ETHWP020426T8" "ETHWP020626T1" "ETHWP020626T2" "ETHWP020626T3" "ETHWP020626T4" "ETHWP020626T5" "ETHWP020626T6" "ETHWP020626T7" "ETHWP020626T8" "BTCDUD012426" "BTCDUD012526" "BTCDUD012626" "BTCDUD012726" "BTCDUD012826" "BTCDUD012926" "BTCDUD013026" "BTCDUD013126" "BTCDUD020126" "BTCDUD020226" "BTCDUD020326" "BTCDUD020426" "BTCDUD020526" "BTCDUD020626" "SOLDUD012426" "SOLDUD012526" "SOLDUD012626" "SOLDUD012726" "SOLDUD012826" "SOLDUD012926" "SOLDUD013026" "SOLDUD013126" "SOLDUD020126" "SOLDUD020226" "SOLDUD020326" "SOLDUD020426" "SOLDUD020526" "SOLDUD020626" "ETHDUD012426" "ETHDUD012526" "ETHDUD012626" "ETHDUD012726" "ETHDUD012826" "ETHDUD012926" "ETHDUD013026" "ETHDUD013126" "ETHDUD020126" "ETHDUD020226" "ETHDUD020326" "ETHDUD020426" "ETHDUD020526" "ETHDUD020626" "XRPUD012426" "XRPUD012526" "XRPUD012626" "XRPUD012726" "XRPUD012826" "XRPUD012926" "XRPUD013026" "XRPUD013126" "XRPUD020126" "XRPUD020226" "XRPUD020326" "XRPUD020426" "XRPUD020526" "XRPUD020626" "BNBUD012426" "BNBUD012526" "BNBUD012626" "BNBUD012726" "BNBUD012826" "BNBUD012926" "BNBUD013026" "BNBUD013126" "BNBUD020126" "BNBUD020226" "BNBUD020326" "BNBUD020426" "BNBUD020526" "BNBUD020626" "ZAMA" "MEGA" "RNBW" "BLT" The asset to repay.  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

post/api/v1/borrowLend

https://api.backpack.exchange/api/v1/borrowLend

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "quantity": "string",

  * "side": "Borrow",

  * "symbol": "BTC"


}`

###  Response samples

  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "code": "ACCOUNT_DEACTIVATED",

  * "message": "string"


}`

## [](#tag/Borrow-Lend/operation/get_borrow_lend_history)Get borrow history.

History of borrow and lend operations for the account.

**Instruction:** `borrowHistoryQueryAll`

##### query Parameters

type| string (BorrowLendEventType)  Enum: "Borrow" "BorrowRepay" "Lend" "LendRedeem" Filter to history for either borrows or lends.  
---|---  
sources| string Filter to return history for a particular source. Can be a single source, or multiple sources separated by commas.  
positionId| string Filter to return history for a borrow lend position.  
symbol| string Filter to the given symbol.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset for pagination. Default `0`.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/borrowLend

https://api.backpack.exchange/wapi/v1/history/borrowLend

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "eventType": "Borrow",

    * "positionId": "string",

    * "positionQuantity": "string",

    * "quantity": "string",

    * "source": "AdlProvider",

    * "symbol": "string",

    * "timestamp": "string",

    * "spotMarginOrderId": "string"

}


]`

## [](#tag/Borrow-Lend/operation/get_interest_history)Get interest history.

History of the interest payments for borrows and lends for the account.

**Instruction:** `interestHistoryQueryAll`

##### query Parameters

asset| string Asset to query. If not set, all assets are returned.  
---|---  
symbol| string Market symbol to query. If not set, all markets are returned. If a futures symbol is supplied, then interest payments on unrealized pnl will be returned. Spot market symbols refer to interest payments on regular borrow lend positions.  
positionId| string Filter to return history for a borrow lend position.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset for pagination. Default `0`.  
source| string (InterestPaymentSource)  Enum: "UnrealizedPnl" "BorrowLend" Filter to return interest payments of a particular source. Borrow interest payments through two mechanisms: borrow lend positions; interest paid on unrealized pnl.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/interest

https://api.backpack.exchange/wapi/v1/history/interest

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "paymentType": "EntryFee",

    * "interestRate": "string",

    * "interval": 0,

    * "marketSymbol": "string",

    * "positionId": "string",

    * "quantity": "string",

    * "symbol": "BTC",

    * "timestamp": "string"

}


]`

## [](#tag/Borrow-Lend/operation/get_borrow_lend_position_history)Get borrow position history.

History of borrow and lend positions for the account.

**Instruction:** `borrowPositionHistoryQueryAll`

##### query Parameters

symbol| string Filter to the given symbol.  
---|---  
side| string (BorrowLendSide)  Enum: "Borrow" "Lend" Return only borrows or only lends.  
state| string (BorrowLendPositionState)  Enum: "Open" "Closed" Return only open positions or closed positions.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset for pagination. Default `0`.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/borrowLend/positions

https://api.backpack.exchange/wapi/v1/history/borrowLend/positions

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "positionId": "string",

    * "quantity": "string",

    * "symbol": "string",

    * "source": "AdlProvider",

    * "cumulativeInterest": "string",

    * "avgInterestRate": "string",

    * "side": "Borrow",

    * "createdAt": "string"

}


]`

## [](#tag/Capital)Capital

Capital management.

## [](#tag/Capital/operation/convert_dust)Convert a dust balance.

Converts a dust balance to USDC. The balance (including lend) must be less than the minimum quantity tradable on the spot order book.

**Instruction:** `convertDust`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

symbol| string Enum: "BTC" "ETH" "SOL" "USDC" "USDT" "PYTH" "JTO" "BONK" "HNT" "MOBILE" "WIF" "JUP" "RENDER" "WEN" "W" "TNSR" "PRCL" "SHARK" "KMNO" "MEW" "BOME" "RAY" "HONEY" "SHFL" "BODEN" "IO" "DRIFT" "PEPE" "SHIB" "LINK" "UNI" "ONDO" "FTM" "MATIC" "STRK" "BLUR" "WLD" "GALA" "NYAN" "HLG" "MON" "ZKJ" "MANEKI" "HABIBI" "UNA" "ZRO" "ZEX" "AAVE" "LDO" "MOTHER" "CLOUD" "MAX" "POL" "TRUMPWIN" "HARRISWIN" "MOODENG" "DBR" "GOAT" "ACT" "DOGE" "BCH" "LTC" "APE" "ENA" "ME" "EIGEN" "CHILLGUY" "PENGU" "EUR" "SONIC" "J" "TRUMP" "MELANIA" "ANIME" "XRP" "SUI" "VINE" "ADA" "MOVE" "BERA" "IP" "HYPE" "BNB" "KAITO" "kPEPE" "kBONK" "kSHIB" "AVAX" "S" "POINTS" "ROAM" "AI16Z" "LAYER" "FARTCOIN" "NEAR" "PNUT" "ARB" "DOT" "APT" "OP" "PYUSD" "HUMA" "WAL" "DEEP" "CETUS" "SEND" "BLUE" "NS" "HAEDAL" "JPY" "TAO" "VIRTUAL" "TIA" "TRX" "FRAG" "PUMP" "WCT" "ES" "SEI" "CRV" "TON" "BPUSD" "HBAR" "XLM" "ZORA" "WLFI" "BPEUR" "SWTCH" "LINEA" "XPL" "BARD" "FLOCK" "AVNT" "PENDLE" "AERO" "ASTER" "GLXY" "0G" "2Z" "FWDI" "ZEUS" "APEX" "EDEN" "FF" "ORDER" "MNT" "ZEC" "PAXG" "MORPHO" "ATH" "KGEN" "XAUT" "FOGO" "SPX" "ETHFI" "APR" "PIPE" "MET" "MONP" "STABLE" "GUSDT" "BTCD121025" "BTCD121125" "BTCD121225" "SOLWP011526A160" "SOLD121125" "SOLD121225" "BTCW12122590000" "BTCW12122591000" "BTCW12122592000" "BTCW12122593000" "BTCW12122594000" "BTCW12122595000" "BTCW121225100000" "SOLW121225140000" "SOLW121225145000" "SOLW121225150000" "SOLW121225155000" "SOLW121225160000" "SOLW121225165000" "SOLW121225170000" "BTCM1225130000" "BTCM1225140000" "BTCM1225150000" "BTCM1225160000" "BTCM1225170000" "BTCM1225200000" "BTCM1225500000" "BTCM12251000000" "SOLDUD011226" "BTCDUD011326" "SOLDUD011326" "BTCDUD011426" "SOLDUD011426" "BTCDUD011526" "SOLDUD011526" "SOLWP011526U120" "SOLWP011526T120" "SOLWP011526T130" "SOLWP011526T140" "SOLWP011526T150" "DEMS28NEWSOM" "DEMS28AOC" "DEMS28BUTTIGIEG" "DEMS28SHAPIRO" "DEMS28KELLY" "DEMS28OSSOFF" "DEMS28KAMALA" "DEMS28MOORE" "DEMS28PRITZKER" "DEMS28BESHEAR" "DEMS28WHITMER" "DEMS28THEROCK" "DEMS28EMANUEL" "DEMS28MAMDANI" "LIT" "FOMC0126H0" "FOMC0126C25" "FOMC0126C50P" "FOMC0126H25P" "BTCWP011526U84" "BTCWP011526T84" "BTCWP011526T89" "BTCWP011526T94" "BTCWP011526T99" "BTCWP011526A104" "BTCDUD011026" "SOLDUD011026" "BTCDUD011126" "SOLDUD011126" "BTCDUD011226" "WHITEWHALE" "INX" "SKR" "XMR" "BTCWP011626T1" "BTCWP011626T2" "BTCWP011626T3" "BTCWP011626T4" "BTCWP011626T5" "BTCWP011626T6" "BTCWP011626T7" "BTCWP011626T8" "BTCWP011726T1" "BTCWP011726T2" "BTCWP011726T3" "BTCWP011726T4" "BTCWP011726T5" "BTCWP011726T6" "BTCWP011726T7" "BTCWP011726T8" "BTCWP011826T1" "BTCWP011826T2" "BTCWP011826T3" "BTCWP011826T4" "BTCWP011826T5" "BTCWP011826T6" "BTCWP011826T7" "BTCWP011826T8" "BTCWP011926T1" "BTCWP011926T2" "BTCWP011926T3" "BTCWP011926T4" "BTCWP011926T5" "BTCWP011926T6" "BTCWP011926T7" "BTCWP011926T8" "BTCWP012026T1" "BTCWP012026T2" "BTCWP012026T3" "BTCWP012026T4" "BTCWP012026T5" "BTCWP012026T6" "BTCWP012026T7" "BTCWP012026T8" "BTCWP012126T1" "BTCWP012126T2" "BTCWP012126T3" "BTCWP012126T4" "BTCWP012126T5" "BTCWP012126T6" "BTCWP012126T7" "BTCWP012126T8" "BTCWP012226T1" "BTCWP012226T2" "BTCWP012226T3" "BTCWP012226T4" "BTCWP012226T5" "BTCWP012226T6" "BTCWP012226T7" "BTCWP012226T8" "BTCWP012326T1" "BTCWP012326T2" "BTCWP012326T3" "BTCWP012326T4" "BTCWP012326T5" "BTCWP012326T6" "BTCWP012326T7" "BTCWP012326T8" "BTCWMS011626T1" "BTCWMS011626T2" "BTCWMS011626T3" "BTCWMS011626T4" "BTCWMS011626T5" "BTCWMS011626T6" "BTCWMS011626T7" "BTCWMS011626T8" "BTCWMS011726T1" "BTCWMS011726T2" "BTCWMS011726T3" "BTCWMS011726T4" "BTCWMS011726T5" "BTCWMS011726T6" "BTCWMS011726T7" "BTCWMS011726T8" "BTCWMS011826T1" "BTCWMS011826T2" "BTCWMS011826T3" "BTCWMS011826T4" "BTCWMS011826T5" "BTCWMS011826T6" "BTCWMS011826T7" "BTCWMS011826T8" "BTCWMS011926T1" "BTCWMS011926T2" "BTCWMS011926T3" "BTCWMS011926T4" "BTCWMS011926T5" "BTCWMS011926T6" "BTCWMS011926T7" "BTCWMS011926T8" "BTCWMS012026T1" "BTCWMS012026T2" "BTCWMS012026T3" "BTCWMS012026T4" "BTCWMS012026T5" "BTCWMS012026T6" "BTCWMS012026T7" "BTCWMS012026T8" "BTCWMS012126T1" "BTCWMS012126T2" "BTCWMS012126T3" "BTCWMS012126T4" "BTCWMS012126T5" "BTCWMS012126T6" "BTCWMS012126T7" "BTCWMS012126T8" "BTCWMS012226T1" "BTCWMS012226T2" "BTCWMS012226T3" "BTCWMS012226T4" "BTCWMS012226T5" "BTCWMS012226T6" "BTCWMS012226T7" "BTCWMS012226T8" "BTCWMS012326T1" "BTCWMS012326T2" "BTCWMS012326T3" "BTCWMS012326T4" "BTCWMS012326T5" "BTCWMS012326T6" "BTCWMS012326T7" "BTCWMS012326T8" "SOLWP011626T1" "SOLWP011626T2" "SOLWP011626T3" "SOLWP011626T4" "SOLWP011626T5" "SOLWP011726T1" "SOLWP011726T2" "SOLWP011726T3" "SOLWP011726T4" "SOLWP011726T5" "SOLWP011826T1" "SOLWP011826T2" "SOLWP011826T3" "SOLWP011826T4" "SOLWP011826T5" "SOLWP011926T1" "SOLWP011926T2" "SOLWP011926T3" "SOLWP011926T4" "SOLWP011926T5" "SOLWP012026T1" "SOLWP012026T2" "SOLWP012026T3" "SOLWP012026T4" "SOLWP012026T5" "SOLWP012126T1" "SOLWP012126T2" "SOLWP012126T3" "SOLWP012126T4" "SOLWP012126T5" "SOLWP012226T1" "SOLWP012226T2" "SOLWP012226T3" "SOLWP012226T4" "SOLWP012226T5" "SOLWP012326T1" "SOLWP012326T2" "SOLWP012326T3" "SOLWP012326T4" "SOLWP012326T5" "SOLWMS011626T1" "SOLWMS011626T2" "SOLWMS011626T3" "SOLWMS011626T4" "SOLWMS011626T5" "SOLWMS011726T1" "SOLWMS011726T2" "SOLWMS011726T3" "SOLWMS011726T4" "SOLWMS011726T5" "SOLWMS011826T1" "SOLWMS011826T2" "SOLWMS011826T3" "SOLWMS011826T4" "SOLWMS011826T5" "SOLWMS011926T1" "SOLWMS011926T2" "SOLWMS011926T3" "SOLWMS011926T4" "SOLWMS011926T5" "SOLWMS012026T1" "SOLWMS012026T2" "SOLWMS012026T3" "SOLWMS012026T4" "SOLWMS012026T5" "SOLWMS012126T1" "SOLWMS012126T2" "SOLWMS012126T3" "SOLWMS012126T4" "SOLWMS012126T5" "SOLWMS012226T1" "SOLWMS012226T2" "SOLWMS012226T3" "SOLWMS012226T4" "SOLWMS012226T5" "SOLWMS012326T1" "SOLWMS012326T2" "SOLWMS012326T3" "SOLWMS012326T4" "SOLWMS012326T5" "ETHWP011626T1" "ETHWP011626T2" "ETHWP011626T3" "ETHWP011626T4" "ETHWP011626T5" "ETHWP011626T6" "ETHWP011626T7" "ETHWP011626T8" "ETHWP011726T1" "ETHWP011726T2" "ETHWP011726T3" "ETHWP011726T4" "ETHWP011726T5" "ETHWP011726T6" "ETHWP011726T7" "ETHWP011726T8" "ETHWP011826T1" "ETHWP011826T2" "ETHWP011826T3" "ETHWP011826T4" "ETHWP011826T5" "ETHWP011826T6" "ETHWP011826T7" "ETHWP011826T8" "ETHWP011926T1" "ETHWP011926T2" "ETHWP011926T3" "ETHWP011926T4" "ETHWP011926T5" "ETHWP011926T6" "ETHWP011926T7" "ETHWP011926T8" "ETHWP012026T1" "ETHWP012026T2" "ETHWP012026T3" "ETHWP012026T4" "ETHWP012026T5" "ETHWP012026T6" "ETHWP012026T7" "ETHWP012026T8" "ETHWP012126T1" "ETHWP012126T2" "ETHWP012126T3" "ETHWP012126T4" "ETHWP012126T5" "ETHWP012126T6" "ETHWP012126T7" "ETHWP012126T8" "ETHWP012226T1" "ETHWP012226T2" "ETHWP012226T3" "ETHWP012226T4" "ETHWP012226T5" "ETHWP012226T6" "ETHWP012226T7" "ETHWP012226T8" "ETHWP012326T1" "ETHWP012326T2" "ETHWP012326T3" "ETHWP012326T4" "ETHWP012326T5" "ETHWP012326T6" "ETHWP012326T7" "ETHWP012326T8" "ETHWMS011626T1" "ETHWMS011626T2" "ETHWMS011626T3" "ETHWMS011626T4" "ETHWMS011626T5" "ETHWMS011626T6" "ETHWMS011626T7" "ETHWMS011626T8" "ETHWMS011726T1" "ETHWMS011726T2" "ETHWMS011726T3" "ETHWMS011726T4" "ETHWMS011726T5" "ETHWMS011726T6" "ETHWMS011726T7" "ETHWMS011726T8" "ETHWMS011826T1" "ETHWMS011826T2" "ETHWMS011826T3" "ETHWMS011826T4" "ETHWMS011826T5" "ETHWMS011826T6" "ETHWMS011826T7" "ETHWMS011826T8" "ETHWMS011926T1" "ETHWMS011926T2" "ETHWMS011926T3" "ETHWMS011926T4" "ETHWMS011926T5" "ETHWMS011926T6" "ETHWMS011926T7" "ETHWMS011926T8" "ETHWMS012026T1" "ETHWMS012026T2" "ETHWMS012026T3" "ETHWMS012026T4" "ETHWMS012026T5" "ETHWMS012026T6" "ETHWMS012026T7" "ETHWMS012026T8" "ETHWMS012126T1" "ETHWMS012126T2" "ETHWMS012126T3" "ETHWMS012126T4" "ETHWMS012126T5" "ETHWMS012126T6" "ETHWMS012126T7" "ETHWMS012126T8" "ETHWMS012226T1" "ETHWMS012226T2" "ETHWMS012226T3" "ETHWMS012226T4" "ETHWMS012226T5" "ETHWMS012226T6" "ETHWMS012226T7" "ETHWMS012226T8" "ETHWMS012326T1" "ETHWMS012326T2" "ETHWMS012326T3" "ETHWMS012326T4" "ETHWMS012326T5" "ETHWMS012326T6" "ETHWMS012326T7" "ETHWMS012326T8" "BTCDUD011626" "BTCDUD011726" "BTCDUD011826" "BTCDUD011926" "BTCDUD012026" "BTCDUD012126" "BTCDUD012226" "BTCDUD012326" "SOLDUD011626" "SOLDUD011726" "SOLDUD011826" "SOLDUD011926" "SOLDUD012026" "SOLDUD012126" "SOLDUD012226" "SOLDUD012326" "ETHDUD011626" "ETHDUD011726" "ETHDUD011826" "ETHDUD011926" "ETHDUD012026" "ETHDUD012126" "ETHDUD012226" "ETHDUD012326" "FDVEDGEX1B" "FDVEDGEX2B" "FDVEDGEX3B" "FDVEDGEX4B" "FDVEDGEX5B" "FDVEXTD300M" "FDVEXTD500M" "FDVEXTD800M" "FDVEXTD1B" "FDVEXTD2B" "FDVEXTD3B" "FDVPARA300M" "FDVPARA500M" "FDVPARA750M" "FDVPARA1N5B" "FDVPARA3B" "FDVPARA5B" "FDVINX200M" "FDVINX300M" "FDVINX400M" "FDVINX600M" "FDVINX800M" "FDVINX1B" "FDVVAR500M" "FDVVAR800M" "FDVVAR1B" "FDVVAR2B" "FDVVAR3B" "FDVVAR4B" "FDVVAR5B" "NBA26HA012026H" "NBA26HA012026A" "NBA26HA012026HN2" "NBA26HA012026AP2" "NBA26HA012026TTLO222" "NBA26HA012026TTLU222" "NBA26HA012026P1O30" "NBA26HA012026P1U30" "NHL26HA012026H" "NHL26HA012026A" "NHL26HA012026HN2" "NHL26HA012026AP2" "NHL26HA012026TTLO4" "NHL26HA012026TTLU4" "NHL26HA012026P1O2" "NHL26HA012026P1U2" "CC" "DASH" "AXS" "BTCWP012626T1" "BTCWP012626T2" "BTCWP012626T3" "BTCWP012626T4" "BTCWP012626T5" "BTCWP012626T6" "BTCWP012626T7" "BTCWP012626T8" "BTCWP012826T1" "BTCWP012826T2" "BTCWP012826T3" "BTCWP012826T4" "BTCWP012826T5" "BTCWP012826T6" "BTCWP012826T7" "BTCWP012826T8" "BTCWP013026T1" "BTCWP013026T2" "BTCWP013026T3" "BTCWP013026T4" "BTCWP013026T5" "BTCWP013026T6" "BTCWP013026T7" "BTCWP013026T8" "BTCWP020226T1" "BTCWP020226T2" "BTCWP020226T3" "BTCWP020226T4" "BTCWP020226T5" "BTCWP020226T6" "BTCWP020226T7" "BTCWP020226T8" "BTCWP020426T1" "BTCWP020426T2" "BTCWP020426T3" "BTCWP020426T4" "BTCWP020426T5" "BTCWP020426T6" "BTCWP020426T7" "BTCWP020426T8" "BTCWP020626T1" "BTCWP020626T2" "BTCWP020626T3" "BTCWP020626T4" "BTCWP020626T5" "BTCWP020626T6" "BTCWP020626T7" "BTCWP020626T8" "SOLWP012626T1" "SOLWP012626T2" "SOLWP012626T3" "SOLWP012626T4" "SOLWP012626T5" "SOLWP012626T6" "SOLWP012826T1" "SOLWP012826T2" "SOLWP012826T3" "SOLWP012826T4" "SOLWP012826T5" "SOLWP012826T6" "SOLWP013026T1" "SOLWP013026T2" "SOLWP013026T3" "SOLWP013026T4" "SOLWP013026T5" "SOLWP013026T6" "SOLWP020226T1" "SOLWP020226T2" "SOLWP020226T3" "SOLWP020226T4" "SOLWP020226T5" "SOLWP020226T6" "SOLWP020426T1" "SOLWP020426T2" "SOLWP020426T3" "SOLWP020426T4" "SOLWP020426T5" "SOLWP020426T6" "SOLWP020626T1" "SOLWP020626T2" "SOLWP020626T3" "SOLWP020626T4" "SOLWP020626T5" "SOLWP020626T6" "ETHWP012626T1" "ETHWP012626T2" "ETHWP012626T3" "ETHWP012626T4" "ETHWP012626T5" "ETHWP012626T6" "ETHWP012626T7" "ETHWP012626T8" "ETHWP012826T1" "ETHWP012826T2" "ETHWP012826T3" "ETHWP012826T4" "ETHWP012826T5" "ETHWP012826T6" "ETHWP012826T7" "ETHWP012826T8" "ETHWP013026T1" "ETHWP013026T2" "ETHWP013026T3" "ETHWP013026T4" "ETHWP013026T5" "ETHWP013026T6" "ETHWP013026T7" "ETHWP013026T8" "ETHWP020226T1" "ETHWP020226T2" "ETHWP020226T3" "ETHWP020226T4" "ETHWP020226T5" "ETHWP020226T6" "ETHWP020226T7" "ETHWP020226T8" "ETHWP020426T1" "ETHWP020426T2" "ETHWP020426T3" "ETHWP020426T4" "ETHWP020426T5" "ETHWP020426T6" "ETHWP020426T7" "ETHWP020426T8" "ETHWP020626T1" "ETHWP020626T2" "ETHWP020626T3" "ETHWP020626T4" "ETHWP020626T5" "ETHWP020626T6" "ETHWP020626T7" "ETHWP020626T8" "BTCDUD012426" "BTCDUD012526" "BTCDUD012626" "BTCDUD012726" "BTCDUD012826" "BTCDUD012926" "BTCDUD013026" "BTCDUD013126" "BTCDUD020126" "BTCDUD020226" "BTCDUD020326" "BTCDUD020426" "BTCDUD020526" "BTCDUD020626" "SOLDUD012426" "SOLDUD012526" "SOLDUD012626" "SOLDUD012726" "SOLDUD012826" "SOLDUD012926" "SOLDUD013026" "SOLDUD013126" "SOLDUD020126" "SOLDUD020226" "SOLDUD020326" "SOLDUD020426" "SOLDUD020526" "SOLDUD020626" "ETHDUD012426" "ETHDUD012526" "ETHDUD012626" "ETHDUD012726" "ETHDUD012826" "ETHDUD012926" "ETHDUD013026" "ETHDUD013126" "ETHDUD020126" "ETHDUD020226" "ETHDUD020326" "ETHDUD020426" "ETHDUD020526" "ETHDUD020626" "XRPUD012426" "XRPUD012526" "XRPUD012626" "XRPUD012726" "XRPUD012826" "XRPUD012926" "XRPUD013026" "XRPUD013126" "XRPUD020126" "XRPUD020226" "XRPUD020326" "XRPUD020426" "XRPUD020526" "XRPUD020626" "BNBUD012426" "BNBUD012526" "BNBUD012626" "BNBUD012726" "BNBUD012826" "BNBUD012926" "BNBUD013026" "BNBUD013126" "BNBUD020126" "BNBUD020226" "BNBUD020326" "BNBUD020426" "BNBUD020526" "BNBUD020626" "ZAMA" "MEGA" "RNBW" "BLT" The asset symbol to convert dust for. If omitted, all dust balances will be converted.  
---|---  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

post/api/v1/account/convertDust

https://api.backpack.exchange/api/v1/account/convertDust

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "symbol": "BTC"


}`

###  Response samples

  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "code": "ACCOUNT_DEACTIVATED",

  * "message": "string"


}`

## [](#tag/Capital/operation/get_balances)Get balances.

Retrieves account balances and the state of the balances (locked or available).

Locked assets are those that are currently in an open order.

**Instruction:** `balanceQuery`

##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/capital

https://api.backpack.exchange/api/v1/capital

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`{

  * "property1": {
    * "available": "string",

    * "locked": "string",

    * "staked": "string"

},

  * "property2": {
    * "available": "string",

    * "locked": "string",

    * "staked": "string"

}


}`

## [](#tag/Capital/operation/get_collateral)Get collateral.

Retrieves collateral information for an account.

**Instruction:** `collateralQuery`

##### query Parameters

subaccountId| integer <uint16>  
---|---  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal server error.

get/api/v1/capital/collateral

https://api.backpack.exchange/api/v1/capital/collateral

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`{

  * "assetsValue": "string",

  * "borrowLiability": "string",

  * "collateral": [
    * {
      * "symbol": "string",

      * "assetMarkPrice": "string",

      * "totalQuantity": "string",

      * "balanceNotional": "string",

      * "collateralWeight": "string",

      * "collateralValue": "string",

      * "openOrderQuantity": "string",

      * "lendQuantity": "string",

      * "availableQuantity": "string"

}

],

  * "imf": "string",

  * "unsettledEquity": "string",

  * "liabilitiesValue": "string",

  * "marginFraction": "string",

  * "mmf": "string",

  * "netEquity": "string",

  * "netEquityAvailable": "string",

  * "netEquityLocked": "string",

  * "netExposureFutures": "string",

  * "pnlUnrealized": "string"


}`

## [](#tag/Capital/operation/get_deposits)Get deposits.

Retrieves deposit history.

**Instruction:** `depositQueryAll`

##### query Parameters

from| integer <int64> Filter to minimum time (milliseconds).  
---|---  
to| integer <int64> Filter to maximum time (milliseconds).  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
excludePlatform| boolean Exclude platform deposits originating from the exchange.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/capital/deposits

https://api.backpack.exchange/wapi/v1/capital/deposits

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "id": 0,

    * "toAddress": "string",

    * "fromAddress": "string",

    * "source": "administrator",

    * "status": "cancelled",

    * "transactionHash": "string",

    * "symbol": "BTC",

    * "quantity": "string",

    * "createdAt": "string",

    * "fiatAmount": 0.1,

    * "fiatCurrency": "AED",

    * "institutionBic": "string",

    * "platformMemo": "string"

}


]`

## [](#tag/Capital/operation/get_deposit_address)Get deposit address.

Retrieves the user specific deposit address if the user were to deposit on the specified blockchain.

**Instruction:** `depositAddressQuery`

##### query Parameters

blockchainrequired| string (Blockchain)  Enum: "0G" "Aptos" "Arbitrum" "Avalanche" "Base" "Berachain" "Bitcoin" "BitcoinCash" "Bsc" "Cardano" "Dogecoin" "Eclipse" "EqualsMoney" "Ethereum" "Fogo" "HyperEVM" "Hyperliquid" "Linea" "Litecoin" "Monad" "Near" "Optimism" "Plasma" "Polygon" "Sei" "Sui" "Solana" "Stable" "Story" "Tron" "XRP" "Zcash" Blockchain symbol to get a deposit address for.  
---|---  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**409 **

Conflict

**500 **

Internal server error.

get/wapi/v1/capital/deposit/address

https://api.backpack.exchange/wapi/v1/capital/deposit/address

###  Response samples

  * 200
  * 400
  * 401
  * 409
  * 500



Content type

application/json; charset=utf-8

Copy

`{

  * "address": "string"


}`

## [](#tag/Capital/operation/get_withdrawals)Get withdrawals.

Retrieves withdrawal history.

**Instruction:** `withdrawalQueryAll`

##### query Parameters

from| integer <int64> Filter to minimum time (milliseconds).  
---|---  
to| integer <int64> Filter to maximum time (milliseconds).  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal Server Error.

get/wapi/v1/capital/withdrawals

https://api.backpack.exchange/wapi/v1/capital/withdrawals

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "id": 0,

    * "blockchain": "0G",

    * "clientId": "string",

    * "identifier": "string",

    * "quantity": "string",

    * "fee": "string",

    * "fiatFee": "string",

    * "fiatState": "initialized",

    * "fiatSymbol": "AED",

    * "providerId": "string",

    * "symbol": "BTC",

    * "status": "confirmed",

    * "subaccountId": 0,

    * "toAddress": "string",

    * "transactionHash": "string",

    * "createdAt": "string",

    * "isInternal": true,

    * "bankName": "string",

    * "bankIdentifier": "string",

    * "accountIdentifier": "string",

    * "triggerAt": "string"

}


]`

## [](#tag/Capital/operation/request_withdrawal)Request withdrawal.

Requests a withdrawal from the exchange.

The `twoFactorToken` field is required if the withdrawal address is not an address that is configured in the address book to not require 2FA.

To configure a 2FA exempt address, please [add an address](https://backpack.exchange/settings/address-book) to the address book and toggle the `Two Factor Authentication Required` option.

**Instruction:** `withdraw`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
X-SIGNATURErequired| string Signature of the request  
  
##### Request Body schema: application/json; charset=utf-8

required

addressrequired| string Address to withdraw to.  
---|---  
blockchainrequired| string Enum: "0G" "Aptos" "Arbitrum" "Avalanche" "Base" "Berachain" "Bitcoin" "BitcoinCash" "Bsc" "Cardano" "Dogecoin" "Eclipse" "EqualsMoney" "Ethereum" "Fogo" "HyperEVM" "Hyperliquid" "Linea" "Litecoin" "Monad" "Near" "Optimism" "Plasma" "Polygon" "Sei" "Sui" "Solana" "Stable" "Story" "Tron" "XRP" "Zcash" Blockchain to withdraw on.  
clientId| string <= 255 characters Custom client id.  
quantityrequired| string <decimal> Quantity to withdraw.  
symbolrequired| string Enum: "BTC" "ETH" "SOL" "USDC" "USDT" "PYTH" "JTO" "BONK" "HNT" "MOBILE" "WIF" "JUP" "RENDER" "WEN" "W" "TNSR" "PRCL" "SHARK" "KMNO" "MEW" "BOME" "RAY" "HONEY" "SHFL" "BODEN" "IO" "DRIFT" "PEPE" "SHIB" "LINK" "UNI" "ONDO" "FTM" "MATIC" "STRK" "BLUR" "WLD" "GALA" "NYAN" "HLG" "MON" "ZKJ" "MANEKI" "HABIBI" "UNA" "ZRO" "ZEX" "AAVE" "LDO" "MOTHER" "CLOUD" "MAX" "POL" "TRUMPWIN" "HARRISWIN" "MOODENG" "DBR" "GOAT" "ACT" "DOGE" "BCH" "LTC" "APE" "ENA" "ME" "EIGEN" "CHILLGUY" "PENGU" "EUR" "SONIC" "J" "TRUMP" "MELANIA" "ANIME" "XRP" "SUI" "VINE" "ADA" "MOVE" "BERA" "IP" "HYPE" "BNB" "KAITO" "kPEPE" "kBONK" "kSHIB" "AVAX" "S" "POINTS" "ROAM" "AI16Z" "LAYER" "FARTCOIN" "NEAR" "PNUT" "ARB" "DOT" "APT" "OP" "PYUSD" "HUMA" "WAL" "DEEP" "CETUS" "SEND" "BLUE" "NS" "HAEDAL" "JPY" "TAO" "VIRTUAL" "TIA" "TRX" "FRAG" "PUMP" "WCT" "ES" "SEI" "CRV" "TON" "BPUSD" "HBAR" "XLM" "ZORA" "WLFI" "BPEUR" "SWTCH" "LINEA" "XPL" "BARD" "FLOCK" "AVNT" "PENDLE" "AERO" "ASTER" "GLXY" "0G" "2Z" "FWDI" "ZEUS" "APEX" "EDEN" "FF" "ORDER" "MNT" "ZEC" "PAXG" "MORPHO" "ATH" "KGEN" "XAUT" "FOGO" "SPX" "ETHFI" "APR" "PIPE" "MET" "MONP" "STABLE" "GUSDT" "BTCD121025" "BTCD121125" "BTCD121225" "SOLWP011526A160" "SOLD121125" "SOLD121225" "BTCW12122590000" "BTCW12122591000" "BTCW12122592000" "BTCW12122593000" "BTCW12122594000" "BTCW12122595000" "BTCW121225100000" "SOLW121225140000" "SOLW121225145000" "SOLW121225150000" "SOLW121225155000" "SOLW121225160000" "SOLW121225165000" "SOLW121225170000" "BTCM1225130000" "BTCM1225140000" "BTCM1225150000" "BTCM1225160000" "BTCM1225170000" "BTCM1225200000" "BTCM1225500000" "BTCM12251000000" "SOLDUD011226" "BTCDUD011326" "SOLDUD011326" "BTCDUD011426" "SOLDUD011426" "BTCDUD011526" "SOLDUD011526" "SOLWP011526U120" "SOLWP011526T120" "SOLWP011526T130" "SOLWP011526T140" "SOLWP011526T150" "DEMS28NEWSOM" "DEMS28AOC" "DEMS28BUTTIGIEG" "DEMS28SHAPIRO" "DEMS28KELLY" "DEMS28OSSOFF" "DEMS28KAMALA" "DEMS28MOORE" "DEMS28PRITZKER" "DEMS28BESHEAR" "DEMS28WHITMER" "DEMS28THEROCK" "DEMS28EMANUEL" "DEMS28MAMDANI" "LIT" "FOMC0126H0" "FOMC0126C25" "FOMC0126C50P" "FOMC0126H25P" "BTCWP011526U84" "BTCWP011526T84" "BTCWP011526T89" "BTCWP011526T94" "BTCWP011526T99" "BTCWP011526A104" "BTCDUD011026" "SOLDUD011026" "BTCDUD011126" "SOLDUD011126" "BTCDUD011226" "WHITEWHALE" "INX" "SKR" "XMR" "BTCWP011626T1" "BTCWP011626T2" "BTCWP011626T3" "BTCWP011626T4" "BTCWP011626T5" "BTCWP011626T6" "BTCWP011626T7" "BTCWP011626T8" "BTCWP011726T1" "BTCWP011726T2" "BTCWP011726T3" "BTCWP011726T4" "BTCWP011726T5" "BTCWP011726T6" "BTCWP011726T7" "BTCWP011726T8" "BTCWP011826T1" "BTCWP011826T2" "BTCWP011826T3" "BTCWP011826T4" "BTCWP011826T5" "BTCWP011826T6" "BTCWP011826T7" "BTCWP011826T8" "BTCWP011926T1" "BTCWP011926T2" "BTCWP011926T3" "BTCWP011926T4" "BTCWP011926T5" "BTCWP011926T6" "BTCWP011926T7" "BTCWP011926T8" "BTCWP012026T1" "BTCWP012026T2" "BTCWP012026T3" "BTCWP012026T4" "BTCWP012026T5" "BTCWP012026T6" "BTCWP012026T7" "BTCWP012026T8" "BTCWP012126T1" "BTCWP012126T2" "BTCWP012126T3" "BTCWP012126T4" "BTCWP012126T5" "BTCWP012126T6" "BTCWP012126T7" "BTCWP012126T8" "BTCWP012226T1" "BTCWP012226T2" "BTCWP012226T3" "BTCWP012226T4" "BTCWP012226T5" "BTCWP012226T6" "BTCWP012226T7" "BTCWP012226T8" "BTCWP012326T1" "BTCWP012326T2" "BTCWP012326T3" "BTCWP012326T4" "BTCWP012326T5" "BTCWP012326T6" "BTCWP012326T7" "BTCWP012326T8" "BTCWMS011626T1" "BTCWMS011626T2" "BTCWMS011626T3" "BTCWMS011626T4" "BTCWMS011626T5" "BTCWMS011626T6" "BTCWMS011626T7" "BTCWMS011626T8" "BTCWMS011726T1" "BTCWMS011726T2" "BTCWMS011726T3" "BTCWMS011726T4" "BTCWMS011726T5" "BTCWMS011726T6" "BTCWMS011726T7" "BTCWMS011726T8" "BTCWMS011826T1" "BTCWMS011826T2" "BTCWMS011826T3" "BTCWMS011826T4" "BTCWMS011826T5" "BTCWMS011826T6" "BTCWMS011826T7" "BTCWMS011826T8" "BTCWMS011926T1" "BTCWMS011926T2" "BTCWMS011926T3" "BTCWMS011926T4" "BTCWMS011926T5" "BTCWMS011926T6" "BTCWMS011926T7" "BTCWMS011926T8" "BTCWMS012026T1" "BTCWMS012026T2" "BTCWMS012026T3" "BTCWMS012026T4" "BTCWMS012026T5" "BTCWMS012026T6" "BTCWMS012026T7" "BTCWMS012026T8" "BTCWMS012126T1" "BTCWMS012126T2" "BTCWMS012126T3" "BTCWMS012126T4" "BTCWMS012126T5" "BTCWMS012126T6" "BTCWMS012126T7" "BTCWMS012126T8" "BTCWMS012226T1" "BTCWMS012226T2" "BTCWMS012226T3" "BTCWMS012226T4" "BTCWMS012226T5" "BTCWMS012226T6" "BTCWMS012226T7" "BTCWMS012226T8" "BTCWMS012326T1" "BTCWMS012326T2" "BTCWMS012326T3" "BTCWMS012326T4" "BTCWMS012326T5" "BTCWMS012326T6" "BTCWMS012326T7" "BTCWMS012326T8" "SOLWP011626T1" "SOLWP011626T2" "SOLWP011626T3" "SOLWP011626T4" "SOLWP011626T5" "SOLWP011726T1" "SOLWP011726T2" "SOLWP011726T3" "SOLWP011726T4" "SOLWP011726T5" "SOLWP011826T1" "SOLWP011826T2" "SOLWP011826T3" "SOLWP011826T4" "SOLWP011826T5" "SOLWP011926T1" "SOLWP011926T2" "SOLWP011926T3" "SOLWP011926T4" "SOLWP011926T5" "SOLWP012026T1" "SOLWP012026T2" "SOLWP012026T3" "SOLWP012026T4" "SOLWP012026T5" "SOLWP012126T1" "SOLWP012126T2" "SOLWP012126T3" "SOLWP012126T4" "SOLWP012126T5" "SOLWP012226T1" "SOLWP012226T2" "SOLWP012226T3" "SOLWP012226T4" "SOLWP012226T5" "SOLWP012326T1" "SOLWP012326T2" "SOLWP012326T3" "SOLWP012326T4" "SOLWP012326T5" "SOLWMS011626T1" "SOLWMS011626T2" "SOLWMS011626T3" "SOLWMS011626T4" "SOLWMS011626T5" "SOLWMS011726T1" "SOLWMS011726T2" "SOLWMS011726T3" "SOLWMS011726T4" "SOLWMS011726T5" "SOLWMS011826T1" "SOLWMS011826T2" "SOLWMS011826T3" "SOLWMS011826T4" "SOLWMS011826T5" "SOLWMS011926T1" "SOLWMS011926T2" "SOLWMS011926T3" "SOLWMS011926T4" "SOLWMS011926T5" "SOLWMS012026T1" "SOLWMS012026T2" "SOLWMS012026T3" "SOLWMS012026T4" "SOLWMS012026T5" "SOLWMS012126T1" "SOLWMS012126T2" "SOLWMS012126T3" "SOLWMS012126T4" "SOLWMS012126T5" "SOLWMS012226T1" "SOLWMS012226T2" "SOLWMS012226T3" "SOLWMS012226T4" "SOLWMS012226T5" "SOLWMS012326T1" "SOLWMS012326T2" "SOLWMS012326T3" "SOLWMS012326T4" "SOLWMS012326T5" "ETHWP011626T1" "ETHWP011626T2" "ETHWP011626T3" "ETHWP011626T4" "ETHWP011626T5" "ETHWP011626T6" "ETHWP011626T7" "ETHWP011626T8" "ETHWP011726T1" "ETHWP011726T2" "ETHWP011726T3" "ETHWP011726T4" "ETHWP011726T5" "ETHWP011726T6" "ETHWP011726T7" "ETHWP011726T8" "ETHWP011826T1" "ETHWP011826T2" "ETHWP011826T3" "ETHWP011826T4" "ETHWP011826T5" "ETHWP011826T6" "ETHWP011826T7" "ETHWP011826T8" "ETHWP011926T1" "ETHWP011926T2" "ETHWP011926T3" "ETHWP011926T4" "ETHWP011926T5" "ETHWP011926T6" "ETHWP011926T7" "ETHWP011926T8" "ETHWP012026T1" "ETHWP012026T2" "ETHWP012026T3" "ETHWP012026T4" "ETHWP012026T5" "ETHWP012026T6" "ETHWP012026T7" "ETHWP012026T8" "ETHWP012126T1" "ETHWP012126T2" "ETHWP012126T3" "ETHWP012126T4" "ETHWP012126T5" "ETHWP012126T6" "ETHWP012126T7" "ETHWP012126T8" "ETHWP012226T1" "ETHWP012226T2" "ETHWP012226T3" "ETHWP012226T4" "ETHWP012226T5" "ETHWP012226T6" "ETHWP012226T7" "ETHWP012226T8" "ETHWP012326T1" "ETHWP012326T2" "ETHWP012326T3" "ETHWP012326T4" "ETHWP012326T5" "ETHWP012326T6" "ETHWP012326T7" "ETHWP012326T8" "ETHWMS011626T1" "ETHWMS011626T2" "ETHWMS011626T3" "ETHWMS011626T4" "ETHWMS011626T5" "ETHWMS011626T6" "ETHWMS011626T7" "ETHWMS011626T8" "ETHWMS011726T1" "ETHWMS011726T2" "ETHWMS011726T3" "ETHWMS011726T4" "ETHWMS011726T5" "ETHWMS011726T6" "ETHWMS011726T7" "ETHWMS011726T8" "ETHWMS011826T1" "ETHWMS011826T2" "ETHWMS011826T3" "ETHWMS011826T4" "ETHWMS011826T5" "ETHWMS011826T6" "ETHWMS011826T7" "ETHWMS011826T8" "ETHWMS011926T1" "ETHWMS011926T2" "ETHWMS011926T3" "ETHWMS011926T4" "ETHWMS011926T5" "ETHWMS011926T6" "ETHWMS011926T7" "ETHWMS011926T8" "ETHWMS012026T1" "ETHWMS012026T2" "ETHWMS012026T3" "ETHWMS012026T4" "ETHWMS012026T5" "ETHWMS012026T6" "ETHWMS012026T7" "ETHWMS012026T8" "ETHWMS012126T1" "ETHWMS012126T2" "ETHWMS012126T3" "ETHWMS012126T4" "ETHWMS012126T5" "ETHWMS012126T6" "ETHWMS012126T7" "ETHWMS012126T8" "ETHWMS012226T1" "ETHWMS012226T2" "ETHWMS012226T3" "ETHWMS012226T4" "ETHWMS012226T5" "ETHWMS012226T6" "ETHWMS012226T7" "ETHWMS012226T8" "ETHWMS012326T1" "ETHWMS012326T2" "ETHWMS012326T3" "ETHWMS012326T4" "ETHWMS012326T5" "ETHWMS012326T6" "ETHWMS012326T7" "ETHWMS012326T8" "BTCDUD011626" "BTCDUD011726" "BTCDUD011826" "BTCDUD011926" "BTCDUD012026" "BTCDUD012126" "BTCDUD012226" "BTCDUD012326" "SOLDUD011626" "SOLDUD011726" "SOLDUD011826" "SOLDUD011926" "SOLDUD012026" "SOLDUD012126" "SOLDUD012226" "SOLDUD012326" "ETHDUD011626" "ETHDUD011726" "ETHDUD011826" "ETHDUD011926" "ETHDUD012026" "ETHDUD012126" "ETHDUD012226" "ETHDUD012326" "FDVEDGEX1B" "FDVEDGEX2B" "FDVEDGEX3B" "FDVEDGEX4B" "FDVEDGEX5B" "FDVEXTD300M" "FDVEXTD500M" "FDVEXTD800M" "FDVEXTD1B" "FDVEXTD2B" "FDVEXTD3B" "FDVPARA300M" "FDVPARA500M" "FDVPARA750M" "FDVPARA1N5B" "FDVPARA3B" "FDVPARA5B" "FDVINX200M" "FDVINX300M" "FDVINX400M" "FDVINX600M" "FDVINX800M" "FDVINX1B" "FDVVAR500M" "FDVVAR800M" "FDVVAR1B" "FDVVAR2B" "FDVVAR3B" "FDVVAR4B" "FDVVAR5B" "NBA26HA012026H" "NBA26HA012026A" "NBA26HA012026HN2" "NBA26HA012026AP2" "NBA26HA012026TTLO222" "NBA26HA012026TTLU222" "NBA26HA012026P1O30" "NBA26HA012026P1U30" "NHL26HA012026H" "NHL26HA012026A" "NHL26HA012026HN2" "NHL26HA012026AP2" "NHL26HA012026TTLO4" "NHL26HA012026TTLU4" "NHL26HA012026P1O2" "NHL26HA012026P1U2" "CC" "DASH" "AXS" "BTCWP012626T1" "BTCWP012626T2" "BTCWP012626T3" "BTCWP012626T4" "BTCWP012626T5" "BTCWP012626T6" "BTCWP012626T7" "BTCWP012626T8" "BTCWP012826T1" "BTCWP012826T2" "BTCWP012826T3" "BTCWP012826T4" "BTCWP012826T5" "BTCWP012826T6" "BTCWP012826T7" "BTCWP012826T8" "BTCWP013026T1" "BTCWP013026T2" "BTCWP013026T3" "BTCWP013026T4" "BTCWP013026T5" "BTCWP013026T6" "BTCWP013026T7" "BTCWP013026T8" "BTCWP020226T1" "BTCWP020226T2" "BTCWP020226T3" "BTCWP020226T4" "BTCWP020226T5" "BTCWP020226T6" "BTCWP020226T7" "BTCWP020226T8" "BTCWP020426T1" "BTCWP020426T2" "BTCWP020426T3" "BTCWP020426T4" "BTCWP020426T5" "BTCWP020426T6" "BTCWP020426T7" "BTCWP020426T8" "BTCWP020626T1" "BTCWP020626T2" "BTCWP020626T3" "BTCWP020626T4" "BTCWP020626T5" "BTCWP020626T6" "BTCWP020626T7" "BTCWP020626T8" "SOLWP012626T1" "SOLWP012626T2" "SOLWP012626T3" "SOLWP012626T4" "SOLWP012626T5" "SOLWP012626T6" "SOLWP012826T1" "SOLWP012826T2" "SOLWP012826T3" "SOLWP012826T4" "SOLWP012826T5" "SOLWP012826T6" "SOLWP013026T1" "SOLWP013026T2" "SOLWP013026T3" "SOLWP013026T4" "SOLWP013026T5" "SOLWP013026T6" "SOLWP020226T1" "SOLWP020226T2" "SOLWP020226T3" "SOLWP020226T4" "SOLWP020226T5" "SOLWP020226T6" "SOLWP020426T1" "SOLWP020426T2" "SOLWP020426T3" "SOLWP020426T4" "SOLWP020426T5" "SOLWP020426T6" "SOLWP020626T1" "SOLWP020626T2" "SOLWP020626T3" "SOLWP020626T4" "SOLWP020626T5" "SOLWP020626T6" "ETHWP012626T1" "ETHWP012626T2" "ETHWP012626T3" "ETHWP012626T4" "ETHWP012626T5" "ETHWP012626T6" "ETHWP012626T7" "ETHWP012626T8" "ETHWP012826T1" "ETHWP012826T2" "ETHWP012826T3" "ETHWP012826T4" "ETHWP012826T5" "ETHWP012826T6" "ETHWP012826T7" "ETHWP012826T8" "ETHWP013026T1" "ETHWP013026T2" "ETHWP013026T3" "ETHWP013026T4" "ETHWP013026T5" "ETHWP013026T6" "ETHWP013026T7" "ETHWP013026T8" "ETHWP020226T1" "ETHWP020226T2" "ETHWP020226T3" "ETHWP020226T4" "ETHWP020226T5" "ETHWP020226T6" "ETHWP020226T7" "ETHWP020226T8" "ETHWP020426T1" "ETHWP020426T2" "ETHWP020426T3" "ETHWP020426T4" "ETHWP020426T5" "ETHWP020426T6" "ETHWP020426T7" "ETHWP020426T8" "ETHWP020626T1" "ETHWP020626T2" "ETHWP020626T3" "ETHWP020626T4" "ETHWP020626T5" "ETHWP020626T6" "ETHWP020626T7" "ETHWP020626T8" "BTCDUD012426" "BTCDUD012526" "BTCDUD012626" "BTCDUD012726" "BTCDUD012826" "BTCDUD012926" "BTCDUD013026" "BTCDUD013126" "BTCDUD020126" "BTCDUD020226" "BTCDUD020326" "BTCDUD020426" "BTCDUD020526" "BTCDUD020626" "SOLDUD012426" "SOLDUD012526" "SOLDUD012626" "SOLDUD012726" "SOLDUD012826" "SOLDUD012926" "SOLDUD013026" "SOLDUD013126" "SOLDUD020126" "SOLDUD020226" "SOLDUD020326" "SOLDUD020426" "SOLDUD020526" "SOLDUD020626" "ETHDUD012426" "ETHDUD012526" "ETHDUD012626" "ETHDUD012726" "ETHDUD012826" "ETHDUD012926" "ETHDUD013026" "ETHDUD013126" "ETHDUD020126" "ETHDUD020226" "ETHDUD020326" "ETHDUD020426" "ETHDUD020526" "ETHDUD020626" "XRPUD012426" "XRPUD012526" "XRPUD012626" "XRPUD012726" "XRPUD012826" "XRPUD012926" "XRPUD013026" "XRPUD013126" "XRPUD020126" "XRPUD020226" "XRPUD020326" "XRPUD020426" "XRPUD020526" "XRPUD020626" "BNBUD012426" "BNBUD012526" "BNBUD012626" "BNBUD012726" "BNBUD012826" "BNBUD012926" "BNBUD013026" "BNBUD013126" "BNBUD020126" "BNBUD020226" "BNBUD020326" "BNBUD020426" "BNBUD020526" "BNBUD020626" "ZAMA" "MEGA" "RNBW" "BLT" Symbol of the asset to withdraw.  
twoFactorToken| string Issued two factor token.  
autoBorrow| boolean Auto borrow to withdraw if required.  
autoLendRedeem| boolean Auto redeem a lend if required.  
recipientInformation| object (WithdrawalRecipientInformation)  Default: null  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**403 **

Forbidden.

**429 **

Too many requests.

**500 **

Internal server error.

**503 **

System under maintenance.

post/wapi/v1/capital/withdrawals

https://api.backpack.exchange/wapi/v1/capital/withdrawals

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "address": "string",

  * "blockchain": "0G",

  * "clientId": "string",

  * "quantity": "string",

  * "symbol": "BTC",

  * "twoFactorToken": "string",

  * "autoBorrow": true,

  * "autoLendRedeem": true,

  * "recipientInformation": null


}`

###  Response samples

  * 200
  * 400
  * 401
  * 403
  * 429
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "id": 0,

  * "blockchain": "0G",

  * "clientId": "string",

  * "identifier": "string",

  * "quantity": "string",

  * "fee": "string",

  * "fiatFee": "string",

  * "fiatState": "initialized",

  * "fiatSymbol": "AED",

  * "providerId": "string",

  * "symbol": "BTC",

  * "status": "confirmed",

  * "subaccountId": 0,

  * "toAddress": "string",

  * "transactionHash": "string",

  * "createdAt": "string",

  * "isInternal": true,

  * "bankName": "string",

  * "bankIdentifier": "string",

  * "accountIdentifier": "string",

  * "triggerAt": "string"


}`

## [](#tag/Capital/operation/get_dust_history)Get dust conversion history.

Retrieves the dust conversion history for the user.

**Instruction:** `dustHistoryQueryAll`

##### query Parameters

id| integer <int64> Filter to a given dust conversion id.  
---|---  
symbol| string Filter to the given symbol.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/dust

https://api.backpack.exchange/wapi/v1/history/dust

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "id": 0,

    * "quantity": "string",

    * "symbol": "string",

    * "usdcReceived": "string",

    * "timestamp": "string"

}


]`

## [](#tag/Capital/operation/get_settlement_history)Get settlement history.

History of settlement operations for the account.

**Instruction:** `settlementHistoryQueryAll`

##### query Parameters

limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
---|---  
offset| integer <uint64> Offset for pagination. Default `0`.  
source| string (SettlementSourceFilter)  Enum: "BackstopLiquidation" "CulledBorrowInterest" "CulledRealizePnl" "CulledRealizePnlBookUtilization" "FundingPayment" "RealizePnl" "TradingFees" "TradingFeesSystem"  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/settlement

https://api.backpack.exchange/wapi/v1/history/settlement

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "quantity": "string",

    * "source": "TradingFees",

    * "subaccountId": 0,

    * "timestamp": "string",

    * "userId": 0,

    * "positionId": "string",

    * "engineSequence": 0

}


]`

## [](#tag/Order)Order

Order management.

## [](#tag/Order/operation/get_order)Get open order.

Retrieves an open order from the order book. This only returns the order if it is resting on the order book (i.e. has not been completely filled, expired, or cancelled).

One of `orderId` or `clientId` must be specified. If both are specified then the request will be rejected.

**Instruction:** `orderQuery`

##### query Parameters

clientId| integer <uint32> Client ID of the order.  
---|---  
orderId| string ID of the order.  
symbolrequired| string Market symbol for the order.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**404 **

Order not found.

**500 **

Internal server error

get/api/v1/order

https://api.backpack.exchange/api/v1/order

###  Response samples

  * 200
  * 400
  * 404
  * 500



Content type

application/json; charset=utf-8

Example

MarketLimitBatchCommandOrderResult_OrderTypeMarket

Copy

`{

  * "orderType": "Market",

  * "id": "string",

  * "clientId": 0,

  * "createdAt": 0,

  * "executedQuantity": "string",

  * "executedQuoteQuantity": "string",

  * "quantity": "string",

  * "quoteQuantity": "string",

  * "reduceOnly": true,

  * "timeInForce": "GTC",

  * "selfTradePrevention": "RejectTaker",

  * "side": "Bid",

  * "status": "Cancelled",

  * "stopLossTriggerPrice": "string",

  * "stopLossLimitPrice": "string",

  * "stopLossTriggerBy": "MarkPrice",

  * "symbol": "string",

  * "takeProfitTriggerPrice": "string",

  * "takeProfitLimitPrice": "string",

  * "takeProfitTriggerBy": "MarkPrice",

  * "triggerBy": "MarkPrice",

  * "triggerPrice": "string",

  * "triggerQuantity": "string",

  * "triggeredAt": 0,

  * "relatedOrderId": "string",

  * "strategyId": "string",

  * "slippageTolerance": "string",

  * "slippageToleranceType": "TickSize"


}`

## [](#tag/Order/operation/execute_order)Execute order.

Submits an order to the matching engine for execution.

**Instruction:** `orderExecute`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
X-BROKER-ID| integer <uint16> Broker ID of the order.  
X-BROKER-KEY| string Broker key of the order.  
  
##### Request Body schema: application/json; charset=utf-8

required

autoLend| boolean If true then the order can lend. Spot margin only.  
---|---  
autoLendRedeem| boolean If true then the order can redeem a lend if required. Spot margin only.  
autoBorrow| boolean If true then the order can borrow. Spot margin only.  
autoBorrowRepay| boolean If true then the order can repay a borrow. Spot margin only.  
brokerId| integer <uint16> Broker ID of the order.  
clientId| integer <uint32> Custom order id.  
orderTyperequired| string Enum: "Market" "Limit" Order type, market or limit.  
postOnly| boolean Only post liquidity, do not take liquidity.  
price| string <decimal> The order price if this is a limit order.  
quantity| string <decimal> The order quantity. Market orders must specify either a `quantity` or `quoteQuantity`. All other order types must specify a `quantity`.  
quoteQuantity| string <decimal> The maximum amount of the quote asset to spend (Ask) or receive (Bid) for market orders. This is used for reverse market orders. The order book will execute a `quantity` as close as possible to the notional value of `quoteQuantity`.  
reduceOnly| boolean If true then the order can only reduce the positon. Futures only.  
selfTradePrevention| string Enum: "RejectTaker" "RejectMaker" "RejectBoth" Action to take if the user crosses themselves in the order book.  
siderequired| string Enum: "Bid" "Ask" Order will be matched against the resting orders on the other side of the order book.  
stopLossLimitPrice| string <decimal> Stop loss limit price. If set the stop loss will be a limit order.  
stopLossTriggerBy| string Enum: "MarkPrice" "LastPrice" "IndexPrice" Reference price that should trigger the stop loss order.  
stopLossTriggerPrice| string Stop loss price (price the stop loss order will be triggered at).  
symbolrequired| string The market for the order.  
takeProfitLimitPrice| string <decimal> Take profit limit price. If set the take profit will be a limit order,  
takeProfitTriggerBy| string Enum: "MarkPrice" "LastPrice" "IndexPrice" Reference price that should trigger the take profit order.  
takeProfitTriggerPrice| string Take profit price (price the take profit order will be triggered at).  
timeInForce| string Enum: "GTC" "IOC" "FOK" How long the order is good for.  
triggerBy| string Enum: "MarkPrice" "LastPrice" "IndexPrice" Reference price that should trigger the order.  
triggerPrice| string Trigger price if this is a conditional order.  
triggerQuantity| string Trigger quantity if this is a trigger order.  
slippageTolerance| string <decimal> Slippage tolerance allowed for the order.  
slippageToleranceType| string Enum: "TickSize" "Percent" Slippage tolerance type.  
  
### Responses

**200 **

Order executed.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

post/api/v1/order

https://api.backpack.exchange/api/v1/order

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "autoLend": true,

  * "autoLendRedeem": true,

  * "autoBorrow": true,

  * "autoBorrowRepay": true,

  * "brokerId": 0,

  * "clientId": 0,

  * "orderType": "Market",

  * "postOnly": true,

  * "price": "string",

  * "quantity": "string",

  * "quoteQuantity": "string",

  * "reduceOnly": true,

  * "selfTradePrevention": "RejectTaker",

  * "side": "Bid",

  * "stopLossLimitPrice": "string",

  * "stopLossTriggerBy": "MarkPrice",

  * "stopLossTriggerPrice": "string",

  * "symbol": "string",

  * "takeProfitLimitPrice": "string",

  * "takeProfitTriggerBy": "MarkPrice",

  * "takeProfitTriggerPrice": "string",

  * "timeInForce": "GTC",

  * "triggerBy": "MarkPrice",

  * "triggerPrice": "string",

  * "triggerQuantity": "string",

  * "slippageTolerance": "string",

  * "slippageToleranceType": "TickSize"


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Example

MarketLimitBatchCommandOrderResult_OrderTypeMarket

Copy

`{

  * "orderType": "Market",

  * "id": "string",

  * "clientId": 0,

  * "createdAt": 0,

  * "executedQuantity": "string",

  * "executedQuoteQuantity": "string",

  * "quantity": "string",

  * "quoteQuantity": "string",

  * "reduceOnly": true,

  * "timeInForce": "GTC",

  * "selfTradePrevention": "RejectTaker",

  * "side": "Bid",

  * "status": "Cancelled",

  * "stopLossTriggerPrice": "string",

  * "stopLossLimitPrice": "string",

  * "stopLossTriggerBy": "MarkPrice",

  * "symbol": "string",

  * "takeProfitTriggerPrice": "string",

  * "takeProfitLimitPrice": "string",

  * "takeProfitTriggerBy": "MarkPrice",

  * "triggerBy": "MarkPrice",

  * "triggerPrice": "string",

  * "triggerQuantity": "string",

  * "triggeredAt": 0,

  * "relatedOrderId": "string",

  * "strategyId": "string",

  * "slippageTolerance": "string",

  * "slippageToleranceType": "TickSize"


}`

## [](#tag/Order/operation/cancel_order)Cancel open order.

Cancels an open order from the order book.

One of `orderId` or `clientId` must be specified. If both are specified then the request will be rejected.

**Instruction:** `orderCancel`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

clientId| integer <uint32> Client ID of the order.  
---|---  
orderId| string ID of the order.  
symbolrequired| string Market the order exists on.  
  
### Responses

**200 **

Order cancelled.

**202 **

Request accepted but not yet executed.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

delete/api/v1/order

https://api.backpack.exchange/api/v1/order

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "clientId": 0,

  * "orderId": "string",

  * "symbol": "string"


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Example

MarketLimitBatchCommandOrderResult_OrderTypeMarket

Copy

`{

  * "orderType": "Market",

  * "id": "string",

  * "clientId": 0,

  * "createdAt": 0,

  * "executedQuantity": "string",

  * "executedQuoteQuantity": "string",

  * "quantity": "string",

  * "quoteQuantity": "string",

  * "reduceOnly": true,

  * "timeInForce": "GTC",

  * "selfTradePrevention": "RejectTaker",

  * "side": "Bid",

  * "status": "Cancelled",

  * "stopLossTriggerPrice": "string",

  * "stopLossLimitPrice": "string",

  * "stopLossTriggerBy": "MarkPrice",

  * "symbol": "string",

  * "takeProfitTriggerPrice": "string",

  * "takeProfitLimitPrice": "string",

  * "takeProfitTriggerBy": "MarkPrice",

  * "triggerBy": "MarkPrice",

  * "triggerPrice": "string",

  * "triggerQuantity": "string",

  * "triggeredAt": 0,

  * "relatedOrderId": "string",

  * "strategyId": "string",

  * "slippageTolerance": "string",

  * "slippageToleranceType": "TickSize"


}`

## [](#tag/Order/operation/execute_order_batch)Execute orders.

Submits a set of orders to the matching engine for execution in a batch.

**Batch commands instruction:** `orderExecute`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
X-BROKER-ID| integer <uint16> Broker ID of the order.  
  
##### Request Body schema: application/json; charset=utf-8

required

Array 

autoLend| boolean If true then the order can lend. Spot margin only.  
---|---  
autoLendRedeem| boolean If true then the order can redeem a lend if required. Spot margin only.  
autoBorrow| boolean If true then the order can borrow. Spot margin only.  
autoBorrowRepay| boolean If true then the order can repay a borrow. Spot margin only.  
brokerId| integer <uint16> Broker ID of the order.  
clientId| integer <uint32> Custom order id.  
orderTyperequired| string Enum: "Market" "Limit" Order type, market or limit.  
postOnly| boolean Only post liquidity, do not take liquidity.  
price| string <decimal> The order price if this is a limit order.  
quantity| string <decimal> The order quantity. Market orders must specify either a `quantity` or `quoteQuantity`. All other order types must specify a `quantity`.  
quoteQuantity| string <decimal> The maximum amount of the quote asset to spend (Ask) or receive (Bid) for market orders. This is used for reverse market orders. The order book will execute a `quantity` as close as possible to the notional value of `quoteQuantity`.  
reduceOnly| boolean If true then the order can only reduce the positon. Futures only.  
selfTradePrevention| string Enum: "RejectTaker" "RejectMaker" "RejectBoth" Action to take if the user crosses themselves in the order book.  
siderequired| string Enum: "Bid" "Ask" Order will be matched against the resting orders on the other side of the order book.  
stopLossLimitPrice| string <decimal> Stop loss limit price. If set the stop loss will be a limit order.  
stopLossTriggerBy| string Enum: "MarkPrice" "LastPrice" "IndexPrice" Reference price that should trigger the stop loss order.  
stopLossTriggerPrice| string Stop loss price (price the stop loss order will be triggered at).  
symbolrequired| string The market for the order.  
takeProfitLimitPrice| string <decimal> Take profit limit price. If set the take profit will be a limit order,  
takeProfitTriggerBy| string Enum: "MarkPrice" "LastPrice" "IndexPrice" Reference price that should trigger the take profit order.  
takeProfitTriggerPrice| string Take profit price (price the take profit order will be triggered at).  
timeInForce| string Enum: "GTC" "IOC" "FOK" How long the order is good for.  
triggerBy| string Enum: "MarkPrice" "LastPrice" "IndexPrice" Reference price that should trigger the order.  
triggerPrice| string Trigger price if this is a conditional order.  
triggerQuantity| string Trigger quantity if this is a trigger order.  
slippageTolerance| string <decimal> Slippage tolerance allowed for the order.  
slippageToleranceType| string Enum: "TickSize" "Percent" Slippage tolerance type.  
  
### Responses

**200 **

Batch orders executed.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

post/api/v1/orders

https://api.backpack.exchange/api/v1/orders

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "autoLend": true,

    * "autoLendRedeem": true,

    * "autoBorrow": true,

    * "autoBorrowRepay": true,

    * "brokerId": 0,

    * "clientId": 0,

    * "orderType": "Market",

    * "postOnly": true,

    * "price": "string",

    * "quantity": "string",

    * "quoteQuantity": "string",

    * "reduceOnly": true,

    * "selfTradePrevention": "RejectTaker",

    * "side": "Bid",

    * "stopLossLimitPrice": "string",

    * "stopLossTriggerBy": "MarkPrice",

    * "stopLossTriggerPrice": "string",

    * "symbol": "string",

    * "takeProfitLimitPrice": "string",

    * "takeProfitTriggerBy": "MarkPrice",

    * "takeProfitTriggerPrice": "string",

    * "timeInForce": "GTC",

    * "triggerBy": "MarkPrice",

    * "triggerPrice": "string",

    * "triggerQuantity": "string",

    * "slippageTolerance": "string",

    * "slippageToleranceType": "TickSize"

}


]`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "operation": "Ok",

    * "orderType": "Market",

    * "id": "string",

    * "clientId": 0,

    * "createdAt": 0,

    * "executedQuantity": "string",

    * "executedQuoteQuantity": "string",

    * "quantity": "string",

    * "quoteQuantity": "string",

    * "reduceOnly": true,

    * "timeInForce": "GTC",

    * "selfTradePrevention": "RejectTaker",

    * "side": "Bid",

    * "status": "Cancelled",

    * "stopLossTriggerPrice": "string",

    * "stopLossLimitPrice": "string",

    * "stopLossTriggerBy": "MarkPrice",

    * "symbol": "string",

    * "takeProfitTriggerPrice": "string",

    * "takeProfitLimitPrice": "string",

    * "takeProfitTriggerBy": "MarkPrice",

    * "triggerBy": "MarkPrice",

    * "triggerPrice": "string",

    * "triggerQuantity": "string",

    * "triggeredAt": 0,

    * "relatedOrderId": "string",

    * "strategyId": "string",

    * "slippageTolerance": "string",

    * "slippageToleranceType": "TickSize"

}


]`

## [](#tag/Order/operation/get_open_orders)Get open orders.

Retrieves all open orders. If a symbol is provided, only open orders for that market will be returned, otherwise all open orders are returned.

**Instruction:** `orderQueryAll`

##### query Parameters

marketType| string (MarketType)  Enum: "SPOT" "PERP" "IPERP" "DATED" "PREDICTION" "RFQ" The market for the orders (SPOT or PERP).  
---|---  
symbol| string The symbol of the market for the orders.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal Server Error.

get/api/v1/orders

https://api.backpack.exchange/api/v1/orders

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "orderType": "Market",

    * "id": "string",

    * "clientId": 0,

    * "createdAt": 0,

    * "executedQuantity": "string",

    * "executedQuoteQuantity": "string",

    * "quantity": "string",

    * "quoteQuantity": "string",

    * "reduceOnly": true,

    * "timeInForce": "GTC",

    * "selfTradePrevention": "RejectTaker",

    * "side": "Bid",

    * "status": "Cancelled",

    * "stopLossTriggerPrice": "string",

    * "stopLossLimitPrice": "string",

    * "stopLossTriggerBy": "MarkPrice",

    * "symbol": "string",

    * "takeProfitTriggerPrice": "string",

    * "takeProfitLimitPrice": "string",

    * "takeProfitTriggerBy": "MarkPrice",

    * "triggerBy": "MarkPrice",

    * "triggerPrice": "string",

    * "triggerQuantity": "string",

    * "triggeredAt": 0,

    * "relatedOrderId": "string",

    * "strategyId": "string",

    * "slippageTolerance": "string",

    * "slippageToleranceType": "TickSize"

}


]`

## [](#tag/Order/operation/cancel_open_orders)Cancel open orders.

Cancels all open orders on the specified market.

**Instruction:** `orderCancelAll`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

symbolrequired| string Market to cancel orders for.  
---|---  
orderType| string Enum: "RestingLimitOrder" "ConditionalOrder" Type of orders to cancel.  
  
### Responses

**200 **

Success.

**202 **

Request accepted but not yet executed.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

delete/api/v1/orders

https://api.backpack.exchange/api/v1/orders

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "symbol": "string",

  * "orderType": "RestingLimitOrder"


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "orderType": "Market",

    * "id": "string",

    * "clientId": 0,

    * "createdAt": 0,

    * "executedQuantity": "string",

    * "executedQuoteQuantity": "string",

    * "quantity": "string",

    * "quoteQuantity": "string",

    * "reduceOnly": true,

    * "timeInForce": "GTC",

    * "selfTradePrevention": "RejectTaker",

    * "side": "Bid",

    * "status": "Cancelled",

    * "stopLossTriggerPrice": "string",

    * "stopLossLimitPrice": "string",

    * "stopLossTriggerBy": "MarkPrice",

    * "symbol": "string",

    * "takeProfitTriggerPrice": "string",

    * "takeProfitLimitPrice": "string",

    * "takeProfitTriggerBy": "MarkPrice",

    * "triggerBy": "MarkPrice",

    * "triggerPrice": "string",

    * "triggerQuantity": "string",

    * "triggeredAt": 0,

    * "relatedOrderId": "string",

    * "strategyId": "string",

    * "slippageTolerance": "string",

    * "slippageToleranceType": "TickSize"

}


]`

## [](#tag/Order/operation/get_fills)Get fill history.

Retrieves historical fills, with optional filtering for a specific order or symbol.

**Instruction:** `fillHistoryQueryAll`

##### query Parameters

orderId| string Filter to the given order.  
---|---  
strategyId| string Filter to the given strategy.  
from| integer <int64> Filter to minimum time (milliseconds).  
to| integer <int64> Filter to maximum time (milliseconds).  
symbol| string Filter to the given symbol.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
fillType| string (FillType)  Enum: "User" "BookLiquidation" "Adl" "Backstop" "Liquidation" "AllLiquidation" "CollateralConversion" "CollateralConversionAndSpotLiquidation" Filter to return fills for different fill types  
marketType| Array of strings (MarketType) Items Enum: "SPOT" "PERP" "IPERP" "DATED" "PREDICTION" "RFQ" Market type.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/fills

https://api.backpack.exchange/wapi/v1/history/fills

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "clientId": "string",

    * "fee": "string",

    * "feeSymbol": "string",

    * "isMaker": true,

    * "orderId": "string",

    * "price": "string",

    * "quantity": "string",

    * "side": "Bid",

    * "symbol": "string",

    * "systemOrderType": "CollateralConversion",

    * "timestamp": "string",

    * "tradeId": 0

}


]`

## [](#tag/Order/operation/get_order_history)Get order history.

Retrieves the order history for the user. This includes orders that have been filled and are no longer on the book. It may include orders that are on the book, but the `/orders` endpoint contains more up to date data.

**Instruction:** `orderHistoryQueryAll`

##### query Parameters

orderId| string Filter to the given order.  
---|---  
strategyId| string Filter to the given strategy.  
symbol| string Filter to the given symbol.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
marketType| Array of strings (MarketType) Items Enum: "SPOT" "PERP" "IPERP" "DATED" "PREDICTION" "RFQ" Market type.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/orders

https://api.backpack.exchange/wapi/v1/history/orders

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "id": "string",

    * "createdAt": "string",

    * "executedQuantity": "string",

    * "executedQuoteQuantity": "string",

    * "expiryReason": "AccountTradingSuspended",

    * "orderType": "Market",

    * "postOnly": true,

    * "price": "string",

    * "quantity": "string",

    * "quoteQuantity": "string",

    * "selfTradePrevention": "RejectTaker",

    * "status": "Cancelled",

    * "side": "Bid",

    * "stopLossTriggerPrice": "string",

    * "stopLossLimitPrice": "string",

    * "stopLossTriggerBy": "MarkPrice",

    * "symbol": "string",

    * "takeProfitTriggerPrice": "string",

    * "takeProfitLimitPrice": "string",

    * "takeProfitTriggerBy": "MarkPrice",

    * "timeInForce": "GTC",

    * "triggerBy": "MarkPrice",

    * "triggerPrice": "string",

    * "triggerQuantity": "string",

    * "clientId": 0,

    * "systemOrderType": "CollateralConversion",

    * "strategyId": "string",

    * "slippageTolerance": "string",

    * "slippageToleranceType": "TickSize"

}


]`

## [](#tag/Position)Position

Positions and futures data.

## [](#tag/Position/operation/get_positions)Get open positions.

Retrieves account position summary.

**Instruction:** `positionQuery`

##### query Parameters

symbol| string Filter for a single position by symbol.  
---|---  
marketType| string (MarketType)  Enum: "SPOT" "PERP" "IPERP" "DATED" "PREDICTION" "RFQ" The market for the orders (SPOT or PERP).  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**404 **

Position not found.

**500 **

Internal server error.

get/api/v1/position

https://api.backpack.exchange/api/v1/position

###  Response samples

  * 200
  * 400
  * 401
  * 404
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "breakEvenPrice": "string",

    * "entryPrice": "string",

    * "estLiquidationPrice": "string",

    * "imf": "string",

    * "imfFunction": {
      * "type": "sqrt",

      * "base": "string",

      * "factor": "string"

},

    * "markPrice": "string",

    * "mmf": "string",

    * "mmfFunction": {
      * "type": "sqrt",

      * "base": "string",

      * "factor": "string"

},

    * "netCost": "string",

    * "netQuantity": "string",

    * "netExposureQuantity": "string",

    * "netExposureNotional": "string",

    * "pnlRealized": "string",

    * "pnlUnrealized": "string",

    * "cumulativeFundingPayment": "string",

    * "subaccountId": 0,

    * "symbol": "string",

    * "userId": 0,

    * "positionId": "string",

    * "cumulativeInterest": "string"

}


]`

## [](#tag/Position/operation/get_funding_payments)Get funding payments.

Users funding payment history for futures.

**Instruction:** `fundingHistoryQueryAll`

##### query Parameters

subaccountId| integer <uint16> Filter for a subaccount.  
---|---  
symbol| string Market symbol to query. If not set, all markets are returned.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset for pagination. Default `0`.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/funding

https://api.backpack.exchange/wapi/v1/history/funding

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "userId": 0,

    * "subaccountId": 0,

    * "symbol": "string",

    * "quantity": "string",

    * "intervalEndTimestamp": "string",

    * "fundingRate": "string"

}


]`

## [](#tag/Position/operation/get_position_history)Get position history.

Retrieves historical positions, with optional filtering for a specific symbol.

**Instruction:** `positionHistoryQueryAll`

##### query Parameters

symbol| string Market symbol to query position history for.  
---|---  
state| string (PositionState)  Enum: "Open" "Closed" Position state to filter positions.  
marketType| Array of strings (MarketType) Items Enum: "SPOT" "PERP" "IPERP" "DATED" "PREDICTION" "RFQ" Market type.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset for pagination. Default `0`.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/position

https://api.backpack.exchange/wapi/v1/history/position

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "id": "string",

    * "symbol": "string",

    * "netQuantity": "string",

    * "netExposureQuantity": "string",

    * "netExposureNotional": "string",

    * "netCost": "string",

    * "markPrice": "string",

    * "entryPrice": "string",

    * "cumulativePnlRealized": "string",

    * "unrealizedPnl": "string",

    * "fundingQuantity": "string",

    * "interest": "string",

    * "liquidated": "string",

    * "imf": "string",

    * "fees": "string",

    * "state": "Open",

    * "closedVolume": "string",

    * "liquidationFees": "string",

    * "closingPrice": "string",

    * "accountLeverage": "string",

    * "openedAt": "string",

    * "closedAt": "string"

}


]`

## [](#tag/RFQ)RFQ

RFQ (Request For Quote) - Maker.

## [](#tag/RFQ/operation/submit_quote)Submit quote.

Submit a quote in response to an RFQ. If valid, the quote may be accepted within the specified time window.

**Instruction:** `quoteSubmit`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

rfqIdrequired| string RFQ ID.  
---|---  
clientId| integer <uint32> Custom RFQ quote ID.  
bidPricerequired| string <decimal> Bid price.  
askPricerequired| string <decimal> Ask price.  
autoLend| boolean Whether to lend proceeds.  
autoLendRedeem| boolean Whether to redeem lends if required to fulfill the Quote.  
autoBorrow| boolean Whether to borrow assets if required to fulfill the Quote.  
autoBorrowRepay| boolean Whether to use proceeds to repay borrows.  
  
### Responses

**200 **

Accepted.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

post/api/v1/rfq/quote

https://api.backpack.exchange/api/v1/rfq/quote

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "rfqId": "string",

  * "clientId": 0,

  * "bidPrice": "string",

  * "askPrice": "string",

  * "autoLend": true,

  * "autoLendRedeem": true,

  * "autoBorrow": true,

  * "autoBorrowRepay": true


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "rfqId": "string",

  * "quoteId": "string",

  * "clientId": 0,

  * "bidPrice": "string",

  * "askPrice": "string",

  * "status": "Cancelled",

  * "createdAt": 0


}`

## [](#tag/RFQ/operation/submit_rfq)Submit RFQ.

Submit an RFQ (Request For Quote). The RFQ will be available for a specified time window for makers to respond to.

**Instruction:** `rfqSubmit`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

clientId| integer <uint32> Custom RFQ ID.  
---|---  
quantity| string <decimal> RFQ quantity (in base asset).  
quoteQuantity| string <decimal> RFQ quote quantity (in quote asset).  
price| string <decimal> RFQ price. Only when execution mode is `Immediate`.  
symbolrequired| string RFQ symbol.  
siderequired| string Enum: "Bid" "Ask" Side of the order.  
executionMode| string Enum: "AwaitAccept" "Immediate" Execution mode. Defaults to `AwaitAccept` when not provided. If `Immediate`, the RFQ must have a price and the first quote within the given price will be automatically accepted. If `AwaitAccept`, the RFQ will wait for the user to accept a specific quote.  
autoLend| boolean Whether to lend proceeds.  
autoLendRedeem| boolean Whether to redeem lends if required to fulfill the RFQ.  
autoBorrow| boolean Whether to borrow assets if required to fulfill the RFQ.  
autoBorrowRepay| boolean Whether to use proceeds to repay borrows.  
  
### Responses

**200 **

Accepted.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

post/api/v1/rfq

https://api.backpack.exchange/api/v1/rfq

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "clientId": 0,

  * "quantity": "string",

  * "quoteQuantity": "string",

  * "price": "string",

  * "symbol": "string",

  * "side": "Bid",

  * "executionMode": "AwaitAccept",

  * "autoLend": true,

  * "autoLendRedeem": true,

  * "autoBorrow": true,

  * "autoBorrowRepay": true


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "rfqId": "string",

  * "clientId": 0,

  * "symbol": "string",

  * "side": "Bid",

  * "price": "string",

  * "quantity": "string",

  * "quoteQuantity": "string",

  * "submissionTime": 0,

  * "systemOrderType": "CollateralConversion",

  * "expiryTime": 0,

  * "status": "Cancelled",

  * "executionMode": "AwaitAccept",

  * "createdAt": 0


}`

## [](#tag/RFQ/operation/accept_quote)Accept quote.

Accept a specific quote from a maker in response to an RFQ.

**Instruction:** `quoteAccept`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

rfqId| string RFQ ID.  
---|---  
clientId| integer <uint32> Custom RFQ ID.  
quoteIdrequired| string RFQ quote ID.  
  
### Responses

**200 **

Accepted.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

post/api/v1/rfq/accept

https://api.backpack.exchange/api/v1/rfq/accept

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "rfqId": "string",

  * "clientId": 0,

  * "quoteId": "string"


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "rfqId": "string",

  * "clientId": 0,

  * "symbol": "string",

  * "side": "Bid",

  * "price": "string",

  * "quantity": "string",

  * "quoteQuantity": "string",

  * "submissionTime": 0,

  * "systemOrderType": "CollateralConversion",

  * "expiryTime": 0,

  * "status": "Cancelled",

  * "executionMode": "AwaitAccept",

  * "createdAt": 0


}`

## [](#tag/RFQ/operation/refresh_rfq)Refresh RFQ.

Refresh a RFQ, extending the time window it is available for.

**Instruction:** `rfqRefresh`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

rfqIdrequired| string RFQ ID. An RFQ can only be refreshed using the RFQ ID.  
---|---  
  
### Responses

**200 **

Accepted.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

post/api/v1/rfq/refresh

https://api.backpack.exchange/api/v1/rfq/refresh

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "rfqId": "string"


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "rfqId": "string",

  * "clientId": 0,

  * "symbol": "string",

  * "side": "Bid",

  * "price": "string",

  * "quantity": "string",

  * "quoteQuantity": "string",

  * "submissionTime": 0,

  * "systemOrderType": "CollateralConversion",

  * "expiryTime": 0,

  * "status": "Cancelled",

  * "executionMode": "AwaitAccept",

  * "createdAt": 0


}`

## [](#tag/RFQ/operation/cancel_rfq)Cancel RFQ.

**Instruction:** `rfqCancel`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

rfqId| string RFQ ID.  
---|---  
clientId| integer <uint32> Custom RFQ ID.  
  
### Responses

**200 **

Accepted.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

post/api/v1/rfq/cancel

https://api.backpack.exchange/api/v1/rfq/cancel

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "rfqId": "string",

  * "clientId": 0


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "rfqId": "string",

  * "clientId": 0,

  * "symbol": "string",

  * "side": "Bid",

  * "price": "string",

  * "quantity": "string",

  * "quoteQuantity": "string",

  * "submissionTime": 0,

  * "systemOrderType": "CollateralConversion",

  * "expiryTime": 0,

  * "status": "Cancelled",

  * "executionMode": "AwaitAccept",

  * "createdAt": 0


}`

## [](#tag/RFQ/operation/get_rfq_history)Get RFQ history.

This includes RFQs that have been filled or expired.

**Instruction:** `rfqHistoryQueryAll`

##### query Parameters

rfqId| string Filter to the given rfq.  
---|---  
symbol| string Filter to the given symbol.  
status| string (OrderStatus)  Enum: "Cancelled" "Expired" "Filled" "New" "PartiallyFilled" "TriggerPending" "TriggerFailed" Filter to the given status.  
side| string (Side)  Enum: "Bid" "Ask" Filter to the given side.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/rfq

https://api.backpack.exchange/wapi/v1/history/rfq

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "rfqId": "string",

    * "clientId": 0,

    * "symbol": "string",

    * "side": "Bid",

    * "price": "string",

    * "quantity": "string",

    * "quoteQuantity": "string",

    * "submissionTime": "string",

    * "expiryTime": "string",

    * "status": "Cancelled",

    * "executionMode": "AwaitAccept",

    * "createdAt": "string"

}


]`

## [](#tag/RFQ/operation/get_quote_history)Get quote history.

Retrieves the quote history for the user. This includes quotes that have been filled or expired.

**Instruction:** `quoteHistoryQueryAll`

##### query Parameters

quoteId| string Filter to the given quote.  
---|---  
symbol| string Filter to the given symbol.  
status| string (OrderStatus)  Enum: "Cancelled" "Expired" "Filled" "New" "PartiallyFilled" "TriggerPending" "TriggerFailed" Filter to the given status.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/quote

https://api.backpack.exchange/wapi/v1/history/quote

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "rfqId": "string",

    * "quoteId": "string",

    * "clientId": 0,

    * "bidPrice": "string",

    * "askPrice": "string",

    * "status": "Cancelled",

    * "createdAt": "string"

}


]`

## [](#tag/RFQ/operation/get_rfq_fill_history)Get RFQ fill history.

Retrieves RFQ fill history for the user.

**Instruction:** `rfqFillHistoryQueryAll`

##### query Parameters

quoteId| string Filter to the given RFQ.  
---|---  
symbol| string Filter to the given symbol.  
side| string (Side)  Enum: "Bid" "Ask" Filter to the given side.  
fillType| string (RfqFillType)  Enum: "User" "CollateralConversion" Filter by fill type (system order type).  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/rfq/fill

https://api.backpack.exchange/wapi/v1/history/rfq/fill

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "rfqId": "string",

    * "clientId": 0,

    * "quoteId": "string",

    * "symbol": "string",

    * "side": "Bid",

    * "quantity": "string",

    * "quoteQuantity": "string",

    * "fillPrice": "string",

    * "createdAt": "string",

    * "filledAt": "string",

    * "systemOrderType": "CollateralConversion"

}


]`

## [](#tag/RFQ/operation/get_quote_fill_history)Get quote fill history.

Retrieves the quote fill history for the user.

**Instruction:** `quoteFillHistoryQueryAll`

##### query Parameters

quoteId| string Filter to the given quote.  
---|---  
symbol| string Filter to the given symbol.  
side| string (Side)  Enum: "Bid" "Ask" Filter to the given side.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/quote/fill

https://api.backpack.exchange/wapi/v1/history/quote/fill

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "clientId": 0,

    * "quoteId": "string",

    * "rfqId": "string",

    * "symbol": "string",

    * "side": "Bid",

    * "quantity": "string",

    * "fillPrice": "string",

    * "fee": "string",

    * "feeSymbol": "string",

    * "createdAt": "string",

    * "filledAt": "string"

}


]`

## [](#tag/Strategy)Strategy

Strategies.

## [](#tag/Strategy/operation/get_strategy)Get open strategy.

Retrieves an open strategy from the engine. This only returns the strategy if it is active (i.e. has not been completely filled, cancelled by the user, or cancelled by the system).

One of `strategyId` or `clientStrategyId` must be specified.

**Instruction:** `strategyQuery`

##### query Parameters

clientStrategyId| integer <uint32> Client ID of the strategy.  
---|---  
strategyId| string ID of the strategy.  
symbolrequired| string Market symbol for the strategy.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**404 **

Strategy not found.

**500 **

Internal server error.

get/api/v1/strategy

https://api.backpack.exchange/api/v1/strategy

###  Response samples

  * 200
  * 400
  * 404
  * 500



Content type

application/json; charset=utf-8

Copy

`{

  * "strategyType": "Scheduled",

  * "id": "string",

  * "clientStrategyId": 0,

  * "createdAt": 0,

  * "executedQuantity": "string",

  * "executedQuoteQuantity": "string",

  * "quantity": "string",

  * "reduceOnly": true,

  * "selfTradePrevention": "RejectTaker",

  * "status": "Running",

  * "side": "Bid",

  * "symbol": "string",

  * "timeInForce": "GTC",

  * "duration": 0,

  * "interval": 0,

  * "randomizedIntervalQuantity": true,

  * "slippageTolerance": "string",

  * "slippageToleranceType": "TickSize"


}`

## [](#tag/Strategy/operation/strategy_create)Create strategy.

Submits a strategy to the engine for processing.

**Instruction:** `strategyCreate`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-BROKER-ID| integer <uint16> Broker ID of the order.  
X-BROKER-KEY| string Broker key of the order.  
  
##### Request Body schema: application/json; charset=utf-8

required

autoLend| boolean If true then the strategy's orders can lend. Spot margin only.  
---|---  
autoLendRedeem| boolean If true then the strategy's orders can redeem a lend if required. Spot margin only.  
autoBorrow| boolean If true then the strategy's orders can borrow. Spot margin only.  
autoBorrowRepay| boolean If true then the strategy's orders can repay a borrow. Spot margin only.  
brokerId| integer <uint16> Broker ID of the orders.  
clientStrategyId| integer <uint32> Custom client strategy id.  
strategyTyperequired| string Value: "Scheduled" Strategy type.  
quantity| string <decimal> The strategy quantity.  
price| string <decimal> The strategy limit price.  
postOnly| boolean Only post liquidity, do not take liquidity.  
reduceOnly| boolean If true then the strategy's orders can only reduce the position. Futures only.  
selfTradePrevention| string Enum: "RejectTaker" "RejectMaker" "RejectBoth" Action to take if the user crosses themselves in the order book.  
siderequired| string Enum: "Bid" "Ask" The side of the strategy.  
symbolrequired| string The market for the strategy.  
timeInForce| string Enum: "GTC" "IOC" "FOK" How long the strategy's orders are good for.  
duration| integer <uint64> Duration of the strategy.  
interval| integer <uint64> Interval of the strategy.  
randomizedIntervalQuantity| boolean Randomized interval quantity for the strategy.  
slippageTolerance| string <decimal> Slippage tolerance allowed for the order.  
slippageToleranceType| string Enum: "TickSize" "Percent" Slippage tolerance type.  
  
### Responses

**200 **

Strategy created.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

post/api/v1/strategy

https://api.backpack.exchange/api/v1/strategy

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "autoLend": true,

  * "autoLendRedeem": true,

  * "autoBorrow": true,

  * "autoBorrowRepay": true,

  * "brokerId": 0,

  * "clientStrategyId": 0,

  * "strategyType": "Scheduled",

  * "quantity": "string",

  * "price": "string",

  * "postOnly": true,

  * "reduceOnly": true,

  * "selfTradePrevention": "RejectTaker",

  * "side": "Bid",

  * "symbol": "string",

  * "timeInForce": "GTC",

  * "duration": 0,

  * "interval": 0,

  * "randomizedIntervalQuantity": true,

  * "slippageTolerance": "string",

  * "slippageToleranceType": "TickSize"


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "strategyType": "Scheduled",

  * "id": "string",

  * "clientStrategyId": 0,

  * "createdAt": 0,

  * "executedQuantity": "string",

  * "executedQuoteQuantity": "string",

  * "quantity": "string",

  * "reduceOnly": true,

  * "selfTradePrevention": "RejectTaker",

  * "status": "Running",

  * "side": "Bid",

  * "symbol": "string",

  * "timeInForce": "GTC",

  * "duration": 0,

  * "interval": 0,

  * "randomizedIntervalQuantity": true,

  * "slippageTolerance": "string",

  * "slippageToleranceType": "TickSize"


}`

## [](#tag/Strategy/operation/cancel_strategy)Cancel open strategy.

Cancels an open strategy currently being run.

One of `strategyId` or `clientStrategyId` must be specified.

**Instruction:** `strategyCancel`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

clientStrategyId| integer <uint32> Client ID of the strategy.  
---|---  
strategyId| string ID of the strategy.  
symbolrequired| string Market the strategy exists on.  
  
### Responses

**200 **

Strategy cancelled.

**202 **

Request accepted but not yet executed.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

delete/api/v1/strategy

https://api.backpack.exchange/api/v1/strategy

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "clientStrategyId": 0,

  * "strategyId": "string",

  * "symbol": "string"


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

`{

  * "strategyType": "Scheduled",

  * "id": "string",

  * "clientStrategyId": 0,

  * "createdAt": 0,

  * "executedQuantity": "string",

  * "executedQuoteQuantity": "string",

  * "quantity": "string",

  * "reduceOnly": true,

  * "selfTradePrevention": "RejectTaker",

  * "status": "Running",

  * "side": "Bid",

  * "symbol": "string",

  * "timeInForce": "GTC",

  * "duration": 0,

  * "interval": 0,

  * "randomizedIntervalQuantity": true,

  * "slippageTolerance": "string",

  * "slippageToleranceType": "TickSize"


}`

## [](#tag/Strategy/operation/get_open_strategies)Get open strategies.

Retrieves all open strategies. If a symbol is provided, only open strategies for that market will be returned, otherwise all open strategies are returned.

**Instruction:** `strategyQueryAll`

##### query Parameters

marketType| string (MarketType)  Enum: "SPOT" "PERP" "IPERP" "DATED" "PREDICTION" "RFQ" The market for the strategies (SPOT or PERP).  
---|---  
strategyType| string (StrategyTypeEnum)  Value: "Scheduled" The strategy type.  
symbol| string The symbol of the market for the strategies.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**500 **

Internal Server Error.

get/api/v1/strategies

https://api.backpack.exchange/api/v1/strategies

###  Response samples

  * 200
  * 400
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "strategyType": "Scheduled",

    * "id": "string",

    * "clientStrategyId": 0,

    * "createdAt": 0,

    * "executedQuantity": "string",

    * "executedQuoteQuantity": "string",

    * "quantity": "string",

    * "reduceOnly": true,

    * "selfTradePrevention": "RejectTaker",

    * "status": "Running",

    * "side": "Bid",

    * "symbol": "string",

    * "timeInForce": "GTC",

    * "duration": 0,

    * "interval": 0,

    * "randomizedIntervalQuantity": true,

    * "slippageTolerance": "string",

    * "slippageToleranceType": "TickSize"

}


]`

## [](#tag/Strategy/operation/cancel_open_strategies)Cancel open strategies.

Cancels all open strategies on the specified market.

**Instruction:** `strategyCancelAll`

##### header Parameters

X-API-KEYrequired| string API key  
---|---  
X-SIGNATURErequired| string Signature of the request  
X-TIMESTAMPrequired| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
##### Request Body schema: application/json; charset=utf-8

required

symbolrequired| string Market to cancel strategies for.  
---|---  
strategyType| string Value: "Scheduled" Type of strategies to cancel.  
  
### Responses

**200 **

Success.

**202 **

Request accepted but not yet executed.

**400 **

Bad request.

**500 **

Internal server error.

**503 **

System under maintenance.

delete/api/v1/strategies

https://api.backpack.exchange/api/v1/strategies

###  Request samples

  * Payload



Content type

application/json; charset=utf-8

Copy

`{

  * "symbol": "string",

  * "strategyType": "Scheduled"


}`

###  Response samples

  * 200
  * 400
  * 500
  * 503



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "strategyType": "Scheduled",

    * "id": "string",

    * "clientStrategyId": 0,

    * "createdAt": 0,

    * "executedQuantity": "string",

    * "executedQuoteQuantity": "string",

    * "quantity": "string",

    * "reduceOnly": true,

    * "selfTradePrevention": "RejectTaker",

    * "status": "Running",

    * "side": "Bid",

    * "symbol": "string",

    * "timeInForce": "GTC",

    * "duration": 0,

    * "interval": 0,

    * "randomizedIntervalQuantity": true,

    * "slippageTolerance": "string",

    * "slippageToleranceType": "TickSize"

}


]`

## [](#tag/Strategy/operation/get_strategies_history)Get strategy history.

Retrieves the strategy history for the user. This returns strategies that are no longer active as they have either been completed, cancelled by the user or cancelled by the system.

**Instruction:** `strategyHistoryQueryAll`

##### query Parameters

strategyId| string Filter to the given strategy.  
---|---  
symbol| string Filter to the given symbol.  
limit| integer <uint64> Maximum number to return. Default `100`, maximum `1000`.  
offset| integer <uint64> Offset. Default `0`.  
marketType| Array of strings (MarketType) Items Enum: "SPOT" "PERP" "IPERP" "DATED" "PREDICTION" "RFQ" Market type.  
sortDirection| string (SortDirection)  Enum: "Asc" "Desc" Sort direction.  
  
##### header Parameters

X-API-KEY| string API key  
---|---  
X-SIGNATURE| string Signature of the request  
X-TIMESTAMP| integer <int64> Timestamp of the request in milliseconds  
X-WINDOW| integer <uint64> Time the request is valid for in milliseconds (default `5000`, maximum `60000`)  
  
### Responses

**200 **

Success.

**400 **

Bad request.

**401 **

Unauthorized.

**500 **

Internal server error.

get/wapi/v1/history/strategies

https://api.backpack.exchange/wapi/v1/history/strategies

###  Response samples

  * 200
  * 400
  * 401
  * 500



Content type

application/json; charset=utf-8

Copy

Expand all  Collapse all 

`[

  * {
    * "id": "string",

    * "createdAt": "string",

    * "executedQuantity": "string",

    * "executedQuoteQuantity": "string",

    * "cancelReason": "Expired",

    * "strategyType": "Scheduled",

    * "quantity": "string",

    * "selfTradePrevention": "RejectTaker",

    * "status": "Running",

    * "side": "Bid",

    * "symbol": "string",

    * "timeInForce": "GTC",

    * "clientStrategyId": 0,

    * "duration": 0,

    * "interval": 0,

    * "randomizedIntervalQuantity": true,

    * "slippageTolerance": "string",

    * "slippageToleranceType": "TickSize"

}


]`

## [](#tag/Streams)Streams

## [](#tag/Streams/Usage)Usage

## [](#tag/Streams/Usage/Subscribing)Subscribing

To use the websocket API, connect to `wss://ws.backpack.exchange`.

To subscribe to a stream with the name `stream` send a text frame over the websocket connection with the following JSON payload:
    
    
    {
      "method": "SUBSCRIBE",
      "params": ["stream"]
    }
    

Similarly, to unsubscribe from a stream with the name `stream`:
    
    
    {
      "method": "UNSUBSCRIBE",
      "params": ["stream"]
    }
    

You can subscribe or unsubscribe from multiple streams if you include more than one in the params field.

All data from streams is wrapped in a JSON object of the following form:
    
    
    {
      "stream": "<stream>",
      "data": "<payload>"
    }
    

The following command can be used to test subscribing to a stream:
    
    
    (sleep 1; \
    echo '{"method":"SUBSCRIBE","params":["depth.SOL_USDC"]}';\
    cat) |\
    wscat -c wss://ws.backpack.exchange
    

The payloads for each stream time are outlined below.

## [](#tag/Streams/Usage/Timing)Timing

Timestamps are in microseconds (except for the K-line start and end times). The event timestamp is the time the event was emitted from the websocket server, and the engine timestamp is the time the event was generated by the matching engine.

If a message aggregates more than one event (for example, a depth message), the engine timestamp will be the timestamp of the last matching engine event.

## [](#tag/Streams/Usage/Keeping-the-connection-alive)Keeping the connection alive

To keep the connection alive, a `Ping` frame will be sent from the server every 60s, and a `Pong` is expected to be received from the client. If a `Pong` is not received within 120s, a `Close` frame will be sent and the connection will be closed.

If the server is shutting down, a `Close` frame will be sent and then a grace period of 30s will be given before the connection is closed. The client should reconnect after receiving the `Close` frame. The client will be reconnected to a server that is not shutting down.

## [](#tag/Streams/Private)Private

Subscribing to a private stream requires a valid signature generated from an ED25519 keypair. For stream subscriptions, the signature should be of the form:
    
    
    instruction=subscribe&timestamp=1614550000000&window=5000
    

Where the timestamp and window are in milliseconds.

Private streams are prefixed with `account.` and require signature data to be submitted in the subscribe parameters. The verifying key and signature should be base64 encoded.
    
    
    {
      "method": "SUBSCRIBE",
      "params": ["stream"],
      "signature": ["<verifying key>", "<signature>", "<timestamp>", "<window>"]
    }
    

## [](#tag/Streams/Private/Order-update)Order update

On any mutation to an order the order will be pushed to the order update stream. The event type of the order update will be one of the following:

  * `orderAccepted`
  * `orderCancelled`
  * `orderExpired`
  * `orderFill`
  * `orderModified`
  * `triggerPlaced`
  * `triggerFailed`



An `orderModified` update will be received when a resting reduce only order's quantity is decreased in order to prevent position side reversal.

### Stream Name Format

  * For all markets: `account.orderUpdate`
  * For single market: `account.orderUpdate.<symbol>`


    
    
    {
      "e": "orderAccepted",   // Event type
      "E": 1694687692980000,  // Event time in microseconds
      "s": "SOL_USD",         // Symbol
      "c": 123,               // Client order ID
      "S": "Bid",             // Side
      "o": "LIMIT",           // Order type
      "f": "GTC",             // Time in force
      "q": "32123",           // Quantity
      "Q": "32123",           // Quantity in quote
      "p": "20",              // Price
      "P": "21",              // Trigger price
      "B": "LastPrice",       // Trigger by
      "a": "30",              // Take profit trigger price
      "b": "10",              // Stop loss trigger price
      "j": "30",              // Take profit limit price
      "k": "10",              // Stop loss limit price
      "d": "MarkPrice",       // Take profit trigger by
      "g": "IndexPrice",      // Stop loss trigger by
      "Y": "10",              // Trigger quantity
      "X": "New",             // Order state
      "R": "PRICE_BAND",      // Order expiry reason
      "i": "1111343026172067" // Order ID
      "t": 567,               // Trade ID
      "l": "1.23",            // Fill quantity
      "z": "321",             // Executed quantity
      "Z": "123",             // Executed quantity in quote
      "L": "20",              // Fill price
      "m": true,              // Whether the order was maker
      "n": "23",              // Fee
      "N": "USD",             // Fee symbol
      "V": "RejectTaker",     // Self trade prevention
      "T": 1694687692989999,  // Engine timestamp in microseconds
      "O": "USER"             // Origin of the update
      "I": "1111343026156135" // Related order ID
      "H": 6023471188         // Strategy ID
      "y": true               // Post only
    }
    

There are several possible values for the `O` field (origin of the update):

  * `USER`: The origin of the update was due to order entry by the user.
  * `LIQUIDATION_AUTOCLOSE`: The origin of the update was due to a liquidation by the liquidation engine.
  * `ADL_AUTOCLOSE`: The origin of the update was due to an ADL (auto-deleveraging) event.
  * `COLLATERAL_CONVERSION`: The origin of the update was due to a collateral conversion to settle debt on the account.
  * `SETTLEMENT_AUTOCLOSE`: The origin of the update was due to the settlement of a position on a dated market.
  * `BACKSTOP_LIQUIDITY_PROVIDER`: The origin of the update was due to a backstop liquidity provider facilitating a liquidation.



Some fields are conditional on the order settings or event type:

  * `c` \- Only present if the order has a client order ID.
  * `q` \- Only present if the order has a quantity set.
  * `Q` \- Only present if the order is reverse market order.
  * `p` \- Only present if the order is a limit order.
  * `P` \- Only present if the order is a trigger order.
  * `B` \- Only present if the order is a trigger order.
  * `a` \- Only present if the order has a take profit trigger price set.
  * `b` \- Only present if the order has a stop loss trigger price set.
  * `d` \- Only present if the order has a take profit trigger price set.
  * `g` \- Only present if the order has a stop loss trigger price set.
  * `Y` \- Only present if the order is a trigger order.
  * `R` \- Only present if the event is a `orderExpired` event.
  * `t` \- Only present if the event is a `orderFill` event.
  * `l` \- Only present if the event is a `orderFill` event.
  * `L` \- Only present if the event is a `orderFill` event.
  * `m` \- Only present if the event is a `orderFill` event.
  * `n` \- Only present if the event is a `orderFill` event.
  * `N` \- Only present if the event is a `orderFill` event.



## [](#tag/Streams/Private/Position-update)Position update

On any mutation to a position the position will be pushed to the position update stream. The event type of the position update will be one of the following:

  * `positionAdjusted`
  * `positionOpened`
  * `positionClosed`



On subscription, a message will be sent to the client with the current open positions, if any. The `e` field will not be present in the message.

### Stream Name Format

  * For all markets: `account.positionUpdate`
  * For single market: `account.positionUpdate.<symbol>`


    
    
    {
      "e": "positionOpened",  // Event type
      "E": 1694687692980000,  // Event time in microseconds
      "s": "SOL_USDC_PERP",    // Symbol
      "b": 123,               // Break event price
      "B": 122,               // Entry price
      "f": 0.5,               // Initial margin fraction
      "M": 122,               // Mark price
      "m": 0.01,              // Maintenance margin fraction
      "q": 5,                 // Net quantity
      "Q": 6,                 // Net exposure quantity
      "n": 732 ,              // Net exposure notional
      "i": "1111343026172067" // Position ID
      "p": "-1",              // PnL realized
      "P": "0",               // PnL unrealized
      "T": 1694687692989999   // Engine timestamp in microseconds
    }
    

The net quantity field will be positive if the position is long and negative if the position is short.

The net exposure quantity field includes exposure from the open position, as well as any open orders.

## [](#tag/Streams/Private/RFQ-Update)RFQ Update

This WebSocket stream provides real-time updates on RFQs (Request for Quotes) that are relevant to makers. Events are pushed to this stream whenever there is a significant state change in an RFQ or its associated quotes, allowing makers to monitor and respond to RFQs as they progress through various states.

### Event Types

For RFQs that submitted by other requesters.

  * `rfqActive`: Indicates that an RFQ is active and open for quotes.



For RFQs that submitted by your account.

  * `rfqAccepted`: Indicates that an RFQ has been accepted and is no
  * `rfqRefreshed`: Indicates that an RFQ has been refreshed, is active and open for quotes.
  * `rfqCancelled`: Indicates that an RFQ has been cancelled or expired.
  * `rfqCandidate`: RFQ has received a new best quote.
  * `rfqFilled`: Indicates that an RFQ has been fully filled with a quote.



For Quotes submitted by your account.

  * `quoteAccepted`: Indicates that a quote submitted by the maker has been accepted.
  * `quoteCancelled`: Indicates that a quote has been cancelled due to quote submission, RFQ being filled, refreshed, cancelled, or expired.



### Quote Submission and RFQ Timing

Makers should submit quotes before the **submission time** (`w` field) is reached, as indicated in each `rfqActive` event. An RFQ remains active until the **expiration time** (`W` field). If no quote is accepted or the RFQ is not cancelled, makers may continue to submit quotes until expiration.

RFQs can periodically request new quotes by issuing additional `rfqActive` events. Each new `rfqActive` event will have the same RFQ ID (`R` field) but updated values for **submission time** and **expiration time** , allowing makers to participate in extended or renewed quoting periods for ongoing RFQs.

### Stream Name Format

  * For all markets: `account.rfqUpdate`
  * For single market: `account.rfqUpdate.<symbol>`



### Example Messages

**RFQ Accepted** (sent to requester)
    
    
    {
      "e": "rfqAccepted",            // Event type
      "E": 1730225420369829,         // Event time in microseconds
      "R": 113392053149171712,       // RFQ ID
      "C": "123",                    // Client RFQ ID
      "s": "SOL_USDC_RFQ",           // Symbol
      "S": "Bid",                    // RFQ side
      "q": "10",                     // Quantity (if quantity in base asset)
      "w": 1730225480368,            // Submission time in milliseconds
      "W": 1730225540368,            // Expiry time in milliseconds
      "X": "New",                    // RFQ status
      "T": 1730225420368765          // Engine timestamp in microseconds
    }
    

**RFQ Active** (broadcast to all rfq listeners)
    
    
    {
      "e": "rfqActive",              // Event type
      "E": 1730225420369829,         // Event time in microseconds
      "R": 113392053149171712,       // RFQ ID
      "s": "SOL_USDC_RFQ",           // Symbol
      "q": "10",                     // Quantity (optional) (if quantity in base asset)
      "w": 1730225480368,            // Submission time in milliseconds
      "W": 1730225540368,            // Expiry time in milliseconds
      "X": "New",                    // RFQ status
      "T": 1730225420368765          // Engine timestamp in microseconds
    }
    

**RFQ Refreshed** (sent to requester)
    
    
    {
      "e": "rfqRefreshed",           // Event type
      "E": 1730225450369829,         // Event time in microseconds
      "R": 113392053149171712,       // RFQ ID
      "C": "123",                    // Client RFQ ID
      "s": "SOL_USDC_RFQ",           // Symbol
      "S": "Bid",                    // RFQ side
      "q": "10",                     // Quantity (optional) (if quantity in base asset)
      "w": 1730225480368,            // Submission time in milliseconds
      "W": 1730225540368,            // Expiry time in milliseconds
      "X": "New",                    // RFQ status
      "T": 1730225450368765          // Engine timestamp in microseconds
    }
    

**RFQ Cancelled** (sent to taker only)
    
    
    {
      "e": "rfqCancelled",           // Event type
      "E": 1730225460369829,         // Event time in microseconds
      "R": 113392053149171712,       // RFQ ID
      "C": "123",                    // Client RFQ ID
      "s": "SOL_USDC_RFQ",           // Symbol
      "S": "Bid",                    // RFQ side
      "Q": "150",                    // Quote quantity (optional) (if quantity in quote asset)
      "w": 1730225480368,            // Submission time in milliseconds
      "W": 1730225540368,            // Expiry time in milliseconds
      "X": "Cancelled",              // RFQ status
      "T": 1730225460368765          // Engine timestamp in microseconds
    }
    

**Quote Accepted** (sent to quoter)
    
    
    {
      "e": "quoteAccepted",          // Event type
      "E": 1730225434631394,         // Event time in microseconds
      "R": 113392053149171712,       // RFQ ID
      "u": 113392054083780608,       // Quote ID
      "C": "123",                    // Client Quote ID
      "s": "SOL_USDC_RFQ",           // Symbol
      "X": "New",                    // Quote status
      "T": 1730225434629778          // Engine timestamp in microseconds
    }
    

**Quote Cancelled** (sent to quoter)
    
    
    {
      "e": "quoteCancelled",         // Event type
      "E": 1730225583761963,         // Event time in microseconds
      "R": 113392061354344448,       // RFQ ID
      "u": 113392062870847488,       // Quote ID
      "C": "123",                    // Client Quote ID
      "s": "SOL_USDC_RFQ",           // Symbol
      "X": "Cancelled",              // Quote status
      "T": 1730225583753811          // Engine timestamp in microseconds
    }
    

**RFQ Candidate** (sent to requester with quote details)
    
    
    {
      "e": "rfqCandidate",           // Event type
      "E": 1730225490648996,         // Event time in microseconds
      "R": 113392053149171712,       // RFQ ID
      "u": 113392054083780608,       // Quote ID
      "C": "123",                    // Client RFQ ID
      "s": "SOL_USDC_RFQ",           // Symbol
      "S": "Bid",                    // RFQ side
      "q": "10",                     // RFQ quantity (in base asset)
      "Q": "150",                    // RFQ quote quantity (in quote asset)
      "p": "15.50",                  // Taker price (quote price + fee)
      "X": "New",                    // RFQ status
      "T": 1730225490647080          // Engine timestamp in microseconds
    }
    

**RFQ Filled** (sent to both requester and quoter)
    
    
    // To requester
    {
      "e": "rfqFilled",              // Event type
      "E": 1730225497648996,         // Event time in microseconds
      "R": 113392053149171712,       // RFQ ID
      "u": 113392054083780608,       // Quote ID
      "C": "123",                    // Client RFQ ID
      "s": "SOL_USDC_RFQ",           // Symbol
      "S": "Bid",                    // RFQ side
      "Q": "150",                    // RFQ quote quantity (optional) (if quantity in quote asset)
      "p": "15.50",                  // Taker price (quote price + fee)
      "X": "Filled",                 // RFQ status
      "T": 1730225497647080          // Engine timestamp in microseconds
    }
    
    // To quoter
    {
      "e": "rfqFilled",              // Event type
      "E": 1730225497648996,         // Event time in microseconds
      "R": 113392053149171712,       // RFQ ID
      "u": 113392054083780608,       // Quote ID
      "C": "123",                    // Client Quote ID
      "s": "SOL_USDC_RFQ",           // Symbol
      "p": "15.00",                  // Price
      "X": "Filled",                 // Quote status
      "T": 1730225497647080          // Engine timestamp in microseconds
    }
    

### Field Descriptions

  * `e` \- Event type (e.g., `rfqActive`, `rfqAccepted`, `rfqRefreshed`, `rfqCancelled`, `quoteAccepted`, `quoteCancelled`, `rfqCandidate`, `rfqFilled`).
  * `E` \- Event time in microseconds.
  * `R` \- RFQ ID, identifying the request for quote.
  * `u` \- Quote ID, identifying the specific quote.
  * `C` \- Client ID (either Client RFQ ID or Client Quote ID depending on context).
  * `s` \- Symbol the RFQ is for.
  * `S` \- Side of the RFQ, either "Bid" or "Ask".
  * `q` \- Quantity for the RFQ (in base asset, if quantity in base asset).
  * `Q` \- Quote quantity for the RFQ (in quote asset, if quantity in quote asset).
  * `p` \- Price associated with the quote/fill event.
  * `w` \- Submission time for the RFQ in milliseconds.
  * `W` \- Expiry time for the RFQ in milliseconds.
  * `X` \- Order status (e.g., `New`, `Cancelled`, `Filled`).
  * `o` \- System order type (e.g., `CollateralConversion`). Only present for system-initiated RFQs.
  * `T` \- Engine timestamp in microseconds.



Some fields are conditional and may be present only in specific events. RFQs are either requested in base quantity or quote quantity, but not both. Either `q` or `Q` will be present.

## [](#tag/Streams/Public)Public

## [](#tag/Streams/Public/Book-ticker)Book ticker

Stream name format: `bookTicker.<symbol>`
    
    
    {
      "e": "bookTicker",          // Event type
      "E": 1694687965941000,      // Event time in microseconds
      "s": "SOL_USDC",            // Symbol
      "a": "18.70",               // Inside ask price
      "A": "1.000",               // Inside ask quantity
      "b": "18.67",               // Inside bid price
      "B": "2.000",               // Inside bid quantity
      "u": "111063070525358080",  // Update ID of event
      "T": 1694687965940999       // Engine timestamp in microseconds
    }
    

## [](#tag/Streams/Public/Depth)Depth

Contains incremental depth updates. Each depth update has the absolute value of the depths at the given levels, and only changes when the depth has changed.

To obtain an initial snapshot of the depth, the client should query the [REST API](https://docs.backpack.exchange/#tag/Markets/operation/get_depth).

The depth stream will push updates as quickly as possible, but under load it may aggregate more than one update into a single event. In this case the `U` and `u` fields will not be the same. The `U` field is the first update ID in the event, and the `u` field is the final update ID in the event.

There are alternative depth streams that aggregates updates into a single message over a 200ms, 600ms or 1000ms period instead of pushing updates in realtime. This is useful for reducing network traffic.

Updates are sequential, so `U` will always be `u + 1` from the previous message. If this is not the case, the client should assume that the depth has been invalidated and requery the REST API.

Stream name format: `depth.<symbol>` (realtime) Stream name format: `depth.200ms.<symbol>` (aggregated) Stream name format: `depth.600ms.<symbol>` (aggregated) Stream name format: `depth.1000ms.<symbol>` (aggregated)
    
    
    {
      "e": "depth",           // Event type
      "E": 1694687965941000,  // Event time in microseconds
      "s": "SOL_USDC",        // Symbol
      "a": [                  // Asks
        [
          "18.70",
          "0.000"
        ]
      ],
      "b": [                  // Bids
        [
          "18.67",
          "0.832"
        ],
        [
          "18.68",
          "0.000"
        ]
      ],
      "U": 94978271,          // First update ID in event
      "u": 94978271,          // Last update ID in event
      "T": 1694687965940999   // Engine timestamp in microseconds
    }
    

## [](#tag/Streams/Public/K-Line)K-Line

Stream name format: `kline.<interval>.<symbol>`
    
    
    {
      "e": "kline",                   // Event type
      "E": 1694687692980000,          // Event time in microseconds
      "s": "SOL_USD",                 // Symbol
      "t": "2024-09-11T12:00:00",     // K-Line start time (ISO 8601 format)
      "T": "2024-09-11T12:01:00",     // K-Line close time (ISO 8601 format)
      "o": "18.75",                   // Open price
      "c": "19.25",                   // Close price
      "h": "19.80",                   // High price
      "l": "18.50",                   // Low price
      "v": "32123",                   // Base asset volume
      "n": 93828,                     // Number of trades
      "X": false                      // Is this k-line closed?
    }
    

## [](#tag/Streams/Public/Liquidation)Liquidation

Contains updates for liquidation events for all liquidation types.

Stream name format: `liquidation`
    
    
    {
      "e": "liquidation",         // Event type
      "E": 1694688638091000,      // Event time in microseconds
      "q": "10",                  // Quantity
      "p": "18.70",               // Price
      "S": "Bid",                 // Side
      "s": "SOL_USDC",            // Symbol
      "T": 567,                   // Engine timestamp in microseconds
    }
    

## [](#tag/Streams/Public/Mark-price)Mark price

Stream name format: `markPrice.<symbol>`
    
    
    {
      "e": "markPrice",           // Event type
      "E": 1694687965941000,      // Event time in microseconds
      "s": "SOL_USDC",            // Symbol
      "p": "18.70",               // Mark price
      "f": "1.70",                // Estimated funding rate. Not included for prediction markets
      "i": "19.70",               // Index price. Not included for prediction markets
      "n": 1694687965941,         // Next funding timestamp in milliseconds. Not included for prediction markets
      "T": 1694687965940999       // Engine timestamp in microseconds
    }
    

## [](#tag/Streams/Public/Ticker)Ticker

The ticker stream pushes 24hr rolling statistics for a single symbol every second.

Stream name format: `ticker.<symbol>`
    
    
    {
      "e": "ticker",          // Event type
      "E": 1694687692980000,  // Event time in microseconds
      "s": "SOL_USD",         // Symbol
      "o": "18.75",           // First price
      "c": "19.24",           // Last price
      "h": "19.80",           // High price
      "l": "18.50",           // Low price
      "v": "32123",           // Base asset volume
      "V": "928190",          // Quote asset volume
      "n": 93828              // Number of trades
    }
    

## [](#tag/Streams/Public/Open-interest)Open interest

Open interest updates are pushed to the openInterest stream every 60 seconds.

Stream name format: `openInterest.<symbol>`
    
    
    {
      "e": "openInterest",          // Event type
      "E": 1694687965941000,        // Event time in microseconds
      "s": "SOL_USDC_PERP",         // Symbol
      "o": "100",                   // Open interest in contracts
    }
    

## [](#tag/Streams/Public/Trade)Trade

Contains public trade data for a single symbol. The trade ID is a sequential number specific to the symbol. This stream includes updates for trades executed as a result of liquidations.

Stream name format: `trade.<symbol>`
    
    
    {
      "e": "trade",                   // Event type
      "E": 1694688638091000,          // Event time in microseconds
      "s": "SOL_USDC",                // Symbol
      "p": "18.68",                   // Price
      "q": "0.122",                   // Quantity
      "b": "111063114377265150",      // Buyer order ID
      "a": "111063114585735170",      // Seller order ID
      "t": 12345,                     // Trade ID
      "T": 1694688638089000,          // Engine timestamp in microseconds
      "m": true                       // Is the buyer the maker?
    }
    
