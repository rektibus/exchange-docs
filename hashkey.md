

[TOC]



# Change log
|Doc Version|API Version|Date|Modification|Author|
|-------|----|--------------|--------|--------|
|v0.1|v1.0|2022/03/21|Initial version|Dingchun|


# 1. Getting Started

The exchange provides two interface modes for API users:

* **REST**: Use synchronous calls (request/response) to complete functions such as order creation, order cancellation, query transaction history,order history, portfolio, transfer history, etc.
* **WebSocket**: Use an asynchronous method (pubsub) to complete the subscribed push notification of orders, transactions, market data and other information.
In order to facilitate users understanding following are the common steps to access and implement API to complete trading programs

## 1.1 Preparations

### 1.1.1 API-KEY Management

* Users have to log in the exchange website and apply for an API-KEY, please make sure to remember the following information when creating an API key:
  * **Access key**: API access key
  * **secret key**：the key used for signature authentication encryption (visible to the application only)

* Users have to assign permissions to API-KEY. There are four kinds of permissions,
  * **READ** read permission is used for data query interfaces such as order query, transaction query, etc.
  * **TRADE** trade permission is used for order placing, order cancelling, etc.
  * **TRANSFER** transfer permission is used for transfer interfaces, user can transfer between sub-accounts under the same main trading account.

* Users can set IP whitelist for API-KEY. If user set IP for the API-KEY, only the IPs in the whitelist can call the API. Each API-KEY will be bound to a maximum of 5 IPs. If the user has multiple  API-KEYs, they have to set IP whitelist for each API-KEY respectively.

* Both REST and WebSocket modes require users to authenticate the transaction through the API-KEY. Refer to the following chapters for the signature algorithm of the API-KEY..

### 1.1.2 Access Preparation

Before making a transaction, users have to query the server information to ensure that the program is in the correct state:

* Users have to query the server time to ensure that the local time and the server time are consistent
* Users need to query the version number to ensure that the version number is included in each request header. The request may be rejected if the version number is incorrect.

## 1.2 Signature Authentication

### 1.2.1 Signature

API requests are likely to be tampered during transmission through the internet. To ensure that the request remains unchanged, all private interfaces other than public interfaces (basic information, market data) must be verified by signature authentication via API-KEY to make sure the parameters or configurations are unchanged during transmission. Each created API-KEY need to be assigned with appropriate permissions in order to access the corresponding interface. Before using the interface, users is required to check the permission type for each interface and confirm there is appropriate permissions.
All HTTP requests to API endpoints require authentication and authorization. Users can obtain x-access-key and x-access-secret  by creating an API key flow. x-access-key and x-access-secret are used to verify and authorize all requests. The following headers should be added to all HTTP requests:

| Key                | Value                  | Description                                                                                                |
| ------------------ |------------------------|------------------------------------------------------------------------------------------------------------|
| x-access-key       | < API-KEY >            | The API Access Key you applied for                                                                         |
| x-access-sign      | < signatureOfRequest > | The value calculated by the hash value from request to ensure that the signature is valid and not tampered |
| x-access-timestamp | < timeOfRequest >      | The timestamp represents the time of request (in milliseconds)                                             |
| x-access-version   | < versionOfRequest >   | Signature protocol version.                                                       |
| Content-Type       | application/json       | Content-Type                                                                                               |

### 1.2.2 Signature Procedures

**Example:**
* The request is in a Map format and is serialized into a Json string. The map requires at least 3 keys: x-access-key, x-access-timestamp, x-access-version, include all columns in body when HTTP method is POST, include all columns in params where HTTP method is GET or DELETE. The example below illustrates how to sign a map.

```java
/*
  *Signature description：required fields for Signature include apiKey, apiSecret, timestamp, version, interface fields of each request.
  *field name and field value are in the form of key-value, and the Key is sorted by ASCII code.
  *The Following is test data demo:
*/

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.util.Base64;
import java.util.TreeMap;
import com.alibaba.fastjson.JSONObject;
import org.apache.commons.codec.binary.Hex;

public class SignDemo {

    public static void main(String[] args) throws Exception {
        String key="84dd8e670471a888e3a7547e120886cb";
        String secret = "3211b4306fcb1d9670cbee5abc69dead";
        String timeOfRequest ="1478692862000";

        TreeMap<String,String> treeMap = new TreeMap<>();

        treeMap.put("x-access-key",key); //api-key
        treeMap.put("x-access-timestamp",timeOfRequest); //current timestamp
        treeMap.put("x-access-version","v1.0");

        treeMap.put("feild1","1");//request field mock1
        treeMap.put("feild2","2");//request field mock2
        treeMap.put("feild3","3");//request field mock3

        String requestText = JSONObject.toJSONString(treeMap);
        //Sort by ASCII of Map key {"feild1":"1","feild2":"2","feild3":"3","x-access-key":"84dd8e670471a888e3a7547e120886cb","x-access-timestamp":"1478692862000","x-access-version":"1"}

        System.out.println(createSignature(requestText,secret));
        //cVfsAceIN7w+3vDf4WEIpA+iWJnK2TjKcmwgVARi8DI=
    }

    private static String createSignature(String requestText,String secret)
            throws Exception {
        return Base64.getEncoder().encodeToString(hmacSha1(requestText, secret));
    }

    private static byte[] hmacSha1(String plainData, String secret)
            throws Exception{
        Mac mac = Mac.getInstance("HmacSHA256");
        SecretKeySpec secretKey =
                new SecretKeySpec(Hex.decodeHex(secret.toCharArray()), "HmacSHA256");
        mac.init(secretKey);
        return mac.doFinal(plainData.getBytes());
    }
}
```

## 1.2 Environment

### 1.2.1 Testing Environment

Restful URL: <https://api-pro-sim.hashkey.com>

WebSocket: wss://api-pro-sim.hashkey.com

### 1.2.2 Production Environment

**Note:** Not public access, application needed

Restful URL: <https://api-pro.hashkey.com>

WebSocket: wss://api-pro.hashkey.com

# 2. REST API

## 2.1 Access

### 2.1.1 REST API Rate Limit
* Unless specified, each API Key has a rate limit of 10 requests per second. For instance, order-related endpoints have a rate limit of 10 requests per second.
* Unless specified, each IP has a rate limit of 10 requests per second.

### 2.1.2 Request Format

All API requests are under RESTful framework. Parameters can be set and sent by the request body in JSON format.

### 2.1.3 Response Format

All endpoints are in JSON standard format.  There are three fields, namely  **error_code**, **error_message**, and **data**. These specific business data are contained in the field **data**.

| **PARAMETER** | **TYPE** | **DESCRIPTION**   |
| ------------- | -------- | ----------------- |
| error_code    | string   | API return status |
| error_message | string   | API error message |
| data          | Object   | API return data   |

## 2.2 Universal

### 2.2.1 Get Timestamp

**Http Request:** GET info/time

**Request Content：** null

**Response Content：**

| **PARAMETER** | **TYPE** | **DESCRIPTION**        |
| ------------- | -------- | ---------------------- |
| timestamp     | int64    | millisecond time-stamp |

**Response Example：**

```json
{
    "error_code":"0000",            // Error code
    "error_message":"",             // Error message
    "data":{
        "timestamp": 1478692862000 // Server timestamp
    }
}
```

### 2.2.2 Get API Version

**Http Request:** GET info/version

**Request Content：** null

**Response Content：**

| **PARAMETER** | **TYPE** | **DESCRIPTION** |
| ------------- | -------- | --------------- |
| version       | string   | Version No.     |

**Response Example：**

```json
{
    "error_code":"0000",        // Error code
    "error_message":"",         // Error message
    "data":{
        "version":"v1.0"        // Server version
    }
}
```

### 2.2.3 Query instruments

**Http Request:** GET info/instruments

**Request Content：** null

**Response Content：**

| **PARAMETER**           | **TYPE** | **DESCRIPTION**                                                                                                                                                    |
|-------------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| instrument_id           | string   | Instrument ID.                                                                                                                                                     |
| base_asset              | string   | Base  Asset.                                                                                                                                                       |
| quote_asset             | string   | Quote Asset.                                                                                                                                                       |
| product_type            | string   | Product Type(Token/Token:digital assets exchange, Token/Fiat:exchange digital assets to fiat currency, ST/Token:exchange ST to digital assets, ST/Fiat:exchange ST to fiat currency) |
| price_tick              | string    | Price tick.                                                                                                                                                        |
| max_market_order_volume | string    | Max market order volume.                                                                                                                                           |
| min_market_order_volume | string    | Min market order volume.                                                                                                                                           |
| max_limit_order_volume  | string    | Max limit order volume.                                                                                                                                            |
| min_limit_order_volume  | string    | Min limit order volume.                                                                                                                                            |

**Response Example：**

```json
{
  "error_code":"0000",        
  "error_message":"",         
  "data":[{
    "instrument_id":"BTC-ETH",                 
    "base_asset":"BTC",                        
    "quote_asset":"ETH",                      
    "product_type": "Token/Token",
    "price_tick": "0.00000001",                
    "max_market_order_volume": "10000000.1",   
    "min_market_order_volume": "0.00000001",   
    "max_limit_order_volume": "10000000.1",    
    "min_limit_order_volume": "0.00000001"
  }]
}
```

### 2.2.4 Query instrument status

**Http Request:** GET info/instrument_status/{:instrument_id}
* instrument_id is required in the above url

**Request example：**

```context
 GET "https://domain/info/instrument_status/ETH-BTC"
```

**Response Content：**

| **PARAMETER** | **TYPE** | **DESCRIPTION**                                                                                                 |
|---------------|----------|-----------------------------------------------------------------------------------------------------------------|
| instrument_id | string   | Instrument ID.                                                                                                  |
| status        | string   | Status  "BeforeTrading"、"NoTrading"、"Continuous"、"AuctionOrdering"、 "AuctionBalance"、 "AuctionMatch"、"Closed"   |

| instrument status       | description        |
|-------------------------|--------------------|
| BeforeTrading           | Before trading     |
| NoTrading               | No trading         |
| Continuous              | Continuous trading |
| AuctionOrdering         | Auction ordering   |
| AuctionBalance          | Auction balance    |
| AuctionMatch            | Auction match      |
| Closed                  | Closed             |

**Response Example：**

```json
{
  "error_code":"0000",       
  "error_message":"",       
  "data":[{
    "instrument_id":"ETH-BTC",          
    "status":"Continuous"                          
  }]
}
```

## 2.3 Trading

### 2.3.1 Create An Order(TRADE permission is required)

**Http Request:** POST /order

**Request Content：**

| **PARAMETER**   | **TYPE** | **REQUIRED**                                                  | **DESCRIPTION**                                                                                              |
| --------------- | -------- |---------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| type            | string   | true                                                          | "limit": limit order; "market": market order; "stopLimit": stop limit order; "stopMarket": stop market order |
| client_order_id | string   | true                                                          | Max length: 20. Must be unique                                                                               |
| instrument_id   | string   | true                                                          | e.g. "ETH-BTC"                                                                                               |
| direction       | string   | true                                                          | "buy" or "sell"                                                                                              |
| stop_price      | string   | false                                                         | Required when order type is stopLimit or stopMarket                                                          |
| price           | string   | false                                                         | Limit price. Required when order type is limit or stopLimit                                                  |
| volume          | string   | true                                                          | Total Volume                                                                                                 |
| post_only       | bool     | false                                                         | Only maker  default false                                                                                           |
| time_in_force (currently unused) | string   | default: limit and stopLimit: GTC, market and stopMarket: IOC |

 **Response Content：**

| **PARAMETER**   | **TYPE** | **DESCRIPTION**                                                                                              |
| --------------- | -------- |--------------------------------------------------------------------------------------------------------------|
| type            | string   | "limit": limit order; "market": market order; "stopLimit": stop limit order; "stopMarket": stop market order |
| sys_order_id    | string   | Server order id.                                                                                             |
| client_order_id | string   | Client order id.                                                                                             |
| instrument_id   | string   | e.g. "ETH-BTC"                                                                                               |
| direction       | string   | "buy" or "sell"                                                                                              |
| stop_price      | string   | Required when order type is stopLimit or stopMarket                                                          |
| price           | string   | Limit Price. Required when order type is limit or stopLimit                                                  |
| volume          | string   | Total Volume                                                                                                 |
| post_only       | bool     | Only maker                                                                                                   |
| timestamp       | int64    | millisecond time-stamp                                                                                       |
| time_in_force (currently unused) | string   | default: limit and stopLimit: GTC, market and stopMarket: IOC                                                |

**Request Example：**

```json
{
    "type": "limit",                    // Order type:
    "client_order_id":"000000001",      // Client order ID
    "instrument_id":"ETH-BTC",          // Instrument ID
    "direction":"buy",                  // Trade direction: buy、sell
    "price":"1",                        // Limit price
    "volume":"1",                       // Total Volume
    "post_only": true                   // Whether to only be a maker
}
```

**Response Example：**

```json
{
    "error_code":"0000",    // Errorcode
    "error_message":"",     // Errormessage
    "data":{
        "type":"limit",                // Order type
        "sys_order_id":"1550849345000001",     // System order ID
        "client_order_id":"000000001",  // Client order ID
        "instrument_id":"ETH-BTC",      // Instrument ID
        "direction":"buy",              // Trade direction
        "stop_price": "0",              // Stop price
        "price":"1",                    // Limit price
        "volume":"1",                   // Total Volume
        "post_only": true,              // Whether to only be a maker
        "timestamp": 1478692862000      // Order timestamp
    }
}
```

### 2.3.2 Cancel An Order(TRADE permission is required)

**Http Request:** DELETE /order/

**Query Parameters：**

| **PARAMETER**   | **TYPE**   | **REQUIRED**  | **DESCRIPTION**                                         |
|-----------------|------------|---------------|---------------------------------------------------------|
| sys_order_id    | string     | false         | This filed is required when client_order_id is null     |
| client_order_id | string     | false         | This filed is required when sys_order_id is null        |
| volume          | string     | false         | If it is not input, the whole order will be cancelled   |
Note: If neither sys_order_id nor client_order_id is empty, then client_order_id is ignored.

**Response Content：**
null

**Request example：**

```context
 DELETE "https://domain/order?&sys_order_id=1550849345000001"
```
**Response Example：**

```json
{
  "error_code":"0000",    // 错误码
  "error_message":""      // 错误描述
}
```

### 2.3.3 Cancel all orders（TRADE permission is required）

**Http Request:** DELETE /orders

**Query Parameters：**

| **PARAMETER** | **TYPE**   | **REQUIRED** | **DESCRIPTION**                         |
|------------|------------|--------------|-----------------------------------------|
| instrument_id       | string     | false        | Cancel orders on a specific instrument_id only |


**Response Content：**
null

**Request example：**

```context
 DELETE "https://domain/orders?instrument_id=BTC-ETH"
```

**Response Example：**

```json
{
    "error_code":"0000",    // Error code
    "error_message":""     // Error message
}
```

