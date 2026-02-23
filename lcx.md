# Lcx API Documentation

Auto-fetched from 1 page(s)


---

# Source: https://docs.lcx.com/

  * Introduction
    * API Version
    * Rate Limiting
  * Authentication
  * SDKs
  * APIs
    * Market API
      * getOrder book
      * getKline (Candles)
      * getTrades
      * getPairs
      * getPair
      * getTickers
      * getTicker
    * Trading API
      * postNew order
      * putUpdate order
      * delCancel order
      * delCancel All orders
      * getOpen orders
      * getOrder
      * getOrders
      * getTrades
    * Account API
      * getBalances
      * getBalance
  * Websockets
    * Market Websocket
      * postSubscribe ticker
      * postSubscribe orderbook
      * postSubscribe trade
    * Trading Websocket
      * postSubscribe wallets
      * postSubscribe orders
      * postSubscribe trades
  * General
    * Errors
      * Message Errors
    * Release Notes



[API docs by Redocly](https://redocly.com/redoc/)

# LCX Exchange API Documentation (1.1.0)

Download OpenAPI specification:

LCX Customer Support: [hello@lcx.com](mailto:hello@lcx.com) [Terms of Service](https://www.lcx.com/terms-of-service/)

## [](#section/Introduction)Introduction

LCX, the Liechtenstein Cryptoassets Exchange, is a financial technology company that is pioneering blockchain infrastructure with a regulated approach. LCX API documentation consists of three parts: table of contents for easy browsing (left), explanation of each API interface (middle), and example code (right). 

The structure of LCX API is:

  * Unauthenticated API: return public information about markets and trades on LCX. Make calls to these endpoints without your API key and secret.

    * [Market data API](/#tag/Market-API): information about the state of the market on LCX.
  * Authenticated API: these private API enable account-specific interactions, such as placing and managing orders, viewing your account history or withdrawing assets. For these calls to succeed you must create your API key and secret and make Authenticated calls.

    * [Trading API](/#tag/Trading-API): manage your orders and trades on LCX.
    * [Account API](/#tag/Account-API) \- information about your LCX account.
  * Unauthenticated Websocket: subscribe to these channels and retrieve the latest information about market data in your Websocket callback.

    * [Market Websocket](/#tag/Market-Websocket) \- information about the state of the market on LCX.
  * Authenticated Websocket: private websocket subscription to retrieve the latest information about your trades and your account in your Websocket callback.

    * [Trading Websocket](/#tag/Trading-Websocket): manage your orders and trades on LCX.



Access LCX API using REST or Websocket. 

The Base URLs are:

API Base URL: <https://exchange-api.lcx.com/>

Websocket Base URL: wss://exchange-api.lcx.com/

LCX is hosted in the EU central (Frankfurt - Germany) and Liechtenstein region.

## [](#section/Introduction/API-Version)API Version

The current API version is 1.1.0 . Please include the following header in the request to get the correct API behaviors.

Header | Value  
---|---  
API-VERSION | 1.1.0  
  
> For those who are familiar with or prefer to reference the earlier version of our API, you can still access the previous documentation. This earlier version might be useful if youâre maintaining legacy systems or need information that was specific to that version. Please note that while we strive to keep the previous documentation updated, the most current features, updates, and support will be found in the latest version. 

> Access Previous Version Documentation: [LCX Exchange API v1 Documentation](https://exchange.lcx.com/v1/docs/#public-api)

## [](#section/Introduction/Rate-Limiting)Rate Limiting

Rate limiting restricts the number of requests made per IP address within a specific timeframe.

  * Market API, the maximum allowable rate is 25 requests per second per IP..
  * Trading API & Account API have a limit of 5 requests per second per IP and a maximum of 90 requests per minute per IP.



> **Warning** : Requests that exceed these limits will return with a 429 status code.

## [](#section/Authentication)Authentication

> Snippet for generating signature(x-access-sign)
    
    
    const CryptoJS = require('crypto-js')
    const axios = require('axios')
    let base_url = 'https://exchange-api.lcx.com'
    let end_point = '/api/create'
    let method = 'POST'
    let api = 'ADD YOUR LCX EXCHANGE API KEY'
    let secret = 'ADD YOUR LCX EXCHANGE SECRET KEY'
    const EXAMPLE_PAYLOAD = {
      OrderType: 'LIMIT',
      Pair: 'LCX/ETH',
      Side: 'BUY',
      Price: 0.03033486,
      Amount: 500,
    }
    // If No Payload, then it is important to pass empty object in EXAMPLE_PAYLOAD, ie. {}
    
    let requestString = method + end_point + JSON.stringify(EXAMPLE_PAYLOAD)
    let hash = CryptoJS.HmacSHA256(requestString, secret)
    let signature = CryptoJS.enc.Base64.stringify(hash)
    let headers = {
      'x-access-key': api,
      'x-access-sign': signature,
      'x-access-timestamp': Date.now(),
    }
    let url = base_url + end_point
    axios
      .post(url, JSON.stringify(EXAMPLE_PAYLOAD), { headers: headers })
      .then((result) => {
        console.log(result)
        // ... result
      })
      .catch((error) => {
        console.log(error)
        // ... error
      })
    

To use LCX Trading APIs, users are required to first gain authentication. LCX uses API keys to allow access to the API. You can register a new LCX API key at [LCX Exchange](http://exchange.lcx.com/).

LCX Exchange expects the API Secret key, signature and timestamp in milliseconds to be included as headers in all API requests to the server, which looks like the following:

  * `x-access-timestamp` \- Current timestamp in milliseconds
  * `x-access-key` \- Your LCX Exchange API Key
  * `x-access-sign` \- Signature signed by your LCX Exchange Secret Key



## [](#section/SDKs)SDKs

LCX SDKs let you execute advanced trading strategies from your app. All API endpoints are accessible through straightforward wrapper functions. Get market data, place orders, and manage your positions using REST or connect via WebSocket for real-time price updates and instant trade execution.

Available SDKs for integration:

  * [LCX SDK for Node.js](https://www.npmjs.com/package/lcx-sdk)



## [](#tag/Market-API)Market API

## [](#tag/Market-API/paths/~1api~1book/get)Order book

This endpoint returns the complete order book for a specified market.

##### query Parameters

pairrequired| string Name of the pair  
---|---  
  
### Responses

**200 **

Success

get/api/book

Exchange server

https://exchange-api.lcx.com/api/book

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = { pair: "LCX/ETH" };
    
    var config = {
      method: "get",
      url: "https://exchange-api.lcx.com/api/book",
      headers: {
        "Content-Type": "application/json",
      },
      params,
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": {
    * "buy": [
      * [
        * 0.022,

        * 3

],

      * [
        * 0.02,

        * 0

],

      * [
        * 0.018,

        * 2.1

]

],

    * "sell": [ ]

},

  * "message": "Successfully API response",

  * "status": "success"


}`

## [](#tag/Market-API/paths/~1v1~1market~1kline/get)Kline (Candles)

This endpoint provides OHLV (Open, High, Low, Close, and Volume) data for the specified market. It displays candles for the given market within a specified timeframe, from a starting timestamp to an ending timestamp (both in seconds)

##### query Parameters

pairrequired| string Name of the pair  
---|---  
resolutionrequired| string Enum: "1" "3" "5" "15" "30" "45" "60" "120" "180" "240" "1D" "1W" "1M" Timeframe  
fromrequired| integer <int64> From time in UTC timestamp in seconds  
torequired| integer <int64> To time in UTC timestamp in seconds  
  
### Responses

**200 **

Success

get/v1/market/kline

https://api-kline.lcx.com/v1/market/kline

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = {
      pair: "ETH/BTC",
      resolution: "60",
      from: 1608129416,
      to: 1608229416,
    };
    
    var config = {
      method: "get",
      url: "https://api-kline.lcx.com/v1/market/kline",
      headers: {
        "Content-Type": "application/json",
      },
      params,
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "count": 3,

  * "data": [
    * {
      * "close": 1.022,

      * "high": 0.022,

      * "low": 0.021,

      * "open": 0.021,

      * "pair": "ETH/BTC",

      * "timeframe": "60",

      * "timestamp": 1605722400000,

      * "volume": 10

},

    * {
      * "close": 0.022,

      * "high": 0.022,

      * "low": 0.02,

      * "open": 0.021,

      * "pair": "ETH/BTC",

      * "timeframe": "60",

      * "timestamp": 1605700800000,

      * "volume": 20.8

},

    * {
      * "close": 0.021,

      * "high": 0.021,

      * "low": 0.02,

      * "open": 0.02,

      * "pair": "ETH/BTC",

      * "timeframe": "60",

      * "timestamp": 1605697200000,

      * "volume": 10.5

}

],

  * "message": "Successfully Api response",

  * "status": "success"


}`

## [](#tag/Market-API/paths/~1api~1trades/get)Trades

This endpoint enables retrieval of past public trades, providing details such as price, size, and time for each trade.

##### query Parameters

pairrequired| string Example: pair=LCX/USDCName of the pair  
---|---  
offsetrequired| integer Example: offset=1Page index, first page = 1, fixed page size = 100  
  
### Responses

**200 **

Success

get/api/trades

Exchange server

https://exchange-api.lcx.com/api/trades

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = { offset: 1, pair: "ETH/BTC" };
    
    var config = {
      method: "get",
      url: "https://exchange-api.lcx.com/api/trades",
      headers: {
        "Content-Type": "application/json",
      },
      params,
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": [
    * [
      * 0.022,

      * 0.01,

      * "SELL",

      * 1605725835

],

    * [
      * 0.021,

      * 0,

      * "BUY",

      * 1605722975

],

    * [
      * 0.022,

      * 0.1,

      * "BUY",

      * 1605703939

],

    * [
      * 0.02,

      * 1,

      * "SELL",

      * 1605703035

],

    * [
      * 0.02,

      * 0.7,

      * "SELL",

      * 1605703035

],

    * [
      * 0.021,

      * 1,

      * "BUY",

      * 1605702910

],

    * [
      * 0.021,

      * 0.2,

      * "BUY",

      * 1605697822

],

    * [
      * 0.02,

      * 0.3,

      * "SELL",

      * 1605697754

]

],

  * "message": "Successfully Api response",

  * "status": "success"


}`

## [](#tag/Market-API/paths/~1api~1pairs/get)Pairs

This endpoint provides access to details of all trading pairs available on the exchange platform.

### Responses

**200 **

Success

get/api/pairs

Exchange server

https://exchange-api.lcx.com/api/pairs

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require('axios')
    
    var config = {
      method: 'get',
      url: 'https://exchange-api.lcx.com/api/pairs',
      headers: {
        'Content-Type': 'application/json',
      },
    }
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data))
      })
      .catch(function (error) {
        console.log(error)
      })
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": [
    * {
      * "Id": "a08ed90e-654c-4395-8605-1599a2e8e7f6",

      * "Symbol": "POLK/BTC",

      * "Base": "POLK",

      * "Quote": "BTC",

      * "Precision": {
        * "Amount": 8,

        * "Price": 8,

        * "Total": 0

},

      * "Orderprecision": {
        * "Amount": 8,

        * "Price": 8,

        * "Total": 8

},

      * "MinOrder": {
        * "Base": 0.01,

        * "Quote": 0.00001

},

      * "MaxOrder": {
        * "Base": 1000,

        * "Quote": 1

},

      * "Status": false,

      * "CreatedAt": "2021-04-10T16:31:46.863+05:30",

      * "UpdatedAt": "2021-04-10T16:31:46.863+05:30",

      * "ListingPrice": 0,

      * "Mode": "trade"

}

],

  * "message": "Successfully API Response",

  * "status": "success"


}`

## [](#tag/Market-API/paths/~1api~1pair/get)Pair

This endpoint allows retrieval of details for a given trading pair available on the exchange platform.

##### query Parameters

pairrequired| string Example: pair=LCX/USDCName of the pair  
---|---  
  
### Responses

**200 **

Success

get/api/pair

Exchange server

https://exchange-api.lcx.com/api/pair

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = { pair: "ETH/BTC" };
    
    var config = {
      method: "get",
      url: "https://exchange-api.lcx.com/api/pair",
      params,
      headers: {
        "Content-Type": "application/json",
      },
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": {
    * "Id": "faafceb6-fd61-4924-8258-68aa83a196cf",

    * "Symbol": "LCX/USDC",

    * "Base": "LCX",

    * "Quote": "USDC",

    * "Precision": {
      * "Amount": 4,

      * "Price": 4,

      * "Total": 2

},

    * "Orderprecision": {
      * "Amount": 1,

      * "Price": 3,

      * "Total": 2

},

    * "MinOrder": {
      * "Base": 10,

      * "Quote": 0.05

},

    * "MaxOrder": {
      * "Base": 5000000,

      * "Quote": 1000000

},

    * "Status": true,

    * "CreatedAt": "2020-02-04T14:16:47+05:30",

    * "UpdatedAt": "2021-09-20T17:28:36.253+05:30",

    * "ListingPrice": 0,

    * "Mode": "trade"

},

  * "message": "Successfully API Response",

  * "status": "success"


}`

## [](#tag/Market-API/paths/~1api~1tickers/get)Tickers

This endpoint enables access to a comprehensive market overview, displaying current best bid and ask prices, the latest traded price, daily volume information, and details on the previous dayâs price movement. It efficiently retrieves multiple tickers with a single query, providing a holistic view of market data.

### Responses

**200 **

Success

get/api/tickers

Exchange server

https://exchange-api.lcx.com/api/tickers

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require('axios')
    
    var config = {
      method: 'get',
      url: 'https://exchange-api.lcx.com/api/tickers',
      headers: {
        'Content-Type': 'application/json',
      },
    }
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data))
      })
      .catch(function (error) {
        console.log(error)
      })
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": {
    * "ADA/LCX": {
      * "bestAsk": 7.8925,

      * "bestBid": 7.6924,

      * "change": -4.3,

      * "chart": [
        * {
          * "Time": 1700024400,

          * "Close": 7.7925

},

        * {
          * "Time": 1700020800,

          * "Close": 7.8514

},

        * {
          * "Time": 1700017200,

          * "Close": 8.2537

},

        * {
          * "Time": 1700013600,

          * "Close": 8.0844

},

        * {
          * "Time": 1700010000,

          * "Close": 8.1701

},

        * {
          * "Time": 1700006400,

          * "Close": 8.2743

},

        * {
          * "Time": 1700002800,

          * "Close": 8.4127

},

        * {
          * "Time": 1699999200,

          * "Close": 8.3796

},

        * {
          * "Time": 1699995600,

          * "Close": 8.4039

},

        * {
          * "Time": 1699992000,

          * "Close": 8.3183

},

        * {
          * "Time": 1699988400,

          * "Close": 8.3666

},

        * {
          * "Time": 1699984800,

          * "Close": 8.0046

},

        * {
          * "Time": 1699981200,

          * "Close": 8.2899

},

        * {
          * "Time": 1699977600,

          * "Close": 8.6266

},

        * {
          * "Time": 1699974000,

          * "Close": 8.444

},

        * {
          * "Time": 1699970400,

          * "Close": 8.673

},

        * {
          * "Time": 1699966800,

          * "Close": 8.6643

},

        * {
          * "Time": 1699963200,

          * "Close": 8.3803

},

        * {
          * "Time": 1699959600,

          * "Close": 8.3819

},

        * {
          * "Time": 1699945200,

          * "Close": 8.3677

},

        * {
          * "Time": 1699941600,

          * "Close": 8.4355

},

        * {
          * "Time": 1699938000,

          * "Close": 8.5026

},

        * {
          * "Time": 1699938000,

          * "Close": 8.1423

}

],

      * "equivalent": 0.35996277,

      * "high": 8.68,

      * "last24Price": 8.1423,

      * "lastPrice": 7.7925,

      * "lastUpdated": 1700025221,

      * "low": 7.7616,

      * "symbol": "ADA/LCX",

      * "usdVolume": 1828.49928314,

      * "volume": 5079.69

},

    * "BTC/EUR": {
      * "bestAsk": 32762.6,

      * "bestBid": 32705.3,

      * "change": -3.84,

      * "chart": [
        * {
          * "Time": 1700024400,

          * "Close": 32727.7

},

        * {
          * "Time": 1700020800,

          * "Close": 32661.6

},

        * {
          * "Time": 1700017200,

          * "Close": 32563.4

},

        * {
          * "Time": 1699995600,

          * "Close": 32741.7

},

        * {
          * "Time": 1699992000,

          * "Close": 32535.6

},

        * {
          * "Time": 1699988400,

          * "Close": 32506

},

        * {
          * "Time": 1699984800,

          * "Close": 32495.2

},

        * {
          * "Time": 1699981200,

          * "Close": 33218.2

},

        * {
          * "Time": 1699977600,

          * "Close": 33444.2

},

        * {
          * "Time": 1699974000,

          * "Close": 33381.8

},

        * {
          * "Time": 1699970400,

          * "Close": 33960.2

},

        * {
          * "Time": 1699966800,

          * "Close": 33913.6

},

        * {
          * "Time": 1699963200,

          * "Close": 33958.8

},

        * {
          * "Time": 1699959600,

          * "Close": 33942.8

},

        * {
          * "Time": 1699956000,

          * "Close": 34046.8

},

        * {
          * "Time": 1699952400,

          * "Close": 34085.8

},

        * {
          * "Time": 1699948800,

          * "Close": 34309.4

},

        * {
          * "Time": 1699945200,

          * "Close": 34245.7

},

        * {
          * "Time": 1699941600,

          * "Close": 34299.5

},

        * {
          * "Time": 1699938000,

          * "Close": 34130.6

},

        * {
          * "Time": 1699938000,

          * "Close": 34021.6

}

],

      * "equivalent": 35615.97771259,

      * "high": 34361.8,

      * "last24Price": 34033.3,

      * "lastPrice": 32727.7,

      * "lastUpdated": 1700025075,

      * "low": 32400.2,

      * "symbol": "BTC/EUR",

      * "usdVolume": 60976.33464283,

      * "volume": 1.71205

},

    * "ETH/BTC": {
      * "bestAsk": 0.05672,

      * "bestBid": 0.05471,

      * "change": -0.89,

      * "chart": [
        * {
          * "Time": 1699999200,

          * "Close": 0.05579

},

        * {
          * "Time": 1699995600,

          * "Close": 0.05571

},

        * {
          * "Time": 1699992000,

          * "Close": 0.05607

},

        * {
          * "Time": 1699988400,

          * "Close": 0.056

},

        * {
          * "Time": 1699984800,

          * "Close": 0.05579

},

        * {
          * "Time": 1699981200,

          * "Close": 0.05615

},

        * {
          * "Time": 1699977600,

          * "Close": 0.05638

},

        * {
          * "Time": 1699974000,

          * "Close": 0.05643

},

        * {
          * "Time": 1699970400,

          * "Close": 0.05602

},

        * {
          * "Time": 1699966800,

          * "Close": 0.05595

},

        * {
          * "Time": 1699959600,

          * "Close": 0.05607

},

        * {
          * "Time": 1699956000,

          * "Close": 0.05611

},

        * {
          * "Time": 1699952400,

          * "Close": 0.05611

},

        * {
          * "Time": 1699948800,

          * "Close": 0.05611

},

        * {
          * "Time": 1699945200,

          * "Close": 0.05616

},

        * {
          * "Time": 1699941600,

          * "Close": 0.05611

},

        * {
          * "Time": 1699938000,

          * "Close": 0.05633

},

        * {
          * "Time": 1699938000,

          * "Close": 0.05629

}

],

      * "equivalent": 1985.62189,

      * "high": 0.05813,

      * "last24Price": 0.05629,

      * "lastPrice": 0.05579,

      * "lastUpdated": 1699999866,

      * "low": 0.05558,

      * "symbol": "ETH/BTC",

      * "usdVolume": 2489.96985005,

      * "volume": 1.254

},

    * "ETH/EUR": {
      * "bestAsk": 1824.6907,

      * "bestBid": 1822.1384,

      * "change": -5.33,

      * "chart": [
        * {
          * "Time": 1700024400,

          * "Close": 1823.1045

},

        * {
          * "Time": 1700020800,

          * "Close": 1822.9794

},

        * {
          * "Time": 1700017200,

          * "Close": 1814.6938

},

        * {
          * "Time": 1700013600,

          * "Close": 1817.0933

},

        * {
          * "Time": 1700010000,

          * "Close": 1819.4888

},

        * {
          * "Time": 1700006400,

          * "Close": 1826.9303

},

        * {
          * "Time": 1700002800,

          * "Close": 1822.7444

},

        * {
          * "Time": 1699999200,

          * "Close": 1831.3464

},

        * {
          * "Time": 1699995600,

          * "Close": 1824.9698

},

        * {
          * "Time": 1699992000,

          * "Close": 1818.5436

},

        * {
          * "Time": 1699988400,

          * "Close": 1820.364

},

        * {
          * "Time": 1699984800,

          * "Close": 1810.1169

},

        * {
          * "Time": 1699981200,

          * "Close": 1865.718

},

        * {
          * "Time": 1699977600,

          * "Close": 1884.9719

},

        * {
          * "Time": 1699974000,

          * "Close": 1882.0813

},

        * {
          * "Time": 1699970400,

          * "Close": 1895.7191

},

        * {
          * "Time": 1699966800,

          * "Close": 1893.6909

},

        * {
          * "Time": 1699963200,

          * "Close": 1895.514

},

        * {
          * "Time": 1699959600,

          * "Close": 1899.3347

},

        * {
          * "Time": 1699956000,

          * "Close": 1911.9563

},

        * {
          * "Time": 1699952400,

          * "Close": 1915.1223

},

        * {
          * "Time": 1699948800,

          * "Close": 1930.2159

},

        * {
          * "Time": 1699945200,

          * "Close": 1927.7655

},

        * {
          * "Time": 1699941600,

          * "Close": 1925.595

},

        * {
          * "Time": 1699938000,

          * "Close": 1934.5607

}

],

      * "equivalent": 1983.99671347,

      * "high": 1934.5907,

      * "last24Price": 1925.705,

      * "lastPrice": 1823.1045,

      * "lastUpdated": 1700025080,

      * "low": 1797.3294,

      * "symbol": "ETH/EUR",

      * "usdVolume": 310027.26243367,

      * "volume": 156.264

},

    * "HBAR/LCX": {
      * "bestAsk": 1.2929,

      * "bestBid": 1.2668,

      * "change": -5.16,

      * "chart": [
        * {
          * "Time": 1700024400,

          * "Close": 1.2798

},

        * {
          * "Time": 1700020800,

          * "Close": 1.2869

},

        * {
          * "Time": 1700017200,

          * "Close": 1.3569

},

        * {
          * "Time": 1700013600,

          * "Close": 1.3317

},

        * {
          * "Time": 1700010000,

          * "Close": 1.3523

},

        * {
          * "Time": 1700006400,

          * "Close": 1.3679

},

        * {
          * "Time": 1700002800,

          * "Close": 1.3765

},

        * {
          * "Time": 1699999200,

          * "Close": 1.3648

},

        * {
          * "Time": 1699995600,

          * "Close": 1.3643

},

        * {
          * "Time": 1699992000,

          * "Close": 1.3613

},

        * {
          * "Time": 1699988400,

          * "Close": 1.3948

},

        * {
          * "Time": 1699984800,

          * "Close": 1.3541

},

        * {
          * "Time": 1699981200,

          * "Close": 1.3614

},

        * {
          * "Time": 1699977600,

          * "Close": 1.404

},

        * {
          * "Time": 1699974000,

          * "Close": 1.3814

},

        * {
          * "Time": 1699970400,

          * "Close": 1.397

},

        * {
          * "Time": 1699966800,

          * "Close": 1.4097

},

        * {
          * "Time": 1699963200,

          * "Close": 1.3731

},

        * {
          * "Time": 1699959600,

          * "Close": 1.3556

},

        * {
          * "Time": 1699956000,

          * "Close": 1.378

},

        * {
          * "Time": 1699952400,

          * "Close": 1.4088

},

        * {
          * "Time": 1699948800,

          * "Close": 1.3983

},

        * {
          * "Time": 1699945200,

          * "Close": 1.3936

},

        * {
          * "Time": 1699941600,

          * "Close": 1.3882

},

        * {
          * "Time": 1699938000,

          * "Close": 1.4022

}

],

      * "equivalent": 0.05911842,

      * "high": 1.4097,

      * "last24Price": 1.3494,

      * "lastPrice": 1.2798,

      * "lastUpdated": 1700025177,

      * "low": 1.2798,

      * "symbol": "HBAR/LCX",

      * "usdVolume": 128.0623214,

      * "volume": 2166.2

},

    * "OP/LCX": {
      * "bestAsk": 40.26,

      * "bestBid": 39.99,

      * "change": 1.95,

      * "chart": [
        * {
          * "Time": 1700020800,

          * "Close": 41.78

},

        * {
          * "Time": 1700017200,

          * "Close": 41.8

},

        * {
          * "Time": 1700013600,

          * "Close": 40.72

},

        * {
          * "Time": 1700010000,

          * "Close": 41.34

},

        * {
          * "Time": 1700006400,

          * "Close": 42.16

},

        * {
          * "Time": 1700002800,

          * "Close": 42.2

},

        * {
          * "Time": 1699999200,

          * "Close": 42.14

},

        * {
          * "Time": 1699995600,

          * "Close": 41.47

},

        * {
          * "Time": 1699992000,

          * "Close": 40.89

},

        * {
          * "Time": 1699988400,

          * "Close": 40.8

},

        * {
          * "Time": 1699984800,

          * "Close": 40.03

},

        * {
          * "Time": 1699981200,

          * "Close": 40.66

},

        * {
          * "Time": 1699977600,

          * "Close": 42.11

},

        * {
          * "Time": 1699974000,

          * "Close": 41.14

},

        * {
          * "Time": 1699970400,

          * "Close": 42.03

},

        * {
          * "Time": 1699966800,

          * "Close": 41

},

        * {
          * "Time": 1699963200,

          * "Close": 40.59

}

],

      * "equivalent": 1.92996401,

      * "high": 42.92,

      * "last24Price": 40.98,

      * "lastPrice": 41.78,

      * "lastUpdated": 1700020845,

      * "low": 39.99,

      * "symbol": "OP/LCX",

      * "usdVolume": 825.87019915,

      * "volume": 427.92

}

},

  * "message": "Tickers fetched successfully",

  * "status": "success"


}`

## [](#tag/Market-API/paths/~1api~1ticker/get)Ticker

This endpoint enables a comprehensive market overview for a specified pair, showcasing current best bid and ask prices, the latest traded price, daily volume details, and the previous dayâs price movement.

##### query Parameters

pairrequired| string Example: pair=LCX/USDCName of the pair  
---|---  
  
### Responses

**200 **

Success

get/api/ticker

Exchange server

https://exchange-api.lcx.com/api/ticker

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = { pair: "ETH/BTC" };
    
    var config = {
      method: "post",
      url: "https://exchange-api.lcx.com/api/ticker",
      headers: {
        "Content-Type": "application/json",
      },
      params,
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data))
      })
      .catch(function (error) {
        console.log(error)
      })
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": {
    * "bestAsk": 7.8925,

    * "bestBid": 7.6924,

    * "change": -4.3,

    * "chart": [
      * {
        * "Time": 1700024400,

        * "Close": 7.7925

},

      * {
        * "Time": 1700020800,

        * "Close": 7.8514

},

      * {
        * "Time": 1700017200,

        * "Close": 8.2537

},

      * {
        * "Time": 1700013600,

        * "Close": 8.0844

},

      * {
        * "Time": 1700010000,

        * "Close": 8.1701

},

      * {
        * "Time": 1700006400,

        * "Close": 8.2743

},

      * {
        * "Time": 1700002800,

        * "Close": 8.4127

},

      * {
        * "Time": 1699999200,

        * "Close": 8.3796

},

      * {
        * "Time": 1699995600,

        * "Close": 8.4039

},

      * {
        * "Time": 1699992000,

        * "Close": 8.3183

},

      * {
        * "Time": 1699988400,

        * "Close": 8.3666

}

],

    * "equivalent": 0.35996277,

    * "high": 8.68,

    * "last24Price": 8.1423,

    * "lastPrice": 7.7925,

    * "lastUpdated": 1700025221,

    * "low": 7.7616,

    * "symbol": "ADA/LCX",

    * "usdVolume": 1828.49928314,

    * "volume": 5079.69

},

  * "message": "Tickers fetched successfully",

  * "status": "success"


}`

## [](#tag/Trading-API)Trading API

## [](#tag/Trading-API/paths/~1api~1create/post)New order

The Create an Order endpoint enables you to create buy/sell orders on limit/market on LCX Exchange.

##### Authorizations:

(_API Key_ _Signature_ _Timestamp_) 

##### Request Body schema: application/json

required

Pairrequired| string Name of the Pair  
---|---  
Amountrequired| float Specifies the amount of the base asset that will be bought/sold.  
Price| float Only for limit orders: Specifies the amount in quote currency that is paid/received for each unit of base currency.  
OrderTyperequired| string Enum: "LIMIT" "MARKET" For limit orders, amount and price are required. For market orders, either amount is required.  
Siderequired| string Enum: "SELL" "BUY" When placing a buy order the base currency will be bought for the quote currency. When placing a sell order the base currency will be sold for the quote currency  
ClientOrderId| string <uuid> A custom-generated UUID in the request uniquely identifies each request and maps it to the WebSocket response. If the ClientOrderId key is not provided, the backend will automatically generate a UUID for it.  
  
### Responses

**200 **

Success

post/api/create

Exchange server

https://exchange-api.lcx.com/api/create

###  Request samples

  * Payload
  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Content type

application/json

Copy

`{

  * "Pair": "LCX/ETH",

  * "Amount": 100,

  * "Price": 0.004,

  * "OrderType": "MARKET",

  * "Side": "SELL"


}`

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": {
    * "Tx": null,

    * "Id": "3dae4495-a219-40dc-99d8-99c49c1d3810",

    * "Pair": "AVAX/USDC",

    * "BasePair": "",

    * "QuotePair": "",

    * "Price": 1,

    * "Amount": 10,

    * "Side": "SELL",

    * "OrderType": "LIMIT",

    * "Status": "OPEN",

    * "Filled": 0,

    * "Average": 1,

    * "Total": 0,

    * "CreatedAt": 1699955183,

    * "UpdatedAt": 1699955183,

    * "UserId": "7d83f7c6-8b51-4388-bd4d-e2e5241fd253",

    * "Fee": 0,

    * "IsFeeInLCX": true,

    * "FeeLevel": 0,

    * "FilledPer": 0,

    * "User": {
      * "Id": "",

      * "EmailId": "",

      * "LastName": "",

      * "FirstName": "",

      * "FeeInLCX": false,

      * "FeeLevel": 0,

      * "Status": false,

      * "Country": "",

      * "Referral_UserId": "",

      * "ReferralStatus": false,

      * "CreatedAt": "0001-01-01T00:00:00Z",

      * "UpdatedAt": "0001-01-01T00:00:00Z",

      * "Wallets": null,

      * "Trades": null

},

    * "Referral_UserId": "00000000-0000-0000-0000-000000000000",

    * "ClientOrderId": "00000000-0000-0000-0000-000000000000"

},

  * "message": "Order created successfully",

  * "status": "success"


}`

## [](#tag/Trading-API/paths/~1api~1modify/put)Update order

This endpoint facilitates updates for any limit buy/sell orders.

##### Authorizations:

(_API Key_ _Signature_ _Timestamp_) 

##### Request Body schema: application/json

required

OrderIdrequired| string Specify only open order ID for updates. Partial orders cannot be modified.  
---|---  
Amountrequired| float Updates amount to this value.  
Pricerequired| float Specifies the amount in quote currency that is paid/received for each unit of base currency.  
  
### Responses

**200 **

Success

put/api/modify

Exchange server

https://exchange-api.lcx.com/api/modify

###  Request samples

  * Payload
  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Content type

application/json

Copy

`{

  * "OrderId": "9f898d18-0980-4fb3-b18c-eeb39fc20324",

  * "Amount": 100,

  * "Price": 0.004


}`

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": {
    * "Tx": null,

    * "Id": "1c78b774-4a96-495c-be74-0dcaf5101461",

    * "Pair": "LCX/EUR",

    * "BasePair": "",

    * "QuotePair": "",

    * "Price": 89.9,

    * "Amount": 10,

    * "Side": "BUY",

    * "OrderType": "LIMIT",

    * "Status": "OPEN",

    * "Filled": 0,

    * "Average": 89.9,

    * "Total": 0,

    * "CreatedAt": 1699270525,

    * "UpdatedAt": 1699526526,

    * "UserId": "7d83f7c6-8b51-4388-bd4d-e2e5241fd253",

    * "Fee": 0,

    * "IsFeeInLCX": true,

    * "FeeLevel": 0,

    * "FilledPer": 0,

    * "User": {
      * "Id": "",

      * "EmailId": "",

      * "LastName": "",

      * "FirstName": "",

      * "FeeInLCX": false,

      * "FeeLevel": 0,

      * "Status": false,

      * "Country": "",

      * "Referral_UserId": "",

      * "ReferralStatus": false,

      * "CreatedAt": "0001-01-01T00:00:00Z",

      * "UpdatedAt": "0001-01-01T00:00:00Z",

      * "Wallets": null,

      * "Trades": null

},

    * "Referral_UserId": "00000000-0000-0000-0000-000000000000",

    * "ClientOrderId": "00000000-0000-0000-0000-000000000000"

},

  * "message": "Order updated successfully",

  * "status": "success"


}`

## [](#tag/Trading-API/paths/~1api~1cancel/delete)Cancel order

This endpoint enables the cancellation of exchange orders using their corresponding Order Id.

##### Authorizations:

(_API Key_ _Signature_ _Timestamp_) 

##### query Parameters

orderIdrequired| string String specifying which order should be updated  
---|---  
  
### Responses

**200 **

Success

delete/api/cancel

Exchange server

https://exchange-api.lcx.com/api/cancel

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = { orderId: "e8737c4a-3804-461c-9e67-4fe0af5aeb06" };
    
    var config = {
      method: "delete",
      url: "https://exchange-api.lcx.com/api/cancel",
      headers: {
        // auth headers
      },
      params,
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": {
    * "Tx": null,

    * "Id": "bb6fc517-9d0b-4c8c-a913-4f6aa8e2d25c",

    * "Pair": "LCX/EUR",

    * "BasePair": "",

    * "QuotePair": "",

    * "Price": 88.5,

    * "Amount": 10,

    * "Side": "BUY",

    * "OrderType": "LIMIT",

    * "Status": "CANCEL",

    * "Filled": 0,

    * "Average": 88.5,

    * "Total": 0,

    * "CreatedAt": 1699270447,

    * "UpdatedAt": 1699525860,

    * "UserId": "7d83f7c6-8b51-4388-bd4d-e2e5241fd253",

    * "Fee": 0,

    * "IsFeeInLCX": false,

    * "FeeLevel": 0,

    * "FilledPer": 0,

    * "User": {
      * "Id": "",

      * "EmailId": "",

      * "LastName": "",

      * "FirstName": "",

      * "FeeInLCX": false,

      * "FeeLevel": 0,

      * "Status": false,

      * "Country": "",

      * "Referral_UserId": "",

      * "ReferralStatus": false,

      * "CreatedAt": "0001-01-01T00:00:00Z",

      * "UpdatedAt": "0001-01-01T00:00:00Z",

      * "Wallets": null,

      * "Trades": null

},

    * "Referral_UserId": "00000000-0000-0000-0000-000000000000",

    * "ClientOrderId": "00000000-0000-0000-0000-000000000000"

},

  * "message": "Order removed successfully",

  * "status": "success"


}`

