Welcome to the BingXAPI.
You can use our API to access market data endpoints of spot trading. The market data API is publicly accessible and provides market data, statistics, order book depth of a Trading Pair.
If you have any questions or feedback, you can join the API issue Telegram group.
BingX sincerely invites you to participate in the API function user survey and share your ideas so that we can better serve you and enhance your trading experience.
Fill in the questionnaire


Signature Authentication
Generate an API Key
To access private endpoints, you must create an API Key on the BingX website under User Center → API Management.
After creation, you will receive an API Key and a Secret Key. Please keep them secure.
For security reasons, it is strongly recommended to configure an IP whitelist.
Never disclose your API Key or Secret Key. If leaked, delete it immediately and create a new one.
Permission Settings
Newly created API Keys have read-only permission by default.
To place orders or perform other write operations, please enable the corresponding permissions in the UI.
Request Requirements
All authenticated REST requests must include:
X-BX-APIKEY in the request header.
signature as a request parameter, calculated using the signature algorithm.
timestamp (milliseconds) as the request time. Requests outside the allowed time window (default 5000ms) will be rejected. The window can be adjusted using recvWindow.
Signature Description
The signature is generated using HMAC-SHA256 and returned as a 64-character lowercase hexadecimal string.
The signing and request construction rules are as follows:
1. Collect all business parameters (excluding signature).
2. Generate timestamp (milliseconds) and include it as a normal parameter.
3. Sort all parameters (business parameters + timestamp) by key in ASCII ascending order.
4. Build the signing string:
key=value&key2=value2&...×tamp=xxx
Parameter values must NOT be URL-encoded here.
5. Use secretKey to calculate HMAC-SHA256 over the signing string to obtain the signature.
URL Encoding Rules (Query String Only)
These rules apply only to query string parameters:
The signature is always calculated from the unencoded signing string.
If the signing string contains '[' or '{', URL-encode only parameter values in the actual request URL.
Do not encode parameter keys.
Use UTF-8 encoding and encode spaces as %20.
If the signing string does not contain '[' or '{', values do not need URL encoding.
Query String Example
Example parameters:
symbol=BTC-USDT
recvWindow=0
timestamp=1696751141337
Sorted signing string:
recvWindow=0&symbol=BTC-USDT×tamp=1696751141337
Generate signature:
echo -n 'recvWindow=0&symbol=BTC-USDT×tamp=1696751141337' | openssl dgst -sha256 -hmac 'SECRET_KEY' -hex
Send request:
https://open-api.bingx.com/xxx?recvWindow=0&symbol=BTC-USDT×tamp=1696751141337&signature=...
Batch Order Query String Example
Example request URL:
https://open-api.bingx.com/openApi/spot/v1/trade/batchOrders?data=%5B%7B%22symbol%22%3A%22BTC-USDT%22%2C%22side%22%3A%22BUY%22%2C%22type%22%3A%22LIMIT%22%2C%22quantity%22%3A0.001%2C%22price%22%3A85000%2C%22newClientOrderId%22%3A%22%22%7D%2C%7B%22symbol%22%3A%22BTC-USDT%22%2C%22side%22%3A%22BUY%22%2C%22type%22%3A%22LIMIT%22%2C%22quantity%22%3A0.001%2C%22price%22%3A42000%2C%22newClientOrderId%22%3A%22%22%7D%5D&recvWindow=60000×tamp=1766679008165&signature=87bd22cfb380dddf8ce6d2901be7f107fef23dcf1e3d066e1519d1daa8fa81c6
Request Body Example
The following example applies to endpoints that require application/json and read parameters from the request body.
Signature parameters (timestamp / signature) must be included in the request body. Do not append them to the URL query.
Example business parameters:
{
"recvWindow": 10000,
"symbol": "ETH-USDT",
"type": "MARKET",
"side": "SELL",
"positionSide": "SHORT",
"quantity": 0.01
}
Example request body:
{
"recvWindow": 10000,
"symbol": "ETH-USDT",
"type": "MARKET",
"side": "SELL",
"positionSide": "SHORT",
"quantity": 0.01,
"timestamp": 1696751141337,
"signature": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
}
Endpoints Using Request Body
The following endpoints use application/json format and send parameters via request body:
Create Sub-account - POST /openApi/subAccount/v1/create
Create Sub-account API Key - POST /openApi/subAccount/v1/apiKey/create
Edit Sub-Account API Key - POST /openApi/subAccount/v1/apiKey/edit
Delete Sub-Account API Key - POST /openApi/subAccount/v1/apiKey/del
Update Sub-account Status (Freeze/Unfreeze) - POST /openApi/subAccount/v1/updateStatus
Query Sub-Mother Account Transferable Amount - POST /openApi/account/transfer/v1/subAccount/transferAsset/supportCoins
Sub-Mother Account Asset Transfer - POST /openApi/account/transfer/v1/subAccount/transferAsset
Success
An HTTP 200 status code indicates a successful response. The response body, if present, will be returned in JSON format.


ommon Error Codes
Common HTTP Error Codes
400 Bad Request – Invalid request format
401 Unauthorized – Invalid API Key
403 Forbidden – You do not have access to the requested resource
404 Not Found – Request not found
429 Too Many Requests – Requests are too frequent and are rate-limited by the system
418 – Received 429 and continued access, so the user is banned
500 Internal Server Error – Internal server error
504 – The server failed to get a response; further confirmation required
Common Business Error Codes
100202 - Balance is not enough to place batch orders
100400 - Invalid parameter
100404 - Order does not exist
100410 - Too many error requests in a short time, temporarily restricted
100421 - LIMIT pending orders reached the maximum limit (1000)
100441 - Account is abnormal, please contact customer service
100490 - Spot symbol is offline, please check symbol status
101202 - The value must be greater than the minimum allowed amount
101204 - Insufficient margin
101205 - No position to close
101209 - Maximum position value for this leverage has been reached
101212 - The available amount is insufficient
101222 - The current leverage poses high risks, please lower the leverage
101253 - Adjustable margin is insufficient
101400 - The minimum order amount requirement is not met
101402 - This account does not support trading of the trading pair
101484 - Advanced identity verification is required
101485 - The minimum size for closing an order is not met
104103 - Please close open positions or cancel pending orders first
109400 - Invalid parameters
109415 - Symbol is currently paused for trading
109420 - Position does not exist
109421 - Order does not exist
109425 - Symbol does not exist
109429 - Request is temporarily restricted due to risk control
109500 - User has pending orders or open positions
Timestamp Specifications
All timestamps in the API are returned in milliseconds.
The request timestamp must be within 5 seconds of the API server time, otherwise the request will be considered expired and rejected.
If there is a significant time discrepancy between the local server and the API server, it is recommended to use the API server time to update the HTTP header.
Example: 1587091154123
Numeric Specifications
To maintain precision across platforms, decimal numbers are returned as strings.
It is recommended to convert numbers into strings when making requests to avoid truncation and precision errors.
Integers (such as trade numbers and orders) are returned without quotation marks.
Rate Limiting
If requests are too frequent, the system will automatically rate-limit them and restore after 5 minutes.
Rate limiting is based on the account UID, with each API having its own independent rate limit.
Users can check the current rate-limiting status using 'X-RateLimit-Requests-Remain' (remaining requests) and 'X-RateLimit-Requests-Expire' (window expiration time) in the HTTP header.
Adjust the request frequency based on these values.
Query System Time
Request Method: GET
Endpoint: GET https://open-api.bingx.com/openApi/swap/v2/server/time
Return Parameters:
code - int64 - Error code, 0 means success, non-zero means failure
msg - string - Error message
serverTime - int64 - Current server time, in milliseconds
Sample Response:
{"code": 0, "msg": "", "data": {"serverTime": 1675319535362}}

Q: Where are BingX servers located?
BingX is hosted on AWS in the Singapore region (ap-southeast-1), utilizing multiple Availability Zones, including Availability Zone IDs: apse1-az1, apse1-az2, and apse1-az3 to ensure high availability and stability.
Q: What is UID?
UID stands for User ID, which is a unique identifier for each user (including parent users and sub-users). UID can be viewed in the personal information section of the web or app interface, and it can also be obtained through the GET /openApi/account/v1/uid interface.
Q: How many API Keys can a user apply for?
Each parent user can create up to 20 sets of API Keys. Each parent user can also create up to 20 sub-users, and each sub-user can create up to 20 sets of API Keys. Each API Key can be set with different permissions.
Q: Why do I often experience disconnections and timeouts?
It could be due to network fluctuations. We recommend reconnecting in such cases.
Q: Why does WebSocket connection always get disconnected?
You can check if your code returns a Pong after receiving a Ping. If you are subscribing to account-related websockets, please also check if you are regularly updating the listenkey. We recommend using our sample code first.
Q: Why does signature authentication always fail?
Please carefully read our signature authentication instructions, or test using our sample code first.
Q: Is the API Key for U-based contracts the same as Spot trading?
The API Key for U-based contracts is the same as the API Key for Spot trading. However, the permissions for spot trading and contract trading are separate and need to be configured accordingly.
Q: How many types of risk control restrictions does BingX have for APIs?
BingX has three types of risk control strategies for APIs: api rate limiting, trading restrictions, and network firewall restrictions. These restrictions may change at any time.
Interface rate limiting: The rate limiting for each api may vary. Please refer to the specific api documentation for details.
Trading restrictions: Trading behavior is evaluated based on the behavior of regular users. If your trading behavior deviates significantly from that of regular users, you may be prohibited from trading, and the duration of the prohibition is uncertain. The duration of the trading prohibition may increase under the following circumstances:
1. Frequently occupying the best bid and ask prices.
2. Frequently placing/canceling orders without any trades.
3. Very low trade completion rate, where the completion rate = number of trades / (number of placed orders + number of canceled orders).
4. Very low trade weight, where the trade weight = total trade amount / (total placed order amount + total canceled order amount).
5. Continuously sending frequent requests after receiving a 429 error response.
Network Firewall Restrictions: Currently, we do not provide explicit information about network firewall restrictions. If you receive an HTTP 403 error message, it means you have violated a network firewall rule. In most cases, this error occurs due to excessive requests and will result in a five-minute temporary ban. However, if your requests are considered malicious, it may lead to a longer ban or even permanent suspension.
Q: How to report API errors?
Please contact our official customer service and provide the following template to report the issue. Our technical support will assist you:
1. Problem description
2. User ID (UID) and order ID (if related to account or order), API KEY
3. Complete request parameters (if applicable)
4. Complete JSON formatted response
5. Time and frequency of the issue (when it started, if it can be reproduced)
6. Signature information
Q: Does the API support standard contract trading?
Currently not supported.
Q: Does the API support stock and forex trading?
Currently not supported.
Q: Does the mobile app support API management?
This feature is under development.
Q: How many channels can be subscribed per IP address on BingX?
Currently, there is no limit, but there is a subscription rate limit. Please do not exceed 10/s.

Connection Limitations
A websocket is limited to a maximum of 200 topics, and 80403 error codes will be returned.
An IP limit is up to 60 websockets, beyond which the link will fail.
Access
The base URL of Live Websocket Market Data: wss://open-api-swap.bingx.com/swap-market
The base URL of VST Websocket Market Data: wss://vst-open-api-ws.bingx.com/swap-market
Data Compression
All response data from the Websocket server is compressed into GZIP format. Clients have to decompress them for further use.
Heartbeats
Once the Websocket Client and Websocket Server get connected, the server will send a heartbeat-Ping message every 5 seconds (the frequency might change).
When the Websocket Client receives this heartbeat message, it should return a Pong message.
Subscriptions
After successfully establishing a connection with the Websocket server, the Websocket client sends the following request to subscribe to a specific topic:
{ "id": "id1", "reqType": "sub", "dataType": "data to sub" }
After a successful subscription, the Websocket client will receive a confirmation message:
{ "id": "id1", "code": 0, "msg": "" }
After that, once the subscribed data is updated, the Websocket client will receive the update message pushed by the server.
Unsubscribe
The format of unsubscription is as follows:
{ "id": "id1", "reqType": "unsub", "dataType": "data to unsub" }
Confirmation of Unsubscription:
{ "id": "id1", "code": 0, "msg": "" }

POST
/openApi/user/auth/userDataStream
(Generate Listen Key)
Copy
Request Type POST
UID Rate Limit 2/second / UID
Signature Verification: Yes
Applicable Accounts: Master and Sub Accounts
The listen key is valid for 1 hour.
API
CURL
curl -X POST 'https://open-api.bingx.com/openApi/user/auth/userDataStream' --header "X-BX-APIKEY:g6ikQYpMiWLecMQ39DUivd4ENem9ygzAim63xUPFhRtCFBUDNLajRoZNiubPemKT"
Response
{"listenKey":"a8ea75681542e66f1a50a1616dd06ed77dab61baa0c296bca03a9b13ee5f2dd7"}
POST /openApi/user/auth/userDataStream
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
No Data
response body
listenKey
string
Listen Key
Request Example
{}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {
    "listenKey": "73a0914be44ce06d087ec2c97d4ec685e4cf26069a20900e2f4cd6694df9b734"
  }
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/user/auth/userDataStream'
    method = "POST"
    paramsMap = {}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())

    PUT
