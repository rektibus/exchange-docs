API Introduction
API Introduction
Welcome to the CoinEx API documentation.

This documentation aims to provide developers with detailed information on how to integrate and interact with the CoinEx exchange.

CoinEx offers a wide range of features and flexible options, allowing you to build your own trading applications, automate trading strategies, or develop other tools related to the exchange.

API Documentation Structure
Our API documentation is organized according to the following structures:

API Introduction: Provides an overall introduction to the API, document organization, and related materials (including demo).
Integration Guide: Describes how to proceed with the entire access process and the corresponding best practices.
Authentication: Describes how to generate an API key and authenticate.
Rate Limit: Provides detailed information on the function, usage and sample code of each API endpoint.
Error Handling：Lists common error codes and corresponding error handling methods.
Enumeration of Definitions: Lists the enumeration values used in the endpoints and the corresponding detailed description.
FAQ: Our API documentation also provides answers to frequently asked questions to help you better understand and utilize the API.
API Base URL
CoinEx provides services through HTTP protocol and WebSockets protocol. The base URL for accessing these services is as follows:

Info
The base URL of HTTP is: https://api.coinex.com/v2

The base URL for spot and futures WS are different, as follows:

Spot: wss://socket.coinex.com/v2/spot
Futures: wss://socket.coinex.com/v2/futures
Authentication and Security
To ensure the security of transaction and accessing account information, our API utilizes an authentication mechanism. Before using the API, you need to create an API secret key and use it for authentication. The API secret key will be associated with your exchange account and used to authenticate and authorize API requests.

For the detailed authentication process, please refer to this link.

Module Grouping
CoinEx API is grouped according to business modules. The specific grouping is as follows:

Module	Submodule	Description
Account	Subaccount	Subaccount management
Subaccount API key management
Subaccount balance inquiry
Asset transfer between subaccounts
Fees	Account trading fee inquiry
Settings	Modify account settings
Assets	Balance	Get balances of various types of accounts
Borrow & Repay	Margin borrow, Margin repay, and borrowing record inquiry
Deposit & Withdrawal	Deposit, withdrawal, and related record inquiry
Asset Transfer	Asset transfer between various types of accounts and related record inquiry
Spot	Market	Get market list, market data, depth, trades, K-line, index, etc.
Trade	Get trading records
Order	Place order, batch orders
Get order status
Get unfilled and filled order lists
Modify order
Cancel order, batch cancel orders, cancel order by client_id
Futures	Market	Get market list, market data, depth, trades, K-line, index, funding rate, etc.
Trade	Get trading records
Order	Place order, batch orders
Get order status
Get unfilled and filled order lists
Modify order
Cancel order, batch cancel orders, cancel order by client_id
Position	Close position
Adjust position margin
Take profit, stop loss
Get current position, historical positio
Get position margin changes, funding rate, auto deleveraging, auto settlement history
Related Resources
Before using this exchange API, you may need to know the following resources:

API Documentation: Provides detailed information about each API endpoint, including request methods, parameters, and response results, etc.
API Management Console: Offers functions for generating, managing, and setting permissions for API keys.
Sample code: To ensure developers can easily get started, the exchange provides sample code in various programming languages for reference and usage.
Support and Feedback
If you encounter any issues or need further assistance while using the API, please feel free to contact our Support Team. We are happy to answer your questions and provide support and guidance during the development process.

We highly value your feedback. If you have any suggestions or improvement ideas for the API documentation, please let us know. We will continuously improve and update the documentation to ensure it stays in sync with our API and meets your needs.

Thank you for choosing CoinEx API services. We look forward to seeing you build outstanding applications and integrate with our exchange. Good luck with your trading!







Integration Guide
The following is a brief introduction to quickly get started using the API services in this centralized cryptocurrency exchange:

Get API Key
Before applying for an API key, you need to apply for an account at CoinEx. For the specific application process, please refer to Help Center.

Once you have your account ready, you can generate the API key in the Developer Console to ensure that you have the necessary permissions.

Prepare for API Calls
Depending on your requirements, select the appropriate API endpoint and refer to the corresponding API documentation to understand the request methods, parameters, and response results.

For details, you can explore the Module Grouping, and find the corresponding module and its corresponding API endpoint, or use the search function to quickly find it.

Build Requests
Use the programming language of your choice to construct a request that meets the API requirements, including setting the request method, URL, request headers and parameters, etc.

Info
The base URL of HTTP is: https: //api.coinex.com/v2

The base URL for spot and futures WS are different, as follows:

Spot: wss: //socket.coinex.com/v2/spot
Futures: wss: //socket.coinex.com/v2/futures
Public Parameter:

Info
HTTP endpoints marked with signature required needs to use the following two public HTTP HEADER parameters for request authentication. For specific usage methods, please refer to Authentication

X-COINEX-KEY
X-COINEX-SIGN
Info
If you need to limit the validity time of the request, you can restrict the validity period through the following public HTTP HEADER parameters in all HTTP endpoints.

When the server receives the request, it will check the timestamp provided in the X-COINEX-TIMESTAMP. If the request was sent more than 5000 milliseconds (default value) ago, it will be considered invalid.This time window value can be customized by sending the optional parameter X-COINEX-WINDOWTIME.

X-COINEX-TIMESTAMP.Required parameter, used to indicate the time at which the request is being sent.
X-COINEX-WINDOWTIME.Optional parameter, used to indicate a time window for which the request is valid. The default value is 5000 milliseconds.
Info
In all APIs, time request parameters and response fields are millisecond-level timestamps.

Response Processing
Parse the response data returned by the API and perform corresponding processing as needed, such as error handling, data extraction, etc.

HTTP Response Processing
For HTTP responses, please determine at first whether the status_code is 200, and then proceed to the next step of processing.
A normal HTTP response will have a unified response structure. You need to determine whether the response is normal by judging the code field in the structure. code should be 0 under normal circumstances.
The unified structure of HTTP normal response is as follows: {
    "code": 0,
    "data": ...
    "message": "OK"
}

WS Response Processing
In the WS protocol, it is recommended to handle the response to subscription requests before proceeding further. Upon sending a subscription request, the server will respond with a subscription result. The response from the WS server is compressed using zip and must be decompressed first.
It's necessary to determine if the 'code' field in the response result is 0.
The unified structure of WS normal response is as follows: {
    "id": 4,
    "message": "OK",
    "code": 0
}

After a successful subscription, the server will push the data when it is updated, and the pushed data can be processed according to your needs.
For specific error explanations, please refer to Error Handling

Security Considerations
Warning
Ensure that HTTPS protocol is used for data transmission in API calls. Additionally, securely manage your API keys to prevent any leakage. The importance of API keys is equivalent to that of your account password. To ensure your account and asset security, please manage and regularly update your keys appropriately.Once you lose your secret key, please go to CoinEx to remove the secret key in time.







Authentication
User Guide: HTTP and WebSocket Endpoint Authentication Process
The following is a user guide for the authentication process of the HTTP and WebSocket endpoints on CoinEx exchange.

Step 1: Obtain API key
Warning
Please do not directly transmit the secret_key obtained from Step 1 in any network request, as this may result in potential asset loss.

Log in to CoinEx.Navigate to the API management page.Create a new API or use an existing API.
Get access_id and secret_key from the created API record.
Step 2: Generate authentication parameters
Generation method for HTTP endpoints
Splice the data into a string according to the format of method + request_path + body(optional) + timestamp. The example is as follows:
prepared_str = "GET"+"/v2/spot/pending-order?market=BTCUSDT&market_type=SPOT&side=buy&page=1&limit=10"+"1700490703564"

As shown in the above example:

method represents the HTTP request method in uppercase letters, such as: GET/POST
request_path represents the path of the requested endpoint, including request parameters(query_string) if applicable, for example: /v2/spot/pending-order?market=BTCUSDT&market_type=SPOT&side=buy&page=1&limit=10.If there is no request parameter (query_string), only the request path needs to be included, for example: /v2/spot/pending-order
body represents the HTTP request body. As in the above example, if there is no request body in some methods (GET/DELETE), it can be omitted.An example of the request body is as follows: '{
    "market": "BTCUSDT",
    "type": "buy",
    "amount": "0.001",
    "price": "10000"
}'
timestamp represents the time when the request was sent, and its value is taken from X-COINEX-TIMESTAMP
Using 'secret_key' as the key. Create your HMAC-SHA256 signature using the above string and convert it to lowercase hexadecimal format with a length of 64 characters. The pseudocode is as follows:
signed_str = hmac.new(bytes(secret_key, 'latin-1'), msg=bytes(prepared_str, 'latin-1'), digestmod=hashlib.sha256).hexdigest().lower()


Generation method for WebSocket endpoints
Splice the data into a string according to the format of timestamp. The example is as follows:
prepared_str = "1700490703564"

Using 'secret_key' as the key. Create your HMAC-SHA256 signature using the above string and convert it to lowercase hexadecimal format with a length of 64 characters. The pseudocode is as follows:
signed_str = hmac.new(bytes(secret_key, 'latin-1'), msg=bytes(prepared_str, 'latin-1'), digestmod=hashlib.sha256).hexdigest().lower()


Step 3: Build authentication request
HTTP Authentication Request
When constructing an HTTP authentication request, the following public parameters are required:

X-COINEX-KEY.The access_id obtained from Step 1
X-COINEX-SIGN.The signed_str generated in Step 2
X-COINEX-TIMESTAMP. The parameter mentioned in the Integration Guide that indicates the time when the request is sent.
An example is as follows:

GET /assets/spot/balance HTTP/1.1
Host: api.coinex.com
-H 'X-COINEX-KEY: XXXXXXXXXX' \
-H 'X-COINEX-SIGN: XXXXXXXXXX' \
-H 'X-COINEX-TIMESTAMP: 1700490703564

WebSocket Authentication Request
Before accessing the WebSocket endpoint that requires authentication, you need to call the authentication method named server.sign. You can view the endpoint details through this link.

The corresponding request fields are as follows:

access_id.The access_id obtained from Step 1
signed_str.The signed_str generated in Step 2
timestamp.The current timestamp in milliseconds.
An example is as follows:




Rate Limit
Rate Limit
Rate limits are mainly divided into two types.

IP Rate Limit, which is based on the user's IP address and limits the access rate from that IP. Currently, the limit setting is relatively high, and users generally will not trigger such limits.

User Rate Limit, which is based on the user's trading account. It includes a Short Cycle Rate Limit and a Long Cycle Rate Limit. Their differences are as follows:

Short Cycle Rate Limit: The main account and its created sub-accounts are independently subject to the Short Cycle Rate Limit. This means that each account has its own limits and quotas, which are independent of other accounts.
Long Cycle Rate Limit: The main account and its created sub-accounts share the same rate limit quota. This means that requests from all accounts will affect this shared quota, and requests from all accounts will be deducted from the same quota.
IP Rate Limit
Rate limit: 400/s

