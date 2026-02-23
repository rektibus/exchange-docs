# Bitstamp API Documentation

Source: Official Bitstamp OpenAPI Spec (bitstamp.json)

## Bitstamp Public API

# What is API?
Bitstamp application programming interface (API) allows our clients to access and control their accounts, using custom
written software.

# Response codes
Response code is a key that can be appended to an API response as **response_code** (string). Additionally, also
explanation may or may not be included as the **response_explanation** (string) key, which defines further explanation
to what has gone wrong when processing a request.

Below is the list of all available response codes and it's explanations:
| response_code | response_explanation (optional) |
| ----------- | ----------- |
| 400.001 | Unknown validation error. |
| 400.002 | Request rejected due to exceeded rate limit. |
| 400.003 | Trading for provided market is disabled. |
| 400.004 | POST parameter(s) is missing from request. |
| 400.005 | POST parameter(s) is missing from request: amount. |
| 400.006 | POST parameter(s) is missing from request: price. |
| 400.007 | POST parameter(s) is malformed. |
| 400.008 | POST parameter(s) is malformed: client_order_id. |
| 400.009 | Insufficient balance for provided user. |
| 400.010 | POST parameter(s) is malformed: offset. |
| 400.011 | POST parameter(s) is malformed: limit. |
| 400.012 | POST parameter(s) is malformed: sort. |
| 400.013 | POST parameter(s) is malformed: since_timestamp. |
| 400.014 | POST parameter(s) is missing from request: order_id. |
| 400.015 | POST parameter(s) is missing from request: client_order_id. |
| 400.016 | POST parameter(s) is malformed: order_id. |
| 400.017 | POST parameter(s) is malformed: client_cancel_id. |
| 400.018 | GET parameters not allowed for this request. |
| 400.019 | Provided client_order_id already exists. |
| 400.020 | Provided order size is lower than minimum order value. |
| 400.021 | Provided price is out of range. |
| 400.022 | POST parameter(s) is missing from request: expire_time. |
| 400.023 | POST parameter(s) is malformed: expire_time. |
| 400.024 | Only one of optional parameters can be set. |
| 400.025 | Both limit_price and any optional parameter cannot be set. |
| 400.026 | POST parameter(s) is malformed: amount. |
| 400.027 | Sell if executed price must be higher than buy price. |
| 400.028 | Buy if executed price must be lower than sell price. |
| 400.029 | 'stop_order_id' is None. |
| 400.030 | 'stop_order_price' is None. |
| 400.031 | 'expire_time' is None. |
| 400.032 | 'expire_time' must be set in future date. |
| 400.033 | 'expire_time' must be None. |
| 400.034 | POST parameter(s) is malformed: until_timestamp. |
| 400.035 | POST parameter(s) is missing from request: id. |
| 400.036 | POST parameter(s) is malformed: id. |
| 400.037 | Provided order size is too large. |
| 400.038 | Provided order amount is too large. |
| 400.039 | Provided order size is higher than maximum order value. |
| 400.040 | Provided leverage differs from ones on open orders. |
| 400.041 | POST parameter(s) is malformed: price. |
| 400.042 | Position management mode already active |
| 400.043 | No positions present |
| 400.044 | POST parameter(s) is malformed: leverage. |
| 400.045 | Open orders present. |
| 400.046 | Provided order amount is too low. |
| 400.047 | POST parameter(s) is malformed: stop_price. |
| 400.048 | POST parameter(s) is malformed: activation_price. |
| 400.049 | POST parameter(s) is missing: subtype. |
| 400.050 | POST parameter(s) is missing: trigger. |
| 400.051 | POST parameter(s) is missing: reduce_only. |
| 400.052 | Too many stop orders on market. |
| 400.053 | Too many trailing stop orders on trade account. |
| 400.054 | Invalid value for trailing_delta. |
| 400.055 | Current price is lower than order price. |
| 400.056 | Current price is higher than order price. |
| 400.057 | Reduce only not supported with provided order parameters. |
| 400.058 | Only GTC, FOK and IOC time in force allowed for take profit and stop loss orders. |
| 400.059 | Either stop price or trailing price with trailing delta must be specified. |
| 400.060 | Trailing delta is required for activation price. |
| 400.061 | Date range exceeds limit. |
| 400.062 | Position not found. |
| 400.063 | Leverage not allowed. |
| 400.064 | Collateral not allowed. |
| 400.065 | Price should be less than 20% above trigger price. |
| 400.066 | Price should be less than 20% below trigger price. |
| 400.067 | Request rejected due to exceeded client rate limit. |
| 400.068 | Request rejected due to exceeded market rate limit. |
| 400.069 | Slippage tolerance is not supported for this order type. |
| 400.070 | Price should be less than 500% of trigger price. |
| 400.071 | Price should be less than 80% below trigger price. |
| 400.072 | At least one of POST parameters must be set in request: id, orig_client_order_id. |
| 400.073 | POST parameter(s) is malformed: orig_client_order_id. |
| 400.074 | Modification rejected: leverage, margin_mode, and reduce_only fields cannot be updated once the order is created |
| 400.075 | Insufficient margin for provided user. |
| 400.076 | Failed to close position due to order size limitations. You should close this position by placing orders instead. |
| 400.077 | Reduced leverage state active. You have to reduce your leverage to place this order. |
| 400.078 | POST parameter(s) is missing from request: order_source. |
| 400.079 | POST parameter(s) is missing from request: market. |
| 400.080 | POST parameter(s) is malformed: order_source. |
| 400.081 | POST parameter(s) is malformed: since_id. |
| 400.082 | POST parameter(s) is malformed: until_id. |
| 400.083 | Event ID market mismatch: event ID does not match requested market. |
| 400.084 | Event ID source mismatch: event ID does not match requested order source. |
| 400.085 | Invalid event ID range: until_id must be greater than since_id. |
| 403.001 | User verification failed. |
| 403.002 | Trading is not allowed on lending account. |
| 403.003 | Trading is not allowed on collateral account. |
| 403.004 | Trading is blocked for user. |
| 403.005 | Action not allowed at cross margin mode. |
| 403.006 | Trading of this market type is not allowed on trade account. |
| 403.007 | Position in liquidation. |
| 403.008 | Account in liquidation. |
| 403.009 | Maximum number of positions on system exceeded. |
| 403.010 | The maximum size of open orders and positions on the market reached. |
| 404.001 | Unknown not found error. |
| 404.002 | Order not found for corresponding request. |
| 404.003 | Currency pair not found for corresponding request. |
| 404.004 | Trade account not found for provided API key. |
| 404.005 | Order book not found. |
| 404.006 | Currency not found for corresponding request. |
| 404.007 | Market not found for corresponding request. |
| 404.008 | No events found for the provided parameters. |
| 405.001 | GET method not allowed. |
| 410.001 | Requested endpoint is deprecated. |
| 500.001 | Unknown server error. |
| 500.002 | One of Bitstamp internal services failed to process request. |
| 500.003 | Unknown error while processing order. |
| 500.004 | No sell orders for provided market. |
| 500.005 | No buy orders for provided market. |
| 500.006 | Cash sell order types are currently disabled. |
| 500.007 | Error while serializing data. |
| 500.008 | Margin option for provided market is disabled. |
| 500.009 | Order book is currently unavailable. |
| 500.010 | Instant trading for provided market is disabled. |
| 500.011 | Market trading for provided market is disabled. |
| 500.012 | Matching blocked for this order book. |
| 500.013 | Unknown matching engine error. |
| 500.014 | Cash order for provided market is disabled. |
| 500.015 | Cannot place order. There are currently no orders for provided market. |
| 500.016 | Your request timed out before order confirmation. Please check order status with id in "order_id" field. |
| 500.017 | Order rejected by matching engine. |
| 500.018 | No orders for provided market. |
| 500.019 | Error at canceling orders |
| 500.020 | Pre reserved orders present |
| 500.021 | Post reserved orders present |
| 500.022 | More than one position present |
| 500.023 | Position management order not filled |