## [](#tag/Trading-API/paths/~1order~1cancel-all/delete)Cancel All orders

Cancel a list of orders by order Ids

##### Authorizations:

(_API Key_ _Signature_ _Timestamp_) 

##### query Parameters

orderIdsrequired| Array of strings Example: orderIds=70aba300-0990-481d-ad76-7bd499f473ab&orderIds=ecaf000a-8f4c-459a-b105-784c0e0436dfList of order ids. Maximum of 25 orders can be deleted at once.  
---|---  
  
### Responses

**200 **

Success

delete/order/cancel-all

Exchange server

https://exchange-api.lcx.com/order/cancel-all

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = {
      orderIds: [
        "70aba300-0990-481d-ad76-7bd499f473ab",
        "ecaf000a-8f4c-459a-b105-784c0e0436df",
      ],
    };
    
    const transformRequestOptions = (params) => {
      let options = "";
      for (const key in params) {
        if (typeof params[key] !== "object" && params[key]) {
          options += `${key}=${params[key]}&`;
        } else if (
          typeof params[key] === "object" &&
          params[key] &&
          params[key].length
        ) {
          params[key].forEach((el) => {
            options += `${key}=${el}&`;
          });
        }
      }
      return options ? options.slice(0, -1) : options;
    };
    
    var config = {
      method: "delete",
      url: "https://exchange-api.lcx.com/order/cancel-all",
      headers: {
        // auth headers
      },
      params,
      paramsSerializer: (params) => transformRequestOptions(params),
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

`{

  * "message": "2 orders cancelled successfully",

  * "status": "success"


}`

## [](#tag/Trading-API/paths/~1api~1open/get)Open orders

This endpoint grants access to all pending orders that are ready for execution.

##### Authorizations:

(_API Key_ _Signature_ _Timestamp_) 

##### query Parameters

offsetrequired| integer Example: offset=1Page index, first page = 1, fixed page size = 100  
---|---  
pair| string Example: pair=LCX/USDCName of the pair  
fromDate| integer Example: fromDate=1689193800Integer specifying from (i.e. showing those later in time) which time all orders should be returned. Should be a timestamp in milliseconds since 1 Jan 1970.  
toDate| integer Example: toDate=1689193800Integer specifying up to (i.e. showing those earlier in time) which time all orders should be returned. Should be a timestamp in milliseconds since 1 Jan 1970.  
  
### Responses

**200 **

Success

get/api/open

Exchange server

https://exchange-api.lcx.com/api/open

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = { pair: "ETH/BTC", offset: 1 };
    
    var config = {
      method: "get",
      url: "https://exchange-api.lcx.com/api/open",
      headers: {
        // auth headers
      },
      params,
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": [
    * {
      * "Tx": null,

      * "Id": "bb6fc517-9d0b-4c8c-a913-4f6aa8e2d25c",

      * "Pair": "LCX/EUR",

      * "BasePair": "",

      * "QuotePair": "",

      * "Price": 88.5,

      * "Amount": 10,

      * "Side": "BUY",

      * "OrderType": "LIMIT",

      * "Status": "OPEN",

      * "Filled": 0,

      * "Average": 0,

      * "Total": 0,

      * "CreatedAt": 0,

      * "UpdatedAt": 1699525860,

      * "UserId": "7d83f7c6-8b51-4388-bd4d-e2e5241fd253",

      * "Fee": 0,

      * "IsFeeInLCX": false,

      * "FeeLevel": 0,

      * "FilledPer": 0,

      * "User": {
        * "Id": "",

        * "EmailId": "",

        * "LastName": "",

        * "FirstName": "",

        * "FeeInLCX": false,

        * "FeeLevel": 0,

        * "Status": false,

        * "Country": "",

        * "Referral_UserId": "",

        * "ReferralStatus": false,

        * "CreatedAt": "0001-01-01T00:00:00Z",

        * "UpdatedAt": "0001-01-01T00:00:00Z",

        * "Wallets": null,

        * "Trades": null

},

      * "Referral_UserId": "00000000-0000-0000-0000-000000000000",

      * "ClientOrderId": "00000000-0000-0000-0000-000000000000"

},

    * {
      * "Tx": null,

      * "Id": "b2109151-0650-4ea9-92ce-120bf535026f",

      * "Pair": "LCX/EUR",

      * "BasePair": "",

      * "QuotePair": "",

      * "Price": 16.4,

      * "Amount": 10,

      * "Side": "BUY",

      * "OrderType": "LIMIT",

      * "Status": "OPEN",

      * "Filled": 0,

      * "Average": 0,

      * "Total": 0,

      * "CreatedAt": 0,

      * "UpdatedAt": 1699270439,

      * "UserId": "7d83f7c6-8b51-4388-bd4d-e2e5241fd253",

      * "Fee": 0,

      * "IsFeeInLCX": true,

      * "FeeLevel": 0,

      * "FilledPer": 0,

      * "User": {
        * "Id": "",

        * "EmailId": "",

        * "LastName": "",

        * "FirstName": "",

        * "FeeInLCX": false,

        * "FeeLevel": 0,

        * "Status": false,

        * "Country": "",

        * "Referral_UserId": "",

        * "ReferralStatus": false,

        * "CreatedAt": "0001-01-01T00:00:00Z",

        * "UpdatedAt": "0001-01-01T00:00:00Z",

        * "Wallets": null,

        * "Trades": null

},

      * "Referral_UserId": "00000000-0000-0000-0000-000000000000",

      * "ClientOrderId": "00000000-0000-0000-0000-000000000000"

}

],

  * "message": "Orders fetched successfully",

  * "status": "success",

  * "totalCount": 7


}`

## [](#tag/Trading-API/paths/~1api~1order/get)Order

This endpoint empowers users to retrieve detailed information for a specific order.

##### Authorizations:

(_API Key_ _Signature_ _Timestamp_) 

##### query Parameters

orderIdrequired| string String specifying which order should be fetched.  
---|---  
  
### Responses

**200 **

Success

get/api/order

Exchange server

https://exchange-api.lcx.com/api/order

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = { orderId: "e8737c4a-3804-461c-9e67-4fe0af5aeb06" };
    
    var config = {
      method: "get",
      url: "https://exchange-api.lcx.com/api/order",
      headers: {
        // auth headers
      },
      params,
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": {
    * "Tx": null,

    * "Id": "5121fe93-ee23-4805-9edb-194d428f71a3",

    * "Pair": "LINK/EUR",

    * "BasePair": "",

    * "QuotePair": "",

    * "Price": 6.11,

    * "Amount": 100,

    * "Side": "BUY",

    * "OrderType": "LIMIT",

    * "Status": "PARTIAL",

    * "Filled": 50,

    * "Average": 0,

    * "Total": 0,

    * "CreatedAt": 0,

    * "UpdatedAt": 1690372738,

    * "UserId": "7d83f7c6-8b51-4388-bd4d-e2e5241fd253",

    * "Fee": 0,

    * "IsFeeInLCX": true,

    * "FeeLevel": 0,

    * "FilledPer": 50,

    * "User": {
      * "Id": "",

      * "EmailId": "",

      * "LastName": "",

      * "FirstName": "",

      * "FeeInLCX": false,

      * "FeeLevel": 0,

      * "Status": false,

      * "Country": "",

      * "Referral_UserId": "",

      * "ReferralStatus": false,

      * "CreatedAt": "0001-01-01T00:00:00Z",

      * "UpdatedAt": "0001-01-01T00:00:00Z",

      * "Wallets": null,

      * "Trades": null

},

    * "Referral_UserId": "00000000-0000-0000-0000-000000000000",

    * "ClientOrderId": "00000000-0000-0000-0000-000000000000"

},

  * "message": "Order fetched successfully",

  * "status": "success"


}`