### 2.3.4 Get Order Data(READ permission is required)

**Http Request:**  GET /orders

**Query Parameters：**

| **PARAMETER**   | **TYPE**     | **REQUIRED** | **DESCRIPTION**                                              |
|-----------------| ------------ |--------------|--------------------------------------------------------------|
| sys_order_id    | string       | false        | Server Order ID                                              |
| instrument_id   | string       | false        | e.g. "ETH-BTC"                                               |
| sorting         | string       | false        | "desc" or "asc"  default "asc"                                 |
| direction       | string       | false        | "buy" or "sell"                                              |
| type            | string       | false        | Order type                                                   |
| status          | array string | false        | Array with order statuses to filter by.                      |
| start_timestamp | string        | true         | millisecond time-stamp                                       |
| end_timestamp   | string        | true         | millisecond time-stamp                                       |
| limit           | string        | true        | Limit on number of results to return. min 1 max 200. |
| page            | string        | true         | Used for pagination. Page number.                            |

**Response Content：**

| **PARAMETER**     | **TYPE** | **DESCRIPTION**                                                                                              |
|-------------------| -------- |--------------------------------------------------------------------------------------------------------------|
| type              | string   | "limit": limit order; "market": market order; "stopLimit": stop limit order; "stopMarket": stop market order |
| sys_order_id      | string   | Server Order ID                                                                                              |
| client_order_id   | string | Client order id.                                                                                             |
| instrument_id     | string   | e.g. "ETH-BTC"                                                                                               |
| direction         | string   | "buy" or "sell"                                                                                              |
| stop_price        | string   | Required when order type is stopLimit or stopMarket                                                          |
| price             | string   | Limit Price. Required when order type is limit or stopLimit                                                  |
| volume            | string   | Original Total Volume                                                                                        |
| status            | string   | Order status                                                                                                 |
| post_only         | bool     | Only maker                                                                                                   |
| timestamp         | int64    | millisecond time-stamp                                                                                       |
| filled_size       | string   | The size that has been filled                                                                                |
| unfilled_size     | string   | The size that has not been filled                                                                            |
| avg_filled_price  | string   | Average filled price                                                                                         |
| sum_trade_amount | string   | cumulative trading amount(turnover)                                                                          |

**Order status**

| order status               | description                                                                            |
|----------------------------|----------------------------------------------------------------------------------------|
| -------------------------- | ------------------------------------------------------------                           |
| NEW                        | The order has been accepted by the engine                                              |
| FILLED                     | The order has been completed                                                           |
| PARTIALLY_FILLED           | A part of the order has been filled, and the rest remains in the order book            |
| CANCELED                   | The order has been canceled by the user, whitout any trade                             |
| PARTIALLY_CANCELED         | A part of the order has been filled, and the  remaining part has been canceled by user |
| NOT_TRIGGERED              | The Stop order  is not triggered                                                       |
| REJECTED                   | The order was not accepted by the engine and not processed. (Currently not enabled)    |

**Request Example：**

```context
 GET "http://domain/orders?sys_order_id=1550849345000001&instrument_id=ETH-BTC&start_timestamp=1656928657000&end_timestamp=1656928717000&limit=50&page=1"
```

**Response Example：**

```json
{
    "error_code":"0000",    // Error code
    "error_message":"",     // Error message
    "data":[{
        "type": "limit",                // Order type
        "sys_order_id":"1550849345000001",     // System order ID
        "client_order_id":"000000001",  // Client order ID
        "instrument_id":"ETH-BTC",      // InstrumentID
        "direction":"buy",              // Trade direction
        "stop_price":"0",               // Stop price
        "price":"1",                    // Limit Price
        "volume":"1",                   // Original Total Volume
        "status": "FILLED",             // Order status
        "post_only": false,             // Only as "maker"
        "timestamp": 1478692862000,     // Order timestamp
        "filled_size": "1",             // The size that has been filled
        "avg_filled_price": "1",        // Average filled price
        "unfilled_size": "0",           // The size that has not been filled
        "sum_trade_amount": "1"         // turnover
    }]
}
```

### 2.3.5 Retrieve Trade Data(READ permission is required)

**Http Request:** GET /trades

**Query Parameters** **:**

| **PARAMETER**   | **TYPE** | **REQUIRED** | **DESCRIPTION**                                              |
|-----------------| -------- |--------------|--------------------------------------------------------------|
| instrument_id   | string   | false        | e.g. "ETH-BTC"                                               |
| sys_order_id    | string   | false        | Server Order ID                                              |
| direction       | string   | false        | "buy" or "sell"                                              |
| sorting         | string   | false        | "desc" or "asc"    default "asc"                               |
| limit           | string    | true        | Limit on number of results to return. min 1 max 200. |
| page            | string    | true         | Used for pagination. Page number.                            |
| start_timestamp | string    | true         | millisecond time-stamp                                       |
| end_timestamp   | string    | true         | millisecond time-stamp                                       |

 **Response Content:**

| **PARAMETER** | **TYPE** | **DESCRIPTION**        |
| ------------- | -------- |------------------------|
| trade_id      | string   | Trade ID               |
| sys_order_id  | string   | Order ID               |
| instrument_id | string   | e.g. "ETH-BTC"         |
| direction     | string   | "buy" or "sell"        |
| price         | string   | Price                  |
| volume        | string   | Volume                 |
| fee           | string   | Fee                    |
| fee_ccy       | string   | Fee Currency           |
| timestamp     | int64    | millisecond time-stamp |
| trade_type    | string   | "Common", "Invalid"    |

**Trade Type**

| Trade type         | description |
|--------------------|-------------|
| Common             | Common Trade        |
| Invalid            |  Invalid Trade        |


**Request Example:**

```context
 GET "http://domain/trades?sys_order_id=1550849345000001&instrument_id=ETH-BTC&start_timestamp=1656928657000&end_timestamp=1656928717000&limit=50&page=1"
```

**Response Example：**

```json
{
    "error_code":"0000",    // Error code
    "error_message":"",     // Error message
    "data":[{
        "sys_order_id":"1550849345000001",     // System order ID
        "trade_id":"1",                 // Trade ID
        "instrument_id":"ETH-BTC",      // Instrument ID
        "direction":"buy",              // Trade direction
        "price":"1",                    // Price
        "volume":"1",                   // Volume
        "fee":"0.05",                   // Transaction Fee
        "fee_ccy": "BTC",              // Transaction Fee currency
        "timestamp": 1478692862000,      // Trade timestamp
        "trade_type": "Common"          // Trade type
    }]
}
```

## 2.4 Asset

### 2.4.1 Query assets(READ permission is required)

**Http Request:** GET /assets

**Request Content：** null

**Response Content：**

| **PARAMETER** | **TYPE** | **DESCRIPTION**        |
| ------------- | -------- | ---------------------- |
| asset         | string   | Asset type, e.g. "BTC" |
| free          | string   | Avalible balance       |
| freeze        | string   | Frozen balance         |

**Response Example：**

```json
{
    "error_code":"0000",
    "error_message":"",
    "data":[{
        "asset":"ETH",
        "free": "1",
        "freeze": "0",
    }, {
        // other asset
    }]
}
```

### 2.4.2 Transfer between trading accounts(TRANSFER permission is required)

**Http Request:** POST /assets/transfer

**Request Content：**

| **PARAMETER**   | **TYPE** | **REQUIRED** | **DESCRIPTION** |
|-----------------| -------- | ------------ |-----------------|
| asset           | string   | true         | Asset ID        |
| amount          | string   | true         | Amount          |
| to_account_id   | string   | true         | To Account ID   |
| from_account_id | string   | true         | From Account ID |

**Response Content：**

| **PARAMETER** | **TYPE** | **REQUIRED** | **DESCRIPTION** |
| ------------- | -------- | ------------ | --------------- |
| error_code    | string   | true         | Error Code      |
| error_message | string   | true         | Error Message   |
| data          | string   | true         | Data            |

**Request Example：**

```json
{
    "asset":"ETH",
    "amount":"1",
    "from_account_id": "B000000000001",
    "to_account_id":"B000000000002"
}
```

**Response Example：**

```json
{
    "error_code":"0000",
    "error_message":"",
    "data":{}
}

```

### 2.4.3 Query withdrawal history（READ permission is required）

**Http Request:** GET /withdraw/history

**Query Parameters** **:**

| **PARAMETER**     | **TYPE** | **REQUIRED** | **DESCRIPTION**                                            |
|-------------------| -------- |--------------|------------------------------------------------------------|
| currency          | string   | false        | Currency                                            |
| status            | string   | false        | Status   "failed"、"withdrawing"、"successful"、"cancelling"、"cancelled"              |
| limit             | string    | true         | Limit on number of results to return. min 1 max 200 |
| page              | string    | true         | Used for pagination. Page number.                          |
| start_timestamp   | string    | true         | millisecond time-stamp                                     |
| end_timestamp     | string    | true         | millisecond time-stamp                                     |


**Response Content：**

| **PARAMETER**     | **TYPE** | **DESCRIPTION**                |
|-------------------|----------|--------------------------------|
| withdraw_order_id | string   | withdraw order ID              |
| txn_id            | string   | Txn ID                         |
| network           | string   | Network (currently unused)     |
| currency          | string   | Currency                       |
| address           | string   | Withdrawal destination address |
| memo              | string   | Memo                           |
| volume            | string   | Volume                         |
| status            | string   | Status                         |
| gas_fee           | string   | Gas Fee                        |
| gas_fee_ccy       | string   | Gas Fee Currency               |
| fee               | string   | Fee                            |
| fee_ccy           | string   | Fee Currency                   |
| timestamp         | int64    | Timestamp                      |

**Request example：**

```context
 GET "https://domain/withdraw/history?currency=BTC&start_timestamp=1656928657000&end_timestamp=1656928717000&limit=50&page=1"
```


**Response Example：**

```json
{
  "error_code":"0000",
  "error_message":"",
  "data":[{
    "withdraw_order_id": "00000001",
    "txn_id": "60fd9007ebfddc753455f95fafa808c4302c836e4d1eebc5a132c36c1d8ac354",
    "currency": "BTC",
    "address": "1FZdVHtiBqMrWdjPyRPULCUceZPJ2WLCsB",
    "memo": "",
    "volume": "1",
    "status": "successful",
    "fee": "0.004",
    "fee_ccy": "BTC",
    "gas_fee": "0.0001",
    "gas_fee_ccy": "BTC",
    "timestamp": 1478692862000
  }]
}
```

### 2.4.4 Query deposit history（READ permission is required）

**Http Request:** GET /deposit/history

**Query Parameters** **:**

| **PARAMETER**     | **TYPE** | **REQUIRED** | **DESCRIPTION**                                            |
|-------------------| -------- |--------------|------------------------------------------------------------|
| currency          | string   | false        | Currency                                                                                          |
| status           | string    | false        | Status  "addressToBeVerified"、"underReview"、"successful"、"failed"、"refundInProgress"、"refundComplete"、"refundFailed" |
| page              | string    | true         | Used for pagination. Page number.                   |
| limit             | string    | true        | Limit on number of results to return. min 1 max 200 |
| start_timestamp   | string    | true         | millisecond time-stamp                                     |
| end_timestamp     | string    | true         | millisecond time-stamp                                     |


**Response Content：**

| **PARAMETER**    | **TYPE** | **DESCRIPTION**            |
|------------------|----------|----------------------------|
| deposit_order_id | string   | Deposit order ID           |
| txn_id           | string   | Txn ID                     |
| network           | string   | Network (currently unused) |
| currency         | string   | Currency                   |
| address          | string   | Deposit source address     |
| memo             | string   | Memo                       |
| volume           | string   | Volume                     |
| status           | string   | Status                     |
| fee              | string   | Fee                        |
| fee_ccy          | string   | Fee Currency               |
| timestamp        | int64    | Timestamp                  |

**Request example：**

```context
 GET "https://domain/deposit/history?currency=BTC&start_timestamp=1656928657000&end_timestamp=1656928717000&limit=50&page=1"
```

**Response Example：**

```json
{
  "error_code":"0000",
  "error_message":"",
  "data":[{
    "deposit_order_id": "00000001",
    "txn_id": "60fd9007ebfddc753455f95fafa808c4302c836e4d1eebc5a132c36c1d8ac354",
    "currency": "BTC",
    "address": "1FZdVHtiBqMrWdjPyRPULCUceZPJ2WLCsB",
    "memo": "",
    "volume": "1",
    "status": "successful",
    "fee": "0.004",
    "fee_ccy": "BTC",
    "timestamp": 1478692862000
  }]
}
```

### 2.4.5 Query assets transfer history（READ permission is required）

**Http Request:** GET /assets/transfer/history

**Query Parameters** **:**

| **PARAMETER**     | **TYPE** | **REQUIRED** | **DESCRIPTION**                                            |
|-------------------| -------- |--------------|------------------------------------------------------------|
| start_timestamp   | string    | true         | millisecond time-stamp                                     |
| end_timestamp     | string    | true         | millisecond time-stamp                                     |
| limit             | string    | true        | Limit on number of results to return. min 1 max 200 |
| page              | string    | true         | Used for pagination. Page number.                          |

**Response Content：**

| **PARAMETER**    | **TYPE** | **DESCRIPTION**    |
|------------------|----------|--------------------|
| asset           | string   | Asset ID           |
| amount          | string   | Amount             |
| from_account_id | string   | From Account ID    |
| to_account_id   | string   | To Account ID      |
| status          | string   | "successful", "failed" |
| timestamp       | int64    | Timestamp          |


**Request example：**

```context
 GET "https://domain/assets/transfer/history?start_timestamp=1656928657000&end_timestamp=1656928717000&limit=50&page=1"
```

**Response Example：**

```json
{
    "error_code":"0000",
    "error_message":"",
    "data":[{
      "asset":"ETH",
      "amount":"1",
      "from_account_id": "B000000000001",
      "to_account_id":"B000000000002",
      "status": "successful",
      "timestamp": 1478692862000
    }]
}
```

## 2.5 Market

### 2.5.1 Get Kline

**Http Request:** GET market/kline

**Query Parameters：**

| **PARAMETER**    | **TYPE** | **REQUIRED** | **DESCRIPTION**                                                                                                                                                     |
|------------------|----------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| instrument_id    | string   | true         | e.g. "ETH-BTC"                                                                                                                                                      |
| period           | string   | true         | m -> minutes; h -> hours; d -> days; w -> weeks; M -> months;<br/> "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h",<br/> "6h", "8h", "12h", "1d", "3d", "1w", "1M" |
| start_timestamp  | string   | true         | millisecond time-stamp  start from 000 milliseconds of this period                                                                                                  |
| end_timestamp    | string   | true         | millisecond time-stamp  end at 000 milliseconds of the next period                                                                                                  |
| page             | string   | true         | Used for pagination. Page number.                   |
| limit            | string   | true         | min 1 max 200                                                                                                                                                       |

**Response Content：**