User Rate Limit
User Rate Limit is divided into two modes: Short Cycle Rate Limit and Long Cycle Rate Limit.

Short Cycle Rate limit tends to control the short-term request volume and prevent malicious use of the API.
Long Cycle Rate Limit tends to control the long-term request volume and prevent abuse of API resources.
Info
For batch requests that contain a specified number of sub-requests, the request quota consumed will be determined by the number of sub-requests included. An example is as follows:

In a batch spot order request sent to POST /spot/batch-order that includes 5 order requests, the request will consume a quota of 5. The 'short-term rate limit' and 'long-term rate limit' rules will be based on this quantity for consumption tracking.

Currently, the endpoints for calculating request margin by sub-request are listed as follows:

Spot module:

Batch place orders POST /spot/batch-order
Batch place stop orders POST /spot/batch-stop-order
Batch modify orders POST /spot/batch-modify-order
Batch cancel orders POST /spot/cancel-batch-order
Batch cancel stop orders POST /spot/cancel-batch-stop-order
Futures module:

Batch place orders POST /futures/batch-order
Batch place stop orders POST /futures/batch-stop-order
Batch modify orders POST /futures/batch-modify-order
Batch cancel orders POST /futures/cancel-batch-order
Batch cancel stop orders POST /futures/cancel-batch-stop-order
The current rate limits are based on groups, and the corresponding relationships between groups can be seen in the following section.The 'short-term rate limit' and 'long-term rate limit' will be applied simultaneously in groups.

Short Cycle Rate Limit
This rate limit strategy is based on grouped request paths to control the request frequency on specific paths. Here is a detailed description:

Grouping: Request paths are divided into multiple groups, each group containing a set of related paths. Paths with similar functions or characteristics are grouped together.

Request Quota: Each group has a shared request quota that represents the number of requests allowed for that group within a specific period. The quota is dynamically restored based on the rate-limiting frequency.

Rate Limiting Frequency: Each group will have a rate-limiting frequency, which is the maximum amount of request quota that can be recovered per second. For example, if the rate limiting frequency is 20r/s, it means that the request quota recovers by 20 requests per second.

Rate Limiting Strategy: When a request is received, the system first determines the group to which the request belongs. Then, the system checks if the request quota for that group allows processing of the request.

a. If the request quota is higher than zero, the request is allowed to be processed and the quota is reduced. After the request is processed, the system can return the corresponding results.

b. If the request margin is zero, the request will be refused. The system will return an error code indicating that the request has exceeded the usage limit.

Account Short Cycle Rate Limit (Spot)
The main and sub-accounts are separately rate-limited and do not affect each other.
Endpoint type	Rate limit	Endpoint path included
Place & edit spot orders	30r/1s	POST /spot/order *Place order
POST /spot/stop-order *Place stop order
POST /spot/modify-order *Edit order
POST /spot/modify-stop-order *Edit stop order
POST /spot/batch-order *Batch place orders
POST /spot/batch-stop-order *Batch place stop orders
POST /spot/batch-modify-order *Batch edit orders
Cancel spot orders	60r/1s	POST /spot/cancel-order *Cancel order
POST /spot/cancel-stop-order *Cancel stop order
POST /spot/cancel-batch-order *Batch cancel orders
POST /spot/cancel-batch-stop-order *Batch cancel stop orders
Batch cancel spot orders	40r/1s	POST /spot/cancel-all-order *Cancel all orders
POST /spot/cancel-order-by-client-id *Cancel order by client_id
POST /spot/cancel-stop-order-by-client-id *Cancel stop order by client_id
Query spot orders	50r/1s	GET /spot/order-status *Query order status
GET /spot/batch-order-status *Batch query order statuses
GET /spot/pending-order *Get unfilled orders
GET /spot/pending-stop-order *Get unfilled stop orders
Query spot order history	10r/1s	GET /spot/order-deals *Get user order executions
GET /spot/user-deals *Get user executions
GET /spot/finished-order *Get filled orders
GET /spot/finished-stop-order *Get filled stop orders
Modify spot accounts	10r/1s	POST /account/settings *Modify account settings
POST /assets/margin/borrow *Borrow margin
POST /assets/margin/repay *Repay margin
POST /assets/transfer *Transfer assets
POST /account/subs *Create sub-account
POST /account/subs/frozen *Disable sub-account
POST /account/subs/unfrozen *Enable sub-account
POST /account/subs/api *Create sub-account API key
POST /account/subs/edit-api *Edit sub-account API key
POST /account/subs/delete-api *Delete sub-account API key
POST /account/subs/transfer *Transfer assets between sub-accounts
POST /assets/renewal-deposit-address *Update deposit address
POST /assets/withdraw *Request withdrawal
POST /assets/cancel-withdraw *Cancel withdrawal request
POST /assets/amm/add-liquidity *Add AMM liquidity
POST /assets/amm/remove-liquidity *Remove AMM liquidity
Query spot accounts	10r/1s	GET /assets/spot/balance *Get spot account balance
GET /account/trade-fee-rate *Get account trade fee rate
GET /assets/amm/liquidity *Get AMM liquidity
GET /assets/financial/balance *Get financial account balance
GET /assets/margin/balance *Get margin account balance
GET /assets/credit/info *Get credit account info
GET /account/subs *Get sub-account list
GET /account/subs/api *Get sub-account API key list
GET /account/subs/api-detail *Get sub-account API key details
GET /account/subs/spot-balance *Get sub-account spot balance
GET /account/subs/info *Get sub-account info
GET /assets/deposit-address *Get deposit address
GET /assets/deposit-withdraw-config *Get deposit/withdraw config
GET /assets/amm/income-history *Get AMM income history
Query spot account history	10r/1s	GET /assets/withdraw *Get withdrawal history
GET /assets/deposit-history *Get deposit history
GET /assets/statement *Get user statement
GET /assets/transfer-history *Get asset transfer history
GET /assets/margin/borrow-history *Get margin borrow history
GET /assets/margin/interest-limit *Get borrow limit
GET /account/subs/transfer-history *Get sub-account transfer history
Account Short Cycle Rate Limit (Futures)
The main and sub-accounts are separately rate-limited and do not affect each other.
Endpoint type	Rate limit	Endpoint path included
Place & edit futures orders & adjust position	20r/1s	POST /futures/order *Place order
POST /futures/stop-order *Place stop order
POST /futures/close-position *Market close all positions
POST /futures/adjust-position-margin *Adjust position margin
POST /futures/adjust-position-leverage *Adjust position leverage
POST /futures/set-position-stop-loss *Set position stop-loss
POST /futures/set-position-take-profit *Set position take-profit
POST /futures/modify-position-stop-loss *Modify stop-loss order
POST /futures/modify-position-take-profit *Modify take-profit order
POST /futures/cancel-position-stop-loss *Cancel stop-loss order
POST /futures/cancel-position-take-profit *Cancel take-profit order
POST /futures/modify-order *Edit order
POST /futures/modify-stop-order *Edit stop order
POST /futures/batch-order *Batch place orders
POST /futures/batch-stop-order *Batch place stop orders
POST /futures/batch-modify-order *Batch edit orders
Cancel futures order	40r/1s	POST /futures/cancel-order *Cancel order
POST /futures/cancel-stop-order *Cancel stop order
POST /futures/cancel-batch-order *Batch cancel orders
POST /futures/cancel-batch-stop-order *Batch cancel stop orders
Batch cancel futures orders	20r/1s	POST /futures/cancel-all-order *Cancel all orders
POST /futures/cancel-order-by-client-id *Cancel order by client_id
POST /futures/cancel-stop-order-by-client-id *Cancel stop order by client_id
Futures query order	50r/1s	GET /futures/pending-order *Get unfilled orders
GET /futures/pending-stop-order *Get unfilled stop orders
GET /futures/order-status *Query order status
GET /futures/batch-order-status *Batch query order status
Futures order history query	10r/1s	GET /futures/finished-order *Get completed orders
GET /futures/finished-stop-order *Get completed stop orders
GET /futures/finished-position *Get position history
GET /futures/user-deals *Get user trades
GET /futures/order-deals *Get order trades
Futures account query	10r/1s	GET /assets/futures/balance *Get futures account balance
GET /futures/position-funding-history *Get position funding rate history
GET /futures/pending-position *Get current position
GET /futures/position-adl-history *Get position ADL history
GET /futures/position-margin-history *Get position margin change history
GET /futures/position-settle-history *Get position settlement history
Info
When accessing an endpoint that triggers rate limit, the following two Header will be returned in the HTTP response header.

X-RateLimit-Limit. This value indicates the maximum number of accesses per second allowed by the group to which the endpoint belongs.
X-RateLimit-Remaining. This value indicates the current number of remaining accesses for the group to which the endpoint belongs.
X-RateLimit-LongPeriod-{period
}-Remaining.This value indicates the number of remaining accesses in the currently configured long period of the group to which the endpoint belongs, and period indicates the limit period, such as 1H,
4H,
8H or 24H.
Long Cycle Rate Limit
Long Cycle Rate Limit primarily evaluates the user's request volume and request quality to determine whether to restrict the total volume of requests within a longer cycle. Among them, request quality mainly includes other reference indicators such as effective trading rate and average order survival time.

The concepts mentioned above are explained as follows:

Cycle. Unlike short cycle rate limit, the cycle here refers to a longer statistical cycle, such as 1h,
4h,
8h, or 24h.
Request Volume. The total sum of all requests within one cycle for a specific group.
Request Quality. It mainly includes other reference indicators such as effective trading rate and average order lifespan.
Effective Trading Rate. The effective trading rate in a cycle = the number of valid orders (completed orders with executive trading) / the total number of orders.
Average Order Lifespan. The average lifespan of orders within a cycle, calculated as the difference between the creation time and completion time of each order.
Only when both the request volume and request quality indicators exceed the limit will it be affected by long cycle rate limit.

The long cycle rate limit will be reset after the end of a cycle and the statistics of the cycle are based on whole hours. For example, assuming that the period of the long cycle rate limit is 8h, then there will be three statistical cycles in a day, namely 0~8h ,
8~16h,
16~24h.

After the long cycle rate limit is triggered, API requests will be placed in low-speed mode, where the allowed rate for each group will be significantly reduced. However, it will not restrict users from canceling orders.

Info
When accessing an endpoint that triggers long-term rate limit, the following Header will be returned in the HTTP response header.

X-RateLimit-LongPeriod-{period
}-Remaining.This value indicates the number of remaining accesses in the currently configured long period of the group to which the endpoint belongs, and period indicates the limit period, such as 1H,
4H,
8H or 24H.For example: X-RateLimit-LongPeriod-24H-Remaining.In addition, there may be multiple long-period frequency limiting rules in effect at the same time, that is, multiple headers with different periods will be returned at the same time.
Common error codes and processing methods after the rate limit is triggered.
Error Code	Method
3008	Service busy, please try again later.
4001	Service unavailable, please try again later.
4213	Rate limit triggered. Please adjust your strategy and reduce the request rate.
Other error handling
If you encounter other errors, you can refer to Error Handling.