/openApi/user/auth/userDataStream
(Extend Listen Key Validity)
Copy
Request Type PUT
UID Rate Limit 2/second / UID
Signature Verification: Yes
Applicable Accounts: Master and Sub Accounts
API Key Permission: Read
API Description:Extend Listen Key Validity
The validity is extended by 60 minutes after this call. It is recommended to send a ping every 30 minutes.
Key Steps for Using the API
CURL
curl -i -X PUT 'https://open-api.bingx.com/openApi/user/auth/userDataStream?listenKey=d84d39fe78762b39e202ba204bf3f7ebed43bbe7a481299779cb53479ea9677d'
Response
http status 200 Success
http status 204 No request parameters
http status 404 This listenKey does not exist
API Parameters
https://open-api.bingx.com
PUT /openApi/user/auth/userDataStream
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
listenKey
string
Listen Key
response body
No Data
Request Example
{
  "listenKey": "73a0914be44ce06d087ec2c97d4ec685e4cf26069a20900e2f4cd6694df9b734"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {}
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/user/auth/userDataStream'
    method = "PUT"
    paramsMap = {
    "listenKey": "73a0914be44ce06d087ec2c97d4ec685e4cf26069a20900e2f4cd6694df9b734"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())

    DELETE
/openApi/user/auth/userDataStream
(Close Listen Key)
Copy
Request Type DELETE
UID Rate Limit 2/second / UID
Signature Verification: Yes
Applicable Accounts: Master and Sub Accounts
API Key Permission: Read
API Description:Close Listen Key
Key Steps for Using the API
CURL
curl -i -X DELETE 'https://open-api.bingx.com/openApi/user/auth/userDataStream?listenKey=d84d39fe78762b39e202ba204bf3f7ebed43bbe7a481299779cb53479ea9677d'
Response
http status 200 Success
http status 204 No request parameters
http status 404 This listenKey does not exist
API Parameters
https://open-api.bingx.com
DELETE /openApi/user/auth/userDataStream
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
listenKey
string
Listen Key
response body
No Data
Request Example
{
  "listenKey": "73a0914be44ce06d087ec2c97d4ec685e4cf26069a20900e2f4cd6694df9b734"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {}
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/user/auth/userDataStream'
    method = "DELETE"
    paramsMap = {
    "listenKey": "73a0914be44ce06d087ec2c97d4ec685e4cf26069a20900e2f4cd6694df9b734"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())


    GET
/openApi/swap/v2/quote/contracts
(USDT-M Perp Futures symbols)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
trading pair, for example: BTC-USDT
timestamp
int64
No
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
contractId
string
contract ID
symbol
string
trading pair, for example: BTC-USDT
quantityPrecision
int64
transaction quantity precision
pricePrecision
int64
price precision
makerFeeRate
float64
take transaction fee
takerFeeRate
float64
make transaction fee
tradeMinQuantity
float64
The minimum trading unit(COIN)
tradeMinUSDT
float64
The minimum trading unit(USDT)
currency
string
settlement and margin currency asset
asset
string
contract trading asset
status
int64
1 online, 25 forbidden to open positions, 5 pre-online, 0 offline
apiStateOpen
string
Whether the API can open a position
apiStateClose
string
Whether API can close positions
ensureTrigger
bool
Whether to support guaranteed stop loss.
triggerFeeRate
string
The fee rate for guaranteed stop loss.
brokerState
bool
Whether to prohibit broker user transactions, true: prohibited
launchTime
long
shelf time; The status of the pair is pre-online before the listing time, and the status of the pair changes to online after the listing time
maintainTime
long
The start time of the prohibition of opening a position, after the time is up, the currency pair is in a state of prohibition from opening a position, and can only close the position
offTime
long
Down line time, after the time is up, the currency pair is in the offline state and trading is prohibited
displayName
string
The trading pair name displayed on the platform is for display purposes only. Unlike the symbol, which is primarily used for order placement.
Request Example
{}
Response Example
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "contractId": "100",
      "symbol": "BTC-USDT",
      "size": "0",
      "quantityPrecision": 4,
      "pricePrecision": 1,
      "feeRate": 0.0005,
      "makerFeeRate": 0.0002,
      "takerFeeRate": 0.0005,
      "tradeMinLimit": 0,
      "tradeMinQuantity": 0.0001,
      "tradeMinUSDT": 2,
      "maxLongLeverage": 125,
      "maxShortLeverage": 125,
      "currency": "USDT",
      "asset": "BTC",
      "status": 1,
      "apiStateOpen": "true",
      "apiStateClose": "true",
      "brokerState": "true",
      "launchTime": 1586275200000,
      "maintainTime": 0,
      "offTime": 0
    },
    {
      "contractId": "101",
      "symbol": "ETH-USDT",
      "size": "0",
      "quantityPrecision": 2,
      "pricePrecision": 2,
      "feeRate": 0.0005,
      "makerFeeRate": 0.0002,
      "takerFeeRate": 0.0005,
      "tradeMinLimit": 0,
      "tradeMinQuantity": 0.01,
      "tradeMinUSDT": 2,
      "maxLongLeverage": 125,
      "maxShortLeverage": 125,
      "currency": "USDT",
      "asset": "ETH",
      "status": 1,
      "apiStateOpen": "true",
      "apiStateClose": "true",
      "brokerState": "true",
      "launchTime": 1586275200000,
      "maintainTime": 0,
      "offTime": 0
    }
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v2/quote/contracts'
    method = "GET"
    paramsMap = {}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())





    GET
/openApi/swap/v2/quote/depth
(Order Book)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, for example: BTC-USDT, please use capital letters
limit
int64
No
Default 20, optional value:[5, 10, 20, 50, 100, 500, 1000]
timestamp
int64
No
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
T
int64
System time, unit: millisecond
asks
array
depth of asks. first element price, second element quantity
bids
array
Buyer depth. first element price, second element quantity
asksCoin
array
depth of asks. first element price, second element quantity(coin)
bidsCoin
array
Buyer depth. first element price, second element quantity(coin)
Request Example
{
  "symbol": "SHIB-USDT",
  "limit": "5"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {
    "T": 1702719083983,
    "bids": [
      [
        "0.000009854",
        "483909"
      ],
      [
        "0.000009853",
        "824851"
      ],
      [
        "0.000009852",
        "539085"
      ],
      [
        "0.000009851",
        "697410"
      ],
      [
        "0.000009850",
        "488828"
      ]
    ],
    "asks": [
      [
        "0.000009860",
        "578208"
      ],
      [
        "0.000009859",
        "279010"
      ],
      [
        "0.000009858",
        "501588"
      ],
      [
        "0.000009857",
        "976049"
      ],
      [
        "0.000009856",
        "687669"
      ]
    ],
    "bidsCoin": [
      [
        "0.000009854",
        "483909000"
      ],
      [
        "0.000009853",
        "824851000"
      ],
      [
        "0.000009852",
        "539085000"
      ],
      [
        "0.000009851",
        "697410000"
      ],
      [
        "0.000009850",
        "488828000"
      ]
    ],
    "asksCoin": [
      [
        "0.000009860",
        "578208000"
      ],
      [
        "0.000009859",
        "279010000"
      ],
      [
        "0.000009858",
        "501588000"
      ],
      [
        "0.000009857",
        "976049000"
      ],
      [
        "0.000009856",
        "687669000"
      ]
    ]
  }
}
error code
109425
Trading pair does not exist
109400
Invalid parameters
109415
Trading pair is suspended
109500
Depth data not available
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v2/quote/depth'
    method = "GET"
    paramsMap = {
    "symbol": "SHIB-USDT",
    "limit": "5"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())


    GET
/openApi/swap/v2/quote/trades
(Recent Trades List)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT
limit
int64
No
default: 500, maximum 1000
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
time
int64
transaction time
isBuyerMaker
bool
Whether the buyer is the maker of the order (true / false)
price
string
transaction price
qty
string
transaction quantity
quoteQty
string
turnover
Request Example
{
  "symbol": "BTC-USDT",
  "limit": 10
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "time": 1702719269849,
      "isBuyerMaker": true,
      "price": "42214.0",
      "qty": "0.0248",
      "quoteQty": "1046.91"
    },
    {
      "time": 1702719269559,
      "isBuyerMaker": false,
      "price": "42214.1",
      "qty": "0.4985",
      "quoteQty": "21043.73"
    },
    {
      "time": 1702719269274,
      "isBuyerMaker": true,
      "price": "42213.9",
      "qty": "0.0394",
      "quoteQty": "1663.23"
    },
    {
      "time": 1702719268954,
      "isBuyerMaker": false,
      "price": "42214.4",
      "qty": "0.1116",
      "quoteQty": "4711.13"
    },
    {
      "time": 1702719268253,
      "isBuyerMaker": true,
      "price": "42214.5",
      "qty": "0.4476",
      "quoteQty": "18895.21"
    },
    {
      "time": 1702719267963,
      "isBuyerMaker": false,
      "price": "42215.2",
      "qty": "0.0708",
      "quoteQty": "2988.84"
    },
    {
      "time": 1702719267148,
      "isBuyerMaker": false,
      "price": "42215.8",
      "qty": "0.6055",
      "quoteQty": "25561.67"
    },
    {
      "time": 1702719265743,
      "isBuyerMaker": false,
      "price": "42216.1",
      "qty": "0.2031",
      "quoteQty": "8574.09"
    },
    {
      "time": 1702719265463,
      "isBuyerMaker": false,
      "price": "42216.1",
      "qty": "0.0160",
      "quoteQty": "675.46"
    },
    {
      "time": 1702719265198,
      "isBuyerMaker": true,
      "price": "42217.2",
      "qty": "0.0112",
      "quoteQty": "472.83"
    }
  ]
}
error code
109425
Trading pair does not exist
109400
Invalid parameters
109415
Trading pair is suspended
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v2/quote/trades'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT",
    "limit": 10
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())


    GET
/openApi/swap/v2/quote/premiumIndex
(Mark Price and Funding Rate)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
symbol
string
trading pair, for example: BTC-USDT
lastFundingRate
string
Last updated funding rate
markPrice
string
current mark price
indexPrice
string
index price
nextFundingTime
int64
The remaining time for the next settlement, in milliseconds
Request Example
{
  "symbol": "BTC-USDT"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {
    "symbol": "BTC-USDT",
    "markPrice": "42216.4",
    "indexPrice": "42219.9",
    "lastFundingRate": "0.00025100",
    "nextFundingTime": 1702742400000
  }
}
error code
109425
Trading pair does not exist
100410
rate limited
109415
Trading pair is suspended
109400
Invalid parameters
109429
Too many invalid requests
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v2/quote/premiumIndex'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())


    GET
/openApi/swap/v2/quote/fundingRate
(Get Funding Rate History)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT
startTime
int64
No
Start time, unit: millisecond
endTime
int64
No
End time, unit: millisecond
limit
int32
No
default: 100 maximum: 1000
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
symbol
string
trading pair, for example: BTC-USDT
fundingRate
string
funding rate
fundingTime
int64
Funding time: milliseconds
Request Example
{
  "symbol": "QNT-USDT",
  "limit": 2
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "symbol": "QNT-USDT",
      "fundingRate": "0.00027100",
      "fundingTime": 1702713600000
    },
    {
      "symbol": "QNT-USDT",
      "fundingRate": "0.00012800",
      "fundingTime": 1702684800000
    }
  ]
}
error code
109425
Trading pair does not exist
100410
rate limited
109400
Invalid parameters
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v2/quote/fundingRate'
    method = "GET"
    paramsMap = {
    "symbol": "QNT-USDT",
    "limit": 2
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())


    GET
/openApi/swap/v3/quote/klines
(Kline/Candlestick Data)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT
interval
string
Yes
time interval, refer to field description
startTime
int64
No
Start time, unit: millisecond
endTime
int64
No
End time, unit: millisecond
timeZone
int32
No
Time zone offset, only supports 0 or 8 (UTC+0 or UTC+8)
limit
int64
No
default: 500 maximum: 1440
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
open
float64
Opening Price
close
float64
Closing Price
high
float64
High Price
low
float64
Low Price
volume
float64
transaction volume
time
int64
k-line time stamp, unit milliseconds
Request Example
{
  "symbol": "KNC-USDT",
  "interval": "1h",
  "timeZone": 8,
  "limit": "1000",
  "startTime": "1702717199998"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "open": "0.7034",
      "close": "0.7065",
      "high": "0.7081",
      "low": "0.7033",
      "volume": "635494.00",
      "time": 1702717200000
    }
  ]
}
error code
109425
Trading pair does not exist
100410
rate limited
109415
Trading pair is suspended
109400
Invalid parameters
109429
Too many invalid requests
109419
Trading pair not supported
109701
Network issue
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v3/quote/klines'
    method = "GET"
    paramsMap = {
    "symbol": "KNC-USDT",
    "interval": "1h",
    "timeZone": 8,
    "limit": "1000",
    "startTime": "1702717199998"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())


    GET
/openApi/swap/v2/quote/openInterest
(Open Interest Statistics)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
openInterest
string
Position Amount
symbol
string
contract name
time
int64
matching engine time
Request Example
{
  "symbol": "EOS-USDT"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {
    "openInterest": "7409966.52",
    "symbol": "EOS-USDT",
    "time": 1702719692859
  }
}
error code
109425
Trading pair does not exist
109400
OpenInterestNotExist
109415
Trading pair is suspended
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v2/quote/openInterest'
    method = "GET"
    paramsMap = {
    "symbol": "EOS-USDT"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())


    GET