| **PARAMETER**   | **TYPE** | **DESCRIPTION**        |
|-----------------| -------- | ---------------------- |
| instrument_id   | string   | e.g. "ETH-BTC"               |
| open            | string   | Open Price                   |
| close           | string   | Close Price                  |
| high            | string   | High Price                   |
| low             | string   | Low Price                    |
| volume          | string   | Volume in base asset, e.g, ETH in ETH-BTC |
| start_timestamp | int64    | Start millisecond time-stamp |
| end_timestamp   | int64    | End millisecond time-stamp   |

**Response Example：**

```json
{
    "error_code":"0000",    // Error code
    "error_message":"",     // Error message
    "data":[
        {
            "instrument_id":"ETH-BTC",      // Instrument ID
            "open":"10",                    // Open price
            "close":"10",                   // Close price
            "high":"10",                    // High price
            "low":"10",                     // Low price
            "volume":"100",                 // Volume
            "start_timestamp":1646213700000,     // Start time
            "end_timestamp":1646213760000        // End time
        }
    ]
}
```

### 2.5.2 Get Trade List

**Http Request:** GET /trades/market

**Query Parameters：**

| **PARAMETER**   | **TYPE** | **REQUIRED** | **DESCRIPTION**                   |
|-----------------|----------|--------------|-----------------------------------|
| instrument_id   | string   | false        | e.g. "ETH-BTC"                    |
| start_timestamp | string    | true         | millisecond time-stamp            |
| end_timestamp   | string    | true         | millisecond time-stamp            |
| limit           | string    | true        | min 1 max 200.          |
| page            | string    | true         | Used for pagination. Page number. |

**Response Content：**

| **PARAMETER** | **TYPE** | **DESCRIPTION**  |
| ------------- | -------- | ---------------- |
| instrument_id | string   | e.g. "ETH-BTC"   |
| trade_id      | string   | Trade ID         |
| price         | string   | Price            |
| volume        | string   | Volume           |
| timestamp     | int64    | millisecond time-stamp |
| direction     | string   | Taker direction        |

**Response Example：**

```json
{
    "error_code":"0000",    // Error code
    "error_message":"",     // Error message
    "data":[
        {
            "instrument_id": "ETH-BTC",     // Instrument ID
            "trade_id": "123456789",        // Trade ID
            "price": "10",                  // Price
            "volume": "100",                // Volume
            "timestamp": 1478692862000      // Trade timestamp
            "direction": "buy"              // Taker direction
        }
    ]
}
```

# 3. Websocket API

## 3.1 Access

### 3.1.1 WebSocket API session Limit
* Use apikey to authorize websocket sessions, and 10 sessions can be authorized at the same time.
* Only authorized sessions can subscribe to private data and public data.

**URL for Access:**
 /stream

### 3.1.2 Heartbeat Message

When user's Websocket client application gets connected with the HashKey Websocket server, the server will periodically (every 10 seconds currently) send a ping message containing the sessionID and current timestamp.

```json
 {"type":"ping","sessionID":"74939a43-0523-4cb1-a870-0dbadfda6a62","data":"1492420473027"}
```

When the user receives the mentioned message from the Websocket client application, a pong message containing the same timestamp should be returned.

```json
{"type":"pong","data":"1492420473027"}
```

**Note**: When the Websocket server sends two ping messages successively but gets no pong message in return, the connection will be disconnected.

### 3.1.3 Request Format

All subscription request bodies are expected to be in valid JSON format. Each topic has its own parameter set. For details, please refer to the endpoint request example.

### 3.1.4 Response Format

All response bodies are expected to be in valid JSON format.  For details, please refer to the endpoint response example.

### 3.1.5 Authentication

**Request Content:**

| **PARAMETER**      | **TYPE** | **REQUIRED** | **DESCRIPTION**                                                                          |
| ------------------ |----------| ------------ |------------------------------------------------------------------------------------------|
| type               | string   | true         | Default: auth                                                                            |
| x-access-key       | string   | true         | The API Access Key you applied for.                                                      |
| x-access-sign      | string   | true         | A value calculated by the hash value from request to ensure it is valid and not tampered. |
| x-access-timestamp | string   | true         | The timestamp represents the time of request (in milliseconds).                          |
| x-access-version   | string   | true         | Signature protocol version. Default version is 1.                                        |

**Request Example：**

 ```json
{
    "type":"auth",
    "auth":{
        "x-access-key":"xxxxxxxxx",
        "x-access-sign":"xxxxxxxxx",
        "x-access-timestamp": "1478692862000",
        "x-access-version":"v1.0"
    },
    "id": 1
}
 ```

**Response Example：**

```json
{
    "type":"auth-resp",
    "error_code": "0000",
    "error_message": "success"
}
```

### 3.1.6 Subscribe

**Request Content:**

| **PARAMETER** | **TYPE**     | **REQUIRED** | **DESCRIPTION**      |
|---------------| ------------ | ------------ |----------------------|
| type          | string       | true         | "sub"                |
| id            | integer      | true         | Unique request id    |
| parameters    | object array | true         | Subscribe parameters |
| => topic      | string       | true         | Topic                |

**Response Content:**

| **PARAMETER** | **TYPE**     | **DESCRIPTION**                                |
| ------------- | ------------ |------------------------------------------------|
| id            | integer      | Unique request id                              |
| result        | object array | Topic list                                     |
| error_code    | string       | 0000: success 0100: partial success 0001: fail |

**Request Example:**

```json
{
    "type": "sub",            // Message type, sub: subscribe
    "parameters":[{
        "topic":"order_rtn",            // Subscribe topoic
        "instrument_id":"ETH-USDT"      // Instrument ID
    }],
    "id": 1                             // Message ID
}
```

**Response Example:**

```json
{
    "id": 1,                          // Message ID
    "result": null,                   // Result is null when all topics are successfully subscribed; otherwise, it returns the topics that are successfully subscribed
    "error_code": "0000"              // Error code is 0000 when all topics are successfully subscribed; otherwise, it returns the error code that unsuccessfully subscribed
}
```

### 3.1.7 Unsubscribe

**Request Content:**

| **PARAMETER** | **TYPE**     | **REQUIRED** | **DESCRIPTION**        |
|---------------|--------------| ------------ |------------------------|
| type          | string       | true         | "unsub"                |
| id            | int64        | true         | Unique request id      |
| parameters    | object array | true         | Unsubscribe parameters |
| => topic      | string       | true         | Topic                  |
| error_code    | string       | true         | Error code             |
| error_message | string       | true         | Explain error info     |

**Response Content:**

| **PARAMETER** | **TYPE**     | **DESCRIPTION**                                |
| ------------- |--------------|------------------------------------------------|
| id            | int64        | Unique request id                              |
| result        | object array | Topic list                                     |
| error_code    | string       | 0000: success 0100: partial success 0001: fail |

**Request Example:**

 ```json
{
    "type":"unsub",
    "parameters":  [{
        "topic":"xxxxxxxxx",
        ......
    }],
    "id": 2
}
 ```

**Response Example:**

```json
{
    "id": 1,
    "result": null,
    "error_code": "0000"
}
```



## 3.2 Market Data (Public stream)

### 3.2.1 Kline

**Push Frequency**
Push every 1000 milliseconds

**Request Content:**

| **PARAMETER** | **TYPE** | **REQUIRED** | **DESCRIPTION**                                              |
| ------------- | -------- | ------------ | ------------------------------------------------------------ |
| type          | string   | true         | "sub"                                                        |
| topic         | string   | true         | "kline"                                                      |
| period        | string   | true         | m -> minutes; h -> hours; d -> days; w -> weeks; M -> months;<br/> "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h",<br/> "6h", "8h", "12h", "1d", "3d", "1w", "1M" |
| instrument_id | string   | true         | e.g. "ETH-USDT", "ETH-BTC"                                   |

**Response Content:**

| **PARAMETER** | **TYPE** | **DESCRIPTION**                               |
| ------------- | -------- | --------------------------------------------- |
| type          | string   | "sub-resp"                                    |
| topic         | string   | "kline"                                       |

**Data Content:**

| **PARAMETER**   | **TYPE** | **DESCRIPTION**                               |
|-----------------| -------- | --------------------------------------------- |
| instrument_id   | string   | e.g. "ETH-USDT", "ETH-BTC"                    |
| high            | string   | High  price                                   |
| open            | string   | Open price                                    |
| low             | string   | Low  price                                    |
| close           | string   | Close  price                                  |
| volume          | string   | Volume in base asset, e.g, ETH in ETH-BTC     |
| start_timestamp | int64    | millisecond time-stamp     e.g. 1646213700000 |
| end_timestamp   | int64    | millisecond time-stamp     e.g. 1646213800000 |

**How to Subscribe：**

```json
{
    "type":"sub",                       // Message type
    "parameters":[{
        "topic":"kline",                // Subscribe topoic(kline)
        "period":"1m",                  // Time period
        "instrument_id":"ETH-USDT"      // Instrument ID
    }],
    "id": 1                             // Message ID
}
```

**Response Example：**

```json
{
    "type":"sub-resp",                      // Message type
    "topic":"kline",                        // Subscribe topoic
    "data":{
            "instrument_id":"ETH-BTC",      // Instrument ID
            "open":"10",                    // Open price
            "close":"10",                   // Close price
            "high":"10",                    // Highest price
            "low":"10",                     // Lowest price
            "volume":"100",                 // Volume in base asset
            "start_timestamp":1646213700000,     // Start time
            "end_timestamp":1646213760000        // End time
    }
}
```

### 3.2.2 Market Data

**Push frequency**
Push every 1000 milliseconds

**Request Content:**

| **PARAMETER** | **TYPE** | **REQUIRED** | **DESCRIPTION**            |
| ------------- | -------- | ------------ | -------------------------- |
| type          | string   | true         | "sub"                      |
| topic         | string   | true         | "market_data"              |
| instrument_id | string   | true         | e.g. "ETH-USDT", "ETH-BTC" |

**Response Content:**

| **PARAMETER**        | **TYPE** | **DESCRIPTION**        |
| -------------------- | -------- | ---------------------- |
| type                 | string   | "sub-resp"             |
| topic                | string   | "market_data"          |

**Data Content:**

| **PARAMETER**        | **TYPE** | **DESCRIPTION**                           |
|----------------------| -------- |-------------------------------------------|
| high                 | string   | High price                                |
| low                  | string   | Low price                                 |
| open                 | string   | Open price                                |
| instrument_id        | string   | e.g. "ETH-USDT", "ETH-BTC"                |
| base                 | string   | Base asset, e.g, ETH in ETH-BTC           |
| quote                | string   | Quote asset, e.g, BTC in ETH-BTC          |
| last_price           | string   | Price of the latest trade                 |
| price_change_rate    | string   | Price change rate of 24 hours             |
| price_change         | string   | Price change  of 24 hours                 |
| volume               | string   | Volume in base asset, e.g, ETH in ETH-BTC |

**How to Subscribe：**

```json
{
    "type":"sub",                           // Message type
    "parameters":[{
        "topic":"market_data",              // Subscribe topoic
        "instrument_id":"ETH-USDT"          // Instrument ID
    }],
    "id": 1                                 // Message ID
}
```

**Response Example：**

```json
{
    "type":"sub-resp",                  // Message type: sub-resp: Subscription results
    "topic":"market_data",              // Subscribe topic
    "data":[
        {
            "open":"0",                 // Open price
            "high":"0",                 // Highest price
            "low":"0",                  // Lowest price
            "base":"ETH",               // Base asset
            "quote":"USDT",             // Quote asset
            "instrument_id":"ETH-USDT", // Instrument ID
            "price_change_rate":"0",    // Price change rate of 24 hours
            "price_change":"0",         // Price change rate of 24 hours
            "last_price":"0",           // Price of the latest trade
            "volume":"0"                // Volume of 24 hours
        }
    ]
}
```

### 3.2.3 Order book Data

**Push frequency**
Push every 500 milliseconds(If there is any change)

**Request Content:**

| **PARAMETER** | **TYPE** | **REQUIRED** | **DESCRIPTION**            |
| ------------- | -------- | ------------ | -------------------------- |
| type          | string   | true         | "sub"                      |
| topic         | string   | true         | "depth_market_data"        |
| instrument_id | string   | true         | e.g. "ETH-USDT", "ETH-BTC" |

**Response Content:**

| **PARAMETER** | **TYPE** | **DESCRIPTION**              |
| ------------- | -------- |------------------------------|
| type          | string   | "sub-resp"                   |
| topic         | string   | "depth_market_data"          |
| instrument_id | string   | e.g. "ETH-USDT", "ETH-BTC"   |

**Data Content:**

| **PARAMETER** | **TYPE** | **DESCRIPTION**     |
| ------------- | -------- | ------------------- |
| volume        | string   | Volume              |
| price         | string   | Price               |
| timestamp     | int64    | Timestamp       |

**How to Subscribe：**

```json
{
    "type":"sub",                           // Message type
    "parameters":[{
        "topic":"depth_market_data",        // Subscribe topoic
        "instrument_id":"ETH-USDT"          // Instrument ID
    }],
    "id": 1                                 // Message ID
}
```

**Response Example：**

```json
{
    "type":"sub-resp",                      // Message type
    "topic":"depth_market_data",            // Subscribe topoic
    "instrument_id":"ETH-USDT",
    "data":{
        "asks":[                            // Sell 50 levels, sorted from small to large according to the price
            {
                "volume":"3",               // volume
                "price":"1.7"                // price
            },
            {
                "volume":"3",
                "price":"2"
            }
        ],
        "bids":[
            {                              // Buy 50 levels, sorted from large to small according to the price
                "volume":"3",
                "price":"1.5"
            }
        ]
    },
  "timestamp": 1646213700000
}
```

### 3.2.4 Total Trade Data

**Request Content:**

| **PARAMETER** | **TYPE** | **REQUIRED** | **DESCRIPTION**            |
| ------------- | -------- |--------------|----------------------------|
| type          | string   | true         | "sub"                      |
| topic         | string   | true         | "trade_rtn_all"            |
| instrument_id | string   | false        | e.g. "ETH-USDT", "ETH-BTC" |

**Response Content:**

| **PARAMETER** | **TYPE** | **DESCRIPTION**  |
| ------------- | -------- | ---------------- |
| type          | string   | "sub-resp"       |
| topic         | string   | Topic            |


**Data Content:**

| **PARAMETER** | **TYPE** | **DESCRIPTION**        |
|---------------| -------- |------------------------|
| instrument_id | string   | Instrument Id          |
| trade_id      | string   | Trade Id               |
| volume        | string   | Volume                 |
| price         | string   | Price                  |
| timestamp     | int64x   | millisecond time-stamp |
| direction     | string   | Taker direction        |

**How to Subscribe：**

```json
{
    "type":"sub",
    "parameters":[{
        "topic":"trade_rtn_all",
        "instrument_id":"ETH-USDT"
    }],
    "id": 1
}
```

**Request Response：**