## [](#tag/Trading-API/paths/~1api~1orderHistory/get)Orders

This endpoint allows users to review previously closed or cancelled orders.

##### Authorizations:

(_API Key_ _Signature_ _Timestamp_) 

##### query Parameters

pair| string Example: pair=LCX/USDCName of the pair  
---|---  
offsetrequired| integer Example: offset=1Page index, first page = 1, fixed page size = 100  
fromDate| integer Example: fromDate=1689193800Integer specifying from (i.e. showing those later in time) which time all orders should be returned. Should be a timestamp in milliseconds since 1 Jan 1970.  
toDate| integer Example: toDate=1689193800Integer specifying up to (i.e. showing those earlier in time) which time all orders should be returned. Should be a timestamp in milliseconds since 1 Jan 1970.  
side| string Enum: "BUY" "SELL" When placing a buy order the base currency will be bought for the quote currency. The base currency will be sold for the quote currency when placing a sell order.  
orderStatus| string Enum: "CANCEL" "CLOSED"  
orderType| string Enum: "LIMIT" "MARKET"  
  
### Responses

**200 **

Success

get/api/orderHistory

Exchange server

https://exchange-api.lcx.com/api/orderHistory

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = { pair: "ETH/BTC", offset: 1 };
    
    var config = {
      method: "get",
      url: "https://exchange-api.lcx.com/api/orderHistory",
      headers: {
        // auth headers
      },
      params,
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": [
    * {
      * "Tx": null,

      * "Id": "9c7e7a80-d353-4832-9735-4fe34ad7252f",

      * "Pair": "LCX/EUR",

      * "BasePair": "",

      * "QuotePair": "",

      * "Price": 5.108,

      * "Amount": 112,

      * "Side": "SELL",

      * "OrderType": "LIMIT",

      * "Status": "CLOSED",

      * "Filled": 112,

      * "Average": 0,

      * "Total": 0,

      * "CreatedAt": 0,

      * "UpdatedAt": 1698330590,

      * "UserId": "7d83f7c6-8b51-4388-bd4d-e2e5241fd253",

      * "Fee": 0,

      * "IsFeeInLCX": true,

      * "FeeLevel": 0,

      * "FilledPer": 100,

      * "User": {
        * "Id": "",

        * "EmailId": "",

        * "LastName": "",

        * "FirstName": "",

        * "FeeInLCX": false,

        * "FeeLevel": 0,

        * "Status": false,

        * "Country": "",

        * "Referral_UserId": "",

        * "ReferralStatus": false,

        * "CreatedAt": "0001-01-01T00:00:00Z",

        * "UpdatedAt": "0001-01-01T00:00:00Z",

        * "Wallets": null,

        * "Trades": null

},

      * "Referral_UserId": "00000000-0000-0000-0000-000000000000",

      * "ClientOrderId": "00000000-0000-0000-0000-000000000000"

}

],

  * "message": "Orders fetched successfully",

  * "status": "success",

  * "totalCount": 2307049


}`

## [](#tag/Trading-API/paths/~1api~1uHistory/get)Trades

This endpoint provides a comprehensive view of all executed orders.

##### Authorizations:

(_API Key_ _Signature_ _Timestamp_) 

##### query Parameters

pair| string Example: pair=LCX/USDCName of the pair  
---|---  
offsetrequired| integer Example: offset=1Page index, first page = 1, fixed page size = 100  
fromDate| integer Example: fromDate=1689193800Integer specifying from (i.e. showing those later in time) which time all orders should be returned. Should be a timestamp in milliseconds since 1 Jan 1970.  
toDate| integer Example: toDate=1689193800Integer specifying up to (i.e. showing those earlier in time) which time all orders should be returned. Should be a timestamp in milliseconds since 1 Jan 1970.  
  
### Responses

**200 **

Success

get/api/uHistory

Exchange server

https://exchange-api.lcx.com/api/uHistory

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = { pair: "ETH/BTC", offset: 1 };
    
    var config = {
      method: "get",
      url: "https://exchange-api.lcx.com/api/uHistory",
      headers: {
        // auth headers
      },
      params,
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": [
    * {
      * "Amount": 100,

      * "CreatedAt": 1697171480,

      * "Fee": 0.1,

      * "FeeCoin": "LCX",

      * "Id": "2d9d0338-ae79-4f3d-962d-2d658750328c",

      * "OrderId": "f4703cc0-f496-42a9-b743-c4c5b761797a",

      * "OrderType": "LIMIT",

      * "Pair": "LCX/EUR",

      * "Price": 0.0386,

      * "Side": "BUY",

      * "Status": "CLOSED",

      * "UserId": "3321eb49-6228-4574-912f-af5aecd3e2f7"

}

],

  * "message": "Successfully Api response",

  * "status": "success",

  * "totalCount": 1


}`

