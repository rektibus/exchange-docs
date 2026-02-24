<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Public Rest API for Binance](#public-rest-api-for-binance)
  - [General API Information](#general-api-information)
  - [HTTP Return Codes](#http-return-codes)
  - [Error Codes](#error-codes)
  - [General Information on Endpoints](#general-information-on-endpoints)
  - [LIMITS](#limits)
    - [General Info on Limits](#general-info-on-limits)
    - [IP Limits](#ip-limits)
    - [Unfilled Order Count](#unfilled-order-count)
  - [Data Sources](#data-sources)
  - [Request Security](#request-security)
    - [SIGNED Endpoint security](#signed-endpoint-security)
      - [Signature Case Sensitivity](#signature-case-sensitivity)
    - [Timing security](#timing-security)
    - [SIGNED Endpoint Examples for POST /api/v3/order](#signed-endpoint-examples-for-post-apiv3order)
      - [HMAC Keys](#hmac-keys)
      - [RSA Keys](#rsa-keys)
      - [Ed25519 Keys](#ed25519-keys)
- [Public API Endpoints](#public-api-endpoints)
  - [General endpoints](#general-endpoints)
    - [Test connectivity](#test-connectivity)
    - [Check server time](#check-server-time)
    - [Exchange information](#exchange-information)
  - [Market Data endpoints](#market-data-endpoints)
    - [Order book](#order-book)
    - [Recent trades list](#recent-trades-list)
    - [Old trade lookup](#old-trade-lookup)
    - [Compressed/Aggregate trades list](#compressedaggregate-trades-list)
    - [Kline/Candlestick data](#klinecandlestick-data)
    - [UIKlines](#uiklines)
    - [Current average price](#current-average-price)
    - [24hr ticker price change statistics](#24hr-ticker-price-change-statistics)
    - [Trading Day Ticker](#trading-day-ticker)
    - [Symbol price ticker](#symbol-price-ticker)
    - [Symbol order book ticker](#symbol-order-book-ticker)
    - [Rolling window price change statistics](#rolling-window-price-change-statistics)
  - [Trading endpoints](#trading-endpoints)
    - [New order (TRADE)](#new-order-trade)
    - [Test new order (TRADE)](#test-new-order-trade)
    - [Cancel order (TRADE)](#cancel-order-trade)
    - [Cancel All Open Orders on a Symbol (TRADE)](#cancel-all-open-orders-on-a-symbol-trade)
    - [Cancel an Existing Order and Send a New Order (TRADE)](#cancel-an-existing-order-and-send-a-new-order-trade)
    - [Order Amend Keep Priority (TRADE)](#order-amend-keep-priority-trade)
    - [Order lists](#order-lists)
      - [New OCO - Deprecated (TRADE)](#new-oco---deprecated-trade)
      - [New Order list - OCO (TRADE)](#new-order-list---oco-trade)
      - [New Order list - OTO (TRADE)](#new-order-list---oto-trade)
      - [New Order list - OTOCO (TRADE)](#new-order-list---otoco-trade)
      - [New Order List - OPO (TRADE)](#new-order-list---opo-trade)
      - [New Order List - OPOCO (TRADE)](#new-order-list---opoco-trade)
      - [Cancel Order list (TRADE)](#cancel-order-list-trade)
    - [SOR](#sor)
      - [New order using SOR (TRADE)](#new-order-using-sor-trade)
      - [Test new order using SOR (TRADE)](#test-new-order-using-sor-trade)
  - [Account Endpoints](#account-endpoints)
    - [Account information (USER_DATA)](#account-information-user_data)
    - [Query order (USER_DATA)](#query-order-user_data)
    - [Current open orders (USER_DATA)](#current-open-orders-user_data)
    - [All orders (USER_DATA)](#all-orders-user_data)
    - [Query Order list (USER_DATA)](#query-order-list-user_data)
    - [Query all Order lists (USER_DATA)](#query-all-order-lists-user_data)
    - [Query Open Order lists (USER_DATA)](#query-open-order-lists-user_data)
    - [Account trade list (USER_DATA)](#account-trade-list-user_data)
    - [Query Unfilled Order Count (USER_DATA)](#query-unfilled-order-count-user_data)
    - [Query Prevented Matches (USER_DATA)](#query-prevented-matches-user_data)
    - [Query Allocations (USER_DATA)](#query-allocations-user_data)
    - [Query Commission Rates (USER_DATA)](#query-commission-rates-user_data)
    - [Query Order Amendments (USER_DATA)](#query-order-amendments-user_data)
    - [Query relevant filters (USER_DATA)](#query-relevant-filters-user_data)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Public Rest API for Binance

## General API Information
* The following base endpoints are available. Please use whichever works best for your setup:
  * **https://api.binance.com**
  * **https://api-gcp.binance.com**
  * **https://api1.binance.com**
  * **https://api2.binance.com**
  * **https://api3.binance.com**
  * **https://api4.binance.com**
* The last 4 endpoints in the point above (`api1`-`api4`) should give better performance but have less stability.
* Responses are in JSON by default. To receive responses in SBE, refer to the [SBE FAQ](./faqs/sbe_faq.md) page.
* If your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
* Some endpoints may return asset and/or symbol names containing non-ASCII characters encoded in UTF-8 even if the request did not contain non-ASCII characters.
* Data is returned in **chronological order**, unless noted otherwise.
  * Without `startTime` or `endTime`, returns the most recent items up to the limit.
  * With `startTime`, returns oldest items from `startTime` up to the limit.
  * With `endTime`, returns most recent items up to `endTime` and the limit.
  * With both, behaves like `startTime` but does not exceed `endTime`.
* All time and timestamp related fields in the JSON responses are in **milliseconds by default.** To receive the information in microseconds, please add the header `X-MBX-TIME-UNIT:MICROSECOND` or `X-MBX-TIME-UNIT:microsecond`.
* We support HMAC, RSA, and Ed25519 keys. For more information, please see [API Key types](faqs/api_key_types.md).
* Timestamp parameters (e.g. `startTime`, `endTime`, `timestamp`) can be passed in milliseconds or microseconds.
* For APIs that only send public market data, please use the base endpoint **https://data-api.binance.vision**. Please refer to [Market Data Only](./faqs/market_data_only.md) page.
* If there are enums or terms you want clarification on, please see the [SPOT Glossary](faqs/spot_glossary.md) for more information.
* APIs have a timeout of 10 seconds when processing a request. If a response from the Matching Engine takes longer than this, the API responds with "Timeout waiting for response from backend server. Send status unknown; execution status unknown." [(-1007 TIMEOUT)](errors.md#-1007-timeout)
  * This does not always mean that the request failed in the Matching Engine.
  * If the status of the request has not appeared in [User Data Stream](user-data-stream.md), please perform an API query for its status.
* **Please avoid SQL keywords in requests** as they may trigger a security block by a WAF (Web Application Firewall) rule. See https://www.binance.com/en/support/faq/detail/360004492232 for more details.
* If your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
* Some endpoints may return asset and/or symbol names containing non-ASCII characters encoded in UTF-8 even if the request did not contain non-ASCII characters.

## HTTP Return Codes

* HTTP `4XX` return codes are used for malformed requests; the issue is on the sender's side.
* HTTP `403` return code is used when a WAF (Web Application Firewall) rule has been violated. This can indicate a rate limit violation or a security block. See https://www.binance.com/en/support/faq/detail/360004492232 for more details.
* HTTP `409` return code is used when a cancelReplace order partially succeeds. (i.e. if the cancellation of the order fails but the new order placement succeeds.)
* HTTP `429` return code is used when breaking a request rate limit.
* HTTP `418` return code is used when an IP has been auto-banned for continuing to send requests after receiving `429` codes.
* HTTP `5XX` return codes are used for internal errors; the issue is on Binance's side.
  It is important to **NOT** treat this as a failure operation; the execution status is
  **UNKNOWN** and could have been a success.


## Error Codes
* Any endpoint can return an ERROR

Sample Payload below:
```javascript
{
  "code": -1121,
  "msg": "Invalid symbol."
}
```
* Specific error codes and messages are defined in [Errors Codes](./errors.md).

## General Information on Endpoints
* For `GET` endpoints, parameters must be sent as a `query string`.
* For `POST`, `PUT`, and `DELETE` endpoints, the parameters may be sent as a
  `query string` or in the `request body` with content type
  `application/x-www-form-urlencoded`. You may mix parameters between both the
  `query string` and `request body` if you wish to do so.
* Parameters may be sent in any order.
* If a parameter sent in both the `query string` and `request body`, the
  `query string` parameter will be used.

## LIMITS

### General Info on Limits
* The following `intervalLetter` values for headers:
    * SECOND => S
    * MINUTE => M
    * HOUR => H
    * DAY => D
* `intervalNum` describes the amount of the interval. For example, `intervalNum` 5 with `intervalLetter` M means "Every 5 minutes".
* The `/api/v3/exchangeInfo` `rateLimits` array contains objects related to the exchange's `RAW_REQUESTS`, `REQUEST_WEIGHT`, and `ORDERS` rate limits. These are further defined in the `ENUM definitions` section under `Rate limiters (rateLimitType)`.
* Requests fail with HTTP status code 429 when you exceed the request rate limit.

### IP Limits
* Every request will contain `X-MBX-USED-WEIGHT-(intervalNum)(intervalLetter)` in the response headers which has the current used weight for the IP for all request rate limiters defined.
* Each route has a `weight` which determines for the number of requests each endpoint counts for. Heavier endpoints and endpoints that do operations on multiple symbols will have a heavier `weight`.
* When a 429 is received, it's your obligation as an API to back off and not spam the API.
* **Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban (HTTP status 418).**
* IP bans are tracked and **scale in duration** for repeat offenders, **from 2 minutes to 3 days**.
* A `Retry-After` header is sent with a 418 or 429 responses and will give the **number of seconds** required to wait, in the case of a 429, to prevent a ban, or, in the case of a 418, until the ban is over.
* **The limits on the API are based on the IPs, not the API keys.**

### Unfilled Order Count
* Every successful order response will contain a `X-MBX-ORDER-COUNT-(intervalNum)(intervalLetter)` header indicating how many orders you have placed for that interval. <br></br> To monitor this, refer to [`GET api/v3/rateLimit/order`](#query-unfilled-order-count).
* Rejected/unsuccessful orders are not guaranteed to have `X-MBX-ORDER-COUNT-**` headers in the response.
* If you have exceeded this, you will receive a 429 error with the `Retry-After` header.
* **Please note that if your orders are consistently filled by trades, you can continuously place orders on the API**. For more information, please see [Spot Unfilled Order Count Rules](./faqs/order_count_decrement.md).
* **The number of unfilled orders is tracked for each account.**

## Data Sources
* The API system is asynchronous, so some delay in the response is normal and expected.
* Each endpoint has a data source indicating where the data is being retrieved, and thus which endpoints have the most up-to-date response.

These are the three sources, ordered by least to most potential for delays in data updates.

  * **Matching Engine** - the data is from the Matching Engine
  * **Memory** - the data is from a server's local or external memory
  * **Database** - the data is taken directly from a database

Some endpoints can have more than 1 data source. (e.g. Memory => Database)
This means that the endpoint will check the first Data Source, and if it cannot find the value it's looking for it will check the next one.

## Request Security

* Each endpoint has a security type indicating required API key permissions, shown next to the endpoint name (e.g., [New order (TRADE)](#place-new-order-trade)).
* If unspecified, the security type is `NONE`.
* Except for `NONE`, all endpoints with a security type are considered `SIGNED` requests (i.e. including a `signature`), except for [listenKey management](#user-data-stream-requests).
* Secure endpoints require a valid API key to be specified and authenticated.
  * API keys can be created on the [API Management](https://www.binance.com/en/support/faq/360002502072) page of your Binance account.
  * **Both API key and secret key are sensitive.** Never share them with anyone.
    If you notice unusual activity in your account, immediately revoke all the keys and contact Binance support.
* API keys can be configured to allow access only to certain types of secure endpoints.
  * For example, you can have an API key with `TRADE` permission for trading,
    while using a separate API key with `USER_DATA` permission to monitor your order status.
  * By default, an API key cannot `TRADE`. You need to enable trading in API Management first.

Security type | Description
------------- | ------------
`NONE`        | Public market data
`TRADE`       | Trading on the exchange, placing and canceling orders
`USER_DATA`   | Private account information, such as order status and your trading history
`USER_STREAM` | Managing User Data Stream subscriptions

### SIGNED Endpoint security

* `SIGNED` endpoints require an additional parameter, `signature`, to be sent in the `query string` or `request body`.

#### Signature Case Sensitivity

* **HMAC:** Signatures generated using HMAC are **not case-sensitive**. This means the signature string can be verified regardless of letter casing.
* **RSA:** Signatures generated using RSA are **case-sensitive**.
* **Ed25519:** Signatures generated using Ed25519 are also **case-sensitive**

Please consult [SIGNED request example (HMAC)](#hmac-keys), [SIGNED request example (RSA)](#rsa-keys), and [SIGNED request example (Ed25519)](#ed25519-keys) on how to compute signature, depending on which API key type you are using.

<a id="timingsecurity"></a>

### Timing security
* `SIGNED` requests also require a `timestamp` parameter which should be the current timestamp either in milliseconds or microseconds. (See [General API Information](#general-api-information))
* An additional optional parameter, `recvWindow`, specifies for how long the request stays valid and may only be specified in milliseconds.
  * `recvWindow` supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
  * If `recvWindow` is not sent, **it defaults to 5000 milliseconds**.
  * Maximum `recvWindow` is 60000 milliseconds.
* Request processing logic is as follows:

```javascript
serverTime = getCurrentTime()
if (timestamp < (serverTime + 1 second) && (serverTime - timestamp) <= recvWindow) {
  // begin processing request
  serverTime = getCurrentTime()
  if (serverTime - timestamp) <= recvWindow {
    // forward request to Matching Engine
  } else {
    // reject request
  }
  // finish processing request
} else {
  // reject request
}
```

**Serious trading is about timing.** Networks can be unstable and unreliable,
which can lead to requests taking varying amounts of time to reach the
servers. With `recvWindow`, you can specify that the request must be
processed within a certain number of milliseconds or be rejected by the
server.


**It is recommended to use a small recvWindow of 5000 or less! The max cannot go beyond 60,000!**

### SIGNED Endpoint Examples for POST /api/v3/order

#### HMAC Keys

The signature payload of your request is the query string concatenated without separator to the HTTP body. Any non-ASCII character must be percent-encoded before signing.

Here is a step-by-step example of how to send a valid signed payload from the Linux command line using `echo`, `openssl`, and `curl`. There is one example with a symbol name comprised entirely of ASCII characters and one example with a symbol name containing non-ASCII characters.

Example API key and secret key:

Key | Value
------------ | ------------
`apiKey` | vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A
`secretKey` | NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j

**WARNING: DO NOT SHARE YOUR API KEY AND SECRET KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:

Parameter | Value
------------ | ------------
`symbol` | LTCBTC
`side` | BUY
`type` | LIMIT
`timeInForce` | GTC
`quantity` | 1
`price` | 0.1
`recvWindow` | 5000
`timestamp` | 1499827319559

Example of a request with a symbol name containing non-ASCII characters:

Parameter | Value
------------ | ------------
`symbol` | １２３４５６
`side` | BUY
`type` | LIMIT
`timeInForce` | GTC
`quantity` | 1
`price` | 0.1
`recvWindow` | 5000
`timestamp` | 1499827319559

**Step 1: Construct the signature payload**

1. Format parameters as `parameter=value` pairs separated by `&`.
2. Percent-encode the string.

For the first set of example parameters (ASCII only), the `parameter=value` string should look like this:

```console
symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559
```

After percent-encoding, the signature payload should look like this:

```console
symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559
```

For the second set of example parameters (some non-ASCII characters), the `parameter=value` string should look like this:

```console
symbol=１２３４５６&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559
```

After percent-encoding, the signature payload should look like this:

```console
symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559
```

**Step 2: Compute the signature**

1. Use the `secretKey` of your API key as the signing key for the HMAC-SHA-256 algorithm.
2. Sign the signature payload constructed in Step 1.
3. Encode the HMAC-SHA-256 output as a hex string.

Note that `secretKey` and the payload are **case-sensitive**, while the resulting signature value is case-insensitive.

**Example commands**

For the first set of example parameters (ASCII only):

```console
$ echo -n "symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"

c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71
```

For the second set of example parameters (some non-ASCII characters):

```console
$ echo -n "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559" | openssl dgst -sha256 -hmac "NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"

e1353ec6b14d888f1164ae9af8228a3dbd508bc82eb867db8ab6046442f33ef3
```

**Step 3: Add signature to the request**

Complete the request by adding the `signature` parameter to the query string.

For the first set of example parameters (ASCII only):

```console
curl -s -v -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=c8db56825ae71d6d79447849e617115f4a920fa2acdcab2b053c4b2838bd6b71"
```

For the second set of example parameters (some non-ASCII characters)

```console
curl -s -v -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559&signature=e1353ec6b14d888f1164ae9af8228a3dbd508bc82eb867db8ab6046442f33ef3"
```

Here is a sample Bash script performing all the steps above:

```bash
apiKey="vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A"
secretKey="NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j"

payload="symbol=LTCBTC&side=BUY&type=LIMIT&timeInForce=GTC&quantity=1&price=0.1&recvWindow=5000&timestamp=1499827319559"

# Sign the request

signature=$(echo -n "$payload" | openssl dgst -sha256 -hmac "$secretKey")
signature=${signature#*= }    # Keep only the part after the "= "

# Send the request

curl -H "X-MBX-APIKEY: $apiKey" -X POST "https://api.binance.com/api/v3/order?$payload&signature=$signature"

```

#### RSA Keys

The signature payload of your request is the query string concatenated without separator to the HTTP body. Any non-ASCII character must be percent-encoded before signing.

To get your API key, you need to upload your RSA Public Key to your account and a corresponding API key will be provided for you.

Only `PKCS#8` keys are supported.

There is one example with a symbol name comprised entirely of ASCII characters and one example with a symbol name containing non-ASCII characters.

These examples assume the private key is stored in the file `./test-prv-key.pem`.

Key | Value
------------ | ------------
`apiKey` | CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ

Example of request with a symbol name comprised entirely of ASCII characters:

Parameter | Value
------------ | ------------
`symbol` | BTCUSDT
`side` | SELL
`type` | LIMIT
`timeInForce` | GTC
`quantity` | 1
`price` | 0.2
`timestamp` | 1668481559918
`recvWindow` | 5000

Example of a request with a symbol name containing non-ASCII characters:

Parameter | Value
------------ | ------------
`symbol` | １２３４５６
`side` | SELL
`type` | LIMIT
`timeInForce` | GTC
`quantity` | 1
`price` | 0.2
`timestamp` | 1668481559918
`recvWindow` | 5000

**Step 1: Construct the signature payload**

1. Format parameters as `parameter=value` pairs separated by `&`.
2. Percent-encode the string.

For the first set of example parameters (ASCII only), the `parameter=value` string should look like this:

```console
symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000
```

After percent-encoding, the signature payload should look like this:

```console
symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000
```

For the second set of example parameters (some non-ASCII characters), the `parameter=value` string should look like this:

```console
symbol=１２３４５６=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000
```

After percent-encoding, the signature payload should look like this:

```console
symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000
```

**Step 2: Compute the signature**

1. Sign the signature payload constructed in Step 1 using the RSASSA-PKCS1-v1_5 algorithm with SHA-256 hash function.
2. Encode the output in base64.

Note that the payload and the resulting `signature` are **case-sensitive**.

For the first set of example parameters (ASCII only):

```console
$  echo -n 'symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A | tr -d '\n'
HZ8HOjiJ1s/igS9JA+n7+7Ti/ihtkRF5BIWcPIEluJP6tlbFM/Bf44LfZka/iemtahZAZzcO9TnI5uaXh3++lrqtNonCwp6/245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH+XxaCmR0WcvlKjNQnp12/eKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang/1WOq+Jaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT/fNnMRxFc7u+j3qI//5yuGuu14KR0MuQKKCSpViieD+fIti46sxPTsjSemoUKp0oXA==
```

For the second set of example parameters (some non-ASCII characters):

```console
$  echo -n 'symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000' | openssl dgst -sha256 -sign ./test-prv-key.pem | openssl enc -base64 -A | tr -d '\n'

qJtv66wyp/1mZE+mIFAAMUoTe8xkmLN7/eAZjuC9x1ocxovItHLl/sNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M+JNIMz5UFxfeA53rXjFlvsyH1Sig+OuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C/QMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt/GuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng==
```

3. Percent-encode the base64 string.

For the first set of example parameters (ASCII only):

```console
HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D
```

For the second set of example parameters (some non-ASCII characters):

```console
qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D
```

**Step 3: Add signature to the request**

Complete the request by adding the `signature` parameter to the query string.

For the first set of example parameters (ASCII only):

```console
curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HZ8HOjiJ1s%2FigS9JA%2Bn7%2B7Ti%2FihtkRF5BIWcPIEluJP6tlbFM%2FBf44LfZka%2FiemtahZAZzcO9TnI5uaXh3%2B%2BlrqtNonCwp6%2F245UFWkiW1elpgtVAmJPbogcAv6rSlokztAfWk296ZJXzRDYAtzGH0gq7CgSJKfH%2BXxaCmR0WcvlKjNQnp12%2FeKXJYO4tDap8UCBLuyxDnR7oJKLHQHJLP0r0EAVOOSIbrFang%2F1WOq%2BJaq4Efc4XpnTgnwlBbWTmhWDR1pvS9iVEzcSYLHT%2FfNnMRxFc7u%2Bj3qI%2F%2F5yuGuu14KR0MuQKKCSpViieD%2BfIti46sxPTsjSemoUKp0oXA%3D%3D'
```

For the second set of example parameters (some non-ASCII characters):

```console
curl -H "X-MBX-APIKEY: CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ" -X POST 'https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D'
```

Here is a sample Bash script performing all the steps above:

```bash
function rawurlencode {
  local string="${1}"
  local strlen=${#string}
  local encoded=""
  local pos c o

  for (( pos=0 ; pos<strlen ; pos++ )); do
     c=${string:$pos:1}
     case "$c" in
        [-_.~a-zA-Z0-9] ) o="${c}" ;;
        * )               printf -v o '%%%02x' "'$c"
     esac
     encoded+="${o}"
  done
  echo "${encoded}"
}

API_KEY="put your own API Key here"
PRIVATE_KEY_PATH="test-prv-key.pem"
# Set up the request:
API_METHOD="POST"
API_CALL="api/v3/order"
API_PARAMS="symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2"
# Sign the request:
timestamp=$(date +%s000)
api_params_with_timestamp="$API_PARAMS&timestamp=$timestamp"

rawSignature=$(echo -n $api_params_with_timestamp | openssl dgst -keyform PEM -sha256 -sign $PRIVATE_KEY_PATH | openssl enc -base64 | tr -d '\n')

# Percent-encode the signature
signature=$(rawurlencode "$rawSignature")

# Send the request:
curl -H "X-MBX-APIKEY: $API_KEY" -X "$API_METHOD" \
    "https://api.binance.com/$API_CALL?$api_params_with_timestamp" \
    --data-urlencode "signature=$signature"
```

#### Ed25519 Keys

**Note: It is highly recommended to use Ed25519 API keys as it should provide the best performance and security out of all supported key types.**

The signature payload of your request is the query string concatenated without separator to the HTTP body. Any non-ASCII character must be percent-encoded before signing.

There is one example with a symbol name comprised entirely of ASCII characters and one example with a symbol name containing non-ASCII characters.

These examples assume the private key is stored in the file `./test-prv-key.pem`.

Key | Value
------------ | ------------
`apiKey` | 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO

Example of request with a symbol name comprised entirely of ASCII characters.

Parameter     | Value
------------  | ------------
`symbol`      | BTCUSDT
`side`        | SELL
`type`        | LIMIT
`timeInForce` | GTC
`quantity`    | 1
`price`       | 0.2
`timestamp`   | 1668481559918
`recvWindow`  | 5000

Example of a request with a symbol name containing non-ASCII characters.

Parameter     | Value
------------  | ------------
`symbol`      | １２３４５６
`side`        | SELL
`type`        | LIMIT
`timeInForce` | GTC
`quantity`    | 1
`price`       | 0.2
`timestamp`   | 1668481559918
`recvWindow`  | 5000


**Step 1: Construct the signature payload**

1. Format parameters as `parameter=value` pairs separated by `&`.
2. Percent-encode the string.

For the first set of example parameters (ASCII only), the `parameter=value` string should look like this:

```console
symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000
```

After percent-encoding, the signature payload should look like this:

```console
symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000
```

For the second set of example parameters (some non-ASCII characters), the `parameter=value` string should look like this:

```console
symbol=１２３４５６&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000
```

After percent-encoding, the signature payload should look like this:

```console
symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000
```

**Step 2: Compute the signature**

1. Sign the payload.
2. Encode the output as a base64 string.

Note that the payload and the resulting `signature` are **case-sensitive**.

For the first set of example parameters (ASCII only):

```console
echo -n "symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000" | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'

HaZnek7KOGa/k5+f6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD/DYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt+BZxEHBN9OYQKpoe0+ovjnXyVOaH8VUKhE/ghUWnThrXJr+hmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr/r+8n6qeEKMYB5j/1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61/ZJv5BTJpa+z5Lv1W9v6jHQWRX2O8uaG3KU/lR3spR7+oGlWOw=
```

For the second set of example parameters (some non-ASCII characters):

```console
echo -n "symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000" | openssl dgst -keyform PEM -sha256 -sign ./test-prv-key.pem | openssl enc -base64 | tr -d '\n'

qJtv66wyp/1mZE+mIFAAMUoTe8xkmLN7/eAZjuC9x1ocxovItHLl/sNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M+JNIMz5UFxfeA53rXjFlvsyH1Sig+OuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C/QMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt/GuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng==
```

3. Percent-encode the base64 string.

For the first set of example parameters (ASCII only):

```console
HaZnek7KOGa%2Fk5%2Bf6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD%2FDYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt%2BBZxEHBN9OYQKpoe0%2BovjnXyVOaH8VUKhE%2FghUWnThrXJr%2BhmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr%2Fr%2B8n6qeEKMYB5j%2F1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61%2FZJv5BTJpa%2Bz5Lv1W9v6jHQWRX2O8uaG3KU%2FlR3spR7%2BoGlWOw%3D
```

For the second set of example parameters (some non-ASCII characters):

```console
qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D
```

**Step 3: Add signature to the request**

Complete the request by adding the `signature` parameter to the query string.

For the first set of example parameters (ASCII only):

```console
curl -H "X-MBX-APIKEY: 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO" -X POST 'https://api.binance.com/api/v3/order?symbol=BTCUSDT&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=HaZnek7KOGa%2Fk5%2Bf6Q1nw8lzMUpo36mRVvvLHCMUCXxlmdQQGZge1luAUKnleD%2FDYeD19YrqzeHbb6xU3MkSIXKhAO1MaYq48uGVYb3vJScEZVOutgMInrZzUcCWNulNkfcbmExSiymCZ5xQBw5QDuzpuDFqRZ1Xt%2BBZxEHBN9OYQKpoe0%2BovjnXyVOaH8VUKhE%2FghUWnThrXJr%2BhmSc5t7ggjiVPQc7pGn3qSNGCQwdpkQC9GHMr%2Fr%2B8n6qeEKMYB5j%2F1wC4d8Jae8FQiU8xcXR0NlUgV2LAw61%2FZJv5BTJpa%2Bz5Lv1W9v6jHQWRX2O8uaG3KU%2FlR3spR7%2BoGlWOw%3D'
```

For the second set of example parameters (some non-ASCII characters):

```console
curl -H "X-MBX-APIKEY: 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO" -X POST 'https://api.binance.com/api/v3/order?symbol=%EF%BC%91%EF%BC%92%EF%BC%93%EF%BC%94%EF%BC%95%EF%BC%96&&side=SELL&type=LIMIT&timeInForce=GTC&quantity=1&price=0.2&timestamp=1668481559918&recvWindow=5000&signature=qJtv66wyp%2F1mZE%2BmIFAAMUoTe8xkmLN7%2FeAZjuC9x1ocxovItHLl%2FsNK7Wq8QjgiHqGn0bb8P7yVvGBEd1gFe71NQ8aM0M%2BJNIMz5UFxfeA53rXjFlvsyH1Sig%2BOuO9Nz5nhCaJ6bEfj2iuv7w27pB3L8MVqmoCi6D9C%2FQMiLxtPaR70CxtnvoOlIgPmpv2bQy029A31NEK19ieVLkoyp1EUkXRaX3v0mohx8yMnUG1dhX9nUg3Oy8TYZ03DQy7kHDGkMKisNX7rt%2FGuGx1HIgjFclDGLsbAFIodvSLjm9FbseasMELoxlAJDlwRnW8zo5sQmL0Fz7ao935QBynrng%3D%3D'
```

Here is a sample Python script performing all the steps above:

```python
#!/usr/bin/env python3

import base64
import requests
import time
import urllib.parse
from cryptography.hazmat.primitives.serialization import load_pem_private_key

# Set up authentication
API_KEY='put your own API Key here'
PRIVATE_KEY_PATH='test-prv-key.pem'

# Load the private key.
# In this example the key is expected to be stored without encryption,
# but we recommend using a strong password for improved security.
with open(PRIVATE_KEY_PATH, 'rb') as f:
    private_key = load_pem_private_key(data=f.read(), password=None)

# Set up the request parameters
params = {
    'symbol':       'BTCUSDT',
    'side':         'SELL',
    'type':         'LIMIT',
    'timeInForce':  'GTC',
    'quantity':     '1.0000000',
    'price':        '0.20',
}

# Timestamp the request
timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds
params['timestamp'] = timestamp

# Sign the request
payload = urllib.parse.urlencode(params, encoding='UTF-8')
signature = base64.b64encode(private_key.sign(payload.encode('ASCII')))
params['signature'] = signature

# Send the request
headers = {
    'X-MBX-APIKEY': API_KEY,
}
response = requests.post(
    'https://api.binance.com/api/v3/order',
    headers=headers,
    data=params,
)
print(response.json())
```

# Public API Endpoints

## General endpoints

### Test connectivity
```
GET /api/v3/ping
```
Test connectivity to the Rest API.

**Weight:**
1

**Parameters:**
NONE

**Data Source:**
Memory

**Response:**
```javascript
{}
```

### Check server time
```
GET /api/v3/time
```
Test connectivity to the Rest API and get the current server time.

**Weight:**
1

**Parameters:**
NONE

**Data Source:**
Memory

**Response:**
```javascript
{
  "serverTime": 1499827319559
}
```

<a id="exchangeInfo"></a>

### Exchange information
```
GET /api/v3/exchangeInfo
```
Current exchange trading rules and symbol information

**Weight:**
20

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol |STRING| No| Example: curl -X GET "https://api.binance.com/api/v3/exchangeInfo?symbol=BNBBTC"
symbols |ARRAY OF STRING|No| Examples: curl -X GET "https://api.binance.com/api/v3/exchangeInfo?symbols=%5B%22BNBBTC%22,%22BTCUSDT%22%5D" <br/> or <br/> curl -g -X  GET 'https://api.binance.com/api/v3/exchangeInfo?symbols=["BTCUSDT","BNBBTC"]'
permissions |ENUM|No|Examples: curl -X GET "https://api.binance.com/api/v3/exchangeInfo?permissions=SPOT" <br/> or <br/> curl -X GET "https://api.binance.com/api/v3/exchangeInfo?permissions=%5B%22MARGIN%22%2C%22LEVERAGED%22%5D" <br/> or <br/> curl -g -X GET 'https://api.binance.com/api/v3/exchangeInfo?permissions=["MARGIN","LEVERAGED"]' |
showPermissionSets|BOOLEAN|No|Controls whether the content of the `permissionSets` field is populated or not. Defaults to `true`
symbolStatus|ENUM|No|Filters for symbols that have this `tradingStatus`. Valid values: `TRADING`, `HALT`, `BREAK` <br> Cannot be used in combination with `symbols` or `symbol`.|

**Notes:**
* If the value provided to `symbol` or `symbols` do not exist, the endpoint will throw an error saying the symbol is invalid.
* All parameters are optional.
* `permissions` can support single or multiple values (e.g. `SPOT`, `["MARGIN","LEVERAGED"]`). This cannot be used in combination with `symbol` or `symbols`.
* If `permissions` parameter not provided, all symbols that have either `SPOT`, `MARGIN`, or `LEVERAGED` permission will be exposed.
  * To display symbols with any permission you need to specify them explicitly in `permissions`: (e.g. `["SPOT","MARGIN",...]`.). See [Account and Symbol Permissions](enums.md#account-and-symbol-permissions) for the full list.

<a id="examples-of-symbol-permissions-interpretation-from-the-response"></a>

**Examples of Symbol Permissions Interpretation from the Response:**

* `[["A","B"]]` means you may place an order if your account has either permission "A" **or** permission "B".
* `[["A"],["B"]]` means you can place an order if your account has permission "A" **and** permission "B".
* `[["A"],["B","C"]]` means you can place an order if your account has permission "A" **and** permission "B" or permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission "B" and permission "C".)

**Data Source:**
Memory

**Response:**
```javascript
{
  "timezone": "UTC",
  "serverTime": 1565246363776,
  "rateLimits": [
    {
      // These are defined in the `ENUM definitions` section under `Rate Limiters (rateLimitType)`.
      // All limits are optional
    }
  ],
  "exchangeFilters": [
    // These are the defined filters in the `Filters` section.
    // All filters are optional.
  ],
  "symbols": [
    {
      "symbol": "ETHBTC",
      "status": "TRADING",
      "baseAsset": "ETH",
      "baseAssetPrecision": 8,
      "quoteAsset": "BTC",
      "quotePrecision": 8, // will be removed in future api versions (v4+)
      "quoteAssetPrecision": 8,
      "baseCommissionPrecision": 8,
      "quoteCommissionPrecision": 8,
      "orderTypes": [
        "LIMIT",
        "LIMIT_MAKER",
        "MARKET",
        "STOP_LOSS",
        "STOP_LOSS_LIMIT",
        "TAKE_PROFIT",
        "TAKE_PROFIT_LIMIT"
      ],
      "icebergAllowed": true,
      "ocoAllowed": true,
      "otoAllowed": true,
      "opoAllowed": true,
      "quoteOrderQtyMarketAllowed": true,
      "allowTrailingStop": false,
      "cancelReplaceAllowed":false,
      "amendAllowed":false,
      "pegInstructionsAllowed": true,
      "isSpotTradingAllowed": true,
      "isMarginTradingAllowed": true,
      "filters": [
        // These are defined in the Filters section.
        // All filters are optional
      ],
      "permissions": [],
      "permissionSets": [
        [
          "SPOT",
          "MARGIN"
        ]
      ],
      "defaultSelfTradePreventionMode": "NONE",
      "allowedSelfTradePreventionModes": [
        "NONE"
      ]
    }
  ],
  // Optional field. Present only when SOR is available.
  // https://github.com/binance/binance-spot-api-docs/blob/master/faqs/sor_faq.md
  "sors": [
    {
      "baseAsset": "BTC",
      "symbols": [
        "BTCUSDT",
        "BTCUSDC"
      ]
    }
  ]
}
```

## Market Data endpoints
### Order book
```
GET /api/v3/depth
```

**Weight:**
Adjusted based on the limit:

|Limit|Request Weight
------|-------
1-100|  5
101-500| 25
501-1000| 50
1001-5000| 250

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
limit | INT | NO | Default: 100; Maximum: 5000. <br/> If limit > 5000, only 5000 entries will be returned.
symbolStatus|ENUM|NO|Filters for symbols that have this `tradingStatus`. <br/>A status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`.<br/> Valid values: `TRADING`, `HALT`, `BREAK`

**Data Source:**
Memory

**Response:**
```javascript
{
  "lastUpdateId": 1027024,
  "bids": [
    [
      "4.00000000",     // PRICE
      "431.00000000"    // QTY
    ]
  ],
  "asks": [
    [
      "4.00000200",
      "12.00000000"
    ]
  ]
}
```


### Recent trades list
```
GET /api/v3/trades
```
Get recent trades.

**Weight:**
25

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
limit | INT | NO | Default: 500; Maximum: 1000.

**Data Source:**
Memory

**Response:**
```javascript
[
  {
    "id": 28457,
    "price": "4.00000100",
    "qty": "12.00000000",
    "quoteQty": "48.000012",
    "time": 1499865549590,
    "isBuyerMaker": true,
    "isBestMatch": true
  }
]
```

### Old trade lookup
```
GET /api/v3/historicalTrades
```
Get older trades.

**Weight:**
25

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
limit | INT | NO | Default: 500; Maximum: 1000.
fromId | LONG | NO | TradeId to fetch from. Default gets most recent trades.

**Data Source:**
Database

**Response:**
```javascript
[
  {
    "id": 28457,
    "price": "4.00000100",
    "qty": "12.00000000",
    "quoteQty": "48.000012",
    "time": 1499865549590,
    "isBuyerMaker": true,
    "isBestMatch": true
  }
]
```

### Compressed/Aggregate trades list
```
GET /api/v3/aggTrades
```
Get compressed, aggregate trades. Trades that fill at the time, from the same taker order, with the same price will have the quantity aggregated.

**Weight:**
4

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
fromId | LONG | NO | ID to get aggregate trades from INCLUSIVE.
startTime | LONG | NO | Timestamp in ms to get aggregate trades from INCLUSIVE.
endTime | LONG | NO | Timestamp in ms to get aggregate trades until INCLUSIVE.
limit | INT | NO | Default: 500; Maximum: 1000.

* If fromId, startTime, and endTime are not sent, the most recent aggregate trades will be returned.

**Data Source:**
Database

**Response:**
```javascript
[
  {
    "a": 26129,         // Aggregate tradeId
    "p": "0.01633102",  // Price
    "q": "4.70443515",  // Quantity
    "f": 27781,         // First tradeId
    "l": 27781,         // Last tradeId
    "T": 1498793709153, // Timestamp
    "m": true,          // Was the buyer the maker?
    "M": true           // Was the trade the best price match?
  }
]
```
<a id="klines"></a>
### Kline/Candlestick data
```
GET /api/v3/klines
```
Kline/candlestick bars for a symbol.
Klines are uniquely identified by their open time.

**Weight:**
2

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
interval | ENUM | YES |
startTime | LONG | NO |
endTime | LONG | NO |
timeZone |STRING| NO| Default: 0 (UTC)
limit | INT | NO | Default: 500; Maximum: 1000.

<a id="kline-intervals"></a>
Supported kline intervals (case-sensitive):

Interval  | `interval` value
--------- | ----------------
seconds   | `1s`
minutes   | `1m`, `3m`, `5m`, `15m`, `30m`
hours     | `1h`, `2h`, `4h`, `6h`, `8h`, `12h`
days      | `1d`, `3d`
weeks     | `1w`
months    | `1M`

**Notes:**

* If `startTime` and `endTime` are not sent, the most recent klines are returned.
* Supported values for `timeZone`:
  * Hours and minutes (e.g. `-1:00`, `05:45`)
  * Only hours (e.g. `0`, `8`, `4`)
  * Accepted range is strictly [-12:00 to +14:00] inclusive
* If `timeZone` provided, kline intervals are interpreted in that timezone instead of UTC.
* Note that `startTime` and `endTime` are always interpreted in UTC, regardless of `timeZone`.

**Data Source:**
Database

**Response:**
```javascript
[
  [
    1499040000000,      // Kline open time
    "0.01634790",       // Open price
    "0.80000000",       // High price
    "0.01575800",       // Low price
    "0.01577100",       // Close price
    "148976.11427815",  // Volume
    1499644799999,      // Kline Close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    "0"                 // Unused field, ignore.
  ]
]
```
<a id="uiKlines"></a>
### UIKlines
```
GET /api/v3/uiKlines
```
The request is similar to klines having the same parameters and response.

`uiKlines` return modified kline data, optimized for presentation of candlestick charts.

**Weight:**
2

**Parameters:**

Name      | Type   | Mandatory    | Description
------    | ------ | ------------ | ------------
symbol    | STRING | YES          |
interval  | ENUM   | YES          |See [`klines`](#kline-intervals)
startTime | LONG   | NO           |
endTime   | LONG   | NO           |
timeZone  |STRING  | NO           | Default: 0 (UTC)
limit     | INT    | NO           | Default: 500; Maximum: 1000.

* If `startTime` and `endTime` are not sent, the most recent klines are returned.
* Supported values for `timeZone`:
  * Hours and minutes (e.g. `-1:00`, `05:45`)
  * Only hours (e.g. `0`, `8`, `4`)
  * Accepted range is strictly [-12:00 to +14:00] inclusive
* If `timeZone` provided, kline intervals are interpreted in that timezone instead of UTC.
* Note that `startTime` and `endTime` are always interpreted in UTC, regardless of `timeZone`.

**Data Source:**
Database

**Response:**
```javascript
[
  [
    1499040000000,      // Kline open time
    "0.01634790",       // Open price
    "0.80000000",       // High price
    "0.01575800",       // Low price
    "0.01577100",       // Close price
    "148976.11427815",  // Volume
    1499644799999,      // Kline close time
    "2434.19055334",    // Quote asset volume
    308,                // Number of trades
    "1756.87402397",    // Taker buy base asset volume
    "28.46694368",      // Taker buy quote asset volume
    "0"                 // Unused field. Ignore.
  ]
]
```

### Current average price
```
GET /api/v3/avgPrice
```
Current average price for a symbol.

**Weight:**
2

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |

**Data Source:**
Memory

**Response:**
```javascript
{
  "mins": 5,                    // Average price interval (in minutes)
  "price": "9.35751834",        // Average price
  "closeTime": 1694061154503    // Last trade time
}
```


### 24hr ticker price change statistics
```
GET /api/v3/ticker/24hr
```
24 hour rolling window price change statistics. **Careful** when accessing this with no symbol.

**Weight:**

<table>
<thead>
    <tr>
        <th>Parameter</th>
        <th>Symbols Provided</th>
        <th>Weight</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td rowspan="2">symbol</td>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>symbol parameter is omitted</td>
        <td>80</td>
    </tr>
    <tr>
        <td rowspan="4">symbols</td>
        <td>1-20</td>
        <td>2</td>
    </tr>
    <tr>
        <td>21-100</td>
        <td>40</td>
    </tr>
    <tr>
        <td>101 or more</td>
        <td>80</td>
    </tr>
    <tr>
        <td>symbols parameter is omitted</td>
        <td>80</td>
    </tr>
</tbody>
</table>

**Parameters:**

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>symbol</td>
        <td>STRING</td>
        <td>NO</td>
        <td rowspan="2">Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, tickers for all symbols will be returned in an array. <br/><br/>
         Examples of accepted format for the symbols parameter:
         ["BTCUSDT","BNBUSDT"] <br/>
         or <br/>
         %5B%22BTCUSDT%22,%22BNBUSDT%22%5D
        </td>
     </tr>
     <tr>
        <td>symbols</td>
        <td>STRING</td>
        <td>NO</td>
     </tr>
     <tr>
        <td>type</td>
        <td>ENUM</td>
        <td>NO</td>
        <td>Supported values: <tt>FULL</tt> or <tt>MINI</tt>. <br/>If none provided, the default is <tt>FULL</tt> </td>
     </tr>
     <tr>
        <td>symbolStatus</td>
        <td>ENUM</td>
        <td>NO</td>
        <td>Filters for symbols that have this <code>tradingStatus</code>.<br>For a single symbol, a status mismatch returns error <code>-1220 SYMBOL_DOES_NOT_MATCH_STATUS</code>. <br>For multiple or all symbols, non-matching ones are simply excluded from the response.<br>Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code> </td>
     </tr>
</tbody>
</table>

**Data Source:**
Memory

**Response - FULL:**
```javascript
{
  "symbol": "BNBBTC",
  "priceChange": "-94.99999800",
  "priceChangePercent": "-95.960",
  "weightedAvgPrice": "0.29628482",
  "prevClosePrice": "0.10002000",
  "lastPrice": "4.00000200",
  "lastQty": "200.00000000",
  "bidPrice": "4.00000000",
  "bidQty": "100.00000000",
  "askPrice": "4.00000200",
  "askQty": "100.00000000",
  "openPrice": "99.00000000",
  "highPrice": "100.00000000",
  "lowPrice": "0.10000000",
  "volume": "8913.30000000",
  "quoteVolume": "15.30000000",
  "openTime": 1499783499040,
  "closeTime": 1499869899040,
  "firstId": 28385,   // First tradeId
  "lastId": 28460,    // Last tradeId
  "count": 76         // Trade count
}
```
OR
```javascript
[
  {
    "symbol": "BNBBTC",
    "priceChange": "-94.99999800",
    "priceChangePercent": "-95.960",
    "weightedAvgPrice": "0.29628482",
    "prevClosePrice": "0.10002000",
    "lastPrice": "4.00000200",
    "lastQty": "200.00000000",
    "bidPrice": "4.00000000",
    "bidQty": "100.00000000",
    "askPrice": "4.00000200",
    "askQty": "100.00000000",
    "openPrice": "99.00000000",
    "highPrice": "100.00000000",
    "lowPrice": "0.10000000",
    "volume": "8913.30000000",
    "quoteVolume": "15.30000000",
    "openTime": 1499783499040,
    "closeTime": 1499869899040,
    "firstId": 28385,   // First tradeId
    "lastId": 28460,    // Last tradeId
    "count": 76         // Trade count
  }
]
```

**Response - MINI:**

```javascript
{
  "symbol":      "BNBBTC",          // Symbol Name
  "openPrice":   "99.00000000",     // Opening price of the Interval
  "highPrice":   "100.00000000",    // Highest price in the interval
  "lowPrice":    "0.10000000",      // Lowest  price in the interval
  "lastPrice":   "4.00000200",      // Closing price of the interval
  "volume":      "8913.30000000",   // Total trade volume (in base asset)
  "quoteVolume": "15.30000000",     // Total trade volume (in quote asset)
  "openTime":    1499783499040,     // Start of the ticker interval
  "closeTime":   1499869899040,     // End of the ticker interval
  "firstId":     28385,             // First tradeId considered
  "lastId":      28460,             // Last tradeId considered
  "count":       76                 // Total trade count
}
```

OR

```javascript
[
  {
    "symbol": "BNBBTC",
    "openPrice": "99.00000000",
    "highPrice": "100.00000000",
    "lowPrice": "0.10000000",
    "lastPrice": "4.00000200",
    "volume": "8913.30000000",
    "quoteVolume": "15.30000000",
    "openTime": 1499783499040,
    "closeTime": 1499869899040,
    "firstId": 28385,
    "lastId": 28460,
    "count": 76
  },
  {
    "symbol": "LTCBTC",
    "openPrice": "0.07000000",
    "highPrice": "0.07000000",
    "lowPrice": "0.07000000",
    "lastPrice": "0.07000000",
    "volume": "11.00000000",
    "quoteVolume": "0.77000000",
    "openTime": 1656908192899,
    "closeTime": 1656994592899,
    "firstId": 0,
    "lastId": 10,
    "count": 11
  }
]
```


### Trading Day Ticker

```
GET /api/v3/ticker/tradingDay
```
Price change statistics for a trading day.

**Weight:**

4 for each requested <tt>symbol</tt>. <br/><br/> The weight for this request will cap at 200 once the number of `symbols` in the request is more than 50.

**Parameters:**

<table>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Mandatory</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>symbol</td>
    <td rowspan="2">STRING</td>
    <td rowspan="2">YES</td>
    <td rowspan="2">Either <tt>symbol</tt> or <tt>symbols</tt> must be provided <br/><br/> Examples of accepted format for the <tt>symbols</tt> parameter: <br/> ["BTCUSDT","BNBUSDT"] <br/>or <br/>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D <br/><br/> The maximum number of <tt>symbols</tt> allowed in a request is 100.
    </td>
  </tr>
  <tr>
     <td>symbols</td>
  </tr>
  <tr>
     <td>timeZone</td>
     <td>STRING</td>
     <td>NO</td>
     <td>Default: 0 (UTC)</td>
  </tr>
  <tr>
      <td>type</td>
      <td>ENUM</td>
      <td>NO</td>
      <td>Supported values: <tt>FULL</tt> or <tt>MINI</tt>. <br/>If none provided, the default is <tt>FULL</tt> </td>
  </tr>
  <tr>
      <td>symbolStatus</td>
      <td>ENUM</td>
      <td>NO</td>
      <td>Filters for symbols that have this <code>tradingStatus</code>.<br>For a single symbol, a status mismatch returns error <code>-1220 SYMBOL_DOES_NOT_MATCH_STATUS</code>. <br>For multiple symbols, non-matching ones are simply excluded from the response.<br>Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code> </td>
  </tr>
</table>

**Notes:**

* Supported values for `timeZone`:
  * Hours and minutes (e.g. `-1:00`, `05:45`)
  * Only hours (e.g. `0`, `8`, `4`)

**Data Source:**
Database

**Response - FULL:**

With `symbol`:

```javascript
{
  "symbol":             "BTCUSDT",
  "priceChange":        "-83.13000000",         // Absolute price change
  "priceChangePercent": "-0.317",               // Relative price change in percent
  "weightedAvgPrice":   "26234.58803036",       // quoteVolume / volume
  "openPrice":          "26304.80000000",
  "highPrice":          "26397.46000000",
  "lowPrice":           "26088.34000000",
  "lastPrice":          "26221.67000000",
  "volume":             "18495.35066000",       // Volume in base asset
  "quoteVolume":        "485217905.04210480",   // Volume in quote asset
  "openTime":           1695686400000,
  "closeTime":          1695772799999,
  "firstId":            3220151555,             // Trade ID of the first trade in the interval
  "lastId":             3220849281,             // Trade ID of the last trade in the interval
  "count":              697727                  // Number of trades in the interval
}

```

With `symbols`:

```javascript
[
  {
    "symbol": "BTCUSDT",
    "priceChange": "-83.13000000",
    "priceChangePercent": "-0.317",
    "weightedAvgPrice": "26234.58803036",
    "openPrice": "26304.80000000",
    "highPrice": "26397.46000000",
    "lowPrice": "26088.34000000",
    "lastPrice": "26221.67000000",
    "volume": "18495.35066000",
    "quoteVolume": "485217905.04210480",
    "openTime": 1695686400000,
    "closeTime": 1695772799999,
    "firstId": 3220151555,
    "lastId": 3220849281,
    "count": 697727
  },
  {
    "symbol": "BNBUSDT",
    "priceChange": "2.60000000",
    "priceChangePercent": "1.238",
    "weightedAvgPrice": "211.92276958",
    "openPrice": "210.00000000",
    "highPrice": "213.70000000",
    "lowPrice": "209.70000000",
    "lastPrice": "212.60000000",
    "volume": "280709.58900000",
    "quoteVolume": "59488753.54750000",
    "openTime": 1695686400000,
    "closeTime": 1695772799999,
    "firstId": 672397461,
    "lastId": 672496158,
    "count": 98698
  }
]
```

**Response - MINI:**

With `symbol`:

```javascript
{
  "symbol":         "BTCUSDT",
  "openPrice":      "26304.80000000",
  "highPrice":      "26397.46000000",
  "lowPrice":       "26088.34000000",
  "lastPrice":      "26221.67000000",
  "volume":         "18495.35066000",       // Volume in base asset
  "quoteVolume":    "485217905.04210480",   // Volume in quote asset
  "openTime":       1695686400000,
  "closeTime":      1695772799999,
  "firstId":        3220151555,             // Trade ID of the first trade in the interval
  "lastId":         3220849281,             // Trade ID of the last trade in the interval
  "count":          697727                  // Number of trades in the interval
}
```

With `symbols`:

```javascript
[
  {
    "symbol": "BTCUSDT",
    "openPrice": "26304.80000000",
    "highPrice": "26397.46000000",
    "lowPrice": "26088.34000000",
    "lastPrice": "26221.67000000",
    "volume": "18495.35066000",
    "quoteVolume": "485217905.04210480",
    "openTime": 1695686400000,
    "closeTime": 1695772799999,
    "firstId": 3220151555,
    "lastId": 3220849281,
    "count": 697727
  },
  {
    "symbol": "BNBUSDT",
    "openPrice": "210.00000000",
    "highPrice": "213.70000000",
    "lowPrice": "209.70000000",
    "lastPrice": "212.60000000",
    "volume": "280709.58900000",
    "quoteVolume": "59488753.54750000",
    "openTime": 1695686400000,
    "closeTime": 1695772799999,
    "firstId": 672397461,
    "lastId": 672496158,
    "count": 98698
  }
]
```

### Symbol price ticker
```
GET /api/v3/ticker/price
```
Latest price for a symbol or symbols.

**Weight:**

<table>
<thead>
    <tr>
        <th>Parameter</th>
        <th>Symbols Provided</th>
        <th>Weight</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td rowspan="2">symbol</td>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>symbol parameter is omitted</td>
        <td>4</td>
    </tr>
    <tr>
        <td>symbols</td>
        <td>Any</td>
        <td>4</td>
    </tr>
</tbody>
</table>

**Parameters:**

<table>
<thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Mandatory</th>
      <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>symbol</td>
        <td>STRING</td>
        <td>NO</td>
        <td rowspan="2"> Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, prices for all symbols will be returned in an array. <br/><br/>
        Examples of accepted format for the symbols parameter:
         ["BTCUSDT","BNBUSDT"] <br/>
         or <br/>
         %5B%22BTCUSDT%22,%22BNBUSDT%22%5D</td>
    </tr>
    <tr>
        <td>symbols</td>
        <td>STRING</td>
        <td>NO</td>
    </tr>
    <tr>
        <td>symbolStatus</td>
        <td>ENUM</td>
        <td>NO</td>
        <td>Filters for symbols that have this <code>tradingStatus</code>.<br>For a single symbol, a status mismatch returns error <code>-1220 SYMBOL_DOES_NOT_MATCH_STATUS</code>. <br>For multiple or all symbols, non-matching ones are simply excluded from the response.<br>Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code> </td>
    </tr>
</tbody>
</table>


**Data Source:**
Memory

**Response:**
```javascript
{
  "symbol": "LTCBTC",
  "price": "4.00000200"
}
```
OR
```javascript
[
  {
    "symbol": "LTCBTC",
    "price": "4.00000200"
  },
  {
    "symbol": "ETHBTC",
    "price": "0.07946600"
  }
]
```

### Symbol order book ticker
```
GET /api/v3/ticker/bookTicker
```
Best price/qty on the order book for a symbol or symbols.

**Weight:**

<table>
<thead>
    <tr>
        <th>Parameter</th>
        <th>Symbols Provided</th>
        <th>Weight</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td rowspan="2">symbol</td>
        <td>1</td>
        <td>2</td>
    </tr>
    <tr>
        <td>symbol parameter is omitted</td>
        <td>4</td>
    </tr>
    <tr>
        <td>symbols</td>
        <td>Any</td>
        <td>4</td>
    </tr>
</tbody>
</table>

**Parameters:**

<table>
<thead>
    <tr>
      <th>Name</th>
      <th>Type</th>
      <th>Mandatory</th>
      <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td>symbol</td>
        <td>STRING</td>
        <td>NO</td>
        <td rowspan="2"> Parameter symbol and symbols cannot be used in combination. <br/> If neither parameter is sent, bookTickers for all symbols will be returned in an array.
         <br/><br/>
        Examples of accepted format for the symbols parameter:
         ["BTCUSDT","BNBUSDT"] <br/>
         or <br/>
         %5B%22BTCUSDT%22,%22BNBUSDT%22%5D</td>
    </tr>
    <tr>
        <td>symbols</td>
        <td>STRING</td>
        <td>NO</td>
    </tr>
    <tr>
        <td>symbolStatus</td>
        <td>ENUM</td>
        <td>NO</td>
        <td>Filters for symbols that have this <code>tradingStatus</code>.<br>For a single symbol, a status mismatch returns error <code>-1220 SYMBOL_DOES_NOT_MATCH_STATUS</code>. <br>For multiple or all symbols, non-matching ones are simply excluded from the response.<br>Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code> </td>
    </tr>
</tbody>
</table>


**Data Source:**
Memory

**Response:**
```javascript
{
  "symbol": "LTCBTC",
  "bidPrice": "4.00000000",
  "bidQty": "431.00000000",
  "askPrice": "4.00000200",
  "askQty": "9.00000000"
}
```
OR
```javascript
[
  {
    "symbol": "LTCBTC",
    "bidPrice": "4.00000000",
    "bidQty": "431.00000000",
    "askPrice": "4.00000200",
    "askQty": "9.00000000"
  },
  {
    "symbol": "ETHBTC",
    "bidPrice": "0.07946700",
    "bidQty": "9.00000000",
    "askPrice": "100000.00000000",
    "askQty": "1000.00000000"
  }
]
```

### Rolling window price change statistics
```
GET /api/v3/ticker
```

**Note:** This endpoint is different from the `GET /api/v3/ticker/24hr` endpoint.

The window used to compute statistics will be no more than 59999ms from the requested `windowSize`.

`openTime` for `/api/v3/ticker` always starts on a minute, while the `closeTime` is the current time of the request.
As such, the effective window will be up to 59999ms wider than `windowSize`.

E.g. If the `closeTime` is 1641287867099 (January 04, 2022 09:17:47:099 UTC) , and the `windowSize` is `1d`. the `openTime` will be: 1641201420000 (January 3, 2022, 09:17:00)

**Weight:**

4 for each requested <tt>symbol</tt> regardless of <tt>windowSize</tt>. <br/><br/> The weight for this request will cap at 200 once the number of `symbols` in the request is more than 50.

**Parameters:**

<table>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Mandatory</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>symbol</td>
    <td rowspan="2">STRING</td>
    <td rowspan="2">YES</td>
    <td rowspan="2">Either <tt>symbol</tt> or <tt>symbols</tt> must be provided <br/><br/> Examples of accepted format for the <tt>symbols</tt> parameter: <br/> ["BTCUSDT","BNBUSDT"] <br/>or <br/>%5B%22BTCUSDT%22,%22BNBUSDT%22%5D <br/><br/> The maximum number of <tt>symbols</tt> allowed in a request is 100.
    </td>
  </tr>
  <tr>
     <td>symbols</td>
  </tr>
  <tr>
     <td>windowSize</td>
     <td>ENUM</td>
     <td>NO</td>
     <td>Defaults to <tt>1d</tt> if no parameter provided <br/> Supported <tt>windowSize</tt> values: <br/> <tt>1m</tt>,<tt>2m</tt>....<tt>59m</tt> for minutes <br/> <tt>1h</tt>, <tt>2h</tt>....<tt>23h</tt> - for hours <br/> <tt>1d</tt>...<tt>7d</tt> - for days <br/><br/> Units cannot be combined (e.g. <tt>1d2h</tt> is not allowed)</td>
  </tr>
  <tr>
      <td>type</td>
      <td>ENUM</td>
      <td>NO</td>
      <td>Supported values: <tt>FULL</tt> or <tt>MINI</tt>. <br/>If none provided, the default is <tt>FULL</tt> </td>
  </tr>
  <tr>
      <td>symbolStatus</td>
      <td>ENUM</td>
      <td>NO</td>
      <td>Filters for symbols that have this <code>tradingStatus</code>.<br>For a single symbol, a status mismatch returns error <code>-1220 SYMBOL_DOES_NOT_MATCH_STATUS</code>.<br>For multiple symbols, non-matching ones are simply excluded from the response.<br>Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code></td>
  </tr>
</table>

**Data Source:**
Database

**Response - FULL:**

When using `symbol`:

```javascript
{
  "symbol":             "BNBBTC",
  "priceChange":        "-8.00000000",  // Absolute price change
  "priceChangePercent": "-88.889",      // Relative price change in percent
  "weightedAvgPrice":   "2.60427807",   // QuoteVolume / Volume
  "openPrice":          "9.00000000",
  "highPrice":          "9.00000000",
  "lowPrice":           "1.00000000",
  "lastPrice":          "1.00000000",
  "volume":             "187.00000000",
  "quoteVolume":        "487.00000000", // Sum of (price * volume) for all trades
  "openTime":           1641859200000,  // Open time for ticker window
  "closeTime":          1642031999999,  // Close time for ticker window
  "firstId":            0,              // Trade IDs
  "lastId":             60,
  "count":              61              // Number of trades in the interval
}

```
or

When using `symbols`:

```javascript
[
  {
    "symbol": "BTCUSDT",
    "priceChange": "-154.13000000",        // Absolute price change
    "priceChangePercent": "-0.740",        // Relative price change in percent
    "weightedAvgPrice": "20677.46305250",  // QuoteVolume / Volume
    "openPrice": "20825.27000000",
    "highPrice": "20972.46000000",
    "lowPrice": "20327.92000000",
    "lastPrice": "20671.14000000",
    "volume": "72.65112300",
    "quoteVolume": "1502240.91155513",     // Sum of (price * volume) for all trades
    "openTime": 1655432400000,             // Open time for ticker window
    "closeTime": 1655446835460,            // Close time for ticker window
    "firstId": 11147809,                   // Trade IDs
    "lastId": 11149775,
    "count": 1967                          // Number of trades in the interval
  },
  {
    "symbol": "BNBBTC",
    "priceChange": "0.00008530",
    "priceChangePercent": "0.823",
    "weightedAvgPrice": "0.01043129",
    "openPrice": "0.01036170",
    "highPrice": "0.01049850",
    "lowPrice": "0.01033870",
    "lastPrice": "0.01044700",
    "volume": "166.67000000",
    "quoteVolume": "1.73858301",
    "openTime": 1655432400000,
    "closeTime": 1655446835460,
    "firstId": 2351674,
    "lastId": 2352034,
    "count": 361
  }
]
```

**Response - MINI:**

When using `symbol`:

```javascript
{
    "symbol": "LTCBTC",
    "openPrice": "0.10000000",
    "highPrice": "2.00000000",
    "lowPrice": "0.10000000",
    "lastPrice": "2.00000000",
    "volume": "39.00000000",
    "quoteVolume": "13.40000000",  // Sum of (price * volume) for all trades
    "openTime": 1656986580000,     // Open time for ticker window
    "closeTime": 1657001016795,    // Close time for ticker window
    "firstId": 0,                  // Trade IDs
    "lastId": 34,
    "count": 35                    // Number of trades in the interval
}
```

OR

When using `symbols`:

```javascript
[
    {
        "symbol": "BNBBTC",
        "openPrice": "0.10000000",
        "highPrice": "2.00000000",
        "lowPrice": "0.10000000",
        "lastPrice": "2.00000000",
        "volume": "39.00000000",
        "quoteVolume": "13.40000000", // Sum of (price * volume) for all trades
        "openTime": 1656986880000,    // Open time for ticker window
        "closeTime": 1657001297799,   // Close time for ticker window
        "firstId": 0,                 // Trade IDs
        "lastId": 34,
        "count": 35                   // Number of trades in the interval
    },
    {
        "symbol": "LTCBTC",
        "openPrice": "0.07000000",
        "highPrice": "0.07000000",
        "lowPrice": "0.07000000",
        "lastPrice": "0.07000000",
        "volume": "33.00000000",
        "quoteVolume": "2.31000000",
        "openTime": 1656986880000,
        "closeTime": 1657001297799,
        "firstId": 0,
        "lastId": 32,
        "count": 33
    }
]
```

## Trading endpoints

### New order (TRADE)
```
POST /api/v3/order
```
Send in a new order.

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

**Weight:**
1

**Unfilled Order Count:**
1

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
side | ENUM | YES |Please see [Enums](enums.md#side) for supported values.
type | ENUM | YES |Please see [Enums](enums.md#ordertypes) for supported values.
timeInForce | ENUM | NO |Please see [Enums](enums.md#timeinforce) for supported values.
quantity | DECIMAL | NO |
quoteOrderQty|DECIMAL|NO|
price | DECIMAL | NO |
newClientOrderId | STRING | NO | A unique id among open orders. Automatically generated if not sent.<br/> Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.
strategyId |LONG| NO|
strategyType |INT| NO| The value cannot be less than `1000000`.
stopPrice | DECIMAL | NO | Used with `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.
trailingDelta|LONG|NO| See [Trailing Stop order FAQ](faqs/trailing-stop-faq.md).
icebergQty | DECIMAL | NO | Used with `LIMIT`, `STOP_LOSS_LIMIT`, and `TAKE_PROFIT_LIMIT` to create an iceberg order.
newOrderRespType | ENUM | NO | Set the response JSON. `ACK`, `RESULT`, or `FULL`; `MARKET` and `LIMIT` order types default to `FULL`, all other orders default to `ACK`.
selfTradePreventionMode |ENUM| NO | The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](enums.md#stpmodes).
pegPriceType | ENUM | NO | `PRIMARY_PEG` or `MARKET_PEG`. <br> See [Pegged Orders Info](#pegged-orders-info)|
pegOffsetValue | INT | NO | Price level to peg the price to (max: 100). <br>See [Pegged Orders Info](#pegged-orders-info)  |
pegOffsetType | ENUM | NO | Only `PRICE_LEVEL` is supported. <br> See [Pegged Orders Info](#pegged-orders-info) |
recvWindow | DECIMAL | NO |The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |


<a id="order-type">Some additional</a> mandatory parameters based on order `type`:

Type | Additional mandatory parameters | Additional Information
------------ | ------------| ------
`LIMIT` | `timeInForce`, `quantity`, `price`|
`MARKET` | `quantity` or `quoteOrderQty`| `MARKET` orders using the `quantity` field specifies the amount of the `base asset` the user wants to buy or sell at the market price. <br/> E.g. MARKET order on BTCUSDT will specify how much BTC the user is buying or selling. <br/><br/> `MARKET` orders using `quoteOrderQty` specifies the amount the user wants to spend (when buying) or receive (when selling) the `quote` asset; the correct `quantity` will be determined based on the market liquidity and `quoteOrderQty`. <br/> E.g. Using the symbol BTCUSDT: <br/> `BUY` side, the order will buy as many BTC as `quoteOrderQty` USDT can. <br/> `SELL` side, the order will sell as much BTC needed to receive `quoteOrderQty` USDT.
`STOP_LOSS` | `quantity`, `stopPrice` or `trailingDelta`| This will execute a `MARKET` order when the conditions are met. (e.g. `stopPrice` is met or `trailingDelta` is activated)
`STOP_LOSS_LIMIT` | `timeInForce`, `quantity`,  `price`, `stopPrice` or `trailingDelta`
`TAKE_PROFIT` | `quantity`, `stopPrice` or `trailingDelta` | This will execute a `MARKET` order when the conditions are met. (e.g. `stopPrice` is met or `trailingDelta` is activated)
`TAKE_PROFIT_LIMIT` | `timeInForce`, `quantity`, `price`, `stopPrice` or `trailingDelta` |
`LIMIT_MAKER` | `quantity`, `price`| This is a `LIMIT` order that will be rejected if the order immediately matches and trades as a taker. <br/> This is also known as a POST-ONLY order.


<a id="pegged-orders-info">Notes on using parameters for Pegged Orders:</a>

* These parameters are allowed for `LIMIT`, `LIMIT_MAKER`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` orders.
* If `pegPriceType` is specified, `price` becomes optional. Otherwise, it is still mandatory.
* `pegPriceType=PRIMARY_PEG` means the primary peg, that is the best price on the same side of the order book as your order.
* `pegPriceType=MARKET_PEG` means the market peg, that is the best price on the opposite side of the order book from your order.
* Use `pegOffsetType` and `pegOffsetValue` to request a price level other than the best one. These parameters must be specified together.

Other info:

* Any `LIMIT` or `LIMIT_MAKER` type order can be made an iceberg order by sending an `icebergQty`.
* Any order with an `icebergQty` MUST have `timeInForce` set to `GTC`.
* For `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` and `TAKE_PROFIT` orders, `trailingDelta` can be combined with `stopPrice`.
* `MARKET` orders using `quoteOrderQty` will not break `LOT_SIZE` filter rules; the order will execute a `quantity` that will have the notional value as close as possible to `quoteOrderQty`.
Trigger order price rules against market price for both MARKET and LIMIT versions:

* Price above market price: `STOP_LOSS` `BUY`, `TAKE_PROFIT` `SELL`
* Price below market price: `STOP_LOSS` `SELL`, `TAKE_PROFIT` `BUY`

**Data Source:**
Matching Engine

**Response - ACK:**
```javascript
{
  "symbol": "BTCUSDT",
  "orderId": 28,
  "orderListId": -1, // Unless it's part of an order list, value will be -1
  "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",
  "transactTime": 1507725176595
}
```

**Response - RESULT:**
```javascript
{
  "symbol": "BTCUSDT",
  "orderId": 28,
  "orderListId": -1, // Unless it's part of an order list, value will be -1
  "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",
  "transactTime": 1507725176595,
  "price": "0.00000000",
  "origQty": "10.00000000",
  "executedQty": "10.00000000",
  "origQuoteOrderQty": "0.000000",
  "cummulativeQuoteQty": "10.00000000",
  "status": "FILLED",
  "timeInForce": "GTC",
  "type": "MARKET",
  "side": "SELL",
  "workingTime": 1507725176595,
  "selfTradePreventionMode": "NONE"
}
```

**Response - FULL:**
```javascript
{
  "symbol": "BTCUSDT",
  "orderId": 28,
  "orderListId": -1, // Unless it's part of an order list, value will be -1
  "clientOrderId": "6gCrw2kRUAF9CvJDGP16IP",
  "transactTime": 1507725176595,
  "price": "0.00000000",
  "origQty": "10.00000000",
  "executedQty": "10.00000000",
  "origQuoteOrderQty": "0.000000",
  "cummulativeQuoteQty": "10.00000000",
  "status": "FILLED",
  "timeInForce": "GTC",
  "type": "MARKET",
  "side": "SELL",
  "workingTime": 1507725176595,
  "selfTradePreventionMode": "NONE",
  "fills": [
    {
      "price": "4000.00000000",
      "qty": "1.00000000",
      "commission": "4.00000000",
      "commissionAsset": "USDT",
      "tradeId": 56
    },
    {
      "price": "3999.00000000",
      "qty": "5.00000000",
      "commission": "19.99500000",
      "commissionAsset": "USDT",
      "tradeId": 57
    },
    {
      "price": "3998.00000000",
      "qty": "2.00000000",
      "commission": "7.99600000",
      "commissionAsset": "USDT",
      "tradeId": 58
    },
    {
      "price": "3997.00000000",
      "qty": "1.00000000",
      "commission": "3.99700000",
      "commissionAsset": "USDT",
      "tradeId": 59
    },
    {
      "price": "3995.00000000",
      "qty": "1.00000000",
      "commission": "3.99500000",
      "commissionAsset": "USDT",
      "tradeId": 60
    }
  ]
}
```
<a id="conditional-fields-in-order-responses"></a>
**Conditional fields in Order Responses**

There are fields in the order responses (e.g. order placement, order query, order cancellation) that appear only if certain conditions are met.

These fields can apply to order lists.

The fields are listed below:

Field          |Description                                                      |Visibility conditions                                           | Examples |
----           | -----                                                           | ---                                                            |---       |
`icebergQty`   | Quantity for the iceberg order | Appears only if the parameter `icebergQty` was sent in the request.| `"icebergQty": "0.00000000"`
`preventedMatchId` |  When used in combination with `symbol`, can be used to query a prevented match. | Appears only if the order expired due to STP.| `"preventedMatchId": 0`
`preventedQuantity` | Order quantity that expired due to STP | Appears only if the order expired due to STP. | `"preventedQuantity": "1.200000"`
`stopPrice`    | Price when the algorithmic order will be triggered | Appears for `STOP_LOSS`. `TAKE_PROFIT`, `STOP_LOSS_LIMIT` and `TAKE_PROFIT_LIMIT` orders.|`"stopPrice": "23500.00000000"`
`strategyId`   | Can be used to label an order that's part of an order strategy. |Appears if the parameter was populated in the request.| `"strategyId": 37463720`
`strategyType` | Can be used to label an order that is using an order strategy.|Appears if the parameter was populated in the request.| `"strategyType": 1000000`
`trailingDelta`| Delta price change required before order activation| Appears for Trailing Stop Orders.|`"trailingDelta": 10`
`trailingTime` | Time when the trailing order is now active and tracking price changes| Appears only for Trailing Stop Orders.| `"trailingTime": -1`
`usedSor`      | Field that determines whether order used SOR | Appears when placing orders using SOR|`"usedSor": true`
`workingFloor` | Field that determines whether the order is being filled by the SOR or by the order book the order was submitted to.|Appears when placing orders using SOR|`"workingFloor": "SOR"`|
`pegPriceType` | Price peg type  | Only for pegged orders  |`"pegPriceType": "PRIMARY_PEG"` |
`pegOffsetType` | Price peg offset type | Only for pegged orders, if requested  |`"pegOffsetType": "PRICE_LEVEL"` |
`pegOffsetValue` | Price peg offset value  | Only for pegged orders, if requested  |`"pegOffsetValue": 5` |
`peggedPrice` | Current price order is pegged at | Only for pegged orders, once determined |`"peggedPrice": "87523.83710000"` |

### Test new order (TRADE)
```
POST /api/v3/order/test
```
Test new order creation and signature/recvWindow long.
Creates and validates a new order but does not send it into the matching engine.

**Weight:**

|Condition| Request Weight|
|------------           | ------------ |
|Without `computeCommissionRates`| 1|
|With `computeCommissionRates`|20|

**Parameters:**

In addition to all parameters accepted by [`POST /api/v3/order`](#new-order-trade),
the following optional parameters are also accepted:

Name                   |Type          | Mandatory    | Description
------------           | ------------ | ------------ | ------------
computeCommissionRates | BOOLEAN      | NO           | Default: `false` <br> See [Commissions FAQ](faqs/commission_faq.md#test-order-diferences) to learn more.

**Data Source:**
Memory

**Response:**

Without `computeCommissionRates`

```javascript
{}
```

With `computeCommissionRates`

```javascript
{
  "standardCommissionForOrder": {  //Standard commission rates on trades from the order.
    "maker": "0.00000112",
    "taker": "0.00000114"
  },
  "specialCommissionForOrder": {    //Special commission rates on trades from the order.
    "maker": "0.05000000",
    "taker": "0.06000000"
  },
  "taxCommissionForOrder": {       //Tax commission rates for trades from the order.
    "maker": "0.00000112",
    "taker": "0.00000114"
  },
  "discount": {                    //Discount on standard commissions when paying in BNB.
    "enabledForAccount": true,
    "enabledForSymbol": true,
    "discountAsset": "BNB",
    "discount": "0.25000000"       //Standard commission is reduced by this rate when paying commission in BNB.
  }
}
```

### Cancel order (TRADE)
```
DELETE /api/v3/order
```
Cancel an active order.

**Weight:**
1

**Parameters:**

Name              | Type   | Mandatory    | Description
------------      | ------ | ------------ | ------------
symbol            | STRING | YES          |
orderId           | LONG   | NO           |
origClientOrderId | STRING | NO           |
newClientOrderId  | STRING | NO           |  Used to uniquely identify this cancel. Automatically generated by default.
cancelRestrictions| ENUM   | NO           | Supported values: <br>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br> `ONLY_PARTIALLY_FILLED ` - Cancel will succeed if order status is `PARTIALLY_FILLED`.
recvWindow        | DECIMAL| NO           | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp         | LONG   | YES          |

Notes:
* Either `orderId` or `origClientOrderId` must be sent.
* If both `orderId` and `origClientOrderId` are provided, the `orderId` is searched first, then the `origClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.

**Data Source:**
Matching Engine

**Response:**
```javascript
{
  "symbol": "LTCBTC",
  "origClientOrderId": "myOrder1",
  "orderId": 4,
  "orderListId": -1, // Unless it's part of an order list, value will be -1
  "clientOrderId": "cancelMyOrder1",
  "transactTime": 1684804350068,
  "price": "2.00000000",
  "origQty": "1.00000000",
  "executedQty": "0.00000000",
  "origQuoteOrderQty": "0.000000",
  "cummulativeQuoteQty": "0.00000000",
  "status": "CANCELED",
  "timeInForce": "GTC",
  "type": "LIMIT",
  "side": "BUY",
  "selfTradePreventionMode": "NONE"
}
```

**Notes:**
* The payload above does not show all fields that can appear in the order response. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).
* The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only `orderId` is sent. Sending `origClientOrderId` or both `orderId` + `origClientOrderId` will be slower.

<a id="regarding-cancelrestrictions"></a>

**Regarding `cancelRestrictions`**

* If the `cancelRestrictions` value is not any of the supported values, the error will be:
```json
{
    "code": -1145,
    "msg": "Invalid cancelRestrictions"
}
```
* If the order did not pass the conditions for `cancelRestrictions`, the error will be:
```json
{
    "code": -2011,
    "msg": "Order was not canceled due to cancel restrictions."
}
```

### Cancel All Open Orders on a Symbol (TRADE)
```
DELETE /api/v3/openOrders
```
Cancels all active orders on a symbol.
This includes orders that are part of an order list.

**Weight:**
1

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
recvWindow | DECIMAL| NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |

**Data Source:**
Matching Engine

**Response:**
```javascript
[
  {
    "symbol": "BTCUSDT",
    "origClientOrderId": "E6APeyTJvkMvLMYMqu1KQ4",
    "orderId": 11,
    "orderListId": -1,
    "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
    "transactTime": 1684804350068,
    "price": "0.089853",
    "origQty": "0.178622",
    "executedQty": "0.000000",
    "origQuoteOrderQty": "0.000000",
    "cummulativeQuoteQty": "0.000000",
    "status": "CANCELED",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "BUY",
    "selfTradePreventionMode": "NONE"
  },
  {
    "symbol": "BTCUSDT",
    "origClientOrderId": "A3EF2HCwxgZPFMrfwbgrhv",
    "orderId": 13,
    "orderListId": -1,
    "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
    "transactTime": 1684804350069,
    "price": "0.090430",
    "origQty": "0.178622",
    "executedQty": "0.000000",
    "origQuoteOrderQty": "0.000000",
    "cummulativeQuoteQty": "0.000000",
    "status": "CANCELED",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "BUY",
    "selfTradePreventionMode": "NONE"
  },
  {
    "orderListId": 1929,
    "contingencyType": "OCO",
    "listStatusType": "ALL_DONE",
    "listOrderStatus": "ALL_DONE",
    "listClientOrderId": "2inzWQdDvZLHbbAmAozX2N",
    "transactionTime": 1585230948299,
    "symbol": "BTCUSDT",
    "orders": [
      {
        "symbol": "BTCUSDT",
        "orderId": 20,
        "clientOrderId": "CwOOIPHSmYywx6jZX77TdL"
      },
      {
        "symbol": "BTCUSDT",
        "orderId": 21,
        "clientOrderId": "461cPg51vQjV3zIMOXNz39"
      }
    ],
    "orderReports": [
      {
        "symbol": "BTCUSDT",
        "origClientOrderId": "CwOOIPHSmYywx6jZX77TdL",
        "orderId": 20,
        "orderListId": 1929,
        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
        "transactTime": 1688005070874,
        "price": "0.668611",
        "origQty": "0.690354",
        "executedQty": "0.000000",
        "origQuoteOrderQty": "0.000000",
        "cummulativeQuoteQty": "0.000000",
        "status": "CANCELED",
        "timeInForce": "GTC",
        "type": "STOP_LOSS_LIMIT",
        "side": "BUY",
        "stopPrice": "0.378131",
        "icebergQty": "0.017083",
        "selfTradePreventionMode": "NONE"
      },
      {
        "symbol": "BTCUSDT",
        "origClientOrderId": "461cPg51vQjV3zIMOXNz39",
        "orderId": 21,
        "orderListId": 1929,
        "clientOrderId": "pXLV6Hz6mprAcVYpVMTGgx",
        "transactTime": 1688005070874,
        "price": "0.008791",
        "origQty": "0.690354",
        "executedQty": "0.000000",
        "origQuoteOrderQty": "0.000000",
        "cummulativeQuoteQty": "0.000000",
        "status": "CANCELED",
        "timeInForce": "GTC",
        "type": "LIMIT_MAKER",
        "side": "BUY",
        "icebergQty": "0.639962",
        "selfTradePreventionMode": "NONE"
      }
    ]
  }
]
```

### Cancel an Existing Order and Send a New Order (TRADE)

```
POST /api/v3/order/cancelReplace
```
Cancels an existing order and places a new order on the same symbol.

Filters and Order Count are evaluated before the processing of the cancellation and order placement occurs.

A new order that was not attempted (i.e. when `newOrderResult: NOT_ATTEMPTED`), will still increase the unfilled order count by 1.

**Weight:**
1

**Unfilled Order Count:**
1

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
side   |ENUM| YES|
type   |ENUM| YES|
cancelReplaceMode|ENUM|YES| The allowed values are: <br/> `STOP_ON_FAILURE` - If the cancel request fails, the new order placement will not be attempted. <br/> `ALLOW_FAILURE` - new order placement will be attempted even if cancel request fails.
timeInForce|ENUM|NO|
quantity|DECIMAL|NO|
quoteOrderQty |DECIMAL|NO
price |DECIMAL|NO
cancelNewClientOrderId|STRING|NO| Used to uniquely identify this cancel. Automatically generated by default.
cancelOrigClientOrderId|STRING| NO| Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent. <br></br> If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order. <br></br> If both conditions are not met the request will be rejected.
cancelOrderId|LONG|NO| Either `cancelOrderId` or `cancelOrigClientOrderId` must be sent. <br></br>If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order. <br></br>If both conditions are not met the request will be rejected.
newClientOrderId |STRING|NO| Used to identify the new order.
strategyId |LONG| NO|
strategyType |INT| NO| The value cannot be less than `1000000`.
stopPrice|DECIMAL|NO|
trailingDelta|LONG|NO|See [Trailing Stop order FAQ](faqs/trailing-stop-faq.md)
icebergQty|DECIMAL|NO|
newOrderRespType|ENUM|NO|Allowed values: <br/> `ACK`, `RESULT`, `FULL` <br/> `MARKET` and `LIMIT` orders types default to `FULL`; all other orders default to `ACK`
selfTradePreventionMode |ENUM| NO |The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](./enums.md#stpmodes).
cancelRestrictions| ENUM   | NO           | Supported values: <br>`ONLY_NEW` - Cancel will succeed if the order status is `NEW`.<br> `ONLY_PARTIALLY_FILLED ` - Cancel will succeed if order status is `PARTIALLY_FILLED`. For more information please refer to [Regarding `cancelRestrictions`](#regarding-cancelrestrictions)
orderRateLimitExceededMode|ENUM|No| Supported values: <br> `DO_NOTHING` (default)- will only attempt to cancel the order if account has not exceeded the unfilled order rate limit<br> `CANCEL_ONLY` - will always cancel the order|
pegPriceType |ENUM |NO |`PRIMARY_PEG` or `MARKET_PEG` <br> See [Pegged Orders](#pegged-orders-info) |
pegOffsetValue |INT |NO |Price level to peg the price to (max: 100) <br> See [Pegged Orders](#pegged-orders-info)  |
pegOffsetType |ENUM |NO |Only `PRICE_LEVEL` is supported  <br> See [Pegged Orders](#pegged-orders-info)|
recvWindow | DECIMAL| NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |


Similar to `POST /api/v3/order`, additional mandatory parameters are determined by `type`.

Response format varies depending on whether the processing of the message succeeded, partially succeeded, or failed.

**Data Source:**
Matching Engine

<table>
<thead>
    <tr>
        <th colspan=3 align=left>Request</th>
        <th colspan=3 align=left>Response</th>
    </tr>
    <tr>
        <th><code>cancelReplaceMode</code></th>
        <th><code>orderRateLimitExceededMode</code></th>
        <th>Unfilled Order Count</th>
        <th><code>cancelResult</code></th>
        <th><code>newOrderResult</code></th>
        <th><code>status</code></th>
    </tr>
</thead>
<tbody>
    <tr>
        <td rowspan="11"><code>STOP_ON_FAILURE</code></td>
        <td rowspan="6"><code>DO_NOTHING</code></td>
        <td rowspan="3">Within Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>200</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>➖ <code>NOT_ATTEMPTED</code></td>
        <td align=right><code>400</code></td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
        <td rowspan="3">Exceeds Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>➖ <code>NOT_ATTEMPTED</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right>N/A</td>
    </tr>
     <tr>
        <td rowspan="5"><code>CANCEL_ONLY</code></td>
        <td rowspan="3">Within Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>200</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>➖ <code>NOT_ATTEMPTED</code></td>
        <td align=right><code>400</code></td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
        <td rowspan="2">Exceeds Limits</td>
        <td>❌ <code>FAILURE</code></td>
        <td>➖ <code>NOT_ATTEMPTED</code></td>
        <td align=right><code>429</code></td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>429</code></td>
    </tr>
    <tr>
        <td rowspan="16"><code>ALLOW_FAILURE</code></td>
        <td rowspan="8"><code>DO_NOTHING</code></td>
        <td rowspan="4">Within Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>200</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>400</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
     <td rowspan="4">Exceeds Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td rowspan="8"><CODE>CANCEL_ONLY</CODE></td>
        <td rowspan="4">Within Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>200</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>400</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
        <td rowspan="4">Exceeds Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>N/A</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>400</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>409</code></td>
    </tr>
</tbody>
</table>

**Response SUCCESS and account has not exceeded the unfilled order count:**

```javascript
// Both the cancel order placement and new order placement succeeded.
{
  "cancelResult": "SUCCESS",
  "newOrderResult": "SUCCESS",
  "cancelResponse": {
    "symbol": "BTCUSDT",
    "origClientOrderId": "DnLo3vTAQcjha43lAZhZ0y",
    "orderId": 9,
    "orderListId": -1,
    "clientOrderId": "osxN3JXAtJvKvCqGeMWMVR",
    "transactTime": 1684804350068,
    "price": "0.01000000",
    "origQty": "0.000100",
    "executedQty": "0.00000000",
    "origQuoteOrderQty": "0.000000",
    "cummulativeQuoteQty": "0.00000000",
    "status": "CANCELED",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "SELL",
    "selfTradePreventionMode": "NONE"
  },
  "newOrderResponse": {
    "symbol": "BTCUSDT",
    "orderId": 10,
    "orderListId": -1,
    "clientOrderId": "wOceeeOzNORyLiQfw7jd8S",
    "transactTime": 1652928801803,
    "price": "0.02000000",
    "origQty": "0.040000",
    "executedQty": "0.00000000",
    "origQuoteOrderQty": "0.000000",
    "cummulativeQuoteQty": "0.00000000",
    "status": "NEW",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "BUY",
    "workingTime": 1669277163808,
    "fills": [],
    "selfTradePreventionMode": "NONE"
  }
}
```

**Response when Cancel Order Fails with STOP_ON FAILURE and account has not exceeded their unfilled order count:**
```javascript
{
  "code": -2022,
  "msg": "Order cancel-replace failed.",
  "data": {
    "cancelResult": "FAILURE",
    "newOrderResult": "NOT_ATTEMPTED",
    "cancelResponse": {
      "code": -2011,
      "msg": "Unknown order sent."
    },
    "newOrderResponse": null
  }
}
```

**Response when Cancel Order Succeeds but New Order Placement Fails and account has not exceeded their unfilled order count:**
```javascript
{
  "code": -2021,
  "msg": "Order cancel-replace partially failed.",
  "data": {
    "cancelResult": "SUCCESS",
    "newOrderResult": "FAILURE",
    "cancelResponse": {
      "symbol": "BTCUSDT",
      "origClientOrderId": "86M8erehfExV8z2RC8Zo8k",
      "orderId": 3,
      "orderListId": -1,
      "clientOrderId": "G1kLo6aDv2KGNTFcjfTSFq",
      "transactTime": 1684804350068,
      "price": "0.006123",
      "origQty": "10000.000000",
      "executedQty": "0.000000",
      "origQuoteOrderQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "CANCELED",
      "timeInForce": "GTC",
      "type": "LIMIT_MAKER",
      "side": "SELL",
      "selfTradePreventionMode": "NONE"
    },
    "newOrderResponse": {
      "code": -2010,
      "msg": "Order would immediately match and take."
    }
  }
}
```

**Response when Cancel Order fails with ALLOW_FAILURE and account has not exceeded their unfilled order count:**

```javascript
{
  "code": -2021,
  "msg": "Order cancel-replace partially failed.",
  "data": {
    "cancelResult": "FAILURE",
    "newOrderResult": "SUCCESS",
    "cancelResponse": {
      "code": -2011,
      "msg": "Unknown order sent."
    },
    "newOrderResponse": {
      "symbol": "BTCUSDT",
      "orderId": 11,
      "orderListId": -1,
      "clientOrderId": "pfojJMg6IMNDKuJqDxvoxN",
      "transactTime": 1648540168818
    }
  }
}
```

**Response when both Cancel Order and New Order Placement fail using `cancelReplaceMode=ALLOW_FAILURE` and account has not exceeded their unfilled order count:**

```javascript
{
  "code": -2022,
  "msg": "Order cancel-replace failed.",
  "data": {
    "cancelResult": "FAILURE",
    "newOrderResult": "FAILURE",
    "cancelResponse": {
      "code": -2011,
      "msg": "Unknown order sent."
    },
    "newOrderResponse": {
      "code": -2010,
      "msg": "Order would immediately match and take."
    }
  }
}
```

**Response when using `orderRateLimitExceededMode=DO_NOTHING` and account's unfilled order count has been exceeded:**

```javascript
{
  "code": -1015,
  "msg": "Too many new orders; current limit is 1 orders per 10 SECOND."
}
```

**Response when using `orderRateLimitExceededMode=CANCEL_ONLY` and account's unfilled order count has been exceeded:**

```javascript
{
  "code": -2021,
  "msg": "Order cancel-replace partially failed.",
  "data": {
    "cancelResult": "SUCCESS",
    "newOrderResult": "FAILURE",
    "cancelResponse": {
      "symbol": "LTCBNB",
      "origClientOrderId": "GKt5zzfOxRDSQLveDYCTkc",
      "orderId": 64,
      "orderListId": -1,
      "clientOrderId": "loehOJF3FjoreUBDmv739R",
      "transactTime": 1715779007228,
      "price": "1.00",
      "origQty": "10.00000000",
      "executedQty": "0.00000000",
      "origQuoteOrderQty": "0.000000",
      "cummulativeQuoteQty": "0.00",
      "status": "CANCELED",
      "timeInForce": "GTC",
      "type": "LIMIT",
      "side": "SELL",
      "selfTradePreventionMode": "NONE"
    },
    "newOrderResponse": {
      "code": -1015,
      "msg": "Too many new orders; current limit is 1 orders per 10 SECOND."
    }
  }
}
```

**Notes:**
* The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).
* The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only `orderId` is sent. Sending `origClientOrderId` or both `orderId` + `origClientOrderId` will be slower.

### Order Amend Keep Priority (TRADE)

```
PUT /api/v3/order/amend/keepPriority
```

Reduce the quantity of an existing open order.

This adds 0 orders to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [Order Amend Keep Priority FAQ](faqs/order_amend_keep_priority.md) to learn more.

**Weight**:
4

**Unfilled Order Count:**
0

**Parameters:**

Name | Type | Mandatory | Description |
---- | ---- | ---- | ---- |
symbol | STRING | YES |  |
orderId | LONG | NO\* | `orderId` or `origClientOrderId` must be sent  |
origClientOrderId | STRING | NO\* | `orderId` or `origClientOrderId` must be sent  |
newClientOrderId | STRING | NO\* | The new client order ID for the order after being amended.  <br> If not sent, one will be randomly generated. <br> It is possible to reuse the current clientOrderId by sending it as the `newClientOrderId`. |
newQty | DECIMAL | YES | `newQty` must be greater than 0 and less than the order's quantity.|
recvWindow | DECIMAL| NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |


**Data Source**: Matching Engine

**Response:**
Response for a single order:

```json
{
  "transactTime": 1741926410255,
  "executionId": 75,
  "amendedOrder":
  {
    "symbol": "BTCUSDT",
    "orderId": 33,
    "orderListId": -1,
    "origClientOrderId": "5xrgbMyg6z36NzBn2pbT8H",
    "clientOrderId": "PFaq6hIHxqFENGfdtn4J6Q",
    "price": "6.00000000",
    "qty": "5.00000000",
    "executedQty": "0.00000000",
    "preventedQty": "0.00000000",
    "quoteOrderQty": "0.00000000",
    "cumulativeQuoteQty": "0.00000000",
    "status": "NEW",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "SELL",
    "workingTime": 1741926410242,
    "selfTradePreventionMode": "NONE"
  }
}
```

Response for an order that is part of an Order list:

```json
{
  "transactTime": 1741669661670,
  "executionId": 22,
  "amendedOrder":
  {
    "symbol": "BTCUSDT",
    "orderId": 9,
    "orderListId": 1,
    "origClientOrderId": "W0fJ9fiLKHOJutovPK3oJp",
    "clientOrderId": "UQ1Np3bmQ71jJzsSDW9Vpi",
    "price": "0.00000000",
    "qty": "4.00000000",
    "executedQty": "0.00000000",
    "preventedQty": "0.00000000",
    "quoteOrderQty": "0.00000000",
    "cumulativeQuoteQty": "0.00000000",
    "status": "PENDING_NEW",
    "timeInForce": "GTC",
    "type": "MARKET",
    "side": "BUY",
    "selfTradePreventionMode": "NONE"
  },
  "listStatus":
  {
    "orderListId": 1,
    "contingencyType": "OTO",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "AT7FTxZXylVSwRoZs52mt3",
    "symbol": "BTCUSDT",
    "orders":
    [
      {
        "symbol": "BTCUSDT",
        "orderId": 8,
        "clientOrderId": "GkwwHZUUbFtZOoH1YsZk9Q"
      },
      {
        "symbol": "BTCUSDT",
        "orderId": 9,
        "clientOrderId": "UQ1Np3bmQ71jJzsSDW9Vpi"
      }
    ]
  }
}
```

**Note:** The payloads above do not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

### Order lists

#### New OCO - Deprecated (TRADE)

```
POST /api/v3/order/oco
```

Send in a new OCO.

* Price Restrictions:
    * `SELL`: Limit Price > Last Price > Stop Price
    * `BUY`: Limit Price < Last Price < Stop Price
* Quantity Restrictions:
    * Both legs must have the same quantity.
    * `ICEBERG` quantities however do not have to be the same
* `OCO` adds **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.


**Weight:**
1

**Unfilled Order Count:**
2

**Parameters:**

Name |Type| Mandatory | Description
-----|-----|----------| -----------
symbol|STRING| YES|
listClientOrderId|STRING|NO| A unique Id for the entire orderList
side|ENUM|YES|
quantity|DECIMAL|YES|
limitClientOrderId|STRING|NO| A unique Id for the limit order
price|DECIMAL|YES|
limitStrategyId |LONG| NO
limitStrategyType | INT| NO | The value cannot be less than `1000000`.
limitIcebergQty|DECIMAL|NO| Used to make the `LIMIT_MAKER` leg an iceberg order.
trailingDelta|LONG|NO|
stopClientOrderId |STRING|NO| A unique Id for the stop loss/stop loss limit leg
stopPrice |DECIMAL| YES
stopStrategyId |LONG| NO
stopStrategyType |INT| NO | The value cannot be less than `1000000`.
stopLimitPrice|DECIMAL|NO | If provided, `stopLimitTimeInForce` is required.
stopIcebergQty|DECIMAL|NO| Used with `STOP_LOSS_LIMIT` leg to make an iceberg order.
stopLimitTimeInForce|ENUM|NO| Valid values are `GTC`/`FOK`/`IOC`
newOrderRespType|ENUM|NO| Set the response JSON.
selfTradePreventionMode |ENUM| NO | The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](./enums.md#stpmodes).
recvWindow|DECIMAL|NO| The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp|LONG|YES|


**Data Source:**
Matching Engine

**Response:**

```json
{
  "orderListId": 0,
  "contingencyType": "OCO",
  "listStatusType": "EXEC_STARTED",
  "listOrderStatus": "EXECUTING",
  "listClientOrderId": "JYVpp3F0f5CAG15DhtrqLp",
  "transactionTime": 1563417480525,
  "symbol": "LTCBTC",
  "orders": [
    {
      "symbol": "LTCBTC",
      "orderId": 2,
      "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos"
    },
    {
      "symbol": "LTCBTC",
      "orderId": 3,
      "clientOrderId": "xTXKaGYd4bluPVp78IVRvl"
    }
  ],
  "orderReports": [
    {
      "symbol": "LTCBTC",
      "orderId": 2,
      "orderListId": 0,
      "clientOrderId": "Kk7sqHb9J6mJWTMDVW7Vos",
      "transactTime": 1563417480525,
      "price": "0.000000",
      "origQty": "0.624363",
      "executedQty": "0.000000",
      "origQuoteOrderQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "STOP_LOSS",
      "side": "BUY",
      "stopPrice": "0.960664",
      "workingTime": -1,
      "selfTradePreventionMode": "NONE"
    },
    {
      "symbol": "LTCBTC",
      "orderId": 3,
      "orderListId": 0,
      "clientOrderId": "xTXKaGYd4bluPVp78IVRvl",
      "transactTime": 1563417480525,
      "price": "0.036435",
      "origQty": "0.624363",
      "executedQty": "0.000000",
      "origQuoteOrderQty": "0.000000",
      "cummulativeQuoteQty": "0.000000",
      "status": "NEW",
      "timeInForce": "GTC",
      "type": "LIMIT_MAKER",
      "side": "BUY",
      "workingTime": 1563417480525,
      "selfTradePreventionMode": "NONE"
    }
  ]
}
```

#### New Order list - OCO (TRADE)

```
POST /api/v3/orderList/oco
```

Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

* An OCO has 2 orders called the **above order** and **below order**.
* One of the orders must be a `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` order and the other must be `STOP_LOSS` or `STOP_LOSS_LIMIT` order.
* Price restrictions
  * If the OCO is on the `SELL` side:
    * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > Last Traded Price >  `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
    * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
  * If the OCO is on the `BUY` side:
    * `LIMIT_MAKER/TAKE_PROFIT_LIMIT price` < Last Traded Price < `stopPrice`
    * `TAKE_PROFIT stopPrice` < Last Traded Price < `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
* OCOs add **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

**Weight:**
1

**Unfilled Order Count:**
2

**Parameters:**

Name                   |Type    | Mandatory | Description
-----                  |------  | -----     |----
symbol                 |STRING  |Yes        |
listClientOrderId      |STRING  |No         |Arbitrary unique ID among open order lists. Automatically generated if not sent. <br> A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. <br> `listClientOrderId` is distinct from the `aboveClientOrderId` and the `belowCLientOrderId`.
side                   |ENUM    |Yes        |`BUY` or `SELL`
quantity               |DECIMAL |Yes        |Quantity for both orders of the order list.
aboveType              |ENUM    |Yes        |Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`
aboveClientOrderId     |STRING  |No         |Arbitrary unique ID among open orders for the above order. Automatically generated if not sent
aboveIcebergQty        |LONG    |No         |Note that this can only be used if `aboveTimeInForce` is `GTC`.
abovePrice             |DECIMAL |No         |Can be used if `aboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.
aboveStopPrice         |DECIMAL |No         |Can be used if `aboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`. <br>Either `aboveStopPrice` or `aboveTrailingDelta` or both, must be specified.
aboveTrailingDelta     |LONG    |No         |See [Trailing Stop order FAQ](faqs/trailing-stop-faq.md).
aboveTimeInForce       |ENUM    |No         |Required if `aboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`
aboveStrategyId        |LONG     |No         |Arbitrary numeric value identifying the above order within an order strategy.
aboveStrategyType      |INT     |No         |Arbitrary numeric value identifying the above order strategy. <br>Values smaller than 1000000 are reserved and cannot be used.
abovePegPriceType      |ENUM    |NO         |See [Pegged Orders](#pegged-orders-info)
abovePegOffsetType     |ENUM    |NO         |
abovePegOffsetValue    |INT     |NO         |
belowType              |ENUM    |Yes        |Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`
belowClientOrderId     |STRING  |No         |Arbitrary unique ID among open orders for the below order. Automatically generated if not sent
belowIcebergQty        |LONG    |No         |Note that this can only be used if `belowTimeInForce` is `GTC`.
belowPrice             |DECIMAL |No         |Can be used if `belowType` is `STOP_LOSS_LIMIT`, `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.
belowStopPrice         |DECIMAL |No         |Can be used if `belowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT, TAKE_PROFIT` or `TAKE_PROFIT_LIMIT` <br>Either belowStopPrice or belowTrailingDelta or both, must be specified.
belowTrailingDelta     |LONG    |No         |See [Trailing Stop order FAQ](faqs/trailing-stop-faq.md).
belowTimeInForce       |ENUM    |No         |Required if `belowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.
belowStrategyId        |LONG    |No          |Arbitrary numeric value identifying the below order within an order strategy.
belowStrategyType      |INT     |No         |Arbitrary numeric value identifying the below order strategy. <br>Values smaller than 1000000 are reserved and cannot be used.
belowPegPriceType      |ENUM    |NO         |See [Pegged Orders](#pegged-orders-info)
belowPegOffsetType     |ENUM    |NO         |
belowPegOffsetValue    |INT     |NO         |
newOrderRespType       |ENUM    |No         |Select response format: `ACK`, `RESULT`, `FULL`
selfTradePreventionMode|ENUM    |No         |The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](./enums.md#stpmodes)
recvWindow             |DECIMAL |No          |The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp              |LONG   |Yes          |

**Data Source:**
Matching Engine

**Response:**

Response format for `orderReports` is selected using the `newOrderRespType` parameter. The following example is for the `RESULT` response type. See [`POST /api/v3/order`](#new-order-trade) for more examples.

```javascript
{
    "orderListId": 1,
    "contingencyType": "OCO",
    "listStatusType": "EXEC_STARTED",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "lH1YDkuQKWiXVXHPSKYEIp",
    "transactionTime": 1710485608839,
    "symbol": "LTCBTC",
    "orders": [
        {
            "symbol": "LTCBTC",
            "orderId": 10,
            "clientOrderId": "44nZvqpemY7sVYgPYbvPih"
        },
        {
            "symbol": "LTCBTC",
            "orderId": 11,
            "clientOrderId": "NuMp0nVYnciDiFmVqfpBqK"
        }
    ],
    "orderReports": [
        {
            "symbol": "LTCBTC",
            "orderId": 10,
            "orderListId": 1,
            "clientOrderId": "44nZvqpemY7sVYgPYbvPih",
            "transactTime": 1710485608839,
            "price": "1.00000000",
            "origQty": "5.00000000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "STOP_LOSS_LIMIT",
            "side": "SELL",
            "stopPrice": "1.00000000",
            "workingTime": -1,
            "icebergQty": "1.00000000",
            "selfTradePreventionMode": "NONE"
        },
        {
            "symbol": "LTCBTC",
            "orderId": 11,
            "orderListId": 1,
            "clientOrderId": "NuMp0nVYnciDiFmVqfpBqK",
            "transactTime": 1710485608839,
            "price": "3.00000000",
            "origQty": "5.00000000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "LIMIT_MAKER",
            "side": "SELL",
            "workingTime": 1710485608839,
            "selfTradePreventionMode": "NONE"
        }
    ]
}
```

#### New Order list - OTO (TRADE)

```
POST /api/v3/orderList/oto
```

Place an OTO.

* An OTO (One-Triggers-the-Other) is an order list comprised of 2 orders.
* The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
* The second order is called the **pending order**. It can be any order type except for `MARKET` orders using parameter `quoteOrderQty`. The pending order is only placed on the order book when the working order gets **fully filled**.
* If either the working order or the pending order is cancelled individually, the other order in the order list will also be canceled or expired.
* When the order list is placed, if the working order gets **immediately fully filled**, the placement response will show the working order as `FILLED` but the pending order will still appear as `PENDING_NEW`. You need to query the status of the pending order again to see its updated status.
* OTOs add **2 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

**Weight:** 1

**Unfilled Order Count:**
2

**Parameters:**

Name                   |Type   |Mandatory | Description
----                   |----   |------    |------
symbol                 |STRING |YES       |
listClientOrderId      |STRING |NO        |Arbitrary unique ID among open order lists. Automatically generated if not sent. <br>A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. <br> `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.
newOrderRespType       |ENUM   |NO        |Format of the JSON response. Supported values: [Order Response Type](./enums.md#orderresponsetype)
selfTradePreventionMode|ENUM   |NO        |The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](./enums.md#stpmodes)
workingType            |ENUM   |YES       |Supported values: `LIMIT`,`LIMIT_MAKER`
workingSide            |ENUM   |YES       |Supported values: [Order Side](./enums.md#side)
workingClientOrderId   |STRING |NO        |Arbitrary unique ID among open orders for the working order.<br> Automatically generated if not sent.
workingPrice           |DECIMAL|YES       |
workingQuantity        |DECIMAL|YES       |Sets the quantity for the working order.
workingIcebergQty      |DECIMAL|NO       |This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.
workingTimeInForce     |ENUM   |NO        |Supported values: [Time In Force](./enums.md#timeinforce)
workingStrategyId      |LONG    |NO        |Arbitrary numeric value identifying the working order within an order strategy.
workingStrategyType    |INT    |NO        |Arbitrary numeric value identifying the working order strategy. <br> Values smaller than 1000000 are reserved and cannot be used.
workingPegPriceType    |ENUM   |NO        |See [Pegged Orders](#pegged-orders-info)
workingPegOffsetType   |ENUM   |NO        |
workingPegOffsetValue  |INT    |NO        |
pendingType            |ENUM   |YES       |Supported values: [Order Types](#order-type)<br> Note that `MARKET` orders using `quoteOrderQty` are not supported.
pendingSide            |ENUM   |YES       |Supported values: [Order Side](./enums.md#side)
pendingClientOrderId   |STRING |NO        |Arbitrary unique ID among open orders for the pending order.<br> Automatically generated if not sent.
pendingPrice           |DECIMAL|NO        |
pendingStopPrice       |DECIMAL|NO        |
pendingTrailingDelta   |DECIMAL|NO        |
pendingQuantity        |DECIMAL|YES       |Sets the quantity for the pending order.
pendingIcebergQty      |DECIMAL|NO        |This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`.
pendingTimeInForce     |ENUM   |NO        |Supported values: [Time In Force](./enums.md#timeinforce)
pendingStrategyId      |LONG    |NO        |Arbitrary numeric value identifying the pending order within an order strategy.
pendingStrategyType    |INT    |NO        |Arbitrary numeric value identifying the pending order strategy. <br> Values smaller than 1000000 are reserved and cannot be used.
pendingPegPriceType    |ENUM   |NO        |See [Pegged Orders](#pegged-orders-info)
pendingPegOffsetType   |ENUM   |NO       |
pendingPegOffsetValue  |INT    |NO       |
recvWindow             |DECIMAL|NO        |The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp              |LONG   |YES       |

<a id="mandatory-parameters-based-on-pendingtype-or-workingtype"></a>

**Mandatory parameters based on `pendingType` or `workingType`**

Depending on the `pendingType` or `workingType`, some optional parameters will become mandatory.

|Type                                                  |Additional mandatory parameters|Additional information|
|----                                                  |----                           |------
|`workingType` = `LIMIT`                               |`workingTimeInForce`           |
|`pendingType` = `LIMIT`                                |`pendingPrice`, `pendingTimeInForce`          |
|`pendingType` = `STOP_LOSS` or `TAKE_PROFIT`           |`pendingStopPrice` and/or `pendingTrailingDelta`|
|`pendingType` = `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`|`pendingPrice`, `pendingStopPrice` and/or `pendingTrailingDelta`, `pendingTimeInForce`|

**Data Source:**

Matching Engine

**Response:**

```javascript
{
    "orderListId": 0,
    "contingencyType": "OTO",
    "listStatusType": "EXEC_STARTED",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "yl2ERtcar1o25zcWtqVBTC",
    "transactionTime": 1712289389158,
    "symbol": "LTCBTC",
    "orders": [
        {
            "symbol": "LTCBTC",
            "orderId": 4,
            "clientOrderId": "Bq17mn9fP6vyCn75Jw1xya"
        },
        {
            "symbol": "LTCBTC",
            "orderId": 5,
            "clientOrderId": "arLFo0zGJVDE69cvGBaU0d"
        }
    ],
    "orderReports": [
        {
            "symbol": "LTCBTC",
            "orderId": 4,
            "orderListId": 0,
            "clientOrderId": "Bq17mn9fP6vyCn75Jw1xya",
            "transactTime": 1712289389158,
            "price": "1.00000000",
            "origQty": "1.00000000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "SELL",
            "workingTime": 1712289389158,
            "selfTradePreventionMode": "NONE"
        },
        {
            "symbol": "LTCBTC",
            "orderId": 5,
            "orderListId": 0,
            "clientOrderId": "arLFo0zGJVDE69cvGBaU0d",
            "transactTime": 1712289389158,
            "price": "0.00000000",
            "origQty": "5.00000000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "PENDING_NEW",
            "timeInForce": "GTC",
            "type": "MARKET",
            "side": "BUY",
            "workingTime": -1,
            "selfTradePreventionMode": "NONE"
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

#### New Order list - OTOCO (TRADE)

```
POST /api/v3/orderList/otoco
```

Place an OTOCO.

* An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
* The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
  * The behavior of the working order is the same as the [OTO](#new-order-list---oto-trade).
* OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. The pending orders are only placed on the order book when the working order gets **fully filled**.
    * The rules of the pending above and pending below follow the same rules as the [Order list OCO](#new-order-list---oco-trade).
* OTOCOs add **3 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

**Weight:** 1

**Unfilled Order Count:**
3

**Parameters:**

Name                     |Type   |Mandatory | Description
----                     |----   |------    |------
symbol                   |STRING |YES       |
listClientOrderId        |STRING |NO        |Arbitrary unique ID among open order lists. Automatically generated if not sent. <br>A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. <br> `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.
newOrderRespType         |ENUM   |NO        |Format of the JSON response. Supported values: [Order Response Type](./enums.md#orderresponsetype)
selfTradePreventionMode  |ENUM   |NO        |The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](./enums.md#stpmodes)
workingType              |ENUM   |YES       |Supported values: `LIMIT`, `LIMIT_MAKER`
workingSide              |ENUM   |YES       |Supported values: [Order side](./enums.md#side)
workingClientOrderId     |STRING |NO        |Arbitrary unique ID among open orders for the working order.<br> Automatically generated if not sent.
workingPrice             |DECIMAL|YES       |
workingQuantity          |DECIMAL|YES        |
workingIcebergQty        |DECIMAL|NO        |This can only be used if `workingTimeInForce` is `GTC` or if `workingType` is `LIMIT_MAKER`.|
workingTimeInForce       |ENUM   |NO        |Supported values: [Time In Force](./enums.md#timeinforce)
workingStrategyId        |LONG    |NO        |Arbitrary numeric value identifying the working order within an order strategy.
workingStrategyType      |INT    |NO        |Arbitrary numeric value identifying the working order strategy. <br> Values smaller than 1000000 are reserved and cannot be used.
workingPegPriceType      |ENUM   |NO        |See [Pegged Orders](#pegged-orders-info)
workingPegOffsetType     |ENUM   |NO        |
workingPegOffsetValue    |INT    |NO        |
pendingSide              |ENUM   |YES       |Supported values: [Order side](./enums.md#side)
pendingQuantity          |DECIMAL|YES       |
pendingAboveType         |ENUM   |YES       |Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`
pendingAboveClientOrderId|STRING |NO        |Arbitrary unique ID among open orders for the pending above order.<br> Automatically generated if not sent.
pendingAbovePrice        |DECIMAL|NO        |Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.
pendingAboveStopPrice    |DECIMAL|NO        |Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`
pendingAboveTrailingDelta|DECIMAL|NO        |See [Trailing Stop FAQ](faqs/trailing-stop-faq.md)
pendingAboveIcebergQty   |DECIMAL|NO        |This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`.
pendingAboveTimeInForce  |ENUM   |NO        |
pendingAboveStrategyId   |LONG   |NO        |Arbitrary numeric value identifying the pending above order within an order strategy.
pendingAboveStrategyType |INT    |NO        |Arbitrary numeric value identifying the pending above order strategy. <br> Values smaller than 1000000 are reserved and cannot be used.
pendingAbovePegPriceType |ENUM  |NO         |See [Pegged Orders](#pegged-orders-info)
pendingAbovePegOffsetType  |ENUM |NO        |
pendingAbovePegOffsetValue |INT |NO         |
pendingBelowType         |ENUM   |NO        |Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`
pendingBelowClientOrderId|STRING |NO        |Arbitrary unique ID among open orders for the pending below order.<br> Automatically generated if not sent.
pendingBelowPrice        |DECIMAL|NO        |Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify limit price
pendingBelowStopPrice    |DECIMAL|NO        |Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT, TAKE_PROFIT or TAKE_PROFIT_LIMIT`. <br>Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified.
pendingBelowTrailingDelta|DECIMAL|NO        |
pendingBelowIcebergQty   |DECIMAL|NO        |This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`.
pendingBelowTimeInForce  |ENUM   |NO        |Supported values: [Time In Force](enums.md#timeinforce)
pendingBelowStrategyId   |LONG    |NO        |Arbitrary numeric value identifying the pending below order within an order strategy.
pendingBelowStrategyType |INT    |NO        |Arbitrary numeric value identifying the pending below order strategy. <br> Values smaller than 1000000 are reserved and cannot be used.
pendingBelowPegPriceType |ENUM  |NO         |See [Pegged Orders](#pegged-orders-info)
pendingBelowPegOffsetType |ENUM |NO         |
pendingBelowPegOffsetValue |INT |NO         |
recvWindow               |DECIMAL|NO        |The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp                |LONG   |YES       |

<a id="mandatory-parameters-based-on-pendingabovetype-pendingbelowtype-or-workingtype"></a>

**Mandatory parameters based on `pendingAboveType`, `pendingBelowType` or `workingType`**

Depending on the `pendingAboveType`/`pendingBelowType` or `workingType`, some optional parameters will become mandatory.

|Type                                                       |Additional mandatory parameters|Additional information|
|----                                                       |----                           |------
|`workingType` = `LIMIT`                                    |`workingTimeInForce`           |
|`pendingAboveType`= `LIMIT_MAKER`                                |`pendingAbovePrice`     |
|`pendingAboveType` = `STOP_LOSS/TAKE_PROFIT`        |`pendingAboveStopPrice` and/or `pendingAboveTrailingDelta`|
|`pendingAboveType=STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT` |`pendingAbovePrice`, `pendingAboveStopPrice` and/or `pendingAboveTrailingDelta`, `pendingAboveTimeInForce`|
|`pendingBelowType`= `LIMIT_MAKER`                                |`pendingBelowPrice`          |
|`pendingBelowType= STOP_LOSS/TAKE_PROFIT`         |`pendingBelowStopPrice` and/or `pendingBelowTrailingDelta`|
|`pendingBelowType=STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT` |`pendingBelowPrice`, `pendingBelowStopPrice` and/or `pendingBelowTrailingDelta`, `pendingBelowTimeInForce`|

**Data Source:**

Matching Engine

**Response:**

```javascript
{
    "orderListId": 1,
    "contingencyType": "OTO",
    "listStatusType": "EXEC_STARTED",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "RumwQpBaDctlUu5jyG5rs0",
    "transactionTime": 1712291372842,
    "symbol": "LTCBTC",
    "orders": [
        {
            "symbol": "LTCBTC",
            "orderId": 6,
            "clientOrderId": "fM9Y4m23IFJVCQmIrlUmMK"
        },
        {
            "symbol": "LTCBTC",
            "orderId": 7,
            "clientOrderId": "6pcQbFIzTXGZQ1e2MkGDq4"
        },
        {
            "symbol": "LTCBTC",
            "orderId": 8,
            "clientOrderId": "r4JMv9cwAYYUwwBZfbussx"
        }
    ],
    "orderReports": [
        {
            "symbol": "LTCBTC",
            "orderId": 6,
            "orderListId": 1,
            "clientOrderId": "fM9Y4m23IFJVCQmIrlUmMK",
            "transactTime": 1712291372842,
            "price": "1.00000000",
            "origQty": "1.00000000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "SELL",
            "workingTime": 1712291372842,
            "selfTradePreventionMode": "NONE"
        },
        {
            "symbol": "LTCBTC",
            "orderId": 7,
            "orderListId": 1,
            "clientOrderId": "6pcQbFIzTXGZQ1e2MkGDq4",
            "transactTime": 1712291372842,
            "price": "1.00000000",
            "origQty": "5.00000000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "PENDING_NEW",
            "timeInForce": "IOC",
            "type": "STOP_LOSS_LIMIT",
            "side": "BUY",
            "stopPrice": "6.00000000",
            "workingTime": -1,
            "selfTradePreventionMode": "NONE"
        },
        {
            "symbol": "LTCBTC",
            "orderId": 8,
            "orderListId": 1,
            "clientOrderId": "r4JMv9cwAYYUwwBZfbussx",
            "transactTime": 1712291372842,
            "price": "3.00000000",
            "origQty": "5.00000000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "PENDING_NEW",
            "timeInForce": "GTC",
            "type": "LIMIT_MAKER",
            "side": "BUY",
            "workingTime": -1,
            "selfTradePreventionMode": "NONE"
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

#### New Order List - OPO (TRADE)

```
POST /api/v3/orderList/opo
```

Place an [OPO](./faqs/opo.md).

* OPOs add 2 orders to the EXCHANGE_MAX_NUM_ORDERS filter and MAX_NUM_ORDERS filter.

**Weight:** 1

**Unfilled Order Count:** 2

**Parameters:**

| Name | Type | Mandatory | Description |
| ----- | ----- | ----- | ----- |
| symbol | STRING | YES |  |
| listClientOrderId | STRING | NO | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`. |
| newOrderRespType | ENUM | NO | Format of the JSON response. Supported values: [Order Response Type](./enums.md#orderresponsetype) |
| selfTradePreventionMode | ENUM | NO | The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](./enums.md#stpmodes) |
| workingType | ENUM | YES | Supported values: `LIMIT`,`LIMIT_MAKER` |
| workingSide | ENUM | YES | Supported values: [Order Side](./enums.md#side) |
| workingClientOrderId | STRING | NO | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent. |
| workingPrice | DECIMAL | YES |  |
| workingQuantity | DECIMAL | YES | Sets the quantity for the working order. |
| workingIcebergQty | DECIMAL | NO | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`. |
| workingTimeInForce | ENUM | NO | Supported values: [Time In Force](./enums.md#timeinforce) |
| workingStrategyId | LONG | NO | Arbitrary numeric value identifying the working order within an order strategy. |
| workingStrategyType | INT | NO | Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used. |
| workingPegPriceType | ENUM | NO | See [Pegged Orders](#pegged-orders-info) |
| workingPegOffsetType | ENUM | NO |  |
| workingPegOffsetValue | INT | NO |  |
| pendingType | ENUM | YES | Supported values: [Order Types](#order-type) Note that `MARKET` orders using `quoteOrderQty` are not supported. |
| pendingSide | ENUM | YES | Supported values: [Order Side](./enums.md#side) |
| pendingClientOrderId | STRING | NO | Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent. |
| pendingPrice | DECIMAL | NO |  |
| pendingStopPrice | DECIMAL | NO |  |
| pendingTrailingDelta | DECIMAL | NO |  |
| pendingIcebergQty | DECIMAL | NO | This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`. |
| pendingTimeInForce | ENUM | NO | Supported values: [Time In Force](./enums.md#timeinforce) |
| pendingStrategyId | LONG | NO | Arbitrary numeric value identifying the pending order within an order strategy. |
| pendingStrategyType | INT | NO | Arbitrary numeric value identifying the pending order strategy. Values smaller than 1000000 are reserved and cannot be used. |
| pendingPegPriceType | ENUM | NO | See [Pegged Orders](#pegged-orders-info) |
| pendingPegOffsetType | ENUM | NO |  |
| pendingPegOffsetValue | INT | NO |  |
| recvWindow | DECIMAL | NO | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified. |
| timestamp | LONG | YES |  |

**Data Source**: Matching Engine

**Response:**

```javascript
{
    "orderListId": 0,
    "contingencyType": "OTO",
    "listStatusType": "EXEC_STARTED",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "H94qCqO27P74OEiO4X8HOG",
    "transactionTime": 1762998011671,
    "symbol": "BTCUSDT",
    "orders": [
        {
            "symbol": "BTCUSDT",
            "orderId": 2,
            "clientOrderId": "JX6xfdjo0wysiGumfHNmPu"
        },
        {
            "symbol": "BTCUSDT",
            "orderId": 3,
            "clientOrderId": "2ZJCY0IjOhuYIMLGN8kU8S"
        }
    ],
    "orderReports": [
        {
            "symbol": "BTCUSDT",
            "orderId": 2,
            "orderListId": 0,
            "clientOrderId": "JX6xfdjo0wysiGumfHNmPu",
            "transactTime": 1762998011671,
            "price": "102264.00000000",
            "origQty": "0.00060000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.00000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "BUY",
            "workingTime": 1762998011671,
            "selfTradePreventionMode": "NONE"
        },
        {
            "symbol": "BTCUSDT",
            "orderId": 3,
            "orderListId": 0,
            "clientOrderId": "2ZJCY0IjOhuYIMLGN8kU8S",
            "transactTime": 1762998011671,
            "price": "0.00000000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.00000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "PENDING_NEW",
            "timeInForce": "GTC",
            "type": "MARKET",
            "side": "SELL",
            "workingTime": -1,
            "selfTradePreventionMode": "NONE"
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

#### New Order List - OPOCO (TRADE)

```
POST /api/v3/orderList/opoco
```

Place an [OPOCO](./faqs/opo.md).

**Weight**: 1

**Unfilled Order Count:** 3

**Parameters:**

| Name | Type | Mandatory | Description |
| ----- | ----- | ----- | ----- |
| symbol | STRING | YES |  |
| listClientOrderId | STRING | NO | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`. |
| newOrderRespType | ENUM | NO | Format of the JSON response. Supported values: [Order Response Type](./enums.md#orderresponsetype) |
| selfTradePreventionMode | ENUM | NO | The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](./enums.md#stpmodes) |
| workingType | ENUM | YES | Supported values: `LIMIT`, `LIMIT_MAKER` |
| workingSide | ENUM | YES | Supported values: [Order side](./enums.md#side) |
| workingClientOrderId | STRING | NO | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent. |
| workingPrice | DECIMAL | YES |  |
| workingQuantity | DECIMAL | YES |  |
| workingIcebergQty | DECIMAL | NO | This can only be used if `workingTimeInForce` is `GTC` or if `workingType` is `LIMIT_MAKER`. |
| workingTimeInForce | ENUM | NO | Supported values: [Time In Force](./enums.md#timeinforce) |
| workingStrategyId | LONG | NO | Arbitrary numeric value identifying the working order within an order strategy. |
| workingStrategyType | INT | NO | Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used. |
| workingPegPriceType | ENUM | NO | See [Pegged Orders](#pegged-orders-info) |
| workingPegOffsetType | ENUM | NO |  |
| workingPegOffsetValue | INT | NO |  |
| pendingSide | ENUM | YES | Supported values: [Order side](./enums.md#side) |
| pendingAboveType | ENUM | YES | Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` |
| pendingAboveClientOrderId | STRING | NO | Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent. |
| pendingAbovePrice | DECIMAL | NO | Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price. |
| pendingAboveStopPrice | DECIMAL | NO | Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` |
| pendingAboveTrailingDelta | DECIMAL | NO | See [Trailing Stop FAQ](./faqs/trailing-stop-faq.md) |
| pendingAboveIcebergQty | DECIMAL | NO | This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`. |
| pendingAboveTimeInForce | ENUM | NO |  |
| pendingAboveStrategyId | LONG | NO | Arbitrary numeric value identifying the pending above order within an order strategy. |
| pendingAboveStrategyType | INT | NO | Arbitrary numeric value identifying the pending above order strategy. Values smaller than 1000000 are reserved and cannot be used. |
| pendingAbovePegPriceType | ENUM | NO | See [Pegged Orders](#pegged-orders-info) |
| pendingAbovePegOffsetType | ENUM | NO |  |
| pendingAbovePegOffsetValue | INT | NO |  |
| pendingBelowType | ENUM | NO | Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT` |
| pendingBelowClientOrderId | STRING | NO | Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent. |
| pendingBelowPrice | DECIMAL | NO | Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify limit price |
| pendingBelowStopPrice | DECIMAL | NO | Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT, TAKE_PROFIT or TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified. |
| pendingBelowTrailingDelta | DECIMAL | NO |  |
| pendingBelowIcebergQty | DECIMAL | NO | This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`. |
| pendingBelowTimeInForce | ENUM | NO | Supported values: [Time In Force](./enums.md#timeinforce) |
| pendingBelowStrategyId | LONG | NO | Arbitrary numeric value identifying the pending below order within an order strategy. |
| pendingBelowStrategyType | INT | NO | Arbitrary numeric value identifying the pending below order strategy. Values smaller than 1000000 are reserved and cannot be used. |
| pendingBelowPegPriceType | ENUM | NO | See [Pegged Orders](#pegged-orders-info) |
| pendingBelowPegOffsetType | ENUM | NO |  |
| pendingBelowPegOffsetValue | INT | NO |  |
| recvWindow | DECIMAL | NO | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified. |
| timestamp | LONG | YES |  |

**Response**

```javascript
{
    "orderListId": 2,
    "contingencyType": "OTO",
    "listStatusType": "EXEC_STARTED",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "bcedxMpQG6nFrZUPQyshoL",
    "transactionTime": 1763000506354,
    "symbol": "BTCUSDT",
    "orders": [
        {
            "symbol": "BTCUSDT",
            "orderId": 9,
            "clientOrderId": "OLSBhMWaIlLSzZ9Zm7fnKB"
        },
        {
            "symbol": "BTCUSDT",
            "orderId": 10,
            "clientOrderId": "mfif39yPTHsB3C0FIXznR2"
        },
        {
            "symbol": "BTCUSDT",
            "orderId": 11,
            "clientOrderId": "yINkaXSJeoi3bU5vWMY8Z8"
        }
    ],
    "orderReports": [
        {
            "symbol": "BTCUSDT",
            "orderId": 9,
            "orderListId": 2,
            "clientOrderId": "OLSBhMWaIlLSzZ9Zm7fnKB",
            "transactTime": 1763000506354,
            "price": "102496.00000000",
            "origQty": "0.00170000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.00000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "BUY",
            "workingTime": 1763000506354,
            "selfTradePreventionMode": "NONE"
        },
        {
            "symbol": "BTCUSDT",
            "orderId": 10,
            "orderListId": 2,
            "clientOrderId": "mfif39yPTHsB3C0FIXznR2",
            "transactTime": 1763000506354,
            "price": "101613.00000000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.00000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "PENDING_NEW",
            "timeInForce": "GTC",
            "type": "STOP_LOSS_LIMIT",
            "side": "SELL",
            "stopPrice": "10100.00000000",
            "workingTime": -1,
            "selfTradePreventionMode": "NONE"
        },
        {
            "symbol": "BTCUSDT",
            "orderId": 11,
            "orderListId": 2,
            "clientOrderId": "yINkaXSJeoi3bU5vWMY8Z8",
            "transactTime": 1763000506354,
            "price": "104261.00000000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.00000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "PENDING_NEW",
            "timeInForce": "GTC",
            "type": "LIMIT_MAKER",
            "side": "SELL",
            "workingTime": -1,
            "selfTradePreventionMode": "NONE"
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

#### Cancel Order list (TRADE)

```
DELETE /api/v3/orderList
```
Cancel an entire Order list

**Weight:**
1

**Parameters:**

Name| Type| Mandatory| Description
----| ----|------|------
symbol|STRING| YES|
orderListId|LONG|NO| Either `orderListId` or `listClientOrderId` must be provided
listClientOrderId|STRING|NO| Either `orderListId` or `listClientOrderId` must be provided
newClientOrderId|STRING|NO| Used to uniquely identify this cancel. Automatically generated by default
recvWindow|DECIMAL|NO| The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp|LONG|YES|

**Notes:**
* Canceling an individual order from an order list will cancel the entire order list.
* If both `orderListId` and `listClientOrderId` parameters are provided, the `orderListId` is searched first, then the `listClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.

**Data Source:**
Matching Engine

**Response:**

```javascript
{
  "orderListId": 0,
  "contingencyType": "OCO",
  "listStatusType": "ALL_DONE",
  "listOrderStatus": "ALL_DONE",
  "listClientOrderId": "C3wyj4WVEktd7u9aVBRXcN",
  "transactionTime": 1574040868128,
  "symbol": "LTCBTC",
  "orders": [
    {
      "symbol": "LTCBTC",
      "orderId": 2,
      "clientOrderId": "pO9ufTiFGg3nw2fOdgeOXa"
    },
    {
      "symbol": "LTCBTC",
      "orderId": 3,
      "clientOrderId": "TXOvglzXuaubXAaENpaRCB"
    }
  ],
  "orderReports": [
    {
      "symbol": "LTCBTC",
      "origClientOrderId": "pO9ufTiFGg3nw2fOdgeOXa",
      "orderId": 2,
      "orderListId": 0,
      "clientOrderId": "unfWT8ig8i0uj6lPuYLez6",
      "transactTime": 1688005070874,
      "price": "1.00000000",
      "origQty": "10.00000000",
      "executedQty": "0.00000000",
      "origQuoteOrderQty": "0.000000",
      "cummulativeQuoteQty": "0.00000000",
      "status": "CANCELED",
      "timeInForce": "GTC",
      "type": "STOP_LOSS_LIMIT",
      "side": "SELL",
      "stopPrice": "1.00000000",
      "selfTradePreventionMode": "NONE"
    },
    {
      "symbol": "LTCBTC",
      "origClientOrderId": "TXOvglzXuaubXAaENpaRCB",
      "orderId": 3,
      "orderListId": 0,
      "clientOrderId": "unfWT8ig8i0uj6lPuYLez6",
      "transactTime": 1688005070874,
      "price": "3.00000000",
      "origQty": "10.00000000",
      "executedQty": "0.00000000",
      "origQuoteOrderQty": "0.000000",
      "cummulativeQuoteQty": "0.00000000",
      "status": "CANCELED",
      "timeInForce": "GTC",
      "type": "LIMIT_MAKER",
      "side": "SELL",
      "selfTradePreventionMode": "NONE"
    }
  ]
}
```

### SOR

#### New order using SOR (TRADE)

```
POST /api/v3/sor/order
```
Places an order using smart order routing (SOR).

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [SOR FAQ](faqs/sor_faq.md) to learn more.

**Weight:**
1

**Unfilled Order Count:**
1

**Parameters:**

Name                    | Type   | Mandatory | Description
------------            | -----  | ------------ | ------------
symbol                  | STRING | YES |
side                    | ENUM   | YES |
type                    | ENUM   | YES |
timeInForce             | ENUM   | NO |
quantity                | DECIMAL| YES |
price                   | DECIMAL| NO |
newClientOrderId        | STRING | NO | A unique id among open orders. Automatically generated if not sent.<br/> Orders with the same `newClientOrderID` can be accepted only when the previous one is filled, otherwise the order will be rejected.
strategyId              |LONG     | NO|
strategyType            |INT     | NO| The value cannot be less than `1000000`.
icebergQty              | DECIMAL| NO | Used with `LIMIT` to create an iceberg order.
newOrderRespType        | ENUM   | NO | Set the response JSON. `ACK`, `RESULT`, or `FULL`. Default to `FULL`
selfTradePreventionMode |ENUM    | NO | The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](enums.md#stpmodes).
recvWindow              | DECIMAL| NO |The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp               | LONG | YES |

**Note:** `POST /api/v3/sor/order` only supports `LIMIT` and `MARKET` orders. `quoteOrderQty` is not supported.

**Data Source:**
Matching Engine

**Response:**

```javascript
{
  "symbol": "BTCUSDT",
  "orderId": 2,
  "orderListId": -1,
  "clientOrderId": "sBI1KM6nNtOfj5tccZSKly",
  "transactTime": 1689149087774,
  "price": "31000.00000000",
  "origQty": "0.50000000",
  "executedQty": "0.50000000",
  "origQuoteOrderQty": "0.000000",
  "cummulativeQuoteQty": "14000.00000000",
  "status": "FILLED",
  "timeInForce": "GTC",
  "type": "LIMIT",
  "side": "BUY",
  "workingTime": 1689149087774,
  "fills": [
    {
      "matchType": "ONE_PARTY_TRADE_REPORT",
      "price": "28000.00000000",
      "qty": "0.50000000",
      "commission": "0.00000000",
      "commissionAsset": "BTC",
      "tradeId": -1,
      "allocId": 0
    }
  ],
  "workingFloor": "SOR",
  "selfTradePreventionMode": "NONE",
  "usedSor": true
}
```

#### Test new order using SOR (TRADE)

```
POST /api/v3/sor/order/test
```

Test new order creation and signature/recvWindow using smart order routing (SOR).
Creates and validates a new order but does not send it into the matching engine.

**Weight:**
| Condition | Request Weight |
| --------- | -------------- |
| Without `computeCommissionRates`  |  1 |
| With `computeCommissionRates`     | 20 |

**Parameters:**

In addition to all parameters accepted by [`POST /api/v3/sor/order`](#new-order-using-sor-trade),
the following optional parameters are also accepted:

Name                   |Type          | Mandatory    | Description
------------           | ------------ | ------------ | ------------
computeCommissionRates | BOOLEAN      | NO            | Default: `false`


**Data Source:**
Memory

**Response:**

Without `computeCommissionRates`

```
{}
```

With `computeCommissionRates`


```javascript
{
  "standardCommissionForOrder": {  //Standard commission rates on trades from the order.
    "maker": "0.00000112",
    "taker": "0.00000114"
  },
  "taxCommissionForOrder": {       //Tax commission rates for trades from the order
    "maker": "0.00000112",
    "taker": "0.00000114"
  },
  "discount": {                    //Discount on standard commissions when paying in BNB.
    "enabledForAccount": true,
    "enabledForSymbol": true,
    "discountAsset": "BNB",
    "discount": "0.25000000"       //Standard commission is reduced by this rate when paying commission in BNB.
  }
}
```



## Account Endpoints

### Account information (USER_DATA)
```
GET /api/v3/account
```
Get current account information.

**Weight:**
20

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
omitZeroBalances |BOOLEAN| NO | When set to `true`, emits only the non-zero balances of an account. <br>Default value: `false`
recvWindow | DECIMAL| NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |

**Data Source:**
Memory => Database

**Response:**
```javascript
{
  "makerCommission": 15,
  "takerCommission": 15,
  "buyerCommission": 0,
  "sellerCommission": 0,
  "commissionRates": {
    "maker": "0.00150000",
    "taker": "0.00150000",
    "buyer": "0.00000000",
    "seller": "0.00000000"
  },
  "canTrade": true,
  "canWithdraw": true,
  "canDeposit": true,
  "brokered": false,
  "requireSelfTradePrevention": false,
  "preventSor": false,
  "updateTime": 123456789,
  "accountType": "SPOT",
  "balances": [
    {
      "asset": "BTC",
      "free": "4723846.89208129",
      "locked": "0.00000000"
    },
    {
      "asset": "LTC",
      "free": "4763368.68006011",
      "locked": "0.00000000"
    }
  ],
  "permissions": [
    "SPOT"
  ],
  "uid": 354937868
}
```

### Query order (USER_DATA)
```
GET /api/v3/order
```
Check an order's status.

**Weight:**
4

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
orderId | LONG | NO |
origClientOrderId | STRING | NO |
recvWindow | DECIMAL| NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |

**Notes:**
* Either `orderId` or `origClientOrderId` must be sent.
* If both `orderId` and `origClientOrderId` are provided, the `orderId` is searched first, then the `origClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.
* For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.

**Data Source:**
Memory => Database

**Response:**
```javascript
{
  "symbol": "LTCBTC",
  "orderId": 1,
  "orderListId": -1,                 // This field will always have a value of -1 if not an order list.
  "clientOrderId": "myOrder1",
  "price": "0.1",
  "origQty": "1.0",
  "executedQty": "0.0",
  "cummulativeQuoteQty": "0.0",
  "status": "NEW",
  "timeInForce": "GTC",
  "type": "LIMIT",
  "side": "BUY",
  "stopPrice": "0.0",
  "icebergQty": "0.0",
  "time": 1499827319559,
  "updateTime": 1499827319559,
  "isWorking": true,
  "workingTime":1499827319559,
  "origQuoteOrderQty": "0.000000",
  "selfTradePreventionMode": "NONE"
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

### Current open orders (USER_DATA)
```
GET /api/v3/openOrders
```
Get all open orders on a symbol. **Careful** when accessing this with no symbol.

**Weight:**
6 for a single symbol; **80** when the symbol parameter is omitted

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | NO |
recvWindow | DECIMAL| NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |

* If the symbol is not sent, orders for all symbols will be returned in an array.

**Data Source:**
Memory => Database

**Response:**
```javascript
[
  {
    "symbol": "LTCBTC",
    "orderId": 1,
    "orderListId": -1, // Unless it's part of an order list, value will be -1
    "clientOrderId": "myOrder1",
    "price": "0.1",
    "origQty": "1.0",
    "executedQty": "0.0",
    "cummulativeQuoteQty": "0.0",
    "status": "NEW",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "BUY",
    "stopPrice": "0.0",
    "icebergQty": "0.0",
    "time": 1499827319559,
    "updateTime": 1499827319559,
    "isWorking": true,
    "origQuoteOrderQty": "0.000000",
    "workingTime": 1499827319559,
    "selfTradePreventionMode": "NONE"
  }
]
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

### All orders (USER_DATA)
```
GET /api/v3/allOrders
```
Get all account orders; active, canceled, or filled.

**Weight:**
20

**Data Source:**
Database

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
orderId | LONG | NO |
startTime | LONG | NO |
endTime | LONG | NO |
limit | INT | NO | Default: 500; Maximum: 1000.
recvWindow | DECIMAL | NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |

**Notes:**
* If `orderId` is set, it will get orders >= that `orderId`. Otherwise most recent orders are returned.
* For some historical orders `cummulativeQuoteQty` will be < 0, meaning the data is not available at this time.
* If `startTime` and/or `endTime` provided, `orderId`  is not required.
* The time between `startTime` and `endTime` can't be longer than 24 hours.

**Response:**
```javascript
[
  {
    "symbol": "LTCBTC",
    "orderId": 1,
    "orderListId": -1, //Unless it's part of an order list, value will be -1
    "clientOrderId": "myOrder1",
    "price": "0.1",
    "origQty": "1.0",
    "executedQty": "0.0",
    "cummulativeQuoteQty": "0.0",
    "status": "NEW",
    "timeInForce": "GTC",
    "type": "LIMIT",
    "side": "BUY",
    "stopPrice": "0.0",
    "icebergQty": "0.0",
    "time": 1499827319559,
    "updateTime": 1499827319559,
    "isWorking": true,
    "origQuoteOrderQty": "0.000000",
    "workingTime": 1499827319559,
    "selfTradePreventionMode": "NONE"
  }
]
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).


### Query Order list (USER_DATA)

```
GET /api/v3/orderList
```
Retrieves a specific order list based on provided optional parameters.

**Weight:**
4

**Parameters:**

Name| Type|Mandatory| Description
----|-----|----|----------
orderListId|LONG|NO*| Query order list by `orderListId`. <br>`orderListId` or `origClientOrderId` must be provided.
origClientOrderId|STRING|NO*| Query order list by `listClientOrderId`. <br>`orderListId` or `origClientOrderId` must be provided.
recvWindow|DECIMAL|NO| The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp|LONG|YES|

**Data Source:**
Database

**Response:**

```javascript
{
  "orderListId": 27,
  "contingencyType": "OCO",
  "listStatusType": "EXEC_STARTED",
  "listOrderStatus": "EXECUTING",
  "listClientOrderId": "h2USkA5YQpaXHPIrkd96xE",
  "transactionTime": 1565245656253,
  "symbol": "LTCBTC",
  "orders": [
    {
      "symbol": "LTCBTC",
      "orderId": 4,
      "clientOrderId": "qD1gy3kc3Gx0rihm9Y3xwS"
    },
    {
      "symbol": "LTCBTC",
      "orderId": 5,
      "clientOrderId": "ARzZ9I00CPM8i3NhmU9Ega"
    }
  ]
}
```

### Query all Order lists (USER_DATA)

```
GET /api/v3/allOrderList
```
Retrieves all order lists based on provided optional parameters.

Note that the time between `startTime` and `endTime` can't be longer than 24 hours.

**Weight:**
20

**Parameters:**

Name|Type| Mandatory| Description
----|----|----|---------
fromId|LONG|NO| If supplied, neither `startTime` or `endTime` can be provided
startTime|LONG|NO|
endTime|LONG|NO|
limit|INT|NO| Default: 500; Maximum: 1000
recvWindow|DECIMAL|NO| The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp|LONG|YES|

**Data Source:**
Database

**Response:**

```javascript
[
  {
    "orderListId": 29,
    "contingencyType": "OCO",
    "listStatusType": "EXEC_STARTED",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "amEEAXryFzFwYF1FeRpUoZ",
    "transactionTime": 1565245913483,
    "symbol": "LTCBTC",
    "orders": [
      {
        "symbol": "LTCBTC",
        "orderId": 4,
        "clientOrderId": "oD7aesZqjEGlZrbtRpy5zB"
      },
      {
        "symbol": "LTCBTC",
        "orderId": 5,
        "clientOrderId": "Jr1h6xirOxgeJOUuYQS7V3"
      }
    ]
  },
  {
    "orderListId": 28,
    "contingencyType": "OCO",
    "listStatusType": "EXEC_STARTED",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "hG7hFNxJV6cZy3Ze4AUT4d",
    "transactionTime": 1565245913407,
    "symbol": "LTCBTC",
    "orders": [
      {
        "symbol": "LTCBTC",
        "orderId": 2,
        "clientOrderId": "j6lFOfbmFMRjTYA7rRJ0LP"
      },
      {
        "symbol": "LTCBTC",
        "orderId": 3,
        "clientOrderId": "z0KCjOdditiLS5ekAFtK81"
      }
    ]
  }
]
```

### Query Open Order lists (USER_DATA)

```
GET /api/v3/openOrderList
```

**Weight:**
6

**Parameters:**

Name| Type|Mandatory| Description
----|-----|---|------------------
recvWindow|DECIMAL|NO| The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp|LONG|YES|

**Data Source:**
Database

**Response:**

```javascript
[
  {
    "orderListId": 31,
    "contingencyType": "OCO",
    "listStatusType": "EXEC_STARTED",
    "listOrderStatus": "EXECUTING",
    "listClientOrderId": "wuB13fmulKj3YjdqWEcsnp",
    "transactionTime": 1565246080644,
    "symbol": "LTCBTC",
    "orders": [
      {
        "symbol": "LTCBTC",
        "orderId": 4,
        "clientOrderId": "r3EH2N76dHfLoSZWIUw1bT"
      },
      {
        "symbol": "LTCBTC",
        "orderId": 5,
        "clientOrderId": "Cv1SnyPD3qhqpbjpYEHbd2"
      }
    ]
  }
]
```

### Account trade list (USER_DATA)
```
GET /api/v3/myTrades
```
Get trades for a specific account and symbol.

**Weight:**

Condition| Weight|
---| ---
|Without orderId|20|
|With orderId|5|


**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
symbol | STRING | YES |
orderId|LONG|NO| This can only be used in combination with `symbol`.
startTime | LONG | NO |
endTime | LONG | NO |
fromId | LONG | NO | TradeId to fetch from. Default gets most recent trades.
limit | INT | NO | Default: 500; Maximum: 1000.
recvWindow | DECIMAL | NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |

**Notes:**
* If `fromId` is set, it will get trades >= that `fromId`.
Otherwise most recent trades are returned.
* The time between `startTime` and `endTime` can't be longer than 24 hours.
* These are the supported combinations of all parameters:
  * `symbol`
  * `symbol` + `orderId`
  * `symbol` + `startTime`
  * `symbol` + `endTime`
  * `symbol` + `fromId`
  * `symbol` + `startTime` + `endTime`
  * `symbol`+ `orderId` + `fromId`

**Data Source:**
Memory => Database

**Response:**
```javascript
[
  {
    "symbol": "BNBBTC",
    "id": 28457,
    "orderId": 100234,
    "orderListId": -1,
    "price": "4.00000100",
    "qty": "12.00000000",
    "quoteQty": "48.000012",
    "commission": "10.10000000",
    "commissionAsset": "BNB",
    "time": 1499865549590,
    "isBuyer": true,
    "isMaker": false,
    "isBestMatch": true
  }
]
```
<a id="query-unfilled-order-count"></a>
### Query Unfilled Order Count (USER_DATA)
```
GET /api/v3/rateLimit/order
```

Displays the user's unfilled order count for all intervals.

**Weight:**
40

**Parameters:**

Name | Type | Mandatory | Description
------------ | ------------ | ------------ | ------------
recvWindow | DECIMAL | NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |

**Data Source:**
Memory

**Response:**

```json
[
  {
    "rateLimitType": "ORDERS",
    "interval": "SECOND",
    "intervalNum": 10,
    "limit": 50,
    "count": 0
  },
  {
    "rateLimitType": "ORDERS",
    "interval": "DAY",
    "intervalNum": 1,
    "limit": 160000,
    "count": 0
  }
]
```

### Query Prevented Matches (USER_DATA)

```
GET /api/v3/myPreventedMatches
```

Displays the list of orders that were expired due to STP.

These are the combinations supported:

* `symbol` + `preventedMatchId`
* `symbol` + `orderId`
* `symbol` + `orderId` + `fromPreventedMatchId` (`limit` will default to 500)
* `symbol` + `orderId` + `fromPreventedMatchId` + `limit`

**Parameters:**

Name                | Type   | Mandatory    | Description
------------        | ----   | ------------ | ------------
symbol              | STRING | YES          |
preventedMatchId    |LONG    | NO           |
orderId             |LONG    | NO           |
fromPreventedMatchId|LONG    | NO           |
limit               |INT     | NO           | Default: `500`; Maximum: `1000`
recvWindow          |DECIMAL | NO           | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp           | LONG   | YES          |

**Weight:**

Case                            | Weight
----                            | -----
If `symbol` is invalid          | 2
Querying by `preventedMatchId`  | 2
Querying by `orderId`           | 20

**Data Source:**

Database

**Response:**

```json
[
  {
    "symbol": "BTCUSDT",
    "preventedMatchId": 1,
    "takerOrderId": 5,
    "makerSymbol": "BTCUSDT",
    "makerOrderId": 3,
    "tradeGroupId": 1,
    "selfTradePreventionMode": "EXPIRE_MAKER",
    "price": "1.100000",
    "makerPreventedQuantity": "1.300000",
    "transactTime": 1669101687094
  }
]
```

### Query Allocations (USER_DATA)

```
GET /api/v3/myAllocations
```

Retrieves allocations resulting from SOR order placement.

**Weight:**
20

**Parameters:**

Name                     | Type  |Mandatory | Description
-----                    | ---   |----      | ---------
symbol                   |STRING |Yes        |
startTime                |LONG   |No        |
endTime                  |LONG   |No        |
fromAllocationId         |INT    |No        |
limit                    |INT    |No        |Default: 500; Maximum: 1000
orderId                  |LONG   |No        |
recvWindow               |DECIMAL|No        |The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp                |LONG   |No        |

Supported parameter combinations:

Parameters                                  | Response |
------------------------------------------- | -------- |
`symbol`                                    | allocations from oldest to newest |
`symbol` + `startTime`                      | oldest allocations since `startTime` |
`symbol` + `endTime`                        | newest allocations until `endTime` |
`symbol` + `startTime` + `endTime`          | allocations within the time range |
`symbol` + `fromAllocationId`               | allocations by allocation ID |
`symbol` + `orderId`                        | allocations related to an order starting with oldest |
`symbol` + `orderId` + `fromAllocationId`   | allocations related to an order by allocation ID |

**Note:** The time between `startTime` and `endTime` can't be longer than 24 hours.

**Data Source:**
Database

**Response:**

```javascript
[
  {
    "symbol": "BTCUSDT",
    "allocationId": 0,
    "allocationType": "SOR",
    "orderId": 1,
    "orderListId": -1,
    "price": "1.00000000",
    "qty": "5.00000000",
    "quoteQty": "5.00000000",
    "commission": "0.00000000",
    "commissionAsset": "BTC",
    "time": 1687506878118,
    "isBuyer": true,
    "isMaker": false,
    "isAllocator": false
  }
]
```

### Query Commission Rates (USER_DATA)

```
GET /api/v3/account/commission
```

Get current account commission rates.


**Weight:**
20

**Parameters:**

Name         | Type    | Mandatory | Description
------------ | -----   | ------------ | ------------
symbol        | STRING | YES          |

**Data Source:**
Database

**Response:**

```javascript
{
  "symbol": "BTCUSDT",
  "standardCommission": {         //Commission rates on trades from the order.
    "maker": "0.00000010",
    "taker": "0.00000020",
    "buyer": "0.00000030",
    "seller": "0.00000040"
  },
  "specialCommission": {         // Special commission rates from the order.
    "maker": "0.01000000",
    "taker": "0.02000000",
    "buyer": "0.03000000",
    "seller": "0.04000000"
  },
  "taxCommission": {              //Tax commission rates for trades from the order.
    "maker": "0.00000112",
    "taker": "0.00000114",
    "buyer": "0.00000118",
    "seller": "0.00000116"
  },
  "discount": {                   //Discount commission when paying in BNB
    "enabledForAccount": true,
    "enabledForSymbol": true,
    "discountAsset": "BNB",
    "discount": "0.75000000"      //Standard commission is reduced by this rate when paying commission in BNB.
  }
}
```

### Query Order Amendments (USER_DATA)

```
GET /api/v3/order/amendments
```

Queries all amendments of a single order.

**Weight**:
4

**Parameters:**

Name | Type | Mandatory | Description |
:---- | :---- | :---- | :---- |
symbol | STRING | YES |  |
orderId | LONG | YES |  |
fromExecutionId | LONG | NO |  |
limit | LONG | NO | Default:500; Maximum: 1000 |
recvWindow | DECIMAL | NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |

**Data Source:**

Database

**Response:**

```json
[
  {
      "symbol": "BTCUSDT",
      "orderId": 9,
      "executionId": 22,
      "origClientOrderId": "W0fJ9fiLKHOJutovPK3oJp",
      "newClientOrderId": "UQ1Np3bmQ71jJzsSDW9Vpi",
      "origQty": "5.00000000",
      "newQty": "4.00000000",
      "time": 1741669661670
  },
  {
      "symbol": "BTCUDST",
      "orderId": 9,
      "executionId": 25,
      "origClientOrderId": "UQ1Np3bmQ71jJzsSDW9Vpi",
      "newClientOrderId": "5uS0r35ohuQyDlCzZuYXq2",
      "origQty": "4.00000000",
      "newQty": "3.00000000",
      "time": 1741672924895
  }
]
```

<a id="myFilters"></a>
### Query relevant filters (USER_DATA)

```
GET /api/v3/myFilters
```

Retrieves the list of [filters](filters.md) relevant to an account on a given symbol. This is the only endpoint that shows if an account has [`MAX_ASSET`](filters.md#max_asset) filters applied to it.

**Weight:**
40

**Parameters:**

Name       | Type         | Mandatory    | Description
---------- | ------------ | ------------ | ------------
symbol     | STRING       | YES          |
recvWindow | DECIMAL      | NO           | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp  | LONG         | YES          |

**Data Source:**
Memory

**Response:**

```javascript
{
  "exchangeFilters": [
    {
      "filterType": "EXCHANGE_MAX_NUM_ORDERS",
      "maxNumOrders": 1000
    }
  ],
  "symbolFilters": [
    {
      "filterType": "MAX_NUM_ORDER_LISTS",
      "maxNumOrderLists": 20
    }
  ],
  "assetFilters": [
    {
      "filterType": "MAX_ASSET",
      "asset": "JPY",
      "limit": "1000000.00000000"
    }
  ]
}
```
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [WebSocket Streams for Binance](#websocket-streams-for-binance)
  - [General WSS information](#general-wss-information)
  - [WebSocket Limits](#websocket-limits)
  - [Live Subscribing/Unsubscribing to streams](#live-subscribingunsubscribing-to-streams)
    - [Subscribe to a stream](#subscribe-to-a-stream)
    - [Unsubscribe to a stream](#unsubscribe-to-a-stream)
    - [Listing Subscriptions](#listing-subscriptions)
    - [Setting Properties](#setting-properties)
    - [Retrieving Properties](#retrieving-properties)
    - [Error Messages](#error-messages)
- [Detailed Stream information](#detailed-stream-information)
  - [Aggregate Trade Streams](#aggregate-trade-streams)
  - [Trade Streams](#trade-streams)
  - [Kline/Candlestick Streams for UTC](#klinecandlestick-streams-for-utc)
  - [Kline/Candlestick Streams with timezone offset](#klinecandlestick-streams-with-timezone-offset)
  - [Individual Symbol Mini Ticker Stream](#individual-symbol-mini-ticker-stream)
  - [All Market Mini Tickers Stream](#all-market-mini-tickers-stream)
  - [Individual Symbol Ticker Streams](#individual-symbol-ticker-streams)
  - [Individual Symbol Rolling Window Statistics Streams](#individual-symbol-rolling-window-statistics-streams)
  - [All Market Rolling Window Statistics Streams](#all-market-rolling-window-statistics-streams)
  - [Individual Symbol Book Ticker Streams](#individual-symbol-book-ticker-streams)
  - [Average Price](#average-price)
  - [Partial Book Depth Streams](#partial-book-depth-streams)
  - [Diff. Depth Stream](#diff-depth-stream)
  - [How to manage a local order book correctly](#how-to-manage-a-local-order-book-correctly)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# WebSocket Streams for Binance

## General WSS information
* The base endpoint is: **wss://stream.binance.com:9443** or **wss://stream.binance.com:443**.
* Streams can be accessed either in a single raw stream or in a combined stream.
* Raw streams are accessed at **/ws/\<streamName\>**
* Combined streams are accessed at **/stream?streams=\<streamName1\>/\<streamName2\>/\<streamName3\>**
* Combined stream events are wrapped as follows: **{"stream":"\<streamName\>","data":\<rawPayload\>}**
* All symbols for streams are **lowercase**
* A single connection to **stream.binance.com** is only valid for 24 hours; expect to be disconnected at the 24 hour mark
* The WebSocket server will send a `ping frame` every 20 seconds.
  * If the WebSocket server does not receive a `pong frame` back from the connection within a minute the connection will be disconnected.
  * When you receive a ping, you must send a pong with a copy of ping's payload as soon as possible.
  * Unsolicited `pong frames` are allowed, but will not prevent disconnection. **It is recommended that the payload for these pong frames are empty.**
* The base endpoint **wss://data-stream.binance.vision** can be subscribed to receive **only** market data messages. <br> User data stream is **NOT** available from this URL.
* All time and timestamp related fields are **milliseconds by default**. To receive the information in microseconds, please add the parameter `timeUnit=MICROSECOND or timeUnit=microsecond` in the URL.
  * For example: `/stream?streams=btcusdt@trade&timeUnit=MICROSECOND`
* If your request contains a symbol name containing non-ASCII characters, then the stream events may contain non-ASCII characters encoded in UTF-8.
* [All Market Mini Tickers Stream](#all-market-mini-tickers-stream and [All Market Rolling Window Statistics Streams](#all-market-rolling-window-statistics-streams) events may contain non-ASCII characters encoded in UTF-8.

## WebSocket Limits
* WebSocket connections have a limit of 5 incoming messages per second. A message is considered:
    * A PING frame
    * A PONG frame
    * A JSON controlled message (e.g. subscribe, unsubscribe)
* A connection that goes beyond the limit will be disconnected; IPs that are repeatedly disconnected may be banned.
* A single connection can listen to a maximum of 1024 streams.
* There is a limit of **300 connections per attempt every 5 minutes per IP**.

## Live Subscribing/Unsubscribing to streams

* The following data can be sent through the WebSocket instance in order to subscribe/unsubscribe from streams. Examples can be seen below.
* The `id` is used as an identifier to uniquely identify the messages going back and forth. The following formats are accepted:
  * 64-bit signed integer
  * alphanumeric strings; max length 36
  * `null`
* In the response, if the `result` received is `null` this means the request sent was a success for non-query requests (e.g. Subscribing/Unsubscribing).

### Subscribe to a stream
* Request
  ```javascript
  {
    "method": "SUBSCRIBE",
    "params": [
      "btcusdt@aggTrade",
      "btcusdt@depth"
    ],
    "id": 1
  }
  ```

* Response
  ```javascript
  {
    "result": null,
    "id": 1
  }
  ```

### Unsubscribe to a stream
* Request
  ```javascript
  {
    "method": "UNSUBSCRIBE",
    "params": [
      "btcusdt@depth"
    ],
    "id": 312
  }
  ```

* Response
  ```javascript
  {
    "result": null,
    "id": 312
  }
  ```


### Listing Subscriptions
* Request
  ```javascript
  {
    "method": "LIST_SUBSCRIPTIONS",
    "id": 3
  }
  ```

* Response
  ```javascript
  {
    "result": [
      "btcusdt@aggTrade"
    ],
    "id": 3
  }
  ```


### Setting Properties
Currently, the only property that can be set is whether `combined` stream payloads are enabled or not.
The combined property is set to `false` when connecting using `/ws/` ("raw streams") and `true` when connecting using `/stream/`.

* Request
  ```javascript
  {
    "method": "SET_PROPERTY",
    "params": [
      "combined",
      true
    ],
    "id": 5
  }
  ```

* Response
  ```javascript
  {
    "result": null,
    "id": 5
  }
  ```

### Retrieving Properties
* Request
  ```javascript
  {
    "method": "GET_PROPERTY",
    "params": [
      "combined"
    ],
    "id": 2
  }
  ```

* Response
  ```javascript
  {
    "result": true, // Indicates that combined is set to true.
    "id": 2
  }
  ```

### Error Messages

Error Message | Description
---|---
{"code": 0, "msg": "Unknown property","id": %s} | Parameter used in the `SET_PROPERTY` or `GET_PROPERTY` was invalid
{"code": 1, "msg": "Invalid value type: expected Boolean"} | Value should only be `true` or `false`
{"code": 2, "msg": "Invalid request: property name must be a string"}| Property name provided was invalid
{"code": 2, "msg": "Invalid request: request ID must be an unsigned integer"}| Parameter `id` had to be provided or the value provided in the `id` parameter is an unsupported type
{"code": 2, "msg": "Invalid request: unknown variant %s, expected one of `SUBSCRIBE`, `UNSUBSCRIBE`, `LIST_SUBSCRIPTIONS`, `SET_PROPERTY`, `GET_PROPERTY` at line 1 column 28"} | Possible typo in the provided method or provided method was neither of the expected values
{"code": 2, "msg": "Invalid request: too many parameters"}| Unnecessary parameters provided in the data
{"code": 2, "msg": "Invalid request: property name must be a string"} | Property name was not provided
{"code": 2, "msg": "Invalid request: missing field `method` at line 1 column 73"} | `method` was not provided in the data
{"code":3,"msg":"Invalid JSON: expected value at line %s column %s"} | JSON data sent has incorrect syntax.


# Detailed Stream information
## Aggregate Trade Streams
The Aggregate Trade Streams push trade information that is aggregated for a single taker order.

**Stream Name:** \<symbol\>@aggTrade

**Update Speed:** Real-time

**Payload:**
```javascript
{
  "e": "aggTrade",    // Event type
  "E": 1672515782136, // Event time
  "s": "BNBBTC",      // Symbol
  "a": 12345,         // Aggregate trade ID
  "p": "0.001",       // Price
  "q": "100",         // Quantity
  "f": 100,           // First trade ID
  "l": 105,           // Last trade ID
  "T": 1672515782136, // Trade time
  "m": true,          // Is the buyer the market maker?
  "M": true           // Ignore
}
```

## Trade Streams
The Trade Streams push raw trade information; each trade has a unique buyer and seller.

**Stream Name:** \<symbol\>@trade

**Update Speed:** Real-time

**Payload:**
```javascript
{
  "e": "trade",       // Event type
  "E": 1672515782136, // Event time
  "s": "BNBBTC",      // Symbol
  "t": 12345,         // Trade ID
  "p": "0.001",       // Price
  "q": "100",         // Quantity
  "T": 1672515782136, // Trade time
  "m": true,          // Is the buyer the market maker?
  "M": true           // Ignore
}
```

## Kline/Candlestick Streams for UTC
The Kline/Candlestick Stream push updates to the current klines/candlestick every second in `UTC+0` timezone

<a id="kline-intervals"></a>
**Kline/Candlestick chart intervals:**

s-> seconds; m -> minutes; h -> hours; d -> days; w -> weeks; M -> months

* 1s
* 1m
* 3m
* 5m
* 15m
* 30m
* 1h
* 2h
* 4h
* 6h
* 8h
* 12h
* 1d
* 3d
* 1w
* 1M


**Stream Name:** \<symbol\>@kline_\<interval\>

**Update Speed:** 1000ms for `1s`, 2000ms for the other intervals

**Payload:**
```javascript
{
  "e": "kline",         // Event type
  "E": 1672515782136,   // Event time
  "s": "BNBBTC",        // Symbol
  "k": {
    "t": 1672515780000, // Kline start time
    "T": 1672515839999, // Kline close time
    "s": "BNBBTC",      // Symbol
    "i": "1m",          // Interval
    "f": 100,           // First trade ID
    "L": 200,           // Last trade ID
    "o": "0.0010",      // Open price
    "c": "0.0020",      // Close price
    "h": "0.0025",      // High price
    "l": "0.0015",      // Low price
    "v": "1000",        // Base asset volume
    "n": 100,           // Number of trades
    "x": false,         // Is this kline closed?
    "q": "1.0000",      // Quote asset volume
    "V": "500",         // Taker buy base asset volume
    "Q": "0.500",       // Taker buy quote asset volume
    "B": "123456"       // Ignore
  }
}
```

## Kline/Candlestick Streams with timezone offset
The Kline/Candlestick Stream push updates to the current klines/candlestick every second in `UTC+8` timezone

**Kline/Candlestick chart intervals:**

Supported intervals: See [`Kline/Candlestick chart intervals`](#kline-intervals)

**UTC+8 timezone offset:**

* Kline intervals open and close in the `UTC+8` timezone. For example the `1d` klines will open at the beginning of the `UTC+8` day, and close at the end of the `UTC+8` day.
* Note that `E` (event time), `t` (start time) and `T` (close time) in the payload are Unix timestamps, which are always interpreted in UTC.

**Stream Name:** \<symbol\>@kline_\<interval\>@+08:00

**Update Speed:** 1000ms for `1s`, 2000ms for the other intervals

**Payload:**
```javascript
{
  "e": "kline",         // Event type
  "E": 1672515782136,   // Event time
  "s": "BNBBTC",        // Symbol
  "k": {
    "t": 1672515780000, // Kline start time
    "T": 1672515839999, // Kline close time
    "s": "BNBBTC",      // Symbol
    "i": "1m",          // Interval
    "f": 100,           // First trade ID
    "L": 200,           // Last trade ID
    "o": "0.0010",      // Open price
    "c": "0.0020",      // Close price
    "h": "0.0025",      // High price
    "l": "0.0015",      // Low price
    "v": "1000",        // Base asset volume
    "n": 100,           // Number of trades
    "x": false,         // Is this kline closed?
    "q": "1.0000",      // Quote asset volume
    "V": "500",         // Taker buy base asset volume
    "Q": "0.500",       // Taker buy quote asset volume
    "B": "123456"       // Ignore
  }
}
```

## Individual Symbol Mini Ticker Stream
24hr rolling window mini-ticker statistics. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

**Stream Name:** \<symbol\>@miniTicker

**Update Speed:** 1000ms

**Payload:**
```javascript
  {
    "e": "24hrMiniTicker",  // Event type
    "E": 1672515782136,     // Event time
    "s": "BNBBTC",          // Symbol
    "c": "0.0025",          // Close price
    "o": "0.0010",          // Open price
    "h": "0.0025",          // High price
    "l": "0.0010",          // Low price
    "v": "10000",           // Total traded base asset volume
    "q": "18"               // Total traded quote asset volume
  }
```

## All Market Mini Tickers Stream
24hr rolling window mini-ticker statistics for all symbols that changed in an array. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs. Note that only tickers that have changed will be present in the array.

**Stream Name:** !miniTicker@arr

**Update Speed:** 1000ms

**Payload:**
```javascript
[
  {
    // Same as <symbol>@miniTicker payload
  }
]
```

## Individual Symbol Ticker Streams
24hr rolling window ticker statistics for a single symbol. These are NOT the statistics of the UTC day, but a 24hr rolling window for the previous 24hrs.

**Stream Name:** \<symbol\>@ticker

**Update Speed:** 1000ms

**Payload:**
```javascript
{
  "e": "24hrTicker",  // Event type
  "E": 1672515782136, // Event time
  "s": "BNBBTC",      // Symbol
  "p": "0.0015",      // Price change
  "P": "250.00",      // Price change percent
  "w": "0.0018",      // Weighted average price
  "x": "0.0009",      // First trade(F)-1 price (first trade before the 24hr rolling window)
  "c": "0.0025",      // Last price
  "Q": "10",          // Last quantity
  "b": "0.0024",      // Best bid price
  "B": "10",          // Best bid quantity
  "a": "0.0026",      // Best ask price
  "A": "100",         // Best ask quantity
  "o": "0.0010",      // Open price
  "h": "0.0025",      // High price
  "l": "0.0010",      // Low price
  "v": "10000",       // Total traded base asset volume
  "q": "18",          // Total traded quote asset volume
  "O": 0,             // Statistics open time
  "C": 86400000,      // Statistics close time
  "F": 0,             // First trade ID
  "L": 18150,         // Last trade Id
  "n": 18151          // Total number of trades
}
```

## Individual Symbol Rolling Window Statistics Streams

Rolling window ticker statistics for a single symbol, computed over multiple windows.

**Stream Name:** \<symbol\>@ticker_\<window_size\>

**Window Sizes:** 1h,4h,1d

**Update Speed:** 1000ms

**Note**: This stream is different from the \<symbol\>@ticker stream.
The open time `"O"` always starts on a minute, while the closing time `"C"` is the current time of the update.
As such, the effective window might be up to 59999ms wider than \<window_size\>.

**Payload:**

```javascript
{
  "e": "1hTicker",    // Event type
  "E": 1672515782136, // Event time
  "s": "BNBBTC",      // Symbol
  "p": "0.0015",      // Price change
  "P": "250.00",      // Price change percent
  "o": "0.0010",      // Open price
  "h": "0.0025",      // High price
  "l": "0.0010",      // Low price
  "c": "0.0025",      // Last price
  "w": "0.0018",      // Weighted average price
  "v": "10000",       // Total traded base asset volume
  "q": "18",          // Total traded quote asset volume
  "O": 0,             // Statistics open time
  "C": 1675216573749, // Statistics close time
  "F": 0,             // First trade ID
  "L": 18150,         // Last trade Id
  "n": 18151          // Total number of trades
}
```


## All Market Rolling Window Statistics Streams

Rolling window ticker statistics for all market symbols, computed over multiple windows.
Note that only tickers that have changed will be present in the array.

**Stream Name:** !ticker_\<window-size\>@arr

**Window Size:** 1h,4h,1d

**Update Speed:** 1000ms

**Payload:**
```javascript
[
  {
    // Same as <symbol>@ticker_<window_size> payload,
    // one for each symbol updated within the interval.
  }
]
```


## Individual Symbol Book Ticker Streams
Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol.
Multiple `<symbol>@bookTicker` streams can be subscribed to over one connection.

**Stream Name:** \<symbol\>@bookTicker

**Update Speed:** Real-time

**Payload:**
```javascript
{
  "u":400900217,     // order book updateId
  "s":"BNBUSDT",     // symbol
  "b":"25.35190000", // best bid price
  "B":"31.21000000", // best bid qty
  "a":"25.36520000", // best ask price
  "A":"40.66000000"  // best ask qty
}
```

## Average Price

Average price streams push changes in the average price over a fixed time interval.

**Stream Name:** \<symbol\>@avgPrice

**Update Speed:** 1000ms

**Payload:**

```javascript
{
  "e": "avgPrice",          // Event type
  "E": 1693907033000,       // Event time
  "s": "BTCUSDT",           // Symbol
  "i": "5m",                // Average price interval
  "w": "25776.86000000",    // Average price
  "T": 1693907032213        // Last trade time
}
```

## Partial Book Depth Streams
Top **\<levels\>** bids and asks, pushed every second. Valid **\<levels\>** are 5, 10, or 20.

**Stream Names:** \<symbol\>@depth\<levels\> OR \<symbol\>@depth\<levels\>@100ms

**Update Speed:** 1000ms or 100ms

**Payload:**
```javascript
{
  "lastUpdateId": 160,  // Last update ID
  "bids": [             // Bids to be updated
    [
      "0.0024",         // Price level to be updated
      "10"              // Quantity
    ]
  ],
  "asks": [             // Asks to be updated
    [
      "0.0026",         // Price level to be updated
      "100"             // Quantity
    ]
  ]
}
```

## Diff. Depth Stream
Order book price and quantity depth updates used to locally manage an order book.

**Stream Name:** \<symbol\>@depth OR \<symbol\>@depth@100ms

**Update Speed:** 1000ms or 100ms

**Payload:**
```javascript
{
  "e": "depthUpdate", // Event type
  "E": 1672515782136, // Event time
  "s": "BNBBTC",      // Symbol
  "U": 157,           // First update ID in event
  "u": 160,           // Final update ID in event
  "b": [              // Bids to be updated
    [
      "0.0024",       // Price level to be updated
      "10"            // Quantity
    ]
  ],
  "a": [              // Asks to be updated
    [
      "0.0026",       // Price level to be updated
      "100"           // Quantity
    ]
  ]
}
```

## How to manage a local order book correctly
1. Open a WebSocket connection to `wss://stream.binance.com:9443/ws/bnbbtc@depth`.
1. Buffer the events received from the stream. Note the `U` of the first event you received.
1. Get a depth snapshot from `https://api.binance.com/api/v3/depth?symbol=BNBBTC&limit=5000`.
1. If the `lastUpdateId` from the snapshot is strictly less than the `U` from step 2, go back to step 3.
1. In the buffered events, discard any event where `u` is <= `lastUpdateId` of the snapshot. The first buffered event should now have `lastUpdateId` within its `[U;u]` range.
1. Set your local order book to the snapshot. Its update ID is `lastUpdateId`.
1. Apply the update procedure below to all buffered events, and then to all subsequent events received.

To apply an event to your local order book, follow this update procedure:
1. Decide whether the update event can be applied:
    * If the event last update ID (`u`) is less than the update ID of your local order book,
      ignore the event.
    * If the event first update ID (`U`) is greater than the update ID of your local order book + 1,
      you have missed some events. <br> Discard your local order book and restart the process from the beginning.
    * Normally, `U` of the next event is equal to `u + 1` of the previous event.
1. For each price level in bids (`b`) and asks (`a`), set the new quantity in the order book:
    * If the price level does not exist in the order book, insert it with new quantity.
    * If the quantity is zero, remove the price level from the order book.
1. Set the order book update ID to the last update ID (`u`) in the processed event.

> [!NOTE]
> Since depth snapshots retrieved from the API have a limit on the number of price levels (5000 on each side maximum), you won't learn the quantities for the levels outside of the initial snapshot unless they change. <br>
> So be careful when using the information for those levels, since they might not reflect the full view of the order book. <br>
> However, for most use cases, seeing 5000 levels on each side is enough to understand the market and trade effectively.
<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->

- [Public WebSocket API for Binance](#public-websocket-api-for-binance)
  - [General API Information](#general-api-information)
  - [Request format](#request-format)
  - [Response format](#response-format)
    - [Status codes](#status-codes)
  - [Event format](#event-format)
  - [Rate limits](#rate-limits)
    - [Connection limits](#connection-limits)
    - [General information on rate limits](#general-information-on-rate-limits)
      - [How to interpret rate limits](#how-to-interpret-rate-limits)
      - [How to show/hide rate limit information](#how-to-showhide-rate-limit-information)
    - [IP limits](#ip-limits)
    - [Unfilled Order Count](#unfilled-order-count)
  - [Request security](#request-security)
    - [SIGNED request security](#signed-request-security)
      - [Signature Case Sensitivity](#signature-case-sensitivity)
    - [Timing security](#timing-security)
    - [SIGNED request example (HMAC)](#signed-request-example-hmac)
    - [SIGNED request example (RSA)](#signed-request-example-rsa)
    - [SIGNED Request Example (Ed25519)](#signed-request-example-ed25519)
  - [Session Authentication](#session-authentication)
    - [Authenticate after connection](#authenticate-after-connection)
    - [Authorize _ad hoc_ requests](#authorize-_ad-hoc_-requests)
  - [Data sources](#data-sources)
- [Public API requests](#public-api-requests)
  - [General requests](#general-requests)
    - [Test connectivity](#test-connectivity)
    - [Check server time](#check-server-time)
    - [Exchange information](#exchange-information)
  - [Market data requests](#market-data-requests)
    - [Order book](#order-book)
    - [Recent trades](#recent-trades)
    - [Historical trades](#historical-trades)
    - [Aggregate trades](#aggregate-trades)
    - [Klines](#klines)
    - [UI Klines](#ui-klines)
    - [Current average price](#current-average-price)
    - [24hr ticker price change statistics](#24hr-ticker-price-change-statistics)
    - [Trading Day Ticker](#trading-day-ticker)
    - [Rolling window price change statistics](#rolling-window-price-change-statistics)
    - [Symbol price ticker](#symbol-price-ticker)
    - [Symbol order book ticker](#symbol-order-book-ticker)
  - [Authentication requests](#authentication-requests)
    - [Log in with API key (SIGNED)](#log-in-with-api-key-signed)
    - [Query session status](#query-session-status)
    - [Log out of the session](#log-out-of-the-session)
  - [Trading requests](#trading-requests)
    - [Place new order (TRADE)](#place-new-order-trade)
    - [Test new order (TRADE)](#test-new-order-trade)
    - [Cancel order (TRADE)](#cancel-order-trade)
    - [Cancel and replace order (TRADE)](#cancel-and-replace-order-trade)
    - [Order Amend Keep Priority (TRADE)](#order-amend-keep-priority-trade)
    - [Cancel open orders (TRADE)](#cancel-open-orders-trade)
    - [Order lists](#order-lists)
      - [Place new OCO - Deprecated (TRADE)](#place-new-oco---deprecated-trade)
      - [Place new Order list - OCO (TRADE)](#place-new-order-list---oco-trade)
      - [Place new Order list - OTO (TRADE)](#place-new-order-list---oto-trade)
      - [Place new Order list - OTOCO (TRADE)](#place-new-order-list---otoco-trade)
      - [OPO (TRADE)](#opo-trade)
      - [OPOCO (TRADE)](#opoco-trade)
      - [Cancel Order list (TRADE)](#cancel-order-list-trade)
    - [SOR](#sor)
      - [Place new order using SOR (TRADE)](#place-new-order-using-sor-trade)
      - [Test new order using SOR (TRADE)](#test-new-order-using-sor-trade)
  - [Account requests](#account-requests)
    - [Account information (USER_DATA)](#account-information-user_data)
    - [Query order (USER_DATA)](#query-order-user_data)
    - [Current open orders (USER_DATA)](#current-open-orders-user_data)
    - [Account order history (USER_DATA)](#account-order-history-user_data)
    - [Query Order list (USER_DATA)](#query-order-list-user_data)
    - [Current open Order lists (USER_DATA)](#current-open-order-lists-user_data)
    - [Account order list history (USER_DATA)](#account-order-list-history-user_data)
    - [Account trade history (USER_DATA)](#account-trade-history-user_data)
    - [Unfilled Order Count (USER_DATA)](#unfilled-order-count-user_data)
    - [Account prevented matches (USER_DATA)](#account-prevented-matches-user_data)
    - [Account allocations (USER_DATA)](#account-allocations-user_data)
    - [Account Commission Rates (USER_DATA)](#account-commission-rates-user_data)
    - [Query Order Amendments (USER_DATA)](#query-order-amendments-user_data)
    - [Query Relevant Filters (USER_DATA)](#query-relevant-filters-user_data)
  - [User Data Stream requests](#user-data-stream-requests)
    - [User Data Stream subscription](#user-data-stream-subscription)
      - [Subscribe to User Data Stream (USER_STREAM)](#subscribe-to-user-data-stream-user_stream)
      - [Unsubscribe from User Data Stream](#unsubscribe-from-user-data-stream)
      - [Listing all subscriptions](#listing-all-subscriptions)
      - [Subscribe to User Data Stream through signature subscription (USER_STREAM)](#subscribe-to-user-data-stream-through-signature-subscription-user_stream)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Public WebSocket API for Binance

## General API Information

* The base endpoint is: **`wss://ws-api.binance.com:443/ws-api/v3`**.
  * If you experience issues with the standard 443 port, alternative port 9443 is also available.
  * The base endpoint for [testnet](https://testnet.binance.vision/) is: `wss://ws-api.testnet.binance.vision/ws-api/v3`
* A single connection to the API is only valid for 24 hours; expect to be disconnected after the 24-hour mark.
* We support HMAC, RSA, and Ed25519 keys. For more information, please see [API Key types](faqs/api_key_types.md).
* Responses are in JSON by default. To receive responses in SBE, refer to the [SBE FAQ](faqs/sbe_faq.md) page.
* If your request contains a symbol name containing non-ASCII characters, then the response may contain non-ASCII characters encoded in UTF-8.
* Some methods may return asset and/or symbol names containing non-ASCII characters encoded in UTF-8 even if the request did not contain non-ASCII characters.
* The WebSocket server will send a `ping frame` every 20 seconds.
  * If the WebSocket server does not receive a `pong frame` back from the connection within a minute the connection will be disconnected.
  * When you receive a ping, you must send a pong with a copy of ping's payload as soon as possible.
  * Unsolicited `pong frames` are allowed, but will not prevent disconnection. **It is recommended that the payload for these pong frames are empty.**
* Data is returned in **chronological order**, unless noted otherwise.
  * Without `startTime` or `endTime`, returns the most recent items up to the limit.
  * With `startTime`, returns oldest items from `startTime` up to the limit.
  * With `endTime`, returns most recent items up to `endTime` and the limit.
  * With both, behaves like `startTime` but does not exceed `endTime`.
* All timestamps in the JSON responses are in **milliseconds in UTC by default**. To receive the information in microseconds, please add the parameter `timeUnit=MICROSECOND` or `timeUnit=microsecond` in the URL.
* Timestamp parameters (e.g. `startTime`, `endTime`, `timestamp`) can be passed in milliseconds or microseconds.
* All field names and values are **case-sensitive**, unless noted otherwise.
* If there are enums or terms you want clarification on, please see [SPOT Glossary](faqs/spot_glossary.md) for more information.
* APIs have a timeout of 10 seconds when processing a request. If a response from the Matching Engine takes longer than this, the API responds with "Timeout waiting for response from backend server. Send status unknown; execution status unknown." [(-1007 TIMEOUT)](errors.md#-1007-timeout)
  * This does not always mean that the request failed in the Matching Engine.
  * If the status of the request has not appeared in [User Data Stream](user-data-stream.md), please perform an API query for its status.
* **Please avoid SQL keywords in requests** as they may trigger a security block by a WAF (Web Application Firewall) rule. See https://www.binance.com/en/support/faq/detail/360004492232 for more details.


## Request format

Requests must be sent as JSON in **text frames**, one request per frame.

Example of request:

```json
{
    "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",
    "method": "order.place",
    "params": {
        "symbol": "BTCUSDT",
        "side": "BUY",
        "type": "LIMIT",
        "price": "0.1",
        "quantity": "10",
        "timeInForce": "GTC",
        "timestamp": 1655716096498,
        "apiKey": "T59MTDLWlpRW16JVeZ2Nju5A5C98WkMm8CSzWC4oqynUlTm1zXOxyauT8LmwXEv9",
        "signature": "5942ad337e6779f2f4c62cd1c26dba71c91514400a24990a3e7f5edec9323f90"
    }
}
```

Request fields:

Name     | Type    | Mandatory | Description
--------- | ------- | --------- | -----------
`id`      | INT / STRING / `null` | YES | Arbitrary ID used to match responses to requests
`method`  | STRING  | YES       | Request method name
`params`  | OBJECT  | NO        | Request parameters. May be omitted if there are no parameters

* Request `id` is truly arbitrary. You can use UUIDs, sequential IDs, current timestamp, etc.
  The server does not interpret `id` in any way, simply echoing it back in the response.

  You can freely reuse IDs within a session.
  However, be careful to not send more than one request at a time with the same ID,
  since otherwise it might be impossible to tell the responses apart.

* Request method names may be prefixed with explicit version: e.g., `"v3/order.place"`.

* The order of `params` is not significant.

## Response format

Responses are returned as JSON in **text frames**, one response per frame.

Example of successful response:

```json
{
    "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",
    "status": 200,
    "result": {
        "symbol": "BTCUSDT",
        "orderId": 12510053279,
        "orderListId": -1,
        "clientOrderId": "a097fe6304b20a7e4fc436",
        "transactTime": 1655716096505,
        "price": "0.10000000",
        "origQty": "10.00000000",
        "executedQty": "0.00000000",
        "origQuoteOrderQty": "0.000000",
        "cummulativeQuoteQty": "0.00000000",
        "status": "NEW",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "workingTime": 1655716096505,
        "selfTradePreventionMode": "NONE"
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 12
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 4043
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 321
        }
    ]
}
```

Example of failed response:

```json
{
    "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",
    "status": 400,
    "error": {
        "code": -2010,
        "msg": "Account has insufficient balance for requested action."
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 13
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 4044
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 322
        }
    ]
}
```

Response fields:

<table>
<thead>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Mandatory</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><code>id</code></td>
    <td>INT / STRING / <code>null</code></td>
    <td>YES</td>
    <td>Same as in the original request</td>
  </tr>
  <tr>
    <td><code>status</code></td>
    <td>INT</td>
    <td>YES</td>
    <td>Response status. See <a href="#status-codes">Status codes</a></td>
  </tr>
  <tr>
    <td><code>result</code></td>
    <td>OBJECT / ARRAY</td>
    <td rowspan="2">YES</td>
    <td>Response content. Present if request succeeded</td>
  </tr>
  <tr>
    <td><code>error</code></td>
    <td>OBJECT</td>
    <td>Error description. Present if request failed</td>
  </tr>
  <tr>
    <td><code>rateLimits</code></td>
    <td>ARRAY</td>
    <td>NO</td>
    <td>Rate limiting status. See <a href="#rate-limits">Rate limits</a></td>
  </tr>
</tbody>
</table>

### Status codes

Status codes in the `status` field are the same as in HTTP.

Here are some common status codes that you might encounter:

* `200` indicates a successful response.
* `4XX` status codes indicate invalid requests; the issue is on your side.
  * `400` – your request failed, see `error` for the reason.
  * `403` – you have been blocked by the Web Application Firewall. This can indicate a rate limit violation or a security block. See https://www.binance.com/en/support/faq/detail/360004492232 for more details.
  * `409` – your request partially failed but also partially succeeded, see `error` for details.
  * `418` – you have been auto-banned for repeated violation of rate limits.
  * `429` – you have exceeded API request rate limit, please slow down.
* `5XX` status codes indicate internal errors; the issue is on Binance's side.
  * **Important:** If a response contains 5xx status code, it **does not** necessarily mean that your request has failed.
    Execution status is _unknown_ and the request might have actually succeeded.
    Please use query methods to confirm the status.
    You might also want to establish a new WebSocket connection for that.

See [Error codes for Binance](errors.md) for a list of error codes and messages.

## Event format

[User Data Stream](user-data-stream.md) events for non-SBE sessions are sent as JSON in **text frames**, one event per frame.

Events in [SBE sessions](faqs/sbe_faq.md) will be sent as **binary frames**.

Please refer to [`userDataStream.subscribe`](#user-data-stream-subscribe) for details on how to subscribe to User Data Stream in WebSocket API.

Example of an event:

```javascript
{
    "subscriptionId": 0,
    "event": {
        "e": "outboundAccountPosition",
        "E": 1728972148778,
        "u": 1728972148778,
        "B": [
            {
                "a": "BTC",
                "f": "11818.00000000",
                "l": "182.00000000"
            },
            {
                "a": "USDT",
                "f": "10580.00000000",
                "l": "70.00000000"
            }
        ]
    }
}
```

Event fields:

| Name | Type | Mandatory | Description |
| :---- | :---- | :---- | :---- |
| `event` | OBJECT | YES | Event payload. See [User Data Streams](user-data-stream.md) |
| `subscriptionId`|INT| NO| Identifies which subscription the event is coming from. See [User Data Stream subscriptions](#general_info_user_data_stream_subscriptions) |

## Rate limits

### Connection limits

There is a limit of **300 connections per attempt every 5 minutes**.

The connection is per **IP address**.

### General information on rate limits

* Current API rate limits can be queried using the [`exchangeInfo`](#exchange-information) request.
* There are multiple rate limit types across multiple intervals.
* Responses can indicate current rate limit status in the optional `rateLimits` field.
* Requests fail with status `429` when unfilled order count or request rate limits are violated.

#### How to interpret rate limits

A response with rate limit status may look like this:

```json
{
    "id": "7069b743-f477-4ae3-81db-db9b8df085d2",
    "status": 200,
    "result": {
        "serverTime": 1656400526260
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 70
        }
    ]
}
```

The `rateLimits` array describes all currently active rate limits affected by the request.

| Name            | Type    | Mandatory | Description
| --------------- | ------- | --------- | -----------
| `rateLimitType` | ENUM    | YES       | Rate limit type: `REQUEST_WEIGHT`, `ORDERS`
| `interval`      | ENUM    | YES       | Rate limit interval: `SECOND`, `MINUTE`, `HOUR`, `DAY`
| `intervalNum`   | INT     | YES       | Rate limit interval multiplier
| `limit`         | INT     | YES       | Request limit per interval
| `count`         | INT     | YES       | Current usage per interval

Rate limits are accounted by intervals.

For example, a `1 MINUTE` interval starts every minute.
Request submitted at 00:01:23.456 counts towards the 00:01:00 minute's limit.
Once the 00:02:00 minute starts, the count will reset to zero again.

Other intervals behave in a similar manner.
For example, `1 DAY` rate limit resets at 00:00 UTC every day,
and `10 SECOND` interval resets at 00, 10, 20... seconds of each minute.

APIs have multiple rate-limiting intervals.
If you exhaust a shorter interval but the longer interval still allows requests,
you will have to wait for the shorter interval to expire and reset.
If you exhaust a longer interval, you will have to wait for that interval to reset,
even if shorter rate limit count is zero.

#### How to show/hide rate limit information

`rateLimits` field is included with every response by default.

However, rate limit information can be quite bulky.
If you are not interested in detailed rate limit status of every request,
the `rateLimits` field can be omitted from responses to reduce their size.

* Optional `returnRateLimits` boolean parameter in request.

  Use `returnRateLimits` parameter to control whether to include `rateLimits` fields in response to individual requests.

  Default request and response:

  ```json
  { "id": 1, "method": "time" }
  ```

  ```json
  {
      "id": 1,
      "status": 200,
      "result": { "serverTime": 1656400526260 },
      "rateLimits": [
          {
              "rateLimitType": "REQUEST_WEIGHT",
              "interval": "MINUTE",
              "intervalNum": 1,
              "limit": 6000,
              "count": 70
          }
      ]
  }
  ```

  Request and response without rate limit status:

  ```json
  { "id": 2, "method": "time", "params": { "returnRateLimits": false } }
  ```

  ```json
  { "id": 2, "status": 200, "result": { "serverTime": 1656400527891 } }
  ```

* Optional `returnRateLimits` boolean parameter in connection URL.

  If you wish to omit `rateLimits` from all responses by default,
  use `returnRateLimits` parameter in the query string instead:

  ```
  wss://ws-api.binance.com:443/ws-api/v3?returnRateLimits=false
  ```

  This will make all requests made through this connection behave as if you have passed `"returnRateLimits": false`.

  If you _want_ to see rate limits for a particular request,
  you need to explicitly pass the `"returnRateLimits": true` parameter.

**Note:** Your requests are still rate limited if you hide the `rateLimits` field in responses.

### IP limits

* Every request has a certain **weight**, added to your limit as you perform requests.
  * The heavier the request (e.g. querying data from multiple symbols), the more weight the request will cost.
  * Connecting to WebSocket API costs 2 weight.
* Current weight usage is indicated by the `REQUEST_WEIGHT` rate limit type.
* Use the [`exchangeInfo`](#exchange-information) request
  to keep track of the current weight limits.
* Weight is accumulated **per IP address** and is shared by all connections from that address.
* If you go over the weight limit, requests fail with status `429`.
  * This status code indicates you should back off and stop spamming the API.
  * Rate-limited responses include a `retryAfter` field, indicating when you can retry the request.
* **Repeatedly violating rate limits and/or failing to back off after receiving 429s will result in an automated IP ban and you will be disconnected.**
  * Requests from a banned IP address fail with status `418`.
  * `retryAfter` field indicates the timestamp when the ban will be lifted.
* IP bans are tracked and **scale in duration** for repeat offenders, **from 2 minutes to 3 days**.

Successful response indicating that in 1 minute you have used 70 weight out of your 6000 limit:

```json
{
    "id": "7069b743-f477-4ae3-81db-db9b8df085d2",
    "status": 200,
    "result": [],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 70
        }
    ]
}
```

Failed response indicating that you are banned and the ban will last until epoch `1659146400000`:

```json
{
    "id": "fc93a61a-a192-4cf4-bb2a-a8f0f0c51e06",
    "status": 418,
    "error": {
        "code": -1003,
        "msg": "Way too much request weight used; IP banned until 1659146400000. Please use WebSocket Streams for live updates to avoid bans.",
        "data": {
            "serverTime": 1659142907531,
            "retryAfter": 1659146400000
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2411
        }
    ]
}
```

### Unfilled Order Count

* Successfully placed orders update the `ORDERS` rate limit type.
* Rejected or unsuccessful orders might or might not update the `ORDERS` rate limit type.
* **Please note that if your orders are consistently filled by trades, you can continuously place orders on the API**. For more information, please see [Spot Unfilled Order Count Rules](./faqs/order_count_decrement.md).
* Use the [`account.rateLimits.orders`](#query-unfilled-order-count) request to keep track of how many orders you have placed within this interval.
* If you exceed this, requests fail with status `429`.
  * This status code indicates you should back off and stop spamming the API.
  * Responses that have a status `429` include a `retryAfter` field, indicating when you can retry the request.
* This is maintained **per account** and is shared by all API keys of the account.

Successful response indicating that you have placed 12 orders in 10 seconds, and 4043 orders in the past 24 hours:
```json
{
    "id": "e2a85d9f-07a5-4f94-8d5f-789dc3deb097",
    "status": 200,
    "result": {
        "symbol": "BTCUSDT",
        "orderId": 12510053279,
        "orderListId": -1,
        "clientOrderId": "a097fe6304b20a7e4fc436",
        "transactTime": 1655716096505,
        "price": "0.10000000",
        "origQty": "10.00000000",
        "executedQty": "0.00000000",
        "origQuoteOrderQty": "0.000000",
        "cummulativeQuoteQty": "0.00000000",
        "status": "NEW",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "BUY",
        "workingTime": 1655716096505,
        "selfTradePreventionMode": "NONE"
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 12
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 4043
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 321
        }
    ]
}
```

## Request security

* Each method has a security type indicating required API key permissions, shown next to the method name (e.g., [Place new order (TRADE)](#place-new-order-trade)).
* If unspecified, the security type is `NONE`.
* Except for `NONE`, all methods with a security type are considered `SIGNED` requests (i.e. including a `signature`), except for [listenKey management](#user-data-stream-requests).
* Secure methods require a valid API key to be specified and authenticated.
  * API keys can be created on the [API Management](https://www.binance.com/en/support/faq/360002502072) page of your Binance account.
  * **Both API key and secret key are sensitive.** Never share them with anyone.
    If you notice unusual activity in your account, immediately revoke all the keys and contact Binance support.
* API keys can be configured to allow access only to certain types of secure methods.
  * For example, you can have an API key with `TRADE` permission for trading,
    while using a separate API key with `USER_DATA` permission to monitor your order status.
  * By default, an API key cannot `TRADE`. You need to enable trading in API Management first.

Security type |  Description
------------- | ------------
`NONE`        | Public market data
`TRADE`       | Trading on the exchange, placing and canceling orders
`USER_DATA`   | Private account information, such as order status and your trading history
`USER_STREAM` | Managing User Data Stream subscriptions

### SIGNED request security

* `SIGNED` requests require an additional parameter: `signature`, authorizing the request.

#### Signature Case Sensitivity

* **HMAC:** Signatures generated using HMAC are **not case-sensitive**. This means the signature string can be verified regardless of letter casing.
* **RSA:** Signatures generated using RSA are **case-sensitive**.
* **Ed25519:** Signatures generated using ED25519 are also **case-sensitive**

Please consult [SIGNED request example (HMAC)](#signed-request-example-hmac), [SIGNED request example (RSA)](#signed-request-example-rsa), and [SIGNED request example (Ed25519)](#signed-request-example-ed25519) on how to compute signature, depending on which API key type you are using.

<a id="timingsecurity"></a>

### Timing security

* `SIGNED` requests also require a `timestamp` parameter which should be the current timestamp either in milliseconds or microseconds. (See [General API Information](#general-api-information))
* An additional optional parameter, `recvWindow`, specifies for how long the request stays valid and may only be specified in milliseconds.
  * `recvWindow` supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
  * If `recvWindow` is not sent, **it defaults to 5000 milliseconds**.
  * Maximum `recvWindow` is 60000 milliseconds.
* Request processing logic is as follows:

```javascript
serverTime = getCurrentTime()
if (timestamp < (serverTime + 1 second) && (serverTime - timestamp) <= recvWindow) {
  // begin processing request
  serverTime = getCurrentTime()
  if (serverTime - timestamp) <= recvWindow {
    // forward request to Matching Engine
  } else {
    // reject request
  }
  // finish processing request
} else {
  // reject request
}
  ```

**Serious trading is about timing.** Networks can be unstable and unreliable,
which can lead to requests taking varying amounts of time to reach the
servers. With `recvWindow`, you can specify that the request must be
processed within a certain number of milliseconds or be rejected by the
server.

**It is recommended to use a small `recvWindow` of 5000 or less!**

### SIGNED request example (HMAC)

Here is a step-by-step guide on how to sign requests using an HMAC secret key.

Example API key and secret key:

Key          | Value
------------ | ------------
`apiKey`       | `vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A`
`secretKey`    | `NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j`

**WARNING: DO NOT SHARE YOUR API KEY AND SECRET KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "------ FILL ME ------"
    }
}
```

Example of a request with a symbol name containing non-ASCII characters:

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "------ FILL ME ------"
    }
}
```

As you can see, the `signature` parameter is currently missing.

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name**:

For the first set of example parameters (ASCII only):

Parameter        | Value
---------------- | ------------
`apiKey`           | vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A
`price`            | 52000.00
`quantity`         | 0.01000000
`recvWindow`       | 100
`side`             | SELL
`symbol`           | BTCUSDT
`timeInForce`      | GTC
`timestamp`        | 1645423376532
`type`             | LIMIT

For the second set of example parameters (some non-ASCII characters):

Parameter | Value
------------ | ------------
`apiKey` | vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A
`price` | 0.10000000
`quantity` | 1.00000000
`recvWindow` | 5000
`side` | BUY
`symbol` | １２３４５６
`timeInForce` | GTC
`timestamp` | 1645423376532
`type` | LIMIT

Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:

```console
apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:

```console
apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

**Step 2: Compute the signature**

1. Use the `secretKey` of your API key as the signing key for the HMAC-SHA-256 algorithm.
2. Sign the UTF-8 bytes of the signature payload constructed in Step 1.
3. Encode the HMAC-SHA-256 output as a hex string.

Note that `apiKey`, `secretKey`, and the payload are **case-sensitive**, while the resulting signature value is case-insensitive.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):

```console
$ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
  | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'

aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24
```

For the second set of example parameters (some non-ASCII characters):

```console
$ echo -n 'apiKey=vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
  | openssl dgst -hex -sha256 -hmac 'NhqPtmdSJYdKjVHjA7PZj4Mge3R5YNiP1e3UZjInClVN65XAbvqqM6A7H5fATj0j'

b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd
```

**Step 3: Add `signature` to request `params`**

Complete the request by adding the `signature` parameter with the signature string.

For the first set of example parameters (ASCII only):

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "aa1b5712c094bc4e57c05a1a5c1fd8d88dcd628338ea863fec7b88e59fe2db24"
    }
}
```

For the second set of example parameters (some non-ASCII characters):

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "1.00000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "b33892ae8e687c939f4468c6268ddd4c40ac1af18ad19a064864c47bae0752cd"
    }
}
```

### SIGNED request example (RSA)

Here is a step-by-step guide on how to sign requests using an RSA private key.

Key          | Value
------------ | ------------
`apiKey`       | `CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ`

These examples assume the private key is stored in the file `test-rsa-prv.pem`.

**WARNING: DO NOT SHARE YOUR API KEY AND PRIVATE KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "------ FILL ME ------"
    }
}
```

Example of a request with a symbol name containing non-ASCII characters:

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "------ FILL ME ------"
    }
}
```

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name**:

For the first set of example parameters (ASCII only):

Parameter        | Value
---------------- | ------------
`apiKey`           | CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ
`price`            | 52000.00
`quantity`         | 0.01000000
`recvWindow`       | 100
`side`             | SELL
`symbol`           | BTCUSDT
`timeInForce`      | GTC
`timestamp`        | 1645423376532
`type`             | LIMIT

For the second set of example parameters (some non-ASCII characters):

Parameter | Value
------------ | ------------
`apiKey` | CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ
`price` | 0.10000000
`quantity` | 1.00000000
`recvWindow` | 5000
`side` | BUY
`symbol` | １２３４５６
`timeInForce` | GTC
`timestamp` | 1645423376532
`type` | LIMIT

Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:

```console
apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:

```console
apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

**Step 2: Compute the signature**

1. Sign the UTF-8 bytes of the signature payload constructed in Step 1 using the RSASSA-PKCS1-v1_5 algorithm with SHA-256 hash function.
2. Encode the output in base64.

Note that `apiKey`, the payload, and the resulting `signature` are **case-sensitive**.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):

```console
$ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
  | openssl dgst -sha256 -sign test-rsa-prv.pem \
  | openssl enc -base64 -A

OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA==
```

For the second set of example parameters (some non-ASCII characters):

```console
$ echo -n 'apiKey=CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT' \
  | openssl dgst -sha256 -sign test-rsa-prv.pem \
  | openssl enc -base64 -A

F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw==
```

**Step 3: Add `signature` to request `params`**

Complete the request by adding the `signature` parameter with the signature string.

For the first set of example parameters (ASCII only):

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "newOrderRespType": "ACK",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "OJJaf8C/3VGrU4ATTR4GiUDqL2FboSE1Qw7UnnoYNfXTXHubIl1iaePGuGyfct4NPu5oVEZCH4Q6ZStfB1w4ssgu0uiB/Bg+fBrRFfVgVaLKBdYHMvT+ljUJzqVaeoThG9oXlduiw8PbS9U8DYAbDvWN3jqZLo4Z2YJbyovyDAvDTr/oC0+vssLqP7NmlNb3fF3Bj7StmOwJvQJTbRAtzxK5PP7OQe+0mbW+D7RqVkUiSswR8qJFWTeSe4nXXNIdZdueYhF/Xf25L+KitJS5IHdIHcKfEw3MQzHFb2ZsGWkjDQwxkwr7Noi0Zaa+gFtxCuatGFm9dFIyx217pmSHtA=="
    }
}
```

For the second set of example parameters (some non-ASCII characters):

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "１２３４５６",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "1.00000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "CAvIjXy3F44yW6Pou5k8Dy1swsYDWJZLeoK2r8G4cFDnE9nosRppc2eKc1T8TRTQ",
        "signature": "F3o/79Ttvl2cVYGPfBOF3oEOcm5QcYmTYWpdVIrKve5u+8paMNDAdUE+teqMxFM9HcquetGcfuFpLYtsQames5bDx/tskGM76TWW8HaM+6tuSYBSFLrKqChfA9hQGLYGjAiflf1YBnDhY+7vNbJFusUborNOloOj+ufzP5q42PvI3H0uNy3W5V3pyfXpDGCBtfCYYr9NAqA4d+AQfyllL/zkO9h9JSdozN49t0/hWGoD2dWgSO0Je6MytKEvD4DQXGeqNlBTB6tUXcWnRW+FcaKZ4KYqnxCtb1u8rFXUYgFykr2CbcJLSmw6ydEJ3EZ/NaZopRr+cU0W2m0HZ3qucw=="
    }
}
```

### SIGNED Request Example (Ed25519)

**Note: It is highly recommended to use Ed25519 API keys as they will provide the best performance and security out of all supported key types.**

Here is a step-by-step guide on how to sign requests using an Ed25519 private key.

Key          | Value
------------ | ------------
`apiKey`       | `4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO`

These examples assume the private key is stored in the file `test-ed25519-prv.pem`.

**WARNING: DO NOT SHARE YOUR API KEY AND PRIVATE KEY WITH ANYONE.**

The example keys are provided here only for illustrative purposes.

Example of request with a symbol name comprised entirely of ASCII characters:

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "------ FILL ME ------"
    }
}
```

Example of a request with a symbol name containing non-ASCII characters:

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "１２３４５６",
        "side": "BUY",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "------ FILL ME ------"
    }
}
```

**Step 1: Construct the signature payload**

Take all request `params` except `signature` and **sort them in alphabetical order by parameter name**:

For the first set of example parameters (ASCII only):

Parameter        | Value
---------------- | ------------
`apiKey`           | 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO
`price`            | 52000.00
`quantity`         | 0.01000000
`recvWindow`       | 100
`side`             | SELL
`symbol`           | BTCUSDT
`timeInForce`      | GTC
`timestamp`        | 1645423376532
`type`             | LIMIT

For the second set of example parameters (some non-ASCII characters):

Parameter     | Value
------------  | ------------
`apiKey`      | 4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO
`price`       | 0.20000000
`quantity`    | 1.00000000
`recvWindow`  | 5000
`side`        | SELL
`symbol`      | １２３４５６
`timeInForce` | GTC
`timestamp`   | 1668481559918
`type`        | LIMIT

Format parameters as `parameter=value` pairs separated by `&`. Values need to be encoded in UTF-8.

For the first set of example parameters (ASCII only), the signature payload should look like this:

```console
apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

For the second set of example parameters (some non-ASCII characters), the signature payload should look like this:

```console
apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT
```

**Step 2: Compute the signature**

1. Sign the UTF-8 bytes of your signature payload constructed in Step 1 using the Ed25519 private key.
2. Encode the output in base64.

Note that `apiKey`, the payload, and the resulting `signature` are **case-sensitive**.

You can cross-check your signature algorithm implementation with OpenSSL:

For the first set of example parameters (ASCII only):

```console
echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=52000.00&quantity=0.01000000&recvWindow=100&side=SELL&symbol=BTCUSDT&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \
  | openssl dgst -sign ./test-ed25519-prv.pem \
  | openssl enc -base64 -A

EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg==
```

For the second set of example parameters (some non-ASCII characters):

```console
echo -n "apiKey=4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO&price=0.10000000&quantity=1.00000000&recvWindow=5000&side=BUY&symbol=１２３４５６&timeInForce=GTC&timestamp=1645423376532&type=LIMIT" \
  | openssl dgst -sign ./test-ed25519-prv.pem \
  | openssl enc -base64 -A

dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA==
```

**Step 3: Add the signature to request `params`**

For the first set of example parameters (ASCII only):

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "0.01000000",
        "price": "52000.00",
        "newOrderRespType": "ACK",
        "recvWindow": 100,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "EocljwPl29jDxWYaaRaOo4pJ9wEblFbklJvPugNscLLuKd5vHM2grWjn1z+rY0aJ7r/44enxHL6mOAJuJ1kqCg=="
    }
}
```

For the second set of example parameters (some non-ASCII characters):

```json
{
    "id": "4885f793-e5ad-4c3b-8f6c-55d891472b71",
    "method": "order.place",
    "params": {
        "symbol": "１２３４５６",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "quantity": "1.00000000",
        "price": "0.10000000",
        "recvWindow": 5000,
        "timestamp": 1645423376532,
        "apiKey": "4yNzx3yWC5bS6YTwEkSRaC0nRmSQIIStAUOh1b6kqaBrTLIhjCpI5lJH8q8R8WNO",
        "signature": "dtNHJeyKry+cNjiGv+sv5kynO9S40tf8k7D5CfAEQAp0s2scunZj+ovJdz2OgW8XhkB9G3/HmASkA9uY9eyFCA=="
    }
}
```

Here is a sample Python script performing all the steps above:

```python
#!/usr/bin/env python3

import base64
import time
import json
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from websocket import create_connection

# Set up authentication
API_KEY='put your own API Key here'
PRIVATE_KEY_PATH='test-prv-key.pem'

# Load the private key.
# In this example the key is expected to be stored without encryption,
# but we recommend using a strong password for improved security.
with open(PRIVATE_KEY_PATH, 'rb') as f:
  private_key = load_pem_private_key(data=f.read(), password=None)

# Set up the request parameters
params = {
    'apiKey':       API_KEY,
    'symbol':       '１２３４５６',
    'side':         'SELL',
    'type':         'LIMIT',
    'timeInForce':  'GTC',
    'quantity':     '1.0000000',
    'price':        '0.10000000',
    'recvWindow':   5000
}

# Timestamp the request
timestamp = int(time.time() * 1000) # UNIX timestamp in milliseconds
params['timestamp'] = timestamp

# Sort parameters alphabetically by name
params = dict(sorted(params.items()))

# Compute the signature payload
payload = '&'.join([f"{k}={v}" for k,v in params.items()]) # no percent encoding here!

# Sign the request
signature = base64.b64encode(private_key.sign(payload.encode('UTF-8')))
params['signature'] = signature.decode('ASCII')

# Send the request
request = {
    'id': 'my_new_order',
    'method': 'order.place',
    'params': params
}

ws = create_connection("wss://ws-api.binance.com:443/ws-api/v3")
ws.send(json.dumps(request))
result =  ws.recv()
ws.close()

print(result)
```

## Session Authentication

**Note:** Only _Ed25519_ keys are supported for this feature.

If you do not want to specify `apiKey` and `signature` in each individual request,
you can authenticate your API key for the active WebSocket session.

Once authenticated, you no longer have to specify `apiKey` and `signature` for those requests that need them.
Requests will be performed on behalf of the account owning the authenticated API key.

**Note:** You still have to specify the `timestamp` parameter for `SIGNED` requests.

### Authenticate after connection

You can authenticate an already established connection using session authentication requests:

* [`session.logon`](#log-in-with-api-key-signed) – authenticate, or change the API key associated with the connection
* [`session.status`](#query-session-status) – check connection status and the current API key
* [`session.logout`](#log-out-of-the-session) – forget the API key associated with the connection

**Regarding API key revocation:**

If during an active session the API key becomes invalid for _any reason_ (e.g. IP address is not whitelisted, API key was deleted, API key doesn't have correct permissions, etc), after the next request the session will be revoked with the following error message:

```javascript
{
    "id": null,
    "status": 401,
    "error": {
        "code": -2015,
        "msg": "Invalid API-key, IP, or permissions for action."
    }
}
```

### Authorize _ad hoc_ requests

Only one API key can be authenticated with the WebSocket connection.
The authenticated API key is used by default for requests that require an `apiKey` parameter.
However, you can always specify the `apiKey` and `signature` explicitly for individual requests,
overriding the authenticated API key and using a different one to authorize a specific request.

For example, you might want to authenticate your `USER_DATA` key to be used by default,
but specify the `TRADE` key with an explicit signature when placing orders.

## Data sources

* The API system is asynchronous. Some delay in the response is normal and expected.

* Each method has a data source indicating where the data is coming from, and thus how up-to-date it is.

Data Source     | Latency  | Description
--------------- | -------- | -----------
Matching Engine | lowest   | The Matching Engine produces the response directly
Memory          | low      | Data is fetched from API server's local or external memory cache
Database        | moderate | Data is retrieved from the database

* Some methods have more than one data source (e.g., Memory => Database).

  This means that the API will look for the latest data in that order:
  first in the cache, then in the database.

# Public API requests

## General requests

### Test connectivity

```javascript
{
    "id": "922bcc6e-9de8-440d-9e84-7c80933a8d0d",
    "method": "ping"
}
```

Test connectivity to the WebSocket API.

**Note:**
You can use regular WebSocket ping frames to test connectivity as well,
WebSocket API will respond with pong frames as soon as possible.
`ping` request along with `time` is a safe way to test request-response handling in your application.

**Weight:**
1

**Parameters:**
NONE

**Data Source:**
Memory

**Response:**
```javascript
{
    "id": "922bcc6e-9de8-440d-9e84-7c80933a8d0d",
    "status": 200,
    "result": {},
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

### Check server time

```javascript
{
    "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",
    "method": "time"
}
```

Test connectivity to the WebSocket API and get the current server time.

**Weight:**
1

**Parameters:**
NONE

**Data Source:**
Memory

**Response:**
```javascript
{
    "id": "187d3cb2-942d-484c-8271-4e2141bbadb1",
    "status": 200,
    "result": {
        "serverTime": 1656400526260
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

<a id="exchangeInfo"></a>

### Exchange information

```javascript
{
    "id": "5494febb-d167-46a2-996d-70533eb4d976",
    "method": "exchangeInfo",
    "params": {
        "symbols": ["BNBBTC"]
    }
}
```

Query current exchange trading rules, rate limits, and symbol information.

**Weight:**
20

**Parameters:**

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>symbol</code></td>
        <td>STRING</td>
        <td rowspan="5" align="center">NO</td>
        <td>Describe a single symbol</td>
    </tr>
    <tr>
        <td><code>symbols</code></td>
        <td>ARRAY of STRING</td>
        <td>Describe multiple symbols</td>
    </tr>
    <tr>
        <td><code>permissions</code></td>
        <td>ARRAY of STRING</td>
        <td>Filter symbols by permissions</td>
    </tr>
    <tr>
        <td><code>showPermissionSets</code></td>
        <td>BOOLEAN</td>
        <td>Controls whether the content of the <code>permissionSets</code> field is populated or not. Defaults to <code>true</code>.</td>
    </tr>
    <tr>
        <td><code>symbolStatus</code></td>
        <td>ENUM</td>
        <td>Filters for symbols that have this <code>tradingStatus</code>.<br></br> Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code> <br> Cannot be used in combination with <code>symbol</code> or <code>symbols</code></td>
    </tr>
</tbody>
</table>

Notes:

* Only one of `symbol`, `symbols`, `permissions` parameters can be specified.

* Without parameters, `exchangeInfo` displays all symbols with `["SPOT, "MARGIN", "LEVERAGED"]` permissions.

  * In order to list *all* active symbols on the exchange, you need to explicitly request all permissions.

* `permissions` accepts either a list of permissions, or a single permission name. E.g. `"SPOT"`.

* [Available Permissions](./enums.md#account-and-symbol-permissions)

<a id="examples-of-symbol-permissions-interpretation-from-the-response"></a>

**Examples of Symbol Permissions Interpretation from the Response:**

* `[["A","B"]]` means you may place an order if your account has either permission "A" **or** permission "B".
* `[["A"],["B"]]` means you can place an order if your account has permission "A" **and** permission "B".
* `[["A"],["B","C"]]` means you can place an order if your account has permission "A" **and** permission "B" or permission "C". (Inclusive or is applied here, not exclusive or, so your account may have both permission "B" and permission "C".)

**Data Source:**
Memory

**Response:**
```javascript
{
    "id": "5494febb-d167-46a2-996d-70533eb4d976",
    "status": 200,
    "result": {
        "timezone": "UTC",
        "serverTime": 1655969291181,
        // Global rate limits. See "Rate limits" section.
        "rateLimits": [
            {
                "rateLimitType": "REQUEST_WEIGHT",     // Rate limit type: REQUEST_WEIGHT, ORDERS, CONNECTIONS
                "interval": "MINUTE",                  // Rate limit interval: SECOND, MINUTE, DAY
                "intervalNum": 1,                      // Rate limit interval multiplier (i.e., "1 minute")
                "limit": 6000                          // Rate limit per interval
            },
            {
                "rateLimitType": "ORDERS",
                "interval": "SECOND",
                "intervalNum": 10,
                "limit": 50
            },
            {
                "rateLimitType": "ORDERS",
                "interval": "DAY",
                "intervalNum": 1,
                "limit": 160000
            },
            {
                "rateLimitType": "CONNECTIONS",
                "interval": "MINUTE",
                "intervalNum": 5,
                "limit": 300
            }
        ],
        // Exchange filters are explained on the "Filters" page:
        // https://github.com/binance/binance-spot-api-docs/blob/master/filters.md
        // All exchange filters are optional.
        "exchangeFilters": [],
        "symbols": [
            {
                "symbol": "BNBBTC",
                "status": "TRADING",
                "baseAsset": "BNB",
                "baseAssetPrecision": 8,
                "quoteAsset": "BTC",
                "quotePrecision": 8,
                "quoteAssetPrecision": 8,
                "baseCommissionPrecision": 8,
                "quoteCommissionPrecision": 8,
                "orderTypes": [
                    "LIMIT",
                    "LIMIT_MAKER",
                    "MARKET",
                    "STOP_LOSS_LIMIT",
                    "TAKE_PROFIT_LIMIT"
                ],
                "icebergAllowed": true,
                "ocoAllowed": true,
                "otoAllowed": true,
                "opoAllowed": true,
                "quoteOrderQtyMarketAllowed": true,
                "allowTrailingStop": true,
                "cancelReplaceAllowed": true,
                "amendAllowed": false,
                "pegInstructionsAllowed": true,
                "isSpotTradingAllowed": true,
                "isMarginTradingAllowed": true,
                // Symbol filters are explained on the "Filters" page:
                // https://github.com/binance/binance-spot-api-docs/blob/master/filters.md
                // All symbol filters are optional.
                "filters": [
                    {
                        "filterType": "PRICE_FILTER",
                        "minPrice": "0.00000100",
                        "maxPrice": "100000.00000000",
                        "tickSize": "0.00000100"
                    },
                    {
                        "filterType": "LOT_SIZE",
                        "minQty": "0.00100000",
                        "maxQty": "100000.00000000",
                        "stepSize": "0.00100000"
                    }
                ],
                "permissions": [],
                "permissionSets": [["SPOT", "MARGIN", "TRD_GRP_004"]],
                "defaultSelfTradePreventionMode": "NONE",
                "allowedSelfTradePreventionModes": ["NONE"]
            }
        ],
        // Optional field. Present only when SOR is available.
        // https://github.com/binance/binance-spot-api-docs/blob/master/faqs/sor_faq.md
        "sors": [
            {
                "baseAsset": "BTC",
                "symbols": ["BTCUSDT", "BTCUSDC"]
            }
        ]
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 20
        }
    ]
}
```

## Market data requests

### Order book

```javascript
{
    "id": "51e2affb-0aba-4821-ba75-f2625006eb43",
    "method": "depth",
    "params": {
        "symbol": "BNBBTC",
        "limit": 5
    }
}
```

Get current order book.

Note that this request returns limited market depth.

If you need to continuously monitor order book updates, please consider using WebSocket Streams:

* [`<symbol>@depth<levels>`](web-socket-streams.md#partial-book-depth-streams)
* [`<symbol>@depth`](web-socket-streams.md#diff-depth-stream)

You can use `depth` request together with `<symbol>@depth` streams to [maintain a local order book](web-socket-streams.md#how-to-manage-a-local-order-book-correctly).

**Weight:**
Adjusted based on the limit:

|  Limit    | Weight |
|:---------:|:------:|
|     1–100 |      5 |
|   101–500 |      25|
|  501–1000 |     50 |
| 1001–5000 |     250 |

**Parameters:**

Name      | Type    | Mandatory | Description
--------- | ------- | --------- | -----------
`symbol`  | STRING  | YES       |
`limit`   | INT     | NO        | Default: 100; Maximum: 5000
`symbolStatus`|ENUM | NO        | Filters for symbols that have this `tradingStatus`.<br/>A status mismatch returns error `-1220 SYMBOL_DOES_NOT_MATCH_STATUS`<br/>Valid values: `TRADING`, `HALT`, `BREAK`

**Data Source:**
Memory

**Response:**
```javascript
{
    "id": "51e2affb-0aba-4821-ba75-f2625006eb43",
    "status": 200,
    "result": {
        "lastUpdateId": 2731179239,
        // Bid levels are sorted from highest to lowest price.
        "bids": [
            [
                "0.01379900",     // Price
                "3.43200000"      // Quantity
            ],
            ["0.01379800", "3.24300000"],
            ["0.01379700", "10.45500000"],
            ["0.01379600", "3.82100000"],
            ["0.01379500", "10.26200000"]
        ],
        // Ask levels are sorted from lowest to highest price.
        "asks": [
            ["0.01380000", "5.91700000"],
            ["0.01380100", "6.01400000"],
            ["0.01380200", "0.26800000"],
            ["0.01380300", "0.33800000"],
            ["0.01380400", "0.26800000"]
        ]
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```


### Recent trades

```javascript
{
    "id": "409a20bd-253d-41db-a6dd-687862a5882f",
    "method": "trades.recent",
    "params": {
        "symbol": "BNBBTC",
        "limit": 1
    }
}
```

Get recent trades.

If you need access to real-time trading activity, please consider using WebSocket Streams:

* [`<symbol>@trade`](web-socket-streams.md#trade-streams)

**Weight:**
25

**Parameters:**

Name      | Type    | Mandatory | Description
--------- | ------- | --------- | -----------
`symbol`  | STRING  | YES       |
`limit`   | INT     | NO        | Default: 500; Maximum: 1000

**Data Source:**
Memory

**Response:**
```javascript
{
    "id": "409a20bd-253d-41db-a6dd-687862a5882f",
    "status": 200,
    "result": [
        {
            "id": 194686783,
            "price": "0.01361000",
            "qty": "0.01400000",
            "quoteQty": "0.00019054",
            "time": 1660009530807,
            "isBuyerMaker": true,
            "isBestMatch": true
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```

### Historical trades

```javascript
{
    "id": "cffc9c7d-4efc-4ce0-b587-6b87448f052a",
    "method": "trades.historical",
    "params": {
        "symbol": "BNBBTC",
        "fromId": 0,
        "limit": 1
    }
}
```

Get historical trades.

**Weight:**
25

**Parameters:**

Name      | Type    | Mandatory | Description
--------- | ------- | --------- | -----------
`symbol`  | STRING  | YES       |
`fromId`  | INT     | NO        | Trade ID to begin at
`limit`   | INT     | NO        | Default: 500; Maximum: 1000

Notes:

* If `fromId` is not specified, the most recent trades are returned.

**Data Source:**
Database

**Response:**
```javascript
{
    "id": "cffc9c7d-4efc-4ce0-b587-6b87448f052a",
    "status": 200,
    "result": [
        {
            "id": 0,
            "price": "0.00005000",
            "qty": "40.00000000",
            "quoteQty": "0.00200000",
            "time": 1500004800376,
            "isBuyerMaker": true,
            "isBestMatch": true
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 10
        }
    ]
}
```

### Aggregate trades

```javascript
{
    "id": "189da436-d4bd-48ca-9f95-9f613d621717",
    "method": "trades.aggregate",
    "params": {
        "symbol": "BNBBTC",
        "fromId": 50000000,
        "limit": 1
    }
}
```

Get aggregate trades.

An *aggregate trade* (aggtrade) represents one or more individual trades.
Trades that fill at the same time, from the same taker order, with the same price –
those trades are collected into an aggregate trade with total quantity of the individual trades.

If you need access to real-time trading activity, please consider using WebSocket Streams:

* [`<symbol>@aggTrade`](web-socket-streams.md#aggregate-trade-streams)

If you need historical aggregate trade data,
please consider using [data.binance.vision](https://github.com/binance/binance-public-data/#aggtrades).

**Weight:**
4

**Parameters:**

Name        | Type    | Mandatory | Description
----------- | ------- | --------- | -----------
`symbol`    | STRING  | YES       |
`fromId`    | LONG    | NO        | Aggregate trade ID to begin at
`startTime` | LONG    | NO        |
`endTime`   | LONG    | NO        |
`limit`     | LONG    | NO        | Default: 500; Maximum: 1000

Notes:

* If `fromId` is specified, return aggtrades with aggregate trade ID >= `fromId`.

  Use `fromId` and `limit` to page through all aggtrades.

* If `startTime` and/or `endTime` are specified, aggtrades are filtered by execution time (`T`).

  `fromId` cannot be used together with `startTime` and `endTime`.

* If no condition is specified, the most recent aggregate trades are returned.

**Data Source:**
Database

**Response:**
```javascript
{
    "id": "189da436-d4bd-48ca-9f95-9f613d621717",
    "status": 200,
    "result": [
        {
            "a": 50000000,          // Aggregate trade ID
            "p": "0.00274100",      // Price
            "q": "57.19000000",     // Quantity
            "f": 59120167,          // First trade ID
            "l": 59120170,          // Last trade ID
            "T": 1565877971222,     // Timestamp
            "m": true,              // Was the buyer the maker?
            "M": true               // Was the trade the best price match?
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```

### Klines

```javascript
{
    "id": "1dbbeb56-8eea-466a-8f6e-86bdcfa2fc0b",
    "method": "klines",
    "params": {
        "symbol": "BNBBTC",
        "interval": "1h",
        "startTime": 1655969280000,
        "limit": 1
    }
}
```

Get klines (candlestick bars).

Klines are uniquely identified by their open & close time.

If you need access to real-time kline updates, please consider using WebSocket Streams:

* [`<symbol>@kline_<interval>`](web-socket-streams.md#klinecandlestick-streams)

If you need historical kline data,
please consider using [data.binance.vision](https://github.com/binance/binance-public-data/#klines).

**Weight:**
2

**Parameters:**

Name        | Type    | Mandatory | Description
----------- | ------- | --------- | -----------
`symbol`    | STRING  | YES       |
`interval`  | ENUM    | YES       |
`startTime` | LONG    | NO        |
`endTime`   | LONG    | NO        |
`timeZone`  | STRING  | NO        | Default: 0 (UTC)
`limit`     | INT     | NO        | Default: 500; Maximum: 1000


<a id="kline-intervals"></a>
Supported kline intervals (case-sensitive):

Interval  | `interval` value
--------- | ----------------
seconds   | `1s`
minutes   | `1m`, `3m`, `5m`, `15m`, `30m`
hours     | `1h`, `2h`, `4h`, `6h`, `8h`, `12h`
days      | `1d`, `3d`
weeks     | `1w`
months    | `1M`

Notes:

* If `startTime`, `endTime` are not specified, the most recent klines are returned.
* Supported values for `timeZone`:
  * Hours and minutes (e.g. `-1:00`, `05:45`)
  * Only hours (e.g. `0`, `8`, `4`)
  * Accepted range is strictly [-12:00 to +14:00] inclusive
* If `timeZone` provided, kline intervals are interpreted in that timezone instead of UTC.
* Note that `startTime` and `endTime` are always interpreted in UTC, regardless of timeZone.

**Data Source:**
Database

**Response:**
```javascript
{
    "id": "1dbbeb56-8eea-466a-8f6e-86bdcfa2fc0b",
    "status": 200,
    "result": [
        [
            1655971200000,       // Kline open time
            "0.01086000",        // Open price
            "0.01086600",        // High price
            "0.01083600",        // Low price
            "0.01083800",        // Close price
            "2290.53800000",     // Volume
            1655974799999,       // Kline close time
            "24.85074442",       // Quote asset volume
            2283,                // Number of trades
            "1171.64000000",     // Taker buy base asset volume
            "12.71225884",       // Taker buy quote asset volume
            "0"                  // Unused field, ignore
        ]
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```

### UI Klines

```javascript
{
    "id": "b137468a-fb20-4c06-bd6b-625148eec958",
    "method": "uiKlines",
    "params": {
        "symbol": "BNBBTC",
        "interval": "1h",
        "startTime": 1655969280000,
        "limit": 1
    }
}
```

Get klines (candlestick bars) optimized for presentation.

This request is similar to [`klines`](#klines), having the same parameters and response.
`uiKlines` return modified kline data, optimized for presentation of candlestick charts.

**Weight:**
2

**Parameters:**

Name        | Type    | Mandatory | Description
----------- | ------- | --------- | -----------
`symbol`    | STRING  | YES       |
`interval`  | ENUM    | YES       | See [`klines`](#kline-intervals)
`startTime` | LONG    | NO        |
`endTime`   | LONG    | NO        |
`timeZone`  | STRING  | NO        | Default: 0 (UTC)
`limit`     | INT     | NO        | Default: 500; Maximum: 1000

Notes:

* If `startTime`, `endTime` are not specified, the most recent klines are returned.
* Supported values for `timeZone`:
  * Hours and minutes (e.g. `-1:00`, `05:45`)
  * Only hours (e.g. `0`, `8`, `4`)
  * Accepted range is strictly [-12:00 to +14:00] inclusive
* If `timeZone` provided, kline intervals are interpreted in that timezone instead of UTC.
* Note that `startTime` and `endTime` are always interpreted in UTC, regardless of timeZone.

**Data Source:**
Database

**Response:**
```javascript
{
    "id": "b137468a-fb20-4c06-bd6b-625148eec958",
    "status": 200,
    "result": [
        [
            1655971200000,       // Kline open time
            "0.01086000",        // Open price
            "0.01086600",        // High price
            "0.01083600",        // Low price
            "0.01083800",        // Close price
            "2290.53800000",     // Volume
            1655974799999,       // Kline close time
            "24.85074442",       // Quote asset volume
            2283,                // Number of trades
            "1171.64000000",     // Taker buy base asset volume
            "12.71225884",       // Taker buy quote asset volume
            "0"                  // Unused field, ignore
        ]
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```

### Current average price

```javascript
{
    "id": "ddbfb65f-9ebf-42ec-8240-8f0f91de0867",
    "method": "avgPrice",
    "params": {
        "symbol": "BNBBTC"
    }
}
```

Get current average price for a symbol.

**Weight:**
2

**Parameters:**

Name        | Type    | Mandatory | Description
----------- | ------- | --------- | -----------
`symbol`    | STRING  | YES       |

**Data Source:**
Memory

**Response:**
```javascript
{
    "id": "ddbfb65f-9ebf-42ec-8240-8f0f91de0867",
    "status": 200,
    "result": {
        "mins": 5,                     // Average price interval (in minutes)
        "price": "9.35751834",         // Average price
        "closeTime": 1694061154503     // Last trade time
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```

### 24hr ticker price change statistics

```javascript
{
    "id": "93fb61ef-89f8-4d6e-b022-4f035a3fadad",
    "method": "ticker.24hr",
    "params": {
        "symbol": "BNBBTC"
    }
}
```

Get 24-hour rolling window price change statistics.

If you need to continuously monitor trading statistics, please consider using WebSocket Streams:

* [`<symbol>@ticker`](web-socket-streams.md#individual-symbol-ticker-streams) or [`!ticker@arr`](web-socket-streams.md#all-market-tickers-stream)
* [`<symbol>@miniTicker`](web-socket-streams.md#individual-symbol-mini-ticker-stream) or [`!miniTicker@arr`](web-socket-streams.md#all-market-mini-tickers-stream)

If you need different window sizes,
use the [`ticker`](#rolling-window-price-change-statistics) request.

**Weight:**
Adjusted based on the number of requested symbols:

| Symbols     | Weight |
|:-----------:|:------:|
|        1–20 |      2 |
|      21–100 |     40 |
| 101 or more |     80 |
| all symbols |     80 |

**Parameters:**

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>symbol</code></td>
        <td>STRING</td>
        <td rowspan="2" align="center">NO</td>
        <td>Query ticker for a single symbol</td>
    </tr>
    <tr>
        <td><code>symbols</code></td>
        <td>ARRAY of STRING</td>
        <td>Query ticker for multiple symbols</td>
    </tr>
    <tr>
        <td><code>type</code></td>
        <td>ENUM</td>
        <td align="center">NO</td>
        <td>Ticker type: <code>FULL</code> (default) or <code>MINI</code></td>
    </tr>
    <tr>
        <td>symbolStatus</td>
        <td>ENUM</td>
        <td rowspan="2" align="center">NO</td>
        <td>Filters for symbols that have this <code>tradingStatus</code>.<br>For a single symbol, a status mismatch returns error <code>-1220 SYMBOL_DOES_NOT_MATCH_STATUS</code>.<br>For multiple or all symbols, non-matching ones are simply excluded from the response.<br>Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code> </td>
    </tr>
</tbody>
</table>

Notes:

* `symbol` and `symbols` cannot be used together.

* If no symbol is specified, returns information about all symbols currently trading on the exchange.

**Data Source:**
Memory

**Response:**

`FULL` type, for a single symbol:

```javascript
{
    "id": "93fb61ef-89f8-4d6e-b022-4f035a3fadad",
    "status": 200,
    "result": {
        "symbol": "BNBBTC",
        "priceChange": "0.00013900",
        "priceChangePercent": "1.020",
        "weightedAvgPrice": "0.01382453",
        "prevClosePrice": "0.01362800",
        "lastPrice": "0.01376700",
        "lastQty": "1.78800000",
        "bidPrice": "0.01376700",
        "bidQty": "4.64600000",
        "askPrice": "0.01376800",
        "askQty": "14.31400000",
        "openPrice": "0.01362800",
        "highPrice": "0.01414900",
        "lowPrice": "0.01346600",
        "volume": "69412.40500000",
        "quoteVolume": "959.59411487",
        "openTime": 1660014164909,
        "closeTime": 1660100564909,
        "firstId": 194696115,     // First trade ID
        "lastId": 194968287,      // Last trade ID
        "count": 272173           // Number of trades
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```

`MINI` type, for a single symbol:

```javascript
{
    "id": "9fa2a91b-3fca-4ed7-a9ad-58e3b67483de",
    "status": 200,
    "result": {
        "symbol": "BNBBTC",
        "openPrice": "0.01362800",
        "highPrice": "0.01414900",
        "lowPrice": "0.01346600",
        "lastPrice": "0.01376700",
        "volume": "69412.40500000",
        "quoteVolume": "959.59411487",
        "openTime": 1660014164909,
        "closeTime": 1660100564909,
        "firstId": 194696115,     // First trade ID
        "lastId": 194968287,      // Last trade ID
        "count": 272173           // Number of trades
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```

If more than one symbol is requested, response returns an array:

```javascript
{
    "id": "901be0d9-fd3b-45e4-acd6-10c580d03430",
    "status": 200,
    "result": [
        {
            "symbol": "BNBBTC",
            "priceChange": "0.00016500",
            "priceChangePercent": "1.213",
            "weightedAvgPrice": "0.01382508",
            "prevClosePrice": "0.01360800",
            "lastPrice": "0.01377200",
            "lastQty": "1.01400000",
            "bidPrice": "0.01377100",
            "bidQty": "7.55700000",
            "askPrice": "0.01377200",
            "askQty": "4.37900000",
            "openPrice": "0.01360700",
            "highPrice": "0.01414900",
            "lowPrice": "0.01346600",
            "volume": "69376.27900000",
            "quoteVolume": "959.13277091",
            "openTime": 1660014615517,
            "closeTime": 1660101015517,
            "firstId": 194697254,
            "lastId": 194969483,
            "count": 272230
        },
        {
            "symbol": "BTCUSDT",
            "priceChange": "-938.06000000",
            "priceChangePercent": "-3.938",
            "weightedAvgPrice": "23265.34432003",
            "prevClosePrice": "23819.17000000",
            "lastPrice": "22880.91000000",
            "lastQty": "0.00536000",
            "bidPrice": "22880.40000000",
            "bidQty": "0.00424000",
            "askPrice": "22880.91000000",
            "askQty": "0.04276000",
            "openPrice": "23818.97000000",
            "highPrice": "23933.25000000",
            "lowPrice": "22664.69000000",
            "volume": "153508.37606000",
            "quoteVolume": "3571425225.04441220",
            "openTime": 1660014615977,
            "closeTime": 1660101015977,
            "firstId": 1592019902,
            "lastId": 1597301762,
            "count": 5281861
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```

### Trading Day Ticker

```javascript
{
    "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",
    "method": "ticker.tradingDay",
    "params": {
        "symbols": ["BNBBTC", "BTCUSDT"],
        "timeZone": "00:00"
    }
}
```

Price change statistics for a trading day.

**Weight:**

4 for each requested <tt>symbol</tt>. <br/><br/> The weight for this request will cap at 200 once the number of `symbols` in the request is more than 50.

**Parameters:**

<table>
  <tr>
    <th>Name</th>
    <th>Type</th>
    <th>Mandatory</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>symbol</code></td>
    <td>STRING</td>
    <td rowspan="2" align="center">YES</td>
    <td>Query ticker of a single symbol</td>
  </tr>
  <tr>
    <td><code>symbols</code></td>
    <td>ARRAY of STRING</td>
    <td>Query ticker for multiple symbols</td>
  </tr>
  <tr>
     <td><code>timeZone</code></td>
     <td>STRING</td>
     <td>NO</td>
     <td>Default: 0 (UTC)</td>
  </tr>
  <tr>
      <td><code>type</code></td>
      <td>ENUM</td>
      <td>NO</td>
      <td>Supported values: <tt>FULL</tt> or <tt>MINI</tt>. <br/>If none provided, the default is <tt>FULL</tt> </td>
  </tr>
  <tr>
      <td>symbolStatus</td>
      <td>ENUM</td>
      <td>NO</td>
      <td>Filters for symbols that have this <code>tradingStatus</code>.<br>For a single symbol, a status mismatch returns error <code>-1220 SYMBOL_DOES_NOT_MATCH_STATUS</code>. <br>For multiple symbols, non-matching ones are simply excluded from the response.<br> Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code> </td>
  </tr>
</table>

**Notes:**

* Supported values for `timeZone`:
  * Hours and minutes (e.g. `-1:00`, `05:45`)
  * Only hours (e.g. `0`, `8`, `4`)

**Data Source:**
Database

**Response: - FULL**

With `symbol`:

```javascript
{
    "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",
    "status": 200,
    "result": {
        "symbol": "BTCUSDT",
        "priceChange": "-83.13000000",            // Absolute price change
        "priceChangePercent": "-0.317",           // Relative price change in percent
        "weightedAvgPrice": "26234.58803036",     // quoteVolume / volume
        "openPrice": "26304.80000000",
        "highPrice": "26397.46000000",
        "lowPrice": "26088.34000000",
        "lastPrice": "26221.67000000",
        "volume": "18495.35066000",               // Volume in base asset
        "quoteVolume": "485217905.04210480",
        "openTime": 1695686400000,
        "closeTime": 1695772799999,
        "firstId": 3220151555,
        "lastId": 3220849281,
        "count": 697727
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 4
        }
    ]
}
```

With `symbols`:

```javascript
{
    "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",
    "status": 200,
    "result": [
        {
            "symbol": "BTCUSDT",
            "priceChange": "-83.13000000",
            "priceChangePercent": "-0.317",
            "weightedAvgPrice": "26234.58803036",
            "openPrice": "26304.80000000",
            "highPrice": "26397.46000000",
            "lowPrice": "26088.34000000",
            "lastPrice": "26221.67000000",
            "volume": "18495.35066000",
            "quoteVolume": "485217905.04210480",
            "openTime": 1695686400000,
            "closeTime": 1695772799999,
            "firstId": 3220151555,
            "lastId": 3220849281,
            "count": 697727
        },
        {
            "symbol": "BNBUSDT",
            "priceChange": "2.60000000",
            "priceChangePercent": "1.238",
            "weightedAvgPrice": "211.92276958",
            "openPrice": "210.00000000",
            "highPrice": "213.70000000",
            "lowPrice": "209.70000000",
            "lastPrice": "212.60000000",
            "volume": "280709.58900000",
            "quoteVolume": "59488753.54750000",
            "openTime": 1695686400000,
            "closeTime": 1695772799999,
            "firstId": 672397461,
            "lastId": 672496158,
            "count": 98698
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 8
        }
    ]
}
```

**Response: - MINI**

With `symbol`:

```javascript
{
    "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",
    "status": 200,
    "result": {
        "symbol": "BTCUSDT",
        "openPrice": "26304.80000000",
        "highPrice": "26397.46000000",
        "lowPrice": "26088.34000000",
        "lastPrice": "26221.67000000",
        "volume": "18495.35066000",              // Volume in base asset
        "quoteVolume": "485217905.04210480",     // Volume in quote asset
        "openTime": 1695686400000,
        "closeTime": 1695772799999,
        "firstId": 3220151555,                   // Trade ID of the first trade in the interval
        "lastId": 3220849281,                    // Trade ID of the last trade in the interval
        "count": 697727                          // Number of trades in the interval
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 4
        }
    ]
}
```

With `symbols`:

```javascript
{
    "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",
    "status": 200,
    "result": [
        {
            "symbol": "BTCUSDT",
            "openPrice": "26304.80000000",
            "highPrice": "26397.46000000",
            "lowPrice": "26088.34000000",
            "lastPrice": "26221.67000000",
            "volume": "18495.35066000",
            "quoteVolume": "485217905.04210480",
            "openTime": 1695686400000,
            "closeTime": 1695772799999,
            "firstId": 3220151555,
            "lastId": 3220849281,
            "count": 697727
        },
        {
            "symbol": "BNBUSDT",
            "openPrice": "210.00000000",
            "highPrice": "213.70000000",
            "lowPrice": "209.70000000",
            "lastPrice": "212.60000000",
            "volume": "280709.58900000",
            "quoteVolume": "59488753.54750000",
            "openTime": 1695686400000,
            "closeTime": 1695772799999,
            "firstId": 672397461,
            "lastId": 672496158,
            "count": 98698
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 8
        }
    ]
}
```

### Rolling window price change statistics

```javascript
{
    "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",
    "method": "ticker",
    "params": {
        "symbols": ["BNBBTC", "BTCUSDT"],
        "windowSize": "7d"
    }
}
```

Get rolling window price change statistics with a custom window.

This request is similar to [`ticker.24hr`](#24hr-ticker-price-change-statistics),
but statistics are computed on demand using the arbitrary window you specify.

**Note:** Window size precision is limited to 1 minute.
While the `closeTime` is the current time of the request, `openTime` always start on a minute boundary.
As such, the effective window might be up to 59999 ms wider than the requested `windowSize`.

<details>
<summary>Window computation example</summary>

For example, a request for `"windowSize": "7d"` might result in the following window:

```javascript
{
    "openTime": 1659580020000,
    "closeTime": 1660184865291
}
```

Time of the request – `closeTime` – is 1660184865291 (August 11, 2022 02:27:45.291).
Requested window size should put the `openTime` 7 days before that – August 4, 02:27:45.291 –
but due to limited precision it ends up a bit earlier: 1659580020000 (August 4, 2022 02:27:00),
exactly at the start of a minute.

</details>

If you need to continuously monitor trading statistics, please consider using WebSocket Streams:

* [`<symbol>@ticker_<window_size>`](web-socket-streams.md#individual-symbol-rolling-window-statistics-streams) or [`!ticker_<window-size>@arr`](web-socket-streams.md#all-market-rolling-window-statistics-streams)

**Weight:**
Adjusted based on the number of requested symbols:

| Symbols | Weight |
|:-------:|:------:|
|    1–50 | 4 per symbol |
|  51–100 |    200 |

**Parameters:**

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>symbol</code></td>
        <td>STRING</td>
        <td rowspan="2" align="center">YES</td>
        <td>Query ticker of a single symbol</td>
    </tr>
    <tr>
        <td><code>symbols</code></td>
        <td>ARRAY of STRING</td>
        <td>Query ticker for multiple symbols</td>
    </tr>
    <tr>
        <td><code>type</code></td>
        <td>ENUM</td>
        <td align="center">NO</td>
        <td>Ticker type: <code>FULL</code> (default) or <code>MINI</code></td>
    </tr>
    <tr>
        <td><code>windowSize</code></td>
        <td>ENUM</td>
        <td align="center">NO</td>
        <td>Default <code>1d</code></td>
    </tr>
    <tr>
        <td>symbolStatus</td>
        <td>ENUM</td>
        <td align="center">NO</td>
        <td>Filters for symbols that have this <code>tradingStatus</code>.<br>For a single symbol, a status mismatch returns error <code>-1220 SYMBOL_DOES_NOT_MATCH_STATUS</code>. <br>For multiple symbols, non-matching ones are simply excluded from the response.<br>Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code> </td>
    </tr>
</tbody>
</table>

Supported window sizes:

Unit    | `windowSize` value
------- | ------------------
minutes | `1m`, `2m` ... `59m`
hours   | `1h`, `2h` ... `23h`
days    | `1d`, `2d` ... `7d`

Notes:

* Either `symbol` or `symbols` must be specified.

* Maximum number of symbols in one request: 200.

* Window size units cannot be combined.
  E.g., <code>1d 2h</code> is not supported.

**Data Source:**
Database

**Response:**

`FULL` type, for a single symbol:

```javascript
{
    "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",
    "status": 200,
    "result": {
        "symbol": "BNBBTC",
        "priceChange": "0.00061500",
        "priceChangePercent": "4.735",
        "weightedAvgPrice": "0.01368242",
        "openPrice": "0.01298900",
        "highPrice": "0.01418800",
        "lowPrice": "0.01296000",
        "lastPrice": "0.01360400",
        "volume": "587179.23900000",
        "quoteVolume": "8034.03382165",
        "openTime": 1659580020000,
        "closeTime": 1660184865291,
        "firstId": 192977765,     // First trade ID
        "lastId": 195365758,      // Last trade ID
        "count": 2387994          // Number of trades
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 4
        }
    ]
}
```

`MINI` type, for a single symbol:

```javascript
{
    "id": "bdb7c503-542c-495c-b797-4d2ee2e91173",
    "status": 200,
    "result": {
        "symbol": "BNBBTC",
        "openPrice": "0.01298900",
        "highPrice": "0.01418800",
        "lowPrice": "0.01296000",
        "lastPrice": "0.01360400",
        "volume": "587179.23900000",
        "quoteVolume": "8034.03382165",
        "openTime": 1659580020000,
        "closeTime": 1660184865291,
        "firstId": 192977765,     // First trade ID
        "lastId": 195365758,      // Last trade ID
        "count": 2387994          // Number of trades
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 4
        }
    ]
}
```

If more than one symbol is requested, response returns an array:

```javascript
{
    "id": "f4b3b507-c8f2-442a-81a6-b2f12daa030f",
    "status": 200,
    "result": [
        {
            "symbol": "BNBBTC",
            "priceChange": "0.00061500",
            "priceChangePercent": "4.735",
            "weightedAvgPrice": "0.01368242",
            "openPrice": "0.01298900",
            "highPrice": "0.01418800",
            "lowPrice": "0.01296000",
            "lastPrice": "0.01360400",
            "volume": "587169.48600000",
            "quoteVolume": "8033.90114517",
            "openTime": 1659580020000,
            "closeTime": 1660184820927,
            "firstId": 192977765,
            "lastId": 195365700,
            "count": 2387936
        },
        {
            "symbol": "BTCUSDT",
            "priceChange": "1182.92000000",
            "priceChangePercent": "5.113",
            "weightedAvgPrice": "23349.27074846",
            "openPrice": "23135.33000000",
            "highPrice": "24491.22000000",
            "lowPrice": "22400.00000000",
            "lastPrice": "24318.25000000",
            "volume": "1039498.10978000",
            "quoteVolume": "24271522807.76838630",
            "openTime": 1659580020000,
            "closeTime": 1660184820927,
            "firstId": 1568787779,
            "lastId": 1604337406,
            "count": 35549628
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 8
        }
    ]
}
```

### Symbol price ticker

```javascript
{
    "id": "043a7cf2-bde3-4888-9604-c8ac41fcba4d",
    "method": "ticker.price",
    "params": {
        "symbol": "BNBBTC"
    }
}
```

Get the latest market price for a symbol.

If you need access to real-time price updates, please consider using WebSocket Streams:

* [`<symbol>@aggTrade`](web-socket-streams.md#aggregate-trade-streams)
* [`<symbol>@trade`](web-socket-streams.md#trade-streams)

**Weight:**
Adjusted based on the number of requested symbols:

| Parameter | Weight |
| --------- |:------:|
| `symbol`  |      2 |
| `symbols` |      4 |
| none      |      4 |

**Parameters:**

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>symbol</code></td>
        <td>STRING</td>
        <td rowspan="2" align="center">NO</td>
        <td>Query price for a single symbol</td>
    </tr>
    <tr>
        <td><code>symbols</code></td>
        <td>ARRAY of STRING</td>
        <td>Query price for multiple symbols</td>
    </tr>
    <tr>
        <td>symbolStatus</td>
        <td>ENUM</td>
        <td align="center">NO</td>
        <td>Filters for symbols that have this <code>tradingStatus</code>.<br>For a single symbol, a status mismatch returns error <code>-1220 SYMBOL_DOES_NOT_MATCH_STATUS</code>.<br>For multiple or all symbols, non-matching ones are simply excluded from the response.<br>Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code> </td>
    </tr>
</tbody>
</table>

Notes:

* `symbol` and `symbols` cannot be used together.

* If no symbol is specified, returns information about all symbols currently trading on the exchange.

**Data Source:**
Memory

**Response:**

```javascript
{
    "id": "043a7cf2-bde3-4888-9604-c8ac41fcba4d",
    "status": 200,
    "result": {
        "symbol": "BNBBTC",
        "price": "0.01361900"
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```

If more than one symbol is requested, response returns an array:

```javascript
{
    "id": "e739e673-24c8-4adf-9cfa-b81f30330b09",
    "status": 200,
    "result": [
        {
            "symbol": "BNBBTC",
            "price": "0.01363700"
        },
        {
            "symbol": "BTCUSDT",
            "price": "24267.15000000"
        },
        {
            "symbol": "BNBBUSD",
            "price": "331.10000000"
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 4
        }
    ]
}
```

### Symbol order book ticker

```javascript
{
    "id": "057deb3a-2990-41d1-b58b-98ea0f09e1b4",
    "method": "ticker.book",
    "params": {
        "symbols": ["BNBBTC", "BTCUSDT"]
    }
}
```

Get the current best price and quantity on the order book.

If you need access to real-time order book ticker updates, please consider using WebSocket Streams:

* [`<symbol>@bookTicker`](web-socket-streams.md#individual-symbol-book-ticker-streams)

**Weight:**
Adjusted based on the number of requested symbols:

| Parameter | Weight |
| --------- |:------:|
| `symbol`  |      2 |
| `symbols` |      4 |
| none      |      4 |

**Parameters:**

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>symbol</code></td>
        <td>STRING</td>
        <td rowspan="2" align="center">NO</td>
        <td>Query ticker for a single symbol</td>
    </tr>
    <tr>
        <td><code>symbols</code></td>
        <td>ARRAY of STRING</td>
        <td>Query ticker for multiple symbols</td>
    </tr>
    <tr>
        <td>symbolStatus</td>
        <td>ENUM</td>
        <td align="center">NO</td>
        <td>Filters for symbols that have this <code>tradingStatus</code>.<br>For a single symbol, a status mismatch returns error <code>-1220 SYMBOL_DOES_NOT_MATCH_STATUS</code>. <br>For multiple or all symbols, non-matching ones are simply excluded from the response.<br>Valid values: <code>TRADING</code>, <code>HALT</code>, <code>BREAK</code> </td>
    </tr>
</tbody>
</table>

Notes:

* `symbol` and `symbols` cannot be used together.

* If no symbol is specified, returns information about all symbols currently trading on the exchange.

**Data Source:**
Memory

**Response:**

```javascript
{
    "id": "9d32157c-a556-4d27-9866-66760a174b57",
    "status": 200,
    "result": {
        "symbol": "BNBBTC",
        "bidPrice": "0.01358000",
        "bidQty": "12.53400000",
        "askPrice": "0.01358100",
        "askQty": "17.83700000"
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 2
        }
    ]
}
```

If more than one symbol is requested, response returns an array:

```javascript
{
    "id": "057deb3a-2990-41d1-b58b-98ea0f09e1b4",
    "status": 200,
    "result": [
        {
            "symbol": "BNBBTC",
            "bidPrice": "0.01358000",
            "bidQty": "12.53400000",
            "askPrice": "0.01358100",
            "askQty": "17.83700000"
        },
        {
            "symbol": "BTCUSDT",
            "bidPrice": "23980.49000000",
            "bidQty": "0.01000000",
            "askPrice": "23981.31000000",
            "askQty": "0.01512000"
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 4
        }
    ]
}
```

## Authentication requests

**Note:** Only _Ed25519_ keys are supported for this feature.

<a id="session-logon"></a>

### Log in with API key (SIGNED)

```javascript
{
    "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",
    "method": "session.logon",
    "params": {
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "1cf54395b336b0a9727ef27d5d98987962bc47aca6e13fe978612d0adee066ed",
        "timestamp": 1649729878532
    }
}
```

Authenticate WebSocket connection using the provided API key.

After calling `session.logon`, you can omit `apiKey` and `signature` parameters for future requests that require them.

Note that only one API key can be authenticated.
Calling `session.logon` multiple times changes the current authenticated API key.

**Weight:**
2

**Parameters:**

Name          | Type    | Mandatory | Description
------------- | ------- | --------- | ------------
`apiKey`      | STRING  | YES       |
`recvWindow`  | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`   | STRING  | YES       |
`timestamp`   | LONG    | YES       |

**Data Source:**
Memory

**Response:**

```javascript
{
    "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",
    "status": 200,
    "result": {
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "authorizedSince": 1649729878532,
        "connectedSince": 1649729873021,
        "returnRateLimits": false,
        "serverTime": 1649729878630,
        "userDataStream": false // is User Data Stream subscription active?
    }
}
```

<a id="session-status"></a>

### Query session status

```javascript
{
    "id": "b50c16cd-62c9-4e29-89e4-37f10111f5bf",
    "method": "session.status"
}
```

Query the status of the WebSocket connection,
inspecting which API key (if any) is used to authorize requests.

**Weight:**
2

**Parameters:**
NONE

**Data Source:**
Memory

**Response:**

```javascript
{
    "id": "b50c16cd-62c9-4e29-89e4-37f10111f5bf",
    "status": 200,
    "result": {
        // if the connection is not authenticated, "apiKey" and "authorizedSince" will be shown as null
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "authorizedSince": 1649729878532,
        "connectedSince": 1649729873021,
        "returnRateLimits": false,
        "serverTime": 1649730611671,
        "userDataStream": true     // is User Data Stream subscription active?
    }
}
```

### Log out of the session

```javascript
{
    "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",
    "method": "session.logout"
}
```

Forget the API key previously authenticated.
If the connection is not authenticated, this request does nothing.

Note that the WebSocket connection stays open after `session.logout` request.
You can continue using the connection,
but now you will have to explicitly provide the `apiKey` and `signature` parameters where needed.

**Weight:**
2

**Parameters:**
NONE

**Data Source:**
Memory

**Response:**

```javascript
{
    "id": "c174a2b1-3f51-4580-b200-8528bd237cb7",
    "status": 200,
    "result": {
        "apiKey": null,
        "authorizedSince": null,
        "connectedSince": 1649729873021,
        "returnRateLimits": false,
        "serverTime": 1649730611671,
        "userDataStream": false // is User Data Stream subscription active?
    }
}
```

## Trading requests

### Place new order (TRADE)

```javascript
{
    "id": "56374a46-3061-486b-a311-99ee972eb648",
    "method": "order.place",
    "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "price": "23416.10000000",
        "quantity": "0.00847000",
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",
        "timestamp": 1660801715431
    }
}
```

Send in a new order.

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

**Weight:**
1

**Unfilled Order Count:**
1

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`symbol`            | STRING  | YES       |
`side`              | ENUM    | YES       | `BUY` or `SELL`
`type`              | ENUM    | YES       |
`timeInForce`       | ENUM    | NO *      |
`price`             | DECIMAL | NO *      |
`quantity`          | DECIMAL | NO *      |
`quoteOrderQty`     | DECIMAL | NO *      |
`newClientOrderId`  | STRING  | NO        | Arbitrary unique ID among open orders. Automatically generated if not sent
`newOrderRespType`  | ENUM    | NO        | <p>Select response format: `ACK`, `RESULT`, `FULL`.</p><p>`MARKET` and `LIMIT` orders use `FULL` by default, other order types default to `ACK`.</p>
`stopPrice`         | DECIMAL | NO *      |
`trailingDelta`     | INT     | NO *      | See [Trailing Stop order FAQ](faqs/trailing-stop-faq.md)
`icebergQty`        | DECIMAL | NO        |
`strategyId`        | LONG    | NO        | Arbitrary numeric value identifying the order within an order strategy.
`strategyType`      | INT     | NO        | <p>Arbitrary numeric value identifying the order strategy.</p><p>Values smaller than `1000000` are reserved and cannot be used.</p>
`selfTradePreventionMode` |ENUM | NO      | The allowed enums is dependent on what is configured on the symbol. Supported values: [STP Modes](enums.md#stpmodes)
`pegPriceType`      | ENUM    | NO        | `PRIMARY_PEG` or `MARKET_PEG` <br> See [Pegged Orders](#pegged-orders-info)
`pegOffsetValue`    | INT     | NO        | Price level to peg the price to (max: 100) <br> See [Pegged Orders](#pegged-orders-info)
`pegOffsetType`     | ENUM    | NO        | Only `PRICE_LEVEL` is supported <br> See [Pegged Orders](#pegged-orders-info)
`apiKey`            | STRING  | YES       |
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |
`timestamp`         | LONG    | YES       |

<a id="order-type">Certain parameters (*)</a> become mandatory based on the order `type`:

<table>
<thead>
    <tr>
        <th>Order <code>type</code></th>
        <th>Mandatory parameters</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>LIMIT</code></td>
        <td>
        <ul>
            <li><code>timeInForce</code></li>
            <li><code>price</code></li>
            <li><code>quantity</code></li>
        </ul>
        </td>
    </tr>
    <tr>
        <td><code>LIMIT_MAKER</code></td>
        <td>
        <ul>
            <li><code>price</code></li>
            <li><code>quantity</code></li>
        </ul>
        </td>
    </tr>
    <tr>
        <td><code>MARKET</code></td>
        <td>
        <ul>
            <li><code>quantity</code> or <code>quoteOrderQty</code></li>
        </ul>
        </td>
    </tr>
    <tr>
        <td><code>STOP_LOSS</code></td>
        <td>
        <ul>
            <li><code>quantity</code></li>
            <li><code>stopPrice</code> or <code>trailingDelta</code></li>
        </ul>
        </td>
    </tr>
    <tr>
        <td><code>STOP_LOSS_LIMIT</code></td>
        <td>
        <ul>
            <li><code>timeInForce</code></li>
            <li><code>price</code></li>
            <li><code>quantity</code></li>
            <li><code>stopPrice</code> or <code>trailingDelta</code></li>
        </ul>
        </td>
    </tr>
    <tr>
        <td><code>TAKE_PROFIT</code></td>
        <td>
        <ul>
            <li><code>quantity</code></li>
            <li><code>stopPrice</code> or <code>trailingDelta</code></li>
        </ul>
        </td>
    </tr>
    <tr>
        <td><code>TAKE_PROFIT_LIMIT</code></td>
        <td>
        <ul>
            <li><code>timeInForce</code></li>
            <li><code>price</code></li>
            <li><code>quantity</code></li>
            <li><code>stopPrice</code> or <code>trailingDelta</code></li>
        </ul>
        </td>
    </tr>
</tbody>
</table>

Supported order types:

<table>
<thead>
    <tr>
        <th>Order <code>type</code></th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>LIMIT</code></td>
        <td>
        <p>
            Buy or sell <code>quantity</code> at the specified <code>price</code> or better.
        </p>
        </td>
    </tr>
    <tr>
        <td><code>LIMIT_MAKER</code></td>
        <td>
        <p>
            <code>LIMIT</code> order that will be rejected if it immediately matches and trades as a taker.
        </p>
        <p>
            This order type is also known as a POST-ONLY order.
        </p>
        </td>
    </tr>
    <tr>
        <td><code>MARKET</code></td>
        <td>
        <p>
            Buy or sell at the best available market price.
        </p>
        <ul>
            <li>
                <p>
                    <code>MARKET</code> order with <code>quantity</code> parameter
                    specifies the amount of the <em>base asset</em> you want to buy or sell.
                    Actually executed quantity of the quote asset will be determined by available market liquidity.
                </p>
                <p>
                    E.g., a MARKET BUY order on BTCUSDT for <code>"quantity": "0.1000"</code>
                    specifies that you want to buy 0.1 BTC at the best available price.
                    If there is not enough BTC at the best price, keep buying at the next best price,
                    until either your order is filled, or you run out of USDT, or market runs out of BTC.
                </p>
            </li>
            <li>
                <p>
                    <code>MARKET</code> order with <code>quoteOrderQty</code> parameter
                    specifies the amount of the <em>quote asset</em> you want to spend (when buying) or receive (when selling).
                    Actually executed quantity of the base asset will be determined by available market liquidity.
                </p>
                <p>
                    E.g., a MARKET BUY on BTCUSDT for <code>"quoteOrderQty": "100.00"</code>
                    specifies that you want to buy as much BTC as you can for 100 USDT at the best available price.
                    Similarly, a SELL order will sell as much available BTC as needed for you to receive 100 USDT
                    (before commission).
                </p>
            </li>
        </ul>
        </td>
    </tr>
    <tr>
        <td><code>STOP_LOSS</code></td>
        <td>
        <p>
            Execute a <code>MARKET</code> order for given <code>quantity</code> when specified conditions are met.
        </p>
        <p>
            I.e., when <code>stopPrice</code> is reached, or when <code>trailingDelta</code> is activated.
        </p>
        </td>
    </tr>
    <tr>
        <td><code>STOP_LOSS_LIMIT</code></td>
        <td>
        <p>
            Place a <code>LIMIT</code> order with given parameters when specified conditions are met.
        </p>
        </td>
    </tr>
    <tr>
        <td><code>TAKE_PROFIT</code></td>
        <td>
        <p>
            Like <code>STOP_LOSS</code> but activates when market price moves in the favorable direction.
        </p>
        </td>
    </tr>
    <tr>
        <td><code>TAKE_PROFIT_LIMIT</code></td>
        <td>
        <p>
            Like <code>STOP_LOSS_LIMIT</code> but activates when market price moves in the favorable direction.
        </p>
        </td>
    </tr>
</tbody>
</table>

<a id="pegged-orders-info"></a>
Notes on using parameters for Pegged Orders:

* These parameters are allowed for `LIMIT`, `LIMIT_MAKER`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT_LIMIT` orders.
* If `pegPriceType` is specified, `price` becomes optional. Otherwise, it is still mandatory.
* `pegPriceType=PRIMARY_PEG` means the primary peg, that is the best price on the same side of the order book as your order.
* `pegPriceType=MARKET_PEG` means the market peg, that is the best price on the opposite side of the order book from your order.
* Use `pegOffsetType` and `pegOffsetValue` to request a price level other than the best one. These parameters must be specified together.

<a id="timeInForce"></a>

Available `timeInForce` options,
setting how long the order should be active before expiration:

 TIF  | Description
----- | --------------
`GTC` | **Good 'til Canceled** – the order will remain on the book until you cancel it, or the order is completely filled.
`IOC` | **Immediate or Cancel** – the order will be filled for as much as possible, the unfilled quantity immediately expires.
`FOK` | **Fill or Kill** – the order will expire unless it cannot be immediately filled for the entire quantity.

Notes:

* `newClientOrderId` specifies `clientOrderId` value for the order.

  A new order with the same `clientOrderId` is accepted only when the previous one is filled or expired.

* Any `LIMIT` or `LIMIT_MAKER` order can be made into an iceberg order by specifying the `icebergQty`.

  An order with an `icebergQty` must have `timeInForce` set to `GTC`.

* Trigger order price rules for `STOP_LOSS`/`TAKE_PROFIT` orders:

  * `stopPrice` must be above market price: `STOP_LOSS BUY`, `TAKE_PROFIT SELL`
  * `stopPrice` must be below market price: `STOP_LOSS SELL`, `TAKE_PROFIT BUY`

* `MARKET` orders using `quoteOrderQty` follow [`LOT_SIZE`](filters.md#lot_size) filter rules.

  The order will execute a quantity that has notional value as close as possible to requested `quoteOrderQty`.

**Data Source:**
Matching Engine

**Response:**

Response format is selected by using the `newOrderRespType` parameter.

`ACK` response type:

```javascript
{
    "id": "56374a46-3061-486b-a311-99ee972eb648",
    "status": 200,
    "result": {
        "symbol": "BTCUSDT",
        "orderId": 12569099453,
        "orderListId": -1, // always -1 for singular orders
        "clientOrderId": "4d96324ff9d44481926157ec08158a40",
        "transactTime": 1660801715639
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 1
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 1
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

`RESULT` response type:

```javascript
{
    "id": "56374a46-3061-486b-a311-99ee972eb648",
    "status": 200,
    "result": {
        "symbol": "BTCUSDT",
        "orderId": 12569099453,
        "orderListId": -1, // always -1 for singular orders
        "clientOrderId": "4d96324ff9d44481926157ec08158a40",
        "transactTime": 1660801715639,
        "price": "23416.10000000",
        "origQty": "0.00847000",
        "executedQty": "0.00000000",
        "origQuoteOrderQty": "0.000000",
        "cummulativeQuoteQty": "0.00000000",
        "status": "NEW",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "SELL",
        "workingTime": 1660801715639,
        "selfTradePreventionMode": "NONE"
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 1
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 1
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

`FULL` response type:

```javascript
{
    "id": "56374a46-3061-486b-a311-99ee972eb648",
    "status": 200,
    "result": {
        "symbol": "BTCUSDT",
        "orderId": 12569099453,
        "orderListId": -1,
        "clientOrderId": "4d96324ff9d44481926157ec08158a40",
        "transactTime": 1660801715793,
        "price": "23416.10000000",
        "origQty": "0.00847000",
        "executedQty": "0.00847000",
        "origQuoteOrderQty": "0.000000",
        "cummulativeQuoteQty": "198.33521500",
        "status": "FILLED",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "SELL",
        "workingTime": 1660801715793,
        // FULL response is identical to RESULT response, with the same optional fields
        // based on the order type and parameters. FULL response additionally includes
        // the list of trades which immediately filled the order.
        "fills": [
            {
                "price": "23416.10000000",
                "qty": "0.00635000",
                "commission": "0.000000",
                "commissionAsset": "BNB",
                "tradeId": 1650422481
            },
            {
                "price": "23416.50000000",
                "qty": "0.00212000",
                "commission": "0.000000",
                "commissionAsset": "BNB",
                "tradeId": 1650422482
            }
        ]
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 1
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 1
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

<a id="conditional-fields-in-order-responses"></a>

**Conditional fields in Order Responses**

There are fields in the order responses (e.g. order placement, order query, order cancellation) that appear only if certain conditions are met.

These fields can apply to Order lists.

The fields are listed below:

Field          |Description                                                      |Visibility conditions                                           | Examples |
----           | -----                                                           | ---                                                            |---       |
`icebergQty`   | Quantity for the iceberg order | Appears only if the parameter `icebergQty` was sent in the request.| `"icebergQty": "0.00000000"`
`preventedMatchId` |  When used in combination with `symbol`, can be used to query a prevented match. | Appears only if the order expired due to STP.| `"preventedMatchId": 0`
`preventedQuantity` | Order quantity that expired due to STP | Appears only if the order expired due to STP. | `"preventedQuantity": "1.200000"`
`stopPrice`    | Price when the algorithmic order will be triggered | Appears for `STOP_LOSS`. `TAKE_PROFIT`, `STOP_LOSS_LIMIT` and `TAKE_PROFIT_LIMIT` orders.|`"stopPrice": "23500.00000000"`
`strategyId`   | Can be used to label an order that's part of an order strategy. |Appears if the parameter was populated in the request.| `"strategyId": 37463720`
`strategyType` | Can be used to label an order that is using an order strategy.|Appears if the parameter was populated in the request.| `"strategyType": 1000000`
`trailingDelta`| Delta price change required before order activation| Appears for Trailing Stop Orders.|`"trailingDelta": 10`
`trailingTime` | Time when the trailing order is now active and tracking price changes| Appears only for Trailing Stop Orders.| `"trailingTime": -1`
`usedSor`      | Field that determines whether order used SOR | Appears when placing orders using SOR|`"usedSor": true`
`workingFloor` | Field that determines whether the order is being filled by the SOR or by the order book the order was submitted to.|Appears when placing orders using SOR|`"workingFloor": "SOR"`
`pegPriceType` |  Price peg type  | Only for pegged orders  | `"pegPriceType": "PRIMARY_PEG"`
`pegOffsetType`| Price peg offset type | Only for pegged orders, if requested  | `"pegOffsetType": "PRICE_LEVEL"`
`pegOffsetValue` | Price peg offset value  | Only for pegged orders, if requested  | `"pegOffsetValue": 5`
`peggedPrice`  | Current price order is pegged at | Only for pegged orders, once determined | `"peggedPrice": "87523.83710000"`

### Test new order (TRADE)

```javascript
{
    "id": "6ffebe91-01d9-43ac-be99-57cf062e0e30",
    "method": "order.test",
    "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "price": "23416.10000000",
        "quantity": "0.00847000",
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "15af09e41c36f3cc61378c2fbe2c33719a03dd5eba8d0f9206fbda44de717c88",
        "timestamp": 1660801715431
    }
}
```

Test order placement.

Validates new order parameters and verifies your signature
but does not send the order into the matching engine.

**Weight:**

|Condition| Request Weight|
|------------           | ------------ |
|Without `computeCommissionRates`| 1|
|With `computeCommissionRates`|20|

**Parameters:**

In addition to all parameters accepted by [`order.place`](#place-new-order-trade),
the following optional parameters are also accepted:

Name                   |Type          | Mandatory    | Description
------------           | ------------ | ------------ | ------------
`computeCommissionRates` | BOOLEAN      | NO         | Default: `false` <br> See [Commissions FAQ](faqs/commission_faq.md#test-order-diferences) to learn more.


**Data Source:**
Memory

**Response:**

Without `computeCommissionRates`:

```javascript
{
    "id": "6ffebe91-01d9-43ac-be99-57cf062e0e30",
    "status": 200,
    "result": {},
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

With `computeCommissionRates`:

```javascript
{
    "id": "6ffebe91-01d9-43ac-be99-57cf062e0e30",
    "status": 200,
    "result": {
        "standardCommissionForOrder": {  // Standard commission rates on trades from the order.
            "maker": "0.00000112",
            "taker": "0.00000114"
        },
        "specialCommissionForOrder": {   // Special commission rates on trades from the order.
            "maker": "0.05000000",
            "taker": "0.06000000"
        },
        "taxCommissionForOrder": {       // Tax commission rates for trades from the order
            "maker": "0.00000112",
            "taker": "0.00000114"
        },
        "discount": {                    // Discount on standard commissions when paying in BNB.
            "enabledForAccount": true,
            "enabledForSymbol": true,
            "discountAsset": "BNB",
            "discount": "0.25000000"     // Standard commission is reduced by this rate when paying in BNB.
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 20
        }
    ]
}
```

### Cancel order (TRADE)

```javascript
{
    "id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",
    "method": "order.cancel",
    "params": {
        "symbol": "BTCUSDT",
        "origClientOrderId": "4d96324ff9d44481926157",
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "33d5b721f278ae17a52f004a82a6f68a70c68e7dd6776ed0be77a455ab855282",
        "timestamp": 1660801715830
    }
}
```

Cancel an active order.

**Weight:**
1

**Parameters:**

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>symbol</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>orderId</code></td>
        <td>LONG</td>
        <td rowspan="2">YES</td>
        <td>Cancel order by <code>orderId</code></td>
    </tr>
    <tr>
        <td><code>origClientOrderId</code></td>
        <td>STRING</td>
        <td>Cancel order by <code>clientOrderId</code></td>
    </tr>
    <tr>
        <td><code>newClientOrderId</code></td>
        <td>STRING</td>
        <td>NO</td>
        <td>New ID for the canceled order. Automatically generated if not sent</td>
    </tr>
    <tr>
      <td><code>cancelRestrictions</code></td>
      <td>ENUM</td>
      <td>NO</td>
      <td>Supported values: <br><code>ONLY_NEW</code> - Cancel will succeed if the order status is <code>NEW</code>.<br> <code>ONLY_PARTIALLY_FILLED</code> - Cancel will succeed if order status is <code>PARTIALLY_FILLED</code>.</td>
    </tr>
    <tr>
        <td><code>apiKey</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>recvWindow</code></td>
        <td>DECIMAL</td>
        <td>NO</td>
        <td>The value cannot be greater than <tt>60000</tt>.<br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.</td>
    </tr>
    <tr>
        <td><code>signature</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>timestamp</code></td>
        <td>LONG</td>
        <td>YES</td>
        <td></td>
    </tr>
</tbody>
</table>

Notes:

* If both `orderId` and `origClientOrderId` parameters are provided, the `orderId` is searched first, then the `origClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.

* `newClientOrderId` will replace `clientOrderId` of the canceled order, freeing it up for new orders.

* If you cancel an order that is a part of an order list, the entire order list is canceled.

* The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only `orderId` is sent. Sending `origClientOrderId` or both `orderId` + `origClientOrderId` will be slower.

**Data Source:**
Matching Engine

**Response:**

When an individual order is canceled:

```javascript
{
    "id": "5633b6a2-90a9-4192-83e7-925c90b6a2fd",
    "status": 200,
    "result": {
        "symbol": "BTCUSDT",
        "origClientOrderId": "4d96324ff9d44481926157",     // clientOrderId that was canceled
        "orderId": 12569099453,
        "orderListId": -1,                                 // set only for legs of an order list
        "clientOrderId": "91fe37ce9e69c90d6358c0",         // newClientOrderId from request
        "transactTime": 1684804350068,
        "price": "23416.10000000",
        "origQty": "0.00847000",
        "executedQty": "0.00001000",
        "origQuoteOrderQty": "0.000000",
        "cummulativeQuoteQty": "0.23416100",
        "status": "CANCELED",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "SELL",
        "stopPrice": "0.00000000",                         // present only if stopPrice set for the order
        "trailingDelta": 0,                                // present only if trailingDelta set for the order
        "icebergQty": "0.00000000",                        // present only if icebergQty set for the order
        "strategyId": 37463720,                            // present only if strategyId set for the order
        "strategyType": 1000000,                           // present only if strategyType set for the order
        "selfTradePreventionMode": "NONE"
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

When an order list is canceled:

```javascript
{
    "id": "16eaf097-bbec-44b9-96ff-e97e6e875870",
    "status": 200,
    "result": {
        "orderListId": 19431,
        "contingencyType": "OCO",
        "listStatusType": "ALL_DONE",
        "listOrderStatus": "ALL_DONE",
        "listClientOrderId": "iuVNVJYYrByz6C4yGOPPK0",
        "transactionTime": 1660803702431,
        "symbol": "BTCUSDT",
        "orders": [
            {
                "symbol": "BTCUSDT",
                "orderId": 12569099453,
                "clientOrderId": "bX5wROblo6YeDwa9iTLeyY"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 12569099454,
                "clientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW"
            }
        ],
        // order list order's status format is the same as for individual orders.
        "orderReports": [
            {
                "symbol": "BTCUSDT",
                "origClientOrderId": "bX5wROblo6YeDwa9iTLeyY",
                "orderId": 12569099453,
                "orderListId": 19431,
                "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",
                "transactTime": 1684804350068,
                "price": "23450.50000000",
                "origQty": "0.00850000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "CANCELED",
                "timeInForce": "GTC",
                "type": "STOP_LOSS_LIMIT",
                "side": "BUY",
                "stopPrice": "23430.00000000",
                "selfTradePreventionMode": "NONE"
            },
            {
                "symbol": "BTCUSDT",
                "origClientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW",
                "orderId": 12569099454,
                "orderListId": 19431,
                "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",
                "transactTime": 1684804350068,
                "price": "23400.00000000",
                "origQty": "0.00850000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "CANCELED",
                "timeInForce": "GTC",
                "type": "LIMIT_MAKER",
                "side": "BUY",
                "selfTradePreventionMode": "NONE"
            }
        ]
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

<a id="regarding-cancelrestrictions"></a>

**Regarding `cancelRestrictions`**

* If the `cancelRestrictions` value is not any of the supported values, the error will be:
```json
{
    "code": -1145,
    "msg": "Invalid cancelRestrictions"
}
```
* If the order did not pass the conditions for `cancelRestrictions`, the error will be:
```json
{
    "code": -2011,
    "msg": "Order was not canceled due to cancel restrictions."
}
```

### Cancel and replace order (TRADE)

```javascript
{
    "id": "99de1036-b5e2-4e0f-9b5c-13d751c93a1a",
    "method": "order.cancelReplace",
    "params": {
        "symbol": "BTCUSDT",
        "cancelReplaceMode": "ALLOW_FAILURE",
        "cancelOrigClientOrderId": "4d96324ff9d44481926157",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "price": "23416.10000000",
        "quantity": "0.00847000",
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "7028fdc187868754d25e42c37ccfa5ba2bab1d180ad55d4c3a7e2de643943dc5",
        "timestamp": 1660813156900
    }
}
```

Cancel an existing order and immediately place a new order instead of the canceled one.

A new order that was not attempted (i.e. when `newOrderResult: NOT_ATTEMPTED`), will still increase the unfilled order count by 1.

**Weight:**
1

**Unfilled Order Count:**
1

**Parameters:**

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>symbol</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>cancelReplaceMode</code></td>
        <td>ENUM</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>cancelOrderId</code></td>
        <td>LONG</td>
        <td rowspan="2">YES</td>
        <td>Cancel order by <code>orderId</code></td>
    </tr>
    <tr>
        <td><code>cancelOrigClientOrderId</code></td>
        <td>STRING</td>
        <td>Cancel order by <code>clientOrderId</code></td>
    </tr>
    <tr>
        <td><code>cancelNewClientOrderId</code></td>
        <td>STRING</td>
        <td>NO</td>
        <td>New ID for the canceled order. Automatically generated if not sent</td>
    </tr>
    <tr>
        <td><code>side</code></td>
        <td>ENUM</td>
        <td>YES</td>
        <td><code>BUY</code> or <code>SELL</code></td>
    </tr>
    <tr>
        <td><code>type</code></td>
        <td>ENUM</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>timeInForce</code></td>
        <td>ENUM</td>
        <td>NO *</td>
        <td></td>
    </tr>
    <tr>
        <td><code>price</code></td>
        <td>DECIMAL</td>
        <td>NO *</td>
        <td></td>
    </tr>
    <tr>
        <td><code>quantity</code></td>
        <td>DECIMAL</td>
        <td>NO *</td>
        <td></td>
    </tr>
    <tr>
        <td><code>quoteOrderQty</code></td>
        <td>DECIMAL</td>
        <td>NO *</td>
        <td></td>
    </tr>
    <tr>
        <td><code>newClientOrderId</code></td>
        <td>STRING</td>
        <td>NO</td>
        <td>Arbitrary unique ID among open orders. Automatically generated if not sent</td>
    </tr>
    <tr>
        <td><code>newOrderRespType</code></td>
        <td>ENUM</td>
        <td>NO</td>
        <td>
            <p>Select response format: <code>ACK</code>, <code>RESULT</code>, <code>FULL</code>.</p>
            <p>
                <code>MARKET</code> and <code>LIMIT</code> orders produce <code>FULL</code> response by default,
                other order types default to <code>ACK</code>.
            </p>
        </td>
    </tr>
    <tr>
        <td><code>stopPrice</code></td>
        <td>DECIMAL</td>
        <td>NO *</td>
        <td></td>
    </tr>
    <tr>
        <td><code>trailingDelta</code></td>
        <td>DECIMAL</td>
        <td>NO *</td>
        <td>See <a href="faqs/trailing-stop-faq.md">Trailing Stop order FAQ</a></td>
    </tr>
    <tr>
        <td><code>icebergQty</code></td>
        <td>DECIMAL</td>
        <td>NO</td>
        <td></td>
    </tr>
    <tr>
        <td><code>strategyId</code></td>
        <td>LONG</td>
        <td>NO</td>
        <td>Arbitrary numeric value identifying the order within an order strategy.</td>
    </tr>
    <tr>
        <td><code>strategyType</code></td>
        <td>INT</td>
        <td>NO</td>
        <td>
            <p>Arbitrary numeric value identifying the order strategy.</p>
            <p>Values smaller than <tt>1000000</tt> are reserved and cannot be used.</p>
        </td>
    </tr>
    <tr>
        <td><code>selfTradePreventionMode</code></td>
        <td>ENUM</td>
        <td>NO</td>
        <td>
            <p>The allowed enums is dependent on what is configured on the symbol.</p>
            <p>Supported values: <a href="enums.md#stpmodes">STP Modes</a>.</p>
        </td>
    </tr>
    <tr>
      <td><code>cancelRestrictions</code></td>
      <td>ENUM</td>
      <td>NO</td>
      <td>Supported values: <br><code>ONLY_NEW</code> - Cancel will succeed if the order status is <code>NEW</code>.<br> <code>ONLY_PARTIALLY_FILLED</code> - Cancel will succeed if order status is <code>PARTIALLY_FILLED</code>. For more information please refer to <a href="#regarding-cancelrestrictions">Regarding <code>cancelRestrictions</code></a>.</td>
    </tr>
    <tr>
        <td><code>apiKey</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>orderRateLimitExceededMode</code></td>
        <td>ENUM</td>
        <td>NO</td>
        <td>Supported values: <br> <code>DO_NOTHING</code> (default)- will only attempt to cancel the order if account has not exceeded the unfilled order rate limit<br> <code>CANCEL_ONLY</code> - will always cancel the order.</td>
    </tr>
    <tr>
        <td><code>pegPriceType</code></td>
        <td>ENUM</td>
        <td>NO</td>
        <td><code>PRIMARY_PEG</code> or <code>MARKET_PEG</code>. <br>See <a href="#pegged-orders-info">Pegged Orders</a>"</td>
    </tr>
    <tr>
        <td><code>pegOffsetValue</code></td>
        <td>INT</td>
        <td>NO</td>
        <td>Price level to peg the price to (max: 100) <br> See <a href="#pegged-orders-info">Pegged Orders</a></td>
    </tr>
    <tr>
        <td><code>pegOffsetType</code></td>
        <td>ENUM</td>
        <td>NO</td>
        <td>Only <code>PRICE_LEVEL</code> is supported<br>See <a href="#pegged-orders-info">Pegged Orders</a></td>
    </tr>
    <tr>
        <td><code>recvWindow</code></td>
        <td>DECIMAL</td>
        <td>NO</td>
        <td>The value cannot be greater than <tt>60000</tt>.<br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.</td>
    </tr>
    <tr>
        <td><code>signature</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>timestamp</code></td>
        <td>LONG</td>
        <td>YES</td>
        <td></td>
    </tr>
</tbody>
</table>

Similar to the [`order.place`](#place-new-order-trade) request,
additional mandatory parameters (*) are determined by the new order [`type`](#order-type).

Available `cancelReplaceMode` options:

* `STOP_ON_FAILURE` – if cancellation request fails, new order placement will not be attempted.
* `ALLOW_FAILURE` – new order placement will be attempted even if the cancel request fails.

<table>
<thead>
    <tr>
        <th colspan=3 align=left>Request</th>
        <th colspan=3 align=left>Response</th>
    </tr>
    <tr>
        <th><code>cancelReplaceMode</code></th>
        <th><code>orderRateLimitExceededMode</code></th>
        <th>Unfilled Order Count</th>
        <th><code>cancelResult</code></th>
        <th><code>newOrderResult</code></th>
        <th><code>status</code></th>
    </tr>
</thead>
<tbody>
    <tr>
        <td rowspan="11"><code>STOP_ON_FAILURE</code></td>
        <td rowspan="6"><code>DO_NOTHING</code></td>
        <td rowspan="3">Within Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>200</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>➖ <code>NOT_ATTEMPTED</code></td>
        <td align=right><code>400</code></td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
        <td rowspan="3">Exceeds Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>➖ <code>NOT_ATTEMPTED</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right>N/A</td>
    </tr>
     <tr>
        <td rowspan="5"><code>CANCEL_ONLY</code></td>
        <td rowspan="3">Within Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>200</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>➖ <code>NOT_ATTEMPTED</code></td>
        <td align=right><code>400</code></td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
        <td rowspan="2">Exceeds Limits</td>
        <td>❌ <code>FAILURE</code></td>
        <td>➖ <code>NOT_ATTEMPTED</code></td>
        <td align=right><code>429</code></td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>429</code></td>
    </tr>
    <tr>
        <td rowspan="16"><code>ALLOW_FAILURE</code></td>
        <td rowspan="8"><code>DO_NOTHING</code></td>
        <td rowspan="4">Within Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>200</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>400</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
     <td rowspan="4">Exceeds Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td rowspan="8"><CODE>CANCEL_ONLY</CODE></td>
        <td rowspan="4">Within Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>200</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>400</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>409</code></td>
    </tr>
    <tr>
        <td rowspan="4">Exceeds Limits</td>
        <td>✅ <code>SUCCESS</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right><code>200</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>400</code></td>
    </tr>
    <tr>
        <td>❌ <code>FAILURE</code></td>
        <td>✅ <code>SUCCESS</code></td>
        <td align=right>N/A</td>
    </tr>
    <tr>
        <td>✅ <code>SUCCESS</code></td>
        <td>❌ <code>FAILURE</code></td>
        <td align=right><code>409</code></td>
    </tr>
</tbody>
</table>

Notes:

* If both `cancelOrderId` and `cancelOrigClientOrderId` parameters are provided, the `cancelOrderId` is searched first, then the `cancelOrigClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.

* `cancelNewClientOrderId` will replace `clientOrderId` of the canceled order, freeing it up for new orders.

* `newClientOrderId` specifies `clientOrderId` value for the placed order.

  A new order with the same `clientOrderId` is accepted only when the previous one is filled or expired.

  The new order can reuse old `clientOrderId` of the canceled order.

* This cancel-replace operation is **not transactional**.

  If one operation succeeds but the other one fails, the successful operation is still executed.

  For example, in `STOP_ON_FAILURE` mode, if the new order placement fails, the old order is still canceled.

* Filters and order count limits are evaluated before cancellation and order placement occurs.

* If new order placement is not attempted, your order count is still incremented.

* Like [`order.cancel`](#cancel-order-trade), if you cancel an individual order from an order list, the entire order list is canceled.

* The performance for canceling an order (single cancel or as part of a cancel-replace) is always better when only `orderId` is sent. Sending `origClientOrderId` or both `orderId` + `origClientOrderId` will be slower.

**Data Source:**
Matching Engine

**Response:**

If both cancel and placement succeed, you get the following response with `"status": 200`:

```javascript
{
    "id": "99de1036-b5e2-4e0f-9b5c-13d751c93a1a",
    "status": 200,
    "result": {
        "cancelResult": "SUCCESS",
        "newOrderResult": "SUCCESS",
        // Format is identical to "order.cancel" format.
        // Some fields are optional and are included only for orders that set them.
        "cancelResponse": {
            "symbol": "BTCUSDT",
            "origClientOrderId": "4d96324ff9d44481926157",     // cancelOrigClientOrderId from request
            "orderId": 125690984230,
            "orderListId": -1,
            "clientOrderId": "91fe37ce9e69c90d6358c0",         // cancelNewClientOrderId from request
            "transactTime": 1684804350068,
            "price": "23450.00000000",
            "origQty": "0.00847000",
            "executedQty": "0.00001000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "0.23450000",
            "status": "CANCELED",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "SELL",
            "selfTradePreventionMode": "NONE"
        },
        // Format is identical to "order.place" format, affected by "newOrderRespType".
        // Some fields are optional and are included only for orders that set them.
        "newOrderResponse": {
            "symbol": "BTCUSDT",
            "orderId": 12569099453,
            "orderListId": -1,
            "clientOrderId": "bX5wROblo6YeDwa9iTLeyY",         // newClientOrderId from request
            "transactTime": 1660813156959,
            "price": "23416.10000000",
            "origQty": "0.00847000",
            "executedQty": "0.00000000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "0.00000000",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "SELL",
            "selfTradePreventionMode": "NONE"
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 1
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 1
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

In `STOP_ON_FAILURE` mode, failed order cancellation prevents new order from being placed
and returns the following response with `"status": 400`:

```javascript
{
    "id": "27e1bf9f-0539-4fb0-85c6-06183d36f66c",
    "status": 400,
    "error": {
        "code": -2022,
        "msg": "Order cancel-replace failed.",
        "data": {
            "cancelResult": "FAILURE",
            "newOrderResult": "NOT_ATTEMPTED",
            "cancelResponse": {
                "code": -2011,
                "msg": "Unknown order sent."
            },
            "newOrderResponse": null
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 1
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 1
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

If cancel-replace mode allows failure and one of the operations fails,
you get a response with `"status": 409`,
and the `"data"` field detailing which operation succeeded, which failed, and why:

```javascript
{
    "id": "b220edfe-f3c4-4a3a-9d13-b35473783a25",
    "status": 409,
    "error": {
        "code": -2021,
        "msg": "Order cancel-replace partially failed.",
        "data": {
            "cancelResult": "SUCCESS",
            "newOrderResult": "FAILURE",
            "cancelResponse": {
                "symbol": "BTCUSDT",
                "origClientOrderId": "4d96324ff9d44481926157",
                "orderId": 125690984230,
                "orderListId": -1,
                "clientOrderId": "91fe37ce9e69c90d6358c0",
                "transactTime": 1684804350068,
                "price": "23450.00000000",
                "origQty": "0.00847000",
                "executedQty": "0.00001000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.23450000",
                "status": "CANCELED",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "SELL",
                "selfTradePreventionMode": "NONE"
            },
            "newOrderResponse": {
                "code": -2010,
                "msg": "Order would immediately match and take."
            }
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 1
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 1
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

```javascript
{
    "id": "ce641763-ff74-41ac-b9f7-db7cbe5e93b1",
    "status": 409,
    "error": {
        "code": -2021,
        "msg": "Order cancel-replace partially failed.",
        "data": {
            "cancelResult": "FAILURE",
            "newOrderResult": "SUCCESS",
            "cancelResponse": {
                "code": -2011,
                "msg": "Unknown order sent."
            },
            "newOrderResponse": {
                "symbol": "BTCUSDT",
                "orderId": 12569099453,
                "orderListId": -1,
                "clientOrderId": "bX5wROblo6YeDwa9iTLeyY",
                "transactTime": 1660813156959,
                "price": "23416.10000000",
                "origQty": "0.00847000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "NEW",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "SELL",
                "workingTime": 1669693344508,
                "fills": [],
                "selfTradePreventionMode": "NONE"
            }
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 1
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 1
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

If both operations fail, response will have `"status": 400`:

```javascript
{
    "id": "3b3ac45c-1002-4c7d-88e8-630c408ecd87",
    "status": 400,
    "error": {
        "code": -2022,
        "msg": "Order cancel-replace failed.",
        "data": {
            "cancelResult": "FAILURE",
            "newOrderResult": "FAILURE",
            "cancelResponse": {
                "code": -2011,
                "msg": "Unknown order sent."
            },
            "newOrderResponse": {
                "code": -2010,
                "msg": "Order would immediately match and take."
            }
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 1
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 1
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

If `orderRateLimitExceededMode` is `DO_NOTHING` regardless of `cancelReplaceMode`, and you have exceeded your unfilled order count, you will get status `429` with the following error:

```javascript
{
    "id": "3b3ac45c-1002-4c7d-88e8-630c408ecd87",
    "status": 429,
    "error": {
        "code": -1015,
        "msg": "Too many new orders; current limit is 50 orders per 10 SECOND."
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 50
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 50
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

If `orderRateLimitExceededMode` is `CANCEL_ONLY` regardless of `cancelReplaceMode`, and you have exceeded your unfilled order count, you will get status `409` with the following error:

```javascript
{
    "id": "3b3ac45c-1002-4c7d-88e8-630c408ecd87",
    "status": 409,
    "error": {
        "code": -2021,
        "msg": "Order cancel-replace partially failed.",
        "data": {
            "cancelResult": "SUCCESS",
            "newOrderResult": "FAILURE",
            "cancelResponse": {
                "symbol": "LTCBNB",
                "origClientOrderId": "GKt5zzfOxRDSQLveDYCTkc",
                "orderId": 64,
                "orderListId": -1,
                "clientOrderId": "loehOJF3FjoreUBDmv739R",
                "transactTime": 1715779007228,
                "price": "1.00",
                "origQty": "10.00000000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.00",
                "status": "CANCELED",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "SELL",
                "selfTradePreventionMode": "NONE"
            },
            "newOrderResponse": {
                "code": -1015,
                "msg": "Too many new orders; current limit is 50 orders per 10 SECOND."
            }
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 50
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 50
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

### Order Amend Keep Priority (TRADE)

```javascript
{
    "id": "56374a46-3061-486b-a311-89ee972eb648",
    "method": "order.amend.keepPriority",
    "params": {
        "newQty": "5",
        "origClientOrderId": "my_test_order1",
        "recvWindow": 5000,
        "symbol": "BTCUSDT",
        "timestamp": 1741922620419,
        "apiKey": "Rl1KOMDCpSg6xviMYOkNk9ENUB5QOTnufXukVe0Ijd40yduAlpHn78at3rJyJN4F",
        "signature": "fa49c0c4ebc331c6ebd3fcb20deb387f60081ea858eebe6e35aa6fcdf2a82e08"
    }
}
```

Reduce the quantity of an existing open order.

This adds 0 orders to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [Order Amend Keep Priority FAQ](faqs/order_amend_keep_priority.md) to learn more.

**Weight**: 4

**Unfilled Order Count:**
0

**Parameters:**

Name | Type | Mandatory | Description |
:---- | :---- | :---- | :---- |
symbol | STRING | YES |  |
orderId | LONG | NO\* | `orderId` or `origClientOrderId` must be sent  |
origClientOrderId | STRING | NO\* | `orderId` or `origClientOrderId` must be sent  |
newClientOrderId | STRING | NO\* | The new client order ID for the order after being amended. <br> If not sent, one will be randomly generated. <br> It is possible to reuse the current clientOrderId by sending it as the `newClientOrderId`. |
newQty | DECIMAL | YES | `newQty` must be greater than 0 and less than the order's quantity. |
recvWindow | DECIMAL | NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |

**Data Source**:
Matching Engine

**Response:**

Response for a single order:

```javascript
{
    "id": "56374a46-3061-486b-a311-89ee972eb648",
    "status": 200,
    "result": {
        "transactTime": 1741923284382,
        "executionId": 16,
        "amendedOrder": {
            "symbol": "BTCUSDT",
            "orderId": 12,
            "orderListId": -1,
            "origClientOrderId": "my_test_order1",
            "clientOrderId": "4zR9HFcEq8gM1tWUqPEUHc",
            "price": "5.00000000",
            "qty": "5.00000000",
            "executedQty": "0.00000000",
            "preventedQty": "0.00000000",
            "quoteOrderQty": "0.00000000",
            "cumulativeQuoteQty": "0.00000000",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "BUY",
            "workingTime": 1741923284364,
            "selfTradePreventionMode": "NONE"
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

Response for an order which is part of an Order list:

```javascript
{
    "id": "56374b46-3061-486b-a311-89ee972eb648",
    "status": 200,
    "result": {
        "transactTime": 1741924229819,
        "executionId": 60,
        "amendedOrder": {
            "symbol": "BTUCSDT",
            "orderId": 23,
            "orderListId": 4,
            "origClientOrderId": "my_pending_order",
            "clientOrderId": "xbxXh5SSwaHS7oUEOCI88B",
            "price": "1.00000000",
            "qty": "5.00000000",
            "executedQty": "0.00000000",
            "preventedQty": "0.00000000",
            "quoteOrderQty": "0.00000000",
            "cumulativeQuoteQty": "0.00000000",
            "status": "NEW",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "BUY",
            "workingTime": 1741924204920,
            "selfTradePreventionMode": "NONE"
        },
        "listStatus": {
            "orderListId": 4,
            "contingencyType": "OTO",
            "listOrderStatus": "EXECUTING",
            "listClientOrderId": "8nOGLLawudj1QoOiwbroRH",
            "symbol": "BTCUSDT",
            "orders": [
                {
                    "symbol": "BTCUSDT",
                    "orderId": 22,
                    "clientOrderId": "g04EWsjaackzedjC9wRkWD"
                },
                {
                    "symbol": "BTCUSDT",
                    "orderId": 23,
                    "clientOrderId": "xbxXh5SSwaHS7oUEOCI88B"
                }
            ]
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

**Note:** The payloads above do not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).


### Cancel open orders (TRADE)

```javascript
{
    "id": "778f938f-9041-4b88-9914-efbf64eeacc8",
    "method": "openOrders.cancelAll",
    "params": {
        "symbol": "BTCUSDT",
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "773f01b6e3c2c9e0c1d217bc043ce383c1ddd6f0e25f8d6070f2b66a6ceaf3a5",
        "timestamp": 1660805557200
    }
}
```

Cancel all open orders on a symbol.
This includes orders that are part of an order list.

**Weight:**
1

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`symbol`            | STRING  | YES       |
`apiKey`            | STRING  | YES       |
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |
`timestamp`         | LONG    | YES       |

**Data Source:**
Matching Engine

**Response:**

Cancellation reports for orders and order lists have the same format as in [`order.cancel`](#cancel-order-trade).

```javascript
{
    "id": "778f938f-9041-4b88-9914-efbf64eeacc8",
    "status": 200,
    "result": [
        {
            "symbol": "BTCUSDT",
            "origClientOrderId": "4d96324ff9d44481926157",
            "orderId": 12569099453,
            "orderListId": -1,
            "clientOrderId": "91fe37ce9e69c90d6358c0",
            "transactTime": 1684804350068,
            "price": "23416.10000000",
            "origQty": "0.00847000",
            "executedQty": "0.00001000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "0.23416100",
            "status": "CANCELED",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "SELL",
            "stopPrice": "0.00000000",
            "trailingDelta": 0,
            "trailingTime": -1,
            "icebergQty": "0.00000000",
            "strategyId": 37463720,
            "strategyType": 1000000,
            "selfTradePreventionMode": "NONE"
        },
        {
            "orderListId": 19431,
            "contingencyType": "OCO",
            "listStatusType": "ALL_DONE",
            "listOrderStatus": "ALL_DONE",
            "listClientOrderId": "iuVNVJYYrByz6C4yGOPPK0",
            "transactionTime": 1660803702431,
            "symbol": "BTCUSDT",
            "orders": [
                {
                    "symbol": "BTCUSDT",
                    "orderId": 12569099453,
                    "clientOrderId": "bX5wROblo6YeDwa9iTLeyY"
                },
                {
                    "symbol": "BTCUSDT",
                    "orderId": 12569099454,
                    "clientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW"
                }
            ],
            "orderReports": [
                {
                    "symbol": "BTCUSDT",
                    "origClientOrderId": "bX5wROblo6YeDwa9iTLeyY",
                    "orderId": 12569099453,
                    "orderListId": 19431,
                    "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",
                    "transactTime": 1684804350068,
                    "price": "23450.50000000",
                    "origQty": "0.00850000",
                    "executedQty": "0.00000000",
                    "origQuoteOrderQty": "0.000000",
                    "cummulativeQuoteQty": "0.00000000",
                    "status": "CANCELED",
                    "timeInForce": "GTC",
                    "type": "STOP_LOSS_LIMIT",
                    "side": "BUY",
                    "stopPrice": "23430.00000000",
                    "selfTradePreventionMode": "NONE"
                },
                {
                    "symbol": "BTCUSDT",
                    "origClientOrderId": "Tnu2IP0J5Y4mxw3IATBfmW",
                    "orderId": 12569099454,
                    "orderListId": 19431,
                    "clientOrderId": "OFFXQtxVFZ6Nbcg4PgE2DA",
                    "transactTime": 1684804350068,
                    "price": "23400.00000000",
                    "origQty": "0.00850000",
                    "executedQty": "0.00000000",
                    "origQuoteOrderQty": "0.000000",
                    "cummulativeQuoteQty": "0.00000000",
                    "status": "CANCELED",
                    "timeInForce": "GTC",
                    "type": "LIMIT_MAKER",
                    "side": "BUY",
                    "selfTradePreventionMode": "NONE"
                }
            ]
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

### Order lists

#### Place new OCO - Deprecated (TRADE)

```javascript
{
    "id": "56374a46-3061-486b-a311-99ee972eb648",
    "method": "orderList.place",
    "params": {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "price": "23420.00000000",
        "quantity": "0.00650000",
        "stopPrice": "23410.00000000",
        "stopLimitPrice": "23405.00000000",
        "stopLimitTimeInForce": "GTC",
        "newOrderRespType": "RESULT",
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "6689c2a36a639ff3915c2904871709990ab65f3c7a9ff13857558fd350315c35",
        "timestamp": 1660801713767
    }
}
```

Send in a new one-cancels-the-other (OCO) pair:
`LIMIT_MAKER` + `STOP_LOSS`/`STOP_LOSS_LIMIT` orders (called *legs*),
where activation of one order immediately cancels the other.

This adds 1 order to `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter

**Weight:**
1

**Unfilled Order Count:**
1

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`symbol`            | STRING  | YES       |
`side`              | ENUM    | YES       | `BUY` or `SELL`
`price`             | DECIMAL | YES       | Price for the limit order
`quantity`          | DECIMAL | YES       |
`listClientOrderId` | STRING  | NO        | Arbitrary unique ID among open order lists. Automatically generated if not sent
`limitClientOrderId`| STRING  | NO        | Arbitrary unique ID among open orders for the limit order. Automatically generated if not sent
`limitIcebergQty`   | DECIMAL | NO        |
`limitStrategyId`   | LONG     | NO        | Arbitrary numeric value identifying the limit order within an order strategy.
`limitStrategyType` | INT     | NO        | <p>Arbitrary numeric value identifying the limit order strategy.</p><p>Values smaller than `1000000` are reserved and cannot be used.</p>
`stopPrice`         | DECIMAL | YES *     | Either `stopPrice` or `trailingDelta`, or both must be specified
`trailingDelta`     | INT     | YES *     | See [Trailing Stop order FAQ](faqs/trailing-stop-faq.md)
`stopClientOrderId` | STRING  | NO        | Arbitrary unique ID among open orders for the stop order. Automatically generated if not sent
`stopLimitPrice`    | DECIMAL | NO *      |
`stopLimitTimeInForce` | ENUM | NO *      | See [`order.place`](#timeInForce) for available options
`stopIcebergQty`    | DECIMAL | NO *      |
`stopStrategyId`    | LONG     | NO        | Arbitrary numeric value identifying the stop order within an order strategy.
`stopStrategyType`  | INT     | NO        | <p>Arbitrary numeric value identifying the stop order strategy.</p><p>Values smaller than `1000000` are reserved and cannot be used.</p>
`newOrderRespType`  | ENUM    | NO        | Select response format: `ACK`, `RESULT`, `FULL` (default)
`selfTradePreventionMode` |ENUM | NO      | The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](./enums.md#stpmodes)
`apiKey`            | STRING  | YES       |
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |
`timestamp`         | LONG    | YES       |

Notes:

* `listClientOrderId` parameter specifies `listClientOrderId` for the OCO pair.

  A new OCO with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired.

  `listClientOrderId` is distinct from `clientOrderId` of individual orders.

* `limitClientOrderId` and `stopClientOrderId` specify `clientOrderId` values for both legs of the OCO.

  A new order with the same `clientOrderId` is accepted only when the previous one is filled or expired.

* Price restrictions on the legs:

  | `side` | Price relation |
  | ------ | -------------- |
  | `BUY`  | `price` < market price < `stopPrice` |
  | `SELL` | `price` > market price > `stopPrice` |

* Both legs have the same `quantity`.

  However, you can set different iceberg quantity for individual legs.

  If `stopIcebergQty` is used, `stopLimitTimeInForce` must be `GTC`.

* `trailingDelta` applies only to the `STOP_LOSS`/`STOP_LOSS_LIMIT` leg of the OCO.

**Data Source:**
Matching Engine

**Response:**

Response format for `orderReports` is selected using the `newOrderRespType` parameter.
The following example is for `RESULT` response type.
See [`order.place`](#place-new-order-trade) for more examples.

```javascript
{
    "id": "57833dc0-e3f2-43fb-ba20-46480973b0aa",
    "status": 200,
    "result": {
        "orderListId": 1274512,
        "contingencyType": "OCO",
        "listStatusType": "EXEC_STARTED",
        "listOrderStatus": "EXECUTING",
        "listClientOrderId": "08985fedd9ea2cf6b28996",
        "transactionTime": 1660801713793,
        "symbol": "BTCUSDT",
        "orders": [
            {
                "symbol": "BTCUSDT",
                "orderId": 12569138901,
                "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 12569138902,
                "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"
            }
        ],
        "orderReports": [
            {
                "symbol": "BTCUSDT",
                "orderId": 12569138901,
                "orderListId": 1274512,
                "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU",
                "transactTime": 1660801713793,
                "price": "23410.00000000",
                "origQty": "0.00650000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "NEW",
                "timeInForce": "GTC",
                "type": "STOP_LOSS_LIMIT",
                "side": "SELL",
                "stopPrice": "23405.00000000",
                "workingTime": -1,
                "selfTradePreventionMode": "NONE"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 12569138902,
                "orderListId": 1274512,
                "clientOrderId": "jLnZpj5enfMXTuhKB1d0us",
                "transactTime": 1660801713793,
                "price": "23420.00000000",
                "origQty": "0.00650000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "NEW",
                "timeInForce": "GTC",
                "type": "LIMIT_MAKER",
                "side": "SELL",
                "workingTime": 1660801713793,
                "selfTradePreventionMode": "NONE"
            }
        ]
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 2
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 2
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

#### Place new Order list - OCO (TRADE)

```javascript
{
    "id": "56374a46-3261-486b-a211-99ed972eb648",
    "method": "orderList.place.oco",
    "params": {
        "symbol": "LTCBNB",
        "side": "BUY",
        "quantity": 1,
        "timestamp": 1711062760647,
        "aboveType": "STOP_LOSS_LIMIT",
        "abovePrice": "1.5",
        "aboveStopPrice": "1.50000001",
        "aboveTimeInForce": "GTC",
        "belowType": "LIMIT_MAKER",
        "belowPrice": "1.49999999",
        "apiKey": "duwNf97YPLqhFIk7kZF0dDdGYVAXStA7BeEz0fIT9RAhUbixJtyS6kJ3hhzJsRXC",
        "signature": "64614cfd8dd38260d4fd86d3c455dbf4b9d1c8a8170ea54f700592a986c30ddb"
    }
}
```

Send in an one-cancels-the-other (OCO) pair, where activation of one order immediately cancels the other.

* An OCO has 2 orders called the **above order** and **below order**.
* One of the orders must be a `LIMIT_MAKER/TAKE_PROFIT/TAKE_PROFIT_LIMIT` order and the other must be `STOP_LOSS` or `STOP_LOSS_LIMIT` order.
* Price restrictions:
  * If the OCO is on the `SELL` side:
    * `LIMIT_MAKER/TAKE_PROFIT_LIMIT` `price` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
    * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
  * If the OCO is on the `BUY` side:
    * `LIMIT_MAKER` `price` < Last Traded Price < `STOP_LOSS/STOP_LOSS_LIMIT` `stopPrice`
    * `TAKE_PROFIT stopPrice` > Last Traded Price > `STOP_LOSS/STOP_LOSS_LIMIT stopPrice`
* OCOs add **2 orders** to the `EXCHANGE_MAX_ORDERS` filter and `MAX_NUM_ORDERS` filter.

**Weight:**
1

**Unfilled Order Count:**
2

**Parameters:**

Name                     |Type    | Mandatory | Description
-----                    |------  | -----     |----
`symbol`                 |STRING  |YES        |
`listClientOrderId`      |STRING  |NO         |Arbitrary unique ID among open order lists. Automatically generated if not sent. <br> A new order list with the same `listClientOrderId` is accepted only when the previous one is filled or completely expired. <br> `listClientOrderId` is distinct from the `aboveClientOrderId` and the `belowCLientOrderId`.
`side`                   |ENUM    |YES        |`BUY` or `SELL`
`quantity`               |DECIMAL |YES        |Quantity for both orders of the order list.
`aboveType`              |ENUM    |YES        |Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`
`aboveClientOrderId`     |STRING  |NO         |Arbitrary unique ID among open orders for the above order. Automatically generated if not sent
`aboveIcebergQty`        |LONG    |NO         |Note that this can only be used if `aboveTimeInForce` is `GTC`.
`abovePrice`             |DECIMAL |NO         |Can be used if `aboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.
`aboveStopPrice`         |DECIMAL |NO         |Can be used if `aboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`. <br>Either `aboveStopPrice` or `aboveTrailingDelta` or both, must be specified.
`aboveTrailingDelta`     |LONG    |NO         |See [Trailing Stop order FAQ](faqs/trailing-stop-faq.md).
`aboveTimeInForce`       |ENUM    |NO         |Required if `aboveType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`.
`aboveStrategyId`        |LONG    |NO         |Arbitrary numeric value identifying the above order within an order strategy.
`aboveStrategyType`      |INT     |NO         |Arbitrary numeric value identifying the above order strategy. <br>Values smaller than 1000000 are reserved and cannot be used.
`abovePegPriceType`      |ENUM    |NO         |See [Pegged Orders](#pegged-orders-info)
`abovePegOffsetType`     |ENUM    |NO         |
`abovePegOffsetValue`    |INT     |NO         |
`belowType`              |ENUM    |YES        |Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`
`belowClientOrderId`     |STRING  |NO         |
`belowIcebergQty`        |LONG    |NO         |Note that this can only be used if `belowTimeInForce` is `GTC`.
`belowPrice`             |DECIMAL |NO         |Can be used if `belowType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.
`belowStopPrice`         |DECIMAL |NO         |Can be used if `belowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT` or `TAKE_PROFIT_LIMIT`. <br>Either `belowStopPrice` or `belowTrailingDelta` or both, must be specified.
`belowTrailingDelta`     |LONG    |NO         |See [Trailing Stop order FAQ](faqs/trailing-stop-faq.md).
`belowTimeInForce`       |ENUM    |NO         |Required if `belowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`
`belowStrategyId`        |LONG    |NO         |Arbitrary numeric value identifying the below order within an order strategy.
`belowStrategyType`      |INT     |NO         |Arbitrary numeric value identifying the below order strategy. <br>Values smaller than 1000000 are reserved and cannot be used.
`belowPegPriceType`      |ENUM    |NO         |See [Pegged Orders](#pegged-orders-info)
`belowPegOffsetType`     |ENUM    |NO         |
`belowPegOffsetValue`    |INT     |NO         |
`newOrderRespType`       |ENUM    |NO         |Select response format: `ACK`, `RESULT`, `FULL`
`selfTradePreventionMode`|ENUM    |NO         |The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](./enums.md#stpmodes).
`apiKey`                 |STRING  |YES        |
`recvWindow`             |DECIMAL |NO         |The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`timestamp`              |LONG    |YES        |
`signature`              |STRING  |YES        |

**Data Source:**
Matching Engine

**Response:**

Response format for `orderReports` is selected using the `newOrderRespType` parameter.
The following example is for `RESULT` response type.
See [`order.place`](#place-new-order-trade) for more examples.

```javascript
{
    "id": "56374a46-3261-486b-a211-99ed972eb648",
    "status": 200,
    "result": {
        "orderListId": 2,
        "contingencyType": "OCO",
        "listStatusType": "EXEC_STARTED",
        "listOrderStatus": "EXECUTING",
        "listClientOrderId": "cKPMnDCbcLQILtDYM4f4fX",
        "transactionTime": 1711062760648,
        "symbol": "LTCBNB",
        "orders": [
            {
                "symbol": "LTCBNB",
                "orderId": 2,
                "clientOrderId": "0m6I4wfxvTUrOBSMUl0OPU"
            },
            {
                "symbol": "LTCBNB",
                "orderId": 3,
                "clientOrderId": "Z2IMlR79XNY5LU0tOxrWyW"
            }
        ],
        "orderReports": [
            {
                "symbol": "LTCBNB",
                "orderId": 2,
                "orderListId": 2,
                "clientOrderId": "0m6I4wfxvTUrOBSMUl0OPU",
                "transactTime": 1711062760648,
                "price": "1.50000000",
                "origQty": "1.000000",
                "executedQty": "0.000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "NEW",
                "timeInForce": "GTC",
                "type": "STOP_LOSS_LIMIT",
                "side": "BUY",
                "stopPrice": "1.50000001",
                "workingTime": -1,
                "selfTradePreventionMode": "NONE"
            },
            {
                "symbol": "LTCBNB",
                "orderId": 3,
                "orderListId": 2,
                "clientOrderId": "Z2IMlR79XNY5LU0tOxrWyW",
                "transactTime": 1711062760648,
                "price": "1.49999999",
                "origQty": "1.000000",
                "executedQty": "0.000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "NEW",
                "timeInForce": "GTC",
                "type": "LIMIT_MAKER",
                "side": "BUY",
                "workingTime": 1711062760648,
                "selfTradePreventionMode": "NONE"
            }
        ]
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 2
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 2
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

#### Place new Order list - OTO (TRADE)

```javascript
{
    "id": "1712544395950",
    "method": "orderList.place.oto",
    "params": {
        "signature": "3e1e5ac8690b0caf9a2afd5c5de881ceba69939cc9d817daead5386bf65d0cbb",
        "apiKey": "Rf07JlnL9PHVxjs27O5CvKNyOsV4qJ5gXdrRfpvlOdvMZbGZbPO5Ce2nIwfRP0iA",
        "pendingQuantity": 1,
        "pendingSide": "BUY",
        "pendingType": "MARKET",
        "symbol": "LTCBNB",
        "recvWindow": "5000",
        "timestamp": "1712544395951",
        "workingPrice": 1,
        "workingQuantity": 1,
        "workingSide": "SELL",
        "workingTimeInForce": "GTC",
        "workingType": "LIMIT"
    }
}
```

Places an OTO.

* An OTO (One-Triggers-the-Other) is an order list comprised of 2 orders.
* The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
* The second order is called the **pending order**. It can be any order type except for `MARKET` orders using parameter `quoteOrderQty`. The pending order is only placed on the order book when the working order gets **fully filled**.
* If either the working order or the pending order is cancelled individually, the other order in the order list will also be canceled or expired.
* When the order list is placed, if the working order gets **immediately fully filled**, the placement response will show the working order as `FILLED` but the pending order will still appear as `PENDING_NEW`. You need to query the status of the pending order again to see its updated status.
* OTOs add **2 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

**Weight:** 1

**Unfilled Order Count:**
2

**Parameters:**

Name                   |Type   |Mandatory | Description
----                   |----   |------    |------
`symbol`                 |STRING |YES       |
`listClientOrderId`      |STRING |NO        |Arbitrary unique ID among open order lists. Automatically generated if not sent. <br>A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. <br> `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`.
`newOrderRespType`       |ENUM   |NO        |Format of the JSON response. Supported values: [Order Response Type](./enums.md#orderresponsetype)
`selfTradePreventionMode`|ENUM   |NO        |The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](./enums.md#stpmodes)
`workingType`            |ENUM   |YES       |Supported values: `LIMIT`,`LIMIT_MAKER`
`workingSide`            |ENUM   |YES       |Supported values: [Order side](./enums.md#side)
`workingClientOrderId`   |STRING |NO        |Arbitrary unique ID among open orders for the working order.<br> Automatically generated if not sent.
`workingPrice`           |DECIMAL|YES       |
`workingQuantity`        |DECIMAL|YES       |Sets the quantity for the working order.
`workingIcebergQty`      |DECIMAL|NO       |This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`.
`workingTimeInForce`     |ENUM   |NO        |Supported values: [Time In Force](./enums.md#timeinforce)
`workingStrategyId`      |LONG   |NO        |Arbitrary numeric value identifying the working order within an order strategy.
`workingStrategyType`    |INT    |NO        |Arbitrary numeric value identifying the working order strategy. <br> Values smaller than 1000000 are reserved and cannot be used.
`workingPegPriceType`    |ENUM   |NO        |See [Pegged Orders](#pegged-orders-info)
`workingPegOffsetType`   |ENUM   |NO        |
`workingPegOffsetValue`  |INT    |NO        |
`pendingType`            |ENUM   |YES       |Supported values: [Order types](#order-type). <br> Note that `MARKET` orders using `quoteOrderQty` are not supported.
`pendingSide`            |ENUM   |YES       |Supported values: [Order side](./enums.md#side)
`pendingClientOrderId`   |STRING |NO        |Arbitrary unique ID among open orders for the pending order.<br> Automatically generated if not sent.
`pendingPrice`           |DECIMAL|NO        |
`pendingStopPrice`       |DECIMAL|NO        |
`pendingTrailingDelta`   |DECIMAL|NO        |
`pendingQuantity`        |DECIMAL|YES       |Sets the quantity for the pending order.
`pendingIcebergQty`      |DECIMAL|NO        |This can only be used if `pendingTimeInForce` is `GTC`, or if `pendingType` is `LIMIT_MAKER`.
`pendingTimeInForce`     |ENUM   |NO        |Supported values: [Time In Force](./enums.md#timeinforce)
`pendingStrategyId`      |LONG   |NO        |Arbitrary numeric value identifying the pending order within an order strategy.
`pendingStrategyType`    |INT    |NO        |Arbitrary numeric value identifying the pending order strategy. <br> Values smaller than 1000000 are reserved and cannot be used.
`pendingPegOffsetType`   |ENUM   |NO        |See [Pegged Orders](#pegged-orders-info)
`pendingPegPriceType`    |ENUM   |NO        |
`pendingPegOffsetValue`  |INT    |NO        |
`recvWindow`             |DECIMAL|NO        |The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`timestamp`              |LONG   |YES       |
`signature`              |STRING |YES       |

<a id="mandatory-parameters-based-on-pendingtype-or-workingtype"></a>

**Mandatory parameters based on `pendingType` or `workingType`**

Depending on the `pendingType` or `workingType`, some optional parameters will become mandatory.

|Type                                                  |Additional mandatory parameters|Additional information|
|----                                                  |----                           |------
|`workingType` = `LIMIT`                               |`workingTimeInForce`           |
|`pendingType` = `LIMIT`                                |`pendingPrice`, `pendingTimeInForce`          |
|`pendingType` = `STOP_LOSS` or `TAKE_PROFIT`           |`pendingStopPrice` and/or `pendingTrailingDelta`|
|`pendingType` =`STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT`|`pendingPrice`, `pendingStopPrice` and/or `pendingTrailingDelta`, `pendingTimeInForce`|

**Data Source:**
Matching Engine

**Response:**

```javascript
{
    "id": "1712544395950",
    "status": 200,
    "result": {
        "orderListId": 626,
        "contingencyType": "OTO",
        "listStatusType": "EXEC_STARTED",
        "listOrderStatus": "EXECUTING",
        "listClientOrderId": "KA4EBjGnzvSwSCQsDdTrlf",
        "transactionTime": 1712544395981,
        "symbol": "1712544378871",
        "orders": [
            {
                "symbol": "LTCBNB",
                "orderId": 13,
                "clientOrderId": "YiAUtM9yJjl1a2jXHSp9Ny"
            },
            {
                "symbol": "LTCBNB",
                "orderId": 14,
                "clientOrderId": "9MxJSE1TYkmyx5lbGLve7R"
            }
        ],
        "orderReports": [
            {
                "symbol": "LTCBNB",
                "orderId": 13,
                "orderListId": 626,
                "clientOrderId": "YiAUtM9yJjl1a2jXHSp9Ny",
                "transactTime": 1712544395981,
                "price": "1.000000",
                "origQty": "1.000000",
                "executedQty": "0.000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.000000",
                "status": "NEW",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "SELL",
                "workingTime": 1712544395981,
                "selfTradePreventionMode": "NONE"
            },
            {
                "symbol": "LTCBNB",
                "orderId": 14,
                "orderListId": 626,
                "clientOrderId": "9MxJSE1TYkmyx5lbGLve7R",
                "transactTime": 1712544395981,
                "price": "0.000000",
                "origQty": "1.000000",
                "executedQty": "0.000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.000000",
                "status": "PENDING_NEW",
                "timeInForce": "GTC",
                "type": "MARKET",
                "side": "BUY",
                "workingTime": -1,
                "selfTradePreventionMode": "NONE"
            }
        ]
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 10000000,
            "count": 10
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 1000,
            "count": 38
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

#### Place new Order list - OTOCO (TRADE)

```javascript
{
    "id": "1712544408508",
    "method": "orderList.place.otoco",
    "params": {
        "signature": "c094473304374e1b9c5f7e2558358066cfa99df69f50f63d09cfee755136cb07",
        "apiKey": "Rf07JlnL9PHVxjs27O5CvKNyOsV4qJ5gXdrRfpvlOdvMZbGZbPO5Ce2nIwfRP0iA",
        "pendingQuantity": 5,
        "pendingSide": "SELL",
        "pendingBelowPrice": 5,
        "pendingBelowType": "LIMIT_MAKER",
        "pendingAboveStopPrice": 0.5,
        "pendingAboveType": "STOP_LOSS",
        "symbol": "LTCBNB",
        "recvWindow": "5000",
        "timestamp": "1712544408509",
        "workingPrice": 1.5,
        "workingQuantity": 1,
        "workingSide": "BUY",
        "workingTimeInForce": "GTC",
        "workingType": "LIMIT"
    }
}
```

Place an OTOCO.

* An OTOCO (One-Triggers-One-Cancels-the-Other) is an order list comprised of 3 orders.
* The first order is called the **working order** and must be `LIMIT` or `LIMIT_MAKER`. Initially, only the working order goes on the order book.
  * The behavior of the working order is the same as the [OTO](#place-new-order-list---oto-trade).
* OTOCO has 2 pending orders (pending above and pending below), forming an OCO pair. The pending orders are only placed on the order book when the working order gets **fully filled**.
    * The rules of the pending above and pending below follow the same rules as the [Order list OCO](#new-order-list---oco-trade).
* OTOCOs add **3 orders** to the `EXCHANGE_MAX_NUM_ORDERS` filter and `MAX_NUM_ORDERS` filter.

**Weight:** 1

**Unfilled Order Count:**
3

**Parameters:**

Name                     |Type   |Mandatory | Description
----                     |----   |------    |------
`symbol`                   |STRING |YES       |
`listClientOrderId`        |STRING |NO        |Arbitrary unique ID among open order lists. Automatically generated if not sent. <br>A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. <br> `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`.
`newOrderRespType`         |ENUM   |NO        |Format of the JSON response. Supported values: [Order Response Type](./enums.md#orderresponsetype)
`selfTradePreventionMode`  |ENUM   |NO        |The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](./enums.md#stpmodes)
`workingType`              |ENUM   |YES       |Supported values: `LIMIT`, `LIMIT_MAKER`
`workingSide`              |ENUM   |YES       |Supported values: [Order Side](./enums.md#side)
`workingClientOrderId`     |STRING |NO        |Arbitrary unique ID among open orders for the working order.<br> Automatically generated if not sent.
`workingPrice`             |DECIMAL|YES       |
`workingQuantity`          |DECIMAL|YES       |
`workingIcebergQty`        |DECIMAL|NO        |This can only be used if `workingTimeInForce` is `GTC`.
`workingTimeInForce`       |ENUM   |NO        |Supported values: [Time In Force](./enums.md#timeinforce)
`workingStrategyId`        |LONG    |NO        |Arbitrary numeric value identifying the working order within an order strategy.
`workingStrategyType`      |INT    |NO        |Arbitrary numeric value identifying the working order strategy. <br> Values smaller than 1000000 are reserved and cannot be used.
`workingPegPriceType`      |ENUM   |NO        |See [Pegged Orders](#pegged-orders-info)
`workingPegOffsetType`     |ENUM   |NO        |
`workingPegOffsetValue`    |INT    |NO        |
`pendingSide`              |ENUM   |YES       |Supported values: [Order Side](./enums.md#side)
`pendingQuantity`          |DECIMAL|YES       |
`pendingAboveType`         |ENUM   |YES       |Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`
`pendingAboveClientOrderId`|STRING |NO        |Arbitrary unique ID among open orders for the pending above order.<br> Automatically generated if not sent.
`pendingAbovePrice`        |DECIMAL|NO        |Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price.
`pendingAboveStopPrice`    |DECIMAL|NO        |Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT`
`pendingAboveTrailingDelta`|DECIMAL|NO        |See [Trailing Stop FAQ](faqs/trailing-stop-faq.md)
`pendingAboveIcebergQty`   |DECIMAL|NO        |This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`.
`pendingAboveTimeInForce`  |ENUM   |NO        |
`pendingAboveStrategyId`   |LONG    |NO        |Arbitrary numeric value identifying the pending above order within an order strategy.
`pendingAboveStrategyType` |INT    |NO        |Arbitrary numeric value identifying the pending above order strategy. <br> Values smaller than 1000000 are reserved and cannot be used.
`pendingAbovePegPriceType` |ENUM   |NO        |See [Pegged Orders](#pegged-orders-info)
`pendingAbovePegOffsetType`|ENUM   |NO        |
`pendingAbovePegOffsetValue` |INT  |NO        |
`pendingBelowType`         |ENUM   |NO        |Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT`
`pendingBelowClientOrderId`|STRING |NO        |Arbitrary unique ID among open orders for the pending below order.<br> Automatically generated if not sent.
`pendingBelowPrice`        |DECIMAL|NO        |Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify the limit price.
`pendingBelowStopPrice`    |DECIMAL|NO        |Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT, TAKE_PROFIT or TAKE_PROFIT_LIMIT`. <br>Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified.
`pendingBelowTrailingDelta`|DECIMAL|NO        |
`pendingBelowIcebergQty`   |DECIMAL|NO        |This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`.
`pendingBelowTimeInForce`  |ENUM   |NO        |Supported values: [Time In Force](./enums.md#timeinforce)
`pendingBelowStrategyId`   |LONG    |NO        |Arbitrary numeric value identifying the pending below order within an order strategy.
`pendingBelowStrategyType` |INT    |NO        |Arbitrary numeric value identifying the pending below order strategy. <br> Values smaller than 1000000 are reserved and cannot be used.
`pendingBelowPegPriceType` |ENUM   |NO        |See [Pegged Orders](#pegged-orders-info)
`pendingBelowPegOffsetType`|ENUM   |NO        |
`pendingBelowPegOffsetValue` |INT  |NO        |
`recvWindow`               |DECIMAL|NO        |The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`timestamp`                |LONG   |YES       |
`signature`                |STRING|YES|

<a id="mandatory-parameters-based-on-pendingabovetype-pendingbelowtype-or-workingtype"></a>

**Mandatory parameters based on `pendingAboveType`, `pendingBelowType` or `workingType`**

Depending on the `pendingAboveType`/`pendingBelowType` or `workingType`, some optional parameters will become mandatory.

|Type                                                       |Additional mandatory parameters|Additional information|
|----                                                       |----                           |------
|`workingType` = `LIMIT`                                    |`workingTimeInForce`           |
|`pendingAboveType`= `LIMIT_MAKER`                                |`pendingAbovePrice`          |
|`pendingAboveType` = `STOP_LOSS/TAKE_PROFIT`         |`pendingAboveStopPrice` and/or `pendingAboveTrailingDelta`|
|`pendingAboveType=STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT`|`pendingAbovePrice`, `pendingAboveStopPrice` and/or `pendingAboveTrailingDelta`, `pendingAboveTimeInForce`|
|`pendingBelowType`= `LIMIT_MAKER`                                |`pendingBelowPrice`          |
`pendingBelowType= STOP_LOSS/TAKE_PROFIT`         |`pendingBelowStopPrice` and/or `pendingBelowTrailingDelta`|
|`pendingBelowType=STOP_LOSS_LIMIT/TAKE_PROFIT_LIMIT`|`pendingBelowPrice`, `pendingBelowStopPrice` and/or `pendingBelowTrailingDelta`, `pendingBelowTimeInForce`|

**Data Source:**
Matching Engine

**Response:**

```javascript
{
    "id": "1712544408508",
    "status": 200,
    "result": {
        "orderListId": 629,
        "contingencyType": "OTO",
        "listStatusType": "EXEC_STARTED",
        "listOrderStatus": "EXECUTING",
        "listClientOrderId": "GaeJHjZPasPItFj4x7Mqm6",
        "transactionTime": 1712544408537,
        "symbol": "1712544378871",
        "orders": [
            {
                "symbol": "LTCBNB",
                "orderId": 23,
                "clientOrderId": "OVQOpKwfmPCfaBTD0n7e7H"
            },
            {
                "symbol": "LTCBNB",
                "orderId": 24,
                "clientOrderId": "YcCPKCDMQIjNvLtNswt82X"
            },
            {
                "symbol": "LTCBNB",
                "orderId": 25,
                "clientOrderId": "ilpIoShcFZ1ZGgSASKxMPt"
            }
        ],
        "orderReports": [
            {
                "symbol": "LTCBNB",
                "orderId": 23,
                "orderListId": 629,
                "clientOrderId": "OVQOpKwfmPCfaBTD0n7e7H",
                "transactTime": 1712544408537,
                "price": "1.500000",
                "origQty": "1.000000",
                "executedQty": "0.000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.000000",
                "status": "NEW",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "BUY",
                "workingTime": 1712544408537,
                "selfTradePreventionMode": "NONE"
            },
            {
                "symbol": "LTCBNB",
                "orderId": 24,
                "orderListId": 629,
                "clientOrderId": "YcCPKCDMQIjNvLtNswt82X",
                "transactTime": 1712544408537,
                "price": "0.000000",
                "origQty": "5.000000",
                "executedQty": "0.000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.000000",
                "status": "PENDING_NEW",
                "timeInForce": "GTC",
                "type": "STOP_LOSS",
                "side": "SELL",
                "stopPrice": "0.500000",
                "workingTime": -1,
                "selfTradePreventionMode": "NONE"
            },
            {
                "symbol": "LTCBNB",
                "orderId": 25,
                "orderListId": 629,
                "clientOrderId": "ilpIoShcFZ1ZGgSASKxMPt",
                "transactTime": 1712544408537,
                "price": "5.000000",
                "origQty": "5.000000",
                "executedQty": "0.000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.000000",
                "status": "PENDING_NEW",
                "timeInForce": "GTC",
                "type": "LIMIT_MAKER",
                "side": "SELL",
                "workingTime": -1,
                "selfTradePreventionMode": "NONE"
            }
        ]
    },
    "rateLimits": [
        {
            "rateLimitType": "ORDERS",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 10000000,
            "count": 18
        },
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 1000,
            "count": 65
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).
#### OPO (TRADE)

```json
{
    "id": "1762941318128",
    "method": "orderList.place.opo",
    "params": {
        "workingPrice": "101496",
        "workingQuantity": "0.0007",
        "workingType": "LIMIT",
        "workingTimeInForce": "GTC",
        "pendingType": "MARKET",
        "pendingSide": "SELL",
        "recvWindow": 5000,
        "workingSide": "BUY",
        "symbol": "BTCUSDT",
        "timestamp": 1762941318129,
        "apiKey": "aHb4Ur1cK1biW3sgibqUFs39SE58f9d5Xwf4uEW0tFh7ibun5g035QKSktxoOBfE",
        "signature": "b50ce8977333a78a3bbad21df178d7e104a8c985d19007b55df688cdf868639a"
    }
}
```

Place an [OPO](./faqs/opo.md).

* OPOs add 2 orders to the EXCHANGE_MAX_NUM_ORDERS filter and MAX_NUM_ORDERS filter.

**Weight:** 1

**Unfilled Order Count:** 2

**Parameters:**

| Name | Type | Mandatory | Description |
| ----- | ----- | ----- | ----- |
| `symbol` | STRING | YES |  |
| `listClientOrderId` | STRING | NO | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId` and the `pendingClientOrderId`. |
| `newOrderRespType` | ENUM | NO | Format of the JSON response. Supported values: [Order Response Type](./enums.md#orderresponsetype) |
| `selfTradePreventionMode` | ENUM | NO | The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](./enums.md#stpmodes) |
| `workingType` | ENUM | YES | Supported values: `LIMIT`,`LIMIT_MAKER` |
| `workingSide` | ENUM | YES | Supported values: [Order Side](./enums.md#side) |
| `workingClientOrderId` | STRING | NO | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent. |
| `workingPrice` | DECIMAL | YES |  |
| `workingQuantity` | DECIMAL | YES | Sets the quantity for the working order. |
| `workingIcebergQty` | DECIMAL | NO | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`. |
| `workingTimeInForce` | ENUM | NO | Supported values: [Time In Force](./enums.md#timeinforce) |
| `workingStrategyId` | LONG | NO | Arbitrary numeric value identifying the working order within an order strategy. |
| `workingStrategyType` | INT | NO | Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used. |
| `workingPegPriceType` | ENUM | NO | See [Pegged Orders](#pegged-orders-info) |
| `workingPegOffsetType` | ENUM | NO |  |
| `workingPegOffsetValue` | INT | NO |  |
| `pendingType` | ENUM | YES | Supported values: [Order Types](#order-type) Note that `MARKET` orders using `quoteOrderQty` are not supported. |
| `pendingSide` | ENUM | YES | Supported values: [Order Side](./enums.md#side) |
| `pendingClientOrderId` | STRING | NO | Arbitrary unique ID among open orders for the pending order. Automatically generated if not sent. |
| `pendingPrice` | DECIMAL | NO |  |
| `pendingStopPrice` | DECIMAL | NO |  |
| `pendingTrailingDelta` | DECIMAL | NO |  |
| `pendingIcebergQty` | DECIMAL | NO | This can only be used if `pendingTimeInForce` is `GTC` or if `pendingType` is `LIMIT_MAKER`. |
| `pendingTimeInForce` | ENUM | NO | Supported values: [Time In Force](./enums.md#timeinforce) |
| `pendingStrategyId` | LONG | NO | Arbitrary numeric value identifying the pending order within an order strategy. |
| `pendingStrategyType` | INT | NO | Arbitrary numeric value identifying the pending order strategy. Values smaller than 1000000 are reserved and cannot be used. |
| `pendingPegPriceType` | ENUM | NO | See [Pegged Orders](#pegged-orders-info) |
| `pendingPegOffsetType` | ENUM | NO |  |
| `pendingPegOffsetValue` | INT | NO |  |
| `recvWindow` | DECIMAL | NO | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified. |
| `timestamp` | LONG | YES |  |

**Data Source**: Matching Engine

**Response:**

```json
{
    "id": "1762941318128",
    "status": 200,
    "result": {
        "orderListId": 2,
        "contingencyType": "OTO",
        "listStatusType": "EXEC_STARTED",
        "listOrderStatus": "EXECUTING",
        "listClientOrderId": "OiOgqvRagBefpzdM5gjYX3",
        "transactionTime": 1762941318142,
        "symbol": "BTCUSDT",
        "orders": [
            {
                "symbol": "BTCUSDT",
                "orderId": 2,
                "clientOrderId": "pUzhKBbc0ZVdMScIRAqitH"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 3,
                "clientOrderId": "x7ISSjywZxFXOdzwsThNnd"
            }
        ],
        "orderReports": [
            {
                "symbol": "BTCUSDT",
                "orderId": 2,
                "orderListId": 2,
                "clientOrderId": "pUzhKBbc0ZVdMScIRAqitH",
                "transactTime": 1762941318142,
                "price": "101496.00000000",
                "origQty": "0.00070000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.00000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "NEW",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "BUY",
                "workingTime": 1762941318142,
                "selfTradePreventionMode": "NONE"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 3,
                "orderListId": 2,
                "clientOrderId": "x7ISSjywZxFXOdzwsThNnd",
                "transactTime": 1762941318142,
                "price": "0.00000000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.00000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "PENDING_NEW",
                "timeInForce": "GTC",
                "type": "MARKET",
                "side": "SELL",
                "workingTime": -1,
                "selfTradePreventionMode": "NONE"
            }
        ]
    }
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

#### OPOCO (TRADE)

```json
{
    "id": "1763000139090",
    "method": "orderList.place.opoco",
    "params": {
        "workingPrice": "102496",
        "workingQuantity": "0.0017",
        "workingType": "LIMIT",
        "workingTimeInForce": "GTC",
        "pendingAboveType": "LIMIT_MAKER",
        "pendingAbovePrice": "104261",
        "pendingBelowStopPrice": "10100",
        "pendingBelowPrice": "101613",
        "pendingBelowType": "STOP_LOSS_LIMIT",
        "pendingBelowTimeInForce": "IOC",
        "pendingSide": "SELL",
        "recvWindow": 5000,
        "workingSide": "BUY",
        "symbol": "BTCUSDT",
        "timestamp": 1763000139091,
        "apiKey": "2wiKgTLyllTCu0QWXaEtKWX9tUQ5iQMiDQqTQPdUe2bZ1IVT9aXoS6o19wkYIKl2",
        "signature": "adfa185c50f793392a54ad5a6e2c39fd34ef6d35944adf2ddd6f30e1866e58d3"
    }
}
```

Place an [OPOCO](./faqs/opo.md).

**Weight**: 1

**Unfilled Order Count:** 3

**Parameters:**

| Name | Type | Mandatory | Description |
| ----- | ----- | ----- | ----- |
| `symbol` | STRING | YES |  |
| `listClientOrderId` | STRING | NO | Arbitrary unique ID among open order lists. Automatically generated if not sent. A new order list with the same listClientOrderId is accepted only when the previous one is filled or completely expired. `listClientOrderId` is distinct from the `workingClientOrderId`, `pendingAboveClientOrderId`, and the `pendingBelowClientOrderId`. |
| `newOrderRespType` | ENUM | NO | Format of the JSON response. Supported values: [Order Response Type](./enums.md#orderresponsetype) |
| `selfTradePreventionMode` | ENUM | NO | The allowed values are dependent on what is configured on the symbol. Supported values: [STP Modes](./enums.md#stpmodes) |
| `workingType` | ENUM | YES | Supported values: `LIMIT`, `LIMIT_MAKER` |
| `workingSide` | ENUM | YES | Supported values: [Order side](./enums.md#side) |
| `workingClientOrderId` | STRING | NO | Arbitrary unique ID among open orders for the working order. Automatically generated if not sent. |
| `workingPrice` | DECIMAL | YES |  |
| `workingQuantity` | DECIMAL | YES |  |
| `workingIcebergQty` | DECIMAL | NO | This can only be used if `workingTimeInForce` is `GTC`, or if `workingType` is `LIMIT_MAKER`. |
| `workingTimeInForce` | ENUM | NO | Supported values: [Time In Force](./enums.md#timeinforce) |
| `workingStrategyId` | LONG | NO | Arbitrary numeric value identifying the working order within an order strategy. |
| `workingStrategyType` | INT | NO | Arbitrary numeric value identifying the working order strategy. Values smaller than 1000000 are reserved and cannot be used. |
| `workingPegPriceType` | ENUM | NO | See [Pegged Orders](#pegged-orders-info) |
| `workingPegOffsetType` | ENUM | NO |  |
| `workingPegOffsetValue` | INT | NO |  |
| `pendingSide` | ENUM | YES | Supported values: [Order side](./enums.md#side) |
| `pendingAboveType` | ENUM | YES | Supported values: `STOP_LOSS_LIMIT`, `STOP_LOSS`, `LIMIT_MAKER`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` |
| `pendingAboveClientOrderId` | STRING | NO | Arbitrary unique ID among open orders for the pending above order. Automatically generated if not sent. |
| `pendingAbovePrice` | DECIMAL | NO | Can be used if `pendingAboveType` is `STOP_LOSS_LIMIT` , `LIMIT_MAKER`, or `TAKE_PROFIT_LIMIT` to specify the limit price. |
| `pendingAboveStopPrice` | DECIMAL | NO | Can be used if `pendingAboveType` is `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, `TAKE_PROFIT_LIMIT` |
| `pendingAboveTrailingDelta` | DECIMAL | NO | See [Trailing Stop FAQ](./faqs/trailing-stop-faq.md) |
| `pendingAboveIcebergQty` | DECIMAL | NO | This can only be used if `pendingAboveTimeInForce` is `GTC` or if `pendingAboveType` is `LIMIT_MAKER`. |
| `pendingAboveTimeInForce` | ENUM | NO |  |
| `pendingAboveStrategyId` | LONG | NO | Arbitrary numeric value identifying the pending above order within an order strategy. |
| `pendingAboveStrategyType` | INT | NO | Arbitrary numeric value identifying the pending above order strategy. Values smaller than 1000000 are reserved and cannot be used. |
| `pendingAbovePegPriceType` | ENUM | NO | See [Pegged Orders](#pegged-orders-info) |
| `pendingAbovePegOffsetType` | ENUM | NO |  |
| `pendingAbovePegOffsetValue` | INT | NO |  |
| `pendingBelowType` | ENUM | NO | Supported values: `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`,`TAKE_PROFIT_LIMIT` |
| `pendingBelowClientOrderId` | STRING | NO | Arbitrary unique ID among open orders for the pending below order. Automatically generated if not sent. |
| `pendingBelowPrice` | DECIMAL | NO | Can be used if `pendingBelowType` is `STOP_LOSS_LIMIT` or `TAKE_PROFIT_LIMIT` to specify limit price |
| `pendingBelowStopPrice` | DECIMAL | NO | Can be used if `pendingBelowType` is `STOP_LOSS`, `STOP_LOSS_LIMIT, TAKE_PROFIT or TAKE_PROFIT_LIMIT`. Either `pendingBelowStopPrice` or `pendingBelowTrailingDelta` or both, must be specified. |
| `pendingBelowTrailingDelta` | DECIMAL | NO |  |
| `pendingBelowIcebergQty` | DECIMAL | NO | This can only be used if `pendingBelowTimeInForce` is `GTC`, or if `pendingBelowType` is `LIMIT_MAKER`. |
| `pendingBelowTimeInForce` | ENUM | NO | Supported values: [Time In Force](./enums.md#timeinforce) |
| `pendingBelowStrategyId` | LONG | NO | Arbitrary numeric value identifying the pending below order within an order strategy. |
| `pendingBelowStrategyType` | INT | NO | Arbitrary numeric value identifying the pending below order strategy. Values smaller than 1000000 are reserved and cannot be used. |
| `pendingBelowPegPriceType` | ENUM | NO | See [Pegged Orders](#pegged-orders-info) |
| `pendingBelowPegOffsetType` | ENUM | NO |  |
| `pendingBelowPegOffsetValue` | INT | NO |  |
| `recvWindow` | DECIMAL | NO | The value cannot be greater than `60000`. Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified. |
| `timestamp` | LONG | YES |  |

**Data Source**:
Matching Engine

**Response:**

```json
{
    "id": "1763000139090",
    "status": 200,
    "result": {
        "orderListId": 1,
        "contingencyType": "OTO",
        "listStatusType": "EXEC_STARTED",
        "listOrderStatus": "EXECUTING",
        "listClientOrderId": "TVbG6ymkYMXTj7tczbOsBf",
        "transactionTime": 1763000139104,
        "symbol": "BTCUSDT",
        "orders": [
            {
                "symbol": "BTCUSDT",
                "orderId": 6,
                "clientOrderId": "3czuJSeyjPwV9Xo28j1Dv3"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 7,
                "clientOrderId": "kyIKnMLKQclE5FmyYgaMSo"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 8,
                "clientOrderId": "i76cGJWN9J1FpADS56TtQZ"
            }
        ],
        "orderReports": [
            {
                "symbol": "BTCUSDT",
                "orderId": 6,
                "orderListId": 1,
                "clientOrderId": "3czuJSeyjPwV9Xo28j1Dv3",
                "transactTime": 1763000139104,
                "price": "102496.00000000",
                "origQty": "0.00170000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.00000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "NEW",
                "timeInForce": "GTC",
                "type": "LIMIT",
                "side": "BUY",
                "workingTime": 1763000139104,
                "selfTradePreventionMode": "NONE"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 7,
                "orderListId": 1,
                "clientOrderId": "kyIKnMLKQclE5FmyYgaMSo",
                "transactTime": 1763000139104,
                "price": "101613.00000000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.00000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "PENDING_NEW",
                "timeInForce": "IOC",
                "type": "STOP_LOSS_LIMIT",
                "side": "SELL",
                "stopPrice": "10100.00000000",
                "workingTime": -1,
                "selfTradePreventionMode": "NONE"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 8,
                "orderListId": 1,
                "clientOrderId": "i76cGJWN9J1FpADS56TtQZ",
                "transactTime": 1763000139104,
                "price": "104261.00000000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.00000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "PENDING_NEW",
                "timeInForce": "GTC",
                "type": "LIMIT_MAKER",
                "side": "SELL",
                "workingTime": -1,
                "selfTradePreventionMode": "NONE"
            }
        ]
    }
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

#### Cancel Order list (TRADE)

```javascript
{
    "id": "c5899911-d3f4-47ae-8835-97da553d27d0",
    "method": "orderList.cancel",
    "params": {
        "symbol": "BTCUSDT",
        "orderListId": 1274512,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "4973f4b2fee30bf6d45e4a973e941cc60fdd53c8dd5a25edeac96f5733c0ccee",
        "timestamp": 1660801720210
    }
}
```

Cancel an active order list.

**Weight**:
1

**Parameters:**

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>symbol</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>orderListId</code></td>
        <td>INT</td>
        <td rowspan="2">YES</td>
        <td>Cancel order list by <code>orderListId</code></td>
    </tr>
    <tr>
        <td><code>listClientOrderId</code></td>
        <td>STRING</td>
        <td>Cancel order list by <code>listClientId</code></td>
    </tr>
    <tr>
        <td><code>newClientOrderId</code></td>
        <td>STRING</td>
        <td>NO</td>
        <td>New ID for the canceled order list. Automatically generated if not sent</td>
    </tr>
    <tr>
        <td><code>apiKey</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>recvWindow</code></td>
        <td>DECIMAL</td>
        <td>NO</td>
        <td>The value cannot be greater than <tt>60000</tt>.<br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.</td>
    </tr>
    <tr>
        <td><code>signature</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>timestamp</code></td>
        <td>LONG</td>
        <td>YES</td>
        <td></td>
    </tr>
</tbody>
</table>

Notes:

* If both `orderListId` and `listClientOrderId` parameters are provided, the `orderListId` is searched first, then the `listClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.

* Canceling an individual order with [`order.cancel`](#cancel-order-trade) will cancel the entire order list as well.

**Data Source:**
Matching Engine

**Response:**

```javascript
{
    "id": "c5899911-d3f4-47ae-8835-97da553d27d0",
    "status": 200,
    "result": {
        "orderListId": 1274512,
        "contingencyType": "OCO",
        "listStatusType": "ALL_DONE",
        "listOrderStatus": "ALL_DONE",
        "listClientOrderId": "6023531d7edaad348f5aff",
        "transactionTime": 1660801720215,
        "symbol": "BTCUSDT",
        "orders": [
            {
                "symbol": "BTCUSDT",
                "orderId": 12569138901,
                "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 12569138902,
                "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"
            }
        ],
        "orderReports": [
            {
                "symbol": "BTCUSDT",
                "orderId": 12569138901,
                "orderListId": 1274512,
                "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU",
                "transactTime": 1660801720215,
                "price": "23410.00000000",
                "origQty": "0.00650000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "CANCELED",
                "timeInForce": "GTC",
                "type": "STOP_LOSS_LIMIT",
                "side": "SELL",
                "stopPrice": "23405.00000000",
                "selfTradePreventionMode": "NONE"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 12569138902,
                "orderListId": 1274512,
                "clientOrderId": "jLnZpj5enfMXTuhKB1d0us",
                "transactTime": 1660801720215,
                "price": "23420.00000000",
                "origQty": "0.00650000",
                "executedQty": "0.00000000",
                "origQuoteOrderQty": "0.000000",
                "cummulativeQuoteQty": "0.00000000",
                "status": "CANCELED",
                "timeInForce": "GTC",
                "type": "LIMIT_MAKER",
                "side": "SELL",
                "selfTradePreventionMode": "NONE"
            }
        ]
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

### SOR

#### Place new order using SOR (TRADE)

```javascript
{
    "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",
    "method": "sor.order.place",
    "params": {
        "symbol": "BTCUSDT",
        "side": "BUY",
        "type": "LIMIT",
        "quantity": 0.5,
        "timeInForce": "GTC",
        "price": 31000,
        "timestamp": 1687485436575,
        "apiKey": "u5lgqJb97QWXWfgeV4cROuHbReSJM9rgQL0IvYcYc7BVeA5lpAqqc3a5p2OARIFk",
        "signature": "fd301899567bc9472ce023392160cdc265ad8fcbbb67e0ea1b2af70a4b0cd9c7"
    }
}
```

Places an order using smart order routing (SOR).

This adds 1 order to the `EXCHANGE_MAX_ORDERS` filter and the `MAX_NUM_ORDERS` filter.

Read [SOR FAQ](../faqs/sor_faq.md) to learn more.

**Weight:**
1

**Unfilled Order Count:**
1

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`symbol`            | STRING  | YES       |
`side`              | ENUM    | YES       | `BUY` or `SELL`
`type`              | ENUM    | YES       |
`timeInForce`       | ENUM    | NO        | Applicable only to `LIMIT` order type
`price`             | DECIMAL | NO        | Applicable only to `LIMIT` order type
`quantity`          | DECIMAL | YES       |
`newClientOrderId`  | STRING  | NO        | Arbitrary unique ID among open orders. Automatically generated if not sent
`newOrderRespType`  | ENUM    | NO        | <p>Select response format: `ACK`, `RESULT`, `FULL`.</p><p>`MARKET` and `LIMIT` orders use `FULL` by default.</p>
`icebergQty`        | DECIMAL | NO        |
`strategyId`        | LONG    | NO        | Arbitrary numeric value identifying the order within an order strategy.
`strategyType`      | INT     | NO        | <p>Arbitrary numeric value identifying the order strategy.</p><p>Values smaller than `1000000` are reserved and cannot be used.</p>
`selfTradePreventionMode` |ENUM | NO      | The allowed enums is dependent on what is configured on the symbol. The possible supported values are: [STP Modes](./enums.md#stpmodes).
`apiKey`            | STRING  | YES       |
`timestamp`         | LONG    | YES       |
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |

**Note:** `sor.order.place` only supports `LIMIT` and `MARKET` orders. `quoteOrderQty` is not supported.

**Data Source:**
Matching Engine

**Response:**

```javascript
{
    "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",
    "status": 200,
    "result": [
        {
            "symbol": "BTCUSDT",
            "orderId": 2,
            "orderListId": -1,
            "clientOrderId": "sBI1KM6nNtOfj5tccZSKly",
            "transactTime": 1689149087774,
            "price": "31000.00000000",
            "origQty": "0.50000000",
            "executedQty": "0.50000000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "14000.00000000",
            "status": "FILLED",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "BUY",
            "workingTime": 1689149087774,
            "fills": [
                {
                    "matchType": "ONE_PARTY_TRADE_REPORT",
                    "price": "28000.00000000",
                    "qty": "0.50000000",
                    "commission": "0.00000000",
                    "commissionAsset": "BTC",
                    "tradeId": -1,
                    "allocId": 0
                }
            ],
            "workingFloor": "SOR",
            "selfTradePreventionMode": "NONE",
            "usedSor": true
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

#### Test new order using SOR (TRADE)

```javascript
{
    "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",
    "method": "sor.order.test",
    "params": {
        "symbol": "BTCUSDT",
        "side": "BUY",
        "type": "LIMIT",
        "quantity": 0.1,
        "timeInForce": "GTC",
        "price": 0.1,
        "timestamp": 1687485436575,
        "apiKey": "u5lgqJb97QWXWfgeV4cROuHbReSJM9rgQL0IvYcYc7BVeA5lpAqqc3a5p2OARIFk",
        "signature": "fd301899567bc9472ce023392160cdc265ad8fcbbb67e0ea1b2af70a4b0cd9c7"
    }
}
```

Test new order creation and signature/recvWindow using smart order routing (SOR).
Creates and validates a new order but does not send it into the matching engine.

**Weight:**

|Condition                       | Request Weight|
|------------                    | ------------ |
|Without `computeCommissionRates`| 1            |
|With `computeCommissionRates`   |20            |

**Parameters:**

In addition to all parameters accepted by [`sor.order.place`](#place-new-order-using-sor-trade),
the following optional parameters are also accepted:

Name                   |Type          | Mandatory    | Description
------------           | ------------ | ------------ | ------------
`computeCommissionRates` | BOOLEAN      | NO           | Default: `false`

**Data Source:**
Memory

**Response:**

Without `computeCommissionRates`:

```javascript
{
    "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",
    "status": 200,
    "result": {},
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 1
        }
    ]
}
```

With `computeCommissionRates`:

```javascript
{
    "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",
    "status": 200,
    "result": {
        "standardCommissionForOrder": {  // Commission rates for the order depending on its role (e.g. maker or taker)
            "maker": "0.00000112",
            "taker": "0.00000114"
        },
        "taxCommissionForOrder": {       // Tax deduction rates for the order depending on its role (e.g. maker or taker)
            "maker": "0.00000112",
            "taker": "0.00000114"
        },
        "discount": {                    // Discount on standard commissions when paying in BNB.
            "enabledForAccount": true,
            "enabledForSymbol": true,
            "discountAsset": "BNB",
            "discount": "0.25"           // Standard commission is reduced by this rate when paying in BNB.
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 20
        }
    ]
}
```

## Account requests

### Account information (USER_DATA)

```javascript
{
    "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",
    "method": "account.status",
    "params": {
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "83303b4a136ac1371795f465808367242685a9e3a42b22edb4d977d0696eb45c",
        "timestamp": 1660801839480
    }
}
```

Query information about your account.

**Weight:**
20

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`apiKey`            | STRING  | YES       |
`omitZeroBalances`  | BOOLEAN | NO        | When set to `true`, emits only the non-zero balances of an account. <br>Default value: false
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |
`timestamp`         | LONG    | YES       |

**Data Source:**
Memory => Database

**Response:**
```javascript
{
    "id": "605a6d20-6588-4cb9-afa0-b0ab087507ba",
    "status": 200,
    "result": {
        "makerCommission": 15,
        "takerCommission": 15,
        "buyerCommission": 0,
        "sellerCommission": 0,
        "canTrade": true,
        "canWithdraw": true,
        "canDeposit": true,
        "commissionRates": {
            "maker": "0.00150000",
            "taker": "0.00150000",
            "buyer": "0.00000000",
            "seller": "0.00000000"
        },
        "brokered": false,
        "requireSelfTradePrevention": false,
        "preventSor": false,
        "updateTime": 1660801833000,
        "accountType": "SPOT",
        "balances": [
            {
                "asset": "BNB",
                "free": "0.00000000",
                "locked": "0.00000000"
            },
            {
                "asset": "BTC",
                "free": "1.3447112",
                "locked": "0.08600000"
            },
            {
                "asset": "USDT",
                "free": "1021.21000000",
                "locked": "0.00000000"
            }
        ],
        "permissions": ["SPOT"],
        "uid": 354937868
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 20
        }
    ]
}
```

### Query order (USER_DATA)

```javascript
{
    "id": "aa62318a-5a97-4f3b-bdc7-640bbe33b291",
    "method": "order.status",
    "params": {
        "symbol": "BTCUSDT",
        "orderId": 12569099453,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "2c3aab5a078ee4ea465ecd95523b77289f61476c2f238ec10c55ea6cb11a6f35",
        "timestamp": 1660801720951
    }
}
```

Check execution status of an order.

**Weight:**
4

**Parameters:**

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>symbol</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>orderId</code></td>
        <td>LONG</td>
        <td rowspan="2">YES</td>
        <td>Lookup order by <code>orderId</code></td>
    </tr>
    <tr>
        <td><code>origClientOrderId</code></td>
        <td>STRING</td>
        <td>Lookup order by <code>clientOrderId</code></td>
    </tr>
    <tr>
        <td><code>apiKey</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>recvWindow</code></td>
        <td>DECIMAL</td>
        <td>NO</td>
        <td>The value cannot be greater than <tt>60000</tt>.<br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.</td>
    </tr>
    <tr>
        <td><code>signature</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>timestamp</code></td>
        <td>LONG</td>
        <td>YES</td>
        <td></td>
    </tr>
</tbody>
</table>

Notes:

* If both `orderId` and `origClientOrderId` are provided, the `orderId` is searched first, then the `origClientOrderId` from that result is checked against that order. If both conditions are not met the request will be rejected.

* For some historical orders the `cummulativeQuoteQty` response field may be negative,
  meaning the data is not available at this time.

**Data Source:**
Memory => Database

**Response:**
```javascript
{
    "id": "aa62318a-5a97-4f3b-bdc7-640bbe33b291",
    "status": 200,
    "result": {
        "symbol": "BTCUSDT",
        "orderId": 12569099453,
        "orderListId": -1,                     // set only for orders of an order list
        "clientOrderId": "4d96324ff9d44481926157",
        "price": "23416.10000000",
        "origQty": "0.00847000",
        "executedQty": "0.00847000",
        "cummulativeQuoteQty": "198.33521500",
        "status": "FILLED",
        "timeInForce": "GTC",
        "type": "LIMIT",
        "side": "SELL",
        "stopPrice": "0.00000000",             // always present, zero if order type does not use stopPrice
        "trailingDelta": 10,                   // present only if trailingDelta set for the order
        "trailingTime": -1,                    // present only if trailingDelta set for the order
        "icebergQty": "0.00000000",            // always present, zero for non-iceberg orders
        "time": 1660801715639,                 // time when the order was placed
        "updateTime": 1660801717945,           // time of the last update to the order
        "isWorking": true,
        "workingTime": 1660801715639,
        "origQuoteOrderQty": "0.00000000",     // always present, zero if order type does not use quoteOrderQty
        "strategyId": 37463720,                // present only if strategyId set for the order
        "strategyType": 1000000,               // present only if strategyType set for the order
        "selfTradePreventionMode": "NONE",
        "preventedMatchId": 0,                 // present only if the order expired due to STP
        "preventedQuantity": "1.200000"        // present only if the order expired due to STP
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 4
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

### Current open orders (USER_DATA)

```javascript
{
    "id": "55f07876-4f6f-4c47-87dc-43e5fff3f2e7",
    "method": "openOrders.status",
    "params": {
        "symbol": "BTCUSDT",
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "d632b3fdb8a81dd44f82c7c901833309dd714fe508772a89b0a35b0ee0c48b89",
        "timestamp": 1660813156812
    }
}
```

Query execution status of all open orders.

If you need to continuously monitor order status updates, please consider using WebSocket Streams:

* [`userDataStream.start`](#user-data-stream-requests) request
* [`executionReport`](./user-data-stream.md#order-update) user data stream event

**Weight:**
Adjusted based on the number of requested symbols:

| Parameter | Weight |
| --------- | ------ |
| `symbol`  |      6 |
| none      |     80 |

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`symbol`            | STRING  | NO        | If omitted, open orders for all symbols are returned
`apiKey`            | STRING  | YES       |
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |
`timestamp`         | LONG    | YES       |

**Data Source:**
Memory => Database

**Response:**

Status reports for open orders are identical to [`order.status`](#query-order-user_data).

Note that some fields are optional and included only for orders that set them.

Open orders are always returned as a flat list.
If all symbols are requested, use the `symbol` field to tell which symbol the orders belong to.

```javascript
{
    "id": "55f07876-4f6f-4c47-87dc-43e5fff3f2e7",
    "status": 200,
    "result": [
        {
            "symbol": "BTCUSDT",
            "orderId": 12569099453,
            "orderListId": -1,
            "clientOrderId": "4d96324ff9d44481926157",
            "price": "23416.10000000",
            "origQty": "0.00847000",
            "executedQty": "0.00720000",
            "origQuoteOrderQty": "0.000000",
            "cummulativeQuoteQty": "172.43931000",
            "status": "PARTIALLY_FILLED",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "SELL",
            "stopPrice": "0.00000000",
            "icebergQty": "0.00000000",
            "time": 1660801715639,
            "updateTime": 1660801717945,
            "isWorking": true,
            "workingTime": 1660801715639,
            "origQuoteOrderQty": "0.00000000",
            "selfTradePreventionMode": "NONE"
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 6
        }
    ]
}
```

**Note:** The payload above does not show all fields that can appear. Please refer to [Conditional fields in Order Responses](#conditional-fields-in-order-responses).

### Account order history (USER_DATA)

```javascript
{
    "id": "734235c2-13d2-4574-be68-723e818c08f3",
    "method": "allOrders",
    "params": {
        "symbol": "BTCUSDT",
        "startTime": 1660780800000,
        "endTime": 1660867200000,
        "limit": 5,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "f50a972ba7fad92842187643f6b930802d4e20bce1ba1e788e856e811577bd42",
        "timestamp": 1661955123341
    }
}
```

Query information about all your orders – active, canceled, filled – filtered by time range.

**Weight:**
20

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`symbol`            | STRING  | YES       |
`orderId`           | LONG    | NO        | Order ID to begin at
`startTime`         | LONG    | NO        |
`endTime`           | LONG    | NO        |
`limit`             | INT     | NO        | Default: 500; Maximum: 1000
`apiKey`            | STRING  | YES       |
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |
`timestamp`         | LONG    | YES       |

Notes:

* If `startTime` and/or `endTime` are specified, `orderId` is ignored.

  Orders are filtered by `time` of the last execution status update.

* If `orderId` is specified, return orders with order ID >= `orderId`.

* If no condition is specified, the most recent orders are returned.

* For some historical orders the `cummulativeQuoteQty` response field may be negative,
  meaning the data is not available at this time.

* The time between `startTime` and `endTime` can't be longer than 24 hours.

**Data Source:**
Database

**Response:**

Status reports for orders are identical to [`order.status`](#query-order-user_data).

Note that some fields are optional and included only for orders that set them.

```javascript
{
    "id": "734235c2-13d2-4574-be68-723e818c08f3",
    "status": 200,
    "result": [
        {
            "symbol": "BTCUSDT",
            "orderId": 12569099453,
            "orderListId": -1,
            "clientOrderId": "4d96324ff9d44481926157",
            "price": "23416.10000000",
            "origQty": "0.00847000",
            "executedQty": "0.00847000",
            "cummulativeQuoteQty": "198.33521500",
            "status": "FILLED",
            "timeInForce": "GTC",
            "type": "LIMIT",
            "side": "SELL",
            "stopPrice": "0.00000000",
            "icebergQty": "0.00000000",
            "time": 1660801715639,
            "updateTime": 1660801717945,
            "isWorking": true,
            "workingTime": 1660801715639,
            "origQuoteOrderQty": "0.00000000",
            "selfTradePreventionMode": "NONE",
            "preventedMatchId": 0,              // This field only appears if the order expired due to STP.
            "preventedQuantity": "1.200000"     // This field only appears if the order expired due to STP.
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 20
        }
    ]
}
```

### Query Order list (USER_DATA)

```javascript
{
    "id": "b53fd5ff-82c7-4a04-bd64-5f9dc42c2100",
    "method": "orderList.status",
    "params": {
        "origClientOrderId": "08985fedd9ea2cf6b28996",
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "d12f4e8892d46c0ddfbd43d556ff6d818581b3be22a02810c2c20cb719aed6a4",
        "timestamp": 1660801713965
    }
}
```

Check execution status of an Order list.

For execution status of individual orders, use [`order.status`](#query-order-user_data).

**Weight:**
4

**Parameters**:

<table>
<thead>
    <tr>
        <th>Name</th>
        <th>Type</th>
        <th>Mandatory</th>
        <th>Description</th>
    </tr>
</thead>
<tbody>
    <tr>
        <td><code>origClientOrderId</code></td>
        <td>STRING</td>
        <td rowspan="2">NO*</td>
        <td>Query order list by <code>listClientOrderId</code>.<br><code>orderListId</code> or <code>origClientOrderId</code> must be provided.</td>
    </tr>
    <tr>
        <td><code>orderListId</code></td>
        <td>INT</td>
        <td>Query order list by <code>orderListId</code>.<br><code>orderListId</code> or <code>origClientOrderId</code> must be provided.</td>
    </tr>
    <tr>
        <td><code>apiKey</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>recvWindow</code></td>
        <td>DECIMAL</td>
        <td>NO</td>
        <td>The value cannot be greater than <tt>60000</tt>.<br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.</td>
    </tr>
    <tr>
        <td><code>signature</code></td>
        <td>STRING</td>
        <td>YES</td>
        <td></td>
    </tr>
    <tr>
        <td><code>timestamp</code></td>
        <td>LONG</td>
        <td>YES</td>
        <td></td>
    </tr>
</tbody>
</table>

Notes:

* `origClientOrderId` refers to `listClientOrderId` of the order list itself.

* If both `origClientOrderId` and `orderListId` parameters are specified,
  only `origClientOrderId` is used and `orderListId` is ignored.

**Data Source:**
Database

**Response:**

```javascript
{
    "id": "b53fd5ff-82c7-4a04-bd64-5f9dc42c2100",
    "status": 200,
    "result": {
        "orderListId": 1274512,
        "contingencyType": "OCO",
        "listStatusType": "EXEC_STARTED",
        "listOrderStatus": "EXECUTING",
        "listClientOrderId": "08985fedd9ea2cf6b28996",
        "transactionTime": 1660801713793,
        "symbol": "BTCUSDT",
        "orders": [
            {
                "symbol": "BTCUSDT",
                "orderId": 12569138901,
                "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"
            },
            {
                "symbol": "BTCUSDT",
                "orderId": 12569138902,
                "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"
            }
        ]
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 4
        }
    ]
}
```

### Current open Order lists (USER_DATA)

```javascript
{
    "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",
    "method": "openOrderLists.status",
    "params": {
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "1bea8b157dd78c3da30359bddcd999e4049749fe50b828e620e12f64e8b433c9",
        "timestamp": 1660801713831
    }
}
```

Query execution status of all open order lists.

If you need to continuously monitor order status updates, please consider using WebSocket Streams:

* [`userDataStream.start`](#user-data-stream-requests) request
* [`executionReport`](./user-data-stream.md#order-update) user data stream event

**Weight**:
6

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`apiKey`            | STRING  | YES       |
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |
`timestamp`         | LONG    | YES       |

**Data Source:**
Database

**Response:**

```javascript
{
    "id": "3a4437e2-41a3-4c19-897c-9cadc5dce8b6",
    "status": 200,
    "result": [
        {
            "orderListId": 0,
            "contingencyType": "OCO",
            "listStatusType": "EXEC_STARTED",
            "listOrderStatus": "EXECUTING",
            "listClientOrderId": "08985fedd9ea2cf6b28996",
            "transactionTime": 1660801713793,
            "symbol": "BTCUSDT",
            "orders": [
                {
                    "symbol": "BTCUSDT",
                    "orderId": 4,
                    "clientOrderId": "CUhLgTXnX5n2c0gWiLpV4d"
                },
                {
                    "symbol": "BTCUSDT",
                    "orderId": 5,
                    "clientOrderId": "1ZqG7bBuYwaF4SU8CwnwHm"
                }
            ]
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 6
        }
    ]
}
```

### Account order list history (USER_DATA)

```javascript
{
    "id": "8617b7b3-1b3d-4dec-94cd-eefd929b8ceb",
    "method": "allOrderLists",
    "params": {
        "startTime": 1660780800000,
        "endTime": 1660867200000,
        "limit": 5,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "c8e1484db4a4a02d0e84dfa627eb9b8298f07ebf12fcc4eaf86e4a565b2712c2",
        "timestamp": 1661955123341
    }
}
```

Query information about all your order lists, filtered by time range.

**Weight:**
20

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`fromId`            | INT     | NO        | Order list ID to begin at
`startTime`         | LONG    | NO        |
`endTime`           | LONG    | NO        |
`limit`             | INT     | NO        | Default: 500; Maximum: 1000
`apiKey`            | STRING  | YES       |
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |
`timestamp`         | LONG    | YES       |

Notes:

* If `startTime` and/or `endTime` are specified, `fromId` is ignored.

  Order lists are filtered by `transactionTime` of the last order list execution status update.

* If `fromId` is specified, return order lists with order list ID >= `fromId`.

* If no condition is specified, the most recent order lists are returned.

* The time between `startTime` and `endTime` can't be longer than 24 hours.

**Data Source:**
Database

**Response:**

Status reports for order lists are identical to [`orderList.status`](#query-order-list-user_data).

```javascript
{
    "id": "8617b7b3-1b3d-4dec-94cd-eefd929b8ceb",
    "status": 200,
    "result": [
        {
            "orderListId": 1274512,
            "contingencyType": "OCO",
            "listStatusType": "EXEC_STARTED",
            "listOrderStatus": "EXECUTING",
            "listClientOrderId": "08985fedd9ea2cf6b28996",
            "transactionTime": 1660801713793,
            "symbol": "BTCUSDT",
            "orders": [
                {
                    "symbol": "BTCUSDT",
                    "orderId": 12569138901,
                    "clientOrderId": "BqtFCj5odMoWtSqGk2X9tU"
                },
                {
                    "symbol": "BTCUSDT",
                    "orderId": 12569138902,
                    "clientOrderId": "jLnZpj5enfMXTuhKB1d0us"
                }
            ]
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 20
        }
    ]
}
```

### Account trade history (USER_DATA)

```javascript
{
    "id": "f4ce6a53-a29d-4f70-823b-4ab59391d6e8",
    "method": "myTrades",
    "params": {
        "symbol": "BTCUSDT",
        "startTime": 1660780800000,
        "endTime": 1660867200000,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "c5a5ffb79fd4f2e10a92f895d488943a57954edf5933bde3338dfb6ea6d6eefc",
        "timestamp": 1661955125250
    }
}
```

Query information about all your trades, filtered by time range.

**Weight:**

Condition| Weight|
---| ---
|Without orderId|20|
|With orderId|5|

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`symbol`            | STRING  | YES       |
`orderId`           | LONG    | NO        |
`startTime`         | LONG    | NO        |
`endTime`           | LONG    | NO        |
`fromId`            | INT     | NO        | First trade ID to query
`limit`             | INT     | NO        | Default: 500; Maximum: 1000
`apiKey`            | STRING  | YES       |
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |
`timestamp`         | LONG    | YES       |

Notes:

* If `fromId` is specified, return trades with trade ID >= `fromId`.

* If `startTime` and/or `endTime` are specified, trades are filtered by execution time (`time`).

  `fromId` cannot be used together with `startTime` and `endTime`.

* If `orderId` is specified, only trades related to that order are returned.

  `startTime` and `endTime` cannot be used together with `orderId`.

* If no condition is specified, the most recent trades are returned.

* The time between `startTime` and `endTime` can't be longer than 24 hours.

**Data Source:**
Memory => Database

**Response:**

```javascript
{
    "id": "f4ce6a53-a29d-4f70-823b-4ab59391d6e8",
    "status": 200,
    "result": [
        {
            "symbol": "BTCUSDT",
            "id": 1650422481,
            "orderId": 12569099453,
            "orderListId": -1,
            "price": "23416.10000000",
            "qty": "0.00635000",
            "quoteQty": "148.69223500",
            "commission": "0.00000000",
            "commissionAsset": "BNB",
            "time": 1660801715793,
            "isBuyer": false,
            "isMaker": true,
            "isBestMatch": true
        },
        {
            "symbol": "BTCUSDT",
            "id": 1650422482,
            "orderId": 12569099453,
            "orderListId": -1,
            "price": "23416.50000000",
            "qty": "0.00212000",
            "quoteQty": "49.64298000",
            "commission": "0.00000000",
            "commissionAsset": "BNB",
            "time": 1660801715793,
            "isBuyer": false,
            "isMaker": true,
            "isBestMatch": true
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 20
        }
    ]
}
```

<a id="query-unfilled-order-count"></a>

### Unfilled Order Count (USER_DATA)

```javascript
{
    "id": "d3783d8d-f8d1-4d2c-b8a0-b7596af5a664",
    "method": "account.rateLimits.orders",
    "params": {
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "76289424d6e288f4dc47d167ac824e859dabf78736f4348abbbac848d719eb94",
        "timestamp": 1660801839500
    }
}
```

Query your current unfilled order count for all intervals.

**Weight:**
40

**Parameters:**

Name                | Type    | Mandatory | Description
------------------- | ------- | --------- | ------------
`apiKey`            | STRING  | YES       |
`recvWindow`        | DECIMAL | NO        | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`signature`         | STRING  | YES       |
`timestamp`         | LONG    | YES       |

**Data Source:**
Memory

**Response:**

```javascript
{
    "id": "d3783d8d-f8d1-4d2c-b8a0-b7596af5a664",
    "status": 200,
    "result": [
        {
            "rateLimitType": "ORDERS",
            "interval": "SECOND",
            "intervalNum": 10,
            "limit": 50,
            "count": 0
        },
        {
            "rateLimitType": "ORDERS",
            "interval": "DAY",
            "intervalNum": 1,
            "limit": 160000,
            "count": 0
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 40
        }
    ]
}
```

### Account prevented matches (USER_DATA)

```javascript
{
    "id": "g4ce6a53-a39d-4f71-823b-4ab5r391d6y8",
    "method": "myPreventedMatches",
    "params": {
        "symbol": "BTCUSDT",
        "orderId": 35,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "c5a5ffb79fd4f2e10a92f895d488943a57954edf5933bde3338dfb6ea6d6eefc",
        "timestamp": 1673923281052
    }
}
```

Displays the list of orders that were expired due to STP.

These are the combinations supported:

* `symbol` + `preventedMatchId`
* `symbol` + `orderId`
* `symbol` + `orderId` + `fromPreventedMatchId` (`limit` will default to 500)
* `symbol` + `orderId` + `fromPreventedMatchId` + `limit`

**Parameters:**

Name                | Type   | Mandatory    | Description
------------        | ----   | ------------ | ------------
symbol              | STRING | YES          |
preventedMatchId    | LONG   | NO           |
orderId             | LONG   | NO           |
fromPreventedMatchId| LONG   | NO           |
limit               | INT    | NO           | Default: `500`; Maximum: `1000`
recvWindow          | DECIMAL| NO           | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp           | LONG   | YES          |

**Weight**

Case                            | Weight
----                            | -----
If `symbol` is invalid          | 2
Querying by `preventedMatchId`  | 2
Querying by `orderId`           | 20

**Data Source:**
Database

**Response:**

```javascript
{
    "id": "g4ce6a53-a39d-4f71-823b-4ab5r391d6y8",
    "status": 200,
    "result": [
        {
            "symbol": "BTCUSDT",
            "preventedMatchId": 1,
            "takerOrderId": 5,
            "makerSymbol": "BTCUSDT",
            "makerOrderId": 3,
            "tradeGroupId": 1,
            "selfTradePreventionMode": "EXPIRE_MAKER",
            "price": "1.100000",
            "makerPreventedQuantity": "1.300000",
            "transactTime": 1669101687094
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 20
        }
    ]
}
```

### Account allocations (USER_DATA)

```javascript
{
    "id": "g4ce6a53-a39d-4f71-823b-4ab5r391d6y8",
    "method": "myAllocations",
    "params": {
        "symbol": "BTCUSDT",
        "orderId": 500,
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "c5a5ffb79fd4f2e10a92f895d488943a57954edf5933bde3338dfb6ea6d6eefc",
        "timestamp": 1673923281052
    }
}
```

Retrieves allocations resulting from SOR order placement.

**Weight:**
20

**Parameters:**

Name                       | Type  |Mandatory | Description
-----                      | ---   |----      | ---------
`symbol`                   |STRING |Yes        |
`startTime`                |LONG   |No        |
`endTime`                  |LONG   |No        |
`fromAllocationId`         |INT    |No        |
`limit`                    |INT    |No        |Default: 500; Maximum: 1000
`orderId`                  |LONG   |No        |
`recvWindow`               |DECIMAL|No        |The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
`timestamp`                |LONG   |No        |

Supported parameter combinations:

Parameters                                  | Response |
------------------------------------------- | -------- |
`symbol`                                    | allocations from oldest to newest |
`symbol` + `startTime`                      | oldest allocations since `startTime` |
`symbol` + `endTime`                        | newest allocations until `endTime` |
`symbol` + `startTime` + `endTime`          | allocations within the time range |
`symbol` + `fromAllocationId`               | allocations by allocation ID |
`symbol` + `orderId`                        | allocations related to an order starting with oldest |
`symbol` + `orderId` + `fromAllocationId`   | allocations related to an order by allocation ID |

**Note:** The time between `startTime` and `endTime` can't be longer than 24 hours.

**Data Source:**
Database

**Response:**

```javascript
{
    "id": "g4ce6a53-a39d-4f71-823b-4ab5r391d6y8",
    "status": 200,
    "result": [
        {
            "symbol": "BTCUSDT",
            "allocationId": 0,
            "allocationType": "SOR",
            "orderId": 500,
            "orderListId": -1,
            "price": "1.00000000",
            "qty": "0.10000000",
            "quoteQty": "0.10000000",
            "commission": "0.00000000",
            "commissionAsset": "BTC",
            "time": 1687319487614,
            "isBuyer": false,
            "isMaker": false,
            "isAllocator": false
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 20
        }
    ]
}
```

### Account Commission Rates (USER_DATA)

```javascript
{
    "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
    "method": "account.commission",
    "params": {
        "symbol": "BTCUSDT",
        "apiKey": "vmPUZE6mv9SD5VNHk4HlWFsOr6aKE2zvsw0MuIgwCIPy6utIco14y7Ju91duEh8A",
        "signature": "c5a5ffb79fd4f2e10a92f895d488943a57954edf5933bde3338dfb6ea6d6eefc",
        "timestamp": 1673923281052
    }
}
```

Get current account commission rates.

**Parameters:**

Name                       | Type  |Mandatory | Description
-----                      | ---   |----      | ---------
`symbol`                   |STRING |YES        |

**Weight:**
20

**Data Source:**
Database

**Response:**

```javascript
{
    "id": "d3df8a61-98ea-4fe0-8f4e-0fcea5d418b0",
    "status": 200,
    "result": {
        "symbol": "BTCUSDT",
        "standardCommission": {          // Standard commission rates on trades from the order.
            "maker": "0.00000010",
            "taker": "0.00000020",
            "buyer": "0.00000030",
            "seller": "0.00000040"
        },
        "specialCommission": {           // Special commission rates from the order.
            "maker": "0.01000000",
            "taker": "0.02000000",
            "buyer": "0.03000000",
            "seller": "0.04000000"
        },
        "taxCommission": {               // Tax commission rates on trades from the order.
            "maker": "0.00000112",
            "taker": "0.00000114",
            "buyer": "0.00000118",
            "seller": "0.00000116"
        },
        "discount": {                    // Discount on standard commissions when paying in BNB.
            "enabledForAccount": true,
            "enabledForSymbol": true,
            "discountAsset": "BNB",
            "discount": "0.75000000"     // Standard commission is reduced by this rate when paying commission in BNB.
        }
    },
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 20
        }
    ]
}
```

### Query Order Amendments (USER_DATA)

```javascript
{
    "id": "6f5ebe91-01d9-43ac-be99-57cf062e0e30",
    "method": "order.amendments",
    "params": {
        "orderId": "23",
        "recvWindow": 5000,
        "symbol": "BTCUSDT",
        "timestamp": 1741925524887,
        "apiKey": "N3Swv7WaBF7S2rzA12UkPunM3udJiDddbgv1W7CzFGnsQXH9H62zzSCST0CndjeE",
        "signature": "0eed2e9d95b6868ea5ec21da0d14538192ef344c30ecf9fe83d58631699334dc"
    }
}
```

Queries all amendments of a single order.

**Weight**:
4

**Parameters:**

Name | Type | Mandatory | Description |
:---- | :---- | :---- | :---- |
symbol | STRING | YES |  |
orderId | LONG | YES |  |
fromExecutionId | LONG | NO |  |
limit | LONG | NO | Default:500; Maximum: 1000 |
recvWindow | DECIMAL | NO | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp | LONG | YES |

**Data Source:**
Database

**Response:**

```javascript
{
    "id": "6f5ebe91-01d9-43ac-be99-57cf062e0e30",
    "status": 200,
    "result": [
        {
            "symbol": "BTCUSDT",
            "orderId": 23,
            "executionId": 60,
            "origClientOrderId": "my_pending_order",
            "newClientOrderId": "xbxXh5SSwaHS7oUEOCI88B",
            "origQty": "7.00000000",
            "newQty": "5.00000000",
            "time": 1741924229819
        }
    ],
    "rateLimits": [
        {
            "rateLimitType": "REQUEST_WEIGHT",
            "interval": "MINUTE",
            "intervalNum": 1,
            "limit": 6000,
            "count": 4
        }
    ]
}
```


<a id="myFilters"></a>
### Query Relevant Filters (USER_DATA)

```javascript
{
    "id": "74R4febb-d142-46a2-977d-90533eb4d97g",
    "method": "myFilters",
    "params": {
        "recvWindow": 5000,
        "symbol": "BTCUSDT",
        "timestamp": 1758008841149,
        "apiKey": "nQ6kG5gDExDd5MZSO0MfOOWEVZmdkRllpNMfm1FjMjkMnmw1NUd3zPDfvcnDJlil",
        "signature": "7edc54dd0493dd5bc47adbab9b17bfc9b378d55c20511ae5a168456d3d37aa3a"
    }
}
```

Retrieves the list of [filters](filters.md) relevant to an account on a given symbol. This is the only method that shows if an account has [`MAX_ASSET`](filters.md#max_asset) filters applied to it.

**Weight:**
40

**Parameters:**

Name       | Type         | Mandatory    | Description
---------- | ------------ | ------------ | ------------
symbol     | STRING       | YES          |
recvWindow | DECIMAL      | NO           | The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.
timestamp  | LONG         | YES          |

**Data Source:**
Memory

**Response:**

```javascript
{
    "id": "1758009606869",
    "status": 200,
    "result": {
        "exchangeFilters": [
            {
                "filterType": "EXCHANGE_MAX_NUM_ORDERS",
                "maxNumOrders": 1000
            }
        ],
        "symbolFilters": [
            {
                "filterType": "MAX_NUM_ORDER_LISTS",
                "maxNumOrderLists": 20
            }
        ],
        "assetFilters": [
            {
                "filterType": "MAX_ASSET",
                "asset": "JPY",
                "limit": "1000000.00000000"
            }
        ]
    }
}
```


## User Data Stream requests

### User Data Stream subscription

<a id=general_info_user_data_stream_subscriptions></a>
**General information:**

* [User Data Stream](user-data-stream.md) subscriptions allow you to receive all the events related to a given account on a WebSocket connection.
* There are 2 ways to start a subscription:
  * If you have an authenticated session, then you can subscribe to events for that authenticated account using [`userDataStream.subscribe`](#user-data-stream-subscribe).
  * In any session, authenticated or not, you can subscribe to events for one or more accounts for which you can provide an API Key signature, using [`userdataStream.subscribe.signature`](#user-data-signature).
  * You can have only one active subscription for a given account on a given connection.
* Subscriptions are identified by a `subscriptionId` which is returned when starting the subscription. That `subscriptionId` allows you to map the events you receive to a given subscription.
  * All active subscriptions for a session can be found using [`session.subscriptions`](#session-subscription).
* Limits
  * A single session supports **up to 1,000 active subscriptions** simultaneously.
    * Attempting to start a new subscription beyond this limit will result in an error.
    * If your accounts are very active, we suggest not opening too many subscriptions at once, in order to not overload your connection.
  * A single session can handle a maximum of **65,535 total subscriptions** over its lifetime.
    * If this limit is reached, you will receive an error and must re-establish a new connection to be able to start new subscriptions.
* To verify the status of User Data Stream subscriptions, check the `userDataStream` field in [`session.status`](#query-session-status):
  * `null` - User Data Stream subscriptions are **not available** on this WebSocket API.
  * `true` - There is at **least one subscription active** in this session.
  * `false` - There are **no active subscriptions** in this session.

<a id="user-data-stream-subscribe"></a>

#### Subscribe to User Data Stream (USER_STREAM)

```javascript
{
    "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",
    "method": "userDataStream.subscribe"
}
```

Subscribe to the User Data Stream in the current WebSocket connection.

**Notes:**

* This method requires an authenticated WebSocket connection using Ed25519 keys. Please refer to [`session.logon`](#session-logon).
* To check the subscription status, use [`session.status`](#session-status), see the `userDataStream` flag indicating you have have an active subscription.
* User Data Stream events are available in both JSON and [SBE](faqs/sbe_faq.md) sessions.
  * Please refer to [User Data Streams](user-data-stream.md) for the event format details.
  * For SBE, only SBE schema 2:1 or later is supported.

**Weight**:
2

**Parameters**:
NONE

**Response**:

```javascript
{
    "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",
    "status": 200,
    "result": {
        "subscriptionId": 0
    }
}
```

#### Unsubscribe from User Data Stream

```javascript
{
    "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",
    "method": "userDataStream.unsubscribe"
}
```

Stop listening to the User Data Stream in the current WebSocket connection.

Note that `session.logout` will only close the subscription created with `userDataStream.subscribe` but not subscriptions opened with `userDataStream.subscribe.signature`.

**Weight**:
2

**Parameters**:

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `subscriptionId` | INT | No | When called with no parameter, this will close all subscriptions. <br>When called with the `subscriptionId` parameter, this will attempt to close the subscription with that subscription id, if it exists. |

**Response**:

```javascript
{
    "id": "d3df8a21-98ea-4fe0-8f4e-0fcea5d418b7",
    "status": 200,
    "result": {}
}
```

<a id="session-subscription"></a>

#### Listing all subscriptions

```javascript
{
    "id": "d3df5a22-88ea-4fe0-9f4e-0fcea5d418b7",
    "method": "session.subscriptions",
    "params": {}
}
```

**Note:**

* Users are expected to track on their side which subscription corresponds to which account.

**Weight**:
2

**Data Source**:
Memory

**Response**:

```javascript
{
    "id": "d3df5a22-88ea-4fe0-9f4e-0fcea5d418b7",
    "status": 200,
    "result": [
        {
            "subscriptionId": 0
        },
        {
            "subscriptionId": 1
        }
    ]
}
```

<a id="user-data-signature"></a>

#### Subscribe to User Data Stream through signature subscription (USER_STREAM)

```javascript
{
    "id": "d3df8a22-98ea-4fe0-9f4e-0fcea5d418b7",
    "method": "userDataStream.subscribe.signature",
    "params": {
        "apiKey": "mjcKCrJzTU6TChLsnPmgnQJJMR616J4yWvdZWDUeXkk6vL6dLyS7rcVOQlADlVjA",
        "timestamp": 1747385641636,
        "signature": "yN1vWpXb+qoZ3/dGiFs9vmpNdV7e3FxkA+BstzbezDKwObcijvk/CVkWxIwMCtCJbP270R0OempYwEpS6rDZCQ=="
    }
}
```

**Weight:**
2

**Parameters**:

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| `apiKey` | STRING | Yes |  |
| `timestamp` | LONG | Yes |  |
| `signature` | STRING | Yes |  |
|`recvWindow`|DECIMAL | No|The value cannot be greater than `60000`. <br> Supports up to three decimal places of precision (e.g., 6000.346) so that microseconds may be specified.|

**Data Source:**
Memory

**Response:**

```javascript
{
    "id": "d3df8a22-98ea-4fe0-9f4e-0fcea5d418b7",
    "status": 200,
    "result": {
        "subscriptionId": 0
    }
}
```
# Filters
Filters define trading rules on a symbol or an exchange.
Filters come in three forms: `symbol filters`, `exchange filters` and `asset filters`.

## Symbol filters
### PRICE_FILTER
The `PRICE_FILTER` defines the `price` rules for a symbol. There are 3 parts:

* `minPrice` defines the minimum `price`/`stopPrice` allowed; disabled on `minPrice` == 0.
* `maxPrice` defines the maximum `price`/`stopPrice` allowed; disabled on `maxPrice` == 0.
* `tickSize` defines the intervals that a `price`/`stopPrice` can be increased/decreased by; disabled on `tickSize` == 0.

Any of the above variables can be set to 0, which disables that rule in the `price filter`. In order to pass the `price filter`, the following must be true for `price`/`stopPrice` of the enabled rules:

* `price` >= `minPrice`
* `price` <= `maxPrice`
* `price` % `tickSize` == 0

**/exchangeInfo format:**
```javascript
{
  "filterType": "PRICE_FILTER",
  "minPrice": "0.00000100",
  "maxPrice": "100000.00000000",
  "tickSize": "0.00000100"
}
```

### PERCENT_PRICE
The `PERCENT_PRICE` filter defines the valid range for the price based on the average of the previous trades.
`avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.

In order to pass the `percent price`, the following must be true for `price`:
* `price` <= `weightedAveragePrice` * `multiplierUp`
* `price` >= `weightedAveragePrice` * `multiplierDown`

**/exchangeInfo format:**
```javascript
{
  "filterType": "PERCENT_PRICE",
  "multiplierUp": "1.3000",
  "multiplierDown": "0.7000",
  "avgPriceMins": 5
}
```

### PERCENT_PRICE_BY_SIDE
The `PERCENT_PRICE_BY_SIDE` filter defines the valid range for the price based on the average of the previous trades.<br/>
`avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used. <br/>
There is a different range depending on whether the order is placed on the `BUY` side or the `SELL` side.

Buy orders will succeed on this filter if:
* `Order price` <= `weightedAveragePrice` * `bidMultiplierUp`
* `Order price` >= `weightedAveragePrice` * `bidMultiplierDown`

Sell orders will succeed on this filter if:
* `Order Price` <= `weightedAveragePrice` * `askMultiplierUp`
* `Order Price` >= `weightedAveragePrice` * `askMultiplierDown`

**/exchangeInfo format:**
```javascript
  {
    "filterType": "PERCENT_PRICE_BY_SIDE",
    "bidMultiplierUp": "1.2",
    "bidMultiplierDown": "0.2",
    "askMultiplierUp": "5",
    "askMultiplierDown": "0.8",
    "avgPriceMins": 1
  }
```


### LOT_SIZE
The `LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for a symbol. There are 3 parts:

* `minQty` defines the minimum `quantity`/`icebergQty` allowed.
* `maxQty` defines the maximum `quantity`/`icebergQty` allowed.
* `stepSize` defines the intervals that a `quantity`/`icebergQty` can be increased/decreased by.

In order to pass the `lot size`, the following must be true for `quantity`/`icebergQty`:

* `quantity` >= `minQty`
* `quantity` <= `maxQty`
* `quantity` % `stepSize` == 0

**/exchangeInfo format:**
```javascript
{
  "filterType": "LOT_SIZE",
  "minQty": "0.00100000",
  "maxQty": "100000.00000000",
  "stepSize": "0.00100000"
}
```

### MIN_NOTIONAL
The `MIN_NOTIONAL` filter defines the minimum notional value allowed for an order on a symbol.
An order's notional value is the `price` * `quantity`.
`applyToMarket` determines whether or not the `MIN_NOTIONAL` filter will also be applied to `MARKET` orders.
Since `MARKET` orders have no price, the average price is used over the last `avgPriceMins` minutes.
`avgPriceMins` is the number of minutes the average price is calculated over. 0 means the last price is used.


**/exchangeInfo format:**
```javascript
{
  "filterType": "MIN_NOTIONAL",
  "minNotional": "0.00100000",
  "applyToMarket": true,
  "avgPriceMins": 5
}
```

### NOTIONAL
The `NOTIONAL` filter defines the acceptable notional range allowed for an order on a symbol. <br/><br/>
`applyMinToMarket` determines whether the `minNotional` will be applied to `MARKET` orders. <br/>
`applyMaxToMarket` determines whether the `maxNotional` will be applied to `MARKET` orders.

In order to pass this filter, the notional (`price * quantity`) has to pass the following conditions:

* `price * quantity` <= `maxNotional`
* `price * quantity` >= `minNotional`

For `MARKET` orders, the average price used over the last `avgPriceMins` minutes will be used for calculation. <br/>
If the `avgPriceMins` is 0, then the last price will be used.

**/exchangeInfo format:**
```javascript
{
   "filterType": "NOTIONAL",
   "minNotional": "10.00000000",
   "applyMinToMarket": false,
   "maxNotional": "10000.00000000",
   "applyMaxToMarket": false,
   "avgPriceMins": 5
}
```

### ICEBERG_PARTS
The `ICEBERG_PARTS` filter defines the maximum parts an iceberg order can have. The number of `ICEBERG_PARTS` is defined as `CEIL(qty / icebergQty)`.

**/exchangeInfo format:**
```javascript
{
  "filterType": "ICEBERG_PARTS",
  "limit": 10
}
```

### MARKET_LOT_SIZE
The `MARKET_LOT_SIZE` filter defines the `quantity` (aka "lots" in auction terms) rules for `MARKET` orders on a symbol. There are 3 parts:

* `minQty` defines the minimum `quantity` allowed.
* `maxQty` defines the maximum `quantity` allowed.
* `stepSize` defines the intervals that a `quantity` can be increased/decreased by.

In order to pass the `market lot size`, the following must be true for `quantity`:

* `quantity` >= `minQty`
* `quantity` <= `maxQty`
* `quantity` % `stepSize` == 0

**/exchangeInfo format:**
```javascript
{
  "filterType": "MARKET_LOT_SIZE",
  "minQty": "0.00100000",
  "maxQty": "100000.00000000",
  "stepSize": "0.00100000"
}
```

### MAX_NUM_ORDERS
The `MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on a symbol.
Note that both "algo" orders and normal orders are counted for this filter.

**/exchangeInfo format:**
```javascript
{
  "filterType": "MAX_NUM_ORDERS",
  "maxNumOrders": 25
}
```

### MAX_NUM_ALGO_ORDERS
The `MAX_NUM_ALGO_ORDERS` filter defines the maximum number of "algo" orders an account is allowed to have open on a symbol.
"Algo" orders are `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.

**/exchangeInfo format:**
```javascript
{
  "filterType": "MAX_NUM_ALGO_ORDERS",
  "maxNumAlgoOrders": 5
}
```

### MAX_NUM_ICEBERG_ORDERS
The `MAX_NUM_ICEBERG_ORDERS` filter defines the maximum number of `ICEBERG` orders an account is allowed to have open on a symbol.
An `ICEBERG` order is any order where the `icebergQty` is > 0.

**/exchangeInfo format:**
```javascript
{
  "filterType": "MAX_NUM_ICEBERG_ORDERS",
  "maxNumIcebergOrders": 5
}
```

### MAX_POSITION

The `MAX_POSITION` filter defines the allowed maximum position an account can have on the base asset of a symbol. An account's position defined as the sum of the account's:
1. free balance of the base asset
1. locked balance of the base asset
1. sum of the qty of all open BUY orders

`BUY` orders will be rejected if the account's position is greater than the maximum position allowed.

If an order's `quantity` can cause the position to overflow, this will also fail the `MAX_POSITION` filter.

**/exchangeInfo format:**
```javascript
{
  "filterType":"MAX_POSITION",
  "maxPosition":"10.00000000"
}
```

### TRAILING_DELTA

The `TRAILING_DELTA` filter defines the minimum and maximum value for the parameter [`trailingDelta`](faqs/trailing-stop-faq.md).

In order for a trailing stop order to pass this filter, the following must be true:

For `STOP_LOSS BUY`, `STOP_LOSS_LIMIT_BUY`,`TAKE_PROFIT SELL` and `TAKE_PROFIT_LIMIT SELL` orders:

* `trailingDelta` >= `minTrailingAboveDelta`
* `trailingDelta` <= `maxTrailingAboveDelta`

For `STOP_LOSS SELL`, `STOP_LOSS_LIMIT SELL`, `TAKE_PROFIT BUY`, and `TAKE_PROFIT_LIMIT BUY` orders:

* `trailingDelta` >= `minTrailingBelowDelta`
* `trailingDelta` <= `maxTrailingBelowDelta`


**/exchangeInfo format:**

```javascript
    {
          "filterType": "TRAILING_DELTA",
          "minTrailingAboveDelta": 10,
          "maxTrailingAboveDelta": 2000,
          "minTrailingBelowDelta": 10,
          "maxTrailingBelowDelta": 2000
   }
```

### MAX_NUM_ORDER_AMENDS

The `MAX_NUM_ORDER_AMENDS` filter defines the maximum number of times an order can be amended on the given symbol.

If there are too many order amendments made on a single order, you will receive the `-2038` error code.

**/exchangeInfo format:**

```javascript
        {
          "filterType": "MAX_NUM_ORDER_AMENDS",
          "maxNumOrderAmends": 10
        }
```

### MAX_NUM_ORDER_LISTS

The `MAX_NUM_ORDER_LISTS` filter defines the maximum number of open order lists an account can have on a symbol. Note that OTOCOs count as one order list.

**/exchangeInfo format:**

```javascript
        {
          "filterType": "MAX_NUM_ORDER_LISTS",
          "maxNumOrderLists": 20
        }
```


## Exchange Filters
### EXCHANGE_MAX_NUM_ORDERS
The `EXCHANGE_MAX_NUM_ORDERS` filter defines the maximum number of orders an account is allowed to have open on the exchange.
Note that both "algo" orders and normal orders are counted for this filter.

**/exchangeInfo format:**
```javascript
{
  "filterType": "EXCHANGE_MAX_NUM_ORDERS",
  "maxNumOrders": 1000
}
```

### EXCHANGE_MAX_NUM_ALGO_ORDERS
The `EXCHANGE_MAX_NUM_ALGO_ORDERS` filter defines the maximum number of "algo" orders an account is allowed to have open on the exchange.
"Algo" orders are `STOP_LOSS`, `STOP_LOSS_LIMIT`, `TAKE_PROFIT`, and `TAKE_PROFIT_LIMIT` orders.

**/exchangeInfo format:**
```javascript
{
  "filterType": "EXCHANGE_MAX_NUM_ALGO_ORDERS",
  "maxNumAlgoOrders": 200
}
```

### EXCHANGE_MAX_NUM_ICEBERG_ORDERS
The `EXCHANGE_MAX_NUM_ICEBERG_ORDERS` filter defines the maximum number of iceberg orders an account is allowed to have open on the exchange.

**/exchangeInfo format:**
```javascript
{
  "filterType": "EXCHANGE_MAX_NUM_ICEBERG_ORDERS",
  "maxNumIcebergOrders": 10000
}
```

### EXCHANGE_MAX_NUM_ORDER_LISTS

The `EXCHANGE_MAX_NUM_ORDERS` filter defines the maximum number of order lists an account is allowed to have open on the exchange. Note that OTOCOs count as one order list.

**/exchangeInfo format:**

```javascript
   {
      "filterType": "EXCHANGE_MAX_NUM_ORDER_LISTS",
      "maxNumOrderLists": 20
    }
```


## Asset Filters
### MAX_ASSET

The `MAX_ASSET` filter defines the maximum quantity of an asset that an account is allowed to transact in a single order.

* When the asset is a symbol's base asset, the limit applies to the order's quantity.
* When the asset is a symbol's quote asset, the limit applies to the order's notional value.
* For example, a MAX_ASSET filter for USDC applies to all symbols that have USDC as either a base or quote asset, such as:
  * USDCBNB
  * BNBUSDC

**/myFilters format:**

```javascript
   {
      "filterType": "MAX_ASSET",
      "asset": "USDC",
      "limit": "42.00000000"
    }
```
# Error codes for Binance

Errors consist of two parts: an error code and a message. Codes are universal,
 but messages can vary. Here is the error JSON payload:
```javascript
{
  "code":-1121,
  "msg":"Invalid symbol."
}
```

## 10xx - General Server or Network issues
### -1000 UNKNOWN
 * An unknown error occurred while processing the request.

### -1001 DISCONNECTED
 * Internal error; unable to process your request. Please try again.

### -1002 UNAUTHORIZED
 * You are not authorized to execute this request.

### -1003 TOO_MANY_REQUESTS
 * Too many requests queued.
 * Too much request weight used; current limit is %s request weight per %s. Please use WebSocket Streams for live updates to avoid polling the API.
 * Way too much request weight used; IP banned until %s. Please use WebSocket Streams for live updates to avoid bans.

### -1006 UNEXPECTED_RESP
 * An unexpected response was received from the message bus. Execution status unknown.

### -1007 TIMEOUT
 * Timeout waiting for response from backend server. Send status unknown; execution status unknown.

### -1008 SERVER_BUSY
  * Server is currently overloaded with other requests. Please try again in a few minutes.

### -1013 INVALID_MESSAGE
  * The request is rejected by the API. (i.e. The request didn't reach the Matching Engine.)
  * Potential error messages can be found in [Filter Failures](#filter-failures) or [Failures during order placement](#other-errors).

### -1014 UNKNOWN_ORDER_COMPOSITION
 * Unsupported order combination.

### -1015 TOO_MANY_ORDERS
 * Too many new orders.
 * Too many new orders; current limit is %s orders per %s.

### -1016 SERVICE_SHUTTING_DOWN
 * This service is no longer available.

### -1020 UNSUPPORTED_OPERATION
 * This operation is not supported.

### -1021 INVALID_TIMESTAMP
 * Timestamp for this request is outside of the recvWindow.
 * Timestamp for this request was 1000ms ahead of the server's time.

### -1022 INVALID_SIGNATURE
 * Signature for this request is not valid.

### -1033 COMP_ID_IN_USE
 * `SenderCompId(49)` is currently in use. Concurrent use of the same SenderCompId within one account is not allowed.

### -1034 TOO_MANY_CONNECTIONS
 * Too many concurrent connections; current limit is '%s'.
 * Too many connection attempts for account; current limit is %s per '%s'.
 * Too many connection attempts from IP; current limit is %s per '%s'.

### -1035 LOGGED_OUT
 * Please send [Logout`<5>`](fix-api.md#logout) message to close the session.

## 11xx - Request issues
### -1100 ILLEGAL_CHARS
 * Illegal characters found in a parameter.
 * Illegal characters found in parameter '%s'; legal range is '%s'.

### -1101 TOO_MANY_PARAMETERS
 * Too many parameters sent for this endpoint.
 * Too many parameters; expected '%s' and received '%s'.
 * Duplicate values for a parameter detected.

### -1102 MANDATORY_PARAM_EMPTY_OR_MALFORMED
 * A mandatory parameter was not sent, was empty/null, or malformed.
 * Mandatory parameter '%s' was not sent, was empty/null, or malformed.
 * Param '%s' or '%s' must be sent, but both were empty/null!
 * Required tag '%s' missing.
 * Field value was empty or malformed.
 * '%s' contains unexpected value. Cannot be greater than %s.

### -1103 UNKNOWN_PARAM
 * An unknown parameter was sent.
 * Undefined Tag.

### -1104 UNREAD_PARAMETERS
 * Not all sent parameters were read.
 * Not all sent parameters were read; read '%s' parameter(s) but was sent '%s'.

### -1105 PARAM_EMPTY
 * A parameter was empty.
 * Parameter '%s' was empty.

### -1106 PARAM_NOT_REQUIRED
 * A parameter was sent when not required.
 * Parameter '%s' sent when not required.
 * A tag '%s' was sent when not required.

### -1108 PARAM_OVERFLOW
 * Parameter '%s' overflowed.

### -1111 BAD_PRECISION
 * Parameter '%s' has too much precision.

### -1112 NO_DEPTH
 * No orders on book for symbol.

### -1114 TIF_NOT_REQUIRED
 * TimeInForce parameter sent when not required.

### -1115 INVALID_TIF
 * Invalid timeInForce.

### -1116 INVALID_ORDER_TYPE
 * Invalid orderType.

### -1117 INVALID_SIDE
 * Invalid side.

### -1118 EMPTY_NEW_CL_ORD_ID
 * New client order ID was empty.

### -1119 EMPTY_ORG_CL_ORD_ID
 * Original client order ID was empty.

### -1120 BAD_INTERVAL
 * Invalid interval.

### -1121 BAD_SYMBOL
 * Invalid symbol.

### -1122 INVALID_SYMBOLSTATUS
  * Invalid symbolStatus.

### -1125 INVALID_LISTEN_KEY
 * This listenKey does not exist.

### -1127 MORE_THAN_XX_HOURS
 * Lookup interval is too big.
 * More than %s hours between startTime and endTime.

### -1128 OPTIONAL_PARAMS_BAD_COMBO
 * Combination of optional parameters invalid.
 * Combination of optional fields invalid. Recommendation: '%s' and '%s' must both be sent.
 * Fields [%s] must be sent together or omitted entirely.
 * Invalid `MDEntryType (269)` combination. BID and OFFER must be requested together.
 * Conflicting fields: ['%s'...]

### -1130 INVALID_PARAMETER
 * Invalid data sent for a parameter.
 * Data sent for parameter '%s' is not valid.

### -1134 BAD_STRATEGY_TYPE
 * `strategyType` was less than 1000000.
 * `TargetStrategy (847)` was less than 1000000.

### -1135 INVALID_JSON
 * Invalid JSON Request
 * JSON sent for parameter '%s' is not valid

### -1139 INVALID_TICKER_TYPE
 * Invalid ticker type.

### -1145 INVALID_CANCEL_RESTRICTIONS
 * `cancelRestrictions` has to be either `ONLY_NEW` or `ONLY_PARTIALLY_FILLED`.

### -1151 DUPLICATE_SYMBOLS
 * Symbol is present multiple times in the list.

### -1152 INVALID_SBE_HEADER
* Invalid `X-MBX-SBE` header; expected `<SCHEMA_ID>:<VERSION>`.
* Invalid SBE message header.

### -1153 UNSUPPORTED_SCHEMA_ID
* Unsupported SBE schema ID or version specified in the `X-MBX-SBE` header.
* Invalid SBE schema ID or version specified.

### -1155 SBE_DISABLED
* SBE is not enabled.

### -1158 OCO_ORDER_TYPE_REJECTED
* Order type not supported in OCO.
* If the order type provided in the `aboveType` and/or `belowType` is not supported.

### -1160 OCO_ICEBERGQTY_TIMEINFORCE
* Parameter '%s' is not supported if `aboveTimeInForce`/`belowTimeInForce` is not GTC.
* If the order type for the above or below leg is `STOP_LOSS_LIMIT`, and `icebergQty` is provided for that leg, the `timeInForce` has to be `GTC` else it will throw an error.
* `TimeInForce (59)` must be `GTC (1)` when `MaxFloor (111)` is used.

### -1161 DEPRECATED_SCHEMA
* Unable to encode the response in SBE schema 'x'. Please use schema 'y' or higher.

### -1165 BUY_OCO_LIMIT_MUST_BE_BELOW
* A limit order in a buy OCO must be below.

### -1166 SELL_OCO_LIMIT_MUST_BE_ABOVE
* A limit order in a sell OCO must be above.

### -1168 BOTH_OCO_ORDERS_CANNOT_BE_LIMIT
* At least one OCO order must be contingent.

### -1169 INVALID_TAG_NUMBER
 * Invalid tag number.

### -1170 TAG_NOT_DEFINED_IN_MESSAGE
 * Tag '%s' not defined for this message type.

### -1171 TAG_APPEARS_MORE_THAN_ONCE
 * Tag '%s' appears more than once.

### -1172 TAG_OUT_OF_ORDER
 * Tag '%s' specified out of required order.

### -1173 GROUP_FIELDS_OUT_OF_ORDER
 * Repeating group '%s' fields out of order.

### -1174 INVALID_COMPONENT
 * Component '%s' is incorrectly populated on '%s' order. Recommendation: '%s'

### -1175 RESET_SEQ_NUM_SUPPORT
 * Continuation of sequence numbers to new session is currently unsupported. Sequence numbers must be reset for each new session.

### -1176 ALREADY_LOGGED_IN
 * [Logon`<A>`](fix-api.md#logon-main) should only be sent once.

### -1177 GARBLED_MESSAGE
 * `CheckSum(10)` contains an incorrect value.
 * `BeginString (8)` is not the first tag in a message.
 * `MsgType (35)` is not the third tag in a message.
 * `BodyLength (9)` does not contain the correct byte count.
 * Only printable ASCII characters and SOH (Start of Header) are allowed.
 * Tag specified without a value.
* Invalid encodingType.

### -1178 BAD_SENDER_COMPID
 * `SenderCompId(49)` contains an incorrect value. The SenderCompID value should not change throughout the lifetime of a session.

### -1179 BAD_SEQ_NUM
 * `MsgSeqNum(34)` contains an unexpected value. Expected: '%d'.

### -1180 EXPECTED_LOGON
 * [Logon`<A>`](fix-api.md#logon-main) must be the first message in the session.

### -1181 TOO_MANY_MESSAGES
 * Too many messages; current limit is '%d' messages per '%s'.

### -1182 PARAMS_BAD_COMBO
 * Conflicting fields: [%s]

### -1183 NOT_ALLOWED_IN_DROP_COPY_SESSIONS
 * Requested operation is not allowed in DropCopy sessions.

### -1184 DROP_COPY_SESSION_NOT_ALLOWED
 * DropCopy sessions are not supported on this server. Please reconnect to a drop copy server.

### -1185 DROP_COPY_SESSION_REQUIRED
 * Only DropCopy sessions are supported on this server. Either reconnect to order entry server or send `DropCopyFlag (9406)` field.

### -1186 NOT_ALLOWED_IN_ORDER_ENTRY_SESSIONS
* Requested operation is not allowed in order entry sessions.

### -1187 NOT_ALLOWED_IN_MARKET_DATA_SESSIONS
* Requested operation is not allowed in market data sessions.

### -1188 INCORRECT_NUM_IN_GROUP_COUNT
* Incorrect NumInGroup count for repeating group '%s'.

### -1189 DUPLICATE_ENTRIES_IN_A_GROUP
* Group '%s' contains duplicate entries.

### -1190 INVALID_REQUEST_ID
* `MDReqID (262)` contains a subscription request id that is already in use on this connection.
* `MDReqID (262)` contains an unsubscription request id that does not match any active subscription.

### -1191 TOO_MANY_SUBSCRIPTIONS
* Too many subscriptions. Connection may create up to '%s' subscriptions at a time.
* Similar subscription is already active on this connection. Symbol='%s', active subscription id: '%s'.

### -1194 INVALID_TIME_UNIT
* Invalid value for time unit; expected either MICROSECOND or MILLISECOND.

### -1196 BUY_OCO_STOP_LOSS_MUST_BE_ABOVE
* A stop loss order in a buy OCO must be above.

### -1197 SELL_OCO_STOP_LOSS_MUST_BE_BELOW
* A stop loss order in a sell OCO must be below.

### -1198 BUY_OCO_TAKE_PROFIT_MUST_BE_BELOW
* A take profit order in a buy OCO must be below.

### -1199 SELL_OCO_TAKE_PROFIT_MUST_BE_ABOVE
* A take profit order in a sell OCO must be above.

### -1210 INVALID_PEG_PRICE_TYPE
* Invalid pegPriceType.

### -1211 INVALID_PEG_OFFSET_TYPE
* Invalid pegOffsetType.

### -1220 SYMBOL_DOES_NOT_MATCH_STATUS
* The symbol's status does not match the requested symbolStatus.

### -1221 INVALID_SBE_MESSAGE_FIELD
* Invalid/missing field(s) in SBE message.

### -1222 OPO_WORKING_MUST_BE_BUY

* Working order in an OPO list must be a bid.

### -1223 OPO_PENDING_MUST_BE_SELL

* Pending orders in an OPO list must be asks.

### -1224 WORKING_PARAM_REQUIRED

* Working order must include the '{param}' tag.

### -1225 PENDING_PARAM_NOT_REQUIRED

* Pending orders should not include the '%s' tag.

### -2010 NEW_ORDER_REJECTED
 * NEW_ORDER_REJECTED

### -2011 CANCEL_REJECTED
 * CANCEL_REJECTED

### -2013 NO_SUCH_ORDER
 * Order does not exist.

### -2014 BAD_API_KEY_FMT
 * API-key format invalid.

### -2015 REJECTED_MBX_KEY
 * Invalid API-key, IP, or permissions for action.

### -2016 NO_TRADING_WINDOW
 * No trading window could be found for the symbol. Try ticker/24hrs instead.

### -2026 ORDER_ARCHIVED
  * Order was canceled or expired with no executed qty over 90 days ago and has been archived.

### -2035 SUBSCRIPTION_ACTIVE
  * User Data Stream subscription already active.

### -2036 SUBSCRIPTION_INACTIVE
  * User Data Stream subscription not active.

### -2039 CLIENT_ORDER_ID_INVALID
  * Client order ID is not correct for this order ID.

### -2042 MAXIMUM_SUBSCRIPTION_IDS
* Maximum subscription ID reached for this connection.

<a id="other-errors"></a>

## Messages for -1010 ERROR_MSG_RECEIVED, -2010 NEW_ORDER_REJECTED, -2011 CANCEL_REJECTED, and -2038 ORDER_AMEND_REJECTED
This code is sent when an error has been returned by the matching engine.
The following messages which will indicate the specific error:


Error message                                                   | Description
------------                                                    | ------------
"Unknown order sent."                                           | The order (by either `orderId`, `clOrdId`, `origClOrdId`) could not be found.
"Duplicate order sent."                                         | The `clOrdId` is already in use.
"Market is closed."                                             | The symbol is not trading.
"Account has insufficient balance for requested action."        | Not enough funds to complete the action.
"Market orders are not supported for this symbol."              | `MARKET` is not enabled on the symbol.
"Iceberg orders are not supported for this symbol."             | `icebergQty` is not enabled on the symbol.
"Stop loss orders are not supported for this symbol."           | `STOP_LOSS` is not enabled on the symbol.
"Stop loss limit orders are not supported for this symbol."     | `STOP_LOSS_LIMIT` is not enabled on the symbol.
"Take profit orders are not supported for this symbol."         | `TAKE_PROFIT` is not enabled on the symbol.
"Take profit limit orders are not supported for this symbol."   | `TAKE_PROFIT_LIMIT` is not enabled on the symbol.
"Order amend is not supported for this symbol."                 | Order amend keep priority is not enabled on the symbol.
"Price * QTY is zero or less."                                  | `price` * `quantity` is too low.
"IcebergQty exceeds QTY."                                       | `icebergQty` must be less than the order quantity.
"This action is disabled on this account."                      | Contact customer support; some actions have been disabled on the account.
"This account may not place or cancel orders."                  | Contact customer support; the account has trading ability disabled.
"Unsupported order combination"                                 | The `orderType`, `timeInForce`, `stopPrice`, and/or `icebergQty` combination isn't allowed.
"Order would trigger immediately."                              | The order's stop price is not valid when compared to the last traded price.
"Cancel order is invalid. Check origClOrdId and orderId."       | No `origClOrdId` or `orderId` was sent in.
"Order would immediately match and take."                       | `LIMIT_MAKER` order type would immediately match and trade, and not be a pure maker order.
"The relationship of the prices for the orders is not correct." | The prices set in the `OCO` is breaking the Price restrictions. <br/> For reference: <br/> `BUY` : `LIMIT_MAKER` `price` < Last Traded Price < `stopPrice` <br>`SELL` : `LIMIT_MAKER` `price` > Last Traded Price > `stopPrice`
"OCO orders are not supported for this symbol"                  | `OCO` is not enabled on the symbol.
"Quote order qty market orders are not support for this symbol."| `MARKET` orders using the parameter `quoteOrderQty` are not enabled on the symbol.
"Trailing stop orders are not supported for this symbol."       | Orders using `trailingDelta` are not enabled on the symbol.
"Order cancel-replace is not supported for this symbol."        | `POST /api/v3/order/cancelReplace` (REST API) or `order.cancelReplace` (WebSocket API) is not enabled on the symbol.
"This symbol is not permitted for this account."                | Account and symbol do not have the same permissions. (e.g. `SPOT`, `MARGIN`, etc)
"This symbol is restricted for this account."                   | Account is unable to trade on that symbol. (e.g. An `ISOLATED_MARGIN` account cannot place `SPOT` orders.)
"Order was not canceled due to cancel restrictions."            | Either `cancelRestrictions` was set to `ONLY_NEW` but the order status was not `NEW` <br/> or <br/> `cancelRestrictions` was set to `ONLY_PARTIALLY_FILLED` but the order status was not `PARTIALLY_FILLED`.
"Rest API trading is not enabled." / "WebSocket API trading is not enabled." | Order is being placed or a server that is not configured to allow access to `TRADE` endpoints.
"FIX API trading is not enabled.                                | Order is placed on a FIX server that is not TRADE enabled.
"Order book liquidity is less than `LOT_SIZE` filter minimum quantity." |Quote quantity market orders cannot be placed when the order book liquidity is less than minimum quantity configured for the `LOT_SIZE` filter.
"Order book liquidity is less than `MARKET_LOT_SIZE` filter minimum quantity."|Quote quantity market orders cannot be placed when the order book liquidity is less than the minimum quantity for `MARKET_LOT_SIZE` filter.
"Order book liquidity is less than symbol minimum quantity." | Quote quantity market orders cannot be placed when there are no orders on the book.
"Order amend (quantity increase) is not supported." | `newQty` must be less than the order quantity.
"The requested action would change no state; rejecting". | The request sent would not have changed the status quo.<br></br>(e.g. `newQty` cannot equal the order quantity.)
"Pegged orders are not supported for this symbol." | `pegInstructionsAllowed` has not been enabled. |
"This order type may not use pegged price." | You are using parameter `pegPriceType` with an unsupported order type. (e.g. `MARKET`) |
"This price peg cannot be used with this order type." | You are using `pegPriceType`=`MARKET_PEG` for a `LIMIT_MAKER` order.|
"Order book liquidity is too low for this pegged order." | The order book doesn’t have the best price level to peg the price to. |
| OPO orders are not supported for this symbol. |  |
| Order amend (pending OPO order) is not supported. | You cannot amend the pending quantity of an OPO order |

## Errors regarding placing orders via cancelReplace

### -2021 Order cancel-replace partially failed
* This code is sent when either the cancellation of the order failed or the new order placement failed but not both.

### -2022 Order cancel-replace failed.
* This code is sent when both the cancellation of the order failed and the new order placement failed.

<a id="filter_failures"></a>

## Filter failures
Error message | Description
------------ | ------------
"Filter failure: PRICE_FILTER" | `price` is too high, too low, and/or not following the tick size rule for the symbol.
"Filter failure: PERCENT_PRICE" | `price` is X% too high or X% too low from the average weighted price over the last Y minutes.
"Filter failure: LOT_SIZE" | `quantity` is too high, too low, and/or not following the step size rule for the symbol.
"Filter failure: MIN_NOTIONAL" | `price` * `quantity` is too low to be a valid order for the symbol.
"Filter failure: NOTIONAL"    | `price` * `quantity` is not within range of the `minNotional` and `maxNotional`
"Filter failure: ICEBERG_PARTS" | `ICEBERG` order would break into too many parts; icebergQty is too small.
"Filter failure: MARKET_LOT_SIZE" | `MARKET` order's `quantity` is too high, too low, and/or not following the step size rule for the symbol.
"Filter failure: MAX_POSITION" | The account's position has reached the maximum defined limit. <br/> This is composed of the sum of the balance of the base asset, and the sum of the quantity of all open `BUY` orders.
"Filter failure: MAX_NUM_ORDERS" | Account has too many open orders on the symbol.
"Filter failure: MAX_NUM_ALGO_ORDERS" | Account has too many open stop loss and/or take profit orders on the symbol.
"Filter failure: MAX_NUM_ICEBERG_ORDERS" | Account has too many open iceberg orders on the symbol.
"Filter failure: MAX_NUM_ORDER_AMENDS" | Account has made too many amendments to a single order on the symbol.
"Filter failure: MAX_NUM_ORDER_LISTS" | Account has too many open order lists on the symbol. |
"Filter failure: TRAILING_DELTA" | `trailingDelta` is not within the defined range of the filter for that order type.
"Filter failure: EXCHANGE_MAX_NUM_ORDERS" | Account has too many open orders on the exchange.
"Filter failure: EXCHANGE_MAX_NUM_ALGO_ORDERS" | Account has too many open stop loss and/or take profit orders on the exchange.
"Filter failure: EXCHANGE_MAX_NUM_ICEBERG_ORDERS" | Account has too many open iceberg orders on the exchange.
"Filter failure: EXCHANGE_MAX_NUM_ORDER_LISTS" | Account has too many open order lists on the exchange.