```json
{
    "type":"sub-resp",
    "topic":"trade_rtn_all",                    // Subscribe topoic
    "data":[
            {
                "instrument_id":"ETH-USDT",     // Instrument ID
                "trade_id":"1000001",           // Trade ID
                "volume":"2",                   // Volume
                "price":"2",                    // Price
                "timestamp":1478692862000,      // Trade time
                "direction": "buy"              // Taker direction
            },
            {
                "instrument_id":"ETH-USDT",
                "trade_id":"1000002",
                "volume":"2",
                "price":"2",
                "timestamp":1478692862000,
                "direction": "buy"              
            }
        ]
}
```

### 3.2.5 Instruments status change

**Request Content:**

| **PARAMETER** | **TYPE** | **REQUIRED** | **DESCRIPTION**             |
| ------------- | -------- | ------------ |-----------------------------|
| type          | string   | true         | "sub"                       |
| topic         | string   | true         | "instruments_status_change" |
| instrument_id | string   | false        | e.g. "ETH-USDT", "ETH-BTC"  |

**Response Content:**

| **PARAMETER** | **TYPE** | **DESCRIPTION**  |
| ------------- | -------- | ---------------- |
| type          | string   | "sub-resp"               |
| topic         | string   | Topic                    |

**Data Content:**

| **PARAMETER** | **TYPE** | **DESCRIPTION**        |
|---------------| -------- |------------------------|
| instrument_id | string   | Instrument Id          |
| status        | string   | Status                 |


**How to Subscribe：**

```json
{
    "type":"sub",
    "parameters":[{
        "topic":"instruments_status_change",
    }],
    "id": 1
}
```

**Request Response：**

```json
{
    "type":"sub-resp",
    "topic":"instruments_status_change",                    
    "data":[
            {
                "instrument_id":"ETH-BTC",      
                "status":""                     
            }
        ]
}
```


## 3.3  Transaction Data (Private Stream)

### 3.3.1 Order Data

**Request Content:**

| **PARAMETER** | **TYPE** | **REQUIRED** | **DESCRIPTION**            |
| ------------- | -------- | ------------ | -------------------------- |
| type          | string   | true         | "sub"                      |
| topic         | string   | true         | "order_rtn"                |
| instrument_id | string   | false        | e.g. "ETH-USDT", "ETH-BTC" |

**Response Content:**

| **PARAMETER**   | **TYPE** | **DESCRIPTION**                                              |
| --------------- | -------- | ------------------------------------------------------------ |
| type            | string   | "sub-resp"                                                   |
| topic           | string   | "order_rtn"                                                  |

**Data Content:**

| **PARAMETER**   | **TYPE** | **DESCRIPTION**                                                                                              |
| --------------- | -------- |--------------------------------------------------------------------------------------------------------------|
| type            | string   | "limit": limit order; "market": market order; "stopLimit": stop limit order; "stopMarket": stop market order |
| sys_order_id    | string   | Server Order ID                                                                                              |
| client_order_id | string   | Client order id.                                                                                             |
| instrument_id   | string   | e.g. "ETH-BTC"                                                                                               |
| direction       | string   | "buy" or "sell"                                                                                              |
| stop_price      | string   | Required when order type is stopLimit or stopMarket                                                          |
| price           | string   | Limit Price. Required when order type is limit or stopLimit                                                  |
| volume          | string   | Original Total Volume                                                                                        |
| status          | string   | Order status                                                                                                 |
| post_only       | bool     | Only maker                                                                                                   |
| timestamp       | int64    | millisecond time-stamp                                                                                       |
| filled_size     | string   | The size that has been filled                                                                                |
| unfilled_size    | string   | The size that has not been filled                                                                            |
| avg_filled_price | string   | Average filled price                                                                                         |
| sum_trade_amount | string   | cumulative trading amount(turnover)                                                                          |

**How to Subscribe：**

```json
{
    "type":"sub",
    "parameters":[{
        "topic":"order_rtn",
        "instrument_id":"ETH-USDT"
    }],
    "id": 1
}
```

**Response Example：**

```json
{
    "type":"sub-resp",
    "topic":"order_rtn",
    "data":[{
        "type": "limit",                // Order type
        "sys_order_id":"1550849345000001",     // System order ID
        "client_order_id":"000000001",  // Client order ID
        "instrument_id":"ETH-BTC",      // InstrumentID
        "direction":"buy",              // Trade direction
        "stop_price":"0",               // Stop price
        "price":"1",                    // Limit Price
        "volume":"1",                   // Original Total Volume
        "status": "FILLED",             // Order status
        "post_only": false,             // Only as "maker"
        "timestamp": 1478692862000,     // Order timestamp
        "filled_size": "1",             // The size that has been filled
        "avg_filled_price": "1",        // Average filled price
        "unfilled_size": "0",           // The size that has not been filled
        "sum_trade_amount": "1"         // turnover
    }]
}
```

### 3.3.2 Trade Data

**Request Content:**

| **PARAMETER** | **TYPE** | **REQUIRED** | **DESCRIPTION**            |
| ------------- | -------- | ------------ | -------------------------- |
| type          | string   | true         | "sub"                      |
| topic         | string   | true         | "trade_rtn"                |
| instrument_id | string   | false        | e.g. "ETH-USDT", "ETH-BTC" |

**Response Content:**

| **PARAMETER**   | **TYPE** | **DESCRIPTION**                      |
|-----------------| -------- |--------------------------------------|
| type            | string   | "sub-resp"                           |
| topic           | string   | "trade_rtn"                          |
| trade_id        | string   | Trade Id                             |
| client_order_id | string   | Client Order Id                      |
| sys_order_id    | string   | Server Order Id                      |
| instrument_id   | string   | e.g. "ETH-BTC"                       |
| direction       | string   | "buy" or "sell"                      |
| price           | string   | Price                                |
| volume          | string   | Volume                               |
| fee             | string   | Fee                                  |
| fee_ccy         | string   | Transaction fee currency, e.g. "ETH" |
| timestamp | int64    | Trade millisecond time-stamp         |
| trade_type    | string   | "Common", "Invalid"                  |


**How to Subscribe：**

```json
{
    "type":"sub",
    "parameters":[{
        "topic":"trade_rtn",
        "instrument_id":"ETH-USDT"
    }],
    "id": 1
}
```

**Response Example：**

```json
{
    "type":"sub-resp",
    "topic":"trade_rtn",
    "data":[
        {
            "sys_order_id":"1550849345000001",     // System order ID
            "client_order_id":"000000001",  // Client order ID
            "trade_id":"1",                 // Trade ID
            "instrument_id":"ETH-BTC",      // Instrument ID
            "direction":"buy",              // Trade direction
            "price":"1",                    // Price
            "volume":"1",                   // Volume
            "fee":"0.05",                   // Transaction fee
            "fee_ccy": "BTC",               // Transaction fee currency
            "timestamp": 1478692862000,     // Trade time
            "trade_type": "Common"          // Trade type
        },
        {
            "sys_order_id":"1550849345000002",
            "client_order_id":"000000002",
            "trade_id":"2",
            "instrument_id":"ETH-BTC",
            "direction":"sell",
            "price":"1",
            "volume":"2",
            "fee":"0.05",
            "fee_ccy": "BTC",
            "timestamp":1478692862000,
            "trade_type": "Common"
        }
    ]
}
```

# 4. Error code

## 4.1 Error Code Classification Standard

| **ERROR CODE RANGE** | **DESCRIPTION**    |
| -------------------- | ------------------ |
| 0000~0099            | Public error code      |
| 0100~0199            | WebSocket error code   |

## 4.2 Error Code Example

| **ERROR CODE**   | **TYPE**   | **ERROR MESSAGE**                                  |
|------------------| ---------- |----------------------------------------------------|
| 0000             | Public error code    | Success                                            |
| 0001             | Public error code    | common parameter error                                    |
| 0002             | Public error code    | System error                                       |
| 0003             | Public error code    | Request not allowed                                |
| 0004             | Public error code | Insufficient account funds                         | |
| 0005             | Public error code | Order not found                                    |
| 0006             | Public error code | Instrument not found                               |
| 0007             | Public error code | Invalid volume                               |
| 0008             | Public error code | Not enough volume to cancel                        |
| 0009             | Public error code | Unsatisfied with the price precision               |
| 0010             | Public error code | Invalid price                                      |
| 0011             | Public error code | Operation for the APIKey user not allowed               |
| 0012             | Public error code | Unsupported order type                             |
| 0013             | Public error code | duplicate orders                                   |
| 0100             | WebSocket error code | Subscription failed                                |
| 0101             | WebSocket error code | Partial subscriptions succeeded                    |



# RestAPI接口文档
## 通用
### 查询服务器时间

Http request:  GET info/time
请求正文：无   
响应正文：    

参数名  | 类型 | 注释   | 说明
--- | ---  | ---  | ---  
timestamp  | String  | 时间戳  | UTC时间
   


样例：

``` java

响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
		"timestamp":"timestamp"
	}
}

```

### 查询API发行号

Http request:  GET info/version
请求正文：无
响应正文：

参数名  | 类型 | 注释   | 说明
--- | ---  | ---  | ---
version  | String  | 版本号 


样例：

``` java

响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
		"version":"version"
	}
}

```

## 交易
### 创建限价单

Http request:  POST limit/order/create
请求正文：

参数名  | 类型  | 是否必填   | 注释   | 说明
--- | ---  | ---  | ---  | ---
orderId  | String   | true  | 订单号  | 不能重复
instrumentId  | String   | true  | 合约号  | 样例 ETH-BTC
direction  |  String  | true  | 方向 | 0-买 1-卖
price  | String | true  | 价格  | 
volume  | String | true | 数量  | 


响应正文：


参数名  | 类型 | 注释   | 说明
--- | ---  | ---  | ---
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量 |
volume  | String | 数量  | 
timestamp  | String | 下单时间戳  | 13位


样例：

``` java
请求样例：
{
	"orderId":"000000001",
	"instrumentId":"BTC-ETH",
	"direction":"0",
	"price":"1",
	"volume":"1"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
		"apiKey":"testApiKey",
		"orderId":"000000001",
     	"orderType":"1",
    	"instrumentId":"BTC-ETH",
    	"direction":"0",
    	"limtPrice":"1",
    	"volume":"1",
    	"stopPrice":"0",
    	"displaySize":"0",
    	"timestamp":"1234567890123"
	}
}

```

### 创建市价单

Http request:  POST market/order/create
请求正文：

参数名  | 类型  | 是否必填   | 注释   | 说明
--- | ---  | ---  | ---  | ---
orderId  | String   | true  | 订单号  | 不能重复
instrumentId  | String   | true  | 合约号  | 样例 ETH-BTC
direction  |  String  | true  | 方向 | 0-买 1-卖
volume  | String | true | 数量  | 

响应正文：

参数名  | 类型 | 注释   | 说明
--- | ---  | ---  | ---
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
timestamp  | String | 下单时间戳  | 13位


样例：

``` java
请求样例：
{
	"orderId":"000000001",
	"instrumentId":"BTC-ETH",
	"direction":"0",
	"volume":"1"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
		"apiKey":"testApiKey",
		"orderId":"000000001",
     	"orderType":"2",
    	"instrumentId":"BTC-ETH",
    	"direction":"0",
    	"limtPrice":"1",
    	"volume":"1",
    	"stopPrice":"0",
    	"displaySize":"0",
    	"timestamp":"1234567890123"
	}
}
```

### 撤销订单

Http request:  POST /order/cancel
请求正文：

参数名  | 类型  | 是否必填   | 注释   | 说明
--- | ---  | ---  | ---  | ---
orderId  | String   | true  | 订单号  | 

响应正文：

参数名  | 类型 | 注释   | 说明
--- | ---  | ---  | ---
apiKey  | String  | apiKey  | 
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
timestamp  | String | 下单时间戳  | 13位


``` java
请求样例：
{
	"orderId":"000000001"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
	    "apiKey":"testApiKey",
		"orderId":"000000001",
     	"orderType":"1",
    	"instrumentId":"BTC-ETH",
    	"direction":"0",
    	"limtPrice":"1",
    	"volume":"2",
    	"stopPrice":"0",
    	"displaySize":"0",
    	"timestamp":"1234567890123"
	}
}
```

### 查询订单

Http request:  GET /order/find
请求正文：

参数名  | 类型  | 是否必填   | 注释   | 说明
--- | ---  | ---  | ---  | ---
orderId  | String   | false  | 订单号  | 
instrumentId  | String   | false  | 合约号  | 样例 ETH-BTC
direction  |  String  | false  | 方向 | 0-买 1-卖
orderType  | String  | false  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
start  | String  | false  | 开始时间  | yyyyMMdd HH:mm:ss
end  | String  | false  | 结束时间  | yyyyMMdd HH:mm:ss

响应正文：

参数名  | 类型 | 注释   | 说明
--- | ---  | ---  | ---
apiKey  | String  | apiKey  | 
orderId  | String  | 订单号  | 不能重复
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
limtPrice  | String  | 价格  | 当订单类型为3 时必填
stopPrice  | String  | 触发价  | 当订单类型为4 时必填
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
orderStatus  | String | 订单状态  | 0-全部成交、1-部分成交 、2-未成交、3-撤单、4-部分成交部分撤单、5-已触发止损
timestamp  | String | 下单时间戳  | 13位


``` java
请求样例：
{
	"instrumentId":"BTC-ETH"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",,
	"data":[
		{
			"apiKey":"testApiKey",
			"orderId":"000000001",
			"orderType":"1",
			"instrumentId":"BTC-ETH",
			"direction":"0",
			"limtPrice":"1",
			"volume":"2",
			"stopPrice":"0",
			"displaySize":"0",
			"orderStatus":"0",
			"timestamp":"1234567890123"
		},
		{
			"apiKey":"testApiKey",
			"orderId":"000000002",
			"orderType":"1",
			"instrumentId":"BTC-ETH",
			"direction":"0",
			"limtPrice":"1",
			"volume":"2",
			"stopPrice":"0",
			"displaySize":"0",
			"orderStatus":"0",
			"timestamp":"1234567890123"
		}
	]
}
```

### 查询成交

Http request:  GET /trade/find
请求正文：

参数名  | 类型  | 是否必填   | 注释   | 说明
--- | ---  | ---  | ---  | ---
instrumentId  | String   | false  | 合约号  | 样例 ETH-BTC
direction  |  String  | false  | 方向 | 0-买 1-卖
start  | String  | false  | 开始时间  | yyyyMMdd HH:mm:ss
end  | String  | false  | 结束时间  | yyyyMMdd HH:mm:ss

响应正文：

参数名  | 类型 | 注释   | 说明
--- | ---  | ---  | ---
apiKey  | String  | apiKey  | 
tradeId  | String  | 成交号  | 
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
price  | String  | 价格  | 
volume  | String  | 数量  | 
fee  | String   | 手续费| 
timestamp  | String | 操作时间戳  | 13位