Error Handling
Error Handling Process
This section includes the process of error handling to assist developers in taking appropriate actions when encountering errors. It explains how to parse error responses, handle different types of errors, and provide appropriate user feedback, etc.

HTTP Error Handling Process
Please check if the HTTP response status code is 200. If the status code is not 200, it indicates that the responses may be originating from CoinEx's server gateway service, which was previously functioning. In this case, it's not appropriate to parse the response according to the JSON format outlined in our documentation. Instead, it is recommended to directly capture and record the returned response body.
Parse the response body according to the specified error response format (see the next section Error Response Format) to determine whether an error has occurred. If the request is successful, the corresponding error code will return the number '0'. If it's not '0', proceed with the next step.
Refer to the error code table below to determine how to handle the error.
If there is no handling method for this error code in the documentation, please save the request parameters and error response, and contact us for help.
WS Error Handling Process
Parse the response body according to the specified error response format (see the next section Error Response Format) to determine whether an error has occurred. If the request is successful, the corresponding error code will return the number '0'. If it's not '0', proceed with the next step.
Refer to the error code table below to determine how to handle the error.
If there is no handling method for this error code in the documentation, please save the request parameters and error response, and contact us for help.
Error Response Format
When the request fails, the server will return an error response following a specific format. This error response includes an error code and an error message.

The agreed error response formats are as follows:

HTTP Error Response
{
    "code": 3008,
    "data": {},
    "message": "service too busy"
}

WS Error Response
{
    "id": 4,
    "message": "invalid parameters",
    "code": 20001
}

HTTP Error Code
Error Code	Advised Method
3008	Service busy, please try again later.
3109	Insufficient balance, please adjust the order quantity or make another deposit.
3127	The order quantity is below the minimum requirement. Please adjust the order quantity.
3606	The price difference between the order price and the latest price is too large. Please adjust the order amount accordingly.
3610	Order cancellation prohibited during the Call Auction period.
3612	The est. ask price is lower than the current bottom ask price. Please reduce the amount.
3613	The est. bid price is higher than the current top bid price. Please reduce the amount.
3614	The deviation between your est. filled price and the index price. Please reduce the amount.
3615	The deviation between your order price and the index price is too high. Please adjust your order price and try again.
3616	The order price exceeds the current top bid price. Please adjust the order price and try again.
3617	The order price exceeds the current bottom ask price. Please adjust the order price and try again.
3618	The deviation between your order price and the index price is too high. Please adjust your order price and try again.
3619	The deviation between your order price and the trigger price is too high. Please adjust your order price and try again.
3620	Market order submission is temporarily unavailable due to insufficient depth in the current market
3621	This order can't be completely executed and has been canceled.
3622	This order can't be set as Maker Only and has been canceled.
3627	The current market depth is low, please reduce your order amount and try again.
3628	The current market depth is low, please reduce your order amount and try again.
3629	The current market depth is low, please reduce your order amount and try again.
3632	The order price exceeds the current top bid price. Please adjust the order price and try again.
3633	The order price exceeds the current bottom ask price. Please adjust the order price and try again.
3634	The deviation between your est. filled price and the index price is too high. Please reduce the amount and try again.
3635	The deviation between your est. filled price and the index price is too high. Please reduce the amount and try again.
3638	Currently in protection period, only Maker Only Limit Orders placement and order cancellations are supported.
3639	Request parameters incorrect. Please check whether the request complies with the document description.
4001	Service unavailable, please try again later.
4002	Service request timed out, please try again later.
4003	Internal error, please contact customer service for help.
4004	Parameter error, please check whether the request parameters are abnormal.
4005	Abnormal access_id, please check whether the value passed by X-COINEX-KEY is normal.
4006	Signature verification failed, please check the signature according to the documentation instructions.
4007	IP address prohibited, please check whether the whitelist or export IP is normal.
4008	Abnormal X-COIN-SIGN value, please check.
4009	Abnormal request method, please check.
4010	Expired request, please try again later.
4011	User prohibited from accessing, please contact customer service for help.
4017	Signature expired, please try again later.
4018	The endpoint has been deprecated. Please use the new version of this endpoint.
4115	User prohibited from trading, please contact customer service for help.
4117	Trading prohibited in this market, please try again later.
4130	Futures trading prohibited, please try again later.
4158	Trading prohibited, please try again later.
4159	API trading is unavailable in the current market
4213	The request is too frequent, please try again later.
4512	Insufficient sub-account permissions, please check.
WS Error Code
Spot WS Error Code	Advised Method
20001	Request parameter error, please check.
20002	No corresponding method found
21001	This method requires authentication, please authenticate first.
21002	Authentication failed
23001	Request service timeout
23002	Requests submitted too frequently
24001	Internal Error
24002	Service unavailable temporarily
Futures WS Error Code	Advised Method
30001	Request parameter error, please check.
30002	No corresponding method found
31001	This method requires authentication, please authenticate first.
31002	Authentication failed
33001	Request service timeout
33002	Requests submitted too frequently
34001	Internal Error
34002	Service unavailable temporarily






Enumeration of Definitions
market_type
SPOT: spot market
MARGIN: margin market
FUTURES: futures market
market_status
bidding: bidding
counting_down: counting down
online: available
order_side
buy: buy order
sell: sell order
order_type
limit: limit order (always valid, good till cancel)
market: market order
maker_only: maker only order (post only order)
ioc: immediate or cancel
fok: fill or kill
stp_mode
ct: Cancel the remaining Taker orders immediately
cm: Cancel the remaining Maker orders immediately
both: Cancel the remaining Taker and Maker orders immediately
order_event
put: Order placed successfully (unfilled/partially filled)
update: Order updated (partially filled)
modify: Order modified successfully (unfilled/partially filled)
finish: Order completed (filled or canceled)
stop_order_event
put: Stop order placed successfully
active: Stop order triggered
cancel: Stop order canceled
stop_order_status
put: Stop order placed successfully
active_success: Stop order triggered successfully
active_fail: Stop order trigger unsuccessful
cancel: Stop order canceled
trigger_direction
higher: The latest price is higher than the trigger price
lower: The latest price is lower than the trigger price
position_event
update: Position updated (opening position/partial closing/margin changes, etc.)
close: All positions closed
sys_close: All positions closed by system
adl: Position automatically reduced (partially/fully closed)
liq: Position liquidated
locale
de-DE
en-US
es-AR
es-ES
es-MX
fr-FR
kk-KZ
id-ID
uk-UA
ja-JP
ru-RU
th-TH
pt-BR
tr-TR
vi-VN
zh-TW
ar-SA
hi-IN
fil-PH
permissions
FUTURES: Futures trading permissions
MARGIN: Margin trading permissions
AMM: AMM (Automated market making) permissions
API: API management permissions
transfer_status
created: The transfer request has been submitted
deducted: Assets have been deducted
failed: Transfer failed
finished: Transfer complete
loan_status
loan: Borrowing loans
debt: In debt
liquidated: The loan is forcefully liquidated
finish: The loan has been fully repaid
deposit_status
processing: deposit being processed
confirming: deposit awaiting block confirmations
cancelled: deposit canceled
finished: deposit credited
too_small: deposit amount lower than the minimum limit
exception: the deposit cannot be processed as usual
withdraw_status
created: 'withdrawal pending for Email confirmation'
audit_required: 'withdrawal to be audited'
audited: 'withdrawal approved'
processing: 'withdrawal being processed'
confirming: 'withdrawal awaiting block confirmations'
finished: 'withdrawal complete'
cancelled: 'withdrawal canceled'
cancellation_failed: 'withdrawal cancellation failed'
failed: 'withdrawal failed'
order_status
open: the order is placed and pending execution;
part_filled: order partially executed (still pending);
filled: order fully executed (completed);
part_canceled: order partially executed and then canceled;
canceled: the order is canceled; to maintain server performance, any canceled orders without execution will not be saved.
contract_type
linear: linear contract (USDT-margined contract), which uses USDT or other stable coins as quote currency, settlement currency, and margin.
inverse: inverse contract (Coin-margined contract), which uses the base currency for both settlement and margin, while USD is used as the quote currency.
margin_mode
isolated: isolated margin. In Isolated Margin mode, the margin for each position is separate and cannot be shared with other positions. The system won't add margin automatically, and any additional margin needs to be manually added by the user.
cross: cross margin. In Cross Margin mode, all available balances in the Futures account can be used as a shared margin for all current positions. To avoid forced liquidation, the system will add margin automatically by using the available balance in the Futures account.
take_profit_type
latest_price: current market price
mark_price: mark price
index_price: index price
stop_loss_type
latest_price: current market price
mark_price: mark price
index_price: index price
position_side
short: short position
long: long position
position_finished_type
liq: Close position by forced liquidation
adl: Close position by ADL
sys: Close position by system
limit: Close position at limit price
market: Close position at market price
market_close_all: Close all positions at market price
take_profit: Take profit and close position
stop_loss: Stop loss and close position
trigger_price_type
latest_price: current market price
mark_price: mark price
index_price: index price
transcation_type
deposit: Deposit
withdraw: Withdraw
trade: Trade
maker_cash_back: Maker cashback
investment_interest: Earn transfer
exchange_order_transfer: Swap
amm_type
infinite: Infinite interval
finite: Finite interval






