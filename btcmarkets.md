## API Overview
BTC Markets provides a simple REST API which allows for integration of business applications, payment systems, trading engines, mobile apps, etc.  

All requests use the "application/json" content type and must use https. 

Unless specified all API methods use http POST.

The base url for the API is: https://api.btcmarkets.net

If you have any feedback on the API please post a question in our support center.


## Getting started
Before using API please take some time to understand the authentication mechanism built into the API.  Some parts of the API require authentication and in those cases you will be required to register with BTC Markets and then [generate a set of API keys](https://www.btcmarkets.net/account/apikey).

Market data API is accessible through https and parameters are passed using GET-requests. All responses are encoded in JSON.

Currently the market APIs are cached for 1 second (Except trades which is cached for 2 seconds).

## Tick:

path: `/market/BTC/AUD/tick`

sample response:
```json
{"bestBid":13837.64,"bestAsk":13865.91,"lastPrice":13865.91,"currency":"AUD","instrument":"BTC","timestamp":1563999153,"volume24h":202.73146,"price24h":-728.71,"low24h":13692.44,"high24h":14594.62}
```

## Orderbook:

path: `/market/BTC/AUD/orderbook`

sample response:
```json
{"currency":"AUD","instrument":"BTC","timestamp":1476243360,"asks":[[844.98,0.45077821],[845.0,2.7069457],[848.68,2.58512],[848.76,0.29745]],"bids":[[844.0,0.00489636],[840.21,0.060724],[840.16,0.1180803],[840.1,0.32130103]]}
```

## Trades:

path: `/market/BTC/AUD/trades`

sample response:
```json
[{"tid":4432702312,"amount":0.01959674,"price":845.0,"date":1378878093},{"tid":59861212129,"amount":1.21434000,"price":845.15,"date":1377840783}]
```
`since` is an optional parameter for trades (get trades since the trade id). For instance:

/market/BTC/AUD/trades?since=59868345231

# v2/

## Active markets:

path: `/v2/market/active`

sample response:
```json
{
    "success": true,
    "errorCode": null,
    "errorMessage": null,
    "markets": [
        {
            "instrument": "BTC",
            "currency": "AUD"
        },
        {
            "instrument": "LTC",
            "currency": "AUD"
        },
        {
            "instrument": "LTC",
            "currency": "BTC"
        },
        {
            "instrument": "ETH",
            "currency": "BTC"
        },
        {
            "instrument": "ETH",
            "currency": "AUD"
        },
        {
            "instrument": "XRP",
            "currency": "AUD"
        },
        {
            "instrument": "XRP",
            "currency": "BTC"
        },
        {
            "instrument": "POWR",
            "currency": "AUD"
        },
        {
            "instrument": "POWR",
            "currency": "BTC"
        },
        {
            "instrument": "OMG",
            "currency": "AUD"
        },
        {
            "instrument": "OMG",
            "currency": "BTC"
        }
    ]
}
```

## Trades:

path: `/v2/market/{instrument}/{currency}/trades`

url parameters:
* `indexForward`: Set to `true` to see trades more recent in time, if a `since` parameter is used. Default is `false`. 
* `limit`: Number of results to return per "page". If not provided, default is 200.
* `since`: a trade id. If provided, and `indexForward` is `false`, returned results will be trades earlier than the trade id provided, non-inclusive. If `indexForward` is `true`, returned results will be trades after the trade id provided, non-inclusive.

pagination: yes

sample request: `/v2/market/BTC/AUD/trades?limit=&since=116082008`

sample response:
```json
{
    "success": true,
    "errorCode": null,
    "errorMessage": null,
    "trades": [
        {
            "id": 116082007,
            "price": 88118000000,
            "volume": 1189817,
            "creationTime": 1468115880783
        },
        {
            "id": 116075304,
            "price": 87100000000,
            "volume": 100000,
            "creationTime": 1468114578646
        },
        {
            "id": 116074896,
            "price": 88374000000,
            "volume": 220427,
            "creationTime": 1468114492317
        },
        {
            "id": 116058580,
            "price": 88142000000,
            "volume": 962049,
            "creationTime": 1468111460168
        },
        {
            "id": 116053310,
            "price": 88266000000,
            "volume": 15328802,
            "creationTime": 1468110652290
        }
    ],
    "paging": {
        "newer": "/v2/market/BTC/AUD/trades?limit=5&since=116082007&indexForward=true",
        "older": "/v2/market/BTC/AUD/trades?limit=5&since=116053310&indexForward=false"
    }
}
```

## Historical Ticks:

path: `/v2/market/{instrument}/{currency}/tickByTime/{[minute | hour | day]}`

url parameters:
* `limit`: Number of results to return per "page". If not provided, default is 3000.
* `since`: a unix timestamp in milliseconds. If provided, and `indexForward` is `false`, returned results will be candles earlier than the timestamp provided, inclusive. If `indexForward` is `true`, returned results will be candles after the timestamp provided, inclusive.
* `indexForward`: Set to `true` to see candles more recent than the timestamp in the `since` parameter, if a `since` parameter is used. Default is `false`. 
* `sortForward`: Set to `true` to see the earliest candles first in the list of returned candles i.e. in chronological order. Default is `false`.

pagination: yes

sample request: `/v2/market/BTC/AUD/tickByTime/hour?since=1537671600000&limit=4&indexForward=true&sortForward=true`

sample response:
```json
{
    "success": true,
    "paging": {
        "newer": "/v2/market/BTC/AUD/tickByTime/hour?limit=4&sortForward=true&indexForward=true&since=1537682400000",
        "older": "/v2/market/BTC/AUD/tickByTime/hour?limit=4&sortForward=true&since=1537671600000"
    },
    "ticks": [
        {
            "timestamp": 1537671600000,
            "open": 908800000000,
            "high": 909771000000,
            "low": 906053000000,
            "close": 906935000000,
            "volume": 1113664994
        },
        {
            "timestamp": 1537675200000,
            "open": 908506000000,
            "high": 909770000000,
            "low": 906936000000,
            "close": 909184000000,
            "volume": 929443810
        },
        {
            "timestamp": 1537678800000,
            "open": 909187000000,
            "high": 909600000000,
            "low": 909187000000,
            "close": 909596000000,
            "volume": 215936611
        },
        {
            "timestamp": 1537682400000,
            "open": 909596000000,
            "high": 909616000000,
            "low": 907175000000,
            "close": 907175000000,
            "volume": 388776816
        }
    ]
}
```Please find the latest and most up to date documentation here:
https://docs.btcmarkets.net


WebSocket feed provides real-time market data covering orderbook updates, order life cycle and trades. 

note: This will remain beta version for a few weeks before it's released around April 2019. 

### Overview
In order to start receiving real time messages, a WebSocket connection needs to be made followed by a message to `subscribe` to channels and also marketIds you are interested in. 
  
The endpoint for WebSocket v2 is: `wss://socket.btcmarkets.net/v2`

### Improvements in v2
WebSocket v2 provides a number of improvements including:  
* Authenticated channels: allows individual traders to receive notifications for changing life cycle of an order including placement, cancellation, matching and triggering
* Channel subscription: allows for easier and more flexible integration using a single WebSocket connection 
* Better data model and json format. e.g. ISO date and time 
* Error handling: publishing error messages in case of issues (e.g. authentication error)   
* Heartbeat message: helps client applications to better managing connections
* Using standard WebSocket instead of specific socket.io implementation 


### Channels 
`tick`, `trade`, `orderbook`, `orderChange`, `fundChange`, `heartbeat`


### MarketIds
Market ids represent a market and are used in order to filter events for only specific markets you are interested in.  

You should be able to pass any active markets as per below:
https://api.btcmarkets.net/v2/market/active  

Format: `BTC-AUD`, `XRP-BTC`, etc. 

Note: marketIds are only applicable to public events (e.g. `tick`, `orderbook`, `trade`)


### Message types   
All messages published include a `json` attribute called `messageType` that represents type of event that is being received. 

Those message types events include: `tick`, `trade`, `orderbook`, `orderChange`, `fundChange`, `error`, `heartbeat`

### Subscribe 
sending `subscribe` message allows you to start receiving events for the specified channels and marketIds.  If you need to change subscription then simply send a new `subscribe` message with new channel names and marketIds.  


### Tick event
The `tick` event is published every time `lastPrice`, `bestBid` or `bestAsk` is updated for a market which is the result of orderbook changes or trade matches.  

sample event:

```javscript
{ marketId: 'BTC-AUD',
  timestamp: '2019-04-08T18:56:17.405Z',
  bestBid: '7309.12',
  bestAsk: '7326.88',
  lastPrice: '7316.81',
  volume24h: '299.12936654',
  messageType: 'tick' 
}
```

### Trade event
In order to receive `trade` events please add `trade` to the list of channels when subscribing via WebSocket. 

sample event:

```javscript
{ marketId: 'BTC-AUD',
  timestamp: '2019-04-08T20:54:27.632Z',
  tradeId: 3153171493,
  price: '7370.11',
  volume: '0.10901605',
  messageType: 'trade' 
}
```

### Orderbook event
In order to receive `orderbook` events please add `orderbook` to the list of channels when subscribing via WebSocket. The current orderbook event represents the latest orderbook state and maximum 50 bids and asks are included in each event. 

For efficiency the `bids` and `asks` are are published as arrays of `tuples` representing `[price, volume]` each order in the orderbook.  


sample event:

```javascript
{ marketId: 'BTC-AUD',
  timestamp: '2019-04-08T22:23:37.643Z',
  bids:
   [ [ '7418.46', '0.04' ],
     [ '7418.45', '0.56' ],
     [ '7100', '0.01' ] ]
  asks:
   [ [ '7437.53', '0.76' ],
     [ '7437.54', '0.3646349' ],
     [ '7446.94', '0.6' ],
     [ '7700', '0.1' ] ]
  messageType: 'orderbook' 
}
```
   
### Sample WebSocket client code (javascript) 

Below sample code connects to `tick` channel. The same code can be used to subscribe to other public channels including heartbeat. 


```javascript
const WebSocket = require('ws');
const ws = new WebSocket('wss://socket.btcmarkets.net/v2');

var request = {
    marketIds:marketIds,
    channels: channels,
    messageType: 'subscribe'
}

ws.on('open', function open() {
    ws.send(JSON.stringify(request));
});

ws.on('message', function incoming(data) {
    console.log(data);
});

```

### Authenticated events
Receiving events about life cycle of your orders require sending authentication information when subscribing to events. The authentication is similar to public trading API authentication using your API key and secret to sign  the message when subscribing via WebSocket. 

Below is sample `javascript` code with authentication:

```javascript
const crypto = require('crypto');
const WebSocket = require('ws');

const key = 'your api key';
const secret = 'your api key secret';

const ws = new WebSocket('wss://socket.btcmarkets.net/v2');

const now = Date.now();
const strToSign =  "/users/self/subscribe" + "\n" + now;
const signature = signMessage(secret, strToSign);

var request = {
    marketIds:['BTC-AUD'],
    channels: ['orderChange', 'heartbeat'],
    key: key,
    signature: signature,
    timestamp: now,
    messageType: 'subscribe'
}

ws.on('open', function open() {
    ws.send(JSON.stringify(request));
});

ws.on('message', function incoming(data) {
    console.log(data);
});

function signMessage(secret, message) {
    var key = Buffer.from(secret, 'base64');
    var hmac = crypto.createHmac('sha512', key);
    var signature = hmac.update(message).digest('base64');
    return signature;
}
 
```

### Order life cycle events

Below are events that are published for every step of order processing.  


* Placed

``` javascript 
{ orderId: 79003,
  marketId: 'BTC-AUD',
  side: 'Bid',
  type: 'Limit',
  openVolume: '1',
  status: 'Placed',
  triggerStatus: '',
  trades: [], 
  timestamp: '2019-04-08T20:41:19.339Z',
  messageType: 'orderChange' 
}
```

* Fully Matched

```javscript 
{ orderId: 79033,
  marketId: 'BTC-AUD',
  side: 'Bid',
  type: 'Limit',
  openVolume: '0',
  status: 'Fully Matched',
  triggerStatus: '',
  trades: [{  
     tradeId:31727,
     price":'0.1634',
     volume":'10',
     fee:'0.001',
     liquidityType:'Taker'
   }],
  timestamp: '2019-04-08T20:50:39.658Z',
  messageType: 'orderChange' 
}
``` 

* Cancelled
```javscript 
{ orderId: 79003,
  marketId: 'BTC-AUD',
  side: 'Bid',
  type: 'Limit',
  openVolume: '1',
  status: 'Cancelled',
  triggerStatus: '',
  trades: [],  
  timestamp: '2019-04-08T20:41:41.857Z',
  messageType: 'orderChange' 
}
```

* Partially Matched
```javscript 
{ orderId: 79003,
  marketId: 'BTC-AUD',
  side: 'Bid',
  type: 'Limit',
  openVolume: '1',
  status: 'Partially Matched',
  triggerStatus: '',
  trades: [{  
     tradeId:31927,
     price:"0.1634',
     volume:"5',
     fee:'0.001',
     liquidityType:'Taker'
  }]
  timestamp: '2019-04-08T20:41:41.857Z',
  messageType: 'orderChange' 
}
```

* Triggered
This event is published when `Stop Limit` orders are triggered.

```javscript 
{ orderId: 7903,
  marketId: 'BTC-AUD',
  side: 'Bid',
  type: 'Limit',
  openVolume: '1.2',
  status: 'Placed',
  triggerStatus: 'Triggered',
  trades: [],
  timestamp: '2019-04-08T20:41:41.857Z',
  messageType: 'orderChange' 
}
```

Notes: 

* `Fully Matched` and 'Partially Matched' events also include a list of trades that are the result of trade execution for that specific instance.  

* In case if two or more events are published by trading engine at the same time then only the last event is published. For instance in the case of a `Stop` order being triggered and matched at the same time then a single event is published.    


### Fund transfer events 
Those events are published when deposit or withdraws of funds are requested by a user or approved by the system (and result in balance updates). Channel name used is `fundChange`. 

```javscript
{
  fundtransferId: 276811,
  type: 'Deposit',
  status: 'Complete',
  timestamp: '2019-04-16T01:38:02.931Z',
  amount: '0.001',
  currency: 'BTC',
  fee: '0',
  messageType: 'fundChange'
}
```

Note: status of a withdraw request is `Pending Authorization` when it's requested in the first place and before it becomes `Complete`.  


### Heartbeat event 
if you subscribe to `heartbeat` event then the server will send you a heartbeat event every 5 seconds. 

heartbeat event:
``` javascript
{
  messageType: 'heartbeat',
  channels: [
    {
      name: 'orderChange'
    },
    {
      name: 'orderbook',
      marketIds: [
        'BTC-AUD',
        'XRP-AUD'
      ]
    },
    {
      name: 'heartbeat'
    }
  ]
}
```

Note: Once a new subscription request is confirmed, a single `heartbeat` event is published to the client in order to confirm the connection working. This is regardless of requesting to subscribe to `heartbeat` channel.   

### Advanced subscription message types
Whilst sending `subscribe` message works in most situations, however you may need to have the flexibility to add or remove subscriptions instead of subscribing to all channels/markets at the same time.

In those situations send the same subscription message (all rules applies for authentication, marketIds, etc) and the message type will be `addSubscription` or `removeSubscription`. If you need to remove subscription for all markets fo a given channel, just send empty list of marketIds. 

### Error event 
In case of errors, a message type of `error` is published. 

* Authentication error 
* Invalid input error 
* Internal server error
* Throttle error

sample error events:

* Invalid Channel names 
```javascript 
{ messageType: 'error',
  code: 3,
  message: 'invalid channel names' 
}
```

* Invalid MarketIds 
```javascript 
{ messageType: 'error',
  code: 3,
  message: 'invalid marketIds' 
}
```

* Authentication error
``` javascript 
{ messageType: 'error',
  code: 1,
  message: 'authentication failed. invalid key' 
}
```

### Sample client code
Below are working example of how to connect to this WebSocket feed in different languages: 

* Java: [[https://github.com/ngin-io/websocket-client-java]]
* Javascript: [[https://github.com/ngin-io/websocket-client-node]]
* Python: [[https://github.com/ngin-io/websocket-client-python]]

### Rate limit
New connections to the WebSocket feed are rate limited to 3 attempts per 10 seconds per IP. Frequent WebSocket connections that exceed the rate limit will be closed by the server.    


### Connection issues
From time to time your WebSocket connection may be disconnected (e.g. as we upgrade software on our servers). We recommend adding logic to your client in order to refresh your connection every 24 hours or in case if the connection drops out. 
 
To authenticate a request, you will need to build a string which includes several elements of the http request. You will then use your private API key to calculate a HMAC of that string. 

This will generate a signature string which needs to be added as a parameter of the request by using the syntax described in the following sections. 


### Timestamp/nonce
A valid client timestamp must be used for authenticated requests. the timestamp included with an authenticated request must be within +/- 30 seconds of the server timestamp at the time when the request is received. Failing to submit a timestamp will result in authentication fail response. Please ensure the computer executing your code has it's time synced to a NTP (Network time protocol) server to ensure it doesn't fall out of sync with the API server.

The intention of these restrictions is to limit the possibility that intercepted requests could be replayed by an adversary.  

### Authentication example for a GET request
Below is an example of creating a signature for /account/balance API

1- Private (Secret) Key

``
werwerwerr5lkZyh7s8JjJMVh5ahd4HnFBR7o+ODQBSmj7DhTKF59fNsRVmYMMVHlTW7EdMhSJwwlbOEJaIpruQ==
``
  * decoded from base 64 and displayed in hexadecimal grouped by bytes, the above secret key becomes: 
``c1 ea f0 7a bc 1e ae be 65 91 9c a1 ee cf 09 8c 93 15 87 96 a1 77 81 e7 14 14 7b a3 e3 83 40 14 a6 8f b0 e1 4c a1 79 f5 f3 6c 45 59 98 30 c5 47 95 35 bb 11 d3 21 48 9c 30 95 b3 84 25 a2 29 ae e4``

2- URI

``
/account/balance
``

3- current timestamp in milliseconds

``
1519429556662
``

The string to sign is:

``
'/account/balance' + '\n' + '1519429556662' + '\n'
``
 
Note: if creating a signature for http GET method then post data will be null and therefore no need to add it to this string. 

Use HmacSHA512 algorithm in order to sign above string with your API private key which results in the following signature: (sample signature only)

``
'sPGaVm2a0TLmqzyNDMYnHPkXAiyu2Dhn/WL3XlTowTSlwpykSApubBR795HLzUljJk6KFvAxhVVplzrIvFuChA=='
``

### Authentication example for a v2 GET request
Below is an example of creating a signature for /v2/order/history API

1- Private (Secret) Key

``
werwerwerr5lkZyh7s8JjJMVh5ahd4HnFBR7o+ODQBSmj7DhTKF59fNsRVmYMMVHlTW7EdMhSJwwlbOEJaIpruQ==
``
  * decoded from base 64 and displayed in hexadecimal grouped by bytes, the above secret key becomes: 
``c1 ea f0 7a bc 1e ae be 65 91 9c a1 ee cf 09 8c 93 15 87 96 a1 77 81 e7 14 14 7b a3 e3 83 40 14 a6 8f b0 e1 4c a1 79 f5 f3 6c 45 59 98 30 c5 47 95 35 bb 11 d3 21 48 9c 30 95 b3 84 25 a2 29 ae e4``

2- URI __Note the request parameters__

``
/v2/order/trade/history/ETH/AUD?indexForward=true&limit=10&since=698825
``

3- current timestamp in milliseconds

``
1519429556662
``

The string to sign is:

``
'/v2/order/trade/history/ETH/AUD' + '\n' + indexForward=true&limit=10&since=698825 + '\n' + '1519429556662' + '\n'
``
 
Note: if creating a signature for http GET method then post data will be null and therefore no need to add it to this string. 

Use HmacSHA512 algorithm in order to sign above string with your API private key which results in the following signature: (sample signature only)

``
GDw4W2jlZWctWgg1nYjSN32TjgbbXWLSj1gnEhYdiG2kweKBUfZS4RCEgaOX+/mvUPu9Mr1B+E2jGuJmE62R8Q=='
``


### Authentication example for a POST request
Below is an example of creating a signature for /order/history API. 

In this example the parameters used to calculate the signature are:

1- Private (Secret) Key

``
werwerwerr5lkZyh7s8JjJMVh5ahd4HnFBR7o+ODQBSmj7DhTKF59fNsRVmYMMVHlTW7EdMhSJwwlbOEJaIpruQ==
``
  * decoded from base 64 and displayed in hexadecimal grouped by bytes, the above secret key becomes: 
``c1 ea f0 7a bc 1e ae be 65 91 9c a1 ee cf 09 8c 93 15 87 96 a1 77 81 e7 14 14 7b a3 e3 83 40 14 a6 8f b0 e1 4c a1 79 f5 f3 6c 45 59 98 30 c5 47 95 35 bb 11 d3 21 48 9c 30 95 b3 84 25 a2 29 ae e4``

2- URI

``
/order/history
``

3- current timestamp in milliseconds

``
1519429556662
``

4- Request body
```json
'{"currency":"AUD","instrument":"BTC","limit":10,"since":null}'
```

The string to sign is:

``
'/order/history' + '\n' + '1519429556662' + '\n' + '{"currency":"AUD","instrument":"BTC","limit":10,"since":null}'
``
 
Note: if creating a signature for http GET method then post data will be null and therefore no need to add it to this string. 

Use HmacSHA512 algorithm in order to sign above string with your API private key which results in the following signature: (sample signature only)

``
'aHVFCu0qPPDe5OKhlHbp7dGI6X01dPLT51+eVr5o4lzkVxXe1UFtuaPCSP91kiznMf/2VVaYraHv7Q8atfd/EA=='
``


Now we are ready to build a http request with all the headers required.


* "Accept": "application/json"
* "Accept-Charset": "UTF-8"
* "Content-Type": "application/json"
* "apikey": "your public API key"
* "timestamp": "timestamp used in above process to create the signature"
* "signature": "aHVFCu0qPPDe5OKhlHbp7dGI6X01dPLT51+eVr5o4lzkVxXe1UFtuaPCSP91kiznMf/2VVaYraHv7Q8atfd/EA=="

## Why Do I Get "authentication failed" Message?
Please check the list below as failing to meet any one of those requirements can cause this error.
* Secret key must be decoded from base64
* The signature is the HMAC encoded to base64.
* Confirm public key and secret are correct by logging into your account and confirming the values are correct.
* Timestamp/nonce is in milliseconds and therefore must be 13 digits long.
* The computer executing your code should have it's time synced to a NTP (Network time protocol) server to ensure it doesn't fall out of sync with the API server. A variance of 30 seconds will cause the request to fail.
* The order of POST variables is important and must exactly match the sample requests provided, otherwise an invalid HMAC will be created.
  * Depending on your programming language, the JSON object used in your POST data may need to be converted to a string before sending the request so that the order of the variables is maintained. 
* For POST requests including price or volume, numbers must be in the appropriate integer format using the 100000000 or 1E8 conversion factor.



Trade API covers all order placement and trade management.

## Order Status
Below is the list of possible order status values:
* New
* Placed
* Failed
* Error
* Cancelled
* Partially Cancelled
* Fully Matched
* Partially Matched

## Number Conversion
All numbers, specifically for price and volume, must be converted to an integer for use in Trading API requests. The conversion is 100000000, or 1E8. For strongly typed programming languages, use of integer or long integer variable types is strongly recommended, as decimals will not be accepted by the API.

## Create an order

places a new order if the parameters are correct and the account has sufficient funds.

sample request:
```json
{
  "currency": "AUD",
  "instrument": "BTC",
  "price": 13000000000,
  "volume": 10000000,
  "orderSide": "Bid",
  "ordertype": "Limit"
}
```

sample success response:
```json
{
  "success": true,
  "errorCode": null,
  "errorMessage": null,
  "id": 100,
  "clientRequestId": null
}
```

sample error response

```json
{
  "success": false,
  "errorCode": 3,
  "errorMessage": "Invalid argument.",
  "errorDetail": "Invalid order type",
  "id": 0,
  "clientRequestId": "null",
}
```

### General notes 
* The clientRequestId is not currently used but must be specified. Any string is valid.
* Price of $130 = 13000000000 (i.e x 100000000)
* Volume of 1 BTC = 100000000 (i.e x 100000000)
* When passing AUD as currency, maximum 2 decimal points are allowed. In above example, $130 and $130.12 are allowed but $130.123 will return "invalid amount".   
* In case of placing **Market** orders, `price` price is ultimately set by matching engine depending on existing orders in the orderbook at the time of trade execution. 

### Order types  
The following types of orders are supported: 
* Limit
* Market
* Stop Limit 
* Take Profit
* Stop 

### Stop orders 
* In the case of placing a **Stop Limit** order, the `ordertype` will be `"Stop Limit"`, and an additional field `triggerPrice` must be supplied with the same number conversion as `price`.
* In the case of placing a **Stop** order, the `ordertype` will be `"Stop"`, and an additional field `triggerPrice` must be supplied with the same number conversion as `price`. When triggerPrice is reached, a market order will be executed. 
* In the case of placing a **Take Profit** order, the `ordertype` will be `"Take Profit"`, and an additional field `triggerPrice` must be supplied with the same number conversion as `price`. When triggerPrice is reached, a market order will be executed.
* For both `Stop` orders and `Take Profit` orders `price` is ultimately set by matching engine depending on existing orders in the orderbook at the time of trade execution (same as for market orders).


### Post-Only orders  (08/30)
`postOnly` is an optional boolean flag with true/false value. The default is false for all new orders. When this option is set to `true` then it means the order should only be posted to the orderbook if it does not result in any trades at the time of placement.  If any part of the order results in trade execution, the order will be cancelled. Please note: once the order is accepted as part of the initial placement then it may execute at any later time depending on the market price movements. The option is only applied for the time of placement.   

`postOnly` option is only applicable to `Limit` orders.

This option is mainly useful for market makers and liquidity providers. 


### Time In Force (08/30)
`timeInForce` option allows traders to control order life time with the following possible values. 
* `GTC`: good to cancel (the default value if not specified)
* `IOC`: immediate or cancel. The order should be cancelled immediately after being placed in the orderbook. The order may be matched against existing orders as part of the initial placement in the orderbook but any volume that is is left from trade matching will be cancelled immediately after placement. Therefore possible results of an order with `IOC` option will be either `Fully Matched`, `Partially Matched`, `Cancelled` or `Partially Cancelled`.

* `FOK`: fill or kill. The order is cancelled if it's not executed fully at the time of placement. Possible results of an order with `FOK` option will be either `Fully Matched` or `Cancelled` immediately.  

Note: When `postOnly` option is set to `true` then the only possible value for `timeInForce` is `IOC` or leave it as empty. 


### Target Amount (08/30)
This is an optional parameter allowing traders to instruct the system to `sell` (or `buy)` as many number of `instrument` as possible so that the `targetAmount` is reached. For example, as a trader, I'd like to receive $100 (the target amount) by selling as many of my `XRPs` (the actual volume is determined by the system at the time of placing the order).  The system then makes best effort to determine the total volume of `XRP` that is needed to sell in order to generate $100 considering all trading fees, partial order match, etc. 

This feature eliminates the need for traders to calculate how many XRP's are needed before placing an order and particularly when marker is moving quickly, this might be a difficult task. 

This option also works for `Bid` orders with the use case being: I'd like to spend maximum $100 on buying `LTC` and the system determines the total volume that I can purchase considering all fees.

`targetAmount` option is only applicable to `Market` orders.

below is a sample request when specifying target amount:

```json
{
  "currency": "AUD",
  "instrument": "XRP",
  "targetAmount": 10000000000,
  "orderSide": "Ask",
  "ordertype": "Market"
}
```
Please note that `price` and `volume` are not required when using `targetAmount`. 


### Self Trade Prevention (08/30)
`selfTrade` option allows traders to control possibility of their own orders execute against each other. For instance if you already have an order already in the orderbook to buy 100 `XRP` for price of 0.50 and then place a new order to sell 100 `XRP` with the same price of 0.50 then the new sell order will be cancelled immediately and won't be submitted to the orderbook. The existing order (the the buy order for 100 XRP) will continue to stay in the orderbook and will work as normal. 

The same is true also when the new order has the potential to partially match existing orders. So in above sample (your existing buy order of 100 `XRP`) and if you place a new sell order with selfTrade option to sell 200 `XRP` (given that 100 of those `XRP` will potentially match with an existing order that does not belong to you) then again the entire new sell order will be cancelled immediately due to self trade option. 
   
Please also note that this option is only checked at the time of order arrival and only once. If the order stays in the orderbook then this option is not applicable anymore. 

Possible values for `selfTrade` option are `A` (self trade is allowed that is the default behavior) and `P` to prevent self trade.

sample request with all of the options:
```json
{
  "currency": "AUD",
  "instrument": "BTC",
  "price": 13000000000,
  "volume": 10000000,
  "orderSide": "Bid",
  "ordertype": "Limit",
  "postOnly": false,
  "timeInForce": "FOK",
  "selfTrade": "A"
}
```


## Cancel an order
path: /order/cancel

http post

sample request:

```json
{"orderIds":[6840125478]}
```

The array of order ids can contain maximum 30 items. 

sample response:
```json
{"success":true,"errorCode":null,"errorMessage":null,"responses":[{"success":false,"errorCode":3,"errorMessage":"order does not exist.","id":6840125478}]}
```


## Order history
path: /order/history

http post

since parameter for this api method is the order id. 

sample request:

```json
{"currency":"AUD","instrument":"BTC","limit":10,"since":33434568724}
```

sample response:

```json
{"success":true,"errorCode":null,"errorMessage":null,"orders":[{"id":1003245675,"currency":"AUD","instrument":"BTC","orderSide":"Bid","ordertype":"Limit","creationTime":1378862733366,"status":"Placed","errorMessage":null,"price":13000000000,"volume":10000000,"openVolume":10000000,"clientRequestId":null,"trades":[]},{"id":4345675,"currency":"AUD","instrument":"BTC","orderSide":"Ask","ordertype":"Limit","creationTime":1378636912705,"status":"Fully Matched","errorMessage":null,"price":13000000000,"volume":10000000,"openVolume":0,"clientRequestId":null,"trades":[{"id":5345677,"creationTime":1378636913151,"description":null,"price":13000000000,"volume":10000000,"fee":100000}]}]}
```

## Open Orders
path: /order/open

http post

This is similar to the order history request and response. The only difference is that this method only returns open orders. 


## Trade History
path: /order/trade/history

http post

since parameter for this api method is the trade id. 

sample request:

```json
{"currency":"AUD","instrument":"BTC","limit":10,"since":33434568724}
```

sample response:

```json
{"success":true,"errorCode":null,"errorMessage":null,"trades":[{"id":374367855,"creationTime":1492232900701,"price":159672000000,"volume":100000,"side":"Ask","fee":1357210,"orderId":374367838},{"id":229485482,"creationTime":1478837751322,"price":94299000000,"volume":100000,"side":"Bid","fee":801540,"orderId":229485469}]}
```


## Order detail
path: /order/detail

http post

sample request:

```json
{"orderIds":[698068, 698771, 698825]}
```
The value(s) for `orderIds` must always be in the format of an array, even if only one ID is included.

sample response:
```json
{
  "success": true,
  "errorCode": null,
  "errorMessage": null,
  "orders": [
    {
      "id": 698068,
      "currency": "AUD",
      "instrument": "ETH",
      "orderSide": "Ask",
      "ordertype": "Market",
      "creationTime": 1516140997056,
      "status": "Fully Matched",
      "errorMessage": null,
      "price": 1200000000,
      "volume": 5000000,
      "openVolume": 0,
      "clientRequestId": null,
      "trades": [
        {
          "id": 698080,
          "creationTime": 1516140997301,
          "description": null,
          "price": 1200000000,
          "volume": 5000000,
          "side": "Ask",
          "fee": 509999,
          "orderId": 698068
        }
      ]
    },
    {
      "id": 698771,
      "currency": "AUD",
      "instrument": "BTC",
      "orderSide": "Bid",
      "ordertype": "Limit",
      "creationTime": 1516919450949,
      "status": "Partially Matched",
      "errorMessage": null,
      "price": 2700000000,
      "volume": 100000000,
      "openVolume": 4400000,
      "clientRequestId": null,
      "trades": [
        {
          "id": 698935,
          "creationTime": 1517808598156,
          "description": null,
          "price": 2700000000,
          "volume": 95600000,
          "side": "Bid",
          "fee": 21940174,
          "orderId": 698771
        }
      ]
    },
    {
      "id": 698825,
      "currency": "AUD",
      "instrument": "BTC",
      "orderSide": "Bid",
      "ordertype": "Limit",
      "creationTime": 1516923611252,
      "status": "Placed",
      "errorMessage": null,
      "price": 2700000000,
      "volume": 100000000,
      "openVolume": 100000000,
      "clientRequestId": null,
      "trades": []
    }
  ]
}
```

# v2

## Open Orders
http GET

path: `/v2/order/open[/{instrument}/{currency}]`

optional: To get all open orders, regardless of instrument and currency, simply leave them out of the path. See second example.

pagination: no

sample request: `/v2/order/open/BTC/AUD`

sample response:
```json
{
    "success": true,
    "errorCode": null,
    "errorMessage": null,
    "orders": [
        {
            "id": 702587,
            "currency": "AUD",
            "instrument": "BTC",
            "orderSide": "Ask",
            "ordertype": "Limit",
            "creationTime": 1531518888090,
            "status": "Placed",
            "errorMessage": null,
            "price": 998700000000,
            "volume": 3000000,
            "openVolume": 3000000,
            "clientRequestId": null,
            "trades": []
        },
        {
            "id": 702590,
            "currency": "AUD",
            "instrument": "BTC",
            "orderSide": "Ask",
            "ordertype": "Limit",
            "creationTime": 1531518897518,
            "status": "Placed",
            "errorMessage": null,
            "price": 889800000000,
            "volume": 4000000,
            "openVolume": 4000000,
            "clientRequestId": null,
            "trades": []
        }
    ]
}
``` 

## Open all orders

sample request: `/v2/order/open`

sample response:
```json
{
    "success": true,
    "errorCode": null,
    "errorMessage": null,
    "orders": [
        {
            "id": 743363,
            "currency": "AUD",
            "instrument": "BTC",
            "orderSide": "Ask",
            "ordertype": "Limit",
            "creationTime": 1535659048351,
            "status": "Placed",
            "errorMessage": null,
            "price": 930706000000,
            "volume": 8404360,
            "openVolume": 8404360,
            "clientRequestId": null,
            "trades": []
        },
        {
            "id": 743565,
            "currency": "AUD",
            "instrument": "ETH",
            "orderSide": "Bid",
            "ordertype": "Limit",
            "creationTime": 1535660328066,
            "status": "Placed",
            "errorMessage": null,
            "price": 34791000000,
            "volume": 363507743,
            "openVolume": 363507743,
            "clientRequestId": null,
            "trades": []
        }
    ]
}

```

## Cancel all orders
This method cancels all open orders for all markets or a specific markets (if `marketIds` parameter is provided as request body)

http POST

path: `/v2/order/cancelall`

If you want to cancel open orders for specific markets only, then please pass the following as the request body:
```json
{
  "marketIds": ["BTC-AUD", "XRP-AUD"] 	
}
```

sample response:

```json
{"success":true,"errorCode":null,"errorMessage":null,"orderIds":[3929899238,3929899017,3929705536]}
```
The response includes orderIds for which cancellation has been requested. 

API authentication note: When calling this POST method and if no `marketIds` is provided then `string to sign` parameter would look like below (there should be an extra `\n` after the timestamp as per below) 
```json
/v2/order/cancelall
1565207864688

```
 
If `marketIds` is provided then `string to sign` parameter would look like below:
```json
/v2/order/cancelall
1565207864688
{"marketIds":["BTC-AUD"]}
```


## Order History

http GET

path: `/v2/order/history/{instrument}/{currency}`

url parameters:
* `indexForward`: Set to `true` to see orders more recent than the orderId in the `since` parameter, if a `since` parameter is used. Default is `false`. 
* `limit`: Number of results to return per "page". If not provided, default is 200.
* `since`: an orderId. If provided, and `indexForward` is `false`, returned results will be trades earlier than the trade id provided, non-inclusive. If `indexForward` is `true`, returned results will be trades after the orderId provided, non-inclusive.

pagination: yes

sample request: `/v2/order/history/BTC/AUD?limit=3&since=701336`

sample response: 
```json
{
    "success": true,
    "errorCode": null,
    "errorMessage": null,
    "orders": [
        {
            "id": 701335,
            "currency": "AUD",
            "instrument": "BTC",
            "orderSide": "Ask",
            "ordertype": "Limit",
            "creationTime": 1525903561732,
            "status": "Fully Matched",
            "errorMessage": null,
            "price": 1000000000,
            "volume": 100000000,
            "openVolume": 0,
            "clientRequestId": null,
            "trades": [
                {
                    "id": 701347,
                    "creationTime": 1525903561932,
                    "description": null,
                    "price": 2600000000,
                    "volume": 100000000,
                    "side": "Ask",
                    "fee": 22099974,
                    "orderId": 701335
                }
            ]
        },
        {
            "id": 701308,
            "currency": "AUD",
            "instrument": "BTC",
            "orderSide": "Ask",
            "ordertype": "Limit",
            "creationTime": 1525903341150,
            "status": "Fully Matched",
            "errorMessage": null,
            "price": 1000000000,
            "volume": 100000000,
            "openVolume": 0,
            "clientRequestId": null,
            "trades": [
                {
                    "id": 701332,
                    "creationTime": 1525903341371,
                    "description": null,
                    "price": 2600000000,
                    "volume": 90000000,
                    "side": "Ask",
                    "fee": 19889976,
                    "orderId": 701308
                },
                {
                    "id": 701321,
                    "creationTime": 1525903341349,
                    "description": null,
                    "price": 2700000000,
                    "volume": 10000000,
                    "side": "Ask",
                    "fee": 2294997,
                    "orderId": 701308
                }
            ]
        },
        {
            "id": 701208,
            "currency": "AUD",
            "instrument": "BTC",
            "orderSide": "Bid",
            "ordertype": "Limit",
            "creationTime": 1525899345980,
            "status": "Fully Matched",
            "errorMessage": null,
            "price": 2700000000,
            "volume": 100000000,
            "openVolume": 0,
            "clientRequestId": null,
            "trades": [
                {
                    "id": 701316,
                    "creationTime": 1525903341332,
                    "description": null,
                    "price": 2700000000,
                    "volume": 10000000,
                    "side": "Bid",
                    "fee": 2294997,
                    "orderId": 701208
                },
                {
                    "id": 701298,
                    "creationTime": 1525899507793,
                    "description": null,
                    "price": 2700000000,
                    "volume": 90000000,
                    "side": "Bid",
                    "fee": 20654975,
                    "orderId": 701208
                }
            ]
        }
    ],
    "paging": {
        "newer": "/v2/order/history/BTC/AUD?limit=3&since=701335&indexForward=true",
        "older": "/v2/order/history/BTC/AUD?limit=3&since=701208&indexForward=false"
    }
}
```
## Trade History

http GET

path: `/v2/order/trade/history/{instrument}/{currency}`

url parameters:
* `indexForward`: Set to `true` to see orders more recent than the tradeId in the `since` parameter, if a `since` parameter is used. Default is `false`. 
* `limit`: Number of results to return per "page". If not provided, default is 200.
* `since`: an tradeId. If provided, and `indexForward` is `false`, returned results will be trades earlier than the trade id provided, non-inclusive. If `indexForward` is `true`, returned results will be trades after the tradeId provided, non-inclusive.

pagination: yes

sample request: `/v2/order/trade/history/BTC/AUD?limit=4&since=701333`

sample response: 
```json
{
    "success": true,
    "errorCode": null,
    "errorMessage": null,
    "trades": [
        {
            "id": 701332,
            "creationTime": 1525903341371,
            "description": null,
            "price": 2600000000,
            "volume": 90000000,
            "side": "Ask",
            "fee": 19889976,
            "orderId": 701308
        },
        {
            "id": 701321,
            "creationTime": 1525903341349,
            "description": null,
            "price": 2700000000,
            "volume": 10000000,
            "side": "Ask",
            "fee": 2294997,
            "orderId": 701308
        },
        {
            "id": 701316,
            "creationTime": 1525903341332,
            "description": null,
            "price": 2700000000,
            "volume": 10000000,
            "side": "Bid",
            "fee": 2294997,
            "orderId": 701208
        },
        {
            "id": 701298,
            "creationTime": 1525899507793,
            "description": null,
            "price": 2700000000,
            "volume": 90000000,
            "side": "Bid",
            "fee": 20654975,
            "orderId": 701208
        }
    ],
    "paging": {
        "newer": "/v2/order/trade/history/BTC/AUD?limit=4&since=701332&indexForward=true",
        "older": "/v2/order/trade/history/BTC/AUD?limit=4&since=701298&indexForward=false"
    }
}
```