``` java
请求样例：
{
	"instrumentId":"BTC-ETH"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":[
		{
			"apiKey":"testApiKey",
			"orderId":"000000001",
			"tradeId":"1",
			"instrumentId":"BTC-ETH",
			"direction":"0",
			"price":"1",
			"volume":"2",
			"fee":"0.05",
			"timestamp":"1234567890123"
		},
		{
			"apiKey":"testApiKey",
			"orderId":"000000001",
			"tradeId":"2",
			"instrumentId":"BTC-ETH",
			"direction":"1",
			"price":"1",
			"volume":"2",
			"fee":"0.05",
			"timestamp":"1234567890123"
		}
	]
}
```

## 资产
### 查询资产

Http request:  GET /balance/find

请求正文：
无参

响应正文：

参数名  | 类型 | 注释   | 说明
--- | ---  | ---  | ---
assetId  | String  | 资产id  | 
balance  | String  | 资产余额  | 
available  | String  | 可用余额  | 
frozen  | String  | 冻结余额  | 


``` java
请求样例：

响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
		"assetId":"ETH",
     	"balance":"20000",
    	"available":"18000",
    	"frozen":"2000"
	}
}
```

# WebSocket接口文档

## WebSocket行情数据(公有流)
### K线数据

 请求正文

参数 |类型  |  是否必填|  描述   |  说明 
--- | --- | --- | ---| ---
type| String |true  |类型|    sub
topic| String   |true|主题    |candle_stick
period  | String|true|K线周期| 1m, 5m, 15m, 30m, 60m
instrumentId| String|true|  币对| ETH/USDT, BTC/ETH ...

 响应正文

 参数  |类型 |  描述   |  说明   
 --- | --- | --- | ---
 type| String   | 类型|   sub-resp
 topic| String  | 主题|   candle_stick
 errorCode  | String| 错误码|  0000 ...
 errorMessage| String   | 错误信息|     success ...
 high| String|  高|  
 open| String   | 开|    
 low| String    | 低|    
 close| String  | 收|    
 instrumentId| String   | 币对|   ETH/USDT, BTC/ETH ...
 volume | String| 成交量 | 
timestamp   | String|时间戳|   1492420473027


``` java
请求样例：
{
    "type":"sub",
    "channel":{
        "topic":"candle_stick",
        "period":"1m",
        "instrumentId":"ETH/USDT"
    }
}

响应样例：
{
    "type":"sub-resp",
    "topic":"candle_stick",
    "errorCode":"0000",
    "errorMessage":"success",
    "data":{
        "close":"2",
        "high":"2",
        "low":"2",
        "open":"2",
        "instrumentId":"ETH/USDT",
        "timestamp":"1492420473027",
        "volume":"0"
    }
}
```


### 行情数据

 请求正文

|  参数 |类型  |是否必填|  描述   |  说明   |
| --- | --- | --- | ---| ---
| type| String  |true| 类型   | sub
| topic| String|true    | 主题    | market_data
| instrumentId| String|true|    币对|     ETH/USDT, BTC/ETH ... 

 响应正文

 参数  |类型 |  描述   |  说明   |
 --- | --- | --- | ---
type    | String| 类型    | sub-resp
topic| String   | 主题    | market_data
errorCode| String   | 错误码   | 0000 ...
errorMessage    | String| 错误信息|     success ...
high| String|   高   | 
low | String| 低 | 
close| String|  收   | 
instrumentId| String    | 币对| ETH/USDT, BTC/ETH ...
base| String    |  源币种    | 
target  | String |    目标币种   | 
lastPrice| String   |   最新价格    | 
lastPriceValuation| String  |  最新价格估值   | 
chgRate| String |  变化比例    | 
chgVol| String  |    变化量  | 
volume| String  | 成交量| 



``` json
请求样例：
{
    "type":"sub",
    "channel":{
        "topic":"market_data",
        "instrumentId":"ETH/USDT"
    }
} 

响应样例：
{
    "type":"sub-resp",
    "topic":"market_data",
    "errorCode":"0000",
    "errorMessage":"success",
    "data":[
        {
            "close":"0",
            "high":"0",
            "low":"0",
            "base":"USDT",
            "target":"ETH",
            "instrumentId":"ETH/USDT",
            "chgRate":"0",
            "chgVol":"0",
            "lastPrice":"3",
            "lastPriceValuation":0,
            "volume":"2"
        },
        {
            "close":"0",
            "high":"0",
            "low":"0",
            "base":"USDT",
            "target":"ETH",
            "instrumentId":"ETH/USDT",
            "chgRate":"0",
            "chgVol":"0",
            "lastPrice":"3",
            "lastPriceValuation":0,
            "volume":"2"
        }
    ]
}
```


### 深度行情数据

 请求正文

  参数  |类型 |是否必填|  描述   |  说明   |
 --- | --- | --- |--- | --- 
type    | String|true |类型 | sub
topic   | String |true|主题 | depth_market_data
instrumentId| String |true| 币对   |ETH/USDT, BTC/ETH ...


 响应正文

  参数 |类型  |  描述   |  说明   |
 --- | --- | --- | --- |
type    | String |类型 |  sub-resp
topic   | String |主题 |  depth_market_data
errorCode   | String |错误码 | 0000 ...
errorMessage| String     |错误信息 |    success ...
amount  | String |  成交量      |
price   | String |  单价   |
total   | String |  总金额 |


``` json
请求样例：
{
    "type":"sub",
    "channel":{
        "topic":"depth_market_data",
        "instrumentId":"ETH/USDT"
    }
}
响应样例：
{
    "type":"sub-resp",
    "topic":"depth_market_data",
    "errorCode":"0000",
    "errorMessage":"success",
    "data":{
        "ask":[
            {
                "amount":"3",
                "price":"2",
                "total":"6"
            },
            {
                "amount":"3",
                "price":"2",
                "total":"6"
            }
        ]
    }
}
```


### 全量成交回报数据


 请求正文

  参数  |类型 |是否必填|  描述   |  说明  
 --- | --- | --- |--- | --- 
type    | String|true |类型 | sub
topic   | String |true|主题 | trade_rtn_all
instrumentId| String |false|    币对   |ETH/USDT, BTC/ETH ...传空为全量


 响应正文

  参数  |类型 |  描述   |  说明   |
 --- | --- | --- | ---
type| String    |类型 |sub-resp
topic   | String|主题|    trade_rtn_all
errorCode| String|  错误码|    0000 ...
errorMessage| String    |错误信息|  success ...
fee | String|       费用  |
instrumentId    | String    |   币对  |
direction| String       |   交易方向    | 0-买入 ， 1-卖出
tradeId     | String|   交易ID        |
volume  | String    |       成交数量    |
total   | String    |   成交额     |
price   | String    |   价格      |
tradeTimestamp  | String    |   交易时间        |


``` json
请求样例：
{
    "type":"sub",
    "channel":{
        "topic":"trade_rtn_all",
        "instrumentId":"ETH/USDT"
    }
}
响应样例：
{
    "type":"sub-resp",
    "topic":"trade_rtn_all",
    "errorCode":"0000",
    "errorMessage":"success",
    "data":[
            {
                "fee":"2",
                "instrumentId":"ETH-USDT",
                "direction":"1",
                "tradeId":"1000001",
                "volume":"2",
                "total":"2",
                "price":"2",
                "tradeTimestamp":"2020/07/01 18:08:08"
            },
            {
                "fee":"2",
                "instrumentId":"ETH-USDT",
                "direction":"1",
                "tradeId":"1000001",
                "volume":"2",
                "total":"2",
                "price":"2",
                "tradeTimestamp":"2020/07/01 18:08:08"
            }
        ]
}
```

# Errors

<aside class="notice">
This error section is stored in a separate file in <code>includes/_errors.md</code>. Slate allows you to optionally separate out your docs into many files...just save them to the <code>includes</code> folder and add them to the top of your <code>index.md</code>'s frontmatter. Files are included in the order listed.
</aside>

The Kittn API uses the following error codes:


Error Code | Meaning
---------- | -------
400 | Bad Request -- Your request is invalid.
401 | Unauthorized -- Your API key is wrong.
403 | Forbidden -- The kitten requested is hidden for administrators only.
404 | Not Found -- The specified kitten could not be found.
405 | Method Not Allowed -- You tried to access a kitten with an invalid method.
406 | Not Acceptable -- You requested a format that isn't json.
410 | Gone -- The kitten requested has been removed from our servers.
418 | I'm a teapot.
429 | Too Many Requests -- You're requesting too many kittens! Slow down!
500 | Internal Server Error -- We had a problem with our server. Try again later.
503 | Service Unavailable -- We're temporarily offline for maintenance. Please try again later.