## [](#tag/Account-API)Account API

## [](#tag/Account-API/paths/~1api~1balances/get)Balances

This endpoint retrieves balances for all listed coins.

##### Authorizations:

(_API Key_ _Signature_ _Timestamp_) 

### Responses

**200 **

Success

get/api/balances

Exchange server

https://exchange-api.lcx.com/api/balances

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require('axios')
    
    var config = {
      method: 'get',
      url: 'https://exchange-api.lcx.com/api/balances',
      headers: {
        // auth headers
      },
    }
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data))
      })
      .catch(function (error) {
        console.log(error)
      })
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": [
    * {
      * "balance": {
        * "freeBalance": 180611.65914222,

        * "occupiedBalance": 0,

        * "totalBalance": 180611.65914222

},

      * "coin": "USDC",

      * "equivalentUSDBalance": {
        * "freeBalance": 327827,

        * "occupiedBalance": 0,

        * "totalBalance": 327827

},

      * "fullName": "USD Coin"

},

    * {
      * "balance": {
        * "freeBalance": 899688.00000001,

        * "occupiedBalance": 0,

        * "totalBalance": 899688.00000001

},

      * "coin": "CELO",

      * "equivalentUSDBalance": {
        * "freeBalance": 6287641166.85,

        * "occupiedBalance": 0,

        * "totalBalance": 6287641166.85

},

      * "fullName": "Celo"

}

],

  * "message": "Wallets fetched successfully",

  * "status": "success",

  * "totalBalance": {
    * "inBTC": 60252968.05093348,

    * "inUSD": 2213935058063.5

}


}`

## [](#tag/Account-API/paths/~1api~1balance/get)Balance

This endpoint retrieves the balance specifically for a listed coin.

##### Authorizations:

(_API Key_ _Signature_ _Timestamp_) 

##### query Parameters

coinrequired| string Example: coin=LCXReturns the balance of specific asset in exchange balance.  
---|---  
  
### Responses

**200 **

Success

get/api/balance

Exchange server

https://exchange-api.lcx.com/api/balance

###  Request samples

  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Copy
    
    
    var axios = require("axios");
    var params = { coin: "ETH" };
    
    var config = {
      method: "get",
      url: "https://exchange-api.lcx.com/api/balance",
      headers: {
        // auth headers
      },
      params,
    };
    
    axios(config)
      .then(function (response) {
        console.log(JSON.stringify(response.data));
      })
      .catch(function (error) {
        console.log(error);
      });
    

###  Response samples

  * 200



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": {
    * "Coin": "LCX",

    * "TotalBalance": 1011.02768906,

    * "FreeBalance": 911.02768906,

    * "OccupiedBalance": 100,

    * "Decimals": 18

},

  * "message": "Successfully Api response",

  * "status": "success"


}`

