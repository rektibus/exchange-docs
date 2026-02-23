Introduction
Welcome to Huobi API！

This is the official Huobi API document, and will be continue updating. Huobi will also publish API announcement in advance for any API change. Please subscribe to our announcements so that you can get the latest updates.

You can click Here to view the announcements. If you want to subscribe, please click "Follow" button in the top right of the page. After login and click "Follow" again, then choose the type you want to follow. After you subscribe, the button will be changed to "Following". If you don't have any account, you need to register first in the login dialog.

How to read this document

The top of the document is the navigation menu for different API business; The language button in the top right is for different languages, it supports Chinese and English right now. The main content of each API document has three parts, the left hand side is the contents, the middle part is the document body, and the right hand side is the request and response sameple.

Below is the content for Spot API document

The first part is the overview:

Quick Start: It introduces the overall knowledge of Huobi API, and suitability for new Huobi API user
API Explorer: It introduces the API Explorer online tool, which is convenient for user to invoke and observe the API
FAQ: It lists the frequently asked questions regardless the specific API
Contact Us: It introduces how to contact us according to different subjects
The second part is detail for each API. Each API category is listed in one section, and each each section has below contents:

Introduction: It introduces notes and description for this API category
Specific API: It introduces the usage, rate limit, request, parameters and response for each API
Error Code: It lists the common error code and the description for this API category
FAQ: It lists the frequently asked questions for this API category
Quick Start
Preparation
Before you use API, you need to login the website to create API Key with proper permissions. The API key is shared for all instruments in Huobi including spot, futures, swap, options.

You can manage your API Keys here.

Every user can create at most 20 API Keys, each can be applied with either permission below:

Read permission: It is used to query the data, such as order query, trade query.
Trade permission: It is used to create order, cancel order and transfer, etc.
Withdraw permission: It is used to create withdraw order, cancel withdraw order, etc.
Please remember below information after creation:

Access Key It is used in API request

Secret Key It is used to generate the signature (only visible once after creation)

 The API Key can bind maximum 20 IP addresses (either host IP or network IP), we strongly suggest you bind IP address for security purpose. The API Key without IP binding will be expired after 90 days.
 Warning: These two keys are important to your account safety, please don't share both of them together to anyone else (including any product or person from Huobi). If you find your API Key is disposed, please remove it immediately.
SDK and Demo
SDK (Suggested)

Java | Python3 | C++ | C# | Go

Other Demos

https://github.com/huobiapi?tab=repositories

Testnet (Stopped)
The testnet has been alive for months, however the active user count is rather low and the cost is high, after considering carefully we decide to shutdown the testnet environment.

It is suggest you use live environment, which is more stable and has more liquidity.

Interface Type
There are two types of interface, you can choose the proper one according to your scenario and preferences.

REST API
REST (Representational State Transfer) is one of the most popular communication mechanism under HTTP, each URL represents a type of resource.

It is suggested to use Rest API for one-off operation, like trading and withdraw.

WebSocket API
WebSocket is a new protocol in HTML5. It is full-duplex between client and server. The connection can be established by a single handshake, and then server can push the notification to client actively.

It is suggest to use WebSocket API to get data update, like market data and order update.

Authentication

Both API has two levels of authentication:

Public API: It is for basic information and market data. It doesn't need authentication.

Private API: It is for account related operation like trading and account management. Each private API must be authenticated with API Key.

Access URLs
You can compare the network latency between two domain api.huobi.pro and api-aws.huobi.pro, and then choose the better one for you.

In general, the domain api-aws.huobi.pro is optimized for AWS client, the latency will be lower.

REST API

https://api.huobi.pro

https://api-aws.huobi.pro

Websocket Feed (market data except MBP incremental)

wss://api.huobi.pro/ws

wss://api-aws.huobi.pro/ws

Websocket Feed (market data only MBP incremental)

wss://api.huobi.pro/feed

wss://api-aws.huobi.pro/feed

Websocket Feed (account and order)

wss://api.huobi.pro/ws/v2

wss://api-aws.huobi.pro/ws/v2

 Please initiate API calls with non-China IP.
 It is not recommended to use proxy to access Huobi API because it will introduce high latency and low stability.
 It is recommended to access Huobi API from AWS Japan for better stability. If your server is in China mainland, it may be not stable.
Authentication
Overview
The API request may be tampered during internet, therefore all private API must be signed by your API Key (Secrete Key).

Each API Key has permission property, please check the API permission, and make sure your API key has proper permission.

A valid request consists of below parts:

API Path: for example api.huobi.pro/v1/order/orders
API Access Key: The 'Access Key' in your API Key
Signature Method: The Hash method that is used to sign, it uses HmacSHA256
Signature Version: The version for the signature protocol, it uses 2
Timestamp: The UTC time when the request is sent, e.g. 2017-05-11T16:22:06. It is useful to prevent the request to be intercepted by third-party.
Parameters: Each API Method has a group of parameters, you can refer to detailed document for each of them.
For GET request, all the parameters must be signed.
For POST request, the parameters needn't be signed and they should be put in request body.
Signature: The value after signed, it is guarantee the signature is valid and the request is not be tempered.
Signature Method
The signature may be different if the request text is different, therefore the request should be normalized before signing. Below signing steps take the order query as an example:

This is a full URL to query one order:

https://api.huobi.pro/v1/order/orders?

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

&SignatureMethod=HmacSHA256

&SignatureVersion=2

&Timestamp=2017-05-11T15:19:30

&order-id=1234567890

1. The request Method (GET or POST, WebSocket use GET), append line break "\n"

GET\n

2. The host with lower case, append line break "\n"

Example: api.huobi.pro\n

3. The path, append line break "\n"

For example, query orders:

/v1/order/orders\n

For example, WebSocket v2

/ws/v2

4. The parameters are URL encoded, and ordered based on ASCII

For example below is the original parameters:

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

order-id=1234567890

SignatureMethod=HmacSHA256

SignatureVersion=2

Timestamp=2017-05-11T15%3A19%3A30

 Use UTF-8 encoding and URL encoded, the hex must be upper case. For example, The semicolon ':' should be encoded as '%3A', The space should be encoded as '%20'.
 The 'timestamp' should be formated as 'YYYY-MM-DDThh:mm:ss' and URL encoded. The value is valid within 5 minutes.
Then above parameter should be ordered like below:

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

SignatureMethod=HmacSHA256

SignatureVersion=2

Timestamp=2017-05-11T15%3A19%3A30

order-id=1234567890

5. Use char "&" to concatenate all parameters

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30&order-id=1234567890

6. Assemble the pre-signed text

GET\n

api.huobi.pro\n

/v1/order/orders\n

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30&order-id=1234567890

7. Use the pre-signed text and your Secret Key to generate a signature

Use the pre-signed text in step 6 and your API Secret Key to generate hash code by HmacSHA256 hash function.
Encode the hash code with base-64 to generate the signature.
4F65x5A2bLyMWVQj3Aqp+B4w+ivaA7n5Oi2SuYtCJ9o=

8. Put the signature into request URL

For Rest interface:

Put all the parameters in the URL
Encode signature by URL encoding and append in the URL with parameter name "Signature".
Finally, the request sent to API should be:

https://api.huobi.pro/v1/order/orders?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&order-id=1234567890&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30&Signature=4F65x5A2bLyMWVQj3Aqp%2BB4w%2BivaA7n5Oi2SuYtCJ9o%3D

For WebSocket interface:

Fill the value according to required JSON schema
The value in JSON doesn't require URL encode
For example:

{ "action": "req", "ch": "auth", "params": { "authType":"api", "accessKey": "e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx", "signatureMethod": "HmacSHA256", "signatureVersion": "2.1", "timestamp": "2019-09-01T18:16:16", "signature": "4F65x5A2bLyMWVQj3Aqp+B4w+ivaA7n5Oi2SuYtCJ9o=" } }

Sub User
Sub user can be used to isolate the assets and trade, the assets can be transferred between parent and sub users. Sub user can only trade with the sub user. The assets can not be transferred between sub users, only parent user has the transfer permission.

Sub user has independent login password and API Key, they are managed under parent user in website.

Each parent user can create 200 sub user, each sub user can create at most 5 API Key, each API key can have two permissions: read and trade.

The sub user API Key can also bind IP address, the expiry policy is the same with parent user.

You can access here to create and manage sub user.

The sub user can access all public API (including basic information and market data), below are the private APIs that sub user can access:

API	Description
POST /v1/order/orders/place	Create and execute an order
POST /v1/order/orders/{order-id}/submitcancel	Cancel an order
POST /v1/order/orders/submitCancelClientOrder	Cancel an Order based on client order ID
POST /v1/order/orders/batchcancel	Cancel multiple orders
POST /v1/order/orders/batchCancelOpenOrders	Cancel the open orders
GET /v1/order/orders/{order-id}	Query a specific order
GET /v1/order/orders	Query orders with criteria
GET /v1/order/openOrders	Query open orders
GET /v1/order/matchresults	Query the order matching result
GET /v1/order/orders/{order-id}/matchresults	Query a specific order matching result
GET /v1/account/accounts	Query all accounts in current user
GET /v1/account/accounts/{account-id}/balance	Query the specific account balance
POST /v1/futures/transfer	Transfer with future account
POST /v1/dw/transfer-in/margin	Transfer from spot to margin account
POST /v1/dw/transfer-out/margin	Transfer from margin to spot account
POST /v1/margin/orders	Request margin loan
POST /v1/margin/orders/{order-id}/repay	Repay the debit for specific order
GET /v1/margin/loan-orders	Query history loan orders
GET /v1/margin/accounts/balance	Query margin account balance
GET /v1/account/history	Query account history
POST /v1/cross-margin/transfer-in	Transfer Asset from Spot Trading Account to Cross Margin Account
POST /v1/cross-margin/transfer-out	Transfer Asset from Cross Margin Account to Spot Trading Account
GET /v1/cross-margin/loan-info	Get Loan Interest Rate and Quota
POST /v1/cross-margin/orders	Request a Margin Loan
POST /v1/cross-margin/orders/{order-id}/repay	Repay Margin Loan
GET /v1/cross-margin/loan-orders	Search Past Margin Orders
GET /v1/cross-margin/accounts/balance	Get the Balance of the Margin Loan Account
GET /v2/account/ledger	Query account ledger
POST /v1/account/transfer	Asset Transfer
GET /v2/point/account	Query Point Balance
POST /v2/point/transfer	Point Transfer
GET /v2/etp/reference	Get reference data of ETP
POST /v2/etp/creation	ETP Creation
POST /v2/etp/redemption	ETP Redemption
GET /v2/etp/transactions	Get ETP Creation & Redemption History
GET /v2/etp/transaction	Get Specific ETP Creation or Redemption Record
GET /v2/etp/rebalance	Get Position Rebalance History
 All other APIs couldn't be accessed by sub user, otherwise the API will return "error-code 403"。