* [简介：](#简介)
	* [联系我们](#联系我们)
* [接入说明：](#接入说明)
	* [接入准备](#接入准备)
	* [SDK示例](#sdk示例)
	* [签名认证](#签名认证)
		* [签名说明](#签名说明)
		* [签名步骤](#签名步骤)
	* [接口概览：](#接口概览)
		* [接口类型](#接口类型)
		* [接口简述](#接口简述)
	* [环境信息](#环境信息)
		* [测试环境](#测试环境)
		* [生产环境](#生产环境)
* [常见问题：](#常见问题)
* [Rest API](#rest-api)
	* [接入说明](#接入说明)
		* [限频规则](#限频规则)
		* [请求格式](#请求格式)
		* [返回格式](#返回格式)
	* [REST API](#rest-api)
* [Websocket API](#websocket-api)
	* [接入说明](#接入说明)
		* [接入地址](#接入地址)
		* [接入限制](#接入限制)
		* [心跳消息](#心跳消息)
		* [请求格式](#请求格式)
		* [返回格式](#返回格式)
	* [鉴权](#鉴权)
	* [订阅主题](#订阅主题)
	* [取消订阅](#取消订阅)
	* [websocket API](#websocket-api)
* [错误信息](#错误信息)
* [Rest API接口文档](#rest-api接口文档)
	* [1、通用](#1-通用)
		* [1.1、查询服务器时间](#11-查询服务器时间)
		* [1.2、查询API发行号](#12-查询api发行号)
	* [2、交易](#2-交易)
		* [2.1、创建限价单](#21-创建限价单)
		* [2.2、创建市价单](#22-创建市价单)
		* [2.3、创建限价止损单](#23-创建限价止损单)
		* [2.4、创建市价止损单](#24-创建市价止损单)
		* [2.5、创建冰山订单](#25-创建冰山订单)
		* [2.6、创建隐藏订单](#26-创建隐藏订单)
		* [2.7、撤销订单](#27-撤销订单)
		* [2.8、查询订单](#28-查询订单)
		* [2.9、查询成交](#29-查询成交)
		* [2.10、做市商报价](#210-做市商报价)
		* [2.11、做市商撤销报价](#211-做市商撤销报价)
	* [3、资产](#3-资产)
		* [3.1、查询资产](#31-查询资产)
* [WebSocket接口文档](#websocket接口文档)
	* [1、WebSocket行情数据(公有流)](#1-websocket行情数据公有流)
		* [1.1、K线数据](#11-k线数据)
		* [1.2、行情数据](#12-行情数据)
		* [1.3、深度行情数据](#13-深度行情数据)
		* [1.4、全量成交回报数据](#14-全量成交回报数据)
	* [2、WebSocket订单交易数据(私有流)](#2-websocket订单交易数据私有流)
		* [1.1、订单数据](#11-订单数据)
		* [1.2、交易数据](#12-交易数据)

#  简介：
欢迎使用HashKey API！此文档是HashKey API的唯一官方文档，HashKey API提供的能力会在此持续更新，请大家及时关注。


## 联系我们
使用过程中如有问题或者建议，您可选择以下任一方式联系我们。


# 接入说明：
## 接入准备
如需使用API ，请先登录网页端，完成API key的申请和权限配置，再据此文档详情进行开发和交易。
每个账户最多可创建10组Api Key，每个Api Key可对应设置读取、交易、提现三种权限。
权限说明如下：
- 读取权限：读取权限用于对数据的查询接口，例如：订单查询、成交查询等。
- 交易权限：交易权限用于下单、撤单、划转类接口。
- 提现权限：提现权限用于创建提币订单、取消提币订单操作。

创建成功后请务必记住以下信息：
 - Access Key API 访问密钥
 - Secret Key 签名认证加密所使用的密钥（仅申请时可见）

## SDK示例
具体示例请参考具体请求样例。


## 签名认证
### 签名说明
API 请求在通过 internet 传输的过程中极有可能被篡改，为了确保请求未被更改，除公共接口（基础信息，行情数据）外的私有接口均必须使用您的 API Key 做签名认证，以校验参数或参数值在传输途中是否发生了更改。
每一个API Key需要有适当的权限才能访问相应的接口，每个新创建的API Key都需要分配权限。在使用接口前，请查看每个接口的权限类型，并确认你的API Key有相应的权限。

对API端点的所有HTTP请求都需要身份验证和授权。
用户可以通过创建API key流程获得key和sercet，key和sercet用于验证和授权所有请求。
以下标头应添加到所有HTTP请求中：
Key  | Value | Description
------------- | ------------- | -----------
x-access-key  | <API_KEY> |您申请的 API Key 中的 Access Key
x-access-sign  |  \<signatureOfRequest>| 签名计算得出的值，用于确保签名有效和未被篡改
x-access-timestamp  | \<timeOfRequest> |当前时间格式为当前的时间戳（以毫秒为单位）
x-access-version  |  \<versionOfRequest>   | 签名协议的版本，默认为1

### 签名步骤

**样例：**
```java
         /**
         * 签名说明：签名所需字段apiKey、apiSecret、timestamp、version、各请求接口字段。
         *                 字段名和字段值采用key-value形式，且对Key使用ASCII码排序.
         *                 以下为测试数据demo
         */
        String key="84dd8e670471a888e3a7547e120886cb";
        String secret = "3211b4306fcb1d9670cbee5abc69dead";
        String timeOfRequest ="1478692862000";

        TreeMap<String,String> treeMap = new TreeMap<>();

        treeMap.put("x-access-key",key); //api-key
        treeMap.put("x-access-timestamp",timeOfRequest); //当前时间戳
        treeMap.put("x-access-version","1");//版本号默认1

        treeMap.put("feild1","1");//请求字段mock1
        treeMap.put("feild2","2");//请求字段mock2
        treeMap.put("feild3","3");//请求字段mock3

        String requestText = JSONObject.toJSONString(treeMap);
        //根据Map key的ASCII 排序 {"feild1":"1","feild2":"2","feild3":"3","x-access-key":"84dd8e670471a888e3a7547e120886cb","x-access-timestamp":"1478692862000","x-access-version":"1"}

        System.out.println(createSignature(requestText,secret));
        //PiB3bk0wWgY2mN9efTmCrKCtn6PZUsrlHhCsXNLUPtU=
		
		private static String createSignature(String requestText,String secret) 
		             throws Exception {
              return Base64Utils.encodeToString(hmacSha1(requestText, secret));
        }

        private static byte[] hmacSha1(String plainData, String secret)  
		            throws Exception{
            Mac mac = Mac.getInstance("HmacSHA256");
            SecretKeySpec secretKey = 
			     new SecretKeySpec(Base64Utils.decodeFromString(secret), "HmacSHA256");
            mac.init(secretKey);
            return mac.doFinal(plainData.getBytes());
         }
```

## 接口概览：
### 接口类型
HashKey Pro为用户提供两种接口，您可根据自己的使用场景来选择适合的方式。
**Rest API**
REST，即Representational State Transfer的缩写，是目前较为流行的基于HTTP的一种通信机制，每一个URL代表一种资源。
交易或资产提币等一次性操作，建议开发者使用REST API进行操作。

**WebSocket API**
WebSocket是HTML5一种新的协议（Protocol）。它实现了客户端与服务器全双工通信，通过一次简单的握手就可以建立客户端和服务器连接，服务器可以根据业务规则主动推送信息给客户端。
市场行情和买卖深度等信息，建议开发者使用WebSocket API进行获取。
### 接口简述

## 环境信息
### 测试环境
Restful URL: https://int.hashkey3.com

WebSocket: wss://int.hashkey3.com

### 生产环境
Restful URL: https://int.hashkey3.com

WebSocket: wss://int.hashkey3.com

# 常见问题：


# Rest API
## 接入说明
### 限频规则
除已单独标注限频值的接口外 - 每个API Key 在1秒之内限制10次 

比如：
资产订单类接口调用根据API Key进行限频：1秒10次

### 请求格式
所有的API请求都是restful，目前只有两种方法：GET和POST
 - GET请求：业务参数都在路径参数里
 - POST请求，业务参数以JSON格式发送在请求主体（body）里

### 返回格式
所有的接口都是JSON格式。在JSON最上层有四个字段：status, ch, ts 和 data。前三个字段表示请求状态和属性，实际的业务数据在data字段里。

参数名称|	类型|	描述
--- | --- | ---
errorCode	|String|	API接口返回状态
errorMessage	|String|	API接口错误描述信息
data	|Object	|接口返回数据主体

## REST API
[rest-api](https://github.com/hashkey-pro/open-api/blob/master/rest-api.md)

# Websocket API
## 接入说明
### 接入地址
-  /api/websocket-api/v1/stream
### 接入限制
-  同一apiKey最多允许创建10条session长连接。比如：订单成交数据订阅，同一apiKey最多允许建立10条session连接。
-  同一ip最多允许建立5条session长连接。比如：行情数据推送无需apiKey，同一ip地址最多允许建立5条连接。

### 心跳消息
当用户的Websocket客户端连接到HashKey Websocket服务器后，服务器会定期（当前设为10秒）向其发送ping消息并包含一整数值如下：

> {"type":"ping","data"="1492420473027"}

当用户的Websocket客户端接收到此心跳消息后，应返回pong消息并包含同一整数值：

> {"type":"pong","data"="1492420473027"}

   注：当Websocket服务器连续两次发送了`ping`消息却没有收到任何一次`pong`消息返回后，服务器将主动断开与此客户端的连接。

### 请求格式
所有的请求都是JSON格式，订阅不同topic传递不同参数，请参考具体接口请求样例。

### 返回格式
所有的响应都是JSON格式，不同topic返回data各有不同，请参考具体接口响应样例。

## 鉴权

**请求正文**
|  参数  |类型 |  是否必填|注释   |  说明   |
| --- | --- |--- | --- |---
type	| String|true |操作类型 |	默认为auth
x-access-key | String |true |访问Key  |您申请的 API Key 中的 Access Key
x-access-sign | String |true | 签名 | 签名计算得出的值，用于确保签名有效和未被篡改
x-access-timestamp| String |true  | 时间戳 |当前时间格式为当前的时间戳（以毫秒为单位）
x-access-version  | String|true |  版本号   | 签名协议的版本，默认为1

**响应正文**
|  参数  |类型 |  是否必填|注释   |  说明   |
| --- | --- |--- | --- |---
type	| String|true |操作类型 |	默认为auth-resp
errorCode	| String |true|错误码 |	0000 
errorMessage| String	|true |错误信息 |	success

``` json
请求样例：
{
    "type":"auth",
    "auth":{
        "x-access-key":"xxxxxxxxx",
        "x-access-sign":"xxxxxxxxx",
        "x-access-timestamp":"150782303000",
		"x-access-version":"2"
    }
}
响应样例：
{
    "type":"auth-resp",
    "errorCode":"0000",
    "errorMessage":"success"    
}
```

## 订阅主题 

**请求正文**
|  参数  |类型 |  是否必填|注释   |  说明   |
| --- | --- |--- | --- |---
type	| String|true |操作类型 |	sub
topic | String |true |订阅的主题  | 
apiKey | String |false | apiKey 私有流必传  | 
...|||


**响应正文**
|  参数  |类型 |  是否必填|注释   |  说明   |
| --- | --- |--- | --- |---
type	| String|true |操作类型 |	默认为sub-resp
errorCode	| String |true|错误码 |	0000 
errorMessage| String	|true |错误信息 |	success
data | Object |true|数据|

``` json
请求样例：
{
    "type":"sub",
    "channels":  [
		{
        "topic":"xxxxxxxxx",
		......
    	},
		{
        "topic":"xxxxxxxxx",
		......
    	}
	]
}
响应样例：
{
    "type":"sub-resp",
    "errorCode":"0000",
    "errorMessage":"success",
	"data": [
		{
		   ....
		}
	]
}
```

## 取消订阅
**请求正文**
|  参数  |类型 |  是否必填|注释   |  说明   |
| --- | --- |--- | --- |---
type	| String|true |操作类型 |	unsub
topic | String |true |订阅的主题  | 
...|||


**响应正文**
|  参数  |类型 |  是否必填|注释   |  说明   |
| --- | --- |--- | --- |---
type	| String|true |操作类型 |	默认为unsub-resp
errorCode	| String |true|错误码 |	0000 
errorMessage| String	|true |错误信息 |	success


``` json
请求样例：
{
    "type":"unsub",
    "channel":  {
        "topic":"xxxxxxxxx",
		......
	}
}
响应样例：
{
    "type":"unsub-resp",
    "errorCode":"0000",
    "errorMessage":"success"
}
```


## websocket API
[websocket-api](https://github.com/hashkey-pro/open-api/blob/master/websocket-api.md)

# 错误信息
**错误码划分规范**
| 错误码 | 描述|
| --- | ---|
0000~0099  |公共错误码 
0100~0199  |WebSocket错误码
0200~0299 | 行情错误码

**错误码对照表**
|错误类型 |  错误码   |  错误信息   |  描述   |          
| --- | --- | --- | --- | 
  |  公共错误码   |0000    | success   |  成功   |
  |  公共错误码   | 0092    | network error   |  网络连接异常   |
  |  公共错误码   | 0096    | system error   |  系统异常   |


# Rest API接口文档
## 1、通用
### 1.1、查询服务器时间
Http request:  GET info/time
请求正文：无
响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
timestamp  | String  | 时间戳  | UTC时间

样例：
```java

响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
		"timestamp":"timestamp"
	}
}

```

### 1.2、查询API发行号
Http request:  GET info/version
请求正文：无
响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
version  | String  | 版本号  |

样例：
```java

响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
		"version":"version"
	}
}

```

## 2、交易
### 2.1、创建限价单
Http request:  POST limit/order/create
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
orderId  | String   | true  | 订单号  | 不能重复
instrumentId  | String   | true  | 合约号  | 样例 ETH-BTC
direction  |  String  | true  | 方向 | 0-买 1-卖
price  | String | true  | 价格  | 
volume  | String | true | 数量  | 

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
timestamp  | String | 下单时间戳  | 13位


样例：
```java
请求样例：
{
	"orderId":"000000001",
	"instrumentId":"BTC-ETH",
	"direction":"0",
	"price":"1",
	"volume":"1"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
		"apiKey":"testApiKey",
		"orderId":"000000001",
     	"orderType":"1",
    	"instrumentId":"BTC-ETH",
    	"direction":"0",
    	"limtPrice":"1",
    	"volume":"1",
    	"stopPrice":"0",
    	"displaySize":"0",
    	"timestamp":"1234567890123"
	}
}

```

### 2.2、创建市价单
Http request:  POST market/order/create
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
orderId  | String   | true  | 订单号  | 不能重复
instrumentId  | String   | true  | 合约号  | 样例 ETH-BTC
direction  |  String  | true  | 方向 | 0-买 1-卖
volume  | String | true | 数量  | 

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
timestamp  | String | 下单时间戳  | 13位


样例：
```java
请求样例：
{
	"orderId":"000000001",
	"instrumentId":"BTC-ETH",
	"direction":"0",
	"volume":"1"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
		"apiKey":"testApiKey",
		"orderId":"000000001",
     	"orderType":"2",
    	"instrumentId":"BTC-ETH",
    	"direction":"0",
    	"limtPrice":"1",
    	"volume":"1",
    	"stopPrice":"0",
    	"displaySize":"0",
    	"timestamp":"1234567890123"
	}
}
```

### 2.3、创建限价止损单
Http request:  POST stopL/order/create
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
orderId  | String   | true  | 订单号  | 不能重复
instrumentId  | String   | true  | 合约号  | 样例 ETH-BTC
direction  |  String  | true  | 方向 | 0-买 1-卖
price  | String | true  | 价格  | 
volume  | String | true | 数量  | 
stopPrice  | String | true | 触发价  | 

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止损限价单 、4-冰山订单 、5-隐藏订单 、6-止损市价单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
timestamp  | String | 下单时间戳  | 13位


样例：
```java
请求样例：
{
	"orderId":"000000001",
	"instrumentId":"BTC-ETH",
	"direction":"0",
	"price":"1",
	"volume":"1"，
	"stopPrice":"2"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
	    "apiKey":"testApiKey",
		"orderId":"000000001",
     	"orderType":"3",
    	"instrumentId":"BTC-ETH",
    	"direction":"0",
    	"limtPrice":"1",
    	"volume":"1",
    	"stopPrice":"2",
    	"displaySize":"0",
    	"timestamp":"1234567890123"
	}
}
```

### 2.4、创建市价止损单
Http request:  POST stopM/order/create
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
orderId  | String   | true  | 订单号  | 不能重复
instrumentId  | String   | true  | 合约号  | 样例 ETH-BTC
direction  |  String  | true  | 方向 | 0-买 1-卖
volume  | String | true | 数量  | 
stopPrice  | String | true | 触发价  | 

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止损限价单 、4-冰山订单 、5-隐藏订单 、6-止损市价单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
timestamp  | String | 下单时间戳  | 13位


样例：
```java
请求样例：
{
	"orderId":"000000001",
	"instrumentId":"BTC-ETH",
	"direction":"0",
	"volume":"1",
	"stopPrice":"2"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
	    "apiKey":"testApiKey",
		"orderId":"000000001",
     	"orderType":"6",
    	"instrumentId":"BTC-ETH",
    	"direction":"0",
    	"limtPrice":"1",
    	"volume":"1",
    	"stopPrice":"2",
    	"displaySize":"0",
    	"timestamp":"1234567890123"
	}
}
```

### 2.5、创建冰山订单
Http request:  POST ice/order/create
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
orderId  | String   | true  | 订单号  | 不能重复
instrumentId  | String   | true  | 合约号  | 样例 ETH-BTC
direction  |  String  | true  | 方向 | 0-买 1-卖
volume  | String | true | 数量  | 
price  | String | true | 价格  | 
displaySize  | String | true | 展示数量  | 

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止损限价单 、4-冰山订单 、5-隐藏订单 、6-止损市价单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
timestamp  | String | 下单时间戳  | 13位


样例：
```java
请求样例：
{
	"orderId":"000000001",
	"instrumentId":"BTC-ETH",
	"direction":"0",
	"volume":"2",
	"price":"1",
	"displaySize":"1"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
	    "apiKey":"testApiKey",
		"orderId":"000000001",
     	"orderType":"4",
    	"instrumentId":"BTC-ETH",
    	"direction":"0",
    	"limtPrice":"1",
    	"volume":"2",
    	"stopPrice":"0",
    	"displaySize":"1",
    	"timestamp":"1234567890123"
	}
}
```

### 2.6、创建隐藏订单
Http request:  POST hidden/order/create
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
orderId  | String   | true  | 订单号  | 不能重复
instrumentId  | String   | true  | 合约号  | 样例 ETH-BTC
direction  |  String  | true  | 方向 | 0-买 1-卖
volume  | String | true | 数量  | 
price  | String | true | 价格  | 

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
timestamp  | String | 下单时间戳  | 13位


样例：
```java
请求样例：
{
	"orderId":"000000001",
	"instrumentId":"BTC-ETH",
	"direction":"0",
	"volume":"2",
	"price":"1"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
	    "apiKey":"testApiKey",
		"orderId":"000000001",
     	"orderType":"5",
    	"instrumentId":"BTC-ETH",
    	"direction":"0",
    	"limtPrice":"1",
    	"volume":"2",
    	"stopPrice":"0",
    	"displaySize":"0",
    	"timestamp":"1234567890123"
	}
}
```

### 2.7、撤销订单
Http request:  POST /order/cancel
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
orderId  | String   | true  | 订单号  | 

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
apiKey  | String  | apiKey  | 
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
timestamp  | String | 下单时间戳  | 13位

```java
请求样例：
{
	"orderId":"000000001"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
	    "apiKey":"testApiKey",
		"orderId":"000000001",
     	"orderType":"1",
    	"instrumentId":"BTC-ETH",
    	"direction":"0",
    	"limtPrice":"1",
    	"volume":"2",
    	"stopPrice":"0",
    	"displaySize":"0",
    	"timestamp":"1234567890123"
	}
}
```

### 2.8、查询订单
Http request:  GET /order/find
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
orderId  | String   | false  | 订单号  | 
instrumentId  | String   | false  | 合约号  | 样例 ETH-BTC
direction  |  String  | false  | 方向 | 0-买 1-卖
orderType  | String  | false  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
start  | String  | false  | 开始时间  | yyyyMMdd HH:mm:ss
end  | String  | false  | 结束时间  | yyyyMMdd HH:mm:ss

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
apiKey  | String  | apiKey  | 
orderId  | String  | 订单号  | 不能重复
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
limtPrice  | String  | 价格  | 当订单类型为3 时必填
stopPrice  | String  | 触发价  | 当订单类型为4 时必填
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
orderStatus  | String | 订单状态  | 0-全部成交、1-部分成交 、2-未成交、3-撤单、4-部分成交部分撤单、5-已触发止损
timestamp  | String | 下单时间戳  | 13位


```java
请求样例：
{
	"instrumentId":"BTC-ETH"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",,
	"data":[
		{
			"apiKey":"testApiKey",
			"orderId":"000000001",
			"orderType":"1",
			"instrumentId":"BTC-ETH",
			"direction":"0",
			"limtPrice":"1",
			"volume":"2",
			"stopPrice":"0",
			"displaySize":"0",
			"orderStatus":"0",
			"timestamp":"1234567890123"
		},
		{
			"apiKey":"testApiKey",
			"orderId":"000000002",
			"orderType":"1",
			"instrumentId":"BTC-ETH",
			"direction":"0",
			"limtPrice":"1",
			"volume":"2",
			"stopPrice":"0",
			"displaySize":"0",
			"orderStatus":"0",
			"timestamp":"1234567890123"
		}
	]
}
```

### 2.9、查询成交
Http request:  GET /trade/find
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
instrumentId  | String   | false  | 合约号  | 样例 ETH-BTC
direction  |  String  | false  | 方向 | 0-买 1-卖
start  | String  | false  | 开始时间  | yyyyMMdd HH:mm:ss
end  | String  | false  | 结束时间  | yyyyMMdd HH:mm:ss

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
apiKey  | String  | apiKey  | 
tradeId  | String  | 成交号  | 
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
price  | String  | 价格  | 
volume  | String  | 数量  | 
fee  | String   | 手续费| 
timestamp  | String | 操作时间戳  | 13位

```java
请求样例：
{
	"instrumentId":"BTC-ETH"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":[
		{
			"apiKey":"testApiKey",
			"orderId":"000000001",
			"tradeId":"1",
			"instrumentId":"BTC-ETH",
			"direction":"0",
			"price":"1",
			"volume":"2",
			"fee":"0.05",
			"timestamp":"1234567890123"
		},
		{
			"apiKey":"testApiKey",
			"orderId":"000000001",
			"tradeId":"2",
			"instrumentId":"BTC-ETH",
			"direction":"1",
			"price":"1",
			"volume":"2",
			"fee":"0.05",
			"timestamp":"1234567890123"
		}
	]
}
```

### 2.10、做市商报价
Http request:  POST /quote/create
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
instrumentId  |  String  | true  | 合约号 | 
bidVolume  | String  | true  | 买方数量  | 
askVolume  | String  | true  | 卖方数量  | 
bidPrice  | String  | true  | 买方价格  | 
askPrice | String  | true  | 卖方价格  | 

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
quoteId  | String  | 报价单号  | 
apiKey  | String   | apiKey  | 
instrumentId  |  String | 合约号 | 
bidVolume  | String  | 买方数量  | 
askVolume | String  | 卖方数量  | 
bidPrice  | String  | 买方价格  | 
askPrice | String  | 卖方价格  | 
insertTimestamp  | String  | 报单时间戳  | 
```java
请求样例：
{
	"instrumentId":"BTC-ETH"，
	"bidVolume":"1"，
	"askVolume":"1"，
	"bidPrice":"1"，
	"askPrice":"1"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
	        "apiKey":"testApiKey",
			"quoteId":"000000001",
			"instrumentId":"BTC-ETH",
			"bidVolume":"1",
			"askVolume":"1",
			"bidPrice":"1",
			"askPrice":"1",
			"insertTimestamp":"1234567890123"
		}
}
```

### 2.11、做市商撤销报价
Http request:  POST /quote/cancel
请求正文：
参数名  | 类型  | 是否必填   | 注释   | 说明
------------- | -------------  | -------------  | -------------  | -------------
quoteId  |  String  | true  | 报价单号 | 

响应正文：
无

```java
请求样例：
{
	"quoteId":"0000001"
}
响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{}
}
```

## 3、资产
### 3.1、查询资产
Http request:  GET /balance/find
请求正文：
无参

响应正文：
参数名  | 类型 | 注释   | 说明
------------- | ------------  | -------------  | -------------
assetId  | String  | 资产id  | 
balance  | String  | 资产余额  | 
available  | String  | 可用余额  | 
frozen  | String  | 冻结余额  | 

```java
请求样例：

响应样例：
{
	"errorCode":"0000",
	"errorMessage":"",
	"data":{
		"assetId":"ETH",
     	"balance":"20000",
    	"available":"18000",
    	"frozen":"2000"
	}
}
```



# WebSocket接口文档

## 1、WebSocket行情数据(公有流)
### 1.1、K线数据

**请求正文**
|  参数 |类型  |  是否必填|  描述   |  说明   |
| --- | --- | --- | ---| ---
type| String |true	|类型|	sub
topic| String	|true|主题	|candle_stick
period	| String|true|K线周期|	1m, 5m, 15m, 30m, 60m
instrumentId| String|true|	币对|	ETH/USDT, BTC/ETH ...

**响应正文**
|  参数  |类型 |  描述   |  说明   |
| --- | --- | --- | ---
| type| String	| 类型| 	sub-resp
| topic| String	| 主题| 	candle_stick
| errorCode	| String| 错误码| 	0000 ...
| errorMessage| String	| 错误信息| 	success ...
| high| String| 	高| 	
| open| String	| 开| 	
| low| String	| 低| 	
| close| String	| 收| 	
| instrumentId| String	| 币对| 	ETH/USDT, BTC/ETH ...
| volume	| String| 成交量 | 
|timestamp	| String|时间戳|	1492420473027

``` json
请求样例：
{
    "type":"sub",
    "channel":{
        "topic":"candle_stick",
        "period":"1m",
        "instrumentId":"ETH/USDT"
    }
}

响应样例：
{
    "type":"sub-resp",
    "topic":"candle_stick",
    "errorCode":"0000",
    "errorMessage":"success",
    "data":{
        "close":"2",
        "high":"2",
        "low":"2",
        "open":"2",
        "instrumentId":"ETH/USDT",
        "timestamp":"1492420473027",
        "volume":"0"
    }
}
```


### 1.2、行情数据
**请求正文**
|  参数 |类型  |是否必填|  描述   |  说明   |
| --- | --- | --- | ---| ---
| type| String	|true| 类型	| sub
| topic| String|true	| 主题	| market_data
| instrumentId| String|true| 	币对| 	ETH/USDT, BTC/ETH ... 

**响应正文**
|  参数  |类型 |  描述   |  说明   |
| --- | --- | --- | ---
|type	| String| 类型	| sub-resp
|topic| String	| 主题	| market_data
|errorCode| String	| 错误码	| 0000 ...
|errorMessage	| String| 错误信息| 	success ...
|high| String| 	高	| 
|low	| String| 低	| 
|close| String| 	收	| 
|instrumentId| String	| 币对| ETH/USDT, BTC/ETH ...
|base| String	|  源币种    | 
|target	| String |    目标币种   | 
|lastPrice| String	|   最新价格    | 
|lastPriceValuation| String	|  最新价格估值   | 
|chgRate| String	|  变化比例    | 
|chgVol| String	|    变化量  | 
|volume| String	| 成交量| 

``` json
请求样例：
{
    "type":"sub",
    "channel":{
        "topic":"market_data",
        "instrumentId":"ETH/USDT"
    }
} 

响应样例：
{
    "type":"sub-resp",
    "topic":"market_data",
    "errorCode":"0000",
    "errorMessage":"success",
    "data":[
        {
            "close":"0",
            "high":"0",
            "low":"0",
            "base":"USDT",
            "target":"ETH",
            "instrumentId":"ETH/USDT",
            "chgRate":"0",
            "chgVol":"0",
            "lastPrice":"3",
            "lastPriceValuation":0,
            "volume":"2"
        },
		{
            "close":"0",
            "high":"0",
            "low":"0",
            "base":"USDT",
            "target":"ETH",
            "instrumentId":"ETH/USDT",
            "chgRate":"0",
            "chgVol":"0",
            "lastPrice":"3",
            "lastPriceValuation":0,
            "volume":"2"
        }
    ]
}
```


### 1.3、深度行情数据

**请求正文**
|  参数  |类型 |是否必填|  描述   |  说明   |
| --- | --- | --- |--- | --- 
type	| String|true |类型 |	sub
topic	| String |true|主题 |	depth_market_data
instrumentId| String |true|	币对	 |ETH/USDT, BTC/ETH ...

**响应正文**
|  参数 |类型  |  描述   |  说明   |
| --- | --- | --- | --- |
type	| String |类型 |	sub-resp
topic	| String |主题 |	depth_market_data
errorCode	| String |错误码 |	0000 ...
errorMessage| String	 |错误信息 |	success ...
amount	| String |  成交量  	 |
price	| String |	单价	 |
total	| String |	总金额 |

``` json
请求样例：
{
    "type":"sub",
    "channel":{
        "topic":"depth_market_data",
        "instrumentId":"ETH/USDT"
    }
}
响应样例：
{
    "type":"sub-resp",
    "topic":"depth_market_data",
    "errorCode":"0000",
    "errorMessage":"success",
    "data":{
        "ask":[
            {
                "amount":"3",
                "price":"2",
                "total":"6"
            },
			{
                "amount":"3",
                "price":"2",
                "total":"6"
            }
        ]
    }
}
```


### 1.4、全量成交回报数据


**请求正文**
|  参数  |类型 |是否必填|  描述   |  说明   |
| --- | --- | --- |--- | --- 
type	| String|true |类型 |	sub
topic	| String |true|主题 |	trade_rtn_all
instrumentId| String |false|	币对	 |ETH/USDT, BTC/ETH ...传空为全量


**响应正文**
|  参数  |类型 |  描述   |  说明   |
| --- | --- | --- | ---
type| String	|类型	|sub-resp
topic	| String|主题|	trade_rtn_all
errorCode| String|	错误码|	0000 ...
errorMessage| String	|错误信息|	success ...
fee	| String|		费用	|
instrumentId	| String	|	币对 	|
direction| String		|	交易方向	| 0-买入 ， 1-卖出
tradeId		| String|	交易ID		|
volume	| String	|		成交数量	|
total	| String	|	成交额		|
price	| String	|	价格		|
tradeTimestamp	| String	|	交易时间		|


``` json
请求样例：
{
    "type":"sub",
    "channel":{
        "topic":"trade_rtn_all",
        "instrumentId":"ETH/USDT"
    }
}
响应样例：
{
    "type":"sub-resp",
    "topic":"trade_rtn_all",
    "errorCode":"0000",
    "errorMessage":"success",
    "data":[
            {
				"fee":"2",
				"instrumentId":"ETH-USDT",
				"direction":"1",
				"tradeId":"1000001",
				"volume":"2",
				"total":"2",
				"price":"2",
				"tradeTimestamp":"2020/07/01 18:08:08"
            },
			{
				"fee":"2",
				"instrumentId":"ETH-USDT",
				"direction":"1",
				"tradeId":"1000001",
				"volume":"2",
				"total":"2",
				"price":"2",
				"tradeTimestamp":"2020/07/01 18:08:08"
            }
        ]
}
```

## 2、WebSocket订单交易数据(私有流)

### 1.1、订单数据


**请求正文**
|  参数  |类型 |是否必填|  描述   |  说明   |
| --- | --- | --- | --- | ---
type| String|true|	类型|	sub
topic	| String|true|主题	|order_rtn
instrumentId| String|false|	币对	|ETH/USDT, BTC/ETH ...传空为全量

**响应正文**
|  参数   | 类型 |  描述   |  说明   |
| --- | --- | --- | --- |
type	 | String|类型	|sub-resp
topic	 | String|主题|	order_rtn
errorCode | String|	错误码|	0000 ...
errorMessage | String	|错误信息|	success ...
apiKey  | String  | apiKey  | 
orderId  | String  | 订单号  | 不能重复
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
orderType  | String  | 订单类型  | 1-限价单、2-市价单 、3-止盈止损 、4-冰山订单 、5-隐藏订单
limtPrice  | String  | 价格  | 
stopPrice  | String  | 触发价  | 
displaySize  | String   | 展示数量| 
volume  | String | 数量  | 
orderStatus  | String | 订单状态  | 0-全部成交、1-部分成交 、2-未成交、3-撤单、4-部分成交部分撤单、5-已触发止损
orderTimestamp  | String | 操作时间戳  | 13位

``` json
请求样例：
{
    "type":"sub",
    "channel":{
        "apiKey":"xxxxxxxxxx",
        "topic":"order_rtn",
        "instrumentId":"ETH/USDT"
    }
}
响应样例：
{
    "type":"sub-resp",
    "topic":"order_rtn",
    "errorCode":"0000",
    "errorMessage":"success",
    "data":[
        {
			"apiKey":"testApiKey",
			"orderId":"000000001",
			"orderType":"1",
			"instrumentId":"BTC-ETH",
			"direction":"0",
			"limtPrice":"1",
			"volume":"2",
			"stopPrice":"0",
			"displaySize":"0",
			"orderStatus":"0",
			"orderTimestamp":"1234567890123"
		},
		{
			"apiKey":"testApiKey",
			"orderId":"000000002",
			"orderType":"1",
			"instrumentId":"BTC-ETH",
			"direction":"0",
			"limtPrice":"1",
			"volume":"2",
			"stopPrice":"0",
			"displaySize":"0",
			"orderStatus":"0",
			"orderTimestamp":"1234567890123"
		}
    ]
}
```

### 1.2、交易数据


**请求正文**
|  参数   | 类型|是否必填 |  描述   |  说明   |
| --- | --- | --- | --- | ---
type| String|true|	类型|	sub
topic	| String|true|主题	|trade_rtn
instrumentId| String|false|	币对	|ETH/USDT, BTC/ETH ...传空为全量



**响应正文**
|  参数   | 类型 |  描述   |  说明   |
| --- | --- | --- | --- | 
type  | String 	|类型	|sub-resp
topic	  | String |主题|	trade_rtn
errorCode  | String |	错误码|	0000 ...
errorMessage	  | String |错误信息|	success ...
apiKey  | String  | apiKey  | 
tradeId  | String  | 成交号  | 
orderId  | String  | 订单号  | 
instrumentId  | String  | 合约号  | 样例 ETH-BTC
direction  |  String  | 方向 | 0-买 1-卖
price  | String  | 价格  | 
volume  | String  | 数量  | 
fee  | String   | 手续费| 
tradeTimestamp  | String | 操作时间戳  | 13位


``` json
请求样例：
{
    "type":"sub",
    "channel":{
        "apiKey":"xxxxxxxxxx",
        "topic":"trade_rtn",
        "instrumentId":"ETH/USDT"
    }
}
响应样例：
{
    "type":"sub-resp",
    "topic":"trade_rtn",
    "errorCode":"0000",
    "errorMessage":"success",
    "data":[
        {
			"apiKey":"testApiKey",
			"orderId":"000000001",
			"tradeId":"1",
			"instrumentId":"BTC-ETH",
			"direction":"0",
			"price":"1",
			"volume":"2",
			"fee":"0.05",
			"tradeTimestamp":"1234567890123"
		},
		{
			"apiKey":"testApiKey",
			"orderId":"000000001",
			"tradeId":"2",
			"instrumentId":"BTC-ETH",
			"direction":"1",
			"price":"1",
			"volume":"2",
			"fee":"0.05",
			"tradeTimestamp":"1234567890123"
		}
    ]
}
```

# docker镜像和容器的基本操作
## docker的三个基本概念

- 镜像 Image
- 容器 Container
- 仓库 Repository

理解了这三个概念，就了解了docker的整个生命周期

## 获取镜像
Docker 官方提供了一个公共的镜像仓库：[Docker Hub](https://hub.docker.com/explore/)，我们就可以从这上面获取镜像，获取镜像的命令：docker pull，格式为：

```shell
$ docker pull [选项] [Docker Registry 地址[:端口]/]仓库名[:标签]
```

- Docker 镜像仓库地址：地址的格式一般是 <域名/IP>[:端口号]，默认地址是 Docker Hub。
- 仓库名：这里的仓库名是两段式名称，即 <用户名>/<软件名>。对于 Docker Hub，如果不给出用户名，则默认为 library，也就是官方镜像。比如：

```shell
$ docker pull ubuntu:16.04
16.04: Pulling from library/ubuntu
bf5d46315322: Pull complete
9f13e0ac480c: Pull complete
e8988b5b3097: Pull complete
40af181810e7: Pull complete
e6f7c7e5c03e: Pull complete
Digest: sha256:147913621d9cdea08853f6ba9116c2e27a3ceffecf3b492983ae97c3d643fbbe
Status: Downloaded newer image for ubuntu:16.04
```

上面的命令中没有给出 Docker 镜像仓库地址，因此将会从 Docker Hub 获取镜像。而镜像名称是 ubuntu:16.04，因此将会获取官方镜像 library/ubuntu 仓库中标签为 16.04 的镜像。
从下载过程中可以看到我们之前提及的分层存储的概念，镜像是由多层存储所构成。下载也是一层层的去下载，并非单一文件。下载过程中给出了每一层的 ID 的前 12 位。并且下载结束后，给出该镜像完整的`sha256`的摘要，以确保下载一致性。

## 运行

有了镜像后，我们就能够以这个镜像为基础启动并运行一个容器。以上面的 ubuntu:16.04 为例，如果我们打算启动里面的 bash 并且进行交互式操作的话，可以执行下面的命令。

```shell
$ docker run -it --rm \
    ubuntu:16.04 \
    /bin/bash
root@e7009c6ce357:/# cat /etc/os-release
NAME="Ubuntu"
VERSION="16.04.4 LTS, Trusty Tahr"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.4 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
```

`docker run`就是运行容器的命令，具体格式我们会在后面的课程中进行详细讲解，我们这里简要的说明一下上面用到的参数。

- -it：这是两个参数，一个是 -i：交互式操作，一个是 -t 终端。我们这里打算进入 bash 执行一些命令并查看返回结果，因此我们需要交互式终端。
- --rm：这个参数是说容器退出后随之将其删除。默认情况下，为了排障需求，退出的容器并不会立即删除，除非手动 docker rm。我们这里只是随便执行个命令，看看结果，不需要排障和保留结果，因此使用`--rm`可以避免浪费空间。
- ubuntu:16.04：这是指用 ubuntu:16.04 镜像为基础来启动容器。
- bash：放在镜像名后的是命令，这里我们希望有个交互式 Shell，因此用的是 bash。

进入容器后，我们可以在 Shell 下操作，执行任何所需的命令。这里，我们执行了`cat /etc/os-release`，这是 Linux 常用的查看当前系统版本的命令，从返回的结果可以看到容器内是 Ubuntu 16.04.4 LTS 系统。最后我们通过 `exit` 退出了这个容器。

## 列出镜像

```shell
$ docker image ls
```

列表包含了**仓库名、标签、镜像 ID、创建时间以及所占用的空间**。镜像 ID 则是镜像的唯一标识，一个镜像可以对应多个标签。

## 镜像大小

如果仔细观察，会注意到，这里标识的所占用空间和在 Docker Hub 上看到的镜像大小不同。比如，ubuntu:16.04 镜像大小，在这里是 127 MB，但是在[Docker Hub](https://hub.docker.com/r/library/ubuntu/tags/)显示的却是 43 MB。这是因为 Docker Hub 中显示的体积是压缩后的体积。在镜像下载和上传过程中镜像是保持着压缩状态的，因此 Docker Hub 所显示的大小是网络传输中更关心的流量大小。而`docker image ls`显示的是镜像下载到本地后，展开的大小，准确说，是展开后的各层所占空间的总和，因为镜像到本地后，查看空间的时候，更关心的是本地磁盘空间占用的大小。
另外一个需要注意的问题是，`docker image ls`列表中的镜像体积总和并非是所有镜像实际硬盘消耗。由于 Docker 镜像是多层存储结构，并且可以继承、复用，因此不同镜像可能会因为使用相同的基础镜像，从而拥有共同的层。由于 Docker 使用`Union FS`，相同的层只需要保存一份即可，因此实际镜像硬盘占用空间很可能要比这个列表镜像大小的总和要小的多。你可以通过以下命令来便捷的查看镜像、容器、数据卷所占用的空间。

```shell
$ docker system df
```

## 新建并启动

所需要的命令主要为`docker run`。
例如，下面的命令输出一个 “Hello World”，之后终止容器。

```shell
$ docker run ubuntu:16.04 /bin/echo 'Hello world'
Hello world
```

这跟在本地直接执行`/bin/echo 'hello world'`几乎感觉不出任何区别。下面的命令则启动一个 bash 终端，允许用户进行交互。

```shell
$ docker run -t -i ubuntu:16.04 /bin/bash
root@af8bae53bdd3:/#
```

其中，`-t`选项让Docker分配一个伪终端（pseudo-tty）并绑定到容器的标准输入上，`-i`则让容器的标准输入保持打开。
在交互模式下，用户可以通过所创建的终端来输入命令，例如：

```shell
root@af8bae53bdd3:/# pwd
/
root@af8bae53bdd3:/# ls
bin boot dev etc home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var
```

当利用`docker run`来创建容器时，Docker 在后台运行的标准操作包括：

- 检查本地是否存在指定的镜像，不存在就从公有仓库下载
- 利用镜像创建并启动一个容器
- 分配一个文件系统，并在只读的镜像层外面挂载一层可读写层
- 从宿主主机配置的网桥接口中桥接一个虚拟接口到容器中去
- 从地址池配置一个 ip 地址给容器
- 执行用户指定的应用程序
- 执行完毕后容器被终止

## 启动已终止容器

可以利用`docker container start`命令，直接将一个已经终止的容器启动运行。
容器的核心为所执行的应用程序，所需要的资源都是应用程序运行所必需的。除此之外，并没有其它的资源。可以在伪终端中利用 ps 或 top 来查看进程信息。

```shell
root@ba267838cc1b:/# ps
  PID TTY          TIME CMD
    1 ?        00:00:00 bash
   11 ?        00:00:00 ps
```

可见，容器中仅运行了指定的 bash 应用。这种特点使得 Docker 对资源的利用率极高，是货真价实的轻量级虚拟化。

## 后台运行

更多的时候，需要让 Docker 在后台运行而不是直接把执行命令的结果输出在当前宿主机下。此时，可以通过添加`-d`参数来实现。下面举两个例子来说明一下。
如果不使用`-d`参数运行容器。

```shell
$ docker run ubuntu:16.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
hello world
hello world
hello world
hello world
```

容器会把输出的结果 (STDOUT) 打印到宿主机上面。如果使用了`-d`参数运行容器。

```shell
$ docker run -d ubuntu:16.04 /bin/sh -c "while true; do echo hello world; sleep 1; done"
77b2dc01fe0f3f1265df143181e7b9af5e05279a884f4776ee75350ea9d8017a
```

此时容器会在后台运行并不会把输出的结果 (STDOUT) 打印到宿主机上面(输出结果可以用 docker logs 查看)。

> 注： 容器是否会长久运行，是和 docker run 指定的命令有关，和 -d 参数无关。
> 使用`-d`参数启动后会返回一个唯一的 id，也可以通过`docker container ls`命令来查看容器信息。


```shell
$ docker container ls
CONTAINER ID  IMAGE         COMMAND               CREATED        STATUS       PORTS NAMES
77b2dc01fe0f  ubuntu:16.04  /bin/sh -c 'while tr  2 minutes ago  Up 1 minute        agitated_wright
要获取容器的输出信息，可以通过 docker container logs 命令。
$ docker container logs [container ID or NAMES]
hello world
hello world
hello world
. . .
```

## 终止容器

可以使用`docker container stop`来终止一个运行中的容器。此外，当 Docker 容器中指定的应用终结时，容器也自动终止。
例如对于上一章节中只启动了一个终端的容器，用户通过 exit 命令或 Ctrl+d 来退出终端时，所创建的容器立刻终止。终止状态的容器可以用`docker container ls -a` 命令看到。例如

```shell
$ docker container ls -a
CONTAINER ID        IMAGE                    COMMAND                CREATED             STATUS                          PORTS               NAMES
ba267838cc1b        ubuntu:16.04             "/bin/bash"            30 minutes ago      Exited (0) About a minute ago                       trusting_newton
```

处于终止状态的容器，可以通过`docker container start`命令来重新启动。
此外，`docker container restart`命令会将一个运行态的容器终止，然后再重新启动它。

## 进入容器

在使用`-d`参数时，容器启动后会进入后台。某些时候需要进入容器进行操作：**exec 命令 -i -t 参数**。
只用`-i`参数时，由于没有分配伪终端，界面没有我们熟悉的`Linux`命令提示符，但命令执行结果仍然可以返回。
当`-i -t`参数一起使用时，则可以看到我们熟悉的 `Linux`命令提示符。

```shell
$ docker run -dit ubuntu:16.04
69d137adef7a8a689cbcb059e94da5489d3cddd240ff675c640c8d96e84fe1f6
$ docker container ls
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS               NAMES
69d137adef7a        ubuntu:16.04       "/bin/bash"         18 seconds ago      Up 17 seconds                           zealous_swirles
$ docker exec -i 69d1 bash
ls
bin
boot
dev
...
$ docker exec -it 69d1 bash
root@69d137adef7a:/#
```

如果从这个 stdin 中 exit，不会导致容器的停止。这就是为什么推荐大家使用`docker exec`的原因。

> 更多参数说明请使用`docker exec --help`查看。


## 删除容器

可以使用`docker container rm`来删除一个处于终止状态的容器。例如:

```shell
$ docker container rm  trusting_newton
trusting_newton
```

也可用使用`docker rm`容器名来删除，如果要删除一个运行中的容器，可以添加`-f`参数。Docker 会发送 `SIGKILL`信号给容器。
用`docker container ls -a (或者docker ps -a)`命令可以查看所有已经创建的包括终止状态的容器，如果数量太多要一个个删除可能会很麻烦，用下面的命令可以清理掉所有处于终止状态的容器。

```shell
$ docker container prune
```

或者

```shell
$ docker ps -aq
```

## 删除本地镜像

如果要删除本地的镜像，可以使用`docker image rm·命令，其格式为：

```shell
$ docker image rm [选项] <镜像1> [<镜像2> ...]
```

或者

```shell
$ docker rmi 镜像名
```

或者用 ID、镜像名、摘要删除镜像
其中，<镜像> 可以是 镜像短 ID、镜像长 ID、镜像名 或者 镜像摘要。
比如我们有这么一些镜像：

```shell
$ docker image ls
REPOSITORY                  TAG                 IMAGE ID            CREATED             SIZE
centos                      latest              0584b3d2cf6d        3 weeks ago         196.5 MB
redis                       alpine              501ad78535f0        3 weeks ago         21.03 MB
docker                      latest              cf693ec9b5c7        3 weeks ago         105.1 MB
nginx                       latest              e43d811ce2f4        5 weeks ago         181.5 MB
```

我们可以用镜像的完整 ID，也称为 长 ID，来删除镜像。使用脚本的时候可能会用长 ID，但是人工输入就太累了，所以更多的时候是用 短 ID 来删除镜像。`docker image ls`默认列出的就已经是短 ID 了，一般取前3个字符以上，只要足够区分于别的镜像就可以了。
比如这里，如果我们要删除**redis:alpine**镜像，可以执行：

```shell
$ docker image rm 501
Untagged: redis:alpine
Untagged: redis@sha256:f1ed3708f538b537eb9c2a7dd50dc90a706f7debd7e1196c9264edeea521a86d
Deleted: sha256:501ad78535f015d88872e13fa87a828425117e3d28075d0c117932b05bf189b7
Deleted: sha256:96167737e29ca8e9d74982ef2a0dda76ed7b430da55e321c071f0dbff8c2899b
Deleted: sha256:32770d1dcf835f192cafd6b9263b7b597a1778a403a109e2cc2ee866f74adf23
Deleted: sha256:127227698ad74a5846ff5153475e03439d96d4b1c7f2a449c7a826ef74a2d2fa
Deleted: sha256:1333ecc582459bac54e1437335c0816bc17634e131ea0cc48daa27d32c75eab3
Deleted: sha256:4fc455b921edf9c4aea207c51ab39b10b06540c8b4825ba57b3feed1668fa7c7
```

我们也可以用镜像名，也就是 <仓库名>:<标签>，来删除镜像。

```shell
$ docker image rm centos
Untagged: centos:latest
Untagged: centos@sha256:b2f9d1c0ff5f87a4743104d099a3d561002ac500db1b9bfa02a783a46e0d366c
Deleted: sha256:0584b3d2cf6d235ee310cf14b54667d889887b838d3f3d3033acd70fc3c48b8a
Deleted: sha256:97ca462ad9eeae25941546209454496e1d66749d53dfa2ee32bf1faabd239d38
```

## 测试java代码

```java
package com.guonl.config;

import com.guonl.interceptor.AuthInterceptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.Ordered;
import org.springframework.web.servlet.config.annotation.InterceptorRegistry;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.ViewControllerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by guonl
 * Date 2020/7/21 3:14 PM
 * Description:
 */
@Configuration
public class WebMvcConfig implements WebMvcConfigurer {

    @Autowired
    private AuthInterceptor authInterceptor;

    private static final List<String> excludeList;

    static {
        excludeList = new ArrayList<>();
        excludeList.add("/ajax/**");
        excludeList.add("/css/**");
        excludeList.add("/fonts/**");
        excludeList.add("/img/**");
        excludeList.add("/js/**");
        excludeList.add("/**/*.js");
        excludeList.add("/**/*.css");
        excludeList.add("/login");//登录
        excludeList.add("/test/**");
    }

    /**
     * 拦截某个请求跳转固定位置
     * @param registry
     */
    @Override
    public void addViewControllers(ViewControllerRegistry registry) {
        registry.addViewController("/").setViewName("forward:index");
        registry.addViewController("/index.html").setViewName("forward:index");
        registry.setOrder(Ordered.HIGHEST_PRECEDENCE);

    }

    /**
     * 添加自定义拦截器
     */
    @Override
    public void addInterceptors(InterceptorRegistry registry) {

        registry.addInterceptor(authInterceptor)
                .addPathPatterns("/**")//拦截的访问路径，拦截所有
                .excludePathPatterns(excludeList);//排除的请求路径，排除静态资源路径
    }
}


```