## [](#tag/Market-Websocket)Market Websocket

Market WebSocket endpoints provide real-time market data including ticker, orderbook, and trade information. 

**Important** : To maintain reliable WebSocket connections, you must send a ping message to the server every 60 seconds. Failure to do so may result in the connection being closed.

## [](#tag/Market-Websocket/paths/~1subscribeTicker/post)Subscribe ticker

The ticker websocket makes available a high level overview of the current market status of a specified pair. It exhibits the current best bid and ask, the last traded price, along with information on the daily volume and price movement over the last day. Also give realtime updates of ticker data.

##### Request Body schema: application/json

required

Topicrequired| string Enum: "subscribe" "unsubscribe"  
---|---  
Typerequired| string Value: "ticker" ticker  
  
### Responses

**200 **

Success - Ticker Snapshot

**200 **

Success - Ticker Update

post/subscribeTicker

Exchange server

https://exchange-api.lcx.com/subscribeTicker

###  Request samples

  * Payload
  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Content type

application/json

Copy

`{

  * "Topic": "subscribe",

  * "Type": "ticker"


}`

###  Response samples

  * 200
  * 200 



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "type": "object",

  * "properties": {
    * "type": "ticker",

    * "topic": "snapshot",

    * "pair": "",

    * "data": {
      * "BTC/USDC": {
        * "bestAsk": 49900,

        * "bestBid": 43500,

        * "change": 0,

        * "equivalent": 44175.6781072649,

        * "high": 44309.0039,

        * "last24Price": 44309.0039,

        * "lastPrice": 44309.0039,

        * "lastUpdated": 1613545721,

        * "low": 44309.0039,

        * "symbol": "BTC/USDC",

        * "volume": 0

},

      * "ETH/BTC": {
        * "bestAsk": 0.037347,

        * "bestBid": 0.03551,

        * "change": 0,

        * "equivalent": 1974.8271966,

        * "high": 0.037347,

        * "last24Price": 0.037347,

        * "lastPrice": 0.037347,

        * "lastUpdated": 1613414932,

        * "low": 0.037347,

        * "symbol": "ETH/BTC",

        * "volume": 0

},

      * "ETH/USDC": {
        * "bestAsk": 1699.27,

        * "bestBid": 1500,

        * "change": 0,

        * "equivalent": 1594.45779657,

        * "high": 1599.27,

        * "last24Price": 1599.27,

        * "lastPrice": 1599.27,

        * "lastUpdated": 1613463023,

        * "low": 1599.27,

        * "symbol": "ETH/USDC",

        * "volume": 0

},

      * "LCX/BTC": {
        * "bestAsk": 1.7e-7,

        * "bestBid": 1.6e-7,

        * "change": 0,

        * "equivalent": 0.008989226,

        * "high": 1.7e-7,

        * "last24Price": 1.7e-7,

        * "lastPrice": 1.7e-7,

        * "lastUpdated": 1613491806,

        * "low": 1.7e-7,

        * "symbol": "LCX/BTC",

        * "volume": 0

},

      * "LCX/ETH": {
        * "bestAsk": 0.00001265,

        * "bestBid": 0.000009,

        * "change": 42.65,

        * "equivalent": 0.019223,

        * "high": 0.00001,

        * "last24Price": 0.00000701,

        * "lastPrice": 0.00001,

        * "lastUpdated": 1613774328,

        * "low": 0.00000851,

        * "symbol": "LCX/ETH",

        * "volume": 30000

},

      * "LCX/USDC": {
        * "bestAsk": 0.0193,

        * "bestBid": 0.01475,

        * "change": -30.72,

        * "equivalent": 0.018,

        * "high": 0.018,

        * "last24Price": 0.02598,

        * "lastPrice": 0.018,

        * "lastUpdated": 1613771976,

        * "low": 0.00012615,

        * "symbol": "LCX/USDC",

        * "volume": 58732.197

}

}

}


}`

## [](#tag/Market-Websocket/paths/~1subscribeOrderbook/post)Subscribe orderbook

The Orderbook websocket gives you all the bids and asks of the given pair at LCX Exchange. Also gives realtime updates of orderbook.

##### Request Body schema: application/json

required

Topicrequired| string Enum: "subscribe" "unsubscribe"  
---|---  
Typerequired| string Value: "orderbook" orderbook  
  
### Responses

**200 **

Success - Orderbook Snapshot

**200 **

Success - Orderbook Update

post/subscribeOrderbook

Exchange server

https://exchange-api.lcx.com/subscribeOrderbook

###  Request samples

  * Payload
  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Content type

application/json

Copy

`{

  * "Topic": "subscribe",

  * "Type": "orderbook"


}`

###  Response samples

  * 200
  * 200 



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "type": "orderbook",

  * "topic": "snapshot",

  * "pair": "LCX/USDC",

  * "data": {
    * "buy": [
      * [
        * 0.01475,

        * 3512.339

],

      * [
        * 0.01201,

        * 0

],

      * [
        * 0.01175,

        * 2136.596

],

      * [
        * 0.00618615,

        * 8116.68

],

      * [
        * 0.00179615,

        * 0

],

      * [
        * 0.0011961,

        * 42638.575

],

      * [
        * 0.00118615,

        * 0

],

      * [
        * 0.00117615,

        * 0

],

      * [
        * 0.00019615,

        * 381351.007

],

      * [
        * 0.00018635,

        * 123836.866

],

      * [
        * 0.00018615,

        * 91050.228

],

      * [
        * 0.00018,

        * 0

],

      * [
        * 0.00017775,

        * 0

],

      * [
        * 0.00017715,

        * 0

],

      * [
        * 0.00017615,

        * 642038.602

],

      * [
        * 0.0001725,

        * 0

],

      * [
        * 0.0001386,

        * 0

],

      * [
        * 0.00012615,

        * 134356.718

],

      * [
        * 0.00012605,

        * 79333.598

],

      * [
        * 0.000125,

        * 20000

],

      * [
        * 0.00000646,

        * 996904.0247678

]

],

    * "lastPrice": 0.018,

    * "sell": [
      * [
        * 0.0193,

        * 600

],

      * [
        * 0.02471,

        * 0

],

      * [
        * 0.0255,

        * 250

],

      * [
        * 0.0257,

        * 2500

],

      * [
        * 0.0258,

        * 10000

],

      * [
        * 0.04,

        * 2918

],

      * [
        * 0.0445,

        * 2400

],

      * [
        * 0.0446,

        * 100000

],

      * [
        * 0.04859999,

        * 2162.365

],

      * [
        * 0.0486,

        * 500

],

      * [
        * 0.049,

        * 4000

],

      * [
        * 0.0491,

        * 1000

],

      * [
        * 0.0499,

        * 1000

],

      * [
        * 0.04999999,

        * 5452.342

],

      * [
        * 0.05,

        * 150

],

      * [
        * 0.0599,

        * 3000

],

      * [
        * 0.06784,

        * 3500

],

      * [
        * 0.06984,

        * 5000

],

      * [
        * 0.079,

        * 1000

],

      * [
        * 0.07984,

        * 5000

],

      * [
        * 0.08,

        * 100

],

      * [
        * 0.0804,

        * 2000

],

      * [
        * 0.0805,

        * 0

],

      * [
        * 0.08984,

        * 5000

],

      * [
        * 0.0899,

        * 13000

],

      * [
        * 0.09,

        * 6750

],

      * [
        * 0.0951324,

        * 1000

],

      * [
        * 0.09699999,

        * 3000

],

      * [
        * 0.0979,

        * 113.658

],

      * [
        * 0.09799999,

        * 1000

],

      * [
        * 0.098,

        * 92426.49527781

],

      * [
        * 0.09984,

        * 5000

],

      * [
        * 0.099866,

        * 101

],

      * [
        * 0.0999,

        * 5800

],

      * [
        * 0.1,

        * 4100

],

      * [
        * 0.15,

        * 500

],

      * [
        * 0.2,

        * 500

],

      * [
        * 0.5,

        * 778.457

],

      * [
        * 0.5899,

        * 1000

],

      * [
        * 0.59,

        * 500

],

      * [
        * 0.616,

        * 500

],

      * [
        * 0.8978,

        * 1000

],

      * [
        * 0.8979,

        * 2831.75

],

      * [
        * 0.98,

        * 500

],

      * [
        * 0.99,

        * 1000

],

      * [
        * 1,

        * 84333.26501299

],

      * [
        * 1.99,

        * 400

],

      * [
        * 6.99,

        * 500

],

      * [
        * 7.99,

        * 500

],

      * [
        * 9.99,

        * 1500

]

]

}


}`

