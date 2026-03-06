here are two types of interface, you can choose the proper one according to your scenario and preferences.

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
It is not recommended to use proxy to access HTX API because it will introduce high latency and low stability.
It is recommended to access HTX API from AWS Japan for better stability. If your server is in China mainland, it may be not stable.

Overview
The API request may be tampered during internet, therefore all private API must be signed by your API Key (Secrete Key).

Each API Key has permission property, please check the API permission, and make sure your API key has proper permission.

A valid request consists of below parts:

API Path: for example api.huobi.pro/v1/order/orders
API Access Key: The 'Access Key' in your API Key
Signature Method: The first one is for users to use the elliptic curve digital signature algorithm, using Ed25519. ‌The second, hash-based protocol for user-computed signatures, uses HmacSHA256.
Ed25519 introduction: It is a high-performance digital signature algorithm that provides fast signature verification and generation while having high security.
Signature Version: The version for the signature protocol, it uses 2
Timestamp: The UTC time when the request is sent, e.g. 2017-05-11T16:22:06. It is useful to prevent the request to be intercepted by third-party.
Parameters: Each API Method has a group of parameters, you can refer to detailed document for each of them.
For GET request, all the parameters must be signed.
For POST request, the parameters needn't be signed and they should be put in request body.
Signature: The value after signed, it is guarantee the signature is valid and the request is not be tempered.
 
Ed25519 Signature Method
The signature may be different if the request text is different, therefore the request should be normalized before signing. Below signing steps take the order query as an example:

This is a full URL to query one order:

https://api.huobi.pro/v1/order/orders?

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

&SignatureMethod=Ed25519

&SignatureVersion=2

&Timestamp=2017-05-11T15:19:30

&order-id=1234567890

1. The request Method (GET or POST, WebSocket use GET), append line break "\n"

GET\n

2. The host with lower case, append line break "\n"

Example:api.huobi.pro\n

3. The path, append line break "\n"

For example, query orders:

/v1/order/orders\n

For example, WebSocket v2

/ws/v2

4. The parameters are URL encoded, and ordered based on ASCII

For example below is the original parameters:

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

order-id=1234567890

SignatureMethod=Ed25519

SignatureVersion=2

Timestamp=2017-05-11T15%3A19%3A30

Use UTF-8 encoding and URL encoded, the hex must be upper case. For example, The semicolon ':' should be encoded as '%3A', The space should be encoded as '%20'.The 'timestamp' should be formated as 'YYYY-MM-DDThh:mm:ss' and URL encoded. The value is valid within 5 minutes.

Then above parameter should be ordered like below:

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx

SignatureMethod=Ed25519

SignatureVersion=2

Timestamp=2017-05-11T15%3A19%3A30

order-id=1234567890

5. Use char "&" to concatenate all parameters

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=Ed25519&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30&order-id=1234567890

6. Assemble the pre-signed text

GET\n

api.huobi.pro\n

/v1/order/orders\n

AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&SignatureMethod=HmacSHA256&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30&order-id=1234567890

7. Use the pre-signed text and your Secret Key to generate a signature

Use the request string obtained in the previous step to generate the private key of Ed25519 and add it to generate a signature.
Encode the generated signature with base-64, and the resulting value is used as the digital signature of this interface call.
4F65x5A2bLyMWVQj3Aqp+B4w+ivaA7n5Oi2SuYtCJ9o=

8. Put the signature into request URL

For Rest interface:

Put all the parameters in the URL
Encode signature by URL encoding and append in the URL with parameter name "Signature".
Finally, the request sent to API should be:

https://api.huobi.pro/v1/order/orders?AccessKeyId=e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx&order-id=1234567890&SignatureMethod=Ed25519&SignatureVersion=2&Timestamp=2017-05-11T15%3A19%3A30&Signature=4F65x5A2bLyMWVQj3Aqp%2BB4w%2BivaA7n5Oi2SuYtCJ9o%3D

For WebSocket interface:

Fill the value according to required JSON schema
The value in JSON doesn't require URL encode
For example:

{ "action": "req", "ch": "auth", "params": { "authType":"api", "accessKey": "e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx", "signatureMethod": "Ed25519", "signatureVersion": "2.1", "timestamp": "2019-09-01T18:16:16", "signature": "4F65x5A2bLyMWVQj3Aqp+B4w+ivaA7n5Oi2SuYtCJ9o=" }}

 

HmacSHA256 Signature Method
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

Example:api.huobi.pro\n

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

Use UTF-8 encoding and URL encoded, the hex must be upper case. For example, The semicolon ':' should be encoded as '%3A', The space should be encoded as '%20'.The 'timestamp' should be formated as 'YYYY-MM-DDThh:mm:ss' and URL encoded. The value is valid within 5 minutes.

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

{ "action": "req", "ch": "auth", "params": { "authType":"api", "accessKey": "e2xxxxxx-99xxxxxx-84xxxxxx-7xxxx", "signatureMethod": "HmacSHA256", "signatureVersion": "2.1", "timestamp": "2019-09-01T18:16:16", "signature": "4F65x5A2bLyMWVQj3Aqp+B4w+ivaA7n5Oi2SuYtCJ9o=" }}



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





Trading symbols
The trading symbols are consist of base currency and quote currency. Take the symbol BTC/USDT as an example, BTC is the base currency, and USDT is the quote currency.

Account
The account-id defines the Identity for different business type, it can be retrieved from API /v1/account/accounts , where the account-type is the business types.The types include:

spot: Spot account
otc: OTC account
margin: Isolated margin account, the detailed currency type is defined in subType
super-margin / cross-margin: Cross-margin account
investment: c2c margin lending account
borrow: c2c margin borrowing account
point: Point card account
minepool: Minepool account
etf: ETF account