Get Maintenance Information
Info
The protection period refers to a continuous period following the system maintenance (It's an optional configuration, and may or may not be set). During the protection period, you can cancel orders, place orders (limited to Maker Only Limit Orders), and adjust (add or reduce) margins.

HTTP request
GET /maintain/info

Request parameters
None

Return parameters
Parameter Name	Type	Notes
started_at	int	Maintenance start time (ms)
ended_at	int	Maintenance end time (ms)
scope	[]string	Maintenance scope:
FUTURES: Futures
SPOT: Spot
ALL_SITE: Overall maintenance
announce_url	string	Announcement link
announce_enabled	bool	Is there an announcement link
protect_duration_start	int	Protection period start time (ms)
protect_duration_end	int	Protection period end time, unit: milliseconds
Request example
GET /maintain-info

Response example
{
    "data": [
        {
            "started_at": 1713852000000,
            "ended_at": 1713852120000,
            "protect_duration_start": 0,
            "protect_duration_end": 0,
            "announce_enabled": false,
            "announce_url": "",
            "scope": [
                "ALL_SITE"
            ]
        },
        {
            "started_at": 1713974400000,
            "ended_at": 1714147200000,
            "protect_duration_start": 1714147200000,
            "protect_duration_end": 1714148100000,
            "announce_enabled": true,
            "announce_url": "https://www.coinex.com/zh-hans/announcements/detail/25997652101012",
            "scope": [
                "SPOT"
            ]
        }
    ],
    "code": 0,
    "message": "OK"
}





Ping
HTTP request
GET /ping

Request parameters
None

Return parameters
Parameter Name	Type	Notes
result	string	pong
Request example
GET /ping

Response example
{
    "code": 0,
    "message": "OK",
    "data": {
        "result": "pong",
    }
}


Get System Time
HTTP request
GET /time

Request parameters
None

Return parameters
Parameter Name	Type	Notes
timestamp	int	Server timestamp, unit: millisecond
Request example
GET /time

Response example
{
    "code": 0,
    "message": "OK",
    "data": {
        "timestamp": 1642231731234,
    }
}



Subscribe System Notice
Reminder
Before using this endpoint, please call the "server.sign" method for signature authorization.
The push delay of this method is: real-time
Subscribe System Notice
Method: notice.subscribe
Parameters:
Parameter Name	Required	Type	Notes
channels	true	[]int	Channel list, currently only supports system maintenance subscription 101
Example:
// Subscribe system maintenance
{
    "method": "notice.subscribe",
    "params": {
        "channels": [
            101
        ]
    },
    "id": 1
}

System Notice Push
Method: notice.update
Parameters:
Parameter Name	Type	Notes
channel	int	Channel, currently only supports system maintenance 101
info	object	notification info
Example:
// System maintenance push
{
    "method": "notice.update",
    "data": {
        "channel": 101,
        "info": {
            "start_time": 1640793607122,
            "end_time": 1640793600122,
            "scope": [
                "FUTURES",
                "SPOT"
            ],
            "protect_duration_start": 1640793600122,
            "protect_duration_end": 1640794200321
        }
    },
    "id": null
}

Unsubscribe System Notice
Method: notice.unsubscribe
Parameters:
Parameter Name	Required	Type	Notes
channels	true	[]int	Channel list, currently only supports system maintenance subscription 101,
null means canceling all subscriptions
Example:
// Unsubscribe system maintenance
{
    "method": "notice.unsubscribe",
    "params": {
        "channels": [
            101
        ]
    },
    "id": 1
}
// Unsubscribe all system notice
{
    "method": "notice.unsubscribe",
    "params": {
        "channels": []
    },
    "id": 1
}




Ping
Request
Method: server.ping

Example: {
    "method": "server.ping",
    "params": {},
    "id": 1
}

Response
Example: {
    "id": 1,
    "code": 0,
    "data": {
        "result": "pong"
    },
    "message": "OK"
}




Signature Authentication
Request Authorization
Method: server.sign
Parameters:
Parameter Name	Required	Type	Notes
access_id	true	string	API access id
signed_str	true	string	Signature string
timestamp	true	int	Timestamp (millisecond)
Example:
// Authorization
{
    "method": "server.sign",
    "params": {
        "access_id": "ABCDEFGHIJK1234567890",
        "signed_str": "1234567890abcdefghijk",
        "timestamp": 1234567890123
    },
    "id": 1
}

Authorization Response
Example:
// success
{
    "id": 1,
    "code": 0,
    "message": "OK"
}
// fail
{
    "id": 1,
    "code": 21002,
    "message": ""
}

















TickerHTTP EndpointGet Market Status
Get Market Status
HTTP request
GET /spot/market

Request parameters
Parameter Name	Required	Type	Notes
market	false	string	List of market names. Use "," to separate multiple market names, a maximum of 10 markets are allowed. An empty string or pass to query all markets.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
maker_fee_rate	string	Maker fee rate
taker_fee_rate	string	Taker fee rate
min_amount	string	Min. transaction volume
base_ccy	string	Base currency
quote_ccy	string	Quote currency
base_ccy_precision	int	Base currency decimal
quote_ccy_precision	int	Quote currency decimal
status	string	Market Status
delisted_at	int	Expected time to be delisted, in milliseconds
is_amm_available	bool	Whether to enable AMM function
is_margin_available	bool	Whether to enable margin trading
is_pre_market_trading_available	bool	Whether to enable pre-market trading
is_api_trading_available	bool	Whether to enable API trading
Request example
GET /spot/market?market=BTCUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": "BTCUSDT",
            "taker_fee_rate": "0.002",
            "maker_fee_rate": "0.002",
            "min_amount": "0.0005",
            "base_ccy": "BTC",
            "quote_ccy": "USDT",
            "base_ccy_precision": 8,
            "quote_ccy_precision": 2,
            "status": "online",
            "delisted_at": 1819704600000,
            "is_amm_available": true,
            "is_margin_available": true,
            "is_pre_trading_available": true,
            "is_api_trading_available": true,
        }
    ],
    "message": "OK"
}



Get Market Information
HTTP request
GET /spot/ticker

Request parameters
Parameter Name	Required	Type	Notes
market	false	string	List of market names. Use "," to separate multiple market names, a maximum of 10 markets are allowed. An empty string or pass to query all markets.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
last	string	Latest price
open	string	Opening price
close	string	Closing price
high	string	Highest price
low	string	Lowest price
volume	string	Filled volume
value	string	Filled value
volume_sell	string	Taker sell volume
volume_buy	string	Taker buy volume
period	int	Period, fixed at 86400, indicates that the data is a one-day value
Response example
GET /spot/ticker?market=LATUSDT,ELONUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": "LATUSDT",
            "last": "0.008157",
            "open": "0.008286",
            "close": "0.008157",
            "high": "0.008390",
            "low": "0.008106",
            "volume": "807714.49139758",
            "volume_sell": "286170.69645599",
            "volume_buy": "266161.23236408",
            "value": "6689.21644207",
            "period": 86400
        },
        {
            "market": "ELONUSDT",
            "last": "0.000000152823",
            "open": "0.000000158650",
            "close": "0.000000152823",
            "high": "0.000000159474",
            "low": "0.000000147026",
            "volume": "88014042237.15",
            "volume_sell": "11455578769.13",
            "volume_buy": "17047669612.10",
            "value": "13345.65122447",
            "period": 86400
        }
    ],
    "message": "OK"
}

Get Market Depth
HTTP request
GET /spot/depth

Request parameters
Parameter Name	Required	Type	Notes
market	true	string	Market name
limit	true	int	Number of depth data items.
One of [5, 10, 20, 50]
interval	true	string	Merge interval.
One of ["0", "0.00000000001", "0.000000000001", "0.0000000001", "0.000000001", "0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01", "0.1", "1", "10", "100", "1000"]
Return parameters
Parameter Name	Type	Notes
market	string	Market name
is_full	bool	True means full push, and false means incremental push
depth	object	Depth data
depth.asks	array	Seller data
asks[n][0]	string	Seller price
asks[n][1]	string	Seller size. During incremental push, a value of 0 indicates the depth at which the price needs to be deleted.
depth.bids	array	Buyer data
bids[n][0]	string	Buyer price
bids[n][1]	string	Buyer size. During incremental push, a value of 0 indicates the depth at which the price needs to be deleted.
depth.last	string	Latest price
depth.updated_at	int	Timestamp, millisecond
depth.checksum	string	Data checksum
Reminder
About Depth Checksum:

The checksum is a signed 32-bit integer of the full depth data, used to verify the accuracy of the depth data.
Construct the checksum string: bid1_price:bid1_amount:bid2_price:bid2_amount:ask1_price:ask1_amout:... (if there is no bid, the checksum string will be ask1_price:ask1_amount:ask2_price:ask2_amount:...)
Encode the checksum string using crc32 algorithm
Please check out the Code Examples to see how to use both full and incremental data pushes in the API client to recover complete depth data and verify its accuracy.

Request example
GET /spot/depth?market=BTCUSDT&limit=5&interval=0.01

Response example
{
    "code": 0,
    "data": {
        "market": "BTCUSDT",
        "is_full": true,
        "depth": {
            "asks": [
                [
                    "30740.00",
                    "0.31763545"
                ],
                [
                    "30769.00",
                    "1.45155000"
                ]
            ],
            "bids": [
                [
                    "30736.00",
                    "0.04857373"
                ],
                [
                    "30733.00",
                    "0.84696320"
                ],
                [
                    "30725.00",
                    "0.12563353"
                ],
                [
                    "30422.00",
                    "0"
                ]
            ],
            "last": "30746.28",
            "updated_at": 1689152421692,
            "checksum": 2578768879
        }
    },
    "message": "OK"
}

Get Market Transactions
HTTP request
GET /spot/deals

Request parameters
Parameter Name	Required	Type	Notes
market	true	string	Market name
limit	false	int	Number of transaction data items.
Default as 100, max. value 1000.
last_id	false	int	The starting point of the query TxID, 0 means to acquire from the latest record
Return parameters
Parameter Name	Type	Notes
deal_id	int	deal id
created_at	int	Transaction timestamp (millisecond)
side	string	Taker side, "buy" or "sell"
price	string	Filled price
amount	string	Executed Amount
Request example
GET /spot/deals?market=BTCUSDT

Response example
{
    "code": 0,
    "data":  [
        {
            "deal_id": 3514376759,
            "created_at": 1689152421692,
            "side": "buy",
            "price": "30718.42",
            "amount": "0.00000325"
        },
        {
            "deal_id": 3514376758,
            "created_at": 1689152421692,
            "side": "buy",
            "price": "30718.42",
            "amount": "0.00015729"
        },
        {
            "deal_id": 3514376757,
            "created_at": 1689152421692,
            "side": "sell",
            "price": "30718.42",
            "amount": "0.00154936"
        }
    ],
    "message": "OK"
}


Get Market Candlestick
HTTP request
GET /spot/kline

Request parameters
Parameter Name	Required	Type	Notes
market	true	string	Market name
price_type	false	string	Price type for drawing candlesticks, default as latest_price, no mark_price in spot markets
limit	false	int	Number of transaction data items.
Default as 100, max. value 1000
period	true	string	Candlestick period.
One of ["1min", "3min", "5min", "15min", "30min", "1hour", "2hour", "4hour", "6hour", "12hour", "1day", "3day", "1week"]
start_time	false	int	Query start time.
Data will not be filtered based on time by default
end_time	false	int	Query end time.
Data will not be filtered based on time by default
Return parameters
Parameter Name	Type	Notes
market	string	Market name
created_at	int	Timestamp (millisecond)
open	string	Opening price
close	string	Closing price
high	string	Highest price
low	string	Lowest price
volume	string	Filled volume
value	string	Filled value
Response example
GET /spot/kline?market=LATUSDT&limit=1&period=1day

Response example
{
    "code": 0,
    "data": [
        {
            "market": "LATUSDT",
            "created_at": 17017617600000,
            "open": "0.008286",
            "close": "0.008157",
            "high": "0.008390",
            "low": "0.008106",
            "volume": "807714.49139758",
            "value": "6689.21644207"
        }
    ],
    "message" : "OK"
}


Get Market Index
HTTP request
GET /spot/index

