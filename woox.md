# Woox API Documentation

Auto-fetched from 2 page(s)


---

# Source: https://docs.woox.io/v5/trading-api/restful-api

[ NAV  ](#)

[cURL](#) [Python](#) [Node.js](#) [Java](#)



  * [General Information](#general-information)
  * [Authentication](#authentication)
    * [Example](#example)
    * [Security](#security)
  * [Error Codes](#error-codes)
    * [order service error code](#order-service-error-code)
  * [RESTful API](#restful-api)
    * [Get System Maintenance Status (Public)](#get-system-maintenance-status-public)
    * [Exchange Information](#exchange-information)
    * [Available Symbols (Public)](#available-symbols-public)
    * [Market Trades (Public)](#market-trades-public)
    * [Market Trades History(Public)](#market-trades-history-public)
    * [Orderbook snapshot (Public)](#orderbook-snapshot-public)
    * [Kline (Public)](#kline-public)
    * [Kline - Historical Data (Public)](#kline-historical-data-public)
    * [Available Token (Public)](#available-token-public)
    * [Token Network (Public)](#token-network-public)
    * [Get Predicted Funding Rate for All Markets (Public)](#get-predicted-funding-rate-for-all-markets-public)
    * [Get Predicted Funding Rate for One Market (Public)](#get-predicted-funding-rate-for-one-market-public)
    * [Get Funding Rate History for One Market (Public)](#get-funding-rate-history-for-one-market-public)
    * [Get Futures Info for All Markets (Public)](#get-futures-info-for-all-markets-public)
    * [Get Futures for One Market (Public)](#get-futures-for-one-market-public)
    * [Token Config](#token-config)
    * [Send Order](#send-order)
    * [Cancel all after](#cancel-all-after)
    * [Cancel Order](#cancel-order)
    * [Cancel Order by client_order_id](#cancel-order-by-client_order_id)
    * [Cancel Orders](#cancel-orders)
    * [Cancel All Pending Orders](#cancel-all-pending-orders)
    * [Get Order](#get-order)
    * [Get Order by client_order_id](#get-order-by-client_order_id)
    * [Get Orders](#get-orders)
    * [Edit Order](#edit-order)
    * [Edit Order by client_order_id](#edit-order-by-client_order_id)
    * [Send Algo Order](#send-algo-order)
    * [Cancel Algo Order](#cancel-algo-order)
    * [Cancel All Pending Algo Orders](#cancel-all-pending-algo-orders)
    * [Cancel Pending Merge Orders by Symbol](#cancel-pending-merge-orders-by-symbol)
    * [Get Algo Order](#get-algo-order)
    * [Get Algo Orders](#get-algo-orders)
    * [Edit Algo Order](#edit-algo-order)
    * [Edit Algo Order by client_order_id](#edit-algo-order-by-client_order_id)
    * [Get Trade](#get-trade)
    * [Get Trades](#get-trades)
    * [Get Trade History](#get-trade-history)
    * [Get Archived Trade History](#get-archived-trade-history)
    * [Get Current Holding](#get-current-holding)
    * [Get Current Holding v2](#get-current-holding-v2)
    * [Get Current Holding (Get Balance) - New](#get-current-holding-get-balance-new)
    * [Get Account Information](#get-account-information)
    * [Get Account Information - New](#get-account-information-new)
    * [Get Token History](#get-token-history)
    * [Get Account API Key & Permission](#get-account-api-key-amp-permission)
    * [Get Buy Power](#get-buy-power)
    * [Get Token Deposit Address](#get-token-deposit-address)
    * [Token Withdraw](#token-withdraw)
    * [Token Withdraw V3](#token-withdraw-v3)
    * [Internal token withdraw](#internal-token-withdraw)
    * [Cancel Withdraw Request](#cancel-withdraw-request)
    * [Get Asset History](#get-asset-history)
    * [Margin Interest Rates](#margin-interest-rates)
    * [Margin Interest Rate of Token](#margin-interest-rate-of-token)
    * [Get Interest History](#get-interest-history)
    * [Repay Interest](#repay-interest)
    * [Get referrals summary](#get-referrals-summary)
    * [Get referral reward history](#get-referral-reward-history)
    * [Get Subaccounts](#get-subaccounts)
    * [Get Assets of Subaccounts](#get-assets-of-subaccounts)
    * [Get Asset Details from a Subaccount](#get-asset-details-from-a-subaccount)
    * [Get IP Restriction](#get-ip-restriction)
    * [Get Transfer History](#get-transfer-history)
    * [Transfer Assets](#transfer-assets)
    * [Get LtV info](#get-ltv-info)
    * [Update Account Mode](#update-account-mode)
    * [Update Position Mode](#update-position-mode)
    * [Update Leverage Setting](#update-leverage-setting)
    * [Update Futures Leverage Setting](#update-futures-leverage-setting)
    * [GET Futures Leverage Setting](#get-futures-leverage-setting)
    * [Update Isolated Margin Setting](#update-isolated-margin-setting)
    * [Get Funding Fee History](#get-funding-fee-history)
    * [Get All Position info](#get-all-position-info)
    * [Get All Position info - New](#get-all-position-info-new)
    * [Get One Position info](#get-one-position-info)
    * [GET InsuranceFund](#get-insurancefund)
    * [GET AssignmentPreference](#get-assignmentpreference)
    * [Add an AssignmentPreference](#add-an-assignmentpreference)
    * [Delete an AssignmentPreference](#delete-an-assignmentpreference)
  * [Websocket API V2](#websocket-api-v2)
    * [PING/PONG](#ping-pong)
    * [request orderbook](#request-orderbook)
    * [orderbook](#orderbook)
    * [orderbookupdate](#orderbookupdate)
    * [trade](#trade)
    * [trades](#trades)
    * [24h ticker](#24h-ticker)
    * [24h tickers](#24h-tickers)
    * [bbo](#bbo)
    * [bbos](#bbos)
    * [k-line](#k-line)
    * [indexprice](#indexprice)
    * [markprice](#markprice)
    * [estfundingrate](#estfundingrate)
    * [openinterests](#openinterests)
    * [markprices](#markprices)
    * [auth](#auth)
    * [balance](#balance)
    * [executionreport](#executionreport)
    * [algoexecutionreportv2](#algoexecutionreportv2)
    * [position push](#position-push)
    * [marginassignment](#marginassignment)
  * [Release Note](#release-note)
    * [2025-09-21](#2025-09-21)
    * [2025-07-14](#2025-07-14)
    * [2025-04-30](#2025-04-30)
    * [2024-09-22](#2024-09-22)
    * [2024-07-14](#2024-07-14)
    * [2024-07-04](#2024-07-04)
    * [2024-06-24](#2024-06-24)
    * [2024-06-09](#2024-06-09)
    * [2024-05-20](#2024-05-20)
    * [2024-05-09](#2024-05-09)
    * [2024-04-22](#2024-04-22)
    * [2024-04-16](#2024-04-16)
    * [2024-03-31 ï¼4/2 system releaseï¼](#2024-03-31-4-2-system-release)
    * [2024-03-25](#2024-03-25)
    * [2024-02-26](#2024-02-26)
    * [2024-02-21](#2024-02-21)
    * [2024-02-21](#2024-02-21-2)
    * [2024-01-30](#2024-01-30)
    * [2024-01-10](#2024-01-10)
    * [2023-12-12](#2023-12-12)
    * [2023-10-30](#2023-10-30)
    * [2023-09-25](#2023-09-25)
    * [2023-07-24](#2023-07-24)
    * [2023-07-03](#2023-07-03)
    * [2023-06-12](#2023-06-12)
    * [2023-04-10](#2023-04-10)
    * [2023-02-06](#2023-02-06)
    * [2022-12-05](#2022-12-05)
    * [2022-11-21](#2022-11-21)
    * [2022-10-24](#2022-10-24)
    * [2022-09-08](#2022-09-08)
    * [2022-08-18](#2022-08-18)
    * [2022-07-28](#2022-07-28)
    * [2022-06-10](#2022-06-10)
    * [2022-05-23](#2022-05-23)
    * [2022-03-21](#2022-03-21)
    * [2022-02-25](#2022-02-25)
    * [2022-01-17](#2022-01-17)
    * [2021-12-24](#2021-12-24)
    * [2021-11-12](#2021-11-12)
    * [2021-10-22](#2021-10-22)
    * [2021-09-27](#2021-09-27)
    * [2021-09-06](#2021-09-06)
    * [2021-09-03](#2021-09-03)
    * [2021-08-06](#2021-08-06)
    * [2021-07-09](#2021-07-09)
    * [2021-06-25](#2021-06-25)


  * Copyright @ 2023 WOO Network.



# General Information

**WOO X. A privately-accessible liquidity venue for the trading of cryptocurrencies.**

WOO X provides clients with an easily accessible deep pool of liquidity sourced from the largest exchanges and from Kronosâ HFT proprietary trading. We utilize advanced crossing and routing methods which provide ease of access and superior trade execution to select exchanges. 

We provide two interfaces to communicate between WOO X and clients. 

  * [RESTful API interface](#restful-api): Provides sending events like create order, cancel order, fetch balance, ...etc.
  * [Websocket interface V2](#websocket-api-v2): Provides real-time orderbook data feed and order update feed.



**Base endpoints:**

We will launch a new domain api.woox.io on 2024/09/22. Please note that the old domain api.woo.org will be decommissioned at a later date, which will be announced separately. If you are a new user, please use the new domain api.woox.io for integration. If you are an existing user, you may continue using api.woo.org, but we recommend migrating to api.woox.io as soon as possible to avoid any service disruptions in the future.

  * `https://api.woox.io/` **(Production)**
  * `https://api-pub.woox.io` **(Production)**
  * `https://api.staging.woox.io` **(staging)**



**Authorization:**  
All our interfaces require key to access, and the token will be pre-generated by us.  
Please set the corrsponding header in your request. Refer to [Authenticaton](#authentication) for more information.

**Symbol:**  
WOO X use the following format: `<TYPE>_<BASE>_<QUOTE>` to represent a symbol name, for example: `SPOT_BTC_USDT` means that it is `BTC_USDT` pair in `SPOT` trading market.

**Rate Limit:**

WebSocket Connection:  
\- The establishment of WebSocket connections is based on the application ID.  
\- The application ID should be appended at the end of the wss endpoint.

RESTful API:  
\- For public endpoints, the rate limit is calculated based on the IP address.  
\- For private endpoints, the rate limit is calculated based on the account (i.e., application ID, unique for each main/sub-account).  
\- All api_keys under the same account (i.e., the same application ID) share their rate limits.

WebSocket Service Connection Restrictions:  
\- WebSocket services have limitations on the number of connections and topic subscriptions.  
\- For each account (main and sub-accounts are independent), there is a restriction on the maximum concurrent connection count, set at 80.  
\- The maximum number of topics within each connection is limited to 50.

IP Connection Limitation:  
\- Simultaneously, there is a restriction on the concurrent connection count for each IP address, capped at 1000.

if your application reached the rate limit of a certain endpoint, the server will return an error result with http code `429`. You may need to wait until the next time horizon.

**Error Message:**

> **Errors consist of three parts: an error code, detail message and a success flag.**
    
    
    {
      "success": false,
      "code": -1005, // Error code
      "message": "order_price must be a positive number" // Detail message  
    }
    

All API will return following json when api failed, the "message" will contain the detail error message, it may be because some data is in the wrong format, or another type of error.  
Specific error codes and messages are defined in [Errors Codes](#error-codes).

# Authentication

Client needs to ask for an `api_key`ï¼`api-timestamp` and `api_secret`, and use these to sign your request.

VIP users add an optional `api-recvwindow` to specify the number of milliseconds after `api-timestamp` the request is valid for. If `api-recvwindow` is not specified, it defaults to 5000.If `api-timestamp` \+ `api-recvwindow` > timestamp in dedicated gateway when itâs ready to process the request, throw an error âRequest has failed as the receive window is exceeded.â

## Example

Here we provide a simple example that shows you how to send a valid request to WOO X.  
Assume following infomation:

Key | Value | Description  
---|---|---  
`api_key` | `AbmyVJGUpN064ks5ELjLfA==` | create from WOO X console  
`api_secret` | `QHKRXHPAW1MC9YGZMAT8YDJG2HPR` | create from WOO X console  
`timestamp` | `1578565539808` | Unix epoch time in milliseconds  
`api-recvwindow` | `5000` | specify the number of milliseconds after `api-timestamp` the request is valid for ï¼VIP usersï¼  
  
Hash your request parameters with `api_secret`, the hashing logic is described as follows: 

> **If the request looks like:**
    
    
    POST /v1/order
    
    # Body parameter:
    symbol:SPOT_BTC_USDT
    order_type:LIMIT
    order_price:9000
    order_quantity:0.11
    side:BUY
    

For `v1` API, please follow the steps to normalize request content:

  1. use **query string** as the parameters for **GET** methods and **body parameters** for **POST** and **DELETE** methods.
  2. concat **query string** and **body parameters** in an alphabetical order in [query string format](https://en.wikipedia.org/wiki/Query_string).
  3. concat `timestamp` with the above result, using `|` as seperator.



> **Normalize request content for V1 API, The result content would look like following**
    
    
    order_price=9000&order_quantity=0.11&order_type=LIMIT&side=BUY&symbol=SPOT_BTC_USDT|1578565539808
    

For `v3` API using request body to pass the parameters, please concatenate the `timestamp`, `http request method`, `request_path` and `request_body` as the normalized content to sign. Besides, please use `application/json` as `Content-Type` in the headers.

var signString = timestamp + method + request_path + request_body;

> **Normalize request content for V3 API, The result content would look like following**
    
    
    1578565539808POST/v3/algo/order{
        "symbol": "PERP_BTC_USDT",
        "side": "BUY",
        "reduceOnly": false,
        "type": "MARKET",
        "quantity": "1",
        "algoType": "TRAILING_STOP",
        "callbackRate": "0.012"
    }
    

> **Then use`api_secret` to hash it with HMAC `SHA256` algorithm, you can use `openssl` to get this:**
    
    
    $ echo -n "order_price=9000&order_quantity=0.11&order_type=LIMIT&side=BUY&symbol=SPOT_BTC_USDT|1578565539808" | openssl dgst -sha256 -hmac "QHKRXHPAW1MC9YGZMAT8YDJG2HPR"
    (stdin)= 20da0852f73b20da0208c7e627975a59ff072379883d8457d03104651032033d
    

Put the **HMAC signature** in request header `x-api-signature`, and put **timestamp** in `x-api-timestamp`, and also **api key** in `x-api-key`.

**So the final request would look like:**

POST /v1/order HTTP/1.1 Content-Type: application/x-www-form-urlencoded x-api-key: AbmyVJGUpN064ks5ELjLfA== x-api-signature: 20da0852f73b20da0208c7e627975a59ff072379883d8457d03104651032033d x-api-timestamp: 1578565539808 cache-control: no-cache symbol=SPOT_BTC_USDT order_type=LIMIT order_price=9000 order_quantity=0.11 side=BUY 

> **sample code**
    
    
    # python sample code for generate signature
    import datetime
    import hmac, hashlib, base64
    import requests
    import json
    
    
    staging_api_secret_key = '6XXXXXXXXXXXXXXXXXXXXXXXB'
    staging_api_key = 'Ppppppppppppppppppp=='
    
    def _generate_signature(data):
      key = staging_api_secret_key#'key' # Defined as a simple string.
      key_bytes= bytes(key , 'utf-8') # Commonly 'latin-1' or 'utf-8'
      data_bytes = bytes(data, 'utf-8') # Assumes `data` is also a string.
      return hmac.new(key_bytes, data_bytes , hashlib.sha256).hexdigest()
    
    
    milliseconds_since_epoch = round(datetime.datetime.now().timestamp() * 1000)
    
    headers = {
        'x-api-timestamp': str(milliseconds_since_epoch),
        'x-api-key': staging_api_key,
        'x-api-signature': _generate_signature("client_order_id=123456&order_price=0.8148&order_quantity=10&order_type=LIMIT&side=BUY&symbol=PERP_XRP_USDT|"+str(milliseconds_since_epoch)),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control':'no-cache'
    }
    data = {
      'client_order_id':123456,
      'order_price' : 0.8148,
      'order_quantity': 10,
      'order_type': 'LIMIT',
      'side':'BUY',
      'symbol': 'PERP_XRP_USDT'
    }
    
    
    
    response = requests.post('https://api.staging.woo.org/v1/order', headers=headers, data=data )
    print(response.json())
    
    
    
    
    # Get current timestamp in milliseconds
    milliseconds_since_epoch = str(int(datetime.datetime.now().timestamp() * 1000))
    
    # Define query parameters
    params = {
        "page": 14,
        "size": 100,
        "from": 1,
        "to": 1739215032222
    }
    
    # Construct request path and query string
    request_path = '/v3/referrals'
    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    url = f'https://api.woox.io{request_path}?{query_string}'
    
    # Concatenate signature content: timestamp + method + request_path + query_string
    signature_payload = milliseconds_since_epoch + 'GET' + request_path + '?' + query_string
    
    # Generate signature
    def _generate_signature(data):
        key_bytes = bytes(prod_api_secret_key, 'utf-8')
        data_bytes = bytes(data, 'utf-8')
        return hmac.new(key_bytes, data_bytes, hashlib.sha256).hexdigest()
    
    signature = _generate_signature(signature_payload)
    
    # Set headers
    headers = {
        'x-api-timestamp': milliseconds_since_epoch,
        'x-api-key': prod_api_key,
        'x-api-signature': signature,
        'Cache-Control': 'no-cache'
    }
    
    # Send GET request with query parameters
    response = requests.get(url, headers=headers)
    
    # Print response
    print(response.content)
    
    
    
    
    
    
    // Node.js sample code for generate signature
    var cryptoJS = require('crypto-js');
    var axios = require('axios');
    async function getAccountInfo() {
    
      const xApiTimestamp = Date.now();
    
      const queryString = '|' + xApiTimestamp;
    
      production_api_secret_key = '3XXXXXXXXXXXXXXXXXXXXXXXXXXXZ'
      production_api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx=='
      console.log(cryptoJS.HmacSHA256(queryString, production_api_secret_key).toString());
      const headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-api-key': production_api_key,
        'x-api-signature': cryptoJS.HmacSHA256(queryString, production_api_secret_key).toString(),
        'x-api-timestamp': xApiTimestamp,
        'cache-control': 'no-cache'
    
      };
    
    
    
      try {
        const res = await axios.get('https://api.woo.org' + '/v1/client/info', {headers:headers});
    
        console.log('response', res);
    
        return res;
    
      } catch (error) {
        console.log(error.response)
        // throw new Error('Error with getAccountInfo : ' + error.message + '\n' + 'queryString : ' + queryString)
    
      }
    
    }
    
    
    getAccountInfo()
    

## Security

There have four-layer checker to check if a request is valid. WOO X server only accepts the request that passed all checkers. The checker is defined as follows:

**Revoken checker:**  
The api key/secret can be revoked manaually by clients' request. if the key was revoked, all access tokens generated by this key cannot be used.

**Request IP checker:**  
The api key/secret can be tied to specific ips (default is empty). if the request is not coming from allowed ip addresses, the request would be rejected.

**Request Timestamp checker:**  
The request would be considered expired and get rejected if the timestamp in `x-api-timestamp` header has a 300+ second difference from the API server time.

**HMAC Parameter Signature:**  
The request must have a `x-api-signature` header that is generated from request parameters and signed with your secret key.

# Error Codes

Errors consist of three parts: an error code and a message. Codes are universal, but messages can vary. Here is the error JSON payload:
    
    
    {
      "success": false,
      "code": -1001, // Error code
      "message": "order_price must be a positive number" // Detail message  
    }
    

Error Code | Status Code | Error Name | Description  
---|---|---|---  
`-1000` | 500 | `UNKNOWN` | An unknown error occurred while processing the request.  
`-1001` | 401 | `INVALID_SIGNATURE` | The api key or secret is in wrong format.  
`-1002` | 401 | `UNAUTHORIZED` | API key or secret is invalid, it may be because the key has insufficient permission or the key is expired/revoked.  
`-1003` | 429 | `TOO_MANY_REQUEST` | Rate limit exceed.  
`-1004` | 400 | `UNKNOWN_PARAM` | An unknown parameter was sent.  
`-1005` | 400 | `INVALID_PARAM` | Some parameters are in the wrong format for api.  
`-1006` | 400 | `RESOURCE_NOT_FOUND` | The data is not found in the server. For example, when the client try canceling a CANCELLED order, will raise this error.  
`-1007` | 409 | `DUPLICATE_REQUEST` | The data already exists or your request is duplicated.  
`-1008` | 400 | `QUANTITY_TOO_HIGH` | The quantity of settlement is higher than you can request.  
`-1009` | 400 | `CAN_NOT_WITHDRAWAL` | Can not request withdrawal settlement, you need to deposit other arrears first.  
`-1011` | 400 | `RPC_NOT_CONNECT` | Can not place/cancel orders, it may be because of internal network error. Please try again in a few seconds.  
`-1012` | 400 | `RPC_REJECT` | The place/cancel order request is rejected by internal module, it may be because the account is in liquidation or other internal errors. Please try again in a few seconds.  
`-1101` | 400 | `RISK_TOO_HIGH` | The risk exposure for the client is too high, it may be caused by sending too big order or the leverage is too low. please refer to [client info](#get-account-information) to check the current exposure.  
`-1102` | 400 | `MIN_NOTIONAL` | The order value (price * size) is too small.  
`-1103` | 400 | `PRICE_FILTER` | The order price is not following the tick size rule for the symbol.  
`-1104` | 400 | `SIZE_FILTER` | The order quantity is not following the step size rule for the symbol.  
`-1105` | 400 | `PERCENTAGE_FILTER` | Price is X% too high or X% too low from the mid price.  
  
## order service error code

code | errorCode | message  
---|---|---  
-1005 | 317136 | Edit tpsl quantity is not allowed for quantity bracket  
-1005 | 317137 | Edit quantity should edit both legs  
-1005 | 317138 | Edit quantity should be same for both legs  
-1005 | 317139 | Trigger price of 1st leg should not be empty for STOP_BRACKET  
-1005 | 317140 | The quantity of a quantity TP/SL order should not be empty.  
-1005 | 317141 | The algo quantity TP/SL limit order should have field price  
-1005 | 317142 | The algo trigger type of quantity TP/SL should not be CLOSE_POSITION  
-1005 | 317143 | The side of TP/SL legs should be the same  
-1006 | 317144 | IndexPrice is not supported for non spot symbol ${symbol}  
-1103 | 317145 | same as INVALID_PRICE_QUOTE_MIN but different 'code'  
-1103 | 317146 | same as INVALID_PRICE_QUOTE_MAX but different 'code'  
-1103 | 317147 | same as INVALID_PRICE_TICKER_SIZE but different 'code'  
-1005 | 317148 | symbol can't be empty.  
-1006 | 317149 | same with TRADE_NOT_FOUND with different ErrorCodes  
-1005 | 317150 | trigger price must be greater than ${price}  
-1005 | 317151 | trigger price must be less than ${price}  
-1005 | 317152 | The order not found for the order id : ${orderId}  
-1005 | 317153 | child order not found for the order id : ${orderId}  
-1012 | 317154 | RPC failed: error: ${msg}  
-1005 | 317155 | unsupported symbol: ${symbol}  
-1006 | 317156 | unsupported symbol: ${symbol}  
-1006 | 317157 | Trading with ${symbol1}/${symbol2} is temporarily suspended. Please try again later.  
-1006 | 317158 | Trading with ${token}-PERP is temporarily suspended. Please try again later.  
-1005 | 317159 | This pair is currently not supported.  
-1006 | 317160 | The order id and symbol are not matched  
-1006 | 317161 | The order is completed  
-1005 | 317162 | The params should not be null or 0  
-1005 | 317163 | cannot edit TP/SL quantity under bracket order  
-1006 | 317164 | Invalid client order id  
-1006 | 317165 | invalid order id list  
-1006 | 317166 | invalid client order id list  
-1005 | 317167 | unsupported algo type: ${algoType}  
-1000 | 317168 | Order failed due to internal service error. Please contact customer service.  
-1006 | 317169 | Trading with ${left}/${right} is temporarily suspended. Please try again later.  
-1005 | 317170 | The order quantity must bigger than the executed quantity.  
-1000 | 317171 | error path format  
-1005 | 317172 | The userId should not be null or 0  
-1005 | 317173 | The orderId should not be null or 0  
-1006 | 317174 | The order is processing  
-1005 | 317176 | The trigger after should from 0 to ${maxTriggerAfter}  
-1005 | 317177 | Order has terminated  
-1005 | 317178 | The receive window is invalid.  
-1005 | 317179 | Request has failed as the receive window: ${recv_window} millisecond is exceeded from ${api_timestamp}  
-1006 | 317184 | The order cannot be found, or it is already completed.  
-1012 | 317206 | Spot trading is disabled while futures credits are active. Please remove or fully utilize your futures credits to enable spot trading.  
-1012 | 317207 | Request failed. Please ensure you have sufficient USDT to cover the futures credits currently in use.  
  
# RESTful API

## Get System Maintenance Status (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/system_info `

For fetch system status to check if system is down or under maintenance.

> **Response**
    
    
    { 
        // functioning properly
        "success":true,
        "data":
            {
                "status":0,
                "msg":"System is functioning properly."
            },
        "timestamp":1676335013700
    }
    {   
        // trading maintenance
        "success":true,
        "data":
            {
                "status":1,
                "msg":"Under trading maintenance."
            },
        "timestamp":1676335013700
    }
    
    {   
        // system maintenance
        "success":true,
        "data":
            {
                "status":2,
                "msg":"Under system maintenance."
            },
        "timestamp":1676335013700
    }
    

**Parameters**

None

## Exchange Information

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/info/:symbol `

Get send order requirement by symbol, there are some rules need to be fullfilled in order to successfully send order, which are defined as follows:

Price filter

  * `price` >= `quote_min`
  * `price` <= `quote_max`
  * `(price - quote_min) % quote_tick` should equal to zero
  * `price` <= `asks[0].price * (1 + price_range)` when BUY
  * `price` >= `bids[0].price * (1 - price_range)` when SELL



Size filter

  * `base_min` <= `quantity` <= `base_max`
  * `(quantity - base_min) % base_tick` should equal to zero



Min Notional filter

  * `price * quantity` should greater than `min_notional`



Risk Exposure filer

  * For margin trading, the margin rate should exceed a certain threshold as per leverage. For spot trading, the order size should be within the holding threshold. See [account_info](#get-account-information)



> **Response**
    
    
    {
        "success":true,
        "info":{
            "symbol":"PERP_ETH_USDT",
            "quote_min":0,
            "quote_max":10000,
            "quote_tick":0.01,
            "base_min":0.001,
            "base_max":5000,
            "base_tick":0.001,
            "min_notional":0,
            "price_range":0.03,
            "price_scope":0.4,
            "created_time":"1647838759.000",
            "updated_time":"1693437961.000",
            "is_stable":0,
            "is_trading":1,
            "precisions":[1,10,50,100,1000,10000],
            "is_prediction":0,
            "base_mmr":0.012,
            "base_imr":0.02
        }
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
  
## Available Symbols (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/info `

Get the available symbols that WOO X supports, and also send order rules for each symbol. The definition of rules can be found at [Exchange Infomation](#exchange-information)

> **Response**
    
    
    {
      "success": true,
      "rows": [
        {
          "created_time": "1575441595.65", // Unix epoch time in seconds
          "updated_time": "1575441595.65", // Unix epoch time in seconds
          "symbol": "SPOT_BTC_USDT",
          "quote_min": 100,
          "quote_max": 100000,
          "quote_tick": 0.01,
          "base_min": 0.0001,
          "base_max": 20,
          "base_tick": 0.0001,
          "min_notional": 0.02,
          "price_range": 0.99,
          "price_scope": 0.01,
          "precisions":[1,10,100,500,1000,10000]
        },
        // ...
      ]
    }
    

**Parameters**

None

## Market Trades (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/market_trades `

Get latest market trades. The response output "source" 1=internal (trade on WOO X), 0=external (trade from aggregrated sources)

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "symbol": "SPOT_ETH_USDT",
                "side": "BUY",
                "source": 0,
                "executed_price": 202,
                "executed_quantity": 0.00025,
                "executed_timestamp": "1567411795.000", // Unix epoch time in seconds
                "rpi": true
            },
            {
                "symbol": "SPOT_ETH_USDT",
                "side": "BUY",
                "source": 1,
                "executed_price": 202,
                "executed_quantity": 0.00025,
                "executed_timestamp": "1567411795.000", // Unix epoch time in seconds
                "rpi": true
            }
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
limit | number | N (default: 10) | Numbers of trades you want to query.  
  
## Market Trades History(Public)

**Limit: 1 requests per 1 second per IP address**

` GET https://api-pub.woo.org/v1/hist/trade `

Get historical market trades data. The response output "source" 1=internal (trade on WOO X), 0=external (trade from aggregrated sources)

> **Response**
    
    
    {
        "success": true,
        "data":{
            "rows": [
                {
                    "symbol": "SPOT_ETH_USDT",
                    "side": "BUY",
                    "source": 0,
                    "executed_price": 202,
                    "executed_quantity": 0.00025,
                    "executed_timestamp": "1567411795.000", // Unix epoch time in seconds
                    "rpi": true
                },
                {
                    "symbol": "SPOT_ETH_USDT",
                    "side": "BUY",
                    "source": 1,
                    "executed_price": 202,
                    "executed_quantity": 0.00025,
                    "executed_timestamp": "1567411795.000", // Unix epoch time in seconds
                    "rpi": true
                }
            ],
            "meta":{
                "total":10911159,
                "records_per_page":100,
                "current_page":1
            }
        },
        "timestamp":1669072422897
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
page | number | N (default: 1) |   
size | number | N (default: 25) |   
start_time | number | Y | start range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
symbol | string | Y |   
  
## Orderbook snapshot (Public)

**Limit: 10 requests per 1 second**

` GET /v1/public/orderbook/:symbol `

SNAPSHOT of current orderbook. Price of asks/bids are in descending order. Note: The original endpoint `GET /v1/orderbook/:symbol` can still be used.

> **Response**
    
    
    {
        "success": true,
        "asks": [
            {
                "price": 10669.4,
                "quantity": 1.56263218
            },
            {
                "price": 10670.3,
                "quantity": 0.36466977
            },
            {
                "price": 10670.4,
                "quantity": 0.06738009
            }
        ],
        "bids": [
            {
                "price": 10669.3,
                "quantity": 0.88159988
            },
            {
                "price": 10669.2,
                "quantity": 0.5
            },
            {
                "price": 10668.9,
                "quantity": 0.00488286
            }
        ],
        "timestamp": 1564710591905   // Unix epoch time in milliseconds
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
max_level | number | N (default: 100) | the levels you wish to show on both sides.  
  
## Kline (Public)

**Limit: 10 requests per 1 second**

` GET /v1/public/kline `

The latest klines of the trading pairs. Note: The original endpoint `GET /v1/kline` can still be used.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "open": 66166.23,
                "close": 66124.56,
                "low": 66038.06,
                "high": 66176.97,
                "volume": 23.45528526,
                "amount": 1550436.21725288,
                "symbol": "SPOT_BTC_USDT",
                "type": "1m",
                "start_timestamp": 1636388220000, // Unix epoch time in milliseconds
                "end_timestamp": 1636388280000
            },
            {
                "open": 66145.13,
                "close": 66166.24,
                "low": 66124.62,
                "high": 66178.60,
                "volume": 15.50705000,
                "amount": 1025863.18892610,
                "symbol": "SPOT_BTC_USDT",
                "type": "1m",
                "start_timestamp": 1636388160000,
                "end_timestamp": 1636388220000
            },
            // ...skip
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
type | enum | Y | `1m`/`5m`/`15m`/`30m`/`1h`/`4h`/`12h`/`1d`/`1w`/`1mon`/`1y`  
limit | number | N (default: 100) | Numbers of klines. Maximum of 1000 klines.  
  
## Kline - Historical Data (Public)

**Limit: 1 request per 1 second per IP**

` GET https://api-pub.woo.org/v1/hist/kline `

The historical klines of the trading pairs. Note that the endpoint is different with other APIs.

> **Response**
    
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "open": 66166.23,
                    "close": 66124.56,
                    "low": 66038.06,
                    "high": 66176.97,
                    "volume": 23.45528526,
                    "amount": 1550436.21725288,
                    "symbol": "SPOT_BTC_USDT",
                    "type": "1m",
                    "start_timestamp": 1636388220000, // Unix epoch time in milliseconds
                    "end_timestamp": 1636388280000
                },
                {
                    "open": 66145.13,
                    "close": 66166.24,
                    "low": 66124.62,
                    "high": 66178.60,
                    "volume": 15.50705000,
                    "amount": 1025863.18892610,
                    "symbol": "SPOT_BTC_USDT",
                    "type": "1m",
                    "start_timestamp": 1636388160000,
                    "end_timestamp": 1636388220000
                },
                // ...skip
            ],
            "meta":{
                "total":67377,
                "records_per_page":100,
                "current_page":1
            }
        },
        "timestamp": 1636388280000
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
type | enum | Y | `1m`/`5m`/`15m`/`30m`/`1h`/`4h`/`12h`/`1d`/`1w`/`1mon`  
start_time | number | Y | start range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_time | number | N | end range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
size | number | N (default: 100) | The page size, default 100  
page | number | N (default: 1) | the page you wish to query.  
  
## Available Token (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/token `

Get the available tokens that WOO X supports, it need to use when you call get deposit address or withdraw api.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "created_time": "1579399877.02", // Unix epoch time in seconds
                "updated_time": "1579399877.02", // Unix epoch time in seconds
                "token": "BTC",
                "delisted": false,
                "balance_token": "BTC",
                "fullname": "Bitcoin",
                "network": "BTC",
                "decimals": 8,
                "can_collateral":true,
                "can_short":true
            }
    
        ]
    }
    

**Parameters**

None

## Token Network (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/token_network `

Get the available networks for each token as well as the deposit/withdrawal information.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "protocol": "ERC20",
                "network": "ETH",
                "token": "1INCH",
                "name": "Ethereum (ERC20)",
                "minimum_withdrawal": 70,
                "withdrawal_fee": 35,
                "allow_deposit": 1,
                "allow_withdraw": 1
            },
            {
                "protocol": "ERC20",
                "network": "ETH",
                "token": "AAVE",
                "name": "Ethereum (ERC20)",
                "minimum_withdrawal": 0.12,
                "withdrawal_fee": 0.06,
                "allow_deposit": 1,
                "allow_withdraw": 1
            },
            {
                "protocol": "BEP20",
                "network": "BSC",
                "token": "ACE",
                "name": "BNB Smart Chain (BEP20)",
                "minimum_withdrawal": 5,
                "withdrawal_fee": 2.5,
                "allow_deposit": 1,
                "allow_withdraw": 1
            },
            {
                "protocol": "ADA",
                "network": "ADA",
                "token": "ADA",
                "name": "Cardano",
                "minimum_withdrawal": 24,
                "withdrawal_fee": 12,
                "allow_deposit": 1,
                "allow_withdraw": 1
            },
            // ...
        ]
    }
    

**Parameters**

None

## Get Predicted Funding Rate for All Markets (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/funding_rates `

Get predicted funding rate and the latest funding rate for all the markets.

> **Response**
    
    
    {
        "success":true,
        "rows": [
            {
                "symbol":"PERP_BTC_USDT",
                "est_funding_rate":-0.00001392,
                "est_funding_rate_timestamp":1681069199002,
                "last_funding_rate":-0.00001666,
                "last_funding_rate_timestamp":1681066800000,
                "next_funding_time":1681070400000,
                "last_funding_rate_interval":1,
                "est_funding_rate_interval":1
            },
            {
                "symbol":"PERP_ETH_USDT",
                "est_funding_rate":-0.00001394,
                "est_funding_rate_timestamp":1681069319011,
                "last_funding_rate":-0.00001661,
                "last_funding_rate_timestamp":1681066800000,
                "next_funding_time":1681070400000,
                "last_funding_rate_interval":1,
                "est_funding_rate_interval":1
            }
        ],
        "timestamp":1681069222726, // Unix epoch time in milliseconds
    }
    

## Get Predicted Funding Rate for One Market (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/funding_rate/:symbol `

Get predicted funding rate and the latest funding rate for one market.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
  
> **Response**
    
    
    {
        "success":true,
        "timestamp":1681069222726,
        "symbol":"PERP_BTC_USDT",
        "est_funding_rate":-0.00001392,
        "est_funding_rate_timestamp":1681069199002,
        "last_funding_rate":-0.00001666,
        "last_funding_rate_timestamp":1681066800000, // use rate to end calculating funding fee time
        "next_funding_time":1681070400000,
        "last_funding_rate_interval":1,
        "est_funding_rate_interval":1
    }
    

## Get Funding Rate History for One Market (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/funding_rate_history `

Get funding rate for one market.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp. If start_t and end_t are not filled, the newest funding rate will be returned.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp. If start_t and end_t are not filled, the newest funding rate will be returned.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
> **Response**
    
    
    {
        "success": true,
        "meta": {
            "total": 670,
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
            {
                "symbol": "PERP_BTC_USDT",
                "funding_rate": 0.12345689,
                "funding_rate_timestamp": 1567411795000, // use rate to end calculating funding fee time
                "next_funding_time": 1567411995000
            },
            {
                "symbol": "PERP_BTC_USDT",
                "funding_rate": 0.12345689,                                                 
                "funding_rate_timestamp": "1567411795.000", // use rate to end calculating funding fee time
                "next_funding_time": 1567411995000
            }
        ],
        "timestamp": 1564710591905 // Unix epoch time in milliseconds
    }
    

## Get Futures Info for All Markets (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/futures `

Get basic futures information for all the markets.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
              "symbol": "PERP_BTC_USDT",
                    "index_price": 56727.31344564,
                    "mark_price": 56727.31344564,
                    "est_funding_rate": 0.12345689,
                    "last_funding_rate": 0.12345689,
                    "next_funding_time": 1567411795000,
                    "open_interest": 0.12345689, // Open Interest is obtained in real-time.
                    "24h_open": 0.16112,
                    "24h_close": 0.32206,
                    "24h_high": 0.33000,
                    "24h_low": 0.14251,
                    "24h_volume": 89040821.98,
                    "24h_amount": 22493062.21
            },
            {
                "symbol": "PERP_ETH_USDT",
                    "index_price": 6727.31344564,
                    "mark_price": 6727.31344564,
                    "est_funding_rate": 0.12345689,
                    "last_funding_rate": 0.12345689,
                    "next_funding_time": 1567411795000,
                    "open_interest": 0.12345689,
                    "24h_open": 0.16112,
                    "24h_close": 0.32206,
                    "24h_high": 0.33000,
                    "24h_low": 0.14251,
                    "24h_volume": 89040821.98,
                    "24h_amount": 22493062.21
            }
        ],
        "timestamp": 1564710591905 // Unix epoch time in milliseconds
    }
    

## Get Futures for One Market (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/futures/:symbol `

Get basic futures information for one market.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
  
> **Response**
    
    
    {
        "success": true,
        "info":{
            "symbol": "PERP_BTC_USDT",
            "index_price": 56727.31344564,
            "mark_price": 56727.31344564,
            "est_funding_rate": 0.12345689,
            "last_funding_rate": 0.12345689,
            "next_funding_time": 1567411795000,
            "open_interest": 0.12345689,
            "24h_open": 0.16112,
           "24h_close": 0.32206,
           "24h_high": 0.33000,
           "24h_low": 0.14251,
           "24h_volume": 89040821.98,
           "24h_amount": 22493062.21
        },
        "timestamp": 1564710591905 // Unix epoch time in milliseconds
    }
    

## Token Config

**Limit: 10 requests per 1 second**

` GET /v1/client/token `

Get the configuration (collateral ratio, margin ratio factor etc) of the token.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "token": "BTC",
                "collateral_ratio": 0.85,
                "margin_factor": 2.3e-8,
                "futures_margin_factor": 2.3e-8,
                "collateral": true,        // if the token is now used as collateral
                "can_collateral": true,    // if the token can be used as collateral
                "can_short": true,         // if the token supports short selling
                "stable": false,            // if the token is stable coin or not
                'margin_max_leverage': 5, 
                'futures_max_leverage': 20, 
                'margin_max_position': 100000000000,
                'futures_max_position': 100000000000
            },
            {
                "token": "ETH",
                "collateral_ratio": 0.85,
                "margin_factor": 2.5e-8,
                "futures_margin_factor": 2.3e-8,
                "collateral": true,
                "can_collateral": true,
                "can_short": true,
                "stable": false, 
                'margin_max_leverage': 5, 
                'futures_max_leverage': 20, 
                'margin_max_position': 100000000000,
                'futures_max_position': 100000000000
            },
            {
                "token": "ASD",
                "collateral_ratio": 1,
                "margin_factor": 0,
                "futures_margin_factor": 0,
                "collateral": false,
                "can_collateral": false,
                "can_short": false,
                "stable": false, 
                'margin_max_leverage': 5, 
                'futures_max_leverage': 20, 
                'margin_max_position': 100000000000,
                'futures_max_position': 100000000000
            }
        ]
    }
    

**Parameters**

None

## Send Order

**Limit: 10 requests per 1 second**

` POST /v1/order `

Place order maker/taker, the order executed information will be updated from websocket stream. will respond immediately with an order created message.

`MARKET` type order behavior: it matches until all size is executed. If the size is too large (larger than the whole book) or the matching price exceeds the price limit (refer to `price_range`), then the remaining quantity will be cancelled.

`IOC` type order behavior: it matches as much as possible at the order_price. If not fully executed, then remaining quantity will be cancelled.

`FOK` type order behavior: if the order can be fully executed at the order_price then the order gets fully executed otherwise it would be cancelled without any execution.

`ASK` type order behavior: the order price is guaranteed to be the best ask price of the orderbook if it gets accepted.

`BID` type order behavior: the order price is guaranteed to be the best bid price of the orderbook if it gets accepted.

`RPI` type order behavior: only available to designated market makers. visible quantity must equal order quantity.

`visible_quantity` behavior: it sets the maximum quantity to be shown on orderbook. By default, it is equal to order_quantity, negative number and number larger than `order_quantity` is not allowed. If it sets to 0, the order would be hidden from the orderbook. It doesn't work for `MARKET`/`IOC`/`FOK` orders since orders with these types would be executed and cancelled immediately and not be shown on orderbook. For `LIMIT`/`POST_ONLY` order, as long as it's not complete, `visible_quantity` is the maximum quantity that is shown on the orderbook.

`order_amount` behavior: for `MARKET`/`BID`/`ASK` order, order can be placed by `order_amount` instead of `order_quantity`. It's the size of the order in terms of the quote currency instead of the base currency. The order would be rejected if both `order_amount` and `order_quantity` are provided. The precision of the number should be within 8 digits.

`client_order_id` behavior: customized order_id, a unique id among open orders. Orders with the same `client_order_id` can be accepted only when the previous one if completed, otherwise the order will be rejected.

For `MARKET`/`BID`/`ASK` order, if margin trading is disabled, `order_amount` is not supported when placing SELL order while `order_quantity` is not supported when placing BUY order.

For `Long`/ `Short` order, It is supported when position mode is HEDGE_MODE and the trading involves futures.

`reduce_only` behavior: only applicable to perpetual symbols. When reduce only is set to true, the system ensures that the order will reduce the position size rather than increasing it. To facilitate this, the system must group related orders to accurately manage the reduce only calculations. There is a cap of 50 orders that can be grouped together and if the limit is exceeded, the system will reject the incoming order.

> **Response**
    
    
    {
      "success": true,
      "order_id": 13,
      "client_order_id": 0,
      "order_type": "LIMIT",
      "order_price": 100.12,
      "order_quantity": 0.987654,
      "order_amount": null,
      "reduce_only": false,
      "timestamp": "1639980423.855" // Unix epoch time in seconds
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
client_order_id | number | N | number for scope : from 0 to 9223372036854775807. (default: 0)  
margin_mode | enum | N | `CROSS`/`ISOLATED`, defualt will be `CROSS`. The `ISOLATED` option only applicable to perp symbols, will be rejected if passed in for spot symbols   
order_tag | string | N | An optional tag for this order. (default: `default`)  
order_type | enum | Y | `LIMIT`/`MARKET`/`IOC`/`FOK`/`POST_ONLY`/`ASK`/`BID`/`RPI`  
post_only_adjusted | boolean | N | when order_type is `POST_ONLY`, `post_only_adjusted` can be true.  
order_price | number | N | If order_type is `MARKET`, then is not required, otherwise this parameter is required.  
order_quantity | number | N | For `MARKET`/`ASK`/`BID` order, if `order_amount` is given, it is not required.  
order_amount | number | N | For `MARKET`/`ASK`/`BID` order, the order size in terms of quote currency  
reduce_only | boolean | N | true or false, default false,If the user's RO order message contains 50 pending orders,the order can be created successfully placed.  
visible_quantity | number | N | The order quantity shown on orderbook. (default: equal to `order_quantity`)  
side | enum | Y | `SELL`/`BUY`  
position_side | enum | N | `SHORT`/`LONG`, If position mode is HEDGE_MODE and the trading involves futures,then is required, otherwise this parameter is not required.  
  
## Cancel all after

**Limit: 10 requests per 1 second**

` POST v1/order/cancel_all_after `

Provide a dead man switch to ensure user orders are canceled in case of an outage. If called repeatedly, the new timeout offset will replace the existing one if already set.When count down hits 0, all of the userâs ordinary and algo orders will be canceled.This API is only available to VIP users.Please reach out to customer service for more information.

> **Response**
    
    
    {
        "success": true,
        "data": {
            "expected_trigger_time": 1711534302938
        },
        "timestamp": 1711534302943
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
trigger_after | integer | Y | Timeout in ms. Max timeout can be set to 900000. To cancel this timer, set timeout to 0.  
  
## Cancel Order

**Limit: 10 requests per 1 second** shared with [cancel_order_by_client_order_id](#cancel-order-by-client_order_id)

` DELETE /v1/order `

Cancel order by order id. The order cancelled information will be updated from websocket stream. note that we give an immediate response with an order cancel sent message, and will update the cancel event via the websocket channel.

> **Response**
    
    
    {
      "success": true,
      "status": "CANCEL_SENT"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
order_id | number | Y | The `order_id` that you wish tocancel  
symbol | string | Y |   
  
## Cancel Order by client_order_id

**Limit: 10 requests per 1 second** shared with [cancel_order](#cancel-order)

` DELETE /v1/client/order `

Cancel order by client order id. The order cancelled information will be updated from websocket stream. note that we give an immediate response with an order cancel sent message, and will update the cancel event via the websocket channel.

Only the latest order with the `symbol` and `client_order_id` would be canceled.

> **Response**
    
    
    {
      "success": true,
      "status": "CANCEL_SENT"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
client_order_id | number | Y | The `client_order_id` that you wish tocancel  
symbol | string | Y |   
  
## Cancel Orders

**Limit: 10 requests per 1 second**

` DELETE /v1/orders `

Cancel orders by symbol.

> **Response**
    
    
    {
      "success": true,
      "status": "CANCEL_ALL_SENT"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
  
## Cancel All Pending Orders

**Limit: 10 requests per 1 second**

` DELETE /v3/orders/pending `

Cancel all pending ordinary orders.

> **Response**
    
    
    // success response
    {
        "success": true,
        "status": "CANCEL_ALL_SENT"
    }
    
    // Failed response
    {
        "success": false,
        "code": -1002,
        "message": "The request is unauthorized."
    }
    

## Get Order

**Limit: 10 requests per 1 second** shared with [get_order_by_client_order_id](#get-order-by-client-order-id)

` GET /v1/order/:oid `

Get specific order details by `order_id`. The `realized_pnl` field in response will only present the settled amount for futures orders.

> **Response**
    
    
    {
        "success": true,
        "created_time": "1577349119.33", // Unix epoch time in seconds
        "side": "SELL",
        "status": "FILLED",
        "symbol": "PERP_BTC_USDT",
        "client_order_id": 0,
        "reduce_only": false,
        "order_id": 1,
        "order_tag": "default",
        "type": "LIMIT",
        "price": 123,
        "quantity": 0.1,
        "amount": null,
        "visible": 0.1,
        "executed": 0.1,
        "total_fee": 0.00123,  // represents the cumulative fees for the entire order
        "fee_asset": "USDT",
        "average_executed_price": 123,
        "realized_pnl":null,
        'total_rebate': 0,   // indicates the aggregate rebates for the entire order
        'rebate_asset': null, 
        "position_side":'SHORT',
        'margin_mode':'CROSS', 
        'leverage':20, 
    
        // Detail transactions of this order
        "Transactions": [
            {
                "id": 2,
                "symbol": "PERP_BTC_USDT",
                "fee": 0.0001,   // fee for a single transaction
                "fee_asset": "usdt", // fee. use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
                "side": "BUY",
                "order_id": 1,
                "executed_price": 123,
                "executed_quantity": 0.05,
                "executed_timestamp": "1567382401.000", // Unix epoch time in seconds
                "is_maker": 1
            }]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
oid | number | Y | The order_id `oid` that you wish to query  
  
## Get Order by client_order_id

**Limit: 10 requests per 1 seconds** shared with [get_order](#get-order)

` GET /v1/client/order/:client_order_id `

Get specific order details by `client_order_id`. If there is more than one order with the same `client_order_id`, return the latest one. The `realized_pnl` field in response will only present the settled amount for futures orders.

> **Response**
    
    
    {
        "success": true,
        "created_time": "1577349119.33", // Unix epoch time in seconds
        "side": "SELL",
        "status": "FILLED",
        "symbol": "SPOT_BTC_USDT",
        "client_order_id": 123,
        "reduce_only": false,
        "order_id": 1,
        "order_tag": "default",
        "type": "LIMIT",
        "price": 123,
        "quantity": 0.1,
        "amount": null,
        "visible": 0.1,
        "executed": 0.1,
        "total_fee": 0.00123,   // represents the cumulative fees for the entire order
        "fee_asset": "USDT",
        "average_executed_price": 123,
        "realized_pnl":null,
        'total_rebate': 0,    // indicates the aggregate rebates for the entire order
        'rebate_asset': null,
        'margin_mode':'CROSS', 
        'leverage':20, 
    
        // Detail transactions of this order
        "Transactions": [
            {
                "id": 2,
                "symbol": "SPOT_BTC_USDT",
                "fee": 0.0001,    // fee for a single transaction
                "fee_asset": "BTC", // fee. use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
                "side": "BUY",
                "order_id": 1,
                "executed_price": 123,
                "executed_quantity": 0.05,
                "executed_timestamp": "1567382401.000", // Unix epoch time in seconds
                "is_maker": 1
            }]
    
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
client_order_id | number | Y | customized order_id when placing order  
  
## Get Orders

**Limit: 10 requests per 1 second**

` GET /v1/orders `

Get orders by customize conditions.  
\- `INCOMPLETE` = `NEW` \+ `PARTIAL_FILLED`  
\- `COMPLETED` = `CANCELLED` \+ `FILLED` \+ `REJECTED` The `realized_pnl` field in response will only present the settled amount for futures orders. The return value default is null unless the input parameter `realized_pnl` set to `true`

> **Response**
    
    
    {
        "success": true,
        "meta": {
            "total": 31,
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
            {
                "side": "SELL",
                "status": "CANCELLED",
                "symbol": "SPOT_BCHABC_USDT",
                "client_order_id": 123,
                "reduce_only": false,
                "order_id": 8197,
                "order_tag": "default",
                "type": "LIMIT",
                "price": 308.51,
                "quantity": 0.0019,
                "amount": null,
                "visible": 0.0019,
                "executed": 0,
                "total_fee": 0,
                "fee_asset": null,
                'total_rebate': 0,
                'rebate_asset': null,
                "created_time": "1575014255.089", // Unix epoch time in seconds
                "updated_time": "1575014255.910", // Unix epoch time in seconds
                "average_executed_price": null,
                "position_side": "LONG",  
                "realized_pnl":null,
                'margin_mode':'CROSS', 
                'leverage':20, 
            },
            // ....skip (total 25 items in one page)
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | N |   
side | string | N | `BUY`/`SELL`  
size | number | N | The page size, default 100, max 500.  
order_type | string | N | `LIMIT`/`MARKET`/`IOC`/`FOK`/`POST_ONLY`/`LIQUIDATE`/`RPI`/`LIQUIDATE_BLP`/`ADL`  
order_tag | string | N | An optional tag for this order.  
realized_pnl | boolean | N | Decide if return data calculate realized pnl value for the futures order.  
status | enum | N | `NEW`/`CANCELLED`/`PARTIAL_FILLED`/`FILLED`/`REJECTED`/`INCOMPLETE`/`COMPLETED`  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
  
## Edit Order

**Limit: 5 requests per 1 second**

` PUT /v3/order/:order_id `

_**Note that for v3 API with json body POST method, please follow the instruction in[authentication](#authentication) section for `v3` API to generate the signature. *_*Please use `string` type for value input field to remain data accurancy.

The API allow you to edit the price and the quantity of the selected order. You must input at least one of it in the request body.

> **Response**
    
    
    // Success response
    {
        "success": true,
        "data": {
            "success": true,
            "status": "EDIT_SENT"
        },
        "timestamp": 1673842319229
    }
    
    // Failed response
    {
        "success": false,
        "code": -1103,
        "message": "The order does not meet the price filter requirement."
    }
    

> **Request**
    
    
    {
        "price": "10.5",
        "quantity": "1.4"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
order_id | number | Y | The `order_id` that you wish to query  
price | string | N | New price of the order.  
quantity | string | N | New quantity of the order.  
  
## Edit Order by client_order_id

**Limit: 5 requests per 1 second**

` PUT /v3/order/client/:client_order_id `

_**Note that for v3 API with json body POST method, please follow the instruction in[authentication](#authentication) section for `v3` API to generate the signature. *_*Please use `string` type for value input field to remain data accurancy.

The API allow you to edit the price and the quantity of the selected order. You must input at least one of it in the request body.

> **Response**
    
    
    // Success response
    {
        "success": true,
        "data": {
            "success": true,
            "status": "EDIT_SENT"
        },
        "timestamp": 1673842319229
    }
    
    // Failed response
    {
        "success": false,
        "code": -1103,
        "message": "The order does not meet the price filter requirement."
    }
    

> **Request**
    
    
    {
        "price": "10.5",
        "quantity": "1.4"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
client_order_id | number | Y | customized order_id when placing order  
price | string | N | New price of the order.  
quantity | string | N | New quantity of the order.  
  
## Send Algo Order

**Limit: 2 requests per 1 second**

` POST /v3/algo/order `

_**Note that for v3 API, please follow the instruction in[authentication](#authentication) section for `v3` API to generate the signature. *_*Please use `string` type for value input field to remain data accurancy.

Place algo order maker/taker, the order executed information will be updated from websocket stream. will respond immediately with an order created message.

To place `Stop Market` order, please use 'STOP' as `algoType` and 'MARKET' as `type`. Please input the trigger price in `triggerPrice` field.

To place `Stop Limit` order, please use 'STOP' as `algoType` and 'LIMIT' as `type`. Please input the trigger price in `triggerPrice` field.

To place `Trailing Stop` order, please use 'TRAILING_STOP' as `algoType` and 'MARKET' as `type`. Please also input your trailing rate setting in `callbackRate` field.

To place `OCO` order, the input fields is 2 layer and includes an array of the objects named `childOrder`. The second order of OCO order should be a STOP_LIMIT or STOP MARKET order object in the array. please use 'OCO' as `algoType` in outter parameters, 'STOP' as `algoType` in `childOrder` object, and 'LIMIT' or 'MARKET' as type.

To place `Positional TP/SL` order, the input fields is 2 layer and includes an array of the objects named `childOrder`. The take-profit or stop-loss order should be the objects in the array. For the sub-order in `childOrder`, please input 'CLOSE_POSITION' as `type`, and 'TAKE_PROFIT' or 'STOP_LOSS' in `algoType` field.

`visible_quantity` behavior: it sets the maximum quantity to be shown on orderbook. By default, it is equal to order_quantity, negative number and number larger than `order_quantity` is not allowed. The visibility of the childOrder will inherit the parent order's visibility setting. If it sets to 0, the order would be hidden from the orderbook. It doesn't work for `MARKET` orders since orders with these types would be executed and cancelled immediately and not be shown on orderbook. For `LIMIT` order, as long as it's not complete, `visible_quantity` is the maximum quantity that is shown on the orderbook.

`client_order_id` behavior: customized order_id, a unique id among open orders. Orders with the same `client_order_id` can be accepted only when the previous one if completed, otherwise the order will be rejected.

For `Long`/ `Short` order, It is supported when position mode is HEDGE_MODE and the trading involves futures.

`reduce_only` behavior: only applicable to perpetual symbols. When reduce only is set to true, the system ensures that the order will reduce the position size rather than increasing it. To facilitate this, the system must group related orders to accurately manage the reduce only calculations. There is a cap of 50 orders that can be grouped together and if the limit is exceeded, the system will reject the incoming order. For algo orders, the check happens when the order gets triggered.

> **Response**
    
    
    {
      "code": 0,
      "data": {
        "rows": [
          {
            "algoType": "string",
            "clientOrderId": 0,
            "orderId": 0,
            "quantity": 0
          }
        ]
      },
      "message": "string",
      "success": true,
      "timestamp": 0
    }
    
    // bracket order response
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "orderId": 432132,
                    "clientOrderId": 0,
                    "algoType": "TAKE_PROFIT",
                    "quantity": 0
                },
                {
                    "orderId": 432133,
                    "clientOrderId": 0,
                    "algoType": "STOP_LOSS",
                    "quantity": 0
                },
                {
                    "orderId": 432131,
                    "clientOrderId": 0,
                    "algoType": "POSITIONAL_TP_SL",
                    "quantity": 0
                },
                {
                    "orderId": 432130,
                    "clientOrderId": 0,
                    "algoType": "BRACKET",
                    "quantity": 10
                }
            ]
        },
        "timestamp": 1676283560233
    }
    
    

> **Request**
    
    
    // stop market order
    
    {
        "symbol":"PERP_BTC_USDT",
        "side":"BUY",
        "orderCombinationType":"STOP_MARKET",
        "algoType":"STOP",
        "triggerPrice":"1000",
        "type":"MARKET",
        "quantity":"0.01"
    }
    
    //stop market limit
    
    {
        "symbol":"PERP_BTC_USDT",
        "side":"BUY",
        "orderCombinationType":"STOP_LIMIT",
        "algoType":"STOP",
        "triggerPrice":"1000",
        "type":"LIMIT",
        "quantity":"0.01",
        "price":1000
    }
    
    //OCO 
    
    {
        "symbol": "PERP_ETH_USDT",
        "side": "BUY",
        "reduceOnly": false,
        "type": "LIMIT",
        "quantity": "1",
        "algoType": "OCO",
        "price": "1000",
        "childOrders": [
            {
                "side": "BUY",
                "algoType": "STOP",
                "triggerPrice": "1600",
                "type": "MARKET"
            }
        ]
    }
    
    //Positional TP/SL
    
    {
        "symbol": "SPOT_BAL_USDT",
        "reduceOnly": false,
        "algoType": "POSITIONAL_TP_SL",
        "childOrders": [
            {
                "algoType": "TAKE_PROFIT",
                "type": "CLOSE_POSITION",
                "side": "BUY",
                "reduceOnly": true,
                "triggerPrice": "72"
            },
            {
                "algoType": "STOP_LOSS",
                "type": "CLOSE_POSITION",
                "side": "BUY",
                "reduceOnly": true,
                "triggerPrice": "74"
            }
        ]
    }
    
    // Bracket order
    
    {
        "symbol": "SPOT_BAL_USDT",
        "side": "BUY",
        "reduceOnly": false,
        "type": "LIMIT",
        "quantity": "1",
        "algoType": "BRACKET",
        "price": "69",
        "childOrders": [
            {
                "symbol": "SPOT_BAL_USDT",
                "reduceOnly": false,
                "algoType": "POSITIONAL_TP_SL",
                "childOrders": [
                    {
                        "algoType": "TAKE_PROFIT",
                        "type": "CLOSE_POSITION",
                        "side": "SELL",
                        "reduceOnly": true,
                        "triggerPrice": "76"
                    },
                    {
                        "algoType": "STOP_LOSS",
                        "type": "CLOSE_POSITION",
                        "side": "SELL",
                        "reduceOnly": true,
                        "triggerPrice": "50"
                    }
                ]
            }
        ]
    }
    

**Parameters - Parent**

Name | Type | Required | Description  
---|---|---|---  
activatedPrice | string | N | activated price for algoType=TRAILING_STOP  
algoType | string | Y | `STOP/OCO/TRAILING_STOP/BRACKET`  
marginMode | enum | N | `CROSS`/`ISOLATED`, defualt will be `CROSS`. The `ISOLATED` option only applicable to perp symbols, will be rejected if passed in for spot symbols   
callbackRate | string | N | callback rate, only for algoType=TRAILING_STOP, i.e. the value = 0.1 represent to 10%.  
callbackValue | string | N | callback value, only for algoType=TRAILING_STOP, i.e. the value = 100  
childOrders | child | N | Child orders for algoType=`POSITIONAL_TP_SL`  
symbol | string | Y |   
clientOrderId | number | N | Client order id defined by client,number for scope : from 0 to 9223372036854775807. (default: 0), duplicated client order id on opening order is not allowed.  
orderTag | string | N | An optional tag for this order. (default: `default`)  
price | string | N | order price  
quantity | string | N | Order quantity, only optional for algoType=`POSITIONAL_TP_SL`  
reduceOnly | boolean | N | true or false, default false.If the user's RO order message contains 50 pending orders,the order can be created successfully placed.  
triggerPrice | string | N | trigger price, if algoType=TRAILING_STOP, you need to provide 'activatedPrice'  
triggerPriceType | string | N | trigger price, default `MARKET_PRICE`, enum: `MARKET_PRICE`  
type | string | Y | `LIMIT`/`MARKET`  
visibleQuantity | number | N | The order quantity shown on orderbook. (default: equal to `orderQuantity`)  
side | enum | Y | `SELL`/`BUY`  
positionSide | enum | N | `SHORT`/`LONG`, If position mode is HEDGE_MODE and the trading involves futures,then is required, otherwise this parameter is not required.  
  
**Parameters - Child**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
algoType | string | Y | `STOP`/`OCO`/`TRAILING_STOP`/`BRACKET`/`POSITIONAL_TP_SL` ï½  
side | enum | Y | `SELL`/`BUY`  
type | string | Y | `LIMIT`/`MARKET`  
triggerPrice | string | N | trigger price, if algoType=TRAILING_STOP, you need to provide 'activatedPrice'  
price | string | N | order price  
reduceOnly | boolean | N | true or false, default false,If the user's RO order message contains 50 pending orders,the order can be created successfully placed.  
childOrders | child | N | Child orders for algoType=`POSITIONAL_TP_SL`  
  
## Cancel Algo Order

**Limit: 10 requests per 1 second** shared with [cancel_algo_order_by_client_order_id](#cancel-algo-order-by-client_order_id)

` DELETE /v3/algo/order/:order_id `

***Note: This v3 API using query string to pass parameter, please follow the instruction in [authentication](#authentication) section for `v3` API to generate the signature. Cancel order by order id. The order cancelled information will be updated from websocket stream. note that we give an immediate response with an order cancel sent message, and will update the cancel event via the websocket channel.

> **Response**
    
    
    // Success response
    {
        "success": true,
        "status": "CANCEL_SENT"
    }
    
    // Failed response
        "success": false,
        "code": -1006,
        "message": "Your order and symbol are not valid or already canceled."
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
order_id | number | Y | The `order_id` that youwish to cancel  
  
## Cancel All Pending Algo Orders

**Limit: 10 requests per 1 second**

` DELETE /v3/algo/orders/pending `

***Note: This v3 API using query string to pass parameter, please follow the instruction in [authentication](#authentication) section for `v3` API to generate the signature. Cancel all pending algo orders.

> **Response**
    
    
    // Success response
    {
        "success": true,
        "status": "CANCEL_SENT"
    }
    
    // Failed response
        "success": false,
        "code": -1006,
        "message": "Your order and symbol are not valid or already canceled."
    }
    

## Cancel Pending Merge Orders by Symbol

**Limit: 10 requests per 1 second**

` DELETE /v3/merge/orders/pending/:symbol `

***Note that for v3 API, please follow the instruction in [authentication](#authentication) section for `v3` API to generate the signature. Cancel both ordinary and algo orders by symbol.

> **Response**
    
    
    {
      "success": true,
      "status": "CANCEL_ALL_SENT"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
side | string | N (default: cancel both sides) | BUY or SELL  
symbol | string | Y |   
marginMode | string | N (default:CROSS) | CROSS or ISOLATED  
  
## Get Algo Order

**Limit: 10 requests per 1 second** shared with [get_algo_order_by_client_order_id](#get-algo-order-by-client-order-id)

` GET /v3/algo/order/:oid ` ***Note: This v3 API using query string to pass parameter, please follow the instruction in [authentication](#authentication) section for `v3` API to generate the signature.

Get specific order details by Algo order's `oid`.

> **Response**
    
    
    // Success response
    {
        "success": true,
        "data": {
            "algoOrderId": 431601,
            "clientOrderId": 0,
            "rootAlgoOrderId": 431601,
            "parentAlgoOrderId": 0,
            "symbol": "SPOT_ADA_USDT",
            "orderTag": "default",
            "algoType": "BRACKET",
            "side": "BUY",
            "quantity": 11,
            "isTriggered": false,
            "triggerStatus": "SUCCESS",
            "type": "LIMIT",
            "status": "FILLED",
            "rootAlgoStatus": "FILLED",
            "algoStatus": "FILLED",
            "triggerPriceType": "MARKET_PRICE",
            "price": 0.33,
            "triggerTime": "0",
            "totalExecutedQuantity": 11,
            "averageExecutedPrice": 0.33,
            "totalFee": 0.0033,
            "feeAsset": "ADA",
            "totalRebate":0,
            "rebateAsset":"",
            "reduceOnly": false,
            "createdTime": "1676277825.917",
            "updatedTime": "1676280901.229",
            "positionSide":"LONG",
            'marginMode':'CROSS', 
            'leverage':20, 
    
        },
        "timestamp": 1676281474630
    }
    
    // Failed response
    {
        "success": false,
        "code": -1006,
        "message": "The order can not be found."
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
oid | number | Y | The Algo order's order_id `oid` that you wish to query  
  
## Get Algo Orders

**Limit: 10 requests per 1 second**

` GET /v3/algo/orders `

***Note: This v3 API using query string to pass parameter, please follow the instruction in [authentication](#authentication) section for `v3` API to generate the signature. Get orders by customize conditions.  
\- `INCOMPLETE` = `NEW` \+ `PARTIAL_FILLED`  
\- `COMPLETED` = `CANCELLED` \+ `FILLED` \+ `REJECTED` The `realizedPnl` field in response will only present the settled amount for futures orders. The return value default is null unless the input parameter `realizedPnl` set to `true`

> **Response**
    
    
    {
      "success": true,
      "data": {
        "rows": [
          {
            "leverage": 10,
            "algoOrderId": 2081697,
            "clientOrderId": 0,
            "rootAlgoOrderId": 2081697,
            "parentAlgoOrderId": 0,
            "symbol": "PERP_WOO_USDT",
            "orderTag": "default",
            "algoType": "POSITIONAL_TP_SL",
            "side": "BUY",
            "quantity": 0,
            "isTriggered": false,
            "triggerStatus": "NEW",
            "rootAlgoStatus": "NEW",
            "algoStatus": "NEW",
            "triggerPriceType": "USELESS",
            "triggerTime": "0",
            "totalExecutedQuantity": 0,
            "visibleQuantity": 0,
            "averageExecutedPrice": 0,
            "totalFee": 0,
            "feeAsset": "",
            "totalRebate": 0,
            "rebateAsset": "",
            "reduceOnly": false,
            "createdTime": "1720589170.566",
            "updatedTime": "1720589616.276",
            "isActivated": true,
            "childOrders": [
              {
                "leverage": 10,
                "algoOrderId": 2081698,
                "clientOrderId": 0,
                "rootAlgoOrderId": 2081697,
                "parentAlgoOrderId": 2081697,
                "symbol": "PERP_WOO_USDT",
                "orderTag": "default",
                "algoType": "TAKE_PROFIT",
                "side": "BUY",
                "quantity": 0,
                "isTriggered": false,
                "triggerPrice": 0.14977,
                "triggerStatus": "USELESS",
                "type": "CLOSE_POSITION",
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "triggerPriceType": "MARK_PRICE",
                "triggerTime": "0",
                "totalExecutedQuantity": 0,
                "visibleQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeAsset": "",
                "totalRebate": 0,
                "rebateAsset": "",
                "reduceOnly": true,
                "createdTime": "1720589170.561",
                "updatedTime": "1720589616.268",
                "isActivated": true,
                "positionSide": "SHORT",
                "marginMode": "ISOLATED"
              },
              {
                "leverage": 10,
                "algoOrderId": 2081699,
                "clientOrderId": 0,
                "rootAlgoOrderId": 2081697,
                "parentAlgoOrderId": 2081697,
                "symbol": "PERP_WOO_USDT",
                "orderTag": "default",
                "algoType": "STOP_LOSS",
                "side": "BUY",
                "quantity": 0,
                "isTriggered": false,
                "triggerPrice": 0.22465,
                "triggerStatus": "USELESS",
                "type": "CLOSE_POSITION",
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "triggerPriceType": "MARK_PRICE",
                "triggerTime": "0",
                "totalExecutedQuantity": 0,
                "visibleQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeAsset": "",
                "totalRebate": 0,
                "rebateAsset": "",
                "reduceOnly": true,
                "createdTime": "1720589170.564",
                "updatedTime": "1720589616.270",
                "isActivated": true,
                "positionSide": "SHORT",
                "marginMode": "ISOLATED"
              }
            ],
            "positionSide": "SHORT",
            "marginMode": "ISOLATED"
          }
        ],
        "meta": {
          "total": 3,
          "records_per_page": 25,
          "current_page": 1
        }
      },
      "timestamp": 1720589635338
    }
    
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
algoType | string | Y | `STOP/OCO/TRAILING_STOP/BRACKET`  
createdTimeEnd | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
createdTimeStart | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
isTriggered | boolean | N | true or false  
orderTag | string | N | An optional tag for this order.  
page | number | N (default: 1) | pag of query pagination  
realizedPnl | boolean | N | Decide if return data calculate realized pnl value for the futures order.  
side | string | N | `BUY`/`SELL`  
size | number | N (default: 25) | size for query pagination  
status | enum | N | `NEW`/`CANCELLED`/`PARTIAL_FILLED`/`FILLED`/`REJECTED`/`INCOMPLETE`/`COMPLETED`  
symbol | string | N |   
orderType | string | N | `LIMIT`/`MARKET`  
  
## Edit Algo Order

**Limit: 5 requests per 1 second**

` PUT /v3/algo/order/:order_id `

_**Note that for v3 API with json body POST method, please follow the instruction in[authentication](#authentication) section for `v3` API to generate the signature. *_*Please use `string` type for value input field to remain data accurancy.

The API allow you to edit the trigger price and the quantity of the selected algo order. You must input at least one of it in the request body.

> **Response**
    
    
    {
        "success": true,
        "data": {
            "success": true,
            "status": "EDIT_SENT"
        },
        "timestamp": 1676277871935
    }
    

> **Request**
    
    
    {
      "activatedPrice": "200",
      "callbackRate": "200",
      "callbackValue": "200",
      "childOrders": [
        {
          "algoOrderId": 123456,
          "price": "1000",
          "quantity": "1000",
          "triggerPrice": "1000"
        }
      ],
      "price": "1000",
      "quantity": "1000",
      "triggerPrice": "1000"
    }
    
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
oid | number | Y | The order_id `oid` that you wish to query  
activatedPrice | string | N | activated price for algoType=TRAILING_STOP  
callbackRate | string | N | new callback rate, only for algoType=TRAILING_STOP, i.e. the value = 0.1 represent to 10%.  
callbackValue | string | N | new callback value, only for algoType=TRAILING_STOP, i.e. the value = 100  
childOrders | array | N | The array list of the child orders, only for algoType=POSITIONAL_TP_SL or TP_SL  
price | number | N | New price of the algo order.  
quantity | number | N | New quantity of the algo order.  
triggerPrice | number | N | New trigger price of the algo order.  
  
## Edit Algo Order by client_order_id

**Limit: 5 requests per 1 second**

` PUT /v3/algo/order/client/:client_order_id `

_**Note that for v3 API with json body POST method, please follow the instruction in[authentication](#authentication) section for `v3` API to generate the signature. *_*Please use `string` type for value input field to remain data accurancy.

The API allow you to edit the price and the quantity of the selected algo order. You must input at least one of it in the request body.

> **Response**
    
    
    {
      "code": 0,
      "data": {
        "status": "string",
        "success": true
      },
      "message": "string",
      "success": true,
      "timestamp": 0
    }
    

> **Request**
    
    
    {
      "activatedPrice": "200",
      "callbackRate": "200",
      "callbackValue": "200",
      "childOrders": [
        {
          "algoOrderId": 123456,
          "price": "1000",
          "quantity": "1000",
          "triggerPrice": "1000"
        }
      ],
      "price": "1000",
      "quantity": "1000",
      "triggerPrice": "1000"
    }
    
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
oid | number | Y | The order_id `oid` that you wish to query  
activatedPrice | string | N | activated price for algoType=TRAILING_STOP  
callbackRate | string | N | new callback rate, only for algoType=TRAILING_STOP, i.e. the value = 0.1 represent to 10%.  
callbackValue | string | N | new callback value, only for algoType=TRAILING_STOP, i.e. the value = 100  
childOrders | array | N | The array list of the child orders, only for algoType=POSITIONAL_TP_SL or TP_SL  
price | number | N | New price of the algo order.  
quantity | number | N | New quantity of the algo order.  
triggerPrice | number | N | New trigger price of the algo order.  
  
## Get Trade

**Limit: 10 requests per 1 second**

` GET /v1/client/trade/:tid `

Get specific transaction detail by `id`. (The data fetch from this API only contains past 3 months data, if you need the data more than 3 months, please submit the ticket in the support center).

> **Response**
    
    
    {
        "success": true,
        "id": 1,
        "symbol": "SPOT_BTC_USDT",
        "fee": 0.0001,
        "fee_asset": "BTC", // fee. use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
        "side": "BUY",
        "order_id": 2,
        "executed_price": 123,
        "executed_quantity": 0.05,
        "is_maker": 0,
        "executed_timestamp": "1567382400.000",  // Unix epoch time in seconds
        "is_match_rpi": true
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
tid | number | Y | The transaction id `tid` that you wish to query  
  
## Get Trades

**Limit: 10 requests per 1 second**

` GET /v1/order/:oid/trades `

Get trades by `order_id`

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "id": 5, // transaction id
                "symbol": "SPOT_BTC_USDT",
                "order_id": 211,
                "order_tag": "default",
                "executed_price": 10892.84,
                "executed_quantity": 0.002,
                "is_maker": 0,
                "side": "SELL",
                "fee": 0,
                "fee_asset": "USDT", // use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
                "executed_timestamp": "1566264290.250",  // Unix epoch time in seconds
                "is_match_rpi": true
            }
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
oid | number | Y | The order id `oid` that you wish to query  
  
## Get Trade History

**Limit: 10 requests per 1 second**

` GET /v1/client/trades `

Return clientâs trade history in a range of time. (The data fetch from this API only contains past 3 months data, if you need the data more than 3 months, please user [Get Archived Trade History](#get-archived-trade-history)).

> **Response**
    
    
    {
        "success": true,
        "meta": {
            "total": 31,
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
            {
                "id": 5, // transaction id
                "symbol": "SPOT_BTC_USDT",
                "order_id": 211,
                "order_tag": "default",
                "executed_price": 10892.84,
                "executed_quantity": 0.002,
                "is_maker": 0,
                "side": "SELL",
                "fee": 0,
                "fee_asset": "USDT", // use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
                "executed_timestamp": "1566264290.250",  // Unix epoch time in seconds
                "is_match_rpi": true
            },
            // ....skip (total 25 items in one page)
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | N |   
order_tag | string | N | An optional tag for this order.  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
## Get Archived Trade History

**Limit: 1 requests per 1 second**

` GET /v1/client/hist_trades `

Return clientâs trade history in a range of time. (The data fetch from this API contains all time historical data).

> **Response**
    
    
    {
        "success": true,
        "data": [
            {
                "id": 217714629, // transaction id
                "symbol": "SPOT_BTC_USDT",
                "order_id": 211,
                "order_tag": "default",
                "executed_price": 10892.84,
                "executed_quantity": 0.002,
                "is_maker": 0,
                "side": "SELL",
                "fee": 0,
                "fee_asset": "USDT", // use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
                "executed_timestamp": "1566264290.250",  // Unix epoch time in seconds
                "is_match_rpi": true
            },
            // ....skip (total 25 items in one page)
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | N |   
start_t | timestamp | Y | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | Y | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
fromId | number | N (default: 1) | fromId is the trade id of the the record. It should be use as a cursor, so searching for trades starting with that trade id query.  
limit | number | N (default: 25) |   
  
## Get Current Holding

**Limit: 10 requests per 1 seconds**

` GET /v1/client/holding `

Holding summary of the client. Note that the number in holding could be negative, it means how much the client owes to WOO X.

> **Response**
    
    
    {
        "success": true,
        "holding": {
            "BTC": 1.014,
            "USDT": -26333.207589999998,
            "BCHABC": 2
        }
    }
    

**Parameters**

None

## Get Current Holding v2

**Limit: 10 requests per 1 seconds**

` GET /v2/client/holding `

** Note: This API will be deprecated at the end of 2023 Q1, please find the replacement API in  [Get Current Holding Get Balance - New](#get-current-holding-get-balance-new) Holding summary of client. Note that the number in holding could be negative, it means how much client owed to WOO X.

> **Response**
    
    
    {
        "holding":[
            {
                "token":"BTC",
                "holding":0.00590139,
                "frozen":0.0,
                "interest":0.0,
                "outstanding_holding":-0.00080,
                "pending_exposure":0.0,
                "opening_cost":-126.36839957,
                "holding_cost":-125.69703515,
                "realised_pnl":73572.86125165,
                "settled_pnl":73573.5326161,
                "fee_24_h":0.01432411,
                "settled_pnl_24_h":0.67528081,
                "updated_time":"1675220398"
            },{
                "token":"UNI",
                "holding":0.00000000,
                "frozen":0.00000000,
                "interest":0.00000000,
                "outstanding_holding":0.00000000,
                "pending_exposure":0.00000000,
                "opening_cost":0,
                "holding_cost":0,
                "realised_pnl":0,
                "settled_pnl":0,
                "fee_24_h":0,
                "settled_pnl_24_h":0,
                "updated_time":"1655269545"
            }   
        ],
        "success":true
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
all | enum | N | `true`/`false`. If `true` then will return all tokens even if balance is empty.  
  
## Get Current Holding (Get Balance) - New

**Limit: 100 requests per 1 mins**

` GET /v3/balances `

Holding summary of client. Note that the number in holding could be negative, it means how much client owed to WOO X. The API is design to replace the legacy API [Get Current Holding](#get-current-holding) and [Get Current Holding v2](#get-current-holding-v2)

> **Response**
    
    
    {
      "success": true,
      "data": {
        "holding": [
          {
            "token": "WOO",
            "holding": 169684.96645139,
            "frozen": 0.0,
            "staked": 1304330.65079109,
            "unbonding": 0.0,
            "vault": 0.0,
            "interest": 0.0,
            "pendingShortQty": 0.0,
            "pendingLongQty": 0.0,
            "availableBalance": 169684.96645139,
            "averageOpenPrice": 0.0,
            "markPrice": 0.22446,
            "launchpadVault": 0.0,
            "earn": 0.0,
            "pnl24H": 0.0,
            "fee24H": 0.0,
            "updatedTime": 1715126422.125
          }
        ],
        "userId": 11446,
        "applicationId": "1ca13dff-f2d6-4fa4-a382-5ce1a79b2bc0"
      },
      "timestamp": 1715197222107
    }
    

**Parameters**

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | N | Use the parameter in query string format (i.e. /v3/balance?token=WOO). If the parameter is empty (or not passed) it will return all token's holding.  
  
## Get Account Information

**Limit: 10 requests per 60 seconds**

` GET /v1/client/info `

** Note: This API will be deprecated at the end of 2023 Q1, please find the replacement API in  [Get Account Information - New](#get-account-information-new) Get account information such as account name, leverage, current exposure ... etc.

> **Response**
    
    
    {
    
        "success": true,
        "application": {
            "application_id": "8935820a-6600-4c2c-9bc3-f017d89aa173",
            "account": "CLIENT_ACCOUNT_01",
            "alias": "CLIENT_ACCOUNT_01",
            "account_mode":"FUTURES" //account mode
            "leverage": 5,
            "taker_fee_rate": 0,
            "maker_fee_rate": 0,
            "futures_leverage": 5,
            "futures_taker_fee_rate": 0,
            "futures_maker_fee_rate": 0,
            "otpauth": false
        },
        "margin_rate": 1000
    }
    

**Parameters**

None

## Get Account Information - New

**Limit: 10 requests per 60 seconds**

` GET /v3/accountinfo `

Get account information such as account name, leverage, current exposure ... etc. The API is design to replace the legacy API [Get Account Information](#get-account-information)

The `referrerID` in the response represent the referral code that the user used to sign up, subaccount would pass main account referrerID. The `accountType` in the response represent the account type is `Main` account or `Subaccount`

> **Response**
    
    
    {
        "success": true,
        "data": {
            "applicationId": "f5f485c7-6ca5-4189-8efe-e842cdc50498",
            "account": "",
            "alias": "",
            "accountMode": "FUTURES",
            "positionMode": "HEDGE",
            "leverage": null, 
            "takerFeeRate": 0,
            "makerFeeRate": 0,
            "interestRate": 1,
            "futuresTakerFeeRate": 0,
            "futuresMakerFeeRate": 0,
            "otpauth": true,
            "marginRatio": 7739.3757,
            "openMarginRatio": 7739.3757,
            "initialMarginRatio": 1.0006,
            "maintenanceMarginRatio": 0.0126,
            "totalCollateral": 1146085.27376211,
            "freeCollateral": 1145937.09993548,
            "totalAccountValue": 1924716.18982933, // include isolated frozen and unrealized pnl
            "totalVaultValue": 778216.06557667,
            "totalStakingValue": 0,
            "referrerID": "",
            "accountType": "Main",
            "totalLaunchpadVaultValue": 0,
            "totalEarnValue": 0
        },
        "timestamp": 1714284212689
    }
    

**Parameters**

None

## Get Token History

**Limit: 10 requests per 60 seconds**

` GET /v1/client/transaction_history `

Get account token balance change history, including `YIELD_TO_BALANCE`, `TRANSACTION_FEE`, `REALIZED_PNL`, `SPOT_TRANSACTION`, `FUTURES_TRADING`, `FUNDING_FEE`

> **Response**
    
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "id": 1606724,
                    "type": "YIELD_TO_BALANCE",
                    "token": "WOO",
                    "amount": 0.30029155,
                    "timestamp": 1686528091385
                },
                {
                    "id": 1686355200000,
                    "type": "REALIZED_PNL",
                    "token": "USDT",
                    "symbol": "PERP_WOO_USDT",
                    "amount": -24.64824179,
                    "timestamp": 1686355200000
                },
                {
                    "id": 7284139,
                    "type": "FUNDING_FEE",
                    "token": "USDT",
                    "amount": 0.02661496,
                    "timestamp": 1686009921667
                },
                ...
            ],
            "meta": {
                "total": 65,
                "records_per_page": 25,
                "current_page": 1
            }
        },
        "timestamp": 1686544732777
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
type | string | N | `WITHDRAW`/`DEPOSIT`/`FIAT_WITHDRAW`/`FIAT_DEPOSIT`/`EARN`/`VAULT_WITHDRAW`/`VAULT_DEPOSIT`/`YIELD_TO_BALANCE`/`CREDIT`/`DISTRIBUTION`/`REFERRAL`/`SUB_ACCOUNT_TRANSFER`/`REBATE`/`LIQUIDATION`/`SPECIAL`/`STAKING`/`UNSTAKING`/`UNSTAKING_FEE`/`INTEREST`/`CONVERT`/`FUNDING_FEE`/`SPOT_TRANSACTION`/`TRANSACTION_FEE`/`REALIZED_PNL`/`RFQ`  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
## Get Account API Key & Permission

**Limit: 10 requests per 60 seconds**

` GET usercenter/api/enabled_credential `

Get api_key list and its permissions of the account. The response will contain your API keysâ permissions based on the credentials.

> **Response**
    
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "account_name": "Main",
                    "user_id": 10001,
                    "api_key": "+Pxxxxxxxxxxxxxxxxxxxx==",
                    "permission": "Read,"
                },
                {
                    "account_name": "Main",
                    "user_id": 10001,
                    "api_key": "Hxxxxxxxxxxxxxxxxxxxx==",
                    "permission": "Read,"
                },
                {
                    "account_name": "Main",
                    "user_id": 10001,
                    "api_key": "Cxxxxxxxxxxxxxxxxxxxx==",
                    "permission": "Read,"
                },
                {
                    "account_name": "testSubAccount",
                    "user_id": 10001,
                    "api_key": "vxxxxxxxxxxxxxxxxxxxx==",
                    "permission": "Read,Enable trade,"
                }
                ...
            ],
            "meta": {
                "total": 11,
                "records_per_page": 5,
                "current_page": 1
            }
        },
        "timestamp": 1685414636917
    }
    

**Parameters**

None

## Get Buy Power

**Limit: 60 requests per 60 seconds**

` GET /v3/buypower `

Get buying power for selected symbol.

> **Response**
    
    
    {
      "success": true,
      "data": [
        {
            "symbol": "SPOT_BTC_USDT",
            "availableBaseQuantity": 1.2,
            "availableQuoteQuantity": 100,
        },
      ],
      "timestamp": 1575014255
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y | symbol that you wish to query  
  
## Get Token Deposit Address

**Limit 60 requests per 60 seconds**

` GET /v1/asset/deposit `

Get your unique deposit address by token

> **Response**
    
    
    {
        "success": true,
        "address": "0x31d64B3230f8baDD91dE1710A65DF536aF8f7cDa",
        "extra": ""
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | Y | token name you want to deposit (can get it by /public/token)  
  
## Token Withdraw

**Limit 20 requests per 60 seconds**

` POST /v1/asset/withdraw `

Initiate a token withdrawal request, `amount` must less than or equal to `holding`

> **Response**
    
    
    {
        "success": true,
        "withdraw_id": "20200119145703654"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | Y | token name you want to withdraw (can get it by /public/token)  
address | string | Y | the address you want to withdraw  
extra | string | N | address extra information such as MEMO or TAG  
amount | number | Y | amount you want to withdraw, must less or equal than holding  
  
## Token Withdraw V3

**Limit 20 requests per 60 seconds**

` POST /v3/asset/withdraw `

Initiate a token withdrawal request, `amount` must less than or equal to `holding`

> **Response**
    
    
    {
        "success": true,
        "data": {
            "withdrawId": "24040901514500001"
        },
        "timestamp": 1712627507204
    }
    
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
network | string | Y | To be obtained from the /public/token endpoint  
address | string | Y | the address you want to withdraw  
extra | string | N | address extra information such as MEMO or TAG  
amount | number | Y | amount you want to withdraw, must less or equal than holding  
balanceToken | string | Y | To be obtained from the /public/token endpoin  
  
## Internal token withdraw

**Limit: 20 requests per 60 seconds**

` POST v1/asset/internal_withdraw `

Initiate a token withdrawal request, amount must less than or equal to holding. When using this API, please note that it cannot be utilized if address verification is enabled.

> **Response**
    
    
    {
        "success": true,
        "withdraw_id": "20200119145703654"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
target_user_id | string | Yes | withdraw target user id  
balance_token | string | Yes | balance token is token name you want to withdraw (can get it by /public/token)  
amount | number | Yes | amount you want to withdraw, must less or equal than holding  
  
## Cancel Withdraw Request

**Limit 5 requests per 60 seconds**

` DELETE /v1/asset/withdraw `

Cancel withdraw request when status is `NEW`

> **Response**
    
    
    {
        "success": true
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | the withdraw id you want to cancel  
  
## Get Asset History

**Limit 10 requests per 60 seconds**

` GET /v1/asset/history `

Get asset history, includes token deposit/withdraw and collateral deposit/withdraw.

> **Response**
    
    
    {
        "success": true,
        "meta": {
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
            {
                "created_time": "1579399877.041", // Unix epoch time in seconds
                "updated_time": "1579399877.041", // Unix epoch time in seconds
                "id": "202029292829292",
                "external_id": "202029292829292",
                "application_id": null,
                "token": "ETH",
                "target_address": "0x31d64B3230f8baDD91dE1710A65DF536aF8f7cDa",
                "source_address": "0x70fd25717f769c7f9a46b319f0f9103c0d887af0",
                "confirming_threshold":12,
                "confirmed_number":12,
                "extra": "",
                "type": "BALANCE",
                "token_side": "DEPOSIT",
                "amount": 1000,
                "tx_id": "0x8a74c517bc104c8ebad0c3c3f64b1f302ed5f8bca598ae4459c63419038106b6",
                "fee_token": null,
                "fee_amount": null,
                "status": "CONFIRMING"
            },
            {
                "created_time": "1579399877.041",
                "updated_time": "1579399877.041",
                "id": "20202020202020022",
                "external_id": "20202020202020022",
                "application_id": null,
                "token": "ETH",
                "target_address": "0x31d64B3230f8baDD91dE1710A65DF536aF8f7cDa",
                "source_address": "0x70fd25717f769c7f9a46b319f0f9103c0d887af0",
                "confirming_threshold":12,
                "confirmed_number":12,
                "extra": "",
                "type": "BALANCE",
                "token_side": "DEPOSIT",
                "amount": 100,
                "tx_id": "0x7f74c517bc104c8ebad0c3c3f64b1f302ed5f8bca598ae4459c63419038106c5",
                "fee_token": null,
                "fee_amount": null,
                "status": "COMPLETED"
            }
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | N | use when query specific transaction id (the result of withdrawal or internal transfer.)  
token | string | N | token name you want to search (can get it by /public/token)  
balance_token | string | N | balance_token name you want to search (can get it by /public/token)  
type | string | N | `BALANCE`/`COLLATERAL`  
token_side | string | N | `DEPOSIT`/`WITHDRAW`  
status | string | N | `NEW`/`CONFIRMING`/`PROCESSING`/`COMPLETED`/`CANCELED`  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
## Margin Interest Rates

**Limit 10 requests per 60 seconds**

` GET /v1/token_interest `

Get the margin interest rate of each token.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "token": "MATIC",
                "current_hourly_base_rate": "0.0001%",
                "est_hourly_base_rate": "0.0001%",
                "current_annual_base_rate": "0.876%",
                "est_annual_base_rate": "0.876%",
                "est_time": "1632394800.000"          // Unix epoch time in seconds
            },
            {
                "token": "USDT",
                "current_hourly_base_rate": "0.0008%",
                "est_hourly_base_rate": "0.0008%",
                "current_annual_base_rate": "7.008%",
                "est_annual_base_rate": "7.008%",
                "est_time": "1632394800.000"          // Unix epoch time in seconds
            },
            {
                "token": "WOO",
                "current_hourly_base_rate": "0.001%",
                "est_hourly_base_rate": "0.001%",
                "current_annual_base_rate": "8.76%",
                "est_annual_base_rate": "8.76%",
                "est_time": "1632394800.000"          // Unix epoch time in seconds
            },
            // ...
        ]
    }
    

**Parameters**

None

## Margin Interest Rate of Token

**Limit 10 requests per 60 seconds**

` GET /v1/token_interest/:token `

Get the margin interest rate of the specific token.

> **Response**
    
    
    {
        "success": true,
        "info": {
            "token": "BTC",
            "current_hourly_base_rate": "0.0001%",
            "est_hourly_base_rate": "0.0001%",
            "current_annual_base_rate": "0.876%",
            "est_annual_base_rate": "0.876%",
            "est_time": "1632448800.000"         // Unix epoch time in seconds
        }
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | Y | should be upper case  
  
## Get Interest History

**Limit 10 requests per 60 seconds**

` GET /v1/interest/history `

Get margin interest history. `loan_amount` will only appear when the side is `LOAN`.

> **Response**
    
    
    {
        "success": true,
        "meta": {
            "total": 349,
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
    
           {
                "created_time": "1579399877.041", // Unix epoch time in seconds
                "updated_time": "1579399877.041", // Unix epoch time in seconds
                "token": "USDT",
                "application_id": null,
                "user_id": null,
                "status": "SUCCEED",
                "quantity": 0.20768326,
                "side": "LOAN",
                "interest": 0.01,
                "hourly_rate": "0.001%",
                "annual_rate": "8.76%",
                "loan_amount": 1000
            }
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | N | interest token which you want to query  
side | string | N | `LOAN`/`REPAY`/`AUTO_REPAY`  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
## Repay Interest

**Limit 10 requests per 60 seconds**

` POST /v1/interest/repay `

REPAY your margin interest.

> **Response**
    
    
    {
        "success": true,
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | Y | interest token which you want to repay  
amount | number | Y | repayment amount  
  
## Get referrals summary

**Limit: 10 requests per 60 seconds**

` GET /v3/referrals `

Get referral information from each user you has referred.

> **Response**
    
    
    // The status of the recommender includes four typesï¼Registered; Verified identity; Deposited; Traded
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "referralId": 12509,
                    "registerTime": "1643076873.484",
                    "referralCode": "OJEDSSMU",
                    "tradeStatus": "Traded",
                    "earnWoo": 144.78597143,
                    "earnUsdt": 0,
                    "email": "staking-005_mas@woo.network",
                    "extraBonus": 0,
                    "extraBonusToken": "WOO",
                    "previousVersionCommissionSum": 10.07981438,
                    "previousVersionCommissionSumToken": "WOO"
                },
                {
                    "referralId": 12192,
                    "registerTime": "1639365757.173",
                    "referralCode": "OJEDSSMU",
                    "tradeStatus": "Traded",
                    "earnWoo": 5729.91597424,
                    "earnUsdt": 80.39717397,
                    "email": "hazel@woo.network",
                    "extraBonus": 0,
                    "extraBonusToken": "WOO",
                    "previousVersionCommissionSum": 5726.55249830,
                    "previousVersionCommissionSumToken": "WOO"
                },
                {
                    "referralId": 10588,
                    "registerTime": "1678349096.000",
                    "referralCode": "OJEDSSMU",
                    "tradeStatus": "Traded",
                    "earnWoo": 2058880.44406483,
                    "earnUsdt": 54128.36568263,
                    "email": "ken@woo.network",
                    "extraBonus": 90,
                    "extraBonusToken": "WOO",
                    "previousVersionCommissionSum": 20160.36080029,
                    "previousVersionCommissionSumToken": "WOO"
                },
                {
                    "referralId": 10492,
                    "registerTime": "1623203745.173",
                    "referralCode": "DIHGLR3T",
                    "tradeStatus": "Traded",
                    "earnWoo": 0,
                    "earnUsdt": 0.76927350,
                    "email": "staking-010@woo.network",
                    "extraBonus": 90,
                    "extraBonusToken": "WOO",
                    "previousVersionCommissionSum": null,
                    "previousVersionCommissionSumToken": "WOO"
                }
            ],
            "meta": {
                "total": 4,
                "records_per_page": 25,
                "current_page": 1
            }
        },
        "timestamp": 1690192103430
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
from | number | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
to | number | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
  
## Get referral reward history

**Limit: 10 requests per 60 seconds**

` GET /v3/referral_rewards `

Get referral reward information 

> **Response**
    
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "trade_date": "2023/07/17",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.47000000,
                    "referral_commission": 53929.73957955,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/07/17",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 2038704.30927676,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/07/12",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.05004760,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/07/11",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.44951069,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/07/11",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.47000000,
                    "referral_commission": 0.04858848,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/07/11",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 3.09802285,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/07/07",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 134.61965671,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12509
                },
                {
                    "trade_date": "2023/07/06",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 15.27442949,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/07/03",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.00811566,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/07/03",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.26545309,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/30",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.00144840,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/30",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.08224395,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/29",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.06940520,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/29",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 4.34149772,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/28",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.01434340,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/28",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.87468814,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/27",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.01949850,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 10492
                },
                {
                    "trade_date": "2023/06/27",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.00900000,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/06/27",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.90196242,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/06/27",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.05706141,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/27",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 3.43115031,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/26",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.74977500,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 10492
                },
                {
                    "trade_date": "2023/06/26",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.05399999,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/06/26",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 2.78932410,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/06/26",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.06862500,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                }
            ],
            "meta": {
                "total": 79,
                "records_per_page": 25,
                "current_page": 1
            }
        },
        "timestamp": 1690273370109
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
from | number | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
to | number | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
|  |  |   
|  |  |   
  
## Get Subaccounts

**Limit: 10 requests per 60 seconds**

` GET /v1/sub_account/all `

Get subaccount list.

> **Response**
    
    
    {
        "rows": [
            {
                "application_id": "6b43de5c-0955-4887-9862-d84e4689f9fe",
                "account": "2",
                "created_time": "1606897264.994"
            },
            {
                "application_id": "5b0df321-3aaf-471f-a386-b922a941d17d",
                "account": "1",
                "created_time": "1606897264.994"
            },
            {
                "application_id": "de25e672-f3e8-4ddc-b264-75d243cb2b9c",
                "account": "test",
                "created_time": "1606897264.994"
            }
        ],
        "success": true
    }
    

**Permission**

Main account only.

**Parameters**

None

## Get Assets of Subaccounts

**Limit: 10 requests per 60 seconds**

` GET /v1/sub_account/assets `

Get assets summary of all subaccounts (including main account).

> **Response**
    
    
    {
        "rows": [
            {
                "application_id": "0b297f58-9d3e-4c91-95cd-863329631b79",
                "account": "Main",
                "usdt_balance": 0.0
            }
        ],
        "success": true
    }
    

**Permission**

Main account only.

**Parameters**

None

## Get Asset Details from a Subaccount

**Limit: 10 requests per 60 seconds**

` GET /v1/sub_account/asset_detail `

Get assets details from a subaccounts.

> **Response**
    
    
    {
        "balances": {
            "BTC": {
                "holding": 0.0,
                "frozen": 0.0,
                "interest": 0.0,
                "staked": 0.0,
                "unbonding": 0.0,
                "vault": 0.0
            },
            "WOO": {
                "holding": 4172706.29647137,
                "frozen": 0.0,
                "interest": 0.0,
                "staked": 51370692,
                "unbonding": 0.0,
                "vault": 0.0
            },
            "BNB": {
                "holding": 0.00070154,
                "frozen": 0.0,
                "interest": 0.0,
                "staked": 0.0,
                "unbonding": 0.0,
                "vault": 0.0
            },
            "ETH": {
                "holding": 0.0,
                "frozen": 0.0,
                "interest": 0.0,
                "staked": 0.0,
                "unbonding": 0.0,
                "vault": 0.0
            },
            "USDT": {
                "holding": 14066.5839369,
                "frozen": 0.0,
                "interest": 0.0,
                "staked": 0.0,
                "unbonding": 0.0,
                "vault": 0.0
            }
        },
        "account": "test",
        "success": true,
        "application_id": "e074dd6b-4c03-49be-937f-856472f7a6cb"
    }
    

**Permission**

Main or Subaccounts.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
application_id | string | Y | application id for an account, user can find it from WOO X console.  
  
## Get IP Restriction

**Limit: 10 requests per 10 seconds**

` GET /v1/sub_account/ip_restriction `

Get allowed IP list of a subaccount's API Key.

> **Response**
    
    
    {
        "rows": [
            {
                "ip_list": "60.248.33.61,1.2.3.4,100.100.1.1,100.100.1.2,100.100.1.3,100.100.1.4,210.64.18.77",
                "api_key": "plXHR+GwX0u8UG/GwMjLsQ==",
                "update_time": "1644553230.916",
                "restrict": true
            }
        ],
        "meta": {
            "total": 1,
            "records_per_page": 25,
            "current_page": 1
        },
        "success": true
    }
    

**Permission**

Main or Subaccounts.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
application_id | string | N | from WOO X console  
api_key | string | N | created from WOO X console  
  
## Get Transfer History

**Limit: 20 requests per 60 seconds**

` GET /v1/asset/main_sub_transfer_history `

Get transfer history between main account and subaccounts. 

> **Response**
    
    
    {
        "success":true,
        "data":{
            "rows":[
                {
                    "id":225,
                    "token":"USDT",
                    "amount":1000000,
                    "status":"COMPLETED",
                    "from_application_id":"046b5c5c-5b44-4d27-9593-ddc32c0a08ae",
                    "to_application_id":"082ae5ae-e26a-4fb1-be5b-03e5b4867663",
                    "from_user":"Main",
                    "to_user":"av",
                    "created_time":"1642660941.534",
                    "updated_time":"1642660941.950"
                },
                // ....skip (total 25 items in one page)
            ],
            "meta":{
                "total":7,
                "records_per_page":5,
                "current_page":1
            }
        }
    }
    

**Permission**

Main or Subaccounts.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
## Transfer Assets

**Limit: 20 requests per 60 seconds** ` POST /v1/asset/main_sub_transfer `

Transfer asset between main account and subaccounts. 

> **Response**
    
    
    {
        "success": true,
        "id": 200
    }
    

**Permission**

Main or Subaccounts.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | Y | token name you want to transfer (can get it by /public/token)  
amount | number | Y | amount you want to transfer  
from_application_id | string | Y | application id you want to transfer from  
to_application_id | string | Y | application id you want to transfer to  
  
## Get LtV info

**Limit: 20 requests per 60 seconds** ` POST /v1/asset/ltv `

For credit user to know whether need to deposit more funds to the platform if I want to withdraw.

> **Response**
    
    
    {
        "user_id": 12136,
        "success": true,
        "ltv_threshold": 0.6,
        "wallet_total_collateral": 1890719757.24550000,
        "credit": 0.00000000,
        "staking_woo_collateral": 0,
        "ltv": 0.00000000,
        "share_credit_user_ltv_infos": [
            {
                "user_id": 12136,
                "wallet_total_collateral": 1890719757.24550000,
                "staking_woo_collateral": 0
            }
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
withdraw_token | string | N | If input this field, the `withdraw_amount` field will be mandatory  
withdraw_amount | number | N | amount you want to withdraw of the `withdraw_token`  
  
## Update Account Mode

**Limit: 5 requests per 60 seconds per user**

` POST /v1/client/account_mode `

Choose account mode: pure spot or margin or futures

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
account_mode | string | Y | PURE_SPOT, MARGIN, FUTURES  
  
> **Response**
    
    
    {
        "success": true
    }
    

## Update Position Mode

**Limit: 2 requests per 1 second per user**

` POST /v1/client/position_mode `

Choose position mode: ONE_WAY or HEDGE_MODE

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
position_mode | string | Y | set ONE_WAY / HEDGE_MODE to position mode  
  
> **Response**
    
    
    {
        "success": true
    }
    

## Update Leverage Setting

**Limit: 5 requests per 60 seconds per user**

` POST /v1/client/leverage `

Choose maximum leverage for margin mode  
**Parameters**

Name | Type | Required | Description  
---|---|---|---  
leverage | int | Y | for margin mode: 3, 4, 5ï¼10 ;  
  
> **Response**
    
    
    {
        "success": true
    }
    

## Update Futures Leverage Setting

**Limit: 60 requests per 60 seconds per user**

` POST /v1/client/futures_leverage `

Choose maximum leverage for futures mode

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y | Perpetual symbol name.  
margin_mode | string | Y | Options are `CROSS`/`ISOLATED`  
position_side | string | Y | Options are `LONG`/`SHORT` in hedge mode; `BOTH` in one way mode.  
leverage | int | Y | Leverage to set  
  
> **Response**
    
    
    {
        "success": true
    }
    

## GET Futures Leverage Setting

**Limit: 10 requests per 60 seconds per user**

` GET /v1/client/futures_leverage `

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y | Perpetual symbol name.  
margin_mode | string | Y | Options are `CROSS`/`ISOLATED`  
position_mode | string | Y | Options are `ONE_WAY`/`HEDGE`, for `HEDGE` mode it will present for both side  
  
> **Response**
    
    
    // cross margin, one way mode
    {
        "success": true,
        "data": {
            "symbol": "PERP_BTC_USDT",
            "margin_mode": "CROSS",
            "position_mode": "ONE_WAY",    
            "details": [
                {
                    "position_side": "BOTH",
                    "leverage": "10"
                }
            ]
        },
        "timestamp": 1696663264324
    }
    
    // cross margin, hedge mode
    {
        "success": true,
        "data": {
            "symbol": "PERP_BTC_USDT",
            "margin_mode": "CROSS",
            "position_mode": "HEDGE_MODE",    
            "details": [
                {
                    "position_side": "LONG",
                    "leverage": "10"
                },
                {
                    "position_side": "SHORT",
                    "leverage": "10"
                },
            ]
        },
        "timestamp": 1696663264324
    }
    
    // isolated margin, one way mode
    {
        "success": true,
        "data": {
            "symbol": "PERP_BTC_USDT",
            "margin_mode": "ISOLATED",
            "position_mode": "ONE_WAY",    
            "details": [
                {
                    "position_side": "BOTH",
                    "leverage": "10"
                }
            ]
        },
        "timestamp": 1696663264324
    }
    
    // isolated margin, hedge mode
    {
        "success": true,
        "data": {
            "symbol": "PERP_BTC_USDT",
            "margin_mode": "ISOLATED",
            "position_mode": "HEDGE_MODE",    
            "details": [
                {
                    "position_side": "LONG",
                    "leverage": "10"
                },
                {
                    "position_side": "SHORT",
                    "leverage": "20"
                },
            ]
        },
        "timestamp": 1696663264324
    }
    

## Update Isolated Margin Setting

**Limit: 20 requests per 60 seconds per user**

` POST /v1/client/isolated_margin `

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y | Perpetual symbol name.  
position_side | string | Y | Options are LONG/SHORT in hedge mode; BOTH in one way mode.  
adjust_token | string | Y | Only USDT is supported.  
adjust_amount | Number | Y | Token amount to be added or reduced.  
action | Number | Y | `ADD`/`REDUCE`  
  
> **Response**
    
    
    {
        "success": true
    }
    

## Get Funding Fee History

**Limit: 20 requests per 60 seconds per user**

` GET /v1/funding_fee/history `

Get funding fee history

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | N | symbol that you wish to query  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 10) | max 5000  
  
> **Response**
    
    
    {
        "success": true,
        "meta": {
                "total": 670,
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
            {
                "id": 10001,
                "symbol": "PERP_BTC_USDT",
                "funding_rate": 0.00345,
                "mark_price": 100,
                "funding_fee": 0.345,
                "payment_type": "Receive", // Receive and Pay
                "status": "COMPLETED",
                "created_time": "1575014255.089", // Unix epoch time in seconds
                "updated_time": "1575014255.910", // Unix epoch time in seconds
                "funding_rate_interval_hours": 1
            },
            // ....skip (total 25 items in one page)
    
    }
    

## Get All Position info

**Limit: 30 requests per 10 seconds per user**

` GET /v1/positions `

** Note: This API will be deprecated at the end of 2023 Q1, please find the replacement API in  [Get Positions - New](#get-positions-new)

**Parameters**

> **Response**
    
    
    {
        "total_account_value": 1924712.88293063,
        "current_margin_ratio": 7719.4699,
        "success": true,
        "total_collateral": 1146084.70891586,
        "total_vault_value": 0.0,
        "total_staking_value": 0.0,
        "positions": [
            {
                "symbol": "PERP_WOO_USDT",
                "holding": 8.0,
                "pending_long_qty": 0.0,
                "pending_short_qty": 0.0,
                "settle_price": 0.31197093,
                "average_open_price": 0.43228,
                "timestamp": "1714247701.266",
                "opening_time": "1712542194.878",
                "mark_price": 0.31851,
                "est_liq_price": 0.0,
                "position_side": "LONG",
                "pnl_24_h": 0.0,
                "fee_24_h": 0.0,
                "margin_mode": "ISOLATED", 
                "leverage": 10, 
                "isolated_margin_token": "USDT",
                "isolated_margin_amount": 99.1,
                "isolated_frozen_long": 81.2,
                "isolated_frozen_short": 88.2
            },
            {
                "symbol": "PERP_WOO_USDT",
                "holding": 8.0,
                "pending_long_qty": 0.0,
                "pending_short_qty": 0.0,
                "settle_price": 0.31197093,
                "average_open_price": 0.43228,
                "timestamp": "1714247701.266",
                "opening_time": "1712542194.878",
                "mark_price": 0.31851,
                "est_liq_price": 0.0,
                "position_side": "LONG",
                "pnl_24_h": 0.0,
                "fee_24_h": 0.0,
                "margin_mode": "CROSS", 
                "leverage": 10, 
                "isolated_margin_token": "",
                "isolated_margin_amount": 0,
                "isolated_frozen_long": 0,
                "isolated_frozen_short": 0
            }
        ],
        "initial_margin_ratio": 1.0006,
        "free_collateral": 1145936.1530736,
        "maintenance_margin_ratio": 0.0126
    }
    

## Get All Position info - New

**Limit: 30 requests per 10 seconds per user**

` GET /v3/positions `

The API is design to replace the legacy API [Get Positions](#get-positions)

**Parameters**

None

> **Response**
    
    
    {
      "success": true,
      "data": {
        "positions": [
          {
            "symbol": "PERP_JTO_USDT",
            "holding": 20.0,
            "pendingLongQty": 0.0,
            "pendingShortQty": 0.0,
            "settlePrice": 2.0771,
            "averageOpenPrice": 2.0771,
            "pnl24H": 0.0,
            "fee24H": 0.0186939,
            "markPrice": 2.07460399,
            "estLiqPrice": 1.92748111,
            "timestamp": 1725916355.494,
            "adlQuantile": 1, // the grades of adlQuantile: 1 through 5
            "positionSide": "BOTH",
            "marginMode": "ISOLATED",
            "isolatedMarginToken": "USDT",
            "isolatedMarginAmount": 4.1604313,
            "isolatedFrozenLong": 0.0,
            "isolatedFrozenShort": 0.0,
            "leverage": 10
          },
          {
            "symbol": "PERP_W_USDT",
            "holding": -50.0,
            "pendingLongQty": 50.0,
            "pendingShortQty": 0.0,
            "settlePrice": 0.1906,
            "averageOpenPrice": 0.1906,
            "pnl24H": 0.0,
            "fee24H": 0.0,
            "markPrice": 0.2103828568089886,
            "estLiqPrice": 4.542491646808989,
            "timestamp": 1725681481.767,
            "adlQuantile": 1,
            "positionSide": "BOTH",
            "marginMode": "CROSS",
            "isolatedMarginToken": "",
            "isolatedMarginAmount": 0.0,
            "isolatedFrozenLong": 0.0,
            "isolatedFrozenShort": 0.0,
            "leverage": 20
          }
        ]
      },
      "timestamp": 1725916369913
    }
    
    

## Get One Position info

**Limit: 30 requests per 10 seconds per user**

ï¼Note that get-one-position-info will only support to response the CROSS mode position of the selected symbol.ï¼

` GET /v1/position/:symbol `

**Parameters**

None

> **Response**
    
    
    {
        "success": true,
        "symbol": "PERP_BTC_USDT",
        "holding": 1.23,
        "pending_long_qty": 0.5,
        "pending_short_qty": 0.23,
        "settle_price": 50000,
        "average_open_price": 49000,
        "pnl_24_h": 20,
        "fee_24_h": 0.2,
        "mark_price": 49550,
        "est_liq_price": 40000,
        "timestamp": "1575014255.089"
    }
    

## GET InsuranceFund

**Limit: token filtered to USDT only**

` GET /v3/public/insuranceFund `

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
  
> **Response**
    
    
    {
       "success": true,
        "data": {
          "rows": [
            {
              "balance": 1000,
              "token": "USDT",
            }
          ]
        },
        "timestamp": 1673323685109 
    }
    

## GET AssignmentPreference

**Limit: 10 requests per 60 seconds**

` GET /v3/liquidator/assignmentPreference `

Get your accountâs assignment preferences.Â 

**Parameters**

None

> **Response**
    
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "symbol": "PERP_BTC_USDT",
                    "type": "USDT_NOTIONAL",
                    "maxAmountPerOrder": 10000,
                    "maxAmountTotal": null,
                    "acceptLong": true,
                    "acceptShort": true,
                },
                {
                    "symbol": "PERP_ETH_USDT",
                    "type": "BASE_TOKEN"
                    "maxAmountPerOrder": "100000",
                    "maxAmountTotal": "1000000",
                    "acceptLong": true,
                    "acceptShort": false,
                },
                ...
            ]
        },
        "timestamp": 1711433755393
    }
    

## Add an AssignmentPreference

**Limit: 10 requests per 60 seconds**

` POST /v3/liquidator/assignmentPreference `

Add an assignment preference for your account. If a preference already exists for the symbol, adding a new one will automatically override the previous preference.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Yes | Perpetual symbol name  
type | string | Yes | Specifies the type for the max amount. Options are USDT_NOTIONAL/BASE_TOKEN/LIMITLESS.  
maxAmountPerOrder | string | Conditional | Max assigned per order. If type is USDT_NOTIONAL or BASE_TOKEN, both maxAmountPerOrder and maxAmountTotal need to be specified. If type is LIMITLESS, maxAmountPerOrder and maxAmountTotal will be ignored.  
maxAmountTotal | string | Conditional | Max position size after assignment. If type is USDT_NOTIONAL or BASE_TOKEN, both maxAmountPerOrder and maxAmountTotal need to be specified. If type is LIMITLESS, maxAmountPerOrder and maxAmountTotal will be ignored.  
acceptLong | boolean | No (default: true) | Whether to accept long positions  
acceptShort | boolean | No (default: true) | Whether to accept short positions  
  
> **Response**
    
    
    {
        "success": true,
        "timestamp": 1711432330937
    }  
    

## Delete an AssignmentPreference

**Limit: 10 requests per 1 seconds**

` DELETE /v3/liquidator/assignmentPreference `

Delete an assignment preference by symbol.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Yes | symbol name  
  
> **Response**
    
    
    {
        "success": true,
        "timestamp": 1711432330937
    }  
    

# Websocket API V2

We will launch a new domain wss.woox.io on 2024/09/22. Please note that the old domain wss.woo.org will be decommissioned at a later date, which will be announced separately.

If you are a new user, please use the new domain wss.woox.io for integration. If you are an existing user, you may continue using wss.woo.org, but we strongly recommend migrating to wss.woox.io as soon as possible to avoid any future service disruptions.

**Market Data Base endpoints:**

  * `wss://wss.staging.woox.io/ws/stream/{application_id}` **(Staging)**
  * `wss://wss.woox.io/ws/stream/{application_id}` **(Production)**
  * `{application_id}` user can find application_id from console
  * user can subscribe/unsubscribe `orderbook`|`orderbook100`|`aggbook10`|`aggbook100`|`aggbook1000`|`ticker`|`tickers`|`bbo`|`trade`|`kline_1m`|`kline_5m`|`kline_15m`|`kline_30m`|`kline_1h`|`kline_1d`|`kline_1w`|`kline_1M`



**Private User Data Stream Base endpoints:**

  * `wss://wss.staging.woox.io/v2/ws/private/stream/{application_id}` **(Staging)**
  * `wss://wss.woox.io/v2/ws/private/stream/{application_id}` **(Production)**
  * `{application_id}` user can find application_id from console
  * User needs to be authenticated before subscribing any topic, would be disconnected if fails the authentication. Refer to [Authenticaton](#authentication) for more information. 
  * User can subscribe/unsubscribe `positioninfo`|`executionreport`



## PING/PONG

  * The server will send a ping command to the client every 10 seconds. If the pong from client is not received within 10 seconds for 10 consecutive times, it will actively disconnect the client.
  * The client can also send ping every 10s to keep alive.



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
event | string | Y | `ping`/`pong`  
      
    
    {
        "event":"ping"
    }
    

**Response**
    
    
    {
        "event":"pong",
        "ts":1614667590000
    }
    

## request orderbook

Push interval: real-time push

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `request`  
params.type | string | Y | `orderbook`  
params.symbol | string | Y | `{symbol}`  
      
    
    {
        "id": "clientID1",
        "event": "request",
        "params": {
            "type": "orderbook",
            "symbol": "SPOT_BTC_USDT"
        }
    }
    

**Response**
    
    
    {
        "id":"123r",
        "event":"request",
        "success":true,
        "ts":1618880432419,
        "data":{
            "symbol":"SPOT_BTC_USDT",
            "ts":1618880432380,
            "asks":[
                [
                    54700,
                    0.443951
                ],
                [
                    54700.02,
                    0.002566
                ],
                ...
            ],
            "bids":[
                [
                    54699.99,
                    2.887466
                ],
                [
                    54699.76,
                    2.034711
                ],
               ...
            ]
        }
    }
    

## orderbook

  * Push interval: 1s
  * `{symbol}@orderbook` 100 levels, only push when there are actual change.



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@orderbook`/`{symbol}@orderbook100`  
      
    
    {
        "id": "clientID2",
        "topic": "SPOT_WOO_USDT@orderbook",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID2",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_WOO_USDT@orderbook"
    }
    

**Subscribed Message**
    
    
    {
        "topic": "SPOT_WOO_USDT@orderbook",
        "ts": 1614152140945,
        "data": {
            "symbol": "SPOT_WOO_USDT",
            "asks": [
                [
                    0.31075,
                    2379.63
                ],
                [
                    0.31076,
                    4818.76
                ],
                [
                    0.31078,
                    8496.1
                ],
                ...
            ],
            "bids": [
                [
                    0.30891,
                    2469.98
                ],
                [
                    0.3089,
                    482.5
                ],
                [
                    0.30877,
                    20
                ],
                ...
            ]
        }
    }
    

## orderbookupdate

  * `{symbol}@orderbookupdate` updated orderbook push every 200ms



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@orderbookupdate`  
      
    
    {
        "id": "clientID2",
        "topic": "SPOT_BTC_USDT@orderbookupdate",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID2",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_BTC_USDT@orderbookupdate"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"SPOT_BTC_USDT@orderbookupdate",
        "ts":1618826337580,
        "data":{
            "symbol":"SPOT_BTC_USDT",
            "prevTs":1618826337380,
            "asks":[
                [
                    56749.15,
                    3.92864
                ],
                [
                    56749.8,
                    0
                ],
                ...
            ],
            "bids":[
                [
                    56745.2,
                    1.03895025
                ],
                [
                    56744.6,
                    1.0807
                ],
                ...
            ]
        }
    }
    

## trade

  * Push interval: real-time push



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@trade`  
      
    
    {
        "id": "clientID3",
        "topic": "SPOT_ADA_USDT@trade",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_ADA_USDT@trade"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"SPOT_ADA_USDT@trade",
        "ts":1618820361552,
        "data":{
            "symbol":"SPOT_ADA_USDT",
            "price":1.27988,
            "size":300,
            "side":"BUY",
            "source":0,
            "rpi":true
        }
    }
    

## trades

  * Push interval: 200ms



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `SPOT_BTC_USDT@trades`  
      
    
    {
        "id": "clientID3",
        "topic": "SPOT_BTC_USDT@trades",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_BTC_USDT@trades"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"SPOT_BTC_USDT@trades",
        "ts":1618820361552,
        "data":[{
            "symbol":"SPOT_BTC_USDT",
            "price":42598.27,
            "size":300,
            "side":"BUY",
            "source":0,
            "rpi":true
        },
        {
            "symbol":"SPOT_BTC_USDT",
            "price":42589.74,
            "size":200,
            "side":"BUY",
            "source":0,
            "rpi":true
        }
        ]
    }
    

## 24h ticker

  * Push interval:1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@ticker`  
      
    
    {
        "id": "clientID4",
        "topic": "SPOT_WOO_USDT@ticker",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID4",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_WOO_USDT@ticker"
    
    }
    

**Subscribed Message**
    
    
    {
        "topic": "SPOT_WOO_USDT@ticker",
        "ts": 1614152270000,
        "data": {
            "symbol": "SPOT_WOO_USDT",
            "open": 0.16112,
            "close": 0.32206,
            "high": 0.33000,
            "low": 0.14251,
            "volume": 89040821.98,
            "amount": 22493062.21,
            "aggregatedQuantity": 20598.85059063,
            "aggregatedAmount": 1303973569.5714033,
            "count": 15442ï¼
            "astTs": 1727161921650
        }
    }
    

## 24h tickers

  * Push interval: 1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `tickers`  
      
    
    {
        "id": "clientID4",
        "topic": "tickers",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID4",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "tickers"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"tickers",
        "ts":1618820615000,
        "data":[
            {
                "symbol":"SPOT_OKB_USDT",
                "open":16.297,
                "close":17.183,
                "high":24.707,
                "low":11.997,
                "volume":0,
                "amount":0,
                "aggregatedQuantity": 20598.85059063,
                "aggregatedAmount": 1303973569.5714033,
                "count":0,
                "astTs": 1727161921650
            },
            {
                "symbol":"SPOT_XRP_USDT",
                "open":1.3515,
                "close":1.43794,
                "high":1.96674,
                "low":0.39264,
                "volume":750127.1,
                "amount":985440.5122,
                "aggregatedQuantity": 20598.85059063,
                "aggregatedAmount": 1303973569.5714033,
                "count":396,
                "astTs": 1727161921650
            },
           ...
        ]
    }
    

## bbo

  * Push interval: 10ms



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@bbo`  
      
    
    {
        "id": "clientID5",
        "topic": "SPOT_WOO_USDT@bbo",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID5",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_WOO_USDT@bbo"
    }
    

**Subscribed Message**
    
    
    {
        "topic": "SPOT_WOO_USDT@bbo",
        "ts": 1614152296945,
        "data": {
            "symbol": "SPOT_WOO_USDT",
            "ask": 0.30939,
            "askSize": 4508.53,
            "bid": 0.30776,
            "bidSize": 25246.14
        }
    }
    

## bbos

  * Push interval: 1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `bbos`  
      
    
    {
        "id": "clientID5",
        "topic": "bbos",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID5",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "bbos"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"bbos",
        "ts":1618822376000,
        "data":[
            {
                "symbol":"SPOT_FIL_USDT",
                "ask":159.0318,
                "askSize":370.43,
                "bid":158.9158,
                "bidSize":16
            },
            {
                "symbol":"SPOT_BTC_USDT",
                "ask":56987.18,
                "askSize":3.163881,
                "bid":56987.17,
                "bidSize":0.941728
            },
           ...
        ]
    }
    

## k-line

  * `{time}`: `1m`/`5m`/`15m`/`30m`/`1h`/`1d`/`1w`/`1M`
  * Push interval: by the selected k-line type.



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | N | `{symbol}@kline_{time}`  
      
    
    {
        "id": "clientID6",
        "topic": "SPOT_BTC_USDT@kline_1m",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID6",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_BTC_USDT@kline_1m"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"SPOT_BTC_USDT@kline_1m",
        "ts":1618822432146,
        "data":{
            "symbol":"SPOT_BTC_USDT",
            "type":"1m",
            "open":56948.97,
            "close":56891.76,
            "high":56948.97,
            "low":56889.06,
            "volume":44.00947568,
            "amount":2504584.9,
            "startTime":1618822380000,
            "endTime":1618822440000
        }
    }
    

## indexprice

  * Push interval: 1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@indexprice`  
      
    
    {
        "id": "clientID3",
        "topic": "SPOT_ETH_USDT@indexprice",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_ETH_USDT@indexprice"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"SPOT_ETH_USDT@indexprice",
        "ts":1618820361552,
        "data":{
            "symbol":"SPOT_ETH_USDT",
            "price":3987.1
        }
    }
    

## markprice

  * Push interval: 1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@markprice`  
      
    
    {
        "id": "clientID3",
        "topic": "PERP_ETH_USDT@markprice",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "PERP_ETH_USDT@markprice"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"PERP_ETH_USDT@markprice",
        "ts":1618820361552,
        "data":{
            "symbol":"PERP_ETH_USDT",
            "price":3987.2
        }
    }
    

## estfundingrate

  * Push interval: 1min



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@estfundingrate`  
      
    
    {
        "id": "clientID3",
        "topic": "PERP_BTC_USDT@estfundingrate",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "PERP_BTC_USDT@estfundingrate"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"PERP_BTC_USDT@estfundingrate",
        "ts":1618820361552,
        "data":{
            "symbol":"PERP_BTC_USDT",
            "fundingRate":1.27988,
            "fundingTs":1618820361552
        }
    }
    

## openinterests

  * Push interval: 10s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `openinterests`  
      
    
    {
        "id": "clientID3",
        "topic": "openinterests",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "openinterests"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"openinterests",
        "ts":1618820361552,
        "data":[
            {
            "symbol":"PERP_BNB_USDT",
            "openinterest":936.37
        },
           {
            "symbol":"PERP_ORDI_USDT",
            "openinterest":110.1
        }
        ]
    }
    

## markprices

  * Push interval: 1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `markprices`  
      
    
    {
        "id": "clientID5",
        "topic": "markprices",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID5",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "openinterests"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"markprices",
        "ts":1618822376000,
        "data":[
            {
               "symbol":"PERP_BTC_USDT",
                "price":51234.13
            },
            {
                "symbol":"PERP_ETH_USDT",
                  "price":3894.34
            },
           ...
        ]
    }
    

## auth

  * refer to [Authenticaton](#authentication) for more details about how to sign the request with `api_key` and `api_secret`. **query string** and **body parameters** are both blank.



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
apikey | string | Y | api key  
sign | string | Y | sign  
timestamp | string | Y | timestamp  
      
    
    {
        "id":"123r",
        "event":"auth",
        "params":{
            "apikey":"CUS69ZJOXwSV38xo...",
            "sign":"4180da84117fc9753b...",
            "timestamp":"1621910107900"
        }
    }
    

**Response**
    
    
    {
        "id":"123r",
        "event":"auth",
        "success":true,
        "ts":1621910107315
    }
    

## balance

  * Push interval: realtime (push on update)



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `balance`  
      
    
    {
        "id": "clientID3",
        "topic": "balance",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "balance"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"balance",
        "ts":1618757714353,
        "data":{
            "balances":{
                "BTC":{
                    "holding":0,
                    "frozen":0,
                    "interest":0,
                    "pendingShortQty":0,
                    "pendingLongQty":0,
                    "version":0,
                    "staked":0,
                    "unbonding":0,
                    "vault":309.8,
                    "launchpadVault":0.0,
                    "earn":0.0,
                    "averageOpenPrice":0,
                    "pnl24H":0,
                    "fee24H":0,
                    "markPrice":0,
                    "timestamp": 1618757713353 
                },
                "ETH":{
                    "holding":0,
                    "frozen":0,
                    "interest":0,
                    "pendingShortQty":0,
                    "pendingLongQty":0,
                    "version":0,
                    "staked":0,
                    "unbonding":0,
                    "vault":309.8,
                    "launchpadVault":0.0,
                    "earn":0.0,
                    "averageOpenPrice":0,
                    "pnl24H":0,
                    "fee24H":0,
                    "markPrice":0,
                    "timestamp": 1618757713353 
                },
                ...
            }
        }
    }
    

## executionreport

  * Push interval: real-time push



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `executionreport`  
      
    
    {
        "id": "clientID3",
        "topic": "executionreport",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "executionreport"
    }
    

**Subscribed Message**
    
    
    // receive for order status in new, filled, partial filled execution report
    {
        "topic": "executionreport",
        "ts": 1675406261689,
        "data":
        {
            "msgType": 0,  // execution report
            "symbol": "SPOT_BTC_USDT",
            "clientOrderId": 0,
            "orderId": 54774393,
            "type": "MARKET",
            "side": "BUY",
            "quantity": 0.0,
            "price": 0.0,
            "tradeId": 56201985,
            "executedPrice": 23534.06,
            "executedQuantity": 0.00040791,
            "fee": 2.1E-7,
            "feeAsset": "BTC",
            "totalExecutedQuantity": 0.00040791,
            "avgPrice": 23534.06,
            "status": "FILLED",
            "reason": "",
            "orderTag": "default",
            "totalFee": 2.1E-7,
            "feeCurrency": "BTC",
            "totalRebate": 0,
            "rebateCurrency": "USDT",
            "visible": 0.0,
            "timestamp": 1675406261689,
            "reduceOnly": false,
            "maker": false,
            "leverage": 10,
            "marginMode": "CROSS",
            "rpi": true
        }
    }
    
    // receive when editing order be rejected
    {
        "topic": "executionreport",
        "ts": 1675406261689,
        "data":
        {
            "msgType": 1,  // edit reject
            "symbol": "SPOT_BTC_USDT",
            "orderId": 54774393,
            "clientOrderId": 11111,
            "reason": ""
        }
    }
    
    // receive when canceling order be rejected
    {
        "topic": "executionreport",
        "ts": 1675406261689,
        "data":
        {
            "msgType": 2,  // cancel reject
            "symbol": "SPOT_BTC_USDT",
            "orderId": 54774393,
            "clientOrderId": 11111,
            "reason": ""
        }
    }
    
    // receive when canceling ALL orders be rejected
    {
        "topic": "executionreport",
        "ts": 1675406261689,
        "data":
        {
            "msgType": 3,  // cancel all reject
            "symbol": "SPOT_BTC_USDT",
            "reason": ""
        }
    }
    
    

## algoexecutionreportv2

  * Push interval: real-time push



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `algoexecutionreportv2`  
      
    
    {
        "id": "clientID3",
        "topic": "algoexecutionreportv2",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "algoexecutionreportv2"
    }
    

**Subscribed Message**
    
    
    {
        "topic": "algoexecutionreportv2",
        "ts": 1667978011834,
        "data": [
            {
                "symbol": "SPOT_BAL_USDT",
                "rootAlgoOrderId": 345181,
                "parentAlgoOrderId": 0,
                "algoOrderId": 345181,
                "clientOrderId": 0,
                "orderTag": "default",
                "status": "NEW",
                "algoType": "BRACKET",
                "side": "SELL",
                "quantity": 1,
                "triggerStatus": "SUCCESS",
                "price": 69,
                "type": "LIMIT",
                "triggerTradePrice": 0,
                "triggerTime": 0,
                "tradeId": 0,
                "executedPrice": 0,
                "executedQuantity": 0,
                "fee": 0,
                "reason": "",
                "feeAsset": "USDT",
                "totalExecutedQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeCurrency": "USDT",
                "totalRebate": 0,
                "rebateCurrency": "BAL",
                "timestamp": 1667978011834,
                "visibleQuantity": 1,
                "reduceOnly": false,
                "activatedPrice": 0,
                "triggered": false,
                "activated": false,
                "maker": false,
                "isTriggered": false,
                "isMaker": false,
                "isActivated": false,
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "leverage": 10,
                "marginMode": "CROSS",
            },
            {
                "symbol": "SPOT_BAL_USDT",
                "rootAlgoOrderId": 345181,
                "parentAlgoOrderId": 345181,
                "algoOrderId": 345182,
                "clientOrderId": 0,
                "orderTag": "default",
                "algoType": "POSITIONAL_TP_SL",
                "side": "BUY",
                "quantity": 0,
                "triggerStatus": "USELESS",
                "price": 0,
                "triggerTradePrice": 0,
                "triggerTime": 0,
                "tradeId": 0,
                "executedPrice": 0,
                "executedQuantity": 0,
                "fee": 0,
                "reason": "",
                "feeAsset": "",
                "totalExecutedQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeCurrency": "USDT",
                "totalRebate": 0,
                "rebateCurrency": "BAL",
                "timestamp": 1667978011900,
                "visibleQuantity": 0,
                "reduceOnly": false,
                "activatedPrice": 0,
                "triggered": false,
                "activated": false,
                "maker": false,
                "isTriggered": false,
                "isMaker": false,
                "isActivated": false,
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "leverage": 10,
                "marginMode": "CROSS",
            },
            {
                "symbol": "SPOT_BAL_USDT",
                "rootAlgoOrderId": 345181,
                "parentAlgoOrderId": 345182,
                "algoOrderId": 345183,
                "clientOrderId": 0,
                "orderTag": "default",
                "algoType": "TAKE_PROFIT",
                "side": "BUY",
                "quantity": 0,
                "triggerPrice": 50,
                "triggerStatus": "USELESS",
                "price": 0,
                "type": "CLOSE_POSITION",
                "triggerTradePrice": 0,
                "triggerTime": 0,
                "tradeId": 0,
                "executedPrice": 0,
                "executedQuantity": 0,
                "fee": 0,
                "reason": "",
                "feeAsset": "",
                "totalExecutedQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeCurrency": "USDT",
                "totalRebate": 0,
                "rebateCurrency": "BAL",
                "timestamp": 1667978011900,
                "visibleQuantity": 0,
                "reduceOnly": true,
                "activatedPrice": 0,
                "triggered": false,
                "activated": false,
                "maker": false,
                "isTriggered": false,
                "isMaker": false,
                "isActivated": false,
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "leverage": 10,
                "marginMode": "CROSS",
            },
            {
                "symbol": "SPOT_BAL_USDT",
                "rootAlgoOrderId": 345181,
                "parentAlgoOrderId": 345182,
                "algoOrderId": 345184,
                "clientOrderId": 0,
                "orderTag": "default",
                "algoType": "STOP_LOSS",
                "side": "BUY",
                "quantity": 0,
                "triggerPrice": 75,
                "triggerStatus": "USELESS",
                "price": 0,
                "type": "CLOSE_POSITION",
                "triggerTradePrice": 0,
                "triggerTime": 0,
                "tradeId": 0,
                "executedPrice": 0,
                "executedQuantity": 0,
                "fee": 0,
                "reason": "",
                "feeAsset": "",
                "totalExecutedQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeCurrency": "USDT",
                "totalRebate": 0,
                "rebateCurrency": "BAL",
                "timestamp": 1667978011900,
                "visibleQuantity": 0,
                "reduceOnly": true,
                "activatedPrice": 0,
                "triggered": false,
                "activated": false,
                "maker": false,
                "isTriggered": false,
                "isMaker": false,
                "isActivated": false,
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "leverage": 10,
                "marginMode": "CROSS",
            }
        ]
    }
    

## position push

  * Push interval: push on update



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | subscribe`/`unsubscribe  
topic | string | Y | position  
      
    
    {
        "id": "clientID5",
        "topic": "position",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID5",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "position"
    }
    

**Subscribed Message**
    
    
    {
        "topic": "position",
        "ts": 1711612096824,
        "data": {
            "positions": [
                "PERP_WOO_USDT": {
                    "holding": 0.0,
                    "pendingLongQty": 0.00020,
                    "pendingShortQty": 0.0,
                    "averageOpenPrice": 0.0,
                    "pnl24H": -1.55902,
                    "fee24H": 0.21800043,
                    "settlePrice": 0.0,
                    "markPrice": 22325.47533333,
                    "version": 93454,
                    "openingTime": 0,
                    "pnl24HPercentage": -0.00542227
                    "adlQuantile": 1,
                    "timestamp": 1677814653001ï¼
                    "leverage": 10,
                    "marginMode": "ISOLATED",
                    "isolatedMarginToken": "USDT",
                    "isolatedMarginAmount": 1000,                
                    "isolatedFrozenLong": 10,
                    "isolatedFrozenShort": 10,
                },
                "PERP_WOO_USDT": {
                    // ... omit existing fields
    
                    "leverage": 10,
                    "marginMode": "CROSS",
                    "isolatedMarginToken": "",
                    "isolatedMarginAmount": 0,                
                    "isolatedFrozenLong": 0,
                    "isolatedFrozenShort": 0,
                }
            ]
        }
    }
    

## marginassignment

  * Push interval: real-time push



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | subscribe`/`unsubscribe  
topic | string | Y | marginassignment  
      
    
    {
        "id": "clientID3",
        "topic": "marginassignment",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "marginassignment"
    }
    

**Subscribed Message**
    
    
    {
         "topic": "marginassignment",
         "ts": 1677814655102,
         "data":{
             "margin": [
                 {   
                     "token": "USDT",
                     "qty": 35.41628771
                 },
                 {
                     "token": "WOO",
                     "qty": 83.62,
                 },
                 ...
             ],
             "orders": [
                 {
                     "id": 5306374839,
                     "symbol": "PERP_NEAR_USDT",
                     "price": 1.7,
                     "type": "LIQUIDATE_BLP",
                     "status": "FILLED",
                     "referencePrice": 1.7,
                     "quantity": 7.0,
                     "side": "BUY",
                     "executedQuantity": 7.0,
                     "executedAmount": 11.9,
                     "visibleQty": 7.0,
                     "feeAsset": "USDT",
                     "fee": 0
                },
                ...
             ]
        }
    }
    
    

# Release Note

All the API changes would be listed here. 

## 2025-09-21

**Post Only Adjusted Order Now Live**

The Post Only Adjusted Order is now supported, giving users more flexibility when providing liquidity.

**How it works:**

  * Normal Post-Only: The order is rejected if it would cross the book and execute immediately as a taker.
  * Post Only Adjusted: Instead of rejecting, the order price is automatically adjusted so it can still rest on the book as a maker. 
    * For buy orders, the price is adjusted to best ask - 1 tick.
    * For sell orders, the price is adjusted to best bid + 1 tick.



## 2025-07-14

**Retail Price Improvement (RPI) Now Live**

The RPI order type is now supported across REST and WebSocket V3 APIs, enabling market makers to provide improved execution for retail flow. Key API updates include:

**REST API Updates**

  * Market Trades (Public) `GET /v1/public/market_trades` added rpi field to response to indicate whether the trade was matched via RPI.
  * Market Trades History(Public) `GET https://api-pub.woo.org/v1/hist/trade` added rpi field to response to indicate whether the trade was matched via RPI.
  * Send Order `POST /v1/order` now supports submitting orders with the RPI order type.
  * Get Orders `GET /v1/orders` supports filtering by RPI order type.
  * Get Trade `GET /v1/client/trade/:tid` added is_match_rpi field to response to indicate whether the trade was matched via RPI.
  * Get Trades `GET /v1/order/:oid/trades` added is_match_rpi field to response to indicate whether the trade was matched via RPI.
  * Get Trade History `GET /v1/client/trades` added is_match_rpi field to response to indicate whether the trade was matched via RPI.
  * Get Archived Trade History `GET /v1/client/hist_trades` added is_match_rpi field to response to indicate whether the trade was matched via RPI.



**WebSocket API V2 Updates**

  * trade topic



Added rpi field to messages to indicate whether the trade was matched via RPI.

  * trades topic



Added rpi field to messages to indicate whether the trade was matched via RPI.

  * executionreport topic



Added rpi field to messages to indicate whether the trade was matched via RPI.

## 2025-04-30

  * For [get-token-history](#get-token-history), the type parameter will be updated from SPOT_TRADING and TRADING_FEE (order-based) to SPOT_TRANSACTION and TRANSACTION_FEE (trade-based). 



## 2024-09-22

  * We plan to release WOO X new domain migration, we are updating our API endpoint(s), please see the following table. Please notice, the new production endpoints will be accessible on 2024/9/22. 

**Environment** | **Old Endpoint** | **New Endpoint**  
---|---|---  
Production | `https://api.woo.org` | `https://api.woox.io`  
| `https://api.woo.network` |   
Production | `wss://wss.woo.org` | `wss://wss.woox.io`  
| `wss://wss.woo.network` |   
Production | `https://api-pub.woo.org` | `https://api-pub.woox.io`  
Staging | `https://api.staging.woo.org` | `https://api.staging.woox.io`  
| `https://api.staging.woo.network` |   
Staging | `wss://wss.staging.woo.org` | `wss://wss.staging.woox.io`  
| `wss://wss.staging.woo.network` |   
  
You only need to replace the base URL, and nothing else needs to be changed. For Production Endpoint base URL change,Please notice, the new production endpoints will be accessible on 2024/9/22.

**API** : `api.woo.org` -> `api.woox.io` **WebSocket** : `wss://wss.woo.org` -> `wss://wss.woox.io`

For Staging Endpoint base URL change,This endpoint is accessible now

**API** : `api.staging.woo.org` -> `api.staging.woox.io` **WebSocket** : `wss://wss.staging.woo.org` -> `wss://wss.staging.woox.io`

  * Add REST API [get-assignmentpreference](#get-assignmentpreference).
  * Add REST API [add-an-assignmentpreference](#add-an-assignmentpreference).
  * Add REST API [delete-an-assignmentpreference](#delete-an-assignmentpreference).
  * Add `network` field in the response of REST API [token network (public)](#token-network-public). 



## 2024-07-14

  * We are going to release Isolated-Margin trading mode in up coming release in 2024-07-04, it will includes following changes:
  * Add `margin_mode` optional parameter for [send-order](#send-order), [send-algo-order](#send-algo-order). 
  * Add `marginMode` and `leverage` in response body for [get-order](#get-order), [get-orders](#get-orders), [get-order-by-client_order_id](#get-order-by-client_order_id).
  * Add `margin_mode` and `leverage` in response body for [get-algo-order](#get-algo-order), [get-algo-orders](#get-algo-orders).
  * Break down the response for [get-all-position-info](#get-all-position-info) and [get-all-position-info](#get-all-position-info-new) to perform the position status of different mode of each symbols by adding `marginMode` and `leverage` fields. Note that [get-one-position-info](#get-one-position-info) will only support to response the `CROSS` mode position of the selected symbol.
  * For [get-account-information-new](#get-account-information-new), the `leverage` field will be become specificially for SPOT/MARGIN leverage, will be deprecated (present null) when account mode is FUTURES. Also, the `totalAccountValue`.
  * For [update-leverage-setting](#update-leverage-setting) endpoint will only supprot MARGIN mode, for FUTURES mode, release new endpoint [update-futures-leverage-setting](#update-futures-leverage-setting) and [get-futures-leverage-setting](#get-futures-leverage-setting) to manage the setting 
  * Add [update-isolated-margin-setting](#update-isolated-margin-setting) endpoint.
  * Add `leverage`, `marginMode`,`isolatedMarginToken`,`isolatedMarginAmount`,`isolatedFrozenLong`,`solatedFrozenShort` fields in the push message of Websocket topic [positions](#position-push).
  * Add `leverage`, `marginMode` fields in the push message of Websocket topic [executionreport](#executionreport) and [algoexecutionreportv2](#algoexecutionreportv2).
  * Sunset RESTful endpoints deprecated by 2023Q1, including [get-current-holding](#get-current-holding) and [get-current-holding-v2](#get-current-holding-v2). Please find the replacement API in [get balances](#get-current-holding-get-balance-new).



## 2024-07-04

  * Adjusted the rate of this API[get-archived-trade-history](#get-archived-trade-history).



## 2024-06-24

  * Add `id` optional parameter for [get-asset-history](#get-asset-history).



## 2024-06-09

  * Add update errorCode definition for order related service[order-service-error-code](#order-service-error-code).



## 2024-05-20

  * Add `x-api-recvwindow` optional paramter for Authenticationï¼only for vip usersï¼



## 2024-05-09

  * Corrected return value for REST API [get-current-holding-get-balance-new](#get-current-holding-get-balance-new).



## 2024-04-22

  * Add REST API [token-withdraw-v3](#token-withdraw-v3).
  * Add return value `balance_token` and `network` for REST API [available-token-(public)](#available-token-public).



## 2024-04-16

  * Add usage instructionsfor REST API [cancel-all-after](#get-cancel-all-after)



## 2024-03-31 ï¼4/2 system releaseï¼

  * Add return value `total_rebate` and `rebate_asset` for REST API [get-order](#get-order), [get-order-by-client_order_id](#get-order-by-client_order_id), [get-orders](#get-orders), [get-algo-order](#get-algo-order) and [get-algo-orders](#get-algo-orders)
  * Add `totalRebate` and `rebateCurrency` message for WSS topic response [executionreport](#executionreport) and [algoexecutionreportv2](#algoexecutionreportv2)
  * Add REST API [cancel-all-after](#cancel-all-after)
  * Add explanation for the parameter `reduce_only` for REST API [send-order](#send-order) and [send-algo-order](#send-algo-order)
  * Upgrade rate limit for [Send Order](#send-order) from 5 requests to 10 requests per symbol per second .



## 2024-03-25

  * Change on webscoekt response data by adding `data` field to all Resopnse Message for the subscription event (`subscribe`), the `data` field will contain the subscribed topic.



## 2024-02-26

  * Add new REST API [Internal-token-withdraw](#internal-token-withdraw) for internal token withdraw
  * Corrected return value for REST API [get-archived-trade-history](#get-archived-trade-history)



## 2024-02-21

  * Corrected return value of `status` paramtere for REST API [get-system-maintenance-status-public](#get-system-maintenance-status-public)



## 2024-02-21

  * Corrected return value of `status` paramtere for REST API [get-system-maintenance-status-public](#get-system-maintenance-status-public)



## 2024-01-30

  * Add `msgType` and `reason` message for WSS topic response [executionreport](#executionreport)



## 2024-01-10

  * Add `positionSide` optional paramtere REST API [Send Order](#send-order),[send-algo-order](#send-algo-order) for placing Short/Long order.



## 2023-12-12

  * Add new Websocket topic [marginassignment](#marginassignment), The topic is design to get margin assignment information.



## 2023-10-30

  * Add REST API [GET InsuranceFund](#get-insurancefund) for fetching insurance fund information.



## 2023-09-25

  * Add `token` optional paramtere REST API [Get Current Holding (Get Balance) - New](#get-current-holding-get-balance-new) for fetching single token's holding information.



## 2023-07-24

  * Upgrade rate limit for [Send Order](#send-order) from 2 requests to 5 requests per symbol per second .
  * Add RESTful API: [Get referrals summary](#get-referrals-summary) and [Get referral reward history](#get-referral-reward-history) for fetching referral rewards detail.



## 2023-07-03

  * Add `averageOpenPrice` and `markPrice` to [Get Current Holding (Get Balances)](#get-current-holding-get-balance-new).
  * Sunset deprecated RESTful API: [Get Account Info](#get-account-information), please find the replacement API in [Get Account Information - New](#get-account-information-new).
  * Sunset deprecated Websocket Topic: [positioninfo](#positioninfo), please find the replacement topic in [balance](#balance).



## 2023-06-12

  * Add `loan_amount` in the response message of API [Get Interest History](#get-interest-history) for side = `LOAN`.
  * Add [Get Token History](#get-token-history) API fetching token balance change history.



## 2023-04-10

  * Add `can_collateral` and `can_short` in the response message of API [Available Token (Public)](#available-token-public).
  * Change response message of Funding Rate related API for new funding rate calculation rules released in 2023-04-10, including [Get Predicted Funding Rate for All Markets](#get-predicted-funding-rate-for-all-markets-public), [Get Predicted Funding Rate for One Market](#get-predicted-funding-rate-for-one-market-public) and [Get Funding Rate History for One Market](#get-funding-rate-history-for-one-market-public).
  * Change [Orderbook Snapshot](#orderbook-snapshot-public) and [Kline](#kline-public) RESTful API from privateto public endpoint. (Those two endpoint will not require authentication anymore).



## 2023-02-06

  * Add [Get Balance](#get-current-holding-get-balance-new) API. The API is design to replace the legacy API [Get Current Holding](#get-current-holding) and [Get Current Holding v2](#get-current-holding-v2).
  * Add [Get Account Information - New](#get-account-information-new). the API is design to replace the legacy API [Get Account Information](#get-account-information).
  * Add [Get All Position Info - New](#get-all-position-info-new). The API is design to replace the legacy API [Get Positions](#get-positions)
  * Add [Get Buy Power](#get-buy-power) for query buying power of selected symbol.
  * Add New Websocket topic [balance](#balance). The topic is design to replace existing topic [positionsinfo](#positionsinfo).



## 2022-12-05

  * Add [Edit Order](#edit-order), [Edit order by client_order_id](#edit-order-by-client_order_id), [Edit Algo Order](#edit-algo-order) and [Edit Algo order by client_order_id](#edit-algo-order-by-client_order_id).
  * Update push frequency for websocket topics: [bbo](#bbo), [24 ticker](#24-ticker), [Open Interest](#openinterest) and [orderbook](#orderbook).
  * Update rate limit for [Get Token Deposit Address](#get-token-deposit-address) and [Token Withdraw](#token-withdraw).



## 2022-11-21

  * Add [Market Trade History](#market-trade-history) for fetching trade history data.



## 2022-10-24

  * Add [Send Algo Order](#send-algo-order) to create Algo Order through the API, support algo types include: `STOP`(stop market & stop limit), `OCO`, `TRAILING_STOP`, `BRACKET` and `POSITIONAL_TP_SL`.
  * Add [Cancel Algo Order](#cancel-algo-order), [Cancel All Pending Algo Orders](#cancel-all-pending-algo-orders) and [Cancel Pending Merge Orders by Symbol](#cancel-pending-merge-orders-by-symbol).
  * Add [Get Algo Order](#get-algo-order) and [Get Algo Orders](#get-algo-orders) to fetch Algo Orders detail through the API.
  * Add [Cancel All Pending Order](#cancel-all-pending-order) to cancel all pending Ordinary Orders (not include Algo Orders) through the API.
  * Update [authentication](#authentication) section for `v3` API to generate the signature with `timestamp`, `request_method`, `request_path` and `request_body`.
  * Add [Get System Maintenance Status](#get-system-maintenance-status-public) API to fetch system status.



## 2022-09-08

  * Add `can_collateral` in the response message of API [Available Token (Public)](#available-token-public).
  * Add `realized_pnl` in the response message of API [Get Order](#get-order), [Get Order by client_order_id](#get-order-by-client_order_id) and [Get Orders](#get-orders). And add `realized_pnl` parameter in the request body of API [Get Orders](#get-orders). The `realized_pnl` field in response will only present the settled amount for futures orders.
  * Newly support `1m` in `type` parameter in the query string of API for [Historical Kline](#kline-historical-data).



## 2022-08-18

  * update [Token Withdraw](#token-withdraw) API by remove `code` parameter, the new version will not require 2FA code for those withdrawal address been verified in the address book.
  * Increase rate limit of [Get All Position info](#get-all-position-info) and [Get One Position info](#get-one-position-info) to 30 requests per second.



## 2022-07-28

  * Add `reduce_only` parameter in the request body of API [Send_Order](#send-order).
  * Add `reduce_only` in the response message of API [Get_Order](#get-order), [Get_Order_by_client_order_id](#get-order-by-client_order_id) and [Get_Orders](#get-orders).
  * Add `source` in the response message of API [Market_Trades(Public)](#market-trades-public).
  * Add `source` in the push message of Websocket Topic [trades](#trade).



## 2022-06-10

  * Add `total_collateral`, `free_collateral`, `total_account_value`, `total_vault_value`, `total_staking_value` and `est_liq_price` for each futures positions in [Position Info](#get-all-position-info).
  * Deprecate websocket subscription topic: [Orderbook](#orderbook) depth 1000, the original {symbol}@orderbook topic will keep alive but push the same data as symbol@orderbook100 (depth 100).



## 2022-05-23

  * Upgrade websocket subscription topic: [bbo](#bbo) push frequency from 200ms to 10ms.
  * Add public API for [Historical Kline](#kline-historical-data).



## 2022-03-21

  * Add public API for [Funding Rate](#get-predicted-funding-rate-for-all-markets-public) and [Futures Info](#get-futures-info-for-all-markets-public).
  * Add private API for [Change Account mode](#update-account-mode), [Change Leverage](#update-leverage-setting).
  * Add private API for [Funding Fee](#get-funding-fee-history), [Position Info](#get-all-position-info).
  * Add `account_mode`, `futures_leverage`, `futures_taker_fee_rate`, `futures_maker_fee_rate` in [Account Information](#get-account-information).
  * Add `futures_margin_factor` in [Token Config](#token-config), 
  * Add Websocket Topics [indexprice](#indexprice), [markprice](#markprice), [openinterest](#openinterest), [estfundingrate](#estfundingrate), [markprices](#markprices), [position push](#position-push)



## 2022-02-25

  * Add API [SubAccount](#get-subaccounts) to manage subaccounts.



## 2022-01-17

  * Add `can_collateral`, `can_short` and `stable` in [Token_Config](#token-config)



## 2021-12-24

  * Add API [Kline](#kline) to query yearly Kline.

  * Add `client_order_id` and `timestamp` in the response message of API [Send_Order](#send-order).




## 2021-11-12

  * Add API [Kline](#kline) to provide at most 1000 klines.



## 2021-10-22

  * Add Public API Token Network to query the token deposit/withdrawal information on each network.

  * Add rate limit on public APIs.




## 2021-09-27

  * Add API [Margin_Interest_Rates](#margin-interest-rates) and [Margin_Interest_Rate_of_Token](#margin-interest-rate-of-token) to query the margin interest rates.



## 2021-09-06

  * Adjust rate limit of API [Get_Order](#get-order) and [Get_Order_by_client_order_id](#get-order-by-client_order_id) to 10 per second in total.

  * Adjust rate limit of API [Cancel_Order](#cancel-order) and [Cancel_Order_by_client_order_id](#cancel-order-by-client_order_id) to 10 per second in total.

  * Adjust rate limit of API [Get_Trade](#get-trade), [Get_Trades](#get-trades) to 10 per second for each.




## 2021-09-03

  * Add API [Token_Config](#token-config)



## 2021-08-06

  * Remove `Transactions` from [Get_Orders](#get-orders)

  * Add `total_fee` and `fee_asset` in [Get_Order](#get-order), [Get_Order_by_client_order_id](#get-order-by-client_order_id), [Get_Orders](#get-orders)




## 2021-07-09

  * Websocket topic [positioninfo](#positioninfo) stop pushing the tokens that have never been traded before to reduce the message size.



## 2021-06-25

  * Add API [Cancel_Order_by_client_order_id](#cancel-order-by-client_order_id)



User could cancel order by the user-specified `client_order_id`.

  * Add API [Get_Trades](#get-trades)



User could get all the trades by `order_id`.

  * Adjust rate limit of API [Send_Order](#send-order) from 120 per minute to 2 per second per symbol



[cURL](#) [Python](#) [Node.js](#) [Java](#)


---

# Source: https://docs.woox.io/v5/trading-api/websocket-api

[ NAV  ](#)

[cURL](#) [Python](#) [Node.js](#) [Java](#)



  * [General Information](#general-information)
  * [Authentication](#authentication)
    * [Example](#example)
    * [Security](#security)
  * [Error Codes](#error-codes)
    * [order service error code](#order-service-error-code)
  * [RESTful API](#restful-api)
    * [Get System Maintenance Status (Public)](#get-system-maintenance-status-public)
    * [Exchange Information](#exchange-information)
    * [Available Symbols (Public)](#available-symbols-public)
    * [Market Trades (Public)](#market-trades-public)
    * [Market Trades History(Public)](#market-trades-history-public)
    * [Orderbook snapshot (Public)](#orderbook-snapshot-public)
    * [Kline (Public)](#kline-public)
    * [Kline - Historical Data (Public)](#kline-historical-data-public)
    * [Available Token (Public)](#available-token-public)
    * [Token Network (Public)](#token-network-public)
    * [Get Predicted Funding Rate for All Markets (Public)](#get-predicted-funding-rate-for-all-markets-public)
    * [Get Predicted Funding Rate for One Market (Public)](#get-predicted-funding-rate-for-one-market-public)
    * [Get Funding Rate History for One Market (Public)](#get-funding-rate-history-for-one-market-public)
    * [Get Futures Info for All Markets (Public)](#get-futures-info-for-all-markets-public)
    * [Get Futures for One Market (Public)](#get-futures-for-one-market-public)
    * [Token Config](#token-config)
    * [Send Order](#send-order)
    * [Cancel all after](#cancel-all-after)
    * [Cancel Order](#cancel-order)
    * [Cancel Order by client_order_id](#cancel-order-by-client_order_id)
    * [Cancel Orders](#cancel-orders)
    * [Cancel All Pending Orders](#cancel-all-pending-orders)
    * [Get Order](#get-order)
    * [Get Order by client_order_id](#get-order-by-client_order_id)
    * [Get Orders](#get-orders)
    * [Edit Order](#edit-order)
    * [Edit Order by client_order_id](#edit-order-by-client_order_id)
    * [Send Algo Order](#send-algo-order)
    * [Cancel Algo Order](#cancel-algo-order)
    * [Cancel All Pending Algo Orders](#cancel-all-pending-algo-orders)
    * [Cancel Pending Merge Orders by Symbol](#cancel-pending-merge-orders-by-symbol)
    * [Get Algo Order](#get-algo-order)
    * [Get Algo Orders](#get-algo-orders)
    * [Edit Algo Order](#edit-algo-order)
    * [Edit Algo Order by client_order_id](#edit-algo-order-by-client_order_id)
    * [Get Trade](#get-trade)
    * [Get Trades](#get-trades)
    * [Get Trade History](#get-trade-history)
    * [Get Archived Trade History](#get-archived-trade-history)
    * [Get Current Holding](#get-current-holding)
    * [Get Current Holding v2](#get-current-holding-v2)
    * [Get Current Holding (Get Balance) - New](#get-current-holding-get-balance-new)
    * [Get Account Information](#get-account-information)
    * [Get Account Information - New](#get-account-information-new)
    * [Get Token History](#get-token-history)
    * [Get Account API Key & Permission](#get-account-api-key-amp-permission)
    * [Get Buy Power](#get-buy-power)
    * [Get Token Deposit Address](#get-token-deposit-address)
    * [Token Withdraw](#token-withdraw)
    * [Token Withdraw V3](#token-withdraw-v3)
    * [Internal token withdraw](#internal-token-withdraw)
    * [Cancel Withdraw Request](#cancel-withdraw-request)
    * [Get Asset History](#get-asset-history)
    * [Margin Interest Rates](#margin-interest-rates)
    * [Margin Interest Rate of Token](#margin-interest-rate-of-token)
    * [Get Interest History](#get-interest-history)
    * [Repay Interest](#repay-interest)
    * [Get referrals summary](#get-referrals-summary)
    * [Get referral reward history](#get-referral-reward-history)
    * [Get Subaccounts](#get-subaccounts)
    * [Get Assets of Subaccounts](#get-assets-of-subaccounts)
    * [Get Asset Details from a Subaccount](#get-asset-details-from-a-subaccount)
    * [Get IP Restriction](#get-ip-restriction)
    * [Get Transfer History](#get-transfer-history)
    * [Transfer Assets](#transfer-assets)
    * [Get LtV info](#get-ltv-info)
    * [Update Account Mode](#update-account-mode)
    * [Update Position Mode](#update-position-mode)
    * [Update Leverage Setting](#update-leverage-setting)
    * [Update Futures Leverage Setting](#update-futures-leverage-setting)
    * [GET Futures Leverage Setting](#get-futures-leverage-setting)
    * [Update Isolated Margin Setting](#update-isolated-margin-setting)
    * [Get Funding Fee History](#get-funding-fee-history)
    * [Get All Position info](#get-all-position-info)
    * [Get All Position info - New](#get-all-position-info-new)
    * [Get One Position info](#get-one-position-info)
    * [GET InsuranceFund](#get-insurancefund)
    * [GET AssignmentPreference](#get-assignmentpreference)
    * [Add an AssignmentPreference](#add-an-assignmentpreference)
    * [Delete an AssignmentPreference](#delete-an-assignmentpreference)
  * [Websocket API V2](#websocket-api-v2)
    * [PING/PONG](#ping-pong)
    * [request orderbook](#request-orderbook)
    * [orderbook](#orderbook)
    * [orderbookupdate](#orderbookupdate)
    * [trade](#trade)
    * [trades](#trades)
    * [24h ticker](#24h-ticker)
    * [24h tickers](#24h-tickers)
    * [bbo](#bbo)
    * [bbos](#bbos)
    * [k-line](#k-line)
    * [indexprice](#indexprice)
    * [markprice](#markprice)
    * [estfundingrate](#estfundingrate)
    * [openinterests](#openinterests)
    * [markprices](#markprices)
    * [auth](#auth)
    * [balance](#balance)
    * [executionreport](#executionreport)
    * [algoexecutionreportv2](#algoexecutionreportv2)
    * [position push](#position-push)
    * [marginassignment](#marginassignment)
  * [Release Note](#release-note)
    * [2025-09-21](#2025-09-21)
    * [2025-07-14](#2025-07-14)
    * [2025-04-30](#2025-04-30)
    * [2024-09-22](#2024-09-22)
    * [2024-07-14](#2024-07-14)
    * [2024-07-04](#2024-07-04)
    * [2024-06-24](#2024-06-24)
    * [2024-06-09](#2024-06-09)
    * [2024-05-20](#2024-05-20)
    * [2024-05-09](#2024-05-09)
    * [2024-04-22](#2024-04-22)
    * [2024-04-16](#2024-04-16)
    * [2024-03-31 ï¼4/2 system releaseï¼](#2024-03-31-4-2-system-release)
    * [2024-03-25](#2024-03-25)
    * [2024-02-26](#2024-02-26)
    * [2024-02-21](#2024-02-21)
    * [2024-02-21](#2024-02-21-2)
    * [2024-01-30](#2024-01-30)
    * [2024-01-10](#2024-01-10)
    * [2023-12-12](#2023-12-12)
    * [2023-10-30](#2023-10-30)
    * [2023-09-25](#2023-09-25)
    * [2023-07-24](#2023-07-24)
    * [2023-07-03](#2023-07-03)
    * [2023-06-12](#2023-06-12)
    * [2023-04-10](#2023-04-10)
    * [2023-02-06](#2023-02-06)
    * [2022-12-05](#2022-12-05)
    * [2022-11-21](#2022-11-21)
    * [2022-10-24](#2022-10-24)
    * [2022-09-08](#2022-09-08)
    * [2022-08-18](#2022-08-18)
    * [2022-07-28](#2022-07-28)
    * [2022-06-10](#2022-06-10)
    * [2022-05-23](#2022-05-23)
    * [2022-03-21](#2022-03-21)
    * [2022-02-25](#2022-02-25)
    * [2022-01-17](#2022-01-17)
    * [2021-12-24](#2021-12-24)
    * [2021-11-12](#2021-11-12)
    * [2021-10-22](#2021-10-22)
    * [2021-09-27](#2021-09-27)
    * [2021-09-06](#2021-09-06)
    * [2021-09-03](#2021-09-03)
    * [2021-08-06](#2021-08-06)
    * [2021-07-09](#2021-07-09)
    * [2021-06-25](#2021-06-25)


  * Copyright @ 2023 WOO Network.



# General Information

**WOO X. A privately-accessible liquidity venue for the trading of cryptocurrencies.**

WOO X provides clients with an easily accessible deep pool of liquidity sourced from the largest exchanges and from Kronosâ HFT proprietary trading. We utilize advanced crossing and routing methods which provide ease of access and superior trade execution to select exchanges. 

We provide two interfaces to communicate between WOO X and clients. 

  * [RESTful API interface](#restful-api): Provides sending events like create order, cancel order, fetch balance, ...etc.
  * [Websocket interface V2](#websocket-api-v2): Provides real-time orderbook data feed and order update feed.



**Base endpoints:**

We will launch a new domain api.woox.io on 2024/09/22. Please note that the old domain api.woo.org will be decommissioned at a later date, which will be announced separately. If you are a new user, please use the new domain api.woox.io for integration. If you are an existing user, you may continue using api.woo.org, but we recommend migrating to api.woox.io as soon as possible to avoid any service disruptions in the future.

  * `https://api.woox.io/` **(Production)**
  * `https://api-pub.woox.io` **(Production)**
  * `https://api.staging.woox.io` **(staging)**



**Authorization:**  
All our interfaces require key to access, and the token will be pre-generated by us.  
Please set the corrsponding header in your request. Refer to [Authenticaton](#authentication) for more information.

**Symbol:**  
WOO X use the following format: `<TYPE>_<BASE>_<QUOTE>` to represent a symbol name, for example: `SPOT_BTC_USDT` means that it is `BTC_USDT` pair in `SPOT` trading market.

**Rate Limit:**

WebSocket Connection:  
\- The establishment of WebSocket connections is based on the application ID.  
\- The application ID should be appended at the end of the wss endpoint.

RESTful API:  
\- For public endpoints, the rate limit is calculated based on the IP address.  
\- For private endpoints, the rate limit is calculated based on the account (i.e., application ID, unique for each main/sub-account).  
\- All api_keys under the same account (i.e., the same application ID) share their rate limits.

WebSocket Service Connection Restrictions:  
\- WebSocket services have limitations on the number of connections and topic subscriptions.  
\- For each account (main and sub-accounts are independent), there is a restriction on the maximum concurrent connection count, set at 80.  
\- The maximum number of topics within each connection is limited to 50.

IP Connection Limitation:  
\- Simultaneously, there is a restriction on the concurrent connection count for each IP address, capped at 1000.

if your application reached the rate limit of a certain endpoint, the server will return an error result with http code `429`. You may need to wait until the next time horizon.

**Error Message:**

> **Errors consist of three parts: an error code, detail message and a success flag.**
    
    
    {
      "success": false,
      "code": -1005, // Error code
      "message": "order_price must be a positive number" // Detail message  
    }
    

All API will return following json when api failed, the "message" will contain the detail error message, it may be because some data is in the wrong format, or another type of error.  
Specific error codes and messages are defined in [Errors Codes](#error-codes).

# Authentication

Client needs to ask for an `api_key`ï¼`api-timestamp` and `api_secret`, and use these to sign your request.

VIP users add an optional `api-recvwindow` to specify the number of milliseconds after `api-timestamp` the request is valid for. If `api-recvwindow` is not specified, it defaults to 5000.If `api-timestamp` \+ `api-recvwindow` > timestamp in dedicated gateway when itâs ready to process the request, throw an error âRequest has failed as the receive window is exceeded.â

## Example

Here we provide a simple example that shows you how to send a valid request to WOO X.  
Assume following infomation:

Key | Value | Description  
---|---|---  
`api_key` | `AbmyVJGUpN064ks5ELjLfA==` | create from WOO X console  
`api_secret` | `QHKRXHPAW1MC9YGZMAT8YDJG2HPR` | create from WOO X console  
`timestamp` | `1578565539808` | Unix epoch time in milliseconds  
`api-recvwindow` | `5000` | specify the number of milliseconds after `api-timestamp` the request is valid for ï¼VIP usersï¼  
  
Hash your request parameters with `api_secret`, the hashing logic is described as follows: 

> **If the request looks like:**
    
    
    POST /v1/order
    
    # Body parameter:
    symbol:SPOT_BTC_USDT
    order_type:LIMIT
    order_price:9000
    order_quantity:0.11
    side:BUY
    

For `v1` API, please follow the steps to normalize request content:

  1. use **query string** as the parameters for **GET** methods and **body parameters** for **POST** and **DELETE** methods.
  2. concat **query string** and **body parameters** in an alphabetical order in [query string format](https://en.wikipedia.org/wiki/Query_string).
  3. concat `timestamp` with the above result, using `|` as seperator.



> **Normalize request content for V1 API, The result content would look like following**
    
    
    order_price=9000&order_quantity=0.11&order_type=LIMIT&side=BUY&symbol=SPOT_BTC_USDT|1578565539808
    

For `v3` API using request body to pass the parameters, please concatenate the `timestamp`, `http request method`, `request_path` and `request_body` as the normalized content to sign. Besides, please use `application/json` as `Content-Type` in the headers.

var signString = timestamp + method + request_path + request_body;

> **Normalize request content for V3 API, The result content would look like following**
    
    
    1578565539808POST/v3/algo/order{
        "symbol": "PERP_BTC_USDT",
        "side": "BUY",
        "reduceOnly": false,
        "type": "MARKET",
        "quantity": "1",
        "algoType": "TRAILING_STOP",
        "callbackRate": "0.012"
    }
    

> **Then use`api_secret` to hash it with HMAC `SHA256` algorithm, you can use `openssl` to get this:**
    
    
    $ echo -n "order_price=9000&order_quantity=0.11&order_type=LIMIT&side=BUY&symbol=SPOT_BTC_USDT|1578565539808" | openssl dgst -sha256 -hmac "QHKRXHPAW1MC9YGZMAT8YDJG2HPR"
    (stdin)= 20da0852f73b20da0208c7e627975a59ff072379883d8457d03104651032033d
    

Put the **HMAC signature** in request header `x-api-signature`, and put **timestamp** in `x-api-timestamp`, and also **api key** in `x-api-key`.

**So the final request would look like:**

POST /v1/order HTTP/1.1 Content-Type: application/x-www-form-urlencoded x-api-key: AbmyVJGUpN064ks5ELjLfA== x-api-signature: 20da0852f73b20da0208c7e627975a59ff072379883d8457d03104651032033d x-api-timestamp: 1578565539808 cache-control: no-cache symbol=SPOT_BTC_USDT order_type=LIMIT order_price=9000 order_quantity=0.11 side=BUY 

> **sample code**
    
    
    # python sample code for generate signature
    import datetime
    import hmac, hashlib, base64
    import requests
    import json
    
    
    staging_api_secret_key = '6XXXXXXXXXXXXXXXXXXXXXXXB'
    staging_api_key = 'Ppppppppppppppppppp=='
    
    def _generate_signature(data):
      key = staging_api_secret_key#'key' # Defined as a simple string.
      key_bytes= bytes(key , 'utf-8') # Commonly 'latin-1' or 'utf-8'
      data_bytes = bytes(data, 'utf-8') # Assumes `data` is also a string.
      return hmac.new(key_bytes, data_bytes , hashlib.sha256).hexdigest()
    
    
    milliseconds_since_epoch = round(datetime.datetime.now().timestamp() * 1000)
    
    headers = {
        'x-api-timestamp': str(milliseconds_since_epoch),
        'x-api-key': staging_api_key,
        'x-api-signature': _generate_signature("client_order_id=123456&order_price=0.8148&order_quantity=10&order_type=LIMIT&side=BUY&symbol=PERP_XRP_USDT|"+str(milliseconds_since_epoch)),
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cache-Control':'no-cache'
    }
    data = {
      'client_order_id':123456,
      'order_price' : 0.8148,
      'order_quantity': 10,
      'order_type': 'LIMIT',
      'side':'BUY',
      'symbol': 'PERP_XRP_USDT'
    }
    
    
    
    response = requests.post('https://api.staging.woo.org/v1/order', headers=headers, data=data )
    print(response.json())
    
    
    
    
    # Get current timestamp in milliseconds
    milliseconds_since_epoch = str(int(datetime.datetime.now().timestamp() * 1000))
    
    # Define query parameters
    params = {
        "page": 14,
        "size": 100,
        "from": 1,
        "to": 1739215032222
    }
    
    # Construct request path and query string
    request_path = '/v3/referrals'
    query_string = '&'.join([f"{key}={value}" for key, value in params.items()])
    url = f'https://api.woox.io{request_path}?{query_string}'
    
    # Concatenate signature content: timestamp + method + request_path + query_string
    signature_payload = milliseconds_since_epoch + 'GET' + request_path + '?' + query_string
    
    # Generate signature
    def _generate_signature(data):
        key_bytes = bytes(prod_api_secret_key, 'utf-8')
        data_bytes = bytes(data, 'utf-8')
        return hmac.new(key_bytes, data_bytes, hashlib.sha256).hexdigest()
    
    signature = _generate_signature(signature_payload)
    
    # Set headers
    headers = {
        'x-api-timestamp': milliseconds_since_epoch,
        'x-api-key': prod_api_key,
        'x-api-signature': signature,
        'Cache-Control': 'no-cache'
    }
    
    # Send GET request with query parameters
    response = requests.get(url, headers=headers)
    
    # Print response
    print(response.content)
    
    
    
    
    
    
    // Node.js sample code for generate signature
    var cryptoJS = require('crypto-js');
    var axios = require('axios');
    async function getAccountInfo() {
    
      const xApiTimestamp = Date.now();
    
      const queryString = '|' + xApiTimestamp;
    
      production_api_secret_key = '3XXXXXXXXXXXXXXXXXXXXXXXXXXXZ'
      production_api_key = 'xxxxxxxxxxxxxxxxxxxxxxxxx=='
      console.log(cryptoJS.HmacSHA256(queryString, production_api_secret_key).toString());
      const headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'x-api-key': production_api_key,
        'x-api-signature': cryptoJS.HmacSHA256(queryString, production_api_secret_key).toString(),
        'x-api-timestamp': xApiTimestamp,
        'cache-control': 'no-cache'
    
      };
    
    
    
      try {
        const res = await axios.get('https://api.woo.org' + '/v1/client/info', {headers:headers});
    
        console.log('response', res);
    
        return res;
    
      } catch (error) {
        console.log(error.response)
        // throw new Error('Error with getAccountInfo : ' + error.message + '\n' + 'queryString : ' + queryString)
    
      }
    
    }
    
    
    getAccountInfo()
    

## Security

There have four-layer checker to check if a request is valid. WOO X server only accepts the request that passed all checkers. The checker is defined as follows:

**Revoken checker:**  
The api key/secret can be revoked manaually by clients' request. if the key was revoked, all access tokens generated by this key cannot be used.

**Request IP checker:**  
The api key/secret can be tied to specific ips (default is empty). if the request is not coming from allowed ip addresses, the request would be rejected.

**Request Timestamp checker:**  
The request would be considered expired and get rejected if the timestamp in `x-api-timestamp` header has a 300+ second difference from the API server time.

**HMAC Parameter Signature:**  
The request must have a `x-api-signature` header that is generated from request parameters and signed with your secret key.

# Error Codes

Errors consist of three parts: an error code and a message. Codes are universal, but messages can vary. Here is the error JSON payload:
    
    
    {
      "success": false,
      "code": -1001, // Error code
      "message": "order_price must be a positive number" // Detail message  
    }
    

Error Code | Status Code | Error Name | Description  
---|---|---|---  
`-1000` | 500 | `UNKNOWN` | An unknown error occurred while processing the request.  
`-1001` | 401 | `INVALID_SIGNATURE` | The api key or secret is in wrong format.  
`-1002` | 401 | `UNAUTHORIZED` | API key or secret is invalid, it may be because the key has insufficient permission or the key is expired/revoked.  
`-1003` | 429 | `TOO_MANY_REQUEST` | Rate limit exceed.  
`-1004` | 400 | `UNKNOWN_PARAM` | An unknown parameter was sent.  
`-1005` | 400 | `INVALID_PARAM` | Some parameters are in the wrong format for api.  
`-1006` | 400 | `RESOURCE_NOT_FOUND` | The data is not found in the server. For example, when the client try canceling a CANCELLED order, will raise this error.  
`-1007` | 409 | `DUPLICATE_REQUEST` | The data already exists or your request is duplicated.  
`-1008` | 400 | `QUANTITY_TOO_HIGH` | The quantity of settlement is higher than you can request.  
`-1009` | 400 | `CAN_NOT_WITHDRAWAL` | Can not request withdrawal settlement, you need to deposit other arrears first.  
`-1011` | 400 | `RPC_NOT_CONNECT` | Can not place/cancel orders, it may be because of internal network error. Please try again in a few seconds.  
`-1012` | 400 | `RPC_REJECT` | The place/cancel order request is rejected by internal module, it may be because the account is in liquidation or other internal errors. Please try again in a few seconds.  
`-1101` | 400 | `RISK_TOO_HIGH` | The risk exposure for the client is too high, it may be caused by sending too big order or the leverage is too low. please refer to [client info](#get-account-information) to check the current exposure.  
`-1102` | 400 | `MIN_NOTIONAL` | The order value (price * size) is too small.  
`-1103` | 400 | `PRICE_FILTER` | The order price is not following the tick size rule for the symbol.  
`-1104` | 400 | `SIZE_FILTER` | The order quantity is not following the step size rule for the symbol.  
`-1105` | 400 | `PERCENTAGE_FILTER` | Price is X% too high or X% too low from the mid price.  
  
## order service error code

code | errorCode | message  
---|---|---  
-1005 | 317136 | Edit tpsl quantity is not allowed for quantity bracket  
-1005 | 317137 | Edit quantity should edit both legs  
-1005 | 317138 | Edit quantity should be same for both legs  
-1005 | 317139 | Trigger price of 1st leg should not be empty for STOP_BRACKET  
-1005 | 317140 | The quantity of a quantity TP/SL order should not be empty.  
-1005 | 317141 | The algo quantity TP/SL limit order should have field price  
-1005 | 317142 | The algo trigger type of quantity TP/SL should not be CLOSE_POSITION  
-1005 | 317143 | The side of TP/SL legs should be the same  
-1006 | 317144 | IndexPrice is not supported for non spot symbol ${symbol}  
-1103 | 317145 | same as INVALID_PRICE_QUOTE_MIN but different 'code'  
-1103 | 317146 | same as INVALID_PRICE_QUOTE_MAX but different 'code'  
-1103 | 317147 | same as INVALID_PRICE_TICKER_SIZE but different 'code'  
-1005 | 317148 | symbol can't be empty.  
-1006 | 317149 | same with TRADE_NOT_FOUND with different ErrorCodes  
-1005 | 317150 | trigger price must be greater than ${price}  
-1005 | 317151 | trigger price must be less than ${price}  
-1005 | 317152 | The order not found for the order id : ${orderId}  
-1005 | 317153 | child order not found for the order id : ${orderId}  
-1012 | 317154 | RPC failed: error: ${msg}  
-1005 | 317155 | unsupported symbol: ${symbol}  
-1006 | 317156 | unsupported symbol: ${symbol}  
-1006 | 317157 | Trading with ${symbol1}/${symbol2} is temporarily suspended. Please try again later.  
-1006 | 317158 | Trading with ${token}-PERP is temporarily suspended. Please try again later.  
-1005 | 317159 | This pair is currently not supported.  
-1006 | 317160 | The order id and symbol are not matched  
-1006 | 317161 | The order is completed  
-1005 | 317162 | The params should not be null or 0  
-1005 | 317163 | cannot edit TP/SL quantity under bracket order  
-1006 | 317164 | Invalid client order id  
-1006 | 317165 | invalid order id list  
-1006 | 317166 | invalid client order id list  
-1005 | 317167 | unsupported algo type: ${algoType}  
-1000 | 317168 | Order failed due to internal service error. Please contact customer service.  
-1006 | 317169 | Trading with ${left}/${right} is temporarily suspended. Please try again later.  
-1005 | 317170 | The order quantity must bigger than the executed quantity.  
-1000 | 317171 | error path format  
-1005 | 317172 | The userId should not be null or 0  
-1005 | 317173 | The orderId should not be null or 0  
-1006 | 317174 | The order is processing  
-1005 | 317176 | The trigger after should from 0 to ${maxTriggerAfter}  
-1005 | 317177 | Order has terminated  
-1005 | 317178 | The receive window is invalid.  
-1005 | 317179 | Request has failed as the receive window: ${recv_window} millisecond is exceeded from ${api_timestamp}  
-1006 | 317184 | The order cannot be found, or it is already completed.  
-1012 | 317206 | Spot trading is disabled while futures credits are active. Please remove or fully utilize your futures credits to enable spot trading.  
-1012 | 317207 | Request failed. Please ensure you have sufficient USDT to cover the futures credits currently in use.  
  
# RESTful API

## Get System Maintenance Status (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/system_info `

For fetch system status to check if system is down or under maintenance.

> **Response**
    
    
    { 
        // functioning properly
        "success":true,
        "data":
            {
                "status":0,
                "msg":"System is functioning properly."
            },
        "timestamp":1676335013700
    }
    {   
        // trading maintenance
        "success":true,
        "data":
            {
                "status":1,
                "msg":"Under trading maintenance."
            },
        "timestamp":1676335013700
    }
    
    {   
        // system maintenance
        "success":true,
        "data":
            {
                "status":2,
                "msg":"Under system maintenance."
            },
        "timestamp":1676335013700
    }
    

**Parameters**

None

## Exchange Information

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/info/:symbol `

Get send order requirement by symbol, there are some rules need to be fullfilled in order to successfully send order, which are defined as follows:

Price filter

  * `price` >= `quote_min`
  * `price` <= `quote_max`
  * `(price - quote_min) % quote_tick` should equal to zero
  * `price` <= `asks[0].price * (1 + price_range)` when BUY
  * `price` >= `bids[0].price * (1 - price_range)` when SELL



Size filter

  * `base_min` <= `quantity` <= `base_max`
  * `(quantity - base_min) % base_tick` should equal to zero



Min Notional filter

  * `price * quantity` should greater than `min_notional`



Risk Exposure filer

  * For margin trading, the margin rate should exceed a certain threshold as per leverage. For spot trading, the order size should be within the holding threshold. See [account_info](#get-account-information)



> **Response**
    
    
    {
        "success":true,
        "info":{
            "symbol":"PERP_ETH_USDT",
            "quote_min":0,
            "quote_max":10000,
            "quote_tick":0.01,
            "base_min":0.001,
            "base_max":5000,
            "base_tick":0.001,
            "min_notional":0,
            "price_range":0.03,
            "price_scope":0.4,
            "created_time":"1647838759.000",
            "updated_time":"1693437961.000",
            "is_stable":0,
            "is_trading":1,
            "precisions":[1,10,50,100,1000,10000],
            "is_prediction":0,
            "base_mmr":0.012,
            "base_imr":0.02
        }
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
  
## Available Symbols (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/info `

Get the available symbols that WOO X supports, and also send order rules for each symbol. The definition of rules can be found at [Exchange Infomation](#exchange-information)

> **Response**
    
    
    {
      "success": true,
      "rows": [
        {
          "created_time": "1575441595.65", // Unix epoch time in seconds
          "updated_time": "1575441595.65", // Unix epoch time in seconds
          "symbol": "SPOT_BTC_USDT",
          "quote_min": 100,
          "quote_max": 100000,
          "quote_tick": 0.01,
          "base_min": 0.0001,
          "base_max": 20,
          "base_tick": 0.0001,
          "min_notional": 0.02,
          "price_range": 0.99,
          "price_scope": 0.01,
          "precisions":[1,10,100,500,1000,10000]
        },
        // ...
      ]
    }
    

**Parameters**

None

## Market Trades (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/market_trades `

Get latest market trades. The response output "source" 1=internal (trade on WOO X), 0=external (trade from aggregrated sources)

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "symbol": "SPOT_ETH_USDT",
                "side": "BUY",
                "source": 0,
                "executed_price": 202,
                "executed_quantity": 0.00025,
                "executed_timestamp": "1567411795.000", // Unix epoch time in seconds
                "rpi": true
            },
            {
                "symbol": "SPOT_ETH_USDT",
                "side": "BUY",
                "source": 1,
                "executed_price": 202,
                "executed_quantity": 0.00025,
                "executed_timestamp": "1567411795.000", // Unix epoch time in seconds
                "rpi": true
            }
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
limit | number | N (default: 10) | Numbers of trades you want to query.  
  
## Market Trades History(Public)

**Limit: 1 requests per 1 second per IP address**

` GET https://api-pub.woo.org/v1/hist/trade `

Get historical market trades data. The response output "source" 1=internal (trade on WOO X), 0=external (trade from aggregrated sources)

> **Response**
    
    
    {
        "success": true,
        "data":{
            "rows": [
                {
                    "symbol": "SPOT_ETH_USDT",
                    "side": "BUY",
                    "source": 0,
                    "executed_price": 202,
                    "executed_quantity": 0.00025,
                    "executed_timestamp": "1567411795.000", // Unix epoch time in seconds
                    "rpi": true
                },
                {
                    "symbol": "SPOT_ETH_USDT",
                    "side": "BUY",
                    "source": 1,
                    "executed_price": 202,
                    "executed_quantity": 0.00025,
                    "executed_timestamp": "1567411795.000", // Unix epoch time in seconds
                    "rpi": true
                }
            ],
            "meta":{
                "total":10911159,
                "records_per_page":100,
                "current_page":1
            }
        },
        "timestamp":1669072422897
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
page | number | N (default: 1) |   
size | number | N (default: 25) |   
start_time | number | Y | start range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
symbol | string | Y |   
  
## Orderbook snapshot (Public)

**Limit: 10 requests per 1 second**

` GET /v1/public/orderbook/:symbol `

SNAPSHOT of current orderbook. Price of asks/bids are in descending order. Note: The original endpoint `GET /v1/orderbook/:symbol` can still be used.

> **Response**
    
    
    {
        "success": true,
        "asks": [
            {
                "price": 10669.4,
                "quantity": 1.56263218
            },
            {
                "price": 10670.3,
                "quantity": 0.36466977
            },
            {
                "price": 10670.4,
                "quantity": 0.06738009
            }
        ],
        "bids": [
            {
                "price": 10669.3,
                "quantity": 0.88159988
            },
            {
                "price": 10669.2,
                "quantity": 0.5
            },
            {
                "price": 10668.9,
                "quantity": 0.00488286
            }
        ],
        "timestamp": 1564710591905   // Unix epoch time in milliseconds
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
max_level | number | N (default: 100) | the levels you wish to show on both sides.  
  
## Kline (Public)

**Limit: 10 requests per 1 second**

` GET /v1/public/kline `

The latest klines of the trading pairs. Note: The original endpoint `GET /v1/kline` can still be used.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "open": 66166.23,
                "close": 66124.56,
                "low": 66038.06,
                "high": 66176.97,
                "volume": 23.45528526,
                "amount": 1550436.21725288,
                "symbol": "SPOT_BTC_USDT",
                "type": "1m",
                "start_timestamp": 1636388220000, // Unix epoch time in milliseconds
                "end_timestamp": 1636388280000
            },
            {
                "open": 66145.13,
                "close": 66166.24,
                "low": 66124.62,
                "high": 66178.60,
                "volume": 15.50705000,
                "amount": 1025863.18892610,
                "symbol": "SPOT_BTC_USDT",
                "type": "1m",
                "start_timestamp": 1636388160000,
                "end_timestamp": 1636388220000
            },
            // ...skip
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
type | enum | Y | `1m`/`5m`/`15m`/`30m`/`1h`/`4h`/`12h`/`1d`/`1w`/`1mon`/`1y`  
limit | number | N (default: 100) | Numbers of klines. Maximum of 1000 klines.  
  
## Kline - Historical Data (Public)

**Limit: 1 request per 1 second per IP**

` GET https://api-pub.woo.org/v1/hist/kline `

The historical klines of the trading pairs. Note that the endpoint is different with other APIs.

> **Response**
    
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "open": 66166.23,
                    "close": 66124.56,
                    "low": 66038.06,
                    "high": 66176.97,
                    "volume": 23.45528526,
                    "amount": 1550436.21725288,
                    "symbol": "SPOT_BTC_USDT",
                    "type": "1m",
                    "start_timestamp": 1636388220000, // Unix epoch time in milliseconds
                    "end_timestamp": 1636388280000
                },
                {
                    "open": 66145.13,
                    "close": 66166.24,
                    "low": 66124.62,
                    "high": 66178.60,
                    "volume": 15.50705000,
                    "amount": 1025863.18892610,
                    "symbol": "SPOT_BTC_USDT",
                    "type": "1m",
                    "start_timestamp": 1636388160000,
                    "end_timestamp": 1636388220000
                },
                // ...skip
            ],
            "meta":{
                "total":67377,
                "records_per_page":100,
                "current_page":1
            }
        },
        "timestamp": 1636388280000
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
type | enum | Y | `1m`/`5m`/`15m`/`30m`/`1h`/`4h`/`12h`/`1d`/`1w`/`1mon`  
start_time | number | Y | start range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_time | number | N | end range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
size | number | N (default: 100) | The page size, default 100  
page | number | N (default: 1) | the page you wish to query.  
  
## Available Token (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/token `

Get the available tokens that WOO X supports, it need to use when you call get deposit address or withdraw api.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "created_time": "1579399877.02", // Unix epoch time in seconds
                "updated_time": "1579399877.02", // Unix epoch time in seconds
                "token": "BTC",
                "delisted": false,
                "balance_token": "BTC",
                "fullname": "Bitcoin",
                "network": "BTC",
                "decimals": 8,
                "can_collateral":true,
                "can_short":true
            }
    
        ]
    }
    

**Parameters**

None

## Token Network (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/token_network `

Get the available networks for each token as well as the deposit/withdrawal information.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "protocol": "ERC20",
                "network": "ETH",
                "token": "1INCH",
                "name": "Ethereum (ERC20)",
                "minimum_withdrawal": 70,
                "withdrawal_fee": 35,
                "allow_deposit": 1,
                "allow_withdraw": 1
            },
            {
                "protocol": "ERC20",
                "network": "ETH",
                "token": "AAVE",
                "name": "Ethereum (ERC20)",
                "minimum_withdrawal": 0.12,
                "withdrawal_fee": 0.06,
                "allow_deposit": 1,
                "allow_withdraw": 1
            },
            {
                "protocol": "BEP20",
                "network": "BSC",
                "token": "ACE",
                "name": "BNB Smart Chain (BEP20)",
                "minimum_withdrawal": 5,
                "withdrawal_fee": 2.5,
                "allow_deposit": 1,
                "allow_withdraw": 1
            },
            {
                "protocol": "ADA",
                "network": "ADA",
                "token": "ADA",
                "name": "Cardano",
                "minimum_withdrawal": 24,
                "withdrawal_fee": 12,
                "allow_deposit": 1,
                "allow_withdraw": 1
            },
            // ...
        ]
    }
    

**Parameters**

None

## Get Predicted Funding Rate for All Markets (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/funding_rates `

Get predicted funding rate and the latest funding rate for all the markets.

> **Response**
    
    
    {
        "success":true,
        "rows": [
            {
                "symbol":"PERP_BTC_USDT",
                "est_funding_rate":-0.00001392,
                "est_funding_rate_timestamp":1681069199002,
                "last_funding_rate":-0.00001666,
                "last_funding_rate_timestamp":1681066800000,
                "next_funding_time":1681070400000,
                "last_funding_rate_interval":1,
                "est_funding_rate_interval":1
            },
            {
                "symbol":"PERP_ETH_USDT",
                "est_funding_rate":-0.00001394,
                "est_funding_rate_timestamp":1681069319011,
                "last_funding_rate":-0.00001661,
                "last_funding_rate_timestamp":1681066800000,
                "next_funding_time":1681070400000,
                "last_funding_rate_interval":1,
                "est_funding_rate_interval":1
            }
        ],
        "timestamp":1681069222726, // Unix epoch time in milliseconds
    }
    

## Get Predicted Funding Rate for One Market (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/funding_rate/:symbol `

Get predicted funding rate and the latest funding rate for one market.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
  
> **Response**
    
    
    {
        "success":true,
        "timestamp":1681069222726,
        "symbol":"PERP_BTC_USDT",
        "est_funding_rate":-0.00001392,
        "est_funding_rate_timestamp":1681069199002,
        "last_funding_rate":-0.00001666,
        "last_funding_rate_timestamp":1681066800000, // use rate to end calculating funding fee time
        "next_funding_time":1681070400000,
        "last_funding_rate_interval":1,
        "est_funding_rate_interval":1
    }
    

## Get Funding Rate History for One Market (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/funding_rate_history `

Get funding rate for one market.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp. If start_t and end_t are not filled, the newest funding rate will be returned.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp. If start_t and end_t are not filled, the newest funding rate will be returned.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
> **Response**
    
    
    {
        "success": true,
        "meta": {
            "total": 670,
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
            {
                "symbol": "PERP_BTC_USDT",
                "funding_rate": 0.12345689,
                "funding_rate_timestamp": 1567411795000, // use rate to end calculating funding fee time
                "next_funding_time": 1567411995000
            },
            {
                "symbol": "PERP_BTC_USDT",
                "funding_rate": 0.12345689,                                                 
                "funding_rate_timestamp": "1567411795.000", // use rate to end calculating funding fee time
                "next_funding_time": 1567411995000
            }
        ],
        "timestamp": 1564710591905 // Unix epoch time in milliseconds
    }
    

## Get Futures Info for All Markets (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/futures `

Get basic futures information for all the markets.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
              "symbol": "PERP_BTC_USDT",
                    "index_price": 56727.31344564,
                    "mark_price": 56727.31344564,
                    "est_funding_rate": 0.12345689,
                    "last_funding_rate": 0.12345689,
                    "next_funding_time": 1567411795000,
                    "open_interest": 0.12345689, // Open Interest is obtained in real-time.
                    "24h_open": 0.16112,
                    "24h_close": 0.32206,
                    "24h_high": 0.33000,
                    "24h_low": 0.14251,
                    "24h_volume": 89040821.98,
                    "24h_amount": 22493062.21
            },
            {
                "symbol": "PERP_ETH_USDT",
                    "index_price": 6727.31344564,
                    "mark_price": 6727.31344564,
                    "est_funding_rate": 0.12345689,
                    "last_funding_rate": 0.12345689,
                    "next_funding_time": 1567411795000,
                    "open_interest": 0.12345689,
                    "24h_open": 0.16112,
                    "24h_close": 0.32206,
                    "24h_high": 0.33000,
                    "24h_low": 0.14251,
                    "24h_volume": 89040821.98,
                    "24h_amount": 22493062.21
            }
        ],
        "timestamp": 1564710591905 // Unix epoch time in milliseconds
    }
    

## Get Futures for One Market (Public)

**Limit: 10 requests per 1 second per IP address**

` GET /v1/public/futures/:symbol `

Get basic futures information for one market.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
  
> **Response**
    
    
    {
        "success": true,
        "info":{
            "symbol": "PERP_BTC_USDT",
            "index_price": 56727.31344564,
            "mark_price": 56727.31344564,
            "est_funding_rate": 0.12345689,
            "last_funding_rate": 0.12345689,
            "next_funding_time": 1567411795000,
            "open_interest": 0.12345689,
            "24h_open": 0.16112,
           "24h_close": 0.32206,
           "24h_high": 0.33000,
           "24h_low": 0.14251,
           "24h_volume": 89040821.98,
           "24h_amount": 22493062.21
        },
        "timestamp": 1564710591905 // Unix epoch time in milliseconds
    }
    

## Token Config

**Limit: 10 requests per 1 second**

` GET /v1/client/token `

Get the configuration (collateral ratio, margin ratio factor etc) of the token.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "token": "BTC",
                "collateral_ratio": 0.85,
                "margin_factor": 2.3e-8,
                "futures_margin_factor": 2.3e-8,
                "collateral": true,        // if the token is now used as collateral
                "can_collateral": true,    // if the token can be used as collateral
                "can_short": true,         // if the token supports short selling
                "stable": false,            // if the token is stable coin or not
                'margin_max_leverage': 5, 
                'futures_max_leverage': 20, 
                'margin_max_position': 100000000000,
                'futures_max_position': 100000000000
            },
            {
                "token": "ETH",
                "collateral_ratio": 0.85,
                "margin_factor": 2.5e-8,
                "futures_margin_factor": 2.3e-8,
                "collateral": true,
                "can_collateral": true,
                "can_short": true,
                "stable": false, 
                'margin_max_leverage': 5, 
                'futures_max_leverage': 20, 
                'margin_max_position': 100000000000,
                'futures_max_position': 100000000000
            },
            {
                "token": "ASD",
                "collateral_ratio": 1,
                "margin_factor": 0,
                "futures_margin_factor": 0,
                "collateral": false,
                "can_collateral": false,
                "can_short": false,
                "stable": false, 
                'margin_max_leverage': 5, 
                'futures_max_leverage': 20, 
                'margin_max_position': 100000000000,
                'futures_max_position': 100000000000
            }
        ]
    }
    

**Parameters**

None

## Send Order

**Limit: 10 requests per 1 second**

` POST /v1/order `

Place order maker/taker, the order executed information will be updated from websocket stream. will respond immediately with an order created message.

`MARKET` type order behavior: it matches until all size is executed. If the size is too large (larger than the whole book) or the matching price exceeds the price limit (refer to `price_range`), then the remaining quantity will be cancelled.

`IOC` type order behavior: it matches as much as possible at the order_price. If not fully executed, then remaining quantity will be cancelled.

`FOK` type order behavior: if the order can be fully executed at the order_price then the order gets fully executed otherwise it would be cancelled without any execution.

`ASK` type order behavior: the order price is guaranteed to be the best ask price of the orderbook if it gets accepted.

`BID` type order behavior: the order price is guaranteed to be the best bid price of the orderbook if it gets accepted.

`RPI` type order behavior: only available to designated market makers. visible quantity must equal order quantity.

`visible_quantity` behavior: it sets the maximum quantity to be shown on orderbook. By default, it is equal to order_quantity, negative number and number larger than `order_quantity` is not allowed. If it sets to 0, the order would be hidden from the orderbook. It doesn't work for `MARKET`/`IOC`/`FOK` orders since orders with these types would be executed and cancelled immediately and not be shown on orderbook. For `LIMIT`/`POST_ONLY` order, as long as it's not complete, `visible_quantity` is the maximum quantity that is shown on the orderbook.

`order_amount` behavior: for `MARKET`/`BID`/`ASK` order, order can be placed by `order_amount` instead of `order_quantity`. It's the size of the order in terms of the quote currency instead of the base currency. The order would be rejected if both `order_amount` and `order_quantity` are provided. The precision of the number should be within 8 digits.

`client_order_id` behavior: customized order_id, a unique id among open orders. Orders with the same `client_order_id` can be accepted only when the previous one if completed, otherwise the order will be rejected.

For `MARKET`/`BID`/`ASK` order, if margin trading is disabled, `order_amount` is not supported when placing SELL order while `order_quantity` is not supported when placing BUY order.

For `Long`/ `Short` order, It is supported when position mode is HEDGE_MODE and the trading involves futures.

`reduce_only` behavior: only applicable to perpetual symbols. When reduce only is set to true, the system ensures that the order will reduce the position size rather than increasing it. To facilitate this, the system must group related orders to accurately manage the reduce only calculations. There is a cap of 50 orders that can be grouped together and if the limit is exceeded, the system will reject the incoming order.

> **Response**
    
    
    {
      "success": true,
      "order_id": 13,
      "client_order_id": 0,
      "order_type": "LIMIT",
      "order_price": 100.12,
      "order_quantity": 0.987654,
      "order_amount": null,
      "reduce_only": false,
      "timestamp": "1639980423.855" // Unix epoch time in seconds
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
client_order_id | number | N | number for scope : from 0 to 9223372036854775807. (default: 0)  
margin_mode | enum | N | `CROSS`/`ISOLATED`, defualt will be `CROSS`. The `ISOLATED` option only applicable to perp symbols, will be rejected if passed in for spot symbols   
order_tag | string | N | An optional tag for this order. (default: `default`)  
order_type | enum | Y | `LIMIT`/`MARKET`/`IOC`/`FOK`/`POST_ONLY`/`ASK`/`BID`/`RPI`  
post_only_adjusted | boolean | N | when order_type is `POST_ONLY`, `post_only_adjusted` can be true.  
order_price | number | N | If order_type is `MARKET`, then is not required, otherwise this parameter is required.  
order_quantity | number | N | For `MARKET`/`ASK`/`BID` order, if `order_amount` is given, it is not required.  
order_amount | number | N | For `MARKET`/`ASK`/`BID` order, the order size in terms of quote currency  
reduce_only | boolean | N | true or false, default false,If the user's RO order message contains 50 pending orders,the order can be created successfully placed.  
visible_quantity | number | N | The order quantity shown on orderbook. (default: equal to `order_quantity`)  
side | enum | Y | `SELL`/`BUY`  
position_side | enum | N | `SHORT`/`LONG`, If position mode is HEDGE_MODE and the trading involves futures,then is required, otherwise this parameter is not required.  
  
## Cancel all after

**Limit: 10 requests per 1 second**

` POST v1/order/cancel_all_after `

Provide a dead man switch to ensure user orders are canceled in case of an outage. If called repeatedly, the new timeout offset will replace the existing one if already set.When count down hits 0, all of the userâs ordinary and algo orders will be canceled.This API is only available to VIP users.Please reach out to customer service for more information.

> **Response**
    
    
    {
        "success": true,
        "data": {
            "expected_trigger_time": 1711534302938
        },
        "timestamp": 1711534302943
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
trigger_after | integer | Y | Timeout in ms. Max timeout can be set to 900000. To cancel this timer, set timeout to 0.  
  
## Cancel Order

**Limit: 10 requests per 1 second** shared with [cancel_order_by_client_order_id](#cancel-order-by-client_order_id)

` DELETE /v1/order `

Cancel order by order id. The order cancelled information will be updated from websocket stream. note that we give an immediate response with an order cancel sent message, and will update the cancel event via the websocket channel.

> **Response**
    
    
    {
      "success": true,
      "status": "CANCEL_SENT"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
order_id | number | Y | The `order_id` that you wish tocancel  
symbol | string | Y |   
  
## Cancel Order by client_order_id

**Limit: 10 requests per 1 second** shared with [cancel_order](#cancel-order)

` DELETE /v1/client/order `

Cancel order by client order id. The order cancelled information will be updated from websocket stream. note that we give an immediate response with an order cancel sent message, and will update the cancel event via the websocket channel.

Only the latest order with the `symbol` and `client_order_id` would be canceled.

> **Response**
    
    
    {
      "success": true,
      "status": "CANCEL_SENT"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
client_order_id | number | Y | The `client_order_id` that you wish tocancel  
symbol | string | Y |   
  
## Cancel Orders

**Limit: 10 requests per 1 second**

` DELETE /v1/orders `

Cancel orders by symbol.

> **Response**
    
    
    {
      "success": true,
      "status": "CANCEL_ALL_SENT"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
  
## Cancel All Pending Orders

**Limit: 10 requests per 1 second**

` DELETE /v3/orders/pending `

Cancel all pending ordinary orders.

> **Response**
    
    
    // success response
    {
        "success": true,
        "status": "CANCEL_ALL_SENT"
    }
    
    // Failed response
    {
        "success": false,
        "code": -1002,
        "message": "The request is unauthorized."
    }
    

## Get Order

**Limit: 10 requests per 1 second** shared with [get_order_by_client_order_id](#get-order-by-client-order-id)

` GET /v1/order/:oid `

Get specific order details by `order_id`. The `realized_pnl` field in response will only present the settled amount for futures orders.

> **Response**
    
    
    {
        "success": true,
        "created_time": "1577349119.33", // Unix epoch time in seconds
        "side": "SELL",
        "status": "FILLED",
        "symbol": "PERP_BTC_USDT",
        "client_order_id": 0,
        "reduce_only": false,
        "order_id": 1,
        "order_tag": "default",
        "type": "LIMIT",
        "price": 123,
        "quantity": 0.1,
        "amount": null,
        "visible": 0.1,
        "executed": 0.1,
        "total_fee": 0.00123,  // represents the cumulative fees for the entire order
        "fee_asset": "USDT",
        "average_executed_price": 123,
        "realized_pnl":null,
        'total_rebate': 0,   // indicates the aggregate rebates for the entire order
        'rebate_asset': null, 
        "position_side":'SHORT',
        'margin_mode':'CROSS', 
        'leverage':20, 
    
        // Detail transactions of this order
        "Transactions": [
            {
                "id": 2,
                "symbol": "PERP_BTC_USDT",
                "fee": 0.0001,   // fee for a single transaction
                "fee_asset": "usdt", // fee. use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
                "side": "BUY",
                "order_id": 1,
                "executed_price": 123,
                "executed_quantity": 0.05,
                "executed_timestamp": "1567382401.000", // Unix epoch time in seconds
                "is_maker": 1
            }]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
oid | number | Y | The order_id `oid` that you wish to query  
  
## Get Order by client_order_id

**Limit: 10 requests per 1 seconds** shared with [get_order](#get-order)

` GET /v1/client/order/:client_order_id `

Get specific order details by `client_order_id`. If there is more than one order with the same `client_order_id`, return the latest one. The `realized_pnl` field in response will only present the settled amount for futures orders.

> **Response**
    
    
    {
        "success": true,
        "created_time": "1577349119.33", // Unix epoch time in seconds
        "side": "SELL",
        "status": "FILLED",
        "symbol": "SPOT_BTC_USDT",
        "client_order_id": 123,
        "reduce_only": false,
        "order_id": 1,
        "order_tag": "default",
        "type": "LIMIT",
        "price": 123,
        "quantity": 0.1,
        "amount": null,
        "visible": 0.1,
        "executed": 0.1,
        "total_fee": 0.00123,   // represents the cumulative fees for the entire order
        "fee_asset": "USDT",
        "average_executed_price": 123,
        "realized_pnl":null,
        'total_rebate': 0,    // indicates the aggregate rebates for the entire order
        'rebate_asset': null,
        'margin_mode':'CROSS', 
        'leverage':20, 
    
        // Detail transactions of this order
        "Transactions": [
            {
                "id": 2,
                "symbol": "SPOT_BTC_USDT",
                "fee": 0.0001,    // fee for a single transaction
                "fee_asset": "BTC", // fee. use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
                "side": "BUY",
                "order_id": 1,
                "executed_price": 123,
                "executed_quantity": 0.05,
                "executed_timestamp": "1567382401.000", // Unix epoch time in seconds
                "is_maker": 1
            }]
    
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
client_order_id | number | Y | customized order_id when placing order  
  
## Get Orders

**Limit: 10 requests per 1 second**

` GET /v1/orders `

Get orders by customize conditions.  
\- `INCOMPLETE` = `NEW` \+ `PARTIAL_FILLED`  
\- `COMPLETED` = `CANCELLED` \+ `FILLED` \+ `REJECTED` The `realized_pnl` field in response will only present the settled amount for futures orders. The return value default is null unless the input parameter `realized_pnl` set to `true`

> **Response**
    
    
    {
        "success": true,
        "meta": {
            "total": 31,
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
            {
                "side": "SELL",
                "status": "CANCELLED",
                "symbol": "SPOT_BCHABC_USDT",
                "client_order_id": 123,
                "reduce_only": false,
                "order_id": 8197,
                "order_tag": "default",
                "type": "LIMIT",
                "price": 308.51,
                "quantity": 0.0019,
                "amount": null,
                "visible": 0.0019,
                "executed": 0,
                "total_fee": 0,
                "fee_asset": null,
                'total_rebate': 0,
                'rebate_asset': null,
                "created_time": "1575014255.089", // Unix epoch time in seconds
                "updated_time": "1575014255.910", // Unix epoch time in seconds
                "average_executed_price": null,
                "position_side": "LONG",  
                "realized_pnl":null,
                'margin_mode':'CROSS', 
                'leverage':20, 
            },
            // ....skip (total 25 items in one page)
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | N |   
side | string | N | `BUY`/`SELL`  
size | number | N | The page size, default 100, max 500.  
order_type | string | N | `LIMIT`/`MARKET`/`IOC`/`FOK`/`POST_ONLY`/`LIQUIDATE`/`RPI`/`LIQUIDATE_BLP`/`ADL`  
order_tag | string | N | An optional tag for this order.  
realized_pnl | boolean | N | Decide if return data calculate realized pnl value for the futures order.  
status | enum | N | `NEW`/`CANCELLED`/`PARTIAL_FILLED`/`FILLED`/`REJECTED`/`INCOMPLETE`/`COMPLETED`  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
  
## Edit Order

**Limit: 5 requests per 1 second**

` PUT /v3/order/:order_id `

_**Note that for v3 API with json body POST method, please follow the instruction in[authentication](#authentication) section for `v3` API to generate the signature. *_*Please use `string` type for value input field to remain data accurancy.

The API allow you to edit the price and the quantity of the selected order. You must input at least one of it in the request body.

> **Response**
    
    
    // Success response
    {
        "success": true,
        "data": {
            "success": true,
            "status": "EDIT_SENT"
        },
        "timestamp": 1673842319229
    }
    
    // Failed response
    {
        "success": false,
        "code": -1103,
        "message": "The order does not meet the price filter requirement."
    }
    

> **Request**
    
    
    {
        "price": "10.5",
        "quantity": "1.4"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
order_id | number | Y | The `order_id` that you wish to query  
price | string | N | New price of the order.  
quantity | string | N | New quantity of the order.  
  
## Edit Order by client_order_id

**Limit: 5 requests per 1 second**

` PUT /v3/order/client/:client_order_id `

_**Note that for v3 API with json body POST method, please follow the instruction in[authentication](#authentication) section for `v3` API to generate the signature. *_*Please use `string` type for value input field to remain data accurancy.

The API allow you to edit the price and the quantity of the selected order. You must input at least one of it in the request body.

> **Response**
    
    
    // Success response
    {
        "success": true,
        "data": {
            "success": true,
            "status": "EDIT_SENT"
        },
        "timestamp": 1673842319229
    }
    
    // Failed response
    {
        "success": false,
        "code": -1103,
        "message": "The order does not meet the price filter requirement."
    }
    

> **Request**
    
    
    {
        "price": "10.5",
        "quantity": "1.4"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
client_order_id | number | Y | customized order_id when placing order  
price | string | N | New price of the order.  
quantity | string | N | New quantity of the order.  
  
## Send Algo Order

**Limit: 2 requests per 1 second**

` POST /v3/algo/order `

_**Note that for v3 API, please follow the instruction in[authentication](#authentication) section for `v3` API to generate the signature. *_*Please use `string` type for value input field to remain data accurancy.

Place algo order maker/taker, the order executed information will be updated from websocket stream. will respond immediately with an order created message.

To place `Stop Market` order, please use 'STOP' as `algoType` and 'MARKET' as `type`. Please input the trigger price in `triggerPrice` field.

To place `Stop Limit` order, please use 'STOP' as `algoType` and 'LIMIT' as `type`. Please input the trigger price in `triggerPrice` field.

To place `Trailing Stop` order, please use 'TRAILING_STOP' as `algoType` and 'MARKET' as `type`. Please also input your trailing rate setting in `callbackRate` field.

To place `OCO` order, the input fields is 2 layer and includes an array of the objects named `childOrder`. The second order of OCO order should be a STOP_LIMIT or STOP MARKET order object in the array. please use 'OCO' as `algoType` in outter parameters, 'STOP' as `algoType` in `childOrder` object, and 'LIMIT' or 'MARKET' as type.

To place `Positional TP/SL` order, the input fields is 2 layer and includes an array of the objects named `childOrder`. The take-profit or stop-loss order should be the objects in the array. For the sub-order in `childOrder`, please input 'CLOSE_POSITION' as `type`, and 'TAKE_PROFIT' or 'STOP_LOSS' in `algoType` field.

`visible_quantity` behavior: it sets the maximum quantity to be shown on orderbook. By default, it is equal to order_quantity, negative number and number larger than `order_quantity` is not allowed. The visibility of the childOrder will inherit the parent order's visibility setting. If it sets to 0, the order would be hidden from the orderbook. It doesn't work for `MARKET` orders since orders with these types would be executed and cancelled immediately and not be shown on orderbook. For `LIMIT` order, as long as it's not complete, `visible_quantity` is the maximum quantity that is shown on the orderbook.

`client_order_id` behavior: customized order_id, a unique id among open orders. Orders with the same `client_order_id` can be accepted only when the previous one if completed, otherwise the order will be rejected.

For `Long`/ `Short` order, It is supported when position mode is HEDGE_MODE and the trading involves futures.

`reduce_only` behavior: only applicable to perpetual symbols. When reduce only is set to true, the system ensures that the order will reduce the position size rather than increasing it. To facilitate this, the system must group related orders to accurately manage the reduce only calculations. There is a cap of 50 orders that can be grouped together and if the limit is exceeded, the system will reject the incoming order. For algo orders, the check happens when the order gets triggered.

> **Response**
    
    
    {
      "code": 0,
      "data": {
        "rows": [
          {
            "algoType": "string",
            "clientOrderId": 0,
            "orderId": 0,
            "quantity": 0
          }
        ]
      },
      "message": "string",
      "success": true,
      "timestamp": 0
    }
    
    // bracket order response
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "orderId": 432132,
                    "clientOrderId": 0,
                    "algoType": "TAKE_PROFIT",
                    "quantity": 0
                },
                {
                    "orderId": 432133,
                    "clientOrderId": 0,
                    "algoType": "STOP_LOSS",
                    "quantity": 0
                },
                {
                    "orderId": 432131,
                    "clientOrderId": 0,
                    "algoType": "POSITIONAL_TP_SL",
                    "quantity": 0
                },
                {
                    "orderId": 432130,
                    "clientOrderId": 0,
                    "algoType": "BRACKET",
                    "quantity": 10
                }
            ]
        },
        "timestamp": 1676283560233
    }
    
    

> **Request**
    
    
    // stop market order
    
    {
        "symbol":"PERP_BTC_USDT",
        "side":"BUY",
        "orderCombinationType":"STOP_MARKET",
        "algoType":"STOP",
        "triggerPrice":"1000",
        "type":"MARKET",
        "quantity":"0.01"
    }
    
    //stop market limit
    
    {
        "symbol":"PERP_BTC_USDT",
        "side":"BUY",
        "orderCombinationType":"STOP_LIMIT",
        "algoType":"STOP",
        "triggerPrice":"1000",
        "type":"LIMIT",
        "quantity":"0.01",
        "price":1000
    }
    
    //OCO 
    
    {
        "symbol": "PERP_ETH_USDT",
        "side": "BUY",
        "reduceOnly": false,
        "type": "LIMIT",
        "quantity": "1",
        "algoType": "OCO",
        "price": "1000",
        "childOrders": [
            {
                "side": "BUY",
                "algoType": "STOP",
                "triggerPrice": "1600",
                "type": "MARKET"
            }
        ]
    }
    
    //Positional TP/SL
    
    {
        "symbol": "SPOT_BAL_USDT",
        "reduceOnly": false,
        "algoType": "POSITIONAL_TP_SL",
        "childOrders": [
            {
                "algoType": "TAKE_PROFIT",
                "type": "CLOSE_POSITION",
                "side": "BUY",
                "reduceOnly": true,
                "triggerPrice": "72"
            },
            {
                "algoType": "STOP_LOSS",
                "type": "CLOSE_POSITION",
                "side": "BUY",
                "reduceOnly": true,
                "triggerPrice": "74"
            }
        ]
    }
    
    // Bracket order
    
    {
        "symbol": "SPOT_BAL_USDT",
        "side": "BUY",
        "reduceOnly": false,
        "type": "LIMIT",
        "quantity": "1",
        "algoType": "BRACKET",
        "price": "69",
        "childOrders": [
            {
                "symbol": "SPOT_BAL_USDT",
                "reduceOnly": false,
                "algoType": "POSITIONAL_TP_SL",
                "childOrders": [
                    {
                        "algoType": "TAKE_PROFIT",
                        "type": "CLOSE_POSITION",
                        "side": "SELL",
                        "reduceOnly": true,
                        "triggerPrice": "76"
                    },
                    {
                        "algoType": "STOP_LOSS",
                        "type": "CLOSE_POSITION",
                        "side": "SELL",
                        "reduceOnly": true,
                        "triggerPrice": "50"
                    }
                ]
            }
        ]
    }
    

**Parameters - Parent**

Name | Type | Required | Description  
---|---|---|---  
activatedPrice | string | N | activated price for algoType=TRAILING_STOP  
algoType | string | Y | `STOP/OCO/TRAILING_STOP/BRACKET`  
marginMode | enum | N | `CROSS`/`ISOLATED`, defualt will be `CROSS`. The `ISOLATED` option only applicable to perp symbols, will be rejected if passed in for spot symbols   
callbackRate | string | N | callback rate, only for algoType=TRAILING_STOP, i.e. the value = 0.1 represent to 10%.  
callbackValue | string | N | callback value, only for algoType=TRAILING_STOP, i.e. the value = 100  
childOrders | child | N | Child orders for algoType=`POSITIONAL_TP_SL`  
symbol | string | Y |   
clientOrderId | number | N | Client order id defined by client,number for scope : from 0 to 9223372036854775807. (default: 0), duplicated client order id on opening order is not allowed.  
orderTag | string | N | An optional tag for this order. (default: `default`)  
price | string | N | order price  
quantity | string | N | Order quantity, only optional for algoType=`POSITIONAL_TP_SL`  
reduceOnly | boolean | N | true or false, default false.If the user's RO order message contains 50 pending orders,the order can be created successfully placed.  
triggerPrice | string | N | trigger price, if algoType=TRAILING_STOP, you need to provide 'activatedPrice'  
triggerPriceType | string | N | trigger price, default `MARKET_PRICE`, enum: `MARKET_PRICE`  
type | string | Y | `LIMIT`/`MARKET`  
visibleQuantity | number | N | The order quantity shown on orderbook. (default: equal to `orderQuantity`)  
side | enum | Y | `SELL`/`BUY`  
positionSide | enum | N | `SHORT`/`LONG`, If position mode is HEDGE_MODE and the trading involves futures,then is required, otherwise this parameter is not required.  
  
**Parameters - Child**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
algoType | string | Y | `STOP`/`OCO`/`TRAILING_STOP`/`BRACKET`/`POSITIONAL_TP_SL` ï½  
side | enum | Y | `SELL`/`BUY`  
type | string | Y | `LIMIT`/`MARKET`  
triggerPrice | string | N | trigger price, if algoType=TRAILING_STOP, you need to provide 'activatedPrice'  
price | string | N | order price  
reduceOnly | boolean | N | true or false, default false,If the user's RO order message contains 50 pending orders,the order can be created successfully placed.  
childOrders | child | N | Child orders for algoType=`POSITIONAL_TP_SL`  
  
## Cancel Algo Order

**Limit: 10 requests per 1 second** shared with [cancel_algo_order_by_client_order_id](#cancel-algo-order-by-client_order_id)

` DELETE /v3/algo/order/:order_id `

***Note: This v3 API using query string to pass parameter, please follow the instruction in [authentication](#authentication) section for `v3` API to generate the signature. Cancel order by order id. The order cancelled information will be updated from websocket stream. note that we give an immediate response with an order cancel sent message, and will update the cancel event via the websocket channel.

> **Response**
    
    
    // Success response
    {
        "success": true,
        "status": "CANCEL_SENT"
    }
    
    // Failed response
        "success": false,
        "code": -1006,
        "message": "Your order and symbol are not valid or already canceled."
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
order_id | number | Y | The `order_id` that youwish to cancel  
  
## Cancel All Pending Algo Orders

**Limit: 10 requests per 1 second**

` DELETE /v3/algo/orders/pending `

***Note: This v3 API using query string to pass parameter, please follow the instruction in [authentication](#authentication) section for `v3` API to generate the signature. Cancel all pending algo orders.

> **Response**
    
    
    // Success response
    {
        "success": true,
        "status": "CANCEL_SENT"
    }
    
    // Failed response
        "success": false,
        "code": -1006,
        "message": "Your order and symbol are not valid or already canceled."
    }
    

## Cancel Pending Merge Orders by Symbol

**Limit: 10 requests per 1 second**

` DELETE /v3/merge/orders/pending/:symbol `

***Note that for v3 API, please follow the instruction in [authentication](#authentication) section for `v3` API to generate the signature. Cancel both ordinary and algo orders by symbol.

> **Response**
    
    
    {
      "success": true,
      "status": "CANCEL_ALL_SENT"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
side | string | N (default: cancel both sides) | BUY or SELL  
symbol | string | Y |   
marginMode | string | N (default:CROSS) | CROSS or ISOLATED  
  
## Get Algo Order

**Limit: 10 requests per 1 second** shared with [get_algo_order_by_client_order_id](#get-algo-order-by-client-order-id)

` GET /v3/algo/order/:oid ` ***Note: This v3 API using query string to pass parameter, please follow the instruction in [authentication](#authentication) section for `v3` API to generate the signature.

Get specific order details by Algo order's `oid`.

> **Response**
    
    
    // Success response
    {
        "success": true,
        "data": {
            "algoOrderId": 431601,
            "clientOrderId": 0,
            "rootAlgoOrderId": 431601,
            "parentAlgoOrderId": 0,
            "symbol": "SPOT_ADA_USDT",
            "orderTag": "default",
            "algoType": "BRACKET",
            "side": "BUY",
            "quantity": 11,
            "isTriggered": false,
            "triggerStatus": "SUCCESS",
            "type": "LIMIT",
            "status": "FILLED",
            "rootAlgoStatus": "FILLED",
            "algoStatus": "FILLED",
            "triggerPriceType": "MARKET_PRICE",
            "price": 0.33,
            "triggerTime": "0",
            "totalExecutedQuantity": 11,
            "averageExecutedPrice": 0.33,
            "totalFee": 0.0033,
            "feeAsset": "ADA",
            "totalRebate":0,
            "rebateAsset":"",
            "reduceOnly": false,
            "createdTime": "1676277825.917",
            "updatedTime": "1676280901.229",
            "positionSide":"LONG",
            'marginMode':'CROSS', 
            'leverage':20, 
    
        },
        "timestamp": 1676281474630
    }
    
    // Failed response
    {
        "success": false,
        "code": -1006,
        "message": "The order can not be found."
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
oid | number | Y | The Algo order's order_id `oid` that you wish to query  
  
## Get Algo Orders

**Limit: 10 requests per 1 second**

` GET /v3/algo/orders `

***Note: This v3 API using query string to pass parameter, please follow the instruction in [authentication](#authentication) section for `v3` API to generate the signature. Get orders by customize conditions.  
\- `INCOMPLETE` = `NEW` \+ `PARTIAL_FILLED`  
\- `COMPLETED` = `CANCELLED` \+ `FILLED` \+ `REJECTED` The `realizedPnl` field in response will only present the settled amount for futures orders. The return value default is null unless the input parameter `realizedPnl` set to `true`

> **Response**
    
    
    {
      "success": true,
      "data": {
        "rows": [
          {
            "leverage": 10,
            "algoOrderId": 2081697,
            "clientOrderId": 0,
            "rootAlgoOrderId": 2081697,
            "parentAlgoOrderId": 0,
            "symbol": "PERP_WOO_USDT",
            "orderTag": "default",
            "algoType": "POSITIONAL_TP_SL",
            "side": "BUY",
            "quantity": 0,
            "isTriggered": false,
            "triggerStatus": "NEW",
            "rootAlgoStatus": "NEW",
            "algoStatus": "NEW",
            "triggerPriceType": "USELESS",
            "triggerTime": "0",
            "totalExecutedQuantity": 0,
            "visibleQuantity": 0,
            "averageExecutedPrice": 0,
            "totalFee": 0,
            "feeAsset": "",
            "totalRebate": 0,
            "rebateAsset": "",
            "reduceOnly": false,
            "createdTime": "1720589170.566",
            "updatedTime": "1720589616.276",
            "isActivated": true,
            "childOrders": [
              {
                "leverage": 10,
                "algoOrderId": 2081698,
                "clientOrderId": 0,
                "rootAlgoOrderId": 2081697,
                "parentAlgoOrderId": 2081697,
                "symbol": "PERP_WOO_USDT",
                "orderTag": "default",
                "algoType": "TAKE_PROFIT",
                "side": "BUY",
                "quantity": 0,
                "isTriggered": false,
                "triggerPrice": 0.14977,
                "triggerStatus": "USELESS",
                "type": "CLOSE_POSITION",
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "triggerPriceType": "MARK_PRICE",
                "triggerTime": "0",
                "totalExecutedQuantity": 0,
                "visibleQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeAsset": "",
                "totalRebate": 0,
                "rebateAsset": "",
                "reduceOnly": true,
                "createdTime": "1720589170.561",
                "updatedTime": "1720589616.268",
                "isActivated": true,
                "positionSide": "SHORT",
                "marginMode": "ISOLATED"
              },
              {
                "leverage": 10,
                "algoOrderId": 2081699,
                "clientOrderId": 0,
                "rootAlgoOrderId": 2081697,
                "parentAlgoOrderId": 2081697,
                "symbol": "PERP_WOO_USDT",
                "orderTag": "default",
                "algoType": "STOP_LOSS",
                "side": "BUY",
                "quantity": 0,
                "isTriggered": false,
                "triggerPrice": 0.22465,
                "triggerStatus": "USELESS",
                "type": "CLOSE_POSITION",
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "triggerPriceType": "MARK_PRICE",
                "triggerTime": "0",
                "totalExecutedQuantity": 0,
                "visibleQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeAsset": "",
                "totalRebate": 0,
                "rebateAsset": "",
                "reduceOnly": true,
                "createdTime": "1720589170.564",
                "updatedTime": "1720589616.270",
                "isActivated": true,
                "positionSide": "SHORT",
                "marginMode": "ISOLATED"
              }
            ],
            "positionSide": "SHORT",
            "marginMode": "ISOLATED"
          }
        ],
        "meta": {
          "total": 3,
          "records_per_page": 25,
          "current_page": 1
        }
      },
      "timestamp": 1720589635338
    }
    
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
algoType | string | Y | `STOP/OCO/TRAILING_STOP/BRACKET`  
createdTimeEnd | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
createdTimeStart | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
isTriggered | boolean | N | true or false  
orderTag | string | N | An optional tag for this order.  
page | number | N (default: 1) | pag of query pagination  
realizedPnl | boolean | N | Decide if return data calculate realized pnl value for the futures order.  
side | string | N | `BUY`/`SELL`  
size | number | N (default: 25) | size for query pagination  
status | enum | N | `NEW`/`CANCELLED`/`PARTIAL_FILLED`/`FILLED`/`REJECTED`/`INCOMPLETE`/`COMPLETED`  
symbol | string | N |   
orderType | string | N | `LIMIT`/`MARKET`  
  
## Edit Algo Order

**Limit: 5 requests per 1 second**

` PUT /v3/algo/order/:order_id `

_**Note that for v3 API with json body POST method, please follow the instruction in[authentication](#authentication) section for `v3` API to generate the signature. *_*Please use `string` type for value input field to remain data accurancy.

The API allow you to edit the trigger price and the quantity of the selected algo order. You must input at least one of it in the request body.

> **Response**
    
    
    {
        "success": true,
        "data": {
            "success": true,
            "status": "EDIT_SENT"
        },
        "timestamp": 1676277871935
    }
    

> **Request**
    
    
    {
      "activatedPrice": "200",
      "callbackRate": "200",
      "callbackValue": "200",
      "childOrders": [
        {
          "algoOrderId": 123456,
          "price": "1000",
          "quantity": "1000",
          "triggerPrice": "1000"
        }
      ],
      "price": "1000",
      "quantity": "1000",
      "triggerPrice": "1000"
    }
    
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
oid | number | Y | The order_id `oid` that you wish to query  
activatedPrice | string | N | activated price for algoType=TRAILING_STOP  
callbackRate | string | N | new callback rate, only for algoType=TRAILING_STOP, i.e. the value = 0.1 represent to 10%.  
callbackValue | string | N | new callback value, only for algoType=TRAILING_STOP, i.e. the value = 100  
childOrders | array | N | The array list of the child orders, only for algoType=POSITIONAL_TP_SL or TP_SL  
price | number | N | New price of the algo order.  
quantity | number | N | New quantity of the algo order.  
triggerPrice | number | N | New trigger price of the algo order.  
  
## Edit Algo Order by client_order_id

**Limit: 5 requests per 1 second**

` PUT /v3/algo/order/client/:client_order_id `

_**Note that for v3 API with json body POST method, please follow the instruction in[authentication](#authentication) section for `v3` API to generate the signature. *_*Please use `string` type for value input field to remain data accurancy.

The API allow you to edit the price and the quantity of the selected algo order. You must input at least one of it in the request body.

> **Response**
    
    
    {
      "code": 0,
      "data": {
        "status": "string",
        "success": true
      },
      "message": "string",
      "success": true,
      "timestamp": 0
    }
    

> **Request**
    
    
    {
      "activatedPrice": "200",
      "callbackRate": "200",
      "callbackValue": "200",
      "childOrders": [
        {
          "algoOrderId": 123456,
          "price": "1000",
          "quantity": "1000",
          "triggerPrice": "1000"
        }
      ],
      "price": "1000",
      "quantity": "1000",
      "triggerPrice": "1000"
    }
    
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
oid | number | Y | The order_id `oid` that you wish to query  
activatedPrice | string | N | activated price for algoType=TRAILING_STOP  
callbackRate | string | N | new callback rate, only for algoType=TRAILING_STOP, i.e. the value = 0.1 represent to 10%.  
callbackValue | string | N | new callback value, only for algoType=TRAILING_STOP, i.e. the value = 100  
childOrders | array | N | The array list of the child orders, only for algoType=POSITIONAL_TP_SL or TP_SL  
price | number | N | New price of the algo order.  
quantity | number | N | New quantity of the algo order.  
triggerPrice | number | N | New trigger price of the algo order.  
  
## Get Trade

**Limit: 10 requests per 1 second**

` GET /v1/client/trade/:tid `

Get specific transaction detail by `id`. (The data fetch from this API only contains past 3 months data, if you need the data more than 3 months, please submit the ticket in the support center).

> **Response**
    
    
    {
        "success": true,
        "id": 1,
        "symbol": "SPOT_BTC_USDT",
        "fee": 0.0001,
        "fee_asset": "BTC", // fee. use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
        "side": "BUY",
        "order_id": 2,
        "executed_price": 123,
        "executed_quantity": 0.05,
        "is_maker": 0,
        "executed_timestamp": "1567382400.000",  // Unix epoch time in seconds
        "is_match_rpi": true
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
tid | number | Y | The transaction id `tid` that you wish to query  
  
## Get Trades

**Limit: 10 requests per 1 second**

` GET /v1/order/:oid/trades `

Get trades by `order_id`

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "id": 5, // transaction id
                "symbol": "SPOT_BTC_USDT",
                "order_id": 211,
                "order_tag": "default",
                "executed_price": 10892.84,
                "executed_quantity": 0.002,
                "is_maker": 0,
                "side": "SELL",
                "fee": 0,
                "fee_asset": "USDT", // use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
                "executed_timestamp": "1566264290.250",  // Unix epoch time in seconds
                "is_match_rpi": true
            }
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
oid | number | Y | The order id `oid` that you wish to query  
  
## Get Trade History

**Limit: 10 requests per 1 second**

` GET /v1/client/trades `

Return clientâs trade history in a range of time. (The data fetch from this API only contains past 3 months data, if you need the data more than 3 months, please user [Get Archived Trade History](#get-archived-trade-history)).

> **Response**
    
    
    {
        "success": true,
        "meta": {
            "total": 31,
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
            {
                "id": 5, // transaction id
                "symbol": "SPOT_BTC_USDT",
                "order_id": 211,
                "order_tag": "default",
                "executed_price": 10892.84,
                "executed_quantity": 0.002,
                "is_maker": 0,
                "side": "SELL",
                "fee": 0,
                "fee_asset": "USDT", // use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
                "executed_timestamp": "1566264290.250",  // Unix epoch time in seconds
                "is_match_rpi": true
            },
            // ....skip (total 25 items in one page)
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | N |   
order_tag | string | N | An optional tag for this order.  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
## Get Archived Trade History

**Limit: 1 requests per 1 second**

` GET /v1/client/hist_trades `

Return clientâs trade history in a range of time. (The data fetch from this API contains all time historical data).

> **Response**
    
    
    {
        "success": true,
        "data": [
            {
                "id": 217714629, // transaction id
                "symbol": "SPOT_BTC_USDT",
                "order_id": 211,
                "order_tag": "default",
                "executed_price": 10892.84,
                "executed_quantity": 0.002,
                "is_maker": 0,
                "side": "SELL",
                "fee": 0,
                "fee_asset": "USDT", // use Base (BTC) as unit when BUY, use Quote (USDT) as unit when SELL
                "executed_timestamp": "1566264290.250",  // Unix epoch time in seconds
                "is_match_rpi": true
            },
            // ....skip (total 25 items in one page)
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | N |   
start_t | timestamp | Y | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | Y | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
fromId | number | N (default: 1) | fromId is the trade id of the the record. It should be use as a cursor, so searching for trades starting with that trade id query.  
limit | number | N (default: 25) |   
  
## Get Current Holding

**Limit: 10 requests per 1 seconds**

` GET /v1/client/holding `

Holding summary of the client. Note that the number in holding could be negative, it means how much the client owes to WOO X.

> **Response**
    
    
    {
        "success": true,
        "holding": {
            "BTC": 1.014,
            "USDT": -26333.207589999998,
            "BCHABC": 2
        }
    }
    

**Parameters**

None

## Get Current Holding v2

**Limit: 10 requests per 1 seconds**

` GET /v2/client/holding `

** Note: This API will be deprecated at the end of 2023 Q1, please find the replacement API in  [Get Current Holding Get Balance - New](#get-current-holding-get-balance-new) Holding summary of client. Note that the number in holding could be negative, it means how much client owed to WOO X.

> **Response**
    
    
    {
        "holding":[
            {
                "token":"BTC",
                "holding":0.00590139,
                "frozen":0.0,
                "interest":0.0,
                "outstanding_holding":-0.00080,
                "pending_exposure":0.0,
                "opening_cost":-126.36839957,
                "holding_cost":-125.69703515,
                "realised_pnl":73572.86125165,
                "settled_pnl":73573.5326161,
                "fee_24_h":0.01432411,
                "settled_pnl_24_h":0.67528081,
                "updated_time":"1675220398"
            },{
                "token":"UNI",
                "holding":0.00000000,
                "frozen":0.00000000,
                "interest":0.00000000,
                "outstanding_holding":0.00000000,
                "pending_exposure":0.00000000,
                "opening_cost":0,
                "holding_cost":0,
                "realised_pnl":0,
                "settled_pnl":0,
                "fee_24_h":0,
                "settled_pnl_24_h":0,
                "updated_time":"1655269545"
            }   
        ],
        "success":true
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
all | enum | N | `true`/`false`. If `true` then will return all tokens even if balance is empty.  
  
## Get Current Holding (Get Balance) - New

**Limit: 100 requests per 1 mins**

` GET /v3/balances `

Holding summary of client. Note that the number in holding could be negative, it means how much client owed to WOO X. The API is design to replace the legacy API [Get Current Holding](#get-current-holding) and [Get Current Holding v2](#get-current-holding-v2)

> **Response**
    
    
    {
      "success": true,
      "data": {
        "holding": [
          {
            "token": "WOO",
            "holding": 169684.96645139,
            "frozen": 0.0,
            "staked": 1304330.65079109,
            "unbonding": 0.0,
            "vault": 0.0,
            "interest": 0.0,
            "pendingShortQty": 0.0,
            "pendingLongQty": 0.0,
            "availableBalance": 169684.96645139,
            "averageOpenPrice": 0.0,
            "markPrice": 0.22446,
            "launchpadVault": 0.0,
            "earn": 0.0,
            "pnl24H": 0.0,
            "fee24H": 0.0,
            "updatedTime": 1715126422.125
          }
        ],
        "userId": 11446,
        "applicationId": "1ca13dff-f2d6-4fa4-a382-5ce1a79b2bc0"
      },
      "timestamp": 1715197222107
    }
    

**Parameters**

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | N | Use the parameter in query string format (i.e. /v3/balance?token=WOO). If the parameter is empty (or not passed) it will return all token's holding.  
  
## Get Account Information

**Limit: 10 requests per 60 seconds**

` GET /v1/client/info `

** Note: This API will be deprecated at the end of 2023 Q1, please find the replacement API in  [Get Account Information - New](#get-account-information-new) Get account information such as account name, leverage, current exposure ... etc.

> **Response**
    
    
    {
    
        "success": true,
        "application": {
            "application_id": "8935820a-6600-4c2c-9bc3-f017d89aa173",
            "account": "CLIENT_ACCOUNT_01",
            "alias": "CLIENT_ACCOUNT_01",
            "account_mode":"FUTURES" //account mode
            "leverage": 5,
            "taker_fee_rate": 0,
            "maker_fee_rate": 0,
            "futures_leverage": 5,
            "futures_taker_fee_rate": 0,
            "futures_maker_fee_rate": 0,
            "otpauth": false
        },
        "margin_rate": 1000
    }
    

**Parameters**

None

## Get Account Information - New

**Limit: 10 requests per 60 seconds**

` GET /v3/accountinfo `

Get account information such as account name, leverage, current exposure ... etc. The API is design to replace the legacy API [Get Account Information](#get-account-information)

The `referrerID` in the response represent the referral code that the user used to sign up, subaccount would pass main account referrerID. The `accountType` in the response represent the account type is `Main` account or `Subaccount`

> **Response**
    
    
    {
        "success": true,
        "data": {
            "applicationId": "f5f485c7-6ca5-4189-8efe-e842cdc50498",
            "account": "",
            "alias": "",
            "accountMode": "FUTURES",
            "positionMode": "HEDGE",
            "leverage": null, 
            "takerFeeRate": 0,
            "makerFeeRate": 0,
            "interestRate": 1,
            "futuresTakerFeeRate": 0,
            "futuresMakerFeeRate": 0,
            "otpauth": true,
            "marginRatio": 7739.3757,
            "openMarginRatio": 7739.3757,
            "initialMarginRatio": 1.0006,
            "maintenanceMarginRatio": 0.0126,
            "totalCollateral": 1146085.27376211,
            "freeCollateral": 1145937.09993548,
            "totalAccountValue": 1924716.18982933, // include isolated frozen and unrealized pnl
            "totalVaultValue": 778216.06557667,
            "totalStakingValue": 0,
            "referrerID": "",
            "accountType": "Main",
            "totalLaunchpadVaultValue": 0,
            "totalEarnValue": 0
        },
        "timestamp": 1714284212689
    }
    

**Parameters**

None

## Get Token History

**Limit: 10 requests per 60 seconds**

` GET /v1/client/transaction_history `

Get account token balance change history, including `YIELD_TO_BALANCE`, `TRANSACTION_FEE`, `REALIZED_PNL`, `SPOT_TRANSACTION`, `FUTURES_TRADING`, `FUNDING_FEE`

> **Response**
    
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "id": 1606724,
                    "type": "YIELD_TO_BALANCE",
                    "token": "WOO",
                    "amount": 0.30029155,
                    "timestamp": 1686528091385
                },
                {
                    "id": 1686355200000,
                    "type": "REALIZED_PNL",
                    "token": "USDT",
                    "symbol": "PERP_WOO_USDT",
                    "amount": -24.64824179,
                    "timestamp": 1686355200000
                },
                {
                    "id": 7284139,
                    "type": "FUNDING_FEE",
                    "token": "USDT",
                    "amount": 0.02661496,
                    "timestamp": 1686009921667
                },
                ...
            ],
            "meta": {
                "total": 65,
                "records_per_page": 25,
                "current_page": 1
            }
        },
        "timestamp": 1686544732777
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
type | string | N | `WITHDRAW`/`DEPOSIT`/`FIAT_WITHDRAW`/`FIAT_DEPOSIT`/`EARN`/`VAULT_WITHDRAW`/`VAULT_DEPOSIT`/`YIELD_TO_BALANCE`/`CREDIT`/`DISTRIBUTION`/`REFERRAL`/`SUB_ACCOUNT_TRANSFER`/`REBATE`/`LIQUIDATION`/`SPECIAL`/`STAKING`/`UNSTAKING`/`UNSTAKING_FEE`/`INTEREST`/`CONVERT`/`FUNDING_FEE`/`SPOT_TRANSACTION`/`TRANSACTION_FEE`/`REALIZED_PNL`/`RFQ`  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
## Get Account API Key & Permission

**Limit: 10 requests per 60 seconds**

` GET usercenter/api/enabled_credential `

Get api_key list and its permissions of the account. The response will contain your API keysâ permissions based on the credentials.

> **Response**
    
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "account_name": "Main",
                    "user_id": 10001,
                    "api_key": "+Pxxxxxxxxxxxxxxxxxxxx==",
                    "permission": "Read,"
                },
                {
                    "account_name": "Main",
                    "user_id": 10001,
                    "api_key": "Hxxxxxxxxxxxxxxxxxxxx==",
                    "permission": "Read,"
                },
                {
                    "account_name": "Main",
                    "user_id": 10001,
                    "api_key": "Cxxxxxxxxxxxxxxxxxxxx==",
                    "permission": "Read,"
                },
                {
                    "account_name": "testSubAccount",
                    "user_id": 10001,
                    "api_key": "vxxxxxxxxxxxxxxxxxxxx==",
                    "permission": "Read,Enable trade,"
                }
                ...
            ],
            "meta": {
                "total": 11,
                "records_per_page": 5,
                "current_page": 1
            }
        },
        "timestamp": 1685414636917
    }
    

**Parameters**

None

## Get Buy Power

**Limit: 60 requests per 60 seconds**

` GET /v3/buypower `

Get buying power for selected symbol.

> **Response**
    
    
    {
      "success": true,
      "data": [
        {
            "symbol": "SPOT_BTC_USDT",
            "availableBaseQuantity": 1.2,
            "availableQuoteQuantity": 100,
        },
      ],
      "timestamp": 1575014255
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y | symbol that you wish to query  
  
## Get Token Deposit Address

**Limit 60 requests per 60 seconds**

` GET /v1/asset/deposit `

Get your unique deposit address by token

> **Response**
    
    
    {
        "success": true,
        "address": "0x31d64B3230f8baDD91dE1710A65DF536aF8f7cDa",
        "extra": ""
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | Y | token name you want to deposit (can get it by /public/token)  
  
## Token Withdraw

**Limit 20 requests per 60 seconds**

` POST /v1/asset/withdraw `

Initiate a token withdrawal request, `amount` must less than or equal to `holding`

> **Response**
    
    
    {
        "success": true,
        "withdraw_id": "20200119145703654"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | Y | token name you want to withdraw (can get it by /public/token)  
address | string | Y | the address you want to withdraw  
extra | string | N | address extra information such as MEMO or TAG  
amount | number | Y | amount you want to withdraw, must less or equal than holding  
  
## Token Withdraw V3

**Limit 20 requests per 60 seconds**

` POST /v3/asset/withdraw `

Initiate a token withdrawal request, `amount` must less than or equal to `holding`

> **Response**
    
    
    {
        "success": true,
        "data": {
            "withdrawId": "24040901514500001"
        },
        "timestamp": 1712627507204
    }
    
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
network | string | Y | To be obtained from the /public/token endpoint  
address | string | Y | the address you want to withdraw  
extra | string | N | address extra information such as MEMO or TAG  
amount | number | Y | amount you want to withdraw, must less or equal than holding  
balanceToken | string | Y | To be obtained from the /public/token endpoin  
  
## Internal token withdraw

**Limit: 20 requests per 60 seconds**

` POST v1/asset/internal_withdraw `

Initiate a token withdrawal request, amount must less than or equal to holding. When using this API, please note that it cannot be utilized if address verification is enabled.

> **Response**
    
    
    {
        "success": true,
        "withdraw_id": "20200119145703654"
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
target_user_id | string | Yes | withdraw target user id  
balance_token | string | Yes | balance token is token name you want to withdraw (can get it by /public/token)  
amount | number | Yes | amount you want to withdraw, must less or equal than holding  
  
## Cancel Withdraw Request

**Limit 5 requests per 60 seconds**

` DELETE /v1/asset/withdraw `

Cancel withdraw request when status is `NEW`

> **Response**
    
    
    {
        "success": true
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | the withdraw id you want to cancel  
  
## Get Asset History

**Limit 10 requests per 60 seconds**

` GET /v1/asset/history `

Get asset history, includes token deposit/withdraw and collateral deposit/withdraw.

> **Response**
    
    
    {
        "success": true,
        "meta": {
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
            {
                "created_time": "1579399877.041", // Unix epoch time in seconds
                "updated_time": "1579399877.041", // Unix epoch time in seconds
                "id": "202029292829292",
                "external_id": "202029292829292",
                "application_id": null,
                "token": "ETH",
                "target_address": "0x31d64B3230f8baDD91dE1710A65DF536aF8f7cDa",
                "source_address": "0x70fd25717f769c7f9a46b319f0f9103c0d887af0",
                "confirming_threshold":12,
                "confirmed_number":12,
                "extra": "",
                "type": "BALANCE",
                "token_side": "DEPOSIT",
                "amount": 1000,
                "tx_id": "0x8a74c517bc104c8ebad0c3c3f64b1f302ed5f8bca598ae4459c63419038106b6",
                "fee_token": null,
                "fee_amount": null,
                "status": "CONFIRMING"
            },
            {
                "created_time": "1579399877.041",
                "updated_time": "1579399877.041",
                "id": "20202020202020022",
                "external_id": "20202020202020022",
                "application_id": null,
                "token": "ETH",
                "target_address": "0x31d64B3230f8baDD91dE1710A65DF536aF8f7cDa",
                "source_address": "0x70fd25717f769c7f9a46b319f0f9103c0d887af0",
                "confirming_threshold":12,
                "confirmed_number":12,
                "extra": "",
                "type": "BALANCE",
                "token_side": "DEPOSIT",
                "amount": 100,
                "tx_id": "0x7f74c517bc104c8ebad0c3c3f64b1f302ed5f8bca598ae4459c63419038106c5",
                "fee_token": null,
                "fee_amount": null,
                "status": "COMPLETED"
            }
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | N | use when query specific transaction id (the result of withdrawal or internal transfer.)  
token | string | N | token name you want to search (can get it by /public/token)  
balance_token | string | N | balance_token name you want to search (can get it by /public/token)  
type | string | N | `BALANCE`/`COLLATERAL`  
token_side | string | N | `DEPOSIT`/`WITHDRAW`  
status | string | N | `NEW`/`CONFIRMING`/`PROCESSING`/`COMPLETED`/`CANCELED`  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
## Margin Interest Rates

**Limit 10 requests per 60 seconds**

` GET /v1/token_interest `

Get the margin interest rate of each token.

> **Response**
    
    
    {
        "success": true,
        "rows": [
            {
                "token": "MATIC",
                "current_hourly_base_rate": "0.0001%",
                "est_hourly_base_rate": "0.0001%",
                "current_annual_base_rate": "0.876%",
                "est_annual_base_rate": "0.876%",
                "est_time": "1632394800.000"          // Unix epoch time in seconds
            },
            {
                "token": "USDT",
                "current_hourly_base_rate": "0.0008%",
                "est_hourly_base_rate": "0.0008%",
                "current_annual_base_rate": "7.008%",
                "est_annual_base_rate": "7.008%",
                "est_time": "1632394800.000"          // Unix epoch time in seconds
            },
            {
                "token": "WOO",
                "current_hourly_base_rate": "0.001%",
                "est_hourly_base_rate": "0.001%",
                "current_annual_base_rate": "8.76%",
                "est_annual_base_rate": "8.76%",
                "est_time": "1632394800.000"          // Unix epoch time in seconds
            },
            // ...
        ]
    }
    

**Parameters**

None

## Margin Interest Rate of Token

**Limit 10 requests per 60 seconds**

` GET /v1/token_interest/:token `

Get the margin interest rate of the specific token.

> **Response**
    
    
    {
        "success": true,
        "info": {
            "token": "BTC",
            "current_hourly_base_rate": "0.0001%",
            "est_hourly_base_rate": "0.0001%",
            "current_annual_base_rate": "0.876%",
            "est_annual_base_rate": "0.876%",
            "est_time": "1632448800.000"         // Unix epoch time in seconds
        }
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | Y | should be upper case  
  
## Get Interest History

**Limit 10 requests per 60 seconds**

` GET /v1/interest/history `

Get margin interest history. `loan_amount` will only appear when the side is `LOAN`.

> **Response**
    
    
    {
        "success": true,
        "meta": {
            "total": 349,
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
    
           {
                "created_time": "1579399877.041", // Unix epoch time in seconds
                "updated_time": "1579399877.041", // Unix epoch time in seconds
                "token": "USDT",
                "application_id": null,
                "user_id": null,
                "status": "SUCCEED",
                "quantity": 0.20768326,
                "side": "LOAN",
                "interest": 0.01,
                "hourly_rate": "0.001%",
                "annual_rate": "8.76%",
                "loan_amount": 1000
            }
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | N | interest token which you want to query  
side | string | N | `LOAN`/`REPAY`/`AUTO_REPAY`  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
## Repay Interest

**Limit 10 requests per 60 seconds**

` POST /v1/interest/repay `

REPAY your margin interest.

> **Response**
    
    
    {
        "success": true,
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | Y | interest token which you want to repay  
amount | number | Y | repayment amount  
  
## Get referrals summary

**Limit: 10 requests per 60 seconds**

` GET /v3/referrals `

Get referral information from each user you has referred.

> **Response**
    
    
    // The status of the recommender includes four typesï¼Registered; Verified identity; Deposited; Traded
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "referralId": 12509,
                    "registerTime": "1643076873.484",
                    "referralCode": "OJEDSSMU",
                    "tradeStatus": "Traded",
                    "earnWoo": 144.78597143,
                    "earnUsdt": 0,
                    "email": "staking-005_mas@woo.network",
                    "extraBonus": 0,
                    "extraBonusToken": "WOO",
                    "previousVersionCommissionSum": 10.07981438,
                    "previousVersionCommissionSumToken": "WOO"
                },
                {
                    "referralId": 12192,
                    "registerTime": "1639365757.173",
                    "referralCode": "OJEDSSMU",
                    "tradeStatus": "Traded",
                    "earnWoo": 5729.91597424,
                    "earnUsdt": 80.39717397,
                    "email": "hazel@woo.network",
                    "extraBonus": 0,
                    "extraBonusToken": "WOO",
                    "previousVersionCommissionSum": 5726.55249830,
                    "previousVersionCommissionSumToken": "WOO"
                },
                {
                    "referralId": 10588,
                    "registerTime": "1678349096.000",
                    "referralCode": "OJEDSSMU",
                    "tradeStatus": "Traded",
                    "earnWoo": 2058880.44406483,
                    "earnUsdt": 54128.36568263,
                    "email": "ken@woo.network",
                    "extraBonus": 90,
                    "extraBonusToken": "WOO",
                    "previousVersionCommissionSum": 20160.36080029,
                    "previousVersionCommissionSumToken": "WOO"
                },
                {
                    "referralId": 10492,
                    "registerTime": "1623203745.173",
                    "referralCode": "DIHGLR3T",
                    "tradeStatus": "Traded",
                    "earnWoo": 0,
                    "earnUsdt": 0.76927350,
                    "email": "staking-010@woo.network",
                    "extraBonus": 90,
                    "extraBonusToken": "WOO",
                    "previousVersionCommissionSum": null,
                    "previousVersionCommissionSumToken": "WOO"
                }
            ],
            "meta": {
                "total": 4,
                "records_per_page": 25,
                "current_page": 1
            }
        },
        "timestamp": 1690192103430
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
from | number | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
to | number | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
  
## Get referral reward history

**Limit: 10 requests per 60 seconds**

` GET /v3/referral_rewards `

Get referral reward information 

> **Response**
    
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "trade_date": "2023/07/17",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.47000000,
                    "referral_commission": 53929.73957955,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/07/17",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 2038704.30927676,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/07/12",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.05004760,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/07/11",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.44951069,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/07/11",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.47000000,
                    "referral_commission": 0.04858848,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/07/11",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 3.09802285,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/07/07",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 134.61965671,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12509
                },
                {
                    "trade_date": "2023/07/06",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 15.27442949,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/07/03",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.00811566,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/07/03",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.26545309,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/30",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.00144840,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/30",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.08224395,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/29",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.06940520,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/29",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 4.34149772,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/28",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.01434340,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/28",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.87468814,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/27",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.01949850,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 10492
                },
                {
                    "trade_date": "2023/06/27",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.00900000,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/06/27",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 0.90196242,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/06/27",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.05706141,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/27",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 3.43115031,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 12192
                },
                {
                    "trade_date": "2023/06/26",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.74977500,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 10492
                },
                {
                    "trade_date": "2023/06/26",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.05399999,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/06/26",
                    "referral_receive_percentage": 0,
                    "referrer_receive_percentage": 0,
                    "referral_rate": 0.00100000,
                    "referral_commission": 2.78932410,
                    "status": "Credited",
                    "reward_token": "WOO",
                    "referral_tier": 0,
                    "referral_program": "AFFILIATE",
                    "referral_id": 10588
                },
                {
                    "trade_date": "2023/06/26",
                    "referral_receive_percentage": 0.50000000,
                    "referrer_receive_percentage": 0.50000000,
                    "referral_rate": 0.30000000,
                    "referral_commission": 0.06862500,
                    "status": "Credited",
                    "reward_token": "USDT",
                    "referral_tier": 5,
                    "referral_program": "TIER",
                    "referral_id": 12192
                }
            ],
            "meta": {
                "total": 79,
                "records_per_page": 25,
                "current_page": 1
            }
        },
        "timestamp": 1690273370109
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
from | number | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
to | number | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
|  |  |   
|  |  |   
  
## Get Subaccounts

**Limit: 10 requests per 60 seconds**

` GET /v1/sub_account/all `

Get subaccount list.

> **Response**
    
    
    {
        "rows": [
            {
                "application_id": "6b43de5c-0955-4887-9862-d84e4689f9fe",
                "account": "2",
                "created_time": "1606897264.994"
            },
            {
                "application_id": "5b0df321-3aaf-471f-a386-b922a941d17d",
                "account": "1",
                "created_time": "1606897264.994"
            },
            {
                "application_id": "de25e672-f3e8-4ddc-b264-75d243cb2b9c",
                "account": "test",
                "created_time": "1606897264.994"
            }
        ],
        "success": true
    }
    

**Permission**

Main account only.

**Parameters**

None

## Get Assets of Subaccounts

**Limit: 10 requests per 60 seconds**

` GET /v1/sub_account/assets `

Get assets summary of all subaccounts (including main account).

> **Response**
    
    
    {
        "rows": [
            {
                "application_id": "0b297f58-9d3e-4c91-95cd-863329631b79",
                "account": "Main",
                "usdt_balance": 0.0
            }
        ],
        "success": true
    }
    

**Permission**

Main account only.

**Parameters**

None

## Get Asset Details from a Subaccount

**Limit: 10 requests per 60 seconds**

` GET /v1/sub_account/asset_detail `

Get assets details from a subaccounts.

> **Response**
    
    
    {
        "balances": {
            "BTC": {
                "holding": 0.0,
                "frozen": 0.0,
                "interest": 0.0,
                "staked": 0.0,
                "unbonding": 0.0,
                "vault": 0.0
            },
            "WOO": {
                "holding": 4172706.29647137,
                "frozen": 0.0,
                "interest": 0.0,
                "staked": 51370692,
                "unbonding": 0.0,
                "vault": 0.0
            },
            "BNB": {
                "holding": 0.00070154,
                "frozen": 0.0,
                "interest": 0.0,
                "staked": 0.0,
                "unbonding": 0.0,
                "vault": 0.0
            },
            "ETH": {
                "holding": 0.0,
                "frozen": 0.0,
                "interest": 0.0,
                "staked": 0.0,
                "unbonding": 0.0,
                "vault": 0.0
            },
            "USDT": {
                "holding": 14066.5839369,
                "frozen": 0.0,
                "interest": 0.0,
                "staked": 0.0,
                "unbonding": 0.0,
                "vault": 0.0
            }
        },
        "account": "test",
        "success": true,
        "application_id": "e074dd6b-4c03-49be-937f-856472f7a6cb"
    }
    

**Permission**

Main or Subaccounts.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
application_id | string | Y | application id for an account, user can find it from WOO X console.  
  
## Get IP Restriction

**Limit: 10 requests per 10 seconds**

` GET /v1/sub_account/ip_restriction `

Get allowed IP list of a subaccount's API Key.

> **Response**
    
    
    {
        "rows": [
            {
                "ip_list": "60.248.33.61,1.2.3.4,100.100.1.1,100.100.1.2,100.100.1.3,100.100.1.4,210.64.18.77",
                "api_key": "plXHR+GwX0u8UG/GwMjLsQ==",
                "update_time": "1644553230.916",
                "restrict": true
            }
        ],
        "meta": {
            "total": 1,
            "records_per_page": 25,
            "current_page": 1
        },
        "success": true
    }
    

**Permission**

Main or Subaccounts.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
application_id | string | N | from WOO X console  
api_key | string | N | created from WOO X console  
  
## Get Transfer History

**Limit: 20 requests per 60 seconds**

` GET /v1/asset/main_sub_transfer_history `

Get transfer history between main account and subaccounts. 

> **Response**
    
    
    {
        "success":true,
        "data":{
            "rows":[
                {
                    "id":225,
                    "token":"USDT",
                    "amount":1000000,
                    "status":"COMPLETED",
                    "from_application_id":"046b5c5c-5b44-4d27-9593-ddc32c0a08ae",
                    "to_application_id":"082ae5ae-e26a-4fb1-be5b-03e5b4867663",
                    "from_user":"Main",
                    "to_user":"av",
                    "created_time":"1642660941.534",
                    "updated_time":"1642660941.950"
                },
                // ....skip (total 25 items in one page)
            ],
            "meta":{
                "total":7,
                "records_per_page":5,
                "current_page":1
            }
        }
    }
    

**Permission**

Main or Subaccounts.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 25) |   
  
## Transfer Assets

**Limit: 20 requests per 60 seconds** ` POST /v1/asset/main_sub_transfer `

Transfer asset between main account and subaccounts. 

> **Response**
    
    
    {
        "success": true,
        "id": 200
    }
    

**Permission**

Main or Subaccounts.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
token | string | Y | token name you want to transfer (can get it by /public/token)  
amount | number | Y | amount you want to transfer  
from_application_id | string | Y | application id you want to transfer from  
to_application_id | string | Y | application id you want to transfer to  
  
## Get LtV info

**Limit: 20 requests per 60 seconds** ` POST /v1/asset/ltv `

For credit user to know whether need to deposit more funds to the platform if I want to withdraw.

> **Response**
    
    
    {
        "user_id": 12136,
        "success": true,
        "ltv_threshold": 0.6,
        "wallet_total_collateral": 1890719757.24550000,
        "credit": 0.00000000,
        "staking_woo_collateral": 0,
        "ltv": 0.00000000,
        "share_credit_user_ltv_infos": [
            {
                "user_id": 12136,
                "wallet_total_collateral": 1890719757.24550000,
                "staking_woo_collateral": 0
            }
        ]
    }
    

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
withdraw_token | string | N | If input this field, the `withdraw_amount` field will be mandatory  
withdraw_amount | number | N | amount you want to withdraw of the `withdraw_token`  
  
## Update Account Mode

**Limit: 5 requests per 60 seconds per user**

` POST /v1/client/account_mode `

Choose account mode: pure spot or margin or futures

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
account_mode | string | Y | PURE_SPOT, MARGIN, FUTURES  
  
> **Response**
    
    
    {
        "success": true
    }
    

## Update Position Mode

**Limit: 2 requests per 1 second per user**

` POST /v1/client/position_mode `

Choose position mode: ONE_WAY or HEDGE_MODE

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
position_mode | string | Y | set ONE_WAY / HEDGE_MODE to position mode  
  
> **Response**
    
    
    {
        "success": true
    }
    

## Update Leverage Setting

**Limit: 5 requests per 60 seconds per user**

` POST /v1/client/leverage `

Choose maximum leverage for margin mode  
**Parameters**

Name | Type | Required | Description  
---|---|---|---  
leverage | int | Y | for margin mode: 3, 4, 5ï¼10 ;  
  
> **Response**
    
    
    {
        "success": true
    }
    

## Update Futures Leverage Setting

**Limit: 60 requests per 60 seconds per user**

` POST /v1/client/futures_leverage `

Choose maximum leverage for futures mode

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y | Perpetual symbol name.  
margin_mode | string | Y | Options are `CROSS`/`ISOLATED`  
position_side | string | Y | Options are `LONG`/`SHORT` in hedge mode; `BOTH` in one way mode.  
leverage | int | Y | Leverage to set  
  
> **Response**
    
    
    {
        "success": true
    }
    

## GET Futures Leverage Setting

**Limit: 10 requests per 60 seconds per user**

` GET /v1/client/futures_leverage `

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y | Perpetual symbol name.  
margin_mode | string | Y | Options are `CROSS`/`ISOLATED`  
position_mode | string | Y | Options are `ONE_WAY`/`HEDGE`, for `HEDGE` mode it will present for both side  
  
> **Response**
    
    
    // cross margin, one way mode
    {
        "success": true,
        "data": {
            "symbol": "PERP_BTC_USDT",
            "margin_mode": "CROSS",
            "position_mode": "ONE_WAY",    
            "details": [
                {
                    "position_side": "BOTH",
                    "leverage": "10"
                }
            ]
        },
        "timestamp": 1696663264324
    }
    
    // cross margin, hedge mode
    {
        "success": true,
        "data": {
            "symbol": "PERP_BTC_USDT",
            "margin_mode": "CROSS",
            "position_mode": "HEDGE_MODE",    
            "details": [
                {
                    "position_side": "LONG",
                    "leverage": "10"
                },
                {
                    "position_side": "SHORT",
                    "leverage": "10"
                },
            ]
        },
        "timestamp": 1696663264324
    }
    
    // isolated margin, one way mode
    {
        "success": true,
        "data": {
            "symbol": "PERP_BTC_USDT",
            "margin_mode": "ISOLATED",
            "position_mode": "ONE_WAY",    
            "details": [
                {
                    "position_side": "BOTH",
                    "leverage": "10"
                }
            ]
        },
        "timestamp": 1696663264324
    }
    
    // isolated margin, hedge mode
    {
        "success": true,
        "data": {
            "symbol": "PERP_BTC_USDT",
            "margin_mode": "ISOLATED",
            "position_mode": "HEDGE_MODE",    
            "details": [
                {
                    "position_side": "LONG",
                    "leverage": "10"
                },
                {
                    "position_side": "SHORT",
                    "leverage": "20"
                },
            ]
        },
        "timestamp": 1696663264324
    }
    

## Update Isolated Margin Setting

**Limit: 20 requests per 60 seconds per user**

` POST /v1/client/isolated_margin `

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y | Perpetual symbol name.  
position_side | string | Y | Options are LONG/SHORT in hedge mode; BOTH in one way mode.  
adjust_token | string | Y | Only USDT is supported.  
adjust_amount | Number | Y | Token amount to be added or reduced.  
action | Number | Y | `ADD`/`REDUCE`  
  
> **Response**
    
    
    {
        "success": true
    }
    

## Get Funding Fee History

**Limit: 20 requests per 60 seconds per user**

` GET /v1/funding_fee/history `

Get funding fee history

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | N | symbol that you wish to query  
start_t | timestamp | N | start time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
end_t | timestamp | N | end time range that you wish to query, noted that the time stamp is a 13-digits timestamp.  
page | number | N (default: 1) | the page you wish to query.  
size | number | N (default: 10) | max 5000  
  
> **Response**
    
    
    {
        "success": true,
        "meta": {
                "total": 670,
            "records_per_page": 25,
            "current_page": 1
        },
        "rows": [
            {
                "id": 10001,
                "symbol": "PERP_BTC_USDT",
                "funding_rate": 0.00345,
                "mark_price": 100,
                "funding_fee": 0.345,
                "payment_type": "Receive", // Receive and Pay
                "status": "COMPLETED",
                "created_time": "1575014255.089", // Unix epoch time in seconds
                "updated_time": "1575014255.910", // Unix epoch time in seconds
                "funding_rate_interval_hours": 1
            },
            // ....skip (total 25 items in one page)
    
    }
    

## Get All Position info

**Limit: 30 requests per 10 seconds per user**

` GET /v1/positions `

** Note: This API will be deprecated at the end of 2023 Q1, please find the replacement API in  [Get Positions - New](#get-positions-new)

**Parameters**

> **Response**
    
    
    {
        "total_account_value": 1924712.88293063,
        "current_margin_ratio": 7719.4699,
        "success": true,
        "total_collateral": 1146084.70891586,
        "total_vault_value": 0.0,
        "total_staking_value": 0.0,
        "positions": [
            {
                "symbol": "PERP_WOO_USDT",
                "holding": 8.0,
                "pending_long_qty": 0.0,
                "pending_short_qty": 0.0,
                "settle_price": 0.31197093,
                "average_open_price": 0.43228,
                "timestamp": "1714247701.266",
                "opening_time": "1712542194.878",
                "mark_price": 0.31851,
                "est_liq_price": 0.0,
                "position_side": "LONG",
                "pnl_24_h": 0.0,
                "fee_24_h": 0.0,
                "margin_mode": "ISOLATED", 
                "leverage": 10, 
                "isolated_margin_token": "USDT",
                "isolated_margin_amount": 99.1,
                "isolated_frozen_long": 81.2,
                "isolated_frozen_short": 88.2
            },
            {
                "symbol": "PERP_WOO_USDT",
                "holding": 8.0,
                "pending_long_qty": 0.0,
                "pending_short_qty": 0.0,
                "settle_price": 0.31197093,
                "average_open_price": 0.43228,
                "timestamp": "1714247701.266",
                "opening_time": "1712542194.878",
                "mark_price": 0.31851,
                "est_liq_price": 0.0,
                "position_side": "LONG",
                "pnl_24_h": 0.0,
                "fee_24_h": 0.0,
                "margin_mode": "CROSS", 
                "leverage": 10, 
                "isolated_margin_token": "",
                "isolated_margin_amount": 0,
                "isolated_frozen_long": 0,
                "isolated_frozen_short": 0
            }
        ],
        "initial_margin_ratio": 1.0006,
        "free_collateral": 1145936.1530736,
        "maintenance_margin_ratio": 0.0126
    }
    

## Get All Position info - New

**Limit: 30 requests per 10 seconds per user**

` GET /v3/positions `

The API is design to replace the legacy API [Get Positions](#get-positions)

**Parameters**

None

> **Response**
    
    
    {
      "success": true,
      "data": {
        "positions": [
          {
            "symbol": "PERP_JTO_USDT",
            "holding": 20.0,
            "pendingLongQty": 0.0,
            "pendingShortQty": 0.0,
            "settlePrice": 2.0771,
            "averageOpenPrice": 2.0771,
            "pnl24H": 0.0,
            "fee24H": 0.0186939,
            "markPrice": 2.07460399,
            "estLiqPrice": 1.92748111,
            "timestamp": 1725916355.494,
            "adlQuantile": 1, // the grades of adlQuantile: 1 through 5
            "positionSide": "BOTH",
            "marginMode": "ISOLATED",
            "isolatedMarginToken": "USDT",
            "isolatedMarginAmount": 4.1604313,
            "isolatedFrozenLong": 0.0,
            "isolatedFrozenShort": 0.0,
            "leverage": 10
          },
          {
            "symbol": "PERP_W_USDT",
            "holding": -50.0,
            "pendingLongQty": 50.0,
            "pendingShortQty": 0.0,
            "settlePrice": 0.1906,
            "averageOpenPrice": 0.1906,
            "pnl24H": 0.0,
            "fee24H": 0.0,
            "markPrice": 0.2103828568089886,
            "estLiqPrice": 4.542491646808989,
            "timestamp": 1725681481.767,
            "adlQuantile": 1,
            "positionSide": "BOTH",
            "marginMode": "CROSS",
            "isolatedMarginToken": "",
            "isolatedMarginAmount": 0.0,
            "isolatedFrozenLong": 0.0,
            "isolatedFrozenShort": 0.0,
            "leverage": 20
          }
        ]
      },
      "timestamp": 1725916369913
    }
    
    

## Get One Position info

**Limit: 30 requests per 10 seconds per user**

ï¼Note that get-one-position-info will only support to response the CROSS mode position of the selected symbol.ï¼

` GET /v1/position/:symbol `

**Parameters**

None

> **Response**
    
    
    {
        "success": true,
        "symbol": "PERP_BTC_USDT",
        "holding": 1.23,
        "pending_long_qty": 0.5,
        "pending_short_qty": 0.23,
        "settle_price": 50000,
        "average_open_price": 49000,
        "pnl_24_h": 20,
        "fee_24_h": 0.2,
        "mark_price": 49550,
        "est_liq_price": 40000,
        "timestamp": "1575014255.089"
    }
    

## GET InsuranceFund

**Limit: token filtered to USDT only**

` GET /v3/public/insuranceFund `

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Y |   
  
> **Response**
    
    
    {
       "success": true,
        "data": {
          "rows": [
            {
              "balance": 1000,
              "token": "USDT",
            }
          ]
        },
        "timestamp": 1673323685109 
    }
    

## GET AssignmentPreference

**Limit: 10 requests per 60 seconds**

` GET /v3/liquidator/assignmentPreference `

Get your accountâs assignment preferences.Â 

**Parameters**

None

> **Response**
    
    
    {
        "success": true,
        "data": {
            "rows": [
                {
                    "symbol": "PERP_BTC_USDT",
                    "type": "USDT_NOTIONAL",
                    "maxAmountPerOrder": 10000,
                    "maxAmountTotal": null,
                    "acceptLong": true,
                    "acceptShort": true,
                },
                {
                    "symbol": "PERP_ETH_USDT",
                    "type": "BASE_TOKEN"
                    "maxAmountPerOrder": "100000",
                    "maxAmountTotal": "1000000",
                    "acceptLong": true,
                    "acceptShort": false,
                },
                ...
            ]
        },
        "timestamp": 1711433755393
    }
    

## Add an AssignmentPreference

**Limit: 10 requests per 60 seconds**

` POST /v3/liquidator/assignmentPreference `

Add an assignment preference for your account. If a preference already exists for the symbol, adding a new one will automatically override the previous preference.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Yes | Perpetual symbol name  
type | string | Yes | Specifies the type for the max amount. Options are USDT_NOTIONAL/BASE_TOKEN/LIMITLESS.  
maxAmountPerOrder | string | Conditional | Max assigned per order. If type is USDT_NOTIONAL or BASE_TOKEN, both maxAmountPerOrder and maxAmountTotal need to be specified. If type is LIMITLESS, maxAmountPerOrder and maxAmountTotal will be ignored.  
maxAmountTotal | string | Conditional | Max position size after assignment. If type is USDT_NOTIONAL or BASE_TOKEN, both maxAmountPerOrder and maxAmountTotal need to be specified. If type is LIMITLESS, maxAmountPerOrder and maxAmountTotal will be ignored.  
acceptLong | boolean | No (default: true) | Whether to accept long positions  
acceptShort | boolean | No (default: true) | Whether to accept short positions  
  
> **Response**
    
    
    {
        "success": true,
        "timestamp": 1711432330937
    }  
    

## Delete an AssignmentPreference

**Limit: 10 requests per 1 seconds**

` DELETE /v3/liquidator/assignmentPreference `

Delete an assignment preference by symbol.

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
symbol | string | Yes | symbol name  
  
> **Response**
    
    
    {
        "success": true,
        "timestamp": 1711432330937
    }  
    

# Websocket API V2

We will launch a new domain wss.woox.io on 2024/09/22. Please note that the old domain wss.woo.org will be decommissioned at a later date, which will be announced separately.

If you are a new user, please use the new domain wss.woox.io for integration. If you are an existing user, you may continue using wss.woo.org, but we strongly recommend migrating to wss.woox.io as soon as possible to avoid any future service disruptions.

**Market Data Base endpoints:**

  * `wss://wss.staging.woox.io/ws/stream/{application_id}` **(Staging)**
  * `wss://wss.woox.io/ws/stream/{application_id}` **(Production)**
  * `{application_id}` user can find application_id from console
  * user can subscribe/unsubscribe `orderbook`|`orderbook100`|`aggbook10`|`aggbook100`|`aggbook1000`|`ticker`|`tickers`|`bbo`|`trade`|`kline_1m`|`kline_5m`|`kline_15m`|`kline_30m`|`kline_1h`|`kline_1d`|`kline_1w`|`kline_1M`



**Private User Data Stream Base endpoints:**

  * `wss://wss.staging.woox.io/v2/ws/private/stream/{application_id}` **(Staging)**
  * `wss://wss.woox.io/v2/ws/private/stream/{application_id}` **(Production)**
  * `{application_id}` user can find application_id from console
  * User needs to be authenticated before subscribing any topic, would be disconnected if fails the authentication. Refer to [Authenticaton](#authentication) for more information. 
  * User can subscribe/unsubscribe `positioninfo`|`executionreport`



## PING/PONG

  * The server will send a ping command to the client every 10 seconds. If the pong from client is not received within 10 seconds for 10 consecutive times, it will actively disconnect the client.
  * The client can also send ping every 10s to keep alive.



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
event | string | Y | `ping`/`pong`  
      
    
    {
        "event":"ping"
    }
    

**Response**
    
    
    {
        "event":"pong",
        "ts":1614667590000
    }
    

## request orderbook

Push interval: real-time push

**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `request`  
params.type | string | Y | `orderbook`  
params.symbol | string | Y | `{symbol}`  
      
    
    {
        "id": "clientID1",
        "event": "request",
        "params": {
            "type": "orderbook",
            "symbol": "SPOT_BTC_USDT"
        }
    }
    

**Response**
    
    
    {
        "id":"123r",
        "event":"request",
        "success":true,
        "ts":1618880432419,
        "data":{
            "symbol":"SPOT_BTC_USDT",
            "ts":1618880432380,
            "asks":[
                [
                    54700,
                    0.443951
                ],
                [
                    54700.02,
                    0.002566
                ],
                ...
            ],
            "bids":[
                [
                    54699.99,
                    2.887466
                ],
                [
                    54699.76,
                    2.034711
                ],
               ...
            ]
        }
    }
    

## orderbook

  * Push interval: 1s
  * `{symbol}@orderbook` 100 levels, only push when there are actual change.



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@orderbook`/`{symbol}@orderbook100`  
      
    
    {
        "id": "clientID2",
        "topic": "SPOT_WOO_USDT@orderbook",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID2",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_WOO_USDT@orderbook"
    }
    

**Subscribed Message**
    
    
    {
        "topic": "SPOT_WOO_USDT@orderbook",
        "ts": 1614152140945,
        "data": {
            "symbol": "SPOT_WOO_USDT",
            "asks": [
                [
                    0.31075,
                    2379.63
                ],
                [
                    0.31076,
                    4818.76
                ],
                [
                    0.31078,
                    8496.1
                ],
                ...
            ],
            "bids": [
                [
                    0.30891,
                    2469.98
                ],
                [
                    0.3089,
                    482.5
                ],
                [
                    0.30877,
                    20
                ],
                ...
            ]
        }
    }
    

## orderbookupdate

  * `{symbol}@orderbookupdate` updated orderbook push every 200ms



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@orderbookupdate`  
      
    
    {
        "id": "clientID2",
        "topic": "SPOT_BTC_USDT@orderbookupdate",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID2",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_BTC_USDT@orderbookupdate"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"SPOT_BTC_USDT@orderbookupdate",
        "ts":1618826337580,
        "data":{
            "symbol":"SPOT_BTC_USDT",
            "prevTs":1618826337380,
            "asks":[
                [
                    56749.15,
                    3.92864
                ],
                [
                    56749.8,
                    0
                ],
                ...
            ],
            "bids":[
                [
                    56745.2,
                    1.03895025
                ],
                [
                    56744.6,
                    1.0807
                ],
                ...
            ]
        }
    }
    

## trade

  * Push interval: real-time push



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@trade`  
      
    
    {
        "id": "clientID3",
        "topic": "SPOT_ADA_USDT@trade",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_ADA_USDT@trade"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"SPOT_ADA_USDT@trade",
        "ts":1618820361552,
        "data":{
            "symbol":"SPOT_ADA_USDT",
            "price":1.27988,
            "size":300,
            "side":"BUY",
            "source":0,
            "rpi":true
        }
    }
    

## trades

  * Push interval: 200ms



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `SPOT_BTC_USDT@trades`  
      
    
    {
        "id": "clientID3",
        "topic": "SPOT_BTC_USDT@trades",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_BTC_USDT@trades"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"SPOT_BTC_USDT@trades",
        "ts":1618820361552,
        "data":[{
            "symbol":"SPOT_BTC_USDT",
            "price":42598.27,
            "size":300,
            "side":"BUY",
            "source":0,
            "rpi":true
        },
        {
            "symbol":"SPOT_BTC_USDT",
            "price":42589.74,
            "size":200,
            "side":"BUY",
            "source":0,
            "rpi":true
        }
        ]
    }
    

## 24h ticker

  * Push interval:1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@ticker`  
      
    
    {
        "id": "clientID4",
        "topic": "SPOT_WOO_USDT@ticker",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID4",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_WOO_USDT@ticker"
    
    }
    

**Subscribed Message**
    
    
    {
        "topic": "SPOT_WOO_USDT@ticker",
        "ts": 1614152270000,
        "data": {
            "symbol": "SPOT_WOO_USDT",
            "open": 0.16112,
            "close": 0.32206,
            "high": 0.33000,
            "low": 0.14251,
            "volume": 89040821.98,
            "amount": 22493062.21,
            "aggregatedQuantity": 20598.85059063,
            "aggregatedAmount": 1303973569.5714033,
            "count": 15442ï¼
            "astTs": 1727161921650
        }
    }
    

## 24h tickers

  * Push interval: 1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `tickers`  
      
    
    {
        "id": "clientID4",
        "topic": "tickers",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID4",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "tickers"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"tickers",
        "ts":1618820615000,
        "data":[
            {
                "symbol":"SPOT_OKB_USDT",
                "open":16.297,
                "close":17.183,
                "high":24.707,
                "low":11.997,
                "volume":0,
                "amount":0,
                "aggregatedQuantity": 20598.85059063,
                "aggregatedAmount": 1303973569.5714033,
                "count":0,
                "astTs": 1727161921650
            },
            {
                "symbol":"SPOT_XRP_USDT",
                "open":1.3515,
                "close":1.43794,
                "high":1.96674,
                "low":0.39264,
                "volume":750127.1,
                "amount":985440.5122,
                "aggregatedQuantity": 20598.85059063,
                "aggregatedAmount": 1303973569.5714033,
                "count":396,
                "astTs": 1727161921650
            },
           ...
        ]
    }
    

## bbo

  * Push interval: 10ms



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@bbo`  
      
    
    {
        "id": "clientID5",
        "topic": "SPOT_WOO_USDT@bbo",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID5",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_WOO_USDT@bbo"
    }
    

**Subscribed Message**
    
    
    {
        "topic": "SPOT_WOO_USDT@bbo",
        "ts": 1614152296945,
        "data": {
            "symbol": "SPOT_WOO_USDT",
            "ask": 0.30939,
            "askSize": 4508.53,
            "bid": 0.30776,
            "bidSize": 25246.14
        }
    }
    

## bbos

  * Push interval: 1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `bbos`  
      
    
    {
        "id": "clientID5",
        "topic": "bbos",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID5",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "bbos"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"bbos",
        "ts":1618822376000,
        "data":[
            {
                "symbol":"SPOT_FIL_USDT",
                "ask":159.0318,
                "askSize":370.43,
                "bid":158.9158,
                "bidSize":16
            },
            {
                "symbol":"SPOT_BTC_USDT",
                "ask":56987.18,
                "askSize":3.163881,
                "bid":56987.17,
                "bidSize":0.941728
            },
           ...
        ]
    }
    

## k-line

  * `{time}`: `1m`/`5m`/`15m`/`30m`/`1h`/`1d`/`1w`/`1M`
  * Push interval: by the selected k-line type.



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | N | `{symbol}@kline_{time}`  
      
    
    {
        "id": "clientID6",
        "topic": "SPOT_BTC_USDT@kline_1m",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID6",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_BTC_USDT@kline_1m"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"SPOT_BTC_USDT@kline_1m",
        "ts":1618822432146,
        "data":{
            "symbol":"SPOT_BTC_USDT",
            "type":"1m",
            "open":56948.97,
            "close":56891.76,
            "high":56948.97,
            "low":56889.06,
            "volume":44.00947568,
            "amount":2504584.9,
            "startTime":1618822380000,
            "endTime":1618822440000
        }
    }
    

## indexprice

  * Push interval: 1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@indexprice`  
      
    
    {
        "id": "clientID3",
        "topic": "SPOT_ETH_USDT@indexprice",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "SPOT_ETH_USDT@indexprice"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"SPOT_ETH_USDT@indexprice",
        "ts":1618820361552,
        "data":{
            "symbol":"SPOT_ETH_USDT",
            "price":3987.1
        }
    }
    

## markprice

  * Push interval: 1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@markprice`  
      
    
    {
        "id": "clientID3",
        "topic": "PERP_ETH_USDT@markprice",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "PERP_ETH_USDT@markprice"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"PERP_ETH_USDT@markprice",
        "ts":1618820361552,
        "data":{
            "symbol":"PERP_ETH_USDT",
            "price":3987.2
        }
    }
    

## estfundingrate

  * Push interval: 1min



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `{symbol}@estfundingrate`  
      
    
    {
        "id": "clientID3",
        "topic": "PERP_BTC_USDT@estfundingrate",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "PERP_BTC_USDT@estfundingrate"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"PERP_BTC_USDT@estfundingrate",
        "ts":1618820361552,
        "data":{
            "symbol":"PERP_BTC_USDT",
            "fundingRate":1.27988,
            "fundingTs":1618820361552
        }
    }
    

## openinterests

  * Push interval: 10s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `openinterests`  
      
    
    {
        "id": "clientID3",
        "topic": "openinterests",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "openinterests"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"openinterests",
        "ts":1618820361552,
        "data":[
            {
            "symbol":"PERP_BNB_USDT",
            "openinterest":936.37
        },
           {
            "symbol":"PERP_ORDI_USDT",
            "openinterest":110.1
        }
        ]
    }
    

## markprices

  * Push interval: 1s



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `markprices`  
      
    
    {
        "id": "clientID5",
        "topic": "markprices",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID5",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "openinterests"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"markprices",
        "ts":1618822376000,
        "data":[
            {
               "symbol":"PERP_BTC_USDT",
                "price":51234.13
            },
            {
                "symbol":"PERP_ETH_USDT",
                  "price":3894.34
            },
           ...
        ]
    }
    

## auth

  * refer to [Authenticaton](#authentication) for more details about how to sign the request with `api_key` and `api_secret`. **query string** and **body parameters** are both blank.



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
apikey | string | Y | api key  
sign | string | Y | sign  
timestamp | string | Y | timestamp  
      
    
    {
        "id":"123r",
        "event":"auth",
        "params":{
            "apikey":"CUS69ZJOXwSV38xo...",
            "sign":"4180da84117fc9753b...",
            "timestamp":"1621910107900"
        }
    }
    

**Response**
    
    
    {
        "id":"123r",
        "event":"auth",
        "success":true,
        "ts":1621910107315
    }
    

## balance

  * Push interval: realtime (push on update)



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `balance`  
      
    
    {
        "id": "clientID3",
        "topic": "balance",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "balance"
    }
    

**Subscribed Message**
    
    
    {
        "topic":"balance",
        "ts":1618757714353,
        "data":{
            "balances":{
                "BTC":{
                    "holding":0,
                    "frozen":0,
                    "interest":0,
                    "pendingShortQty":0,
                    "pendingLongQty":0,
                    "version":0,
                    "staked":0,
                    "unbonding":0,
                    "vault":309.8,
                    "launchpadVault":0.0,
                    "earn":0.0,
                    "averageOpenPrice":0,
                    "pnl24H":0,
                    "fee24H":0,
                    "markPrice":0,
                    "timestamp": 1618757713353 
                },
                "ETH":{
                    "holding":0,
                    "frozen":0,
                    "interest":0,
                    "pendingShortQty":0,
                    "pendingLongQty":0,
                    "version":0,
                    "staked":0,
                    "unbonding":0,
                    "vault":309.8,
                    "launchpadVault":0.0,
                    "earn":0.0,
                    "averageOpenPrice":0,
                    "pnl24H":0,
                    "fee24H":0,
                    "markPrice":0,
                    "timestamp": 1618757713353 
                },
                ...
            }
        }
    }
    

## executionreport

  * Push interval: real-time push



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `executionreport`  
      
    
    {
        "id": "clientID3",
        "topic": "executionreport",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "executionreport"
    }
    

**Subscribed Message**
    
    
    // receive for order status in new, filled, partial filled execution report
    {
        "topic": "executionreport",
        "ts": 1675406261689,
        "data":
        {
            "msgType": 0,  // execution report
            "symbol": "SPOT_BTC_USDT",
            "clientOrderId": 0,
            "orderId": 54774393,
            "type": "MARKET",
            "side": "BUY",
            "quantity": 0.0,
            "price": 0.0,
            "tradeId": 56201985,
            "executedPrice": 23534.06,
            "executedQuantity": 0.00040791,
            "fee": 2.1E-7,
            "feeAsset": "BTC",
            "totalExecutedQuantity": 0.00040791,
            "avgPrice": 23534.06,
            "status": "FILLED",
            "reason": "",
            "orderTag": "default",
            "totalFee": 2.1E-7,
            "feeCurrency": "BTC",
            "totalRebate": 0,
            "rebateCurrency": "USDT",
            "visible": 0.0,
            "timestamp": 1675406261689,
            "reduceOnly": false,
            "maker": false,
            "leverage": 10,
            "marginMode": "CROSS",
            "rpi": true
        }
    }
    
    // receive when editing order be rejected
    {
        "topic": "executionreport",
        "ts": 1675406261689,
        "data":
        {
            "msgType": 1,  // edit reject
            "symbol": "SPOT_BTC_USDT",
            "orderId": 54774393,
            "clientOrderId": 11111,
            "reason": ""
        }
    }
    
    // receive when canceling order be rejected
    {
        "topic": "executionreport",
        "ts": 1675406261689,
        "data":
        {
            "msgType": 2,  // cancel reject
            "symbol": "SPOT_BTC_USDT",
            "orderId": 54774393,
            "clientOrderId": 11111,
            "reason": ""
        }
    }
    
    // receive when canceling ALL orders be rejected
    {
        "topic": "executionreport",
        "ts": 1675406261689,
        "data":
        {
            "msgType": 3,  // cancel all reject
            "symbol": "SPOT_BTC_USDT",
            "reason": ""
        }
    }
    
    

## algoexecutionreportv2

  * Push interval: real-time push



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | `subscribe`/`unsubscribe`  
topic | string | Y | `algoexecutionreportv2`  
      
    
    {
        "id": "clientID3",
        "topic": "algoexecutionreportv2",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "algoexecutionreportv2"
    }
    

**Subscribed Message**
    
    
    {
        "topic": "algoexecutionreportv2",
        "ts": 1667978011834,
        "data": [
            {
                "symbol": "SPOT_BAL_USDT",
                "rootAlgoOrderId": 345181,
                "parentAlgoOrderId": 0,
                "algoOrderId": 345181,
                "clientOrderId": 0,
                "orderTag": "default",
                "status": "NEW",
                "algoType": "BRACKET",
                "side": "SELL",
                "quantity": 1,
                "triggerStatus": "SUCCESS",
                "price": 69,
                "type": "LIMIT",
                "triggerTradePrice": 0,
                "triggerTime": 0,
                "tradeId": 0,
                "executedPrice": 0,
                "executedQuantity": 0,
                "fee": 0,
                "reason": "",
                "feeAsset": "USDT",
                "totalExecutedQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeCurrency": "USDT",
                "totalRebate": 0,
                "rebateCurrency": "BAL",
                "timestamp": 1667978011834,
                "visibleQuantity": 1,
                "reduceOnly": false,
                "activatedPrice": 0,
                "triggered": false,
                "activated": false,
                "maker": false,
                "isTriggered": false,
                "isMaker": false,
                "isActivated": false,
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "leverage": 10,
                "marginMode": "CROSS",
            },
            {
                "symbol": "SPOT_BAL_USDT",
                "rootAlgoOrderId": 345181,
                "parentAlgoOrderId": 345181,
                "algoOrderId": 345182,
                "clientOrderId": 0,
                "orderTag": "default",
                "algoType": "POSITIONAL_TP_SL",
                "side": "BUY",
                "quantity": 0,
                "triggerStatus": "USELESS",
                "price": 0,
                "triggerTradePrice": 0,
                "triggerTime": 0,
                "tradeId": 0,
                "executedPrice": 0,
                "executedQuantity": 0,
                "fee": 0,
                "reason": "",
                "feeAsset": "",
                "totalExecutedQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeCurrency": "USDT",
                "totalRebate": 0,
                "rebateCurrency": "BAL",
                "timestamp": 1667978011900,
                "visibleQuantity": 0,
                "reduceOnly": false,
                "activatedPrice": 0,
                "triggered": false,
                "activated": false,
                "maker": false,
                "isTriggered": false,
                "isMaker": false,
                "isActivated": false,
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "leverage": 10,
                "marginMode": "CROSS",
            },
            {
                "symbol": "SPOT_BAL_USDT",
                "rootAlgoOrderId": 345181,
                "parentAlgoOrderId": 345182,
                "algoOrderId": 345183,
                "clientOrderId": 0,
                "orderTag": "default",
                "algoType": "TAKE_PROFIT",
                "side": "BUY",
                "quantity": 0,
                "triggerPrice": 50,
                "triggerStatus": "USELESS",
                "price": 0,
                "type": "CLOSE_POSITION",
                "triggerTradePrice": 0,
                "triggerTime": 0,
                "tradeId": 0,
                "executedPrice": 0,
                "executedQuantity": 0,
                "fee": 0,
                "reason": "",
                "feeAsset": "",
                "totalExecutedQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeCurrency": "USDT",
                "totalRebate": 0,
                "rebateCurrency": "BAL",
                "timestamp": 1667978011900,
                "visibleQuantity": 0,
                "reduceOnly": true,
                "activatedPrice": 0,
                "triggered": false,
                "activated": false,
                "maker": false,
                "isTriggered": false,
                "isMaker": false,
                "isActivated": false,
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "leverage": 10,
                "marginMode": "CROSS",
            },
            {
                "symbol": "SPOT_BAL_USDT",
                "rootAlgoOrderId": 345181,
                "parentAlgoOrderId": 345182,
                "algoOrderId": 345184,
                "clientOrderId": 0,
                "orderTag": "default",
                "algoType": "STOP_LOSS",
                "side": "BUY",
                "quantity": 0,
                "triggerPrice": 75,
                "triggerStatus": "USELESS",
                "price": 0,
                "type": "CLOSE_POSITION",
                "triggerTradePrice": 0,
                "triggerTime": 0,
                "tradeId": 0,
                "executedPrice": 0,
                "executedQuantity": 0,
                "fee": 0,
                "reason": "",
                "feeAsset": "",
                "totalExecutedQuantity": 0,
                "averageExecutedPrice": 0,
                "totalFee": 0,
                "feeCurrency": "USDT",
                "totalRebate": 0,
                "rebateCurrency": "BAL",
                "timestamp": 1667978011900,
                "visibleQuantity": 0,
                "reduceOnly": true,
                "activatedPrice": 0,
                "triggered": false,
                "activated": false,
                "maker": false,
                "isTriggered": false,
                "isMaker": false,
                "isActivated": false,
                "rootAlgoStatus": "NEW",
                "algoStatus": "NEW",
                "leverage": 10,
                "marginMode": "CROSS",
            }
        ]
    }
    

## position push

  * Push interval: push on update



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | subscribe`/`unsubscribe  
topic | string | Y | position  
      
    
    {
        "id": "clientID5",
        "topic": "position",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID5",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "position"
    }
    

**Subscribed Message**
    
    
    {
        "topic": "position",
        "ts": 1711612096824,
        "data": {
            "positions": [
                "PERP_WOO_USDT": {
                    "holding": 0.0,
                    "pendingLongQty": 0.00020,
                    "pendingShortQty": 0.0,
                    "averageOpenPrice": 0.0,
                    "pnl24H": -1.55902,
                    "fee24H": 0.21800043,
                    "settlePrice": 0.0,
                    "markPrice": 22325.47533333,
                    "version": 93454,
                    "openingTime": 0,
                    "pnl24HPercentage": -0.00542227
                    "adlQuantile": 1,
                    "timestamp": 1677814653001ï¼
                    "leverage": 10,
                    "marginMode": "ISOLATED",
                    "isolatedMarginToken": "USDT",
                    "isolatedMarginAmount": 1000,                
                    "isolatedFrozenLong": 10,
                    "isolatedFrozenShort": 10,
                },
                "PERP_WOO_USDT": {
                    // ... omit existing fields
    
                    "leverage": 10,
                    "marginMode": "CROSS",
                    "isolatedMarginToken": "",
                    "isolatedMarginAmount": 0,                
                    "isolatedFrozenLong": 0,
                    "isolatedFrozenShort": 0,
                }
            ]
        }
    }
    

## marginassignment

  * Push interval: real-time push



**Parameters**

Name | Type | Required | Description  
---|---|---|---  
id | string | Y | id generate by client  
event | string | Y | subscribe`/`unsubscribe  
topic | string | Y | marginassignment  
      
    
    {
        "id": "clientID3",
        "topic": "marginassignment",
        "event": "subscribe"
    }
    

**Response**
    
    
    {
        "id": "clientID3",
        "event": "subscribe",
        "success": true,
        "ts": 1609924478533,
        "data": "marginassignment"
    }
    

**Subscribed Message**
    
    
    {
         "topic": "marginassignment",
         "ts": 1677814655102,
         "data":{
             "margin": [
                 {   
                     "token": "USDT",
                     "qty": 35.41628771
                 },
                 {
                     "token": "WOO",
                     "qty": 83.62,
                 },
                 ...
             ],
             "orders": [
                 {
                     "id": 5306374839,
                     "symbol": "PERP_NEAR_USDT",
                     "price": 1.7,
                     "type": "LIQUIDATE_BLP",
                     "status": "FILLED",
                     "referencePrice": 1.7,
                     "quantity": 7.0,
                     "side": "BUY",
                     "executedQuantity": 7.0,
                     "executedAmount": 11.9,
                     "visibleQty": 7.0,
                     "feeAsset": "USDT",
                     "fee": 0
                },
                ...
             ]
        }
    }
    
    

# Release Note

All the API changes would be listed here. 

## 2025-09-21

**Post Only Adjusted Order Now Live**

The Post Only Adjusted Order is now supported, giving users more flexibility when providing liquidity.

**How it works:**

  * Normal Post-Only: The order is rejected if it would cross the book and execute immediately as a taker.
  * Post Only Adjusted: Instead of rejecting, the order price is automatically adjusted so it can still rest on the book as a maker. 
    * For buy orders, the price is adjusted to best ask - 1 tick.
    * For sell orders, the price is adjusted to best bid + 1 tick.



## 2025-07-14

**Retail Price Improvement (RPI) Now Live**

The RPI order type is now supported across REST and WebSocket V3 APIs, enabling market makers to provide improved execution for retail flow. Key API updates include:

**REST API Updates**

  * Market Trades (Public) `GET /v1/public/market_trades` added rpi field to response to indicate whether the trade was matched via RPI.
  * Market Trades History(Public) `GET https://api-pub.woo.org/v1/hist/trade` added rpi field to response to indicate whether the trade was matched via RPI.
  * Send Order `POST /v1/order` now supports submitting orders with the RPI order type.
  * Get Orders `GET /v1/orders` supports filtering by RPI order type.
  * Get Trade `GET /v1/client/trade/:tid` added is_match_rpi field to response to indicate whether the trade was matched via RPI.
  * Get Trades `GET /v1/order/:oid/trades` added is_match_rpi field to response to indicate whether the trade was matched via RPI.
  * Get Trade History `GET /v1/client/trades` added is_match_rpi field to response to indicate whether the trade was matched via RPI.
  * Get Archived Trade History `GET /v1/client/hist_trades` added is_match_rpi field to response to indicate whether the trade was matched via RPI.



**WebSocket API V2 Updates**

  * trade topic



Added rpi field to messages to indicate whether the trade was matched via RPI.

  * trades topic



Added rpi field to messages to indicate whether the trade was matched via RPI.

  * executionreport topic



Added rpi field to messages to indicate whether the trade was matched via RPI.

## 2025-04-30

  * For [get-token-history](#get-token-history), the type parameter will be updated from SPOT_TRADING and TRADING_FEE (order-based) to SPOT_TRANSACTION and TRANSACTION_FEE (trade-based). 



## 2024-09-22

  * We plan to release WOO X new domain migration, we are updating our API endpoint(s), please see the following table. Please notice, the new production endpoints will be accessible on 2024/9/22. 

**Environment** | **Old Endpoint** | **New Endpoint**  
---|---|---  
Production | `https://api.woo.org` | `https://api.woox.io`  
| `https://api.woo.network` |   
Production | `wss://wss.woo.org` | `wss://wss.woox.io`  
| `wss://wss.woo.network` |   
Production | `https://api-pub.woo.org` | `https://api-pub.woox.io`  
Staging | `https://api.staging.woo.org` | `https://api.staging.woox.io`  
| `https://api.staging.woo.network` |   
Staging | `wss://wss.staging.woo.org` | `wss://wss.staging.woox.io`  
| `wss://wss.staging.woo.network` |   
  
You only need to replace the base URL, and nothing else needs to be changed. For Production Endpoint base URL change,Please notice, the new production endpoints will be accessible on 2024/9/22.

**API** : `api.woo.org` -> `api.woox.io` **WebSocket** : `wss://wss.woo.org` -> `wss://wss.woox.io`

For Staging Endpoint base URL change,This endpoint is accessible now

**API** : `api.staging.woo.org` -> `api.staging.woox.io` **WebSocket** : `wss://wss.staging.woo.org` -> `wss://wss.staging.woox.io`

  * Add REST API [get-assignmentpreference](#get-assignmentpreference).
  * Add REST API [add-an-assignmentpreference](#add-an-assignmentpreference).
  * Add REST API [delete-an-assignmentpreference](#delete-an-assignmentpreference).
  * Add `network` field in the response of REST API [token network (public)](#token-network-public). 



## 2024-07-14

  * We are going to release Isolated-Margin trading mode in up coming release in 2024-07-04, it will includes following changes:
  * Add `margin_mode` optional parameter for [send-order](#send-order), [send-algo-order](#send-algo-order). 
  * Add `marginMode` and `leverage` in response body for [get-order](#get-order), [get-orders](#get-orders), [get-order-by-client_order_id](#get-order-by-client_order_id).
  * Add `margin_mode` and `leverage` in response body for [get-algo-order](#get-algo-order), [get-algo-orders](#get-algo-orders).
  * Break down the response for [get-all-position-info](#get-all-position-info) and [get-all-position-info](#get-all-position-info-new) to perform the position status of different mode of each symbols by adding `marginMode` and `leverage` fields. Note that [get-one-position-info](#get-one-position-info) will only support to response the `CROSS` mode position of the selected symbol.
  * For [get-account-information-new](#get-account-information-new), the `leverage` field will be become specificially for SPOT/MARGIN leverage, will be deprecated (present null) when account mode is FUTURES. Also, the `totalAccountValue`.
  * For [update-leverage-setting](#update-leverage-setting) endpoint will only supprot MARGIN mode, for FUTURES mode, release new endpoint [update-futures-leverage-setting](#update-futures-leverage-setting) and [get-futures-leverage-setting](#get-futures-leverage-setting) to manage the setting 
  * Add [update-isolated-margin-setting](#update-isolated-margin-setting) endpoint.
  * Add `leverage`, `marginMode`,`isolatedMarginToken`,`isolatedMarginAmount`,`isolatedFrozenLong`,`solatedFrozenShort` fields in the push message of Websocket topic [positions](#position-push).
  * Add `leverage`, `marginMode` fields in the push message of Websocket topic [executionreport](#executionreport) and [algoexecutionreportv2](#algoexecutionreportv2).
  * Sunset RESTful endpoints deprecated by 2023Q1, including [get-current-holding](#get-current-holding) and [get-current-holding-v2](#get-current-holding-v2). Please find the replacement API in [get balances](#get-current-holding-get-balance-new).



## 2024-07-04

  * Adjusted the rate of this API[get-archived-trade-history](#get-archived-trade-history).



## 2024-06-24

  * Add `id` optional parameter for [get-asset-history](#get-asset-history).



## 2024-06-09

  * Add update errorCode definition for order related service[order-service-error-code](#order-service-error-code).



## 2024-05-20

  * Add `x-api-recvwindow` optional paramter for Authenticationï¼only for vip usersï¼



## 2024-05-09

  * Corrected return value for REST API [get-current-holding-get-balance-new](#get-current-holding-get-balance-new).



## 2024-04-22

  * Add REST API [token-withdraw-v3](#token-withdraw-v3).
  * Add return value `balance_token` and `network` for REST API [available-token-(public)](#available-token-public).



## 2024-04-16

  * Add usage instructionsfor REST API [cancel-all-after](#get-cancel-all-after)



## 2024-03-31 ï¼4/2 system releaseï¼

  * Add return value `total_rebate` and `rebate_asset` for REST API [get-order](#get-order), [get-order-by-client_order_id](#get-order-by-client_order_id), [get-orders](#get-orders), [get-algo-order](#get-algo-order) and [get-algo-orders](#get-algo-orders)
  * Add `totalRebate` and `rebateCurrency` message for WSS topic response [executionreport](#executionreport) and [algoexecutionreportv2](#algoexecutionreportv2)
  * Add REST API [cancel-all-after](#cancel-all-after)
  * Add explanation for the parameter `reduce_only` for REST API [send-order](#send-order) and [send-algo-order](#send-algo-order)
  * Upgrade rate limit for [Send Order](#send-order) from 5 requests to 10 requests per symbol per second .



## 2024-03-25

  * Change on webscoekt response data by adding `data` field to all Resopnse Message for the subscription event (`subscribe`), the `data` field will contain the subscribed topic.



## 2024-02-26

  * Add new REST API [Internal-token-withdraw](#internal-token-withdraw) for internal token withdraw
  * Corrected return value for REST API [get-archived-trade-history](#get-archived-trade-history)



## 2024-02-21

  * Corrected return value of `status` paramtere for REST API [get-system-maintenance-status-public](#get-system-maintenance-status-public)



## 2024-02-21

  * Corrected return value of `status` paramtere for REST API [get-system-maintenance-status-public](#get-system-maintenance-status-public)



## 2024-01-30

  * Add `msgType` and `reason` message for WSS topic response [executionreport](#executionreport)



## 2024-01-10

  * Add `positionSide` optional paramtere REST API [Send Order](#send-order),[send-algo-order](#send-algo-order) for placing Short/Long order.



## 2023-12-12

  * Add new Websocket topic [marginassignment](#marginassignment), The topic is design to get margin assignment information.



## 2023-10-30

  * Add REST API [GET InsuranceFund](#get-insurancefund) for fetching insurance fund information.



## 2023-09-25

  * Add `token` optional paramtere REST API [Get Current Holding (Get Balance) - New](#get-current-holding-get-balance-new) for fetching single token's holding information.



## 2023-07-24

  * Upgrade rate limit for [Send Order](#send-order) from 2 requests to 5 requests per symbol per second .
  * Add RESTful API: [Get referrals summary](#get-referrals-summary) and [Get referral reward history](#get-referral-reward-history) for fetching referral rewards detail.



## 2023-07-03

  * Add `averageOpenPrice` and `markPrice` to [Get Current Holding (Get Balances)](#get-current-holding-get-balance-new).
  * Sunset deprecated RESTful API: [Get Account Info](#get-account-information), please find the replacement API in [Get Account Information - New](#get-account-information-new).
  * Sunset deprecated Websocket Topic: [positioninfo](#positioninfo), please find the replacement topic in [balance](#balance).



## 2023-06-12

  * Add `loan_amount` in the response message of API [Get Interest History](#get-interest-history) for side = `LOAN`.
  * Add [Get Token History](#get-token-history) API fetching token balance change history.



## 2023-04-10

  * Add `can_collateral` and `can_short` in the response message of API [Available Token (Public)](#available-token-public).
  * Change response message of Funding Rate related API for new funding rate calculation rules released in 2023-04-10, including [Get Predicted Funding Rate for All Markets](#get-predicted-funding-rate-for-all-markets-public), [Get Predicted Funding Rate for One Market](#get-predicted-funding-rate-for-one-market-public) and [Get Funding Rate History for One Market](#get-funding-rate-history-for-one-market-public).
  * Change [Orderbook Snapshot](#orderbook-snapshot-public) and [Kline](#kline-public) RESTful API from privateto public endpoint. (Those two endpoint will not require authentication anymore).



## 2023-02-06

  * Add [Get Balance](#get-current-holding-get-balance-new) API. The API is design to replace the legacy API [Get Current Holding](#get-current-holding) and [Get Current Holding v2](#get-current-holding-v2).
  * Add [Get Account Information - New](#get-account-information-new). the API is design to replace the legacy API [Get Account Information](#get-account-information).
  * Add [Get All Position Info - New](#get-all-position-info-new). The API is design to replace the legacy API [Get Positions](#get-positions)
  * Add [Get Buy Power](#get-buy-power) for query buying power of selected symbol.
  * Add New Websocket topic [balance](#balance). The topic is design to replace existing topic [positionsinfo](#positionsinfo).



## 2022-12-05

  * Add [Edit Order](#edit-order), [Edit order by client_order_id](#edit-order-by-client_order_id), [Edit Algo Order](#edit-algo-order) and [Edit Algo order by client_order_id](#edit-algo-order-by-client_order_id).
  * Update push frequency for websocket topics: [bbo](#bbo), [24 ticker](#24-ticker), [Open Interest](#openinterest) and [orderbook](#orderbook).
  * Update rate limit for [Get Token Deposit Address](#get-token-deposit-address) and [Token Withdraw](#token-withdraw).



## 2022-11-21

  * Add [Market Trade History](#market-trade-history) for fetching trade history data.



## 2022-10-24

  * Add [Send Algo Order](#send-algo-order) to create Algo Order through the API, support algo types include: `STOP`(stop market & stop limit), `OCO`, `TRAILING_STOP`, `BRACKET` and `POSITIONAL_TP_SL`.
  * Add [Cancel Algo Order](#cancel-algo-order), [Cancel All Pending Algo Orders](#cancel-all-pending-algo-orders) and [Cancel Pending Merge Orders by Symbol](#cancel-pending-merge-orders-by-symbol).
  * Add [Get Algo Order](#get-algo-order) and [Get Algo Orders](#get-algo-orders) to fetch Algo Orders detail through the API.
  * Add [Cancel All Pending Order](#cancel-all-pending-order) to cancel all pending Ordinary Orders (not include Algo Orders) through the API.
  * Update [authentication](#authentication) section for `v3` API to generate the signature with `timestamp`, `request_method`, `request_path` and `request_body`.
  * Add [Get System Maintenance Status](#get-system-maintenance-status-public) API to fetch system status.



## 2022-09-08

  * Add `can_collateral` in the response message of API [Available Token (Public)](#available-token-public).
  * Add `realized_pnl` in the response message of API [Get Order](#get-order), [Get Order by client_order_id](#get-order-by-client_order_id) and [Get Orders](#get-orders). And add `realized_pnl` parameter in the request body of API [Get Orders](#get-orders). The `realized_pnl` field in response will only present the settled amount for futures orders.
  * Newly support `1m` in `type` parameter in the query string of API for [Historical Kline](#kline-historical-data).



## 2022-08-18

  * update [Token Withdraw](#token-withdraw) API by remove `code` parameter, the new version will not require 2FA code for those withdrawal address been verified in the address book.
  * Increase rate limit of [Get All Position info](#get-all-position-info) and [Get One Position info](#get-one-position-info) to 30 requests per second.



## 2022-07-28

  * Add `reduce_only` parameter in the request body of API [Send_Order](#send-order).
  * Add `reduce_only` in the response message of API [Get_Order](#get-order), [Get_Order_by_client_order_id](#get-order-by-client_order_id) and [Get_Orders](#get-orders).
  * Add `source` in the response message of API [Market_Trades(Public)](#market-trades-public).
  * Add `source` in the push message of Websocket Topic [trades](#trade).



## 2022-06-10

  * Add `total_collateral`, `free_collateral`, `total_account_value`, `total_vault_value`, `total_staking_value` and `est_liq_price` for each futures positions in [Position Info](#get-all-position-info).
  * Deprecate websocket subscription topic: [Orderbook](#orderbook) depth 1000, the original {symbol}@orderbook topic will keep alive but push the same data as symbol@orderbook100 (depth 100).



## 2022-05-23

  * Upgrade websocket subscription topic: [bbo](#bbo) push frequency from 200ms to 10ms.
  * Add public API for [Historical Kline](#kline-historical-data).



## 2022-03-21

  * Add public API for [Funding Rate](#get-predicted-funding-rate-for-all-markets-public) and [Futures Info](#get-futures-info-for-all-markets-public).
  * Add private API for [Change Account mode](#update-account-mode), [Change Leverage](#update-leverage-setting).
  * Add private API for [Funding Fee](#get-funding-fee-history), [Position Info](#get-all-position-info).
  * Add `account_mode`, `futures_leverage`, `futures_taker_fee_rate`, `futures_maker_fee_rate` in [Account Information](#get-account-information).
  * Add `futures_margin_factor` in [Token Config](#token-config), 
  * Add Websocket Topics [indexprice](#indexprice), [markprice](#markprice), [openinterest](#openinterest), [estfundingrate](#estfundingrate), [markprices](#markprices), [position push](#position-push)



## 2022-02-25

  * Add API [SubAccount](#get-subaccounts) to manage subaccounts.



## 2022-01-17

  * Add `can_collateral`, `can_short` and `stable` in [Token_Config](#token-config)



## 2021-12-24

  * Add API [Kline](#kline) to query yearly Kline.

  * Add `client_order_id` and `timestamp` in the response message of API [Send_Order](#send-order).




## 2021-11-12

  * Add API [Kline](#kline) to provide at most 1000 klines.



## 2021-10-22

  * Add Public API Token Network to query the token deposit/withdrawal information on each network.

  * Add rate limit on public APIs.




## 2021-09-27

  * Add API [Margin_Interest_Rates](#margin-interest-rates) and [Margin_Interest_Rate_of_Token](#margin-interest-rate-of-token) to query the margin interest rates.



## 2021-09-06

  * Adjust rate limit of API [Get_Order](#get-order) and [Get_Order_by_client_order_id](#get-order-by-client_order_id) to 10 per second in total.

  * Adjust rate limit of API [Cancel_Order](#cancel-order) and [Cancel_Order_by_client_order_id](#cancel-order-by-client_order_id) to 10 per second in total.

  * Adjust rate limit of API [Get_Trade](#get-trade), [Get_Trades](#get-trades) to 10 per second for each.




## 2021-09-03

  * Add API [Token_Config](#token-config)



## 2021-08-06

  * Remove `Transactions` from [Get_Orders](#get-orders)

  * Add `total_fee` and `fee_asset` in [Get_Order](#get-order), [Get_Order_by_client_order_id](#get-order-by-client_order_id), [Get_Orders](#get-orders)




## 2021-07-09

  * Websocket topic [positioninfo](#positioninfo) stop pushing the tokens that have never been traded before to reduce the message size.



## 2021-06-25

  * Add API [Cancel_Order_by_client_order_id](#cancel-order-by-client_order_id)



User could cancel order by the user-specified `client_order_id`.

  * Add API [Get_Trades](#get-trades)



User could get all the trades by `order_id`.

  * Adjust rate limit of API [Send_Order](#send-order) from 120 per minute to 2 per second per symbol



[cURL](#) [Python](#) [Node.js](#) [Java](#)
