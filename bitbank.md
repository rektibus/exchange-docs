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
timestamp | number | published at unix timestamp (milliseconds)

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
        ],
        "timestamp": 0
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
[English](public-stream.md)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [リアルタイムデータ配信API](#%E3%83%AA%E3%82%A2%E3%83%AB%E3%82%BF%E3%82%A4%E3%83%A0%E3%83%87%E3%83%BC%E3%82%BF%E9%85%8D%E4%BF%A1api)
  - [API 概要](#api-%E6%A6%82%E8%A6%81)
  - [WSチャンネル一覧](#ws%E3%83%81%E3%83%A3%E3%83%B3%E3%83%8D%E3%83%AB%E4%B8%80%E8%A6%A7)
    - [ティッカー](#%E3%83%86%E3%82%A3%E3%83%83%E3%82%AB%E3%83%BC)
    - [約定履歴](#%E7%B4%84%E5%AE%9A%E5%B1%A5%E6%AD%B4)
    - [板情報の差分配信](#%E6%9D%BF%E6%83%85%E5%A0%B1%E3%81%AE%E5%B7%AE%E5%88%86%E9%85%8D%E4%BF%A1)
    - [板情報](#%E6%9D%BF%E6%83%85%E5%A0%B1)
      - [circuit_break_info.modeが `NONE` もしくは 見積価格がNull の場合](#circuit_break_infomode%E3%81%8C-none-%E3%82%82%E3%81%97%E3%81%8F%E3%81%AF-%E8%A6%8B%E7%A9%8D%E4%BE%A1%E6%A0%BC%E3%81%8Cnull-%E3%81%AE%E5%A0%B4%E5%90%88)
      - [circuit_break_info.modeが `NONE` 以外 かつ 見積価格が存在する 場合](#circuit_break_infomode%E3%81%8C-none-%E4%BB%A5%E5%A4%96-%E3%81%8B%E3%81%A4-%E8%A6%8B%E7%A9%8D%E4%BE%A1%E6%A0%BC%E3%81%8C%E5%AD%98%E5%9C%A8%E3%81%99%E3%82%8B-%E5%A0%B4%E5%90%88)
    - [サーキットブレイク情報](#%E3%82%B5%E3%83%BC%E3%82%AD%E3%83%83%E3%83%88%E3%83%96%E3%83%AC%E3%82%A4%E3%82%AF%E6%83%85%E5%A0%B1)
  - [板情報の処理方法](#%E6%9D%BF%E6%83%85%E5%A0%B1%E3%81%AE%E5%87%A6%E7%90%86%E6%96%B9%E6%B3%95)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# リアルタイムデータ配信API

## API 概要

- エンドポイント URL: **wss://stream.bitbank.cc**.
- [socket.io 4.x](https://socket.io/docs/v4/)（Engine.io protocol v4）によって実装されています。下記のサンプルコードでは[github.com/websockets/wscat](https://github.com/websockets/wscat) を利用しています。
- 2022-07-26 より [socket.io](https://socket.io/) が [2.x](https://socket.io/docs/v2/) -> [4.x](https://socket.io/docs/v4/) にバージョンアップされました。
- stream.bitbank.ccの6時間後に自動切断される仕様は廃止されました。エラーが発生した場合は切断されますので、エラー内容をご確認ください。

## WSチャンネル一覧

### ティッカー

ティッカーのwsチャンネルの名前： `ticker_{pair}`。
通貨ペアの一覧: [ペア一覧](pairs.md)。

通常モード以外の場合、sell <= buy となる場合があります。

**Response:**

Name | Type | Description
------------ | ------------ | ------------
sell | string | 現在の売り注文の最安値
buy | string | 現在の買い注文の最高値
high | string | 過去24時間の最高値取引価格
low | string | 過去24時間の最安値取引価格
open | string | 24時間前の始値
last | string | 最新取引価格
vol | string | 過去24時間の出来高
timestamp | number | 日時（UnixTimeのミリ秒）

**サンプルコード:**

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

**レスポンスのフォーマット:**

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

### 約定履歴

約定履歴のwsチャンネルの名前： `transactions_{pair}`。

通貨ペアの一覧: [ペア一覧](pairs.md)。

**Response:**

Name | Type | Description
------------ | ------------ | ------------
transaction_id | number | 取引ID
side | string | `buy` または `sell`
price | string | 価格
amount | string | 数量
executed_at | number | 約定日時（UnixTimeのミリ秒）

**サンプルコード:**

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

**レスポンスのフォーマット:**

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

### 板情報の差分配信

板情報の差分配信のwsチャンネルの名前： `depth_diff_{pair}`。
通貨ペアの一覧: [ペア一覧](pairs.md)。

通常モード以外の場合、a <= b となる場合があります。

**Response:**

Name | Type | Description
------------ | ------------ | ------------
a | [string, string][] | [ask, amount][]
b | [string, string][] | [bid, amount][]
ao | string \| undefined | [asks](#板情報)の最高値よりも高いasksの数量。数量の変動がない場合はメッセージに含まれません。
bu | string \| undefined | [bids](#板情報)の最安値よりも安いbidsの数量。数量の変動がない場合はメッセージに含まれません。
au | string \| undefined | [bids](#板情報)の最安値よりも安いasksの数量。数量の変動がない場合はメッセージに含まれません。
bo | string \| undefined | [asks](#板情報)の最高値よりも高いbidsの数量。数量の変動がない場合はメッセージに含まれません。
am | string \| undefined | 新しい成行売り数量。数量の変動がない場合はメッセージに含まれません。
bm | string \| undefined | 新しい成行買い数量。数量の変動がない場合はメッセージに含まれません。
t | number | 日時（UnixTimeのミリ秒）
s | string | シーケンスID、単調増加しますが連続しているとは限りません

`a` (asks)と `b` (bids)のamountは絶対数量です。またamountが0なものはその気配値が無くなったことを示します。

`s` は `depth_whole_{pair}` の `sequenceId` と共通のシーケンスIDです。

使い方については [板情報の処理方法](#%E6%9D%BF%E6%83%85%E5%A0%B1%E3%81%AE%E5%87%A6%E7%90%86%E6%96%B9%E6%B3%95) の節をご覧ください。

<a name="depth-diff-sample-code"></a>**サンプルコード:**

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

**レスポンスのフォーマット:**

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

### 板情報

板情報のwsチャンネルの名前： `depth_whole_{pair}`
通貨ペアの一覧: [ペア一覧](pairs.md)。

通常モード以外の場合、asks <= bids となる場合があります。

#### circuit_break_info.modeが `NONE` もしくは 見積価格がNull の場合

- asks, bidsで配信されるデータは、Best Bid Offerから200件ずつです。
- したがって、asks, bidsのBBO（Best Bid Offer）は必ず `最も安いAsk > 最も高いBid` となります。

#### circuit_break_info.modeが `NONE` 以外 かつ 見積価格が存在する 場合

- asks, bidsで配信されるデータは、見積価格から上下200件ずつです。（最大400件）
- したがって、通常時とは異なり、 `最も安いAsk < 最も高いBid` となる場合があります。
- また、配信データの価格範囲よりも安い売り注文は `asks_under` に、高い買い注文は `bids_over` に加算されます。

**Response:**

Name | Type | Description
------------ | ------------ | ------------
asks | [string, string][] | 売り板 [価格, 数量]
bids | [string, string][] | 買い板 [価格, 数量]
asks_over | string | asksの最高値(asks配列の一番最後の要素)よりも高いasksの数量
bids_under | string | bidsの最安値(bids配列の一番最後の要素)よりも安いbidsの数量
asks_under | string | bidsの最安値(bids配列の一番最後の要素)よりも安いasksの数量。通常モードの場合は `0`
bids_over | string | asksの最高値(asks配列の一番最後の要素)よりも高いbidsの数量。通常モードの場合は `0`
ask_market | string | 成行売り数量。通常モードの場合は `0`
bid_market | string | 成行買い数量。通常モードの場合は `0`
timestamp | number | timestamp
sequenceId | number | シーケンスID、単調増加しますが連続しているとは限りません

`sequenceId` は `depth_diff_{pair}` の `s` と共通のシーケンスIDです。

使い方については [板情報の処理方法](#%E6%9D%BF%E6%83%85%E5%A0%B1%E3%81%AE%E5%87%A6%E7%90%86%E6%96%B9%E6%B3%95) の節をご覧ください。

<a name="depth-whole-sample-code"></a>**サンプルコード:**

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

**レスポンスのフォーマット:**

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

### サーキットブレイク情報

[Public API] サーキットブレイク情報を取得。

**Response:**

Name | Type | Description
------------ | ------------ | ------------
mode | string | `NONE` または `CIRCUIT_BREAK` または `FULL_RANGE_CIRCUIT_BREAK` または `RESUMPTION` または `LISTING`
estimated_itayose_price | string \| null | 見積価格。通常モードまたは見積価格が無い場合はnull
estimated_itayose_amount | string \| null | 見積数量。通常モードであればnull
itayose_upper_price | string \| null | CB時制限値幅価格上限。通常モード、無期限サーキットブレイクモード、新規上場モードはnull
itayose_lower_price | string \| null | CB時制限値幅価格下限。通常モード、無期限サーキットブレイクモード、新規上場モードはnull
upper_trigger_price | string \| null | CB突入判定価格上限。CB中はnull
lower_trigger_price | string \| null | CB突入判定価格下限。CB中はnull
fee_type | string | `NORMAL` または `SELL_MAKER` または `BUY_MAKER` または `DYNAMIC`
reopen_timestamp | number \| null | サーキットブレイク終了予定時刻（UnixTimeのミリ秒）。通常モード、またはCB終了予定時刻がない場合はnull
timestamp | number | 日時（UnixTimeのミリ秒）

`mode` および `fee_type` の詳細は[サーキットブレーカー制度](https://bitbank.cc/docs/circuit-breaker-mode/)のページをご確認ください。

**サンプルコード:**

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

**レスポンスのフォーマット:**

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

## 板情報の処理方法

あるペアのリアルタイムな板情報は以下のように `depth_whole_{pair}` および `depth_diff_{pair}` roomのメッセージを処理することで得られます:

1. `depth_whole_{pair}` および `depth_diff_{pair}` について受信を開始します。方法については[板情報](#depth-whole-sample-code)および[板情報の差分配信のサンプルコード](#depth-diff-sample-code)をご覧ください。
1. `depth_diff_{pair}` メッセージたちを継続的にバッファ（記憶）します。
1. `depth_diff_{pair}` メッセージを受信したら、
    * その数量が「非0」なら、板のその気配値について追加または上書きします。
    * その数量が「0」なら、板からその気配値を取り除きます。
1.  `depth_whole_{pair}` メッセージを受信したら、
    * 板をその `data` で置き換え、
    * バッファしておいた `depth_diff_{pair}` たちを、
        * その `s` の昇順で、
        * その `s` が `depth_whole_{pair}` の `sequenceId` より大きいものについてのみ、
    * 適用します。

`depth_whole_{pair}` の処理方法について例示します。
例えば以下の順でメッセージを受信した場合:

> diff{s=3}, diff{s=5}, diff{s=6}, diff{s=8}, whole{sequenceId=5}

`whole{sequenceId=5}` で板を置き換えた後、 `diff{s=6}` と `diff{s=8}` をこの順で適用しなおします。 `diff{s=3}` と `diff{s=5}` は無視します。

シーケンスIDは（少なくともroomごとには）巻き戻ることはありませんので、
バッファした `depth_diff_{pair}` メッセージたちのうち、その `s` が最後の `depth_whole_{pair}` メッセージの `sequenceId` より小さいか等しいものについて破棄することでリソース使用量を削減できます。

**注意事項:**

* `depth_diff_{pair}` メッセージはその時々のbest bid/askより200エントリに対するものしか配信されません。
  このため、正確な板情報を得るには `depth_whole_{pair}` メッセージで定期的に置き換えし続ける必要があります。
  （さもなくば価格変動時に変動方向の価格を見過すことになります。）
* `depth_whole_{pair}` メッセージは `depth_diff_{pair}` メッセージより遅延することがあります。
  このため、 `depth_diff_{pair}` メッセージをバッファし `depth_whole_{pair}` メッセージ受信時に再適用する必要があります。
