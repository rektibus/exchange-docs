# Ascendex API Documentation

Auto-fetched from 2 page(s)


---

# Source: https://ascendex.github.io/ascendex-pro-api-v2/

ERROR: Failed to fetch: 404 Client Error: Not Found for url: https://ascendex.github.io/ascendex-pro-api-v2/


---

# Source: https://ascendex.github.io/ascendex-futures-pro-api-v2/

[ NAV  ](#)

[ ](https://ascendex.com)

[Cash/Margin APIs](https://ascendex.github.io/ascendex-pro-api/) [Futures APIs](https://ascendex.github.io/ascendex-futures-pro-api-v2/)

[shell](#) [python](#) [java](#)



  * [Introducing Futures Pro (v2) APIs](#introducing-futures-pro-v2-apis)
    * [General](#general)
    * [Obtain API Keys](#obtain-api-keys)
    * [SDKs and Client Libraries](#sdks-and-client-libraries)
    * [Market Making Incentive Program](#market-making-incentive-program)
    * [Got Questions?](#got-questions)
    * [Change Log](#change-log)
  * [Futures Trading System Specification](#futures-trading-system-specification)
    * [Contract Position Notional (CPN)](#contract-position-notional-cpn)
    * [Margin Group](#margin-group)
    * [Total Margin](#total-margin)
    * [Group Collateral Balance](#group-collateral-balance)
    * [Position Initial/Maintenance Margin Rate](#position-initial-maintenance-margin-rate)
    * [Position Initial/Maintenance Margin](#position-initial-maintenance-margin)
    * [Liquidation Price](#liquidation-price)
    * [Unrealized PnL](#unrealized-pnl)
    * [Realized PnL](#realized-pnl)
  * [RESTful APIs](#restful-apis)
    * [Exchange Latency Info](#exchange-latency-info)
    * [General Info (Public)](#general-info-public)
      * [Futures Contracts Info](#futures-contracts-info)
      * [Futures Collateral Asset Info](#futures-collateral-asset-info)
    * [Market Data (Public)](#market-data-public)
      * [Futures Pricing Data](#futures-pricing-data)
      * [Bar Info](#bar-info)
      * [Historical Bar Data](#historical-bar-data)
      * [Ticker](#ticker)
    * [Authenticate a RESTful Request](#authenticate-a-restful-request)
      * [Create Request](#create-request)
      * [Sign a Request](#sign-a-request)
    * [Account Data](#account-data)
      * [Account Info](#account-info)
      * [VIP Fee Schedule](#vip-fee-schedule)
      * [Fee Schedule by Symbol](#fee-schedule-by-symbol)
      * [Risk Limit Info(Deprecated)](#risk-limit-info-deprecated)
      * [Risk Limit Info (v2)](#risk-limit-info-v2)
      * [Position](#position)
      * [Free Margin](#free-margin)
      * [Change Margin (for Isolated Positions)](#change-margin-for-isolated-positions)
      * [Change Margin Type](#change-margin-type)
      * [Change Contract Leverage](#change-contract-leverage)
      * [Deposit to the Futures Account](#deposit-to-the-futures-account)
      * [Withdraw from the Futures Account](#withdraw-from-the-futures-account)
      * [Funding Payment History](#funding-payment-history)
    * [Order](#order)
      * [Generate Order Id](#generate-order-id)
      * [New Order](#new-order)
      * [Place Batch Orders](#place-batch-orders)
      * [Cancel Order](#cancel-order)
      * [Cancel Batch Orders](#cancel-batch-orders)
      * [Cancel All Open Orders](#cancel-all-open-orders)
      * [List Open Orders](#list-open-orders)
      * [List Current History Orders](#list-current-history-orders)
      * [Query Order By ID](#query-order-by-id)
    * [Balance Snapshot And Update Detail](#balance-snapshot-and-update-detail)
      * [Futures Account Balance Snapshot](#futures-account-balance-snapshot)
      * [Futures Order and Balance Detail](#futures-order-and-balance-detail)
  * [WebSocket](#websocket)
    * [How to Connect](#how-to-connect)
    * [WebSocket Authentication](#websocket-authentication)
    * [Keep the Connection Alive](#keep-the-connection-alive)
    * [Public Stream Data](#public-stream-data)
      * [Channel: Futures Pricing Data](#channel-futures-pricing-data)
      * [Channel: Level 1 Order Book Data (BBO)](#channel-level-1-order-book-data-bbo)
      * [Channel: Level 2 Order Book Updates](#channel-level-2-order-book-updates)
      * [Channel: Market Trades](#channel-market-trades)
      * [Channel: Bar Data](#channel-bar-data)
    * [Private Stream Data](#private-stream-data)
      * [Channel: Order](#channel-order)
      * [Channel: Account Update](#channel-account-update)
    * [WebSocket - Data Request](#websocket-data-request)
      * [WS: Account Snapshot](#ws-account-snapshot)
      * [WS: Place Order](#ws-place-order)
      * [WS: Cancel Order](#ws-cancel-order)
      * [WS: Cancel All Orders](#ws-cancel-all-orders)
      * [WS: Query Open Orders](#ws-query-open-orders)
  * [Appendix](#appendix)
    * [ENUM Definitions](#enum-definitions)
      * [Account Category (`ac`)](#account-category-ac)
      * [Order Type (`orderType`)](#order-type-ordertype)
      * [Side (`side`)](#side-side)
      * [Response Type (`respInst`)](#response-type-respinst)
      * [Time in Force (`timeInForce`)](#time-in-force-timeinforce)
      * [Execution Instruction (`execInst`)](#execution-instruction-execinst)
      * [Order Status (`status`)](#order-status-status)
      * [Margin Type (`marginType`)](#margin-type-margintype)
      * [WebSocket Operations (`op`)](#websocket-operations-op)
      * [WebSocket Message Types (`m`)](#websocket-message-types-m)


  * [Sign Up for ascendex.com](https://ascendex.com)



# Introducing Futures Pro (v2) APIs

## General

**Mainnet** URL: [https://ascendex.com](https://ascendex.com/)

**Testnet**

Testnet URL: [https://api-test.ascendex-sandbox.com](https://api-test.ascendex-sandbox.com/)

You are free to register one or more accounts in the testnet. You can use the magic code **888888** to bypass all verification code checks (email verification, phone number verification, two-step authentication, etc.).

You accounts will automatically receive initial funding. 

Please expect the testnet to be reset every a few days. 

## Obtain API Keys

Prior to use API, you need to login the website to create API Key with proper permissions. The API key is shared for all instruments in AscendEx including cash, margin and futures.

You can create and manage your API Keys [here](https://ascendex.com/en/account/api-key).

Every user can create up to 10 API Keys, each can be applied with either permission below:

  * **View permission** : It is used to query the data, such as order query, trade query.
  * **Trade permission** : It is used to place order, cancel order and transfer, etc.
  * **Transfer permission** : It is used to create/cancel asset transfer order, etc.



Please remember below information after creation:

  * **Access Key** is used in API request
  * **Secret Key** is used to generate the signature (only visible once after creation)
  * The API Key can bind maximum 20 IP addresses (either host IP or network IP), we strongly suggest you bind IP address for security purpose. The API Key without IP binding will be expired after 90 days.



## SDKs and Client Libraries

**Official SDK**

**CCXT** is our authorized SDK provider and you may access the AscendEX API through CCXT. For more information, please visit: <https://ccxt.trade>

**Demo Code**

Python Demo: <https://github.com/ascendex/ascendex-futures-api-demo-v2>

## Market Making Incentive Program

AscendEX offers a Market Making Incentive Program for professional liquidity providers. Key benefits of this program include:

  * Favorable fee structure.
  * Monthly bonus pending satisfying KPI.
  * Direct Market Access and Co-location service.



Users with good maker strategies and significant trading volume are welcome to participate in this long-term program. If your account has a trading volume of more than 150,000,000 USDT in the last 30 days on any exchange, please send the following information via email to institution@ascendex.com, with the subject "Market Maker Incentive Application":

  * One AscendEX account ID.
  * A brief explanation of your market making method (NO detail is needed), as well as estimation of maker orders' percentage.



## Got Questions?

Join our official telegram channel: <https://t.me/AscendEX_Official_API>

## Change Log

**2022-08-16**

[Funding Payment History](#funding-payment-history) added to get account funding payment history.

**2022-05-19**

[Limit Info API](#risk-limit-info) is deprecated, use [Limit Info API v2](#risk-limit-info-v2) to get ban info and message threshold info.

**2022-02-28**

  * Added the [Limit Info API](#risk-limit-info) to get ban info and risk limit info.



**2021-11-22**

  * Added the [ticker API](#ticker) for futures contracts.
  * Added the [VIP fee schedule API](#vip-fee-schedule) and the [Fee Schedule by Symbol API](#fee-schedule-by-symbol).



**2021-03-18**

  * Added WebSocket [_Query Open Orders_](#ws-query-open-orders) API.



**2021-03-03**

  * Fixed bug of cancelling a filled order with empty fields error response.
  * Added _symbol_ to error response from WebSocket [_Place Order_](#ws-place-order).
  * Updated _nextFundingTime_ value in RESTful [_Futures Pricing Data_](#futures-pricing-data) response.
  * Updated nextFundingTime _f_ value in WebSocket [_Futures Pricing Data_](#channel-futures-pricing-data) message.
  * Added error response demo in [_Place New Order_](#new-order).
  * Added error response demo in [_Place Batch Orders_](#place-batch-orders).
  * Fixed bug in [_Cancel All Open Orders_](#cancel-all-open-orders) when no data is passed in request body.
  * Fixed bug of _URL Not Found_ in [_Account Info_](#account-info).
  * Added _openInterest_ in [_Futures Pricing Data_](#futures-pricing-data)
  * Added _oi_ (open interest) in [_Channel: Futures Pricing Data_](#channel-futures-pricing-data)



**2021-02-26**

  * Updated _respInst_ field requirement in [_Place Batch Orders_](#place-batch-orders).
  * Updated _respInst_ field explanation in [_Place New Order_](#new-order).



**2021-02-25**

  * Updated _id_ field requirement in WebSocket [_Place Order_](#ws-place-order) request.



**2021-02-23**

  * Removed collapseDecimals field from [_Futures Contracts Info_](#futures-contracts-info) response.



**2021-02-22**

  * Added RESTful [_Current Order History_](#list-current-history-orders) API.



**2021-02-21**

  * Added [_Order Id Generate Algorithm_](#generate-order-id).
  * Added RESTful [_Place Batch Orders_](#place-batch-orders) API.
  * Added RESTful [_Cancel Batch Orders_](#cancel-batch-orders) API.
  * Added RESTful [_Query Order By ID_](#query-order-by-id) API.



**2021-02-19**

  * Added WebSocket [_Account Snapshot_](#ws-account-snapshot) API.
  * Added WebSocket [_Place Order_](#ws-place-order) API.
  * Added WebSocket [_Cancel Order_](#ws-cancel-order) API.
  * Added WebSocket [_Cancel All Orders_](#ws-cancel-all-orders) API.



**2021-02-18**

  * Replaced `baseAsset` and `quoteAsset` with `settlementAsset` in [_Futures Contract Info_](#futures-contracts-info) response.
  * Updated [_Account Info_](#account-info) API path.



# Futures Trading System Specification

### Contract Position Notional (CPN)

  * CPN = abs(position size * mark price) for the contract 



CPN is defined for each contract.

### Margin Group

**The Isolated Group**

The isolated group manages a single position with a certain amount of margin moved out of the crossed group. It isolates the risk of the position from other margin groups. Your maximum loss will be limited to the total margin moved into the isolated group.

Each account may have at most one isolated group per contract.

**The Crossed Group**

The crossed group manages all positions except those in isolated groups. 

### Total Margin

**For the isolated group**

Total margin is set by the user. You can find its value in the `isolatedMargin` field from the [Position](#position) endpoint. 

You can increase / decrease the total margin of the isolated margin group via the [Change Margin](#change-margin-for-isolated-positions) endpoint.

For the isolated group, we also refer to **total margin** as **isolated margin**.

**For the crossed group**

  * Total Margin = sum(Asset Balance * Reference Price * Collateral Discount Factor) for each collateral asset



Discount factor can be found in the `discountFactor` field from the [Futures Collateral Asset Info](#futures-collateral-asset-info) endpoint.

### Group Collateral Balance

**For the isolated group**

  * Group Collateral Balance = isolated margin + unrealized pnl of the isolated position



**For the crossed group**

  * Group Collateral Balance = total margin of the crossed group + total unrealized pnl of all positions in the crossed group



The **Group Collateral Balance** is important to determine the risk level of the margin group. If it becomes lower than the **position maintanence margin** , all positions in the margin group are expected to be liquidated. 

### Position Initial/Maintenance Margin Rate

Initial/Maintenance Margin Rate is system-specified for each position bracket and each contract. You may refer to the `marginRequirements` section from the [Futures Contract Info](#futures-contracts-info) endpoint for position brackets.

You should compare [Contract Position Notional (CPN)](#contract-position-notional-cpn) with each position bracket to determine your initial and maintenance margin rate.

### Position Initial/Maintenance Margin

**For the isolated group**

  * Position Initial Margin = CPN * Initial Margin Rate
  * Position Maintenance Margin = CPN * Maintenance Margin



**For the crossed group**

  * Position Initial Margin = sum(CPN * Initial Margin Rate) for each contract in the crossed group
  * Position Maintenance Margin = sum(CPN * Maintenance Margin Rate) for each contract in the crossed group



### Liquidation Price

  * V = Total Margin + Unrealized Pnl - Maintenance Margin



**For long positions**

  * R = abs(position size) * (1 - maintenance margin rate)
  * Liquidation Price = mark price - V / R



If the calculated liquidation price is negative, the position won't be liquidation even when the price becomes zero.

**For short positions**

  * R = abs(position size) * (1 + maintenance margin rate)
  * Liquidation Price = mark price + V / R



### Unrealized PnL

The **Unrealized PnL** of a position is calculated as:

  * Unrealized PnL = mark price * position + reference cost



Note that **position** and **reference cost** are of opposite signs.

The **Unrealized PnL** will be rolled (settled) when:

  * position is closed or flipped side (long becomes short, vice versa)
  * every 15 minutes AND abs(Unrealized Pnl) >= 10 USDT



Assume your current position is P, the current reference cost if RC, and unrealized PnL is L, after rolling:

  * position = P
  * reference cost = RC + L
  * realized PnL = 0 



You should always include the unrealized PnL when calculating the collateral balance. 

### Realized PnL

**Realized Pnl** is merely a bookkeeping entry for all profits and losses realized by the current position under the assumption that the position was built on an average cost basis. 

If you are mostly concerned about the risk of your positions, you can ignore the realized PnL. 

# RESTful APIs

### Exchange Latency Info

> Latency Info 
    
    
    curl -X GET https://ascendex.com/api/pro/v1/exchange-info?requestTime="$(date +%s%N | cut -b1-13)"
    

> Latency Info - Sample response::
    
    
    {
        "code": 0,
        "data":
        {
            "requestTimeEcho": 1640052379050,
            "requestReceiveAt": 1640052379063,
            "latency": 13
        }
    }
    

**HTTP Request**

`GET /api/pro/v1/exchange-info`

#### Request Parameters

Name | Type | Required | Value Range | Description  
---|---|---|---|---  
requestTime | Long | Yes | milliseconds since UNIX epoch in UTC | the client's local time. The server compare it with the system time to calculate latency.  
  
## General Info (Public)

### Futures Contracts Info

> Response - Futures Contracts Info
    
    
    {
        "code": 0,
        "data": [
            {
                "symbol"          : "BTC-PERP",
                "status"          : "Normal",
                "displayName"     : "BTCUSDT",    // the name displayed on the webpage
                "settlementAsset" : "USDT",       // settlement asset
                "underlying"      : "BTC/USDT",
                "tradingStartTime": 1579701600000,
                "priceFilter": {
                    "minPrice"  : "0.25",     // the order price cannot be smaller than the minPrice
                    "maxPrice"  : "1000000",  // the order price cannot be greater than the maxPrice
                    "tickSize"  : "0.25"      // the order price must be a multiple of the tickSize
                },
                "lotSizeFilter": {
                    "minQty"  : "0.0001",     // the order quantity cannot be smaller than the minQty
                    "maxQty"  : "1000000000", // the order quantity cannot be greater than the maxQty
                    "lotSize" : "0.0001"      // the order quantity must be a multiple of the lotSize
                },
                "marginRequirements": [
                    {
                        "positionNotionalLowerbound": "0",     // position lower bound
                        "positionNotionalUpperbound": "50000", // position upper bound
                        "initialMarginRate"         : "0.01",  // initial margin rate
                        "maintenanceMarginRate"     : "0.006"  // maintenance margin rate
                    },
                    {
                        "positionNotionalLowerbound": "50000",
                        "positionNotionalUpperbound": "200000",
                        "initialMarginRate"         : "0.02",
                        "maintenanceMarginRate"     : "0.012"
                    }
                ]
            }
        ]
    }
    

Get information for all futures contracts.

**HTTP Request**

`GET /api/pro/v2/futures/contract`

**Response**

### Futures Collateral Asset Info

> Response - Futures Collateral Asset Info
    
    
    {
        "code": 0,
        "data": [
            {
                "asset"           : "BTC",
                "assetName"       : "Bitcoin",
                "conversionFactor": "0.995",
                "discountFactor"  : "0.98",
                "displayName"     : "BTC",
                "statusCode"      : "Normal"
            },
            {
                "asset"           : "USDT",
                "assetName"       : "Tether",
                "conversionFactor": "1",
                "discountFactor"  : "1",
                "displayName"     : "USDT",
                "statusCode"      : "Normal"
            },
            {
                "asset"           : "USDTR",
                "assetName"       : "Futures Reward Token",
                "conversionFactor": "1",
                "discountFactor"  : "1",
                "displayName"     : "USDTR",
                "statusCode"      : "NoTransaction"
            }
        ]
    }
    

Get information for all futures collateral assets.

**HTTP Request**

`GET /api/pro/v2/futures/collateral`

## Market Data (Public)

Anyone can access public market data via the API endpoints. No authentication is needed. 

### Futures Pricing Data

> Requesting pricing data for all futures contract
    
    
    {
        "code": 0,
        "data": {
            "contracts": [
                {
                    "symbol"         : "BTC-PERP",          // contract symbol
                    "time"           : 1614815005717,       // server time (UTC timestamp in milliseconds)
                    "fundingRate"    : "0.000564448",       // funding rate 
                    "indexPrice"     : "50657.35",          // index price of the underlying
                    "markPrice"      : "50667.130409723",   // mark price of the contract
                    "openInterest"   : "90.7366",           // funding rate
                    "nextFundingTime": 1614816000000        // next funding time (UTC timestamp in milliseconds)
                }
            ],
            "collaterals": [
                {
                    "asset": "USDTR",
                    "referencePrice": "1"
                },
                {
                    "asset": "USDC",
                    "referencePrice": "0.9994"
                },
                {
                    "asset": "ETH",
                    "referencePrice": "1582.3264074"
                },
                {
                    "asset": "PAX",
                    "referencePrice": "0.99645"
                },
                {
                    "asset": "BTC",
                    "referencePrice": "50636.14"
                },
                {
                    "asset": "USDT",
                    "referencePrice": "1"
                }
            ],
        }
    }
    

Get pricing data for all futures contracts. 

**HTTP Request**

`GET /api/pro/v2/futures/pricing-data`

### Bar Info

> Request 
    
    
    curl -X GET "https://ascendex.com/api/pro/v1/barhist/info"
    

> Sample response
    
    
    {
        "code": 0,
        "data": [
            {
                "name": "1",
                "intervalInMillis": 60000
            },
            {
                "name": "5",
                "intervalInMillis": 300000
            },
            {
                "name": "15",
                "intervalInMillis": 900000
            },
            {
                "name": "30",
                "intervalInMillis": 1800000
            },
            {
                "name": "60",
                "intervalInMillis": 3600000
            },
            {
                "name": "120",
                "intervalInMillis": 7200000
            },
            {
                "name": "240",
                "intervalInMillis": 14400000
            },
            {
                "name": "360",
                "intervalInMillis": 21600000
            },
            {
                "name": "720",
                "intervalInMillis": 43200000
            },
            {
                "name": "1d",
                "intervalInMillis": 86400000
            },
            {
                "name": "1w",
                "intervalInMillis": 604800000
            },
            {
                "name": "1m",
                "intervalInMillis": 2592000000
            }
        ]
    }
    

**HTTP Request**

`GET /api/pro/v1/barhist/info`

This API returns a list of all bar intervals supported by the server. 

#### Request Parameters

This API endpoint does not take any parameters. 

#### Resposne

Name | Type | Description  
---|---|---  
`name` | `String` | name of the interval  
`intervalInMillis` | `Long` | length of the interval  
  
Plesae note that the one-month bar (`1m`) always resets at the month start. The `intervalInMillis` value for the one-month `bar` is only indicative. 

The value in the `name` field should be your input to the [Historical Bar Data](#historical-bar-data) API.

### Historical Bar Data

> Request 
    
    
    curl -X GET "https://ascendex.com/api/pro/v1/barhist?symbol=BTC-PERP&interval=1"
    

> Sample response
    
    
    {
        "code": 0,
        "data":
        [
            {
                "m": "bar",
                "s": "BTC-PERP",
                "data":
                {
                    "i": "1",
                    "ts": 1637619240000,
                    "o": "56263",
                    "c": "56260",
                    "h": "56263",
                    "l": "56239",
                    "v": "0.0126"
                }
            },
            {
                "m": "bar",
                "s": "BTC-PERP",
                "data":
                {
                    "i": "1",
                    "ts": 1637619300000,
                    "o": "56243",
                    "c": "56243",
                    "h": "56243",
                    "l": "56243",
                    "v": "0.0001"
                }
            }
        ]
    }
    

#### HTTP Request

`GET /api/pro/v1/barhist`

This API returns a list of **bar** s, with each contains the open/close/high/low prices of a symbol for a specific time range. 

#### Request Parameters

Name | Type | Required | Description  
---|---|---|---  
`symbol` | `String` | Yes | e.g. `"BTC-PERP"`  
`interval` | `String` | Yes | a string representing the interval type.  
`to` | `Long` | No | UTC timestamp in milliseconds. If not provided, this field will be set to the current time.  
`from` | `Long` | No | UTC timestamp in milliseconds.  
`n` | `Int` | No | default 10, number of bars to be returned, this number will be capped at 500  
  
The requested time range is determined by three parameters - `to`, `from`, and `n` \- according to rules below:

  * `from`/`to` each specifies the start timestamp of the first/last bar. 
  * `to` is always honored. If not provided, this field will be set to the current system time. 
  * For `from` and `to`: 
    * if only `from` is provided, then the request range is determined by `[from, to]`, inclusive. However, if the range is too wide, the server will increase `from` so the number of bars in the response won't exceed 500. 
    * if only `n` is provided, then the server will return the most recent `n` data bars to time `to`. However, if `n` is greater than 500, only 500 bars will be returned. 
    * if both `from` and `n` are specified, the server will pick one that returns fewer bars. 



#### Response

Name | Type | value | Description  
---|---|---|---  
`m` | String | `bar` | message type  
`s` | String |  | symbol  
`data:ts` | Long |  | bar start time in milliseconds  
`i` | String |  | interval  
`o` | String |  | open price  
`c` | String |  | close price  
`h` | String |  | high price  
`l` | String |  | low price  
`v` | String |  | volume in quote asset  
  
#### Code Sample

Please refer python code to [get bar history]{https://github.com/ascendex/ascendex-pro-api-demo/blob/main/python/query_pub_barhist.py}

### Ticker

> Ticker for one trading pair
    
    
    // curl -X GET 'https://ascendex.com/api/pro/v2/futures/ticker?symbol=BTC-PERP'
    {
        "code": 0,
        "data":
        {
            "symbol":  "BTC-PERP",
            "open":    "59488",
            "close":   "56725",
            "high":    "59724",
            "low":     "56672",
            "baseVol": "208.7414",
            "ask":
            [
                "56730",
                "0.0005"
            ],
            "bid":
            [
                "56710",
                "0.0042"
            ]
        }
    }
    

> List of Tickers for one or multiple trading pairs
    
    
    // curl -X GET "https://ascendex.com/api/pro/v2/futures/ticker?symbol=BTC-PERP,"
    {
        "code": 0,
        "data":
        [
            {
                "symbol":  "BTC-PERP",
                "open":    "59488",
                "close":   "56716",
                "high":    "59724",
                "low":     "56672",
                "baseVol": "208.7414",
                "ask":
                [
                    "56720",
                    "0.2315"
                ],
                "bid":
                [
                    "56712",
                    "0.0024"
                ]
            }
        ]
    }
    

#### HTTP Request

`GET api/pro/v2/futures/ticker`

You can get summary statistics of one or multiple symbols (spot market) with this API. 

#### Request Parameters

Name | Type | Required | Value Range | Description  
---|---|---|---|---  
`symbol` | `String` | No |  | you may specify one, multiple, or all symbols of interest. See below.  
  
This API endpoint accepts one optional string field `symbol`: 

  * If you do not specify `symbol`, the API will responde with tickers of all symbols in a list. 
  * If you set `symbol` to be a single symbol, such as `ASD/USDT`, the API will respond with the ticker of the target symbol as an object. If you want to wrap the object in a one-element list, append a comma to the symbol, e.g. `ASD/USDT,`.
  * You shall specify `symbol` as a comma separated symbol list, e.g. `ASD/USDT,BTC/USDT`. The API will respond with a list of tickers. 



#### Respond Content

The API will respond with a ticker object or a list of ticker objects, depending on how you set the `symbol` parameter. 

Each ticker object contains the following fields:

Field | Type | Description  
---|---|---  
`symbol` | `String` |   
`open` | `String` | the traded price 24 hour ago  
`close` | `String` | the last traded price  
`high` | `String` | the highest price over the past 24 hours  
`low` | `String` | the lowest price over the past 24 hours  
`volume` | `String` | the total traded volume in quote asset over the paste 24 hours  
`ask` | `[String, String]` | the price and size at the current best ask level  
`bid` | `[String, String]` | the price and size at the current best bid level  
  
#### Code Sample

Please refer to python code to [query ticker info]{https://github.com/ascendex/ascendex-pro-api-demo/blob/main/python/query_pub_ticker.py}

## Authenticate a RESTful Request

### Create Request

To access private data via RESTful APIs, you must include the following headers:

  * `x-auth-key` \- required, the api key as a string. 
  * `x-auth-timestamp` \- required, the UTC timestamp in milliseconds of your request
  * `x-auth-signature` \- required, the request signature (see [Sign a Request](#sign-a-request))



The timestamp in the header will be checked against server time. If the difference is greater than 30 seconds, the request will be rejected. 

### Sign a Request

> Signing a RESTful Request
    
    
    # bash 
    APIPATH=info
    APIKEY=CEcrjGyipqt0OflgdQQSRGdrDXdDUY2x
    SECRET=hV8FgjyJtpvVeAcMAgzgAFQCN36wmbWuN7o3WPcYcYhFd8qvE43gzFGVsFcCqMNk
    TIMESTAMP=`date +%s%N | cut -c -13` # 1608133910000
    MESSAGE=$TIMESTAMP+$APIPATH
    SIGNATURE=`echo -n $MESSAGE | openssl dgst -sha256 -hmac $SECRET -binary | base64`
    echo $SIGNATURE  # /pwaAgWZQ1Xd/J4yZ4ReHSPQxd3ORP/YR8TvAttqqYM=
    
    curl -X GET -i \
      -H "Accept: application/json" \
      -H "Content-Type: application/json" \
      -H "x-auth-key: $APIKEY" \
      -H "x-auth-signature: $SIGNATURE" \
      -H "x-auth-timestamp: $TIMESTAMP" \
      https://ascendex.com/api/pro/v1/info
    
    
    
    # python 3.6+
    import time, hmac, hashlib, base64
    
    api_path  = "info"
    api_key   = "CEcrjGyipqt0OflgdQQSRGdrDXdDUY2x"
    sec_key   = "hV8FgjyJtpvVeAcMAgzgAFQCN36wmbWuN7o3WPcYcYhFd8qvE43gzFGVsFcCqMNk"
    timestamp = int(round(time.time() * 1e3)) # 1608133910000
    
    message = bytes(f"{timestamp}+{api_path}", 'utf-8')
    secret = bytes(sec_key, 'utf-8')
    
    signature = base64.b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())
    
    header = {
      "x-auth-key": api_key,
      "x-auth-signature": signature, 
      "x-auth-timestamp": timestamp,
    }
    print(signature)  # b'/pwaAgWZQ1Xd/J4yZ4ReHSPQxd3ORP/YR8TvAttqqYM='
    
    
    
    // java 1.8+
    import javax.crypto.Mac;
    import javax.crypto.spec.SecretKeySpec;
    import org.apache.commons.codec.binary.Base64;
    
    public class SignatureExample {
    
      public static void main(String[] args) {
        try {
          long timestamp = System.currentTimeMillis(); // 1562952827927
          String api_path = "user/info";
          String secret = "hV8FgjyJtpvVeAcMAgzgAFQCN36wmbWuN7o3WPcYcYhFd8qvE43gzFGVsFcCqMNk";
          String message = timestamp + "+" + api_path;
    
          Mac sha256_HMAC = Mac.getInstance("HmacSHA256");
          SecretKeySpec secret_key = new SecretKeySpec(secret.getBytes(), "HmacSHA256");
          sha256_HMAC.init(secret_key);
    
          String hash = Base64.encodeBase64String(sha256_HMAC.doFinal(message.getBytes()));
          System.out.println(hash); // vBZf8OQuiTJIVbNpNHGY3zcUsK5gJpwb5lgCgarpxYI=
        }
        catch (Exception e) {
          System.out.println("Error");
        }
      }
    }
    

To query APIs with private data, you must include a signature using base64 encoded HMAC sha256 algorithm. The prehash string is `<timestamp>+<api-path>`. The `timestamp` is the UTC timestamp in milliseconds. The `api-path` is provided in each API description.

See the code demos in (`bash`/`python`/`java`) on the right.

## Account Data

### Account Info

> Account Info - Sample response:
    
    
    {
        "code": 0,
        "data": {
            "accountGroup": 0,
            "email": "yyzzxxz@gmail.com",
            "expireTime": 1604620800000,         // expire time, UTC timestamp in milliseconds. If -1, the api key will not expire
            "allowedIps": ["123.123.123.123"],
            "cashAccount": [
                "sample-cash-account-id"
            ],
            "marginAccount": [
                "sample-margin-account-id"
            ],
            "futuresAccount": [
                "sample-futures-account-id"
            ],
            "userUID":            "U0866943712",
            "tradePermission":     true,
            "transferPermission":  true,
            "viewPermission":      true,
            "limitQuota":          1000
        }
    }
    

**HTTP Request**

`GET /api/pro/v2/account/info`

**Signature**

You should sign the message in header as specified in [**Authenticate a RESTful Request**](#sign-a-request) section.

**prehash string**

`<timestamp>+v2/account/info`

Obtain the account information. 

You can obtain your `accountGroup` from this API, which you will need to include in the URL for all your private RESTful requests.

#### Response Content

Name | Type | Description  
---|---|---  
accountGroup | Int | non-negative integer  
email | String |   
expireTime | Long | the time when the API key will be expired (UTC timestamp in milliseconds). If -1, the api key will not expire  
allowedIps | List[String] | list of IPs allowed for the api key  
cashAccount | List[String] |   
marginAccount | List[String] |   
tradePermission | Boolean |   
transferPermission | Boolean |   
viewPermission | Boolean |   
userUID | String | an unique id associated with user  
  
See a demo at [query private account info](https://github.com/ascendex/ascendex-pro-api-demo/blob/main/python/query_prv_account_info.py).

### VIP Fee Schedule

> Fee Schedule - Sample response for general info::
    
    
    {
        "code": 0,
        "data":
        {
            "domain": "futures",
            "userUID": "U0866943712",
            "vipLevel": 0,
            "genericFee":
            {
                "largeCap":
                {
                    "maker": "0.00085",
                    "taker": "0.00085"
                },
                "smallCap":
                {
                    "maker": "0.001",
                    "taker": "0.001"
                }
            }
        }
    }
    

**HTTP Request**

`GET <account-group>/api/pro/v1/futures/fee/info`

**Signature**

You should sign the message in header as specified in [**Authenticate a RESTful Request**](#sign-a-request) section.

**prehash string**

`<timestamp>+fee/info`

See a demo at [query fee](https://github.com/ascendex/ascendex-pro-api-demo/blob/main/python/query_fee.py).

### Fee Schedule by Symbol

> Fee Schedule - Sample response for each symbol::
    
    
    {
        "code": 0,
        "data":
        {
            "domain": "futures",
            "userUID": "U0866943712",
            "vipLevel": 0,
            "productFee":
            [
                {
                    "fee":
                    {
                        "maker": "0.0001",
                        "taker": "0.0001"
                    },
                    "symbol": "BTC-PERP"
                },
                {
                    "fee":
                    {
                        "maker": "0.0001",
                        "taker": "0.0001"
                    },
                    "symbol": "ETH-PERP"
                }
            ]
        }
    }
    

**HTTP Request**

`GET <account-group>/api/pro/v1/futures/fee`

**Signature**

You should sign the message in header as specified in [**Authenticate a RESTful Request**](#sign-a-request) section.

**prehash string**

`<timestamp>+fee`

See a demo at [query fee](https://github.com/ascendex/ascendex-pro-api-demo/blob/main/python/query_fee.py).

### Risk Limit Info(Deprecated)

This API has been deprecated, please use [risk limit info v2](#risk-limit-info-v2) instead.

> Risk Limit Info
    
    
    curl -X GET https://ascendex.com/api/pro/v1/risk-limit-info"
    

> Risk Limit Info - Sample response::
    
    
    {
      "code": 0,
      "data": {
        "ip": "0.0.0.0",
        "webSocket": {
          "windowSizeInMinutes": 5,
          "maxNumRequests": 45,
          "maxSessionPerIp": 30,
          "isBanned": true,
          "bannedUntil": 1644807691158,
          "violationCode": 100014,
          "reason": "exceeds MAX_REQ_COUNT_PER_IP[45], 49 requests recently"
        }
      }
    }
    

**HTTP Request**

`GET /api/pro/v1/risk-limit-info`

#### Request Parameters

Name | Type | Required | Value Range | Description  
---|---|---|---|---  
ip | String | No | valid ip address | the client's ip address to be checked if it is banned due to violation of risk limits.  
  
### Risk Limit Info (v2)

> Risk Limit Info v2

Our message thresholds in web socket are based on `op` field and `action` field. Each threshold will have two levels, which are based on counts of messages received in `1` minute. If level 1 threshold is violated, this type of messages will be ignored in the following 15 minutes, other functions are not affected. If you keep sending these messages and triggered level 2 threshold, the violated WebSocket session will be killed and this ip will be banned for 15 minutes. Currently, We have following threshold groups:

  * `admin op`, includes `auth/ping/pong`

  * `stream op`, includes `sub/unsub`

  * `req op`, includes all `req` op, but `order req` and `snapshot req` have their own thresholds

    * `order req`, includes `place_order/cancel_order/cancel_all`
    * `snapshot req`, includes `depth_snapshot/depth_snapshot_top100`



All the operations fall into same `op`/`req` group will share a threshold, meaning the sum of count of these messages should not violate the threshold.

For `req op`, we have two fine granularity threshold `order req` and `snapshot req`, which will have their specialized threshold value for messages belonging to their types.
    
    
    curl -X GET https://ascendex.com/api/pro/v2/risk-limit-info"
    

> Risk Limit Info - Sample response::
    
    
    {
      "code": 0,
      "data": {
        "ip": "173.123.133.23",
        "webSocket": {
          "status": {
            "isBanned": false,
            "bannedUntil": -1,
            "violationCode": 0,
            "reason": ""
          },
          "limits": {
            "maxWebSocketSessionsPerIpAccountGroup": 20,
            "maxWebSocketSessionsPerIpTotal": 300
          },
          "messageThreshold": {
            "level1OpThreshold": {
              "auth": 800,
              "ping": 800,
              "pong": 800,
              "sub": 150,
              "unsub": 150,
              "req": 10000
            },
            "level2OpThreshold": {
              "auth": 1000,
              "ping": 1000,
              "pong": 1000,
              "sub": 200,
              "unsub": 200,
              "req": 10000
            },
            "level1ReqThreshold": {
              "place_order": 8000,
              "cancel_order": 8000,
              "cancel_all": 8000,
              "batch_place_order": 10000,
              "batch_cancel_order": 10000,
              "depth_snapshot": 400,
              "depth_snapshot_top100": 400,
              "market_trades": 10000,
              "balance": 10000,
              "open_order": 10000,
              "margin_risk": 10000,
              "futures_account_snapshot": 10000,
              "futures_open_orders": 10000
            },
            "level2ReqThreshold": {
              "place_order": 10000,
              "cancel_order": 10000,
              "cancel_all": 10000,
              "batch_place_order": 10000,
              "batch_cancel_order": 10000,
              "depth_snapshot": 500,
              "depth_snapshot_top100": 500,
              "market_trades": 10000,
              "balance": 10000,
              "open_order": 10000,
              "margin_risk": 10000,
              "futures_account_snapshot": 10000,
              "futures_open_orders": 10000
            }
          }
        }
      }
    }
    

**HTTP Request**

`GET /api/pro/v2/risk-limit-info`

#### Request Parameters

Name | Type | Required | Value Range | Description  
---|---|---|---|---  
ip | String | No | valid ip address | the client's ip address to be checked if it is banned due to violation of risk limits.  
  
### Position

> Response
    
    
    {
        "code": 0,
        "data": {
            "ac"             : "FUTURES",                   // account category
            "accountId"      : "sample-futures-account-id", // account ID
            "collaterals": [
                {
                    "asset"         : "ETH",          // collateral asset 
                    "balance"       : "100",          // balance 
                    "discountFactor": "0.95",         // discount factor
                    "referencePrice": "481.79793092"  // reference price (quote in USDT)
                },
                {
                    "asset"         : "BTC",
                    "balance"       : "10",
                    "discountFactor": "0.98",
                    "referencePrice": "17600.095"
                },
                {
                    "asset"         : "USDT",
                    "balance"       : "10000",
                    "discountFactor": "1",
                    "referencePrice": "1"
                }
            ],
            "contracts": [
                {
                    "symbol"               : "BTC-PERP",     // contract symbol
                    "side"                 : "LONG",         // side
                    "position"             : "0.5",          // positive for long position and negative for short position
                    "referenceCost"        : "-16800",       // reference cost
                    "unrealizedPnl"        : "0",            // unrealized pnl 
                    "realizedPnl"          : "0",            // realized pnl
                    "avgOpenPrice"         : "0",            // Average Opening Price
                    "marginType"           : "cross",        // margin type: isolated / cross
                    "isolatedMargin"       : "0",            // isolated margin
                    "leverage"             : "10",           // leverage
                    "takeProfitPrice"      : "0",            // take profit price (by position exit order)
                    "takeProfitTrigger"    : "market",       // take profit trigger (by position exit order)
                    "stopLossPrice"        : "0",            // stop loss price (by position exit order)
                    "stopLossTrigger"      : "market",       // stop loss trigger (by position exit order)
                    "buyOpenOrderNotional" : "1362.419625",  // buy open order notional
                    "sellOpenOrderNotional": "0",            // sell open order notional
                    "indexPrice"           : "17600.095",    // price of the contract's underlying product price
                    "markPrice"            : "-1"            // contract's mark price
                }
            ]
        }
    }
    

Get current position data - a full snapshot of your futures account. 

**HTTP Request**

`GET /<grp>/api/pro/v2/futures/position`

**Prehash String**

`<timestamp>+v2/futures/position`

### Free Margin

> Response
    
    
    {
      "code": 0,
      "data": {
        "collaterals": [
          {
            "asset": "BTC",              // collateral asset
            "availableForTransfer": "1"  // maximum amount allowed to be transferred out
          },
          {
            "asset": "USDT",
            "availableForTransfer": "10000"
          }
        ],
        "crossed": {
          "freeMargin": "30000"
        },
        "isolated": [
          {
            "freeMargin": "0",
            "symbol": "BTC-PERP"
          }
        ]
      }
    }
    

Get free margin for each margin group (crossed & isolated) and amount avaible for withdrawal for each collateral asset.

See [Change Margin](#change-margin-for-isolated-positions) on how to increase or decrease margin for the isolated position.

**HTTP Request**

`GET /<grp>/api/pro/v2/futures/free-margin`

**Prehash String**

`<timestamp>+v2/futures/free-margin`

### Change Margin (for Isolated Positions)

> Successful Response
    
    
    {
        "code": 0
    }
    

You can only change margin for isolated margin positions.

See [Free Margin](#free-margin) on the maximum amount you can increase / decrease the isolated margin.

**HTTP Request**

`POST /<grp>/api/pro/v2/futures/isolated-position-margin`

**Prehash String**

`<timestamp>+v2/futures/isolated-position-margin`

**Request Parameters**

PARAMETER | TYPE | REQUIRED | DESCRIPTION  
---|---|---|---  
symbol | String | Yes | e.g. `BTC-PERP`  
amount | String | Yes | margin amount in string type, e.g. "100". Set `amount` to positive will increase the isolated margin; set `amount`  
  
to a negative number will decrease the isolated margin. 

When you increase/decrease the isolated margin by a certain amount, the same amount X will be deducted/added from your USDT balance in the collateral. 

When you have non-USDT collateral assets, you may be able to increase the isolated margin by an amount more than your USDT balance. In which case, your USDT balance will become negative after the operation. 

### Change Margin Type

> Response
    
    
    {
        "code": 0
    }
    

You can change the margin type of a position:

  * crossed margin (`crossed`) 
  * isolated margin (`isolated`)



**HTTP Request**

`POST /<grp>/api/pro/v2/futures/margin-type`

**Prehash String**

`<timestamp>+v2/futures/margin-type`

**Request Parameters**

PARAMETER | TYPE | REQUIRED | DESCRIPTION  
---|---|---|---  
symbol | String | Yes | e.g. `BTC-PERP`  
[marginType](#margin-type-margintype) | ENUM | Yes | You can switch between two margin types: `isolated` and `crossed`  
  
### Change Contract Leverage

> Response
    
    
    {
        "code": 0,
        "data": {
            "leverage": 10,
            "symbol"  : "BTC-PERP"
        }
    }
    

**HTTP Request**

`POST /<grp>/api/pro/v2/futures/leverage`

**Request Parameters**

PARAMETER | TYPE | REQUIRED | DESCRIPTION  
---|---|---|---  
symbol | String | Yes | e.g. `BTC-PERP`  
leverage | Int | Yes | the leverage should be an integer between `1` and `100`  
  
### Deposit to the Futures Account

> Successful Response
    
    
    {
        "code": 0
    }
    

You can deposit collateral assets to your Futures account from your Cash account.

**HTTP Request**

`POST /<grp>/api/pro/v2/futures/transfer/deposit`

**Prehash String**

`<timestamp>+v2/futures/transfer/deposit`

**Request Parameters**

PARAMETER | TYPE | REQUIRED | DESCRIPTION  
---|---|---|---  
asset | String | Yes | e.g. `BTC`  
amount | String | Yes | the amount to deposit in string type, e.g. "1". Only positive value is allowed.  
  
### Withdraw from the Futures Account

> Successful Response
    
    
    {
        "code": 0
    }
    

You can withdraw collateral assets from your Futures account to your Cash account.

**HTTP Request**

`POST /<grp>/api/pro/v2/futures/transfer/withdraw`

**Prehash String**

`<timestamp>+v2/futures/transfer/withdraw`

**Request Parameters**

PARAMETER | TYPE | REQUIRED | DESCRIPTION  
---|---|---|---  
asset | String | Yes | e.g. `BTC`  
amount | String | Yes | the amount to withdraw in string type, e.g. "1". Only positive value is allowed.  
  
### Funding Payment History

> Response
    
    
    {
      "code": 0,
      "data": {
        "data": [
          {
            "fundingRate": "0.00003666",
            "paymentInUSDT": "-0.000142423",
            "symbol": "BTC-PERP",
            "timestamp": 1642780800000
          },
          {
            "fundingRate": "0.000109429",
            "paymentInUSDT": "-0.000428031",
            "symbol": "BTC-PERP",
            "timestamp": 1642752000000
          }
        ],
        "hasNext": true,
        "page": 1,
        "pageSize": 2
      }
    }
    

Get funding payment history of your account. 

**HTTP Request**

`GET /<grp>/api/pro/v2/futures/funding-payments`

**Prehash String**

`<timestamp>+v2/futures/funding-payments`

**Request Parameters**

Name | Type | Required | Description  
---|---|---|---  
`symbol` | String | No | e.g. `BTCUSDT`  
`page` | Int | No | page number, default 1  
`pageSize` | Int | No | size of the page, 1~100, default 20.  
  
**Code Sample**

Please refer to python code to [get funding history](https://github.com/ascendex/ascendex-futures-api-demo-v2/blob/main/cli/get-funding-history.py)

## Order

### Generate Order Id

We use the following method to generate an unique id for each order place/cancel request. (You could get `userUID` from `Account Info` API.)

**Method**

  * A = 'a' for order via rest api, or 's' for order via websocket;

  * B = Convert timestamp (in miliseconds) to hex string;

  * C = User UID (11 chars, starting with 'U' followed by 10 digits);

  * D = If user provide client order Id (with length >= 9, letters and digits only), then take the right 9 chars; otherwise, we randomly generate 9 chars;

  * Final order Id is concatenation of strings A, B, C, D from above steps, i.e., orderId = A + B + C + D.




**Extra info on`id`**

  * `id` value must satisfy regrex pattern `"^\w[\w\-]*\w$"` (i.e. start and end with word character), and with length up to 32. ("Invalid Client Order id" error for violation)

  * `id` value with length 9 is recommended, since we take the right most 9 chars for order Id generation.

  * `id` value with length < 9 will not be used in order Id generation, but we still echo it back in order ack message (empty string when no `id` value provided).

  * If a valid `id` value is provided when placing order, order Id from server side is pre-determined. This could be helpful for order status check in case of accidently internet connection issue.




**Code Sample**

Please refer to python code to [gen server order id](https://github.com/ascendex/ascendex-futures-api-demo-v2/blob/80942a5f2414a01c72d2ed660957a9e8d29a511e/cli/util.py#L82)

### New Order

> Successful Response
    
    
    {
        "code": 0,
        "data": {
            "meta": {
                "action"  : "place-order",
                "id"      : "abcd1234abcd1234",
                "respInst": "ACCEPT"   // ACK, ACCEPT, or DONE
            },
            "order": {
                "ac"          : "FUTURES",
                "accountId"   : "sample-futures-account-id",
                "seqNum"      : 14,    // sequence number, also -1 in ACK mode
                "time"        : 1605677683714,
                "orderId"     : "sample-order-id",
                "orderType"   : "Limit",
                "side"        : "Buy",
                "symbol"      : "BTC-PERP",
                "price"       : "9500",
                "orderQty"    : "0.1",
                "stopPrice"   : "0",
                "stopBy"      : "market",
                "status"      : "New",
                "lastExecTime": 1605677684479,
                "lastPx"      : "0",
                "lastQty"     : "0",
                "avgFilledPx" : "0",
                "cumFilledQty": "0",
                "fee"         : "0",
                "cumFee"      : "0",
                "feeAsset"    : "USDT",
                "errorCode"   : ""
            }
        }
    }
    

> Error Response
    
    
    {
        "ac": "FUTURES",
        "accountId": "sample-futures-account-id",
        "action": "place-order",
        "code": 300014,
        "info": {
            "id": "abcd1234abcd1234",
            "symbol": "BTC-PERP"
        },
        "message": "Order price doesn't conform to the required tick size: 1",
        "reason": "TICK_SIZE_VIOLATION"
    }
    

**HTTP Request**

`POST /<grp>/api/pro/v2/futures/order`

**Prehash String**

`<timestamp>+v2/futures/order`

**Request Parameters**

PARAMETER | TYPE | REQUIRED | DESCRIPTION  
---|---|---|---  
id | String |  | >=9 chars (letter and digit number only). Optional but recommended. We echo it back to help you match response with request. By setting this field, you can obtain the orderId before sending the request. It is also useful when you place order in batch mode.  
time | Long | Yes | Milliseconds since UNIX epoch in UTC. We do not process request placed more than 30 seconds ago.  
symbol | String | Yes | e.g. `BTC-PERP`  
orderPrice | String |  | Required for `Limit` and `StopLimit` orders  
orderQty | String | Yes | Order size. Please set scale properly for each symbol.  
[orderType](#order-type-ordertype) | ENUM | Yes |   
[side](#side-side) | ENUM | Yes |   
[respInst](#response-type-respinst) | ENUM |  | `ACK` for limit order and `Done` for market order by default  
postOnly | Boolean |  | `false` by default  
stopPrice | String |  | required for `StopLimit` and `StopMarket` orders  
[timeInForce](#time-in-force-timeinforce) | ENUM |  | `GTC` by default  
[execInst](#execution-instruction-execinst) | ENUM |  |   
posStopLossPrice | String |  | position stop loss price  
posTakeProfitPrice | String |  | position take profit price  
  
### Place Batch Orders

> Place Batch Orders - Request Body
    
    
    {
        "orders": [
                    {
                        "id"        : "sampleRequestId1",
                        "time"      : 1613878579169,
                        "symbol"    : "BTC-PERP",
                        "price"     : "34000",
                        "orderQty"  : "0.1",
                        "orderType" : "limit",
                        "side"      : "buy",
                        "respInst"  : "ACK"
                    },
                    {
                        "id"        : "sampleRequestId2",
                        "time"      : 1613878579169,
                        "symbol"    : "BTC-PERP",
                        "price"     : "35000",
                        "orderQty"  : "0.2",
                        "orderType" : "market",
                        "side"      : "buy",
                        "respInst"  : "ACK"
                    }
                  ]
    }
    

> Place Batch Orders - Successful ACK Response (Status 200, code 0)
    
    
    {
        "code": 0,
        "data": {
            "meta": {
                "action"  : "batch-place-order",
                "respInst": "ACK"
            },
            "orders": [
                {
                    "id"       : "sampleRequestId1",
                    "orderId"  : "a177c2a8cfe1U0123456789eqntvwWsy",
                    "orderType": "Limit",
                    "symbol"   : "BTC-PERP",
                    "timestamp": 1613878579202
                },
                {
                    "id"       : "sampleRequestId2",
                    "orderId"  : "a177c2a8cfe1U0123456789equestId2",
                    "orderType": "Market",
                    "symbol"   : "BTC-PERP",
                    "timestamp": 1613878579202
                }
            ]
        }
    }
    

> Error Response
    
    
    {
        "ac": "FUTURES",
        "accountId": "sample-futures-account-id",
        "action": "batch-place-order",
        "code": 300013,
        "info": [
            {
                "code": 300013,
                "id": "sampleRequestId1",
                "message": "Some invalid order in this batch.",
                "reason": "INVALID_BATCH_ORDER",
                "symbol": "BTC-PERP"
            },
            {
                "code": 320008,
                "id": "sampleRequestId2",
                "message": "Futures account exposure higher than system acceptable level.",
                "reason": "FUTURES_TOO_RISKY",
                "symbol": "BTC-PERP"
            }
        ],
        "message": "Batch Order failed, please check each order info for detail.",
        "reason": "INVALID_BATCH_ORDER"
    }
    

Place multiple orders in a batch. If any order(s) fails our basic check, the whole batch request will fail.

You may submit up to 10 orders at a time. Server will respond with error if you submit more than 10 orders.

**HTTP Request**

`POST /<grp>/api/pro/v2/futures/order/batch`

**Prehash String**

`<timestamp>+v2/futures/order/batch`

**Request Parameters**

Name | Data Type | Description  
---|---|---  
orders | List | List of order items  
  
please refer to [placing new order](#new-order) for order item definition.

**respInst** field is required for market order and only _ACK_ is allowed.

### Cancel Order

> Response
    
    
    {
        "code": 0,
        "data": {
            "meta": {
                "action"  : "cancel-order",       // action
                "id"      : "abcd1234abcd1234",   // user provided ID
                "respInst": "ACCEPT"              // response instruction
            },
            "order": {
                "ac"          : "FUTURES",                    // account category
                "accountId"   : "sample-futures-account-id",  // account ID
                "seqNum"      : 14,                           // sequence number
                "time"        : 1605677683714,                // order creation time (UTC time in milliseconds)
                "orderId"     : "sample-order-id",            // order ID
                "orderType"   : "Limit",                      // order type
                "side"        : "Buy",                        // side
                "symbol"      : "BTC-PERP",                   // contract symbol
                "price"       : "9500",                  // order price 
                "orderQty"    : "0.1",                        // order qty
                "stopPrice"   : "0",                          // stop price
                "stopBy"      : "market",                     // stop price trigger 
                "status"      : "Canceled",                   // order status
                "lastExecTime": 1605677684479,                // last execution time (UTC time in milliseconds)
                "lastPx"      : "0",                          // last filled price
                "lastQty"     : "0",                          // last filled quantity
                "avgFilledPx" : "0",                          // average filled price of all fills 
                "cumFilledQty": "0",                          // cummulative filled quantity
                "fee"         : "0",                          // fee of the last fill
                "cumFee"      : "0",                          // cummulative fee
                "feeAsset"    : "USDT",                       // fee asset
                "errorCode"   : ""                            // error code
            }
        }
    }
    

**HTTP Request**

`DELETE /<grp>/api/pro/v2/futures/order`

**Prehash String**

`<timestamp>+v2/futures/order`

**Request Parameters**

PARAMETER | TYPE | REQUIRED | DESCRIPTION  
---|---|---|---  
id | String |  | >=9 chars (letter and digit number only). Optional but recommended. We echo it back to help you match response with request. This is especially useful when you cancel in batch mode.  
orderId | String | Yes | 32 chars order id. You should set the value to be the orderId of the target order you want to cancel.  
symbol | String | Yes | Symbol of the order to cancel  
time | Long | Yes | milliseconds since UNIX epoch in UTC. We do not process request sent more than 30 seconds ago.  
[respInst](#response-type-respinst) | ENUM |  | `ACK` by default  
  
**Response**

_respInst_

### Cancel Batch Orders

> Cancel Batch Orders - Request Body
    
    
    {
       "orders":[
          {
             "id":"sampleRequestId1",
             "orderId":"a177c2a8cfe1U0123456789eqntvwWsy",
             "symbol":"BTC-PERP",
             "time":1613900544076
          },
          {
             "id":"sampleRequestId2",
             "orderId":"a177c2a8cfe1U0123456789equestId2",
             "symbol":"BTC-PERP",
             "time":1613900544076
          }
       ]
    }
    

> Cancel Batch Orders - Successful ACK Response (Status 200, code 0)
    
    
    {
       "code":0,
       "data":{
          "meta":{
             "action":"batch-cancel-order",
             "respInst":"ACK"
          },
          "orders":[
             {
                "id":"sampleRequestId1",
                "orderId":"a177c2a8cfe1U0123456789eqntvwWsy",
                "orderType":"",
                "symbol":"BTC-PERP",
                "timestamp":1613900544091
             },
             {
                "id":"sampleRequestId2",
                "orderId":"a177c2a8cfe1U0123456789equestId2",
                "orderType":"",
                "symbol":"BTC-PERP",
                "timestamp":1613900544168
             }
          ]
       }
    }
    

Cancel multiple orders in a batch. If any order(s) fails our basic check, the whole batch request will fail.

You may submit up to 10 orders to cancel at a time. Server will respond with error if you submit more than 10 orders.

**HTTP Request**

`DELETE /<grp>/api/pro/v2/futures/order/batch`

**Prehash String**

`<timestamp>+v2/futures/order/batch`

**Request Parameters**

Name | Data Type | Description  
---|---|---  
orders | List | List of order items to cancel  
  
please refer to [cancel order](#cancel-order) for order item definition

### Cancel All Open Orders

> Response
    
    
    {
        "code": 0
    }
    

**HTTP Request**

`DELETE /<grp>/api/pro/v2/futures/order/all`

**Prehash String**

`<timestamp>+v2/futures/order/all`

**Request Parameters**

PARAMETER | TYPE | REQUIRED | DESCRIPTION  
---|---|---|---  
symbol | String | No | the optional symbol filter  
  
### List Open Orders

> Response
    
    
    {
        "code": 0,
        "data": [
            {
                "ac"          : "FUTURES",                   // account category
                "accountId"   : "sample-futures-account-id", // account ID
                "seqNum"      : 14,                          // sequence number
                "time"        : 1605677683714,               // order creation time
                "orderId"     : "sample-order-id",           // order ID
                "orderType"   : "Limit",                     // order type
                "side"        : "Buy",                       // order side
                "symbol"      : "BTC-PERP",                  // contract symbol
                "price"       : "9500",                      // order price
                "orderQty"    : "0.1",                       // order quantity
                "stopPrice"   : "0",                         // stop price
                "stopBy"      : "market",                    // stop price trigger         
                "status"      : "New",                       // order status 
                "lastExecTime": 1605677684479,               // last execution time
                "lastPx"      : "0",                         // last filled price 
                "lastQty"     : "0",                         // last filled quantity
                "avgFilledPx" : "0",                         // average filled price of all fills
                "cumFilledQty": "0",                         // cummulative filled quantity
                "fee"         : "0",                         // fee of the last fill
                "cumFee"      : "0",                         // cummulative fee 
                "feeAsset"    : "USDT",                      // fee asset
                "errorCode"   : ""                           // error code
            }
        ]
    }
    

**HTTP Request**

`GET /<grp>/api/pro/v2/futures/order/open`

**Prehash String**

`<timestamp>+v2/futures/order/open`

### List Current History Orders

> Current History Orders - Request Body
    
    
    {
       "symbol":"BTC-PERP",
       "n":20,
       "executedOnly":true
    }
    

> Successful Response (Status 200, code 0)
    
    
    {
       "code":0,
       "data":[
          {
             "ac":"FUTURES",
             "accountId":"sampleFuturesAccountId",
             "avgFilledPx":"58501",
             "cumFee":"0.058501",
             "cumFilledQty":"0.001",
             "errorCode":"",
             "execInst":"NULL_VAL",
             "fee":"0.058501",
             "feeAsset":"USDT",
             "lastExecTime":1613992168196,
             "lastPx":"58501",
             "lastQty":"0.001",
             "orderId":"a177c29e4064U0123456789dVeUxlVyA",
             "orderQty":"0.001",
             "orderType":"Limit",
             "posStopLossPrice":"0",
             "posStopLossTrigger":"market",
             "posTakeProfitPrice":"0",
             "posTakeProfitTrigger":"market",
             "price"     :"59027",
             "seqNum":1041950,
             "side":"Buy",
             "status":"Filled",
             "stopBy":"market",
             "stopPrice":"0",
             "symbol":"BTC-PERP",
             "time":1613992168190
          },
          ...
       ]
    }
    

This API returns all current history orders for futures account.

**HTTP Request**

`GET <account-group>/api/pro/v2/futures/order/hist/current`

**Prehash String**

`<timestamp>+v2/futures/order/hist/current`

**Request Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | String | No | symbol filter, e.g. `"BTC-PERP"`  
n | Int | No | maximum number of orders to be included in the response  
executedOnly | Boolean | No | if `True`, include orders with non-zero filled quantities only.  
  
**Response**

Return a list of history orders in _" data"_ field.

### Query Order By ID

> Query order with single order id - Request Body
    
    
    {
       "orderId":"a177c29e4064U0123456789dVeUxlVyA"
    }
    

> Successful Response (Status 200, code 0)
    
    
    {
        "code"     : 0,
        "accountId": "sampleFuturesAccountId",
        "ac"       : "FUTURES",
        "data": {
            "ac"                  : "FUTURES",
            "accountId"           : "sampleFuturesAccountId",
            "avgFilledPx"         : "0",
            "cumFee"              : "0",
            "cumFilledQty"        : "0",
            "errorCode"           : "",
            "execInst"            : "NULL_VAL",
            "fee"                 : "0",
            "feeAsset"            : "USDT",
            "lastExecTime"        : 1613877923408,
            "lastPx"              : "0",
            "lastQty"             : "0",
            "orderId"             : "a177c29e4064U0123456789dVeUxlVyA",
            "orderQty"            : "0.1",
            "orderType"           : "Limit",
            "posStopLossPrice"    : "0",
            "posStopLossTrigger"  : "None",
            "posTakeProfitPrice"  : "0",
            "posTakeProfitTrigger": "None",
            "price"               : "34000",
            "seqNum"              : 18586710,
            "side"                : "Buy",
            "status"              : "New",
            "stopBy"              : "",
            "stopPrice"           : "0",
            "symbol"              : "BTC-PERP",
            "time"                : 1613877922641
        }
    }
    

> Query Order with multiple order ids - Request Body
    
    
    {
       "orderId":"a177c29e4064U0123456789dVeUxlVyA,a177c29e4064U0123456789dVeUxlVyB"
    }
    

> Successful Response (Status 200, code 0)
    
    
    {
        "code"     : 0,
        "accountId": "sampleFuturesAccountId",
        "ac"       : "FUTURES",
        "data": [
            {
                "ac"                  : "FUTURES",
                "accountId"           : "sampleFuturesAccountId",
                "orderId"             : "a177c29e4064U0123456789dVeUxlVyA",
                ...
            },
    {
                "ac"                  : "FUTURES",
                "accountId"           : "sampleFuturesAccountId",
                "orderId"             : "a177c29e4064U0123456789dVeUxlVyB",
                ...
            }
        ]
    }
    

**HTTP Request**

`GET /<grp>/api/pro/v2/futures/order/status`

**Prehash String**

`<timestamp>+v2/futures/order/status`

**Request Parameters**

PARAMETER | TYPE | REQUIRED | DESCRIPTION  
---|---|---|---  
orderId | String | Yes | a single order id, or multiple order ids separated by _,_  
  
The API will respond with a list of objects in the data field. Each object in the list contains information of a single order. There's one exception, if you use only a single orderId, the data field of the API response will be simplified to a single object. If you want the API to respond with a list of only one object in this case, add a comma (`,`) to the orderId.

## Balance Snapshot And Update Detail

Here we provide rest API to get daily balance snapshot, and intraday balance and order fills update details. We recommend calling balance snapshot endpoint(`futures/balance/snapshot`) to get balance at the beginning of the day, and get the sequence number `sn`; then start to query balance or order fills update from `futures/balance/history` by setting parameter `sn` value to be `sn + 1`.

Please note we enforce rate limit 8 / minute. Data query for most recent 7 days is supported.

### Futures Account Balance Snapshot

This API returns futures balance snapshot on daily basis.

#### HTTP Request

`GET api/pro/data/v1/futures/balance/snapshot`

#### Signature

You should sign the message in header as specified in [**Authenticate a RESTful Request**](#signing-a-Request) section.

#### Prehash String

`<timestamp>+data/v1/futures/balance/snapshot`

#### Request Parameters

Name | Type | Required | Value Range | Description  
---|---|---|---|---  
**date** | `String` | Yes | `YYYY-mm-dd` | balance date  
  
#### Response Content

Name | Type | Description  
---|---|---  
**meta** | `Json` | `meta` info. See detail below  
**collateralBalance** | `Json Array` | `collateral balance` info. See detail below  
**contractBalance** | `Json Array` | `contract balance` info. See detail below  
  
`meta` field provides some basic info about the balance snapshot data.

`meta` schema

Name | Type | Description | Sample Response  
---|---|---|---  
**ac** | `String` | account category | `"futures`  
**accountId** | `String` | accountId |   
**sn** | `Long` | sequence number |   
**balanceTime** | `Long` | balance snapshot time in milli seconds |   
  
`collateralBalance` field provides array of ‘asset’ and ‘totalBalance’ for collateral balance.

`collateralBalance` schema

Name | Type | Description | Sample Response  
---|---|---|---  
**asset** | `String` | asset code | `"USDT"`  
**totalBalance** | `String` | current asset total balance | `"1234.56"`  
  
`contractBalance` field provides array of current contract positions infomation.

`contractBalance` schema

Name | Type | Description | Sample Response  
---|---|---|---  
**contract** | `String` | contract name | `"USDT"`  
**futuresAssetBalance** | `String` | current contract position | `"1234.56"`  
**isolatedMargin** | `String` | Isolated margin | `"134.56"`  
**refCostBalance** | `String` | Reference cost | `"34.56"`  
  
#### Code Sample

Please refer to python code to [query balance snapshot](https://github.com/ascendex/ascendex-pro-api-demo/blob/main/python/query_balance_and_order_fills.py)

### Futures Order and Balance Detail

This API is for intraday balance change detail from balance event and order fillss.

#### HTTP Request

`GET api/pro/data/v1/futures/balance/history`

#### Prehash String

`<timestamp>+data/v1/futures/balance/history`

> Futures Account Balance Detail - Sample response
    
    
    {
        "balance": [
            {
                "data": [
                    {
                        "asset": "XPRTPC",
                        "curBalance": "-7.873230189",
                        "deltaQty": "0.004117158"
                    }
                ],
                "eventType": "Fundingpayment",
                "sn": 18591022051,
                "transactTime": 1634947227877
            },
            {
                "data": [
                    {
                        "asset": "BTCPC",
                        "curBalance": "-307.654491085",
                        "deltaQty": "10.673854479"
                    },
                    {
                        "asset": "USDT",
                        "curBalance": "149.493187792",
                        "deltaQty": "10.673854479"
                    }
                ],
                "eventType": "Futuressettlement",
                "sn": 18590550015,
                "transactTime": 1634913817331
            }
        ],
        "meta": {
            "ac": "futures",
            "accountId": "futfi7p9j312936d2hkjJpAahWyb4RCJ"
        },
        "order": [
            {
                "data": [
                    {
                        "asset": "PORTP",
                        "curBalance": "1",
                        "dataType": "trade",
                        "deltaQty": "1"
                    },
                    {
                        "asset": "PORTPC",
                        "curBalance": "-6.213726",
                        "dataType": "trade",
                        "deltaQty": "-6.21"
                    },
                    {
                        "asset": "PORTPC",
                        "curBalance": "-6.213726",
                        "dataType": "fee",
                        "deltaQty": "-0.003726"
                    }
                ],
                "liquidityInd": "RemovedLiquidity",
                "orderId": "r17ca5840c64U7684578612bportL84r",
                "orderType": "Market",
                "side": "Buy",
                "sn": 18589783182,
                "transactTime": 1634864467246
            }
        ]
    }
    

#### Request Parameters

Name | Type | Required | Value Range | Description  
---|---|---|---|---  
**sn** | `Long` | Yes | start from snapshot `sn` | Start sn  
**limit** | `Int` | No | 1 to 500 | Number of records. max 500  
  
#### Response Content

Name | Type | Description  
---|---|---  
**meta** | `Json` | `meta` info. See detail below  
**order** | `Json Array` | `order` info. See detail below  
**balance** | `Json Array` | `balance` info. See detail below  
  
##### Meta

`meta` field provides some basic info.

`meta` schema

Name | Type | Description | Sample Response  
---|---|---|---  
**ac** | `String` | account category | `"cash", "margin", "futures`  
**accountId** | `String` | accountId |   
  
##### Order

`order` field provides an array of asset balance detail from order fill event.

`order` schema

Name | Type | Description | Sample Response  
---|---|---|---  
**liquidityInd** | `String` | liquidity indicator | `RemovedLiquidity` for taker order, `AddedLiquidity` for maker order, or `NULL_VAL`  
**orderId** | `String` | orderId | order Id  
**orderType** | `String` | order type | `market`, `limit`  
**side** | `String` | order side | `buy`, `sell`  
**sn** | `Long` | sequence number | unique and increasing sequence number  
**transactTime** | `Long` | transactTime in milli seconds |   
**data** | `Json Array` | list of order info json objects | see detail below  
  
order balance detail by asset

`data` schema

Name | Type | Description | Sample Response  
---|---|---|---  
**asset** | `String` | asset code | `"USDT"`  
**curBalance** | `String` | asset balance after this transaction | `"1234.56"`  
**dataType** | `String` | `trade` for trading asset; `fee` for fee balance asset | `trade`, `fee`  
**deltaQty** | `String` | balance change in this transaction | `100`  
  
##### Balance

`balance` field provides an array of asset balance detail due to balance event.

`balance` schema

Name | Type | Description | Sample Response  
---|---|---|---  
**eventType** | `String` | balance event type | `deposit`, `withdrawal`  
**sn** | `Long` | sequence number |   
**transactTime** | `Long` | transactTime in milli seconds |   
**data** | `Json Array` | list of balance info json objects | see detail below  
  
`data` schema

Name | Type | Description | Sample Response  
---|---|---|---  
**asset** | `String` | asset code | `"USDT"`  
**curBalance** | `String` | asset balance after this transaction | `"1234.56"`  
**deltaQty** | `String` | balance change in this transaction | `100`  
  
#### Code Sample

Please refer to python code to [query order and balance detail](https://github.com/ascendex/ascendex-pro-api-demo/blob/main/python/query_balance_and_order_fills.py)

# WebSocket

## How to Connect

Base endpoints:

  * Testnet: 

    * Public endpoint: `wss://api-test.ascendex-sandbox.com:443/api/pro/v2/stream`
    * Private endpoint: `wss://api-test.ascendex-sandbox.com:443/<grp>/api/pro/v2/stream`
  * Mainnet:

    * Public endpoint: `wss://ascendex.com:443/api/pro/v2/stream`
    * Private endpoint: `wss://ascendex.com:443/<grp>/api/pro/v2/stream` You can only authenticate a WebSocket session via a private endpoint.



## WebSocket Authentication

You must authenticate the websocket session in order to recieve private data and send account specific requests (e.g. placing new orders). 

You have two options to authenticate a websocket session. 

  * by adding authentication data in the request header when connecting to websocket. 
  * by sending an `op:auth` message to the server after you have connected to websocket. 



Once you successfully connect to the websocket, you will receive a `connected` message: 

  * for authenticated websocket session: `{"m":"connected","type":"auth"}`
  * for unauthenticated websocket session: `{"m":"connected","type":"unauth"}`



If the session is disconnected for some reason, you will receive a `disconnected` message:

  * `{"m":"disconnected","code":100005,"reason":"INVALID_WS_REQUEST_DATA","info":"Session is disconnected due to missing pong message from the client"}`



**Method 1 - WebSocket Authentication with Request Headers**

> Authenticate with Headers
    
    
    # # Install wscat from Node.js if you haven't
    # npm install -g wscat  
    
    APIPATH=v2/stream
    APIKEY=BclE7dBGbS1AP3VnOuq6s8fJH0fWbH7r
    SECRET=fAZcQRUMxj3eX3DreIjFcPiJ9UR3ZTdgIw8mxddvtcDxLoXvdbXJuFQYadUUsF7q
    TIMESTAMP=`date +%s%N | cut -c -13`
    MESSAGE=$TIMESTAMP+$APIPATH
    SIGNATURE=`echo -n $MESSAGE | openssl dgst -sha256 -hmac $SECRET -binary | base64`
    
    wscat -H "x-auth-key: $APIKEY" \
      -H "x-auth-signature: $SIGNATURE" \
      -H "x-auth-timestamp: $TIMESTAMP" \
      -c wss://api-test.ascendex-sandbox.com:443/api/pro/v2/stream -w 1 -x '{"op":"sub", "id": "abc123", "ch": "order:cshQtyfq8XLAA9kcf19h8bXHbAwwoqDo:ASD/USDT"}'
    

This is similar to the way you authenticate any RESTful request. You need to add the following header fields to the connection request:

  * `x-auth-key`
  * `x-auth-timestamp`
  * `x-auth-signature`



The server will then check if the data is correctly signed before upgrading the connection protocol to WebSocket. 

Note that if you specify these header fields, the server will reject the websocket connection request if authentication fails. 

**Method 2 - WebSocket Authentication by Sending the Auth Message**

> Authenticate by Sending the `auth` Message
    
    
    # # Install wscat from Node.js if you haven't
    # npm install -g wscat  
    
    APIPATH=v2/stream
    APIKEY=BclE7dBGbS1AP3VnOuq6s8fJH0fWbH7r
    SECRET=fAZcQRUMxj3eX3DreIjFcPiJ9UR3ZTdgIw8mxddvtcDxLoXvdbXJuFQYadUUsF7q
    TIMESTAMP=`date +%s%N | cut -c -13`
    MESSAGE=$TIMESTAMP+$APIPATH
    SIGNATURE=`echo -n $MESSAGE | openssl dgst -sha256 -hmac $SECRET -binary | base64`
    
    wscat -c wss://api-test.ascendex-sandbox.com:443/1/api/pro/v2/stream -w 1 -x "{\"op\":\"auth\", \"id\": \"abc123\", \"t\": $TIMESTAMP, "key": \"$APIKEY\", \"sig\": \"$SIGNATURE\"}"
    

You can also authenticate a live websocket session by sending an `op:auth` message to the server. 

Name | Type | Required | Description  
---|---|---|---  
`op` | `String` | Yes | `"auth"`  
`id` | `String` | No | optional id field, you may safely skip it  
`t` | `Long` | Yes | UTC timestamp in milliseconds, use this timestamp to generate signature  
`key` | `String` | Yes | your api key  
`sig` | `String` | Yes | the signature is generated by signing `"<timestamp>+v2/stream"`  
  
More comprehensive examples can be found at:

  * Python demo for [websocket auth](https://github.com/ascendex/ascendex-futures-api-demo-v2/blob/main/scripts/minimum_websocket_client_sandbox.py)



**Authentication Response**

> Auth success message
    
    
    {  
      "m": "auth",
      "id": "abc123",
      "code": 0
    }
    

> Auth error message
    
    
    {
      "m":"auth",
      "id": "abc123",
      "code": 200006,
      "err": "Unable to find User Account Data"
    }
    

You will receive a message for authentication result after you send authentication request.

Field | Type | Description  
---|---|---  
`m` | `String` | `"auth"`  
`id` | `String` | echo back the id if you provide one in the request  
`code` | `Long` | Any code other than 0 indicate an error in authentication  
`err` | `Optional[String]` | Provide detailed error message if code is not 0  
  
## Keep the Connection Alive

In order to keep the websocket connection alive, you have two options, detailed below.

#### Method 1: Responding to Server's ping messages

> Method 1. keep the connection alive by responding to Server pushed ping message 
    
    
    <<< { "m": "ping", "hp": 3 }  # Server pushed ping message
    >>> { "op": "pong" }   # Client responds with pong
    

If the server doesn't receive any client message after a while, it will send a `ping` message to the client. Once the `ping` message is received, the client should promptly send a `pong` message to the server. If you missed two consecutive `ping` messages, the session will be disconnected. 

**Server Ping Message Schema**

Name | Type | Description  
---|---|---  
op | String | `ping`  
hp | Int | health point: when this value decreases to 0, the session will be disconnected.  
  
#### Method 2: Sending ping messages to Server

> Method 2. keep the connection alive by sending ping message to the server
    
    
    >>> { "op": "ping" }                                    # Client initiated ping message (every 30 seconds)
    <<< { "m":"pong", "code":0, "ts":1614164189, "hp": 2 }  # Server responds to client ping 
    

You can also send `ping` message to the server every 15 seconds to keep the connection alive. The server will stop sending `ping` message for 30 seconds if a client initiated `ping` message is received. 

**Server Pong Message Schema**

Name | Type | Description  
---|---|---  
m | String | `pong`  
code | Int | error code, for the pong mesage, the error code is always 0 (success)  
ts | Long | server time in UTC miliseconds  
hp | Int | health point: when this value decreases to 0, the session will be disconnected.  
  
## Public Stream Data

### Channel: Futures Pricing Data

> Sample Futures Pricing Data Message
    
    
    {
        "m": "futures-pricing-data",
        "con": [  // contracts
            {
                "s" : "BTC-PERP",        // symbol
                "t" : 1614814705716,     // data time
                "ip": "50702.8",         // index price
                "mp": "50652.3553",      // mark price
                "r" : "0.000565699",     // funding rate 
                "oi": "90.7367",         // open interest
                "f" : 1614816000000      // next funding time
            }
        ], 
        "col": [  // collateral assets
            {
                "a": "USDTR",  // asset
                "p": "1"       // reference price (quote in USDT)
            },
            {
                "a": "USDC",
                "p": "0.99935"
            },
            {
                "a": "ETH",
                "p": "1582.505"
            },
            {
                "a": "PAX",
                "p": "0.9964"
            },
            {
                "a": "BTC",
                "p": "50621.795"
            },
            {
                "a": "USDT",
                "p": "1"
            }
        ]
    }
    

**Subscribe to the Channel**

`{"op":"sub", "id":"sample-id", "ch":"futures-pricing-data"}`

### Channel: Level 1 Order Book Data (BBO)

> Subscribe to `BTC-PERP` quote stream
    
    
    { "op": "sub", "id": "abc123", "ch":"bbo:BTC-PERP" }
    

> Unsubscribe to `BTC-PERP` quote stream
    
    
    { "op": "unsub", "id": "abc123", "ch":"bbo:BTC-PERP" }
    

> BBO Message 
    
    
    {
        "m": "bbo",
        "symbol": "BTC-PERP",
        "data": {
            "ts": 1573068442532,
            "bid": [
                "9309.11",
                "0.0197172"
            ],
            "ask": [
                "9309.12",
                "0.8851266"
            ]
        }
    }
    

You can subscribe to updates of best bid/offer data stream only. Once subscribed, you will receive BBO message whenever the price and/or size changes at the top of the order book. 

Each BBO message contains price and size data for exactly one bid level and one ask level. 

### Channel: Level 2 Order Book Updates

> Subscribe to `BTC-PERP` depth updates stream
    
    
    { "op": "sub", "id": "abc123", "ch":"depth:BTC-PERP" }
    

> Unsubscribe to `BTC-PERP` depth updates stream
    
    
    { "op": "unsub", "id": "abc123", "ch":"depth:BTC-PERP" }
    

> The Depth Message 
    
    
    {
        "m": "depth",
        "symbol": "BTC-PERP",
        "data": {
            "ts": 1573069021376,
            "seqnum": 2097965,
            "asks": [
                [
                    "0.06844",
                    "10760"
                ]
            ],
            "bids": [
                [
                    "0.06777",
                    "562.4"
                ],
                [
                    "0.05",
                    "221760.6"
                ]
            ]
        }
    }
    

If you want to keep track of the most recent order book snapshot in its entirety, the most efficient way is to subscribe to the `depth` channel. 

Each `depth` message contains a `bids` list and an `asks` list in its `data` field. Each list contains a series of `[price, size]` pairs that you can use to update the order book snapshot. In the message, `price` is always positive and `size` is always non-negative. 

  * if `size` is positive and the `price` doesn't exist in the current order book, you should **add** a new level `[price, size]`. 
  * if `size` is positive and the `price` exists in the current order book, you should **update** the existing level to `[price, size]`. 
  * if `size` is zero, you should **delete** the level at `price`. 



See [Orderbook Snapshot](https://github.com/ascendex/ascendex-pro-api-demo/blob/main/python/websocket_orderbook_snapshot.py) for code examples.

### Channel: Market Trades

> Subscribe to `BTC-PERP` market trades stream
    
    
    { "op": "sub", "id": "abc123", "ch":"trades:BTC-PERP" }
    

> Unsubscribe to `BTC-PERP` market trades stream
    
    
    { "op": "unsub", "id": "abc123", "ch":"trades:BTC-PERP" }
    

> Trade Message 
    
    
    {
        "m": "trades",
        "symbol": "BTC-PERP",
        "data": [
            {
                "p":      "0.068600",
                "q":      "100.000",
                "ts":      1573069903254,
                "bm":      false,
                "seqnum":  144115188077966308
            }
        ]
    }
    

The `data` field is a list containing one or more trade objects. The server may combine consecutive trades with the same price and `bm` value into one aggregated item. Each trade object contains the following fields:

Name | Type | Description  
---|---|---  
seqnum | Long | the sequence number of the trade record. `seqnum` is always increasing for each symbol, but may not be consecutive  
p | String | the executed price expressed as a string  
q | String | the aggregated traded amount expressed as string  
ts | Long | the UTC timestamp in milliseconds of the first trade  
bm | Boolean | if true, the buyer of the trade is the maker.  
  
### Channel: Bar Data

> Subscribe to `BTC-PERP` 1 minute bar stream
    
    
    { "op": "sub", "id": "abc123", "ch":"bar:1:BTC-PERP" }
    

> Unsubscribe to `BTC-PERP` 1 minute bar stream
    
    
    { "op": "unsub", "id": "abc123", "ch":"bar:1:BTC-PERP" }
    
    //  Alternatively, you can unsubscribe all bar streams for BTC-PERP
    { "op": "unsub", "id": "abc123", "ch":"bar:*:BTC-PERP" }
    
    // Or unsubscribe all 1 minute bar stream
    { "op": "unsub", "id": "abc123", "ch":"bar:1" }
    
    // Or unsubscribe all bar stream
    { "op": "unsub", "id": "abc123", "ch":"bar" }
    

> Bar Data Message 
    
    
    {
        "m": "bar",
        "s": "BTC-PERP",    
        "data": {
            "i":  "1",
            "ts": 1575398940000,
            "o":  "0.04993",
            "c":  "0.04970",
            "h":  "0.04993",
            "l":  "0.04970",
            "v":  "8052"
        }
    }
    

The `data` field is a list containing one or more trade objects. The server may combine consecutive trades with the same price and `bm` value into one aggregated item. Each trade object contains the following fields:

Name | Type | Description  
---|---|---  
seqnum | Long | the sequence number of the trade record. `seqnum` is always increasing for each symbol, but may not be consecutive  
p | String | the executed price expressed as a string  
q | String | the aggregated traded amount expressed as string  
ts | Long | the UTC timestamp in milliseconds of the first trade  
bm | Boolean | if true, the buyer of the trade is the maker.  
  
## Private Stream Data

### Channel: Order
    
    
    {
      "m"      : "futures-order",
      "sn"     : 127,                   // sequence number
      "e"      : "ExecutionReport",     // event
      "a"      : "sample-futures-account-id",  // account Id
      "ac"     : "FUTURES",             // account category 
      "t"      : 1606335352348,         // last execution time
      "ct"     : 1606335351541,         // order creation time
      "orderId": "a176010c4957U68469127074abcd1234",  // order Id
      "sd"     : "Buy",                 // side 
      "ot"     : "Limit",               // order type 
      "q"      : "0.1",                 // order quantity (base asset)
      "p"      : "18000",               // order price
      "sp"     : "0",                   // stop price
      "spb"    : "",                    // stop trigger
      "s"      : "BTC-PERP",            // symbol 
      "st"     : "New",                 // order status
      "lp"     : "0",                   // last filled price
      "lq"     : "0",                   // last filled quantity (base asset)
      "ap"     : "0",                   // average filled price
      "cfq"    : "0",                   // cummulative filled quantity (base asset)
      "f"      : "0",                   // commission fee of the current execution
      "cf"     : "0",                   // cumulative commission fee
      "fa"     : "USDT",                // fee asset
      "ei"     : "NULL_VAL",            // execution instruction
      "err"    : ""                     // error message
    }
    

**Subscribe to the Channel**

`{"op":"sub", "id":"sample-id", "ch":"futures-order"}`

### Channel: Account Update
    
    
    
    {
      "m"     : "futures-account-update",            // message
      "e"     : "ExecutionReport",                   // event type
      "t"     : 1612508562129,                       // server time (UTC time in milliseconds)
      "acc"   : "sample-futures-account-id",         // account ID
      "at"    : "FUTURES",                           // account type
      "sn"    : 23128,                               // sequence number, strictly increasing for each account
      "id"    : "r177710001cbU3813942147C5kbFGOan",  // request ID for this account update
      "col": [
        {
          "a": "USDT",               // asset code
          "b": "1000000",            // balance 
          "f": "1"                   // discount factor
        }
      ],
      "pos": [
        {
          "s"   : "BTC-PERP",        // symbol
          "sd"  : "LONG",            // side
          "pos" : "0.011",           // position
          "rc"  : "-385.840455",     // reference cost
          "up"  : "18.436008668",    // unrealized pnl
          "rp"  : "0",               // realized pnl
          "aop" : "35041.363636363", // Average Opening Price
          "boon": "0",               // Buy Open Order Notional
          "soon": "0",               // Sell Open Order Notional
          "mt"  : "crossed",         // margin type: isolated / cross
          "iw"  : "0",               // isolated margin
          "lev" : "10",              // leverage
          "tp"  : "0",               // take profit price (by position exit order)
          "tpt" : "market",          // take profit trigger (by position exit order)
          "sl"  : "0",               // stop loss price (by position exit order)
          "slt" : "market",          // stop loss trigger (by position exit order)
        }
      ]
    }
    

**Subscribe to the Channel**

`{"op":"sub", "id":"sample-id", "ch":"futures-account-update"}`

## WebSocket - Data Request

### WS: Account Snapshot

> Requesting Futures Account Snapshot
    
    
    {
       "op"    : "req",
       "id"    : "abc123456",
       "action": "futures-account-snapshot"
    }
    

> Futures Account Snapshot response
    
    
    {
       "m"  : "futures-account-snapshot",  // message
       "id" : "abc123456",                 // echo back the request Id
       "e"  : "ClientRequest",             // event name
       "t"  : 1613748277356,               // server time in milliseconds (UTC)
       "acc": "futH9N59hR0BMVEjHnBleHLn0mfUl5lo",  // accountId
       "ac" : "FUTURES",                   // account category
       "sn" : 9982,                        // sequence number
       "col":[  // collateral balances
          {
             "a": "ETH",     // collateral asset code
             "b": "500",     // collateral balance
             "f": "0.95"     // discount factor
          },
          {
             "a": "BTC",
             "b": "100",
             "f": "0.98"
          },
          {
             "a": "USDT",
             "b": "1000000",
             "f": "1"
          }
       ],
       "pos":[  // contract positions
          {
             "s"   : "BTC-PERP",  // contract symbol
             "sd"  : "NULL_VAL",  // side: LONG / SHORT / NULL_VAL
             "pos" : "0",         // position
             "rc"  : "0",         // reference cost
             "up"  : "0",         // unrealized pnl
             "rp"  : "0",         // realized pnl
             "aop" : "0",         // average opening price
             "mt"  : "crossed",   // margin type: isolated / cross
             "boon": "0",         // buy open order notional
             "soon": "0",         // sell open order notional
             "lev" : "10",        // leverage
             "iw"  : "0",         // isolated margin
             "tp"  : "0",         // take profit price (by position exit order)
             "tpt" : "market",    // take profit trigger (by position exit order)
             "sl"  : "0",         // stop loss price (by position exit order)
             "slt" : "market"     // stop loss trigger (by position exit order)
          }
       ]
    }
    

You can request the futures account snapshot via websocket by a `futures-account-snapshot` action. 

The request schema:

Name | Data Type | Description  
---|---|---  
op | String | `req`  
action | String | `futures-account-snapshot`  
id | String | for result match purpose  
  
### WS: Place Order

> Request to place new order
    
    
    {
       "op"    : "req",
       "action": "place-order",
       "ac"    : "futures",         // the Account Category
       "id"    : "sampleRequestID", // the server will echo back this id in the ack message. 
       "args":{
          "time"      : 1613753879921,
          "symbol"    : "BTC-PERP",
          "price"     : "30000",
          "orderQty"  : "0.12",
          "orderType" : "limit",
          "side"      : "buy",
          "postOnly"  : false,
          "respInst"  : "ACK"
       }
    }
    

> Successful ACK message
    
    
    {
       "m"     : "order",
       "code"  : 0,
       "id"    : "sampleRequestID",   // echo back the original request Id
       "action": "place-order",
       "ac"    : "FUTURES",
       "info": {
          "orderId": "s177bbb671b7U1234567890leOrderId",
          "symbol" : "BTC-PERP"
       }
    }
    

> Error response message
    
    
    {
       "m"     : "order",
       "code"  : 300001,
       "id"    : "sampleRequestID",  // echo back the original request Id
       "action": "place-order",
       "ac"    : "FUTURES",
       "info": {
          "symbol"  : "BTC-PERP",
          "reason"  : "INVALID_PRICE",
          "errorMsg": "Order price is too low from market price."
       }
    }
    

Place order via websocket 

**Request**

Make new order request follow the general websocket request rule, with proper place new order parameters as specified in rest api for _args_ field.

see [placing order via RESTful API](#new-order).

_id_

As described in [Generate Order Id](#generate-order-id), the server uses a deterministic algorithm to compute the orderId based on client inputs. For every order request placed via WebSocket, **We strongly recommend you put a non-repeatable id**.

**Response**

Respond with _m_ field as _order_ , and _action_ field as _place-order_ ; if you provide _id_ in your request, it will be echoed back as _id_ to help you identify; _code_ field to indicate if this is a successful _zero_ or failed _non-zero_.

_code=0_

With _code_ field as _zero_ to indicate this new order request pass some basic sanity check, and has been sent to matching engine. 

_info_ field provide some detail: if you provide _id_ in your request, it will be echoed back as _id_ to help you identify; we also provide server side generated _orderId_ , which is the id you should use for future track or action on the order. 

_code=non-zero_

With _code_ field as _non-zero_ to indicate there is some obvisous errors in your request. 

_info_ field provide some detail: we also provide error _reason_ and _errorMsg_ detail.

### WS: Cancel Order

> Request to cancel existing open order
    
    
    {
       "op"    : "req",
       "action": "cancel-order",
       "ac"    : "futures",
       "id"    : "sampleRequestId",    // server will echo back this Id.
       "args":{
          "time":1613744943323,
          "orderId":"s177bab1b474U5051470287bbtcpKiOR",
          "symbol":"BTC-PERP"
       }
    }
    

> Successful ACK message
    
    
    {
       "m"     : "order",
       "action": "cancel-order",
       "ac"    : "FUTURES",
       "id"    : "sampleRequestId", // echo back the original request Id
       "code":0,
       "info":{
          "orderId": "s177bab1b474U5051470287bbtcpKiOR",
          "symbol" : "BTC-PERP"
       }
    }
    

> Error response message
    
    
    {
       "m"     : "order",
       "action": "cancel-order",
       "ac"    : "FUTURES",
       "code"  : 300006,
       "id"    : "sampleRequestId", // echo back the original request Id
       "info":{
          "symbol"  : "BTC-PERP",
          "reason"  : "INVALID_ORDER_ID",
          "errorMsg": "Client Order Id too Long: s177bab1b474U5051470287bbtcpKiOR1"
       }
    }
    

Cancel an existing open order via websocket 

**Request**

Make order cancelling request follow the general websocket request rule by setting `action` to be `cancel-orde`, with proper cancel order parameters as specified in rest api for _args_ field.

**Response**

Respond with _m_ field as _order_ , and _action_ field as _cancel-order_ ; _code_ field to indicate if this is a successful _zero_ or failed _non-zero_.

_code=0_

With _code_ field as _zero_ to indicate this cancel order request pass some basic sanity check, and has been sent to matching engine. 

_info_ field provide some detail: if you provide _symbol_ in your request, it will be echoed back as _symbol_ to help you idintify; we also echo back target _orderId_ to be cancelled. 

_code=non-zero_

With _code_ field as _non-zero_ to indicate there is some obvisous errors in your cancel order request. 

_info_ field provide some detail: we also provide error _reason_ and _errorMsg_ detail.

### WS: Cancel All Orders

> Request to cancel all existing open orders 
    
    
    {
       "op"    : "req",
       "action": "cancel-all",
       "ac"    : "futures",
       "id"    : "sampleRequestId", // server will echo back this Id.
       "args": {   // you can also omit the args field
       }
    }
    

> Request to cancel existing open order related to symbol "BTC-PERP"
    
    
    {
       "op"    : "req",
       "action": "cancel-all",
       "ac"    : "futures",
       "id"    : "sampleRequestId", // server will echo back this Id.
       "args":{ 
            "symbol": "BTC-PERP"     
       }
    }
    

> Successful ACK message
    
    
    {
       "m"     : "order",
       "code"  : 0,
       "action": "cancel-all",
       "ac"    : "FUTURES",
       "id"    : "sampleRequestId", // echo back the original request Id
       "info":{
          "symbol":""
       }
    }
    

> Error response message
    
    
    {
       "m"     : "order",
       "code"  : 300012,
       "action": "cancel-all",
       "ac"    : "FUTURES",
       "id"    : "sampleRequestId", // echo back the original request Id
       "info":{
          "symbol"  : "",
          "reason"  : "INVALID_PRODUCT",
          "errorMsg": "Invalid Product Symbol"
       }
    }
    

Cancel all open orders on account level via websocket with optional symbol.

**Request**

Make general websocket request with `action` field as `cancel-All` and set proper `ac` value(`futures`), and provide _symbol_ value in _args_.

**Response**

With _code_ field as _zero_ to indicate this cancel all order request has been received by server and sent to matching engine. 

_info_ field provide some detail: if you provide _symbol_ in your request to cancel orders.

With _code_ field as _non-zero_ to indicate there is some obvisous errors in your request. 

_info_ field provide some detail: we also provide error _reason_ and _errorMsg_ detail.

### WS: Query Open Orders

> Requesting open orders on symbol BTC-PERP
    
    
    {
       "op"    : "req",
       "id"    : "abc123456",
       "action": "futures-open-orders",
       "args":{
          "symbol":"BTC-PERP"
       }
    }
    

> Open orders response
    
    
    {
       "m":"futures-open-orders",
       "code":0,
       "id":"abc123456",
       "ac":"FUTURES",
       "data":[
          {
             "ac":"FUTURES",
             "accountId":"sample-futures-account-id",
             "time":1615696544843,
             "orderId":"r1782f04c58aU3792951278sbtcp7EbA",
             "seqNum":13,
             "orderType":"Limit",
             "execInst":"NULL_VAL",
             "side":"Sell",
             "symbol":"BTC-PERP",
             "price"     :"66000",
             "orderQty":"0.0001",
             "stopPrice":"0",
             "stopBy":"market",
             "status":"New",
             "lastExecTime":1615696544851,
             "lastQty":"0",
             "lastPx":"0",
             "avgFilledPx":"0",
             "cumFilledQty":"0",
             "fee":"0",
             "cumFee":"0",
             "feeAsset":"USDT",
             "errorCode":"",
             "posStopLossPrice":"0",
             "posStopLossTrigger":"None",
             "posTakeProfitPrice":"0",
             "posTakeProfitTrigger":"None"
          },
          ...
       ]
    }
    

> Error response message
    
    
    {
       "m":"error",
       "id":"abc123456",
       "code":100005,
       "reason":"INVALID_WS_REQUEST_DATA",
       "info":"Missing required parameter: args"
    }
    

You can request the open order via websocket by a `futures-open-orders` action. 

The request schema:

Name | Data Type | Description  
---|---|---  
op | String | `req`  
action | String | `futures-open-orders`  
id | String | for result match purpose  
args:symbol | Optional[String] | add the (optional) symbol filter, see below for details.  
  
The `symbol` key in the `args` map allows you to customize the symbol filter in a flexible way:

  * to query open orders of the **a specific symbol** , set `symbol` to a valid symbol code. For instance, `{"symbol": "BTC-PERP"}`
  * to query **all open orders** , you may simply omit the `symbol` key (`{}`). 



# Appendix

## ENUM Definitions

### Account Category (`ac`)

  * `CASH`
  * `MARGIN`
  * `FUTURES`



### Order Type (`orderType`)

  * `Limit`
  * `Market`
  * `StopLimit`
  * `StopMarket`



### Side (`side`)

  * `Buy`
  * `Sell`



### Response Type (`respInst`)

  * `ACK`
  * `ACCEPT`
  * `DONE`



### Time in Force (`timeInForce`)

  * `GTC` \- good till cancelled 
  * `IOC` \- immediate or cancel
  * `FOK` \- fill or kill



### Execution Instruction (`execInst`)

  * `Post`
  * `Liquidation`
  * `InternalPost`
  * `StopOnMarket`
  * `StopOnMark`
  * `StopOnRef`
  * `ReduceOnly`
  * `PostReduceOnly`
  * `PostStopMarket`
  * `PostStopMark`
  * `PostStopRef`
  * `ReduceOnlyMarket`
  * `ReduceOnlyMark`
  * `ReduceOnlyRef`
  * `PostReduceMarket`
  * `PostReduceMark`
  * `PostReduceRef`
  * `OpenStopMkt`
  * `OpenStopMark`
  * `OpenStopRef`
  * `OpenPostStopMkt`
  * `OpenPostStopMark`
  * `OpenPostStopRef`
  * `PosStopMkt`
  * `PosStopMark`
  * `PosStopRef`



### Order Status (`status`)

  * `New`
  * `PartiallyFilled`
  * `Filled`
  * `Canceled`
  * `Rejected`
  * `PendingNew` \- a conditional order (stop limit / stop market) that hasn't been triggered yet.



### Margin Type (`marginType`)

  * `crossed`
  * `isolated`



### WebSocket Operations (`op`)

  * `auth`



### WebSocket Message Types (`m`)

  * `auth`
  * `sub`
  * `unsub`
  * `bbo`
  * `futures-pricing-data-batch`
  * `futures-order`
  * `futures-account-update`



[shell](#) [python](#) [java](#)
