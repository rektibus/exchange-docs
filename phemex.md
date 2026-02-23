## Table of Contents * [Phemex Public API](#publicapi) * [General Public API Information](#general)

* [REST API Standards](#restapi)
    * [HTTP Restful Response](#restresponse)
        * [HTTP Return Codes](#httpreturncodes)
        * [HTTP Restful Response Format](#responseformat)
        * [Restful Response Error Codes](#errorcode)
    * [HTTP REST Request Header](#httprestheader)
    * [API Rate Limits](#apiratelimits)
    * [Endpoint security type](#securitytype)
        * [Signature Example 1: HTTP GET Request](#signatureexample1)
        * [Singature Example 2: HTTP GET Request with multiple query string](#signatureexample2)
        * [Signature Example 3: HTTP POST Request](#signatureexample3)
    * [Common data explained](#fieldexplained)
        * [Margin Mode and Leverage](#marginModeAndLeverage)
        * [Price/Ratio/Value Scales](#scalingfactors)
        * [Common constants](#commconsts)
    * [REST API List](#restapilist)
        * [Market API List](#marketapilist)
            * [Query Product Information](#queryproductinfo)
        * [Trade API List](#orderapilist)
            * [Place Order With Put Method, *Prefered*](#placeorderwithput)
            * [Order examples](#orderexample)
            * [Place Order](#placeorder)
            * [Amend Order by OrderID](#amendorder)
            * [Cancel Single Order by OrderID or ClOrdID](#cancelsingleorder)
            * [Bulk Cancel Orders](#cancelorder)
            * [Cancel All Orders](#cancelall)
            * [Query Trading Account and Positions](#querytradeaccount)
            * [Query Trading Account and Positions with unrealized PNL](#queryPosWithPnl)
            * [Change Position Leverage](#changeleverage)
            * [Change Position Risklimt](#changerisklimit)
            * [Assign Position Balance in Isolated Margin Mode](#assignposbalance)
            * [Query Open Orders by Symbol](#queryopenorder)
            * [Query Closed Orders by Symbol](#queryorder)
            * [Query Order by orderID](#queryorderbyid)
            * [Query User Trades by Symbol](#querytrade)
        * [Market Data API List ](#mdapilist)
            * [Query Order Book](#queryorderbook)
            * [Query kline](#querykline)
            * [Query Recent Trades](#querytrades)
            * [Query 24 Hours Ticker](#query24hrsticker)
            * [Query History Trades](#queryhisttrades)
        * [Asset API List](#assetapilist)
            * [Query client and wallets](#clientwalletquery)
            * [Transfer self balance to parent or subclients](#walletransferout)
            * [Transfer from sub-client wallet](#walletransferin)
        * [Future Data Api List](#futureDataAPIList)
            * [Query Funding Fees History](#futureDataFundingFeesHist)
            * [Query Orders History](#futureDataOrdersHist)
            * [Query Orders By Ids](#futureDataOrdersByIds)
            * [Query Trades History](#futureDataTradesHist)
            * [Query Trading Fees History](#futureDataTradingFeesHist)
            * [Query Trading Account Detail](#futureDataTradingAccountDetail)
        * [Withdraw](#withdraw)
            * [Request withdraw](#requestwithdraw)
            * [Confirm withdraw](#confirmwithdraw)
            * [Cancel withdraw](#cancelwithdraw)
            * [List withdraw requests](#listwithdraw)
            * [Withdraw address management](#withdrawaddrmgmt)
* [Websocket API Standards](#wsapi)
    * [Session Management](#sessionmanagement)
    * [API Rate Limits](#wsapiratelimits)
    * [WebSocket API List](#wsapilist)
        * [Heartbeat](#heartbeat)
        * [API User Authentication](#apiuserauth)
        * [Subscribe OrderBook](#booksub)
        * [Subscribe Full OrderBook](#booksub2)
        * [Unsubscribe OrderBook](#bookunsub)
        * [Subscribe Trade](#tradesub)
        * [Unsubscribe Trade](#tradeunsub)
        * [Subscribe Kline](#klinesub)
        * [Unsubscribe Kline](#klinesub)
        * [Subscribe Account-Order-Position (AOP)](#aopsub)
        * [Unsubscribe Account-Order-Position (AOP)](#aopunsub)
        * [Subscribe 24 Hours Ticker](#tickersub)
        * [Subscribe symbol price](#symbpricesub)

<a name="publicapi"/>

# Phemex Public API

<a name="general"/>

## General Public API Information

* Phemex provides HTTP Rest API for client to operate Orders, all endpoints return a JSON object.
* The default Rest API base endpoint is: **https://api.phemex.com**. The High rate limit Rest API base endpoint
  is: **https://vapi.phemex.com**. Or for the testnet is:  **https://testnet-api.phemex.com**
* Phemex provides WebSocket API for client to receive market data, order and position updates.
* The WebSocket API url is: **wss://phemex.com/ws**. The High rate limit WebSocket API url is: **wss:
  //vapi.phemex.com/ws**. Or for the testnet is:  **wss://testnet.phemex.com/ws**

<a name="restapi"/>

# REST API Standards

<a name="restresponse"/>

## Restful API Response

<a name="httpreturncodes"/>

### HTTP Return Codes

* HTTP `401` return code is used when unauthenticated
* HTTP `403` return code is used when lack of priviledge.
* HTTP `429` return code is used when breaking a request rate limit.
* HTTP `5XX` return codes are used for Phemex internal errors. Note: This doesn't means the operation failed, the
  execution status is **UNKNOWN** and could be Succeed.

<a name="responseformat"/>

### Rest Response format

* All restful API except ***starting*** with `/md` shares same response format.

```
{
  "code": <code>,
  "msg": <msg>,
  "data": <data>
}
```

| Field | Description | 
|-------|------|
| code | 0 means `success`, non-zero means `error`|
| msg  | when code is non-zero, it gives short error description |
| data | operation dependant |

<a name="errorcode"/>

### Error codes

[Trading Error Codes](TradingErrorCode.md)

<a name="httprestheader"/>

## HTTP REST Request Header

Every HTTP Rest Request must have the following Headers:

* x-phemex-access-token : This is ***API-KEY*** (id field) from Phemex site.
* x-phemex-request-expiry : This describes the Unix ***EPoch SECONDS*** to expire the request, normally it should be (
  Now() + 1 minute)
* x-phemex-request-signature : This is HMAC SHA256 signature of the http request. Secret is ***API Secret***, its
  formula is : HMacSha256( URL Path + QueryString + Expiry + body )

Optional Headers:

* x-phemex-request-tracing: a unique string to trace http-request, less than 40 bytes. This header is a must in
  resolving latency issues.

<a name="apiratelimits"/>

## API Rate Limits

* [Order spamming limitations](https://phemex.com/user-guides/order-spamming-limitations)
* RateLimit group of contract trading api is ***CONTRACT***.
* RateLimit Explained [phemex ratelimit docs](/Generic-API-Info.en.md)
* Contract trading api response carries following headers.

```
X-RateLimit-Remaining-CONTRACT, # Remaining request permits in this minute
X-RateLimit-Capacity-CONTRACT, # Request ratelimit capacity
X-RateLimit-Retry-After-CONTRACT, # Reset timeout in seconds for current ratelimited user
```

<a name="securitytype"/>

## Endpoint security type

* Each API call must be signed and pass to server in HTTP header `x-phemex-request-signature`.
* Endpoints use `HMAC SHA256` signatures. The `HMAC SHA256 signature` is a keyed `HMAC SHA256` operation. Use
  your `apiSecret` as the key and the string `URL Path + QueryString + Expiry + body )` as the value for the HMAC
  operation.
* `apiSecret` = `Base64::urlDecode(API Secret)`
* The `signature` is **case sensitive**.

<a name="signatureexample1"/>

### Signature Example 1: HTTP GET Request

* API REST Request URL: https://api.phemex.com/accounts/accountPositions?currency=BTC
    * Request Path: /accounts/accountPositions
    * Request Query: currency=BTC
    * Request Body: <null>
    * Request Expiry: 1575735514
    * Signature: HMacSha256( /accounts/accountPositions + currency=BTC + 1575735514 )

<a name="signatureexample2"/>

### Singature Example 2: HTTP GET Request with multiple query string

* API REST Request
  URL: https://api.phemex.com/orders/activeList?ordStatus=New&ordStatus=PartiallyFilled&ordStatus=Untriggered&symbol=BTCUSD
    * Request Path: /orders/activeList
    * Request Query: ordStatus=New&ordStatus=PartiallyFilled&ordStatus=Untriggered&symbol=BTCUSD
    * Request Body: <null>
    * Request Expire: 1575735951
    * Signature: HMacSha256(/orders/activeList +
      ordStatus=New&ordStatus=PartiallyFilled&ordStatus=Untriggered&symbol=BTCUSD + 1575735951)
    * signed string
      is `/orders/activeListordStatus=New&ordStatus=PartiallyFilled&ordStatus=Untriggered&symbol=BTCUSD1575735951`

<a name="signatureexample3"/>

### Signature Example 3: HTTP POST Request

* API REST Request URL: https://api.phemex.com/orders
    * Request Path: /orders
    * Request Query: <null>
    * Request Body: {"symbol":"BTCUSD","clOrdID":"uuid-1573058952273","side":"Sell","priceEp":93185000,"orderQty":7,"
      ordType":"Limit","reduceOnly":false,"timeInForce":"GoodTillCancel","takeProfitEp":0,"stopLossEp":0}
    * Request Expiry: 1575735514
    * Signature: HMacSha256( /orders + 1575735514 + {"symbol":"BTCUSD","clOrdID":"uuid-1573058952273","side":"Sell","
      priceEp":93185000,"orderQty":7,"ordType":"Limit","reduceOnly":false,"timeInForce":"GoodTillCancel","takeProfitEp":
      0,"stopLossEp":0})
    * signed string
      is `/orders1575735514{"symbol":"BTCUSD","clOrdID":"uuid-1573058952273","side":"Sell","priceEp":93185000,"orderQty":7,"ordType":"Limit","reduceOnly":false,"timeInForce":"GoodTillCancel","takeProfitEp":0,"stopLossEp":0}`

## Request/response field explained

<a name="fieldexplained"/>

### Margin mode and leverage

<a name="marginModeAndLeverage"/>

#### Leverage

* The absolute value of `leverageEr` determines initial-margin-rate, i.e. `initialMarginRate = 1/abs(leverage)`
* The sign of `leverageEr` indicates margin mode, i.e. `leverage <= 0` means `cross-margin-mode`, `leverage > 0`
  means `isolated-margin-mode`.
* The result of setting `leverageEr` to `0` is leverage to maximum leverage supported by user selected risklimit, and
  margin-mode is `cross-margin-mode`.

#### Cross Margin Mode

* `Position margin` includes two parts, one part is balance assigned to position, another part is account available
  balance.
* Position in cross-margin-mode may be affected by other position, because account available balance is shared among all
  positions in cross mode.

#### Isolated Margin Mode

* `Position margin` only includes balance assgined to position, by default it is initial-margin.
* Position in isolatd-margin-mode is independent of other positions.

### Price/Ratio/Value Scales

<a name="scalingfactors"/>

Fields with post-fix "Ep", "Er" or "Ev" have been scaled based on symbol setting.

* Fields with post-fix "Ep" are scaled prices, `priceScale` in [products](#queryproductinfo)
* Fields with post-fix "Er" are scaled ratios, `ratioScale` in [products](#queryproductinfo)
* Fields with post-fix "Ev" are scaled values, `valueScale` of `settleCurrency` in [products](#queryproductinfo)

| Symbol | Price scale | Ratio scale | Value scale | settlement currency |
|--------|-------------|-------------|-------------|---------------------|
| BTCUSD | 10,000      | 100,000,000 | 100,000,000 | BTC                |
| cETHUSD| 10,000      | 100,000,000 | 100,000,000 | ETH                |
| uBTCUSD| 10,000      | 100,000,000 |      10,000 | USD                |
| ETHUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| XRPUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| LINKUSD| 10,000      | 100,000,000 |      10,000 | USD                |
| XTZUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| LTCUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| GOLDUSD| 10,000      | 100,000,000 |      10,000 | USD                |
| ADAUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| BCHUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| COMPUSD| 10,000      | 100,000,000 |      10,000 | USD                |
| ALGOUSD| 10,000      | 100,000,000 |      10,000 | USD                |
| YFIUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| DOTUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| UNIUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| BATUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| CHZUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| MANAUSD| 10,000      | 100,000,000 |      10,000 | USD                |
| ENJUSD | 10,000      | 100,000,000 |      10,000 | USD                |
|SUSHIUSD| 10,000      | 100,000,000 |      10,000 | USD                |
| SNXUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| GRTUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| MKRUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| TRXUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| EOSUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| ONTUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| NEOUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| ZECUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| FILUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| KSMUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| XMRUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| QTUMUSD| 10,000      | 100,000,000 |      10,000 | USD                |
| XLMUSD | 10,000      | 100,000,000 |      10,000 | USD                |
| ATOMUSD| 10,000      | 100,000,000 |      10,000 | USD                |
| LUNAUSD| 10,000      | 100,000,000 |      10,000 | USD                |
| SOLUSD | 10,000      | 100,000,000 |      10,000 | USD                |

<a name="commconsts"/>

### Common constants

* order type

| order type | description |
|-----------|-------------|
| Limit | -- |
| Market | -- |
| Stop | -- |
| StopLimit | -- |
| MarketIfTouched | -- |
| LimitIfTouched | -- |

* order Status

| order status | description | 
|------------|-------------|
| Created | order acked from order request, a transient state |
| Init | Same as `Created`, order acked from order request, a transient state |
| Untriggered | Conditional order waiting to be triggered |
| Triggered | Conditional order being triggered|
| Deactivated | untriggered conditonal order being removed |
| Rejected | Order rejected |
| New | Order placed into orderbook |
| PartiallyFilled | Order partially filled |
| Filled | Order fully filled |
| Canceled | Order canceled |

* TimeInForce

| timeInForce | description |
|------------|-------------|
| GoodTillCancel | -- |
| PostOnly | -- |
| ImmediateOrCancel | -- |
| FillOrKill | -- |

* Execution instruction

| Execution instruction | description |
|------------|-------------|
| ReduceOnly | reduce position size, never increase position size |
| CloseOnTrigger | close the position  |

* Trigger source

| trigger | description |
|------------|-------------|
| ByMarkPrice | trigger by mark price|
| ByLastPrice | trigger by last price |

<a name="restapilist"/>

## REST API List

<a name="marketapilist"/>

### Market API List

<a name="queryproductinfo"/>

#### Query Product Information

* Request：

```
GET /public/products 
```

<a name="orderapilist"/>

### Trade API List

<a name="placeorderwithput"/>

#### Place order with argument in url query string

* Request

```
PUT /orders/create?clOrdID=<clOrdID>&symbol=<symbol>&reduceOnly=<reduceOnly>&closeOnTrigger=<closeOnTrigger>&orderQty=<orderQty>&displayQty=<displayQty>&ordType=<ordType>&priceEp=<priceEp>&side=<side>&text=<text>&timeInForce=<timeInForce>&stopPxEp=<stopPxEp>&takeProfitEp=<takeProfitEp>&stopLossEp=<stopLossEp>&pegOffsetValueEp=<pegOffsetValueEp>&pegPriceType=<pegPriceType>&trailingStopEp=<trailingStopEp>&triggerType=<triggerType>&tpTrigger=<tpTrigger>&tpSlTs=<tpSlTs>&slTrigger=<slTrigger>
```

| Field | Type | Required | Description | Possible values |
|-------|-------|--------|--------------|-----------------|
| symbol | String | Yes | Which symbol to place order | [Trading symbols](#symbpricesub) | 
| clOrdID | String | Yes | client order id, max length is 40| |
| side |  Enum | Yes | Order direction, Buy or Sell | Buy, Sell | 
| orderQty | Integer | Yes | Order quantity | |
| priceEp | Integer | - | Scaled price, required for limit order | | 
| ordType | Enum | - | default to Limit | Market, Limit, Stop, StopLimit, MarketIfTouched, LimitIfTouched| 
| stopPxEp | Integer | - | Trigger price for stop orders | |
| timeInForce | Enum | - | Time in force. default to GoodTillCancel | GoodTillCancel, ImmediateOrCancel, FillOrKill, PostOnly| 
| reduceOnly | Boolean | - | whether reduce position side only. Enable this flag, i.e. reduceOnly=true, position side won't change | true, false |
| closeOnTrigger | Boolean | - | implicitly reduceOnly, plus cancel other orders in the same direction(side) when necessary | true, false|
| triggerType | Enum | - | Trigger source, whether trigger by mark price, index price or last price | ByMarkPrice, ByLastPrice |
| takeProfitEp | Integer | - | Scaled take profit price | |
| stopLossEp | Integer | - | Scaled stop loss price | | 
| slTrigger | Enum | - |Trigger source, by mark-price or last-price | ByMarkPrice, ByLastPrice |
| tpTrigger | Enum | - | Trigger source, by mark-price or last-price | ByMarkPrice, ByLastPrice |
| pegOffsetValueEp | Integer | - | Trailing offset from current price. Negative value when position is long, positive when position is short | |
| pegPriceType | Enum | - | Trailing order price type |TrailingStopPeg, TrailingTakeProfitPeg |

* HTTP Response:

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "bizError": 0,
    "orderID": "ab90a08c-b728-4b6b-97c4-36fa497335bf",
    "clOrdID": "137e1928-5d25-fecd-dbd1-705ded659a4f",
    "symbol": "BTCUSD",
    "side": "Sell",
    "actionTimeNs": 1580547265848034600,
    "transactTimeNs": 0,
    "orderType": null,
    "priceEp": 98970000,
    "price": 9897,
    "orderQty": 1,
    "displayQty": 1,
    "timeInForce": null,
    "reduceOnly": false,
    "stopPxEp": 0,
    "closedPnlEv": 0,
    "closedPnl": 0,
    "closedSize": 0,
    "cumQty": 0,
    "cumValueEv": 0,
    "cumValue": 0,
    "leavesQty": 1,
    "leavesValueEv": 10104,
    "leavesValue": 0.00010104,
    "stopPx": 0,
    "stopDirection": "UNSPECIFIED",
    "ordStatus": "Created"
  }
}
```

* Important fields description
    * Order average filled price, inverse contract:`avgPrice = (cumQty/cumValueEv)/contractSize`; linear
      contract: `avgPrice = (cumValueEv/cumQty)/contractSize`. `contractSize` is fixed in [product](#marketapilist) api.

| Field | Description |
|------|----------|
| bizError | bizError = 0 means processing normally, non-zero values mean wrong state. Separate section to explain these errors; `code` in response is equal to bizError if response contains only one order |
| cumQty | cumulative filled order quantity |
| cumValueEv | cumulative filled order value (scaled) |
| leavesQty | unfilled order quantity | 
| leavesValueEv | unfilled order value |

<a name="orderexample"/>

* More order type examples

    * Stop-loss orders (ordType = Stop/StopLimit) and Take-profit order (ordType = MarketIfTouched/LimitIfTouched)
    * Stop-loss order is triggered when price moves against order-side(buy/sell), while Take-profit order is triggered
      when price moves in profitable direction to order-side(buy/sell).

      | ordType                         | side | parameter requirements            | trigger condition |
      |---------------------------------|------|-----------------------------------|-------------------|
      | Stop/StopLimit                  | Sell |  stopPxEp < last-price/mark-price | last/mark-price <= stopPxEp  |
      | Stop/StopLimit                  | Buy  |  stopPxEp > last-price/mark-price | last/mark-price >= stopPxEp  |
      | MarketIfTouched/LimitIfTouched  | Sell |  stopPxEp > last-price/mark-price | last/mark-price >= stopPxEp  |
      | MarketIfTouched/LimitIfTouched  | Buy  |  stopPxEp < last-price/mark-price | last/mark-price <= stopPxEp  |

    * StopLoss Sell order, triggered order is placed as limit order (Assume current last-price is 30k)

  ```javasript
  {
      "clOrdID": "stop-loss-order-then-limit",
      "symbol": "BTCUSD",
      "side": "Sell",
      "ordType": "StopLimit",
      "triggerType": "ByMarkPrice",
      "stopPxEp": "299550000",         // "trigger price, when ordType= Stop/StopLimit and side = Sell, stopPxEp must less than last-price"
      "priceEp": "299650000",          // "when ordType = StopLimit, priceEp is required, when ordType = Stop, priceEp is not required "
      "orderQty": 10000
  }
  ```

    * StopLoss Buy order, triggered order is placed as market order (Assume current last-price is 30k)

  ```javasript
  {
      "clOrdID": "stop-loss-order-then-market",
      "symbol": "BTCUSD",
      "side": "Buy",
      "ordType": "Stop",
      "triggerType": "ByMarkPrice",
      "stopPxEp": "333550000",         // "trigger price, when ordType = Stop/StopLimit and side = Buy, stopPxEp must be larger than last-price"
      "priceEp": "0",                  // not required 
      "orderQty": 10000
  }

  ```

    * Take-profit Sell order, triggered order is placed as limit order (Assume current last-price is 30k)

  ```javasript
  {
      "clOrdID": "take-profit-order-then-limit",
      "symbol": "BTCUSD",
      "side": "Sell",
      "ordType": "LimitIfTouched",
      "triggerType": "ByMarkPrice",
      "stopPxEp": "333550000",         // "trigger price, when ordType = LimitIfTouched/MarketIfTouched and side = Sell, stopPxEp is larger than last-price"
      "priceEp": "334550000",          // "when ordType = LimitIfTouched, priceEp is required, when ordType = MarketIfTouched, priceEp is not required "
      "orderQty": 10000
  }
  ```

    * Take-profit Buy order, triggered order is placed as market order (Assume current last-price is 30k)

  ```javasript
  {
      "clOrdID": "take-profit-order-then-market",
      "symbol": "BTCUSD",
      "side": "Buy",
      "ordType": "MarketIfTouched",
      "triggerType": "ByLastPrice",
      "stopPxEp": "299550000",         // "when ordType = LimitIfTouched/MarketIfTouched and side = Buy, stopPxEp is less than last-price"
      "priceEp": "0",                  // "not required"
      "orderQty": 10000
  }
  ```

    * Place a order with stop-loss and take-profit

  ```javasript
  {
      "clOrdID": "order-with-take-profit-stop-loss",
      "symbol": "BTCUSD",
      "side": "Buy",
      "priceEp": 300000000,
      "orderQty": 1000,
      "ordType": "Limit",
      "takeProfitEp": 3111100000,
      "tpTrigger": "ByLastPrice",
      "stopLossEp": "299990000",
      "slTrigger": "ByMarkPrice"
  }
  ```

    * Trailing stop order(Assume current position is long, current last-price is 32k)

  ```javasript
  {
    "symbol": "BTCUSD",
    "side": "Sell",                    // assume current position is long
    "ordType": "Stop",
    "orderQty": 0,
    "priceEp": 0,
    "triggerType": "ByLastPrice",
    "stopPxEp": 315000,                // "if position is long, this value should be less than last-price; if position is short, this value is larger than last-price",
    "timeInForce": "ImmediateOrCancel",
    "closeOnTrigger": true, 
    "pegPriceType": "TrailingStopPeg",
    "pegOffsetValueEp": -10000000,     // retraces by $1000.0 from the optimal price, sign is opposite to position side, i.e. Long Position => negative sign; Shot Position => positive sign
    "clOrdID": "cl-order-id"
  }
  ```

    * Trailing stop order with activiation price

  ```javasript
  {
    "symbol": "BTCUSD",
    "side": "Sell",
    "ordType": "Stop",
    "orderQty": 0,
    "priceEp": 0,
    "triggerType": "ByLastPrice",
    "stopPxEp": 340000000,             // activation price of this trailing order, this value should be larger than last-price
    "timeInForce": "ImmediateOrCancel",
    "closeOnTrigger": true,
    "pegPriceType": "TrailingTakeProfitPeg",
    "pegOffsetValueEp": -10000000,     // retraces by $1000.0 from the optimal price, sign is opposite to position side, i.e. Long Position => negative sign; Shot Position => positive sign  
    "clOrdID": "cl-order-id"
  }
  ```

<a name="placeorder"/>

#### Place Order

* HTTP Request:

```
POST /orders
```

```json
{
  "actionBy": "FromOrderPlacement",
  "symbol": "BTCUSD",
  "clOrdID": "uuid-1573058952273",
  "side": "Sell",
  "priceEp": 93185000,
  "orderQty": 7,
  "ordType": "Limit",
  "reduceOnly": false,
  "triggerType": "UNSPECIFIED",
  "pegPriceType": "UNSPECIFIED",
  "timeInForce": "GoodTillCancel",
  "takeProfitEp": 0,
  "stopLossEp": 0,
  "pegOffsetValueEp": 0,
  "pegPriceType": "UNSPECIFIED"
}
```

* Fields are the same as [above place-order](#placeorderwithput)
  <a name="amendorder"/>

#### Amend order by orderID

* Request

```
PUT
/orders/replace?symbol=<symbol>&orderID=<orderID>&origClOrdID=<origClOrdID>&clOrdID=<clOrdID>&price=<price>&priceEp=<priceEp>&orderQty=<orderQty>&stopPx=<stopPx>&stopPxEp=<stopPxEp>&takeProfit=<takeProfit>&takeProfitEp=<takeProfitEp>&stopLoss=<stopLoss>&stopLossEp=<stopLossEp>&pegOffsetValueEp=<pegOffsetValueEp>&pegPriceType=<pegPriceType>
```

| Field  | Required | Description |
|--------|----------|-------------|
| symbol | Yes  | order symbol, cannot be changed|
| orderID| Yes  |order id, cannot be changed |
| origClOrdID | No | original clOrderID |
| clOrdID| No | new clOrdID |
| price  | No | new order price |
| priceEp| No | new order price with scale |
| orderQty | No | new orderQty |
| stopPx | No | new stop price |
| stopPxEp | No | new stop price with scale |
| takeProfit | No | new stop profit price |
| takeProfitEp | No | new stop profit price with scale |
| stopLoss | No | new stop loss price |
| stopLossEp | No | new stop loss price with scale |
| pegOffsetValueEp | No | New trailing offset |
| pegPriceType | No | New peg price type |

* Response
    * amended order

<a name="cancelsingleorder"/>

#### Cancel Single Order by orderID or clOrdID

* Request

```
DELETE /orders/cancel?symbol=<symbol>&orderID=<orderID>
DELETE /orders/cancel?symbol=<symbol>&clOrdID=<clOrdID>
```

This api accepts Either `orderID` or `clOrdID` not both. i.e. it is an error if both parameters are provided.

* Response
    * Full Order
    * This response means cancel operations succeeded not the order is canceled. One needs to query to order to
      determine whether this order has been cancelled or not.

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "bizError": 0,
    "orderID": "2585817b-85df-4dea-8507-5db1920b9954",
    "clOrdID": "4b19fd1e-a1a7-2986-d02a-0288ad5137d4",
    "symbol": "BTCUSD",
    "side": "Buy",
    "actionTimeNs": 1580533179846642700,
    "transactTimeNs": 1580532966633276200,
    "orderType": null,
    "priceEp": 80040000,
    "price": 8004,
    "orderQty": 1,
    "displayQty": 1,
    "timeInForce": null,
    "reduceOnly": false,
    "stopPxEp": 0,
    "closedPnlEv": 0,
    "closedPnl": 0,
    "closedSize": 0,
    "cumQty": 0,
    "cumValueEv": 0,
    "cumValue": 0,
    "leavesQty": 1,
    "leavesValueEv": 12493,
    "leavesValue": 0.00012493,
    "stopPx": 0,
    "stopDirection": "UNSPECIFIED",
    "ordStatus": "New"
  }
}

```

<a name="cancelorder"/>

#### Bulk Cancel Orders

* Request

```
DELETE /orders?symbol=<symbol>&orderID=<orderID1>,<orderID2>,<orderID3>
```

* Response
    * Canceled orders

<a name="cancelall"/>

#### Cancel All Orders

* In order to cancel all orders, include conditional order and active order, one must invoke this API twice with
  different arguments.
* `untriggered=false` to cancel active order including triggerred conditional order.
* `untriggered=true` to cancel conditional order, the order is not triggerred.

* Request

```
DELETE /orders/all?symbol=<symbol>&untriggered=<untriggered>&text=<text>
```

| Field       | Type   | Required  | Description                    | Possible values         |
|-------------|--------|-----------|--------------------------------|-------------------------|
| symbol      | String | Yes       | which Symbol to cancel         | [Trading symbols](#symbpricesub) |
| untriggered | Boolean| No        | default to false, default cancel non-conditional order; if intending to cancel conditional order, set this to true| true,false|
| text        | comments| No       | comments of this operation, limited to 40 characters  |  |

* Response
    * `data` part of response is subject to change, ***DONT*** rely on it

<a name="querytradeaccount"/>

#### Query trading account and positions

* Request

```
GET /accounts/accountPositions?currency=<currency>
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| currency | string | in url query parameter. which trading account | BTC,USD |

* Response

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "account": {
      "accountId": 0,
      "currency": "BTC",
      "accountBalanceEv": 0,
      "totalUsedBalanceEv": 0
    },
    "positions": [
      {
        "accountID": 0,
        "symbol": "BTCUSD",
        "currency": "BTC",
        "side": "None",
        "positionStatus": "Normal",
        "crossMargin": false,
        "leverageEr": 0,
        "leverage": 0,
        "initMarginReqEr": 0,
        "initMarginReq": 0.01,
        "maintMarginReqEr": 500000,
        "maintMarginReq": 0.005,
        "riskLimitEv": 10000000000,
        "riskLimit": 100,
        "size": 0,
        "value": 0,
        "valueEv": 0,
        "avgEntryPriceEp": 0,
        "avgEntryPrice": 0,
        "posCostEv": 0,
        "posCost": 0,
        "assignedPosBalanceEv": 0,
        "assignedPosBalance": 0,
        "bankruptCommEv": 0,
        "bankruptComm": 0,
        "bankruptPriceEp": 0,
        "bankruptPrice": 0,
        "positionMarginEv": 0,
        "positionMargin": 0,
        "liquidationPriceEp": 0,
        "liquidationPrice": 0,
        "deleveragePercentileEr": 0,
        "deleveragePercentile": 0,
        "buyValueToCostEr": 1150750,
        "buyValueToCost": 0.0115075,
        "sellValueToCostEr": 1149250,
        "sellValueToCost": 0.0114925,
        "markPriceEp": 93169002,
        "markPrice": 9316.9002,
        "markValueEv": 0,
        "markValue": null,
        "estimatedOrdLossEv": 0,
        "estimatedOrdLoss": 0,
        "usedBalanceEv": 0,
        "usedBalance": 0,
        "takeProfitEp": 0,
        "takeProfit": null,
        "stopLossEp": 0,
        "stopLoss": null,
        "realisedPnlEv": 0,
        "realisedPnl": null,
        "cumRealisedPnlEv": 0,
        "cumRealisedPnl": null
      }
    ]
  }
}
```

<b>Note</b> `unRealizedPnlEv` needs to be calculated in client side with latest `markPrice`, formula is as below.

```
Inverse long contract: unRealizedPnl = (posSize * contractSize) / avgEntryPrice - (posSize * contractSize) / markPrice
Inverse short contract: unRealizedPnl =  (posSize *contractSize) / markPrice - (posSize * contractSize) / avgEntryPrice 
Linear long contract:  unRealizedPnl = (posSize * contractSize) * markPrice - (posSize * contractSize) * avgEntryPrice
Linear short contract:  unRealizedPnl = (posSize * contractSize) * avgEntryPrice - (posSize * contractSize) * markPrice

posSize is a signed vaule. contractSize is a fixed value.
```

#### Query trading account and positions with unrealized-pnl

<a name="queryPosWithPnl"/>

Below API presents unrealized pnl at `markprice` of positions with **considerable** cost, thus
its [ratelimit](/Generic-API-Info.en.md#contractAPIGroup) weight is very high.

* Request

```
GET /accounts/positions?currency=<currency>
```

* Response

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "account": {
      "accountId": 111100001,
      "currency": "BTC",
      "accountBalanceEv": 879599942377,
      "totalUsedBalanceEv": 285,
      "bonusBalanceEv": 0
    },
    "positions": [
      {
        "accountID": 111100001,
        "symbol": "BTCUSD",
        "currency": "BTC",
        "side": "Buy",
        "positionStatus": "Normal",
        "crossMargin": false,
        "leverageEr": 0,
        "initMarginReqEr": 1000000,
        "maintMarginReqEr": 500000,
        "riskLimitEv": 10000000000,
        "size": 5,
        "valueEv": 26435,
        "avgEntryPriceEp": 189143181,
        "posCostEv": 285,
        "assignedPosBalanceEv": 285,
        "bankruptCommEv": 750000,
        "bankruptPriceEp": 5000,
        "positionMarginEv": 879599192377,
        "liquidationPriceEp": 5000,
        "deleveragePercentileEr": 0,
        "buyValueToCostEr": 1150750,
        "sellValueToCostEr": 1149250,
        "markPriceEp": 238287555,
        "markValueEv": 0,
        "unRealisedPosLossEv": 0,
        "estimatedOrdLossEv": 0,
        "usedBalanceEv": 285,
        "takeProfitEp": 0,
        "stopLossEp": 0,
        "cumClosedPnlEv": -8913353,
        "cumFundingFeeEv": 123996,
        "cumTransactFeeEv": 940245,
        "realisedPnlEv": 0,
        "unRealisedPnlEv": 5452,
        "cumRealisedPnlEv": 0
      }
    ]
  }
}

```

<b>Note</b> Highly recommend calculating `unRealizedPnlEv` in client side with latest `markPrice` to avoid ratelimit
penalty.

<a name="changeleverage"/>

#### Change leverage

* Request

```
PUT /positions/leverage?symbol=<symbol>&leverage=<leverage>&leverageEr=<leverageEr>
```

| Field                | Type   | Description                                | Possible values |
|----------------------|--------|--------------------------------------------|--------------|
| symbol               | string | which postion needs to change              | [Trading symbols](#symbpricesub) |
| leverage             | integer   | unscaled leverage                       |  |
| leverageEr           | integer   | ratio scaled leverage, leverage wins when both leverage and leverageEr provided|  |

* Response

```json
{
  "code": 0,
  "msg": "OK"
}
```

<a name = "changerisklimit"/>

#### Change position risklimit

* Request

```
PUT /positions/riskLimit?symbol=<symbol>&riskLimit=<riskLimit>&riskLimitEv=<riskLimitEv>
```

| Field                | Type   | Description                                | Possible values |
|----------------------|--------|--------------------------------------------|--------------|
| symbol               | string | which postion needs to change              | [Trading symbols](#symbpricesub) |
| riskLimit             | integer   | unscaled value, reference BTC/USD value scale   |  |
| riskLimitEv           | integer   | value scaled risklimit, riskLimitEv wins when both riskLimit and riskLimitEv provided|  |

<a name="assignposbalance"/>

#### Assign position balance in isolated marign mode

* Request

***This API is POST***

```
POST /positions/assign?symbol=<symbol>&posBalance=<posBalance>&posBalanceEv=<posBalanceEv>
```

| Field                | Type   | Description                                | Possible values |
|----------------------|--------|--------------------------------------------|--------------|
| symbol               | string | which postion needs to change              | [Trading symbols](#symbpricesub) |
| posBalance             | integer   | unscaled value                       |  |
| posBalanceEv           | integer   | value scaled for position balance, posBalanceEv wins when both posBalance and posBalanceEv provided|  |

<a name="queryopenorder"/>

#### Query open orders by symbol

* Order status includes `New`, `PartiallyFilled`, `Filled`, `Canceled`, `Rejected`, `Triggered`, `Untriggered`;
* Open order status includes `New`, `PartiallyFilled`, `Untriggered`;

* Request

```
GET /orders/activeList?symbol=<symbol>
```

| Field                | Type   | Description                                | Possible values |
|----------------------|--------|--------------------------------------------|--------------|
| symbol | String | which symbol needs to query | [Trading symbols](#symbpricesub)  |

* Response
    * Full order

```json
{
  "code": 0,
  "msg": "",
  "data": {
    "rows": [
      {
        "bizError": 0,
        "orderID": "9cb95282-7840-42d6-9768-ab8901385a67",
        "clOrdID": "7eaa9987-928c-652e-cc6a-82fc35641706",
        "symbol": "BTCUSD",
        "side": "Buy",
        "actionTimeNs": 1580533011677666800,
        "transactTimeNs": 1580533011677666800,
        "orderType": null,
        "priceEp": 84000000,
        "price": 8400,
        "orderQty": 1,
        "displayQty": 1,
        "timeInForce": null,
        "reduceOnly": false,
        "stopPxEp": 0,
        "closedPnlEv": 0,
        "closedPnl": 0,
        "closedSize": 0,
        "cumQty": 0,
        "cumValueEv": 0,
        "cumValue": 0,
        "leavesQty": 0,
        "leavesValueEv": 0,
        "leavesValue": 0,
        "stopPx": 0,
        "stopDirection": "Falling",
        "ordStatus": "Untriggered"
      },
      {
        "bizError": 0,
        "orderID": "93397a06-e76d-4e3b-babc-dff2696786aa",
        "clOrdID": "71c2ab5d-eb6f-0d5c-a7c4-50fd5d40cc50",
        "symbol": "BTCUSD",
        "side": "Sell",
        "actionTimeNs": 1580532983785506600,
        "transactTimeNs": 1580532983786370300,
        "orderType": null,
        "priceEp": 99040000,
        "price": 9904,
        "orderQty": 1,
        "displayQty": 1,
        "timeInForce": null,
        "reduceOnly": false,
        "stopPxEp": 0,
        "closedPnlEv": 0,
        "closedPnl": 0,
        "closedSize": 0,
        "cumQty": 0,
        "cumValueEv": 0,
        "cumValue": 0,
        "leavesQty": 1,
        "leavesValueEv": 10096,
        "leavesValue": 0.00010096,
        "stopPx": 0,
        "stopDirection": "UNSPECIFIED",
        "ordStatus": "New"
      },
      {
        "bizError": 0,
        "orderID": "2585817b-85df-4dea-8507-5db1920b9954",
        "clOrdID": "4b19fd1e-a1a7-2986-d02a-0288ad5137d4",
        "symbol": "BTCUSD",
        "side": "Buy",
        "actionTimeNs": 1580532966629408500,
        "transactTimeNs": 1580532966633276200,
        "orderType": null,
        "priceEp": 80040000,
        "price": 8004,
        "orderQty": 1,
        "displayQty": 1,
        "timeInForce": null,
        "reduceOnly": false,
        "stopPxEp": 0,
        "closedPnlEv": 0,
        "closedPnl": 0,
        "closedSize": 0,
        "cumQty": 0,
        "cumValueEv": 0,
        "cumValue": 0,
        "leavesQty": 1,
        "leavesValueEv": 12493,
        "leavesValue": 0.00012493,
        "stopPx": 0,
        "stopDirection": "UNSPECIFIED",
        "ordStatus": "New"
      }
    ]
  }
}

```

<a name="queryorder"/>

#### Query closed orders by symbol

* This API is for ***closed*** orders. For open orders, please use [open order query](#queryopenorder)

* Request

```
GET /exchange/order/list?symbol=<symbol>&start=<start>&end=<end>&offset=<offset>&limit=<limit>&ordStatus=<ordStatus>&withCount=<withCount>
```

| Field                | Type   | Description                                | Possible values |
|----------------------|--------|--------------------------------------------|--------------|
| symbol | String | which symbol needs to query | [Trading symbols](#symbpricesub) |
| start  | Integer | start time range, Epoch millis，available only from the last 2 month | |
| end  | Integer | end time range, Epoch millis | |
| offset | Integer | offset to resultset | | 
| limit | Integer | limit of resultset, max 200 | | 
| ordStatus | String | order status list filter | New, PartiallyFilled, Untriggered, Filled, Canceled | 

* Response
    * sample response

```json
{
  "code": 0,
  "msg": "OK",
  "data": {
    "total": 39,
    "rows": [
      {
        "orderID": "7d5a39d6-ff14-4428-b9e1-1fcf1800d6ac",
        "clOrdID": "e422be37-074c-403d-aac8-ad94827f60c1",
        "symbol": "BTCUSD",
        "side": "Sell",
        "orderType": "Limit",
        "actionTimeNs": 1577523473419470300,
        "priceEp": 75720000,
        "price": null,
        "orderQty": 12,
        "displayQty": 0,
        "timeInForce": "GoodTillCancel",
        "reduceOnly": false,
        "takeProfitEp": 0,
        "takeProfit": null,
        "stopLossEp": 0,
        "closedPnlEv": 0,
        "closedPnl": null,
        "closedSize": 0,
        "cumQty": 0,
        "cumValueEv": 0,
        "cumValue": null,
        "leavesQty": 0,
        "leavesValueEv": 0,
        "leavesValue": null,
        "stopLoss": null,
        "stopDirection": "UNSPECIFIED",
        "ordStatus": "Canceled",
        "transactTimeNs": 1577523473425416400
      },
      {
        "orderID": "b63bc982-be3a-45e0-8974-43d6375fb626",
        "clOrdID": "uuid-1577463487504",
        "symbol": "BTCUSD",
        "side": "Sell",
        "orderType": "Limit",
        "actionTimeNs": 1577963507348468200,
        "priceEp": 71500000,
        "price": null,
        "orderQty": 700,
        "displayQty": 700,
        "timeInForce": "GoodTillCancel",
        "reduceOnly": false,
        "takeProfitEp": 0,
        "takeProfit": null,
        "stopLossEp": 0,
        "closedPnlEv": 0,
        "closedPnl": null,
        "closedSize": 0,
        "cumQty": 700,
        "cumValueEv": 9790209,
        "cumValue": null,
        "leavesQty": 0,
        "leavesValueEv": 0,
        "leavesValue": null,
        "stopLoss": null,
        "stopDirection": "UNSPECIFIED",
        "ordStatus": "Filled",
        "transactTimeNs": 1578026629824704800
      }
    ]
  }
}
```

<a name="queryorderbyid"/>

#### Query user order by orderID or Query user order by client order ID

* Request

```
GET /exchange/order?symbol=<symbol>&orderID=<orderID1,orderID2>
GET /exchange/order?symbol=<symbol>&clOrdID=<clOrdID1,clOrdID2>
```

Description : available only from the last 2 month

* Response

```json
{
  "code": 0,
  "msg": "OK",
  "data": [
    {
      "orderID": "7d5a39d6-ff14-4428-b9e1-1fcf1800d6ac",
      "clOrdID": "e422be37-074c-403d-aac8-ad94827f60c1",
      "symbol": "BTCUSD",
      "side": "Sell",
      "orderType": "Limit",
      "actionTimeNs": 1577523473419470300,
      "priceEp": 75720000,
      "price": null,
      "orderQty": 12,
      "displayQty": 0,
      "timeInForce": "GoodTillCancel",
      "reduceOnly": false,
      "takeProfitEp": 0,
      "takeProfit": null,
      "stopLossEp": 0,
      "closedPnlEv": 0,
      "closedPnl": null,
      "closedSize": 0,
      "cumQty": 0,
      "cumValueEv": 0,
      "cumValue": null,
      "leavesQty": 0,
      "leavesValueEv": 0,
      "leavesValue": null,
      "stopLoss": null,
      "stopDirection": "UNSPECIFIED",
      "ordStatus": "Canceled",
      "transactTimeNs": 1577523473425416400
    },
    {
      "orderID": "b63bc982-be3a-45e0-8974-43d6375fb626",
      "clOrdID": "uuid-1577463487504",
      "symbol": "BTCUSD",
      "side": "Sell",
      "orderType": "Limit",
      "actionTimeNs": 1577963507348468200,
      "priceEp": 71500000,
      "price": null,
      "orderQty": 700,
      "displayQty": 700,
      "timeInForce": "GoodTillCancel",
      "reduceOnly": false,
      "takeProfitEp": 0,
      "takeProfit": null,
      "stopLossEp": 0,
      "closedPnlEv": 0,
      "closedPnl": null,
      "closedSize": 0,
      "cumQty": 700,
      "cumValueEv": 9790209,
      "cumValue": null,
      "leavesQty": 0,
      "leavesValueEv": 0,
      "leavesValue": null,
      "stopLoss": null,
      "stopDirection": "UNSPECIFIED",
      "ordStatus": "Filled",
      "transactTimeNs": 1578026629824704800
    }
  ]
}
```

<a name="querytrade"/>

#### Query user trade

* Request

```
GET /exchange/order/trade?symbol=<symbol>&start=<start>&end=<end>&limit=<limit>&offset=<offset>&withCount=<withCount>
```

| Field     | Type     | Required | Description                                                     | Possible Values                 | 
|-----------|----------|----------|-----------------------------------------------------------------|---------------------------------|
| symbol    | String   | Yes      | Trading symbol                                                  | BTCUSD, ETHUSD ...              |
| tradeType | String   | No       | Trade type of execution order                                   | Trade,Funding,AdlTrade,LiqTrade |
| start     | Long     | No       | Epoch time in milli-seconds of range start. available only from the last 2 month                    | --                              |
| end       | Long     | No       | Epoch time in milli-seconds of range end                        | --                              |
| limit     | Integer  | No       | The expected count of returned data-set. Default to 50. Max to 200| --                              |
| offset    | Integer  | No       | Offset of total dataset in a range                              | --                              |
| withCount | Boolean  | No       | A flag to tell if the count of total result set is required     | --                              |

* Response
    * Response of this API includes normal trade, funding records, liquidation, ADL trades,etc. `tradeType` can
      distiguish these types.
    * Sample trade response

```json
{
  "code": 0,
  "msg": "OK",
  "data": {
    "total": 79,
    "rows": [
      {
        "transactTimeNs": 1578026629824704800,
        "symbol": "BTCUSD",
        "currency": "BTC",
        "action": "Replace",
        "side": "Sell",
        "tradeType": "Trade",
        "execQty": 700,
        "execPriceEp": 71500000,
        "orderQty": 700,
        "priceEp": 71500000,
        "execValueEv": 9790209,
        "feeRateEr": -25000,
        "execFeeEv": -2447,
        "ordType": "Limit",
        "execID": "b01671a1-5ddc-5def-b80a-5311522fd4bf",
        "orderID": "b63bc982-be3a-45e0-8974-43d6375fb626",
        "clOrdID": "uuid-1577463487504",
        "execStatus": "MakerFill"
      },
      {
        "transactTimeNs": 1578009600000000000,
        "symbol": "BTCUSD",
        "currency": "BTC",
        "action": "SettleFundingFee",
        "side": "Buy",
        "tradeType": "Funding",
        "execQty": 700,
        "execPriceEp": 69473435,
        "orderQty": 0,
        "priceEp": 0,
        "execValueEv": 10075793,
        "feeRateEr": 4747,
        "execFeeEv": 479,
        "ordType": "UNSPECIFIED",
        "execID": "381fbe21-a116-472d-a547-9e2368dcc194",
        "orderID": "00000000-0000-0000-0000-000000000000",
        "clOrdID": "SettlingFunding",
        "execStatus": "Init"
      }
    ]
  }
}

```

* Possible trade types

|TradeTypes| Description |
|---------|--------------|
| Trade | Normal trades |
| Funding | Funding on positions |
| AdlTrade |  Auto-delevearage trades |
| LiqTrade | Liquidation trades |

<a name="mdapilist"/>

### Market Data API List

<a name="queryorderbook"/>

#### Query Order Book

* Request：

```
GET /md/orderbook?symbol=<symbol>
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| symbol      | String | Contract symbol name                       | [Trading symbols](#symbpricesub) |

* Response:

```javascript
{
  "error": null,
  "id": 0,
  "result": {
    "book": {
      "asks": [
        [
          <priceEp>,
          <size>
        ],
        ...
        ...
        ...
      ],
      "bids": [
        [
          <priceEp>,
          <size>
        ],
        ...
        ...
        ...
      ]
    ]
    },
    "depth": 30,
    "sequence": <sequence>,
    "timestamp": <timestamp>,
    "symbol": "<symbol>",
    "type": "snapshot"
  }
}
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| timestamp   | Integer| Timestamp in nanoseconds                   |              |
| priceEp     | Integer| Scaled book level price                    |              |
| size        | Integer| Scaled book level size                     |              |
| sequence    | Integer| current message sequence                   |              |
| symbol      | String | Contract symbol name                       | [Trading symbols](#symbpricesub) |

* Sample：

```
GET /md/orderbook?symbol=BTCUSD
```

```json
{
  "error": null,
  "id": 0,
  "result": {
    "book": {
      "asks": [
        [
          87705000,
          1000000
        ],
        [
          87710000,
          200000
        ]
      ],
      "bids": [
        [
          87700000,
          2000000
        ],
        [
          87695000,
          200000
        ]
      ]
    },
    "depth": 30,
    "sequence": 455476965,
    "timestamp": 1583555482434235628,
    "symbol": "BTCUSD",
    "type": "snapshot"
  }
}
```

<a name="querykline"/>

### Query kline

NOTE:

1. please be noted that kline interfaces
   have [rate limits](https://github.com/phemex/phemex-api-docs/blob/master/Generic-API-Info.en.md#rate-limits) rule,
   please check the Other group
   under [api groups](https://github.com/phemex/phemex-api-docs/blob/master/Generic-API-Info.en.md#api-groups)

```
GET /exchange/public/md/v2/kline?symbol=<symbol>&resolution=<resolution>&limit=<limit>
```

* Response

```javascript
{
  "code": 0,
  "msg": "OK",
  "data": {
    "total": -1,
    "rows": [
      [
        <timestamp>,
        <interval>,
        <last_close>,
        <open>,
        <high>,
        <low>,
        <close>,
        <volume>,
        <turnover>
      ],
      [
        ...
      ]
    ]
  }
}
```

* Request

| Field      | Type    | Required | Description     | Possible Values                         |
|------------|---------|----------|-----------------|-----------------------------------------|
| symbol     | String  | Yes      | symbol name     | BTCUSD,ETHUSD,uBTCUSD,cETHUSD,XRPUSD... | 
| resolution | Integer | Yes      | kline interval  | described as below                      |
| limit      | Integer | No       | limit of result | described as below                      | 

* Value of `resolution`s

|resolution|Description |
|----------|------------|
|60|MINUTE_1|
|300|MINUTE_5|
|900|MINUTE_15|
|1800|MINUTE_30|
|3600|HOUR_1|
|14400|HOUR_4|
|86400|DAY_1|
|604800|WEEK_1|
|2592000|MONTH_1|
|7776000|SEASON_1|
|31104000|YEAR_1|

* Value of `limit`s

| limit    | Description |
|----------|-------------|
| 5        | limit 5     |
| 10       | limit 10    |
| 50      | limit 50    |
| 100     | limit 100   |
| 500     | limit 500   |
| 1000    | limit 1000  |

**NOTE**, for backward compatibility reason, phemex also provides kline query with from/to, however, this interface
is **NOT** recommended.

```
GET /exchange/public/md/kline?symbol=<symbol>&to=<to>&from=<from>&resolution=<resolution>

```

| Field       | Type    | Required    | Description            | Possible Values                                                                                                |
|-------------|---------|-------------|------------------------|----------------------------------------------------------------------------------------------------------------|
|symbol       | String  | Yes         | symbol name            | BTCUSD,ETHUSD,uBTCUSD,cETHUSD,XRPUSD...                                                                        | 
| from        | Integer | Yes         | start time in seconds  | value aligned in resolution boundary                                                                           |
| to          | Integer | Yes         | end time in seconds    | value aligned in resolution boundary; Number of k-lines return between [`from`, `to`) should be less than 1000 | 
| resolution  | Integer | Yes         | kline interval         | the same as described above                                                                                    |

<a name="querytrades"/>

#### Query Recent Trades

* Request：

```
GET /md/trade?symbol=<symbol>
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| symbol      | String | Contract symbol name                       | [Trading symbols](#symbpricesub) |

* Response:

```javascript
{
  "error": null,
  "id": 0,
  "result": {
    "type": "snapshot",
    "sequence": <sequence>,
    "symbol": "<symbol>",
    "trades": [
      [
        <timestamp>,
        "<side>",
        <priceEp>,
        <size>
      ],
      ...
      ...
      ...
    ]
  }
}

```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| timestamp   | Integer| Timestamp in nanoseconds                   |              |
| side        | String | Trade side string                          | Buy, Sell    |
| priceEp     | Integer| Scaled trade price                         |              |
| size        | Integer| Scaled trade size                          |              |
| sequence    | Integer| Current message sequence                   |              |
| symbol      | String | Contract symbol name                       | [Trading symbols](#symbpricesub) |

* Sample：

```
GET /md/trade?symbol=BTCUSD
```

```json
{
  "error": null,
  "id": 0,
  "result": {
    "sequence": 15934323,
    "symbol": "BTCUSD",
    "trades": [
      [
        1579164056368538508,
        "Sell",
        86960000,
        121
      ],
      [
        1579164055036820552,
        "Sell",
        86960000,
        58
      ]
    ],
    "type": "snapshot"
  }
}
```

<a name="query24hrsticker"/>

#### Query 24 Hours Ticker

* Request：

```
GET v1/md/ticker/24hr?symbol=<symbol>
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| symbol      | String | Contract symbol name                       | [Trading symbols](#symbpricesub) |

* Response:

```javascript
{
  "error": null,
  "id": 0,
  "result": {
      "askEp": <best ask priceEp>,
      "bidEp": <best bid priceEp>,
      "fundingRateEr": <funding rateEr>,
      "highEp": <high priceEp>,
      "indexEp": <index priceEp>,
      "lastEp": <last priceEp>,
      "lowEp": <low priceEp>,
      "markEp": <mark priceEp>,
      "openEp": <open priceEp>,
      "openInterest": <open interest>,
      "predFundingRateEr": <predicated funding rateEr>,
      "symbol": <symbol>,
      "timestamp": <timestamp>,
      "turnoverEv": <turnoverEv>,
      "volume": <volume>
  }
}
```

| Field         | Type   | Description                                | Possible values |
|---------------|--------|--------------------------------------------|--------------|
| open priceEp  | Integer| The scaled open price in last 24 hours     |              |
| high priceEp  | Integer| The scaled highest price in last 24 hours  |              |
| low priceEp   | Integer| The scaled lowest price in last 24 hours   |              |
| close priceEp | Integer| The scaled close price in last 24 hours    |              |
| index priceEp | Integer| Scaled index price                         |              |
| mark priceEp  | Integer| Scaled mark price                          |              |
| open interest | Integer| current open interest                      |              |
| funding rateEr| Integer| Scaled funding rate                        |              |
| predicated funding rateEr| Integer| Scaled predicated funding rate  |              |
| timestamp     | Integer| Timestamp in nanoseconds                   |              |
| symbol        | String | Contract symbol name                       | [Trading symbols](#symbpricesub) |
| turnoverEv    | Integer| The scaled turnover value in last 24 hours |              |
| volume        | Integer| Symbol trade volume in last 24 hours       |              |

* Sample：

```
GET v1/md/ticker/24hr?symbol=BTCUSD
```

```json
{
  "error": null,
  "id": 0,
  "result": {
    "close": 87425000,
    "fundingRate": 10000,
    "high": 92080000,
    "indexPrice": 87450676,
    "low": 87130000,
    "markPrice": 87453092,
    "open": 90710000,
    "openInterest": 7821141,
    "predFundingRate": 7609,
    "symbol": "BTCUSD",
    "timestamp": 1583646442444219017,
    "turnover": 1399362834123,
    "volume": 125287131
  }
}
```

<a name="queryhisttrades"/>

#### Query History Trades By symbol

* Query History trades by symbol
* RateLimit of this api is 5 per second

```
GET /exchange/public/nomics/trades?market=<symbol>&since=<since>
```

| Field  | Type     | Description                                                       | Possible values                   |
|--------|----------|-------------------------------------------------------------------|-----------------------------------|
| market | String   | the market of symbol                                              |[Trading symbols](#scalingfactors) |
| since  | String   | Last id of response field, 0-0-0 is from the very initial trade   | default 0-0-0                     |
| start  | Integer  | Epoch time in milli-seconds of range start                        |                                   |
| end    | Integer  | Epoch time in milli-seconds of range end                          |                                   |

* Response

```json
{
  "code": 0,
  "data": [
    {
      "id": "string",
      "amount_quote": "string",
      "price": "string",
      "side": "string",
      "timestamp": "string",
      "type": "string"
    }
  ],
  "msg": "string"
}
```

* Sample

```json
{
  "code": 0,
  "msg": "OK",
  "data": [
    {
      "id": "1183-3-2",
      "timestamp": "2019-11-24T08:32:17.046Z",
      "price": "7211.00000000",
      "amount_quote": "1",
      "side": "sell",
      "type": "limit"
    },
    {
      "id": "1184-2-1",
      "timestamp": "2019-11-24T08:32:17.047Z",
      "price": "7211.00000000",
      "amount_quote": "1",
      "side": "buy",
      "type": "limit"
    }
  ]
}
```

<a name="assetapilist"/>

### Asset API list

* Asset includes BTC in wallets, BTC in btc-trading account, USD in usd-trading account.
* In wallet level, Main/parent client can transfer BTC between Sub-client and main/parent client.
* In wallet level, Sub client can *only* transfer self BTC to main/parent client wallet.
* client can *only* transfer its own asset between wallet and trading accounts.

<a name="clientwalletquery"/>

#### Query client and wallets

* Request

```
/phemex-user/users/children?offset=<offset>&limit=<limit>&withCount=<withCount>
```

* Response

```json
{
  "code": 0,
  "msg": "OK",
  "data": {
    "total": 87,
    "rows": [
      {
        "userId": 612,
        "email": "x**@**.com",
        "nickName": "nickName",
        "passwordState": 1,
        "clientCnt": 0,
        "totp": 1,
        "logon": 0,
        "parentId": 0,
        "parentEmail": null,
        "status": 1,
        "wallet": {
          "totalBalance": "989.25471319",
          "totalBalanceEv": 98925471319,
          "availBalance": "989.05471319",
          "availBalanceEv": 98905471319,
          "freezeBalance": "0.20000000",
          "freezeBalanceEv": 20000000,
          "currency": "BTC",
          "currencyCode": 1
        },
        "userMarginVo": [
          {
            "currency": "BTC",
            "accountBalance": "3.90032508",
            "totalUsedBalance": "0.00015666",
            "accountBalanceEv": 390032508,
            "totalUsedBalanceEv": 15666,
            "bonusBalanceEv": 0,
            "bonusBalance": "0"
          },
          {
            "currency": "USD",
            "accountBalance": "38050.35000000",
            "totalUsedBalance": "0.00000000",
            "accountBalanceEv": 380503500,
            "totalUsedBalanceEv": 0,
            "bonusBalanceEv": 0,
            "bonusBalance": "0"
          }
        ]
      },
      ...
    ]
  }
}
```

Wallet fields

| Field | Type | Description | 
|-------|------|-------------|
| currency | String | currency name |
| totalBalanceEv | Integer | scaled balance amount value |
| availBalanceEv | Integer | scaled available balance value |
| freezeBalanceEv | Integer | scaled used balance value |

Margin fields

| Field | Type | Description |
|-------|------|-------------|
| currency | String | currency name |
| accountBalanceEv | Integer | scaled trading account balance value |
| totalUsedBalanceEv | Integer | Scaled used trading account balance value |
| bonusBalanceEv | Integer | Scaled bonus value |

<a name="walletransferout"/>

#### Main/parent-client transfer self wallet balance to sub-client wallet. (Or Subclient transfer self wallet balance to main/parent client wallet )

* Request
    * Main/parent can transfer its wallet balance to its own subclients.
    * Sub-client can only transfer its wallet balance to its parent/main client.
    * When sub-client transfer its wallet balance, `clientCnt = 0`

```
POST: /exchange/wallets/transferOut
```

```javascript
{
    "amount": 0,                       // unscaled amount
    "amountEv": 0,                     // scaled amount, when both amount and amountEv are provided, amountEv wins.
    "clientCnt": 0,                    // client number, this is from API in children list; when sub-client issues this API, client must be 0.
    "currency": "string"
}

```

| Field | Type |  Required | Description |
|-------|-----|---------|---------------|
| amount | Integer | - | unscaled amount value to transfer |
| amountEv | Integer | - | scaled amount value to transfer |
| clientCnt | Integer | Yes | which client to transfer |
| currency | String | Yes | currency name, currently only support BTC |

* Response
    * This API is synchrous, `code == 0` means succeeded. If timed-out, history can be queried.

```json
{
  "code": 0,
  "msg": "OK",
  "data": "OK"
}
```

<a name="walletransferin"/>

#### Transfer from sub-client wallet. Only main/parent client has priviledge.

* Request

```
POST: /exchange/wallets/transferIn
```

```json
{
    "amountEv":10000000,
    "currency":"BTC",
    "clientCnt":1
}
```

* Response

```json
{
  "code": 0,
  "msg": "OK",
  "data": "OK"
}
```

<a name="futureDataApiList"/>

### Future Data API List

<a name="futureDataFundingFeesHist"/>

#### Query Funding Fees History

* Http Request

```
GET /api-data/futures/funding-fees?symbol=<symbol>
```

| Field    | Type           | Required | Description               | Possible Values                 |
|----------|----------------|----------|---------------------------|---------------------------------|
| symbol   | String         | True     | the currency to query     | uBTCUSD ...                     |
| offset   | Integer        | False    | page start from 0         | start from 0, default 0         |
| limit    | Integer        | False    | page size                 | default 20, max 200             |

* Response

```json
[
  {
    "createTime": 0,
    "currency": "string",
    "execFeeEv": 0,
    "execPriceEp": 0,
    "execQty": 0,
    "execValueEv": 0,
    "feeRateEr": 0,
    "fundingRateEr": 0,
    "side": "string",
    "symbol": "string"
  }
]
```

<a name="futureDataOrdersHist"/>

#### Query Orders History

* Http Request

```
GET /api-data/futures/orders?symbol=<symbol>
```

| Field    | Type           | Required | Description               | Possible Values                 |
|----------|----------------|----------|---------------------------|---------------------------------|
| symbol   | String         | True     | the currency to query     | uBTCUSD ...                     |
| start    | Long           | False    | start time in millisecond | default 2 days ago from the end |
| end      | Long           | False    | end time in millisecond   | default now                     |
| offset   | Integer        | False    | page start from 0         | start from 0, default 0         |
| limit    | Integer        | False    | page size                 | default 20, max 200             |

* Response

```json
[
  {
    "actionTimeNs": 0,
    "bizError": 0,
    "clOrdID": "string",
    "closedPnlEv": 0,
    "closedSize": 0,
    "cumQty": 0,
    "cumValueEv": 0,
    "displayQty": 0,
    "leavesQty": 0,
    "leavesValueEv": 0,
    "ordStatus": "string",
    "orderID": "string",
    "orderQty": 0,
    "orderType": "string",
    "priceEp": 0,
    "reduceOnly": true,
    "side": "string",
    "stopDirection": "string",
    "stopLossEp": 0,
    "symbol": "string",
    "takeProfitEp": 0,
    "timeInForce": "string",
    "transactTimeNs": 0
  }
]
```

<a name="futureDataOrdersByIds"/>

#### Query Orders By Ids

* Http Request

```
GET /api-data/futures/orders/by-order-id?symbol=<symbol>
```

| Field    | Type     | Required | Description            | Possible Values                                                                                                                     |
|----------|----------|----------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
| symbol   | String   | True     | the currency to query  | uBTCUSD ...                                                                                                                         |
| orderID  | String   | False    | order id               | orderID and clOrdID can not be both empty. If both IDs are given, it will return list of orders which match both orderID or clOrdID |
| clOrdID  | String   | False    | client order id        | refer to orderID                                                                                                                    |

* Response

```json
[
  {
    "actionTimeNs": 0,
    "bizError": 0,
    "clOrdID": "string",
    "closedPnlEv": 0,
    "closedSize": 0,
    "cumQty": 0,
    "cumValueEv": 0,
    "displayQty": 0,
    "leavesQty": 0,
    "leavesValueEv": 0,
    "ordStatus": "string",
    "orderID": "string",
    "orderQty": 0,
    "orderType": "string",
    "priceEp": 0,
    "reduceOnly": true,
    "side": "string",
    "stopDirection": "string",
    "stopLossEp": 0,
    "symbol": "string",
    "takeProfitEp": 0,
    "timeInForce": "string",
    "transactTimeNs": 0
  }
]
```

<a name="futureDataTradesHist"/>

#### Query Trades History

* Http Request

```
GET /api-data/futures/trades?symbol=<symbol>
```

| Field    | Type           | Required | Description               | Possible Values                 |
|----------|----------------|----------|---------------------------|---------------------------------|
| symbol   | String         | True     | the currency to query     | uBTCUSD ...                     |
| start    | Long           | False    | start time in millisecond | default 2 days ago from the end |
| end      | Long           | False    | end time in millisecond   | default now                     |
| offset   | Integer        | False    | page start from 0         | start from 0, default 0         |
| limit    | Integer        | False    | page size                 | default 20, max 200             |

* Response

```json
[
  {
    "action": "string",
    "clOrdID": "string",
    "closedPnlEv": 0,
    "closedSize": 0,
    "currency": "string",
    "execFeeEv": 0,
    "execID": "string",
    "execPriceEp": 0,
    "execQty": 0,
    "execStatus": "string",
    "execValueEv": 0,
    "feeRateEr": 0,
    "ordType": "string",
    "orderID": "string",
    "orderQty": 0,
    "priceEp": 0,
    "side": "string",
    "symbol": "string",
    "tradeType": "string",
    "transactTimeNs": 0
  }
]
```

<a name="futureDataTradingFeesHist"/>

#### Query Trading Fees History

* Http Request

```
GET /api-data/futures/trading-fees?symbol=<symbol>
```

| Field    | Type           | Required | Description               | Possible Values                 |
|----------|----------------|----------|---------------------------|---------------------------------|
| symbol   | String         | True     | the currency to query     | uBTCUSD ...                     |
| offset   | Integer        | False    | page start from 0         | start from 0, default 0         |
| limit    | Integer        | False    | page size                 | default 20, max 200             |

* Response

```json
[
  {
    "createTime": 0,
    "currency": "string",
    "exchangeFeeValueEv": 0,
    "id": 0,
    "makerRateEr": 0,
    "makerValueEv": 0,
    "symbol": "string",
    "takerRateEr": 0,
    "takerValueEv": 0,
    "userId": 0
  }
]
```


<a name="futureDataTradingAccountDetail"/>

#### Query Trading Account Detail

* Http Request

```
GET /api-data/futures/v2/tradeAccountDetail?currency=<currecny>&type=<type>&limit=<limit>&offset=<offset>&start=<start>&end=<end>&withCount=<withCount>
```

| Field     | Type      | Required | Description                    | Possible Values    |
|-----------|-----------|----------|--------------------------------|--------------------|
| currency  | String    | False    | the currency to query          | USDT、USD、BTC、ETH |
| type      | Integer   | False    | TradeAccountBizType Enum       |                    |
| start     | Integer   | False    | start time range, Epoch millis | default 0          |
| end       | Integer   | False    | end time range, Epoch millis   | default 0          |
| offset    | Integer   | False    | offset to resultset, max 1000  | default 0          |
| limit     | Integer   | False    | limit of resultset             | default 20         |
| withCount | Integer   | False    | result with total count        | default false      |

* Response

```json
[
  {
    "createTime": 0,
    "currency": "string",
    "exchangeFeeValueEv": 0,
    "id": 0,
    "makerRateEr": 0,
    "makerValueEv": 0,
    "symbol": "string",
    "takerRateEr": 0,
    "takerValueEv": 0,
    "userId": 0
  }
]
```

<a name="withdraw"/>

### Withdraw

* Several restrictions are required for withdraw: 1. bind Google 2FA, 2. Password change out of 24hour, 3. meet minimum
  BTC amount requirement.

<a name="requestwithdraw"/>

#### Request Withdraw

* Request

```
POST /exchange/wallets/createWithdraw?otpCode=<otpCode>
```

```javascript
{
  "address": <address>,                // address must set before withdraw
  "amountEv": <amountEv>,              // scaled btc value
  "currency": <currency>               // fixed to BTC 
}
```

| Filed | Type | Required |  Description | Possible values |
|------|------|----------|--------------|-----------------|
| otpCode | String | Yes | In URL query, From Google 2FA| |
| address | String | Yes | In body, address must be saved before hand | |
| amountEv | Integer | Yes | In body, scaled amount value | |
| currency | String | Yes | In body, currently only support BTC | |

* Sample code to get Google 2FA code via API

```java
api 'com.warrenstrange:googleauth:1.1.2'

import com.warrenstrange.googleauth.GoogleAuthenticator;

@Test
public void testAuth() {
    String secret = "XXXXXXXXXXXXXXXX"; // save from binding Google 2FA
    GoogleAuthenticator gAuth = new GoogleAuthenticator();
    int code = gAuth.getTotpPassword(secret);
    boolean ans = gAuth.authorize(secret, code);
    Assert.assertTrue(ans);
}

```

* Response

```javascript
{
    "code": 0,
    "msg" : "OK",
    "data": <withdrawRequest> 
}
```

Response Fileds

| Filed | Type | Description |
|-------|------|-------------|
| id    | Integer | withdraw id |
| currency | String | currency name |
| status | String | Withdraw request processing state |
| amountEv | Integer | Scaled withdraw amount |
| feeEv | Integer | Scaled withdraw fee amount |
| address | String | Withdraw target address |
| txhash | String | transaction hash on blockchain |
| submitedAt | Integer | submitted time in epoch |
| expiredTime | Integer | expire time in epoch |

<a name="confirmwithdraw"/>

#### Confirm withdraw

* After withdraw request submitted, a confirmation link is sent to registration email. The confirm code should be
  extracted out from the link and then passed in as url query parameter.

* Request

```
GET /exchange/wallets/confirm/withdraw?code=<withdrawConfirmCode>
```

* Response

```javascript
{
    "code": 0,
    "msg" : "OK"
}
```

<a name="cancelwithdraw"/>

#### Cancel withdraw

* Withdraw request can be canceled before mannual `review`;

* Request

```
POST /exchange/wallets/cancelWithdraw
```

```javascript
{
    id: <withdrawRequestId>
}
```

<a name="listwithdraw"/>

#### List withdraws

* Request

```
GET /exchange/wallets/withdrawList?currency=<currency>&limit=<limit>&offset=<offset>&withCount=<withCount>
```

* Response
    * List of withdraw requests

<a name="withdrawaddrmgmt"/>

#### Withdraw address management

* Withdraw address management support create, remove and list. Recommend manage it from website.

* Request

```
POST /exchange/wallets/createWithdrawAddress?otpCode={optCode}
```

```javascript
{
    "address": <address>,
    "currency": <currency>
    "remark": <name>
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| address | String | Yes | valid BTC address |
| currency | String | Yes | Currrently only support `BTC` |
| remark | String | Yes | Name of this address |

* Response

```javascript
{
    "code": 0,
    "msg": "OK",
    "data": 1                //subject to change
}

```

<a name="wsapi"/>

# Websocket API Standards

<a name="sessionmanagement"/>

## Session Management

* Each client is required to actively send heartbeat (ping) message to Phemex data gateway ('DataGW' in short) with
  interval less than 30 seconds, otherwise DataGW will drop the connection. If a client sends a ping message, DataGW
  will reply with a pong message.
* Clients can use WS built-in ping message or the application level ping message to DataGW as heartbeat. The heartbeat
  interval is recommended to be set as *5 seconds*, and actively reconnect to DataGW if don't receive messages in *3
  heartbeat intervals*.

<a name="wsapiratelimits"/>

## API Rate Limits

* Each Client has concurrent connection limit to *5* in maximum.
* Each connection has subscription limit to *20* in maximum.
* Each connection has throttle limit to *20* request/s.

<a name="wsapilist"/>

## WebSocket API List

<a name="heartbeat"/>

### Heartbeat

* Request：

```javascript
{
  "id": <id>,
  "method": "server.ping",
  "params": []
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": "pong"
}
```

* Sample：

```javascript
> {
  "id": 1234,
  "method": "server.ping",
  "params": []
}

< {
  "error": null,
  "id": 1234,
  "result": "pong"
}
```

<a name="apiuserauth"/>

### API User Authentication

Market trade/orderbook are published publicly without user authentication.
While for client private account/position/order data, the client should send user.auth message to Data Gateway to
authenticate the session.

* Request

```javascript
{
  "method": "user.auth",
  "params": [
    "API",
    "<token>",
    "<signature>",
    <expiry>
  ],
  "id": 1234
}
```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| type        | String | Token type       | API             |
| token       | String | API Key     |                 |
| signature   | String | Signature generated by a funtion as HMacSha256(API Key + expiry) with ***API Secret*** ||
| expiry      | Integer| A future time after which request will be rejected, in epoch ***second***. Maximum expiry is request time plus 2 minutes ||

* Sample:

```javascript
> {
  "method": "user.auth",
  "params": [
    "API",
    "806066b0-f02b-4d3e-b444-76ec718e1023",
    "8c939f7a6e6716ab7c4240384e07c81840dacd371cdcf5051bb6b7084897470e",
    1570091232
  ],
  "id": 1234
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

<a name="booksub"/>

### Subscribe 30-Levels OrderBook

On each successful subscription, DataGW will immediately send the current Order Book snapshot to client and all later
order book updates will be published.
Incremental messages are published with **depth=30 and 20ms interval**. 

* Request

```javascript
{
  "id": <id>,
  "method": "orderbook.subscribe",
  "params": [
    "<symbol>"
  ]
}
```

* Response

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample：

```javascript
> {
  "id": 1234,
  "method": "orderbook.subscribe",
  "params": [
    "BTCUSD"
  ]
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

<a name="booksub2"/>

### Subscribe Full OrderBook

On each successful subscription, DataGW will immediately send the current Order Book snapshot to client and all later
order book updates will be published.
Incremental messages are published with **full depth and 100ms interval**. 

* Request

```javascript
{
  "id": <id>,
  "method": "orderbook.subscribe",
  "params": [
    "<symbol>",
    true
  ]
}
```

* Response

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample：

```javascript
> {
  "id": 1234,
  "method": "orderbook.subscribe",
  "params": [
    "BTCUSD",
    true
  ]
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

#### OrderBook Message:

DataGW publishes order book message with types: incremental, snapshot. And snapshot messages are published with 60-second interval for client self-verification.

* Message Format：

```javascript
{
  "book": {
    "asks": [
      [
        <priceEp>,
        <qty>
      ],
      .
      .
      .
    ],
    "bids": [
      [
        <priceEp>,
        <qty>
      ],
      .
      .
      .
    ]
  },
  "depth": <depth>,
  "sequence": <sequence>,
  "timestamp": <timestamp>,
  "symbol": "<symbol>",

```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| side        | String | Price level side | bid, ask        |
| priceEp     | Integer| Scaled price     |                 |
| qty         | Integer| Price level size. Non-zero qty indicates price level insertion or updation, and qty 0 indicates price level deletion. |                 |
| sequence    | Integer| Latest message sequence |          |
| depth       | Integer| Market depth     | 30              |
| type        | String | Message type     | snapshot, incremental |

* Sample：

```javascript
< {"book":{"asks":[[86765000,19609],[86770000,7402],[86775000,3807],[86780000,7395],[86785000,3599],[86790000,7253],[86795000,4019],[86800000,4366],[86805000,3216],[86810000,3107],[86815000,7453],[86820000,1771],[86825000,895],[86830000,3420],[86835000,1818],[86840000,1272],[86845000,1064],[86850000,195],[86855000,1630],[86860000,1017],[86865000,3509],[86870000,1105],[86875000,1262],[86880000,893],[86885000,862],[86890000,1030],[86895000,2315],[86900000,2994],[86905000,2026],[86910000,3387],[86915000,1382],[86920000,1202],[86925000,3150],[86930000,1773],[86935000,1778],[86940000,1384],[86945000,1842],[86950000,1019],[86955000,2660],[86960000,1599],[86965000,920],[86970000,1834],[86975000,752],[86980000,1384],[86985000,2471],[86990000,2133],[86995000,2981],[87000000,1091],[87005000,994],[87010000,1217],[87015000,1098],[87020000,526],[87025000,1779],[87030000,1098],[87035000,892],[87040000,2168],[87045000,822],[87050000,2410],[87055000,630],[87060000,1684],[87065000,2556],[87070000,19],[87080000,1445],[87085000,29],[87105000,2002],[87115000,658],[87120000,660],[87905000,991]],"bids":[[86760000,18995],[86755000,6451],[86750000,5311],[86745000,6867],[86740000,6180],[86735000,3127],[86730000,4852],[86725000,6213],[86720000,3902],[86715000,4510],[86710000,10063],[86705000,1118],[86700000,1891],[86695000,767],[86690000,20920],[86685000,2535],[86680000,1105],[86675000,645],[86670000,1424],[86665000,1773],[86660000,1464],[86655000,1160],[86650000,1462],[86645000,2446],[86640000,538],[86635000,506],[86630000,2291],[86625000,2981],[86620000,1712],[86615000,984],[86610000,1058],[86605000,1261],[86600000,1074],[86595000,1408],[86590000,717],[86585000,1582],[86580000,1950],[86575000,1540],[86570000,2960],[86565000,598],[86560000,759],[86555000,1266],[86550000,1943],[86545000,259],[86540000,2106],[86535000,2365],[86530000,857],[86525000,1200],[86520000,2371],[86515000,2103],[86510000,1468],[86505000,747],[86500000,1369],[86495000,2121],[86490000,3674],[86485000,1345],[86480000,1290],[86475000,1716],[86470000,1851],[86465000,1861],[86460000,1092],[86435000,21],[86430000,986],[86420000,1202],[86415000,22],[86405000,1199],[86390000,470],[86365000,920],[86360000,192],[86355000,474],[86350000,1838],[86335000,1104],[86285000,2205],[86280000,2390],[86275000,95],[86255000,2836],[86250000,589],[86240000,424],[86235000,937],[86225000,374],[86220000,1591],[86215000,517],[86210000,559],[86205000,702],[86190000,54]]},"depth":30,"sequence":1191904,"symbol":"BTCUSD","type":"snapshot"}
< {"book":{"asks":[[86775000,4621]],"bids":[]},"depth":30,"sequence":1191905,"symbol":"BTCUSD","type":"incremental"}
< {"book":{"asks":[],"bids":[[86755000,8097]]},"depth":30,"sequence":1191906,"symbol":"BTCUSD","type":"incremental"}
```

<a name="bookunsub"/>

### Unsubscribe OrderBook

It unsubscribes all orderbook related subscriptions.

* Request

```javascript
{
  "id": <id>,
  "method": "orderbook.unsubscribe",
  "params": []
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

<a name="tradesub"/>

### Subscribe Trade

On each successful subscription, DataGW will send the 200 history trades immediately for the subscribed symbol and all
the later trades will be published.

* Request

```javascript
{
  "id": <id>,
  "method": "trade.subscribe",
  "params": [
    "<symbol>"
  ]
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample:

```javascript
> {
  "id": 1234,
  "method": "trade.subscribe",
  "params": [
    "BTCUSD"
  ]
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

#### Trade Message Format：

DataGW publishes trade message with types: incremental, snapshot. Incremental messages are published with 20ms interval.
And snapshot messages are published on connection initial setup for client recovery.

```javascript
{
  "trades": [
    [
      <timestamp>,
      "<side>",
      <priceEp>,
      <qty>
    ],
    .
    .
    .
  ],
  "sequence": <sequence>,
  "symbol": "<symbol>",
  "type": "<type>"
}
```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| timestamp   | Integer| Timestamp in nanoseconds for each trade ||
| side        | String | Execution taker side| bid, ask        |
| priceEp     | Integer| Scaled execution price  |                 |
| qty         | Integer| Execution size   |                 |
| sequence    | Integer| Latest message sequence ||
| symbol      | String | Contract symbol name     ||
| type        | String | Message type     |snapshot, incremental |

* Sample

```javascript
< {
  "sequence": 1167852,
  "symbol": "BTCUSD",
  "trades": [
    [
      1573716998128563500,
      "Buy",
      86735000,
      56
    ],
    [
      1573716995033683000,
      "Buy",
      86735000,
      52
    ],
    [
      1573716991485286000,
      "Buy",
      86735000,
      51
    ],
    [
      1573716988636291300,
      "Buy",
      86735000,
      12
    ]
  ],
  "type": "snapshot"
}

< {
  "sequence": 1188273,
  "symbol": "BTCUSD",
  "trades": [
    [
      1573717116484024300,
      "Buy",
      86730000,
      21
    ]
  ],
  "type": "incremental"
}
```

<a name="tradeunsub"/>

### Unsubscribe Trade

It unsubscribes all trade subscriptions or for a symbol.

* Request

```javascript
# unsubscribe all trade subsciptions
{
  "id": <id>,
  "method": "trade.unsubscribe",
  "params": [
  ]
}

# unsubscribe all trade subsciptions for a symbol
{
  "id": <id>,
  "method": "trade.unsubscribe",
  "params": [
    "<symbol>"
  ]
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

<a name="klinesub"/>

### Subscribe Kline

On each successful subscription, DataGW will send the 1000 history klines immediately for the subscribed symbol and all
the later kline update will be published in real-time.

* Request

```javascript
{
  "id": <id>,
  "method": "kline.subscribe",
  "params": [
    "<symbol>",
    "<interval>"
  ]
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample:

```javascript
# subscribe 1-day kline
> {
  "id": 1234,
  "method": "kline.subscribe",
  "params": [
    "BTCUSD",
    86400
  ]
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

#### Kline Message Format：

DataGW publishes kline message with types: incremental, snapshot. Incremental messages are published with 20ms interval.
And snapshot messages are published on connection initial setup for client recovery.

```javascript
{
  "kline": [
    [
      <timestamp>,
      "<interval>",
      <lastCloseEp>,
      <openEp>,
      <highEp>,
      <lowEp>,
      <closeEp>,
      <volume>,
      <turnoverEv>,
    ],
    .
    .
    .
  ],
  "sequence": <sequence>,
  "symbol": "<symbol>",
  "type": "<type>"
}
```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| timestamp   | Integer| Timestamp in nanoseconds for each trade ||
| interval    | Integer| Kline interval type      | 60, 300, 900, 1800, 3600, 14400, 86400, 604800, 2592000, 7776000, 31104000 |
| lastCloseEp | Integer| Scaled last close price  |                 |
| openEp      | Integer| Scaled open price        |                 |
| highEp      | Integer| Scaled high price        |                 |
| lowEp       | Integer| Scaled low price         |                 |
| closeEp     | Integer| Scaled close price       |                 |
| volume      | Integer| Trade voulme during the current kline interval ||
| turnoverEv  | Integer| Scaled turnover value    |                 |
| sequence    | Integer| Latest message sequence  ||
| symbol      | String | Contract symbol name     ||
| type        | String | Message type     |snapshot, incremental |

* Sample

```javascript
< {
  "kline": [
    [
      1590019200,
      86400,
      95165000,
      95160000,
      95160000,
      95160000,
      95160000,
      164,
      1723413
    ],
    [
      1589932800,
      86400,
      97840000,
      97840000,
      98480000,
      92990000,
      95165000,
      246294692,
      2562249857942
    ],
    [
      1589846400,
      86400,
      97335000,
      97335000,
      99090000,
      94490000,
      97840000,
      212484260,
      2194232158593
    ]
  ],
  "sequence": 1118993873,
  "symbol": "BTCUSD",
  "type": "snapshot"
}

< {
  "kline": [
    [
      1590019200,
      86400,
      95165000,
      95160000,
      95750000,
      92585000,
      93655000,
      84414679,
      892414738605
    ]
  ],
  "sequence": 1122006398,
  "symbol": "BTCUSD",
  "type": "incremental"
}
```

<a name="klineunsub"/>

### Unsubscribe Kline

It unsubscribes all kline subscriptions or for a symbol.

* Request

```javascript
# unsubscribe all Kline subscriptions
{
  "id": <id>,
  "method": "kline.unsubscribe",
  "params": []
}

# unsubscribe all Kline subscriptions of a symbol
{
  "id": <id>,
  "method": "kline.unsubscribe",
  "params": [
    "<symbol>"
  ]
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

<a name="aopsub"/>

### Subscribe Account-Order-Position (AOP)

AOP subscription requires the session been authorized successfully. DataGW extracts the user information from the given
token and sends AOP messages back to client accordingly. 0 or more latest account snapshot messages will be sent to
client immediately on subscription, and incremental messages will be sent for later updates. Each account snapshot
contains a trading account information, holding positions, and open / max 100 closed / max 100 filled order event
message history.

* Request

```javascript
{
  "id": <id>,
  "method": "aop.subscribe",
  "params": []
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample

```javascript
> {
  "id": 1234,
  "method": "aop.subscribe",
  "params": []
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

#### Account-Order-Position (AOP) Message Sample:

```javascript
{
  "accounts": [
    {
      "accountBalanceEv": 9992165009,
      "accountID": 604630001,
      "currency": "BTC",
      "totalUsedBalanceEv": 10841771568,
      "userID": 60463
    }
  ],
  "orders": [
    {
      "accountID": 604630001,
      ...
    }
  ],
  "positions": [
    {
      "accountID": 604630001,
      ...
    }
  ],
  "sequence": 11450,
  "timestamp": <timestamp>,
  "type": "<type>"
}

```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| timestamp   | Integer| Transaction timestamp in nanoseconds | |
| sequence    | Integer| Latest message sequence |          |
| symbol      | String | Contract symbol name    |          |
| type        | String | Message type     | snapshot, incremental |

* Sample:

```javascript
< {"accounts":[{"accountBalanceEv":100000024,"accountID":675340001,"bonusBalanceEv":0,"currency":"BTC","totalUsedBalanceEv":1222,"userID":67534}],"orders":[{"accountID":675340001,"action":"New","actionBy":"ByUser","actionTimeNs":1573711481897337000,"addedSeq":1110523,"bonusChangedAmountEv":0,"clOrdID":"uuid-1573711480091","closedPnlEv":0,"closedSize":0,"code":0,"cumQty":2,"cumValueEv":23018,"curAccBalanceEv":100000005,"curAssignedPosBalanceEv":0,"curBonusBalanceEv":0,"curLeverageEr":0,"curPosSide":"Buy","curPosSize":2,"curPosTerm":1,"curPosValueEv":23018,"curRiskLimitEv":10000000000,"currency":"BTC","cxlRejReason":0,"displayQty":2,"execFeeEv":-5,"execID":"92301512-7a79-5138-b582-ac185223727d","execPriceEp":86885000,"execQty":2,"execSeq":1131034,"execStatus":"MakerFill","execValueEv":23018,"feeRateEr":-25000,"lastLiquidityInd":"AddedLiquidity","leavesQty":0,"leavesValueEv":0,"message":"No error","ordStatus":"Filled","ordType":"Limit","orderID":"e9a45803-0af8-41b7-9c63-9b7c417715d9","orderQty":2,"pegOffsetValueEp":0,"priceEp":86885000,"relatedPosTerm":1,"relatedReqNum":2,"side":"Buy","stopLossEp":0,"stopPxEp":0,"symbol":"BTCUSD","takeProfitEp":0,"timeInForce":"GoodTillCancel","tradeType":"Trade","transactTimeNs":1573712555309040417,"userID":67534},{"accountID":675340001,"action":"New","actionBy":"ByUser","actionTimeNs":1573711490507067000,"addedSeq":1110980,"bonusChangedAmountEv":0,"clOrdID":"uuid-1573711488668","closedPnlEv":0,"closedSize":0,"code":0,"cumQty":3,"cumValueEv":34530,"curAccBalanceEv":100000013,"curAssignedPosBalanceEv":0,"curBonusBalanceEv":0,"curLeverageEr":0,"curPosSide":"Buy","curPosSize":5,"curPosTerm":1,"curPosValueEv":57548,"curRiskLimitEv":10000000000,"currency":"BTC","cxlRejReason":0,"displayQty":3,"execFeeEv":-8,"execID":"80899855-5b95-55aa-b84e-8d1052f19886","execPriceEp":86880000,"execQty":3,"execSeq":1131408,"execStatus":"MakerFill","execValueEv":34530,"feeRateEr":-25000,"lastLiquidityInd":"AddedLiquidity","leavesQty":0,"leavesValueEv":0,"message":"No error","ordStatus":"Filled","ordType":"Limit","orderID":"7e03cd6b-e45e-48d9-8937-8c6628e7a79d","orderQty":3,"pegOffsetValueEp":0,"priceEp":86880000,"relatedPosTerm":1,"relatedReqNum":3,"side":"Buy","stopLossEp":0,"stopPxEp":0,"symbol":"BTCUSD","takeProfitEp":0,"timeInForce":"GoodTillCancel","tradeType":"Trade","transactTimeNs":1573712559100655668,"userID":67534},{"accountID":675340001,"action":"New","actionBy":"ByUser","actionTimeNs":1573711499282604000,"addedSeq":1111025,"bonusChangedAmountEv":0,"clOrdID":"uuid-1573711497265","closedPnlEv":0,"closedSize":0,"code":0,"cumQty":4,"cumValueEv":46048,"curAccBalanceEv":100000024,"curAssignedPosBalanceEv":0,"curBonusBalanceEv":0,"curLeverageEr":0,"curPosSide":"Buy","curPosSize":9,"curPosTerm":1,"curPosValueEv":103596,"curRiskLimitEv":10000000000,"currency":"BTC","cxlRejReason":0,"displayQty":4,"execFeeEv":-11,"execID":"0be06645-90b8-5abe-8eb0-dca8e852f82f","execPriceEp":86865000,"execQty":4,"execSeq":1132422,"execStatus":"MakerFill","execValueEv":46048,"feeRateEr":-25000,"lastLiquidityInd":"AddedLiquidity","leavesQty":0,"leavesValueEv":0,"message":"No error","ordStatus":"Filled","ordType":"Limit","orderID":"66753807-9204-443d-acf9-946d15d5bedb","orderQty":4,"pegOffsetValueEp":0,"priceEp":86865000,"relatedPosTerm":1,"relatedReqNum":4,"side":"Buy","stopLossEp":0,"stopPxEp":0,"symbol":"BTCUSD","takeProfitEp":0,"timeInForce":"GoodTillCancel","tradeType":"Trade","transactTimeNs":1573712618104628671,"userID":67534}],"positions":[{"accountID":675340001,"assignedPosBalanceEv":0,"avgEntryPriceEp":86875941,"bankruptCommEv":75022,"bankruptPriceEp":90000,"buyLeavesQty":0,"buyLeavesValueEv":0,"buyValueToCostEr":1150750,"createdAtNs":0,"crossSharedBalanceEv":99998802,"cumClosedPnlEv":0,"cumFundingFeeEv":0,"cumTransactFeeEv":-24,"currency":"BTC","dataVer":4,"deleveragePercentileEr":0,"displayLeverageEr":1000000,"estimatedOrdLossEv":0,"execSeq":1132422,"freeCostEv":0,"freeQty":-9,"initMarginReqEr":1000000,"lastFundingTime":1573703858883133252,"lastTermEndTime":0,"leverageEr":0,"liquidationPriceEp":90000,"maintMarginReqEr":500000,"makerFeeRateEr":0,"markPriceEp":86786292,"orderCostEv":0,"posCostEv":1115,"positionMarginEv":99925002,"positionStatus":"Normal","riskLimitEv":10000000000,"sellLeavesQty":0,"sellLeavesValueEv":0,"sellValueToCostEr":1149250,"side":"Buy","size":9,"symbol":"BTCUSD","takerFeeRateEr":0,"term":1,"transactTimeNs":1573712618104628671,"unrealisedPnlEv":-107,"updatedAtNs":0,"usedBalanceEv":1222,"userID":67534,"valueEv":103596}],"sequence":1310812,"timestamp":1573716998131003833,"type":"snapshot"}
< {"accounts":[{"accountBalanceEv":99999989,"accountID":675340001,"bonusBalanceEv":0,"currency":"BTC","totalUsedBalanceEv":1803,"userID":67534}],"orders":[{"accountID":675340001,"action":"New","actionBy":"ByUser","actionTimeNs":1573717286765750000,"addedSeq":1192303,"bonusChangedAmountEv":0,"clOrdID":"uuid-1573717284329","closedPnlEv":0,"closedSize":0,"code":0,"cumQty":0,"cumValueEv":0,"curAccBalanceEv":100000024,"curAssignedPosBalanceEv":0,"curBonusBalanceEv":0,"curLeverageEr":0,"curPosSide":"Buy","curPosSize":9,"curPosTerm":1,"curPosValueEv":103596,"curRiskLimitEv":10000000000,"currency":"BTC","cxlRejReason":0,"displayQty":4,"execFeeEv":0,"execID":"00000000-0000-0000-0000-000000000000","execPriceEp":0,"execQty":0,"execSeq":1192303,"execStatus":"New","execValueEv":0,"feeRateEr":0,"leavesQty":4,"leavesValueEv":46098,"message":"No error","ordStatus":"New","ordType":"Limit","orderID":"e329ae87-ce80-439d-b0cf-ad65272ed44c","orderQty":4,"pegOffsetValueEp":0,"priceEp":86770000,"relatedPosTerm":1,"relatedReqNum":5,"side":"Buy","stopLossEp":0,"stopPxEp":0,"symbol":"BTCUSD","takeProfitEp":0,"timeInForce":"GoodTillCancel","transactTimeNs":1573717286765896560,"userID":67534},{"accountID":675340001,"action":"New","actionBy":"ByUser","actionTimeNs":1573717286765750000,"addedSeq":1192303,"bonusChangedAmountEv":0,"clOrdID":"uuid-1573717284329","closedPnlEv":0,"closedSize":0,"code":0,"cumQty":4,"cumValueEv":46098,"curAccBalanceEv":99999989,"curAssignedPosBalanceEv":0,"curBonusBalanceEv":0,"curLeverageEr":0,"curPosSide":"Buy","curPosSize":13,"curPosTerm":1,"curPosValueEv":149694,"curRiskLimitEv":10000000000,"currency":"BTC","cxlRejReason":0,"displayQty":4,"execFeeEv":35,"execID":"8d1848a2-5faf-52dd-be71-9fecbc8926be","execPriceEp":86770000,"execQty":4,"execSeq":1192303,"execStatus":"TakerFill","execValueEv":46098,"feeRateEr":75000,"lastLiquidityInd":"RemovedLiquidity","leavesQty":0,"leavesValueEv":0,"message":"No error","ordStatus":"Filled","ordType":"Limit","orderID":"e329ae87-ce80-439d-b0cf-ad65272ed44c","orderQty":4,"pegOffsetValueEp":0,"priceEp":86770000,"relatedPosTerm":1,"relatedReqNum":5,"side":"Buy","stopLossEp":0,"stopPxEp":0,"symbol":"BTCUSD","takeProfitEp":0,"timeInForce":"GoodTillCancel","tradeType":"Trade","transactTimeNs":1573717286765896560,"userID":67534}],"positions":[{"accountID":675340001,"assignedPosBalanceEv":0,"avgEntryPriceEp":86843828,"bankruptCommEv":75056,"bankruptPriceEp":130000,"buyLeavesQty":0,"buyLeavesValueEv":0,"buyValueToCostEr":1150750,"createdAtNs":0,"crossSharedBalanceEv":99998186,"cumClosedPnlEv":0,"cumFundingFeeEv":0,"cumTransactFeeEv":11,"currency":"BTC","dataVer":5,"deleveragePercentileEr":0,"displayLeverageEr":1000000,"estimatedOrdLossEv":0,"execSeq":1192303,"freeCostEv":0,"freeQty":-13,"initMarginReqEr":1000000,"lastFundingTime":1573703858883133252,"lastTermEndTime":0,"leverageEr":0,"liquidationPriceEp":130000,"maintMarginReqEr":500000,"makerFeeRateEr":0,"markPriceEp":86732335,"orderCostEv":0,"posCostEv":1611,"positionMarginEv":99924933,"positionStatus":"Normal","riskLimitEv":10000000000,"sellLeavesQty":0,"sellLeavesValueEv":0,"sellValueToCostEr":1149250,"side":"Buy","size":13,"symbol":"BTCUSD","takerFeeRateEr":0,"term":1,"transactTimeNs":1573717286765896560,"unrealisedPnlEv":-192,"updatedAtNs":0,"usedBalanceEv":1803,"userID":67534,"valueEv":149694}],"sequence":1315725,"timestamp":1573717286767188294,"type":"incremental"}
```

<a name="aopsubv1"/>

### Subscribe Account-Order-Position (AOP) v1

AOP subscription v1 requires the session been authorized successfully. DataGW extracts the user information from the given token and sends AOP messages back to client accordingly. 0 or more latest account snapshot messages will be sent to client immediately on subscription, and incremental messages will be sent for later updates. Each account snapshot contains a trading account information, holding positions, events, and open / limited closed / limited filled order event message history.

* Request

```
{
"id": <id>,
"method": "aop_v1.subscribe",
"params": [
  <close/fills limit>,
  <publish_0_size_positions>
  <skip_0_fields>]
}
```

* Response:

```
{
"error": null,
"id": <id>,
"result": {
  "status": "success"
}
}
```

* Sample
```
> {
  "id": 1234,
  "method": "aop_v1.subscribe",
  "params": [5, true, false]
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```




#### Account-Order-Position (AOP) Message Sample:

```javascript
{"accounts": [{ "accountBalanceEv": 999998500550, "accountID": 11324490004, "bonusBalanceEv": 0, "currency": "ETH",  "totalUsedBalanceEv": 302173448, "userID": 1132449  } ],"events": [],"orders": {"closed": [ { "accountID": 11324490004,...}], "fills": [ { "accountID": 11324490004,... } ],"open": [ { "accountID": 11324490004,... }   ]},"positions": [  {   "accountID": 11324490004,...}], "sequence": 115915989, "timestamp": <timestamp>, "type": "<type>", "version": "v1"}

```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| timestamp   | Integer| Transaction timestamp in nanoseconds | |
| sequence    | Integer| Latest message sequence |          |
| symbol      | String | Contract symbol name    |          |
| type        | String | Message type     | snapshot, incremental |
| version     | String | Message version  | v1 |



* Sample:

```
{"accounts":[{"accountBalanceEv":304011000007611398,"accountID":11324490001,"bonusBalanceEv":0,"currency":"BTC","totalUsedBalanceEv":100032635,"userID":1132449}],"events":[],"orders":{"closed":[{"accountID":11324490001,"bonusChangedAmountEv":0,"clOrdID":"38a54851-f5a5-91a2-c86f-343caded0384","closedPnlEv":0,"closedSize":0,"code":0,"cumQty":1000000,"cumValueEv":2367167637,"currency":"BTC","cxlRejReason":0,"displayQty":0,"leavesQty":0,"leavesValueEv":0,"ordStatus":"Filled","ordType":"Limit","orderID":"06518c40-6fb2-4e95-9d91-e8342de6d2e1","orderQty":1000000,"pegOffsetValueEp":0,"priceEp":422455000,"side":"Buy","slTrigger":"ByMarkPrice","stopLossEp":0,"stopPxEp":0,"symbol":"BTCUSD","takeProfitEp":0,"timeInForce":"GoodTillCancel","tpTrigger":"ByLastPrice","transactTimeNs":1647935193813494272,"userID":1132449},{"accountID":11324490001,"bonusChangedAmountEv":0,"clOrdID":"6bb07b9c-c171-6c8d-eeb3-8f4ef870ae8e","closedPnlEv":0,"closedSize":0,"code":11081,"cumQty":0,"cumValueEv":0,"currency":"BTC","cxlRejReason":0,"displayQty":0,"leavesQty":1000000,"leavesValueEv":2367116024,"ordStatus":"Rejected","ordType":"Limit","orderID":"84682434-ac59-4a23-8915-193295f81913","orderQty":1000000,"pegOffsetValueEp":0,"priceEp":422455000,"side":"Buy","slTrigger":"ByMarkPrice","stopLossEp":0,"stopPxEp":0,"symbol":"BTCUSD","takeProfitEp":0,"timeInForce":"GoodTillCancel","tpTrigger":"ByLastPrice","transactTimeNs":1647935206668239427,"userID":1132449}],"fills":[{"accountID":11324490001,"bonusChangedAmountEv":0,"currency":"BTC","execFeeEv":1100230,"execID":"6b72f087-1bc4-5ad2-8de7-0fcb948e3238","execPriceEp":422445000,"execQty":619715,"execSeq":1045041976,"execStatus":"TakerFill","execValueEv":1466972031,"ordType":"Limit","orderID":"06518c40-6fb2-4e95-9d91-e8342de6d2e1","orderQty":1000000,"priceEp":422455000,"side":"Buy","symbol":"BTCUSD","tradeType":"Trade","transactTimeNs":1647935193813494272,"userID":1132449},{"accountID":11324490001,"bonusChangedAmountEv":0,"currency":"BTC","execFeeEv":535137,"execID":"659de6ab-e4dd-5e5d-b5c3-654a2db8b5cb","execPriceEp":422445000,"execQty":301421,"execSeq":1045041976,"execStatus":"TakerFill","execValueEv":713515368,"ordType":"Limit","orderID":"06518c40-6fb2-4e95-9d91-e8342de6d2e1","orderQty":1000000,"priceEp":422455000,"side":"Buy","symbol":"BTCUSD","tradeType":"Trade","transactTimeNs":1647935193813494272,"userID":1132449}],"open":[]},"positions":[{"accountID":11324490001,"assignedPosBalanceEv":100032635,"avgEntryPriceEp":419422835,"bankruptCommEv":585024000000,"bankruptPriceEp":5000,"buyLeavesQty":0,"buyLeavesValueEv":0,"buyValueToCostEr":1150750,"createdAtNs":0,"crossSharedBalanceEv":304010999907578763,"cumClosedPnlEv":18515572,"cumFundingFeeEv":0,"cumTransactFeeEv":10904174,"curTermRealisedPnlEv":7612065,"currency":"BTC","dataVer":27,"deleveragePercentileEr":0,"displayLeverageEr":1000000,"estimatedOrdLossEv":0,"execSeq":1045041976,"freeCostEv":0,"freeQty":-3900160,"initMarginReqEr":1000000,"lastFundingTime":1647415223469509283,"lastTermEndTime":1647423491682801920,"leverageEr":0,"liquidationPriceEp":5000,"maintMarginReqEr":500000,"makerFeeRateEr":0,"markPriceEp":422792875,"orderCostEv":0,"posCostEv":100032635,"positionMarginEv":304010414983611398,"positionStatus":"Normal","riskLimitEv":10000000000,"sellLeavesQty":0,"sellLeavesValueEv":0,"sellValueToCostEr":1149250,"side":"Buy","size":3900160,"symbol":"BTCUSD","takerFeeRateEr":0,"term":2,"transactTimeNs":1647935206668239427,"unrealisedPnlEv":74120406,"updatedAtNs":0,"usedBalanceEv":100032635,"userID":1132449,"valueEv":9298873779}],"sequence":849885032,"timestamp":1647949615819850918,"type":"snapshot","version":"v1"}

```


<a name="aopunsub"/>

### Unsubscribe Account-Order-Position (AOP)

* Request：

```javascript
{
  "id": <id>,
  "method": "aop.unsubscribe",
  "params": []
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

<a name="tickersub"/>

### Subscribe 24 Hours Ticker

On each successful subscription, DataGW will publish 24-hour ticker metrics for all symbols every 1 second.

* Request

```javascript
{
  "id": <id>,
  "method": "market24h.subscribe",
  "params": []
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample:

```javascript
> {
  "method": "market24h.subscribe",
  "params": [],
  "id": 1234
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

#### Hours Ticker Message Format：

```javascript
{
  "market24h": {
    "open": <open priceEp>,
    "high": <high priceEp>,
    "low": <low priceEp>,
    "close": <close priceEp>,
    "indexPrice": <index priceEp>,
    "markPrice": <mark priceEp>,
    "openInterest": <open interest>,
    "fundingRate": <funding rateEr>,
    "predFundingRate": <predicated funding rateEr>,
    "symbol": "<symbol>",
    "turnover": <turnoverEv>,
    "volume": <volume>
  },
  "timestamp": <timestamp>
}
```

| Field         | Type   | Description                                | Possible values |
|---------------|--------|--------------------------------------------|--------------|
| open priceEp  | Integer| The scaled open price in last 24 hours     |              |
| high priceEp  | Integer| The scaled highest price in last 24 hours  |              |
| low priceEp   | Integer| The scaled lowest price in last 24 hours   |              |
| close priceEp | Integer| The scaled close price in last 24 hours    |              |
| index priceEp | Integer| Scaled index price                         |              |
| mark priceEp  | Integer| Scaled mark price                          |              |
| open interest | Integer| current open interest                      |              |
| funding rateEr| Integer| Scaled funding rate                        |              |
| predicated funding rateEr| Integer| Scaled predicated funding rate  |              |
| timestamp     | Integer| Timestamp in nanoseconds                   |              |
| symbol        | String | Contract symbol name                       | [Trading symbols](#symbpricesub) |
| turnoverEv    | Integer| The scaled turnover value in last 24 hours |              |
| volume        | Integer| Symbol trade volume in last 24 hours       |              |

* Sample:

```javascript
{
  "market24h": {
    "close": 87425000,
    "fundingRate": 10000,
    "high": 92080000,
    "indexPrice": 87450676,
    "low": 87130000,
    "markPrice": 87453092,
    "open": 90710000,
    "openInterest": 7821141,
    "predFundingRate": 7609,
    "symbol": "BTCUSD",
    "timestamp": 1583646442444219017,
    "turnover": 1399362834123,
    "volume": 125287131
  },
  "timestamp": 1576490244024818000
}
```

<a name="symbpricesub"/>

### Subscribe tick event for symbol price

* Every trading symbol has a suite of other symbols, each symbol follows same patterns,
  i.e. `index` symbol follows a pattern `.<BASECURRENCY>`,
  `mark` symbol follows a pattern `.M<BASECURRENCY>`,
  predicated funding rate's symbol follows a pattern `.<BASECURRENCY>FR`,
  while funding rate symbol follows a pattern `.<BASECURRENCY>FR8H`
* Price is retrieved by subscribing symbol tick.
* all available symbols (pfr=predicated funding rate)

   | symbol      | index symbol |  mark symbol  | pfr symbol   | funding rate symbol |
   |-------------|--------------|---------------|--------------|---------------------|
   | BTCUSD      | .BTC         | .MBTC         | .BTCFR       | .BTCFR8H            |
   | XRPUSD      | .XRP         | .MXRP         | .XRPFR       | .XRPFR8H            |
   | ETHUSD      | .ETH         | .METH         | .ETHFR       | .ETHFR8H            |
   | LINKUSD     | .LINK        | .MLINK        | .LINKFR      | .LINKFR8H           |
   | XTZUSD      | .XTZ         | .MXTZ         | .XTZFR       | .XTZFR8H            |
   | LTCUSD      | .LTC         | .MLTC         | .LTCFR       | .LTCFR8H            |
   | GOLDUSD     | .GOLD        | .MGOLD        | .GOLDFR      | .GOLDFR8H           |
   | ADAUSD      | .ADA         | .MADA         | .ADAFR       | .ADAFR8H            |
   | BCHUSD      | .BCH         | .MBCH         | .BCHFR       | .BCHFR8H            |
   | COMPUSD     | .COMP        | .MCOMP        | .COMPFR      | .COMPFR8H           |
   | ALGOUSD     | .ALGO        | .MALGO        | .ALGOFR      | .ALGOFR8H           |
   | YFIUSD      | .YFI         | .MYFI         | .YFIFR       | .YFIFR8H            |
   | DOTUSD      | .DOT         | .MDOT         | .DOTFR       | .DOTFR8H            |
   | UNIUSD      | .UNI         | .MUNI         | .UNIFR       | .UNIFR8H            |
   | BATUSD      | .BAT         | .MBAT         | .BATFR       | .BATFR8H            |
   | CHZUSD      | .CHZ         | .MCHZ         | .CHZFR       | .CHZFR8H            |
   | MANAUSD     | .MANA        | .MMANA        | .MANAFR      | .MANAFR8H           |
   | ENJUSD      | .ENJ         | .MENJ         | .ENJFR       | .ENJFR8H            |
   | SUSHIUSD    | .SUSHI       | .MSUSHI       | .SUSHIFR     | .SUSHIFR8H          |
   | SNXUSD      | .SNX         | .MSNX         | .SNXFR       | .SNXFR8H            |
   | GRTUSD      | .GRT         | .MGRT         | .GRTFR       | .GRTFR8H            |
   | MKRUSD      | .MKR         | .MMKR         | .MKRFR       | .MKRFR8H            |
   | TRXUSD      | .TRX         | .MTRX         | .TRXFR       | .TRXFR8H            |
   | EOSUSD      | .EOS         | .MEOS         | .EOSFR       | .EOSFR8H            |
   | ONTUSD      | .ONT         | .MONT         | .ONTFR       | .ONTFR8H            |
   | NEOUSD      | .NEO         | .MNEO         | .NEOFR       | .NEOFR8H            |
   | ZECUSD      | .ZEC         | .MZEC         | .ZECFR       | .ZECFR8H            |
   | FILUSD      | .FIL         | .MFIL         | .FILFR       | .FILFR8H            |
   | KSMUSD      | .KSM         | .MKSM         | .KSMFR       | .KSMFR8H            |
   | XMRUSD      | .XMR         | .MXMR         | .XMRFR       | .XMRFR8H            |
   | QTUMUSD     | .QTUM        | .MQTUM        | .QTUMFR      | .QTUMFR8H           |
   | XLMUSD      | .XLM         | .MXLM         | .XLMFR       | .XLMFR8H            |
   | ATOMUSD     | .ATOM        | .MATOM        | .ATOMFR      | .ATOMFR8H           |
   | LUNAUSD     | .LUNA        | .MLUNA        | .LUNAFR      | .LUNAFR8H           |
   | SOLUSD      | .SOL         | .MSOL         | .SOLFR       | .SOLFR8H            |
   | u1000RSRUSD | .u1000RSR    | .Mu1000RSR    | .u1000RSRFR  | .u1000RSRFR8H       |

* Request

    * The symbol in params can be replaced by any symbol.

```javascript
{
  "method": "tick.subscribe",
  "params": [
    <symbol>
  ],
  "id": <id>
}
```

* Response

ack message

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

push event

```javascript
{
  "tick": {
    "last": <priceEp>,
    "scale": <scale>,
    "symbol": <symbol>
    "timestamp": <timestamp_nano>
  }
}
```

* Sample

```javascript
{"method":"tick.subscribe","params":[".BTC"],"id":1580631267153}
{"error":null,"id":1580631267153,"result":{"status":"success"}}
{"tick":{"last":93385362,"scale":4,"symbol":".BTC","timestamp":1580635719408000000}}
{"tick":{"last":93390304,"scale":4,"symbol":".BTC","timestamp":1580635719821000000}}
{"tick":{"last":93403484,"scale":4,"symbol":".BTC","timestamp":1580635721424000000}}
```

## Table of Contents

* [Phemex Public API](#publicapi)
    * [General Public API Information](#general)
* [REST API Standards](#restapi)
    * [HTTP Restful Response](#restresponse)
        * [HTTP Return Codes](#httpreturncodes)
        * [HTTP Restful Response Format](#responseformat)
        * [Restful Response Error Codes](#errorcode)
    * [HTTP REST Request Header](#httprestheader)
    * [API Rate Limits](#apiratelimits)
    * [Endpoint security type](#securitytype)
        * [Signature Example 1: HTTP GET Request](#signatureexample1)
        * [Singature Example 2: HTTP GET Request with multiple query string](#signatureexample2)
        * [Signature Example 3: HTTP POST Request](#signatureexample3)
    * [Request/Response field explained](#fieldexplained)
        * [Spot currency and Symbol](#spotCurrencySym)
        * [Common constants](#commconsts)
    * [REST API List](#restapilist)
        * [Market API List](#marketapilist)
            * [Query Product Information](#queryproductinfo)
        * [Market Data API List ](#mdapilist)
            * [Query Order Book](#queryorderbook)
            * [Query Recent Trades](#querytrades)
            * [Query 24 Hours Ticker](#query24hrsticker)
        * [Spot Trading Api List](#spotTradingApi)
            * [Place Order With PUT method, *Preferred*](#spotPutPlaceOrder)
            * [Place Order](#spotPlaceOrder)
            * [Amend Order](#spotAmendOrder)
            * [Cancel Order](#spotCancelOrder)
            * [Cancel All Order by Symbol](#spotCancelAll)
            * [Query Open Order by clOrdID or orderID](#spotQueryOpenOrder)
            * [List all Open Orders by Symbol](#spotListAllOpenOrder)
            * [Query Wallets](#spotQueryWallet)
            * [Query Closed orders, *Deprecated*](#spotQueryClosedOrder)
            * [Query history trades, *Deprecated*](#spotQueryHistTrade)
        * [Spot Asset Api List](#spotAssetAPIList)
            * [Query Deposit address](#depositAddr)
            * [Query Deposit history](#depositHist)
            * [Query withdraw history](#withdrawHist)
        * [Spot Data Api List](#spotDataAPIList)
            * [Query Funds History](#spotDataFundsHist)
            * [Query Orders History](#spotDataOrdersHist)
            * [Query Orders By Ids](#spotDataOrdersByIds)
            * [Query PNLs](#spotDataPnls)
            * [Query Trades](#spotDataTradesHist)
            * [Query Trades By Ids](#spotDataTradesByIds)

* [Websocket API Standards](#wsapi)
    * [Session Management](#sessionmanagement)
    * [API Rate Limits](#wsapiratelimits)
    * [WebSocket API List](#wsapilist)
        * [Heartbeat](#heartbeat)
        * [API User Authentication](#apiuserauth)
        * [Subscribe OrderBook](#booksub)
        * [Subscribe Full OrderBook](#booksub2)
        * [Unsubscribe OrderBook](#bookunsub)
        * [Subscribe Trade](#tradesub)
        * [Unsubscribe Trade](#tradeunsub)
        * [Subscribe Kline](#klinesub)
        * [Unsubscribe Kline](#klinesub)
        * [Subscribe Wallet-Order](#wosub)
        * [Unsubscribe Wallet-Order](#wounsub)
        * [Subscribe 24 Hours Ticker](#tickersub)
        * [All Spot trading currencies](#currencyinfo)
        * [All Spot trading products](#productinfo)
        * [Subscribe Investment Account](#investmentaccount)

<a name="publicapi"/>

# Phemex Public API

<a name="general"/>

## General Public API Information

* Phemex provides HTTP Rest API for client to operate Orders, all endpoints return a JSON object.
* The default Rest API base endpoint is: **https://api.phemex.com**. The High rate limit Rest API base endpoint
  is: **https://vapi.phemex.com**. Or for the testnet is:  **https://testnet-api.phemex.com**
* Phemex provides WebSocket API for client to receive market data, order and position updates.
* The WebSocket API url is: **wss://phemex.com/ws**. The High rate limit WebSocket API url is: **wss:
  //vapi.phemex.com/ws**. Or for the testnet is:  **wss://testnet.phemex.com/ws**

<a name="restapi"/>

# REST API Standards

<a name="restresponse"/>

## Restful API Response

<a name="httpreturncodes"/>

### HTTP Return Codes

* HTTP `401` return code is used when unauthenticated
* HTTP `403` return code is used when lack of priviledge.
* HTTP `429` return code is used when breaking a request rate limit.
* HTTP `5XX` return codes are used for Phemex internal errors. Note: This doesn't means the operation failed, the
  execution status is **UNKNOWN** and could be Succeed.

<a name="responseformat"/>

### Rest Response format

* All restful API except ***starting*** with `/md` shares same response format.

```javascript
{
  "code": <code>,
  "msg": <msg>,
  "data": <data>
}
```

| Field | Description | 
|-------|------|
| code | 0 means `success`, non-zero means `error`|
| msg  | when code is non-zero, it gives short error description |
| data | operation dependant |

<a name="errorcode"/>

### Error codes

[Trading Error Codes](TradingErrorCode.md)

## HTTP REST Request Header

Every HTTP Rest Request must have the following Headers:

* x-phemex-access-token : This is ***API-KEY*** (id field) from Phemex site.
* x-phemex-request-expiry : This describes the Unix ***EPoch SECONDS*** to expire the request, normally it should be (
  Now() + 1 minute)
* x-phemex-request-signature : This is HMAC SHA256 signature of the http request. Secret is ***API Secret***, its
  formula is : HMacSha256( URL Path + QueryString + Expiry + body )

Optional Headers:

* x-phemex-request-tracing: a unique string to trace http-request, less than 40 bytes. This header is a must in
  resolving latency issues.

<a name="apiratelimits"/>

## API Rate Limits

* [Order spamming limitations](https://phemex.com/user-guides/order-spamming-limitations)
* RateLimit group of contract trading api is ***SPOTORDER***.
* RateLimit Explained [phemex ratelimite docs](/Generic-API-Info.en.md)
* Contract trading api response carries following headers.

```
X-RateLimit-Remaining-SPOTORDER, # Remaining request permits in this minute
X-RateLimit-Capacity-SPOTORDER, # Request ratelimit capacity
X-RateLimit-Retry-After-SPOTORDER, # Reset timeout in seconds for current ratelimited user
```

<a name="securitytype"/>

## Endpoint security type

* Each API call must be signed and pass to server in HTTP header `x-phemex-request-signature`.
* Endpoints use `HMAC SHA256` signatures. The `HMAC SHA256 signature` is a keyed `HMAC SHA256` operation. Use
  your `apiSecret` as the key and the string `URL Path + QueryString + Expiry + body )` as the value for the HMAC
  operation.
* `apiSecret` = `Base64::urlDecode(API Secret)`
* The `signature` is **case sensitive**.

<a name="signatureexample1"/>

### Signature Example 1: HTTP GET Request

* API REST Request URL: https://api.phemex.com/spot/wallets?currency=BTC
    * Request Path: /spot/wallets
    * Request Query: currency=BTC
    * Request Body: <null>
    * Request Expiry: 1587552406
    * Signature: HMacSha256( /spot/wallets + currency=BTC + 1587552406 )

<a name="signatureexample2"/>

### Singature Example 2: HTTP GET Request with multiple query string

* API REST Request
  URL: https://api.phemex.com/spot/orders/active?symbol=sBTCUSDT&orderID=bc2b8ff1-a73b-4673-aa5b-fda632285fcc
    * Request Path: /spot/orders/active
    * Request Query: symbol=sBTCUSDT&orderID=bc2b8ff1-a73b-4673-aa5b-fda632285fcc
    * Request Body: <null>
    * Request Expire: 1587552407
    * Signature: HMacSha256(/spot/orders/active + symbol=sBTCUSDT&orderID=bc2b8ff1-a73b-4673-aa5b-fda632285fcc +
      1587552407)
    * signed string is `/spot/orders/activesymbol=sBTCUSDT&orderID=bc2b8ff1-a73b-4673-aa5b-fda632285fcc1587552407`

<a name="signatureexample3"/>

### Signature Example 3: HTTP POST Request

* API REST Request URL: https://api.phemex.com/spot/orders
    * Request Path: /spot/orders
    * Request Query: <null>
    * Request Body:
   ```json
   {"symbol":"sBTCUSDT","clOrdID":"ece0187f-7e02-44b5-a778-404125f124fa","side":"Buy","qtyType":"ByBase","quoteQtyEv":"0","baseQtyEv":"100000","priceEp":"700000000","stopPxEp":"0","execInst":"","ordType":"Limit","timeInForce":"","text":""}
   ```
    * Request Expiry: 1587552407
    * signed string is
   ```
    /spot/orders1587552407{"symbol":"sBTCUSDT","clOrdID":"ece0187f-7e02-44b5-a778-404125f124fa","side":"Buy","qtyType":"ByBase","quoteQtyEv":"0","baseQtyEv":"100000","priceEp":"700000000","stopPxEp":"0","execInst":"","ordType":"Limit","timeInForce":"","text":""}
   ```

## Request/response field explained

<a name="spotCurrencySym"/>

<a name="spotCurrency"/>

### Spot Currency and Symbols

* Spot Currency and its scale factor
  See [all spot trading currencies](#currencyinfo) for details.

<a name="spotSymList"/>

* Spot symbol and its scale factor

All spot symbols use the same price and ratio scale factors (price scale facor(Ep) = 8, ratio scale factor(Er) = 8).

See [all spot trading products](#productinfo) for details.

<a name="commconsts"/>

### Common constants

* order type

| order type | description |
|-----------|-------------|
| Limit | -- |
| Market | -- |
| Stop | -- |
| StopLimit | -- |
| MarketIfTouched | -- |
| LimitIfTouched | -- |
| MarketAsLimit | -- |
| StopAsLimit | -- |
| MarketIfTouchedAsLimit | -- |

* order Status

| order status | description | 
|------------|-------------|
| Untriggered | Conditional order waiting to be triggered |
| Triggered | Conditional order being triggered|
| Rejected | Order rejected |
| New | Order placed in cross engine |
| PartiallyFilled | Order partially filled |
| Filled | Order fully filled |
| Canceled | Order canceled |

* TimeInForce

| timeInForce | description |
|------------|-------------|
| GoodTillCancel | -- |
| PostOnly | -- |
| ImmediateOrCancel | -- |
| FillOrKill | -- |

* Trigger source

| trigger | description |
|------------|-------------|
| ByLastPrice | trigger by last price |

<a name="restapilist"/>

## REST API List

<a name="marketapilist"/>

### Market API List

<a name="queryproductinfo"/>

#### Query Product Information

* Request：

```
GET /public/products
```

<a name="mdapilist"/>

### Market Data API List

<a name="queryorderbook"/>

#### Query Order Book

* Request：

```
GET /md/orderbook?symbol=<symbol>
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| symbol      | String | symbol name                                | [Trading symbols](#productinfo) |

* Response:

```javascript
{
  "error": null,
  "id": 0,
  "result": {
    "book": {
      "asks": [
        [
          <priceEp>,
          <size>
        ],
        ...
        ...
        ...
      ],
      "bids": [
        [
          <priceEp>,
          <size>
        ],
        ...
        ...
        ...
      ],
    ]
    },
    "depth": 30,
    "sequence": <sequence>,
    "timestamp": <timestamp>,
    "symbol": "<symbol>",
    "type": "snapshot"
  }
}
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| timestamp   | Integer| Timestamp in nanoseconds                   |              |
| priceEp     | Integer| Scaled book level price                    |              |
| size        | Integer| Scaled book level size                     |              |
| sequence    | Integer| current message sequence                   |              |
| symbol      | String | Spot symbol name                       | [Trading symbols](#productinfo) |

* Sample：

```
GET /md/orderbook?symbol=sBTCUSDT
```

```json
{
  "error": null,
  "id": 0,
  "result": {
    "book": {
      "asks": [
        [
          877050000000,
          1000000
        ],
        [
          877100000000,
          200000
        ]
      ],
      "bids": [
        [
          877000000000,
          2000000
        ],
        [
          876950000000,
          200000
        ]
      ]
    },
    "depth": 30,
    "sequence": 455476965,
    "timestamp": 1583555482434235628,
    "symbol": "sBTCUSDT",
    "type": "snapshot"
  }
}
```

<a name="querytrades"/>

#### Query Recent Trades

* Request：

```
GET /md/trade?symbol=<symbol>
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| symbol      | String | symbol name                                | [Trading symbols](#productinfo) |

* Response:

```javascript
{
  "error": null,
  "id": 0,
  "result": {
    "type": "snapshot",
    "sequence": <sequence>,
    "symbol": "<symbol>",
    "trades": [
      [
        <timestamp>,
        "<side>",
        <priceEp>,
        <size>
      ],
      ...
      ...
      ...
    ]
  }
}

```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| timestamp   | Integer| Timestamp in nanoseconds                   |              |
| side        | String | Trade side string                          | Buy, Sell    |
| priceEp     | Integer| Scaled trade price                         |              |
| size        | Integer| Scaled trade size                          |              |
| sequence    | Integer| Current message sequence                   |              |
| symbol      | String | Spot symbol name                       | [Trading symbols](#productinfo) |

* Sample：

```
GET /md/trade?symbol=sBTCUSDT
```

```json
{
  "error": null,
  "id": 0,
  "result": {
    "sequence": 15934323,
    "symbol": "sBTCUSDT",
    "trades": [
      [
        1579164056368538508,
        "Sell",
        869600000000,
        1210000
      ],
      [
        1579164055036820552,
        "Sell",
        869600000000,
        580000
      ]
    ],
    "type": "snapshot"
  }
}

```

<a name="query24hrsticker"/>

#### Query 24 Hours Ticker

* Request：

```
GET /md/spot/ticker/24hr?symbol=<symbol>
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| symbol      | String | symbol name                                | [Trading symbols](#productinfo) |

* Response:

```javascript
{
  "error": null,
  "id": 0,
  "result": {
    "openEp": <open priceEp>,
    "highEp": <high priceEp>,
    "lowEp": <low priceEp>,
    "lastEp": <last priceEp>,
    "bidEp": <bid priceEp>,
    "askEp": <ask priceEp>,
    "symbol": "<symbol>",
    "turnoverEv": <turnoverEv>,
    "volumeEv": <volumeEv>,
    "timestamp": <timestamp>
  }
}
```

| Field         | Type   | Description                                | Possible values |
|---------------|--------|--------------------------------------------|--------------|
| open priceEp  | Integer| The scaled open price in last 24 hours     |              |
| high priceEp  | Integer| The scaled highest price in last 24 hours  |              |
| low priceEp   | Integer| The scaled lowest price in last 24 hours   |              |
| last priceEp  | Integer| The scaled last price                      |              |
| bid priceEp   | Integer| Scaled bid price                           |              |
| ask priceEp   | Integer| Scaled ask price                           |              |
| timestamp     | Integer| Timestamp in nanoseconds                   |              |
| symbol        | String | symbol name                                | [Trading symbols](#productinfo) |
| turnoverEv    | Integer| The scaled turnover value in last 24 hours |              |
| volumeEv      | Integer| The scaled trade volume in last 24 hours   |              |

* Sample：

```
GET /md/spot/ticker/24hr?symbol=sBTCUSDT
```

```json
{
  "error": null,
  "id": 0,
  "result": {
    "askEp": 892100000000,
    "bidEp": 891835000000,
    "highEp": 898264000000,
    "lastEp": 892486000000,
    "lowEp": 870656000000,
    "openEp": 896261000000,
    "symbol": "sBTCUSDT",
    "timestamp": 1590571240030003249,
    "turnoverEv": 104718804814499,
    "volumeEv": 11841148100
  }
}
```

<a name="mdapilistv1"/>

### Market Data API List

<a name="queryorderbookv1"/>

#### Query Order Book

* Request：

```
GET /v1/md/orderbook?symbol=<symbol>
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| symbol      | String | Spot symbol name                       | [Trading symbols](#productinfo) |

* Response:

```javascript
{
  "error": null,
  "id": 0,
  "result": {
    "book": {
      "asks": [
        [
          <priceEp>,
          <size>
        ],
        ...
        ...
        ...
      ],
      "bids": [
        [
          <priceEp>,
          <size>
        ],
        ...
        ...
        ...
      ],
    ]
    },
    "depth": 30,
    "sequence": <sequence>,
    "symbol": "<symbol>",
    "timestamp": "<timestamp>",
    "type": "snapshot"
  }
}
```

| Field       | Type   | Description                                | Possible values |
|-------------|--------|--------------------------------------------|--------------|
| timestamp   | Integer| Timestamp in nanoseconds                   |              |
| priceEp     | Integer| Scaled book level price                    |              |
| size        | Integer| Scaled book level size                     |              |
| sequence    | Integer| current message sequence                   |              |
| symbol      | String | Spot symbol name                       | [Trading symbols](#productinfo) |

* Sample：

```
GET /v1/md/orderbook?symbol=sBTCUSDT
```

```json
{
  "error": null,
  "id": 0,
  "result": {
    "book": {
      "asks": [
        [
          87705000000,
          1000000
        ],
        [
          87710000000,
          200000
        ]
      ],
      "bids": [
        [
          877000000000,
          2000000
        ],
        [
          876950000000,
          200000
        ]
      ]
    },
    "depth": 30,
    "sequence": 455476965,
    "symbol": "sBTCUSDT",
    "timestamp": 1583552267253988998,
    "type": "snapshot"
  }
}
```

<a name="spotTradingApi"/>

### Spot Trading Api List

<a name="spotPutPlaceOrder"/>

* Http Request:

```
PUT /spot/orders/create?symbol=<symbol>&trigger=<trigger>&clOrdID=<clOrdID>&priceEp=<priceEp>&baseQtyEv=<baseQtyEv>&quoteQtyEv=<quoteQtyEv>&stopPxEp=<stopPxEp>&text=<text>&side=<side>&qtyType=<qtyType>&ordType=<ordType>&timeInForce=<timeInForce>&execInst=<execInst>
```

| Field       | Type   | Required | Description               | Possible values |
|----------   |--------|----------|---------------------------|-----------------|
| symbol      | String | Yes      |                           | [Spot Trading symbols](#spotSymList) |
| side        | Enum   | Yes      |                           |  Sell, Buy     | 
| qtyType     | Enum   | Yes      | default ByBase            | ByBase, ByQuote|
| quoteQtyEv  | Number | --       | Required when qtyType = ByQuote|  |
| baseQtyEv   | Number | --       |                           | Required when qtyType = ByBase   |
| priceEp     | Number |          |                           | Scaled price            |
| stopPxEp    | Number | --       | used in conditional order |   |
| trigger     | Enum   | --       | Required in conditional order | ByLastPrice |
| timeInForce    | Enum   | No       | Default GoodTillCancel | GoodTillCancel, PostOnly,ImmediateOrCancel,FillOrKill |
| ordType    | Enum   | No        | Default to Limit         |Market, Limit, Stop, StopLimit, MarketIfTouched, LimitIfTouched|

* Http Response

```javascript
{
  "code": 0,
  "msg": "",
  "data": {
    "orderID": "d1d09454-cabc-4a23-89a7-59d43363f16d",
    "clOrdID": "309bcd5c-9f6e-4a68-b775-4494542eb5cb",
    "priceEp": 0,
    "action": "New",
    "trigger": "UNSPECIFIED",
    "pegPriceType": "UNSPECIFIED",
    "stopDirection": "UNSPECIFIED",
    "bizError": 0,
    "symbol": "sBTCUSDT",
    "side": "Buy",
    "baseQtyEv": 0,
    "ordType": "Limit",
    "timeInForce": "GoodTillCancel",
    "ordStatus": "Created",
    "cumFeeEv": 0,
    "cumBaseQtyEv": 0,
    "cumQuoteQtyEv": 0,
    "leavesBaseQtyEv": 0,
    "leavesQuoteQtyEv": 0,
    "avgPriceEp": 0,
    "cumBaseAmountEv": 0,
    "cumQuoteAmountEv": 0,
    "quoteQtyEv": 0,
    "qtyType": "ByBase",
    "stopPxEp": 0,
    "pegOffsetValueEp": 0
  }
}
```

<a name="spotPlaceOrder"/>

#### Place order

* Http Request:

```
POST /spot/orders
```

```json
{
  "symbol": "sBTCUSDT",
  "clOrdID": "",
  "side": "Buy/Sell",
  "qtyType": "ByBase/ByQuote",
  "quoteQtyEv": 0,
  "baseQtyEv": 0,
  "priceEp": 0,
  "stopPxEp": 0,
  "trigger": "UNSPECIFIED",
  "ordType": "Limit",
  "timeInForce": "GoodTillCancel"
}
```

* Fields are the same as [above place-order](#spotPutPlaceOrder)

<a name="spotAmendOrder"/>

#### Amend Order

* Http Request

```
PUT /spot/orders?symbol=<symbol>&orderID=<orderID>&origClOrdID=<origClOrdID>&clOrdID=<clOrdID>&priceEp=<priceEp>&baseQtyEV=<baseQtyEV>&quoteQtyEv=<quoteQtyEv>&stopPxEp=<stopPxEp> 
```

* Http Response

    * amended order

<a name="spotCancelOrder"/>

#### Cancel Order

```
DELETE /spot/orders?symbol=<symbol>&orderID=<orderID>
DELETE /spot/orders?symbol=<symbol>&clOrdID=<clOrdID>
```

* Http Response
    * Canceled order

<a name="spotCancelAll"/>

#### Cancel all order by symbol

```
DELETE /spot/orders/all?symbol=<symbol>&untriggered=<untriggered>
```

| Field | Type | Required | Description |
|---------|--------|-------|-------------|
| symbol  | Enum   | Yes   | The symbol to cancel |
| untriggered | Boolean | No | set false to cancel non-conditiaonal order, true to conditional order |

* Http Response
    * Total orders canceled

<a name="spotQueryOpenOrder"/>

#### Query Open order by clOrdID or orderID

* Http Request

```
GET /spot/orders/active?symbol=<symbol>&orderID=<orderID>
GET /spot/orders/active?symbol=<symbol>&clOrDID=<clOrdID>
```

* Http Response

    * Order object

<a name="spotListAllOpenOrder"/>

#### Query all open orders by symbol

* Http Request

```
GET /spot/orders?symbol=<symbol>
```

* Http Response
    * List of orders

<a name="spotQueryWallet"/>

#### Query wallets

* Query spot wallet by currency

* Http Request

```
GET /spot/wallets?currency=<currency>
```

* Http Response

```json
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "currency": "BTC",
      "balanceEv": 0,
      "lockedTradingBalanceEv": 0,
      "lockedWithdrawEv": 0,
      "lastUpdateTimeNs": 0
    }
  ]
}
```

<a name="spotQueryClosedOrder"/>

#### Query spot closed orders

    * Query closed orders by symbol

**NOTE:** deprecated, recommend [Query Orders by IDs](#spotDataOrdersByIds)

* Http Request

```
GET /exchange/spot/order?symbol=<symbol>&ordStatus=<ordStatus1,orderStatus2>ordType=<ordType1,orderType2>&start=<start>&end=<end>&limit=<limit>&offset=<offset>
```

| Field      | Type | Required | Description |  Possible Values |
|-----------|------|----------|-------------|------------------|
| symbol    | String | Yes    | symbol to query | [Trading symbols](#productinfo) |
| ordStatus | enum   | No     | order status filter |[common constants for order status](#commconsts) |
| ordType   | enum   | No     | order type filter |[common constants for order type](#commconsts) |
| start     | integer | No    | Epoch millisecond, start of time range    |  within 3 month        |
| end       | integer | No    | Epoch millisecond, end of time range      | within 3 months |

* Http Response

    * return a list of spot order model.

```json
{
  "code": 0,
  "msg": "OK",
  "data": {
    "total": 2,
    "rows": [
      {
        "orderID": "string",
        "stopPxEp": 0,
        "avgPriceEp": 0,
        "qtyType": "<ByQuote/ByBase>",
        "leavesBaseQtyEv": 0,
        "leavesQuoteQtyEv": 0,
        "baseQtyEv": "0",
        "feeCurrency": "string",
        "stopDirection": "UNSPECIFIED",
        "symbol": "string",
        "side": "enum",
        "quoteQtyEv": 0,
        "priceEp": 0,
        "ordType": "enum",
        "timeInForce": "enum",
        "ordStatus": "enum",
        "execStatus": "enum",
        "createTimeNs": 0,
        "cumFeeEv": 0,
        "cumBaseValueEv": 0,
        "cumQuoteValueEv": 0
      }
    ]
  }
}
```

* Sample Response

```json
{
  "code": 0,
  "msg": "OK",
  "data": {
    "total": 2,
    "rows": [
      {
        "orderID": "b2b7018d-f02f-4c59-b4cf-051b9c2d2e83",
        "stopPxEp": 0,
        "avgPriceEp": 970056000000,
        "qtyType": "ByQuote",
        "leavesBaseQtyEv": 0,
        "leavesQuoteQtyEv": 0,
        "baseQtyEv": "0",
        "feeCurrency": "1",
        "stopDirection": "UNSPECIFIED",
        "symbol": "sBTCUSDT",
        "side": "Buy",
        "quoteQtyEv": 1000000000,
        "priceEp": 970056000000,
        "ordType": "Limit",
        "timeInForce": "GoodTillCancel",
        "ordStatus": "Filled",
        "execStatus": "MakerFill",
        "createTimeNs": 1589449348601287000,
        "cumFeeEv": 0,
        "cumBaseValueEv": 103000,
        "cumQuoteValueEv": 999157680
      }
    ]
  }
}
```

<a name="spotQueryHistTrade"/>

#### Query spot history trades

* Query spot history trades by symbol

**NOTE:**  Deprecated, recommend [Query Trades](#spotDataTradesHist)

* Http Request

```
GET /exchange/spot/order/trades?symbol=<symbol>&start=<start>&end=<end>&limit=<limit>&offset=<offset>
```

| Field | Type | Required | Description | Possible values |
|-------|------|----------|-------------|-----------------|
| symbol | string | Yes   | symbol to query | [spot symbol list](#spotSymList) |
| start | integer | No    | Epoch millisecond, start of time range      |  |
| end   | integer | No    | Epoch millisecond, end of time range  | | 

* Http Response

```json
{
  "code": 0,
  "msg": "OK",
  "data": {
    "total": 1,
    "rows": [
      {
        "qtyType": "ByQuote/ByBase",
        "transactTimeNs": 0,
        "clOrdID": "string"
        "orderID": "string",
        "symbol": "string",
        "side": "enum",
        "priceEP": 0,
        "baseQtyEv": 0,
        "quoteQtyEv": 0,
        "action": "enum",
        "execStatus": "enum",
        "ordStatus": "enum",
        "ordType": "enum",
        "execInst": "enum",
        "timeInForce": "enum",
        "stopDirection": "enum",
        "tradeType": "enum",
        "stopPxEp": 0,
        "execId": "0",
        "execPriceEp": 0,
        "execBaseQtyEv": 0,
        "execQuoteQtyEv": 0,
        "leavesBaseQtyEv": 0,
        "leavesQuoteQtyEv": 0,
        "execFeeEv": 0,
        "feeRateEr": 0
      }
    ]
  }
}
```

* Sample Response

```json
{
  "code": 0,
  "msg": "OK",
  "data": {
    "total": 1,
    "rows": [
      {
        "qtyType": "ByQuote",
        "transactTimeNs": 1589450974800550100,
        "clOrdID": "8ba59d40-df25-d4b0-14cf-0703f44e9690",
        "orderID": "b2b7018d-f02f-4c59-b4cf-051b9c2d2e83",
        "symbol": "sBTCUSDT",
        "side": "Buy",
        "priceEP": 970056000000,
        "baseQtyEv": 0,
        "quoteQtyEv": 1000000000,
        "action": "New",
        "execStatus": "MakerFill",
        "ordStatus": "Filled",
        "ordType": "Limit",
        "execInst": "None",
        "timeInForce": "GoodTillCancel",
        "stopDirection": "UNSPECIFIED",
        "tradeType": "Trade",
        "stopPxEp": 0,
        "execId": "c6bd8979-07ba-5946-b07e-f8b65135dbb1",
        "execPriceEp": 970056000000,
        "execBaseQtyEv": 103000,
        "execQuoteQtyEv": 999157680,
        "leavesBaseQtyEv": 0,
        "leavesQuoteQtyEv": 0,
        "execFeeEv": 0,
        "feeRateEr": 0
      }
    ]
  }
}
```

<a name="spotAssetApiList"/>

# Spot Asset API

<a name="depositAddr"/>

#### Query deposit address by currency

* Http Request

```
GET /exchange/wallets/v2/depositAddress?currency=<currency>&chainName=<chainName>
```

| Field    | Type   | Required  | Description| Possible Values |
|----------|--------|-----------|------------|-----------------|
| currency | String | True      | the currency to query | BTC,ETH, USDT ... |
| chainName| String | True      | the chain for this currency | BTC, ETH, EOS |

* chainName is provided by below currency settings interface.

```
GET /exchange/public/cfg/chain-settings?currency=<currency>
```

* Response

```json
{
  "address": "1Cdxxxxxxxxxxxxxx",
  "tag": null
}
```

<a name="depositHist"/>

#### Query recent deposit history within 3 months

* Http Request

```
GET /exchange/wallets/depositList?currency=<currency>&offset=<offset>&limit=<limit>
```

| Field    | Type   | Required  | Description| Possible Values |
|----------|--------|-----------|------------|-----------------|
| currency | String | True      | the currency to query | BTC,ETH, ... |

* Response

```json
{
  "address": "1xxxxxxxxxxxxxxxxxx",
  "amountEv": 1000000,
  "confirmations": 1,
  "createdAt": 1574685871000,
  "currency": "BTC",
  "currencyCode": 1,
  "status": "Success",
  "txHash": "9e84xxxxxxxxxxxxxxxxxxxxxxxxxxxxx",
  "type": "Deposit"
}
```

<a name="withdrawHist"/>

#### Query recent withdraw history within 3 months

* Http Request

```
GET /exchange/wallets/withdrawList?currency=<currency>&offset=<offset>&limit=<limit>
```

* Response

```json
{
  "address": "1Lxxxxxxxxxxx",
  "amountEv": 200000,
  "currency": "BTC",
  "currencyCode": 1,
  "expiredTime": 0,
  "feeEv": 50000,
  "rejectReason": null,
  "status": "Succeed",
  "txHash": "44exxxxxxxxxxxxxxxxxxxxxx",
  "withdrawStatus": ""
}
```

<a name="spotDataApiList"/>

### Spot Data Api List

<a name="spotDataFundsHist"/>

#### Query Funds History

* Http Request

```
GET /api-data/spots/funds?currency=<currency>
```

| Field    | Type           | Required | Description               | Possible Values                 |
|----------|----------------|----------|---------------------------|---------------------------------|
| currency | String         | True     | the currency to query     | BTC,ETH, USDT ...               |
| start    | Long           | False    | start time in millisecond | default 2 days ago from the end |
| end      | Long           | False    | end time in millisecond   | default now                     |
| offset   | Integer        | False    | page start from 0         | start from 0, default 0         |
| limit    | Integer        | False    | page size                 | default 20, max 200             |

* Response

```json
[
  {
    "action": "string",
    "amountEv": 0,
    "balanceEv": 0,
    "bizCode": 0,
    "createTime": 0,
    "currency": "string",
    "execId": "string",
    "execSeq": 0,
    "feeEv": 0,
    "id": 0,
    "side": "string",
    "text": "string",
    "transactTimeNs": 0
  }
]
```

<a name="spotDataOrdersHist"/>

#### Query Orders History

* Http Request

```
GET /api-data/spots/orders?symbol=<symbol>
```

| Field     | Type    | Required | Description               | Possible Values                 |
|-----------|---------|----------|---------------------------|---------------------------------|
| symbol    | String  | True     | the currency to query     | sBTCUSDT ...                    |
| start     | Long    | False    | start time in millisecond | default 2 days ago from the end |
| end       | Long    | False    | end time in millisecond   | default now                     |
| offset    | Integer | False    | page start from 0         | start from 0, default 0         |
| limit     | Integer | False    | page size                 | default 20, max 200             |

* Response

```json
[
  {
    "avgPriceEp": 0,
    "avgTransactPriceEp": 0,
    "baseQtyEv": "string",
    "createTimeNs": 0,
    "cumBaseValueEv": 0,
    "cumFeeEv": 0,
    "cumQuoteValueEv": 0,
    "execStatus": "string",
    "feeCurrency": "string",
    "leavesBaseQtyEv": 0,
    "leavesQuoteQtyEv": 0,
    "ordStatus": "string",
    "ordType": "string",
    "orderID": "string",
    "priceEp": 0,
    "qtyType": "string",
    "quoteQtyEv": 0,
    "side": "string",
    "stopDirection": "string",
    "stopPxEp": 0,
    "symbol": "string",
    "timeInForce": "string"
  }
]
```

<a name="spotDataOrdersByIds"/>

#### Query Orders By Ids

* Http Request

```
GET /api-data/spots/orders/by-order-id?symbol=<symbol>&oderId=<orderID>&clOrdID=<clOrdID>
```

| Field    | Type   | Required | Description           | Possible Values                                                                                                                           |
|----------|--------|----------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| symbol   | String | True     | the currency to query | sBTCUSDT ...                                                                                                                              |
| orderID  | String | False    | order id              | orderID and clOrdID can not be both empty. If both IDs are given, it will return orderID if there is any, otherwise will try to find clOrdID |
| clOrdID  | String | False    | client order id       | refer to orderID                                                                                                                          |

* Response

```json
[
  {
    "avgPriceEp": 0,
    "avgTransactPriceEp": 0,
    "baseQtyEv": "string",
    "createTimeNs": 0,
    "cumBaseValueEv": 0,
    "cumFeeEv": 0,
    "cumQuoteValueEv": 0,
    "execStatus": "string",
    "feeCurrency": "string",
    "leavesBaseQtyEv": 0,
    "leavesQuoteQtyEv": 0,
    "ordStatus": "string",
    "ordType": "string",
    "orderID": "string",
    "priceEp": 0,
    "qtyType": "string",
    "quoteQtyEv": 0,
    "side": "string",
    "stopDirection": "string",
    "stopPxEp": 0,
    "symbol": "string",
    "timeInForce": "string"
  }
]
```

<a name="spotDataPnls"/>

#### Query PNLs

* Http Request

```
GET /api-data/spots/pnls
```

| Field    | Type   | Required | Description           | Possible Values                                                                                                                           |
|----------|--------|----------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| start     | Long    | False    | start time in millisecond | default 2 days ago from the end |
| end       | Long    | False    | end time in millisecond   | default now                     |

* Response

```json
[
  {
    "collectTime": 0,
    "cumPnlEv": 0,
    "dailyPnlEv": 0,
    "userId": 0
  }
]
```

<a name="spotDataTradesHist"/>

#### Query Trades History

* Http Request

```
GET /api-data/spots/trades?symbol=<symbol>
```

| Field     | Type    | Required | Description               | Possible Values                 |
|-----------|---------|----------|---------------------------|---------------------------------|
| symbol    | String  | True     | the currency to query     | sBTCUSDT ...                    |
| start     | Long    | False    | start time in millisecond | default 2 days ago from the end |
| end       | Long    | False    | end time in millisecond   | default now                     |
| offset    | Integer | False    | page start from 0         | start from 0, default 0         |
| limit     | Integer | False    | page size                 | default 20, max 200             |

* Response

```json
[
  {
    "action": "string",
    "baseCurrency": "string",
    "baseQtyEv": 0,
    "clOrdID": "string",
    "execBaseQtyEv": 0,
    "execFeeEv": 0,
    "execId": "string",
    "execInst": "string",
    "execPriceEp": 0,
    "execQuoteQtyEv": 0,
    "execStatus": "string",
    "feeCurrency": "string",
    "feeRateEr": 0,
    "leavesBaseQtyEv": 0,
    "leavesQuoteQtyEv": 0,
    "ordStatus": "string",
    "ordType": "string",
    "orderID": "string",
    "priceEP": 0,
    "qtyType": "string",
    "quoteCurrency": "string",
    "quoteQtyEv": 0,
    "side": "string",
    "stopDirection": "string",
    "stopPxEp": 0,
    "symbol": "string",
    "timeInForce": "string",
    "tradeType": "string",
    "transactTimeNs": 0
  }
]
```

<a name="spotDataTradesByIds"/>

#### Query Orders By Ids

* Http Request

```
GET /api-data/spots/trades/by-order-id?symbol=<symbol>&oderId=<orderID>&clOrdID=<clOrdID>
```

| Field    | Type   | Required | Description           | Possible Values                                                                                                                           |
|----------|--------|----------|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| symbol   | String | True     | the currency to query | sBTCUSDT ...                                                                                                                              |
| orderID  | String | False    | order id              | orderID and clOrdID can not be both empty. If both IDs are given, it will return orderID if there is any, otherwise will try to find clOrdID |
| clOrdID  | String | False    | client order id       | refer to orderID                                                                                                                          |

* Response

```json
[
  {
    "action": "string",
    "baseCurrency": "string",
    "baseQtyEv": 0,
    "clOrdID": "string",
    "execBaseQtyEv": 0,
    "execFeeEv": 0,
    "execId": "string",
    "execInst": "string",
    "execPriceEp": 0,
    "execQuoteQtyEv": 0,
    "execStatus": "string",
    "feeCurrency": "string",
    "feeRateEr": 0,
    "leavesBaseQtyEv": 0,
    "leavesQuoteQtyEv": 0,
    "ordStatus": "string",
    "ordType": "string",
    "orderID": "string",
    "priceEP": 0,
    "qtyType": "string",
    "quoteCurrency": "string",
    "quoteQtyEv": 0,
    "side": "string",
    "stopDirection": "string",
    "stopPxEp": 0,
    "symbol": "string",
    "timeInForce": "string",
    "tradeType": "string",
    "transactTimeNs": 0
  }
]
```

<a name="wsapi"/>

# Websocket API Standards

<a name="sessionmanagement"/>

## Session Management

* Each client is required to actively send heartbeat (ping) message to Phemex data gateway ('DataGW' in short) with
  interval less than 30 seconds, otherwise DataGW will drop the connection. If a client sends a ping message, DataGW
  will reply with a pong message.
* Clients can use WS built-in ping message or the application level ping message to DataGW as heartbeat. The heartbeat
  interval is recommended to be set as *5 seconds*, and actively reconnect to DataGW if don't receive messages in *3
  heartbeat intervals*.

<a name="wsapiratelimits"/>

## API Rate Limits

* Each Client has concurrent connection limit to *5* in maximum.
* Each connection has subscription limit to *20* in maximum.
* Each connection has throttle limit to *20* request/s.

<a name="wsapilist"/>

## WebSocket API List

<a name="heartbeat"/>

### Heartbeat

* Request：

```javascript
{
  "id": <id>,
  "method": "server.ping",
  "params": []
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": "pong"
}
```

* Sample：

```javascript
> {
  "id": 1234,
  "method": "server.ping",
  "params": []
}

< {
  "error": null,
  "id": 1234,
  "result": "pong"
}
```

<a name="apiuserauth"/>

### API User Authentication

Market trade/orderbook are published publicly without user authentication.
While for client private account/position/order data, the client should send user.auth message to Data Gateway to
authenticate the session.

* Request

```javascript
{
  "method": "user.auth",
  "params": [
    "API",
    "<token>",
    "<signature>",
    <expiry>
  ],
  "id": 1234
}
```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| type        | String | Token type       | API             |
| token       | String | API Key     |                 |
| signature   | String | Signature generated by a funtion as HMacSha256(API Key + expiry) with ***API Secret*** ||
| expiry      | Integer| A future time after which request will be rejected, in epoch ***second***. Maximum expiry is request time plus 2 minutes ||

* Sample:

```javascript
> {
  "method": "user.auth",
  "params": [
    "API",
    "806066b0-f02b-4d3e-b444-76ec718e1023",
    "8c939f7a6e6716ab7c4240384e07c81840dacd371cdcf5051bb6b7084897470e",
    1570091232
  ],
  "id": 1234
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

<a name="booksub"/>

### Subscribe OrderBook

On each successful subscription, DataGW will immediately send the current Order Book snapshot to client and all later
order book updates will be published.
Incremental messages are published with **depth=30 and 20ms interval**.

* Request

```javascript
{
  "id": <id>,
  "method": "orderbook.subscribe",
  "params": [
    "<symbol>"
  ]
}
```

* Response

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample：

```javascript
> {
  "id": 1234,
  "method": "orderbook.subscribe",
  "params": [
    "sBTCUSDT"
  ]
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

<a name="booksub2"/>

### Subscribe Full OrderBook

On each successful subscription, DataGW will immediately send the current Order Book snapshot to client and all later
order book updates will be published.
Incremental messages are published with **full depth and 100ms interval**.

* Request

```javascript
{
  "id": <id>,
  "method": "orderbook.subscribe",
  "params": [
    "<symbol>",
    true
  ]
}
```

* Response

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample：

```javascript
> {
  "id": 1234,
  "method": "orderbook.subscribe",
  "params": [
    "sBTCUSDT",
    true
  ]
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

#### OrderBook Message:

DataGW publishes order book message with types: incremental, snapshot. And snapshot messages are published with 60-second interval for client self-verification.

* Message Format：

```javascript
{
  "book": {
    "asks": [
      [
        <priceEp>,
        <qty>
      ],
      .
      .
      .
    ],
    "bids": [
      [
        <priceEp>,
        <qty>
      ],
      .
      .
      .
    ]
  },
  "depth": <depth>,
  "sequence": <sequence>,
  "timestamp": <timestamp>,
  "symbol": "<symbol>"
}
```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| side        | String | Price level side | bid, ask        |
| priceEp     | Integer| Scaled price     |                 |
| qty         | Integer| Price level size. Non-zero qty indicates price level insertion or updation, and qty 0 indicates price level deletion. |                 |
| sequence    | Integer| Latest message sequence |          |
| depth       | Integer| Market depth     | 30              |
| type        | String | Message type     | snapshot, incremental |

* Sample：

```javascript
< {"book":{"asks":[[892697000000,1781800],[892708000000,7543500],[892718000000,6552500],[892720000000,4714100],[892728000000,8431000],[892735000000,11644800],[892756000000,5909600],[892790000000,9053100],[892798000000,3336400],[892819000000,1689500],[892828000000,1616700],[892855000000,6484000],[892869000000,6873200],[892872000000,1919900],[892875000000,2373200],[892942000000,1875300],[892944000000,3117500],[892962000000,1353500],[892965000000,2589800],[892966000000,11169800],[892973000000,7829700],[892977000000,2697200],[892978000000,2110700],[892985000000,12563700],[892988000000,5374100],[893023000000,3816000],[893031000000,5852700],[893035000000,4990900],[893061000000,3479500],[893083000000,327900]],"bids":[[892376000000,6866500],[892354000000,14209000],[892353000000,5287200],[892348000000,6417800],[892340000000,8074400],[892334000000,3991900],[892303000000,4558000],[892295000000,10154700],[892280000000,16214500],[892277000000,11425300],[892270000000,39156500],[892268000000,13821100],[892260000000,32157500],[892257000000,5466100],[892252000000,11468700],[892241000000,13940300],[892226000000,33832300],[892220000000,3000000],[892171000000,4320400],[892165000000,4454000],[892152000000,5336400],[892144000000,4539200],[892134000000,7472200],[892127000000,5352700],[892087000000,10264400],[892082000000,4908000],[892038000000,1485500],[892031000000,4089200],[892030000000,4895500],[892014000000,3846600]]},"depth":30,"sequence":677996311,"symbol":"sBTCUSDT","timestamp":1590570810187570850,"type":"snapshot"}
< {"book":{"asks":[[892696000000,1669700],[892697000000,10455500],[892728000000,0],[892735000000,0],[892748000000,1550900],[892790000000,0],[892819000000,19087900],[892860000000,17152500],[892882000000,11546100],[892893000000,10986500],[892973000000,0],[892985000000,0],[893004000000,8306500],[893061000000,0],[893065000000,5446400],[893073000000,0],[893083000000,0],[893073000000,0],[893083000000,0]],"bids":[]},"depth":30,"sequence":677996548,"symbol":"sBTCUSDT","timestamp":1590570810819505422,"type":"incremental"}
< {"book":{"asks":[],"bids":[[892387000000,4792900],[892354000000,3170700],[892226000000,0],[892187000000,14425000],[892171000000,6366500],[892165000000,0],[892135000000,11511400],[892134000000,0],[892127000000,0],[892090000000,5446000],[892079000000,4687800],[892041000000,8590200],[892030000000,0],[892014000000,0]]},"depth":30,"sequence":677996941,"symbol":"sBTCUSDT","timestamp":1590570811244188841,"type":"incremental"}
```

<a name="bookunsub"/>

### Unsubscribe OrderBook

It unsubscribes all orderbook related subscriptions.

* Request

```javascript
{
  "id": <id>,
  "method": "orderbook.unsubscribe",
  "params": []
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

<a name="tradesub"/>

### Subscribe Trade

On each successful subscription, DataGW will send the 200 history trades immediately for the subscribed symbol and all
the later trades will be published.

* Request

```javascript
{
  "id": <id>,
  "method": "trade.subscribe",
  "params": [
    "<symbol>"
  ]
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample:

```javascript
> {
  "id": 1234,
  "method": "trade.subscribe",
  "params": [
    "sBTCUSDT"
  ]
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

#### Trade Message Format：

DataGW publishes trade message with types: incremental, snapshot. Incremental messages are published with 20ms interval.
And snapshot messages are published on connection initial setup for client recovery.

```javascript
{
  "trades": [
    [
      <timestamp>,
      "<side>",
      <priceEp>,
      <qty>
    ],
    .
    .
    .
  ],
  "sequence": <sequence>,
  "symbol": "<symbol>",
  "type": "<type>"
}
```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| timestamp   | Integer| Timestamp in nanoseconds for each trade ||
| side        | String | Execution taker side| bid, ask        |
| priceEp     | Integer| Scaled execution price  |                 |
| qty         | Integer| Execution size   |                 |
| sequence    | Integer| Latest message sequence ||
| symbol      | String | Spot symbol name     ||
| type        | String | Message type     |snapshot, incremental |

* Sample

```javascript
< {
  "sequence": 1167852,
  "symbol": "sBTCUSDT",
  "trades": [
    [
      1573716998128563500,
      "Buy",
      867350000000,
      560000
    ],
    [
      1573716995033683000,
      "Buy",
      867350000000,
      520000
    ],
    [
      1573716991485286000,
      "Buy",
      867350000000,
      510000
    ],
    [
      1573716988636291300,
      "Buy",
      867350000000,
      120000
    ]
  ],
  "type": "snapshot"
}

< {
  "sequence": 1188273,
  "symbol": "sBTCUSDT",
  "trades": [
    [
      1573717116484024300,
      "Buy",
      86730000000,
      210000
    ]
  ],
  "type": "incremental"
}
```

<a name="tradeunsub"/>

### Unsubscribe Trade

It unsubscribes all trade subscriptions.

* Request

```javascript
{
  "id": <id>,
  "method": "trade.subscribe",
  "params": [
    "<symbol>"
  ]
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

<a name="klinesub"/>

### Subscribe Kline

On each successful subscription, DataGW will send the 1000 history klines immediately for the subscribed symbol and all
the later kline update will be published in real-time.

* Request

```javascript
{
  "id": <id>,
  "method": "kline.subscribe",
  "params": [
    "<symbol>",
    "<interval>"
  ]
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample:

```javascript
# subscribe 1-day kline
> {
  "id": 1234,
  "method": "kline.subscribe",
  "params": [
    "sBTCUSDT",
    86400
  ]
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

#### Kline Message Format：

DataGW publishes kline message with types: incremental, snapshot. Incremental messages are published with 20ms interval.
And snapshot messages are published on connection initial setup for client recovery.

```javascript
{
  "kline": [
    [
      <timestamp>,
      "<interval>",
      <lastCloseEp>,
      <openEp>,
      <highEp>,
      <lowEp>,
      <closeEp>,
      <volumeEv>,
      <turnoverEv>,
    ],
    .
    .
    .
  ],
  "sequence": <sequence>,
  "symbol": "<symbol>",
  "type": "<type>"
}
```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| timestamp   | Integer| Timestamp in nanoseconds for each trade ||
| interval    | Integer| Kline interval type      | 60, 300, 900, 1800, 3600, 14400, 86400, 604800, 2592000, 7776000, 31104000 |
| lastCloseEp | Integer| Scaled last close price  |                 |
| openEp      | Integer| Scaled open price        |                 |
| highEp      | Integer| Scaled high price        |                 |
| lowEp       | Integer| Scaled low price         |                 |
| closeEp     | Integer| Scaled close price       |                 |
| volumeEv    | Integer| Scaled trade voulme during the current kline interval ||
| turnoverEv  | Integer| Scaled turnover value    |                 |
| sequence    | Integer| Latest message sequence  ||
| symbol      | String | Contract symbol name     ||
| type        | String | Message type     |snapshot, incremental |

* Sample

```javascript
< {
  "kline": [
    [
      1590019200,
      86400,
      952057000000,
      952000000000,
      955587000000,
      947835000000,
      954446000000,
      1162621600,
      11095452729869
    ],
    [
      1589932800,
      86400,
      977566000000,
      978261000000,
      984257000000,
      935452000000,
      952057000000,
      11785486656,
      113659374080189
    ],
    [
      1589846400,
      86400,
      972343000000,
      972351000000,
      989607000000,
      949106000000,
      977566000000,
      11337554900,
      109928494593609
    ]
  ],
  "sequence": 380876982,
  "symbol": "sBTCUSDT",
  "type": "snapshot"
}

< {
  "kline": [
    [
      1590019200,
      86400,
      952057000000,
      952000000000,
      955587000000,
      928440000000,
      941597000000,
      4231329700,
      40057408967508
    ]
  ],
  "sequence": 396865028,
  "symbol": "sBTCUSDT",
  "type": "incremental"
}
```

<a name="klineunsub"/>

### Unsubscribe Kline

It unsubscribes all kline subscriptions or for a symbol.

* Request

```javascript
# unsubscribe all Kline subscriptions
{
  "id": <id>,
  "method": "kline.unsubscribe",
  "params": []
}

# unsubscribe all Kline subscriptions of a symbol
{
  "id": <id>,
  "method": "kline.unsubscribe",
  "params": [
    "<symbol>"
  ]
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

<a name="wosub"/>

### Subscribe Wallet-Order messages

WO subscription requires the session been authorized successfully. DataGW extracts the user information from the given
token and sends WO messages back to client accordingly. 0 or more latest WO snapshot messages will be sent to client
immediately on subscription, and incremental messages will be sent for later updates. Each account snapshot contains a
users' wallets and open / max 100 closed / max 100 filled order event message history.

* Request

```javascript
{
  "id": <id>,
  "method": "wo.subscribe",
  "params": [
    "close/fills limits(default 0, means max 100)
  ]
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample

```javascript
> {
  "id": 1234,
  "method": "wo.subscribe",
  "params": []
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

#### Wallet-Order Message Sample:

```javascript
{"wallets":[],"orders":[{"userID":60463,...}],"sequence":11450, "timestamp":<timestamp>, "type":"<type>"}
```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| timestamp   | Integer| Transaction timestamp in nanoseconds | |
| sequence    | Integer| Latest message sequence |          |
| type        | String | Message type     | snapshot, incremental |

* Sample:

```javascript
< {"orders":{"closed":[{"action":"New","avgPriceEp":0,"baseCurrency":"BTC","baseQtyEv":10000,"bizError":0,"clOrdID":"123456","createTimeNs":1587463924959744646,"cumBaseQtyEv":10000,"cumFeeEv":0,"cumQuoteQtyEv":66900000,"curBaseWalletQtyEv":899990000,"curQuoteWalletQtyEv":66900000,"cxlRejReason":0,"feeCurrency":"BTC","leavesBaseQtyEv":0,"leavesQuoteQtyEv":0,"ordStatus":"Filled","ordType":"Limit","orderID":"35217ade-3c6b-48c7-a280-8a1edb88013e","pegOffsetValueEp":0,"priceEp":68000000,"qtyType":"ByBase","quoteCurrency":"USDT","quoteQtyEv":66900000,"side":"Sell","stopPxEp":0,"symbol":"sBTCUSDT","timeInForce":"GoodTillCancel","transactTimeNs":1587463924964876798,"triggerTimeNs":0,"userID":200076}],"fills":[{"avgPriceEp":0,"baseCurrency":"BTC","baseQtyEv":10000,"clOrdID":"123456","execBaseQtyEv":10000,"execFeeEv":0,"execID":"8135ebe3-f767-577b-b70d-1a839d5178e0","execPriceEp":669000000000,"execQuoteQtyEv":66900000,"feeCurrency":"BTC","lastLiquidityInd":"RemovedLiquidity","ordType":"Limit","orderID":"35217ade-3c6b-48c7-a280-8a1edb88013e","priceEp":68000000,"qtyType":"ByBase","quoteCurrency":"USDT","quoteQtyEv":66900000,"side":"Sell","symbol":"sBTCUSDT","transactTimeNs":1587463924964876798,"userID":200076}],"open":[{"action":"New","avgPriceEp":0,"baseCurrency":"BTC","baseQtyEv":100000000,"bizError":0,"clOrdID":"31f793f4-163d-aa3f-5994-0e1164719ba2","createTimeNs":1587547657438535949,"cumBaseQtyEv":0,"cumFeeEv":0,"cumQuoteQtyEv":0,"curBaseWalletQtyEv":630000005401500000,"curQuoteWalletQtyEv":351802500000,"cxlRejReason":0,"feeCurrency":"BTC","leavesBaseQtyEv":100000000,"leavesQuoteQtyEv":0,"ordStatus":"New","ordType":"Limit","orderID":"b98b25c5-6aa4-4158-b9e5-477e37bd46d8","pegOffsetValueEp":0,"priceEp":666500000000,"qtyType":"ByBase","quoteCurrency":"USDT","quoteQtyEv":0,"side":"Sell","stopPxEp":0,"symbol":"sBTCUSDT","timeInForce":"GoodTillCancel","transactTimeNs":1587547657442752950,"triggerTimeNs":0,"userID":200076}]},"sequence":349,"timestamp":1587549121318737606,"type":"snapshot","wallets":[{"balanceEv":0,"currency":"LTC","lastUpdateTimeNs":1587481897840503662,"lockedTradingBalanceEv":0,"lockedWithdrawEv":0,"userID":200076},{"balanceEv":351802500000,"currency":"USDT","lastUpdateTimeNs":1587543489127498121,"lockedTradingBalanceEv":0,"lockedWithdrawEv":0,"userID":200076},{"balanceEv":630000005401500000,"currency":"BTC","lastUpdateTimeNs":1587547210089640382,"lockedTradingBalanceEv":100000000,"lockedWithdrawEv":0,"userID":200076},{"balanceEv":0,"currency":"ETH","lastUpdateTimeNs":1587481897840503662,"lockedTradingBalanceEv":0,"lockedWithdrawEv":0,"userID":200076},{"balanceEv":0,"currency":"XRP","lastUpdateTimeNs":1587481897840503662,"lockedTradingBalanceEv":0,"lockedWithdrawEv":0,"userID":200076},{"balanceEv":0,"currency":"LINK","lastUpdateTimeNs":1587481897840503662,"lockedTradingBalanceEv":0,"lockedWithdrawEv":0,"userID":200076},{"balanceEv":0,"currency":"XTZ","lastUpdateTimeNs":1587481897840503662,"lockedTradingBalanceEv":0,"lockedWithdrawEv":0,"userID":200076}]}
< {"orders":{"closed":[],"fills":[],"open":[{"action":"New","avgPriceEp":0,"baseCurrency":"BTC","baseQtyEv":100000000,"bizError":0,"clOrdID":"0c1099e5-b900-5351-cf60-edb15ea2539c","createTimeNs":1587549529513521745,"cumBaseQtyEv":0,"cumFeeEv":0,"cumQuoteQtyEv":0,"curBaseWalletQtyEv":630000005401500000,"curQuoteWalletQtyEv":351802500000,"cxlRejReason":0,"feeCurrency":"BTC","leavesBaseQtyEv":100000000,"leavesQuoteQtyEv":0,"ordStatus":"New","ordType":"Limit","orderID":"494a6cbb-32b3-4d6a-b9b7-196ea2506fb5","pegOffsetValueEp":0,"priceEp":666500000000,"qtyType":"ByBase","quoteCurrency":"USDT","quoteQtyEv":0,"side":"Sell","stopPxEp":0,"symbol":"sBTCUSDT","timeInForce":"GoodTillCancel","transactTimeNs":1587549529518394235,"triggerTimeNs":0,"userID":200076}]},"sequence":350,"timestamp":1587549529519959388,"type":"incremental","wallets":[{"balanceEv":630000005401500000,"currency":"BTC","lastUpdateTimeNs":1587547210089640382,"lockedTradingBalanceEv":200000000,"lockedWithdrawEv":0,"userID":200076},{"balanceEv":351802500000,"currency":"USDT","lastUpdateTimeNs":1587543489127498121,"lockedTradingBalanceEv":0,"lockedWithdrawEv":0,"userID":200076}]}

```

<a name="wounsub"/>

### Unsubscribe Wallet-Order

* Request：

```javascript
{
  "id": <id>,
  "method": "wo.unsubscribe",
  "params": []
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

<a name="tickersub"/>

### Subscribe 24 Hours Ticker

On each successful subscription, DataGW will publish 24-hour ticker metrics for all symbols every 1 second.

* Request

```javascript
{
  "id": <id>,
  "method": "spot_market24h.subscribe",
  "params": []
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
    "status": "success"
  }
}
```

* Sample:

```javascript
> {
  "method": "spot_market24h.subscribe",
  "params": [],
  "id": 1234
}

< {
  "error": null,
  "id": 1234,
  "result": {
    "status": "success"
  }
}
```

#### Hours Ticker Message Format：

```javascript
{
  "spot_market24h": {
    "openEp": <open priceEp>,
    "highEp": <high priceEp>,
    "lowEp": <low priceEp>,
    "lastEp": <last priceEp>,
    "bidEp": <bid priceEp>,
    "askEp": <ask priceEp>,
    "symbol": "<symbol>",
    "turnoverEv": <turnoverEv>,
    "volumeEv": <volumeEv>
  },
  "timestamp": <timestamp>
}
```

| Field         | Type   | Description                                | Possible values |
|---------------|--------|--------------------------------------------|--------------|
| open priceEp  | Integer| The scaled open price in last 24 hours     |              |
| high priceEp  | Integer| The scaled highest price in last 24 hours  |              |
| low priceEp   | Integer| The scaled lowest price in last 24 hours   |              |
| last priceEp  | Integer| The scaled last price                      |              |
| bid priceEp   | Integer| Scaled bid price                           |              |
| ask priceEp   | Integer| Scaled ask price                           |              |
| timestamp     | Integer| Timestamp in nanoseconds                   |              |
| symbol        | String | Spot Symbol name                       | [Trading symbols](#productinfo) |
| turnoverEv    | Integer| The scaled turnover value in last 24 hours |              |
| volumeEv      | Integer| The scaled trade volume in last 24 hours   |              |

* Sample:

```javascript
< {
  "spot_market24h": {
    "askEp": 892100000000,
    "bidEp": 891835000000,
    "highEp": 898264000000,
    "lastEp": 892486000000,
    "lowEp": 870656000000,
    "openEp": 896261000000,
    "symbol": "sBTCUSDT",
    "timestamp": 1590571240030003249,
    "turnoverEv": 104718804814499,
    "volumeEv": 11841148100
  },
  "timestamp": 1576490244024818000
}
```

<a name="currencyinfo"/>

### All Spot trading currencies

| currency | value scale factor | min value  |  max value | need addr arg |
|--------|---------------|------------|------------|------------|
|BTC|8|1|5e+18|0|
|USDT|8|1|5e+18|0|
|ETH|8|1|5e+18|0|
|XRP|8|1|5e+18|1|
|LINK|8|1|5e+18|0|
|XTZ|8|1|5e+18|0|
|LTC|8|1|5e+18|0|
|ADA|8|1|5e+18|0|
|TRX|8|1|5e+18|0|
|ONT|8|1|5e+18|0|
|BCH|8|1|5e+18|0|
|NEO|8|1|5e+18|0|
|EOS|8|1|5e+18|1|
|COMP|8|1|5e+18|0|
|LEND|8|1|5e+18|0|
|YFI|8|1|5e+18|0|
|DOT|8|1|5e+18|0|
|UNI|8|1|5e+18|0|
|AAVE|8|1|5e+18|0|
|DOGE|8|1|5e+18|0|
|BAT|8|1|5e+18|0|
|CHZ|8|1|5e+18|0|
|MANA|8|1|5e+18|0|
|ENJ|8|1|5e+18|0|
|SUSHI|8|1|5e+18|0|
|SNX|8|1|5e+18|0|
|GRT|8|1|5e+18|0|
|MKR|8|1|5e+18|0|
|ALGO|8|1|5e+18|0|
|VET|8|1|5e+18|0|
|ZEC|8|1|5e+18|0|
|FIL|8|1|5e+18|0|
|KSM|8|1|5e+18|0|
|XMR|8|1|5e+18|0|
|QTUM|8|1|5e+18|0|
|XLM|8|1|5e+18|1|
|ATOM|8|1|5e+18|1|
|LUNA|8|1|5e+18|1|
|SOL|8|1|5e+18|0|
|AXS|8|1|5e+18|0|
|MATIC|8|1|5e+18|0|
|SHIB|2|1|5e+18|0|
|FTM|8|1|5e+18|0|
|DYDX|8|1|5e+18|0|
|VPAD|4|1|5e+18|0|

<a name="productinfo"/>

### All Spot trading products

|  symbol|  type | price scale factor | ratio scale factor |  baseTickSize|  baseTickSizeEv|  quoteTickSize|  quoteTickSizeEv|  baseQtyPrecision|  quoteQtyPrecision|  pricePrecision|  minOrderValue|  minOrderValueEv|  maxBaseOrderSize|  maxBaseOrderSizeEv|  maxOrderValue|  maxOrderValueEv|  defaultTakerFee|  defaultTakerFeeEr|  defaultMakerFee|  defaultMakerFeeEr|
|---------|---------|---------|---------|-------------|-----------|-----------------|------------|------------|-------------|------|--------|-------|------|--------|-------|------|------|-------|-------|--------|
|sBTCUSDT|Spot|8|8|0.000001 BTC|100|0.01 USDT|1000000|6|2|2|10 USDT|1000000000|1000 BTC|100000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sETHUSDT|Spot|8|8|0.00001 ETH|1000|0.01 USDT|1000000|5|2|2|10 USDT|1000000000|10000 ETH|1000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sXRPUSDT|Spot|8|8|0.1 XRP|10000000|0.00001 USDT|1000|1|2|5|10 USDT|1000000000|5000000 XRP|500000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sLINKUSDT|Spot|8|8|0.01 LINK|1000000|0.0001 USDT|10000|2|2|4|10 USDT|1000000000|5000000 LINK|500000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sXTZUSDT|Spot|8|8|0.01 XTZ|1000000|0.0001 USDT|10000|2|2|4|10 USDT|1000000000|2000000 XTZ|200000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sLTCUSDT|Spot|8|8|0.00001 LTC|1000|0.01 USDT|1000000|5|2|2|10 USDT|1000000000|100000 LTC|10000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sADAUSDT|Spot|8|8|0.1 ADA|10000000|0.00005 USDT|5000|1|2|5|10 USDT|1000000000|5000000 ADA|500000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sTRXUSDT|Spot|8|8|0.1 TRX|10000000|0.00005 USDT|5000|1|2|5|10 USDT|1000000000|5000000 TRX|500000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sONTUSDT|Spot|8|8|0.1 ONT|10000000|0.0005 USDT|50000|1|2|4|10 USDT|1000000000|5000000 ONT|500000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sBCHUSDT|Spot|8|8|0.00001 BCH|1000|0.01 USDT|1000000|5|2|2|10 USDT|1000000000|10000 BCH|1000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sNEOUSDT|Spot|8|8|0.001 NEO|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|5000000 NEO|500000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sEOSUSDT|Spot|8|8|0.01 EOS|1000000|0.0001 USDT|10000|2|2|4|10 USDT|1000000000|5000000 EOS|500000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sDOGEUSDT|Spot|8|8|1 DOGE|100000000|0.000001 USDT|100|0|2|6|10 USDT|1000000000|5000000 DOGE|500000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sBATUSDT|Spot|8|8|0.01 BAT|1000000|0.00001 USDT|1000|2|2|5|10 USDT|1000000000|300000 BAT|30000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sCHZUSDT|Spot|8|8|0.01 CHZ|1000000|0.00001 USDT|1000|2|2|5|10 USDT|1000000000|700000 CHZ|70000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sMANAUSDT|Spot|8|8|0.01 MANA|1000000|0.00001 USDT|1000|2|2|5|10 USDT|1000000000|400000 MANA|40000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sENJUSDT|Spot|8|8|0.01 ENJ|1000000|0.00001 USDT|1000|2|2|5|10 USDT|1000000000|200000 ENJ|20000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sSUSHIUSDT|Spot|8|8|0.001 SUSHI|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|40000 SUSHI|4000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sSNXUSDT|Spot|8|8|0.001 SNX|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|30000 SNX|3000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sGRTUSDT|Spot|8|8|0.01 GRT|1000000|0.00001 USDT|1000|2|2|5|10 USDT|1000000000|200000 GRT|20000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sUNIUSDT|Spot|8|8|0.001 UNI|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|15000 UNI|1500000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sAAVEUSDT|Spot|8|8|0.0001 AAVE|10000|0.01 USDT|1000000|4|2|2|10 USDT|1000000000|1000 AAVE|100000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sYFIUSDT|Spot|8|8|0.00001 YFI|1000|0.01 USDT|1000000|5|2|2|10 USDT|1000000000|10 YFI|1000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sCOMPUSDT|Spot|8|8|0.0001 COMP|10000|0.01 USDT|1000000|4|2|2|10 USDT|1000000000|1000 COMP|100000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sMKRUSDT|Spot|8|8|0.00001 MKR|1000|0.01 USDT|1000000|5|2|2|10 USDT|1000000000|100 MKR|10000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sDOTUSDT|Spot|8|8|0.001 DOT|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|10000 DOT|1000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sALGOUSDT|Spot|8|8|0.01 ALGO|1000000|0.00001 USDT|1000|2|2|5|10 USDT|1000000000|300000 ALGO|30000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sVETUSDT|Spot|8|8|0.1 VET|10000000|0.000001 USDT|100|1|2|6|10 USDT|1000000000|2000000 VET|200000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sZECUSDT|Spot|8|8|0.0001 ZEC|10000|0.01 USDT|1000000|4|2|2|10 USDT|1000000000|2000 ZEC|200000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sFILUSDT|Spot|8|8|0.0001 FIL|10000|0.01 USDT|1000000|4|2|2|10 USDT|1000000000|3000 FIL|300000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sKSMUSDT|Spot|8|8|0.0001 KSM|10000|0.01 USDT|1000000|4|2|2|10 USDT|1000000000|1000 KSM|100000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sXMRUSDT|Spot|8|8|0.0001 XMR|10000|0.01 USDT|1000000|4|2|2|10 USDT|1000000000|1500 XMR|150000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sQTUMUSDT|Spot|8|8|0.001 QTUM|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|30000 QTUM|3000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sXLMUSDT|Spot|8|8|0.01 XLM|1000000|0.00001 USDT|1000|2|2|5|10 USDT|1000000000|1000000 XLM|100000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sATOMUSDT|Spot|8|8|0.001 ATOM|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|20000 ATOM|2000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sLUNAUSDT|Spot|8|8|0.001 LUNA|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|40000 LUNA|4000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sSOLUSDT|Spot|8|8|0.001 SOL|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|10000 SOL|1000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sAXSUSDT|Spot|8|8|0.001 AXS|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|10000 AXS|1000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sMATICUSDT|Spot|8|8|0.01 MATIC|1000000|0.00001 USDT|1000|2|2|5|10 USDT|1000000000|300000 MATIC|30000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sSHIBUSDT|Spot|8|8|1 SHIB|100|0.00000001 USDT|1|0|2|8|10 USDT|1000000000|5000000000 SHIB|500000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sFTMUSDT|Spot|8|8|0.01 FTM|1000000|0.00001 USDT|1000|2|2|5|10 USDT|1000000000|200000 FTM|20000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sDYDXUSDT|Spot|8|8|0.001 DYDX|100000|0.001 USDT|100000|3|2|3|10 USDT|1000000000|30000 DYDX|3000000000000|5000000 USDT|500000000000000|0.001|100000|0.001|100000|
|sVPADUSDT|Spot|8|8|0.1 VPAD|1000|0.000001 USDT|100|1|2|6|10 USDT|1000000000|15000000 VPAD|150000000000|500000 USDT|50000000000000|0.001|100000|0.001|100000|

<a name="investmentaccount"/>

### Subscribe Investment Account

on subscription to investment account then you will get your investment information of each currency type.

* Request：

```javascript
{
  "id": <id>,
  "method": "wm.subscribe",
  "params": []
}
```

* Response:

```javascript
{
  "error": null,
  "id": <id>,
  "result": {
      "status":"success"
    }
}
```

* Sample：

```javascript
{
  "id": 1234,
  "method": "wm.subscribe",
  "params": []
}

{
  "error": null,
  "id": 1234,
  "result": {
      "status":"success"
    }
}
```

#### Investment Account Message Format：

```javascript
{
  "investments":[
    {
      "currency":<currency>,
      "balanceEv":<balanceEv>,
      "userId":<userId>,
      "demandPendingInterestBalanceEv":<demandPendingInterestBalanceEv>,
      "demandInterestedBalanceEv":<demandInterestedBalanceEv>,
      "timedDepositBalanceEv":<timedDepositBalanceEv>,
      "currentTimeMillis":<currentTimeMillis>
  ]
}
```

| Field       | Type   | Description      | Possible values |
|-------------|--------|------------------|-----------------|
| currency    | String |invested currency |      BTC,ETH    |
| balanceEv   | Long   |invested amount   |        0        |
| userId      | Long   | your user id     | 1234            |
| demandPendingInterestBalanceEv | Long   | pending interest for flexible product  | 0 |
| demandInterestedBalanceEv      | Long   | paid interest for flexible product     | 0 |
| timedDepositBalanceEv          | Long | amount for fixed product                 | 20000000000 |
| currentTimeMillis              | Long |   time in milli    | 1653972360166 |

* Sample：

```javascript
{
  "investments":[
    {
      "currency":"USDT",
      "balanceEv":21797700000,
      "userId":1234,
      "demandPendingInterestBalanceEv":0,
      "demandInterestedBalanceEv":0,
      "timedDepositBalanceEv":20000000000,
      "currentTimeMillis":1653972360161
    },
    {
      "currency":"BTC",
      "balanceEv":0,
      "userId":1234,
      "demandPendingInterestBalanceEv":0,
      "demandInterestedBalanceEv":0,
      "timedDepositBalanceEv":0,
      "currentTimeMillis":1653972360166
    }
  ]
}
```