/openApi/swap/v2/quote/ticker
(24hr Ticker Price Change Statistics)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
symbol
string
trading pair, for example: BTC-USDT
priceChange
string
24 hour price change
priceChangePercent
string
price change percentage
lastPrice
string
latest transaction price
lastQty
string
latest transaction amount
highPrice
string
24-hour highest price
lowPrice
string
24 hours lowest price
volume
string
24-hour volume
quoteVolume
string
24-hour turnover, the unit is USDT
openPrice
string
first price within 24 hours
openTime
int64
The time when the first transaction occurred within 24 hours
closeTime
int64
The time when the last transaction occurred within 24 hours
bidPrice
float64
bid price
bidQty
float64
bid quantity
askPrice
float64
ask price
askQty
float64
ask quantity
Request Example
{
  "symbol": "SFP-USDT"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {
    "symbol": "SFP-USDT",
    "priceChange": "0.0295",
    "priceChangePercent": "4.15",
    "lastPrice": "0.7409",
    "lastQty": "10",
    "highPrice": "0.7506",
    "lowPrice": "0.6903",
    "volume": "4308212",
    "quoteVolume": "3085449.53",
    "openPrice": "0.7114",
    "openTime": 1702719833853,
    "closeTime": 1702719798603,
    "askPrice": "0.7414",
    "askQty": "99",
    "bidPrice": "0.7413",
    "bidQty": "84"
  }
}
error code
109425
Trading pair does not exist
100410
rate limited
109400
Invalid parameters
109415
Trading pair is suspended
109429
Too many invalid requests
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v2/quote/ticker'
    method = "GET"
    paramsMap = {
    "symbol": "SFP-USDT"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())



109400
timestamp is invalid
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v1/market/historicalTrades'
    method = "GET"
    paramsMap = {
    "fromId": "412551",
    "limit": "500",
    "symbol": "ETH-USDT",
    "recvWindow": "60000"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())

    GET
/openApi/swap/v2/quote/bookTicker
(Symbol Order Book Ticker)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Professional Futures Trading
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
symbol
string
There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT
bid_price
float64
Optimal purchase price
bid_qty
float64
Order quantity
ask_price
float64
Best selling price
lastUpdateId
int64
The ID of the latest trade
time
long
The time of the trade in milliseconds
ask_qty
float64
Order quantity
Request Example
{
  "symbol": "BTC-USDT"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {
    "book_ticker": {
      "symbol": "BTC-USDT",
      "bid_price": 42211.1,
      "bid_qty": 12663,
      "ask_price": 42211.8,
      "ask_qty": 128854
    }
  }
}
error code
109425
Trading pair does not exist
109400
Invalid parameters
109415
Trading pair is suspended
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v2/quote/bookTicker'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())

    GET
/openApi/swap/v1/market/markPriceKlines
(Mark Price Kline/Candlestick Data)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT
interval
string
Yes
time interval, refer to field description
startTime
int64
No
Start time, unit: millisecond
endTime
int64
No
End time, unit: millisecond
limit
int64
No
default: 500 maximum: 1440
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
open
float64
Opening Price
close
float64
Closing Price
high
float64
High Price
low
float64
Low Price
openTime
int64
transaction volume
closeTime
int64
k-line time stamp, unit milliseconds
Request Example
{
  "symbol": "KNC-USDT",
  "interval": "1h",
  "limit": "1000",
  "startTime": "1702717199998"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "open": "0.7034",
      "close": "0.7065",
      "high": "0.7081",
      "low": "0.7033",
      "volume": "635494.00",
      "openTime": 1705820520000,
      "closeTime": 1705820520000
    }
  ]
}
error code
109425
Trading pair does not exist
109415
Trading pair is suspended
109701
Network issue
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v1/market/markPriceKlines'
    method = "GET"
    paramsMap = {
    "symbol": "KNC-USDT",
    "interval": "1h",
    "limit": "1000",
    "startTime": "1702717199998"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())

    GET
/openApi/swap/v1/ticker/price
(Symbol Price Ticker)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
There must be a hyphen/ "-" in the trading pair symbol. eg: BTC-USDT,If no transaction pair parameters are sent, all transaction pair information will be returned
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
symbol
string
trading pair, for example: BTC-USDT
price
string
price
time
int64
matching engine time
Request Example
{
  "symbol": "TIA-USDT"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {
    "symbol": "TIA-USDT",
    "price": "14.0658",
    "time": 1702718922941
  }
}
error code
109425
Trading pair does not exist
109400
Invalid parameters
109415
Trading pair is suspended
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v1/ticker/price'
    method = "GET"
    paramsMap = {
    "symbol": "TIA-USDT"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())

    GET
/openApi/swap/v1/tradingRules
(Trading Rules)
Copy
Request Type GET
UID Rate Limit 5/second / UID
Signature Verification: No
API Key Permission: Read
endpoint description：This endpoint retrieves the trading rules for a specified contract trading pair, including minimum order size, minimum order value, limit order price limits, market order price protection range, maximum number of open orders, and spread protection thresholds.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, e.g. BTC-USDT. Please use uppercase letters. If not provided, information for all trading pairs will be returned.
timestamp
int64
Yes
Current timestamp in milliseconds. Required for request signature validation; must match the current system time.
recvWindow
int64
No
Request validity window value in milliseconds.
response body
minSizeCoin
string
Minimum order quantity, denominated in coin.
minSizeUsd
string
Minimum order amount, denominated in USDT.
maxMumOrder
string
Maximum number of open orders for this contract, including: limit orders, market orders, stop orders, trailing orders, take-profit orders, stop-loss orders, and OCO orders.
protectionThreshold
string
Spread protection threshold (decimal). If spread protection is enabled and when a strategy order is triggered, if the spread between the latest price and mark price exceeds this threshold, the order will fail.
buyMaxPrice
string
Upper limit ratio for limit order buy price (decimal). Limit order price must satisfy: current price × lower limit < order price < current price × upper limit.
buyMinPrice
string
Lower limit ratio for limit order buy price (decimal). Limit order price must satisfy: current price × lower limit < order price < current price × upper limit.
sellMaxPrice
string
Upper limit ratio for limit order sell price (decimal). Limit order price must satisfy: current price × lower limit < order price < current price × upper limit.
sellMinPrice
string
Lower limit ratio for limit order sell price (decimal). Limit order price must satisfy: current price × lower limit < order price < current price × upper limit.
marketRatio
string
Price tolerance ratio for market orders (decimal). If the spread between the market order execution price and mark price exceeds this ratio, the order may fail or be partially filled.
Request Example
{
  "symbol": "BTC-USDT"
}
Response Example
{
  "code": 0,
  "msg": "",
  "timestamp": 1756711590730,
  "data": {
    "minSizeCoin": "0.0001",
    "minSizeUsd": "2.00",
    "maxNumOrder": "200",
    "protectionThreshold": "0.05",
    "buyMaxPrice": "1.1",
    "buyMinPrice": "0.2",
    "sellMaxPrice": "5",
    "sellMinPrice": "0.9",
    "marketRatio": "0.08"
  }
}
error code
109400
Contract does not exist
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/swap/v1/tradingRules'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())


















































    WSS
Partial Order Book Depth
Push limited order book depth information.
Subscription Type: The dataType is <symbol>@depth<level>@<interval>, for example, BTC-USDT@depth20@200ms, SOL-USDT@depth100@500ms.
The push interval for BTC-USDT and ETH-USDT is 200ms, and for other contracts it is 500ms.
subscription address
PROD
wss://open-api-swap.bingx.com/swap-market
VST
wss://vst-open-api-ws.bingx.com/swap-market
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@depth5@500ms
data update
code
int64
Error code. 0 indicates success, 1 indicates an error.
dataType
string
Subscribed data type, for example: BTC-USDT@trade.
data
string
Pushed data content.
T
string
Trade timestamp.
s
string
Trading pair.
m
string
Whether the buyer is the market maker. If true, the trade was initiated by a sell order; otherwise, it was initiated by a buy order.
q
string
Trade volume.
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@depth5@500ms"
}
subscribe success sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "code": 0,
  "msg": "",
  "dataType": "",
  "data": null
}
data update sample
{
  "code": 0,  // Error code. 0 indicates success, 1 indicates an error.
  "dataType": "BTC-USDT@depth5@500ms",  // Subscribed data type, for example: BTC-USDT@trade.
  "ts": 1759996742928,
  "data": {
      "bids": [
            [
              "121825.7",
              "7.7622"
            ],
            [
              "121825.6",
              "0.0060"
            ],
            [
              "121825.4",
              "0.1234"
            ],
            [
              "121825.2",
              "0.0021"
            ],
            [
              "121825.0",
              "0.0023"
            ]
          ],
      "asks": [
            [
              "121827.3",
              "0.0025"
            ],
            [
              "121827.1",
              "0.0010"
            ],
            [
              "121826.5",
              "0.0028"
            ],
            [
              "121826.1",
              "0.0143"
            ],
            [
              "121825.9",
              "9.2345"
            ]
          ]
    }  // Pushed data content.
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@depth5@500ms"
}
error code
403
Internal service call exception
1006
Internal service call exception.Generally network related issue
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-swap.bingx.com/swap-market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@depth5@500ms"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if utf8_data == "Ping": # this is very important , if you receive 'Ping' you need to send 'Pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
                  




   WSS
Subscribe the Latest Trade Detail
Real time push.
Subscribe to the trade detail data of a trading pair.
Subscription Type: The dataType is <symbol>@trade, e.g. BTC-USDT@trade, ETH-USDT@trade.
subscription address
PROD
wss://open-api-swap.bingx.com/swap-market
VST
wss://vst-open-api-ws.bingx.com/swap-market
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@trade
data update
code
int64
Error code, 0 for normal, 1 for error
dataType
string
Subscribed data type, e.g., BTC-USDT@trade
data
string
Push content
T
string
Trade time
s
string
Trading pair
m
string
Whether the buyer is a market maker. If true, this trade is a passive sell order; otherwise, it is a passive buy order.
p
string
price
q
string
Volume quantity
subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "sub",
  "dataType": "BTC-USDT@trade"
}
subscribe success sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "code": 0,
  "msg": "",
  "dataType": "",
  "data": null
}
data update sample
{
  "code": 0,  // Error code, 0 for normal, 1 for error
  "dataType": "BTC-USDT@trade",  // Subscribed data type, e.g., BTC-USDT@trade
  "data": [
      {
        "q": "0.0162",  // Volume quantity
        "p": "121934.9",  // price
        "T": 1759994162450,  // Trade time
        "m": false,  // Whether the buyer is a market maker. If true, this trade is a passive sell order; otherwise, it is a passive buy order.
        "s": "BTC-USDT"  // Trading pair
      },
      {
        "q": "0.0551",  // Volume quantity
        "p": "121926.9",  // price
        "T": 1759994162450,  // Trade time
        "m": true,  // Whether the buyer is a market maker. If true, this trade is a passive sell order; otherwise, it is a passive buy order.
        "s": "BTC-USDT"  // Trading pair
      }
    ]  // Push content
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@trade"
}
error code
403
Internal service call exception
1006
Internal service call exception.Generally network related issue
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-swap.bingx.com/swap-market" 
CHANNEL= {"id":"24dd0e35-56a4-4f7a-af8a-394c7060909c","reqType":"sub","dataType":"BTC-USDT@trade"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if utf8_data == "Ping": # this is very important , if you receive 'Ping' you need to send 'Pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()

WSS
Subscribe K-Line Data
Subscribe to market k-line data of one trading pair
Subscription Type: The dataType is <symbol>@kline_<interval>, e.g. BTC-USDT@kline_1m.
Subscription Example: {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType": "sub","dataType":"BTC-USDT@kline_1m"}
subscription address
PROD
wss://open-api-swap.bingx.com/swap-market
VST
wss://vst-open-api-ws.bingx.com/swap-market
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@kline_1m
data update
code
int64
Error code. 0 indicates success, 1 indicates an error.
dataType
string
Subscribed data type, for example: BTC-USDT@trade.
data
string
Pushed data content.
c
string
Close price.
h
string
High price.
l
string
Low price.
o
string
Open price.
v
string
Trading volume.
s
string
Trading pair.
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@depth5@500ms"
}
subscribe success sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "code": 0,
  "msg": "",
  "dataType": "",
  "data": null
}
data update sample
{
  "code": 0,  // Error code. 0 indicates success, 1 indicates an error.
  "dataType": "BTC-USDT@kline_1m",  // Subscribed data type, for example: BTC-USDT@trade.
  "s": "BTC-USDT",  // Trading pair.
  "data": [
      {
        "c": "121697.7",  // Close price.
        "o": "121684.1",  // Open price.
        "h": "121697.7",  // High price.
        "l": "121638.7",  // Low price.
        "v": "5.8244",  // Trading volume.
        "T": 1759997460000
      }
    ]  // Pushed data content.
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@depth5@500ms"
}
error code
403
Internal service call exception
1006
Internal service call exception.Generally network related issue
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-swap.bingx.com/swap-market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@depth5@500ms"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if utf8_data == "Ping": # this is very important , if you receive 'Ping' you need to send 'Pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
                  

 WSS