Request parameters
Parameter Name	Required	Type	Notes
market	false	string	List of market names. Use "," to separate multiple market names, a maximum of 10 markets are allowed. An empty string or pass to query all markets.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
created_at	int	Transaction timestamp (milliseconds)
price	string	Index price
sources	array	Index component
sources[n].exchange	string	Exchange name
sources[n].created_at	int	Data collection time
sources[n].index_weight	string	Index weight
sources[n].index_price	string	Index price
Request example
GET /spot/index?market=BTCUSDT

Response example
{
    "code": 0,
    "data":  [
        {
            "market": "BTCUSDT",
            "created_at": 1689152421692,
            "price": "30718.42",
            "sources": [
                {
                    "exchange": "kucoin",
                    "created_at": 1689152421685,
                    "index_weight": "1.00000000",
                    "index_price": "30718.42"
                }
            ]
        }
    ],
    "message": "OK"
}


Market Status Subscription
Info
Subscribe to 24h market status
The push delay of this method is about：200ms
24h Market Status Subscription
Method: state.subscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to subscribe to all markets.
Subscription example:
// Subscribe to a singular market
{
    "method": "state.subscribe",
    "params": {"market_list": ["BTCUSDT"]},
    "id": 1
}

// Subscribe to multiple markets
{
    "method": "state.subscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT", "BNBUSDT"]},
    "id": 1
}

// Subscribe to all markets
{
    "method": "state.subscribe",
    "params": {"market_list": []},
    "id": 1
}

24h Market Status Push
Method: state.update
Parameters:
Parameter Name	Type	Notes
market	string	Market name
last	string	Latest price
open	string	Opening price
close	string	Closing price
high	string	Highest price
low	string	Lowest price
volume	string	Filled volume
value	string	Filled value
volume_sell	string	Best ask size
volume_buy	string	Best bid size
period	int	Period, fixed at 86400, indicates that the data is a one-day value
Subscription example:
{
    "method": "state.update",
    "data": {
        "state_list": [
            {
                "market": "LATUSDT",
                "last": "0.008157",
                "open": "0.008286",
                "close": "0.008157",
                "high": "0.008390",
                "low": "0.008106",
                "volume": "807714.49139758",
                "volume_sell": "286170.69645599",
                "volume_buy": "266161.23236408",
                "value": "6689.21644207",
                "period": 86400
            },
            {
                "market": "ELONUSDT",
                "last": "0.000000152823",
                "open": "0.000000158650",
                "close": "0.000000152823",
                "high": "0.000000159474",
                "low": "0.000000147026",
                "volume": "88014042237.15",
                "volume_sell": "11455578769.13",
                "volume_buy": "17047669612.10",
                "value": "13345.65122447",
                "period": 86400,
            }
        ]
    },
    "id": null
}

Cancel Market Status Data Subscription
Method: state.unsubscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to unsubscribe to all markets.
Unsubscribe example:
// Cancel all subscribed markets
{
    "method": "state.unsubscribe",
    "params": {"market_list": []},
    "id": 1
}

// Cancel a singular subscribed market
{
    "method": "state.unsubscribe",
    "params": {"market_list": ["BTCUSDT"]},
    "id": 1
}

// Cancel multiple subscribed markets
{
    "method": "state.unsubscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT", "BNBUSDT"]},
    "id": 1
}


Market Depth Subscription
Info
The push delay of this method is about：200ms
Market Depth Subscription
Method: depth.subscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list[n][0]	true	string	market name.
market_list[n][1]	true	int	limit, number of push depth items, one of [5, 10, 20, 50]
market_list[n][2]	true	string	interval, merge interval, one of ["0", "0.00000000001", "0.000000000001", "0.0000000001", "0.000000001", "0.00000001", "0.0000001", "0.000001", "0.00001", "0.00 01", "0.001", "0.01", "0.1", "1", "10", "100", "1000"]
market_list[n][3]	true	bool	if_full, whether it is a full subscription
Subscription example
{
  "method": "depth.subscribe",
  "params": {"market_list": [
        ["BTCUSDT", 10, "0", true],
        ["ETHUSDT", 10, "0", false]
    ]
  },
  "id": 1
}

Depth Push
Method: depth.update
Parameters:
Parameter Name	Type	Notes
market	string	Market name
is_full	bool	True means full push, and false means incremental push
depth	object	Depth data
depth.asks	array	Seller data
asks[n][0]	string	Seller price
asks[n][1]	string	Seller size. During incremental push, a value of 0 indicates the depth at which the price needs to be deleted.
depth.bids	array	Buyer data
bids[n][0]	string	Buyer price
bids[n][1]	string	Buyer size. During incremental push, a value of 0 indicates the depth at which the price needs to be deleted.
depth.last	string	Latest price
depth.updated_at	int	Timestamp, millisecond
depth.checksum	string	Data checksum
Reminder
About incremental and full depth push:

Incremental push: Each push delivers the depth data updated from the last push to the present time.In every 200 milliseconds. No push if there is no depth update.
Full push: Each push delivers the complete depth data.In every 200 milliseconds. No push if there is no depth update.
For multiple market subscriptions, use the market params to separate push messages in different markets.
Full market depth push is delivered every 1 minute.
About Depth Checksum:

The checksum is a signed 32-bit integer of the full depth data, used to verify the accuracy of the depth data.
Construct the checksum string: bid1_price:bid1_amount:bid2_price:bid2_amount:ask1_price:ask1_amout:... (if there is no bid, the checksum string will be ask1_price:ask1_amount:ask2_price:ask2_amount:...)
Encode the checksum string using crc32 algorithm
Please check out the Code Examples to see how to use both full and incremental data pushes in the API client to recover complete depth data and verify its accuracy.

Push example
{
    "method": "depth.update",
    "data": {
        "market": "BTCUSDT",
        "is_full": true,
        "depth": {
            "asks": [
                [
                    "30740.00",
                    "0.31763545"
                ],
                [
                    "30769.00",
                    "1.45155000"
                ]
            ],
            "bids": [
                [
                    "30736.00",
                    "0.04857373"
                ],
                [
                    "30733.00",
                    "0.84696320"
                ],
                [
                    "30725.00",
                    "0.12563353"
                ],
                [
                    "30422.00",
                    "0"
                ]
            ],
            "last": "30746.28",
            "updated_at": 1689152421692,
            "checksum": 2578768879
        }
    },
    "id": null
}

Cancel Market Depth Subscription
Method: depth.unsubscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to unsubscribe to all markets.
Unsubscribe example:
// unsubscribe to singular market depth
{
  "method": "depth.unsubscribe",
  "params": {"market_list": ["BTCUSDT"]},
  "id": 1
}

// unsubscribe to multiple market depths
{
  "method": "depth.unsubscribe",
  "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
  "id": 1
}

// unsubscribe to all market depths
{
  "method": "depth.unsubscribe",
  "params": {"market_list": []},
  "id": 1
}


Market Transaction Subscription
Info
The push delay of this method is about：200ms
Market Transaction Subscription
Method: deals.subscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to subscribe to all markets.
Subscription example:
// Subscribe to a singular market
{
  "method": "deals.subscribe",
  "params": {"market_list": ["BTCUSDT"]},
  "id": 1
}

// Subscribe to multiple markets
{
  "method": "deals.subscribe",
  "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
  "id": 1
}

// Subscribe to all markets
{
  "method": "deals.subscribe",
  "params": {"market_list": []},
  "id": 1
}

Latest Market Transaction Push
Method: deals.update
Parameters:
Parameter Name	Type	Notes
market	string	Market name
deal_list	array	List of latest transactions
deal_list[n].deal_id	int	deal id
deal_list[n].created_at	int	Transaction timestamp (milliseconds)
deal_list[n].side	string	Taker side, "buy" or "sell"
deal_list[n].price	string	Filled price
deal_list[n].amount	string	Executed Amount
Example:
// market's deal
{
    "method": "deals.update",
    "data": {
        "market": "BTCUSDT",
        "deal_list": [
            {
                "deal_id": 3514376759,
                "created_at": 1689152421692,
                "side": "buy",
                "price": "30718.42",
                "amount": "0.00000325"
            },
            {
                "deal_id": 3514376758,
                "created_at": 1689152421692,
                "side": "buy",
                "price": "30718.42",
                "amount": "0.00015729"
            },
            {
                "deal_id": 3514376757,
                "created_at": 1689152421692,
                "side": "sell",
                "price": "30718.42",
                "amount": "0.00154936"
            }
        ]
    },
    "id": null
}

Cancel Latest Market Transaction Subscription
Method: deals.unsubscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to unsubscribe to all markets.
Example:
// Cancel a singular subscription
{
    "method": "deals.unsubscribe",
    "params": {"market_list": ["BTCUSDT"]},
    "id": 1
}

// Cancel multiple subscriptions

{
    "method": "deals.unsubscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
    "id": 1
}

// Cancel all subscriptions
{
    "method": "deals.unsubscribe",
    "params": {"market_list": []},
    "id": 1
}


Info
The push delay of this method is about：5000ms
Market Index Subscription
Method: index.subscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names
Example:
// Subscribe to a singular market
{
    "method": "index.subscribe",
    "params": {"market_list": ["BTCUSDT"]},
    "id": 1
}

// Subscribe to multiple markets
{
    "method": "index.subscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
    "id": 1
}

Market Index Price Push
Method: index.update
Parameters:
Parameter Name	Type	Notes
market	string	Market name
index_price	string	Index price
Example
{
    "method": "index.update",
    "data": {
        "market": "BTCUSDT",
        "index_price": "40000.91"
    }, 
    "id": null
}

Cancel Index Price Subscription
Method: index.unsubscribe
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to unsubscribe to all markets.
Example:
// Unsubscribe to a singular market
{
    "method": "index.unsubscribe",
    "params": {"market_list": ["ETHUSDT"]},
    "id": 1
}

// Unsubscribe to multiple markets
{
    "method": "index.unsubscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
    "id": 1
}

// Unsubscribe to all markets
{
    "method": "index.unsubscribe",
    "params": {"market_list": []},
    "id": 1
}


BBO (Best-bid-offer) Subscription
Info
The push delay of this method is: real-time
BBO (Best-bid-offer) Subscription
Method: bbo.subscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names
Example:
// Subscribe to a singular market
{
    "method": "bbo.subscribe",
    "params": {"market_list": ["BTCUSDT"]},
    "id": 1
}

// Subscribe to multiple markets
{
    "method": "bbo.subscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
    "id": 1
}

BBO (Best-bid-offer) Update Push
Method: bbo.update
Parameters:
Parameter Name	Type	Notes
market	string	Market name
updated_at	int	Timestamp (millisecond)
best_bid_price	string	Best bid price
best_bid_size	string	Best bid size
best_ask_price	string	Best ask price
best_ask_size	string	Best ask size
Example
{
    "method": "bbo.update",
    "data": {
        "market": "BTCUSDT",
        "updated_at": 1642145331234,
        "best_bid_price": "20000",
        "best_bid_size": "0.1",
        "best_ask_price": "20001",
        "best_ask_size": "0.15"
    },
    "id": null
}