## [](#tag/Market-Websocket/paths/~1subscribeTrade/post)Subscribe trade

The trade websocket is used whenever a trade occurs at LCX Exchange. It is inclusive of all the crucial details of the trade, like the price, size and the time of execution. Also gives realtime updates of trades.

##### Request Body schema: application/json

required

Topicrequired| string Enum: "subscribe" "unsubscribe"  
---|---  
Typerequired| string Value: "trade"  
  
### Responses

**200 **

Success - Trade Snapshot

**200 **

Success - Trade Update

post/subscribeTrade

Exchange server

https://exchange-api.lcx.com/subscribeTrade

###  Request samples

  * Payload
  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Content type

application/json

Copy

`{

  * "Topic": "subscribe",

  * "Type": "trade"


}`

###  Response samples

  * 200
  * 200 



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "type": "trade",

  * "topic": "snapshot",

  * "pair": "ETH/BTC",

  * "data": [
    * [
      * 0.04326133,

      * 0.039,

      * "BUY",

      * 1613796138

],

    * [
      * 0.04322488,

      * 0.055,

      * "BUY",

      * 1613796137

],

    * [
      * 0.04314891,

      * 0.005,

      * "BUY",

      * 1613796137

],

    * [
      * 0.0422793,

      * 0.001,

      * "BUY",

      * 1613796137

],

    * [
      * 0.04140969,

      * 0.022,

      * "SELL",

      * 1613728909

],

    * [
      * 0.04079948,

      * 0.001,

      * "BUY",

      * 1613725383

],

    * [
      * 0.04014255,

      * 0.067,

      * "BUY",

      * 1613725383

],

    * [
      * 0.04124575,

      * 0.076,

      * "BUY",

      * 1613725383

],

    * [
      * 0.04140438,

      * 0.008,

      * "BUY",

      * 1613725383

],

    * [
      * 0.0415904,

      * 0.005,

      * "BUY",

      * 1613725383

],

    * [
      * 0.04186627,

      * 0.005,

      * "BUY",

      * 1613725383

],

    * [
      * 0.04219354,

      * 0.038,

      * "BUY",

      * 1613725383

],

    * [
      * 0.03947762,

      * 0.043,

      * "BUY",

      * 1613724435

],

    * [
      * 0.03924449,

      * 0.005,

      * "BUY",

      * 1613724435

],

    * [
      * 0.03924244,

      * 0.084,

      * "BUY",

      * 1613724435

],

    * [
      * 0.04000856,

      * 0.016,

      * "BUY",

      * 1613724435

],

    * [
      * 0.04003541,

      * 0.01,

      * "BUY",

      * 1613724435

],

    * [
      * 0.04017875,

      * 0.003,

      * "BUY",

      * 1613724435

],

    * [
      * 0.03845357,

      * 0.001,

      * "BUY",

      * 1613724435

],

    * [
      * 0.03930356,

      * 0.038,

      * "BUY",

      * 1613724435

],

    * [
      * 0.03766265,

      * 0.001,

      * "BUY",

      * 1613723256

]

]


}`

## [](#tag/Trading-Websocket)Trading Websocket

Trading WebSocket endpoints provide real-time updates about your account, including wallet balances, orders, and trades.

**Important** : To maintain reliable WebSocket connections, you must send a ping message to the server every 60 seconds. Failure to do so may result in the connection being closed.

## [](#tag/Trading-Websocket/paths/~1api~1auth~1ws?x-access-key={value}&x-access-sign={value}&x-access-timestamp={value}/post)Subscribe wallets

Wallet websocket enables you to receive wallet updates and snapshots regarding any activity on your account.

##### query Parameters

x-access-key| string Your LCX Exchange API Key  
---|---  
x-access-sign| string Signature signed by your LCX Exchange Secret Key  
x-access-timestamp| string Current timestamp in milliseconds  
  
##### Request Body schema: application/json

required

Topicrequired| string Enum: "subscribe" "unsubscribe"  
---|---  
Typerequired| string Value: "user_wallets"  
  
### Responses

**200 **

Success - Wallets Update

post/api/auth/ws?x-access-key={value}&x-access-sign={value}&x-access-timestamp={value}

Exchange server

https://exchange-api.lcx.com/api/auth/ws?x-access-key={value}&x-access-sign={value}&x-access-timestamp={value}

###  Request samples

  * Payload
  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Content type

application/json

Copy

`{

  * "Topic": "subscribe",

  * "Type": "user_wallets"


}`

###  Response samples

  * 200 



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "userid": "3321eb49-6228-4574-912f-af5aecd3e2f7",

  * "type": "user_wallets",

  * "topic": "update",

  * "data": {
    * "data": [
      * {
        * "balance": {
          * "freeBalance": 19.47944315,

          * "occupiedBalance": 0,

          * "totalBalance": 19.47944315

},

        * "coin": "BTC",

        * "equivalentUSDBalance": {
          * "freeBalance": 1113696.83,

          * "occupiedBalance": 0,

          * "totalBalance": 1113696.83

}

},

      * {
        * "balance": {
          * "freeBalance": 1920.64812163,

          * "occupiedBalance": 0,

          * "totalBalance": 1920.64812163

},

        * "coin": "USDC",

        * "equivalentUSDBalance": {
          * "freeBalance": 1920.64,

          * "occupiedBalance": 0,

          * "totalBalance": 1920.64

}

},

      * {
        * "balance": {
          * "freeBalance": 396785.98523184,

          * "occupiedBalance": 0,

          * "totalBalance": 396785.98523184

},

        * "coin": "LCX",

        * "equivalentUSDBalance": {
          * "freeBalance": 9638.78,

          * "occupiedBalance": 0,

          * "totalBalance": 9638.78

}

},

      * {
        * "balance": {
          * "freeBalance": 266.00853689,

          * "occupiedBalance": 0.2,

          * "totalBalance": 266.20853689

},

        * "coin": "ETH",

        * "equivalentUSDBalance": {
          * "freeBalance": 536858.42,

          * "occupiedBalance": 403.64,

          * "totalBalance": 537262.06

}

}

],

    * "totalBalance": {
      * "inBTC": 29.078767,

      * "inUSD": 1662518.31

}

}


}`