Subscribe to 24-hour price changes
Push every 1 second.
Push 24-hour price changes.
Subscription Type: The dataType is <symbol>@ticker, such as BTC-USDT@ticker.
subscription address
PROD
wss://open-api-swap.bingx.com/swap-market
VST
wss://vst-open-api-ws.bingx.com/swap-market
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@ticker
data update
code
int64
Error code, 0 for normal, 1 for error
dataType
string
Subscribed data type, for example BTC-USDT@ticker
data
string
Push content
e
string
Event type
E
int64
Event time
s
string
Trading pair, for example: BTC-USDT
p
string
24-hour price change
P
string
Price change percentage
o
string
First price within 24 hours
h
string
24-hour high price
l
string
24-hour low price
L
string
Latest transaction amount
c
string
Latest transaction price
v
string
24-hour volume
q
string
24-hour turnover, unit is USDT
O
int64
First transaction time within 24 hours
C
int64
Last transaction time within 24 hours
B
string
Best bid price
b
string
Best bid quantity
A
string
Best ask price
a
string
Best ask quantity
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@ticker"
}
subscribe success sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "code": 0,
  "msg": "",
  "dataType": "",
  "data": null
}
data update sample
{
  "code": 0,  // Error code, 0 for normal, 1 for error
  "dataType": "BTC-USDT@ticker",  // Subscribed data type, for example BTC-USDT@ticker
  "data": {
      "e": "24hTicker",  // Event type
      "E": 1759998119388,  // Event time
      "s": "BTC-USDT",  // Trading pair, for example: BTC-USDT
      "p": "-262.0",  // 24-hour price change
      "P": "-0.21",  // Price change percentage
      "c": "121621.7",  // Latest transaction price
      "L": "0.0010",  // Latest transaction amount
      "h": "124152.9",  // 24-hour high price
      "l": "121412.0",  // 24-hour low price
      "v": "17030.6463",  // 24-hour volume
      "q": "210028.10",  // 24-hour turnover, unit is USDT
      "o": "121883.7",  // First price within 24 hours
      "O": 1759998027573,  // First transaction time within 24 hours
      "C": 1759998119403,  // Last transaction time within 24 hours
      "A": "121621.7",  // Best ask price
      "a": "11.3115",  // Best ask quantity
      "B": "121621.5",  // Best bid price
      "b": "6.4426"  // Best bid quantity
    }  // Push content
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@ticker"
}
error code
403
Internal service call exception
1006
Internal service call exception.Generally network related issue
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-swap.bingx.com/swap-market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@ticker"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if utf8_data == "Ping": # this is very important , if you receive 'Ping' you need to send 'Pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()

WSS
Subscribe to latest price changes
Real time push.
Push latest price changes.
Subscription Type: dataType is <symbol>@lastPrice, such as BTC-USDT@lastPrice.
subscription address
PROD
wss://open-api-swap.bingx.com/swap-market
VST
wss://vst-open-api-ws.bingx.com/swap-market
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@lastPrice
data update
code
int64
Error code, 0 for normal, 1 for error
dataType
string
Subscribed data type, for example BTC-USDT@ticker
data
string
Push content
e
string
Event type
E
int64
Event time
s
string
Trading pair, for example: BTC-USDT
c
string
Last Price
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@lastPrice"
}
subscribe success sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "code": 0,
  "msg": "",
  "dataType": "",
  "data": null
}
data update sample
{
  "code": 0,  // Error code, 0 for normal, 1 for error
  "dataType": "BTC-USDT@lastPrice",  // Subscribed data type, for example BTC-USDT@ticker
  "data": {
      "e": "lastPriceUpdate",  // Event type
      "E": 1760001029063,  // Event time
      "s": "BTC-USDT",  // Trading pair, for example: BTC-USDT
      "c": "121485.9"  // Last Price
    }  // Push content
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@lastPrice"
}
error code
403
Internal service call exception
1006
Internal service call exception.Generally network related issue
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-swap.bingx.com/swap-market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@lastPrice"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if utf8_data == "Ping": # this is very important , if you receive 'Ping' you need to send 'Pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
                  

   WSS
Subscribe to latest mark price changes
Real time push.
Push latest mark price changes.
Subscription Type: dataType is <symbol>@markPrice, such as BTC-USDT@markPrice.
subscription address
PROD
wss://open-api-swap.bingx.com/swap-market
VST
wss://vst-open-api-ws.bingx.com/swap-market
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@markPrice
data update
code
int64
Error code, 0 for normal, 1 for error
dataType
string
Subscribed data type, for example BTC-USDT@ticker
data
string
Push content
e
string
Event type
E
int64
Event time
s
string
Trading pair, for example: BTC-USDT
p
string
Last Price
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@markPrice"
}
subscribe success sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "code": 0,
  "msg": "",
  "dataType": "",
  "data": null
}
data update sample
{
  "code": 0,  // Error code, 0 for normal, 1 for error
  "dataType": "BTC-USDT@markPrice",  // Subscribed data type, for example BTC-USDT@ticker
  "data": {
      "e": "markPriceUpdate",  // Event type
      "E": 1760001628357,  // Event time
      "s": "BTC-USDT",  // Trading pair, for example: BTC-USDT
      "p": "121570.0"  // Last Price
    }  // Push content
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@markPrice"
}
error code
403
Internal service call exception
1006
Internal service call exception.Generally network related issue
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-swap.bingx.com/swap-market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@markPrice"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if utf8_data == "Ping": # this is very important , if you receive 'Ping' you need to send 'Pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()



WSS
Subscribe to the Book Ticker Streams
Push every 200 ms.
Push the Book Ticker Streams.
Subscription Type: dataType is <symbol>@bookTicker, such as BTC-USDT@bookTicker.
subscription address
PROD
wss://open-api-swap.bingx.com/swap-market
VST
wss://vst-open-api-ws.bingx.com/swap-market
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@bookTicker
data update
code
int64
Error code, 0 for normal, 1 for error
dataType
string
Subscribed data type, for example BTC-USDT@bookTicker
data
string
Push content
e
string
Event type
u
int64
Update ID
E
int64
Event push time
T
int64
Match time
s
string
Trading pair, for example: BTC-USDT
b
string
Best bid price for buy orders
B
string
Best bid quantity for buy orders
a
string
Best ask price for sell orders
A
string
Best ask price for sell orders
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@bookTicker"
}
subscribe success sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "code": 0,
  "msg": "",
  "dataType": "",
  "data": null
}
data update sample
{
  "code": 0,  // Error code, 0 for normal, 1 for error
  "dataType": "BTC-USDT@bookTicker",  // Subscribed data type, for example BTC-USDT@bookTicker
  "data": {
      "e": "bookTicker",  // Event type
      "u": 578534658,  // Update ID
      "E": 1760001840686,  // Event push time
      "T": 1760001840687,  // Match time
      "s": "BTC-USDT",  // Trading pair, for example: BTC-USDT
      "b": "121584.1",  // Best bid price for buy orders
      "B": "18.7084",  // Best bid quantity for buy orders
      "a": "121584.3",  // Best ask price for sell orders
      "A": "4.9602"  // Best ask price for sell orders
    }  // Push content
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@bookTicker"
}
error code
403
Internal service call exception
1006
Internal service call exception.Generally network related issue
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-swap.bingx.com/swap-market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@bookTicker"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if utf8_data == "Ping": # this is very important , if you receive 'Ping' you need to send 'Pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
                  
WSS
Incremental Depth Information
Push frequency explanation: BTC-USDT and ETH-USDT push frequency is 200ms, while other pairs are 800ms.
How to maintain an incremental depth on the client-side: After a successful subscription, a full depth with action = 'all' is returned, along with a 'lastUpdateId' for handling subsequent incremental updates.
After receiving the full depth, the WebSocket should cache this depth in memory.
Subsequent depth changes will return incremental depth with action = 'update'. The lastUpdateId for the Nth incremental depth will be N-1 lastUpdateId + 1.
In rare cases, if the lastUpdateId is not continuous, you can reconnect or get the latest 3 incremental snapshots and attempt to read continuous lastUpdateIds from the snapshot.
Iterate through the incremental depth and compare it with the current depth. Consider thread-safety and coding practices. After comparison, update the depth snapshot and update the lastUpdateId.
Subscription type: dataType should be <symbol>@incrDepth, e.g., BTC-USDT@incrDepth
Subscription example: {"id":"975f7385-7f28-4ef1-93af-df01cb9ebb53","reqType": "sub","dataType":"BTC-USDT@incrDepth"}
subscription address
PROD
wss://open-api-swap.bingx.com/swap-market
VST
wss://vst-open-api-ws.bingx.com/swap-market
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@incrDepth
data update
code
int64
Error code, 0 for normal, non-zero for error
dataType
string
Subscribed data type, for example BTC-USDT@incrDepth
data
object
Push content, containing detailed depth update information
action
string
Depth update type: all for full snapshot, update for incremental
lastUpdateId
int64
Change ID, a continuously increasing long integer describing the continuity between incremental depth updates
time
int64
Depth update time in milliseconds
bids
array
Changed bid depth entries, each element is [price, quantity]
asks
array
Changed ask depth entries, each element is [price, quantity]
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@incrDepth"
}
subscribe success sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "code": 0,
  "msg": "",
  "dataType": "",
  "data": null
}
data update sample
{
  "code": 0,  // Error code, 0 for normal, non-zero for error
  "dataType": "BTC-USDT@incrDepth",  // Subscribed data type, for example BTC-USDT@incrDepth
  "data": {
      "action": "update",  // Depth update type: all for full snapshot, update for incremental
      "lastUpdateId": 393592635,  // Change ID, a continuously increasing long integer describing the continuity between incremental depth updates
      "time": 1760002514979,  // Depth update time in milliseconds
      "bids": [
            [
              "121706.6",
              "16.8741"
            ],
            [
              "121706.5",
              "1.1466"
            ],
            [
              "121706.4",
              "0.0079"
            ],
            [
              "121706.2",
              "0.1190"
            ],
            [
              "121706.0",
              "0.0405"
            ],
            [
              "121705.6",
              "0.0022"
            ],
            [
              "121705.3",
              "0.0447"
            ],
            [
              "121705.2",
              "0.1520"
            ],
            [
              "121704.0",
              "0.0071"
            ],
            [
              "121703.8",
              "0.3957"
            ],
            [
              "121698.4",
              "1.2145"
            ],
            [
              "121697.2",
              "1.5386"
            ],
            [
              "121678.9",
              "2.1586"
            ],
            [
              "121678.5",
              "0.0000"
            ],
            [
              "121668.0",
              "3.4117"
            ],
            [
              "121667.9",
              "0.0000"
            ]
          ],  // Changed bid depth entries, each element is [price, quantity]
      "asks": [
            [
              "122539.8",
              "0.0002"
            ],
            [
              "122006.8",
              "0.0000"
            ],
            [
              "122005.9",
              "37.5215"
            ],
            [
              "121938.5",
              "0.0000"
            ],
            [
              "121937.7",
              "41.5480"
            ],
            [
              "121928.0",
              "30.5472"
            ],
            [
              "121814.5",
              "0.0001"
            ],
            [
              "121808.7",
              "23.5113"
            ],
            [
              "121740.1",
              "0.0000"
            ],
            [
              "121739.3",
              "1.9374"
            ],
            [
              "121737.7",
              "0.0000"
            ],
            [
              "121736.9",
              "1.6937"
            ],
            [
              "121732.9",
              "0.0001"
            ],
            [
              "121732.0",
              "5.6568"
            ],
            [
              "121731.0",
              "0.0000"
            ],
            [
              "121730.8",
              "2.6757"
            ],
            [
              "121728.6",
              "0.0000"
            ],
            [
              "121728.4",
              "2.7471"
            ],
            [
              "121717.6",
              "0.0000"
            ],
            [
              "121717.4",
              "2.9621"
            ],
            [
              "121716.4",
              "0.0000"
            ],
            [
              "121716.2",
              "2.3870"
            ],
            [
              "121715.2",
              "0.0000"
            ],
            [
              "121715.0",
              "0.2549"
            ],
            [
              "121714.6",
              "0.0000"
            ],
            [
              "121713.8",
              "0.3252"
            ],
            [
              "121711.5",
              "0.0000"
            ],
            [
              "121710.9",
              "0.0113"
            ],
            [
              "121709.4",
              "0.0038"
            ],
            [
              "121708.7",
              "0.0054"
            ],
            [
              "121708.0",
              "0.0021"
            ],
            [
              "121707.6",
              "0.0081"
            ],
            [
              "121707.3",
              "0.0077"
            ],
            [
              "121706.9",
              "0.0042"
            ],
            [
              "121706.8",
              "4.7697"
            ]
          ]  // Changed ask depth entries, each element is [price, quantity]
    }  // Push content, containing detailed depth update information
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@incrDepth"
}
error code
403
Internal service call exception
1006
Internal service call exception.Generally network related issue
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-swap.bingx.com/swap-market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@incrDepth"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if utf8_data == "Ping": # this is very important , if you receive 'Ping' you need to send 'Pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
                  