Cancel BBO (Best-bid-offer) Subscription
Method: bbo.unsubscribe
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to unsubscribe to all markets.
Example:
// Unsubscribe to a singular market
{
    "method": "bbo.unsubscribe",
    "params": {"market_list": ["ETHUSDT"]},
    "id": 1
}

// Unsubscribe to multiple markets
{
    "method": "bbo.unsubscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
    "id": 1
}

// Unsubscribe to all markets
{
    "method": "bbo.unsubscribe",
    "params": {"market_list": []},
    "id": 1
}














Get Market Status
HTTP request
GET /futures/market

Request parameters
Parameter Name	Required	Type	Notes
market	false	string	List of market names. Use "," to separate multiple market names, a maximum of 10 markets are allowed. An empty string or pass to query all markets.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
contract_type	string	Contract Type
maker_fee_rate	string	Maker fee rate
taker_fee_rate	string	Taker fee rate
min_amount	string	Min. transaction volume
base_ccy	string	Base currency
quote_ccy	string	Quote currency
base_ccy_precision	int	Base currency decimal
quote_ccy_precision	int	Quote currency decimal
status	string	Market Status
delisted_at	int	Expected time to be delisted, in milliseconds
tick_size	string	Tick size
leverage	[]int	Leverage
open_interest_volume	string	Futures position size
is_market_available	bool	Whether the market is open
is_copy_trading_available	bool	Whether to enable copy trading
is_api_trading_available	bool	Whether to enable API trading
Request example
GET /futures/market?market=BTCUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": "BTCUSDT",
            "contract_type": "linear",
            "taker_fee_rate": "0.002",
            "maker_fee_rate": "0.002",
            "min_amount": "0.0005",
            "base_ccy": "BTC",
            "quote_ccy": "USDT",
            "base_ccy_precision": 8,
            "quote_ccy_precision": 2,
            "tick_size": "0.5",
            "delisted_at": 1819704600000,
            "is_market_available": true,
            "is_copy_trading_available": true,
            "is_api_trading_available": true,
            "leverage": ["3", "5", "8", "10", "15", "20", "30", "50", "100"],
            "open_interest_volume": "100"
        }
    ],
    "message": "OK"
}

HTTP request
Request parameters
Return parameters
Request example
Response example




TickerHTTP EndpointGet Market Information
Get Market Information
HTTP request
GET /futures/ticker

Request parameters
Parameter Name	Required	Type	Notes
market	false	string	List of market names. Use "," to separate multiple market names, a maximum of 10 markets are allowed. An empty string or pass to query all markets.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
last	string	Latest price
open	string	Opening price
close	string	Closing price
high	string	Highest price
low	string	Lowest price
volume	string	Filled volume
value	string	Filled value
volume_sell	string	Taker sell volume
volume_buy	string	Taker buy volume
index_price	string	Index price
mark_price	string	Mark price
open_interest_volume	string	Futures position size
period	int	Period, fixed at 86400, indicates that the data is a one-day value
Response example
GET /futures/ticker?market=LATUSDT,ELONUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": "LATUSDT",
            "last": "0.008157",
            "open": "0.008286",
            "close": "0.008157",
            "high": "0.008390",
            "low": "0.008106",
            "volume": "807714.49139758",
            "volume_sell": "286170.69645599",
            "volume_buy": "266161.23236408",
            "value": "6689.21644207",
            "index_price": "0.008158",
            "mark_price": "0.008158",
            "open_interest_volume": "2423143.47419274",
            "period": 86400
        },
        {
            "market": "ELONUSDT",
            "last": "0.000000152823",
            "open": "0.000000158650",
            "close": "0.000000152823",
            "high": "0.000000159474",
            "low": "0.000000147026",
            "volume": "88014042237.15",
            "volume_sell": "11455578769.13",
            "volume_buy": "17047669612.10",
            "value": "13345.65122447",
            "index_price": "0.000000152821",
            "mark_price": "0.000000152821",
            "open_interest_volume": "264042126711.45",
            "period": 86400,
        }
    ],
    "message": "OK"
}

HTTP request
Request parameters
Return parameters
Response example
Response example



TickerHTTP EndpointGet Market Depth
Get Market Depth
HTTP request
GET /futures/depth

Request parameters
Parameter Name	Required	Type	Notes
market	true	string	Market name
limit	true	int	Number of depth data items.
One of [5, 10, 20, 50]
interval	true	string	Merge interval.
One of ["0", "0.00000000001", "0.000000000001", "0.0000000001", "0.000000001", "0.00000001", "0.0000001", "0.000001", "0.00001", "0.0001", "0.001", "0.01", "0.1", "1", "10", "100", "1000"]
Return parameters
Parameter Name	Type	Notes
market	string	Market name
is_full	bool	True means full push, and false means incremental push
depth	object	Depth data
depth.asks	array	Seller data
asks[n][0]	string	Seller price
asks[n][1]	string	Seller size. During incremental push, a value of 0 indicates the depth at which the price needs to be deleted.
depth.bids	array	Buyer data
bids[n][0]	string	Buyer price
bids[n][1]	string	Buyer size. During incremental push, a value of 0 indicates the depth at which the price needs to be deleted.
depth.last	string	Latest price
depth.updated_at	int	Timestamp, millisecond
depth.checksum	string	Data checksum
Reminder
About Depth Checksum:

The checksum is a signed 32-bit integer of the full depth data, used to verify the accuracy of the depth data.
Construct the checksum string: bid1_price:bid1_amount:bid2_price:bid2_amount:ask1_price:ask1_amout:... (if there is no bid, the checksum string will be ask1_price:ask1_amount:ask2_price:ask2_amount:...)
Encode the checksum string using crc32 algorithm
Please check out the Code Examples to see how to use both full and incremental data pushes in the API client to recover complete depth data and verify its accuracy.

Request example
GET /futures/depth?market=BTCUSDT&limit=5&interval=0.01

Response example
{
    "code": 0,
    "data": {
        "market": "BTCUSDT",
        "is_full": true,
        "depth": {
            "asks": [
                [
                    "30740.00",
                    "0.31763545"
                ],
                [
                    "30769.00",
                    "1.45155000"
                ]
            ],
            "bids": [
                [
                    "30736.00",
                    "0.04857373"
                ],
                [
                    "30733.00",
                    "0.84696320"
                ],
                [
                    "30725.00",
                    "0.12563353"
                ],
                [
                    "30422.00",
                    "0"
                ]
            ],
            "last": "30746.28",
            "updated_at": 1689152421692,
            "checksum": 2578768879
        }
    },
    "message": "OK"
}

HTTP request
Request parameters
Return parameters
Request example
Response example



TickerHTTP EndpointGet Market Transactions
Get Market Transactions
HTTP request
GET /futures/deals

Request parameters
Parameter Name	Required	Type	Notes
market	true	string	Market name
limit	false	int	Number of transaction data items.
Default as 100, max. value 1000.
last_id	false	int	The starting point of the query TxID, 0 means to acquire from the latest record
Return parameters
Parameter Name	Type	Notes
deal_id	int	deal id
created_at	int	Transaction timestamp (milliseconds)
side	string	Taker side, "buy" or "sell"
price	string	Filled price
amount	string	Executed Amount
Request example
GET /futures/deals?market=BTCUSDT

Response example
{
    "code": 0,
    "data":  [
        {
            "deal_id": 3514376759,
            "created_at": 1689152421692,
            "side": "buy",
            "price": "30718.42",
            "amount": "0.00000325"
        },
        {
            "deal_id": 3514376758,
            "created_at": 1689152421692,
            "side": "buy",
            "price": "30718.42",
            "amount": "0.00015729"
        },
        {
            "deal_id": 3514376757,
            "created_at": 1689152421692,
            "side": "sell",
            "price": "30718.42",
            "amount": "0.00154936"
        }
    ],
    "message": "OK"
}

HTTP request
Request parameters
Return parameters
Request example
Response example



TickerHTTP EndpointGet Market Candlestick
Get Market Candlestick
HTTP request
GET /futures/kline

Request parameters
Parameter Name	Required	Type	Notes
market	true	string	Market name
price_type	false	string	Price type for drawing candlesticks, default as latest_price.
limit	false	int	Number of transaction data items.
Default as 100, max. value 1000.
period	true	string	Candlestick period.
One of ["1min", "3min", "5min", "15min", "30min", "1hour", "2hour", "4hour", "6hour", "12hour" , "1day", "3day", "1week"]
start_time	false	int	Query start time.
Data will not be filtered based on time by default
end_time	false	int	Query end time.
Data will not be filtered based on time by default
Return parameters
Parameter Name	Type	Notes
market	string	Market name
created_at	int	Timestamp (millisecond)
open	string	Opening price
close	string	Closing price
high	string	Highest price
low	string	Lowest price
volume	string	Filled volume
value	string	Filled value
Response example
GET /futures/kline?market=LATUSDT&limit=1&period=1day

Response example
{
    "code": 0,
    "data": [
        {
            "market": "LATUSDT",
            "created_at": 17017617600000,
            "open": "0.008286",
            "close": "0.008157",
            "high": "0.008390",
            "low": "0.008106",
            "volume": "807714.49139758",
            "value": "6689.21644207"
        }
    ],
    "message" : "OK"
}

HTTP request
Request parameters
Return parameters
Response example
Response example




TickerHTTP EndpointGet Market Index
Get Market Index
HTTP request
GET /futures/index

Request parameters
Parameter Name	Required	Type	Notes
market	false	string	List of market names. Use "," to separate multiple market names, a maximum of 10 markets are allowed. An empty string or pass to query all markets.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
created_at	int	Transaction timestamp (milliseconds)
price	string	Index price
sources	array	Index component
sources[n].exchange	string	Exchange name
sources[n].created_at	int	Data collection time
sources[n].index_weight	string	Index weight
Request example
GET /futures/index?market=BTCUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": "BTCUSDT",
            "created_at": 1703561120000,
            "price": "30718.42",
            "sources": [
                {
                    "created_at": 1703561102173,
                    "exchange" : "binance",
                    "index_weight": "0.25"
                },
                {
                    "created_at": 1703561124859,
                    "exchange": "coinex",
                    "index_weight": "0.25"
                },
                {
                    "created_at": 1703561123704,
                    "exchange": " meexc",
                    "index_weight": "0.25"
                },
                {
                    "created_at": 1703561125040,
                    "exchange": "bybit ",
                    "index_weight": "0.25"
                }
            ]
        }
    ],
    "message": "OK "
}

HTTP request
Request parameters
Return parameters
Request example
Response example



TickerHTTP EndpointGet Market Funding Rate
Get Market Funding Rate
HTTP request
GET /futures/funding-rate

