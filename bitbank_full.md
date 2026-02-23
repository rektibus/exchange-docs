# Official Documentation for the bitbank.cc APIs and Streams.

[日本語](README_JP.md)

* Official Announcements regarding system maintenance, api update, etc. will be reported here: **[https://blog.bitbank.cc/tag/service](https://blog.bitbank.cc/tag/service)**

Name | Description
------------ | ------------
[rest-api.md](./rest-api.md) | Details on the Private REST API.
[public-api.md](./public-api.md) | Details on the Public API.
[public-stream.md](./public-stream.md) | Details on available real time streams api.
[private-stream.md](./private-stream.md) | Details on available real time private streams api.
[errors.md](./errors.md) | Descriptions of possible error messages from the Private REST API.

**Issue Tracker:**

Bug reports are welcome! You can use the issue tracker to report bugs and request features on [https://github.com/bitbankinc/bitbank-api-docs/issues](https://github.com/bitbankinc/bitbank-api-docs/issues).

Pull request welcome! You can use our pull request to improve our documents [https://github.com/bitbankinc/bitbank-api-docs/pulls](https://github.com/bitbankinc/bitbank-api-docs/pulls).
[日本語](public-api_JP.md)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Public REST API for Bitbank](#public-rest-api-for-bitbank)
  - [General API Information](#general-api-information)
  - [General endpoints](#general-endpoints)
    - [Ticker](#ticker)
    - [Tickers](#tickers)
    - [TickersJPY](#tickersjpy)
    - [Depth](#depth)
      - [In circuit_break_info.mode is `NONE` or estimated price is null](#in-circuit_break_infomode-is-none-or-estimated-price-is-null)
      - [In circuit_break_info.mode is not `NONE` and estimated price is not null](#in-circuit_break_infomode-is-not-none-and-estimated-price-is-not-null)
    - [Transactions](#transactions)
    - [Candlestick](#candlestick)
    - [Circuit Break Info](#circuit-break-info)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Public REST API for Bitbank

## General API Information

- The base endpoint is: **[https://public.bitbank.cc](https://public.bitbank.cc)**
- HTTP `4XX` return codes are used for malformed requests; the issue is on the sender's side.
- Any endpoint can return an ERROR; the error payload is as follows:

```json
{
  "success": 0,
  "data": {
    "code": 10000
  }
}
```

## General endpoints

### Ticker

Get Ticker information

Except for continuous trading mode, it may be the case that sell <= buy.

```txt
GET /{pair}/ticker
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | YES | pair enum: [pair list](pairs.md)

**Response:**

Name | Type | Description
------------ | ------------ | ------------
sell | string | the lowest price of sell orders
buy | string | the highest price of buy orders
high | string | the highest price in last 24 hours
low | string | the lowest price in last 24 hours
open | string | the open price at 24 hours ago
last | string | the latest price executed
vol | string | trading volume in last 24 hours
timestamp | number | ticked at unix timestamp (milliseconds)

**Response format:**

```json
{
  "success": 1,
  "data": {
    "sell": "string",
    "buy": "string",
    "high": "string",
    "low": "string",
    "open": "string",
    "last": "string",
    "vol": "string",
    "timestamp": 0
  }
}
```

### Tickers

Get All Tickers information

Except for continuous trading mode, it may be the case that sell <= buy.

```txt
GET /tickers
```

**Parameters:**

nothing

**Response:**

Name | Type | Description
------------ | ------------ | ------------
pair | string | pair enum: [pair list](pairs.md)
sell | string | the lowest price of sell orders
buy | string | the highest price of buy orders
high | string | the highest price in last 24 hours
low | string | the lowest price in last 24 hours
open | string | the open price at 24 hours ago
last | string | the latest price executed
vol | string | trading volume in last 24 hours
timestamp | number | ticked at unix timestamp (milliseconds)

**Response format:**

```json
{
  "success": 1,
  "data": [{
    "pair": "string",
    "sell": "string",
    "buy": "string",
    "high": "string",
    "low": "string",
    "open": "string",
    "last": "string",
    "vol": "string",
    "timestamp": 0
  }]
}
```

### TickersJPY

Get All JPY Pair Tickers information

Except for continuous trading mode, it may be the case that sell <= buy.

```txt
GET /tickers_jpy
```

**Parameters:**

nothing

**Response:**

Name | Type | Description
------------ | ------------ | ------------
pair | string | JPY pair enum: [pair list](pairs.md)
sell | string | the lowest price of sell orders
buy | string | the highest price of buy orders
high | string | the highest price in last 24 hours
low | string | the lowest price in last 24 hours
open | string | the open price at 24 hours ago
last | string | the latest price executed
vol | string | trading volume in last 24 hours
timestamp | number | ticked at unix timestamp (milliseconds)

**Response format:**

```json
{
  "success": 1,
  "data": [{
    "pair": "string",
    "sell": "string",
    "buy": "string",
    "high": "string",
    "low": "string",
    "open": "string",
    "last": "string",
    "vol": "string",
    "timestamp": 0
  }]
}
```

### Depth

Get Depth information.

#### In circuit_break_info.mode is `NONE` or estimated price is null

- Asks and bids data is restricted to 200 entries each from best bid offer.
- Asks and bids price never cross.

#### In circuit_break_info.mode is not `NONE` and estimated price is not null

- Asks and bids data is restricted to 200 entries each around the estimated price. (Max 400 entries)
- Asks and bids price possibly cross.
- asks_under, bids_over possibly includes the quantity of orders which price is out of range.

```txt
GET /{pair}/depth
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | YES | pair enum: [pair list](pairs.md)

**Response:**

Name | Type | Description
------------ | ------------ | ------------
asks | [string, string][] | array of [price, amount]
bids | [string, string][] | array of [price, amount]
asks_over | string | the quantity of asks over the highest price of asks orders.
bids_under | string | the quantity of bids under the lowest price of bids orders.
asks_under | string | the quantity of asks under the lowest price of asks orders. Usually "0" in `NORMAL` mode.
bids_over | string | the quantity of bids over the highest price of bids orders. Usually "0" in `NORMAL` mode.
ask_market | string | the quantity of market sell orders. Usually "0" in `NORMAL` mode.
bid_market | string | the quantity of market buy orders. Usually "0" in `NORMAL` mode.
timestamp | number | published at timestamp
sequenceId | number | sequence id, increased monotonically but not always consecutive

**Response format:**

```json
{
  "success": 1,
  "data": {
    "asks": [
      [
        "string",  "string"
      ]
    ],
    "bids": [
      [
        "string",  "string"
      ]
    ],
    "asks_over": "string",
    "bids_under": "string",
    "asks_under": "string",
    "bids_over": "string",
    "ask_market": "string",
    "bid_market": "string",
    "timestamp": 0,
    "sequenceId": "string"
  }
}
```

### Transactions

Get latest executed transactions. If you omit YYYYMMDD, you can get the latest 60.

```txt
GET /{pair}/transactions/{YYYYMMDD}
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | YES | pair enum: [pair list](pairs.md)
YYYYMMDD | string | NO | date formatted as `YYYYMMDD`

**Response:**

Name | Type | Description
------------ | ------------ | ------------
transaction_id | number | transaction id
side | string | enum: `buy`, `sell`
price | string | price
amount | string | amount
executed_at | number | executed at unix timestamp (milliseconds)

**Response format:**

```json
{
  "success": 1,
  "data": {
    "transactions": [
      {
        "transaction_id": 0,
        "side": "string",
        "price": "string",
        "amount": "string",
        "executed_at": 0
      }
    ]
  }
}
```

### Candlestick

Get candlestick information.

```txt
GET /{pair}/candlestick/{candle-type}/{YYYY}
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | YES | pair enum: [pair list](pairs.md)
candle-type | string | YES | candle type enum: `1min`, `5min`, `15min`, `30min`, `1hour`, `4hour`, `8hour`, `12hour`, `1day`, `1week`, `1month`
YYYY | string | YES | date formatted as `YYYY` or  `YYYYMMDD`

- YYYY Format depends on the candle-type:
  - `YYYYMMDD`: `1min`, `5min`, `15min`, `30min`, `1hour`
  - `YYYY`: `4hour`, `8hour`, `12hour`, `1day`, `1week`, `1month`

**Response:**

Name | Type | Description
------------ | ------------ | ------------
type | string | candle type enum: `1min`, `5min`, `15min`, `30min`, `1hour`, `4hour`, `8hour`, `12hour`, `1day`, `1week`, `1month`
ohlcv | [string, string, string, string, string, number][] | [open, high, low, close, volume, **unix timestamp (milliseconds)**]

**Response format:**

```json
{
  "success": 1,
  "data": {
    "candlestick": [
      {
        "type": "string",
        "ohlcv": [
          [
            "string",
            "string",
            "string",
            "string",
            "string",
            0
          ]
        ]
      }
    ]
  }
}
```

### Circuit Break Info

Get circuit break informations.

```txt
GET /{pair}/circuit_break_info
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | YES | pair enum: [pair list](pairs.md)

**Response:**

Name | Type | Description
------------ | ------------ | ------------
mode | string | enum: `NONE`, `CIRCUIT_BREAK`, `FULL_RANGE_CIRCUIT_BREAK`, `RESUMPTION`, `LISTING`
estimated_itayose_price | string \| null | estimated price. Null if mode is `NONE` or when there is no estimated price.
estimated_itayose_amount | string \| null | estimated amount. Null if mode is `NONE`.
itayose_upper_price | string \| null | itayose price range upper limit. Null if mode is in `NONE`, `FULL_RANGE_CIRCUIT_BREAK` or `LISTING`.
itayose_lower_price | string \| null | itayose price range lower limit. Null if mode is in `NONE`, `FULL_RANGE_CIRCUIT_BREAK` or `LISTING`.
upper_trigger_price | string \| null | upper trigger price. Null if mode is not `NONE`.
lower_trigger_price | string \| null | lower trigger price. Null if mode is not `NONE`.
fee_type | string | enum: `NORMAL`, `SELL_MAKER`, `BUY_MAKER`, `DYNAMIC`
reopen_timestamp | number \| null | reopen timestamp(milliseconds). Null if mode is `NONE`, or reopen timestamp is undetermined yet.
timestamp | number | ticked at unix timestamp (milliseconds)

For details on `mode` and `fee_type`, please check the [Circuit breaker system](https://bitbank.cc/docs/circuit-breaker-mode/) page.

**Response format:**

```json
{
  "success": 1,
  "data": {
    "mode": "string",
    "estimated_itayose_price": "string",
    "estimated_itayose_amount": "string",
    "itayose_upper_price": "string",
    "itayose_lower_price": "string",
    "upper_trigger_price": "string",
    "lower_trigger_price": "string",
    "fee_type": "string",
    "reopen_timestamp": 0,
    "timestamp": 0
  }
}
```
[日本語](rest-api_JP.md)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Private REST API for Bitbank](#private-rest-api-for-bitbank)
  - [General API Information](#general-api-information)
  - [Authorization](#authorization)
    - [ACCESS-TIME-WINDOW method](#access-time-window-method)
    - [ACCESS-NONCE method](#access-nonce-method)
    - [ACCESS-SIGNATURE](#access-signature)
      - [Sample](#sample)
        - [ACCESS-TIME-WINDOW](#access-time-window)
        - [ACCESS-NONCE](#access-nonce)
  - [Rate limit](#rate-limit)
  - [General endpoints](#general-endpoints)
    - [Assets](#assets)
      - [return user's asset list](#return-users-asset-list)
    - [Order](#order)
      - [Fetch order information](#fetch-order-information)
      - [Create new order](#create-new-order)
      - [Cancel order](#cancel-order)
      - [Cancel multiple orders](#cancel-multiple-orders)
      - [Fetch multiple orders](#fetch-multiple-orders)
      - [Fetch active orders](#fetch-active-orders)
    - [Margin](#margin)
      - [Fetch Margin Trading Status](#fetch-margin-trading-status)
      - [Fetch positions information](#fetch-positions-information)
    - [Trade](#trade)
      - [Fetch trade history](#fetch-trade-history)
    - [Deposit](#deposit)
      - [Fetch deposit history](#fetch-deposit-history)
      - [Fetch unconfirmed deposits](#fetch-unconfirmed-deposits)
      - [Fetch deposit originators](#fetch-deposit-originators)
      - [Confirm deposits](#confirm-deposits)
      - [Confirm all deposits](#confirm-all-deposits)
    - [Withdrawal](#withdrawal)
      - [Get withdrawal accounts](#get-withdrawal-accounts)
      - [New withdrawal request](#new-withdrawal-request)
      - [Fetch withdrawal history](#fetch-withdrawal-history)
    - [Status](#status)
      - [Get exchange status](#get-exchange-status)
    - [Settings](#settings)
      - [Get all pairs info](#get-all-pairs-info)
    - [Private stream](#private-stream)
      - [Get channel and token for private stream](#get-channel-and-token-for-private-stream)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Private REST API for Bitbank

## General API Information

- The base endpoint is: **[https://api.bitbank.cc/v1](https://api.bitbank.cc/v1)**
- Any endpoint can return an ERROR; the error payload is as follows:

```json
{
  "success": 0,
  "data": {
    "code": 20003
  }
}
```

- Specific error codes and messages defined in another document [errors.md](errors.md).
- For `GET` endpoints, parameters must be sent as a `query string`.
- For `POST` endpoints, the parameters may be sent as a `request body` with content type `application/json`.
- Parameters may be sent in any order.

## Authorization

- Private REST API requires requests contain additional HTTP Authorization headers with the following information.
- If both ACCESS-NONCE and ACCESS-TIME-WINDOW are specified, the ACCESS-TIME-WINDOW method takes precedence.

### ACCESS-TIME-WINDOW method

- ACCESS-KEY : ACCESS-KEY and API secret can be generated in your access key page.
- ACCESS-SIGNATURE : Specify the signature described below.
- ACCESS-REQUEST-TIME : ACCESS-REQUEST-TIME should be an integer and usually use the current UNIX timestamp (in milliseconds). Please note that the time zone is UTC.
- ACCESS-TIME-WINDOW : ACCESS-TIME-WINDOW should be an integer and allows you to specify the number of milliseconds a request is valid. If not specified, 5000 will be applied by default. We recommend using a small value below 5000. The maximum value cannot exceed 60000. The logic is as follows.

```typescript
if (ACCESS-REQUEST-TIME < (serverTime + 1000) && (serverTime - ACCESS-REQUEST-TIME) <= ACCESS-TIME-WINDOW) {
  // process request
} else {
  // reject request
}
```

### ACCESS-NONCE method

- ACCESS-KEY : ACCESS-KEY and API secret can be generated in your access key page.
- ACCESS-NONCE : ACCESS-NONCE should be an integer and increased every time a new request is issued (you can use unix timestamp as ACCESS-NONCE).
- ACCESS-SIGNATURE : Specify the signature described below.

### ACCESS-SIGNATURE

- Hash the following string with `HMAC-SHA256`, using your API secret as hash key.
  - GET: [ACCESS-NONCE, full request path with query parameters] concatenated (include `/v1` in request path).
  - POST: [ACCESS-NONCE, JSON string of request body] concatenated (include query parameters in request body).

#### Sample

##### ACCESS-TIME-WINDOW

- e.g. GET: /v1/user/assets

```bash
export API_SECRET="hoge"
export ACCESS_REQUEST_TIME="1721121776490"
export ACCESS_TIME_WINDOW="1000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_REQUEST_TIME$ACCESS_TIME_WINDOW/v1/user/assets" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"


echo $ACCESS_SIGNATURE
9ec5745960d05573c8fb047cdd9191bd0c6ede26f07700bb40ecf1a3920abae8
```

- e.g. POST endpoint

```bash
export API_SECRET="hoge"
export ACCESS_REQUEST_TIME="1721121776490"
export ACCESS_TIME_WINDOW="1000"
export REQUEST_BODY='{"pair": "xrp_jpy", "price": "20", "amount": "1","side": "buy", "type": "limit"}'
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_REQUEST_TIME$ACCESS_TIME_WINDOW$REQUEST_BODY" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"


echo $ACCESS_SIGNATURE
7868665738ae3f8a796224e0413c1351ddd7ec2af121db12815c0a5b74b8764c
```

##### ACCESS-NONCE

- e.g. GET: /v1/user/assets

```bash
export API_SECRET="hoge"
export ACCESS_NONCE="1721121776490"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/assets" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"


echo $ACCESS_SIGNATURE
f957817b95c3af6cf5e2e9dfe1503ea8088f46879d4ab73051467fd7b94f1aba
```

- e.g. POST endpoint

```bash
export API_SECRET="hoge"
export ACCESS_NONCE="1721121776490"
export REQUEST_BODY='{"pair": "xrp_jpy", "price": "20", "amount": "1","side": "buy", "type": "limit"}'
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE$REQUEST_BODY" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"


echo $ACCESS_SIGNATURE
8ef83c2b991765b18c95aade7678471747c06890a23a453c76238345b5c86fb8
```

## Rate limit

- We limits REST API calls per user, per UPDATE or QUERY, per second.
  - UPDATE is order, cancel and withdrawal request.
  - QUERY is others.
- We also limits REST API calls system wide, to avoid overload of our matching engine.
  - This limit is high enough for usual case.
- We return HTTP 429 when you reached a limit. Please reduce API calls when you get 429 often.
- We usually limits QUERY requests to 10 calls per second and UPDATE requests to 6 calls per second.
  - We can raise your rate limits depending on your usage.
  - Please contact `onboarding@bitcoinbank.co.jp` from your bitbank account's email address to raise limits.

## General endpoints

### Assets

#### return user's asset list

```txt
GET /user/assets
```

**Parameters:**
None

**Response:**

Name | Type | Description
------------ | ------------ | ------------
asset | string  | asset enum: [asset list](assets.md)
free_amount | string | free amount
amount_precision | number | amount precision
onhand_amount | string | onhand amount
locked_amount | string | locked amount
withdrawing_amount | string | amount of locked amount being withdrawn
withdrawal_fee | { min: string, max: string } or { under: string, over: string, threshold:string } for `jpy` | withdrawal fee
stop_deposit | boolean | deposit status（All networks: stop_deposit = `true`）
stop_withdrawal | boolean | withdrawal status（All networks: stop_withdrawal = `true`）
network_list | { asset: string, network: string, stop_deposit: boolean, stop_withdrawal: boolean, withdrawal_fee: string } or undefined for `jpy` | network list
collateral_ratio | string | collateral ratio

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/assets" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/assets"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "assets": [
      {
        "asset": "string",
        "free_amount": "string",
        "amount_precision": 0,
        "onhand_amount": "string",
        "locked_amount": "string",
        "withdrawing_amount": "string",
        "withdrawal_fee": {
            "min": "string",
            "max": "string"
        },
        "stop_deposit": false,
        "stop_withdrawal": false,
        "network_list": [
            {
                "asset": "string",
                "network": "string",
                "stop_deposit": false,
                "stop_withdrawal": false,
                "withdrawal_fee": "string"
            }
        ],
        "collateral_ratio": "string"
      },
      {
        "asset": "jpy",
        "free_amount": "string",
        "amount_precision": 0,
        "onhand_amount": "string",
        "locked_amount": "string",
        "withdrawing_amount": "string",
        "withdrawal_fee": {
            "under": "string",
            "over": "string",
            "threshold": "string"
        },
        "stop_deposit": false,
        "stop_withdrawal": false,
        "collateral_ratio": "string"
      },
    ]
  }
}
```


### Order

#### Fetch order information

```txt
GET /user/spot/order
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | YES | pair enum: [pair list](pairs.md)
order_id | number | YES | order id

**Response:**

Name | Type | Description
------------ | ------------ | ------------
order_id | number | order id
pair | string | pair enum: [pair list](pairs.md)
side | string | `buy` or `sell`
position_side | string \| undefined | `long` or `short`(only for margin trading)
type | string | one of `limit`, `market`, `stop`, `stop_limit`, `take_profit`, `stop_loss`, `losscut`
start_amount | string \| null | order qty when placed
remaining_amount | string \| null | qty not executed
executed_amount| string | qty executed
price | string \| undefined | order price (present only if type = `limit` or `stop_limit`)
post_only | boolean \| undefined | whether Post Only or not (present only if type = `limit`)
user_cancelable | boolean | whether cancelable order or not
average_price | string | avg executed price
ordered_at | number | ordered at unix timestamp (milliseconds)
expire_at | number \| null | expiration time in unix timestamp (milliseconds)
triggered_at | number \| undefined | triggered at unix timestamp (milliseconds) (present only if type = `stop`, `stop_limit`, `take_profit`, `stop_loss`)
trigger_price | string \| undefined | trigger price (present only if type = `stop`, `stop_limit`, `take_profit`, `stop_loss`)
status | string | status enum: `INACTIVE`, `UNFILLED`, `PARTIALLY_FILLED`, `FULLY_FILLED`, `CANCELED_UNFILLED`, `CANCELED_PARTIALLY_FILLED`, `REJECTED`

**Caveat:**

* This API cannot fetch informations of an order that is executed or canceled more than 3 months ago. (it returns a 50009 error code.)
  Please use [the page of download order history](https://app.bitbank.cc/account/data/orders/download) instead for fetching those orders.

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/spot/order?pair=btc_jpy&order_id=1" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/spot/order?pair=btc_jpy&order_id=1"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "order_id": 0,
    "pair": "string",
    "side": "string",
    "position_side": "string",
    "type": "string",
    "start_amount": "string",
    "remaining_amount": "string",
    "executed_amount": "string",
    "price": "string",
    "post_only": false,
    "user_cancelable": true,
    "average_price": "string",
    "ordered_at": 0,
    "expire_at": 0,
    "triggered_at": 0,
    "trigger_price": "string",
    "status": "string"
  }
}
```

#### Create new order

```txt
POST /user/spot/order
```

**Parameters(requestBody):**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | YES | pair enum: [pair list](pairs.md)
amount | string | NO | amount. required if type is other than `take_profit`, `stop_loss`
price | string | NO | price
side | string | YES | `buy` or `sell`
position_side | string | NO | `long` or `short`
type | string | YES | one of `limit`, `market`, `stop`, `stop_limit`, `take_profit`, `stop_loss`, `losscut`
post_only | boolean | NO | Post Only (`true` can be specified only if type = `limit`. default `false`)
trigger_price | string | NO | trigger price

**Response:**

Name | Type | Description
------------ | ------------ | ------------
order_id | number | order id
pair | string | pair enum: [pair list](pairs.md)
side | string | `buy` or `sell`
position_side | string \| undefined | `long` or `short`(only for margin trading)
type | string | one of `limit`, `market`, `stop`, `stop_limit`, `take_profit`, `stop_loss`, `losscut`
start_amount | string \| null | order qty when placed
remaining_amount | string \| null | qty not executed
executed_amount| string | qty executed
price | string \| undefined | order price (present only if type = `limit` or `stop_limit`)
post_only | boolean \| undefined | whether Post Only or not (present only if type = `limit`)
user_cancelable | boolean | whether cancelable order or not
average_price | string | avg executed price
ordered_at | number | ordered at unix timestamp (milliseconds)
expire_at | number \| null | expiration time in unix timestamp (milliseconds)
trigger_price | string \| undefined | trigger price (present only if type = `stop`, `stop_limit`, `take_profit`, `stop_loss`)
status | string | status enum: `INACTIVE`, `UNFILLED`, `PARTIALLY_FILLED`, `FULLY_FILLED`, `CANCELED_UNFILLED`, `CANCELED_PARTIALLY_FILLED`

**Caveat:**
- Except for circuit_break_info.mode is `NONE`, market order are restricted. If restricted, it returns 70020 error code.
- `post_only` option is treated as `false` except, circuit_break_info.mode is `NONE`.

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export REQUEST_BODY='{"pair": "xrp_jpy", "price": "20", "amount": "1","side": "buy", "type": "limit"}'
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE$REQUEST_BODY" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" -H "Content-Type: application/json" -d "$REQUEST_BODY" "https://api.bitbank.cc/v1/user/spot/order"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "order_id": 0,
    "pair": "string",
    "side": "string",
    "position_side": "string",
    "type": "string",
    "start_amount": "string",
    "remaining_amount": "string",
    "executed_amount": "string",
    "price": "string",
    "post_only": false,
    "user_cancelable": true,
    "average_price": "string",
    "ordered_at": 0,
    "expire_at": 0,
    "trigger_price": "string",
    "status": "string"
  }
}
```

#### Cancel order

```txt
POST /user/spot/cancel_order
```

**Parameters(requestBody):**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | YES | pair enum: [pair list](pairs.md)
order_id | number | YES | order id

**Response:**

Name | Type | Description
------------ | ------------ | ------------
order_id | number | order id
pair | string | pair enum: [pair list](pairs.md)
side | string | `buy` or `sell`
position_side | string \| undefined | `long` or `short`(only for margin trading)
type | string | one of `limit`, `market`, `stop`, `stop_limit`, `take_profit`, `stop_loss`, `losscut`
start_amount | string \| null | order qty when placed
remaining_amount | string \| null | qty not executed
executed_amount| string | qty executed
price | string \| undefined | order price (present only if type = `limit` or `stop_limit`)
post_only | boolean \| undefined | whether Post Only or not (present only if type = `limit`)
user_cancelable | boolean | whether cancelable order or not
average_price | string | avg executed price
ordered_at | number | ordered at unix timestamp (milliseconds)
expire_at | number \| null | expiration time in unix timestamp (milliseconds)
canceled_at | number | canceled at unix timestamp (milliseconds)
triggered_at | number \| undefined | triggered at unix timestamp (milliseconds) (present only if type = `stop`, `stop_limit`, `take_profit`, `stop_loss`)
trigger_price | string \| undefined | trigger price (present only if type = `stop`, `stop_limit`, `take_profit`, `stop_loss`)
status | string | status enum: `INACTIVE`, `UNFILLED`, `PARTIALLY_FILLED`, `FULLY_FILLED`, `CANCELED_UNFILLED`, `CANCELED_PARTIALLY_FILLED`

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export REQUEST_BODY='{"pair": "xrp_jpy", "order_id": 1}'
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE$REQUEST_BODY" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" -H "Content-Type: application/json" -d "$REQUEST_BODY" "https://api.bitbank.cc/v1/user/spot/cancel_order"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "order_id": 0,
    "pair": "string",
    "side": "string",
    "position_side": "string",
    "type": "string",
    "start_amount": "string",
    "remaining_amount": "string",
    "executed_amount": "string",
    "price": "string",
    "post_only": false,
    "user_cancelable": true,
    "average_price": "string",
    "ordered_at": 0,
    "expire_at": 0,
    "canceled_at": 0,
    "triggered_at": 0,
    "trigger_price": "string",
    "status": "string"
  }
}
```

#### Cancel multiple orders

```txt
POST /user/spot/cancel_orders
```

**Parameters(requestBody):**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | YES | pair enum: [pair list](pairs.md)
order_ids | number[] | YES | order ids. Up to 30 ids can be specified

**Response:**

Name | Type | Description
------------ | ------------ | ------------
orders | Array | list of object same as [Cancel order response](#cancel-order)

**Response format:**

```json
{
  "success": 1,
  "data": {
    "orders": [
      {
        "order_id": 0,
        "pair": "string",
        "side": "string",
        "type": "string",
        "start_amount": "string",
        "remaining_amount": "string",
        "executed_amount": "string",
        "price": "string",
        "post_only": false,
        "user_cancelable": true,
        "average_price": "string",
        "ordered_at": 0,
        "expire_at": 0,
        "canceled_at": 0,
        "triggered_at": 0,
        "trigger_price": "string",
        "status": "string"
      }
    ]
  }
}
```

#### Fetch multiple orders

```txt
POST /user/spot/orders_info
```

*(it should be a POST method)*

**Parameters (requestBody):**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | YES | pair enum: [pair list](pairs.md)
order_ids | number[] | YES | order ids

**Caveat:**

* This API cannot fetch informations of orders that is executed or canceled more than 3 months ago. (it don't return any error nor those orders.)
  Please use [the page of download order history](https://app.bitbank.cc/account/data/orders/download) instead for fetching those orders.

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export REQUEST_BODY='{"pair": "xrp_jpy", "order_ids": [1]}'
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE$REQUEST_BODY" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" -H "Content-Type: application/json" -d "$REQUEST_BODY" "https://api.bitbank.cc/v1/user/spot/orders_info"
```

</p>
</details>

**Response:**

Name | Type | Description
------------ | ------------ | ------------
orders | Array | list of object same as [Fetch order information response](#fetch-order-information)

**Response format:**

```json
{
  "success": 1,
  "data": {
    "orders": [
      {
        "order_id": 0,
        "pair": "string",
        "side": "string",
        "position_side": "string",
        "type": "string",
        "start_amount": "string",
        "remaining_amount": "string",
        "executed_amount": "string",
        "price": "string",
        "post_only": false,
        "user_cancelable": true,
        "average_price": "string",
        "ordered_at": 0,
        "expire_at": 0,
        "canceled_at": 0,
        "triggered_at": 0,
        "trigger_price": "string",
        "status": "string"
      }
    ]
  }
}
```
#### Fetch active orders

```txt
GET /user/spot/active_orders
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | NO | pair enum: [pair list](pairs.md). when specifying an order id, pair must also be specified
count | number | NO | take limit
from_id | number | NO | take from order id
end_id | number | NO | take until order id
since | number | NO | since unix timestamp
end | number | NO | end unix timestamp

**Response:**

Name | Type | Description
------------ | ------------ | ------------
orders | Array | list of object same as [Fetch order information response](#fetch-order-information)

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/spot/active_orders?pair=btc_jpy" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/spot/active_orders?pair=btc_jpy"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "orders": [
      {
        "order_id": 0,
        "pair": "string",
        "side": "string",
        "position_side": "string",
        "type": "string",
        "start_amount": "string",
        "remaining_amount": "string",
        "executed_amount": "string",
        "price": "string",
        "post_only": false,
        "user_cancelable": true,
        "average_price": "string",
        "ordered_at": 0,
        "expire_at": 0,
        "triggered_at": 0,
        "trigger_price": "string",
        "status": "string"
      }
    ]
  }
}
```

### Margin

#### Fetch Margin Trading Status

```txt
GET /user/margin/status
```

**Parameters:**
None

**Response:**

Name | Type | Description
---- | ---- | -----------
status | string | account status: `NORMAL` (normal), `LOSSCUT` (forced liquidation is ongoing), `CALL` (margin call), `DEBT` (payables occurred), `SETTLED` (debt permanently resolved). It also returns `NORMAL` if you have not applied to a margin trade yet.
total_margin_balance_percentage | string \| null | Margin balance percentage. Truncated to two decimal places. Returns `null` if there are no positions.
total_margin_balance | string | Total margin balance. Truncated to four decimal places.
margin_position_profit_loss | string | Unrealized profit and loss. Rounded towards -∞ to four decimal places.
unrealized_cost | string | Unrealized cost. Rounded towards +∞ to four decimal places.
total_margin_position_product | string | Total position size. Truncated to four decimal places.
open_margin_position_product | string | Open position size. Truncated to four decimal places.
open_margin_order_product | string | Open order size. Truncated to four decimal places.
total_position_maintenance_margin | string | Maintenance margin required for all positions. Rounded up to four decimal places.
total_long_position_maintenance_margin | string | Maintenance margin required for long positions. Rounded up to four decimal places.
total_short_position_maintenance_margin | string | Maintenance margin required for short positions. Rounded up to four decimal places.
total_open_order_maintenance_margin | string | Maintenance margin required for all open orders. Rounded up to four decimal places.
total_long_open_order_maintenance_margin | string | Maintenance margin required for long open orders. Rounded up to four decimal places.
total_short_open_order_maintenance_margin | string | Maintenance margin required for short open orders. Rounded up to four decimal places.
margin_call_percentage | string \| null | Margin call threshold in percentage. Rounded up to zero decimal places. Returns `null` if there are no positions.
losscut_percentage | string \| null | Forced liquidation threshold in percentage. Rounded up to zero decimal places. Returns `null` if there are no positions.
buy_credit | string | available credit for buying
sell_credit | string | available credit for selling
available_balances | {pair: string, long: string, short: string}[] | available balances for opening new positions

Each item in `available_balances` has the following structure:

Name | Type | Description
---- | ---- | -----------
pair | string | margin pair name
long | string | Available balance for opening long positions. Truncated to four decimal places.
short | string | Available balance for opening short positions. Truncated to four decimal places.

**Sample Code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/margin/status" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/margin/status"
```

</p>
</details>

**Response format:**

```json
{
  "success": 1,
  "data": {
    "status": "NORMAL",
    "total_margin_balance_percentage": null,
    "total_margin_balance": "0.0000",
    "margin_position_profit_loss": "0.0000",
    "unrealized_cost": "0.0000",
    "total_margin_position_product": "0.0000",
    "open_margin_position_product": "0.0000",
    "open_margin_order_product": "0.0000",
    "total_position_maintenance_margin": "0.0000",
    "total_long_position_maintenance_margin": "0.0000",
    "total_short_position_maintenance_margin": "0.0000",
    "total_open_order_maintenance_margin": "0.0000",
    "total_long_open_order_maintenance_margin": "0.0000",
    "total_short_open_order_maintenance_margin": "0.0000",
    "margin_call_percentage": null,
    "losscut_percentage": null,
    "buy_credit": "0",
    "sell_credit": "0",
    "available_balances": [
      {
        "pair": "btc_jpy",
        "long": "0.0000",
        "short": "0.0000"
      },
    ]
  }
}
```

#### Fetch positions information

```txt
GET /user/margin/positions
```

**Parameters:**
None

**Response:**

Name | Type | Description
------------ | ------------ | ------------
notice | { what: string \| null, occurred_at: number \| null, amount: string \| null, due_date_at: number \| null } | information regarding `margin_call` or `debt` or `settled`
payables | { amount: string } | payables amount
positions | [{ pair: string, position_side: string, open_amount: string, product: string, average_price: string, unrealized_fee_amount: string, unrealized_interest_amount: string }] | information of positions
losscut_threshold | { individual: string, company: string } | losscut threshold

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/margin/positions" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/margin/positions"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "notice": {
      "what": "string",
      "occurred_at": 0,
      "amount": "0",
      "due_date_at": 0
    },
    "payables": {
      "amount": "0"
    },
    "positions": [
      {
        "pair": "string",
        "position_side": "string",
        "open_amount": "0",
        "product": "0",
        "average_price": "0",
        "unrealized_fee_amount": "0",
        "unrealized_interest_amount": "0"
      }
    ],
    "losscut_threshold": {
      "individual": "0",
      "company": "0"
    }
  }
}
```


### Trade

#### Fetch trade history

```txt
GET /user/spot/trade_history
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
pair | string | NO | pair enum: [pair list](pairs.md). when specifying an order id, pair must also be specified
count | number | NO | take limit (up to 1000)
order_id | number | NO | order id
since | number | NO | since unix timestamp
end | number | NO | end unix timestamp
order | string | NO | histories in order(order enum: `asc` or `desc`, default to `desc`)

**Response:**

Name | Type | Description
------------ | ------------ | ------------
trade_id | number | trade id
pair | string | pair enum: [pair list](pairs.md)
order_id | number | order id
side | string | `buy` or `sell`
position_side | string \| undefined | `long` or `short`(only for margin trading)
type | string | one of `limit`, `market`, `stop`, `stop_limit`, `take_profit`, `stop_loss`, `losscut`
amount | string | amount
price | string | order price
maker_taker | string | maker or taker
fee_amount_base | string | base asset fee amount
fee_amount_quote | string | quote asset fee amount
fee_occurred_amount_quote | string | quote fee occurred amount which taken later. In case of spot trading, this value is same as fee_amount_quote.
profit_loss | string \| undefined | realized profit and loss
interest | string \| undefined | interest
executed_at | number | order executed at unix timestamp (milliseconds)

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/spot/trade_history?pair=btc_jpy" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/spot/trade_history?pair=btc_jpy"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "trades": [
      {
        "trade_id": 0,
        "pair": "string",
        "order_id": 0,
        "side": "string",
        "position_side": "string",
        "type": "string",
        "amount": "string",
        "price": "string",
        "maker_taker": "string",
        "fee_amount_base": "string",
        "fee_amount_quote": "string",
        "profit_loss": "string",
        "interest": "string",
        "executed_at": 0
      }
    ]
  }
}
```

### Deposit

#### Fetch deposit history

```txt
GET /user/deposit_history
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
asset | string | NO | enum: [asset list](assets.md)
count | number | NO | take limit (up to 100)
since | number | NO | since unix timestamp
end | number | NO | end unix timestamp

**Response:**

Name | Type | Description
------------ | ------------ | ------------
uuid | string | uuid for each deposit
address | string | deposit address
asset | string | enum: [asset list](assets.md)
network | string | enum: [network list](networks.md)
amount | number | deposit amount
txid | string \| null | deposit transaction id (only for crypto assets)
status | string | deposit status enum: `FOUND`, `CONFIRMED`, `DONE`
found_at | number | found at unix timestamp (milliseconds)
confirmed_at | number | confirmed (about to be added to your balance) at unix timestamp (milliseconds, exists only for confirmed one)

**Caveat:**

* If you do not specify the asset parameter, the deposit history for all crypto assets will be returned.
* To retrieve the history in JPY, set the `asset` parameter to `jpy`.
* The deposit history response currently does not contain destination tag, memo and bank account. Use txid for matching asset flows with other systems.

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/deposit_history" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/deposit_history"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "deposits": [
      {
        "uuid": "string",
        "asset": "string",
        "network": "string",
        "amount": "string",
        "txid": "string",
        "status": "string",
        "found_at": 0,
        "confirmed_at": 0
      }
    ]
  }
}
```

#### Fetch unconfirmed deposits

```txt
GET /user/unconfirmed_deposits
```

**Parameters:**
None

**Response:**

Name | Type | Description
------------ | ------------ | ------------
uuid | string | deposit uuid
asset | string | enum: [asset list](assets.md)
amount | string | deposit amount
network | string | enum: [network list](networks.md)
txid | string | deposit transaction id
created_at | number| created at unix timestamp (milliseconds)

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/unconfirmed_deposits" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/unconfirmed_deposits"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "deposits": [
      {
        "uuid": "string",
        "asset": "string",
        "amount": "string",
        "network": "string",
        "txid": "string",
        "created_at": 0
      }
    ]
  }
}
```

#### Fetch deposit originators

```txt
GET /user/deposit_originators
```

**Parameters:**
None

**Response:**

Name | Type | Description
------------ | ------------ | ------------
uuid | string | originator uuid
label | string | originator label
deposit_type | string | deposit type enum: `WALLET`, `ELSE`
deposit_purpose | string \| null | deposit purpose
originator_status | string | originator status enum: `SCREENING`, `CONFIRMED`, `REJECTED`, `DEPRECATED`
originator_type | string | originator type enum: `OWN`, `PERSON`, `COMPANY`
originator_last_name | string \| null | originator last name
originator_first_name | string \| null | originator first name
originator_country | string \| null | originator country
originator_prefecture | string \| null | originator prefecture/state/province/region
originator_city | string \| null | originator city
originator_address | string \| null | originator address
originator_building | string \| null | originator building
originator_company_name | string \| null | originator company name
originator_company_type | string \| null | originator company type
originator_company_type_position \| null | string | originator company type position
uuid | string | originator substantial controller uuid
name | string | originator substantial controller name
country | string | originator substantial controller country
prefecture | string \| null | originator substantial controller prefecture

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/deposit_originators" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/deposit_originators"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "originators": [
      {
        "uuid": "string",
        "label": "string",
        "deposit_type": "string",
        "deposit_purpose": "string",
        "originator_status": "string",
        "originator_type": "string",
        "originator_last_name": null,
        "originator_first_name": null,
        "originator_country": "string",
        "originator_prefecture": "string",
        "originator_city": "string",
        "originator_address": "string",
        "originator_building": null,
        "originator_company_name": "string",
        "originator_company_type": "string",
        "originator_company_type_position": "string",
        "originator_substantial_controllers": [
            {
                "uuid": "string",
                "name": "string",
                "country": "string",
                "prefecture": null
            }
        ]
      }
    ]
  }
}
```

#### Confirm deposits

```txt
POST /user/confirm_deposits
```

**Parameters (requestBody):**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
deposits | object[] | YES | Array of unconfirmed deposit uuid and originator uuid objects. Details of the content are below.

**detail of deposits**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
uuid | string | YES | unconfirmed deposit uuid
originator_uuid | string | YES | originator uuid

**Request format:**

```json
{
  "deposits": [
    {
      "uuid": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "originator_uuid": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    {
      "uuid": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
      "originator_uuid": "xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    },
    {
      …
    }
  ]
}
```

**Response:**
None

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export REQUEST_BODY='{"deposits": [{ "uuid": "___deposit uuid___", "originator_uuid": "___originator uuid___" }]}'
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE$REQUEST_BODY" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" -H "Content-Type: application/json" -d "$REQUEST_BODY" "https://api.bitbank.cc/v1/user/confirm_deposits"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {}
}
```

#### Confirm all deposits

```txt
POST /user/confirm_deposits_all
```

**Parameters (requestBody):**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
originator_uuid | string | YES | originator uuid

**Response:**
None

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export REQUEST_BODY='{"originator_uuid": "___originator uuid___"}'
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE$REQUEST_BODY" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" -H "Content-Type: application/json" -d "$REQUEST_BODY" "https://api.bitbank.cc/v1/user/confirm_deposits_all"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {}
}
```

### Withdrawal

#### Get withdrawal accounts

```txt
GET /user/withdrawal_account
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
asset | string | YES | asset enum: [asset list](assets.md)

**Response:**

Name | Type | Description
------------ | ------------ | ------------
uuid | string | withdrawal account uuid
label | string | withdrawal account label
network | string | network: [networks](networks.md)
address | string | withdrawal address

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/withdrawal_account?asset=btc" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/withdrawal_account?asset=btc"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "accounts": [
      {
        "uuid": "string",
        "label": "string",
        "network": "string",
        "address": "string"
      }
    ]
  }
}
```
#### New withdrawal request

```txt
POST /user/request_withdrawal
```

**Parameters (requestBody):**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
asset | string | YES | enum: [asset list](assets.md)
uuid | string | YES | withdrawal account's uuid
amount | string | YES | withdrawal amount
otp_token | string | NO | provide if MFA is set up
sms_token | string | NO | provide if MFA is set up

**Response:**

Name | Type | Description
------------ | ------------ | ------------
uuid | string | uuid for each withdrawal
asset | string | enum: [asset list](assets.md)
account_uuid | string | account uuid
amount | string | withdrawal amount
fee | string | withdrawal fee
label | string | withdrawal account label (only for crypto assets)
address | string | withdrawal destination address (only for crypto assets)
network | string | enum (only for crypto assets): [network list](networks.md)
destination_tag | number or string | withdrawal destination tag or memo (only for crypto that have it)
txid | string \| null | withdrawal transaction id (only for crypto assets)
bank_name | string | bank of withdrawal account (only for fiat assets)
branch_name | string | bank branch of withdrawal account (only for fiat assets)
account_type | string | type of withdrawal account (only for fiat assets)
account_number | string | withdrawal account number (only for fiat assets)
account_owner | string | owner of withdrawal account (only for fiat assets)
status | string | withdrawal status enum: `CONFIRMING`, `EXAMINING`, `SENDING`,  `DONE`, `REJECTED`, `CANCELED`, `CONFIRM_TIMEOUT`
requested_at | number | requested at unix timestamp (milliseconds)

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export REQUEST_BODY='{"asset": "xrp", "uuid": "___your uuid___", "amount": "1"}'
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE$REQUEST_BODY" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" -H "Content-Type: application/json" -d "$REQUEST_BODY" "https://api.bitbank.cc/v1/user/request_withdrawal"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "uuid": "string",
    "asset": "string",
    "account_uuid": "string",
    "amount": "string",
    "fee": "string",

    "label": "string",
    "address": "string",
    "network": "string",
    "txid": "string",
    "destination_tag": 0,

    "bank_name": "string",
    "branch_name": "string",
    "account_type": "string",
    "account_number": "string",
    "account_owner": "string",

    "status": "string",
    "requested_at": 0
  }
}
```
#### Fetch withdrawal history

```txt
GET /user/withdrawal_history
```

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
asset | string | NO | enum: [asset list](assets.md)
count | number | NO | take limit (up to 100)
since | number | NO | since unix timestamp
end | number | NO | end unix timestamp

**Response:**

Name | Type | Description
------------ | ------------ | ------------
uuid | string | uuid for each withdrawal
asset | string | enum: [asset list](assets.md)
account_uuid | string | account uuid
amount | string | withdrawal amount
fee | string | withdrawal fee
label | string | withdrawal account label (only for crypto assets)
address | string | withdrawal destination address (only for crypto assets)
network | string | enum (only for crypto assets): [network list](networks.md)
destination_tag | number or string | withdrawal destination tag or memo (only for crypto that have it)
txid | string \| null | withdrawal transaction id (only for crypto assets)
bank_name | string | bank of withdrawal account (only for fiat assets)
branch_name | string | bank branch of withdrawal account (only for fiat assets)
account_type | string | type of withdrawal account (only for fiat assets)
account_number | string | withdrawal account number (only for fiat assets)
account_owner | string | owner of withdrawal account (only for fiat assets)
status | string | withdrawal status enum: `CONFIRMING`, `EXAMINING`, `SENDING`,  `DONE`, `REJECTED`, `CANCELED`, `CONFIRM_TIMEOUT`
requested_at | number | requested at unix timestamp (milliseconds)

**Caveat:**

* If you do not specify the asset parameter, the withdrawal history for all crypto assets will be returned.
* To retrieve the history in JPY, set the `asset` parameter to `jpy`.

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/withdrawal_history" | openssl dgst -sha256 -hmac "$API_SECRET")"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/withdrawal_history"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "withdrawals": [
      {
        "uuid": "string",
        "asset": "string",
        "account_uuid": "string",
        "amount": "string",
        "fee": "string",

        "label": "string",
        "address": "string",
        "network": "string",
        "txid": "string",
        "destination_tag": 0,

        "bank_name": "string",
        "branch_name": "string",
        "account_type": "string",
        "account_number": "string",
        "account_owner": "string",

        "status": "string",
        "requested_at": 0
      }
    ]
  }
}
```

### Status

#### Get exchange status

*Not require authentication.*

```txt
GET /spot/status
```

**Parameters:**
None

**Response:**

Name | Type | Description
------------ | ------------ | ------------
pair | string | pair enum: [pair list](pairs.md)
status | string | enum: `NORMAL`, `BUSY`, `VERY_BUSY`, `HALT`
min_amount| string | minimum order amount (The busier the exchange is, the higher the min_amount will be)

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
curl "https://api.bitbank.cc/v1/spot/status"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "statuses": [
      {
        "pair": "string",
        "status": "string",
        "min_amount": "string"
      }
    ]
  }
}
```

### Settings

#### Get all pairs info

*Not require authentication.*

```txt
GET /spot/pairs
```

**Parameters:**
None

**Response:**

Name | Type | Description
------------ | ------------ | ------------
name | string | pair enum: [pair list](pairs.md)
base_asset | string | base asset
quote_asset | string | quote asset
maker_fee_rate_base | string | maker fee (base asset)
taker_fee_rate_base | string | taker fee (base asset)
maker_fee_rate_quote | string | maker fee (quote asset)
taker_fee_rate_quote | string | taker fee (quote asset)
margin_open_maker_fee_rate_quote | string \| null | open maker fee (quote asset)
margin_open_taker_fee_rate_quote | string \| null | open taker fee (quote asset)
margin_close_maker_fee_rate_quote | string \| null | close maker fee (quote asset)
margin_close_taker_fee_rate_quote | string \| null | close taker fee (quote asset)
margin_long_interest | string \| null | long position interest/day
margin_short_interest | string \| null | short position interest/day
margin_current_individual_ratio | string \| null | current individual risk assumption ratio
margin_current_individual_until | number \| null | current application end date and time of individual risk assumption ratio(unix timestamp milliseconds)
margin_current_company_ratio | string \| null | current company risk assumption ratio
margin_current_company_until | number \| null | current application end date and time of company risk assumption ratio(unix timestamp milliseconds)
margin_next_individual_ratio | string \| null | next individual risk assumption ratio
margin_next_individual_until | number \| null | next application end date and time of individual risk assumption ratio(unix timestamp milliseconds)
margin_next_company_ratio | string \| null | next company risk assumption ratio
margin_next_company_until | number \| null | curnextrent application end date and time of company risk assumption ratio(unix timestamp milliseconds)
unit_amount | string | minimum order amount
limit_max_amount | string | max order amount
market_max_amount | string | market order max amount
market_allowance_rate | string | market order allowance rate
price_digits | number | price digits count
amount_digits | number | amount digits count
is_enabled | boolean | pair enable flag
stop_order | boolean | order suspended flag
stop_order_and_cancel | boolean | order and cancel suspended flag
stop_market_order | boolean | "market order" suspended flag
stop_stop_order | boolean | "stop (market) order" suspended flag
stop_stop_limit_order | boolean | "stop limit order" suspended flag
stop_margin_long_order | boolean | open long positions suspended flag
stop_margin_short_order | boolean | open short positions suspended flag
stop_buy_order | boolean | "buy order" suspended flag
stop_sell_order | boolean | "sell order" suspended flag

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
curl "https://api.bitbank.cc/v1/spot/pairs"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "pairs": [
      {
        "name": "string",
        "base_asset": "string",
        "maker_fee_rate_base": "string",
        "taker_fee_rate_base": "string",
        "maker_fee_rate_quote": "string",
        "taker_fee_rate_quote": "string",
        "margin_open_maker_fee_rate_quote": "string",
        "margin_open_taker_fee_rate_quote": "string",
        "margin_close_maker_fee_rate_quote": "string",
        "margin_close_taker_fee_rate_quote": "string",
        "margin_long_interest": "string",
        "margin_short_interest": "string",
        "margin_current_individual_ratio": "string",
        "margin_current_individual_until": 0,
        "margin_current_company_ratio": "string",
        "margin_current_company_until": 0,
        "margin_next_individual_ratio": "string",
        "margin_next_individual_until": 0,
        "margin_next_company_ratio": "string",
        "margin_next_company_until": 0,
        "unit_amount": "string",
        "limit_max_amount": "string",
        "market_max_amount": "string",
        "market_allowance_rate": "string",
        "price_digits": 0,
        "amount_digits": 0,
        "is_enabled": true,
        "stop_order": false,
        "stop_order_and_cancel": false,
        "stop_market_order": false,
        "stop_stop_order": false,
        "stop_stop_limit_order": false,
        "stop_margin_long_order": false,
        "stop_margin_short_order": false,
        "stop_buy_order": false,
        "stop_sell_order": false
      }
    ]
  }
}
```

### Private stream

#### Get channel and token for private stream

Get channel and token for private stream.
Please refer to [the page of private stream](private-stream.md) for more details.

pubnub_channel is assigned a unique channel for each user.
pubnub_token has TTL(time to live) of 12 hours.
When the pubnub_token expires, the connection to PubNub will be disconnected. Please call this API again to obtain a new pubnub_token.

```txt
GET /user/subscribe
```

**Parameters:**
None

**Response:**

Name | Type | Description
------------ | ------------ | ------------
pubnub_channel | string | channel name
pubnub_token | string | token

**Sample code:**

<details>
<summary>Curl</summary>
<p>

```sh
export API_KEY=___your api key___
export API_SECRET=___your api secret___
export ACCESS_NONCE="$(date +%s)000"
export ACCESS_SIGNATURE="$(echo -n "$ACCESS_NONCE/v1/user/subscribe" | openssl dgst -sha256 -hmac "$API_SECRET" | awk '{print $NF}')"

curl -H "ACCESS-KEY: $API_KEY" -H "ACCESS-NONCE: $ACCESS_NONCE" -H "ACCESS-SIGNATURE: $ACCESS_SIGNATURE" "https://api.bitbank.cc/v1/user/subscribe"
```

</p>
</details>


**Response format:**

```json
{
  "success": 1,
  "data": {
    "pubnub_channel": "string",
    "pubnub_token": "string"
  }
}
```
[日本語](public-stream_JP.md)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Web Socket Streams for Bitbank](#web-socket-streams-for-bitbank)
  - [General WSS information](#general-wss-information)
  - [General endpoints](#general-endpoints)
    - [Ticker](#ticker)
    - [Transactions](#transactions)
    - [Depth Diff](#depth-diff)
    - [Depth Whole](#depth-whole)
      - [In circuit_break_info.mode is `NONE` or estimated price is null](#in-circuit_break_infomode-is-none-or-estimated-price-is-null)
      - [In circuit_break_info.mode is not `NONE` and estimated price is not null](#in-circuit_break_infomode-is-not-none-and-estimated-price-is-not-null)
    - [Circuit Break Info](#circuit-break-info)
  - [How to manage a local order book correctly](#how-to-manage-a-local-order-book-correctly)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Web Socket Streams for Bitbank

## General WSS information

- The base endpoint is: **wss://stream.bitbank.cc**.
- [socket.io 4.x](https://socket.io/docs/v4/) (Engine.io protocol v4) is used under the hood, and the following code examples are demonstrated with [github.com/websockets/wscat](https://github.com/websockets/wscat)
- From 2022-07-26, [socket.io](https://socket.io/) is upgraded from [2.x](https://socket.io/docs/v2/) to [4.x](https://socket.io/docs/v4/)
- The specification of disconnection after 6 hours is abolished. Continuously, if an error occurs the connection will be closed. Please check the error messages.

## General endpoints

### Ticker

Ticker channel name is `ticker_{pair}`, available pairs are written in [pair list](pairs.md).

Except for continuous trading mode, it may be the case that sell <= buy.

**Response:**

Name | Type | Description
------------ | ------------ | ------------
sell | string | the lowest price of sell orders
buy | string | the highest price of buy orders
high | string | the highest price in last 24 hours
low | string | the lowest price in last 24 hours
open | string | the open price at 24 hours ago
last | string | the latest price executed
vol | string | trading volume in last 24 hours
timestamp | number | ticked at unix timestamp (milliseconds)

**Sample code:**

<details>
<summary>wscat</summary>
<p>

```sh
$ wscat -c 'wss://stream.bitbank.cc/socket.io/?EIO=4&transport=websocket'

connected (press CTRL+C to quit)
< 0{"sid":"bDAf6vgk5xPau87WAA1u","upgrades":[],"pingInterval":25000,"pingTimeout":60000}
> 40
< 40{"sid":"lUkRb31kqoS9cLPNMc0W"}
> 42["join-room","ticker_btc_jpy"]
< 42["message",{"room_name":"ticker_btc_jpy","message":{"pid":851203833,"data":{"sell":"896490","buy":"896489","open":"896489","high":"905002","low":"881500","last":"896489","vol":"650.2026","timestamp":1570080042822}}}]
< 42["message",{"room_name":"ticker_btc_jpy","message":{"pid":851203952,"data":{"sell":"896490","buy":"896489","open":"896489","high":"905002","low":"881500","last":"896489","vol":"650.2226","timestamp":1570080053768}}}]
...

```

</p>
</details>

**Response format:**

```json
[
    "message",
    {
        "room_name": "ticker_btc_jpy",
        "message": {
            "pid": 0,
            "data": {
                "last": "string",
                "open": "string",
                "timestamp": 0,
                "sell": "string",
                "vol": "string",
                "buy": "string",
                "high": "string",
                "low": "string"
            }
        }
    }
]
```

### Transactions

Transactions channel name is `transactions_{pair}`, available pairs are written in [pair list](pairs.md).

**Response:**

Name | Type | Description
------------ | ------------ | ------------
transaction_id | number | transaction id
side | string | enum: `buy`, `sell`
price | string | price
amount | string | amount
executed_at | number | executed at unix timestamp (milliseconds)

**Sample code:**

<details>
<summary>wscat</summary>
<p>

```sh
$ wscat -c 'wss://stream.bitbank.cc/socket.io/?EIO=4&transport=websocket'

connected (press CTRL+C to quit)
< 0{"sid":"PG3FbI0WrKIP7hKMABH_","upgrades":[],"pingInterval":25000,"pingTimeout":60000}
> 40
< 40{"sid":"lUkRb31kqoS9cLPNMc0W"}
> 42["join-room","transactions_xrp_jpy"]
< 42["message",{"room_name":"transactions_xrp_jpy","message":{"pid":851205254,"data":{"transactions":[{"transaction_id":34745047,"side":"sell","price":"26.930","amount":"4703.5671","executed_at":1570080162855},{"transaction_id":34745046,"side":"sell","price":"26.930","amount":"500.0000","executed_at":1570080162829},{"transaction_id":34745045,"side":"sell","price":"26.930","amount":"378.0000","executed_at":1570080162802},{"transaction_id":34745044,"side":"sell","price":"26.930","amount":"12.0000","executed_at":1570080162758},{"transaction_id":34745043,"side":"sell","price":"26.930","amount":"301.4874","executed_at":1570080162725}]}}}]
...

```

</p>
</details>

**Response format:**

```json
[
    "message",
    {
        "room_name": "transactions_btc_jpy",
        "message": {
            "pid": 0,
            "data": {
                "transactions": [
                    {
                        "side": "string",
                        "executed_at": 0,
                        "amount": "string",
                        "price": "string",
                        "transaction_id": 0
                    }
                ]
            }
        }
    }
]
```

### Depth Diff

Depth Diff channel name is `depth_diff_{pair}`, available pairs are written in [pair list](pairs.md).

Except for continuous trading mode, it may be the case that a <= b.

**Response:**

Name | Type | Description
------------ | ------------ | ------------
a | [string, string][] | [ask, amount][]
b | [string, string][] | [bid, amount][]
ao | string \| undefined | optional. The quantity of asks over the highest price of [asks orders](#Depth-Whole). If there is no change in quantity, it will not be included in the message.
bu | string \| undefined | optional. The quantity of bids under the lowest price of [bids orders](#Depth-Whole). If there is no change in quantity, it will not be included in the message.
au | string \| undefined | optional. The quantity of asks under the lowest price of [bids orders](#Depth-Whole) orders. If there is no change in quantity, it will not be included in the message.
bo | string \| undefined | optional. The quantity of bids over the highest price of [asks orders](#Depth-Whole). If there is no change in quantity, it will not be included in the message.
am | string \| undefined | optional. The quantity of market sell orders. If there is no change in quantity, it will not be included in the message.
bm | string \| undefined | optional. The quantity of market buy orders. If there is no change in quantity, it will not be included in the message.
t | number | published at unix timestamp (milliseconds)
s | string | sequence id, increased monotonically but not always consecutive

The amount of `a` (asks) and `b` (bids) is absolute, and its 0 means its price level has gone.

The `s` (sequence id) is common with the `sequenceId` of `depth_whole_{pair}`.

For usage, see [How to manage a local order book correctly](#how-to-manage-a-local-order-book-correctly) section.

<a name="depth-diff-sample-code"></a>**Sample code:**

<details>
<summary>wscat</summary>
<p>

```sh
$ wscat -c 'wss://stream.bitbank.cc/socket.io/?EIO=4&transport=websocket'
connected (press CTRL+C to quit)
< 0{"sid":"9-zd3P1G-BNu_w37ABMX","upgrades":[],"pingInterval":25000,"pingTimeout":60000}
> 40
< 40{"sid":"lUkRb31kqoS9cLPNMc0W"}
> 42["join-room","depth_diff_xrp_jpy"]
< 42["message",{"room_name":"depth_diff_xrp_jpy","message":{"data":{"a":[],"b":[["26.758","20000.0000"],["26.212","0"]],"t":1570080269609,"s":"1234567890"}}}]
< 42["message",{"room_name":"depth_diff_xrp_jpy","message":{"data":{"a":[],"b":[["26.212","1000.0000"],["26.815","0"]],"t":1570080270100,"s":"1234567893"}}}]
...

```

</p>
</details>

**Response format:**

```json
[
    "message",
    {
        "room_name": "depth_diff_xrp_jpy",
        "message": {
            "data": {
                "b": [
                    [
                        "26.872",
                        "43.3989"
                    ],
                    [
                        "26.871",
                        "100.0000"
                    ],
                ],
                "a": [
                    [
                        "27.839",
                        "1634.3980"
                    ],
                    [
                        "28.450",
                        "0"
                    ]
                ],
                "ao": "1",
                "bu": "1",
                "am": "1",
                "bm": "1",
                "t": 1568344204624,
                "s": "1234567890"
            }
        }
    }
]
```

### Depth Whole

Whole depth channel name is `depth_whole_{pair}`, available pairs are written in [pair list](pairs.md).

Except for continuous trading mode, it may be the case that asks <= bids.

#### In circuit_break_info.mode is `NONE` or estimated price is null

- Asks and bids data is restricted to 200 entries each from best bid offer.
- Asks and bids price never cross.

#### In circuit_break_info.mode is not `NONE` and estimated price is not null

- Asks and bids data is restricted to 200 entries each around the estimated price. (Max 400 entries)
- Asks and bids price possibly cross.
- asks_under, bids_over possibly includes the quantity of orders which price is out of range.

**Response:**

Name | Type | Description
------------ | ------------ | ------------
asks | [string, string][] | array of [price, amount]
bids | [string, string][] | array of [price, amount]
asks_over | string | the quantity of asks over the highest price of asks orders.
bids_under | string | the quantity of bids under the lowest price of bids orders.
asks_under | string | the quantity of asks under the lowest price of asks orders. Usually "0" in `NORMAL` mode.
bids_over | string | the quantity of bids over the highest price of bids orders. Usually "0" in `NORMAL` mode.
ask_market | string | the quantity of market sell orders. Usually "0" in `NORMAL` mode.
bid_market | string | the quantity of market buy orders. Usually "0" in `NORMAL` mode.
timestamp | number | published at timestamp
sequenceId | number | sequence id, increased monotonically but not always consecutive

The `sequenceId` is common with the `s` of `depth_diff_{pair}`.

For usage, see [How to manage a local order book correctly](#how-to-manage-a-local-order-book-correctly) section.

<a name="depth-whole-sample-code"></a>**Sample code:**

<details>
<summary>wscat</summary>
<p>

```sh
$ wscat -c 'wss://stream.bitbank.cc/socket.io/?EIO=4&transport=websocket'
connected (press CTRL+C to quit)
< 0{"sid":"PR6GLrwlEFjzHIPrABBM","upgrades":[],"pingInterval":25000,"pingTimeout":60000}
> 40
< 40{"sid":"lUkRb31kqoS9cLPNMc0W"}
> 42["join-room","depth_whole_xrp_jpy"]
< 42["message",{"room_name":"depth_whole_xrp_jpy","message":{"data":{"asks":[["26.928","1000.0000"],["26.929","56586.5153"],["26.930","218.3431"],["26.931","3123.8845"],["26.933","1799.0000"],["26.934","377.9136"],["26.938","3411.1507"],["26.950","80.0000"],["26.955","80.0000"],["26.958","7434.5900"],["26.959","15000.0000"],["26.960","15000.0000"],["26.964","10837.6620"],["26.979","15000.0000"], ...]}}}]

```

</p>
</details>

**Response format:**

```json
[
    "message",
    {
        "room_name": "depth_whole_xrp_jpy",
        "message": {
            "data": {
                "bids": [
                    [
                        "27.537",
                        "6211.6210"
                    ],
                    [
                        "27.523",
                        "875.3413"
                    ],
                ],
                "asks": [
                    [
                        "27.538",
                        "7233.6837"
                    ],
                    [
                        "27.540",
                        "19.4551"
                    ],
                ],
                "asks_over": "0.123",
                "bids_under": "0.123",
                "asks_under": "0",
                "bids_over": "0",
                "ask_market": "0",
                "bid_market": "0",
                "timestamp": 1568344476514,
                "sequenceId": "1234567890"
            }
        }
    }
]
```

### Circuit Break Info

Get circuit break informations.

**Response:**

Name | Type | Description
------------ | ------------ | ------------
mode | string | enum: `NONE`, `CIRCUIT_BREAK`, `FULL_RANGE_CIRCUIT_BREAK`, `RESUMPTION`, `LISTING`
estimated_itayose_price | string \| null | estimated price. Null if mode is `NONE` or when there is no estimated price.
estimated_itayose_amount | string \| null | estimated amount. Null if mode is `NONE`.
itayose_upper_price | string \| null | itayose price range upper limit. Null if mode is in `NONE`, `FULL_RANGE_CIRCUIT_BREAK` or `LISTING`.
itayose_lower_price | string \| null | itayose price range lower limit. Null if mode is in `NONE`, `FULL_RANGE_CIRCUIT_BREAK` or `LISTING`.
upper_trigger_price | string \| null | upper trigger price. Null if mode is not `NONE`.
lower_trigger_price | string \| null | lower trigger price. Null if mode is not `NONE`.
fee_type | string | enum: `NORMAL`, `SELL_MAKER`, `BUY_MAKER`, `DYNAMIC`
reopen_timestamp | number \| null | reopen timestamp(milliseconds). Null if mode is `NONE`, or reopen timestamp is undetermined yet.
timestamp | number | ticked at unix timestamp (milliseconds)

For details on `mode` and `fee_type`, please check the [Circuit breaker system](https://bitbank.cc/docs/circuit-breaker-mode/) page.

**Sample code:**

<details>
<summary>wscat</summary>
<p>

```sh
$ wscat -c 'wss://stream.bitbank.cc/socket.io/?EIO=4&transport=websocket'

connected (press CTRL+C to quit)
< 0{"sid":"PG3FbI0WrKIP7hKMABH_","upgrades":[],"pingInterval":25000,"pingTimeout":60000}
> 40
< 40{"sid":"lUkRb31kqoS9cLPNMc0W"}
> 42["join-room","circuit_break_info_xrp_jpy"]
< 42["message",{"room_name":"circuit_break_info_xrp_jpy","message":{"data":{"mode":"NONE","estimated_itayose_price":null,"estimated_itayose_amount":null,"itayose_upper_price":null,"itayose_lower_price":null,"upper_trigger_price":"1200000","lower_trigger_price":"800000","fee_type":"NORMAL","reopen_timestamp":null,"timestamp":1570080162855}}}]
< 42["message",{"room_name":"circuit_break_info_xrp_jpy","message":{"data":{"mode":"CIRCUIT_BREAK","estimated_itayose_price":"1000000","estimated_itayose_amount":null,"itayose_upper_price":"1300000","itayose_lower_price":"800000","upper_trigger_price":null,"lower_trigger_price":null,"fee_type":"SELL_MAKER","reopen_timestamp":1234573890000,"timestamp":1570080162856}}}]
...

```

</p>
</details>

**Response format:**

```json
[
    "message",
    {
        "room_name": "circuit_break_info_btc_jpy",
        "message": {
            "data": {
              "mode": "string",
              "estimated_itayose_price": "string",
              "estimated_itayose_amount": "string",
              "itayose_upper_price": "string",
              "itayose_lower_price": "string",
              "upper_trigger_price": "string",
              "lower_trigger_price": "string",
              "fee_type": "string",
              "reopen_timestamp": 0,
              "timestamp": 0
            }
        }
    }
]
```

## How to manage a local order book correctly

You can manage a local (typically on-memory) order book of a pair, by using room `depth_whole_{pair}` and `depth_diff_{pair}` as follows:

1. Subscribe both `depth_whole_{pair}` and `depth_diff_{pair}`. See [the sample code of Depth Whole](#depth-whole-sample-code) and [Depth Diff](#depth-diff-sample-code) for usage.
1. Buffer the `depth_diff_{pair}` messages you receive continuously.
1. When you receive a `depth_diff_{pair}` message,
    * If its amount is NOT zero, add or overwrite the amount of that price level to your local order book.
    * If its amount IS zero, remove that price level from your local order book.
1. When you receive a `depth_whole_{pair}` message,
    * replace your local order book by its `data`,
    * and apply buffered `depth_diff_{pair}`s,
        * that in ascending `s` order,
        * only for `s` is greater than the `sequenceId` of `depth_whole_{pair}`.

Here is an example of processing `depth_whole_{pair}`.
If you receive following messages in this order:

> diff{s=3}, diff{s=5}, diff{s=6}, diff{s=8}, whole{sequenceId=5}

you should replace the local order book by `whole{sequenceId=5}`, then apply `diff{s=6}` then `diff{s=8}` and ignore about `diff{s=3}` and `diff{s=5}`.

The sequence id never rewinds (at least on each room),
so you can forget `depth_diff_{pair}` messages that its `s` is less or equal than latest `depth_whole_{pair}`'s `sequenceId,` to reduce resource usage.

**Caveats:**

* `depth_diff_{pair}` messages are sent for only ~200 price levels from best bid/ask at that time.
  For that reason, you must refresh your local order book with each `depth_whole_{pair}` message to get the correct order book.
  (or you'll miss some price levels on price change.)
* A `depth_whole_{pair}` message sometimes be sent delayed from `depth_diff_{pair}` messages.
  For that reason, you must buffer `depth_diff_{pair}` messages and apply them on receiving a `depth_whole_{pair}` message.
[日本語](private-stream_JP.md)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Private stream for bitbank](#private-stream-for-bitbank)
  - [Introduction](#introduction)
    - [What is a private stream?](#what-is-a-private-stream)
    - [What is PubNub?](#what-is-pubnub)
  - [How to use](#how-to-use)
    - [Step 1: Get your API key](#step-1-get-your-api-key)
    - [Step 2: Get channel name and token](#step-2-get-channel-name-and-token)
    - [Step 3: Connect to PubNub](#step-3-connect-to-pubnub)
    - [Step 4: Receive order user data](#step-4-receive-order-user-data)
      - [method: asset_update](#method-asset_update)
      - [method: spot_order_new](#method-spot_order_new)
      - [method: spot_order](#method-spot_order)
      - [method: spot_order_invalidation](#method-spot_order_invalidation)
      - [method: spot_trade](#method-spot_trade)
      - [method: dealer_order_new](#method-dealer_order_new)
      - [method: withdrawal](#method-withdrawal)
      - [method: deposit](#method-deposit)
      - [method: margin_position_update](#method-margin_position_update)
      - [method: margin_payable_update](#method-margin_payable_update)
      - [method: margin_notice_update](#method-margin_notice_update)
    - [Step 5: Reconnect to PubNub](#step-5-reconnect-to-pubnub)
  - [Example code](#example-code)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Private stream for bitbank

## Introduction

### What is a private stream?

A private stream is a feature that allows you to receive real-time user data (such as order and asset change information) from the bitbank server.
This feature is useful when you want to trade using real-time user data.
User data is sent using PubNub and can be received in real-time.

### What is PubNub?

PubNub is a service that provides real-time data streaming. bitbank uses PubNub to provide users with real-time user data.

Using the PubNub SDK, you can connect to the PubNub server based on the information obtained from the API and receive user data.

## How to use

### Step 1: Get your API key

To use the private stream, please get your API key and secret from the bitbank website.

### Step 2: Get channel name and token

To connect to the private stream, you need to get the channel name and token from REST API GET /v1/user/subscribe endpoint.

Refer to ["Get channel and token for private stream"](rest-api.md#get-channel-and-token-for-private-stream) in [rest-api](rest-api.md).

### Step 3: Connect to PubNub

To connect to the private stream, you need to use the PubNub SDK. You can connect to the private stream by following the steps below:

1. Install the [PubNub SDK](https://www.pubnub.com/docs/sdks) for your language. ex. JavaScript: `npm install pubnub`
2. Create a PubNub configuration. ex. [JavaScript](https://www.pubnub.com/docs/sdks/javascript/api-reference/configuration)
3. Receive user data from the private stream. ex. [JavaScript](https://www.pubnub.com/docs/sdks/javascript/api-reference/publish-and-subscribe#subscribe)

Use `sub-c-ecebae8e-dd60-11e6-b6b1-02ee2ddab7fe` as the subscribeKey.

Refer to the [Example code](#example-code) for detailed implementation.

### Step 4: Receive order user data

Once you have connected to the private stream, you can start receiving user data. The user data is sent in JSON format and contains the following information:

#### method: asset_update

Receive information about changes in owned assets.

Name | Type | Description
------------ | ------------ | ------------
asset | string  | Asset name: [Asset list](assets.md)
amount_precision | number | Precision
free_amount | string | Available amount
locked_amount | string | Locked amount
onhand_amount | string | On-hand amount
withdrawing_amount | string | Withdrawing amount

**Response format:**

```json
{
  "message": {
    "method": "asset_update",
    "params": [
      {
        "asset": "string",
        "amountPrecision": 0,
        "freeAmount": "string",
        "lockedAmount": "string",
        "onhandAmount": "string",
        "withdrawingAmount": "string"
      }
    ]
  }
}
```

#### method: spot_order_new

Receive information about new orders.

If you are managing active orders locally, when you receive a notification with the status `FULLY_FILLED`, `CANCELED_UNFILLED`, or `CANCELED_PARTIALLY_FILLED`, it indicates that the order has been executed or canceled, so please remove it from your order information.

Name | Type | Description
------------ | ------------ | ------------
average_price | string | avg executed price
canceled_at | number | canceled at unix timestamp (milliseconds)
executed_amount | string | qty executed
executed_at | number | order executed at unix timestamp (milliseconds)
order_id | number | order ID
ordered_at | number | ordered at unix timestamp (milliseconds)
pair | string | pair enum: [pair list](pairs.md)
price | string | order price
trigger_price | string \| undefined | trigger price(present only if type = `stop`, `stop_limit`, `take_profit`, `stop_loss`)
remaining_amount | string \| null | qty not executed
position_side | string \| undefined | `long` or `short`(only for margin trading)
side | string | `buy` or `sell`
start_amount | string \| null | order qty when placed
status | string | status enum: `INACTIVE`, `UNFILLED`, `PARTIALLY_FILLED`, `FULLY_FILLED`, `CANCELED_UNFILLED`, `CANCELED_PARTIALLY_FILLED`
type | string | one of `limit`, `market`, `stop`, `stop_limit`, `take_profit`, `stop_loss`, `losscut`
expire_at | number \| null | expiration time in unix timestamp (milliseconds)
triggered_at | number \| undefined | triggered at unix timestamp (milliseconds) (present only if type = `stop`, `stop_limit`, `take_profit`, `stop_loss`)
post_only | boolean \| undefined | whether Post Only or not (present only if type = `limit`)
user_cancelable | boolean | User cancelable
is_just_triggered | boolean | Just triggered

**Response format:**

```json
{
  "message": {
    "method": "spot_order_new",
    "params": [
      {
        "average_price": "string",
        "canceled_at": 0,
        "executed_amount": "string",
        "executed_at": 0,
        "order_id": 0,
        "ordered_at": 0,
        "pair": "string",
        "price": "string",
        "trigger_price": "string",
        "remaining_amount": "string",
        "position_side": "string",
        "side": "string",
        "start_amount": "string",
        "status": "string",
        "type": "string",
        "expire_at": 0,
        "triggered_at": 0,
        "post_only": false,
        "user_cancelable": true,
        "is_just_triggered": false
      }
    ]
  }
}
```

#### method: spot_order

Receive information about order updates.

The content is the same as `spot_order_new`.

If you are managing active orders locally, when you receive a notification with the status `FULLY_FILLED`, `CANCELED_UNFILLED`, or `CANCELED_PARTIALLY_FILLED`, it indicates that the order has been executed or canceled, so please remove it from your order information.

**Response format:**

```json
{
  "message": {
    "method": "spot_order",
    "params": [
      {
        "average_price": "string",
        "canceled_at": 0,
        "executed_amount": "string",
        "executed_at": 0,
        "order_id": 0,
        "ordered_at": 0,
        "pair": "string",
        "price": "string",
        "trigger_price": "string",
        "remaining_amount": "string",
        "position_side": "string",
        "side": "string",
        "start_amount": "string",
        "status": "string",
        "type": "string",
        "expire_at": 0,
        "triggered_at": 0,
        "post_only": false,
        "user_cancelable": true,
        "is_just_triggered": false
      }
    ]
  }
}
```

#### method: spot_order_invalidation

Receive information about order invalidation.

This notification is sent when an order is invalidated due to asset shortages within our matching engine.
Therefore, this notification does not occur frequently.
Immediate cancellations of orders that typically occur are notified via `spot_order_new`, `spot_order`, or error responses from the REST API.

If you are managing active orders locally, please remove the notified order from your order information.

Name | Type | Description
------------ | ------------ | ------------
order_id | number | order ID

**Response format:**

```json
{
  "message": {
    "method": "spot_order_invalidation",
    "params": {
      "order_id": [1, 2, 3]
    }
  }
}
```

#### method: spot_trade

Receive information about trades.

Name | Type | Description
------------ | ------------ | ------------
amount | string | executed amount
executed_at | number | order executed at unix timestamp (milliseconds)
fee_amount_base | string | base asset fee amount
fee_amount_quote | string | quote asset fee amount
fee_occurred_amount_quote | string | Quote fee occurred. Collected on close orders for margin trading. For spot trading, it is collected immediately and is the same as `fee_amount_quote`.
maker_taker | string | maker or taker
order_id | number | order ID
pair | string | pair enum: [pair list](pairs.md)
price | string | order price
position_side | string \| undefined | `long` or `short`(only for margin trading)
side | string | `buy` or `sell`
trade_id | number | trade ID
type | string | one of `limit`, `market`, `stop`, `stop_limit`, `take_profit`, `stop_loss`, `losscut`
profit_loss | string \| undefined | realized profit and loss
interest | string \| undefined | interest

**Response format:**

```json
{
  "message": {
    "method": "spot_trade",
    "params": [
      {
        "amount": "string",
        "executed_at": 0,
        "fee_amount_base": "string",
        "fee_amount_quote": "string",
        "fee_occurred_amount_quote": "string",
        "maker_taker": "string",
        "order_id": 0,
        "pair": "string",
        "price": "string",
        "position_side": "string",
        "side": "string",
        "trade_id": 0,
        "type": "string",
        "profit_loss": "string",
        "interest": "string"
      }
    ]
  }
}
```

#### method: dealer_order_new

Receive information about new dealer orders.

Name | Type | Description
------------ | ------------ | ------------
order_id | string | order ID
asset | string | enum: [asset list](assets.md)
side | string | `buy` or `sell`
price | string | price
amount | string | amount
ordered_at | number | ordered at unix timestamp (milliseconds)

**Response format:**

```json
{
  "message": {
    "method": "dealer_order_new",
    "params": [
      {
        "order_id": 0,
        "asset": "string",
        "side": "string",
        "price": "string",
        "amount": "string",
        "ordered_at": 0
      }
    ]
  }
}
```

#### method: withdrawal

Receive information about withdrawals.

Name | Type | Description
------------ | ------------ | ------------
uuid | string | withdrawal ID
network | string | enum: [network list](networks.md)(only for crypto assets)
asset | string | enum: [asset list](assets.md)
account_uuid | string | account UUID
asset | string | enum: [asset list](assets.md)
fee | string | withdrawal fee
label | string | withdrawal account label (only for crypto assets)
address | string | withdrawal destination address (only for crypto assets)
txid | string \| null | withdrawal transaction id (only for crypto assets)
bank_name | string | bank of withdrawal account (only for fiat assets)
branch_name | string | bank branch of withdrawal account (only for fiat assets)
account_type | string | type of withdrawal account (only for fiat assets)
account_number | string | withdrawal account number (only for fiat assets)
account_owner | string | owner of withdrawal account (only for fiat assets)
status | string | withdrawal status enum: `CONFIRMING`, `EXAMINING`, `SENDING`,  `DONE`, `REJECTED`, `CANCELED`, `CONFIRM_TIMEOUT`
requested_at | number | requested at unix timestamp (milliseconds)

**Response format:**

```json
{
  "message": {
    "method": "withdrawal",
    "params": [
      {
        "uuid": "string",
        "asset": "string",
        "account_uuid": "string",
        "amount": "string",
        "fee": "string",
        "bank_name": "string",
        "branch_name": "string",
        "account_type": "string",
        "account_number": "string",
        "account_owner": "string",
        "status": "string",
        "requested_at": 0
      }
    ]
  }
}
```

#### method: deposit

Receive information about deposits.

Name | Type | Description
------------ | ------------ | ------------
uuid | string | deposit ID
asset | string | enum: [asset list](assets.md)
amount | number | deposit amount
network | string | enum: [network list](networks.md)(only for crypto assets)
address | string | deposit address(only for crypto assets)
txid | string \| null | deposit transaction id (only for crypto assets)
found_at | number | found at unix timestamp (milliseconds)
confirmed_at | number | confirmed (about to be added to your balance) at unix timestamp (milliseconds, exists only for confirmed one)
status | string | deposit status enum: `FOUND`, `CONFIRMED`, `DONE`

**Response format:**

```json
{
  "message": {
    "method": "deposit",
    "params": [
      {
        "uuid": "string",
        "asset": "string",
        "amount": "string",
        "network": "string",
        "address": "string",
        "txid": "string",
        "found_at": 0,
        "confirmed_at": 0,
        "status": "string"
      }
    ]
  }
}
```

#### method: margin_position_update

Receive information about margin positions.

Name | Type | Description
------------ | ------------ | ------------
pair | string | pair enum: [pair list](pairs.md)
position_side | string | `long` or `short`
average_price | string | avg executed price
open_amount | string | open amount
locked_amount | string | locked amount
product | string | average executed price x open amount
unrealized_fee_amount | string | unrealized fee amount
unrealized_interest_amount | string | unrealized interest amount

**Response format:**

```json
{
  "message": {
    "method": "margin_position_update",
    "params": [
      {
        "pair": "string",
        "position_side": "string",
        "average_price": "string",
        "open_amount": "string",
        "locked_amount": "string",
        "product": "string",
        "unrealized_fee_amount": "string",
        "unrealized_interest_amount": "string"
      }
    ]
  }
}
```

#### method: margin_payable_update

Receive information about margin payables.

Name | Type | Description
------------ | ------------ | ------------
amount | string | payable amount

**Response format:**

```json
{
  "message": {
    "method": "margin_payable_update",
    "params": [
      {
        "amount": "string"
      }
    ]
  }
}
```

#### method: margin_notice_update

Receive information about margin notices.

This is published when a margin call or insufficient funds occur, or when they are partially deposited or partially repaid.
Additionally, if these are resolved or fully settled, a message with all properties set to `null` will be published.

Name | Type | Description
------------ | ------------ | ------------
what | string \| null | what the notice is for (marginCall, debt, or settled)
occurred_at | number \| null | occurrence time
amount | string \| null | amount
due_date_at | number \| null | due date

**Response format:**

```json
{
  "message": {
    "method": "margin_notice_update",
    "params": [
      {
        "what": "string",
        "occurred_at": 0,
        "amount": "string",
        "due_date_at": 0
      }
    ]
  }
}
```

### Step 5: Reconnect to PubNub

If the connection to the private stream is lost, you can reconnect to PubNub by following the steps below:

1. Detect that the connection to PubNub has been lost from the status event.
2. Reconnect to PubNub.

Refer to the [Example code](#example-code) for detailed implementation.

## Example code

Here is an example code that shows how to connect to the private stream and receive user data:

```javascript
// npm install pubnub
const PubNub = require('pubnub');
const crypto = require('crypto');

const API_KEY = '<your_api_key>';
const API_SECRET = '<your_api_secret>';

const PUBNUB_SUB_KEY = 'sub-c-ecebae8e-dd60-11e6-b6b1-02ee2ddab7fe';

const store = new Map();
// status only changes in the direction from 0 to 3
const STATUS_STAGE = {
    INACTIVE: 0,
    UNFILLED: 1,
    PARTIALLY_FILLED: 2,
    FULLY_FILLED: 3,
    CANCELED_PARTIALLY_FILLED: 3,
    CANCELED_UNFILLED: 3,
}

const main = async () => {

    const { channel, token } = await getChannelAndToken();

    const pubnub = getPubNubAndAddListener(channel, token);

    subscribePrivateChannel(pubnub, channel, token);

    // If the status becomes 3 (inactive), remove it from the store after 1 minute
    setInterval(() => {
      const now = new Date().getTime();
      store.forEach((value, key) => {
        if (now - value.last_update_at > 60 * 1000 && STATUS_STAGE[value.status] === 3) {
          store.delete(key);
        }
      });

      console.log('store:', store);
    }, 60 * 1000);
}

const toSha256 = (key, value) =>{
  return crypto
    .createHmac('sha256', key)
    .update(Buffer.from(value))
    .digest('hex')
    .toString();
}

const getPubNubAndAddListener = (channel, token) => {
  const pubnub = new PubNub({
    subscribeKey: PUBNUB_SUB_KEY,
    userId: channel,
    ssl: true,
  });
  /**
   * Note: In some SDKs, there are separate message receiving methods on the subscription instance in addition to addListener.
   *       Using both may result in messages being delivered to only one handler.
   *       It is recommended to handle both status and message events within addListener.
   *
   * The following are not recommended:
   * JavaScript: subscription.onMessage
   * Java: subscription.setOnMessage
   * C#: subscription.OnMessage
   * Ruby: subscription.on_message
   * etc.
   */
  pubnub.addListener({
    status: async (status) => {
      switch (status.category) {
        /**
         * When pubnub channel connection established successfully.
         * This is called once after trying to start to connect.
         */
        case 'PNConnectedCategory': {
          console.info('pubnub connection established');
          break;
        }

        /**
         * When connection restored.
         */
        case 'PNNetworkUpCategory':
        case 'PNReconnectedCategory': {
          console.info('pubnub connection restored');
          // When network down, pubnub disposes subscribers so we need to re-subscribe manually.
          subscribePrivateChannel(pubnub_channel, token);
          break;
        }

        /**
         * When connection failed by timeout.
         * In this case, we need to reconnect manually.
         */
        case 'PNTimeoutCategory': {
          console.warn('pubnub connection Failed by timeout.');
          await reconnect();
          break;
        }

        /**
         * When connection failed due to network error.
         */
        case 'PNNetworkDownCategory':
        case 'PNNetworkIssuesCategory': {
          console.error('pubnub connection network error', status);
          await reconnect();
          break;
        }

        /**
         * This will be called when token is expired.
         */
        case 'PNAccessDeniedCategory': {
          console.error('pubnub access denied', status);
          await reconnect();
          break;
        }

        /**
         * This will not be called.
         * Maybe pubnub-library is not implement these events.
         */
        case 'PNBadRequestCategory':
        case 'PNMalformedResponseCategory':
        case 'PNDecryptionErrorCategory': {
          console.error('pubnub connection failed', status);
          break;
        }

        /**
         * This will not be called.
         * If this called, implement new handling for the event.
         */
        default: {
          console.warn('default');
        }
      }
    },

    // Since message order is not guaranteed, only the most up-to-date order status should remain in the store, even if order messages arrive out of sequence.
    // When an order message arrives, check the store: if it doesn't exist, add it; if it does, update only if the order status has progressed.
    message: (data) => {
      if (data && data.message) {
        console.info('message received', JSON.stringify(data.message));
      }
      if (data.message.method === 'spot_order_new' || data.message.method === 'spot_order') {
        const order = data.message.params[0];
        if (!store.has(order.order_id)) {
          store.set(order.order_id, {
            status: order.status,
            remaining_amount: order.remaining_amount,
            last_update_at: new Date().getTime(),
          });
        } else {
          const last = store.get(order.order_id);
          if (STATUS_STAGE[last.status] < STATUS_STAGE[order.status] || (STATUS_STAGE[last.status] === STATUS_STAGE[order.status] && last.remaining_amount > order.remaining_amount)) {
            store.set(order.order_id, {
              status: order.status,
              remaining_amount: order.remaining_amount,
              last_update_at: new Date().getTime(),
            });
          }
        }
      }
    },
  });

  return pubnub;
}

const getChannelAndToken = async () => {
  const nonce = new Date().getTime();
  const timeWindow = '5000';
  const message = `${nonce}${timeWindow}/v1/user/subscribe`;

  // Get channel and token from API
  const res = await fetch('https://api.bitbank.cc/v1/user/subscribe', {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'ACCESS-KEY': API_KEY,
      'ACCESS-REQUEST-TIME': nonce.toString(),
      'ACCESS-TIME-WINDOW': timeWindow,
      'ACCESS-SIGNATURE': toSha256(API_SECRET, message),
    },
  }).then((res) => res.json());

  const channel = res.data.pubnub_channel;
  const token = res.data.pubnub_token;
  return { channel, token };
}