# Request limits
As standard, all clients can make 400 requests per second. There is a default limit threshold of 10,000 requests per 10
minutes in place. The rate limits mentioned above can be increased upon request and the client entering a bespoke
agreement with Bitstamp. For real time data please refer to the
[**websocket API**](https://www.bitstamp.net/websocket/v2/).

## Commercial Use of Bitstamp's Exchange Data
Companies seeking to utilize Bitstamp's exchange data for their own commercial purposes are directed to contact
partners@bitstamp.net to receive and sign a commercial use Data License Agreement.

Bitstamp allows the incorporation and redistribution of our exchange data for commercial purposes.
This includes the right to create ratios, calculations, new original works, statistics, and similar, based on the
exchange data.

# Authentication

All private API calls require authentication. For a successful authentication you need to provide the following
authorization headers in your request:

## Possible authentication errors
<table>
<thead><th>Code</th><th>Reason</th><th>Action</th></thead>
<tbody>
<tr><td><strong>API0001</strong></td><td>API key not found</td><td>Check your API key value.</td></tr>
<tr><td><strong>API0002</strong></td><td>IP address not allowed</td><td>This IP address has no permission to use this API key.</td></tr>
<tr><td><strong>API0003</strong></td><td>No permission found</td><td>API key doesn't have permission for calling this api endpoint.</td></tr>
<tr><td><strong>API0004</strong></td><td>Invalid nonce</td><td>Check your nonce value. It must be different than last nonce used in the last 300 seconds.</td></tr>
<tr><td><strong>API0005</strong></td><td>Invalid signature</td><td>Posted signature doesn't match with ours.</td></tr>
<tr><td><strong>API0006</strong></td><td>Your account is frozen</td><td>Contact support to unfreeze your account.</td></tr>
<tr><td><strong>API0008</strong></td><td>Authentication failed</td><td>Can't find customer with selected API key.</td></tr>
<tr><td><strong>API0009</strong></td><td>Please update your profile with your FATCA information, before using API.</td><td>Check that you filled out the FATCA information form on your account.</td></tr>
<tr><td><strong>API0010</strong></td><td>Invalid version</td><td>Check that you send "v2" in the version authorization header.</td></tr>
<tr><td><strong>API0011</strong></td><td>Wrong API key format</td><td>Check that your API key string is correct.</td></tr>
<tr><td><strong>API0012</strong></td><td>X-Auth header is required</td><td>X-Auth header is probably missing in your request.</td></tr>
<tr><td><strong>API0013</strong></td><td>X-Auth-Signature header is required</td><td>X-Auth-Signature header is probably missing in your request.</td></tr>
<tr><td><strong>API0014</strong></td><td>X-Auth-Nonce header is required</td><td>X-Auth-Nonce header is probably missing in your request.</td></tr>
<tr><td><strong>API0015</strong></td><td>X-Auth-Timestamp header is required</td><td>X-Auth-Timestamp header is probably missing in your request.</td></tr>
<tr><td><strong>API0016</strong></td><td>X-Auth-Version header is required</td><td>X-Auth-Version header is probably missing in your request.</td></tr>
<tr><td><strong>API0017</strong></td><td>X-Auth-Timestamp header is out of boundaries</td><td>Timestamp you added in the header is either too old or too new. Check that timestamp is within 150 second timeframe.</td></tr>
<tr><td><strong>API0018</strong></td><td>X-Auth-Timestamp header is invalid</td><td>Check the format of X-Auth-Timestamp header.</td></tr>
<tr><td><strong>API0019</strong></td><td>Content-Type header is not accepted</td><td>Please specify the correct content type.</td></tr>
<tr><td><strong>API0020</strong></td><td>Content-Type header should not be present</td><td>Please make sure you're not sending any body in the request.</td></tr>
<tr><td><strong>API0021</strong></td><td>Please make sure url query string is not too long</td><td>Please make sure the total length of the url does not exceed 2000 characters.</td></tr>
</tbody>
</table>
<SecurityDefinitions />

## Authentication examples
**Note:** if the request body is empty, the Content-Type header has to be removed both from the headers and from the
signature

<div class="api__code mb48">
    <div class="api__code-header">
        <span>Python</span>
        <span class="icon icon--code"></span>
    </div>

```python
import hashlib
import hmac
import time
import requests
import uuid
import sys
from urllib.parse import urlencode

api_key = 'api_key'
API_SECRET = b'api_key_secret'

timestamp = str(int(round(time.time() * 1000)))
nonce = str(uuid.uuid4())
content_type = 'application/x-www-form-urlencoded'
payload = {'offset': '1'}

payload_string = urlencode(payload)

# '' (empty string) in message represents any query parameters or an empty string in case there are none
message = 'BITSTAMP ' + api_key + \
    'POST' + \
    'www.bitstamp.net' + \
    '/api/v2/user_transactions/' + \
    '' + \
    content_type + \
    nonce + \
    timestamp + \
    'v2' + \
    payload_string
message = message.encode('utf-8')
signature = hmac.new(API_SECRET, msg=message, digestmod=hashlib.sha256).hexdigest()
headers = {
    'X-Auth': 'BITSTAMP ' + api_key,
    'X-Auth-Signature': signature,
    'X-Auth-Nonce': nonce,
    'X-Auth-Timestamp': timestamp,
    'X-Auth-Version': 'v2',
    'Content-Type': content_type
}
r = requests.post(
    'https://www.bitstamp.net/api/v2/user_transactions/',
    headers=headers,
    data=payload_string
    )
if not r.status_code == 200:
    raise Exception('Status code not 200')

string_to_sign = (nonce + timestamp + r.headers.get('Content-Type')).encode('utf-8') + r.content
signature_check = hmac.new(API_SECRET, msg=string_to_sign, digestmod=hashlib.sha256).hexdigest()
if not r.headers.get('X-Server-Auth-Signature') == signature_check:
    raise Exception('Signatures do not match')

print(r.content)


```

</div>
<div class="api__code mb48">
    <div class="api__code-header">
        <span>Java</span>
        <span class="icon icon--code"></span>
    </div>

```java
package com.example.AuthenticationExample;

import org.apache.commons.codec.binary.Hex;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.UUID;

public class Authentication {
    public static void main(String[] args) {
        String apiKey = String.format("%s %s", "BITSTAMP", "api_key");
        String apiKeySecret = "api_key_secret";
        String httpVerb = "POST";
        String urlHost = "www.bitstamp.net";
        String urlPath = "/api/v2/user_transactions/";
        String urlQuery = "";
        String timestamp = String.valueOf(System.currentTimeMillis());
        String nonce = UUID.randomUUID().toString();
        String contentType = "application/x-www-form-urlencoded";
        String version = "v2";
        String payloadString = "offset=1";
        String signature = apiKey +
            httpVerb +
            urlHost +
            urlPath +
            urlQuery +
            contentType +
            nonce +
            timestamp +
            version +
            payloadString;

        try {
            SecretKeySpec secretKey = new SecretKeySpec(apiKeySecret.getBytes(), "HmacSHA256");
            Mac mac = Mac.getInstance("HmacSHA256");
            mac.init(secretKey);
            byte[] rawHmac = mac.doFinal(signature.getBytes());
            signature = new String(Hex.encodeHex(rawHmac)).toUpperCase();

            HttpClient client = HttpClient.newHttpClient();
            HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://www.bitstamp.net/api/v2/user_transactions/"))
                .POST(HttpRequest.BodyPublishers.ofString(payloadString))
                .setHeader("X-Auth", apiKey)
                .setHeader("X-Auth-Signature", signature)
                .setHeader("X-Auth-Nonce", nonce)
                .setHeader("X-Auth-Timestamp", timestamp)
                .setHeader("X-Auth-Version", version)
                .setHeader("Content-Type", contentType)
                .build();

            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            if (response.statusCode() != 200) {
                throw new RuntimeException("Status code not 200");
            }

            String serverSignature = response.headers().map().get("x-server-auth-signature").get(0);
            String responseContentType = response.headers().map().get("Content-Type").get(0);
            String stringToSign = nonce + timestamp + responseContentType + response.body();

            mac.init(secretKey);
            byte[] rawHmacServerCheck = mac.doFinal(stringToSign.getBytes());
            String newSignature = new String(Hex.encodeHex(rawHmacServerCheck));

            if (!newSignature.equals(serverSignature)) {
                throw new RuntimeException("Signatures do not match");
            }

            System.out.println(response.body());

        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}


```

</div>
<div class="api__code mb48">
    <div class="api__code-header">
        <span>C++</span>
        <span class="icon icon--code"></span>
    </div>

```cpp
#include <curl/curl.h>
#include <openssl/hmac.h>
#include <uuid/uuid.h>

#include <iostream>
#include <string>
#include <chrono>
#include <iomanip>

static size_t write_call_back(void *contents, size_t size, size_t nmemb, void *userp)
{
    ((std::string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

std::string b2a_hex(char *byte_arr, int n)
{
    const static std::string hex_codes = "0123456789abcdef";
    std::string hex_string;
    for ( int i = 0; i < n ; ++i ) {
        unsigned char bin_value = byte_arr[i];
        hex_string += hex_codes[( bin_value >> 4 ) & 0x0F];
        hex_string += hex_codes[bin_value & 0x0F];
    }
    return hex_string;
}

std::string url_encode(std::string data)
{
    std::string res = data;
    CURL *curl = curl_easy_init();

    if(curl) {
        char *output = curl_easy_escape(curl, data.c_str(), data.length());
        if(output) {
            res = output;
            curl_free(output);
        }
    }

    return res;
}


int main() {

    const std::string api_key = "api_key";
    const std::string api_secret = "api_key_secret";

    std::chrono::milliseconds timestamp = std::chrono::duration_cast< std::chrono::milliseconds >(
            std::chrono::system_clock::now().time_since_epoch()
    );

    uuid_t uuid;
    uuid_string_t nonce;
    uuid_generate(uuid);
    uuid_unparse_lower(uuid, nonce);

    std::string x_auth = "BITSTAMP " + api_key;
    std::string x_auth_nonce = nonce;
    std::string x_auth_timestamp = std::to_string(timestamp.count());
    std::string x_auth_version = "v2";
    std::string content_type = "application/x-www-form-urlencoded";
    std::string payload = url_encode("{offset:1}");

    std::string http_method = "POST";
    std::string url_host = "www.bitstamp.net";
    std::string url_path = "/api/v2/user_transactions/";
    std::string url_query = "";

    std::string data_to_sign = "";
    data_to_sign.append(x_auth);
    data_to_sign.append(http_method);
    data_to_sign.append(url_host);
    data_to_sign.append(url_path);
    data_to_sign.append(url_query);
    data_to_sign.append(content_type);
    data_to_sign.append(x_auth_nonce);
    data_to_sign.append(x_auth_timestamp);
    data_to_sign.append(x_auth_version);
    data_to_sign.append(payload);

    // calculate hmac signature
    unsigned char* result;
    unsigned int len = 20;
    result = (unsigned char*)malloc(sizeof(char) * len);

    HMAC_CTX ctx;
    HMAC_CTX_init(&ctx);

    HMAC_Init_ex(&ctx, api_secret.c_str(), api_secret.length(), EVP_sha256(), NULL);
    HMAC_Update(&ctx, (unsigned char*)data_to_sign.c_str(), data_to_sign.length());
    HMAC_Final(&ctx, result, &len);
    HMAC_CTX_cleanup(&ctx);

    std::string x_auth_signature = b2a_hex( (char *)result, 32 );
    free(result);

    // send request
    CURL *curl;
    CURLcode res;
    std::string read_buffer;

    curl = curl_easy_init();

    if(curl) {

        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, ("X-Auth: " + x_auth).c_str());
        headers = curl_slist_append(headers, ("X-Auth-Signature: " + x_auth_signature).c_str());
        headers = curl_slist_append(headers, ("X-Auth-Nonce: " + x_auth_nonce).c_str());
        headers = curl_slist_append(headers, ("X-Auth-Timestamp: " + x_auth_timestamp).c_str());
        headers = curl_slist_append(headers, ("X-Auth-Version: " + x_auth_version).c_str());
        headers = curl_slist_append(headers, ("Content-Type: " + content_type).c_str());

        std::string url = "https://" + url_host + url_path + url_query;

        curl_easy_setopt(curl, CURLOPT_URL, url.c_str());
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, payload.c_str());
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, write_call_back);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &read_buffer);

        res = curl_easy_perform(curl);

        if(res != CURLE_OK) {
            std::cout << "curl_easy_perform() failed: " << curl_easy_strerror(res) << std::endl;
        }

        std::cout << "curl_easy_perform() response: " << read_buffer << std::endl;

        curl_easy_cleanup(curl);

    }

    return 0;

}


```

</div>

# Changelog

### 2026-02-16

* Introduced new order data endpoints for WebSocket gap recovery:
    * `POST /api/v2/order_data/`: Retrieve historical public order events for a specific market.
    * `POST /api/v2/account_order_data/`: Retrieve historical order events for authenticated user's account.

### 2026-02-05

* Introduced a new replace order endpoint:
    * `POST /api/v2/replace_order/`: Replace existing order.

### 2025-10-23

* Cancel Order endpoint enhancement
  * The `POST /api/v2/cancel_order/` endpoint’s successful response payload now includes a new field: `{ "status": Cancel pending }`
  * Status values:
    * Canceled — indicates the order was successfully canceled.
    * Cancel pending — indicates a repeated cancel request while cancellation is still in progress; the API returns HTTP 200 OK immediately with this status.

### 2025-06-16

* Derivatives related private endpoints
  * see all endpoints under the Derivatives section
  * derivatives added to order related endpoints
  * `GET api/v2/trade_history/` added for derivatives under Orders
  * `POST api/v2/get_max_order_amount/` added for derivatives under Orders
* Derivatives related public endpoints
  * new endpoint `GET api/v2/funding_rate_history/{market_symbol}/`
  * new endpoint `GET api/v2/funding_rate/{market_symbol}/`
  * derivatives markets are being returned on public endpoints like  `api/v2/ticker/{market_symbol}/`  and  `api/v2/markets/`

### 2024-12-04

* Updated withdrawal endpoints:
  * Crypto withdrawals subject to Travel rule may require address verification

### 2024-11-20

* Updated Contacts endpoint:
  * `POST /api/v2/travel_rule/contacts`: Fields **retail_info.first_name** and **retail_info.last_name** are now required.

### 2024-10-15

* `GET /api/v2/trading-pairs-info/` is obsolete and replaced by endpoint `api/v2/markets/`
  * We will no longer guarantee `/api/v2/trading-pairs-info/` to work after Dec 31st 2024
* Added new error code API5012 to `/api/v2/earn/unsubscribe/`
* `GET /api/v2/currencies/` has been extended with the following information:
  * networks: which blockchains are supported for withdrawals, minimum withdrawal amounts, deposits, decimal precision and status per blockchain

### 2024-07-17

* Updated descriptions for Ripple IOU endpoint by adding support for ETH-IOU:
  * `POST /api/v2/ripple_address/`
  * `POST /api/v2/ripple_withdrawal/`

### 2024-03-13

* Added transfer_id param to crypto endpoints:
  * `POST /api/v2/{currency}_address/` response
  * `POST /api/v2/{currency}_withdrawal/` request

### 2023-10-12

* New API changes due to compliance with Travel Rule requirements:
  * Travel Rule endpoints: https://www.bitstamp.net/api/#tag/Travel-rule-public
  * Changes to all crypto withdrawals to provide optional Travel Rule data (this data will become mandatory in the near future which will be a breaking change!).
* All endpoints for creating new orders have an optional **client_order_id field**. If submitted, up until now client_order_id had to be unique. We are deprecating the checking of duplicate **client_order_id** and will allow duplicates beginning November 2023. If you currently rely on us checking for duplicates and us rejecting those, this change may cause you to submit multiple orders so please make the necessary changes to not rely on that check.
* New API endpoints that enable you to access full Earn (Staking and Lending) functionality.

### 2023-09-29

* Added **revoke_all_api_keys** as a kill switch functionality to terminate all API connectivity:
  * `POST /api/v2/revoke_all_api_keys/`

### 2023-09-25

* Updated GTD order description by noting that the orders expire at midnight:
  * `POST /api/v2/buy/{market_symbol}/`
  * `POST /api/v2/sell/{market_symbol}/`

### 2023-09-22

* Extended error responses for `/api/v2/cancel_order`:
  * `POST /api/v2/cancel_order/`

### 2023-08-31

* Added market property with the goal of deprecating **currency_pair** long term:
  * `GET /api/v2/fees/trading/`
* Added datetime and type properties to order status endpoint:
  * `GET /api/v2/order_status/`

### 2023-07-05

* Introduced a new side field (0 - buy; 1 - sell) to all Ticker endpoints:
  * `GET /api/v2/ticker/`
  * `GET /api/v2/ticker/{currency_pair}/`
  * `GET /api/v2/ticker_hour/`

### 2023-06-29

* Updated **destination_tag** field description for Ripple IOU address endpoint:
  * `POST /api/v2/ripple_address/`

### 2023-04-07

* Introduced a new Currencies endpoint:
  * `GET /api/v2/currencies/`: Get listed currencies info.


Version: v2

## Servers

- https://www.bitstamp.net — Production server
- https://sandbox.bitstamp.net — Test server

## Endpoints

### POST `/api/v2/account_balances/`

**Account balances**

Return account balances.

**Responses:**

- `200`: Post operation

### POST `/api/v2/account_balances/{currency}/`

**Account balance for currency**

Return account balances for currency.

**Responses:**

- `200`: Post operation

### POST `/api/v2/account_order_data/`

**Order event data for gap recovery**

Retrieve historical order events for a specific market to enable gap recovery.

**Responses:**

- `200`: Post operation

### POST `/api/v2/adjust_position_collateral/`

**Adjusts collateral value for position**

Returns updated collateral setting.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 204           |             | Position collateral is adjusted successfully.                                   |
| 400           | API5504     | Selected market is not supported.                                               |
| 400           | API5506     | Trade account does not support derivatives.                                     |
| 400           | API5508     | Collateral cannot be changed.                                                   |
| 400           | API5509     | Given position is not isolated. Collateral cannot be changed.                   |
| 400           | API5510     | Given position is not found.                                                    |


**Responses:**

- `204`: Post operation
- `400`: ValidationError | Provided data is invalid.

### POST `/api/v2/btc_unconfirmed/`

**Unconfirmed bitcoin deposits**

This API call is cached for 60 seconds. This call will be executed on the account (Sub or Main), to which
the used API key is bound to.


**Responses:**

- `200`: Post operation

### POST `/api/v2/buy/instant/{market_symbol}/`

**Buy instant order**

Open a buy instant order. By placing an instant order you acknowledge that the execution of your order
depends on the market conditions and that these conditions may be subject to sudden changes that cannot be
foreseen. This call will be executed on the account (Sub or Main), to which the used API key is bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing amount and/or price POST parameters | Missing one or both parameters. |
| 'parameter': Enter a number. Use "." as a decimal point. | 'parameter' can only be number. |
| Minimum order size is 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH | Order value must be at least 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH |
| You can only buy 'amount' 'currency'. Check your account balance for details. | Account has less 'available_currency' than is required to make this order. |
| Maximum market buy amount at the moment is 'amount' 'currency'. Please use limit order instead. | Order amount exceeds the limit amount set for market buy orders. |
| Order could not be placed. | Order could not be placed (perhaps due to internal error or trade halt). Please retry placing order. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/buy/market/{market_symbol}/`

**Buy market order**

Open a buy market order. By placing a market order you acknowledge that the execution of your order depends
on the market conditions and that these conditions may be subject to sudden changes that cannot be
foreseen. This call will be executed on the account (Sub or Main), to which the used API key is bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing amount and/or price POST parameters | Missing one or both parameters. |
| 'parameter': Enter a number. Use "." as a decimal point. | 'parameter' can only be number. |
| Minimum order size is 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH | Order value must be at least 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH |
| You can only buy 'amount' 'currency'. Check your account balance for details. | Account has less 'available_currency' than is required to make this order. |
| Maximum market buy amount at the moment is 'amount' 'currency'. Please use limit order instead. | Order amount exceeds the limit amount set for market buy orders. |
| Order could not be placed. | Order could not be placed (perhaps due to internal error or trade halt). Please retry placing order. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/buy/{market_symbol}/`

**Buy limit order**

Open a buy limit order. This call will be executed on the account (Sub or Main), to which the used API key
is bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing amount and/or price POST parameters | Missing one or both parameters. |
| 'parameter': Enter a number. Use "." as a decimal point. | 'parameter' can only be number. |
| Minimum order size is 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH | Order value must be at least 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH |
| Price is more than 20% above market price. | Order price must not exceed 20% of current price. |
| You need 'order_value' USD to open that order. You have only 'available_fiat' USD available. Check your account balance for details. | Account has less 'available_fiat' than is required to make this order. |
| Sell if executed price must be higher than buy price. | 'limit_price' must be larger than 'price' parameter. |
| Both limit_price and daily_order cannot be set. | Only one of those parameters can be set. |
| Order could not be placed. | Order could not be placed (perhaps due to internal error or trade halt). Please retry placing order. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/cancel_all_orders/`

**Cancel all orders**

Cancel all open orders. This call will be executed on the account (Sub or Main), to which the used API key is bound to.

**Responses:**

- `200`: Post operation

### POST `/api/v2/cancel_all_orders/{market_symbol}/`

**Cancel all orders for market**

Cancel all open orders for a market. This call will be executed on the account (Sub or Main), to which the used API key is bound to.

**Responses:**

- `200`: Post operation

### POST `/api/v2/cancel_order/`

**Cancel order**

Cancel an order. This call will be executed on the account (Sub or Main), to which the used API key is
bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing id POST param. | Id parameter missing. |
| Invalid id POST param. | Id parameter must be a positive integer. |
| Invalid client_cancel_id POST param. | client_cancel_id parameter can contain at most 180 characters. |
| Invalid client_order_id POST param. | client_order_id parameter can contain at most 180 characters. |
| Order not found | Order with that id was not found in orderbook. Order might already be filled or canceled. Please check order status. |
| Order cancellation failed due to internal error. Please try again. | Please retry cancelling order. |
| Order cancelattion failed due to trade halt. | You can cancel order after trade halt is lifted. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/close_position/`

**Close position**

Closes position based on position id and returns details of the closed position.

**The below table defines the HTTP Status codes that this API may return**

| Status Code   | Response Code | Reason                                                                          |
|---------------|---------------|---------------------------------------------------------------------------------|
| 200           |               | Returned closed position data.                                                  |
| 200           | 400.043       | No positions present.                                                           |
| 400           | API5505       | Invalid arguments.                                                              |
| 400           | 400.002       | Request rejected due to exceeded rate limit.                                    |
| 400           | 400.076       | Failed to close position due to order size limitations. You should close this position by placing orders instead. |
| 400           | 500.001       | Unknown server error.                                                           |
| 400           | 500.003       | Unknown error while processing order.                                           |
| 400           | 500.009       | Order book is currently unavailable.                                            |
| 400           | 500.013       | Unknown matching engine error.                                                  |
| 400           | 500.016       | Your request timed out. Check order status using order_id.                      |
| 403           | 403.004       | Trading is blocked for user.                                                    |


**Responses:**

- `200`: Post operation
- `400`: Provided data is invalid.

### POST `/api/v2/close_positions/`

**Close positions**

Closes positions corresponding to the inputs and returns 2 lists,
one containing closed positions and another containing positions which failed to close.

**The below table defines the HTTP Status codes that this API may return**

| Status Code   | Response Code | Reason                                                                                                                        |
|---------------|---------------|-------------------------------------------------------------------------------------------------------------------------------|
| 200           |               | Returned 2 lists, one containing closed positions with data and another containing positions with data which failed to close. |
| 200           | 400.043       | No positions present                                                                                                          |
| 400           | API5504       | Selected market is not supported.                                                                                             |
| 400           | API5505       | Invalid arguments.                                                                                                            |
| 400           | API5506       | Trade account does not support derivatives.                                                                                   |
| 400           | 400.002       | Request rejected due to exceeded rate limit.                                                                                  |
| 400           | 500.001       | Unknown server error.                                                                                                         |
| 400           | 500.003       | Unknown error while processing order.                                                                                         |
| 400           | 500.009       | Order book is currently unavailable.                                                                                          |
| 400           | 500.013       | Unknown matching engine error.                                                                                                |
| 400           | 500.016       | Your request timed out. Check order status using order_id.                                                                    |                                                                                        |


**Responses:**

- `200`: Post operation
- `400`: Provided data is invalid.

### POST `/api/v2/collateral_change_impact/`

**Estimated collateral change impact**

Returns estimated collateral change impact for open positions based on input.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned estimated collateral change impact                                     |
| 400           | API5504     | Selected market is not supported.                                               |
| 400           | API5506     | Trade account does not support derivatives.                                     |
| 503           |             | Service currently unavailable. Try again later.                                 |


**Responses:**

- `200`: Post operation
- `400`: Provided data is invalid.

### GET `/api/v2/collateral_currencies/`

**Collateral currencies**

Returns collateral currencies with haircut


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation

### POST `/api/v2/crypto-transactions/`

**Crypto transactions**

Return user's crypto transactions. This call will be executed on the account, to which the used API key is
bound to. This call is for your main account only.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Limit too large | Max value of limit parameter is 1000. |
| Invalid limit | Limit parameter should be number from 1 to 1000. |
| Offset too large | Offset parameter cannot be larger than 200000. |
| Invalid offset | Offset parameter needs to be a number from 0 to 200000. |
| Invalid since_timestamp parameter | since_timestamp can only be digit. |
| since_timestamp parameter must be higher than .. | Make sure that since_timestamp is less than 30 days in the past. |
| Failed to convert since_timestamp parameter | Check the value of since_timestamp parameter. |
| Invalid until_timestamp parameter | until_timestamp can only be digit. |
| until_timestamp parameter must be higher than .. | Make sure that until_timestamp is less than 30 days in the past. |
| Failed to convert until_timestamp parameter | Check the value of until_timestamp parameter. |
</details>


**Responses:**

- `200`: Post operation

### GET `/api/v2/crypto-transactions/deposits/`

**List crypto deposits with review status**

Returns cryptocurrency deposits for the authenticated user with review status information.

**The below table defines the HTTP Status codes that this API may return**

| Response code | Reason                                                    |
|---------------|-----------------------------------------------------------|
| 200           | Successfully retrieved deposits                           |
| 400           | Invalid parameters (timestamp, limit, or offset)          |
| 403           | Insufficient permissions                                  |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| offset | query | string | False | Skip that many transactions before returning results (maximum: 200000). |
| limit | query | string | False | Limit result to that many transactions (maximum: 1000). |
| since_timestamp | query | string | False | (Optional) Show only transactions from unix timestamp (for max 30 days old). |
| until_timestamp | query | string | False | Show only transactions to unix timestamp (for max 30 days old). |
| status | query | string | False | If not provided, all deposits will be returned. |

**Responses:**

- `200`: Get operation
- `400`: RequestError | RequestError

### POST `/api/v2/crypto-transactions/deposits/{deposit_id}/`

**Update deposit originator information**

Submit originator/beneficiary details for a pending cryptocurrency deposit requiring
travel rule compliance information before it can be credited.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Reason                                                    |
|---------------|-----------------------------------------------------------|
| 204           | Successfully updated                                      |
| 400           | VASP not found, contact not found, or service error       |
| 403           | Insufficient permissions                                  |


**Responses:**

- `204`: Post operation
- `400`: ValidationError | ValidationError | ValidationError | RequestError | Provided data is invalid.

### GET `/api/v2/currencies/`

**Currencies**

Returns list of all currencies with basic data.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation

### POST `/api/v2/earn/subscribe/`

**Subscribe to earn**

Subscribe given amount to lending / staking.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                              |
|---------------|-------------|-------------------------------------------------------------------------------------|
| 200           |             | Successfully subscribed to earn.                                                    |
| 400           | API5001     | Earn request amount too low.                                                        |
| 400           | API5002     | Earn request amount too high.                                                       |
| 400           | API5003     | Decimal places in amount exceed maximum allowed.                                    |
| 400           | API5004     | Operation is unsupported.                                                           |
| 400           | API5005     | Operation is currently unavailable, please try again later.                         |
| 400           | API5006     | Required personal information is missing, please reach out to support@bitstamp.net. |
| 400           | API5007     | Operation is unavailable, please reach out to support@bitstamp.net.                 |
| 400           | API5011     | Something went wrong, try again later.                                              |
| 403           |             | This feature is not available for your account.                                     |


**Responses:**

- `204`: Post operation
- `400`: ForbiddenError | Provided data is invalid.

### GET `/api/v2/earn/subscriptions/`

**Get earn subscriptions**

Get earn subscriptions for user.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                      |
|---------------|-------------|-------------------------------------------------------------|
| 200           |             | Returned earn subscriptions                                 |
| 400           | API5011     | Something went wrong, try again later.                      |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation

### POST `/api/v2/earn/subscriptions/setting/`

**Manage subscription settings**

Manage subscription settings (opt in, opt out). Currently only supported for staking.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                      |
|---------------|-------------|-------------------------------------------------------------|
| 200           |             | Successfully update subscription setting.                   |
| 400           | API5004     | Operation is unsupported.                                   |
| 400           | API5005     | Operation is currently unavailable, please try again later. |
| 400           | API5008     | Already opted in.                                           |
| 400           | API5009     | Not opted in.                                               |
| 400           | API5010     | Insufficient balance.                                       |
| 400           | API5011     | Something went wrong, try again later.                      |
| 403           |             | This feature is not available for your account.             |


**Responses:**

- `204`: Post operation
- `400`: ForbiddenError | Provided data is invalid.

### GET `/api/v2/earn/transactions/`

**Get earn transactions**

Get earn transaction history.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                      |
|---------------|-------------|-------------------------------------------------------------|
| 200           |             | Returned earn transaction history.                          |
| 400           | API5011     | Something went wrong, try again later.                      |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| limit | query | integer | False | Limit result to that many events (default: 100; maximum: 1000) |
| offset | query | integer | False | Skip that many events before returning results (default: 0, maximum: 200000) |
| currency | query | string | False | Currency |
| quote_currency | query | string | False | Currency in which value is calculated |

**Responses:**

- `200`: Get operation

### POST `/api/v2/earn/unsubscribe/`

**Unsubscribe from earn**

Unsubscribe given amount from lending / staking.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                      |
|---------------|-------------|-------------------------------------------------------------|
| 200           |             | Successfully unsubscribed from earn.                        |
| 400           | API5001     | Earn request amount too low.                                |
| 400           | API5002     | Earn request amount too high.                               |
| 400           | API5003     | Decimal places in amount exceed maximum allowed.            |
| 400           | API5004     | Operation is unsupported.                                   |
| 400           | API5005     | Operation is currently unavailable, please try again later. |
| 400           | API5011     | Something went wrong, try again later.                      |
| 400           | API5012     | Staked balance is insufficient.                             |
| 403           |             | This feature is not available for your account.             |


**Responses:**

- `204`: Post operation
- `400`: ForbiddenError | Provided data is invalid.

### POST `/api/v2/estimated_order_impact/`

**Estimated order impact**

Returns estimated order impact

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned estimated margin impact of order parameters.                                                         |
| 400           | API5504     | Selected market is not supported.                                               |
| 400           | API5506     | Trade account does not support derivatives.                                     |
| 503           |             | Service currently unavailable. Try again later.                                 |


**Responses:**

- `200`: Post operation
- `400`: Provided data is invalid.

### GET `/api/v2/eur_usd/`

**EUR/USD conversion rate**

Return EUR/USD conversion rate.

**Responses:**

- `200`: Get operation

### POST `/api/v2/fees/trading/`

**Trading fees**

Return all trading fees.

**Responses:**

- `200`: Post operation

### POST `/api/v2/fees/trading/{market_symbol}/`

**Trading fee for market**

Return trading fees for market.

**Responses:**

- `200`: Post operation

### POST `/api/v2/fees/withdrawal/`

**Withdrawal fees**

Return withdrawal fees.

**Responses:**

- `200`: Post operation

### POST `/api/v2/fees/withdrawal/{currency}/`

**Withdrawal fee for currency**

Return withdrawal fee for currency.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Invalid network selection | The selected network is not supported for 'currency'. Please select a compatible network for it. |
</details>


**Responses:**

- `200`: Post operation

### GET `/api/v2/funding_rate/{market_symbol}/`

**Current funding rate data**

Returns current funding rate data.


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation
- `400`: NotFoundError | RequestError

### GET `/api/v2/funding_rate_history/{market_symbol}/`

**Funding rate history data**

Returns historic funding rate data.


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| limit | query | integer | False | Max number of results. |
| since_timestamp | query | integer | False | (Optional) Show only funding rates from unix timestamp (for max 30 days old). |
| until_timestamp | query | integer | False | Show only funding rates to unix timestamp (for max 30 days old). |

**Responses:**

- `200`: Get operation
- `400`: NotFoundError | RequestError

### POST `/api/v2/get_max_order_amount/`

**Max buy/sell order amount**

Returns max buy/sell order amount for given parameters.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned max amount, amount currency, value and value currency for given params.|
| 400           | API5502     | Something went wrong, try again later.                                          |
| 400           | API5503     | Unknown order type.                                                             |
| 400           | API5504     | Selected market is not supported.                                               |
| 400           | API5505     | Invalid arguments.                                                              |
| 400           | API5506     | Trade account does not support derivatives.                                     |
| 400           | 400.002     | Request rejected due to exceeded rate limit.                                    |
| 400           | 400.003     | Unknown error while processing order.                                           |


**Responses:**

- `200`: Post operation
- `400`: RequestError | Provided data is invalid.

### POST `/api/v2/instant_convert_address/info/`

**Instant convert address**

Shows transactions for the instant convert address.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Address not found. | Provided address is wrong. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/instant_convert_address/new/`

**New instant convert address**

Creates a new instant convert address which will automatically sell your crypto for specified fiat currency.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing liquidation_currency parameter. | Parameter liquidation_currency is required for this call. |
| Invalid currency / Currency [...] not supported. | Invalid liquidation_currency. |
| Cannot create new address, please try later. | At the moment we can't create new deposit address. Try again later. |
| Invalid address format. | Invalid address_format. |
| Your trading features are currently disabled | No new liquidation addresses can be created at this time. If a URL is provided you can follow it to resolve any issues which might be causing this. |
</details>


**Responses:**

- `200`: Post operation

### GET `/api/v2/leverage_settings/`

**Leverage settings list**

Returns leverage settings list

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned leverage settings list.                                                |
| 503           |             | Service currently unavailable. Try again later.                                 |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| margin_mode | query | string | False | Margin mode. |
| market | query | string | False | Market name. |

**Responses:**

- `200`: Get operation

### POST `/api/v2/leverage_settings/`

**Update leverage setting with override**

Returns updated leverage setting.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 201           |             | Returned leverage settings list.                                                |
| 503           |             | Service currently unavailable. Try again later.                                 |


**Responses:**

- `201`: Post operation
- `400`: exception | Provided data is invalid.

### GET `/api/v2/margin_info/`

**Margin info**

Returns margin information

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned margin information.                                                    |
| 400           | API5506     | Trade account does not support derivatives.                                     |
| 503           |             | Service currently unavailable. Try again later.                                 |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation

### GET `/api/v2/margin_tiers/`

**Margin Tiers**

Returns a list of Margin Tiers for each Market

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation

### GET `/api/v2/markets/`

**Markets**

View that returns list of all available markets.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation

### GET `/api/v2/my_markets/`

**Trading markets**

Returns all markets that can be traded on selected account.


**Responses:**

- `200`: Get operation

### GET `/api/v2/ohlc/{market_symbol}/`

**OHLC data**

Returns OHLC (Open High Low Close) data.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing data for required field. | Step and limit parameters are missing. |
| Not a valid choice. | Value entered in parameter is invalid. |
| Must be between 1 and 1000. | Limit value must be between 1 and 1000. |
</details>


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| step | query | integer | True | Timeframe in seconds. |
| limit | query | integer | True | Limit OHLC results. |
| start | query | integer | False | Unix timestamp from when OHLC data will be started. |
| end | query | integer | False | Unix timestamp to when OHLC data will be shown.If none from start or end timestamps are posted then endpoint returns OHLC data to current unixtime. If both start and end timestamps are posted, end timestamp will be used. |
| exclude_current_candle | query | boolean | False | If set, results won't include current (open) candle. |

**Responses:**

- `200`: Get operation

### POST `/api/v2/open_orders/`

**Open orders**

Return user's open orders. This API call is cached for 10 seconds. This call will be executed on the account (Sub or Main), to which the used API key is bound to.

**Responses:**

- `200`: Post operation

### POST `/api/v2/open_orders/{market_symbol}/`

**Open orders for market**

Return user's open orders for market. This API call is cached for 10 seconds. This call will be executed on the account (Sub or Main), to which the used API key is bound to.

**Responses:**

- `200`: Post operation

### GET `/api/v2/open_positions/`

**Open positions list**

Returns open positions list

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned open positions.                                                        |
| 400           | API5506     | Trade account does not support derivatives.                                     |
| 400           | API5507     | Missing trade account and user params.                                          |
| 400           | 400.007     | Market not found for corresponding request.                                     |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation

### GET `/api/v2/open_positions/{market_symbol}/`

**Open positions list by market**

Returns open positions list by market

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned open positions for given market.                                       |
| 400           | API5504     | Selected market is not supported.                                               |
| 400           | API5506     | Trade account does not support derivatives.                                     |
| 400           | 400.007     | Market not found for corresponding request.                                     |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation
- `400`: NotFoundError | InvalidMarketTypeError

### GET `/api/v2/order_book/{market_symbol}/`

**Order book**

Returns order book data.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| POST method not allowed for this request. | HTTP method other than GET used. |
| Invalid GET parameter. | Missing group parameter. |
| Internal error. | Order book unavailable. |
</details>


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| group | query | integer | False | The group parameter is used for accessing different data from order book. Possible values are 0 (orders are not grouped at same price), 1 (orders are grouped at same price - default) or 2 (orders with their order ids are not grouped at same price). |

**Responses:**

- `200`: Get operation

### POST `/api/v2/order_data/`

**Public order event data for gap recovery**

Retrieve historical public order events for a specific market to enable gap recovery.

**Responses:**

- `200`: Post operation

### POST `/api/v2/order_status/`

**Order status**

Returns order status. This call will be executed on the account (Sub or Main), to which the
used API key is bound to. Order can be fetched by using either id or client_order_id parameter. For closed
orders, this call only returns information for the last 30 days. 'Order not found' error will be returned
for orders outside this time range.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing id POST param | Id parameter missing. |
| Invalid order id | Order id parameter can only be number. |
| Order not found. | Order with that id was not found in our system. |
</details>


**Responses:**

- `200`: Post operation

### GET `/api/v2/position_history/`

**Positions history list**

Returns positions history list

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned positions history.                                                     |
| 400           | API5506     | Trade account does not support derivatives.                                     |
| 400           | API5507     | Missing trade account and user params.                                          |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| offset | query | string | False | (Optional) Skip that many records before returning results (default: 0, maximum: 200000). If you need to export older history contact support or use a combination of limit and since_id parameters. |
| limit | query | string | False | (Optional) Limit result to that many records (default: 100; maximum: 1000). |
| since_id | query | string | False | (Optional) Show only records from specified id. If since_id parameter is used, limit parameter is set to 1000. |
| sort | query | string | False | Sorting order: asc - ascending; desc - descending (default: desc). |

**Responses:**

- `200`: Get operation

### GET `/api/v2/position_history/{market_symbol}/`

**Positions history list by market**

Returns positions history list by market

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned positions history for given market.                                    |
| 400           | API5504     | Selected market is not supported.                                               |
| 400           | API5506     | Trade account does not support derivatives.                                     |
| 400           | API5507     | Missing trade account and user params.                                          |
| 404           | 400.007     | Market not found for corresponding request.                                     |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| offset | query | string | False | (Optional) Skip that many records before returning results (default: 0, maximum: 200000). If you need to export older history contact support or use a combination of limit and since_id parameters. |
| limit | query | string | False | (Optional) Limit result to that many records (default: 100; maximum: 1000). |
| since_id | query | string | False | (Optional) Show only records from specified id. If since_id parameter is used, limit parameter is set to 1000. |
| sort | query | string | False | Sorting order: asc - ascending; desc - descending (default: desc). |

**Responses:**

- `200`: Get operation
- `400`: NotFoundError | InvalidMarketTypeError

### GET `/api/v2/position_settlement_transactions/`

**Position settlement transaction list**

Returns position settlement transaction list


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| offset | query | string | False | (Optional) Skip that many records before returning results (default: 0, maximum: 200000). If you need to export older history contact support or use a combination of limit and since_id parameters. |
| limit | query | string | False | (Optional) Limit result to that many records (default: 100; maximum: 1000). |
| since_id | query | string | False | (Optional) Show only records from specified id. If since_id parameter is used, limit parameter is set to 1000. |
| sort | query | string | False | Sorting order: asc - ascending; desc - descending (default: desc). |
| since_timestamp | query | string | False | (Optional) Show only settlement transactions from unix timestamp (for max 30 days old). |
| until_timestamp | query | string | False | (Optional) Show only settlement transactions to unix timestamp (for max 30 days old). |

**Responses:**

- `200`: Get operation

### GET `/api/v2/position_settlement_transactions/{transaction_id}/`

**Position settlement transaction list by market transaction**

Returns position settlement transaction list by market transaction


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| offset | query | string | False | (Optional) Skip that many records before returning results (default: 0, maximum: 200000). If you need to export older history contact support or use a combination of limit and since_id parameters. |
| limit | query | string | False | (Optional) Limit result to that many records (default: 100; maximum: 1000). |
| since_id | query | string | False | (Optional) Show only records from specified id. If since_id parameter is used, limit parameter is set to 1000. |
| sort | query | string | False | Sorting order: asc - ascending; desc - descending (default: desc). |
| since_timestamp | query | string | False | (Optional) Show only settlement transactions from unix timestamp (for max 30 days old). |
| until_timestamp | query | string | False | (Optional) Show only settlement transactions to unix timestamp (for max 30 days old). |

**Responses:**

- `200`: Get operation

### GET `/api/v2/position_status/{position_id}/`

**Position status**

Returns the position's status and metadata. This call will be executed on the trade account, to which the
used API key is bound to.


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation

### POST `/api/v2/replace_order/`

**Replace order**

Replace an existing order with a new one by atomically canceling the existing order and placing
a new order with updated price and/or amount. This call will be executed on the account (Sub or Main),
to which the used API key is bound to.

**Order Identification:** You must provide either `id` (order ID) or `orig_client_order_id` to identify
the order to be replaced.

**Required Parameters:**
- `amount`: New order amount (decimal, min: 0.00000001, max: 92233720368)
- `price`: New order price (decimal, min: 0.00000001, max: 99999999.99999)
- Either `id` or `orig_client_order_id`

**Optional Parameters:**
- `client_order_id`: Client-specified ID for the new order (max 180 characters)

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Error | Description |
| ----------- | ----------- |
| Missing id POST param. | Neither `id` nor `orig_client_order_id` parameter provided. |
| Invalid id POST param. | The `id` parameter must be a positive integer. |
| Invalid orig_client_order_id POST param. | The `orig_client_order_id` parameter exceeds 180 characters. |
| Invalid client_order_id POST param. | The `client_order_id` parameter exceeds 180 characters. |
| Enter a number. Use "." as a decimal point. | Invalid `amount` or `price` format. |
| The minimum allowed amount is 0.00000001. | The `amount` is below the minimum threshold. |
| The maximum allowed amount is 92233720368. | The `amount` exceeds the maximum threshold. |
| The minimum allowed price is 0.00000001. | The `price` is below the minimum threshold. |
| The maximum allowed price is 99999999.99999. | The `price` exceeds the maximum threshold. |
| Order not found | Order with that id was not found in orderbook. Order might already be filled or canceled. |
| No permission found | API key lacks required permissions (cancel_order and buy/sell based on order type). |
| Insufficient balance | User does not have sufficient balance to increase the order size. |
| Order replacement failed due to trade halt. | Trading is currently halted. Try again after trade halt is lifted. |
| Provided client_order_id already exists. | The specified `client_order_id` is already in use. |
| Modification rejected: leverage, margin_mode, and reduce_only fields cannot be updated once the order is created | Perpetuals only: Cannot modify `leverage`, `margin_mode`, or `reduce_only` after order creation.|
| Order replacement failed due to internal error. Please try again. | Internal error occurred. Retry the request. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/revoke_all_api_keys/`

**Revoke all API access**

Revoke all API keys across all user's accounts.

**Responses:**

- `200`: Post operation
- `400`: Provided data is invalid.

### POST `/api/v2/ripple_address/`

**Ripple IOU deposit address**

This API call is cached for 60 seconds. This call will be executed on the account (Sub or Main), to which
the used API key is bound to. This endpoint supports withdrawals of USD, BTC, EUR and ETH IOU on the XRP Ledger.

*IOU supported globally except in the US and Singapore. ETH-IOU is also unsupported in UK.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| User not verified | Your account needs to be verified before you can use this endpoint. |
| Your deposits are currently disabled | No new deposits can be made at this time. If a URL is provided you can follow it to resolve any issues which might be causing this. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/ripple_withdrawal/`

**Ripple IOU withdrawal**

This call will be executed on the account (Sub or Main), to which the used
API key is bound to. This endpoint supports withdrawals of USD, BTC, EUR or ETH IOU on the XRP Ledger.

*IOU supported globally except in the US and Singapore. ETH-IOU is also unsupported in UK

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing amount and/or address POST parameters | One or both parameters missing. |
| User not verified | Your account needs to be verified before you can use this endpoint. |
| 'crypto_currency' withdrawals are currently unavailable for your account | Contact support for additional information. |
| Not allowed to withdraw to specified 'crypto_currency' address | API key is set for withdrawing to another 'crypto_currency' address. |
| Enter a number. Use "." as a decimal point | Amount parameter can only be number. |
| You have only 'available' 'crypto_currency' available. Check your account balance for details | Account has less available 'crypto_currency' than are required to make this withdrawal. |
| Your withdrawals are currently disabled | No new withdrawals can be opened at this time. If a URL is provided you can follow it to resolve any issues which might be causing this. |
| Ensure this value is greater than or equal to 'minimum_withdrawal_amount' | Minimum withdrawal amount is 'minimum_withdrawal_amount'. |
| Ensure this value has at least 'minimum_address_length' characters (it has x). Ensure this value has at most 'maximum_address_length' characters (it has x). | Address parameter must be between 'minimum_address_length' and 'maximum_address_length' characters long. |
| Contact does not exist | Review and validate the contact_uuid to ensure it matches an existing contact, you may also create contacts at the /v2/travel_rule/contacts endpoint |
| Contact is missing required information | Ensure that contact has all the required information in case of retail_info, first_name and last_name are required. |
| Vasp does not exist | Verify that the vasp_uuid exists within the /v2/travel_rule/vasps endpoint. |
| contact_uuid: You must set this field because contact_thirdparty=True | contact_uuid must be provided if withdrawing to a third party |
| The address you provided is not verified | You must verify this address before you can withdraw to it. |

</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/sell/instant/{market_symbol}/`

**Sell instant order**

Open an instant sell order. By placing an instant order you acknowledge that the execution of your order
depends on the market conditions and that these conditions may be subject to sudden changes that cannot be
foreseen. This call will be executed on the account (Sub or Main), to which the used API key is bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing amount and/or price POST parameters | Missing one or both parameters. |
| 'parameter': Enter a number. Use "." as a decimal point. | 'parameter' can only be number. |
| Minimum order size is 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH | Order value must be at least 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH |
| You can only sell 'amount' 'currency'. Check your account balance for details. | Account has less 'available_currency' than is required to make this order. |
| Order could not be placed. | Order could not be placed (perhaps due to internal error or trade halt). Please retry placing order. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/sell/market/{market_symbol}/`

**Sell market order**

Open a sell market order. By placing a market order you acknowledge that the execution of your order depends
on the market conditions and that these conditions may be subject to sudden changes that cannot be
foreseen. This call will be executed on the account (Sub or Main), to which the used API key is bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing amount and/or price POST parameters | Missing one or both parameters. |
| 'parameter': Enter a number. Use "." as a decimal point. | 'parameter' can only be number. |
| Minimum order size is 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH | Order value must be at least 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH |
| You can only sell 'amount' 'currency'. Check your account balance for details. | Account has less 'available_currency' than is required to make this order. |
| No buy orders for currency pair 'currency_pair' | The buy side of the orderbook for 'currency_pair' is empty, therefore a market sell order cannot be placed. |
| Maximum market sell amount at the moment is 'amount' 'currency'. Please use limit order instead. | Order amount exceeds the limit amount set for market sell orders. |
| Order could not be placed. | Order could not be placed (perhaps due to internal error or trade halt). Please retry placing order. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/sell/{market_symbol}/`

**Sell limit order**

Open a sell limit order. This call will be executed on the account (Sub or Main), to which the used API key
is bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing amount and/or price POST parameters | Missing one or both parameters. |
| 'parameter': Enter a number. Use "." as a decimal point. | 'parameter' can only be number. |
| Minimum order size is 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH | Order value must be at least 10 USD / 10 EUR / 10 GBP / 10 USDT / 10 USDC / 10 PAX / 10 GUSD / 0.0002 BTC / 0.002 ETH |
| Price is more than 20% below market price. | Order price must not exceed 20% of current price. |
| You have only 'available_btc' BTC available. Check your account balance for details. | Account has less 'available_btc' than is required to make this order. |
| Buy if executed price must be lower than sell price. | 'limit_price' must be lower than 'price' parameter. |
| Both limit_price and daily_order cannot be set. | Only one of those parameters can be set. |
| Order could not be placed. | Order could not be placed (perhaps due to internal error or trade halt). Please retry placing order. |
</details>


**Responses:**

- `200`: Post operation

### GET `/api/v2/ticker/`

**Tickers for all markets**

Return ticker data for all markets. Passing any GET parameters, will result in your request being rejected.

**Responses:**

- `200`: Get operation

### GET `/api/v2/ticker/{market_symbol}/`

**Market ticker**

Return ticker data for the requested currency pair. Passing any GET parameters, will result in your request being rejected.

**Responses:**

- `200`: Get operation

### GET `/api/v2/ticker_hour/{market_symbol}/`

**Hourly  ticker**

Return hourly ticker data for the requested currency pair. Passing any GET parameters, will result in your request being rejected.

**Responses:**

- `200`: Get operation

### GET `/api/v2/trade_history/`

**Derivatives Trade history**

Returns derivatives trade history

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned derivatives trade history for.                                         |
| 400           | API5501     | One of "market" or "order_id" parameter is required in request.                 |
| 400           | API5502     | Something went wrong, try again later.                                          |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| limit | query | string | False | (Optional) Limit result to that many records (default: 100; maximum: 1000). |
| sort | query | string | False | Sorting order: asc - ascending; desc - descending (default: desc). |
| order_id | query | string | False | Order ID. |
| since_timestamp | query | integer | False | (Optional) Show only trades from unix timestamp. |
| until_timestamp | query | integer | False | Show only trades to unix timestamp. |
| after_id | query | string | False | (Optional) Show only records from specified id. If after_id parameter is used, limit parameter is set to 1000. |

**Responses:**

- `200`: Get operation
- `400`: ValidationError

### GET `/api/v2/trade_history/{market_symbol}/`

**Derivatives trade history for market**

Returns derivatives trade history for requested market

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                          |
|---------------|-------------|---------------------------------------------------------------------------------|
| 200           |             | Returned derivatives trade history for given market.                            |
| 400           | API5501     | One of "market" or "order_id" parameter is required in request.                 |
| 400           | API5502     | Something went wrong, try again later.                                          |
| 400           | API5503     | Unknown order type.                                                             |
| 400           | 400.007     | Market not found for corresponding request.                                     |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| limit | query | string | False | (Optional) Limit result to that many records (default: 100; maximum: 1000). |
| sort | query | string | False | Sorting order: asc - ascending; desc - descending (default: desc). |
| order_id | query | string | False | Order ID. |
| since_timestamp | query | integer | False | (Optional) Show only trades from unix timestamp. |
| until_timestamp | query | integer | False | Show only trades to unix timestamp. |
| after_id | query | string | False | (Optional) Show only records from specified id. If after_id parameter is used, limit parameter is set to 1000. |

**Responses:**

- `200`: Get operation
- `400`: ValidationError | NotFoundError | NotFoundError

### GET `/api/v2/transactions/{market_symbol}/`

**Transactions**

Return transaction data from a given time frame.

**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| time | query | string | False | The time interval from which we want the transactions to be returned. Possible values are minute, hour (default) or day. |

**Responses:**

- `200`: Get operation

### POST `/api/v2/transfer-from-main/`

**Transfer balance from Main to Sub Account**

Transfers the desired balance from your Main Account to a Sub Account, specified by the subAccount
parameter. This call can only be performed by your Main Account.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| 'parameter': Enter a number. Use "." as a decimal point. | 'parameter' can only be number. |
| You have only 'available' 'currency' available. Check your account balance for details. | Account has less 'available_currency' than is required to make this transfer. |
| Select a valid choice. X is not one of the available choices. | X is not valid currency. Select a valid currency. |
| Sub account with identifier "X" does not exist. | Can't find sub account with id X. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/transfer-to-main/`

**Transfer balance from Sub to Main account**

Transfers the desired balance from a Sub Account to your Main Account.
Can be called by either the Main Account or a Sub Account, but requires a permission in both cases.
The subAccount parameter must be provided if the Main Account is initiating the call.
If a Sub Account is making the call, then it is the target Sub Account for the transfer and no further
clarification is required.
In that case, passing this parameter will have no additional effect.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| 'parameter': Enter a number. Use "." as a decimal point. | 'parameter' can only be number. |
| You have only 'available' 'currency' available. Check your account balance for details. | Account has less 'available_currency' than is required to make this transfer. |
| Select a valid choice. X is not one of the available choices. | X is not valid currency. Select a valid currency. |
| Sub account with identifier "X" does not exist. | Can't find sub account with id X. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/travel_rule/addresses/`

**Submit counterparty info for a crypto address**

Enables an address to be registered with contact data and a vasp name,
meeting Travel Rule requirements, before using the address to transfer crypto to/from the platform.

| Response Code | Status Code | Reason                                                                     |
|---------------|-------------|----------------------------------------------------------------------------|
| 201           |             | Successfully submitted counterparty info.                                  |
| 403           |             | You do not have sufficient permissions to access this endpoint.            |


**Responses:**

- `201`: Post operation
- `400`: ValidationError | ValidationError | ValidationError | ValidationError | RequestError | Provided data is invalid.

### GET `/api/v2/travel_rule/contacts/`

**Get all contacts**

Returns all contacts that have been previously created.
These can then be used to provide the originator or beneficiary details of a Travel Rule message, when
transferring crypto from/to the platform.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                     |
|---------------|-------------|----------------------------------------------------------------------------|
| 200           |             | Successfully retrieved the list of contacts.                               |
| 403           |             | You do not have sufficient permissions to access this endpoint.            |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| per_page | query | integer | False |  |
| page | query | integer | False |  |

**Responses:**

- `200`: Get operation

### POST `/api/v2/travel_rule/contacts/`

**Create contact**

Enables a contact to be created and relevant information to be provided and stored.
This can then be used to provide the originator or beneficiary details of a Travel Rule message, when
transferring crypto from/to the platform.

| Response Code | Status Code | Reason                                                                     |
|---------------|-------------|----------------------------------------------------------------------------|
| 201           |             | Successfully created the contact.                                          |
| 403           |             | You do not have sufficient permissions to access this endpoint.            |


**Responses:**

- `201`: Post operation
- `400`: Provided data is invalid.

### GET `/api/v2/travel_rule/contacts/{contact_uuid}/`

**Get contact**

Returns a specific contact that has been previously created.
This can then be used to provide the originator or beneficiary details of a Travel Rule message, when
transferring crypto from/to the platform.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                     |
|---------------|-------------|----------------------------------------------------------------------------|
| 200           |             | Successfully retrieved the contact.                                        |
| 403           |             | You do not have sufficient permissions to access this endpoint.            |
| 404           |             | Contact with given contact uuid is not found.                              |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|

**Responses:**

- `200`: Get operation
- `400`: NotFoundError

### GET `/api/v2/travel_rule/satoshi_test/`

**Get all satoshi tests**

This function retrieves all active Satoshi tests previously created by the authenticated user
for cryptocurrency address verification. These small cryptocurrency deposits are used to verify
ownership of external wallet addresses, a requirement under Travel Rule regulations.

Each test provides deposit instructions, including:
- The specific amount to deposit
- The source (user) address being verified
- The Bitstamp deposit address to send to
- The current verification status
- The expiration time for the test

This endpoint allows you to view the status and details of all current and past satoshi tests
associated with your account.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                     |
|---------------|-------------|----------------------------------------------------------------------------|
| 200           |             | Successfully retrieved the list of Satoshi tests.                          |
| 403           |             | You do not have sufficient permissions to access this endpoint.            |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| network | query | string | False | The cryptocurrency network (e.g., "bitcoin", "ethereum"). |
| address | query | string | False | The external cryptocurrency address to verify. |
| status | query | string | False | The current status of the verification test. |

**Responses:**

- `200`: Get operation

### POST `/api/v2/travel_rule/satoshi_test/`

**Create satoshi test**

Starts a new Satoshi test to verify a cryptocurrency address for a given external wallet.

This process is necessary to comply with the Travel Rule for incoming cryptocurrency transfers,
as it verifies the user's control over the designated external wallet address.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                                   |
|---------------|-------------|------------------------------------------------------------------------------------------|
| 201           |             | The Satoshi test was created successfully.                                               |
| 400           |             | The address format is invalid, the network is not supported, or the currency is invalid. |
| 403           |             | Access to this endpoint is restricted due to insufficient permissions.                   |


**Responses:**

- `201`: Post operation
- `400`: ValidationError | ValidationError | RequestError | Provided data is invalid.

### GET `/api/v2/travel_rule/vasps/`

**VASP list**

A list of Virtual Asset Service Providers needed to comply with the Travel Rule.
These may be needed when transferring cryptocurrency from/to the platform.
This is required in cases where the originating or destination address of the crypto transfer
is hosted by a VASP.

**The below table defines the HTTP Status codes that this API may return**

| Response Code | Status Code | Reason                                                                     |
|---------------|-------------|----------------------------------------------------------------------------|
| 200           |             | Successfully retrieved the vasp list.                                      |
| 400           |             | Could not fetch VASP list, service unavailable.                            |


**Parameters:**

| Name | In | Type | Required | Description |
|------|-----|------|----------|-------------|
| per_page | query | integer | False |  |
| page | query | integer | False |  |

**Responses:**

- `200`: Get operation
- `400`: RequestError

### POST `/api/v2/user_transactions/`

**User transactions**

Return user transactions from a given time frame. This call will be executed on the account (Sub
or Main), to which the used API key is bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Invalid offset | Offset parameter should be number from 0 to 200000. |
| Limit too large | Max value of limit parameter is 1000. |
| Invalid limit | Limit parameter should be number from 1 to 1000. |
| Invalid sort parameter | Sort parameter can only be 'asc' or 'desc'. |
| Invalid since_timestamp parameter | since_timestamp can only be digit. |
| since_timestamp parameter must be higher than .. | Make sure that since_timestamp is less than 30 days in the past. |
| Failed to convert since_timestamp parameter | Check the value of since_timestamp parameter. |
| Invalid until_timestamp parameter | until_timestamp can only be digit. |
| until_timestamp parameter must be higher than .. | Make sure that until_timestamp is less than 30 days in the past. |
| Failed to convert until_timestamp parameter | Check the value of until_timestamp parameter. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/user_transactions/{market_symbol}/`

**User transactions for market**

Return user transactions for a market from a given time frame. This call will be executed on
the account (Sub or Main), to which the used API key is bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Invalid offset | Offset parameter should be number from 0 to 200000. |
| Limit too large | Max value of limit parameter is 1000. |
| Invalid limit | Limit parameter should be number from 1 to 1000. |
| Invalid sort parameter | Sort parameter can only be 'asc' or 'desc'. |
| Invalid since_timestamp parameter | since_timestamp can only be digit. |
| since_timestamp parameter must be higher than .. | Make sure that since_timestamp is less than 30 days in the past. |
| Failed to convert since_timestamp parameter | Check the value of since_timestamp parameter. |
| Invalid until_timestamp parameter | until_timestamp can only be digit. |
| until_timestamp parameter must be higher than .. | Make sure that until_timestamp is less than 30 days in the past. |
| Failed to convert until_timestamp parameter | Check the value of until_timestamp parameter. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/websockets_token/`

**Websockets token**

Generates token required for subscribing to private WebSocket channels.

**Responses:**

- `200`: Post operation

### POST `/api/v2/withdrawal-requests/`

**Withdrawal requests**

Return user's withdrawal requests. This call will be executed on the account (Sub or Main), to which the
used API key is bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Invalid timedelta | Timedelta needs to have only numeric characters. |
| Timedelta too large | Timedelta too large. |
| Invalid offset | Offset needs to be numeric characters between 0 and 200000. |
| Invalid limit | Limit needs to be numeric characters between 1 and 1000. |
| Invalid id | Id needs to have only numeric characters. |
| Both limit and offset must be present | Both limit and offset must be present. |
| Too many parameters | Pick one or combination of parameters and run again. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/withdrawal/cancel/`

**Cancel bank or crypto withdrawal**

Cancels a bank or crypto withdrawal request. This call can only be performed by your Main Account.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Cancelling bank withdrawals with sub account API keys is not supported. | This API endpoint can only be utilized by your main account. |
| Missing parameters: [...] | Parameters stated in the list ([...]) are required for this call. |
| No active bank withdrawal with id=X found. | Could not find any active bank withdrawal with the id X. Will return the same response for already cancelled withdrawal requests. |
| Cannot cancel a withdrawal in process (id=X). | The bank withdrawal request with id=X is currently being processed and cannot be cancelled. |
| Your withdrawals are currently disabled | No bank withdrawals can be canceled at this time. If a URL is provided you can follow it to resolve any issues which might be causing this. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/withdrawal/open/`

**Open bank withdrawal**

Opens a bank withdrawal request (SEPA or international). Withdrawal requests opened via API are
automatically confirmed (no confirmation e-mail will be sent), but are processed just like withdrawals
opened through the platform's interface. This call can only be performed by your Main Account.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Opening bank withdrawals with sub account API keys is not supported. | This API endpoint can only be utilized by your main account. |
| 'X': ['This field is required.'] | Parameter X is required for this call. |
| 'X': ['Select a valid choice. Y is not one of the available choices.'] | Y is not a valid value for parameter X. |
| Bank withdrawals temporarily disabled. | No new bank withdrawals can be opened at this time. |
| Unsupported withdrawal type (must be either SEPA or international). | When opening bank withdrawals, you must specify one of the two supported types: SEPA or international. |
| When opening bank withdrawals, you must specify one of the two supported types: SEPA or international. | To open this withdrawal, your balance must have at least 'amount' of target currency available. |
| 'X': ['Enter a number. Use "." as a decimal point.'] | Parameter X can only be a decimal number. |
| Your withdrawals are currently disabled | No new withdrawals can be opened at this time. If a URL is provided you can follow it to resolve any issues which might be causing this. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/withdrawal/status/`

**Fiat withdrawal status**

Checks the status of a fiat withdrawal request. This call can only be performed by your Main Account.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Performing bank withdrawal status checks with sub account API keys is not supported. | This API endpoint can only be utilized by your main account. |
| Missing parameters: [...]. | Parameters stated in the list ([...]) are required for this call. |
| No bank withdrawal with id=X found. | Could not find any bank withdrawal with the id X. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/{currency}_address/`

**Crypto deposit address**

This call will be executed on the account (Sub or Main), to which the used API key is bound to.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| User not verified | Your account needs to be verified before you can use this endpoint. |
| Your deposits are currently disabled | No new deposits can be made at this time. If a URL is provided you can follow it to resolve any issues which might be causing this. |
| Invalid network selection | The selected network is not supported for 'currency'. Please select a compatible network for it. |
</details>


**Responses:**

- `200`: Post operation

### POST `/api/v2/{currency}_withdrawal/`

**Crypto withdrawal**

Request a crypto withdrawal.

<details>
<summary style='cursor: pointer'><strong>Possible errors</strong></summary>

| Reason | Action |
| ----------- | ----------- |
| Missing amount and/or address POST parameters | One or both parameters missing. |
| User not verified | Your account needs to be verified before you can use this endpoint. |
| 'crypto_currency' withdrawals are currently unavailable for your account | Contact support for additional information. |
| Not allowed to withdraw to specified 'crypto_currency' address | API key is set for withdrawing to another 'crypto_currency' address. |
| Enter a number. Use "." as a decimal point | Amount parameter can only be number. |
| You have only 'available' 'crypto_currency' available. Check your account balance for details | Account has less available 'crypto_currency' than are required to make this withdrawal. |
| Your withdrawals are currently disabled | No new withdrawals can be opened at this time. If a URL is provided you can follow it to resolve any issues which might be causing this. |
| Ensure this value is greater than or equal to 'minimum_withdrawal_amount' | Minimum withdrawal amount is 'minimum_withdrawal_amount'. |
| Ensure this value has at least 'minimum_address_length' characters (it has x). Ensure this value has at most 'maximum_address_length' characters (it has x). | Address parameter must be between 'minimum_address_length' and 'maximum_address_length' characters long. |
| Invalid network selection | The selected network is not supported for 'currency'. Please select a compatible network for it. |
| Contact does not exist | Review and validate the contact_uuid to ensure it matches an existing contact, you may also create contacts at the /v2/travel_rule/contacts endpoint |
| Contact is missing required information | Ensure that contact has all the required information in case of retail_info, first_name and last_name are required. |
| Vasp does not exist | Verify that the vasp_uuid exists within the /v2/travel_rule/vasps endpoint. |
| contact_uuid: You must set this field because contact_thirdparty=True | contact_uuid must be provided if withdrawing to a third party |
| The address you provided is not verified | You must verify this address before you can withdraw to it. |
</details>


**Responses:**

- `200`: Post operation

## Schemas

### AccountBalancesResponse

| Property | Type | Description |
|----------|------|-------------|
| currency | string | Currency name. |
| total | string | Total balance on exchange. |
| available | string | Available balance for trading. |
| reserved | string | Reserved balance for trading. |

### AccountOrderDataRequest

| Property | Type | Description |
|----------|------|-------------|
| order_source | string | Order source type: orderbook or stop_order. |
| market | string | Market symbol (e.g., "BTC/USD"). |
| since_id | string | Starting MarketEventID (inclusive, hex format). If omitted, defaults to 24h before until_id. |
| until_id | string | Ending MarketEventID (exclusive, hex format). If omitted, defaults to now. |

### AccountOrderEvent

| Property | Type | Description |
|----------|------|-------------|
| event | string | Event type: order_created, order_changed, order_deleted, stop_active, stop_inactive. |
| event_id | string | MarketEventID in hex format for pagination (format: 4-2-2-2-6 hex grouping). |
| order_source | string | Order source: orderbook or stop_order. |
| trade_account_id | integer | Trade account unique ID. 0 represents the main account. Sub-accounts have unique IDs > 0. |
| data |  | Order event data. |

### AddressSchema

| Property | Type | Description |
|----------|------|-------------|
| address | string | Cryptocurrency address. |
| network | string | Cryptocurrency network. |
| memo_id | string | Address memo id - applicable to: XLM, HBAR, GYEN, VCHF, VEUR, ZUSD, COREUM, SEI, TON, ATOM. |
| destination_tag | string | Address destination tag - applicable to: XRP. |
| transfer_id | integer | Address transfer id - applicable to: XRP. |
| contact_thirdparty | boolean | If the address is in your name (regardless of whether this is a hosted or unhosted wallet), this should be set to False. If address is not in your name, set it to True. |
| contact_uuid | string | If setting the contact_thirdparty field to True, you need to provide the UUID of the contact from the /v2/travel_rule/contacts/ endpoint. |
| vasp_uuid | string | When address is hosted wallet by a Virtual Asset Services Provider, provide the UUID from the /v2/travel_rule/vasps/ endpoint. |

### AdjustCollateralActionSchema

| Property | Type | Description |
|----------|------|-------------|
| position_id | string | Position id. |
| new_amount | number | New collateral amount. |

### BankWithdrawalStatusRequest

| Property | Type | Description |
|----------|------|-------------|
| id | string | ID of the withdrawal request. |

### BankWithdrawalStatusResponse

| Property | Type | Description |
|----------|------|-------------|
| status | string | Status of the withdrawal request. |

### BuyInstantOrderRequest

| Property | Type | Description |
|----------|------|-------------|
| amount | number | Amount in counter currency (Example: For BTC/USD pair, amount is quoted in USD) |
| client_order_id | string | Client order ID set by the client for internal reference. It should be unique, but there are no additional constraints or checks guaranteed on the field by Bitstamp. |
| margin_mode | string | Margin mode. Required for derivatives markets. |
| leverage | string | Leverage rate. Required for derivatives markets. |

### BuySellLimitOrderRequest

| Property | Type | Description |
|----------|------|-------------|
| subtype | string | Order subtype. (Derivatives only) |
| amount | number | Amount. |
| price | number | Price. |
| limit_price | number | If the order gets executed, a new opposite order will be placed, with "limit_price" as its price. |
| daily_order | boolean | Opens limit order which will be canceled at 0:00 UTC unless it already has been executed. |
| ioc_order | boolean | An Immediate-Or-Cancel (IOC) order is an order that must be executed immediately. Any portion of an IOC order that cannot be filled immediately will be cancelled. |
| fok_order | boolean | A Fill-Or-Kill (FOK) order is an order that must be executed immediately in its entirety. If the order cannot be immediately executed in its entirety, it will be cancelled. |
| moc_order | boolean | A Maker-Or-Cancel (MOC) order is an order that ensures it is not fully or partially filled when placed. In case it would be, the order is cancelled. |
| gtd_order | boolean | A Good-Till-Date (GTD) lets you select an expiration time up until which the order will be open. Note that all GTD orders are cancelled at 00:00:00 UTC. |
| expire_time | integer | Unix timestamp in milliseconds. Required in case of GTD order. |
| client_order_id | string | Client order ID set by the client for internal reference. It should be unique, but there are no additional constraints or checks guaranteed on the field by Bitstamp. |
| margin_mode | string | Margin mode. Required for derivatives markets. |
| leverage | string | Leverage rate. Required for derivatives markets. |
| stop_price | string | When the stop price is reached, a stop order becomes a limit/market order. (Derivatives only) |
| trigger | string | Trigger price type that stop price is matching or goes over a market price. (Derivatives only) |
| activation_price | string | When the activation price is reached, a trailing order starts trailing the market price in favorable direction. (Derivatives only) |
| trailing_delta | integer | Trailing delta is the percentage of movement in the unfavorable direction from highest or lowest price. The range you can set is in BPS (5% equals 500) and should be between 1 to 2000. (Derivatives only) |
| reduce_only | boolean | A reduce-only order can only reduce your current position. (Derivatives only) |

### BuySellMarketOrderRequest

| Property | Type | Description |
|----------|------|-------------|
| subtype | string | Order subtype. (Derivatives only) |
| amount | number | Amount in base currency (Example: For BTC/USD pair, amount is quoted in BTC) |
| client_order_id | string | Client order ID set by the client for internal reference. It should be unique, but there are no additional constraints or checks guaranteed on the field by Bitstamp. |
| margin_mode | string | Margin mode. Required for derivatives markets. |
| leverage | string | Leverage rate. Required for derivatives markets. |
| stop_price | string | When the stop price is reached, a stop order becomes a limit/market order. (Derivatives only) |
| trigger | string | Trigger price type that stop price is matching or goes over a market price. (Derivatives only) |
| activation_price | string | When the activation price is reached, a trailing order starts trailing the market price in favorable direction. (Derivatives only) |
| trailing_delta | integer | Trailing delta is the percentage of movement in the unfavorable direction from highest or lowest price. The range you can set is in BPS (5% equals 500) and should be between 1 to 2000. (Derivatives only) |
| reduce_only | boolean | A reduce-only order can only reduce your current position. (Derivatives only) |

### BuySellOrderResponse

| Property | Type | Description |
|----------|------|-------------|
| subtype | string | Order subtype. (Derivatives only) |
| id | string | Order ID. |
| market | string | Market formatted as "BTC/USD". |
| datetime | string | Date and time. |
| type | string | 0 (buy) or 1 (sell). |
| price | string | Price. |
| amount | string | Amount. |
| client_order_id | string | Client order ID sent with request. Only returned if parameter was used in request. |
| margin_mode | string | Margin mode. (Derivatives only) |
| leverage | string | Leverage rate. (Derivatives only) |
| stop_price | string | When the stop price is reached, a stop order becomes a limit/market order. (Derivatives only) |
| trigger | string | Trigger price type that stop price is matching or goes over a market price. (Derivatives only) |
| activation_price | string | When the activation price is reached, a trailing order starts trailing the market price in favorable direction. (Derivatives only) |
| trailing_delta | integer | Trailing delta is the percentage of movement in the unfavorable direction from highest or lowest price. The range you can set is in BPS (5% equals 500) and should be between 1 to 2000. (Derivatives only) |

### CancelAllOrdersResponse

| Property | Type | Description |
|----------|------|-------------|
| canceled | array |  |
| success | boolean | "true" if all orders were successfully canceled and "false" otherwise |

### CancelBankOrCryptoWithdrawalRequest

| Property | Type | Description |
|----------|------|-------------|
| id | string | ID of the withdrawal request. |

### CancelBankWithdrawalResponse

| Property | Type | Description |
|----------|------|-------------|
| id | string | ID of the cancelled withdrawal request. |
| amount | number | Amount of the cancelled withdrawal request. |
| currency | string | Currency of the cancelled withdrawal request. |
| account_currency | string | Account currency (balance currency from which the withdrawal was requested) of the cancelled withdrawal request. |
| type | string | The type of the cancelled withdrawal request. |

### CancelOrderRequest

| Property | Type | Description |
|----------|------|-------------|
| id | string | Order ID. |
| client_order_id | string | Client Order ID. |

### CancelOrderResponse

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Order ID. |
| amount | number | Order amount. |
| price | number | Order price. |
| type | integer | Order type. |
| market | string | Market formatted as "BTC/USD". |
| status | string | Order status. |

### ClosePositionActionSchema

| Property | Type | Description |
|----------|------|-------------|
| position_id | string | Position id. |

### ClosePositionsActionSchema

| Property | Type | Description |
|----------|------|-------------|
| market | string | Market name. |
| margin_mode | string | Margin mode. |
| order_type | string | Order type. |

### ClosedPosition

| Property | Type | Description |
|----------|------|-------------|
| id | string | Position id. |
| market | string | Market name. |
| market_type | string | Market type. |
| margin_mode | string | Margin mode. |
| pnl_currency | string | Settlement currency. |
| entry_price | string | Entry price. |
| pnl_percentage | string | Profit & loss in percentage. |
| pnl_realized | string | Realized profit & loss (in settlement currency). |
| pnl_settled | string | Profit & loss settled |
| leverage | string | Leverage. |
| pnl | string | Profit & loss. |
| cumulative_price_pnl | string | Accumulated price profit & loss since inception. If not available set to null. |
| cumulative_trading_fees | string | Accumulated trading fees since inception. If not available set to null. |
| cumulative_liquidation_fees | string | Accumulated liquidation fees since inception. If not available set to null. |
| cumulative_funding | string | Accumulated funding acquired during settlement since inception. If not available set to null. |
| cumulative_socialized_loss | string | Accumulated socialized loss acquired during settlement since inception. If not available set to null. |
| amount_delta | string | Max range between min and max amount. |
| time_opened | string | Position open timestamp in microseconds. |
| time_closed | string | Position close timestamp in microseconds. |
| status | string | Position status |
| exit_price | string | Exit price. |
| settlement_price | string | Settlement price. |
| closing_fee_amount | string | Closing fee amount |

### ClosedPositionSchema

| Property | Type | Description |
|----------|------|-------------|
| id | string | Position id. |
| market | string | Market name. |
| market_type | string | Market type. |
| margin_mode | string | Margin mode. |
| pnl_currency | string | Settlement currency. |
| entry_price | string | Entry price. |
| pnl_percentage | string | Profit & loss in percentage. |
| pnl_realized | string | Realized profit & loss (in settlement currency). |
| pnl_settled | string | Profit & loss settled |
| leverage | string | Leverage. |
| pnl | string | Profit & loss. |
| cumulative_price_pnl | string | Accumulated price profit & loss since inception. If not available set to null. |
| cumulative_trading_fees | string | Accumulated trading fees since inception. If not available set to null. |
| cumulative_liquidation_fees | string | Accumulated liquidation fees since inception. If not available set to null. |
| cumulative_funding | string | Accumulated funding acquired during settlement since inception. If not available set to null. |
| cumulative_socialized_loss | string | Accumulated socialized loss acquired during settlement since inception. If not available set to null. |
| amount_delta | string | Max range between min and max amount. |
| time_opened | string | Position open timestamp in microseconds. |
| time_closed | string | Position close timestamp in microseconds. |
| status | string | Position status |
| exit_price | string | Exit price. |
| settlement_price | string | Settlement price. |
| closing_fee_amount | string | Closing fee amount |

### ClosedPositionsSchema

| Property | Type | Description |
|----------|------|-------------|
| closed | array |  |
| failed | array |  |

### CollateralChangeImpactActionSchema

| Property | Type | Description |
|----------|------|-------------|
| margin_mode | string | Margin mode. |
| market | string | Market should be included only when using ISOLATED margin mode. |
| target_collateral | object | Dictionary of currencies with final collateral amounts. Exactly one of target_collateral or collateral_deltas should be specified. |
| collateral_deltas | object | Dictionary of currencies with collateral deltas. Exactly one of target_collateral or collateral_deltas should be specified. |

### CollateralChangeImpactDataSchema

| Property | Type | Description |
|----------|------|-------------|
| margin_currency | string | Margin currency. |
| estimated_initial_margin_ratio | string | Estimated initial margin ratio after change. |
| estimated_maintenance_margin_ratio | string | Estimated maintenance margin ratio after change. |
| estimated_liquidation_prices | object | For ISOLATED margin mode returns the respective position id and liquidation prices. For CROSS margin mode returns all CROSS position ids and their respective liquidation prices. |
| total_estimated_margin | string | For CROSS margin mode account margin including adjustments. For ISOLATED equity of position. |

### CollateralCurrenciesSchema

| Property | Type | Description |
|----------|------|-------------|
| currency | string | Currency. |
| haircut | string | Currency haircut. |

### ContactSchema

| Property | Type | Description |
|----------|------|-------------|
| retail_info |  | Additional info if the beneficiary is a retail client |
| corporate_info |  | Additional info if the beneficiary is a corporate client |
| id | string | Id of the contact |
| description | string | Alias for your internal usage of the contact |

### CorporateInfo

| Property | Type | Description |
|----------|------|-------------|
| company_name | string | Name of the company |
| address | string |  |
| country | string | ISO 3166-1 alpha 2 country code |
| lei | string |  |
| company_id | string |  |

### CorporateInfoSchemaWithB2B2CValidation

| Property | Type | Description |
|----------|------|-------------|
| company_name | string | Name of the company |
| address | string |  |
| country | string | ISO 3166-1 alpha 2 country code |
| lei | string |  |
| company_id | string |  |

### CryptoTransaction

| Property | Type | Description |
|----------|------|-------------|
| currency | string | Currency. |
| network | string | Cryptocurrency network. |
| destinationAddress | string | Destination address. |
| txid | string | Transaction hash. |
| amount | number | Amount. |
| datetime | integer | Date and time. |

### CryptoTransactionDeposit

| Property | Type | Description |
|----------|------|-------------|
| id | integer | deposit ID |
| network | string | Cryptocurrency network. |
| currency | string | Cryptocurrency. |
| txid | string | Bitstamp's transaction id. |
| amount | number | Cryptocurrency amount. |
| datetime | integer | deposit creation datetime. |
| status | string | Status of deposit review. |
| pending_reason | string | Reason that deposit review is in pending. |
| destinationAddress | string | Deposit destination address |

### CryptoTransactionDepositsActionSchema

| Property | Type | Description |
|----------|------|-------------|
| originator_thirdparty | boolean | If the address you are depositing from is in your name (regardless of if this is a hosted or unhosted wallet), this should be set to False. If you are depositing from a third party, set it to True. |
| originator_id | string | If setting the originator_thirdparty field to True, you need to provide the UUID of the contact from the /v2/travel_rule/contacts/ endpoint or provide originator_info. |
| originator_info |  | If setting the originator_thirdparty field to True, you need to provide originator_info in JSON form of the object from /v2/travel_rule/contacts/ endpoint or provide originator_id. |
| beneficiary_info |  | Processing of beneficiary_info is enabled by request. You need to provide the contact object in JSON form and the contact information should represent the receiver details. For corporate users, the LEI or company ID is mandatory. For retail users, the date and place of birth or ID type and number are mandatory. |
| vasp_uuid | string | When depositing from a hosted wallet by a Virtual Asset Services Provider, provide the UUID from the /v2/travel_rule/vasps/ endpoint. |

### CryptoTransactionDepositsDataSchema

| Property | Type | Description |
|----------|------|-------------|
| id | integer | deposit ID |
| network | string | Cryptocurrency network. |
| currency | string | Cryptocurrency. |
| destination_address | string | Deposit destination address |
| txid | string | Bitstamp's transaction id. |
| amount | number | Cryptocurrency amount. |
| datetime | integer | deposit creation datetime. |
| status | string | Status of deposit review. |
| pending_reason | string | Reason that deposit review is in pending. |

### CryptoTransactionsRequest

| Property | Type | Description |
|----------|------|-------------|
| limit | integer | Limit result to that many transactions (default: 100; maximum: 1000). |
| offset | integer | Skip that many transactions before returning results (default: 0, maximum: 200000). |
| include_ious | boolean | True - shows also ripple IOU transactions. |
| since_timestamp | string | (Optional) Show only transactions from unix timestamp (for max 30 days old). |
| until_timestamp | string | (Optional) Show only transactions to unix timestamp (for max 30 days old). |

### CryptoTransactionsResponse

| Property | Type | Description |
|----------|------|-------------|
| ripple_iou_transactions | array | Ripple IOU transactions. |
| deposits | array | Deposits. |
| withdrawals | array | Withdrawals. |

### CryptoWithdrawalRequest

| Property | Type | Description |
|----------|------|-------------|
| network | string | Cryptocurrency network. |
| amount | number | Cryptocurrency amount. |
| address | string | Cryptocurrency address. |
| memo_id | string | Address memo id - applicable to: XLM, HBAR, GYEN, VCHF, VEUR, ZUSD, COREUM, SEI, TON, ATOM. |
| destination_tag | string | Address destination tag - applicable to: XRP. |
| transfer_id | integer | Address transfer id - applicable to: CSPR. |
| originator_info |  | Processing of originator_info is enabled by request. You need to provide the contact object in JSON form and the contact information should represent the sender details (if the withdrawal is not being initiated in your name).For corporate users, the LEI or company ID is mandatory. For retail users, the date and place of birth or ID type and number are mandatory. |
| beneficiary_info |  | If setting the beneficiary_thirdparty field to True, you need to provide beneficiary_info in JSON form of the object from /v2/travel_rule/contacts/ endpoint or provide beneficiary_id. |
| beneficiary_thirdparty | boolean | If the address you are withdrawing to is in your name (regardless of if this is a hosted or unhosted wallet), this should be set to False. If you are withdrawing to a third party, set it to True. |
| beneficiary_id | string | If setting the beneficiary_thirdparty field to True, you need to provide the UUID of the contact from the /v2/travel_rule/contacts/ endpoint or provide beneficiary_info. |
| vasp_uuid | string | When withdrawing to a hosted wallet by a Virtual Asset Services Provider, provide the UUID from the /v2/travel_rule/vasps/ endpoint. |

### CryptoWithdrawalResponse

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Withdrawal ID. |

### CurrencyNetwork

| Property | Type | Description |
|----------|------|-------------|
| network | string |  |
| withdrawal_minimum_amount | string |  |
| withdrawal_decimals | integer |  |
| deposit | string |  |
| withdrawal | string |  |

### CurrencySchema

| Property | Type | Description |
|----------|------|-------------|
| name | string |  |
| currency | string |  |
| type | string |  |
| symbol | string |  |
| decimals | integer |  |
| logo | string |  |
| available_supply | string |  |
| deposit | string |  |
| withdrawal | string |  |
| networks | array |  |

### CustomerInfo

| Property | Type | Description |
|----------|------|-------------|
| retail_info |  | Additional info if the beneficiary is a retail client |
| corporate_info |  | Additional info if the beneficiary is a corporate client |

### CustomerInfoWithB2B2CValidation

| Property | Type | Description |
|----------|------|-------------|
| retail_info |  | Additional info if the beneficiary is a retail client |
| corporate_info |  | Additional info if the beneficiary is a corporate client |

### DepositAddressRequest

| Property | Type | Description |
|----------|------|-------------|
| network | string | Cryptocurrency network. |

### DepositAddressResponse

| Property | Type | Description |
|----------|------|-------------|
| address | string | Address for requested currency. |
| memo_id | string | Memo ID in case of network HBAR or XLM, otherwise not present. |
| destination_tag | integer | Destination tag in case of currency XRP or Ripple, otherwise not present. |
| transfer_id | integer | Transfer ID in case of network CSPR, otherwise not present. |

### EarnSubscriptionSchema

| Property | Type | Description |
|----------|------|-------------|
| currency | string | Currency |
| earn_type | string | Type of Earn product |
| earn_term | string | Type of Earn term |
| amount | number | Amount to subscribe or unsubscribe with. |

### EarnSubscriptionSettingSchema

| Property | Type | Description |
|----------|------|-------------|
| setting | string | Type of setting action. |
| currency | string | Currency |
| earn_type | string | Type of Earn product |

### EarnSubscriptionsSchema

| Property | Type | Description |
|----------|------|-------------|
| currency | string | Currency |
| type | string | Type of Earn product |
| term | string | Type of Earn term |
| estimated_annual_yield | number | Estimated annual yield |
| distribution_period | string | Period in which the rewards are distributed |
| activation_period | string | Expected time until earn option starts to earn rewards |
| minimum_subscription_amount | number | Minimum amount for subscription |
| amount | number | Amount on which you are earning interest |
| available_amount | number | Amount on which you are earning interest that is available to withdraw from Earn |
| amount_earned | number | Amount that has been earned |

### EarnTransactionSchema

| Property | Type | Description |
|----------|------|-------------|
| datetime | string | Date and time of earn history event |
| type | string | Type of earn history event |
| amount | number | Amount in base currency |
| currency | string | Currency |
| value | number | Amount in quote currency |
| quote_currency | string | Currency in which value is calculated |
| status | string | Status of earn history event |

### EmptySchema

| Property | Type | Description |
|----------|------|-------------|

### ErrorResponse

| Property | Type | Description |
|----------|------|-------------|
| status | string | "error" |
| reason | string | Error reason. |

### ErrorSchema

| Property | Type | Description |
|----------|------|-------------|
| code | string |  |
| message | string |  |
| field | string |  |

### EstimatedOrderImpactActionSchema

| Property | Type | Description |
|----------|------|-------------|
| market | string | Market name. |
| order_type | string | Order type. |
| amount | number | New order amount. |
| order_side | string | Order side. |
| margin_mode | string | Margin mode. |
| leverage | number | Leverage value. |
| price | number | Price. |
| reduce_only | boolean | A reduce-only order can only reduce your current position. |

### EstimatedOrderImpactDataSchema

| Property | Type | Description |
|----------|------|-------------|
| margin_currency | string | Margin currency. |
| additional_required_margin | string | Estimated additional required margin to allow such an order to be placed. This includes the margin required to restore IM requirements of existing position(s) on top of the IM requirements for the order. |
| margin_required_for_order | string | Estimated additional margin that the order would occupy, without the margin required to restore IM requirements of existing position(s). |
| estimated_liquidation_prices | object | If available, then estimated liquidation prices (ELP) simulating the order placement are returned. For ISOLATED margin mode only the ELP of the submitted market is returned. For CROSS margin mode, in addition to the submitted market, ELPs for any markets where you have open CROSS positions are returned. Returns a dict of markets as keys and ELPs as values. |
| estimated_fee | string | Estimated fee. |
| is_order_placeable | string | Outcome of checking if order can be placed. |
| margin_tier |  | Margin tier details. |

### EurUsdConversionRateResponse

| Property | Type | Description |
|----------|------|-------------|
| buy | string | Buy conversion rate. |
| sell | string | Sell conversion rate. |

### Fee

| Property | Type | Description |
|----------|------|-------------|
| maker | string | Fee for maker of the market. |
| taker | string | Fee for taker of the market. |

### FeeTradingResponse

| Property | Type | Description |
|----------|------|-------------|
| currency_pair | string | Currency pair name (deprecated). |
| market | string | Market for fees. |
| fees |  | Dictionary of maker and taker fees. |

### FeeWithdrawalRequest

| Property | Type | Description |
|----------|------|-------------|
| network | string | Cryptocurrency network. |

### FeeWithdrawalResponse

| Property | Type | Description |
|----------|------|-------------|
| currency | string | Currency name. |
| fee | string | Customer withdrawal fee. |
| network | string | Cryptocurrency network. |

### FundingRateHistorySchema

| Property | Type | Description |
|----------|------|-------------|
| market | string | Market name. |
| funding_rate_history | array | History of funding rates. |

### FundingRateSchema

| Property | Type | Description |
|----------|------|-------------|
| funding_rate | string | Funding rate. |
| timestamp | string | Funding rate unix timestamp. |
| market | string | Market name. |
| next_funding_time | string | Next funding time unix timestamp. |

### InstantConvertAddressInfoRequest

| Property | Type | Description |
|----------|------|-------------|
| address | string | Shows transactions for specific instant convert address or for all users instant convert addresses. |

### InstantConvertAddressInfoResponse

| Property | Type | Description |
|----------|------|-------------|
| address | string | Address set for automatic conversion |
| currency_pair | string | Currency pair. |
| transactions | array | List of transactions. |

### LeverageSettingsActionSchema

| Property | Type | Description |
|----------|------|-------------|
| margin_mode | string | Margin mode. |
| market | string | Market name. |
| leverage | number | Leverage value. |

### LeverageSettingsDataSchema

| Property | Type | Description |
|----------|------|-------------|
| margin_mode | string | Margin mode. |
| market | string | Market name. |
| leverage_current | string | Current leverage. |
| leverage_max | string | Max possible leverage. |

### MarginInfoSchema

| Property | Type | Description |
|----------|------|-------------|
| account_margin | string | Total value of collateral assets in account_margin_currency |
| account_margin_available | string | Gross available value of collateral assets in account_margin_currency |
| account_margin_reserved | string | Gross reserved value of collateral assets in account_margin_currency |
| account_margin_currency | string | Account margin currency |
| assets | array | Margin info per asset |
| initial_margin_ratio | string | Initial margin ratio. If not available set to null. |
| maintenance_margin_ratio | string | Maintenance margin ratio. If not available set to null. |
| implied_leverage | string | Implied leverage. If not available set to null. |

### MarketMarginTiersSchema

| Property | Type | Description |
|----------|------|-------------|
| market | string | Market |
| tiers | array | List of margin tiers for the market. |

### MarketSchema

| Property | Type | Description |
|----------|------|-------------|
| name | string | Market name. |
| market_symbol | string | Symbol of market (used in url). |
| base_currency | string | Market's base currency. |
| base_decimals | integer | Decimal precision for base currency (BTC/USD - base: BTC). |
| counter_currency | string | Market's counter currency. |
| counter_decimals | integer | Decimal precision for counter currency (BTC/USD - counter: USD). |
| minimum_order_value | string | Minimum order size in counter currency. |
| maximum_order_value | string | Maximum order size in counter currency. |
| minimum_order_amount | string | Minimum order amount in base currency. |
| maximum_order_amount | string | Maximum order amount in base currency. |
| trading | string | Trading engine status (Enabled/Disabled). |
| instant_order_counter_decimals | integer | Decimal precision for counter currency for instant buy and cash sell orders. |
| instant_and_market_orders | string | Instant and market orders status (Enabled/Disabled). |
| description | string | Market description. |
| market_type | string | Market type. |
| underlying_asset | string | Underlying asset for derivatives. |
| payoff_type | string | Payoff type (Linear) for derivatives. |
| contract_size | string | Contract size in base currency for derivatives. |
| tick_size | string | Tick size. |
| isin | string | International Securities Identification Number for derivatives. |

### MaxBuySellActionSchema

| Property | Type | Description |
|----------|------|-------------|
| market | string | Market name. |
| margin_mode | string | Margin mode. |
| leverage | number | Leverage. |
| order_type | string | Order type. |
| side | string | Order side. |
| price | number | Order limit price. |
| stop_price | number | Stop price for Stop Loss, Take Profit, Stop Loss Limit and Take Profit Limit orders. |
| activation_price | number | Activation price for trailing orders. |
| trailing_delta | integer | Trailing delta for trailing orders. |
| additional_collateral | object | Dictionary of additional collateral to take into account when estimating max buy/sell. Keys should be supported collateral currencies, like {"BTC": "1.01"}. |

### MaxBuySellSchema

| Property | Type | Description |
|----------|------|-------------|
| maximum_order_amount | string |  |
| maximum_order_value | string |  |
| maximum_order_amount_currency | string |  |
| maximum_order_value_currency | string |  |

### NewInstantConvertAddressRequest

| Property | Type | Description |
|----------|------|-------------|
| liquidation_currency | string | Deposited BTCs will be automatically converted to liquidation_currency. |
| address_format | string | 	Address format. Can be either "P2SHP2WSH" or "BECH32". |

### NewInstantConvertAddressResponse

| Property | Type | Description |
|----------|------|-------------|
| address | string | Address set for automatic conversion. |

### OHLCData

| Property | Type | Description |
|----------|------|-------------|
| timestamp | string | Unix timestamp date and time. |
| open | string | Opening price. |
| high | string | Price high. |
| low | string | Price low. |
| close | string | Closing price. |
| volume | string | Volume. |

### OHLCDataResponseSchema

| Property | Type | Description |
|----------|------|-------------|
| pair | string | Trading pair. |
| market | string | Market. |
| ohlc | array | OHLC data. |

### OpenBankWithdrawalRequest

| Property | Type | Description |
|----------|------|-------------|
| amount | string | The amount to withdraw. |
| account_currency | string | The balance from which you wish to withdraw. Can be either "USD", "EUR" or "GBP". |
| name | string | Full user or company name. |
| iban | string | User or company IBAN. |
| bic | string | The target bank BIC. |
| address | string | User or company address. |
| postal_code | string | User or company postal code. |
| city | string | User or company city. |
| country | string | User or company country. Country codes must be in accordance with the ISO 3166-1 standard (use two character Alpha-2 codes). Disclaimer: Not all country choices listed at this reference URL are supported. For a detailed list please refer to our platform's withdrawal interfaces. |
| type | string | Type of the withdrawal request ("sepa" or "international"). |
| bank_name | string | Target bank name (international withdrawals only). |
| bank_address | string | Target bank address (international withdrawals only). |
| bank_postal_code | string | Target bank postal code (international withdrawals only). |
| bank_city | string | Target bank city (international withdrawals only). |
| bank_country | string | Target bank country. Country codes must be in accordance with the ISO 3166-1 standard (use two character Alpha-2 codes). Disclaimer: Not all country choices listed at this reference URL are supported. For a detailed list please refer to our platform's withdrawal interfaces (international withdrawals only). |
| currency | string | The currency in which the funds should be withdrawn (may involve conversion fees). Currency codes must be in accordance with the ISO 4217 standard. Disclaimer: Not all currency choices listed at this reference URL are supported. For a detailed list please refer to our platform's withdrawal interfaces. (international withdrawals only) |
| comment | string | Withdrawal comment. |
| intermed_routing_num_or_bic | string | Intermediary bank routing number / bic |

### OpenBankWithdrawalResponse

| Property | Type | Description |
|----------|------|-------------|
| withdrawal_id | integer | Withdrawal ID. |

### OpenOrdersAllResponse

| Property | Type | Description |
|----------|------|-------------|
| id | string | Order ID. |
| datetime | string | Date and time. |
| type | string | Order type: 0 - buy; 1 - sell. |
| subtype | string | Order subtype. (Derivatives only) |
| price | string | Price. |
| amount | string | Remaining amount. |
| amount_at_create | string | Initial amount. |
| currency_pair | string | Currency Pair (deprecated). |
| market | string | Market formatted as "BTC/USD". |
| limit_price | string | Limit price. (Only returned if limit order was placed with limit_price parameter.) |
| client_order_id | string | Client order id. (Only returned if order was placed with client order id parameter.) |
| margin_mode | string | Margin mode. (Derivatives only) |
| leverage | string | Leverage rate. (Derivatives only) |
| reserved_margin | string | Reserved margin amount. (Derivatives only) |
| stop_price | string | When the stop price is reached, a stop order becomes a limit/market order. (Derivatives only) |
| trigger | string | Trigger price type that stop price is matching or goes over a market price. (Derivatives only) |
| activation_price | string | When the activation price is reached, a trailing order starts trailing the market price in favorable direction. (Derivatives only) |
| trailing_delta | integer | Trailing delta is the percentage of movement in the unfavorable direction from highest or lowest price. The range you can set is in BPS (5% equals 500) and should be between 1 to 2000. (Derivatives only) |
| reduce_only | boolean | A reduce-only order can only reduce your current position. (Derivatives only) |

### OpenOrdersPairResponse

| Property | Type | Description |
|----------|------|-------------|
| id | string | Order ID. |
| datetime | string | Date and time. |
| type | string | Order type: 0 - buy; 1 - sell. |
| subtype | string | Order subtype. (Derivatives only) |
| price | string | Price. |
| amount | string | Remaining amount. |
| amount_at_create | string | Initial amount. |
| market | string | Market formatted as "BTC/USD". |
| limit_price | string | Limit price. (Only returned if limit order was placed with limit_price parameter.) |
| client_order_id | string | Client order id. (Only returned if order was placed with client order id parameter.) |
| margin_mode | string | Margin mode. (Derivatives only) |
| leverage | string | Leverage rate. (Derivatives only) |
| reserved_margin | string | Reserved margin amount. (Derivatives only) |
| stop_price | string | When the stop price is reached, a stop order becomes a limit/market order. (Derivatives only) |
| trigger | string | Trigger price type that stop price is matching or goes over a market price. (Derivatives only) |
| activation_price | string | When the activation price is reached, a trailing order starts trailing the market price in favorable direction. (Derivatives only) |
| trailing_delta | integer | Trailing delta is the percentage of movement in the unfavorable direction from highest or lowest price. The range you can set is in BPS (5% equals 500) and should be between 1 to 2000. (Derivatives only) |
| reduce_only | boolean | A reduce-only order can only reduce your current position. (Derivatives only) |

### OpenPositionSchema

| Property | Type | Description |
|----------|------|-------------|
| id | string | Position id. |
| market | string | Market name. |
| market_type | string | Market type. |
| margin_mode | string | Margin mode. |
| settlement_currency | string | Settlement currency. |
| entry_price | string | Entry price. |
| pnl_percentage | string | Profit & loss in percentage. |
| pnl_realized | string | Realized profit & loss (in settlement currency). |
| pnl_settled_since_inception | string | Profit & loss settled since inception. |
| leverage | string | Leverage. |
| pnl | string | Profit & loss. |
| cumulative_price_pnl | string | Accumulated price profit & loss since inception. If not available set to null. |
| cumulative_trading_fees | string | Accumulated trading fees since inception. If not available set to null. |
| cumulative_liquidation_fees | string | Accumulated liquidation fees since inception. If not available set to null. |
| cumulative_funding | string | Accumulated funding acquired during settlement since inception. If not available set to null. |
| cumulative_socialized_loss | string | Accumulated socialized loss acquired during settlement since inception. If not available set to null. |
| size | string | Position size |
| pnl_unrealized | string | Unrealized profit & loss (in settlement currency). |
| pnl_in_settlement | string | The profits and losses of open and closed positions that are to be settled within the currently running periodic settlement. |
| implied_leverage | string | Implied leverage. If not available set to null. |
| initial_margin | string | Initial margin. |
| initial_margin_ratio | string | Initial margin ratio. If not available set to null. |
| current_margin | string | Current margin. |
| collateral_reserved | string | Collateral reserved for this isolated position. |
| maintenance_margin | string | Maintenance margin. |
| maintenance_margin_ratio | string | Maintenance margin ratio. If not available set to null. |
| estimated_liquidation_price | string | Estimated liquidation price. |
| estimated_closing_fee_amount | string | Estimated closing fee amount. |
| mark_price | string | Mark price. |
| current_value | string | Position current value. |
| entry_value | string | Position entry value. |
| strike_price | string | Position strike price. |
| side | string | Contract side. |
| margin_tier | string | Margin tier. |

### Order

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Order ID. |
| amount | number | Order amount. |
| price | number | Order price. |
| type | integer | Order type. |
| currency_pair | string | Currency pair formatted as "BTC/USD". |
| market | string | Market formatted as "BTC/USD". |

### OrderBookResponse

| Property | Type | Description |
|----------|------|-------------|
| timestamp | string | Unix timestamp date and time. |
| microtimestamp | string | Unix timestamp date and time in microseconds. |
| bids | array | List of buy orders. |
| asks | array | List of sell orders. |

### OrderDataRequest

| Property | Type | Description |
|----------|------|-------------|
| market | string | Market symbol (e.g., "BTC/USD"). |
| since_id | string | Starting MarketEventID (inclusive, hex format). If omitted, defaults to 24h before until_id. |
| until_id | string | Ending MarketEventID (exclusive, hex format). If omitted, defaults to now. |

### OrderEvent

| Property | Type | Description |
|----------|------|-------------|
| event | string | Event type: order_created, order_changed, order_deleted, stop_active, stop_inactive. |
| event_id | string | MarketEventID in hex format for pagination (format: 4-2-2-2-6 hex grouping). |
| order_source | string | Order source: orderbook or stop_order. |
| data |  | Order event data. |

### OrderStatusRequest

| Property | Type | Description |
|----------|------|-------------|
| id | string | Order ID. |
| client_order_id | string | (Optional) Client order id. (Can only be used if order was placed with client order id parameter.). |
| omit_transactions | string | (Optional) Omits list of transactions for order ID. Possible value: True |

### OrderStatusResponse

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Order ID. |
| datetime | string | Date and time. |
| type | string | Type: 0 - buy; 1 - sell. |
| subtype | string | Order subtype. (Derivatives only) |
| status | string | Open, Finished, Expired or Canceled. |
| market | string | Market formatted as "BTC/USD". |
| transactions | array |  |
| amount_remaining | string | Amount remaining. |
| client_order_id | string | Client order id. (Only returned if order was placed with client order id parameter.). |
| margin_mode | string | Margin mode. (Derivatives only) |
| leverage | string | Leverage rate. (Derivatives only) |
| stop_price | string | When the stop price is reached, a stop order becomes a limit/market order. (Derivatives only) |
| trigger | string | Trigger price type that stop price is matching or goes over a market price. (Derivatives only) |
| activation_price | string | When the activation price is reached, a trailing order starts trailing the market price in favorable direction. (Derivatives only) |
| trailing_delta | integer | Trailing delta is the percentage of movement in the unfavorable direction from highest or lowest price. The range you can set is in BPS (5% equals 500) and should be between 1 to 2000. (Derivatives only) |

### OrderTransaction

| Property | Type | Description |
|----------|------|-------------|
| tid | integer | Transaction ID. |
| price | string | Price. |
| {from_currency} | string | {from_currency} amount. |
| {to_currency} | string | {to_currency} amount. |
| fee | string | Transaction fee. |
| datetime | string | Date and time. |
| type | integer | Transaction type: 0 - deposit; 1 - withdrawal; 2 - market trade. |

### PaginationSchema

        Pagination schema for response.
        Args:
            page: (int) page number
            size: (int) page full size
            count:  (int) number of items in current page
        

| Property | Type | Description |
|----------|------|-------------|
| page | integer |  |
| size | integer |  |
| count | integer |  |

### PositionHistorySchema

| Property | Type | Description |
|----------|------|-------------|
| id | string | Position id. |
| market | string | Market name. |
| market_type | string | Market type. |
| margin_mode | string | Margin mode. |
| pnl_currency | string | Settlement currency. |
| entry_price | string | Entry price. |
| pnl_percentage | string | Profit & loss in percentage. |
| pnl_realized | string | Realized profit & loss (in settlement currency). |
| pnl_settled | string | Profit & loss settled |
| leverage | string | Leverage. |
| pnl | string | Profit & loss. |
| cumulative_price_pnl | string | Accumulated price profit & loss since inception. If not available set to null. |
| cumulative_trading_fees | string | Accumulated trading fees since inception. If not available set to null. |
| cumulative_liquidation_fees | string | Accumulated liquidation fees since inception. If not available set to null. |
| cumulative_funding | string | Accumulated funding acquired during settlement since inception. If not available set to null. |
| cumulative_socialized_loss | string | Accumulated socialized loss acquired during settlement since inception. If not available set to null. |
| amount_delta | string | Max range between min and max amount. |
| time_opened | string | Position open timestamp in microseconds. |
| time_closed | string | Position close timestamp in microseconds. |
| status | string | Position status |
| exit_price | string | Exit price. |
| settlement_price | string | Settlement price. |

### PositionSettlementTransactionSchema

| Property | Type | Description |
|----------|------|-------------|
| transaction_id | string | Transaction id. Used by the since_id parameter. |
| position_id | string | Position id. |
| settlement_time | integer | Settlement timestamp. |
| settlement_type | string | Settlement type. |
| settlement_price | string | Settlement price. Not available for CLOSED settlement types. |
| market | string | Market name. |
| market_type | string | Market type. |
| pnl_currency | string | Profit & loss currency. |
| pnl_settled | string | Profit & loss settled. |
| pnl_component_price | string | Profit & loss component price. |
| pnl_component_fees | string | Profit & loss component fees. |
| pnl_component_funding | string | Profit & loss component funding. |
| pnl_component_socialized_loss | string | Profit & loss component socialized loss. |
| margin_mode | string | Margin mode. |
| size | string | Position size |
| strike_price | string | Strike price. |
| fees_component_trading | string | Trading fees. |
| fees_component_liquidation | string | Liquidation fees. |

### PositionStatusSchema

| Property | Type | Description |
|----------|------|-------------|
| id | string | Position id. |
| market | string | Market name. |
| market_type | string | Market type. |
| margin_mode | string | Margin mode. |
| settlement_currency | string | Settlement currency. |
| entry_price | string | Entry price. |
| pnl_percentage | string | Profit & loss in percentage. |
| pnl_realized | string | Realized profit & loss (in settlement currency). |
| pnl_settled_since_inception | string | Profit & loss settled since inception. |
| leverage | string | Leverage. |
| pnl | string | Profit & loss. |
| cumulative_price_pnl | string | Accumulated price profit & loss since inception. If not available set to null. |
| cumulative_trading_fees | string | Accumulated trading fees since inception. If not available set to null. |
| cumulative_liquidation_fees | string | Accumulated liquidation fees since inception. If not available set to null. |
| cumulative_funding | string | Accumulated funding acquired during settlement since inception. If not available set to null. |
| cumulative_socialized_loss | string | Accumulated socialized loss acquired during settlement since inception. If not available set to null. |
| pnl_in_settlement | string | The profits and losses of open and closed positions that are to be settled within the currently running periodic settlement. |
| time_opened | string | Position open timestamp in microseconds. |
| status | string | Position status. |
| margin_tier | string | Margin tier. |
| side | string | Contract side. Open positions only. |
| size | string | Position size. Open positions only. |
| pnl_unrealized | string | Unrealized profit & loss (in settlement currency). Open positions only. |
| implied_leverage | string | Implied leverage. If not available set to null. Open positions only. |
| initial_margin | string | Initial margin. Open positions only. |
| initial_margin_ratio | string | Initial margin ratio. If not available set to null. Open positions only. |
| current_margin | string | Current margin. Open positions only. |
| collateral_reserved | string | Collateral reserved for this isolated position. Open positions only. |
| maintenance_margin | string | Maintenance margin. Open positions only. |
| maintenance_margin_ratio | string | Maintenance margin ratio. If not available set to null. Open positions only. |
| estimated_liquidation_price | string | Estimated liquidation price. Open positions only. |
| estimated_closing_fee_amount | string | Estimated closing fee amount. Open positions only. |
| mark_price | string | Mark price. Open positions only. |
| current_value | string | Position current value. Open positions only. |
| entry_value | string | Position entry value. Open positions only. |
| strike_price | string | Position strike price. Open positions only. |
| exit_price | string | Exit price. Closed positions only. |
| settlement_price | string | Settlement price. If not available set to null. Closed positions only. |
| amount_delta | string | Max range between min and max amount. Closed positions only. |
| time_closed | string | Position close timestamp in microseconds. Closed positions only. |

### PrivateOrderEventData

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Order ID. |
| id_str | string | Order ID as string. |
| order_type | integer | Order type: 0 - buy; 1 - sell. |
| order_subtype | integer | Order subtype identifier. |
| datetime | string | Unix timestamp in seconds. |
| microtimestamp | string | Unix timestamp in microseconds. |
| amount | number | Remaining amount. |
| amount_str | string | Remaining amount as string (preserves full precision). |
| amount_traded | string | Amount traded (preserves full precision). |
| amount_at_create | string | Initial amount (preserves full precision). |
| price | number | Order price. |
| price_str | string | Order price as string (preserves full precision). |
| is_liquidation | boolean | Whether this is a liquidation order. |
| trade_account_id | integer | Trade account unique ID. 0 represents the main account. Sub-accounts have unique IDs > 0. |
| client_order_id | string | Client-provided order ID. Only present if the order was placed with a client_order_id. |
| reduce_only | boolean | Whether this is a reduce-only order (derivatives only). Only present when the order is reduce-only (true). A reduce-only order can only reduce an existing position, not increase it. |
| stop_price | string | Stop price for stop orders (preserves full precision). Only present for stop orders. |
| activation_price | string | Activation price for trailing orders (preserves full precision). Only present for trailing orders. |
| trailing_delta | integer | Trailing delta in basis points (BPS). Only present for trailing orders. |

### PublicOrderEventData

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Order ID. |
| id_str | string | Order ID as string. |
| order_type | integer | Order type: 0 - buy; 1 - sell. |
| order_subtype | integer | Order subtype identifier. |
| datetime | string | Unix timestamp in seconds. |
| microtimestamp | string | Unix timestamp in microseconds. |
| amount | number | Remaining amount. |
| amount_str | string | Remaining amount as string (preserves full precision). |
| amount_traded | string | Amount traded (preserves full precision). |
| amount_at_create | string | Initial amount (preserves full precision). |
| price | number | Order price. |
| price_str | string | Order price as string (preserves full precision). |
| is_liquidation | boolean | Whether this is a liquidation order. |

### ReplaceOrderRequest

| Property | Type | Description |
|----------|------|-------------|
| id | string | Order ID. |
| orig_client_order_id | string | Original client Order ID of the order being replaced. |
| client_order_id | string | Client Order ID of the new (updated) order. |
| amount | number | Amount. |
| price | number | Price. |

### ReplaceOrderResponse

| Property | Type | Description |
|----------|------|-------------|
| order_id | integer | Order ID. |
| order_type | string | Order type: 0 - buy; 1 - sell. |
| market | string | Market formatted as "BTC/USD". |
| amount | number | Order amount. |
| price | number | Order price. |
| datetime | string | Date and time. |
| orig_order_id | integer | ID of the order that was replaced. |
| orig_client_order_id | string | Client order ID of the order that was replaced (if provided when placing the original order). |
| status | string | Order status. |

### RetailInfo

| Property | Type | Description |
|----------|------|-------------|
| first_name | string | First name of the contact |
| last_name | string | Last name of the contact |
| date_of_birth | string |  |
| place_of_birth | string |  |
| id_type | string |  |
| id_number | string |  |
| street_and_house_number | string |  |
| city | string |  |
| zip | string |  |
| country | string | ISO 3166-1 alpha 2 country code |

### RetailInfoSchemaWithB2B2CValidation

| Property | Type | Description |
|----------|------|-------------|
| first_name | string | First name of the contact |
| last_name | string | Last name of the contact |
| date_of_birth | string |  |
| place_of_birth | string |  |
| id_type | string |  |
| id_number | string |  |
| street_and_house_number | string |  |
| city | string |  |
| zip | string |  |
| country | string | ISO 3166-1 alpha 2 country code |

### RevokedAPIKeySchema

| Property | Type | Description |
|----------|------|-------------|
| revoked_api_keys | array | API keys that were revoked. |

### RippleIOUDepositAddressResponse

| Property | Type | Description |
|----------|------|-------------|
| address | string | Ripple address. |
| destination_tag | integer | Destination tag. |

### RippleIOUWithdrawalRequest

| Property | Type | Description |
|----------|------|-------------|
| currency | string | Currency to withdraw. |
| amount | number | Currency amount. |
| address | string | Ripple address. |
| originator_info |  | Processing of originator_info is enabled by request. You need to provide the contact object in JSON form and the contact information should represent the sender details (if the withdrawal is not being initiated in your name).For corporate users, the LEI or company ID is mandatory. For retail users, the date and place of birth or ID type and number are mandatory. |
| beneficiary_info |  | If setting the beneficiary_thirdparty field to True, you need to provide beneficiary_info in JSON form of the object from /v2/travel_rule/contacts/ endpoint or provide beneficiary_id. |
| beneficiary_thirdparty | boolean | If the address you are withdrawing to is in your name (regardless of if this is a hosted or unhosted wallet), this should be set to False. If you are withdrawing to a third party, set it to True. |
| beneficiary_id | string | If setting the beneficiary_thirdparty field to True, you need to provide the UUID of the contact from the /v2/travel_rule/contacts/ endpoint or provide beneficiary_info. |
| vasp_uuid | string | When withdrawing to a hosted wallet by a Virtual Asset Services Provider, provide the UUID from the /v2/travel_rule/vasps/ endpoint. |

### RippleIOUWithdrawalResponse

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Withdrawal ID. |

### SatoshiTestActionSchema

| Property | Type | Description |
|----------|------|-------------|
| address | string | The external cryptocurrency address to verify. |
| network | string | The cryptocurrency network (e.g., "bitcoin", "ethereum"). |
| currency | string | The transaction currency for the verification test. |

### SatoshiTestDataSchema

| Property | Type | Description |
|----------|------|-------------|
| network | string | The cryptocurrency network (chain currency). |
| currency | string | The transaction currency for the test. |
| amount | number | The small amount to deposit for verification. |
| user_address | string | The external address being verified (the address you control). |
| deposit_address | string | The Bitstamp deposit address to send the test deposit to. |
| status | string | The current status of the verification test. |
| expires | integer | The expiration time for the test. |

### SellInstantOrderRequest

| Property | Type | Description |
|----------|------|-------------|
| amount | number | Amount in base currency (Example: For BTC/USD pair, amount is quoted in BTC) |
| amount_in_counter | boolean | (Optional) Instant sell orders allow you to sell an amount of the base currency determined by the value of it in the counter currency. Amount_in_counter sets the amount parameter to refer to the counter currency instead of the base currency of the selected market. |
| client_order_id | string | Client order ID set by the client for internal reference. It should be unique, but there are no additional constraints or checks guaranteed on the field by Bitstamp. |
| margin_mode | string | Margin mode. (Derivatives only) |
| leverage | string | Leverage rate. (Derivatives only) |
| reduce_only | boolean | A reduce-only order can only reduce your current position. Can not be set to True when using amount_in_counter. (Derivatives only) |

### SimpleErrorResponse

| Property | Type | Description |
|----------|------|-------------|
| error | string | The reason for the error. |

### StatusValues

| Property | Type | Description |
|----------|------|-------------|
| status | string | Order status. |

### TickerHourResponse

| Property | Type | Description |
|----------|------|-------------|
| last | string | Last price. |
| high | string | Last hour price high. |
| low | string | Last hour price low. |
| vwap | string | Last hour volume weighted average price. |
| volume | string | Last hour volume. |
| bid | string | Highest buy order. |
| ask | string | Lowest sell order. |
| timestamp | string | Unix timestamp date and time. |
| open | string | First price of the hour. |
| side | string | Ticker side: 0 - buy; 1 - sell. |
| market_type | string | Market type. |
| mark_price | string | Mark price for derivatives. |
| index_price | string | Index price for derivatives. |
| open_interest | string | Open interest in base currency for derivatives. |
| open_interest_value | string | Open interest in counter currency for derivatives. |

### TickerResponse

| Property | Type | Description |
|----------|------|-------------|
| last | string | Last price. |
| high | string | Last 24 hours price high. |
| low | string | Last 24 hours price low. |
| vwap | string | Last 24 hours volume weighted average price. |
| volume | string | Last 24 hours volume. |
| bid | string | Highest buy order. |
| ask | string | Lowest sell order. |
| timestamp | string | Unix timestamp date and time. |
| open | string | First price of the day. |
| open_24 | string | 24 hours time delta transaction price |
| percent_change_24 | string | 24 hours price change percent |
| side | string | Ticker side: 0 - buy; 1 - sell. |
| market_type | string | Market type. |
| mark_price | string | Mark price for derivatives. |
| index_price | string | Index price for derivatives. |
| open_interest | string | Open interest in base currency for derivatives. |
| open_interest_value | string | Open interest in counter currency for derivatives. |

### TickerWithPairResponse

| Property | Type | Description |
|----------|------|-------------|
| last | string | Last price. |
| high | string | Last 24 hours price high. |
| low | string | Last 24 hours price low. |
| vwap | string | Last 24 hours volume weighted average price. |
| volume | string | Last 24 hours volume. |
| bid | string | Highest buy order. |
| ask | string | Lowest sell order. |
| timestamp | string | Unix timestamp date and time. |
| open | string | First price of the day. |
| open_24 | string | 24 hours time delta transaction price |
| percent_change_24 | string | 24 hours price change percent |
| side | string | Ticker side: 0 - buy; 1 - sell. |
| market_type | string | Market type. |
| mark_price | string | Mark price for derivatives. |
| index_price | string | Index price for derivatives. |
| open_interest | string | Open interest in base currency for derivatives. |
| open_interest_value | string | Open interest in counter currency for derivatives. |
| pair | string | Market name. (Deprecated) |
| market | string | Market name. |

### Trade

| Property | Type | Description |
|----------|------|-------------|
| exchange_rate | string | Exchange rate. |
| btc_amount | string | BTC amount. |
| fees | string | Fees. |

### TradeSchema

| Property | Type | Description |
|----------|------|-------------|
| trade_id | string | Trade ID. |
| order_id | string | Order ID. |
| self_trade_order_id | string | Order ID of the complementary order of the self trade. |
| datetime | string | Date and time. |
| fee | string | Trade fee. |
| liquidation_fee | string | Liquidation fee. |
| fee_currency | string | Trade fee currency. |
| market | string | Market where trade was made. |
| margin_mode | string | Margin mode. |
| leverage | string | Leverage. |
| side | string | Trade side. |
| type | string | Trade type. |
| self_trade_type | string | Trade type of the complementary side of the self trade. |
| price | string | Price. |
| amount | string | Amount. |

### TradingPair

| Property | Type | Description |
|----------|------|-------------|
| name | string | Trading pair. |
| url_symbol | string | URL symbol of trading pair. |

### Transaction

| Property | Type | Description |
|----------|------|-------------|
| order_id | integer | Conversion order ID. |
| count | integer | Number of transactions. |
| trades | array | Trades. |

### TransactionsResponse

| Property | Type | Description |
|----------|------|-------------|
| date | string | Unix timestamp date and time. |
| tid | string | Transaction ID. |
| price | string | Price. |
| amount | string | Amount. |
| type | string | 0 (buy) or 1 (sell). |

### TransferToFromMainRequest

| Property | Type | Description |
|----------|------|-------------|
| amount | number | Amount. |
| currency | string | Currency. |
| subAccount | integer | The Sub Account unique identifier. |

### TransferToFromMainResponse

| Property | Type | Description |
|----------|------|-------------|
| status | string | "ok" or "error" |
| reason | string | Additional error information. |

### UserTransactionsRequest

| Property | Type | Description |
|----------|------|-------------|
| offset | string | Skip that many transactions before returning results (default: 0, maximum: 200000). If you need to export older history contact support OR use combination of limit and since_id parameters. |
| limit | string | Limit result to that many transactions (default: 100; maximum: 1000). |
| sort | string | Sorting by date and time: asc - ascending; desc - descending (default: desc). |
| since_timestamp | string | (Optional) Show only transactions from unix timestamp (for max 30 days old). |
| until_timestamp | string | Show only transactions to unix timestamp (for max 30 days old). |
| since_id | string | (Optional) Show only transactions from specified transaction id. If since_id parameter is used, limit parameter is set to 1000. |

### UserTransactionsResponse

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Transaction ID. |
| datetime | string | Date and time. |
| type | string | Transaction type: 0 - deposit; 1 - withdrawal; 2 - market trade; 14 - sub account transfer; 25 - credited with staked assets; 26 - sent assets to staking; 27 - staking reward; 32 - referral reward; 35 - inter account transfer; 33 - settlement transfer; 36 - simple buy; 53 - small balance conversion; 55 - small balance conversion; 58 - derivatives periodic settlement; 59 - insurance fund claim; 60 - insurance fund premium; 61 - collateral liquidation. |
| fee | string | Transaction fee. |
| {from_currency} | string | {from_currency} amount. |
| {to_currency} | string | {to_currency} amount. |
| {currency_pair} | number | {currency_pair} exchange rate. |
| order_id | integer | Executed order ID. |
| self_trade | boolean | True if transaction is a self trade transaction. |
| self_trade_order_id | integer | Order ID of the complementary order of the self trade. |

### VaspSchema

| Property | Type | Description |
|----------|------|-------------|
| uuid | string | VASP unique identifier |
| name | string | Name of the VASP |

### WebsocketsTokenResponse

| Property | Type | Description |
|----------|------|-------------|
| token | string | Token. |
| valid_sec | integer | Validity of token in seconds. |
| user_id | integer | User ID. |

### WithdrawalRequestsRequest

| Property | Type | Description |
|----------|------|-------------|
| id | string | Withdrawal request id. |
| timedelta | string | Withdrawal requests from number of seconds ago to now (max. 50000000). |
| limit | string | Limit result to that many withdrawal requests (minimum: 1; maximum: 1000; default: 1000). |
| offset | string | Skip that many withdrawal requests before returning results (minimum: 0; maximum: 200000). |

### WithdrawalRequestsResponse

| Property | Type | Description |
|----------|------|-------------|
| id | integer | Withdrawal ID. |
| datetime | string | Date and time. |
| type | integer | 0 (SEPA), 2 (WIRE transfer), 17 (BCH), 1 (BTC), 16 (ETH), 15 (LTC), 18 (PAX), 19 (XLM), 14 (XRP), 20 (LINK), 21 (OMG), 22 (USDC), 24 (AAVE), 25 (BAT), 26 (UMA), 27 (DAI), 28 (KNC), 29 (MKR), 30 (ZRX), 31 (GUSD), 32 (ALGO), 33 (AUDIO), 34 (CRV), 35 (SNX), 36 (UNI), 38 (YFI), 39 (COMP), 40 (GRT), 42 (USDT), 43 (EURT), 46 (MATIC), 47 (SUSHI), 48 (CHZ), 49 (ENJ), 50 (HBAR), 51 (ALPHA), 52 (AXS), 53 (FTT), 54 (SAND), 55 (STORJ), 56 (ADA), 57 (FET), 58 (RGT), 59 (SKL), 60 (CEL), 61 (SLP), 62 (SXP), 65 (DYDX), 66 (FTM), 67 (SHIB), 69 (AMP), 71 (GALA), 72 (PERP). |
| currency | string | Currency. |
| network | string | Cryptocurrency network. |
| amount | string | Amount. |
| status | integer | 0 (open), 1 (in process), 2 (finished), 3 (canceled), 4 (failed) or 11 (reversed). |
| txid | integer | Bitstamp's transaction id. |
| address | string | Withdrawal address. |
| transaction_id | string | Transaction ID (crypto withdrawals only). |

### _AssetMarginInfo

| Property | Type | Description |
|----------|------|-------------|
| asset | string | Currency for collateral |
| total_amount | string | Total balance of collateral |
| available | string | Available balance of collateral |
| reserved | string | Reserved balance of collateral |
| margin_available | string | Margin available |

### _EstimatedOrderImpactMarginTier

| Property | Type | Description |
|----------|------|-------------|
| tier | integer | Margin tier if order is placed. |
| breakdown | array | Breakdown. |

### _EstimatedOrderImpactMarginTierBreakdown

| Property | Type | Description |
|----------|------|-------------|
| tier | integer | Tier. |
| amount | string | Amount. |
| exposure | string | Exposure. |
| leverage | string | Leverage. |

### _FundingRateTick

| Property | Type | Description |
|----------|------|-------------|
| funding_rate | string | Funding rate. |
| timestamp | string | Funding rate unix timestamp. |

### _MarginTier

| Property | Type | Description |
|----------|------|-------------|
| tier | string | Tier number. |
| size_limit_low | string | Lower bound of position size for this tier. |
| size_limit_high | string | Upper bound of position size for this tier. |
| max_leverage | string | Maximum leverage for this tier. |
| initial_margin_rate | string | Initial margin rate percentage. |
| maintenance_margin_rate | string | Maintenance margin rate percentage. |
| close_out_margin_rate | string | Close out margin rate percentage. |
| initial_margin_previous_level_max | string | Maximum initial margin required up to this tier. |
| maintenance_margin_previous_level_max | string | Maximum maintenance margin required up to this tier. |
| close_out_margin_previous_level_max | string | Maximum close out margin required up to this tier. |

## Authentication

### x_auth

Type: apiKey
In: header
Name: X-Auth

### x_auth_signature

Type: apiKey
In: header
Name: X-Auth-Signature

### x_auth_nonce

Type: apiKey
In: header
Name: X-Auth-Nonce

### x_auth_timestamp

Type: apiKey
In: header
Name: X-Auth-Timestamp

### x_auth_version

Type: apiKey
In: header
Name: X-Auth-Version

### x_content_type

Type: apiKey
In: header
Name: Content-Type

### x_auth_subaccount_id

Type: apiKey
In: header
Name: X-Auth-Subaccount-Id