Request parameters
Parameter Name	Required	Type	Notes
market	false	string	List of market names. Use "," to separate multiple market names, a maximum of 10 markets are allowed. An empty string or pass to query all markets.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
mark_price	string	Mark price
latest_funding_rate	string	Current funding rate. The funding rate at the current settlement time, calculated every minute, for reference only.
If the funding rate is positive, the long positions pay the short side;
If the funding rate is negative, the short positions pay the long side.
next_funding_rate	string	Next funding rate. Consistent with the current funding rate.At the time of funding rate collection, the predicted funding rate = current funding rate
max_funding_rate	string	Max. funding rate.The upper limit of the funding rate at the current market.
min_funding_rate	string	Min. funding rate.The lower limit of the funding rate at the current market.
latest_funding_time	int	The time when the current funding rate is collected. Funding rates are calculated every minute and are paid/collected once every 8 hours by default. When the premium rate is too high, it can be dynamically adjusted to 2h or 4h.
next_funding_time	int	The time when the next funding rate will be collected. Funding rates are calculated every minute and are paid/collected once every 8 hours by default. When the premium rate is too high, it can be dynamically adjusted to 2h or 4h.
Response example
GET /futures/funding-rate?market=LATUSDT,ELONUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": "LATUSDT",
            "mark_price": "0.008157",
            "latest_funding_rate": "-0.00007488",
            "next_funding_rate": "-0.00027732",
            "max_funding_rate": "0.00375",
            "min_funding_rate": "-0.00375",
            "latest_funding_time": 1642145331234,
            "next_funding_time": 1642231731234
        },
        {
            "market": "ELONUSDT",
            "mark_price": "0.000000152823",
            "latest_funding_rate": "-0.00003688",
            "next_funding_rate": "-0.00013372",
            "max_funding_rate": "0.00375",
            "min_funding_rate": "-0.00375",
            "latest_funding_time": 1642145331234,
            "next_funding_time": 1642231731234
        }
    ],
    "message": "OK"
}

HTTP request
Request parameters
Return parameters
Response example
Response example


TickerHTTP EndpointGet Market Funding Rate History
Get Market Funding Rate History
HTTP request
GET /futures/funding-rate-history

Request parameters
Parameter Name	Required	Type	Notes
market	true	string	Market name
start_time	false	int	Query start time.
Data will not be filtered based on time by default
end_time	false	int	Query end time.
Data will not be filtered based on time by default
page	false	int	Number of pagination. Default is 1.
limit	false	int	Number in each page. Default is 10.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
funding_time	int	Funding rate collection time
theoretical_funding_rate	string	Theoretical funding rate. The theoretical funding rate to be collected for the current period after calculation
actual_funding_rate	string	Actual funding rate. The actual funding rate charged in the current period
Response example
GET /futures/funding-rate-history?market=LATUSDT,ELONUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": "LATUSDT",
            "funding_time": 1642145331234,
            "theoretical_funding_rate": "-0.00007488",
            "actual_funding_rate": "-0.00027732"
        },
        {
            "market": "ELONUSDT",
            "funding_time": 1642145331234,
            "theoretical_funding_rate": "-0.00003688",
            "actual_funding_rate": "-0.00013372"
        }
    ],
    "pagination": {
        "has_next": false
    },
    "message": "OK"
}

HTTP request
Request parameters
Return parameters
Response example
Response example




TickerHTTP EndpointGet Market Premium Index Price History
Get Market Premium Index Price History
HTTP request
GET /futures/premium-index-history

Request parameters
Parameter Name	Required	Type	Notes
market	true	string	Market name
start_time	false	int	Query start time.
Query the data in the past 8 hours by default. The query time range cannot be greater than 1 day, and the maximum query time is the data of the past 30 days.
end_time	false	int	Query end time.
Query the data in the past 8 hours by default. The query time range cannot be greater than 1 day, and the maximum query time is the data of the past 30 days.
page	false	int	Number of pagination. Default is 1.
limit	false	int	Number in each page. Default is 10.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
created_at	int	Data creation time
premium_index	string	Premium index. The main basis for calculating the funding rate
Response example
GET /futures/premium-index-history?market=LATUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": "LATUSDT",
            "created_at": 1642145400000,
            "premium_index": "-0.00027732"
        },
        {
            "market": "LATUSDT",
            "created_at": 1642146000000,
            "premium_index": "-0.00013372"
        }
    ],
    "message": "OK"
}

HTTP request
Request parameters
Return parameters
Response example
Response example



TickerHTTP EndpointGet Market Position Level
Get Market Position Level
HTTP request
GET /futures/position-level

Request parameters
Parameter Name	Required	Type	Notes
market	false	string	List of market names. Use "," to separate multiple market names, a maximum of 10 markets are allowed. An empty string or pass to query all markets.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
level	[]object	Position Level
level[n].amount	string	Upper limit of the current position
level[n].leverage	string	Leverage of current level
level[n].maintenance_margin_rate	string	Current maintenance margin rate
level[n].min_initial_margin_rate	string	Minimum initial margin rate for the current level
Response example
GET /futures/position-level?market=BTCUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": "BTCUSDT",
            "level": [
                {"amount": "20", "leverage": "100", "maintenance_margin_rate": "0.005", "min_initial_margin_rate": "0.01"},
                {"amount": "50", "leverage": "50", "maintenance_margin_rate": "0.01", "min_initial_margin_rate": "0.02"},
                {"amount": "100", "leverage": "30", "maintenance_margin_rate": "0.015", "min_initial_margin_rate": "0.0333"},
                {"amount": "200", "leverage": "20", "maintenance_margin_rate": "0.02", "min_initial_margin_rate": "0.05"},
                {"amount": "500", "leverage": "15", "maintenance_margin_rate": "0.025", "min_initial_margin_rate": "0.06"},
                {"amount": "1000", "leverage": "10", "maintenance_margin_rate": "0.03", "min_initial_margin_rate": "0.1"},
            ]
        }
    ],
    "message": "OK"
}

HTTP request
Request parameters
Return parameters
Response example
Response example



TickerHTTP EndpointGet Market Liquidation History
Get Market Liquidation History
HTTP request
GET /futures/liquidation-history

Request parameters
Parameter Name	Required	Type	Notes
market	true	string	Market name
start_time	false	int	Query start time.
Data will not be filtered based on time by default
end_time	false	int	Query end time.
Data will not be filtered based on time by default
page	false	int	Number of pagination. Default is 1.
limit	false	int	Number in each page. Default is 10.
Return parameters
Parameter Name	Type	Notes
market	string	Market name
side	string	Position side
liq_price	string	Liquidation price.
(Long position) Forced liquidation price = Settlement price * (1 - forced liquidation margin rate)/(1 - maintenance margin rate)
(Short position) Forced liquidation price = Settlement price * (1 + forced liquidation margin rate)/(1 + maintenance margin rate)
liq_amount	string	Liquidation amount
bkr_price	string	Bankruptcy price.
(Long position) Bankruptcy price = Settlement price * (1 - forced liquidation margin rate)
(Short position) Bankruptcy price = Settlement price * (1 + liquidation margin rate)
created_at	int	Data creation time
Response example
GET /futures/liquidation-history?market=LATUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": " LATUSDT",
            "side": "long",
            "liq_price": "0.009061",
            "liq_amount": "184378262",
            "bkr_price": "0.009038",
            "created_at": 1691482451000
        },
        {
            "market": " LATUSDT",
            "side": "long",
            "liq_price": "0.009030",
            "liq_amount": "375947238",
            "bkr_price": "0.009016",
            "created_at": 1691482829000
        }
    ],
    "pagination": {
        "has_next": false
    },
    "message": "OK"
}

HTTP request
Request parameters
Return parameters
Response example
Response example



TickerHTTP EndpointGet Market Basis Rate History
Get Market Basis Rate History
HTTP request
GET /futures/basis-history

Request parameters
Parameter Name	Required	Type	Notes
market	true	string	Market name
start_time	false	int	Query start time.
Data will not be filtered based on time by default
Acquiring data of last 7 days by default
end_time	false	int	Query end time.
Data will not be filtered based on time by default
Acquiring data of last 7 days by default
Return parameters
Parameter Name	Type	Notes
market	string	Market name
created_at	int	Data creation time
basis_rate	string	Basis rate
Response example
GET /futures/basis-history?market=LATUSDT

Response example
{
    "code": 0,
    "data": [
        {
            "market": "LATUSDT",
            "created_at": 1642145400000,
            "basis_rate": "-0.00027732"
        },
        {
            "market": "LATUSDT",
            "funding_time": 1642146000000,
            "basis_rate": "-0.00013372"
        }
    ],
    "message": "OK"
}

HTTP request
Request parameters
Return parameters
Response example
Response example




TickerWS EndpointMarket Status Subscription
Market Status Subscription
Info
Subscribe to 24h market status
The push delay of this method is about：200ms
24h Market Status Subscription
Method: state.subscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to subscribe to all markets.
Subscription example:
// Subscribe to a singular market
{
    "method": "state.subscribe",
    "params": {"market_list": ["BTCUSDT"]},
    "id": 1
}

// Subscribe to multiple markets
{
    "method": "state.subscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT", "BNBUSDT"]},
    "id": 1
}

// Subscribe to all markets
{
    "method": "state.subscribe",
    "params": {"market_list": []},
    "id": 1
}

24h Market Status Push
Method: state.update
Parameters:
Parameter Name	Type	Notes
market	string	Market name
last	string	Latest price
open	string	Opening price
close	string	Closing price
high	string	Highest price
low	string	Lowest price
volume	string	24H volume
value	string	24h value
volume_sell	string	Best ask size
volume_buy	string	Best bid size
insurance_fund_size	string	Insurance fund amount
mark_price	string	Mark price
index_price	string	Index price
open_interest_size	string	Current position
latest_funding_rate	string	Current funding rate.The funding rate at the current settlement time, calculated every minute, for reference only.
If the funding rate is positive, the long positions pay the short side;
If the funding rate is negative, the short positions pay the long side.
next_funding_rate	string	Next funding rate.Consistent with the current funding rate.At the time of funding rate collection, the predicted funding rate = current funding rate
latest_funding_time	int	The time when the current funding rate is collected.Funding rates are calculated every minute and are paid/collected once every 8 hours by default. When the premium rate is too high, it can be dynamically adjusted to 2h or 4h.
next_funding_time	int	The time when the next funding rate will be collected.Funding rates are calculated every minute and are paid/collected once every 8 hours by default. When the premium rate is too high, it can be dynamically adjusted to 2h or 4h.
period	int	Period, fixed at 86400, indicates that the data is a one-day value
Subscription example:
{
    "method": "state.update",
    "data": {
        "state_list": [
            {
                "market": "ETHUSD_SIGNPRICE",
                "last": "1892.29",
                "open": "1884.62",
                "close": "1892.29",
                "high": "1894.09",
                "low": "1863.72",
                "volume": "0",
                "value": "0",
                "volume_sell": "0",
                "volume_buy": "0",
                "open_interest_size": "0",
                "insurance_fund_size": "0",
                "latest_funding_rate": "0",
                "next_funding_rate": "0",
                "latest_funding_time": 1642145331234,
                "next_funding_time": 1642231731234,
                "period": 86400
            },
            {
                "market": "DOTUSDT",
                "last": "5.2483",
                "open": "5.15690000000000000000",
                "close": "5.2483",
                "high": "5.30640000000000000000",
                "low": "5.09040000000000000000",
                "volume": "51996.00000000000000000000",
                "value": "269813.72216000000000000000",
                "volume_sell": "11747.70000000",
                "volume_buy": "14624.70000000",
                "open_interest_size": "92414.6",
                "insurance_fund_size": "24497980.15228462554747551920",
                "mark_price": "5.2513",
                "index_price": "5.2513",
                "latest_funding_rate": "-0.00012921",
                "next_funding_rate": "0.00009768",
                "latest_funding_time": 1642145331234,
                "next_funding_time": 1642231731234,
                "period": 86400
            }
        ]
    ],
    "id": null
}