const subscribePrivateChannel = (pubnub, channel, token) => {
  pubnub.setToken(token);
  pubnub.subscribe({
    channels: [channel],
  });
}

const reconnect = async () => {
  // Reconnect to pubnub
  const { channel, token } = await getChannelAndToken();
  const pubnub = getPubNubAndAddListener(channel, token);

  subscribePrivateChannel(pubnub, channel, token);
}

main().catch(console.error);
```<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Error codes for Bitbank](#error-codes-for-bitbank)
  - [SYSTEM_ERROR](#system_error)
  - [AUTHENTICATION_ERROR](#authentication_error)
  - [REQUIRED_PARAMETER_ERROR](#required_parameter_error)
  - [INVALID_PARAMETER_ERROR](#invalid_parameter_error)
  - [DATA_ERROR](#data_error)
  - [VALUE_ERROR](#value_error)
  - [STOP_UPDATE_REQUEST_SYSTEM_STATUS](#stop_update_request_system_status)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

[日本語](errors_JP.md)

# Error codes for Bitbank

Here is the format of error JSON payload:

```json
{
  "success": 0,
  "data": {
    "code": 20003
  }
}
```

The following is the list of Bitbank's error codes.

## SYSTEM_ERROR

- `10000` Url not found.
- `10001` System error.
- `10002` Malformed request.
- `10003` System error.
- `10005` Timeout waiting for response.
- `10007` System maintenance.
- `10008` Server is busy. Retry later.
- `10009` You sent requests too frequently. Retry later with decreased requests.

## AUTHENTICATION_ERROR

- `20001` Authentication failed api authorization.
- `20002` Invalid ACCESS-KEY.
- `20003` ACCESS-KEY not found.
- `20004` ACCESS-NONCE not found.
- `20005` Invalid ACCESS-SIGNATURE.
- `20011` MFA failed.
- `20014` SMS verification failed.
- `20018` Please login. (This happens when you request API without `/v1/`.)
- `20019` Please login. (This also happens when you request API without `/v1/`.)
- `20023` Missing OTP code.
- `20024` Missing SMS code.
- `20025` Missing OTP and SMS code.
- `20026` MFA is temporarily locked because too many failures. Please retry after 60 seconds.
- `20033` ACCESS-REQUEST-TIME not found.
- `20034` Invalid time of ACCESS-REQUEST-TIME.
- `20035` No request was sent within ACCESS-TIME-WINDOW.
- `20036` ACCESS-REQUEST-TIME and ACCESS-NONCE not found.
- `20037` Invalid ACCESS-REQUEST-TIME.
- `20038` Invalid ACCESS-TIME-WINDOW.
- `20039` Invalid ACCESS-NONCE.

## REQUIRED_PARAMETER_ERROR

- `30001` Missing order quantity.
- `30006` Missing order id.
- `30007` Missing order id array.
- `30009` Missing asset.
- `30012` Missing order price.
- `30013` Missing side.
- `30015` Missing order type.
- `30016` Missing asset.
- `30019` Missing uuid.
- `30039` Missing withdraw amount.
- `30101` Missing trigger price.
- `30103` Missing withdrawal type.
- `30104` Missing withdrawal name.
- `30105` Missing VASP.
- `30106` Missing beneficiary type.
- `30107` Missing beneficiary last name.
- `30108` Missing beneficiary first name.
- `30109` Missing beneficiary last kana.
- `30110` Missing beneficiary first kana.
- `30111` Missing beneficiary company name.
- `30112` Missing beneficiary company kana.
- `30113` Missing beneficiary company type.
- `30114` Missing beneficiary company type position.
- `30115` Missing uploaded documents.
- `30116` Missing withdrawal purpose.
- `30117` Missing beneficiary country.
- `30118` Missing beneficiary zip code.
- `30119` Missing beneficiary prefecture.
- `30120` Missing beneficiary city.
- `30121` Missing beneficiary address.
- `30122` Missing beneficiary building.
- `30123` Missing extraction request category.

## INVALID_PARAMETER_ERROR

- `40001` Invalid order quantity.
- `40006` Invalid count.
- `40007` Invalid end param.
- `40008` Invalid end_id.
- `40009` Invalid from_id.
- `40013` Invalid order id.
- `40014` Invalid order id array.
- `40015` Too many orders are specified.
- `40017` Invalid asset.
- `40020` Invalid order price.
- `40021` Invalid order side.
- `40022` Invalid trading start time.
- `40024` Invalid order type.
- `40025` Invalid asset.
- `40028` Invalid uuid.
- `40048` Invalid withdraw amount.
- `40112` Invalid trigger price.
- `40113` Invalid post_only.
- `40114` post_only can not be specified with such order type.
- `40116` Invalid withdrawal type.
- `40117` Invalid withdrawal name.
- `40118` Invalid VASP.
- `40119` Invalid beneficiary type.
- `40120` Invalid beneficiary last name.
- `40121` Invalid beneficiary first name.
- `40122` Invalid beneficiary last kana.
- `40123` Invalid beneficiary first kana.
- `40124` Invalid beneficiary company name.
- `40125` Invalid beneficiary company kana.
- `40126` Invalid beneficiary company type.
- `40127` Invalid beneficiary company type position.
- `40152` Invalid originator label.
- `40153` Invalid originator last name.
- `40154` Invalid originator first name.
- `40155` Invalid originator company name.
- `40156` Invalid originator prefecture.
- `40157` Invalid originator city.
- `40158` Invalid originator address.
- `40159` Invalid originator building.
- `40160` Invalid originator substantial controller name.
- `40163` Invalid beneficiary substantial controller name.
- `40164` Invalid position side.
- `40165` Can not be margin trading with such pair.
- `40200` Stop open orders cannot be accepted.

## DATA_ERROR

- `50003` Account is restricted.
- `50004` Account is provisional.
- `50005` Account is blocked.
- `50006` Account is blocked.
- `50008` Identity verification is not finished.
- `50009` Order not found.
- `50010` Order can not be canceled.
- `50011` Api not found.
- `50026` Order has already been canceled.
- `50027` Order has already been executed.
- `50033` Withdrawals to this address require additional entries.
- `50034` VASP not found.
- `50035` Company information is not registerd.
- `50037` We are temporarily restricting withdrawals while we verify your last deposit. Please try again in a few minutes.
- `50038` Cannot withdraw to chosen VASP service.
- `50043` Originator already registered.
- `50044` Originator not found.
- `50045` Deposit not found.
- `50046` Cannot edit beneficiary under review.
- `50047` Cannot edit disabled beneficiary.
- `50048` Cannot withdraw to beneficiary under review.
- `50049` Beneficiary requires additional entries.
- `50050` Cannot withdraw to chosen beneficiary.
- `50051` Cannot confirm deposit with originator under review.
- `50052` Originator requires additional entries.
- `50053` Cannot edit originator under review.
- `50054` Cannot withdraw because the information registration for unreflected deposits has not been completed.
- `50058` Margin trading review has not been completed.
- `50059` Temporarily restricting new margin orders. Please try your request again after a while.
- `50060` Temporarily restricting new margin orders. Please try your request again after a while.
- `50061` Exceeds available balance for open order.
- `50062` Exceeds total margin position.
- `50070` Withdrawals in JPY are not available.
- `50071` Withdrawals in CC are not available.
- `50072` Buy orders cannot be used in spot transactions.
- `50073` Sell orders cannot be used in spot transactions.
- `50078` Open orders cannot be used in margin trading.
- `50079` Close orders cannot be used in margin trading.
- `50080` Open orders cannot be used in margin trading.
- `50081` Close orders cannot be used in margin trading.
- `50083` Withdrawals can not be used due to realized loss.

## VALUE_ERROR

- `60001` Insufficient amount.
- `60002` Market buy order quantity has exceeded the upper limit.
- `60003` Order quantity has exceeded the limit.
- `60004` Order quantity has exceeded the lower threshold.
- `60005` Order price has exceeded the upper limit.
- `60006` Order price has exceeded the lower limit.
- `60011` Too many Simultaneous orders, current limit is 30.
- `60016` Trigger price has exceeded the upper limit.
- `60017` Withdrawal amount has exceeded the upper limit.
- `60018` Trigger price to trigger immediately cannot be specified.
- `60019` The side of a TakeProfit or StopLoss order must be in the close direction.

## STOP_UPDATE_REQUEST_SYSTEM_STATUS

- `70001` System error.
- `70002` System error.
- `70003` System error.
- `70004` Order is restricted during suspension of transactions.
- `70005` Buy ​​order has been temporarily restricted.
- `70006` Sell ​​order has been temporarily restricted.
- `70009` Market order has been temporarily restricted. Please use limit order instead.
- `70010` Minimum Order Quantity is increased temporarily.
- `70011` System is busy. Please try again.
- `70012` System error.
- `70013` Order and cancel has been temporarily restricted.
- `70014` Withdraw and cancel request has been temporarily restricted.
- `70015` Lending and cancel request has been temporarily restricted.
- `70016` Lending and cancel request has been restricted.
- `70017` Orders on pair have been suspended.
- `70018` Order and cancel on pair have been suspended.
- `70019` Order cancel request is in process.
- `70020` Market order has been temporarily restricted.
- `70021` Limit order price is over the threshold.
- `70022` Stop limit order has been temporarily restricted.
- `70023` Stop order has been temporarily restricted.
- `70024` Long open order has been temporarily restricted.
- `70025` Short open order has been temporarily restricted.
- `70026` Order has been temporarily restricted.