Glossary
Trading symbols
The trading symbols are consist of base currency and quote currency. Take the symbol BTC/USDT as an example, BTC is the base currency, and USDT is the quote currency.

Account
The account-id defines the Identity for different business type, it can be retrieved from API /v1/account/accounts , where the account-type is the business types. The types include:

spot: Spot account
otc: OTC account
margin: Isolated margin account, the detailed currency type is defined in subType
super-margin / cross-margin: Cross-margin account
investment: c2c margin lending account
borrow: c2c margin borrowing account
point: Point card account
minepool: Minepool account
etf: ETF account
You can refer to Huobi Course to get detailed information

API Access
Overview
Category	URL Path	Description
Common	/v1/common/*	Common interface, including currency, currency pair, timestamp, etc
Market Data	/market/*	Market data interface, including trading, depth, quotation, etc
Account	/v1/account/* /v1/subuser/*	Account interface, including account information, sub-user ,etc
Order	/v1/order/*	Order interface, including order creation, cancellation, query, etc
Margin	/v1/margin/*	Margin interface, including debit, payment, query, etc
Cross Margin	/v1/cross-margin/*	Cross margin interface, including debit, payment, query, etc
Above is a general category, it doesn't cover all API, you can refer to detailed API document according to your requirement.

New Version Rate limit Rule
The new version rate limit is applied on UID basis, which means, the overall access rate, from all API keys under same UID, to single endpoint, shouldn’t exceed the rate limit applied on that endpoint.

It is suggested to read HTTP Header X-HB-RateLimit-Requests-Remain and X-HB-RateLimit-Requests-Expire to get the remaining count of request and the expire time for current rate limit time window, then you can adjust the API access rate dynamically.

Request Format
The API is restful and there are two method: GET and POST.

GET request: All parameters are included in URL, and do not carry body(content-length>0), in otherwise will return 403 error code.
POST request: All parameters are formatted as JSON and put int the request body
Response Format
The response is JSON format.There are four fields in the top level: status, ch, ts and data. The first three fields indicate the general status, the business data is is under data field.

Below is an example of response:

{
  "status": "ok",
  "ch": "market.btcusdt.kline.1day",
  "ts": 1499223904680,
  "data": // per API response data in nested JSON object
}
Field	Data Type	Description
status	string	Status of API response
ch	string	The data stream. It may be empty as some API doesn't have data stream
ts	int	The UTC timestamp when API respond, the unit is millisecond
data	object	The body data in response
Data Type
The JSON data type described in this document is defined as below:

string: a sequence of characters that are quoted
int: a 32-bit integer, mainly used for status code, size and count
long: a 64-bit integer, mainly used for Id and timestamp
float: a fraction represented in decimal format, mainly used for volume and price, recommend to use high precision decimal data types in program
Best Practice
Security
It is strongly suggested to bind your IP with your API Key to ensure that your API Key can only be used in your machine. Furthermore, your API Key will be expired after 90 days if it is not binded with any IP.
It is strongly suggested not to share your API Key with any body or third-party software, otherwise your personal information and asset may be stolen. If your expose your API Key by accident, please do delete the API Key and create a new one.
General
API Access

It is suggested not to use temporary domain or proxy, which may be not stable.
It is suggested to use AWS Japan to access API for lower latency
It is suggested to connect to domain api-aws.huobi.pro if your server is based on AWS, because this domain is optimized for AWS client, the latency will be lower.
New Version Rate limit Rule

Only those endpoints marked with rate limit value separately are applied with new rate limit rule.

It is suggested to read HTTP Header X-HB-RateLimit-Requests-Remain and X-HB-RateLimit-Requests-Expire to get the remaining count of request and the expire time for current rate limit time window, then you can adjust the API access rate dynamically.

The overall access rate, from all API keys under same UID, to single endpoint, shouldn’t exceed the rate limit applied on that endpoint.

Market
Market data

It is suggested to use WebSocket interface to subscribe the market update and then cache the data locally, because WebSocket notification has lower latency and not have rate limit.
It is suggested not to subscribe too many topics in a single websocket connection, it may generate more notifications and cause network latency and disconnection.
Latest trade

It is suggested to subscribe WebSocket topic market.$symbol.trade.detail, the response field price represents the latest price, and it has lower latency.
It is suggested to use tradeId to de-duplicate if you subscribe WebSocket topic market.$symbol.trade.detail.
Depth

It is suggested to subscribe WebSocket topic market.$symbol.bbo if you only need the best bid and best offer.
It is suggested to subscribe WebSocket topic market.$symbol.depth.$type if you need multiple bid and offer with normal latency.
It is suggested to subscribe WebSocket topic market.$symbol.mbp.$level if you need multiple bid and offer with lower latency
It is suggested to use version field to de-duplicate and discard the smaller data if you use Rest interface /market/depth and WebSocket topic market.$symbol.depth.$type. It is suggest to use seqNum to de-duplicate and discard the smaller data if yo subscribe WebSocket topic market.$symbol.mbp.$levels.
Order
Place an order (/v1/order/orders/place)

It is suggested to follow the symbol reference (/v1/common/symbols) to validate the amount and value before placing the older, otherwise you may place an invalid order and waste your time.
It is suggested to provide an unique client-order-id field when placing the order, it is useful to track your orders status if you fail to get the order id response. Later you can use the client-order-id to match the WebSocket order notification or query order detail by interface /v1/order/orders/getClientOrder.The uniqueness of the clientOrderId passed in when you place an order will no longer be verified. We recommend you to manage clientOrderId by yourself to ensure its uniqueness. If multiple orders use the same clientOrderId, the latest order corresponding to the clientOrderId will be returned when querying/canceling an order.
Search history olders (/v1/order/orders)

It is recommended to use start-time and end-time to query, that are two timestamps with 13 digits (millisecond). The maximum query time window is 48 hours (2 days), the more precision you provide, the better performance you will get. You can query for multiple iterations.
Order update

It is suggested to subscribe WebSocket topic orders.$symbol, which has lower latency and more accurate sequence.
Account
Asset update

It is suggested to subscribe both WebSocket topic orders.$symbol and account.update#${mode}. The former one tells the order status update and arrives earlier than the latter one, and the latter one confirms the final asset balance.
It is suggested not to subscribe WebSocket topic accounts, which is replaced by accounts.update#${mode}, and will be retired later.
API Explorer
API Explorer allows user to invoke and observe each API request and response without writing any program. The UI is designed as the same as document, which has input parameters and response description, user can use it easily without any additional user guide.

This Explorer encapsulates a shared API Key, and will show the signature calcuation steps and request parameters when it invokes API. If you encounter signature problem, you can copy the API Key and timestamp to your program and compare with the result in Explorer.

Frequently Asked Questions
This section lists the frequently asked questions regardless the specific API, such as network, signature or common errors.

For specific API question, please check the Error Code and FAQ in each API category.

Q1：What is UID and account-id?
UID is the unique ID for a user (including master user and sub user), it can be found in Web or App personal information part, or retrieved from API GET /v2/user/uid.

The account-id defines the identity for different account type under one user, it can be retrieved from API /v1/account/accounts , where the account-type is the account types.

The types include but not limited to below types, contract account types (futures/swap/option) are not included:

spot: Spot account
otc: OTC account
margin: Isolated margin account, the detailed currency type is defined in subType
super-margin / cross-margin: Cross-margin account
investment: c2c margin lending account
borrow: c2c margin borrowing account
point: Point card account
minepool: Minepool account
etf: ETF account
Q2：How many API Keys one user can apply?
Every user can create 20 API Keys, and each API Key can be granted with 3 permissions: read, trade and withdraw.

Each user could create up to 200 sub users, and each sub user could create 20 API Keys, each API key can be granted with 2 permissions: read and trade.

Below are the explanation for permissions:

Read permission: It is used to query data, for example, query orders, query trades.
Trade permission: it is used to place order, cancel order and transfer.
Withdraw permission: it is used to withdraw, cancel withdraw.
Q3：Why APIs are always disconnected or timeout?
Please follow below suggestions:

It is unstable if the client's server locates in China mainland, it is suggested to invoke API from a server at AWS Japan.
It is suggested to invoke API only to host api.huobi.pro or api-was.huobi.pro.
Q4：Why the WebSocket is often disconnected?
Please check below possible reasons:

The client didn't respond 'Pong'. It is requird to respond 'Pong' after receive 'Ping' from server.
The server didn't receive 'Pong' successfully due to network issue.
The connection is broken due to network issue.
It is suggested to implement WebSocket re-connect mechanism. If Ping/Pong works well but the connection is broken, the application should be able to re-connect automatically.
Q5：What is the difference between api.huobi.pro and api-aws.huobi.pro?
The host api-aws.huobi.pro is optimized for AWS client, the latency is lower.

Q6：Why the signature authentication always fail?
Please check whether you follow below rules:

1.The parameter in signature text should be ordered by ASCII, for example below is the original parameters:

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

order-id=1234567890

SignatureMethod=HmacSHA256

SignatureVersion=2

Timestamp=2017-05-11T15%3A19%3A30

They should be ordered like below:

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

SignatureMethod=HmacSHA256

SignatureVersion=2

Timestamp=2017-05-11T15%3A19%3A30

order-id=1234567890

2.The signature text should be URL encoded, for example

The semicolon :should be encoded as %3A, The space should be encoded as %20.
The timestamp should be formatted as YYYY-MM-DDThh:mm:ss and after encoded it should be like 2017-05-11T15%3A19%3A30
3.The signature should be base64 encoded.

4.The parameter for Get request should be included in signature request.

5.The Timestamp should be UTC time and the format should be YYYY-MM-DDTHH:mm:ss.

6.The time difference between your timestamp and standard should be less than 1 minute.

7.The message body doesn't need URL encoded if you are using WebSocket for authentication.

8.The host in signature text should be the same as the host in your API request.

The proxy may change the request host, you can try without proxy;

Some http/websocket library may include port in the host, you can try to append port in signature host, like "api.huobi.pro:443"

9.The hidden text in API Key and Secret Key may have impact on the signature.

10.Check the byte[] is directly to be Base64 encoded after generated from the HmacSHA256 signature, instead of hexadecimal string to be Base64 encoded.

Right now the official SDK supports multiple languages, you can refer to the signature implementation, or below three signature examples.

JAVA signature example | C++ signature example | Python signature example

Q7：Why the API return 'Incorrect Access Key'?
Please check whether Access Key is wrong in URL request, such as:

The AccessKeyId is not included in URL parameter
The length of AccessKey is wrong
The AccessKey is already deleted
The URL request is not assembled correctly which cause AccessKey is parsed unexpected in server side.
Q8：Why the API return 'gateway-internal-error'?
Please check below possible reasons:

It may be due to network issue or server internal error, please try again later.
The data format should be correct (standard JSON).
The Content-Type in POST header should be application/json .
Q9：Why the API return 'login-required'?
Please check below possible reasons:

The URL request parameter should include AccessKeyId.
The URL request parameter should include Signature.
Q10: Why the API return HTTP 405 'method-not-allowed'?
It indicates the request path doesn't exist, please check the path spelling carefully. Due to the Nginx setting, the request path is case sensitive, please follow the path definition in document.

Contact Us
Market Maker Program
It is very welcome for market maker who has good market making strategy and large trading volume. If your Huobi Spot account or Contract account has at least 10 BTC, you can send your email to:

Vip@global-hgroup.com for Huobi(spot / leverage) market maker
Vip@global-hgroup.com for Huobi Contract market maker
And provide below details:

UID (not linked to any rebate program in any accounts)
Screenshot of trading volume in other transaction platform (such as trading volume within 30 days, or VIP status)
A brief description of your market-making strategy
 Market makers will not be able to use point cards, VIP rate, rebate or any other fee promotion.
Technical Support
If you have any other questions on API, you can contact us by below ways:

Join official Telegram group: API技术交流群01
Contact customer support from Help Center or send email to support@huobigroup.com.
If you encounter API errors, please use below template in your feedback:

1. Problem description
2. UID, Account Id and Order Id (if related with account and order)
3. Raw URL request
4. Raw JSON request (if any)
5. Raw JSON response
6. Problem time and frequency (such as, when this problem occurs, whether it is reproducible)
7. Pre-signed text (Required for authentication issue)

Below is an example：

1. Problem description: API authentication error
2. UID：123456
3. Raw URL request: https://api.huobi.pro/v1/account/accounts?&SignatureVersion=2&SignatureMethod=HmacSHA256&Timestamp=2019-11-06T03%3A25%3A39&AccessKeyId=rfhxxxxx-950000847-boooooo3-432c0&Signature=HhJwApXKpaLPewiYLczwfLkoTPnFPHgyF61iq0iTFF8%3D
4. Raw JSON request: N/A
5. Raw JSON response：{"status":"error","err-code":"api-signature-not-valid","err-msg":"Signature not valid: Incorrect Access key [Access key错误]","data":null}
6. Problem time and frequency: It occurs every time
7. Pre-signed text:
GET\n
api.huobi.pro\n
/v1/account/accounts\n
AccessKeyId=rfhxxxxx-950000847-boooooo3-432c0&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2019-11-06T03%3A26%3A13

Note：It is safe to share your Access Key, which is to prove your identity, and it will not affect your account safety. Remember do not share your Secret Key to any one. If you expose your Secret Key by accident, please remove the related API Key immediately.

Reference Data
Introduction
Reference data APIs provide public reference information such as system status, market status, symbol info, currency info, chain info and server timestamp.

Get system status
This endpoint allows users to get system status, Incidents and planned maintenance.

The system status can also be obtained through email, SMS, webhook, RSS/Atom feed. Users can click here to subscribe. The subscription function depends on Google services. Before you subscribe, please ensure that you can access Google services normally.

curl "https://status.huobigroup.com/api/v2/summary.json"
HTTP Request
GET https://status.huobigroup.com/api/v2/summary.json
Request Parameters
No parameter is available for this endpoint.

Response:

{
  "page": {  // Basic information of huobi spot status page
    "id": "p0qjfl24znv5",  // page id
    "name": "Huobi",  // page name
    "url": "https://status.huobigroup.com", // page url
    "time_zone": "Etc/UTC", // time zone
    "updated_at": "2020-02-07T10:25:14.717Z" // page update time
  },
  "components": [  // System components and their status
    {
      "id": "h028tnzw1n5l",  // component id
      "name": "Deposit", // component name
      "status": "operational", // component status
      "created_at": "2019-12-05T02:07:12.372Z",  // component create time
      "updated_at": "2020-02-07T09:27:15.563Z", // component update time
      "position": 1,
      "description": null,
      "showcase": true,
      "group_id": "gtd0nyr3pf0k",
      "page_id": "p0qjfl24znv5",
      "group": false,
      "only_show_if_degraded": false
    }
  ],
  "incidents": [ // System fault incidents and their status
        {
            "id": "rclfxz2g21ly",  // incident id
            "name": "Market data is delayed",  // incident name
            "status": "investigating",  // incident status
            "created_at": "2020-02-11T03:15:01.913Z",  // incident created time
            "updated_at": "2020-02-11T03:15:02.003Z",   // incident updated time
            "monitoring_at": null,
            "resolved_at": null,
            "impact": "minor",  // incident impact
            "shortlink": "http://stspg.io/pkvbwp8jppf9",
            "started_at": "2020-02-11T03:15:01.906Z",
            "page_id": "p0qjfl24znv5",
            "incident_updates": [
                {
                    "id": "dwfsk5ttyvtb",
                    "status": "investigating",
                    "body": "Market data is delayed",
                    "incident_id": "rclfxz2g21ly",
                    "created_at": "2020-02-11T03:15:02.000Z",
                    "updated_at": "2020-02-11T03:15:02.000Z",
                    "display_at": "2020-02-11T03:15:02.000Z",
                    "affected_components": [
                        {
                            "code": "nctwm9tghxh6",
                            "name": "Market data",
                            "old_status": "operational",
                            "new_status": "degraded_performance"
                        }
                    ],
                    "deliver_notifications": true,
                    "custom_tweet": null,
                    "tweet_id": null
                }
            ],
            "components": [
                {
                    "id": "nctwm9tghxh6",
                    "name": "Market data",
                    "status": "degraded_performance",
                    "created_at": "2020-01-13T09:34:48.284Z",
                    "updated_at": "2020-02-11T03:15:01.951Z",
                    "position": 8,
                    "description": null,
                    "showcase": false,
                    "group_id": null,
                    "page_id": "p0qjfl24znv5",
                    "group": false,
                    "only_show_if_degraded": false
                }
            ]
        }
    ],
      "scheduled_maintenances": [  // System scheduled maintenance events and their status
        {
            "id": "k7g299zl765l", // incident id
            "name": "Schedule maintenance", // incident name
            "status": "scheduled", // incident status
            "created_at": "2020-02-11T03:16:31.481Z",  // incident create time
            "updated_at": "2020-02-11T03:16:31.530Z",  // incident update time
            "monitoring_at": null,
            "resolved_at": null,
            "impact": "maintenance",  // incident impact
            "shortlink": "http://stspg.io/md4t4ym7nytd",
            "started_at": "2020-02-11T03:16:31.474Z",
            "page_id": "p0qjfl24znv5",
            "incident_updates": [
                {
                    "id": "8whgr3rlbld8",
                    "status": "scheduled",
                    "body": "We will be undergoing scheduled maintenance during this time.",
                    "incident_id": "k7g299zl765l",
                    "created_at": "2020-02-11T03:16:31.527Z",
                    "updated_at": "2020-02-11T03:16:31.527Z",
                    "display_at": "2020-02-11T03:16:31.527Z",
                    "affected_components": [
                        {
                            "code": "h028tnzw1n5l",
                            "name": "Deposit And Withdraw - Deposit",
                            "old_status": "operational",
                            "new_status": "operational"
                        }
                    ],
                    "deliver_notifications": true,
                    "custom_tweet": null,
                    "tweet_id": null
                }
            ],
            "components": [
                {
                    "id": "h028tnzw1n5l",
                    "name": "Deposit",
                    "status": "operational",
                    "created_at": "2019-12-05T02:07:12.372Z",
                    "updated_at": "2020-02-10T12:34:52.970Z",
                    "position": 1,
                    "description": null,
                    "showcase": false,
                    "group_id": "gtd0nyr3pf0k",
                    "page_id": "p0qjfl24znv5",
                    "group": false,
                    "only_show_if_degraded": false
                }
            ],
            "scheduled_for": "2020-02-15T00:00:00.000Z",  // scheduled maintenance start time
            "scheduled_until": "2020-02-15T01:00:00.000Z"  // scheduled maintenance end time
        }
    ],
    "status": {  // The overall current status of the system
        "indicator": "minor",   // system indicator
        "description": "Partially Degraded Service"  // system description
    }
}
Response Content
Field	Data Type	Description
page		basic information of huobi spot status page
{id	string	page id
name	string	page name
url	string	page url
time_zone	string	time zone
updated_at}	string	page update time
components		System components and their status
[{id	string	component id
name	string	component name, including Order submission, Order cancellation, Deposit etc.
status	string	component status, value range: operational, degraded_performance, partial_outage, major_outage, under maintenance
created_at	string	component created time
updated_at	string	component updated time
.......}]		for details of other fields, please refer to the return example
incidents		System fault incident and their status. If there is no fault at present, it will return to null
[{id	string	incident id
name	string	incident name
status	string	incident status, value range: investigating, identified, monitoring, resolved
created_at	string	incident creat time
updated_at	string	incident update time
.......}]		for details of other fields, please refer to the return example
scheduled_maintenances		System scheduled maintenance incident and status. If there is no scheduled maintenance at present, it will return to null
[{id	string	incident id
name	string	incident name
status	string	incident staus, value range: scheduled, in progress, verifying, completed
created_at	string	incident created time
updated_at	string	incident updated time
scheduled_for	string	scheduled maintenance start time
scheduled_until	string	scheduled maintenance end time
.......}]		for details of other fields, please refer to the return example
status		The overall current status of the system
{indicator	string	system indicator, value range: none, minor, major, critical, maintenance
description}	string	system description, value range: All Systems Operational, Minor Service Outager, Partial System Outage, Partially Degraded Service, Service Under Maintenance
Get Market Status
The endpoint returns current market status
The enum values of market status includes: 1 - normal (order submission & cancellation are allowed)，2 - halted (order submission & cancellation are prohibited)，3 - cancel-only(order submission is prohibited but order cancellation is allowed).
Halt reason includes: 2 - emergency maintenance，3 - schedule maintenance.

curl "https://api.huobi.pro/v2/market-status"
HTTP Request
GET /v2/market-status
Request Parameter
None.

Responds:

{
    "code": 200,
    "message": "success",
    "data": {
        "marketStatus": 1
    }
}
Response Content
Field	Data Type	Required	Description
code	integer	TRUE	Status code
message	string	FALSE	Error message (if any)
<data>	object	TRUE	
marketStatus	integer	TRUE	Market status (1=normal, 2=halted, 3=cancel-only)
haltStartTime	long	FALSE	Halt start time (unix time in millisecond) , only valid for marketStatus=halted or cancel-only
haltEndTime	long	FALSE	Estimated halt end time (unix time in millisecond) , only valid for marketStatus=halted or cancel-only; if this field is not returned during marketStatus=halted or cancel-only, it implicates the halt end time cannot be estimated at this time.
haltReason	integer	FALSE	Halt reason (2=emergency-maintenance, 3=scheduled-maintenance) , only valid for marketStatus=halted or cancel-only
affectedSymbols	string	FALSE	Affected symbols, separated by comma. If affect all symbols just respond with value ‘all’. Only valid for marketStatus=halted or cancel-only
</data>			
Get all Supported Trading Symbol(V2)
API Key Permission：Read

GET /v2/settings/common/symbols
Request Parameters
Parameter	Data Type	Required	Description
ts	long	false	timestamp to get incremental data
Note
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".
response

{
    "status":"ok",
    "data":[
        {
            "tags": "",
            "state": "online",
            "wr": "1.5",
            "sc": "ethusdt",
            "p": [
                {
                    "id": 9,
                    "name": "Grayscale",
                    "weight": 91
                }
            ],
            "bcdn": "ETH",
            "qcdn": "USDT",
            "elr": null,
            "tpp": 2,
            "tap": 4,
            "fp": 8,
            "smlr": null,
            "flr": null,
            "whe": false,
            "cd": false,
            "te": true,
            "sp": "main",
            "d": null,
            "bc": "eth",
            "qc": "usdt",
            "toa": 1514779200000,
            "ttp": 8,
            "w": 999400000,
            "lr": 5,
            "dn": "ETH/USDT"
        }
    ],
    "ts":"1641870869718",
    "full":1
}
Response Content
Parameter	Full Name	Data Type	Description
status	status	string	status
data	<data>	Object	
sc	symbol_code	string	symbol(outside)
dn	display_name	string	display name
si	state_isolated	string	Leverage status of symbol：online，offline
scr	state_cross	string	Full leverage status of symbol ：online，offline
bc	base_currency	string	base currency
bcdn	base_currency_display_name	string	base currency display name
qc	quote_currency	string	quote currency
qcdn	quote_currency_display_name	string	quote currency display name
state	state	string	symbol status. unknown，not-online，pre-online，online，suspend，offline，transfer-board，fuse
whe	white_enabled	boolean	white enabled
cd	country_disabled	boolean	country disabled
te	trade_enabled	boolean	trade enabled
toa	trade_open_at	long	the time trade open at
sp	symbol_partition	string	symbol partition
w	weight	int	weight sort
ttp	trade_total_precision	decimal(10,6)	trade total precision
tap	trade_amount_precision	decimal(10,6)	trade amount precision
tpp	trade_price_precision	decimal(10,6)	trade price precision
fp	fee_precision	decimal(10,6)	fee precision
suspend_desc	suspend_desc	string	suspend desc
transfer_board_desc	transfer_board_desc	string	transfer board desc
tags	tags	string	Tags, multiple tags are separated by commas, such as: st, hadax
lr	leverage_ratio	decimal	leverage ratio, such as: 3.5, or null if the symbol does not support this leverage ratio
smlr	super_margin_leverage_ratio	decimal	super-margin leverage ratio, such as: 3, or null if the symbol does not support super-margin
flr	funding_leverage_ratio	String	C2C leverage ratio, such as:3, or null if the symbol does not support C2C
wr	withdraw_risk	string	withdraw_risk, such as: 3, or null if the symbol does not support super-margin
d	direction	int	direction: 1 for long and 2 for short
elr	etp_leverage_ratio	string	etp leverage ratio
p	partitions	Object	
castate	ca state	string	not Required. The state of the call auction; it will only be displayed when it is in the 1st and 2nd stage of the call auction. Enumeration values: "ca_1", "ca_2"
ca1oa	ca1 open at	long	not Required. this information is only available for that symbols configured with call auction. The total number of milliseconds since 0:0:0:00,000 on January 1, 1970 UTC to the present.
ca2oa	ca2 open at	long	not Required. this information is only available for that symbols configured with call auction. The total number of milliseconds since 0:0:0:00,000 on January 1, 1970 UTC to the present.
</data>			
ts	ts	String	timestamp of incremental data
full	full	int	full data flag: 0 for no and 1 for yes
err_code	err_code	string	error code(returned when the interface reports an error)
err_msg	err_msg	string	error msg(returned when the interface reports an error)
Get all Supported Currencies(V2)
API Key Permission：Read

GET /v2/settings/common/currencies
Request Parameters
Parameter	Data Type	Required	Description
ts	long	false	timestamp to get incremental data
Note
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".
response

{
    "status":"ok",
    "data":[
        {
            "tags":"",
            "cawt":false,
            "fc":12,
            "sc":12,
            "dma":"1",
            "wma":"10",
            "ft":"eth",
            "whe":false,
            "cd":false,
            "qc":true,
            "sp":"8",
            "wp":6,
            "fn":"Tether USDT",
            "at":1,
            "cc":"usdt",
            "v":true,
            "de":true,
            "wed":true,
            "w":10006,
            "state":"online",
            "dn":"USDT",
            "dd":"Please don’t deposit any other digital assets except USDT to the above address. Otherwise, you may lose your assets permanently. !>_<!Depositing to the above address requires confirmations of the entire network. It will arrive after 12 confirmations, and it will be available to withdraw after 12 confirmations. !>_<!Minimum deposit amount: 1 USDT. Any deposits less than the minimum will not be credited or refunded.!>_<!Your deposit address won’t change often. If there are any changes, we will notify you via announcement or email.!>_<!Please make sure that your computer and browser are secure and your information is protected from being tampered or leaked.",
            "svd":null,
            "swd":null,
            "sdd":null,
            "wd":"Minimum withdrawal amount: 10 USDT (ERC20). !>_<!To ensure the safety of your funds, your withdrawal request will be manually reviewed if your security strategy or password is changed. Please wait for phone calls or emails from our staff.!>_<!Please make sure that your computer and browser are secure and your information is protected from being tampered or leaked."
        }
    ],
    "ts":"1641869938436",
    "full":1
}
Response Content
Parameter	Full Name	Data Type	Description
status	status	string	status
data	<data>	Object	
cc	currency_code	string	currency code
dn	display_name	string	currency display name
fn	full-name	string	currency full name
at	asset_type	int	asset type, 1 virtual currency 2 fiat currency
wp	withdraw_precision	int	withdraw precision
ft	fee_type	string	fee type, eth: Fixed fee, btc: Interval fee husd: Fee charged in proportion
dma	deposit_min_amount	string	deposit min amount
wma	withdraw_min_amount	string	withdraw min amount
sp	show_precision	string	show precision
w	weight	string	weight
qc	quote_currency	boolean	be quote currency
state	state	string	symbol state. unkown, not-online, online, offline
v	visible	boolean	visible or not -- users who have offline currency but have assets can see it
whe	white_enabled	boolean	white enabled
cd	country_disabled	boolean	country disabled--users who have country disabled currency but have assets can see it
de	deposit_enabled	boolean	deposit enabled
wed	withdraw_enabled	boolean	withdraw enabled
cawt	currency_addr_with_tag	boolean	currency addr with tag
fc	fast_confirms	int	fast confirms
sc	safe_confirms	int	safe confirms
swd	suspend_withdraw_desc	string	suspend withdraw desc
wd	withdraw_desc	string	withdraw desc
sdd	suspend_deposit_desc	string	suspend deposit desc
dd	deposit_desc	string	deposit desc
svd	suspend_visible_desc	string	suspend visible desc
tags	tags	string	Tags, multiple tags are separated by commas, such as: st, hadax
</data>			
ts	ts	String	timestamp of incremental data
full	full	int	full data flag: 0 for no and 1 for yes
err_code	err_code	string	error code(returned when the interface reports an error)
err_msg	err_msg	string	error msg(returned when the interface reports an error)
Get Currencys Settings
API Key Permission：Read

GET /v1/settings/common/currencys
Request Parameters
Parameter	Data Type	Required	Description
ts	long	false	timestamp to get incremental data
Note
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".
response

{
    "status":"ok",
    "data":[
        {
            "tags":"",
            "name":"usdt",
            "state":"online",
            "cawt":false,
            "fc":12,
            "sc":12,
            "sp":"8",
            "iqc":true,
            "ct":"eth",
            "de":true,
            "we":true,
            "cd":false,
            "oe":1,
            "v":true,
            "whe":false,
            "wet":1609430400000,
            "det":1609430400000,
            "cp":"all",
            "vat":1508839200000,
            "ss":[
                "INSTITUTION",
                "MINEPOOL",
                "OTC"
            ],
            "fn":"Tether USDT",
            "wp":6,
            "w":10006,
            "dma":"1",
            "wma":"10",
            "dn":"USDT",
            "dd":"Please don’t deposit any other digital assets except USDT to the above address. Otherwise, you may lose your assets permanently. !>_<!Depositing to the above address requires confirmations of the entire network. It will arrive after 12 confirmations, and it will be available to withdraw after 12 confirmations. !>_<!Minimum deposit amount: 1 USDT. Any deposits less than the minimum will not be credited or refunded.!>_<!Your deposit address won’t change often. If there are any changes, we will notify you via announcement or email.!>_<!Please make sure that your computer and browser are secure and your information is protected from being tampered or leaked.",
            "svd":null,
            "swd":null,
            "sdd":null,
            "wd":"Minimum withdrawal amount: 10 USDT (ERC20). !>_<!To ensure the safety of your funds, your withdrawal request will be manually reviewed if your security strategy or password is changed. Please wait for phone calls or emails from our staff.!>_<!Please make sure that your computer and browser are secure and your information is protected from being tampered or leaked."
        }
    ],
    "ts":"1641872721891",
    "full":1
}
Response Content
Parameter	Full Name	Data Type	Description
status	status	string	status
data	<data>	Object	
name	name	string	currency name
dn	display-name	string	currency display name
vat	visible-assets-timestamp	long	visible assets timestamp
det	deposit-enable-timestamp	long	deposit enable timestamp
wet	withdraw-enable-timestamp	long	withdraw enable timestamp
wp	withdraw-precision	int	withdraw precision
ct	currency-type	string	currency type
cp	currency-partition	string	currency partition. INVALID, all(PRO and HADAX), pro, hadax
ss	support-sites	array	support sites. unknown, otc, futures(coin-m futures), minepool( not supports mulan), institution, swap(coin-m swap), asset(mulan does not support transfer, it is only used for reconciliation, cfd(cfd contract in Japan), chat(Huobi Chat IM), option, linear-swap(usdt-m), custody(funding account in HK), turbine, margin, super-margin
oe	otc-enable	integer	0: disable, 1: enable
dma	deposit-min-amount	string	deposit min amount
wma	withdraw-min-amount	string	withdraw min amount
sp	show-precision	string	show precision
w	weight	string	weight
qc	quote-currency	boolean	be quote currency
state	state	string	currency state. unkown, not-online, online, offline
v	visible	boolean	visible
whe	white-enabled	boolean	white enabled
cd	country-disabled	boolean	country disabled
de	deposit-enabled	boolean	deposit enabled
we	withdraw-enabled	boolean	withdraw enabled
cawt	currency-addr-with-tag	boolean	currency addr with tag
cao	currency-addr-oneoff	boolean	currency addr oneoff
fc	fast-confirms	int	fast confirms
sc	safe-confirms	int	safe confirms
swd	suspend-withdraw-desc	string	suspend withdraw desc
wd	withdraw-desc	string	withdraw desc
sdd	suspend-deposit-desc	string	suspend deposit desc
dd	deposit-desc	string	deposit desc
svd	suspend-visible-desc	string	suspend visible desc
tags	tags	string	Tags, multiple tags are separated by commas, such as: st, hadax
fn	full-name	string	currency full name
bc	block-chains		
iqc	is-quote-currency		
</data>			
ts	ts	String	timestamp of incremental data
full	full	int	full data flag: 0 for no and 1 for yes
err-code	err-code	string	error code(returned when the interface reports an error)
err-msg	err-msg	string	error msg(returned when the interface reports an error)
Get Symbols Setting
API Key Permission：Read

GET /v1/settings/common/symbols
Request Parameters
Parameter	Data Type	Required	Description
ts	long	false	timestamp to get incremental data
Note
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".
response

{
    "status":"ok",
    "data":[
        {
            "symbol":"agldusdt",
            "tags":"",
            "state":"online",
            "bcdn":"AGLD",
            "qcdn":"USDT",
            "elr":null,
            "tm":"PRO",
            "sn":"AGLD/USDT",
            "ve":true,
            "dl":false,
            "te":true,
            "ce":true,
            "cd":false,
            "tet":1630668600000,
            "we":false,
            "toa":1630668600000,
            "tca":1893470400000,
            "voa":1630666800000,
            "vca":1893470400000,
            "bc":"agld",
            "qc":"usdt",
            "sp":"innovation",
            "d":null,
            "tpp":4,
            "tap":4,
            "fp":8,
            "w":950000000,
            "ttp":8
        }
    ],
    "ts":"1641880066563",
    "full":1
}
Response Content
Parameter	Full Name	Data Type	Description
status	status	string	status
data	<data>	Object	
symbol	symbol	string	symbol(outside)
sn	symbol-name	string	symbol name
bc	base-currency	string	base currency
qc	quote-currency	string	quote currency
state	state	string	symbol status. unknown，not-online，pre-online，online，suspend，offline，transfer-board，fuse
ve	visible-enabled	boolean	visible
we	white-enabled	boolean	white enabled
dl	delist	boolean	delist
cd	country-disabled	boolean	country disabled
te	trade-enabled	boolean	trade enabled
ce	cancel-enabled	boolean	cancel enabled
tet	trade-enable-timestamp	long	trade enable timestamp
toa	trade-open-at	long	the time trade open at
tca	trade-close-at	long	the time trade close at
voa	visible-open-at	long	visible open at
vca	visible-close-at	long	visible close at
sp	symbol-partition	string	symbol partition
tm	trade-market	string	symbol partition
w	weight	int	weight sort
ttp	trade-total-precision	decimal(10,6)	trade total precision
tap	trade-amount-precision	decimal(10,6)	trade amount precision
tpp	trade-price-precision	decimal(10,6)	trade price precision
fp	fee-precision	decimal(10,6)	fee precision
tags	tags	string	Tags, multiple tags are separated by commas, such as: st, hadax
d	direction		
bcdn	base_currency_display_name	string	base currency display name
qcdn	quote_currency_display_name	string	quote currency display name
elr	etp_leverage_ratio	string	etp leverage ratio
castate	ca state	string	Not required. The state of the call auction; it will only be displayed when it is in the 1st and 2nd stage of the call auction. Enumeration values: "ca_1", "ca_2"
ca1oa	ca1 open at	long	not Required. the open time of call auction phase 1, total milliseconds since January 1, 1970 0:0:0:00ms UTC
ca1ca	ca1 close at	long	not Required. the close time of call auction phase 1, total milliseconds since January 1, 1970 0:0:0:00ms UTC
ca2oa	ca2 open at	long	not Required. the open time of call auction phase 2, total milliseconds since January 1, 1970 0:0:0:00ms UTC
ca2ca	ca2 close at	long	not Required. the close time of call auction phase 2, total milliseconds since January 1, 1970 0:0:0:00ms UTC
</data>			
ts	ts	String	timestamp of incremental data
full	full	int	full data flag: 0 for no and 1 for yes
err-code	err-code	string	error code(returned when the interface reports an error)
err-msg	err-msg	string	error msg(returned when the interface reports an error)
Get Market Symbols Setting
API Key Permission：Read

GET /v1/settings/common/market-symbols
Request Parameters
Parameter	Data Type	Required	Description
symbols	string	false	symbols. NA means all symbols, multiple symbols separated with comma
ts	long	false	timestamp to get incremental data
Note
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".
response

{
    "status":"ok",
    "data":[
        {
            "symbol":"btc3lusdt",
            "state":"online",
            "bc":"btc3l",
            "qc":"usdt",
            "pp":4,
            "ap":4,
            "sp":"main",
            "vp":8,
            "minoa":0.01,
            "maxoa":199.0515,
            "minov":5,
            "lominoa":0.01,
            "lomaxoa":199.0515,
            "lomaxba":199.0515,
            "lomaxsa":199.0515,
            "smminoa":0.01,
            "blmlt":1.1,
            "slmgt":0.9,
            "smmaxoa":199.0515,
            "bmmaxov":2500,
            "msormlt":0.1,
            "mbormlt":0.1,
            "maxov":2500,
            "u":"btcusdt",
            "mfr":0.035,
            "ct":"23:55:00",
            "rt":"00:00:00",
            "rthr":4,
            "in":16.3568,
            "at":"enabled",
            "tags":"etp,nav,holdinglimit,activities"
        }
    ],
    "ts":"1641880897191",
    "full":1
}
Response Content
Parameter	Full Name	Data Type	Description
status	status	string	status
data	<data>	Object	
symbol	symbol	string	symbol(outside)
bc	base-currency	string	base currency
qc	quote-currency	string	quote currency
state	state	string	symbol status. unknown，not-online，pre-online，online，suspend，offline，transfer-board，fuse
sp	symbol-partition	string	symbol partition
tags	tags	string	Tags, multiple tags are separated by commas, such as: st, hadax
lr	leverage_ratio	decimal	leverage ratio of margin symbol, provided by Global
smlr	super_margin_leverage_ratio	decimal	leverage ratio of super-margin symbol, provided by Global
pp	price-precision	integer	price precision
ap	amount-precision	integer	amount precision
vp	value-precision	integer	value precision
minoa	min-order-amt	decimal	min order amount
maxoa	max-order-amt	decimal	max order amount
minov	min-order-value	decimal	min order value
lominoa	limit-order-min-order-amt	decimal	min amount of limit price order
lomaxoa	limit-order-max-order-amt	decimal	max amount of limit price order
lomaxba	limit-order-max-buy-amt	decimal	max amount of limit price buy order
lomaxsa	limit-order-max-sell-amt	decimal	max amount of limit price sell order
smminoa	sell-market-min-order-amt	decimal	min amount of market price sell order
smmaxoa	sell-market-max-order-amt	decimal	max amount of market price sell order
bmmaxov	buy-market-max-order-value	decimal	max amount of market price buy order
blmlt	buy-limit-must-less-than	decimal(10,6)	Buy limit must less than
slmgt	sell-limit-must-greater-than	decimal(10,6)	Sell limit must greater than
msormlt	market-sell-order-rate-must-less-than	decimal(10,6)	Market sell order rate must less than
mbormlt	market-buy-order-rate-must-less-than	decimal(10,6)	Market buy order rate must less than
at	api-trading	string	trading by api interface
u	underlying	string	ETP: symbol
mfr	mgmt-fee-rate	decimal	
ct	charge-time	string	charge time(unix time in millisecond, just for symbols of ETP)
rt	rebal-time	string	rebal time(unix time in millisecond, just for symbols of ETP)
rthr	rebal-threshold	decimal	rebal threshold(just for symbols of ETP)
in	init-nav	decimal	ETP: init nav
maxov	max-order-value	decimal	max value of market price order
flr	funding-leverage-ratio	decimal	C2C: funding leverage ratio
castate	ca state	string	not Required. The state of the call auction; it will only be displayed when it is in the 1st and 2nd stage of the call auction. Enumeration values: "ca_1", "ca_2"
</data>			
ts	ts	String	timestamp of incremental data
full	full	int	full data flag: 0 for no and 1 for yes
err-code	err-code	string	error code(returned when the interface reports an error)
err-msg	err-msg	string	error msg(returned when the interface reports an error)
Get Chains Information
API Key Permission：Read

GET /v1/settings/common/chains
Request Parameters
Parameter	Data Type	Required	Description
show-desc	string	false	show desc, 0: no, 1: all, 2: suspend deposit/withdrawal and chain exchange
currency	string	false	currency
ts	long	false	timestamp to get incremental data
Note
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".
response

{
    "status": "ok",
    "data": [
        {
            "chain": "hrc20nft",
            "currency": "nft",
            "code": "hrc20nft",
            "ct": "live",
            "ac": "eth",
            "default": 0,
            "dma": "160298",
            "wma": "160298",
            "de": true,
            "we": true,
            "wp": 6,
            "ft": "eth",
            "dn": "HECO",
            "fn": "",
            "awt": false,
            "adt": false,
            "ao": false,
            "fc": 10,
            "sc": 20,
            "v": true,
            "sda": "",
            "swa": "",
            "deposit-tips-desc": "Minimum deposit amount:160298\nAny deposits less than the minimum amount will not be credited or refunded.",
            "withdraw-desc": "Minimum withdrawal amount: 160298 NFT(HECO). !>_<!To ensure the safety of your funds, your withdrawal request will be manually reviewed if your security strategy or password is changed. Please wait for phone calls or emails from our staff.!>_<!Please make sure that your computer and browser are secure and your information is protected from being tampered or leaked.",
            "suspend-deposit-desc": "",
            "suspend-withdraw-desc": "",
            "replace-chain-info-desc": "",
            "replace-chain-notification-desc": "",
            "replace-chain-popup-desc": ""
        }
    ],
    "ts": "1641880897191",
    "full": 1
}
Response Content
Parameter	Full Name	Data Type	Description
status	status	string	status
data	<data>	Object	
adt	addr-deposit-tag	boolean	has addr deposit tag
ac	address-chain	string	address of chain
ao	addr-oneoff	boolean	addr oneoff
awt	addr-with-tag	boolean	addr with tag
chain	chain	string	chain name
ct	chain-type	string	chain type. plain, live, old, new, legal, tooold
code	code	string	obsolete, please to use chain
currency	currency	string	currency
deposit-desc	deposit-desc	string	deposit desc
de	deposit-enable	boolean	deposit enable
dma	deposit-min-amount	string	deposit-min-amount, if the amount is less than this amount will be: 1. The small amount will exceed the deposit-min-amount and then be credited 2. The small amount will not be accumulated and will never be credited to the account
deposit-tips-desc	deposit-tips-desc	string	deposit tips desc
dn	display-name	string	display name, general be upper
fc	fast-confirms	integer	fast-confirms, when height of the exchange node to that chain tail is greater than this number, the deposit and withdrawal will be not settled to the user account, this deposit order is regarded as an unsafe deposit, and the available amount in the withdrawal and account transfer must be excluded that amount from this order.
ft	fee-type	string	fee type
default	is-default	integer	is default
replace-chain-info-desc	replace-chain-info-desc	string	replace chain info desc
replace-chain-notification-desc	replace-chain-notification-desc	string	replace chain notification desc
replace-chain-popup-desc	replace-chain-popup-desc	string	replace chain popup desc
sc	safe-confirms	integer	safe confirms, When the distance between the height of the current exchange's chain node and the chain tail is greater than this number, the asset management DW will mark this order as a safe deposit, and it will be regarded as the available amount when withdrawing and transferring funds.
sda	suspend-deposit-announcement	string	suspend deposit announcement
suspend-deposit-desc	suspend-deposit-desc	string	suspend deposit desc
swa	suspend-withdraw-announcement	string	suspend withdraw announcement
suspend-withdraw-desc	suspend-withdraw-desc	string	suspend withdraw desc
v	visible	boolean	visible
withdraw-desc	withdraw-desc	string	withdraw desc
we	withdraw-enable	boolean	withdraw enable
wma	withdraw-min-amount	string	withdraw min amount, refused to withdraw if less than this amount
wp	withdraw-precision	integer	withdraw precision, refused to withdraw if greater than this amount
fn	full-name	string	
withdraw-tips-desc	withdraw-tips-desc	string	withdraw tips desc
suspend-visible-desc	suspend-visible-desc	string	suspend visible desc
</data>			
ts	ts	String	timestamp of incremental data
full	full	int	full data flag: 0 for no and 1 for yes
err-code	err-code	string	error code(returned when the interface reports an error)
err-msg	err-msg	string	error msg(returned when the interface reports an error)
APIv2 - Currency & Chains
API user could query static reference information for each currency, as well as its corresponding chain(s). (Public Endpoint)

HTTP Request
GET /v2/reference/currencies
curl "https://api.huobi.pro/v2/reference/currencies?currency=usdt"
Request Parameters
Field Name	Required	Data Type	Description	Value Range
currency	false	string	Currency	btc, ltc, bch, eth, etc ...(available currencies in Huobi)
authorizedUser	false	boolean	Authorized user	true or false (if not filled, default value is true)
Response:

{
    "code":200,
    "data":[
        {
            "chains":[
                {
                    "chain":"trc20usdt",
                    "displayName":"",
                    "baseChain": "TRX",
                    "baseChainProtocol": "TRC20",
                    "isDynamic": false,
                    "depositStatus":"allowed",
                    "maxTransactFeeWithdraw":"1.00000000",
                    "maxWithdrawAmt":"280000.00000000",
                    "minDepositAmt":"100",
                    "minTransactFeeWithdraw":"0.10000000",
                    "minWithdrawAmt":"0.01",
                    "numOfConfirmations":999,
                    "numOfFastConfirmations":999,
                    "withdrawFeeType":"circulated",
                    "withdrawPrecision":5,
                    "withdrawQuotaPerDay":"280000.00000000",
                    "withdrawQuotaPerYear":"2800000.00000000",
                    "withdrawQuotaTotal":"2800000.00000000",
                    "withdrawStatus":"allowed"
                },
                {
                    "chain":"usdt",
                    "displayName":"",
                    "baseChain": "BTC",
                    "baseChainProtocol": "OMNI",
                    "isDynamic": false,
                    "depositStatus":"allowed",
                    "maxWithdrawAmt":"19000.00000000",
                    "minDepositAmt":"0.0001",
                    "minWithdrawAmt":"2",
                    "numOfConfirmations":30,
                    "numOfFastConfirmations":15,
                    "transactFeeRateWithdraw":"0.00100000",
                    "withdrawFeeType":"ratio",
                    "withdrawPrecision":7,
                    "withdrawQuotaPerDay":"90000.00000000",
                    "withdrawQuotaPerYear":"111000.00000000",
                    "withdrawQuotaTotal":"1110000.00000000",
                    "withdrawStatus":"allowed"
                },
                {
                    "chain":"usdterc20",
                    "displayName":"",
                    "baseChain": "ETH",
                    "baseChainProtocol": "ERC20",
                    "isDynamic": false,
                    "depositStatus":"allowed",
                    "maxWithdrawAmt":"18000.00000000",
                    "minDepositAmt":"100",
                    "minWithdrawAmt":"1",
                    "numOfConfirmations":999,
                    "numOfFastConfirmations":999,
                    "transactFeeWithdraw":"0.10000000",
                    "withdrawFeeType":"fixed",
                    "withdrawPrecision":6,
                    "withdrawQuotaPerDay":"180000.00000000",
                    "withdrawQuotaPerYear":"200000.00000000",
                    "withdrawQuotaTotal":"300000.00000000",
                    "withdrawStatus":"allowed"
                }
            ],
            "currency":"usdt",
            "instStatus":"normal"
        }
    ]
}

Response Content
Field Name	Required	Data Type	Description	Value Range
code	true	int	Status code	
message	false	string	Error message (if any)	
<data>	true	object		
currency	true	string	Currency	
<chains>	true	object		
chain	true	string	Chain name	
displayName	true	string	Chain display name	
baseChain	false	string	Base chain name	
baseChainProtocol	false	string	Base chain protocol	
isDynamic	false	boolean	Is dynamic fee type or not (only applicable to withdrawFeeType = fixed)	true,false
numOfConfirmations	true	int	Number of confirmations required for deposit success (trading & withdrawal allowed once reached)	
numOfFastConfirmations	true	int	Number of confirmations required for quick success (trading allowed but withdrawal disallowed once reached)	
minDepositAmt	true	string	Minimal deposit amount in each request	
depositStatus	true	string	Deposit status	allowed,prohibited
minWithdrawAmt	true	string	Minimal withdraw amount in each request	
maxWithdrawAmt	true	string	Maximum withdraw amount in each request	
withdrawQuotaPerDay	true	string	Maximum withdraw amount in a day (Singapore timezone)	
withdrawQuotaPerYear	true	string	Maximum withdraw amount in a year	
withdrawQuotaTotal	true	string	Maximum withdraw amount in total	
withdrawPrecision	true	int	Withdraw amount precision	
withdrawFeeType	true	string	Type of withdraw fee (only one type can be applied to each currency)	fixed,circulated,ratio
transactFeeWithdraw	false	string	Withdraw fee in each request (only applicable to withdrawFeeType = fixed)	
minTransactFeeWithdraw	false	string	Minimal withdraw fee in each request (only applicable to withdrawFeeType = circulated or ratio)	
maxTransactFeeWithdraw	false	string	Maximum withdraw fee in each request (only applicable to withdrawFeeType = circulated or ratio)	
transactFeeRateWithdraw	false	string	Withdraw fee in each request (only applicable to withdrawFeeType = ratio)	
withdrawStatus	true	string	Withdraw status	allowed,prohibited
</data>				
instStatus	true	string	Instrument status	normal,delisted
</chains>				
Status Code
Status Code	Error Message	Scenario
200	success	Request successful
500	error	System error
2002	invalid field value in "field name"	Invalid field value
Get Current Timestamp
This endpoint returns the current timestamp, i.e. the number of milliseconds that have elapsed since 00:00:00 UTC on 1 January 1970.

curl "https://api.huobi.pro/v1/common/timestamp"
HTTP Request
GET /v1/common/timestamp
Request Parameters
No parameter is needed for this endpoint.

Response:

{
    "status":"ok",
    "data":1629715504949
}
Response Content
参数名称	是否必须	类型	描述	取值范围
status	true	string	Request Processing Result	
data	true	long	current system timestamp	
Market Data
Introduction
Market data APIs provide public market information such as varies of candlestick, depth and trade information.

The market data is updated once per second.

Get Klines(Candles)
This endpoint retrieves all klines in a specific range.

HTTP Request
GET /market/history/kline
curl "https://api.huobi.pro/market/history/kline?period=1day&size=200&symbol=btcusdt"
Query Parameters
Parameter	Data Type	Required	Default	Description	Value Range
symbol	string	true	NA	The trading symbol to query	All trading symbol supported, e.g. btcusdt, bccbtcn (to retrieve candlesticks for ETP NAV, symbol = ETP trading symbol + suffix 'nav'，for example: btc3lusdtnav)
period	string	true	NA	The period of each candle	1min, 5min, 15min, 30min, 60min, 4hour, 1day, 1mon, 1week, 1year
size	integer	false	150	The number of data returns	[1-2000]
This API doesn't support customized period, refer to Websocket K line API to get the emurated period value.
To query HB10, put "hb10" at symbol position.
The start time for candlesticks is based on Singapore time (GMT+8), for example, the duration for daily candlesticks is from 00:00:00 to 23:59:59 Singapore time.
The above command returns JSON structured like this:

{
    "ch": "market.btcusdt.kline.5min",
    "status": "ok",
    "ts": 1629769247172,
    "data": [
        {
            "id": 1629769200,
            "open": 49056.37,
            "close": 49025.51,
            "low": 49022.86,
            "high": 49056.38,
            "amount": 3.946281917950917,
            "vol": 193489.67275732,
            "count": 196
        },
        {
            "id": 1629768900,
            "open": 48994.61,
            "close": 49056.37,
            "low": 48966.72,
            "high": 49072.46,
            "amount": 30.72223099519689,
            "vol": 1505870.732227976,
            "count": 1504
        }
    ]
}
Response Content
Field	Data Type	Description
status	string	Request Processing Result "ok","error"
ch	string	Data belonged channel，Format：market.$symbol.kline.$period
ts	long	Time of Respond Generation, Unit: Millisecond
<data>	object	
id	long	The UNIX timestamp in seconds as response id
amount	float	Accumulated trading volume, in base currency
count	integer	The number of completed trades
open	float	The opening price
close	float	The closing price
low	float	The low price
high	float	The high price
vol	float	Accumulated trading value, in quote currency
</data>		
Get Latest Aggregated Ticker
This endpoint retrieves the latest ticker with some important 24h aggregated market data.

HTTP Request
GET /market/detail/merged
curl "https://api.huobi.pro/market/detail/merged?symbol=ethusdt"
Request Parameters
Parameter	Data Type	Required	Default	Description	Value Range
symbol	string	true	NA	The trading symbol to query	All supported trading symbol, e.g. btcusdt, bccbtc.Refer to /v1/common/symbols
The above command returns JSON structured like this:

{
    "ch": "market.btcusdt.detail.merged",
    "status": "ok",
    "ts": 1629788763750,
    "tick": {
        "id": 272156789143,
        "version": 272156789143,
        "open": 50080.0,
        "close": 49820.92,
        "low": 48767.0,
        "high": 50500.0,
        "amount": 12055.365781937457,
        "vol": 5.985618685709001E8,
        "count": 420573,
        "bid": [
            49819.48,
            2.58112
        ],
        "ask": [
            49819.49,
            0.002411
        ]
    }
}
Response Content
Field	Data Type	Description
status	string	Request Processing Result "ok","error"
ch	string	Data belonged channel，Format：market.$symbol.detail.merged
ts	long	Time of Respond Generation, Unit: Millisecond
<tick>	object	
id	long	The internal identity
amount	float	Accumulated trading volume of last 24 hours (rotating 24h), in base currency
count	integer	The number of completed trades (rotating 24h)
open	float	The opening price of last 24 hours (rotating 24h)
close	float	The last price of last 24 hours (rotating 24h)
low	float	The lowest price of last 24 hours (rotating 24h)
high	float	The highest price of last 24 hours (rotating 24h)
vol	float	Accumulated trading value of last 24 hours (rotating 24h), in quote currency
bid	object	The current best bid in format [price, size]
ask	object	The current best ask in format [price, size]
</tick>		
Get Latest Tickers for All Pairs
This endpoint retrieves the latest tickers for all supported pairs.

The returned data object can contain large amount of tickers.
HTTP Request
GET /market/tickers
curl "https://api.huobi.pro/market/tickers"
Request Parameters
No parameters are needed for this endpoint.

The above command returns JSON structured like this:

{
    "status":"ok",
    "ts":1629789355531,
    "data":[
        {
            "symbol":"smtusdt",
            "open":0.004659,
            "high":0.004696,
            "low":0.0046,
            "close":0.00468,
            "amount":36551302.17544405,
            "vol":170526.0643855023,
            "count":1709,
            "bid":0.004651,
            "bidSize":54300.341,
            "ask":0.004679,
            "askSize":1923.4879
        },
        {
            "symbol":"ltcht",
            "open":12.795626,
            "high":12.918053,
            "low":12.568926,
            "close":12.918053,
            "amount":1131.801675005825,
            "vol":14506.9381937385,
            "count":923,
            "bid":12.912687,
            "bidSize":0.1068,
            "ask":12.927032,
            "askSize":5.3228
        }
    ]
}
Response Content
Response content is an array of object, each object has below fields.

Field	Data Type	Description
status	string	Request Processing Result "ok","error"
ts	long	Time of Respond Generation, Unit: Millisecond
<data>	object	
amount	float	The aggregated trading volume in last 24 hours (rotating 24h)
count	integer	The number of completed trades of last 24 hours (rotating 24h)
open	float	The opening price of a nature day (Singapore time)
close	float	The closing price of a nature day (Singapore time)
low	float	The lowest price of a nature day (Singapore time)
high	float	The highest price of a nature day (Singapore time)
vol	float	The aggregated trading value in last 24 hours (rotating 24h)
symbol	string	The trading symbol of this object, e.g. btcusdt, bccbtc
bid	float	Best bid price
bidSize	float	Best bid size
ask	float	Best ask price
askSize	float	Best ask size
</data>		
Get Market Depth
This endpoint retrieves the current order book of a specific pair.

HTTP Request
GET /market/depth
curl "https://api.huobi.pro/market/depth?symbol=btcusdt&type=step0"
Request Parameters
Parameter	Data Type	Required	Default Value	Description	Value Range
symbol	string	true	NA	The trading symbol to query	Refer to GET /v1/common/symbols
depth	integer	false	20	The number of market depth to return on each side	5, 10, 20
type	string	true	step0	Market depth aggregation level, details below	step0, step1, step2, step3, step4, step5
when type is set to "step0", the default value of "depth" is 150 instead of 20.
"type" Details

Value	Description
step0	No market depth aggregation
step1	Aggregation level = precision*10
step2	Aggregation level = precision*100
step3	Aggregation level = precision*1000
step4	Aggregation level = precision*10000
step5	Aggregation level = precision*100000
The above command returns JSON structured like this:

{
    "ch": "market.btcusdt.depth.step0",
    "status": "ok",
    "ts": 1629790438801,
    "tick": {
        "ts": 1629790438215,
        "version": 136107114472,
        "bids": [
            [
                49790.87,
                0.779876
            ],
            [
                49785.9,
                1.82E-4
            ],
            [
                49784.48,
                0.002758
            ],
            [
                49784.29,
                0.05
            ],
            [
                49783.06,
                0.005038
            ]
        ],
        "asks": [
            [
                49790.88,
                2.980472
            ],
            [
                49790.89,
                0.006613
            ],
            [
                49792.16,
                0.080302
            ],
            [
                49792.67,
                0.030112
            ],
            [
                49793.23,
                0.043103
            ]
        ]
    }
}
Response Content
The returned data object is under 'tick' object instead of 'data' object in the top level JSON
Field	Data Type	Description
status	string	Request Processing Result "ok","error"
ch	string	Data belonged channel，Format： market.$symbol.depth.$type
ts	long	Time of Respond Generation, Unit: Millisecond
<tick>	object	
ts	integer	The UNIX timestamp in milliseconds is adjusted to Singapore time
version	integer	Internal data
bids	object	The current all bids in format [price, size]
asks	object	The current all asks in format [price, size]
</tick>		
Get the Last Trade
This endpoint retrieves the latest trade with its price, volume, and direction.

HTTP Request
GET /market/trade
curl "https://api.huobi.pro/market/trade?symbol=ethusdt"
Request Parameters
Parameter	Data Type	Required	Default Value	Description	Value Range
symbol	string	true	NA	The trading symbol to query	Refer to GET /v1/common/symbols
The above command returns JSON structured like this:

{
    "ch": "market.btcusdt.trade.detail",
    "status": "ok",
    "ts": 1629792192037,
    "tick": {
        "id": 136107843051,
        "ts": 1629792191928,
        "data": [
            {
                "id": 136107843051348400221001656,
                "ts": 1629792191928,
                "trade-id": 102517374388,
                "amount": 0.028416,
                "price": 49806.0,
                "direction": "buy"
            },
            {
                "id": 136107843051348400229813302,
                "ts": 1629792191928,
                "trade-id": 102517374387,
                "amount": 0.025794,
                "price": 49806.0,
                "direction": "buy"
            }
        ]
    }
}
Response Content
The returned data object is under 'tick' object instead of 'data' object in the top level JSON
Parameter	Data Type	Description
status	string	Request Processing Result "ok","error"
ch	string	Data belonged channel，Format：market.$symbol.trade.detail
ts	long	Time of Respond Generation, Unit: Millisecond
<tick>	object	
id	long	global transaction ID
ts	long	Latest Creation Time
<data>	object	
id	integer	The unique trade id of this trade (to be obsoleted)
trade-id	integer	The unique trade id (NEW)
amount	float	The trading volume in base currency
price	float	The trading price in quote currency
ts	integer	The UNIX timestamp in milliseconds adjusted to Singapore time
direction	string	The direction of the taker trade: 'buy' or 'sell'
</data>		
</tick>		
Get the Most Recent Trades
This endpoint retrieves the most recent trades with their price, volume, and direction.

HTTP Request
GET /market/history/trade
curl "https://api.huobi.pro/market/history/trade?symbol=ethusdt&size=2"
Request Parameters
Parameter	Data Type	Required	Default Value	Description	Value Range
symbol	string	true	NA	The trading symbol to query	All supported trading symbol, e.g. btcusdt, bccbtc.Refer to GET /v1/common/symbols
size	integer	false	1	The number of data returns	[1-2000]
The above command returns JSON structured like this:

{
    "ch": "market.btcusdt.trade.detail",
    "status": "ok",
    "ts": 1629793657842,
    "data": [
        {
            "id": 136108764379,
            "ts": 1629793656939,
            "data": [
                {
                    "id": 136108764379348400430265987,
                    "ts": 1629793656939,
                    "trade-id": 102517381182,
                    "amount": 1.24E-4,
                    "price": 49656.4,
                    "direction": "buy"
                }
            ]
        },
        {
            "id": 136108763320,
            "ts": 1629793656198,
            "data": [
                {
                    "id": 136108763320348400439066863,
                    "ts": 1629793656198,
                    "trade-id": 102517381181,
                    "amount": 0.01125,
                    "price": 49655.0,
                    "direction": "buy"
                },
                {
                    "id": 136108763320348400429773626,
                    "ts": 1629793656198,
                    "trade-id": 102517381180,
                    "amount": 8.3E-4,
                    "price": 49651.35,
                    "direction": "buy"
                }
            ]
        }
    ]
}
Response Content
The returned data object is an array which represents one recent timestamp; each timestamp object again is an array which represents all trades occurred at this timestamp.
Field	Data Type	Description
status	string	Request Processing Result "ok","error"
ch	string	Data belonged channel，Format：market.$symbol.trade.detail
ts	long	Time of Respond Generation, Unit: Millisecond
<data>	object	
id	long	global transaction ID
ts	long	Latest Creation Time
<data>	object	
id	integer	The unique trade id of this trade (to be obsoleted)
trade-id	integer	The unique trade id (NEW)
amount	float	The trading volume in base currency
price	float	The trading price in quote currency
ts	integer	The UNIX timestamp in milliseconds adjusted to Singapore time
direction	string	The direction of the taker trade: 'buy' or 'sell'
</data>		
</data>		
Get the Last 24h Market Summary
This endpoint retrieves the summary of trading in the market for the last 24 hours.

It is possible that the accumulated volume and the accumulated value counted for current 24h window is smaller than the previous ones.
HTTP Request
GET /market/detail/
curl "https://api.huobi.pro/market/detail?symbol=ethusdt"
Request Parameters
Parameter	Data Type	Required	Default Value	Description	Value Range
symbol	string	true	NA	The trading symbol to query	Refer to /v1/common/symbols
The above command returns JSON structured like this:

{
    "ch": "market.btcusdt.detail",
    "status": "ok",
    "ts": 1629795484817,
    "tick": {
        "id": 272164011416,
        "low": 48767.0,
        "high": 50500.0,
        "open": 50266.89,
        "close": 49728.71,
        "vol": 6.010379336834868E8,
        "amount": 12110.642402972368,
        "version": 272164011416,
        "count": 420452
    }
}
Response Content
The returned data object is under 'tick' object instead of 'data' object in the top level JSON
Field	Data Type	Description
status	string	Request Processing Result "ok","error"
ch	string	Data belonged channel，Format： market.$symbol.detail
ts	long	Time of Respond Generation, Unit: Millisecond
<tick>	object	
id	integer	The internal identity
amount	float	The aggregated trading volume in USDT of last 24 hours (rotating 24h)
count	integer	The number of completed trades of last 24 hours (rotating 24h)
open	float	The opening price of last 24 hours (rotating 24h)
close	float	The closing price of last 24 hours (rotating 24h)
low	float	The lowest price of last 24 hours (rotating 24h)
high	float	The highest price of last 24 hours (rotating 24h)
vol	float	The trading volume in base currency of last 24 hours (rotating 24h)
version	integer	Internal data
</tick>		
Error Code
Below is the error code, error message and description returned by Market data APIs.

Error Code	Error Message	Description
invalid-parameter	invalid symbol	Parameter symbol is invalid
invalid-parameter	invalid period	Parameter period is invalid for candlestick data
invalid-parameter	invalid depth	Parameter depth is invalid for depth data
invalid-parameter	invalid type	Parameter type is invalid
invalid-parameter	invalid size	Parameter size is invalid
invalid-parameter	invalid size,valid range: [1, 2000]	Parameter size range is invalid
invalid-parameter	request timeout	Request timeout please try again
Account
Introduction
Account APIs provide account related (such as basic info, balance, history, point) query and transfer functionality.

All endpoints in this section require authentication
Get all Accounts of the Current User
API Key Permission：Read
Rate Limit (NEW): 100times/2s

This endpoint returns a list of accounts owned by this API user.

HTTP Request
GET /v1/account/accounts
Request Parameters
No parameter is available for this endpoint
The above command returns JSON structured like this:

{
    "status": "ok",
    "data": [
        {
            "id": 10000001,
            "type": "spot",
            "subtype": "",
            "state": "working"
        },
        {
            "id": 10000002,
            "type": "otc",
            "subtype": "",
            "state": "working"
        },
        {
            "id": 10000003,
            "type": "point",
            "subtype": "",
            "state": "working"
        }
    ]
}
Response Content
Field	Data Type	Description	Value Range
status	true	string	Request Processing Result
<data>	true	object	
id	integer	Unique account id	NA
state	string	Account state	working, lock
type	string	The type of this account	spot, margin, otc, point, super-margin, investment, borrow, grid-trading, deposit-earning, otc-options
subtype	string	The type of sub account (applicable only for isolated margin accout)	The corresponding trading symbol (currency pair) the isolated margin is based on, e.g. btcusdt
</data>	true	object	
Margin/super-margin/borrow account will only be created after the initial incoming asset transfer.