Category	URL Path	Description
Common	/v1/common/*	Common interface, including currency, currency pair, timestamp, etc
Market Data	/market/*	Market data interface, including trading, depth, quotation, etc
Account	/v1/account/* /v1/subuser/*	Account interface, including account information, sub-user ,etc
Order	/v1/order/*	Order interface, including order creation, cancellation, query, etc
Margin	/v1/margin/*	Margin interface, including debit, payment, query, etc
Cross Margin	/v1/cross-margin/*	Cross margin interface, including debit, payment, query, etc
Above is a general category, it doesn't cover all API, you can refer to detailed API document according to your requirement.




The new version rate limit is applied on UID basis, which means, the overall access rate, from all API keys under same UID, to single endpoint, shouldn’t exceed the rate limit applied on that endpoint.

It is suggested to read HTTP Header X-HB-RateLimit-Requests-Remain and X-HB-RateLimit-Requests-Expire to get the remaining count of request and the expire time for current rate limit time window, then you can adjust the API access rate dynamically.


The API is restful and there are two method: GET and POST.

GET request: All parameters are included in URL, and do not carry body(content-length>0), in otherwise will return 403 error code.
POST request: All parameters are formatted as JSON and put int the request body




The response is JSON format.There are four fields in the top level: status, ch, ts and data. The first three fields indicate the general status, the business data is is under data field.

Below is an example of response:

{ "status": "ok", "ch": "market.btcusdt.kline.1day", "ts": 1499223904680, "data": // per API response data in nested JSON object}
Field	Data Type	Description
status	string	Status of API response
ch	string	The data stream. It may be empty as some API doesn't have data stream
ts	int	The UTC timestamp when API respond, the unit is millisecond
data	object	The body data in response


The JSON data type described in this document is defined as below:

string: a sequence of characters that are quoted
int: a 32-bit integer, mainly used for status code, size and count
long: a 64-bit integer, mainly used for Id and timestamp
float: a fraction represented in decimal format, mainly used for volume and price, recommend to use high precision decimal data types in program


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










Reference data APIs provide public reference information such as system status, market status, symbol info, currency info, chain info and server timestamp.




/v2/market-status ( Get Market Status)
Request type: GET

Signature verification: No

Interface description:  The endpoint returns current market status
The enum values of market status includes: 1 - normal (order submission & cancellation are allowed)，2 - halted (order submission & cancellation are prohibited)，3 - cancel-only(order submission is prohibited but order cancellation is allowed).
Halt reason includes: 2 - emergency maintenance，3 - schedule maintenance.

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description

No data

Notes:  
No parameters are needed for this endpoint.

Response Parameter
Parameter	Data Type	Required	Description
code	integer	 false	Status code
message	string	 false	Error message (if any)
<data>	object	 false	
marketStatus	integer	 false	Market status (1=normal, 2=halted, 3=cancel-only)
haltStartTime	long	 false	Halt start time (unix time in millisecond) , only valid for marketStatus=halted or cancel-only
haltEndTime	long	 false	Estimated halt end time (unix time in millisecond) , only valid for marketStatus=halted or cancel-only; if this field is not returned during marketStatus=halted or cancel-only, it implicates the halt end time cannot be estimated at this time.
haltReason	integer	 false	Halt reason (2=emergency-maintenance, 3=scheduled-maintenance) , only valid for marketStatus=halted or cancel-only
affectedSymbols	string	 false	Affected symbols, separated by comma. If affect all symbols just respond with value ‘all’. Only valid for marketStatus=halted or cancel-only
</data>		 false	








/v2/settings/common/symbols ( Get all Supported Trading Symbol(V2))
Request type: GET

Signature verification: No

Interface permission: Read

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description
ts	long	 false	timestamp to get incremental data
Notes: 
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".

Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	status
data	Object	 false	
si	string	 false	state_isolated
scr	string	 false	state_cross
sc	string	 false	symbol(outside)
dn	string	 false	display name
bc	string	 false	base currency
bcdn	string	 false	base currency display name
qc	string	 false	quote currency
qcdn	string	 false	quote currency display name
state	string	 false	symbol status. unknown，not-online，pre-online，online，suspend，offline，transfer-board，fuse
whe	boolean	 false	white enabled
cd	boolean	 false	country disabled
te	boolean	 false	trade enabled
toa	long	 false	the time trade open at
sp	string	 false	symbol partition
w	int	 false	weight sort
ttp	decimal(10,6)	 false	trade total precision
tap	decimal(10,6)	 false	trade amount precision
tpp	decimal(10,6)	 false	trade price precision
fp	decimal(10,6)	 false	fee precision
suspend_desc	string	 false	suspend desc
transfer_board_desc	string	 false	transfer board desc
tags	string	 false	Tags, multiple tags are separated by commas, such as: st, hadax
lr	decimal	 false	leverage ratio, such as: 3.5, or null if the symbol does not support this leverage ratio
smlr	decimal	 false	super-margin leverage ratio, such as: 3, or null if the symbol does not support super-margin.For trading pairs launched after September 15, 2020, this field does not return a value. You can query it through /v1/settings/common/market-symbols.
flr	String	 false	C2C leverage ratio, such as:3, or null if the symbol does not support C2C
wr	string	 false	withdraw_risk, such as: 3, or null if the symbol does not support super-margin
d	int	 false	direction: 1 for long and 2 for short
elr	string	 false	etp leverage ratio
p	Object	 false	
castate	string	 false	not Required. The state of the call auction; it will only be displayed when it is in the 1st and 2nd stage of the call auction. Enumeration values: "ca_1", "ca_2"
ca1oa	long	 false	not Required. this information is only available for that symbols configured with call auction. The total number of milliseconds since 0:0:0:00,000 on January 1, 1970 UTC to the present.
ca2oa	long	 false	not Required. this information is only available for that symbols configured with call auction. The total number of milliseconds since 0:0:0:00,000 on January 1, 1970 UTC to the present.
</data>		 false	
ts	String	 false	timestamp of incremental data
full	int	 false	full data flag: 0 for no and 1 for yes
err_code	string	 false	error code(returned when the interface reports an error)
err_msg	string	 false	error msg(returned when the interface reports an error)
Request example
curl”https://api.huobi.pro/v1/settings/common/symbols“
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"tags":""
"state":"online"
"wr":"1.5"
"sc":"ethusdt"
"p":[
0:{
"id":9
"name":"Grayscale"
"weight":91
}
]
"bcdn":"ETH"
"qcdn":"USDT"
"elr":NULL
"tpp":2
"tap":4
"fp":8
"smlr":NULL
"flr":NULL
"whe":false
"cd":false
"te":true
"sp":"main"
"d":NULL
"bc":"eth"
"qc":"usdt"
"toa":1514779200000
"ttp":8
"w":999400000
"lr":5
"dn":"ETH/USDT"
}
]
"ts":"1641870869718"
"full":1
}











/v2/settings/common/currencies ( Get all Supported Currencies(V2))
Request type: GET

Signature verification: No

Interface permission: Read

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description
ts	long	 false	timestamp to get incremental data
Notes: 
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".

Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	status
data	Object	 false	
cc	string	 false	currency code
dn	string	 false	currency display name
fn	string	 false	currency full name
at	int	 false	asset type, 1 virtual currency 2 fiat currency
wp	int	 false	withdraw precision
ft	string	 false	fee type, eth: Fixed fee, btc: Interval fee husd: Fee charged in proportion
dma	string	 false	deposit min amount
wma	string	 false	withdraw min amount
sp	string	 false	show precision
w	string	 false	weight
qc	boolean	 false	be quote currency
state	string	 false	symbol state. unkown, not-online, online, offline
v	boolean	 false	visible or not -- users who have offline currency but have assets can see it
whe	boolean	 false	white enabled
cd	boolean	 false	country disabled--users who have country disabled currency but have assets can see it
de	boolean	 false	deposit enabled
wed	boolean	 false	withdraw enabled
cawt	boolean	 false	currency addr with tag
fc	int	 false	fast confirms
sc	int	 false	safe confirms
swd	string	 false	suspend withdraw desc
wd	string	 false	withdraw desc
sdd	string	 false	suspend deposit desc
dd	string	 false	deposit desc
svd	string	 false	suspend visible desc
tags	string	 false	Tags, multiple tags are separated by commas, such as: st, hadax
</data>		 false	
ts	String	 false	timestamp of incremental data
full	int	 false	full data flag: 0 for no and 1 for yes
err_code	string	 false	error code(returned when the interface reports an error)
err_msg	string	 false	error msg(returned when the interface reports an error)
Request example
curl"https://api.huobi.pro/v2/settings/common/currencies"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"tags":""
"cawt":false
"fc":12
"sc":12
"dma":"1"
"wma":"10"
"ft":"eth"
"whe":false
"cd":false
"qc":true
"sp":"8"
"wp":6
"fn":"Tether USDT"
"at":1
"cc":"usdt"
"v":true
"de":true
"wed":true
"w":10006
"state":"online"
"dn":"USDT"
"dd":"Please don’t deposit any other digital assets except USDT to the above address. Otherwise, you may lose your assets permanently. !>_<!Depositing to the above address requires confirmations of the entire network. It will arrive after 12 confirmations, and it will be available to withdraw after 12 confirmations. !>_<!Minimum deposit amount: 1 USDT. Any deposits less than the minimum will not be credited or refunded.!>_<!Your deposit address won’t change often. If there are any changes, we will notify you via announcement or email.!>_<!Please make sure that your computer and browser are secure and your information is protected from being tampered or leaked."
"svd":NULL
"swd":NULL
"sdd":NULL
"wd":"Minimum withdrawal amount: 10 USDT (ERC20). !>_<!To ensure the safety of your funds, your withdrawal request will be manually reviewed if your security strategy or password is changed. Please wait for phone calls or emails from our staff.!>_<!Please make sure that your computer and browser are secure and your information is protected from being tampered or leaked."
}
]
"ts":"1641869938436"
"full":1





/v1/settings/common/currencys ( Get Currencys Settings)
Request type: GET

Signature verification: No

Interface permission: Read

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description
ts	long	 false	timestamp to get incremental data
Notes: 
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".

Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	status
<data>	Object	 false	
name	string	 false	currency name
dn	string	 false	currency display name
vat	long	 false	visible assets timestamp
det	long	 false	deposit enable timestamp
wet	long	 false	withdraw enable timestamp
wp	int	 false	withdraw precision
ct	string	 false	currency type
cp	string	 false	currency partition. INVALID, all(PRO and HADAX), pro, hadax
ss	array	 false	support sites. unknown, otc, futures(coin-m futures), minepool( not supports mulan), institution, swap(coin-m swap), asset(mulan does not support transfer, it is only used for reconciliation, cfd(cfd contract in Japan), chat(HTX Chat IM), option, linear-swap(usdt-m), custody(funding account in HK), turbine, margin, super-margin
oe	integer	 false	0: disable, 1: enable
dma	string	 false	deposit min amount
wma	string	 false	withdraw min amount
sp	string	 false	show precision
w	string	 false	weight
qc	boolean	 false	be quote currency
state	string	 false	currency state. unkown, not-online, online, offline
v	boolean	 false	visible
whe	boolean	 false	white enabled
cd	boolean	 false	country disabled
de	boolean	 false	deposit enabled
we	boolean	 false	withdraw enabled
cawt	boolean	 false	currency addr with tag
cao	boolean	 false	currency addr oneoff
fc	int	 false	fast confirms
sc	int	 false	safe confirms
swd	string	 false	suspend withdraw desc
wd	string	 false	withdraw desc
sdd	string	 false	suspend deposit desc
dd	string	 false	deposit desc
svd	string	 false	suspend visible desc
tags	string	 false	Tags, multiple tags are separated by commas, such as: st, hadax
fn	string	 false	currency full name
bc		 false	
iqc		 false	
</data>		 false	
ts	String	 false	timestamp of incremental data
full	int	 false	full data flag: 0 for no and 1 for yes
err-code	string	 false	error code(returned when the interface reports an error)
err-msg	string	 false	error msg(returned when the interface reports an error)
Request example
curl"https://api.huobi.pro/v1/settings/common/currencys"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"tags":""
"name":"usdt"
"state":"online"
"cawt":false
"fc":12
"sc":12
"sp":"8"
"iqc":true
"ct":"eth"
"de":true
"we":true
"cd":false
"oe":1
"v":true
"whe":false
"wet":1609430400000
"det":1609430400000
"cp":"all"
"vat":1508839200000
"ss":[
0:"INSTITUTION"
1:"MINEPOOL"
2:"OTC"
]
"fn":"Tether USDT"
"wp":6
"w":10006
"dma":"1"
"wma":"10"
"dn":"USDT"
"dd":"Please don’t deposit any other digital assets except USDT to the above address. Otherwise, you may lose your assets permanently. !>_<!Depositing to the above address requires confirmations of the entire network. It will arrive after 12 confirmations, and it will be available to withdraw after 12 confirmations. !>_<!Minimum deposit amount: 1 USDT. Any deposits less than the minimum will not be credited or refunded.!>_<!Your deposit address won’t change often. If there are any changes, we will notify you via announcement or email.!>_<!Please make sure that your computer and browser are secure and your information is protected from being tampered or leaked."
"svd":NULL
"swd":NULL
"sdd":NULL
"wd":"Minimum withdrawal amount: 10 USDT (ERC20). !>_<!To ensure the safety of your funds, your withdrawal request will be manually reviewed if your security strategy or password is changed. Please wait for phone calls or emails from our staff.!>_<!Please make sure that your computer and browser are secure and your information is protected from being tampered or leaked."
}
]
"ts":"1641872721891"
"full":1
}




/v1/settings/common/symbols ( Get Symbols Setting)
Request type: GET

Signature verification: No

Interface permission: Read

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description
ts	long	 false	timestamp to get incremental data
Notes: 
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".

Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	status
data	Object	 false	
symbol	string	 false	symbol(outside)
sn	string	 false	symbol name
bc	string	 false	base currency
qc	string	 false	quote currency
state	string	 false	symbol status. unknown，not-online，pre-online，online，suspend，offline，transfer-board，fuse
ve	boolean	 false	visible
we	boolean	 false	white enabled
dl	boolean	 false	delist
cd	boolean	 false	country disabled
te	boolean	 false	trade enabled
ce	boolean	 false	cancel enabled
tet	long	 false	trade enable timestamp
toa	long	 false	the time trade open at
tca	long	 false	the time trade close at
voa	long	 false	visible open at
vca	long	 false	visible close at
sp	string	 false	symbol partition
tm	string	 false	symbol partition
w	int	 false	weight sort
ttp	decimal(10,6)	 false	trade total precision
tap	decimal(10,6)	 false	trade amount precision
tpp	decimal(10,6)	 false	trade price precision
fp	decimal(10,6)	 false	fee precision
tags	string	 false	Tags, multiple tags are separated by commas, such as: st, hadax
d		 false	
bcdn	string	 false	base currency display name
qcdn	string	 false	quote currency display name
elr	string	 false	etp leverage ratio
castate	string	 false	Not required. The state of the call auction; it will only be displayed when it is in the 1st and 2nd stage of the call auction. Enumeration values: "ca_1", "ca_2"
ca1oa	long	 false	not Required. the open time of call auction phase 1, total milliseconds since January 1, 1970 0:0:0:00ms UTC
ca1ca	long	 false	not Required. the close time of call auction phase 1, total milliseconds since January 1, 1970 0:0:0:00ms UTC
ca2oa	long	 false	not Required. the open time of call auction phase 2, total milliseconds since January 1, 1970 0:0:0:00ms UTC
ca2ca	long	 false	not Required. the close time of call auction phase 2, total milliseconds since January 1, 1970 0:0:0:00ms UTC
</data>		 false	
ts	String	 false	timestamp of incremental data
full	int	 false	full data flag: 0 for no and 1 for yes
err-code	string	 false	error code(returned when the interface reports an error)
err-msg	string	 false	error msg(returned when the interface reports an error)
Request example
curl
"https://api.huobi.pro/v1/settings/common/symbols"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"symbol":"agldusdt"
"tags":""
"state":"online"
"bcdn":"AGLD"
"qcdn":"USDT"
"elr":NULL
"tm":"PRO"
"sn":"AGLD/USDT"
"ve":true
"dl":false
"te":true
"ce":true
"cd":false
"tet":1630668600000
"we":false
"toa":1630668600000
"tca":1893470400000
"voa":1630666800000
"vca":1893470400000
"bc":"agld"
"qc":"usdt"
"sp":"innovation"
"d":NULL
"tpp":4
"tap":4
"fp":8
"w":950000000
"ttp":8
}
]
"ts":"1641880066563"
"full":1






/v1/settings/common/market-symbols ( Get Market Symbols Setting)
Request type: GET

Signature verification: No

Interface permission: Read

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description
symbols	string	 false	symbols. NA means all symbols, multiple symbols separated with comma
ts	long	 false	timestamp to get incremental data
Notes: 
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".

Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	status
data	Object	 false	
symbol	string	 false	symbol(outside)
bc	string	 false	base currency
qc	string	 false	quote currency
state	string	 false	symbol status. unknown，not-online，pre-online，online，suspend，offline，transfer-board，fuse
sp	string	 false	symbol partition
tags	string	 false	Tags, multiple tags are separated by commas, such as: st, hadax
lr	decimal	 false	leverage ratio of margin symbol, provided by Global
smlr	decimal	 false	leverage ratio of super-margin symbol, provided by Global
pp	integer	 false	price precision
ap	integer	 false	amount precision
vp	integer	 false	value precision
minoa	decimal	 false	min order amount
maxoa	decimal	 false	max order amount
minov	decimal	 false	min order value
lominoa	decimal	 false	min amount of limit price order
lomaxoa	decimal	 false	max amount of limit price order
lomaxba	decimal	 false	max amount of limit price buy order
lomaxsa	decimal	 false	max amount of limit price sell order
smminoa	decimal	 false	min amount of market price sell order
smmaxoa	decimal	 false	max amount of market price sell order
bmmaxov	decimal	 false	max amount of market price buy order
blmlt	decimal(10,6)	 false	Buy limit must less than
slmgt	decimal(10,6)	 false	Sell limit must greater than
msormlt	decimal(10,6)	 false	Market sell order rate must less than
mbormlt	decimal(10,6)	 false	Market buy order rate must less than
at	string	 false	trading by api interface
u	string	 false	ETP: symbol
mfr	decimal	 false	
ct	string	 false	charge time(unix time in millisecond, just for symbols of ETP)
rt	string	 false	rebal time(unix time in millisecond, just for symbols of ETP)
rthr	decimal	 false	rebal threshold(just for symbols of ETP)
in	decimal	 false	ETP: init nav
maxov	decimal	 false	max value of market price order
flr	decimal	 false	C2C: funding leverage ratio
castate	string	 false	not Required. The state of the call auction; it will only be displayed when it is in the 1st and 2nd stage of the call auction. Enumeration values: "ca_1", "ca_2"
</data>		 false	
ts	String	 false	timestamp of incremental data
full	int	 false	full data flag: 0 for no and 1 for yes
err-code	string	 false	error code(returned when the interface reports an error)
err-msg	string	 false	error msg(returned when the interface reports an error)
Request example
curl"https://api.huobi.pro/v1/settings/common/market-symbols"
Response Example
Success Example
{
"status":"ok"
"data":[
0:{
"symbol":"btc3lusdt"
"state":"online"
"bc":"btc3l"
"qc":"usdt"
"pp":4
"ap":4
"sp":"main"
"vp":8
"minoa":0.01
"maxoa":199.0515
"minov":5
"lominoa":0.01
"lomaxoa":199.0515
"lomaxba":199.0515
"lomaxsa":199.0515
"smminoa":0.01
"blmlt":1.1
"slmgt":0.9
"smmaxoa":199.0515
"bmmaxov":2500
"msormlt":0.1
"mbormlt":0.1
"maxov":2500
"u":"btcusdt"
"mfr":0.035
"ct":"23:55:00"
"rt":"00:00:00"
"rthr":4
"in":16.3568
"at":"enabled"
"tags":"etp,nav,holdinglimit,activities"
}
]
"ts":"1641880897191"
"full":1
}










v1/settings/common/chains ( Get Chains Information)
Request type: GET

Signature verification: No

Interface permission: Read

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description
show-desc	string	 false	show desc, 0: no, 1: all, 2: suspend deposit/withdrawal and chain exchange
currency	string	 false	currency
ts	long	 false	timestamp to get incremental data
Notes: 
It returns updated data from this timestample to the current time if filled in with ts. If there is no update, the "data" of response is "[]".

Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	status
data	Object	 false	
adt	boolean	 false	has addr deposit tag
ac	string	 false	address of chain
ao	boolean	 false	addr oneoff
awt	boolean	 false	addr with tag
chain	string	 false	chain name
ct	string	 false	chain type. plain, live, old, new, legal, tooold
code	string	 false	obsolete, please to use chain
currency	string	 false	currency
deposit-desc	string	 false	deposit desc
de	boolean	 false	deposit enable
dma	string	 false	deposit-min-amount, if the amount is less than this amount will be: 1. The small amount will exceed the deposit-min-amount and then be credited 2. The small amount will not be accumulated and will never be credited to the account
deposit-tips-desc	string	 false	deposit tips desc
dn	string	 false	display name, general be upper
fc	integer	 false	fast-confirms, when height of the exchange node to that chain tail is greater than this number, the deposit and withdrawal will be not settled to the user account, this deposit order is regarded as an unsafe deposit, and the available amount in the withdrawal and account transfer must be excluded that amount from this order.
ft	string	 false	fee type
default	integer	 false	is default
replace-chain-info-desc	string	 false	replace chain info desc
replace-chain-notification-desc	string	 false	replace chain notification desc
replace-chain-popup-desc	string	 false	replace chain popup desc
ca	string	 false	contract address
cct	integer	 false	contract chain type 0; coin; 1: token
         
sc	integer	 false	safe confirms, When the distance between the height of the current exchange's chain node and the chain tail is greater than this number, the asset management DW will mark this order as a safe deposit, and it will be regarded as the available amount when withdrawing and transferring funds.
sda	string	 false	suspend deposit announcement
suspend-deposit-desc	string	 false	suspend deposit desc
swa	string	 false	suspend withdraw announcement
suspend-withdraw-desc	string	 false	suspend withdraw desc
v	boolean	 false	visible
withdraw-desc	string	 false	withdraw desc
we	boolean	 false	withdraw enable
wma	string	 false	withdraw min amount, refused to withdraw if less than this amount
wp	integer	 false	withdraw precision, refused to withdraw if greater than this amount
fn	string	 false	
withdraw-tips-desc	string	 false	withdraw tips desc
suspend-visible-desc	string	 false	suspend visible desc
</data>		 false	
ts	String	 false	timestamp of incremental data
full	int	 false	full data flag: 0 for no and 1 for yes
err-code	string	 false	error code(returned when the interface reports an error)
err-msg	string	 false	error msg(returned when the interface reports an error)
Request example
curl"https://api.huobi.pro/v1/settings/common/chains"
Response Example
Success Example
{
           "status": "ok",
           "data": [
             {
               "chain": "husd",
               "currency": "husd",
               "code": "husd",
               "ct": "plain",
               "ac": "eth",
               "default": 1,
               "dma": "1",
               "wma": "1",
               "de": true,
               "we": false,
               "wp": 8,
               "ft": "eth",
               "dn": "HUSD",
               "fn": "",
               "awt": false,
               "adt": false,
               "ao": false,
               "fc": 999,
               "sc": 999,
               "v": true,
               "sda": null,
               "swa": null,
               "deposit-desc": "",
               "deposit-tips-desc": "",
               "withdraw-desc": "",
               "suspend-deposit-desc": "",
               "suspend-withdraw-desc": "",
               "replace-chain-info-desc": "",
               "replace-chain-notification-desc": "",
               "replace-chain-popup-desc": "",
               "ca": "0x24902AA0cf0000a08c0EA0b003B0c0bF600000E0",
               "cct": 0
             },
           ],
           "ts": "1640743459822",
           "full": 1
         }





         /v2/reference/currencies ( APIv2 - Currency & Chains)
Request type: GET

Signature verification: No

Interface permission: Read

Interface description:  API user could query static reference information for each currency, as well as its corresponding chain(s). (Public Endpoint)

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description	Value Range
currency	string	 false	Currency	btc, ltc, bch, eth, etc ...(available currencies in HTX)
authorizedUser	boolean	 false	Authorized user	true or false (if not filled, default value is true)
Response Parameter
Parameter	Data Type	Required	Description	Value Range
code	int	 false	Status code	
message	string	 false	Error message (if any)	
<data>	object	 false		
currency	string	 false	Currency	
<chains>	object	 false		
chain	string	 false	Chain name	
displayName	string	 false	Chain display name	
baseChain	string	 false	Base chain name	
baseChainProtocol	string	 false	Base chain protocol	
isDynamic	boolean	 false	Is dynamic fee type or not (only applicable to withdrawFeeType = fixed)	true,false
numOfConfirmations	int	 false	Number of confirmations required for deposit success (trading & withdrawal allowed once reached)	
numOfFastConfirmations	int	 false	Number of confirmations required for quick success (trading allowed but withdrawal disallowed once reached)	
minDepositAmt	string	 false	Minimal deposit amount in each request	
depositStatus	string	 false	Deposit status	allowed,prohibited
minWithdrawAmt	string	 false	Minimal withdraw amount in each request	
maxWithdrawAmt	string	 false	Maximum withdraw amount in each request	
withdrawQuotaPerDay	string	 false	Maximum withdraw amount in a day (Singapore timezone)	
withdrawQuotaPerYear	string	 false	Maximum withdraw amount in a year	
withdrawQuotaTotal	string	 false	Maximum withdraw amount in total	
withdrawPrecision	int	 false	Withdraw amount precision	
withdrawFeeType	string	 false	Type of withdraw fee (only one type can be applied to each currency)	fixed,circulated,ratio
transactFeeWithdraw	string	 false	Withdraw fee in each request (only applicable to withdrawFeeType = fixed)	
minTransactFeeWithdraw	string	 false	Minimal withdraw fee in each request (only applicable to withdrawFeeType = circulated or ratio)	
maxTransactFeeWithdraw	string	 false	Maximum withdraw fee in each request (only applicable to withdrawFeeType = circulated or ratio)	
transactFeeRateWithdraw	string	 false	Withdraw fee in each request (only applicable to withdrawFeeType = ratio)	
withdrawStatus	string	 false	Withdraw status	allowed,prohibited
</data>		 false		
instStatus	string	 false	Instrument status	normal,delisted
</chains>		 false		
Request example
curl"https://api.huobi.pro/v2/reference/currencies?currency=usdt"
Response Example
Success Example
{
"code":200
"data":[
0:{
"chains":[
0:{
"chain":"trc20usdt"
"displayName":""
"baseChain":"TRX"
"baseChainProtocol":"TRC20"
"isDynamic":false
"depositStatus":"allowed"
"maxTransactFeeWithdraw":"1.00000000"
"maxWithdrawAmt":"280000.00000000"
"minDepositAmt":"100"
"minTransactFeeWithdraw":"0.10000000"
"minWithdrawAmt":"0.01"
"numOfConfirmations":999
"numOfFastConfirmations":999
"withdrawFeeType":"circulated"
"withdrawPrecision":5
"withdrawQuotaPerDay":"280000.00000000"
"withdrawQuotaPerYear":"2800000.00000000"
"withdrawQuotaTotal":"2800000.00000000"
"withdrawStatus":"allowed"
}
1:{
"chain":"usdt"
"displayName":""
"baseChain":"BTC"
"baseChainProtocol":"OMNI"
"isDynamic":false
"depositStatus":"allowed"
"maxWithdrawAmt":"19000.00000000"
"minDepositAmt":"0.0001"
"minWithdrawAmt":"2"
"numOfConfirmations":30
"numOfFastConfirmations":15
"transactFeeRateWithdraw":"0.00100000"
"withdrawFeeType":"ratio"
"withdrawPrecision":7
"withdrawQuotaPerDay":"90000.00000000"
"withdrawQuotaPerYear":"111000.00000000"
"withdrawQuotaTotal":"1110000.00000000"
"withdrawStatus":"allowed"
}
2:{
"chain":"usdterc20"
"displayName":""
"baseChain":"ETH"
"baseChainProtocol":"ERC20"
"isDynamic":false
"depositStatus":"allowed"
"maxWithdrawAmt":"18000.00000000"
"minDepositAmt":"100"
"minWithdrawAmt":"1"
"numOfConfirmations":999
"numOfFastConfirmations":999
"transactFeeWithdraw":"0.10000000"
"withdrawFeeType":"fixed"
"withdrawPrecision":6
"withdrawQuotaPerDay":"180000.00000000"
"withdrawQuotaPerYear":"200000.00000000"
"withdrawQuotaTotal":"300000.00000000"
"withdrawStatus":"allowed"
}
]
"currency":"usdt"
"instStatus":"normal"
}
]
}




v1/common/timestamp ( Get Current Timestamp)
Request type: GET

Signature verification: No

Interface description:  This endpoint returns the current timestamp, i.e. the number of milliseconds that have elapsed since 00:00:00 UTC on 1 January 1970.

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description

No data

Notes: 
No parameter is needed for this endpoint.

Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	Request Processing Result
data	long	 false	current system timestamp
Request example
curl"https://api.huobi.pro/v1/common/timestamp"
Response Example
Success Example
{
"status":"ok"
"data":1629715504949
}
























MARKET DATA


Market data APIs provide public market information such as varies of candlestick, depth and trade information.

The market data is updated once per second.

Below is the error code, error message and description returned by Market data APIs.

Error Code	Error Message	Description
invalid-parameter	invalid symbol	Parameter symbol is invalid
invalid-parameter	invalid period	Parameter period is invalid for candlestick data
invalid-parameter	invalid depth	Parameter depth is invalid for depth data
invalid-parameter	invalid type	Parameter type is invalid
invalid-parameter	invalid size	Parameter size is invalid
invalid-parameter	invalid size,valid range: [1, 2000]	Parameter size range is invalid
invalid-parameter	request timeout	Request timeout please try again




/market/history/kline ( Get Klines(Candles))
Request type: GET

Signature verification: No

Rate Limit:  4,500 5 minutes

Interface description:  This endpoint retrieves all klines in a specific range.


Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description	Value Range	Default Value
symbol	string	 false	The trading symbol to query	All trading symbol supported, e.g. btcusdt, bccbtcn (to retrieve candlesticks for ETP NAV, symbol = ETP trading symbol + suffix 'nav'，for example: btc3lusdtnav)	
period	string	 false	The period of each candle	1min, 5min, 15min, 30min, 60min, 4hour, 1day, 1mon, 1week, 1year	
size	integer	 false	The number of data returns	[1-2000]	150
Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	Request Processing Result "ok","error"
ch	string	 false	Data belonged channel，Format：market.$symbol.kline.$period
ts	long	 false	Time of Respond Generation, Unit: Millisecond
<data>	object	 false	
id	long	 false	The UNIX timestamp in seconds as response id
amount	float	 false	Accumulated trading volume, in base currency
count	integer	 false	The number of completed trades
open	float	 false	The opening price
close	float	 false	The closing price
low	float	 false	The low price
high	float	 false	The high price
vol	float	 false	Accumulated trading value, in quote currency
</data>		 false	
Request example
curl"https://api.huobi.pro/market/history/kline?period=1day&size=200&symbol=btcusdt"
Response Example
Success Example
{
"ch":"market.btcusdt.kline.5min"
"status":"ok"
"ts":1629769247172
"data":[
0:{
"id":1629769200
"open":49056.37
"close":49025.51
"low":49022.86
"high":49056.38
"amount":3.946281917950917
"vol":193489.67275732
"count":196
}
1:{
"id":1629768900
"open":48994.61
"close":49056.37
"low":48966.72
"high":49072.46
"amount":30.72223099519689
"vol":1505870.732227976
"count":1504
}
]
}




/market/detail/merged ( Get Latest Aggregated Ticker)
Request type: GET

Signature verification: No

Rate Limit:  4,500 5 minutes

Interface description:  This endpoint retrieves the latest ticker with some important 24h aggregated market data.

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description	Value Range
symbol	string	 false	The trading symbol to query	All supported trading symbol, e.g. btcusdt, bccbtc.Refer to /v1/common/symbols
Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	Request Processing Result "ok","error"
ch	string	 false	Data belonged channel，Format：market.$symbol.detail.merged
ts	long	 false	Time of Respond Generation, Unit: Millisecond
<tick>	object	 false	
id	long	 false	The internal identity
amount	float	 false	Accumulated trading volume of last 24 hours (rotating 24h), in base currency
count	integer	 false	The number of completed trades (rotating 24h)
open	float	 false	The opening price of last 24 hours (rotating 24h)
close	float	 false	The last price of last 24 hours (rotating 24h)
low	float	 false	The lowest price of last 24 hours (rotating 24h)
high	float	 false	The highest price of last 24 hours (rotating 24h)
vol	float	 false	Accumulated trading value of last 24 hours (rotating 24h), in quote currency
bid	object	 false	The current best bid in format [price, size]
ask	object	 false	The current best ask in format [price, size]
</tick>		 false	
Request example
curl"https://api.huobi.pro/market/detail/merged?symbol=ethusdt"
Response Example
Success Example
{
"ch":"market.btcusdt.detail.merged"
"status":"ok"
"ts":1629788763750
"tick":{
"id":272156789143
"version":272156789143
"open":50080
"close":49820.92
"low":48767
"high":50500
"amount":12055.365781937457
"vol":598561868.5709001
"count":420573
"bid":[
0:49819.48
1:2.58112
]
"ask":[
0:49819.49
1:0.002411
]
}
}




/market/tickers ( Get Latest Tickers for All Pairs)
Request type: GET

Signature verification: No

Rate Limit:  4,500 5 minutes

Interface description:  This endpoint retrieves the latest tickers for all supported pairs.

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description

No data

Notes:  
No parameters are needed for this endpoint.

Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	Request Processing Result "ok","error"
ts	long	 false	Time of Respond Generation, Unit: Millisecond
<data>	object	 false	
amount	float	 false	The aggregated trading volume in last 24 hours (rotating 24h)
count	integer	 false	The number of completed trades of last 24 hours (rotating 24h)
open	float	 false	The opening price of a nature day (Singapore time)
close	float	 false	The closing price of a nature day (Singapore time)
low	float	 false	The lowest price of a nature day (Singapore time)
high	float	 false	The highest price of a nature day (Singapore time)
vol	float	 false	The aggregated trading value in last 24 hours (rotating 24h)
symbol	string	 false	The trading symbol of this object, e.g. btcusdt, bccbtc
bid	float	 false	Best bid price
bidSize	float	 false	Best bid size
ask	float	 false	Best ask price
askSize	float	 false	Best ask size
</data>		 false	
Request example
curl"https://api.huobi.pro/market/tickers"
Response Example
Success Example
{
"status":"ok"
"ts":1629789355531
"data":[
0:{
"symbol":"smtusdt"
"open":0.004659
"high":0.004696
"low":0.0046
"close":0.00468
"amount":36551302.17544405
"vol":170526.0643855023
"count":1709
"bid":0.004651
"bidSize":54300.341
"ask":0.004679
"askSize":1923.4879
}
1:{
"symbol":"ltcht"
"open":12.795626
"high":12.918053
"low":12.568926
"close":12.918053
"amount":1131.801675005825
"vol":14506.9381937385
"count":923
"bid":12.912687
"bidSize":0.1068
"ask":12.927032
"askSize":5.3228
}
]
}



/market/depth ( Get Market Depth)
Request type: GET

Signature verification: No

Rate Limit: 4,000 5 minutes

Interface description:  This endpoint retrieves the current order book of a specific pair.

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description	Value Range	Default Value
symbol	string	 false	The trading symbol to query	Refer to GET /v1/common/symbols	
depth	integer	 false	The number of market depth to return on each side	5, 10, 20，30	20
type	string	 false	Market depth aggregation level, details below	step0: no aggregation; returns 150 levels of data by default.
step1: aggregation = quote precision × 10; returns 20 levels of data by default.
step2: aggregation = quote precision × 100; returns 20 levels of data by default.
step3: aggregation = quote precision × 1,000; returns 20 levels of data by default.
step4: aggregation = quote precision × 5,000; returns 20 levels of data by default.
step5: aggregation = quote precision × 100,000; returns 20 levels of data by default.	step0
Notes: 
When the type value is 'step0', if 'depth' is not entered, the default value is 150。

Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	Request Processing Result "ok","error"
ch	string	 false	Data belonged channel，Format： market.$symbol.depth.$type
ts	long	 false	Time of Respond Generation, Unit: Millisecond
<tick>	object	 false	
ts	integer	 false	The UNIX timestamp in milliseconds is adjusted to Singapore time
version	integer	 false	Internal data
bids	object	 false	The current all bids in format [price, size]
asks	object	 false	The current all asks in format [price, size]
</tick>		 false	
Request example
curl"https://api.huobi.pro/market/depth?symbol=btcusdt&depth=5&type=step0"
Response Example
Success Example
{
"ch":"market.btcusdt.depth.step0"
"status":"ok"
"ts":1629790438801
"tick":{
"ts":1629790438215
"version":136107114472
"bids":[
0:[
0:49790.87
1:0.779876
]
1:[
0:49785.9
1:0.000182
]
2:[
0:49784.48
1:0.002758
]
3:[
0:49784.29
1:0.05
]
4:[
0:49783.06
1:0.005038
]
]
"asks":[
0:[
0:49790.88
1:2.980472
]
1:[
0:49790.89
1:0.006613
]
2:[
0:49792.16
1:0.080302
]
3:[
0:49792.67
1:0.030112
]
4:[
0:49793.23
1:0.043103
]
]
}
}








/market/trade ( Get the Last Trade)
Request type: GET

Signature verification: No

Rate Limit: 4,500 5 minutes

Interface description:  This endpoint retrieves the latest trade with its price, volume, and direction.

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description	Value Range
symbol	string	 false	The trading symbol to query	Refer to GET /v1/common/symbols
Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	Request Processing Result "ok","error"
ch	string	 false	Data belonged channel，Format：market.$symbol.trade.detail
ts	long	 false	Time of Respond Generation, Unit: Millisecond
<tick>	object	 false	
id	long	 false	global transaction ID
ts	long	 false	Latest Creation Time
<data>	object	 false	
id	integer	 false	The unique trade id of this trade (to be obsoleted)
trade-id	integer	 false	The unique trade id (NEW)
amount	float	 false	The trading volume in base currency
price	float	 false	The trading price in quote currency
ts	integer	 false	The UNIX timestamp in milliseconds adjusted to Singapore time
direction	string	 false	The direction of the taker trade: 'buy' or 'sell'
</data>		 false	
</tick>		 false	
Request example
curl"https://api.huobi.pro/market/trade?symbol=btcusdt"
Response Example
Success Example
{
"ch":"market.btcusdt.trade.detail"
"status":"ok"
"ts":1629792192037
"tick":{
"id":136107843051
"ts":1629792191928
"data":[
0:{
"id":1.361078430513484e+26
"ts":1629792191928
"trade-id":102517374388
"amount":0.028416
"price":49806
"direction":"buy"
}
1:{
"id":1.361078430513484e+26
"ts":1629792191928
"trade-id":102517374387
"amount":0.025794
"price":49806
"direction":"buy"
}
]
}
}










/market/history/trade ( Get the Most Recent Trades)
Request type: GET

Signature verification: No

Rate Limit: 3,000 5 minutes

Interface description:  This endpoint retrieves the most recent trades with their price, volume, and direction.

Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description	Value Range	Default Value
symbol	string	 false	The trading symbol to query	All supported trading symbol, e.g. btcusdt, bccbtc.Refer to GET /v1/common/symbols	
size	integer	 false	The number of data returns	[1-2000]	1
Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	Request Processing Result "ok","error"
ch	string	 false	Data belonged channel，Format：market.$symbol.trade.detail
ts	long	 false	Time of Respond Generation, Unit: Millisecond
<data>	object	 false	
id	long	 false	global transaction ID
ts	long	 false	Latest Creation Time
<data>	object	 false	
id	integer	 false	The unique trade id of this trade (to be obsoleted)
trade-id	integer	 false	The unique trade id (NEW)
amount	float	 false	The trading volume in base currency
price	float	 false	The trading price in quote currency
ts	integer	 false	The UNIX timestamp in milliseconds adjusted to Singapore time
direction	string	 false	The direction of the taker trade: 'buy' or 'sell'
</data>		 false	
</data>		 false	
Notes: 
 The returned data object is an array which represents one recent timestamp; each timestamp object again is an array which represents all trades occurred at this timestamp.

Request example
curl"https://api.huobi.pro/market/history/trade?symbol=btcusdt&size=2"
Response Example
Success Example
{
"ch":"market.btcusdt.trade.detail"
"status":"ok"
"ts":1629793657842
"data":[
0:{
"id":136108764379
"ts":1629793656939
"data":[
0:{
"id":1.361087643793484e+26
"ts":1629793656939
"trade-id":102517381182
"amount":0.000124
"price":49656.4
"direction":"buy"
}
]
}
1:{
"id":136108763320
"ts":1629793656198
"data":[
0:{
"id":1.361087633203484e+26
"ts":1629793656198
"trade-id":102517381181
"amount":0.01125
"price":49655
"direction":"buy"
}
1:{
"id":1.361087633203484e+26
"ts":1629793656198
"trade-id":102517381180
"amount":0.00083
"price":49651.35
"direction":"buy"
}
]
}
]
}








/market/detail ( Get the Last 24h Market Summary)
Request type: GET

Signature verification: No

Rate Limit: 4,500 5 minutes

Interface description:  This endpoint retrieves the summary of trading in the market for the last 24 hours.


Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description	Value Range
symbol	string	 false	The trading symbol to query	Refer to /v1/common/symbols
Response Parameter
Parameter	Data Type	Required	Description
status	string	 false	Request Processing Result "ok","error"
ch	string	 false	Data belonged channel，Format： market.$symbol.detail
ts	long	 false	Time of Respond Generation, Unit: Millisecond
<tick>	object	 false	
id	integer	 false	The internal identity
amount	float	 false	The aggregated trading volume in USDT of last 24 hours (rotating 24h)
count	integer	 false	The number of completed trades of last 24 hours (rotating 24h)
open	float	 false	The opening price of last 24 hours (rotating 24h)
close	float	 false	The closing price of last 24 hours (rotating 24h)
low	float	 false	The lowest price of last 24 hours (rotating 24h)
high	float	 false	The highest price of last 24 hours (rotating 24h)
vol	float	 false	The trading volume in base currency of last 24 hours (rotating 24h)
version	integer	 false	Internal data
</tick>		 false	
Request example
curl"https://api.huobi.pro/market/detail?symbol=ethusdt"
Response Example
Success Example
{
"ch":"market.btcusdt.detail"
"status":"ok"
"ts":1629795484817
"tick":{
"id":272164011416
"low":48767.7
"high":50500.6
"open":50266.89
"close":49728.71
"vol":601037933.6834868
"amount":12110.642402972368
"version":272164011416
"count":420452
}
}









/market/fullMbp (Full Order Book)
Request type: GET

Signature verification: No

Interface permission: Read

Rate Limit: 5 times/1s

Interface description: Query the complete market depth data, Updated once per second,and support returning up to 5000 levels.


Request Address
Environment	Address
Online	https://api.huobi.pro
Online  (preferred by aws customers)	https://api-aws.huobi.pro
Request Parameter
Parameter	Data Type	Required	Description
symbol		string	 true	Trading Pairs, and support returning up to 5000 levels.	
Response Parameter
Parameter	Data Type	Required	Description
status	string		 false	Request Processing Result "ok","error"	
ch	string		 false	Data belonged channel，Format： market.$symbol.depth.$type	
ts		long	 false	Time of Respond Generation, Unit: Millisecond	
<tick>			 false	
ts		调整为新加坡时间的时间戳，单位毫秒		 false	The UNIX timestamp in milliseconds is adjusted to Singapore time	
version		内部字段		 false	Internal data	
bids		当前的所有买单 [price, size]		 false	The current all bids in format [price, size]	
asks		当前的所有卖单 [price, size]		 false	The current all asks in format [price, size]	
</tick>			 false	
Request example
curl"https://api.huobi.pro/market/fullMbp?symbol=ethusdt"
Response Example
Success Example
{
"ch":"market.btcusdt.depth.step0"
"status":"ok"
"ts":1629790438801
"tick":{
"ts":1629790438215
"version":136107114472
"bids":[
0:[
0:49790.87
1:0.779876
]
1:[
0:49785.9
1:0.000182
]
2:[
0:49784.48
1:0.002758
]
3:[
0:49784.29
1:0.05
]
4:[
0:49783.06
1:0.005038
]
]
"asks":[
0:[
0:49790.88
1:2.980472
]
1:[
0:49790.89
1:0.006613
]
2:[
0:49792.16
1:0.080302
]
3:[
0:49792.67
1:0.030112
]
4:[
0:49793.23
1:0.043103
]
]
}
}



