Cancel Market Status Data Subscription
Method: state.unsubscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to unsubscribe to all markets.
Unsubscribe example:
// Cancel all subscribed markets
{
    "method": "state.unsubscribe",
    "params": {"market_list": []},
    "id": 1
}

// Cancel a singular subscribed market
{
    "method": "state.unsubscribe",
    "params": {"market_list": ["BTCUSDT"]},
    "id": 1
}

// Cancel multiple subscribed markets
{
    "method": "state.unsubscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT", "BNBUSDT"]},
    "id": 1
}

24h Market Status Subscription
24h Market Status Push
Cancel Market Status Data Subscription



TickerWS EndpointMarket Depth Subscription
Market Depth Subscription
Info
The push delay of this method is about：200ms
Market Depth Subscription
Method: depth.subscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list[n][0]	true	string	market name.
market_list[n][1]	true	int	limit, number of push depth items, one of [5, 10, 20, 50]
market_list[n][2]	true	string	interval, merge interval, one of ["0", "0.00000000001", "0.000000000001", "0.0000000001", "0.000000001", "0.00000001", "0.0000001", "0.000001", "0.00001", "0.00 01", "0.001", "0.01", "0.1", "1", "10", "100", "1000"]
market_list[n][3]	true	bool	if_full, whether it is a full subscription
Subscription example
{
    "method": "depth.subscribe",
    "params": {
        "market_list": [
            ["BTCUSDT", 10, "0", true],
            ["ETHUSDT", 10, "0", false]
        ]
    },
    "id": 1
}

Depth Push
Method: depth.update
Parameters:
Parameter Name	Type	Notes
market	string	Market name
is_full	bool	True means full push, and false means incremental push
depth	object	Depth data
depth.asks	array	Seller data
asks[n][0]	string	Seller price
asks[n][1]	string	Seller size. During incremental push, a value of 0 indicates the depth at which the price needs to be deleted.
depth.bids	array	Buyer data
bids[n][0]	string	Buyer price
bids[n][1]	string	Buyer size. During incremental push, a value of 0 indicates the depth at which the price needs to be deleted.
depth.last	string	Latest price
depth.updated_at	int	Timestamp (millisecond)
depth.checksum	string	Data checksum
Reminder
About incremental and full depth push:

Incremental push: Each push delivers the depth data updated from the last push to the present time.In every 200 milliseconds. No push if there is no depth update.
Full push: Each push delivers the complete depth data.In every 200 milliseconds. No push if there is no depth update.
For multiple market subscriptions, use the market params to separate push messages in different markets.
Full market depth push is delivered every 1 minute.
About Depth Checksum:

The checksum is a signed 32-bit integer of the full depth data, used to verify the accuracy of the depth data.
Construct the checksum string: bid1_price:bid1_amount:bid2_price:bid2_amount:ask1_price:ask1_amout:... (if there is no bid, the checksum string will be ask1_price:ask1_amount:ask2_price:ask2_amount:...)
Encode the checksum string using crc32 algorithm
Please check out the Code Examples to see how to use both full and incremental data pushes in the API client to recover complete depth data and verify its accuracy.

Push example
{
    "method": "depth.update",
    "data": {
        "market": "BTCUSDT",
        "is_full": true,
        "depth": {
            "asks": [
                [
                    "30740.00",
                    "0.31763545"
                ],
                [
                    "30769.00",
                    "1.45155000"
                ]
            ],
            "bids": [
                [
                    "30736.00",
                    "0.04857373"
                ],
                [
                    "30733.00",
                    "0.84696320"
                ],
                [
                    "30725.00",
                    "0.12563353"
                ],
                [
                    "30422.00",
                    "0"
                ]
            ],
            "last": "30746.28",
            "updated_at": 1689152421692,
            "checksum": 2578768879
        }
    },
    "id": null
}

Cancel Market Depth Subscription
Method: depth.unsubscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to unsubscribe to all markets.
Unsubscribe example:
// unsubscribe to singular market depth
{
  "method": "depth.unsubscribe",
  "params": {"market_list": ["BTCUSDT"]},
  "id": 1
}

// unsubscribe to multiple market depths
{
  "method": "depth.unsubscribe",
  "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
  "id": 1
}

// unsubscribe to all market depths
{
  "method": "depth.unsubscribe",
  "params": {"market_list": []},
  "id": 1
}

Market Depth Subscription
Depth Push
Cancel Market Depth Subscription



TickerWS EndpointMarket Transaction Subscription
Market Transaction Subscription
Info
The push delay of this method is about：200ms
Market Transaction Subscription
Method: deals.subscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to subscribe to all markets.
Subscription example:
// Subscribe to a singular market
{
  "method": "deals.subscribe",
  "params": {"market_list": ["BTCUSDT"]},
  "id": 1
}

// Subscribe to multiple markets
{
  "method": "deals.subscribe",
  "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
  "id": 1
}

// Subscribe to all markets
{
  "method": "deals.subscribe",
  "params": {"market_list": []},
  "id": 1
}

Latest Market Transaction Push
Method: deals.update
Parameters:
Parameter Name	Type	Notes
market	string	Market name
deal_list	array	List of latest transactions
deal_list[n].deal_id	int	Txid
deal_list[n].created_at	int	Transaction timestamp (milliseconds)
deal_list[n].side	string	Taker side, "buy" or "sell"
deal_list[n].price	string	Filled price
deal_list[n].amount	string	Executed Amount
Example:
// market's deal
{
    "method": "deals.update",
    "data": {
        "market": "BTCUSDT",
        "deal_list": [
            {
                "deal_id": 3514376759,
                "created_at": 1689152421692,
                "side": "buy",
                "price": "30718.42",
                "amount": "0.00000325"
            },
            {
                "deal_id": 3514376758,
                "created_at": 1689152421692,
                "side": "buy",
                "price": "30718.42",
                "amount": "0.00015729"
            },
            {
                "deal_id": 3514376757,
                "created_at": 1689152421692,
                "side": "sell",
                "price": "30718.42",
                "amount": "0.00154936"
            }
        ]
    },
    "id": null
}

Cancel Latest Market Transaction Subscription
Method: deals.unsubscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to unsubscribe to all markets.
Example:
// Cancel a singular subscription
{
    "method": "deals.unsubscribe",
    "params": {"market_list": ["BTCUSDT"]},
    "id": 1
}

// Cancel multiple subscriptions

{
    "method": "deals.unsubscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
    "id": 1
}

// Cancel all subscriptions
{
    "method": "deals.unsubscribe",
    "params": {"market_list": []},
    "id": 1
}

Market Transaction Subscription
Latest Market Transaction Push
Cancel Latest Market Transaction Subscription



TickerWS EndpointMarket Index Subscription
Market Index Subscription
Info
The push delay of this method is about：5000ms
Market Index Subscription
Method: index.subscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	Market list. Empty list to subscribe to all markets.
Example:
// Subscribe to a singular market
{
    "method": "index.subscribe",
    "params": {"market_list": ["BTCUSDT"]},
    "id": 1
}

// Subscribe to multiple markets
{
    "method": "index.subscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
    "id": 1
}

Market Index Price Push
Method: index.update
Parameters:
Parameter Name	Type	Notes
market	string	Market name
index_price	string	Index price
mark_price	string	Mark price
Example:
{
    "method": "index.update",
    "data": {
        "market": "BTCUSDT",
        "index_price": "20000",
        "mark_price": "20000"
    },
    "id": null
}

Cancel Index Subscription
Method: index.unsubscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	Market list. Empty list to subscribe to all markets.
Example:
// Unsubscribe to a singular market
{
  "method": "index.unsubscribe",
  "params": {"market_list": ["BTCUSDT"]},
  "id": 1
}

// Unsubscribe to multiple markets
{
  "method": "index.unsubscribe",
  "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
  "id": 1
}

// Unsubscribe to all markets
{
  "method": "index.unsubscribe",
  "params": {"market_list": []},
  "id": 1
}

Market Index Subscription
Market Index Price Push
Cancel Index Subscription




TickerWS EndpointBBO (Best-bid-offer) Subscription
BBO (Best-bid-offer) Subscription
Info
The push delay of this method is: real-time
BBO (Best-bid-offer) Subscription
Method: bbo.subscribe
Parameters:
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names
Example:
// Subscribe to a singular market
{
    "method": "bbo.subscribe",
    "params": {"market_list": ["BTCUSDT"]},
    "id": 1
}

// Subscribe to multiple markets
{
    "method": "bbo.subscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
    "id": 1
}

BBO (Best-bid-offer) Update Push
Method: bbo.update
Parameters:
Parameter Name	Type	Notes
market	string	Market name
updated_at	int	Timestamp (millisecond)
best_bid_price	string	Best bid price
best_bid_size	string	Best bid size
best_ask_price	string	Best ask price
best_ask_size	string	Best ask size
Example
{
    "method": "bbo.update",
    "data": {
        "market": "BTCUSDT",
        "updated_at": 1642145331234,
        "best_bid_price": "20000",
        "best_bid_size": "0.1",
        "best_ask_price": "20001",
        "best_ask_size": "0.15"
    },
    "id": null
}

Cancel BBO (Best-bid-offer) Subscription
Method: bbo.unsubscribe
Parameter Name	Required	Type	Notes
market_list	true	[]string	List of market names. Empty list to unsubscribe to all markets.
Example:
// Unsubscribe to a singular market
{
    "method": "bbo.unsubscribe",
    "params": {"market_list": ["ETHUSDT"]},
    "id": 1
}

// Unsubscribe to multiple markets
{
    "method": "bbo.unsubscribe",
    "params": {"market_list": ["BTCUSDT", "ETHUSDT"]},
    "id": 1
}

// Unsubscribe to all markets
{
    "method": "bbo.unsubscribe",
    "params": {"market_list": []},
    "id": 1
}

BBO (Best-bid-offer) Subscription
BBO (Best-bid-offer) Update Push
Cancel BBO (Best-bid-offer) Subscription