GET
/openApi/spot/v1/common/symbols
(Spot trading symbols)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Spot trading allows users to buy or sell digital assets at the current market price.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
Trading pair, e.g., BTC-USDT
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
symbol
string
Trading symbol
tickSize
float64
Price tick size
stepSize
float64
Quantity step size
minQty
float64
Deprecated; can be calculated using minQty=minNotional/price
maxQty
float64
Deprecated; can be calculated using maxQty=maxNotional/price
minNotional
float64
Minimum trading notional
maxNotional
float64
Maximum trading notional
maxMarketNotional
float64
Maximum notional amount allowed for a single market order
status
int64
0 offline, 1 online, 5 pre-open, 10 accessed, 25 suspended, 29 pre-delisted, 30 delisted
apiStateBuy
boolean
Buy allowed
apiStateSell
boolean
Sell allowed
timeOnline
long
Symbol online time
offTime
long
Symbol offline time
maintainTime
long
Symbol maintenance time
displayName
string
Display name for UI
Request Example
{
  "symbol": "BTC-USDT"
}
Response Example
{
  "code": 0,
  "msg": "",
  "debugMsg": "",
  "data": {
    "symbols": [
      {
        "symbol": "BTC-USDT",
        "minQty": 0.0001826,
        "maxQty": 18.2663756,
        "minNotional": 5,
        "maxNotional": 500000,
        "maxMarketNotional": 500000,
        "status": 1,
        "tickSize": 0.01,
        "stepSize": 0.00001
      }
    ]
  }
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/spot/v1/common/symbols'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())



   GET
/openApi/spot/v1/market/trades
(Recent Trades List)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Retrieve the most recent market trades for a specified symbol.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, e.g., BTC-USDT
limit
int64
No
default 100, max 500
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
id
long
transaction id
price
float64
price
qty
float64
quantity
time
long
time
buyerMaker
boolean
Buyer or not
Request Example
{
  "symbol": "BTC-USDT",
  "limit": 5
}
Response Example
{
  "code": 0,
  "timestamp": 1702720325973,
  "data": [
    {
      "id": 76909154,
      "price": 42195.21,
      "qty": 0.00195,
      "time": 1702720325553,
      "buyerMaker": true
    },
    {
      "id": 76909153,
      "price": 42195.31,
      "qty": 0.00139,
      "time": 1702720325552,
      "buyerMaker": true
    },
    {
      "id": 76909152,
      "price": 42195.48,
      "qty": 0.00177,
      "time": 1702720325552,
      "buyerMaker": false
    },
    {
      "id": 76909151,
      "price": 42195.15,
      "qty": 0.00247,
      "time": 1702720324643,
      "buyerMaker": true
    },
    {
      "id": 76909150,
      "price": 42195.25,
      "qty": 0.02968,
      "time": 1702720324643,
      "buyerMaker": true
    }
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/spot/v1/market/trades'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT",
    "limit": 5
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())


    GET
/openApi/spot/v1/market/depth
(Order Book)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Get the order book depth for a specified symbol. It provides the most recent buy and sell orders for the given trading pair.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, e.g., BTC-USDT
limit
int64
No
default 20, max 1000
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
bids
array
first element price, second element quantity
asks
array
first element price, second element quantity
ts
int64
Timestamp of depth, Unit: milliseconds
Request Example
{
  "symbol": "BTC-USDT",
  "limit": 5
}
Response Example
{
  "code": 0,
  "timestamp": 1702720487674,
  "data": {
    "bids": [
      [
        "42182.22",
        "0.99114"
      ],
      [
        "42182.19",
        "1.00643"
      ],
      [
        "42182.17",
        "0.95406"
      ],
      [
        "42182.10",
        "0.87420"
      ],
      [
        "42182.08",
        "1.17445"
      ]
    ],
    "asks": [
      [
        "42183.23",
        "3.57139"
      ],
      [
        "42183.22",
        "2.05573"
      ],
      [
        "42183.20",
        "2.26065"
      ],
      [
        "42183.19",
        "1.61695"
      ],
      [
        "42183.17",
        "4.14752"
      ]
    ],
    "ts": 1702720487674
  }
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/spot/v1/market/depth'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT",
    "limit": 5
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())



GET
/openApi/spot/v2/market/kline
(Kline/Candlestick Data)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Get the Kline/candlestick data for a specified symbol. It provides historical market data in the form of candlesticks, with options to specify time intervals.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, for example: BTC-USDT, please use capital letters.
interval
string
Yes
Time interval, refer to field description
startTime
int64
No
Start time, unit: milliseconds
endTime
int64
No
End time, unit: milliseconds
timeZone
int32
No
Time zone offset, only supports 0 or 8 (UTC+0 or UTC+8)
limit
int64
No
Default value: 500 Maximum value: 1440
timestamp
int64
Yes
Timestamp of initiating the request, Unit: milliseconds
recvWindow
int64
No
Request valid time window value, Unit: milliseconds
response body
klines
array
Candlestick chart array
Request Example
{
  "symbol": "BTC-USDT",
  "interval": "1m",
  "timeZone": 8,
  "limit": 5
}
Response Example
{
  "code": 0,
  "timestamp": 1702720626772,
  "data": [
    [
      1702720620000,
      42216.29,
      42216.94,
      42216.29,
      42216.72,
      0.2,
      1702720679999,
      8548.46
    ],
    [
      1702720560000,
      42220.61,
      42221.1,
      42215.56,
      42216.63,
      2.93,
      1702720619999,
      123968.7
    ],
    [
      1702720500000,
      42182.59,
      42220.38,
      42182.59,
      42220.38,
      1.53,
      1702720559999,
      64851.33
    ],
    [
      1702720440000,
      42182.84,
      42183.16,
      42182.22,
      42182.81,
      2.54,
      1702720499999,
      107559.45
    ],
    [
      1702720380000,
      42199.72,
      42204.53,
      42180.2,
      42182.76,
      1.1,
      1702720439999,
      46549.09
    ]
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/spot/v2/market/kline'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT",
    "interval": "1m",
    "timeZone": 8,
    "limit": 5
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())



  GET
/openApi/spot/v1/ticker/24hr
(24hr Ticker Price Change Statistics)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Get the 24-hour price change statistics for a specified symbol. This includes information on price changes, price percentage, high/low prices, and trading volume over the last 24 hours.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
Trading pairs, such as: BTC-USDT, will return all symbol data when no parameters are entered
timestamp
int64
Yes
The timestamp of the request, in milliseconds
recvWindow
int64
No
Request valid time window value, unit: millisecond
response body
symbol
string
Trading pair, for example: BTC-USDT
openPrice
string
Opening price in the last 24 hours
highPrice
string
The highest price in the last 24 hours
lowPrice
string
The lowest price in the last 24 hours
lastPrice
string
Latest price
volume
string
Total trading volume (base asset)
quoteVolume
string
Total quote volume (quote asset)
openTime
int64
The start time of the ticker interval
closeTime
int64
end time of the ticker interval
count
int64
The number of transactions within the statistical time
bidPrice
float64
bid price
bidQty
float64
bid quantity
askPrice
float64
ask price
askQty
float64
ask quantity
priceChangePercent
string
Price change percentage field
Request Example
{
  "symbol": "BTC-USDT"
}
Response Example
{
  "code": 0,
  "timestamp": 1702720823624,
  "data": [
    {
      "symbol": "BTC-USDT",
      "openPrice": 42827.65,
      "highPrice": 42893.56,
      "lowPrice": 41648.71,
      "lastPrice": 42215.15,
      "priceChange": 1244.85,
      "priceChangePercent": "2.91%",
      "volume": 5099.21,
      "quoteVolume": 214948771.34,
      "openTime": 1702634423624,
      "closeTime": 1702720823624,
      "askPrice": 42215.55,
      "askQty": 2.20125,
      "bidPrice": 42214.65,
      "bidQty": 0.8962
    }
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/spot/v1/ticker/24hr'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())



  GET
/openApi/spot/v2/market/depth
(Order Book aggregation)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Get the aggregated order book depth for a specified symbol. It provides a summary of the current buy and sell orders, aggregated into price levels. This endpoint helps to understand the market liquidity at different price levels.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, such as: BTC-USDT
depth
int64
Yes
Query depth
type
string
Yes
step0 default precision, step1 to step5 are 10 to 100000 times precision respectively
response body
bids
array
Buy depth, where the first element of the array is the price and the second element is the quantity
asks
array
Sell depth, where the first element of the array is the price and the second element is the quantity
ts
int64
Timestamp
Request Example
{
  "symbol": "BTC-USDT",
  "limit": 20,
  "type": "step0"
}
Response Example
{
  "code": 0,
  "timestamp": 1707143021361,
  "data": {
    "bids": [
      [
        "43340.92",
        "1.91154"
      ],
      [
        "43340.88",
        "3.85804"
      ],
      [
        "43340.85",
        "4.26840"
      ],
      [
        "43340.83",
        "2.08925"
      ],
      [
        "43340.81",
        "2.04579"
      ],
      [
        "43340.79",
        "1.58294"
      ],
      [
        "43340.77",
        "1.54605"
      ],
      [
        "43340.76",
        "2.11097"
      ],
      [
        "43340.74",
        "1.82713"
      ],
      [
        "43340.72",
        "1.97847"
      ],
      [
        "43340.69",
        "3.12035"
      ],
      [
        "43340.65",
        "3.49761"
      ],
      [
        "43340.61",
        "3.61076"
      ],
      [
        "43340.56",
        "4.56538"
      ],
      [
        "43340.47",
        "4.3701"
      ],
      [
        "43340.46",
        "3.47356"
      ],
      [
        "43340.44",
        "10.99309"
      ],
      [
        "43340.23",
        "9.78746"
      ],
      [
        "43339.90",
        "9.77564"
      ],
      [
        "43339.86",
        "11.06385"
      ]
    ],
    "asks": [
      [
        "43341.79",
        "5.76033"
      ],
      [
        "43341.86",
        "3.9063"
      ],
      [
        "43341.88",
        "5.76033"
      ],
      [
        "43341.90",
        "4.98845"
      ],
      [
        "43341.92",
        "4.98845"
      ],
      [
        "43341.94",
        "5.25236"
      ],
      [
        "43341.95",
        "22.48145"
      ],
      [
        "43341.98",
        "9.40042"
      ],
      [
        "43342.00",
        "13.58550"
      ],
      [
        "43342.02",
        "9.44509"
      ],
      [
        "43342.05",
        "5.25236"
      ],
      [
        "43342.07",
        "4.83999"
      ],
      [
        "43342.08",
        "4.74583"
      ],
      [
        "43342.10",
        "4.58787"
      ],
      [
        "43342.11",
        "5.61344"
      ],
      [
        "43342.13",
        "4.57564"
      ],
      [
        "43342.15",
        "5.14039"
      ],
      [
        "43342.17",
        "4.65339"
      ],
      [
        "43342.19",
        "5.32833"
      ],
      [
        "43342.22",
        "9.74216"
      ]
    ],
    "ts": 1707143021361
  }
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/spot/v2/market/depth'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT",
    "limit": 20,
    "type": "step0"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':




GET
/openApi/spot/v2/ticker/price
(Symbol Price Ticker)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Get the latest market price for a specified symbol. This endpoint provides the most recent price for the trading pair.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, such as: BTC-USDT
response body
price
string
Latest price
symbol
string
Trading pair, such as: BTC-USDT
timestamp
int64
Timestamp
Request Example
{
  "symbol": "BTC-USDT"
}
Response Example
{
  "code": 0,
  "timestamp": 1707147143049,
  "data": [
    {
      "symbol": "BTC-USDT",
      "trades": [
        {
          "timestamp": 1707147142579,
          "tradeId": "86521463",
          "price": "42902.61",
          "amount": "",
          "type": 1,
          "volume": "0.11689"
        }
      ]
    }
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/spot/v2/ticker/price'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())




 GET
/openApi/spot/v1/ticker/bookTicker
(Symbol Order Book Ticker)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Get the best (lowest ask and highest bid) price and quantity for a specified symbol in the order book. This endpoint provides the most competitive prices for the given trading pair.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, such as: BTC-USDT
response body
eventType
string
Data type
symbol
string
Trading pair, such as: BTC-USDT
bidPrice
string
Best bid price
bidVolume
string
Best bid volume
askPrice
string
Best ask price
askVolume
string
Best ask volume
Request Example
{
  "symbol": "BTC-USDT"
}
Response Example
{
  "code": 0,
  "timestamp": 1707147866795,
  "data": [
    {
      "eventType": "bookTicker",
      "time": 1707147866623,
      "symbol": "BTC-USDT",
      "bidPrice": "42738.64",
      "bidVolume": "5.19530",
      "askPrice": "42739.50",
      "askVolume": "5.72867"
    }
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/spot/v1/ticker/bookTicker'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())




GET
/openApi/market/his/v1/kline
(Historical K-line)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Get historical candlestick (Kline) data for a specified symbol. This endpoint provides historical market data in the form of candlesticks with different time intervals.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, e.g., BTC-USDT, please use uppercase letters
interval
string
Yes
Time interval, reference field description
startTime
int64
No
Start time, unit: milliseconds
endTime
int64
No
End time, unit: milliseconds
limit
int64
No
Default value: 500 Maximum value: 500
response body
klines
array
K-line array
Request Example
{
  "symbol": "BTC-USDT",
  "interval": "1m",
  "limit": 5
}
Response Example
{
  "code": 0,
  "timestamp": 1702720626772,
  "data": [
    [
      1702720620000,
      42216.29,
      42216.94,
      42216.29,
      42216.72,
      0.2,
      1702720679999,
      8548.46
    ],
    [
      1702720560000,
      42220.61,
      42221.1,
      42215.56,
      42216.63,
      2.93,
      1702720619999,
      123968.7
    ],
    [
      1702720500000,
      42182.59,
      42220.38,
      42182.59,
      42220.38,
      1.53,
      1702720559999,
      64851.33
    ],
    [
      1702720440000,
      42182.84,
      42183.16,
      42182.22,
      42182.81,
      2.54,
      1702720499999,
      107559.45
    ],
    [
      1702720380000,
      42199.72,
      42204.53,
      42180.2,
      42182.76,
      1.1,
      1702720439999,
      46549.09
    ]
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/market/his/v1/kline'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT",
    "interval": "1m",
    "limit": 5
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())




GET
/openApi/market/his/v1/trade
(Old Trade Lookup)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Get historical trades for a specified symbol. This endpoint returns a list of trades that occurred in the past, with details such as the trade price, quantity, and trade time.
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, e.g., BTC-USDT, please use uppercase letters
limit
int64
No
Default 100, maximum 500
fromId
string
No
The last recorded tid
response body
id
long
Trade id
price
float64
Price
qty
float64
Quantity
time
long
Time
buyerMaker
boolean
Buyer maker
Request Example
{
  "symbol": "BTC-USDT",
  "limit": 5
}
Response Example
{
  "code": 0,
  "timestamp": 1702720325973,
  "data": [
    {
      "tid": "170891918044290305561",
      "t": 1708919180442,
      "ms": 2,
      "s": "BTC-USDT",
      "p": 51496.35,
      "v": 0.00063
    },
    {
      "tid": "170891917959890305560",
      "t": 1708919179598,
      "ms": 1,
      "s": "BTC-USDT",
      "p": 51495.89,
      "v": 0.00188
    },
    {
      "tid": "170891917942490305559",
      "t": 1708919179424,
      "ms": 1,
      "s": "BTC-USDT",
      "p": 51496.159,
      "v": 0.00075
    },
    {
      "tid": "170891917907790305558",
      "t": 1708919179077,
      "ms": 2,
      "s": "BTC-USDT",
      "p": 51496.13,
      "v": 0.01044
    },
    {
      "tid": "170891917896690305557",
      "t": 1708919178966,
      "ms": 1,
      "s": "BTC-USDT",
      "p": 51496,
      "v": 0.00129
    }
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/market/his/v1/trade'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USDT",
    "limit": 5
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())


WSS
Subscription transaction by transaction
Subscribe to the trade detail data of a trading pair
Due to multi-threaded push, it cannot be guaranteed that the push transaction ID is ordered.
Subscription Type
The dataType is <symbol>@trade E.g. BTC-USDT@trade ETH-USDT@trade
Subscription example
{"id":"24dd0e35-56a4-4f7a-af8a-394c7060909c","reqType": "sub","dataType":"BTC-USDT@trade"}
subscription address
PROD
wss://open-api-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@trade
data update
e
string
Event type
E
int64
Event time
s
string
Trading pair
t
int64
Trade ID
p
string
Execution price
q
string
Execution quantity
T
int64
Execution time
m
boolean
Whether the buyer is a market maker. If true, this trade is a passive sell order; otherwise, it is a passive buy order.
subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "sub",
  "dataType": "BTC-USDT@trade"
}
subscribe success sample
{
  "code": 0,
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "msg": "SUCCESS",
  "timestamp": 1760066128475
}
data update sample
{
  "code": 0,
  "data": {
      "E": 1760066129336,  // Event time
      "T": 1760066129316,  // Execution time
      "e": "trade",  // Event type
      "m": true,  // Whether the buyer is a market maker. If true, this trade is a passive sell order; otherwise, it is a passive buy order.
      "p": "121123.47",  // Execution price
      "q": "0.003189",  // Execution quantity
      "s": "BTC-USDT",  // Trading pair
      "t": "172356086"  // Trade ID
    },
  "dataType": "BTC-USDT@trade",
  "success": true,
  "timestamp": 1760066129336
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@trade"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-ws.bingx.com/market" 
CHANNEL= {"id":"24dd0e35-56a4-4f7a-af8a-394c7060909c","reqType":"sub","dataType":"BTC-USDT@trade"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
                  



 WSS
K-line Streamst
Subscribe to market k-line data of one trading pair
Subscription Type
The dataType is <symbol>@kline_<interval> E.g. BTC-USDT@kline_1min
Subscription Example
{"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType": "sub","dataType":"BTC-USDT@kline_1min"}
subscription address
PROD
wss://open-api-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@kline_1m
data update
T
int64
K-line end time
c
string
Last trade price during this K-line period
h
string
Highest trade price during this K-line period
i
string
K-line interval
l
string
Lowest trade price during this K-line period
n
int64
Number of trades during this K-line period
o
string
First trade price during this K-line period
q
string
Turnover during this K-line period
s
string
Trading pair
t
int64
K-line start time
v
string
Volume during this K-line period
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@depth5@500ms"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "data": {
      "E": 1760066282349,
      "K": {
            "T": 1760066339999,  // K-line end time
            "c": "121137.93299999999",  // Last trade price during this K-line period
            "h": "121137.946",  // Highest trade price during this K-line period
            "i": "1min",  // K-line interval
            "l": "121137.93299999999",  // Lowest trade price during this K-line period
            "n": 4,  // Number of trades during this K-line period
            "o": "121137.946",  // First trade price during this K-line period
            "q": "3131.052371",  // Turnover during this K-line period
            "s": "BTC-USDT",  // Trading pair
            "t": 1760066280000,  // K-line start time
            "v": "0.025847000000000000"  // Volume during this K-line period
          },
      "e": "kline",
      "s": "BTC-USDT"  // Trading pair
    },
  "dataType": "BTC-USDT@kline_1min",
  "success": true
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@depth5@500ms"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@depth5@500ms"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
                                   
WSS
Subscribe Market Depth Data
Push limited file depth information every 300ms. Default level 20.
Subscription Type
The dataType is <symbol>@depth<level> E.g. BTC-USDT@depth50
Subscription Example
{"id":"975f7385-7f28-4ef1-93af-df01cb9ebb53","reqType": "sub","dataType":"BTC-USDT@depth50"}
subscription address
PROD
wss://open-api-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@depth5@500ms
data update
dataType
string
Subscribed data type, for example BTC-USDT@depth
data
string
Push content
asks
array
Changed sell order depth
bids
array
Changed buy order depth
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@depth5@500ms"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "data": {
      "asks": [
            [
              "121398.38",
              "0.000025"
            ],
            [
              "121396.60",
              "0.000010"
            ],
            [
              "121395.65",
              "0.000009"
            ],
            [
              "121394.84",
              "0.000021"
            ],
            [
              "121392.60",
              "0.000008"
            ],
            [
              "121384.53",
              "0.000040"
            ],
            [
              "121383.01",
              "0.000049"
            ],
            [
              "121376.52",
              "0.000008"
            ],
            [
              "121375.00",
              "0.000024"
            ],
            [
              "121367.22",
              "0.000050"
            ],
            [
              "121366.37",
              "0.000024"
            ],
            [
              "121364.86",
              "0.000012"
            ],
            [
              "121362.22",
              "0.000017"
            ],
            [
              "121358.78",
              "12.021056"
            ],
            [
              "121350.73",
              "0.000008"
            ],
            [
              "121348.59",
              "0.000008"
            ],
            [
              "121348.56",
              "0.000016"
            ],
            [
              "121346.96",
              "0.000008"
            ],
            [
              "121342.34",
              "0.000010"
            ],
            [
              "121339.35",
              "0.000012"
            ],
            [
              "121337.82",
              "0.000008"
            ],
            [
              "121337.72",
              "0.000008"
            ],
            [
              "121335.26",
              "0.000017"
            ],
            [
              "121333.24",
              "0.000020"
            ],
            [
              "121333.12",
              "0.000009"
            ],
            [
              "121333.08",
              "0.000263"
            ],
            [
              "121333.02",
              "0.000082"
            ],
            [
              "121332.99",
              "0.000008"
            ],
            [
              "121332.91",
              "0.000024"
            ],
            [
              "121331.98",
              "0.000007"
            ],
            [
              "121325.48",
              "0.000555"
            ],
            [
              "121325.00",
              "0.000094"
            ],
            [
              "121319.49",
              "0.000018"
            ],
            [
              "121316.45",
              "0.000212"
            ],
            [
              "121316.22",
              "0.000008"
            ],
            [
              "121310.00",
              "0.000015"
            ],
            [
              "121309.83",
              "0.000018"
            ],
            [
              "121306.09",
              "0.000008"
            ],
            [
              "121303.39",
              "53.862426"
            ],
            [
              "121300.00",
              "0.000131"
            ],
            [
              "121292.32",
              "0.000008"
            ],
            [
              "121278.76",
              "0.000216"
            ],
            [
              "121273.65",
              "0.000008"
            ],
            [
              "121269.16",
              "0.000008"
            ],
            [
              "121268.48",
              "0.000009"
            ],
            [
              "121266.37",
              "0.000012"
            ],
            [
              "121250.00",
              "0.000013"
            ],
            [
              "121247.72",
              "0.966935"
            ],
            [
              "121246.81",
              "1.161872"
            ],
            [
              "121228.63",
              "0.000150"
            ]
          ],  // Changed sell order depth
      "bids": [
            [
              "121228.61",
              "0.000321"
            ],
            [
              "121210.43",
              "4.538315"
            ],
            [
              "121210.42",
              "0.000825"
            ],
            [
              "121210.24",
              "0.089875"
            ],
            [
              "121210.20",
              "0.293284"
            ],
            [
              "121209.32",
              "0.284686"
            ],
            [
              "121175.99",
              "50.747159"
            ],
            [
              "121143.64",
              "15.227434"
            ],
            [
              "121098.43",
              "4.126438"
            ],
            [
              "121051.22",
              "4.160294"
            ],
            [
              "121046.59",
              "5.444737"
            ],
            [
              "121007.77",
              "5.059377"
            ],
            [
              "120969.30",
              "4.669210"
            ],
            [
              "120964.82",
              "0.000049"
            ],
            [
              "120957.46",
              "0.000024"
            ],
            [
              "120944.39",
              "0.000015"
            ],
            [
              "120926.85",
              "4.821994"
            ],
            [
              "120919.23",
              "0.000009"
            ],
            [
              "120918.09",
              "14.072688"
            ],
            [
              "120915.60",
              "0.000049"
            ],
            [
              "120909.05",
              "0.000017"
            ],
            [
              "120907.81",
              "0.000006"
            ],
            [
              "120906.63",
              "0.000030"
            ],
            [
              "120905.80",
              "0.000052"
            ],
            [
              "120905.29",
              "0.000001"
            ],
            [
              "120905.08",
              "0.000102"
            ],
            [
              "120902.76",
              "0.000024"
            ],
            [
              "120902.34",
              "0.000005"
            ],
            [
              "120901.45",
              "0.000009"
            ],
            [
              "120900.36",
              "0.000094"
            ],
            [
              "120900.00",
              "0.000009"
            ],
            [
              "120896.00",
              "0.000008"
            ],
            [
              "120895.13",
              "0.000004"
            ],
            [
              "120894.15",
              "0.000014"
            ],
            [
              "120893.38",
              "0.000008"
            ],
            [
              "120890.59",
              "0.000296"
            ],
            [
              "120889.15",
              "0.000022"
            ],
            [
              "120888.88",
              "0.000022"
            ],
            [
              "120885.74",
              "7.146244"
            ],
            [
              "120885.64",
              "0.000451"
            ],
            [
              "120885.12",
              "0.000005"
            ],
            [
              "120884.88",
              "0.000021"
            ],
            [
              "120883.65",
              "0.000052"
            ],
            [
              "120883.45",
              "0.000011"
            ],
            [
              "120880.52",
              "0.000024"
            ],
            [
              "120880.16",
              "0.000008"
            ],
            [
              "120879.78",
              "0.000005"
            ],
            [
              "120879.41",
              "0.000019"
            ],
            [
              "120879.16",
              "0.000056"
            ],
            [
              "120878.47",
              "0.000014"
            ]
          ],  // Changed buy order depth
      "lastUpdateId": 14669994934
    },  // Push content
  "dataType": "BTC-USDT@depth50",  // Subscribed data type, for example BTC-USDT@depth
  "success": true,
  "timestamp": 1760066405887
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@depth5@500ms"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@depth5@500ms"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
                  





WSS
Subscribe to 24-hour Price Change
Pushes data of 24-hour price change every 1000ms.
Subscription Type
dataType is <symbol>@ticker, for example, BTC-USDT@ticker
Subscription Example
{"id":"975f7385-7f28-4ef1-93af-df01cb9ebb53","reqType": "sub","dataType":"BTC-USDT@ticker"}
subscription address
PROD
wss://open-api-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@depth5@500ms
data update
e
string
Event type
E
int64
Event time
s
string
Trading pair
p
string
Price change
P
string
Price change percentage
o
string
Open price
h
string
Highest price
l
string
Lowest price
c
string
Latest trade price
v
string
Volume
q
string
Turnover
O
int64
Statistics start time
C
int64
Statistics end time
B
string
Best bid price
b
string
Best bid quantity
A
string
Best ask price
a
string
Best ask quantity
n
int64
Number of trades
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@depth5@500ms"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "timestamp": 1760066441401,
  "dataType": "BTC-USDT@ticker",
  "data": {
      "e": "24hTicker",  // Event type
      "E": 1760066441399,  // Event time
      "s": "BTC-USDT",  // Trading pair
      "p": -632.32,  // Price change
      "P": "-0.52%",  // Price change percentage
      "o": 121931.93,  // Open price
      "h": 123750,  // Highest price
      "l": 119666.27,  // Lowest price
      "c": 121299.61,  // Latest trade price
      "v": 3087.49,  // Volume
      "q": 375356180.14,  // Turnover
      "O": 1759980041399,  // Statistics start time
      "C": 1760066441399,  // Statistics end time
      "A": 121300,  // Best ask price
      "a": 0.00013099999999999999,  // Best ask quantity
      "B": 121291.64,  // Best bid price
      "b": 9.293124  // Best bid quantity
    }
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@depth5@500ms"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@depth5@500ms"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
                  




 WSS
Spot Latest Trade Price
Real-time Push
Subscription Type
dataType is <symbol>@lastPrice, for example, BTC-USDT@lastPrice
Subscription Example
{"id":"975f7385-7f28-4ef1-93af-df01cb9ebb53","reqType": "sub","dataType":"BTC-USDT@lastPrice"}
subscription address
PROD
wss://open-api-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@depth5@500ms
data update
c
string
Price
s
string
Currency pair name, such as BTC
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@lastPrice"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "data": {
      "c": "121324.91",  // Price
      "e": "lastPriceUpdate",
      "s": "BTC-USDT"  // Currency pair name, such as BTC
    },
  "dataType": "BTC-USDT@lastPrice",
  "success": true
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@lastPrice"
}
error code
403
Internal service call exception
1006
Internal service call exception
80015
symbol:BTC-USD1T not supported
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@lastPrice"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()




 WSS
Spot Best Order Book
Real-time Push
Subscription Type
dataType is <symbol>@bookTicker, for example, BTC-USDT@bookTicker
Subscription Example
{"id":"975f7385-7f28-4ef1-93af-df01cb9ebb53","reqType": "sub","dataType":"BTC-USDT@bookTicker"}
subscription address
PROD
wss://open-api-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@depth5@500ms
data update
e
string
Event type
E
int64
Event push time
s
string
Trading pair
b
string
Best bid price for buy orders
B
string
Best bid quantity for buy orders
a
string
Best ask price for sell orders
A
string
Best ask quantity for sell orders
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@bookTicker"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "data": {
      "A": "0.000016",  // Best ask quantity for sell orders
      "B": "4.372149",  // Best bid quantity for buy orders
      "E": 1760066515920,  // Event push time
      "a": "121348.56",  // Best ask price for sell orders
      "b": "121342.22",  // Best bid price for buy orders
      "e": "bookTicker",  // Event type
      "s": "BTC-USDT"  // Trading pair
    },
  "dataType": "BTC-USDT@bookTicker",
  "success": true
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@bookTicker"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@bookTicker"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()




WSS
Incremental and Full Depth Information
Push incremental depth information of 1000 levels every 500ms.
How the client should maintain incremental depth locally
1. After successfully subscribing, a full depth with an action field value of 'all' will be returned, along with a lastUpdateId used to handle the continuity of subsequent incremental depth. After receiving the full depth, the WebSocket should cache the full depth data in memory.
2. Subsequent depth changes will return incremental depth, with the action field set to 'update'. The value of the Nth incremental depth's lastUpdateId should be the N-1th depth's lastUpdateId + 1.
3. In rare cases where lastUpdateId is not continuous, you can choose to reconnect, or cache the last three incremental depths and try to merge the data by finding continuous lastUpdateId from the cache (because due to multithreading or network routing issues, data order may not be strongly guaranteed).
4. Then, iterate over the received incremental depth and compare it with the current depth one by one. It's recommended to consider thread-safe design and coding practices (as the push frequency may increase later). The data structure could be a sorted map, such as TreeMap:
(1) If the price level does not exist in the current depth, it means a new price level should be added. (Add)
(2) If the quantity corresponding to the price is 0, the price level should be removed from the current depth. (Delete)
(3) If the quantity corresponding to the price is different from the current value, replace it with the quantity returned by the incremental depth. (Update)
(4) After traversing, you will obtain the latest depth, update the depth cache, and remember to update the lastUpdateId.
Subscription Type
The dataType is <symbol>@incrDepth, for example, BTC-USDT@incrDepth
Subscription Example
{"id":"975f7385-7f28-4ef1-93af-df01cb9ebb53","reqType": "sub","dataType":"BTC-USDT@incrDepth"}
subscription address
PROD
wss://open-api-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@depth5@500ms
data update
dataType
string
Subscribed data type, for example BTC-USDT@incrDepth
action
string
Depth type: all-full depth, update-incremental
lastUpdateId
int64
Update ID, this is a continuously incrementing long integer value used to describe the sequential relationship between returned incremental depths
data
string
Push content
asks
array
Changed sell order depth (price:quantity)
bids
array
Changed buy order depth (price:quantity)
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USDT@incrDepth"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "timestamp": 1769443327977,
  "success": true,
  "dataType": "BTC-USDT@incrDepth",  // Subscribed data type, for example BTC-USDT@incrDepth
  "data": {
      "action": "update",  // Depth type: all-full depth, update-incremental
      "lastUpdateId": 524997,  // Update ID, this is a continuously incrementing long integer value used to describe the sequential relationship between returned incremental depths
      "sourceUpdateId": 15253687425,
      "asks": {
            "87554.35": "0.004666",
            "87555.23": "0",
            "87559.97": "3.136896",
            "87560.71": "0.000056",
            "87560.92": "0"
          },  // Changed sell order depth (price:quantity)
      "bids": {
            "87555.22": "0",
            "87554.34": "0.001949",
            "87549.60": "0",
            "87549.10": "0",
            "87548.90": "0"
          }  // Changed buy order depth (price:quantity)
    }  // Push content
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USDT@incrDepth"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USDT@incrDepth"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()






































                                                               GET
/openApi/cswap/v1/market/contracts
(Contract Information)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Contract Information
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
trading pair, for example: BTC-USD
timestamp
int64
Yes
Request timestamp, in milliseconds.
recvWindow
int64
No
The window of time for which the request is valid, in milliseconds.
response body
code
int64
Status Code
msg
string
Description
timestamp
int64
Response time, Unit: milliseconds
data
List<Data>
Request Example
{}
Response Example
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "symbol": "BTC-USD",
      "pricePrecision": 1,
      "minTickSize": "100",
      "minTradeValue": "100",
      "minQty": "1.00000000",
      "status": 1,
      "timeOnline": 1710738000000
    },
    {
      "symbol": "ETH-USD",
      "pricePrecision": 2,
      "minTickSize": "10",
      "minTradeValue": "10",
      "minQty": "1.00000000",
      "status": 1,
      "timeOnline": 1710738000000
    }
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/cswap/v1/market/contracts'
    method = "GET"
    paramsMap = {}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())







 GET
/openApi/cswap/v1/market/premiumIndex
(Price & Current Funding Rate)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Price & Current Funding Rate
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
trading pair, for example: BTC-USD
timestamp
int64
Yes
Request timestamp, in milliseconds.
recvWindow
int64
No
The window of time for which the request is valid, in milliseconds.
response body
code
int64
Status Code
msg
string
Description
timestamp
int64
Response time, Unit: milliseconds
data
List<Data>
Request Example
{
  "symbol": "BTC-USD"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {
    "symbol": "BTC-USD",
    "markPrice": "42216.4",
    "indexPrice": "42219.9",
    "lastFundingRate": "0.00025100",
    "nextFundingTime": 1702742400000
  }
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/cswap/v1/market/premiumIndex'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USD"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())



GET
/openApi/cswap/v1/market/openInterest
(Get Swap Open Positions)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Get Swap Open Positions
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
trading pair, for example: BTC-USD
timestamp
int64
Yes
Request timestamp, in milliseconds.
recvWindow
int64
No
The window of time for which the request is valid, in milliseconds.
response body
code
int64
Status Code
msg
string
Description
timestamp
int64
Response time, Unit: milliseconds
data
List<Data>
Request Example
{
  "symbol": "BTC-USD"
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": {
    "openInterest": "35876.52",
    "symbol": "BTC-USD",
    "time": 1702719692859
  }
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/cswap/v1/market/openInterest'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USD"
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())




 GET
/openApi/cswap/v1/market/klines
(Get K-line Data)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:only supports querying K-line data for the last 30 days
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, e.g., BTC-USD. Please use uppercase letters.
interval
string
Yes
Time interval, optional values are: 1m, 3m, 5m, 15m, 30m, 1h, 2h, 4h, 6h, 8h, 12h, 1d, 3d, 1w, 1M.
startTime
int64
No
Start time, the returned result includes the K-line of this time.
endTime
int64
No
End time, the returned result does not include the K-line of this time.
timeZone
int32
No
Time zone offset, only supports 0 or 8 (UTC+0 or UTC+8)
limit
int64
No
The number of returned results. The default is 500 if not filled, and the maximum is 1000.
timestamp
int64
Yes
Request timestamp, in milliseconds.
recvWindow
int64
No
The window of time for which the request is valid, in milliseconds.
response body
code
int64
Status code.
msg
string
Description message.
timestamp
int64
Response time, Unit: milliseconds
data
List<Data>
Request Example
{
  "symbol": "BTC-USD",
  "interval": "1m",
  "startTime": 1716912000000,
  "endTime": 1716998400000,
  "timeZone": 8,
  "limit": 100,
  "timestamp": 1717050357477
}
Response Example
{
  "code": 0,
  "msg": "",
  "data": [
    {
      "open": "67792.6",
      "close": "67792.6",
      "high": "67792.6",
      "low": "67792.6",
      "volume": "3.00",
      "time": 1716998340000
    }
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/cswap/v1/market/klines'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USD",
    "interval": "1m",
    "startTime": 1716912000000,
    "endTime": 1716998400000,
    "timeZone": 8,
    "limit": 100,
    "timestamp": 1717050357477
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())



 GET
/openApi/cswap/v1/market/depth
(Query Depth Data)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Query Depth Data
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
Yes
Trading pair, e.g., BTC-USD. Please use uppercase letters.
limit
int64
No
The number of returned results. The default is 20 if not filled, optional values: 5, 10, 20, 50, 100, 500, 1000.
timestamp
int64
Yes
Request timestamp, in milliseconds.
recvWindow
int64
No
The window of time for which the request is valid, in milliseconds.
response body
code
int64
Status code.
msg
string
Description message.
timestamp
int64
Response time, Unit: milliseconds
data
List<Data>
Request Example
{
  "symbol": "BTC-USD",
  "limit": 100,
  "timestamp": 1717050357477
}
Response Example
{
  "code": 0,
  "msg": "",
  "debugMsg": "",
  "data": {
    "T": 1717052420270,
    "bids": [
      [
        "67753.0",
        "1360.0"
      ],
      [
        "67752.9",
        "10.0"
      ],
      [
        "67752.8",
        "11.0"
      ],
      [
        "67752.7",
        "1.0"
      ],
      [
        "67752.6",
        "1.0"
      ]
    ],
    "asks": [
      [
        "67754.9",
        "4.0"
      ],
      [
        "67754.8",
        "4.0"
      ],
      [
        "67754.7",
        "22.0"
      ],
      [
        "67754.6",
        "19.0"
      ],
      [
        "67754.5",
        "703.0"
      ]
    ]
  }
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/cswap/v1/market/depth'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USD",
    "limit": 100,
    "timestamp": 1717050357477
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())





GET
/openApi/cswap/v1/market/ticker
(Query 24-Hour Price Change)
Copy
Request Type GET
IP Rate Limit IP Rate Limit :500 requests per 10 seconds.
Signature Verification: No
API Key Permission: Read
Endpoint description:Query 24-Hour Price Change
host
PROD
https://open-api.bingx.com
VST
https://open-api-vst.bingx.com
REQUEST PARAMETER
symbol
string
No
Trading pair, e.g., BTC-USD. Please use uppercase letters.
timestamp
int64
Yes
Request timestamp, in milliseconds.
recvWindow
int64
No
The window of time for which the request is valid, in milliseconds.
response body
code
int64
Status code.
msg
string
Description message.
timestamp
int64
Response time, Unit: milliseconds
data
List<Data>
Request Example
{
  "symbol": "BTC-USD",
  "timestamp": 1717050357477
}
Response Example
{
  "code": 0,
  "msg": "",
  "debugMsg": "",
  "data": [
    {
      "symbol": "BTC-USD",
      "priceChange": "-561.1",
      "priceChangePercent": "-0.8200%",
      "lastPrice": "67713.5",
      "lastQty": "38",
      "highPrice": "68346.9",
      "lowPrice": "67521.3",
      "volume": "3825668.00",
      "quoteVolume": "5084.51",
      "openPrice": "68279.2",
      "closeTime": "1717053813892",
      "bidPrice": "67712.7",
      "bidQty": "2100",
      "askPrice": "80000.0",
      "askQty": "1600"
    }
  ]
}
error code
No Data
Code Example
PythonGolangNode.jsJavaC#PHPShell

import time
import requests
import hmac
import urllib.parse
from hashlib import sha256

APIURL = "https://open-api.bingx.com"
APIKEY = ""
SECRETKEY = ""

def demo():
    payload = {}
    path = '/openApi/cswap/v1/market/ticker'
    method = "GET"
    paramsMap = {
    "symbol": "BTC-USD",
    "timestamp": 1717050357477
}
    paramsStr, urlParamsStr = parseParam(paramsMap)
    return send_request(method, path, paramsStr, urlParamsStr, payload)

def get_sign(api_secret, payload):
    signature = hmac.new(api_secret.encode("utf-8"), payload.encode("utf-8"), digestmod=sha256).hexdigest()
    print("sign=" + signature)
    return signature


def send_request(method, path, paramsStr, urlParamsStr, payload):
    url = "%s%s?%s&signature=%s" % (APIURL, path, urlParamsStr, get_sign(SECRETKEY, paramsStr))
    print(url)
    headers = {
        'X-BX-APIKEY': APIKEY,
    }
    response = requests.request(method, url, headers=headers, data=payload)
    return response.text

def parseParam(paramsMap):
    sortedKeys = sorted(paramsMap)
    paramsList = []
    urlParamsList = []
    for x in sortedKeys:
        value = paramsMap[x]
        paramsList.append("%s=%s" % (x, value))
    timestamp = str(int(time.time() * 1000))
    paramsStr = "&".join(paramsList)
    if paramsStr != "": 
        paramsStr = paramsStr + "&timestamp=" + timestamp
    else:
        paramsStr = "timestamp=" + timestamp
    contains = '[' in paramsStr or '{' in paramsStr
    for x in sortedKeys:
        value = paramsMap[x]
        if contains:
            encodedValue = urllib.parse.quote(str(value), safe='')
            urlParamsList.append("%s=%s" % (x, encodedValue))
        else:
            urlParamsList.append("%s=%s" % (x, value))
    urlParamsStr = "&".join(urlParamsList)
    if urlParamsStr != "": 
        urlParamsStr = urlParamsStr + "&timestamp=" + timestamp
    else:
        urlParamsStr = "timestamp=" + timestamp
    return paramsStr, urlParamsStr


if __name__ == '__main__':
    print("demo:", demo())




  WSS
Subscription transaction by transaction
Subscribe to the trade detail data of a trading pair
Subscription Type
The dataType is <symbol>@trade, for example: BTC-USD@trade, ETH-USD@trade
Subscription example
{"id":"24dd0e35-56a4-4f7a-af8a-394c7060909c","reqType":"sub","dataType":"BTC-USD@trade"}
subscription address
PROD
wss://open-api-cswap-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USD@trade
data update
e
string
Event type
E
int64
Event time
s
string
Trading pair
t
int64
Trade ID
p
string
Trade price
q
string
Quantity filled (contract quantity)
T
int64
Trade time
m
boolean
Whether the buyer is a market maker. If true, this trade is a passive sell order; otherwise, it is a passive buy order.
enenenenenene

subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "sub",
  "dataType": "BTC-USD@trade"
}
subscribe success sample
{
  "code": 0,
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "msg": "SUCCESS",
  "timestamp": 1760066128475
}
data update sample
{
  "code": 0,
  "dataType": "BTC-USD@trade",
  "data": {
      "e": "trade",  // Event type
      "E": 1760077547810,  // Event time
      "s": "BTC-USD",  // Trading pair
      "t": "143720871",  // Trade ID
      "p": "121596.7",  // Trade price
      "q": "5",  // Quantity filled (contract quantity)
      "T": 1760077547483,  // Trade time
      "m": false  // Whether the buyer is a market maker. If true, this trade is a passive sell order; otherwise, it is a passive buy order.
    }
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USD@trade"
}
error code
403
Internal service call exception
1006
Internal service call exception
80015
symbol:BTC-USD1T not supported
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-cswap-ws.bingx.com/market" 
CHANNEL= {"id":"24dd0e35-56a4-4f7a-af8a-394c7060909c","reqType":"sub","dataType":"BTC-USD@trade"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()





   WSS
Subscribe to the Latest Transaction Price
Subscribe to the latest transaction price
Subscription Type
Data type is <symbol>@lastPrice, e.g., BTC-USD@lastPrice, ETH-USDT@lastPrice
Subscription Example
{"id":"24dd0e35-56a4-4f7a-af8a-394c7060909c","reqType":"sub","dataType":"BTC-USD@lastPrice"}
subscription address
PROD
wss://open-api-cswap-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USD@lastPrice
data update
e
string
Event type
E
int64
Event time
s
string
Trading pair
p
string
Latest price
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USD@lastPrice"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "dataType": "BTC-USD@lastPrice",
  "data": {
      "p": "121613.4",  // Latest price
      "e": "lastPrice",  // Event type
      "s": "BTC-USD",  // Trading pair
      "E": 1760077573083  // Event time
    }
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USD@lastPrice"
}
error code
403
Internal service call exception
1006
Internal service call exception
80015
symbol:BTC-USD1T not supported
80015
dataType not supported
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-cswap-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USD@lastPrice"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()




 WSS
Subscribe to Mark Price
Subscribe to Mark Price
Subscription Type
Data type is <symbol>@markPrice, e.g., BTC-USD@markPrice, ETH-USD@markPrice
Subscription Example
{"id":"24dd0e35-56a4-4f7a-af8a-394c7060909c","reqType":"sub","dataType":"BTC-USD@markPrice"}
subscription address
PROD
wss://open-api-cswap-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USD@markPrice
data update
e
string
Event type
E
int64
Event time
s
string
Trading pair
p
string
Latest price
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USD@markPrice"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "timestamp": 1760077606104,
  "dataType": "BTC-USD@markPrice",
  "data": {
      "p": "121609.4",  // Latest price
      "e": "markPrice",  // Event type
      "s": "BTC-USD",  // Trading pair
      "E": 1760077605360  // Event time
    }
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USD@markPrice"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-cswap-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USD@markPrice"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()



WSS
Subscribe to Limited Depth
Subscribe to Limited Depth
Subscription Type
Data type is <symbol>@depth<count>, e.g., BTC-USD@depth5, ETH-USDT@depth5
Subscription Example
{"id":"24dd0e35-56a4-4f7a-af8a-394c7060909c","reqType":"sub","dataType":"BTC-USD@depth5"}
subscription address
PROD
wss://open-api-cswap-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USD@depth5
data update
dataType
string
Event type
symbol
string
Trading pair
bids
array
Buy order book levels
asks
array
Sell order book levels
aggPrecision
string
Aggregation precision
timestamp
int64
Timestamp
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USD@depth5"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "dataType": "BTC-USD@depth5",  // Event type
  "data": {
      "symbol": "BTC-USD",  // Trading pair
      "bids": [
            {
              "p": "121592.4",
              "a": "0.385715",
              "v": "469.0"
            },
            {
              "p": "121592.3",
              "a": "0.003290",
              "v": "4.0"
            },
            {
              "p": "121583.9",
              "a": "0.421108",
              "v": "512.0"
            },
            {
              "p": "121583.5",
              "a": "0.031254",
              "v": "38.0"
            },
            {
              "p": "121583.1",
              "a": "0.043592",
              "v": "53.0"
            }
          ],  // Buy order book levels
      "asks": [
            {
              "p": "121603.0",
              "a": "0.053453",
              "v": "65.0"
            },
            {
              "p": "121602.6",
              "a": "0.421866",
              "v": "513.0"
            },
            {
              "p": "121599.7",
              "a": "0.898029",
              "v": "1092.0"
            },
            {
              "p": "121594.2",
              "a": "0.152145",
              "v": "185.0"
            },
            {
              "p": "121594.1",
              "a": "0.640656",
              "v": "779.0"
            }
          ],  // Sell order book levels
      "aggPrecision": "0.1",  // Aggregation precision
      "timestamp": 1760077637962  // Timestamp
    }
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USD@depth5"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-cswap-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USD@depth5"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()


   WSS
Subscribe to Best Bid and Ask
Subscribe to Best Bid and Ask
Subscription Type
Data type is <symbol>@bookTicker, e.g., BTC-USD@bookTicker
Subscription Example
{"id":"24dd0e35-56a4-4f7a-af8a-394c7060909c","reqType":"sub","dataType":"BTC-USD@bookTicker"}
subscription address
PROD
wss://open-api-cswap-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USD@bookTicker
data update
s
string
Currency pair name
e
string
Event type
T
int64
Latest trade timestamp
p
string
Latest trade price
u
int64
Trade ID
E
int64
Depth (best bid/ask) update time
b
string
Best bid price
B
int64
Best bid contract order quantity
a
string
Best ask price
A
int64
Best ask contract order quantity
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USD@bookTicker"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "dataType": "BTC-USD@bookTicker",
  "data": {
      "s": "BTC-USD",  // Currency pair name
      "e": "bookTicker",  // Event type
      "E": 1760077682526,  // Depth (best bid/ask) update time
      "u": "143721002",  // Trade ID
      "T": 1760077681684,  // Latest trade timestamp
      "p": "121576.0",  // Latest trade price
      "b": "121574.7",  // Best bid price
      "B": "106",  // Best bid contract order quantity
      "a": "121576.1",  // Best ask price
      "A": "1801"  // Best ask contract order quantity
    }
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USD@bookTicker"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-cswap-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USD@bookTicker"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()



 WSS
Subscribe to Latest Trading Pair K-Line
Subscribe to Latest Trading Pair K-Line
Subscription Type
Data type is <symbol>@kline_<interval>, e.g., BTC-USD@kline_1m
Subscription Example
{"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USD@kline_1m"}
subscription address
PROD
wss://open-api-cswap-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USDT@kline_1m
data update
t
int64
Start time of this K-line
o
string
Opening price of this K-line
c
string
Closing price of this K-line
h
string
HHighest traded price during this K-line period
l
string
Lowest traded price during this K-line period
u
int64
Number of trades during this K-line period
a
string
Quantity of currency pairs traded
s
string
Trading pair
v
string
Number of contract lots traded
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USD@kline_1m"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "timestamp": 1760077714555,
  "dataType": "BTC-USD@kline_1m",
  "data": {
      "t": 1760077680000,  // Start time of this K-line
      "o": 121576,  // Opening price of this K-line
      "c": 121521.2,  // Closing price of this K-line
      "l": 121521.2,  // Lowest traded price during this K-line period
  
      "h": 121576,  // HHighest traded price during this K-line period
  
      "a": 0.1283302,  // Quantity of currency pairs traded
      "v": 156,  // Number of contract lots traded
      "u": 34,  // Number of trades during this K-line period
      "s": "BTC-USD"  // Trading pair
    }
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USD@kline_1m"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-cswap-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USD@kline_1m"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()


                                                            WSS
Subscribe to 24-Hour Price Change
Pushes data of 24-hour price change every 1000ms
Subscription Type
dataType is <symbol>@ticker, e.g., BTC-USD@ticker
Subscription Example
{"id":"975f7385-7f28-4ef1-93af-df01cb9ebb53","reqType":"sub","dataType":"BTC-USD@ticker"}
subscription address
PROD
wss://open-api-cswap-ws.bingx.com/market
VST
subscription parameters
id
string
subscribe id
reqType
string
subscribe type
sub/unsub
dataType
string
data type
BTC-USD@ticker
data update
s
string
Currency pair name
E
int64
Millisecond timestamp
o
string
Opening price
h
string
Highest price
l
string
Lowest price
v
string
Volume
m
string
Trade amount, for coin-based: coin quantity, for USDT-based: USDT amount
q
string
Trade amount, for coin-based: USD, for USDT-based: unused
p
string
Price change
P
string
Price change percentage
c
string
Latest price
C
int64
Latest trade time
L
string
Latest trade quantity
B
string
Best bid price
b
string
Best bid quantity
A
string
Best ask price
a
string
Best ask quantity
subscribe sample
{
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "reqType": "sub",
  "dataType": "BTC-USD@ticker"
}
subscribe success sample
{
  "code": 0,
  "id": "e745cd6d-d0f6-4a70-8d5a-043e4c741b40",
  "msg": "SUCCESS",
  "timestamp": 1760066281286
}
data update sample
{
  "code": 0,
  "timestamp": 1760077808757,
  "dataType": "BTC-USD@ticker",
  "data": {
      "s": "BTC-USD",  // Currency pair name
      "E": 1760077806000,  // Millisecond timestamp
      "o": "122088.5",  // Opening price
      "h": "123748.0",  // Highest price
      "l": "119640.0",  // Lowest price
      "v": "1673445.00",  // Volume
      "m": "1377.02",  // Trade amount, for coin-based: coin quantity, for USDT-based: USDT amount
      "q": "167344500.0",  // Trade amount, for coin-based: USD, for USDT-based: unused
      "p": "-567.4",  // Price change
      "P": "-0.4600%",  // Price change percentage
      "c": "121523.3",  // Latest price
      "C": "1760077807856",  // Latest trade time
      "L": "21",  // Latest trade quantity
      "B": "121521.0",  // Best bid price
      "b": "528",  // Best bid quantity
      "A": "121523.4",  // Best ask price
      "a": "580"  // Best ask quantity
    }
}
cancel subscribe sample
{
  "id": "24dd0e35-56a4-4f7a-af8a-394c7060909c",
  "reqType": "unsub",
  "dataType": "BTC-USD@ticker"
}
error code
No Data
code demo
PythonGolangNodejsJavaC#PHP
                      
import json
import websocket
import gzip
import io
URL="wss://open-api-cswap-ws.bingx.com/market" 
CHANNEL= {"id":"e745cd6d-d0f6-4a70-8d5a-043e4c741b40","reqType":"sub","dataType":"BTC-USD@ticker"}
class Test(object):

    def __init__(self):
        self.url = URL 
        self.ws = None

    def on_open(self, ws):
        print('WebSocket connected')
                subStr = json.dumps(CHANNEL)
        ws.send(subStr)
        print("Subscribed to :",subStr)
        
    def on_data(self, ws, string, type, continue_flag):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(string), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)

    def on_message(self, ws, message):
        compressed_data = gzip.GzipFile(fileobj=io.BytesIO(message), mode='rb')
        decompressed_data = compressed_data.read()
        utf8_data = decompressed_data.decode('utf-8')
        print(utf8_data)  #this is the message you need 
        if "ping" in utf8_data:   # this is very important , if you receive 'Ping' you need to send 'pong' 
           ws.send("Pong")

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws, close_status_code, close_msg):
        print('The connection is closed!')

    def start(self):
        self.ws = websocket.WebSocketApp(
            self.url,
            on_open=self.on_open,
            on_message=self.on_message,
            # on_data=self.on_data,
            on_error=self.on_error,
            on_close=self.on_close,
        )
        self.ws.run_forever()


if __name__ == "__main__":
    test = Test()
    test.start()
                                                                                    