## [](#tag/Trading-Websocket/paths/~1api~1auth~1ws?x-access-key={value}&x-access-sign={value}&x-access-timestamp={timestamp-value}/post)Subscribe orders

Order websocket enables you to receive order updates regarding any order related activity in your account.

##### query Parameters

x-access-key| string Your LCX Exchange API Key  
---|---  
x-access-sign| string Signature signed by your LCX Exchange Secret Key  
x-access-timestamp| string Current timestamp in milliseconds  
  
##### Request Body schema: application/json

required

Topicrequired| string Enum: "subscribe" "unsubscribe"  
---|---  
Typerequired| string Value: "user_orders"  
  
### Responses

**200 **

Success - Orders Update

post/api/auth/ws?x-access-key={value}&x-access-sign={value}&x-access-timestamp={timestamp-value}

Exchange server

https://exchange-api.lcx.com/api/auth/ws?x-access-key={value}&x-access-sign={value}&x-access-timestamp={timestamp-value}

###  Request samples

  * Payload
  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Content type

application/json

Copy

`{

  * "Topic": "subscribe",

  * "Type": "user_orders"


}`

###  Response samples

  * 200 



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "data": {
    * "Tx": null,

    * "Id": "4d845efc-2ffe-44fb-b37b-bde70ddee94e",

    * "Pair": "MATIC/EUR",

    * "BasePair": "",

    * "QuotePair": "",

    * "Price": 0.61,

    * "Amount": 100,

    * "Side": "BUY",

    * "OrderType": "LIMIT",

    * "Status": "OPEN",

    * "Filled": 0,

    * "Average": 0.61,

    * "Total": 0,

    * "CreatedAt": 1716222351,

    * "UpdatedAt": 1716222351,

    * "UserId": "7d83f7c6-8b51-4388-bd4d-e2e5241fd253",

    * "Fee": 0,

    * "IsFeeInLCX": false,

    * "FeeLevel": 3,

    * "FilledPer": 0,

    * "User": {
      * "Id": "",

      * "EmailId": "",

      * "LastName": "",

      * "FirstName": "",

      * "FeeInLCX": false,

      * "FeeLevel": 0,

      * "Status": false,

      * "Country": "",

      * "Referral_UserId": "",

      * "ReferralStatus": false,

      * "CreatedAt": "0001-01-01T00:00:00Z",

      * "UpdatedAt": "0001-01-01T00:00:00Z",

      * "Wallets": null,

      * "Trades": null

},

    * "IsTaker": false,

    * "Referral_UserId": "b3521d0e-3f4d-4ec0-a51d-24d8ab15c967",

    * "ClientOrderId": "7c3e3e96-1227-424f-b062-56bad5d6f2d0"

},

  * "method": "create",

  * "topic": "update",

  * "type": "user_orders"


}`

## [](#tag/Trading-Websocket/paths/~1api~1auth~1ws?x-access-key={value}&x-access-sign={value}&x-access-timestamp={timestamp}/post)Subscribe trades

Trades websocket enables you to receive trade updates regarding any trade related activity in your account.

##### query Parameters

x-access-key| string Your LCX Exchange API Key  
---|---  
x-access-sign| string Signature signed by your LCX Exchange Secret Key  
x-access-timestamp| string Current timestamp in milliseconds  
  
##### Request Body schema: application/json

required

Topicrequired| string Enum: "subscribe" "unsubscribe"  
---|---  
Typerequired| string Value: "user_trades"  
  
### Responses

**200 **

Success - Trades Update

post/api/auth/ws?x-access-key={value}&x-access-sign={value}&x-access-timestamp={timestamp}

Exchange server

https://exchange-api.lcx.com/api/auth/ws?x-access-key={value}&x-access-sign={value}&x-access-timestamp={timestamp}

###  Request samples

  * Payload
  * Javascript
  * Python
  * Java
  * Golang
  * PHP



Content type

application/json

Copy

`{

  * "Topic": "subscribe",

  * "Type": "user_trades"


}`

###  Response samples

  * 200 



Content type

application/json

Copy

Expand all  Collapse all 

`{

  * "topic": "update",

  * "type": "user_trades",

  * "data": {
    * "userId": "d5a18319-23bb-467c-96fd-70b2b2f35b56",

    * "orderId": "f06fd380-c045-4943-8267-d0d5413ec7c7",

    * "price": 0.0626,

    * "amount": 100,

    * "side": "BUY",

    * "createdAt": 1703567167,

    * "IsTaker": true,

    * "fee": 0.07499995,

    * "feeCoin": "LCX",

    * "tradeId": "4a2cf029-8e35-4d84-a08e-8d6c2e8637e2"

}


}`

## [](#tag/Errors)Errors

## [](#tag/Errors/Message-Errors)Message Errors

These appear when there is an error in the code used. When this happens, an error message will be sent including the error code indicating the exact error to the user.

## [](#tag/Release-Notes)Release Notes

  * **Version 1.1.2**

Impacted WebSockets : 

Subscribe Orderbook  
Topic: orderbook  
Change : 

    * Response Body: The `data` field in orderbook update messages has been updated to support multiple orderbook changes in a single update. Instead of returning a single orderbook change `[price, amount, side]`, the response now returns an array of orderbook changes `[[price, amount, side], [price, amount, side], ...]`.

Subscribe Trade  
Topic: trade  
Change : 

    * Response Body: The `data` field in trade update messages has been updated to support multiple trade executions in a single update. Instead of returning a single trade `[price, amount, side, timestamp]`, the response now returns an array of trades `[[price, amount, side, timestamp], [price, amount, side, timestamp], ...]`.

Subscribe Ticker  
Topic: ticker  
Change : 

    * Response Body: Both snapshot and update responses now use the same unified response structure for consistency.
  * **Version 1.1.1**

Impacted APIs : 

New order  
Method: POST  
URL : {baseUrl}/api/create  
Change : 

    * Request Body : A new optional field, ClientOrderId, has been added. If this key is not provided in the request, the backend will auto-generate a ClientOrderId of type UUID and include it in the response. 
    * Response Body: The ClientOrderId field has been included in the response body.

Cancel order  
Method: DELETE  
URL : {baseUrl}/api/cancel  
Change : 

    * Response Body: The ClientOrderId field has been included in the response body.

Open orders  
Method: GET  
URL : {baseUrl}/api/open  
Change : 

    * Response Body: The ClientOrderId field has been included in the response body.

Order  
Method: GET  
URL : {baseUrl}/api/order  
Change : 

    * Response Body: The ClientOrderId field has been included in the response body.

Orders  
Method: GET  
URL : {baseUrl}/api/orderHistory  
Change : 

    * Response Body: The ClientOrderId field has been included in the response body.

Impacted WebSockets: 

Subscribe orders  
Topic: update  
Change : 

    * Response Body: The ClientOrderId field has been added to the data updates sent via WebSockets for user orders
  * **Version 1.1.0**  
We are excited to announce the release of version 1.1.0 of the LCX API. This new version includes a range of new endpoints that enhance functionality and provide our users with more detailed and robust data access. Below is a summary of the newly added APIs:

Get Tickers: Retrieve a list of tickers.  
Method: GET  
URL: {baseUrl}/api/tickers

Get Ticker: Obtain information about a specific ticker.  
Method: GET  
URL: {baseUrl}/api/ticker

Get OrderBook: Access the order book for a specific trading pair.  
Method: GET  
URL: {baseUrl}/api/book

Get Pairs: List all available trading pairs.  
Method: GET  
URL: {baseUrl}/api/pairs

Get Pair: Get information about a specific trading pair.  
Method: GET  
URL: {baseUrl}/api/pair

Cancel Order: Cancel an existing order.  
Method: DELETE  
URL: {baseUrl}/api/cancel

Modify Order: Modify an existing order.  
Method: PUT  
URL: {baseUrl}/api/modify

Get Order: Retrieve information about a specific order.  
Method: GET  
URL: {baseUrl}/api/order

Get User Trade History: Access the trade history of a user.  
Method: GET  
URL: {baseUrl}/api/uHistory

Get Recent Trade: Obtain recent trade information.  
Method: GET  
URL: {baseUrl}/api/trades

Get Order History: Retrieve a user's order history.  
Method: GET  
URL: {baseUrl}/api/orderHistory

Get Open Order: List all open orders for a user.  
Method: GET  
URL: {baseUrl}/api/Open

Get Balance: Check the balance of a user.  
Method: GET  
URL: {baseUrl}/api/balance



