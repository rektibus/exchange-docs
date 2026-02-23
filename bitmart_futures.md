Update Plan
【2025-08-23 Important Notice】 Temporary Suspension of API Key Management Due to Domain Upgrade.Due to a service upgrade on the domain api-cloud-v2.bitmart.com, the API key creation and modification functions on the website will be temporarily unavailable on August 23, 2025, from 20:30 to 21:00 (UTC+8). The interruption is expected to last about 1–3 minutes. 👉 Note: This does not affect spot or futures trading operations. Thank you for your understanding.

【2025-04-16 Important Notice】The OpenAPI service of futures trading has launched the one-way position order function

【2024-11-11 Important Notice】The V1 OpenAPI service for futures trading will be fully discontinued on 2024-11-30. Please use the V2 OpenAPI for future trading.

The domain name https://api-cloud.bitmart.com will not provide Futures 1.0 HTTP services. Please use the domain name https://api-cloud-v2.bitmart.com to access Futures 2.0 HTTP services
The domain name wss://openapi-ws.bitmart.com will not provide Futures 1.0 Websocket services. Please use the domain name wss://openapi-ws-v2.bitmart.com to access Futures 2.0 Websocket services
【2025-10-18 Important Notice】
BitMart Futures Server Upgrade Notice
Time: UTC+0, October 18, 2025, 02:00–03:00
Duration: Approximately 1 hour
During the upgrade, the following functions will be temporarily paused for 5–6 minutes:

Transfer of assets into Futures accounts
Futures trading (including market data, order placement, order cancellation, position closing, trade queries, and grid trading functions)
Copy trading for futures
Futures account opening
Note:
1.Spot trading functions will not be affected. If this may impact your trading, please consider transferring assets or closing positions in advance.
2.During the upgrade, if you attempt to call any of the suspended functions, the system may return error code 40020 or 25601.

Change Log
2026-02-03
REST API
[New] /contract/private/affiliate/rebate-inviteUser GET The Referral Commission Information Of The Invited Users
Feature: Query up to 60 days of data
[New] /contract/private/affiliate/invite-check GET Check If It Is An Invited User
Feature: Used for API This is suitable for agents to check whether a user is a user they invited.
2025-12-11
REST API
[New] /contract/private/affiliate/rebate-user Get Affiliate Rebate Data
Feature: Query up to 60 days of data
[New] /contract/private/affiliate/rebate-api Get API Rebate Data
Feature: Query up to 60 days of data
2025-12-02
REST API
[Update] /contract/private/trades Get Order Trade (KEYED)
Feat：Add new request field order_id,client_order_id,support order_id and client_order_id queries
2025-11-18
REST API
[New] Simulated Trading Feature
Feature: Support API simulated trading for contract trading testing
REST endpoint: https://demo-api-cloud-v2.bitmart.com
WebSocket Public Channel: wss://openapi-wsdemo-v2.bitmart.com/api?protocol=1.1
WebSocket Private Channel: wss://openapi-wsdemo-v2.bitmart.com/user?protocol=1.1
[New] /contract/private/claim Simulated Claim (SIGNED)
Feature: Support simulated account claim
2025-09-23
REST API
[Update] /contract/private/trades Get Order Trade
Request field symbol changed to optional
2025-08-11
REST API
[Update] /contract/private/order-history Get Order History
Feat：Add new request field order_id,client_order_id,support order_id and client_order_id queries
2025-07-04
REST API
[Update] /contract/private/order-history Get Order History
Feat：Response field type add new value planorder
Feat：Add new response field： trigger_price,execution_price,returned at plan order only
[Update] /contract/private/position-v2 Get Current Position V2
Feat：Add new response field： position_amount
2025-06-20
REST API
[New] /contract/public/market-trade Query the latest trade data
Feat: Retrieve up to the most recent 100 trade records
2025-06-05
REST API
[Update] /contract/public/details Applicable to query contract details
Feat：Add new response field： status
Feat：Add new response field： delist_time
2025-06-04
REST API
[New] /contract/public/leverage-bracket
Feat: Support retrieving risk limit bracket
2025-05-08
REST API
[New] /contract/private/position-v2 Get Current Position V2 (KEYED)
Feat: If symbol is not provided, only trading pairs with existing positions will return data; trading pairs without positions will not return anything.
Feat: If symbol is provided, data will be returned regardless of whether there is an existing position. If there is no position, the position-related fields will be displayed as zero.
2025-04-10
Websocket Stream
[Update] [Private] Position Channel
Feat：Add new response field position_mode
[Update] [Private] Order Channel
Feat：Add new response field position_mode
2025-04-08
REST API
[New] /contract/private/set-position-mode Set Position Mode (SIGNED)
Feat: Applicable for setting position mode
[New] /contract/private/get-position-mode Get Position Mode (KEYED)
Feat: Applicable for getting position mode
[Update] /contract/private/position Get Current Position (KEYED)
Feat：Add new response field position_mode
[Update] /contract/private/order Get Order Detail (KEYED)
Feat：Add new response field position_mode
[Update] /contract/private/order-history Get Order History (KEYED)
Feat：Add new response field position_mode
[Update] /contract/private/get-open-orders Get All Open Orders (KEYED)
Feat：Add new response field position_mode
[Update] /contract/private/current-plan-order Get All Current Plan Orders (KEYED)
Feat：Add new response field position_mode
2025-04-03
REST API
[Update] /contract/private/order Get Order Detail (KEYED)
Feat：Add new request field account, support differentiation between futures and copy_trading
Feat：Add new response field account
[Update] /contract/private/order-history Get Order History (KEYED)
Feat：Add new request field account, support differentiation between futures and copy_trading
Feat：Add new response field account
[Update] /contract/private/position Get Current Position (KEYED)
Feat：Add new request field account, support differentiation between futures and copy_trading
Feat：Add new response field account
[Update] /contract/private/position-risk Get Current Position Risk Details(KEYED)
Feat：Add new request field account, support differentiation between futures and copy_trading
Feat：Add new response field account
[Update] /contract/private/trades Get Order Trade (KEYED)
Feat：Add new request field account, support differentiation between futures and copy_trading
Feat：Add new response field account
[Update] /contract/private/transaction-history Get Transaction History (KEYED)
Feat：Add new request field account, support differentiation between futures and copy_trading
Feat：Add new response field account
2025-04-01
REST API
[Update] /contract/private/cancel-all-after Applicable for canceling all contract orders timed(SIGNED)
Add new field symbol, support canceling open orders timed by symbol
2025-03-27
REST API
[New] /contract/private/cancel-all-after Applicable for canceling all contract orders timed(SIGNED)
Feature：Support canceling open orders timed
2025-03-06
REST API
[New] /contract/private/modify-limit-order Applicable for modifying contract limit orders(SIGNED)
Feature：Support modifying limit orders
[Update] /contract/private/submit-order Applicable for placing contract orders(SIGNED)
Add new field stp_mode, support setting up Self-Trading-Protection
2025-02-11
Websocket Stream
[Update] [Public] Ticker Channel
Support subscription by trading pair
Rename fair_price->mark_price
Add index_price
[New] [Public] MarkPrice KlineBin Channel
Support subscription MarkPrice Kline data
REST API
[New] /contract/public/markprice-kline Get MarkPrice K-line
Support retrieving MarkPrice Kline data
2025-1-16
Websocket Stream
[Update] [Public] Trade Channel
Feature：Add new response field m, support differentiation between maker and taker.
2024-12-17
REST API
[New] /contract/private/submit-trail-order Support replacing trail orders(SIGNED)
Feature：Support replacing trail orders
[New] /contract/private/cancel-trail-order Support cancel trail orders(SIGNED)
Feature：Support cancel trail orders
[Update] /contract/private/submit-order Applicable for placing orders(SIGNED)
Feature：Remove the fields related replacing trail orders
2024-12-12
REST API
[New] /contract/public/funding-rate-history Query Funding Rate History (NONE)
Feature：Query futures funding rate history
[New] /contract/private/transaction-history Query Transaction History (KEYED)
Feature：Query Transfers, Realized PnL, Funding costs, Fees and other fund records
2024-12-11
Websocket Stream
[New] [Public] Individual Symbol Book Ticker Channel
Supports BBO push
[Update] [Public] Depth Channel
Supports optional update speed of @100ms,@200ms
[Update] [Public] Depth-All Channel
Supports optional update speed of @100ms,@200ms
[Update] [Public] Depth-Increase Channel
Supports optional update speed of @100ms,@200ms
2024-12-04
REST API
[Update] /account/v1/transfer-contract Transfer (SIGNED)
Feature：support sub-account call
2024-11-28
REST API
[Update] /contract/private/modify-plan-order Modify Plan Order (SIGNED)
Remove the field client_order_id
Websocket Order
[Update] 【Private】Order Channel
The field of state adds type status_approval
2024-11-25
Websocket Stream
[New] [Public] Funding rate Channel
Supports funding rate push
2024-11-01
Websocket Stream
[New] [Public] Full-depth Channel
Supports full-depth simultaneous push
[New] [Public] Incremental Depth Push Channel
Supports incremental depth push
2024-10-29
REST API
[Update] /contract/public/kline Get K-line
Single time request size upper limit 500
2024-10-24
REST API
[Update] /contract/public/details Get Contract Details
Add new response field market_max_volume
2024-10-17
REST API
[New] /contract/private/trade-fee-rate Support querying trade fee rate(KEYED)
Feature：Support querying trade fee rate
[Update] /contract/public/funding-rate Get Current Funding Rate
Update rate limit from 2 times/2 sec to 12 times/2 sec
[Update] /contract/public/details Get Contract Details
Add new response field funding_interval_hour
Support get funding interval
2024-10-10
REST API
[Update] /contract/private/submit-tp-sl-order Support replacing contract TP/SL orders(SIGNED)
Change the default value of field plan_category to 2-Position TP/SL
2024-09-26
Documentation
[Deleted] Futures 1.0 documentation
2024-09-19
REST API
[New] /contract/private/submit-tp-sl-order Support replacing contract TP/SL orders(SIGNED)
Feature：Support replacing contract TP/SL orders
[New] /contract/private/modify-plan-order Support modifying contract plan orders(SIGNED)
Feature：Support modifying contract plan orders
[New] /contract/private/modify-preset-plan-order Support modifying contract preset plan orders(SIGNED)
Feature：Support modifying contract preset plan orders
[New] /contract/private/modify-tp-sl-order Support modifying contract TP/SL orders(SIGNED)
Feature：Support modifying contract TP/SL orders
[Update] /contract/private/cancel-order Cancel a single futures order
Add new request field client_order_id
Support batch cancel orders by symbol
[Update] /contract/private/cancel-plan-order Cancel Plan Order
Add new request field client_order_id
Support batch cancel orders by symbol
[Update] /contract/private/current-plan-order Get All Current Plan Orders
Add new request field plan_type
2024-07-23
Add a new endpoint named current-plan-order
/contract/private/current-plan-ordersupport query contract all current plan orders（TP/SL、plan）
New endpoints for trading
/contract/private/submit-leverageSubmit Leverage (SIGNED)
New endpoints for Sub-Account
/account/contract/sub-account/main/v1/transfer-listGet Sub-Account Transfer History (For Main Account）(KEYED)
/account/contract/sub-account/v1/transfer-historyGet Account Futures Asset Transfer History (For Main/Sub Account）(KEYED)
New endpoints for Sub-Account
/account/contract/sub-account/main/v1/sub-to-mainSub-Account to Main-Account (For Main Account) (SIGNED)
/account/contract/sub-account/main/v1/main-to-subMain-Account to Sub-Account (For Main Account) (SIGNED)
/account/contract/sub-account/sub/v1/sub-to-mainSub-Account to Main-Account (For Sub-Account) (SIGNED)
/account/contract/sub-account/main/v1/walletGet Sub-Account Futures Wallet Balance (For Main Account) (KEYED)
New endpoints for order
/contract/private/get-open-ordersGet All Open Orders (KEYED)
New endpoints for transfer
/account/v1/transfer-contractGet Transfer List (SIGNED)
/account/v1/transfer-contract-listTransfer (SIGNED)
New endpoints for websocket order notify
/contract/public/websocket/order
New endpoints for trading
/contract/private/submit-plan-orderSubmit Plan Order (SIGNED)
/contract/private/cancel-plan-orderCancel Plan Order (SIGNED)
New endpoints for trading
/contract/private/orders-historyGet Order History (KEYED)
/contract/private/tradesGet Order Trade (KEYED)
/contract/private/positionGet Current Position (KEYED)
New endpoints for Futures Market Data
/contract/public/klineGet K-line
/contract/public/funding-rateGet Current Funding Rate
New endpoints for Futures Account Data
/contract/private/assets-detailGet Contract Assets (KEYED)
New websocket for public data
/contract/public/websocket
New endpoints for get current funding rate of a specified contract
/contract/public/open-interest
New endpoints for Futures Market Data
/contract/public/detailsGet Contract Details
/contract/public/depthGet Market Depth
Introduction
API Key Create
Many APIs require an API Access Key for access. Please refer to this page to set up.
When setting up an API Access Key, it is recommended to set up an IP access whitelist for security purposes.
Never give your API Access key/secret key to anyone.
PNG

If you accidentally leak your API key, delete it immediately and generate a new one.
After creating an API Key, you will receive three pieces of information that you must remember:
Access Key: represents the identity of the account, this is your api key
Secret Key: used for API signature
Memo: used for API signature
PNG

The Access Key and Secret Key will be randomly generated and provided by BitMart, and the Memo will be provided by you to ensure the security of API access.

API Key Permission Settings
The default permission of a newly created API is Read-Only.
To withdraw funds through the API, you need to modify the permissions in the UI and select Withdraw.
Permission descriptions:
Read-only (query spot trading orders, query contract trading orders, query funds)
Spot-Trade (place orders, cancel orders)
Withdraw (withdraw funds)
Margin-Trade (repayment, borrowing, placing orders, etc.)
Future-Trade (long position, short position, closing position, etc.)
PNG

Read-Only Permissions:
API Name	Authentication Type	Description
/account/v1/wallet	KEYED	Query account assets
/account/v1/deposit/address	KEYED	Query deposit addresses for each currency
/account/v1/withdraw/address/list	KEYED	Query withdraw address list
/account/v2/deposit-withdraw/history	KEYED	Query deposit and withdrawal history
/account/v1/deposit-withdraw/detail	KEYED	Query deposit and withdrawal details
/spot/v1/wallet	KEYED	Query wallet balance for all currencies
/spot/v4/query/order	SIGNED	Query order by id (v4)
/spot/v4/query/client-order	SIGNED	Query order by client order id (v4)
/spot/v4/query/open-orders	SIGNED	Current open orders (v4)
/spot/v4/query/history-orders	SIGNED	Account orders (v4)
/spot/v4/query/trades	SIGNED	Account trade list (v4)
/spot/v4/query/order-trades	SIGNED	Order trade list(v4)
/spot/v1/user_fee	KEYED	Query basic fee rate for current user
/spot/v1/trade_fee	KEYED	Query fee rate for a specific trading pair for current user
/spot/v1/margin/isolated/pairs	KEYED	Query loan interest rate and limit for a trading pair
/spot/v1/margin/isolated/account	KEYED	Query isolated margin account information
/spot/v1/margin/isolated/borrow_record	KEYED	Query isolated margin borrowing record
/spot/v1/margin/isolated/repay_record	KEYED	Query isolated margin repayment record
/contract/private/get-open-orders	KEYED	Query Contract All Open Orders
/contract/private/order	KEYED	Query contract order details
/contract/private/trade-fee-rate	KEYED	Query Trade Fee Rate
/contract/private/order-history	KEYED	Query contract order history
/contract/private/trades	KEYED	Query contract trade details
/contract/private/transaction-history	KEYED	Get Contract Transaction History
/contract/private/assets-detail	KEYED	Query contract asset details
/contract/private/position	KEYED	Query position details
/contract/private/position-v2	KEYED	Query position details V2
/contract/private/current-plan-order	KEYED	Query Current Plan Orders
/contract/private/position-risk	KEYED	Query Position Risk Details
/contract/private/get-position-mode	KEYED	Get position mode
Withdraw Permissions:
API Name	Authentication Type	Description
/account/v1/withdraw/charge	KEYED	Query withdrawal limits
/account/v1/withdraw/apply	SIGNED	Apply for withdrawal
Spot-Trade Permissions:
API Name	Authentication Type	Description
/spot/v1/submit_order	SIGNED	Place an order
/spot/v2/submit_order	SIGNED	Place an order
/spot/v1/batch_orders	SIGNED	Place multiple orders
/spot/v2/batch_orders	SIGNED	Place multiple orders
/spot/v4/batch_orders	SIGNED	Place multiple orders
/spot/v1/cancel_order	SIGNED	Cancel an unfinished order
/spot/v3/cancel_order	SIGNED	Cancel an unfinished order
/spot/v1/cancel_orders	SIGNED	Cancel multiple orders
/spot/v4/cancel_orders	SIGNED	Cancel multiple orders
Margin-Trade Permissions:
API Name	Authentication Type	Description
/spot/v1/margin/submit_order	SIGNED	Margin order placement
/spot/v1/margin/isolated/transfer	SIGNED	Transfer funds between margin and spot accounts
/spot/v1/margin/isolated/borrow	SIGNED	Isolated margin borrowing
/spot/v1/margin/isolated/repay	SIGNED	Repay isolated margin debt
Future-Trade Permissions:
API Name	Authentication Type	Description
/contract/private/submit-order	SIGNED	Place an order for a futures contract
/contract/private/cancel-order	SIGNED	Cancel a single futures order
/contract/private/cancel-orders	SIGNED	Batch cancel futures orders
/contract/private/submit-plan-order	SIGNED	Place a plan order for futures contracts
/contract/private/cancel-plan-order	SIGNED	Cancel futures plan orders
/account/v1/transfer-contract	SIGNED	Future account transfer
/account/v1/transfer-contract-list	SIGNED	Get Future account transfer list
/contract/private/submit-tp-sl-order	SIGNED	Place a tp or sl order for a futures contract
/contract/private/modify-plan-order	SIGNED	Modify a plan order for a futures contract
/contract/private/modify-preset-plan-order	SIGNED	Modify a preset plan order for a futures contract
/contract/private/modify-tp-sl-order	SIGNED	Modify a tp or sl order for a futures contract
/contract/private/submit-trail-order	SIGNED	Place a trail order for futures contracts
/contract/private/cancel-trail-order	SIGNED	Cancel futures trail order
/contract/private/modify-limit-order	SIGNED	Modify futures limit order
/contract/private/cancel-all-after	SIGNED	Timed cancel all open orders
/contract/private/set-position-mode	SIGNED	Set position mode
Sub-Account Permissions:
You need to enter Institution Verification to use the sub-account endpoints.

After the creation is successful, the sub-account has Read-only permission by default.

PNG

Sub-Account Spot-Trade Permissions:
Same as the above spot trading authority

Sub-Account Contract-Trade Permissions:
Same as above futures trading authority

Sub-Account Inter-Account Transfer Permissions:
API Name	Authentication Type	Description
/account/sub-account/main/v1/sub-to-main	SIGNED	Sub-Account Transfer to Main-Account (For Main Account, use spot account)
/account/sub-account/sub/v1/sub-to-main	SIGNED	Sub-Account Transfer to Main-Account (For Sub-Account, use spot account)
/account/sub-account/main/v1/main-to-sub	SIGNED	Main-Account Transfer to Sub-Account (For Main Account, use spot account)
/account/sub-account/main/v1/sub-to-sub	SIGNED	Sub-Account Transfer to Sub-Account (For Main Account, use spot account)
/account/sub-account/main/v1/transfer-list	KEYED	Get Sub-Account Transfer History (For Main Account, use spot account)
/account/sub-account/v1/transfer-history	KEYED	Get Account Spot Asset Transfer History (For Main/Sub Account, use spot account)
/account/sub-account/main/v1/wallet	KEYED	Get Sub-Account Spot Wallet Balance (For Main Account, use spot account)
/account/sub-account/main/v1/subaccount-list	KEYED	Get Sub-Account List (For Main Account, use spot account)
/account/contract/sub-account/main/v1/sub-to-main	SIGNED	Sub-Account Transfer to Main-Account (For Main Account, use futures account)
/account/contract/sub-account/main/v1/main-to-sub	SIGNED	Main-Account Transfer to Sub-Account (For Main Account, use futures account)
/account/contract/sub-account/sub/v1/sub-to-main	SIGNED	Sub-Account Transfer to Main-Account (For Sub-Account, use futures account)
/account/contract/sub-account/main/v1/wallet	KEYED	Get Sub-Account Futures Wallet Balance (For Main Account, use futures account)
/account/contract/sub-account/v1/transfer-history	KEYED	Get Account Futures Asset Transfer History (For Main/Sub Account, use futures account)
/account/contract/sub-account/main/v1/transfer-list	KEYED	Get Sub-Account Transfer History (For Main Account, use futures account)
Contract Agent Permissions:
API Name	Authentication Type	Description
/contract/private/affiliate/rebate-list	KEYED	Get Futures Rebate List
/contract/private/affiliate/rebate-api	KEYED	Get API Rebate Data
/contract/private/affiliate/rebate-user	KEYED	Get User Rebate Data
/contract/private/affiliate/trade-list	KEYED	Get Futures Trade List
API Library
In order to facilitate access, we provide SDK in some languages for reference. For more programming codes, please refer to the Quick Start API on the page.

Available SDK:
Java
Python
Nodejs
Go
PHP
In addition to the SDK, we also provide code samples in multiple languages, and the samples mainly demonstrate how to use the signed interface. It can be built and run standalone or as part of your codebase.

Python Signature Example
Go Signature Example
Nodejs Signature Example
Java Signature Example
PHP Signature Example
Ruby Signature Example
C# Signature Example
Rust Signature Example
C++ Signature Example
Postman
FAQ
Here are some frequently asked questions.

Q1. Will different API KEY in the same account return different data?
Different API KEY data under the same account is the same.
Q2. How to fill information in when applying for APIKEY?
1. `memo` is provided by the user, it can be any string, used to confuse the signature algorithm
2. Binding ip is optional, it is recommended to fill in for account security
3. API permissions can be checked according to user needs
Q3. How is the HTTP status code 429 created?
The request interface exceeds the access frequency limit, it is recommended to reduce the access frequency.
Q4. Using ccxt, the API KEY is correctly filled in, but it will also prompt 'message': 'Header X-BM-SIGN is wrong'
The parameter uid of ccxt needs to be filled in as the memo when creating the API
Here is an example of initialization:

bitmart = ccxt.bitmart({
'apiKey': 'your_api_key',
'secret': 'your_api_secret',
'uid': 'your_api_memo' // not your uid, is the api memo
});
Q5. The program I wrote myself always prompts 'message': 'Header X-BM-SIGN is wrong'
Please refer to Quick Access API, select the language you use, and there are correct signature methods for reference.
Q6. Where is the location of BitMart servers?
We are using Google Cloud Services and deployed in Taiwan.
Q7. When will the VIP fee I applied for take effect?
We will update on the 8th, 18th and 28th of every month.
Q8. Why does it prompt "IP is forbidden. We recommend enabling IP whitelist for API trading. "
Because you set up an IP whitelist when creating the API, which means that this API KEY can only send requests through this IP, and other IPs using this API KEY will prompt that it is prohibited.
Why set up: IP whitelist is a network security measure used to control who can access specific network resources or services. If a whitelist IP is added, the service will only accept API requests from that IP and reject API requests from other IPs.
Contact Us
Get support in our Telegram group BitMart API Club
Please take 1 minute to help us improve: API Satisfaction Survey
Basic Information
API Basic Information
This article lists the rest baseurl of the interfaces: https://api-cloud-v2.bitmart.com
All interface responses are in JSON format.
Request Parameter Settings
For GET and DELETE method interfaces, parameters must be sent in the query string, i.e., the parameters concatenated after the URL?.
For POST and PUT method interfaces, parameters are sent in the request body in JSON format.
HTTP Response Codes
HTTP 4XX Error codes are used to indicate wrong request content, behavior, and format. The problem is from the request sender.
HTTP 403 The error code indicates a violation of the restriction (prohibited call).
HTTP 429 The error code indicates that the access frequency is overrun and the IP will be blocked.
HTTP 418 The error code indicates that the IP has been blocked after error code 429.
HTTP 5XX Error codes are used to indicate problems with BitMart server.
API Returned Codes
code Error code
message Error description
trace Event tracking ID for each request, which is returned by the server for every request
data User Data
For details, please refer to Error Code List

Signature
The authentication type of each API endpoint will be indicated. If it is marked as SIGNED,it means that the endpoint requires a signature to access. If it is marked as KEYED, it means that the endpoint only requires an API Access KEY to be set in the request header.

Authentication Type
NONE: Public endpoint, accessible to anyone
KEYED: Endpoint requires a valid X-BM-KEY to be set in the request header
SIGNED: Endpoint requires a valid X-BM-KEY and X-BM-SIGN signature to be set in the request header
1. Setting Request Parameters
1.1 Set Request Header Key
Create X-BM-TIMESTAMP

Copy Success// Java
System.currentTimeMillis();

// Python
int(time.time() * 1000) 

// Golang
time.Now().UnixNano() / int64(time.Millisecond)

// Nodejs & TypeScript
Date.now();

// Javascript
Date.now();

// PHP
round(microtime(true) * 1000)

// C#
DateTimeOffset.UtcNow.ToUnixTimeMilliseconds()

X-BM-KEY (Your created API Access KEY)
X-BM-SIGN (Signature using Sha-256)
X-BM-TIMESTAMP (Current timestamp in milliseconds when the request is sent)
1.2 Set Request Body Params
For GET/DELETE requests, the query string is in form format, such as symbol=BMX&side=BUY.
For POST/PUT requests, the query string is in JSON format, such as {"symbol":"BMX","side":"BUY"}.
2. Example
Shell Example

Copy Successecho -n '1589793796145#test001#{"symbol":"BTC_USDT","price":"8600","count":"100"}' | openssl dgst -sha256 -hmac "6c6c98544461bbe71db2bca4c6d7fd0021e0ba9efc215f9c6ad41852df9d9df9"
    (stdin)= c31dc326bf87f38bfb49a3f8494961abfa291bd549d0d98d9578e87516cee46d

    curl --location --request POST 'localhost:8080/spot/v1/test-post'
    --header 'Content-Type: application/json'
    --header 'X-BM-KEY: 80618e45710812162b04892c7ee5ead4a3cc3e56'
    --header 'X-BM-SIGN: c31dc326bf87f38bfb49a3f8494961abfa291bd549d0d98d9578e87516cee46d'
    --header 'X-BM-TIMESTAMP: 1589793796145'
    --d '{"symbol":"BTC_USDT","price":"8600","count":"100"}'

Request API: /spot/v1/test-post (SIGNED)
Request method: POST
Current timestamp: timestamp=1589793796145
Request body: {"symbol":"BTC_USDT","price":"8600","count":"100"}
Then set the following:

X-BM-TIMESTAMP=1589793796145
X-BM-KEY=Your_api_access_key
X-BM-SIGN= hmac_sha256(Your_api_secret_key, X-BM-TIMESTAMP + '#' + Your_api_memo + '#' + {"symbol":"BTC_USDT","price":"8600","count":"100"})
Assuming the key you applied for is as follows:

accessKey=80618e45710812162b04892c7ee5ead4a3cc3e56
secretKey=6c6c98544461bbe71db2bca4c6d7fd0021e0ba9efc215f9c6ad41852df9d9df9
memo=test001
then the right side is a complete request

You can also refer to the SDK or Quick Start API below to implement

Rate Limit
The speed of the public interface is limited according to the IP, and the speed of the private interface is limited according to the API KEY. When the requests exceed the rate limit, the 429 status will be returned: the request is too frequent.

Endpoints Limit Rules:
Futures Market Endpoints	Endpoint Name	Limit Target	Rate
/contract/public/details	Get a detailed list of all trading pairs	IP	12 times/2 sec
/contract/public/depth	Get full depth of trading pairs	IP	12 times/2 sec
/contract/public/open-interest	Get Contract Open Interest	IP	2 times/2 sec
/contract/public/funding-rate	Get Current Funding Rate	IP	12 times/2 sec
/contract/public/funding-rate-history	Get history Funding Rate	IP	12 times/2 sec
/contract/public/kline	Get K-line	IP	12 times/2 sec
/contract/public/markprice-kline	Get Mark Price K-line	IP	12 times/2 sec
/contract/public/leverage-bracket	Get Contract Leverage Risk Limit	IP	12 times/2 sec
/contract/public/market-trade	Get Market Trade	IP	12 times/2 sec
Futures Trade Endpoints	Endpoint Name	Limit Target	Rate
/contract/private/submit-order	Submit Contract Order	X-BM-KEY	24 times/2 sec
/contract/private/cancel-order	Cancel Contract Order	X-BM-KEY	40 times/2 sec
/contract/private/cancel-orders	Batch Cancel Contract Orders	X-BM-KEY	2 times/2 sec
/contract/private/submit-plan-order	Submit Contract Plan Order	UID	24 times/2 sec
/contract/private/cancel-plan-order	Cancel Contract Plan Order	UID	40 times/2 sec
/contract/private/submit-tp-sl-order	Submit Contract TP or SL order	UID	24 times/2 esc
/contract/private/modify-plan-order	Modify Contract Plan Order	UID	24 times/2 esc
/contract/private/modify-preset-plan-order	Modify Contract Preset Plan Order	UID	24 times/2 esc
/contract/private/modify-tp-sl-order	Modify Contract TP or SL Order	UID	24 times/2 esc
/contract/private/modify-limit-order	Modify Contract Limit Order	UID	24 times/2 esc
/contract/private/cancel-all-after	Timed cancel all open orders	UID	4 times/2 esc
/contract/private/submit-trail-order	Submit Trail Order	UID	24 times/2 esc
/contract/private/cancel-trail-order	Cancel Trail Order	UID	24 times/2 esc
/contract/private/set-position-mode	Set position mode	X-BM-KEY	2 times/2 esc
/contract/private/get-position-mode	Get position mode	X-BM-KEY	2 times/2 esc
/contract/private/get-open-orders	Get Contract All Open Orders	X-BM-KEY	50 times/2 sec
/contract/private/order	Get Contract Order Detail	X-BM-KEY	50 times/2 sec
/contract/private/order-history	Get Contract Order History	X-BM-KEY	6 times/2 sec
/contract/private/trades	Get Contract Order Trade Detail	X-BM-KEY	6 times/2 sec
/contract/private/transaction-history	Get Transaction History	X-BM-KEY	6 times/2 sec
/contract/private/assets-detail	Get Contract Assets Detail	X-BM-KEY	12 times/2 sec
/contract/private/position	Get Current Position Detail	X-BM-KEY	6 times/2 sec
/contract/private/position-v2	Get Current Position Detail V2	X-BM-KEY	6 times/2 sec
/contract/private/submit-leverage	Submit Contract Leverage	X-BM-KEY	24 times/2 sec
/account/v1/transfer-contract	Transfer	X-BM-KEY	1 times/2 sec
/account/v1/transfer-contract-list	Get Transfer List	X-BM-KEY	1 times/2 sec
/contract/private/current-plan-order	Get Contract All Current Plan Orders	X-BM-KEY	50 times/2 sec
/contract/private/position-risk	Get Position Risk Info	X-BM-KEY	24 times/2 sec
/contract/private/trade-fee-rate	Get Trade Fee Rate	X-BM-KEY	2 times/2 esc
|

Sub-Account Endpoints	Endpoint Name	Limit Target	Rate
/account/contract/sub-account/main/v1/sub-to-main	Sub-Account Transfer to Main-Account (For Main Account, ues futures account)	X-BM-KEY	8 times/2s
/account/contract/sub-account/main/v1/main-to-sub	Main-Account Transfer to Sub-Account (For Main Account, ues futures account)	X-BM-KEY	8 times/2s
/account/contract/sub-account/sub/v1/sub-to-main	Sub-Account Transfer to Main-Account (For Sub-Account, ues futures account)	X-BM-KEY	8 times/2s
/account/contract/sub-account/main/v1/wallet	Get Sub-Account Futures Wallet Balance (For Main Account, ues futures account)	X-BM-KEY	12 times/2s
/account/contract/sub-account/v1/transfer-history	Get Account Futures Asset Transfer History (For Main/Sub Account, ues futures account)	X-BM-KEY	8 times/2s
/account/contract/sub-account/main/v1/transfer-list	Get Sub-Account Transfer History (For Main Account, ues futures account)	X-BM-KEY	8 times/2s
Contract-Agent Endpoints	Interface Name	Limit Target	Rate
/contract/private/affiliate/rebate-list	Get Futures Rebate List	X-BM-KEY	24 times/2s
/contract/private/affiliate/rebate-user	Get User Rebate Data	X-BM-KEY	24 times/2s
/contract/private/affiliate/rebate-api	Get API Rebate Data	X-BM-KEY	24 times/2s
/contract/private/affiliate/trade-list	Get Futures Trade List	X-BM-KEY	24 times/2s
/contract/private/affiliate/invite-check	GET Check If It Is An Invited User	X-BM-KEY	24 times/2s
/contract/private/affiliate/rebate-inviteUser	GET The Referral Commission Information Of The Invited Users	X-BM-KEY	24 times/2s
REST API
Speed limit judgment:

Each call to the interface will return 3 Response Headers with limit tags, as shown below:

Example:

Copy SuccessX-BM-RateLimit-Remaining: 10
X-BM-RateLimit-Limit: 600
X-BM-RateLimit-Reset: 60
The above setting means that it can be called 600 times within 60 seconds, and currently has been called 10 times
Response Header	Description
X-BM-RateLimit-Remaining	The number of requests that have been used in the current time window
X-BM-RateLimit-Limit	The max number of requests in the current time window
X-BM-RateLimit-Reset	Current time window, in seconds
Note that when X-BM-RateLimit-Remaining> X-BM-RateLimit-Limit, please do not continue to call, otherwise it will be banned
Futures Public API Definitions
Field description
symbol is the name of the trading pair, consisting of the trading currency and the quote currency. Taking BTCUSDT as an example, BTC is the transaction currency, USDT is the pricing currency, and the transaction pair is mainly used in contract transactions
order_id order number, the order ID of the same currency pair of each business line is unique
Order State（Field:state)
2=status_check
4=status_finish
Order Side（Field:side)
1=buy_open_long
2=buy_close_short
3=sell_close_long
4=sell_open_short
Position（Field:position_type)
1=long
2=short
Position Direction: (Field: position_side)
both (For One-way position mode)
long (For Hedge position mode)
short (For Hedge position mode)
Order Type（Field:type)
limit
market
liquidate
bankruptcy
adl
trailing
planorder
Open Type（Field:open_type)
cross
isolated
Order Mode（Field:mode)
1=GTC (Good Till Cancel)
2=FOK (Fill or Kill)
3=IOC (Immediate or Cancel)
4=Maker Only (Good Till Crossing)
Timestamp
All the times returned by the system are in the form of timestamps.

Futures Market Data
Get Contract Details
Applicable to query contract details

Request URL
GET https://api-cloud-v2.bitmart.com/contract/public/details

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/public/details?symbol=BTCUSDT
Field	Type	Required?	Description
symbol	String	No	Symbol of the contract(like BTCUSDT)
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "trace": "9b92a999-9463-4c96-91a4-93ad1cad0d72",
  "data": {
    "symbols": [
      {
        "symbol": "BTCUSDT",
        "product_type": 1,
        "open_timestamp": 1594080000123,
        "expire_timestamp": 0,
        "settle_timestamp": 0,
        "base_currency": "BTC",
        "quote_currency": "USDT",
        "last_price": "23920",
        "volume_24h": "18969368",
        "turnover_24h": "458933659.7858",
        "index_price": "23945.25191635",
        "index_name": "BTCUSDT",
        "contract_size": "0.001",
        "min_leverage": "1",
        "max_leverage": "100",
        "price_precision": "0.1",
        "vol_precision": "1",
        "max_volume": "500000",
        "market_max_volume": "500000",
        "min_volume": "1",
        "funding_rate": "0.0001",
        "expected_funding_rate": "0.00011",
        "open_interest": "4134180870",
        "open_interest_value": "94100888927.0433258",
        "high_24h": "23900",
        "low_24h": "23100",
        "change_24h": "0.004",
        "funding_interval_hours": 8,
        "status": "Delisted",
        "delist_time": 1745830379
      },
      ...
    ]
  }
}
Field	Type	Description
symbols	List	Array of trading pair details
Description of the trading pair details field:

Trading pair details	Type	Description
symbols	List	Array of trading pair details
symbol	String	Symbol of the contract
product_type	Int	Contract type
-1=perpetual
-2=futures
base_currency	String	Base currency
quote_currency	String	Quote currency
volume_precision	String	Volume Precision
price_precision	String	Price Precision
max_volume	String	Maximum limit order quantity
market_max_volume	String	Maximum market order quantity
min_volume	String	Minimum order quantity
contract_size	String	Contract Size
index_price	String	Index Price
index_name	String	Index Name
min_leverage	String	Minimum leverage ratio
max_leverage	String	Maximum leverage ratio
turnover_24h	String	24 hours turnover
volume_24h	String	24 hours volume
last_price	String	Last Price
open_timestamp	Long	Opening time for the first time
expire_timestamp	Long	Expiration time，If null is returned, it does not expire
settle_timestamp	Long	Settlement time，If null is returned, it will not be automatically settlement
funding_rate	String	current funding rate
expected_funding_rate	String	expect funding rate
open_interest	String	Open interest
open_interest_value	String	Value of open interest
high_24h	String	24h High
low_24h	String	24h Low
change_24h	String	24h Change
funding_interval_hours	Int	Funding interval
status	String	Status
-Trading
-Delisted
delist_time	Int	Delisting time(status=Trading, Expected delisting time)
Get Market Depth
Get full depth of trading pairs.

Request URL
GET https://api-cloud-v2.bitmart.com/contract/public/depth

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/public/depth?symbol=BTCUSDT
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "trace": "b9bff62d-9ac8-4815-8808-8f745673c096",
  "data": {
    "asks": [
      [
        "23935.4",
        "65",
        "65"
      ]
    ],
    "bids": [
      [
        "23935.4",
        "65",
        "65"
      ]
    ],
    "timestamp": 1660285421287,
    "symbol": "BTCUSDT"
  }
}
Field	Type	Description
timestamp	Long	Unix timestamp in milliseconds for when the last updated time occurred
bids	List	Bid order depth
asks	List	Ask order depth
symbol	String	symbol
Return a maximum of 50 pieces of data.
Market depth details：

Field	Type	Description
The first	String	The price at current depth. For example 23935.4
The second	String	Total quantity of current price depth. For example 65
The third	String	Accumulates the total quantity above (including) the current price depth. For example 65
Get Market Trade
Query the latest trade data

Request URL
GET https://api-cloud-v2.bitmart.com/contract/public/market-trade

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/public/market-trade?symbol=BTCUSDT&limit=100
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
limit	Long	No	Count(Default 50; max 100;)
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [
    {
      "symbol": "BTCUSDT",
      "price": "104146.5",
      "qty": "0.037",
      "quote_qty": "3853.4205",
      "time": 1750347973,
      "is_buyer_maker": true
    },
    {
      "symbol": "BTCUSDT",
      "price": "104146.6",
      "qty": "0.023",
      "quote_qty": "2395.3718",
      "time": 1750347972,
      "is_buyer_maker": true
    }
  ],
  "trace": "26f999a04cfa11f09ce9d6002fd59247.4375416.39621015744567440"
}
Field	Type	Description
symbol	String	Symbol
price	String	Trade price
qty	String	Trade value - coin
quote_qty	String	Trade value - USDT
time	Long	Market trade time stamp
is_buyer_maker	Bool	True if Buyer of the trade is maker
Get Futures Openinterest
Applicable for querying the open interest and open interest value data of the specified contract

Request URL
GET https://api-cloud-v2.bitmart.com/contract/public/open-interest

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/public/open-interest?symbol=BTCUSDT

Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
Response Data
Response

Copy Success{
  "code": 1000,
  "trace": "0cc6f4c4-8b8c-4253-8e90-8d3195aa109c",
  "message": "Ok",
  "data": {
    "timestamp": 1661239541734,
    "symbol": "BTCUSDT",
    "open_interest": "4134180870",
    "open_interest_value": "94100888927.0433258"
  }
}
Field	Type	Description
timestamp	Long	Timestamp
symbol	String	Symbol of the contract
open_interest	String	Open interest
open_interest_value	String	Value of open interest
Get Current Funding Rate
Applicable for checking the current funding rate of a specified contract

Request URL
GET https://api-cloud-v2.bitmart.com/contract/public/funding-rate

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/public/funding-rate?symbol=BTCUSDT

Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "timestamp": 1662518172178,
    "symbol": "BTCUSDT",
    "rate_value": "0.000164",
    "expected_rate": "0.000164",
    "funding_time": 1709971200000,
    "funding_upper_limit": "0.0375",
    "funding_lower_limit": "-0.0375"
  },
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
timestamp	Long	Timestamp
symbol	String	Symbol of the contract
rate_value	String	Funding rate of the previous period
expected_rate	String	Funding rate for the next period
funding_time	Long	Next funding settlement time
funding_upper_limit	Long	Upper limit of funding rate for this trading pair
funding_lower_limit	Long	Lower limit of funding rate for this trading pair
Get K-line
Applicable for querying MarketPrice K-line data. Single time request size upper limit 500

Request URL
GET https://api-cloud-v2.bitmart.com/contract/public/kline

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/public/kline?symbol=BTCUSDT&step=5&start_time=1662518172&end_time=1662518172

Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
step	Long	No	K-Line step, default is 1 minute. step: 1, 3, 5, 15, 30, 60, 120, 240, 360, 720, 1440, 4320, 10080
start_time	Long	Yes	Start time(Timestamp in Seconds)
end_time	Long	Yes	End time(Timestamp in Seconds)
Response Data
Response

Copy Success{
  "code": 1000,
  "trace": "0cc6f4c4-8b8c-4253-8e90-8d3195aa109c",
  "message": "Ok",
  "data": [{
    "timestamp": 1662518160,
    "open_price": "100",
    "close_price": "120",
    "high_price": "130",
    "low_price": "90",
    "volume": "941008"
    },
    {
      "timestamp": 1662518161,
      "open_price": "100",
      "close_price": "120",
      "high_price": "130",
      "low_price": "90",
      "volume": "941008"
    }
  ]
}
Field	Type	Description
timestamp	Long	Time Window
open_price	String	Opening Price
close_price	String	Closing Price
high_price	String	Highest Price
low_price	String	Lowest Price
volume	String	Turnover
Get MarkPrice K-line
Applicable for querying MarkPrice K-line data. Single time request size upper limit 500

Request URL
GET https://api-cloud-v2.bitmart.com/contract/public/markprice-kline

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/public/markprice-kline?symbol=BTCUSDT&step=5&start_time=1662518172&end_time=1662518172

Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
step	Long	No	K-Line step, default is 1 minute. step: 1, 3, 5, 15, 30, 60, 120, 240, 360, 720, 1440, 4320, 10080
start_time	Long	Yes	Start time(Timestamp in Seconds)
end_time	Long	Yes	End time(Timestamp in Seconds)
Response Data
Response

Copy Success{
  "code": 1000,
  "trace": "0cc6f4c4-8b8c-4253-8e90-8d3195aa109c",
  "message": "Ok",
  "data": [{
    "timestamp": 1662518160,
    "open_price": "100",
    "close_price": "120",
    "high_price": "130",
    "low_price": "90",
    "volume": "941008"
    },
    {
      "timestamp": 1662518161,
      "open_price": "100",
      "close_price": "120",
      "high_price": "130",
      "low_price": "90",
      "volume": "941008"
    }
  ]
}
Field	Type	Description
timestamp	Long	Time Window
open_price	String	Opening Price
close_price	String	Closing Price
high_price	String	Highest Price
low_price	String	Lowest Price
volume	String	Turnover
Get Funding Rate History
Applicable for querying funding rate history data

Request URL
GET https://api-cloud-v2.bitmart.com/contract/public/funding-rate-history

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/public/funding-rate-history?symbol=BTCUSDT&limit=10
Field	Type	Required?	Description
symbol	String	Yes	Instrument name, e.g. BTCUSDT
limit	String	No	Number of results per request. The maximum is 100; The default is 100
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "list": [
      {
        "symbol": "BTCUSDT",
        "funding_rate": "0.000090600584",
        "funding_time": "1733979600000"
      }
    ]
  },
  "trace": "4b588ac6b7cb11ef96b16280797cd561.3819021.39457365988950452"
}
Field	Type	Description
list	list	Array of list details
Description of the list details field:

Field	Type	Description
symbol	String	Instrument name, e.g. BTCUSDT
funding_rate	String	Actual funding rate
funding_time	String	Settlement time, Unix timestamp format in milliseconds, e.g. 1733738400000
Get Current Leverage Risk Limit
Applicable for checking the current leverage risk limit of a specified contract

Request URL
GET https://api-cloud-v2.bitmart.com/contract/public/leverage-bracket

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/public/leverage-bracket?symbol=BTCUSDT
Field	Type	Required?	Description
symbol	String	No	Symbol of the contract(like BTCUSDT)
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "rules": [
      {
        "symbol": "FUNUSDT",
        "brackets": [
          {
            "bracket": 1,
            "initial_leverage": 50,
            "notional_cap": "10000",
            "notional_floor": "0",
            "maint_margin_ratio": "0.01",
            "cum": "0"
          },
          {
            "bracket": 2,
            "initial_leverage": 25,
            "notional_cap": "100000",
            "notional_floor": "10000",
            "maint_margin_ratio": "0.02",
            "cum": "100"
          },
          {
            "bracket": 3,
            "initial_leverage": 20,
            "notional_cap": "200000",
            "notional_floor": "100000",
            "maint_margin_ratio": "0.025",
            "cum": "600"
          },
          {
            "bracket": 4,
            "initial_leverage": 16,
            "notional_cap": "400000",
            "notional_floor": "200000",
            "maint_margin_ratio": "0.03125",
            "cum": "1850"
          },
          {
            "bracket": 5,
            "initial_leverage": 10,
            "notional_cap": "700000",
            "notional_floor": "400000",
            "maint_margin_ratio": "0.05",
            "cum": "9350"
          },
          {
            "bracket": 6,
            "initial_leverage": 8,
            "notional_cap": "1100000",
            "notional_floor": "700000",
            "maint_margin_ratio": "0.0625",
            "cum": "18100"
          },
          {
            "bracket": 7,
            "initial_leverage": 5,
            "notional_cap": "1600000",
            "notional_floor": "1100000",
            "maint_margin_ratio": "0.1",
            "cum": "59350"
          },
          {
            "bracket": 8,
            "initial_leverage": 4,
            "notional_cap": "2200000",
            "notional_floor": "1600000",
            "maint_margin_ratio": "0.125",
            "cum": "99350"
          },
          {
            "bracket": 9,
            "initial_leverage": 2,
            "notional_cap": "2900000",
            "notional_floor": "2200000",
            "maint_margin_ratio": "0.25",
            "cum": "374350"
          },
          {
            "bracket": 10,
            "initial_leverage": 1,
            "notional_cap": "3700000",
            "notional_floor": "2900000",
            "maint_margin_ratio": "0.5",
            "cum": "1099350"
          }
        ]
      }
    ]
  },
  "trace": "02bae860-de73-4a82-a1f5-fe38cd769275"
}
Field	Type	Description
bracket	Int	Risk bracket / Margin tier
initial_leverage	Int	Maximum leverage in this bracket
notional_cap	String	Maximum notional value in this bracket
notional_floor	String	Minimum notional value in this bracket
maint_margin_ratio	String	Maintenance margin ratio
cum	String	Cumulative maintenance margin amount
Futures Account Data
Get Contract Assets (KEYED)
Applicable for querying user contract asset details

Request URl
GET https://api-cloud-v2.bitmart.com/contract/private/assets-detail

Request Limit
See Detailed Rate Limit

Request Parameter
Request None

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/assets-detail
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [
    {
      "currency": "USDT",
      "position_deposit": "100",
      "frozen_balance": "100",
      "available_balance": "100",
      "equity": "100",
      "unrealized": "100"
    },
    {
      "currency": "BTC",
      "available_balance": "0",
      "frozen_balance": "0",
      "unrealized": "0",
      "equity": "0",
      "position_deposit": "0"
    },
    {
      "currency": "ETH",
      "available_balance": "0",
      "frozen_balance": "0",
      "unrealized": "0",
      "equity": "0",
      "position_deposit": "0"
    }
  ],
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
currency	String	Currency
position_deposit	String	Position margin
frozen_balance	String	Transaction freeze amount
available_balance	String	Available amount
equity	String	Total equity
unrealized	String	Unrealized P&L
Futures Trading
Get Trade Fee Rate (KEYED)
Applicable for querying trade fee rate

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/trade-fee-rate

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/trade-fee-rate?symbol=BTCUSDT
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "symbol": "BTCUSDT",
    "taker_fee_rate": "0.0006",
    "maker_fee_rate": "0.0002"
  },
  "trace": "638d5048-ad21-4a4b-1234-d0756fbfc7ba"
}
Field	Type	Description
symbol	String	Symbol of the contract
taker_fee_rate	String	Taker fee rate
maker_fee_rate	String	Maker fee rate
Get Order Detail (KEYED)
Applicable for querying contract order detail

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/order?symbol=BTCUSDT&order_id=220609666322019
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
order_id	String	Yes	Order ID
account	String	No	Trading account
-futures
-copy_trading
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "order_id": "220906179895578",
    "client_order_id": "BM123",
    "price": "1",
    "size": "1000",
    "symbol": "BTCUSDT",
    "state": 2,
    "side": 1,
    "type": "limit",
    "position_mode": "hedge_mode",
    "account": "futures",
    "leverage": "5",
    "open_type": "isolated",
    "deal_avg_price": "0",
    "deal_size": "1000",
    "create_time": 1662368173000,
    "update_time": 1662368173000
  },
  "trace": "638d5048-ad21-4a4b-9365-d0756fbfc7ba"
}
Field	Type	Description
symbol	String	Symbol of the contract
order_id	String	Order ID
client_order_id	String	Client-defined OrderId (If the field is not defined, a empty string is returned)
side	Int	Order side
hedge mode
-1=buy_open_long
-2=buy_close_short
-3=sell_close_long
-4=sell_open_short
oneway mode
-1=buy
-2=buy(reduce only)
-3=sell(reduce only)
-4=sell
type	String	Order type
-limit
- market
- liquidate
- bankruptcy
-adl
position_mode	String	Position mode
-hedge_mode
-one_way_mode
account	String	Trading account
-futures
-copy_trading
leverage	String	Leverage order multipliers
open_type	String	Open type
-cross
-isolated
deal_avg_price	String	Average deal price
deal_size	String	Deal amount
price	String	Consignment price
size	String	Order amount
state	Int	Order status
-1=status_approval
-2=status_check
-4=status_finish
activation_price	String	Activation price, returned at trailing order
callback_rate	String	Callback rate, returned at trailing order
activation_price_type	Int	Activation price type, returned at trailing order
-1=last_price
-2=fair_price
preset_take_profit_price_type	Int	Pre-set TP price type
-1=last_price
-2=fair_price
preset_stop_loss_price_type	Int	Pre-set SL price type
-1=last_price
-2=fair_price
preset_take_profit_price	String	Pre-set TP price
preset_stop_loss_price	String	Pre-set SL price
create_time	Long	Order created timestamp (ms)
update_time	Long	Latest transaction timestamp (ms)
Get Order History (KEYED)
Applicable for querying contract order history

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/order-history

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/order-history?symbol=BTCUSDT&start_time=1662368173&end_time=1662368179
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
order_id	String	No	Order ID
client_order_id	String	No	Client-defined OrderId
account	String	No	Trading account
-futures
-copy_trading
start_time	Long	No	Start time(Timestamp in Seconds)
end_time	Long	No	End time(Timestamp in Seconds)
Note
If the time range start_time and end_time are not filled in, the default query is the data of the last 7 days
If the time range is filled in, end_time must be greater than the value of start_time, and the maximum query interval of start_time and end_time is 90 days
Each request returns a maximum of 200 records, and any records exceeding that will not be returned.
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [
    {
      "order_id": "3000101684062644",
      "client_order_id": "PLAN_3000097492004577",
      "price": "0",
      "trigger_price": "0",
      "execution_price": "0",
      "size": "1",
      "symbol": "BTCUSDT",
      "state": 4,
      "side": 2,
      "type": "market",
      "account": "futures",
      "position_mode": "hedge_mode",
      "leverage": "20",
      "open_type": "cross",
      "deal_avg_price": "84802",
      "deal_size": "1",
      "create_time": 1743160485193,
      "update_time": 1743160485258,
      "activation_price_type": 1,
      "activation_price": "0",
      "callback_rate": "0",
      "preset_take_profit_price_type": 0,
      "preset_stop_loss_price_type": 0,
      "preset_take_profit_price": "",
      "preset_stop_loss_price": ""
    }
  ],
  "trace": "b15f261868b540889e57f826e0420621.80.17434162457898722"
}
Field	Type	Description
symbol	String	Symbol of the contract
order_id	String	Order ID
client_order_id	String	Client-defined OrderId (If the field is not defined, a empty string is returned)
side	Int	Order side
hedge mode
-1=buy_open_long
-2=buy_close_short
-3=sell_close_long
-4=sell_open_short
oneway mode
-1=buy
-2=buy(reduce only)
-3=sell(reduce only)
-4=sell
type	String	Order type
-limit
- market
- liquidate
- bankruptcy
- adl
- trailing
- planorder
account	String	Trading account
-futures
-copy_trading
position_mode	String	Position mode
-hedge_mode
-one_way_mode
leverage	String	Leverage order multipliers
open_type	String	Open type
-cross
-isolated
deal_avg_price	String	Average deal price
deal_size	String	Deal amount
price	String	Consignment price
trigger_price	String	Trigger price,returned at plan order
execution_price	String	Executive price,returned at plan order only
-Market price=If the execution price is a market price, return to Market
-Limit price=If the execution price is a limit price, return the set limit price
state	Int	Order status
-2=status_check
-4=status_finish
activation_price	String	Activation price, returned at trailing order
callback_rate	String	Callback rate, returned at trailing order
activation_price_type	Int	Activation price type, returned at trailing order
-1=last_price
-2=fair_price
executive_order_id	String	Activation Execute Order ID
preset_take_profit_price_type	Int	Pre-set TP price type
-0=unset
-1=last_price
-2=fair_price
preset_stop_loss_price_type	Int	Pre-set SL price type
-0=unset
-1=last_price
-2=fair_price
preset_take_profit_price	String	Pre-set TP price
preset_stop_loss_price	String	Pre-set SL price
create_time	Long	Order created timestamp (ms)
update_time	Long	Order updated timestamp (ms)
Get All Open Orders (KEYED)
Applicable for querying contract all open orders

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/get-open-orders

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/get-open-orders?symbol=BTCUSDT&order_state=partially_filled&type=market&limit=10
Field	Type	Required?	Description
symbol	String	No	Symbol of the contract(like BTCUSDT)
type	string	No	Order type
-limit
- market
- trailing
order_state	string	No	Order state
-all(default)
- partially_filled
limit	int	No	The number of returned results, with a maximum of 100 and a default of 100
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [
    {
      "order_id": "220908185908509",
      "client_order_id": "BM123",
      "price": "14277",
      "size": "7216",
      "symbol": "BTCUSDT",
      "state": 4,
      "side": 3,
      "type": "limit",
      "position_mode": "hedge_mode",
      "leverage": "0",
      "open_type": "isolated",
      "deal_avg_price": "14277",
      "deal_size": "7216",
      "preset_take_profit_price_type": 1,
      "preset_stop_loss_price_type": 2,
      "preset_take_profit_price": "68000",
      "preset_stop_loss_price": "60000",
      "create_time": 1662368173000,
      "update_time": 1662368173000
    }
  ],
  "trace": "80ba1f07-1b6f-46ad-81dd-78ac7e9bbccd"
}
Field	Type	Description
symbol	String	Symbol of the contract
order_id	String	Order ID
client_order_id	String	Client-defined OrderId (If the field is not defined, a empty string is returned)
side	Int	Order side
hedge mode
-1=buy_open_long
-2=buy_close_short
-3=sell_close_long
-4=sell_open_short
oneway mode
-1=buy
-2=buy(reduce only)
-3=sell(reduce only)
-4=sell
type	String	Order type
- limit
- market
- trailing
position_mode	String	Position mode
-hedge_mode
-one_way_mode
size	String	Order amount
leverage	String	Leverage order multipliers
String	String	Leverage order multipliers
open_type	String	Open type
-cross
-isolated
deal_avg_price	String	Average deal price
deal_size	String	Deal amount
price	String	Consignment price
state	Int	Order status
-2=status_check
activation_price	String	Activation price, returned at trailing order
callback_rate	String	Callback rate, returned at trailing order
activation_price_type	Int	Activation price type, returned at trailing order
-1=last_price
-2=fair_price
preset_take_profit_price_type	Int	Pre-set TP price type
-1=last_price
-2=fair_price
preset_stop_loss_price_type	Int	Pre-set SL price type
-1=last_price
-2=fair_price
preset_take_profit_price	String	Pre-set TP price
preset_stop_loss_price	String	Pre-set SL price
create_time	Long	Order created timestamp (ms)
update_time	Long	Order updated timestamp (ms)
Get All Current Plan Orders (KEYED)
Applicable for querying contract all plan orders

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/current-plan-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/current-plan-order?symbol=BTCUSDT&type=market&limit=10
Field	Type	Required?	Description
symbol	String	No	Symbol of the contract(like BTCUSDT)
type	String	No	Order type
-limit
- market
limit	int	No	The number of returned results, with a maximum of 100 and a default of 100
plan_type	String	No	Plan order type
-plan
- profit_loss
default all
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [
    {
      "order_id": "220908185908509",
      "client_order_id": "BM123",
      "executive_price": "14277",
      "trigger_price": "14277",
      "size": "7216",
      "symbol": "BTCUSDT",
      "state": 4,
      "side": 3,
      "mode": 1,
      "position_mode": "hedge_mode",
      "price_way": 2,
      "price_type": 1,
      "plan_category": 2,
      "type": "stop_loss",
      "leverage": "0",
      "open_type": "isolated",
      "create_time": 1662368173000,
      "update_time": 1662368173000
    }
  ],
  "trace": "80ba1f07-1b6f-46ad-81dd-78ac7e9bbccd"
}
Field	Type	Description
symbol	String	Symbol of the contract
order_id	String	Order ID
client_order_id	String	Client-defined OrderId (If the field is not defined, a empty string is returned)
side	Int	Order side
hedge mode
-1=buy_open_long
-2=buy_close_short
-3=sell_close_long
-4=sell_open_short
oneway mode
-1=buy
-2=buy(reduce only)
-3=sell(reduce only)
-4=sell
mode	Int	Order mode
-1=GTC
-2=FOK
-3=IOC
-4=Maker Only
position_mode	String	Position mode
-hedge_mode
-one_way_mode
price_way	Int	Price way
-1=price_way_long
-2=price_way_short
price_type	Int	Trigger price type
-1=last_price
-2=fair_price
type	String	Order type
- plan
- take_profit
- stop_loss
plan_category	Int	TP/SL type
- 1=TP/SL
- 2=Position TP/SL
size	String	Order amount
leverage	String	Leverage order multipliers
open_type	String	Open type
-cross
-isolated
executive_price	String	Executive price
trigger_price	String	Trigger price
state	Int	Order status
-1=status_approval
-2=status_check
preset_take_profit_price_type	Int	Pre-set TP price type
-1=last_price
-2=fair_price
preset_stop_loss_price_type	Int	Pre-set SL price type
-1=last_price
-2=fair_price
preset_take_profit_price	String	Pre-set TP price
preset_stop_loss_price	String	Pre-set SL price
create_time	Long	Order created timestamp (ms)
update_time	Long	Order updated timestamp (ms)
Get Current Position (KEYED)
Applicable for checking the position details a specified contract

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/position

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/position?symbol=BTCUSDT
Field	Type	Required?	Description
symbol	String	No	Symbol of the contract(like BTCUSDT)
account	String	No	Trading account
-futures
-copy_trading
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [
    {
      "symbol": "BTCUSDT",
      "leverage": "5",
      "timestamp": 1663814313531,
      "current_fee": "5.00409471",
      "open_timestamp": 1662714817820,
      "current_value": "16680.3157",
      "mark_value": "16673.27053207877",
      "mark_price": "93000.50",
      "position_value": "18584.272343943943943944339",
      "position_cross": "3798.397624451826977945",
      "maintenance_margin": "4798.397624451826977945",
      "margin_type":"Isolated",
      "position_mode": "hedge_mode",
      "close_vol": "100",
      "close_avg_price": "20700.7",
      "open_avg_price": "20200",
      "entry_price": "20201",
      "current_amount": "899",
      "unrealized_value": "1903.956643943943943944339",
      "realized_value": "55.049173071454605573",
      "position_type": 2,
      "account": "futures"
    }
  ],
  "trace": "ae96cae5-1f09-4ea5-971e-4474a6724bc8"
}
Field	Type	Description
leverage	String	Leverage multiplier
symbol	String	Symbol of the contract
current_fee	String	Current position fees
open_timestamp	Long	Opening timestamp
current_value	String	Position value based on last price
mark_value	String	Position value based on mark price
mark_price	String	mark price
position_value	String	Position value based on entry price
open_avg_price	String	Open average price
close_avg_price	String	Close average price
entry_price	String	Average entry price of the position
close_vol	String	Close volume
position_cross	String	Margin calls to positions
maintenance_margin	String	Maintenance Margin
margin_type	String	Margin type of the position
-Cross
-Isolated
position_mode	String	Position mode
-hedge_mode
-one_way_mode
current_amount	String	Current position amount
unrealized_value	String	Unrealized PnL
realized_value	String	Realized PnL
position_type	Int	position type
-1=long
-2=short
account	String	Trading account
-futures
-copy_trading
timestamp	Long	Current timestamp(ms)
Get Current Position V2 (KEYED)
Applicable for checking the position details a specified contract

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/position-v2

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/position-v2?symbol=BTCUSDT
Field	Type	Required?	Description
symbol	String	No	Symbol of the contract(like BTCUSDT)
account	String	No	Trading account
-futures(default)
-copy_trading
Note
If symbol is not provided, data will only be returned for trading pairs with existing positions; trading pairs without positions will not return any data.
If symbol is provided, data will be returned regardless of whether there is a position. If the user has no position, the position-related fields will be displayed as zero.
Response Data
For One-way position mode:

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [
    {
      "symbol": "BTCUSDT",
      "leverage": "51",
      "timestamp": 1746687390815,
      "current_fee": "0.0000397",
      "open_timestamp": 0,
      "current_value": "0",
      "mark_price": "98952",
      "position_value": "0",
      "position_cross": "0",
      "maintenance_margin": "0",
      "close_vol": "0",
      "close_avg_price": "0",
      "open_avg_price": "0",
      "entry_price": "0",
      "current_amount": "0",
      "position_amount": "5",
      "realized_value": "0",
      "mark_value": "0",
      "account": "futures",
      "open_type": "isolated",
      "position_side": "both",
      "unrealized_pnl": "0",
      "liquidation_price": "0",
      "max_notional_value": "500000",
      "initial_margin": "0"
    }
  ],
  "trace": "37ffeecd-3a6f-494a-8337-5c3a6012abfa"
}
For Hedge position mode：

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [
    {
      "symbol": "BTCUSDT",
      "leverage": "51",
      "timestamp": 1746687096451,
      "current_fee": "0.0000397",
      "open_timestamp": 0,
      "current_value": "0",
      "mark_price": "98911.62032609",
      "position_value": "0",
      "position_cross": "0",
      "maintenance_margin": "0",
      "close_vol": "0",
      "close_avg_price": "0",
      "open_avg_price": "0",
      "entry_price": "0",
      "current_amount": "0",
      "position_amount": "5",
      "realized_value": "0",
      "mark_value": "0",
      "account": "futures",
      "open_type": "isolated",
      "position_side": "long",
      "unrealized_pnl": "0",
      "liquidation_price": "0",
      "max_notional_value": "500000",
      "initial_margin": "0"
    },
    {
      "symbol": "BTCUSDT",
      "leverage": "51",
      "timestamp": 1746687096451,
      "current_fee": "0.0000397",
      "open_timestamp": 0,
      "current_value": "0",
      "mark_price": "98911.62032609",
      "position_value": "0",
      "position_cross": "0",
      "maintenance_margin": "0",
      "close_vol": "0",
      "close_avg_price": "0",
      "open_avg_price": "0",
      "entry_price": "0",
      "current_amount": "0",
      "position_amount": "5",
      "realized_value": "0",
      "mark_value": "0",
      "account": "futures",
      "open_type": "isolated",
      "position_side": "short",
      "unrealized_pnl": "0",
      "liquidation_price": "0",
      "max_notional_value": "500000",
      "initial_margin": "0"
    }
  ],
  "trace": "ab2131db-5827-45ca-a1be-94522510e107"
}
Field	Type	Description
leverage	String	Leverage multiplier
symbol	String	Symbol of the contract
current_fee	String	Current position fees
open_timestamp	Long	Opening timestamp
current_value	String	Position value based on last price
mark_price	String	Mark price
mark_value	String	Position value based on mark price
position_value	String	Position value based on entry price
open_avg_price	String	Open average price
close_avg_price	String	Close average price
entry_price	String	Average entry price of the position
close_vol	String	Close volume
position_cross	String	Margin calls to positions
maintenance_margin	String	Maintenance Margin
open_type	String	Position margin type
-cross
-isolated
position_side	String	Position side
-long
-short
-both
liquidation_price	String	Liquidation price
max_notional_value	String	Maximum notional value currently allowed
current_amount	String	Current position amount
position_amount	String	Current position direction amount
-Hedge mode=always positive
-One-way mode=positive represent long, negative represent short
unrealized_pnl	String	Unrealized PnL
realized_value	String	Realized PnL
initial_margin	String	Position margin
account	String	Trading account
-futures
-copy_trading
timestamp	Long	Current timestamp(ms)
Get Current Position Risk Details(KEYED)
Applicable for checking the position risk details a specified contract

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/position-risk

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/position-risk?symbol=BTCUSDT
Field	Type	Required?	Description
symbol	String	No	Symbol of the contract(like BTCUSDT)
account	String	No	Trading account
-futures
-copy_trading
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [
    {
      "symbol":"BTCUSDT",
      "position_amt":"1",
      "mark_price":"67957.7",
      "unrealized_profit":"969.6",
      "liquidation_price":"64245",
      "leverage":"20",
      "max_notional_value":"3000000",
      "margin_type":"Isolated",
      "isolated_margin":"3078.51948691",
      "position_side":"Long",
      "notional":"66988.1",
      "update_time":1712390438,
      "account": "futures"
    }
  ],
  "trace": "ae96cae5-1f09-4ea5-971e-4474a6724bc8"
}
字段	类型	描述
symbol	String	Symbol of the contract(like BTCUSDT)
position_amt	String	Position amount
mark_price	String	Mark Price of the contract
unrealized_profit	String	Unrealized profit of the position
liquidation_price	String	LiquidationPrice of the position
leverage	String	Position leverage
max_notional_value	String	Maximum notional value for the current risk level
margin_type	String	Margin type of the position
-Cross
-Isolated
isolated_margin	String	Margin for the isolated position
position_side	String	Position side
-Long
-Short
notional	String	notional = position_amt*mark_Price
account	String	Trading account
-futures
-copy_trading
update_time	Long	Unix timestamp in milliseconds for when the last updated time occurred
Get Order Trade (KEYED)
Applicable for querying contract order trade detail

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/trades

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/trades?symbol=BTCUSDT&start_time=1662368173&end_time=1662368179
Field	Type	Required?	Description
symbol	String	No	Symbol of the contract(like BTCUSDT)
account	String	No	Trading account
-futures
-copy_trading
start_time	Long	No	Start time(Timestamp in Seconds)
end_time	Long	No	End time(Timestamp in Seconds)
order_id	Long	No	Order ID
client_order_id	String	No	Client Order ID
Note
If the time range start_time and end_time are not filled in, the default query is the data of the last 7 days
If the time range is filled in, end_time must be greater than the value of start_time, and the maximum query interval of start_time and end_time is 90 days
Each request returns a maximum of 200 records, and any records exceeding that will not be returned.
Supported query order types: limit, market, liquidate, bankruptcy, adl, trailing
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [{
    "order_id": "220921197409432",
    "trade_id": "1141853921",
    "symbol": "BTCUSDT",
    "side": 1,
    "price": "19313.3",
    "vol": "108",
    "exec_type": "Maker",
    "profit": false,
    "realised_profit": "-0.00832",
    "paid_fees": "0",
    "account": "futures",
    "create_time": 1663663818589
  }],
  "trace": "638d5048-ad21-4a4b-9365-d0756fbfc7ba"
}
Field	Type	Description
symbol	String	Symbol of the contract
order_id	String	Order ID
trade_id	String	Trade detail ID
side	Int	Order side
hedge mode
-1=buy_open_long
-2=buy_close_short
-3=sell_close_long
-4=sell_open_short
oneway mode
-1=buy
-2=buy(reduce only)
-3=sell(reduce only)
-4=sell
price	String	Deal price
vol	String	Deal vol
profit	Boolean	Profitable or not
exec_type	String	Liquidity type
-Taker
-Maker
realised_profit	String	realised profit
paid_fees	String	paid fees
account	String	Trading account
-futures
-copy_trading
create_time	Long	Transaction create timestamp (ms)
Get Transaction History (KEYED)
Applicable for querying futures transaction history

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/transaction-history

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/contract/private/transaction-history?symbol=BTCUSDT&start_time=1662368173000&end_time=1662368179000
Field	Type	Required?	Description
symbol	String	No	Symbol of the contract
flow_type	Int	No	Type
- 0 = All (default)
- 1 = Transfer
- 2 = Realized PNL
- 3 = Funding Fee
- 4 = Commission Fee
- 5 = Liquidation Clearance
account	String	No	Trading account
-futures
-copy_trading
start_time	Long	No	Start time(Timestamp in Milliseconds)
end_time	Long	No	End time(Timestamp in Milliseconds)
page_size	Int	No	Default 100; max 1000
If start_time and end_time are not sent, only data from the last 7 days will be returned.
If type is not sent, all types of account profit and loss transaction history will be returned.
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": [
    {
      "symbol": "",
      "type": "Transfer",
      "amount": "-0.37500000",
      "asset": "USDT",
      "account": "futures",
      "time": "1570608000000",
      "tran_id": "9689322392"
    },
    {
      "symbol": "BTCUSDT",
      "type": "Commission Fee",
      "amount": "-0.01000000",
      "asset": "USDT",
      "account": "futures",
      "time": "1570636800000",
      "tran_id": "9689322392"
    }
  ],
  "trace": "80ba1f07-1b6f-46ad-81dd-78ac7e9bbccd"
}
Field	Type	Description
symbol	String	Symbol of the contract
flow_type	Int	Type
- 0 = All (default)
- 1 = Transfer
- 2 = Realized PNL
- 3 = Funding Fee
- 4 = Commission Fee
- 5 = Liquidation Clearance
type	String	Type
- Transfer
- Realized PNL
- Funding Fee
- Commission Fee
- Liquidation Clearance
account	String	Trading account
-futures
-copy_trading
amount	String	Amount, supports positive and negative values
asset	String	Transaction currency
time	String	Transaction timestamp, timestamp in ms
tran_id	String	Transaction ID
Get Transfer List (SIGNED)
Query futures account transfer records

Request URl
POST https://api-cloud-v2.bitmart.com/account/v1/transfer-contract-list

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
    "currency":"USDT",
    "time_start":1684391137804,
    "time_end":1684392577804,
    "page":1,
    "limit":10,
    "recvWindow":5000
}'
https://api-cloud-v2.bitmart.com/account/v1/transfer-contract-list
Field	Type	Required?	Description
currency	String	No	Currency (like USDT)
time_start	Long	No	Start time(Timestamp in Milliseconds, e.g. 1681701557927)
time_end	Long	No	End time (Timestamp in Milliseconds, e.g. 1681701557927)
page	Int	Yes	Number of pages, allowed range [1,1000]
limit	Int	Yes	Number of queries, allowed range [10,100]
recvWindow	Long	No	Trade time limit, allowed range (0,60000], default: 5000 milliseconds
Note
If the time range time_start and time_end are not filled in, all data will be displayed by default.
When filling in the time range, time_end must be greater than the value of time_start.
If only time_start is filled in, query the historical records starting from the timestamp.
If only time_end is filled in, query the historical records starting from this timestamp.
Response Data
Response

Copy Success{
    "message":"OK",
    "code":1000,
    "trace":"82abff12-b9d9-4f66-89ea-3b604c6d84",
    "data":{
        "records":[{
            "transfer_id":"664651258694168576",
            "currency":"USDT",
            "amount":"0.1",
            "type":"contract_to_spot",
            "state":"FINISHED",
            "timestamp":1638631674326
        }]
    }
}
Field	Type	Description
transfer_id	String	ID
currency	String	Currency
amount	String	Amount
type	String	Type
-spot_to_contract
-contract_to_spot
state	String	Result
-PROCESSING=Waiting to execute
-FINISHED=Successful transfer
-FAILED=Transfer failed
timestamp	Long	Transfer creation time in milliseconds, e.g. 1638631674326
Submit Order (SIGNED)
Applicable for placing contract orders

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/submit-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "client_order_id":"BM1234",
  "side":4,
  "mode":1,
  "type":"limit",
  "leverage":"1",
  "open_type":"isolated",
  "size":10,
  "price":"2000"
}'
https://api-cloud-v2.bitmart.com/contract/private/submit-order
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
client_order_id	String	No	Client-defined OrderId(A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters)
type	String	No	Order type
-limit(default)
-market
side	Int	Yes	Order side
hedge mode
-1=buy_open_long
-2=buy_close_short
-3=sell_close_long
-4=sell_open_short
oneway mode
-1=buy
-2=buy(reduce only)
-3=sell(reduce only)
-4=sell
leverage	String	No	Order leverage
open_type	String	No	Open type
-cross
-isolated
mode	Int	No	Order mode
-1=GTC(default)
-2=FOK
-3=IOC
-4=Maker Only
price	String	Yes	Order price, required at limit order
size	Int	Yes	Order size (Number of contracts)
preset_take_profit_price_type	Int	No	Pre-set TP price type
-1=last_price(default)
-2=fair_price
preset_stop_loss_price_type	Int	No	Pre-set SL price type
-1=last_price(default)
-2=fair_price
preset_take_profit_price	String	No	Pre-set TP price
preset_stop_loss_price	String	No	Pre-set SL price
stp_mode	Int	No	Self Trading Protection
-1=cancel_maker(default)
-2=cancel_taker
-3=cancel_both
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "order_id": 220609666322019,
    "price": "25637.2"
  },
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
order_id	Int	Order ID
price	String	Order Submit Price，if submit market type order，will return string："market price"
Modify Limit Order (SIGNED)
Applicable for modifying contract limit orders

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/modify-limit-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "order_id":220906179559421,
  "client_order_id":"123456",
  "price":"1450",
  "size":1
}'
https://api-cloud-v2.bitmart.com/contract/private/modify-limit-order
参数	类型	是否必填	描述
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
order_id	Int	No	Order ID(order_id or client_order_id must give one)
client_order_id	String	No	Client-defined OrderId(A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters)
price	String	No	Order Price（price or size must give one）
size	Int	No	Order Size（size or price must give one）
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "order_id": 220609666322019,
    "client_order_id": "123456"
  },
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
order_id	Int	Order ID
client_order_id	String	Client Order ID
Cancel Order (SIGNED)
Applicable for canceling a specific contract order

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/cancel-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "order_id": "220906179559421"
}'
https://api-cloud-v2.bitmart.com/contract/private/cancel-order
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT),（If not submitted order_id and client_order_id, cancel all orders under the symbol）
order_id	String	No	Order ID
client_order_id	String	No	Client-defined OrderId
Response Data
If code value is 1000, it means the order cancellation is successfully submitted, cancellation results will be pushed by websocket service.

Response

Copy Success{
  "code": 1000,
  "trace": "0cc6f4c4-8b8c-4253-8e90-8d3195aa109c",
  "message": "Ok",
  "data": {
  }
}
Cancel All Orders (SIGNED)
Applicable for batch order cancellation under a particular contract

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/cancel-orders

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT"
}'
https://api-cloud-v2.bitmart.com/contract/private/cancel-orders
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
Response Data
If code value is 1000, it means the order cancellation is successfully submitted, cancellation results will be pushed by websocket service.

Response

Copy Success{
  "code": 1000,
  "trace": "0cc6f4c4-8b8c-4253-8e90-8d3195aa109c",
  "message": "Ok",
  "data": {
  }
}
Timed Cancel All Orders (SIGNED)
Applicable for canceling all contract orders timed

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/cancel-all-after

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
   "timeout":10,
   "symbol":"BTCUSDT"
}'
https://api-cloud-v2.bitmart.com/contract/private/cancel-all-after
Field	Type	Required?	Description
timeout	Int	Yes	The duration of canceling orders(second,minimum value: 5 seconds) 0:Canceling the setting
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
Response Data
If code value is 1000, it means the order cancellation is successfully submitted, cancellation results will be pushed by websocket service.

Response

Copy Success{
  "code": 1000,
  "trace": "0cc6f4c4-8b8c-4253-8e90-8d3195aa109c",
  "message": "Ok",
  "data": {
    "result": true,
    "set_time": 1743064715,
    "cancel_time": 1743064725
  }
}
Field	type	Description
result	Bool	Is the setting successful: true/false
set_time	Int	Set time, timestamp
cancel_time	Int	The first time of cancel, timestamp
Submit Plan Order (SIGNED)
Applicable for placing contract plan orders

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/submit-plan-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "side":4,
  "mode":1,
  "type":"limit",
  "leverage":"1",
  "open_type":"isolated",
  "size":10,
  "trigger_price":"2000",
  "executive_price":"1450",
  "price_type":1,
  "price_way":1
}'
https://api-cloud-v2.bitmart.com/contract/private/submit-plan-order
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
type	String	No	Order type
-limit(default)
-market
-take_profit
-stop_loss
side	Int	Yes	Order side
hedge mode
-1=buy_open_long
-2=buy_close_short
-3=sell_close_long
-4=sell_open_short
oneway mode
-1=buy
-2=buy(reduce only)
-3=sell(reduce only)
-4=sell
leverage	String	Yes	Order leverage
open_type	String	Yes	Open type, required at close position
-cross
-isolated
mode	Int	No	Order mode
-1=GTC(default)
-2=FOK
-3=IOC
-4=Maker Only
size	Int	Yes	Order size (Number of contracts)
trigger_price	String	Yes	Trigger price
executive_price	String	No	Execution price for plan order, mandatory when type = limit
price_way	Int	Yes	Price way
-1=price_way_long
-2=price_way_short
price_type	Int	Yes	Trigger price type
-1=last_price
-2=fair_price
plan_category	Int	No	TP/SL type
-1=TP/SL
-2=Position TP/SL
preset_take_profit_price_type	Int	No	Pre-set TP price type
-1=last_price(default)
-2=fair_price
preset_stop_loss_price_type	Int	No	Pre-set SL price type
-1=last_price(default)
-2=fair_price
preset_take_profit_price	String	No	Pre-set TP price
preset_stop_loss_price	String	No	Pre-set SL price
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "order_id": 220609666322019
  },
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
order_id	Int	Order ID
Cancel Plan Order (SIGNED)
Applicable for canceling a specific contract plan order

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/cancel-plan-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "order_id": "220906179559421",
  "client_order_id": "123456789"
}'
https://api-cloud-v2.bitmart.com/contract/private/cancel-plan-order
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
order_id	String	No	Order ID
client_order_id	String	No	Client Order ID
Response Data
If code value is 1000, it means the order cancellation is successfully submitted, cancellation results will be pushed by websocket service.

Response

Copy Success{
  "code": 1000,
  "trace": "0cc6f4c4-8b8c-4253-8e90-8d3195aa109c",
  "message": "Ok",
  "data": {
  }
}
Transfer (SIGNED)
Transfer between spot account and contract account

Request URl
POST https://api-cloud-v2.bitmart.com/account/v1/transfer-contract

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "currency":"USDT",
  "amount":"10",
  "type":"spot_to_contract",
  "recvWindow":5000
}'
https://api-cloud-v2.bitmart.com/account/v1/transfer-contract
Field	Type	Required?	Description
currency	String	Yes	Currency (Only USDT is supported)
amount	String	Yes	Transfer amount，allowed range[0.01,10000000000]
type	String	Yes	Transfer type
-spot_to_contract
-contract_to_spot
recvWindow	Long	No	Trade time limit, allowed range (0,60000], default: 5000 milliseconds
Response Data
Response

Copy Success{
  "message":"OK",
  "code":1000,
  "trace":"34018ca3-fe24-446a-9e1d-f82edfb3e3",
  "data":{
    "currency":"USDT",
    "amount":"10"
  }
}
Field	Type	Description
currency	String	currency
amount	String	Amount successfully transferred
code returns 1000, which means the transfer is successful.
Submit Leverage (SIGNED)
Applicable for adjust contract leverage `

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/submit-leverage

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "leverage":"5",
  "open_type":"isolated"
}'
https://api-cloud-v2.bitmart.com/contract/private/submit-leverage
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
leverage	String	No	Order leverage
open_type	String	Yes	Open type, required at close position
-cross
-isolated
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "symbol":"ETHUSDT",
    "leverage":"5",
    "open_type":"isolated",
    "max_value":"100"
  },
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
symbol	String	Symbol of the contract(like BTCUSDT)
leverage	String	Order leverage
open_type	String	Open type, required at close position
-cross
-isolated
max_value	String	Maximum leverage
Submit TP/SL Order (SIGNED)
Applicable for placing contract TP/SL orders

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/submit-tp-sl-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "side":2,
  "type":"take_profit",
  "size":10,
  "trigger_price":"2000",
  "executive_price":"1450",
  "price_type":1,
  "plan_category":1,
  "client_order_id":"123456789",
  "category":"limit"
}'
https://api-cloud-v2.bitmart.com/contract/private/submit-plan-order
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
type	String	Yes	Order type
-take_profit
-stop_loss
side	Int	Yes	Order side
hedge mode
-2=buy_close_short
-3=sell_close_long
oneway mode
-2=buy(reduce only)
-3=sell(reduce only)
size	Int	No	Order size (Number of contracts) Default the size of position
trigger_price	String	Yes	Trigger price
executive_price	String	Yes	Execution price
price_type	Int	Yes	Trigger price type
-1=last_price
-2=fair_price
plan_category	Int	No	TP/SL type
-1=TP/SL
-2=Position TP/SL(default)
client_order_id	String	No	Client-defined OrderId(A combination of case-sensitive alphanumerics, all numbers, or all letters of up to 32 characters)
category	String	No	Trigger order type, position TP/SL default market
-limit
-market
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "order_id": "220609666322019",
    "client_order_id": "123456789"
  },
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
order_id	String	Order ID
client_order_id	String	Client Order ID
Modify Plan Order (SIGNED)
Applicable for modifying contract plan orders

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/modify-plan-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "order_id":"220906179559421",
  "trigger_price":"2000",
  "executive_price":"1450",
  "price_type":1,
  "type":"limit"
}'
https://api-cloud-v2.bitmart.com/contract/private/modify-plan-order
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
order_id	String	No	Order ID(order_id or client_order_id must give one)
trigger_price	String	Yes	Trigger price
executive_price	String	No	Execution price for plan order, mandatory when type = limit
price_type	Int	Yes	Trigger price type
-1=last_price
-2=fair_price
type	String	Yes	Order type
-limit
-market
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "order_id": "220609666322019"
  },
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
order_id	String	Order ID
Modify Preset Plan Order (SIGNED)
Applicable for modifying contract preset plan orders

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/modify-preset-plan-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "order_id":"220609666322019",
  "preset_take_profit_price":"2000",
  "preset_stop_loss_price":"1900",
  "preset_take_profit_price_type":1,
  "preset_stop_loss_price_type":1
}'
https://api-cloud-v2.bitmart.com/contract/private/modify-preset-plan-order
Field	Type	Required?	Description
order_id	String	Yes	Order ID
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
preset_take_profit_price_type	Int	No	Pre-set TP price type
-1=last_price(default)
-2=fair_price
preset_stop_loss_price_type	Int	No	Pre-set SL price type
-1=last_price(default)
-2=fair_price
preset_take_profit_price	String	No	Pre-set TP price
preset_stop_loss_price	String	No	Pre-set SL price
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "order_id": "220609666322019"
  },
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
order_id	String	Order ID
Modify TP/SL Order (SIGNED)
Applicable for modifying TP/SL orders

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/modify-tp-sl-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "trigger_price":"2100",
  "executive_price":"2100",
  "price_type":2,
  "order_id":"37758000001",
  "client_order_id":"",
  "plan_category":2,
  "category": "limit"
}'
https://api-cloud-v2.bitmart.com/contract/private/modify-tp-sl-order
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
order_id	String	No	Order ID(order_id or client_order_id must give one)
client_order_id	String	No	Client order ID(order_id or client_order_id must give one)
trigger_price	String	Yes	Trigger price
executive_price	String	No	Execution price for order, mandatory when plan_category = 1
price_type	Int	Yes	Trigger price type
-1=last_price
-2=fair_price
plan_category	Int	No	TP/SL type
-1=TP/SL
-2=Position TP/SL
category	String	No	Order type, Position TP/SL default market
-limit
-market
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "order_id": "220609666322019"
  },
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
order_id	String	Order ID
Submit Trail Order (SIGNED)
Applicable for placing contract trail orders

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/submit-trail-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "side":4,
  "leverage":"1",
  "open_type":"isolated",
  "size":10,
  "activation_price":"2000",
  "callback_rate":"1",
  "activation_price_type":1
}'
https://api-cloud-v2.bitmart.com/contract/private/submit-trail-order
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
side	Int	Yes	Order side
hedge mode
-1=buy_open_long
-2=buy_close_short
-3=sell_close_long
-4=sell_open_short
oneway mode
-1=buy
-2=buy(reduce only)
-3=sell(reduce only)
-4=sell
leverage	String	Yes	Order leverage
open_type	String	Yes	Open type, required at close position
-cross
-isolated
size	Int	Yes	Order size (Number of contracts)
activation_price	String	Yes	Activation price, required at trailing order
callback_rate	String	Yes	Callback rate, required at trailing order, min 0.1, max 5 where 1 for 1%
activation_price_type	Int	Yes	Activation price type, required at trailing order
-1=last_price
-2=fair_price
Response Data
Response

Copy Success{
  "code": 1000,
  "message": "Ok",
  "data": {
    "order_id": 220609666322019
  },
  "trace": "13f7fda9-9543-4e11-a0ba-cbe117989988"
}
Field	Type	Description
order_id	Int	Order ID
Cancel Trail Order (SIGNED)
Applicable for canceling a specific contract trail order

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/cancel-trail-order

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "symbol":"ETHUSDT",
  "order_id": "220906179559421"
}'
https://api-cloud-v2.bitmart.com/contract/private/cancel-trail-order
Field	Type	Required?	Description
symbol	String	Yes	Symbol of the contract(like BTCUSDT)
order_id	String	No	Order ID
Response Data
If code value is 1000, it means the order cancellation is successfully submitted, cancellation results will be pushed by websocket service.

Response

Copy Success{
  "code": 1000,
  "trace": "0cc6f4c4-8b8c-4253-8e90-8d3195aa109c",
  "message": "Ok",
  "data": {
  }
}
Set Position Mode (SIGNED)
Applicable for setting position mode

Request URL
POST https://api-cloud-v2.bitmart.com/contract/private/set-position-mode

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
  "position_mode":"one_way_mode"
}'
https://api-cloud-v2.bitmart.com/contract/private/set-position-mode
Field	Type	Required?	Description
position_mode	String	Yes	Position Mode
-hedge_mode
-one_way_mode
Response Data
Response

Copy Success{
  "code": 1000,
  "trace": "0cc6f4c4-8b8c-4253-8e90-8d3195aa109c",
  "message": "Ok",
  "data": {
    "position_mode":"one_way_mode"
  }
}
Field	Type	Description
position_mode	String	Position Mode
-hedge_mode
-one_way_mode
Get Position Mode (KEYED)
Applicable for getting position mode

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/get-position-mode

Request Limit
See Detailed Rate Limit

Request Parameter
Request

None

Copy Successcurl 
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
https://api-cloud-v2.bitmart.com/contract/private/get-position-mode
Response Data
Response

Copy Success{
  "code": 1000,
  "trace": "0cc6f4c4-8b8c-4253-8e90-8d3195aa109c",
  "message": "Ok",
  "data": {
    "position_mode":"one_way_mode"
  }
}
Field	Type	Description
position_mode	String	Position Mode
-hedge_mode
-one_way_mode
Simulated Trading
Simulated Trading
Simulation API Domain:

REST:https://demo-api-cloud-v2.bitmart.com

WebSocket Public Channel:wss://openapi-wsdemo-v2.bitmart.com/api?protocol=1.1

WebSocket Private Channel:wss://openapi-wsdemo-v2.bitmart.com/user?protocol=1.1

Tutorial
1. Create simulating trading API KEY
Please refer to this page to create an API keyCreate api key
While setting the API Key, for security reasons, it is recommended to set an IP access whitelist
2. Using simulated trading
The domain name and API path provided by the simulating trading are consistent with those of the actual trading
Please use the API key you created to request the REST domain name of the simulating trading and switch to the simulation environment
For example:Request URL
POST https://demo-api-cloud-v2.bitmart.com/contract/private/submit-order
FAQ
💡Q1. How to obtain the API key for simulating trading?
💬A: The simulated trading API key is equivalent to the online trading API key, it is the same key, but the requested domain name is different

💡Q2. How to use simulated trading USDX funds?
💬A: USDX uniformly uses USDT instead of USDT on the simulation trading API
For example:
* The trading pair 'BTCUDSX' is displayed as'BTCUDST'on the API
* Please also use 'symbol=BTCUSDT' when placing an order

💡Q3. Does simulated trading support spot trading, withdrawal, recharge, subscription redemption, and transfer?
💬A: Currently not supported

💡Q4. I use an online API key to call simulated trading. Is the fund also simulated trading?
💬A: Yes, automatically use simulated account funds after switching to simulated trading

💡Q5. How to switch from online environment to simulated trading?
💬A: Please use a simulated domain name https://demo-api-cloud-v2.bitmart.com Replace online https://api-cloud-v2.bitmart.com Switchable simulation trading

Claim (SIGNED)
Add available funds to the futures account (Only available in the Simulated-Environment)

Request URL
POST https://demo-api-cloud-v2.bitmart.com/contract/private/claim

Request Limit
See Detailed Rate Limit

Response Data
Response

Copy Success{
  "message":"OK",
  "code":1000,
  "trace":"34018ca3-fe24-446a-9e1d-f82edfb3e3",
  "data":{
    "currency":"USDT",
    "amount":"10"
  }
}
Field	Type	Description
currency	String	Currency
amount	String	Current asset balance
Sub-Account
Sub-Account interface function is currently open to institutional users only, and will be opened gradually
Sub-Account to Main-Account (For Main Account) (SIGNED)
Sub-account futures asset transfer to Main-account futures asset (For Main Account)

Request URL
POST https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/sub-to-main

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"USDT",
    "subAccount":"subAccountName@xxx.com"
}'
https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/sub-to-main`
Field	Type	Required?	Description
requestNo	String	Yes	UUID,unique identifier, max length 64
amount	String	Yes	Transfer amount
currency	String	Yes	Currently only USDT is supported
subAccount	String	Yes	Sub-Account username
Response Data
Response

Copy Success{
  "message": "OK",
  "code": 1000,
  "trace": "c1e4e99ff0ec452f8b8bc5f1eb38d733.76.16861963186213159",
  "data": {}
}
If code value is 1000,it means the transfer is successful.

Main-Account to Sub-Account (For Main Account) (SIGNED)
Main-account futures asset transfer to Sub-account futures asset (For Main Account)

Request URL
POST https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/main-to-sub

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"BTC",
    "subAccount":"subAccountName@xxx.com"
}'
https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/main-to-sub`
Field	Type	Required?	Description
requestNo	String	Yes	UUID,unique identifier, max length 64
amount	String	Yes	Transfer amount
currency	String	Yes	Currently only USDT is supported
subAccount	String	Yes	Sub-Account username
Response Data
Response

Copy Success{
  "message": "OK",
  "code": 1000,
  "trace": "c1e4e99ff0ec452f8b8bc5f1eb38d733.76.16861963186213159",
  "data": {}
}
If code value is 1000,it means the transfer is successful.

Sub-Account to Main-Account (For Sub-Account) (SIGNED)
Sub-Account futures asset transfer to Main-Account futures asset (For Sub-Account)

Request URL
POST https://api-cloud-v2.bitmart.com/account/contract/sub-account/sub/v1/sub-to-main

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl
 -H 'X-BM-KEY:{{AccessKey}}'
 -H 'X-BM-TIMESTAMP:{{currentTime}}'
 -H 'X-BM-SIGN:{{SIGN}}' 
 -X POST -d '{
    "requestNo":"4e2adcff-2122-1ce7-2557-4f65d2ce1ca2",
    "amount":"1",
    "currency":"USDT"
}'
https://api-cloud-v2.bitmart.com/account/contract/sub-account/sub/v1/sub-to-main`
Field	Type	Required?	Description
requestNo	String	Yes	UUID,unique identifier, max length 64
amount	String	Yes	Transfer amount
currency	String	Yes	Currently only USDT is supported
Response Data
Response

Copy Success{
  "message": "OK",
  "code": 1000,
  "trace": "c1e4e99ff0ec452f8b8bc5f1eb38d733.76.16861970092723253",
  "data": {}
}
If code value is 1000,it means the transfer is successful.

Get Sub-Account Futures Wallet Balance (For Main Account) (KEYED)
Get Sub-Account futures wallet balance (For Main Account) (KEYED)

Request URL
GET https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/wallet

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/wallet?subAccount=subAccount1@xxx.com&currency=USDT
Field	Type	Required?	Description
subAccount	String	Yes	Sub-Account username
currency	String	No	currency
Response Data
Response

Copy Success{
  "message": "OK",
  "code": 1000,
  "trace": "87db8cd43374470f96aacb0e3fcaf34c.77.16872314088656435",
  "data": {
    "wallet": [
      {
        "currency": "USDT",
        "name": "USDT",
        "available": "204.15216696",
        "frozen": "0.00000000"
      }
    ]
  }
}
Field	Type	Description
currency	String	Token symbol, e.g., 'BTC'
name	String	Token name, e.g., 'Bitcoin'
available	String	Available Balance
frozen	String	Frozen Balance
The return list contains only assets with a balance greater than 0.
Get Sub-Account Transfer History (For Main Account) (KEYED)
Query Sub-Account Futures Asset Transfer History (For Main Account)

Request URL
GET https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/transfer-list

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/account/contract/sub-account/main/v1/transfer-list?subAccount=subAccountName@xxx.com&limit=10
Field	Type	Required?	Description
subAccount	String	Yes	Sub-Account username
limit	Int	Yes	Recent N records, allowed range[1,100]
Response Data
Response

Copy Success{
  "message": "OK",
  "code": 1000,
  "trace": "ba950ec2bd114fd7bc069cb812b0129f.62.16887213774200649",
  "data": [
    {
      "fromAccount": "subAccountName@xxx.com",
      "toAccount": "masterAccountName@xxx.com",
      "toWalletType": "future",
      "fromWalletType": "future",
      "currency": "USDT",
      "amount": "1",
      "submissionTime": 1686207254
    }
  ]
}
Field	Type	Description
fromAccount	String	Transfer out Sub-Account username
fromWalletType	String	Transfer out wallet type
-future=futures wallet
toAccount	String	Transfer to Sub-Account username
toWalletType	String	Transfer to wallet type
-future=futures wallet
currency	String	currency
amount	String	Transfer amount
submissionTime	Long	The request timestamp is accurate to seconds(UTC-0)
Get Account Futures Asset Transfer History (For Main/Sub Account) (KEYED)
Get account Futures asset transfer history (For Main/Sub Account)

Request URL
GET https://api-cloud-v2.bitmart.com/account/contract/sub-account/v1/transfer-history

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl -H 'X-BM-KEY:{{AccessKey}}'
https://api-cloud-v2.bitmart.com/account/contract/sub-account/v1/transfer-history?limit=10
Field	Type	Required?	Description
limit	Int	Yes	Recent N records, allowed range[1,100]
Response Data
Response

Copy Success{
  "message": "OK",
  "code": 1000,
  "trace": "ba950ec2bd114fd7bc069cb812b0129f.62.16887215218140681",
  "data": [
    {
      "fromAccount": "masterAccount@xxx.com",
      "toAccount": "subAccount@xxx.com",
      "toWalletType": "future",
      "fromWalletType": "future",
      "currency": "USDT",
      "amount": "1",
      "submissionTime": 1686207254
    }
  ]
}
Field	Type	Description
fromAccount	String	Transfer out Sub-Account username
fromWalletType	String	Transfer out wallet type
-future=futures wallet
toAccount	String	Transfer to Sub-Account username
toWalletType	String	Transfer to wallet type
-future=futures wallet
currency	String	currency
amount	String	Transfer amount
submissionTime	Long	The request timestamp is accurate to seconds(UTC-0)
WebSocket Subscription
Overview
Server URL
Public Channel: wss://openapi-ws-v2.bitmart.com/api?protocol=1.1

Private Channel: wss://openapi-ws-v2.bitmart.com/user?protocol=1.1

Format
The message format sent by the client to the BitMart server.

{"action":"<operation>", "args":["<topic1>","<topic2>"]}

Explain:

operation request action, value: [subscribe=Subscribe channel, unsubscribe=Unsubscribe channel, login=Account login]
args request parameter, value: channel array or parameters required for login
topic channel topic, composed of <channel>:<filter>
channel is composed of business/name
filter is filterable data, refer to each channel description for details
Example:

Example 1: {"action": "subscribe", "args": ["futures/depth50:BTCUSDT"]}
Means to subscribe to the depth data of the trading pair BTCUSDT
Example 2: {"action": "login", "args": ["80618e45710812162b04892c7ee5ead4a3cc3e56", "1589267764859", "3ceeb7e1b8cb165a975e28a2e2dfaca4d30b358873c0351c1a071d8c83314556", "web"]}
Login request before private channel subscription
Successful Response Format
The format of the success message returned by the BitMart server to the client.

Return success field is ture

Successful Response Format

Copy SuccessWhen action=access ：
{"action":"access","success":true}

When action=unsubscribe ：
{"action":"unsubscribe","group":"Depth:1","success":true,"request":{"action":"unsubscribe","args":["Depth:1"]}}

When action=subscribe ：
{"action":"subscribe","group":"Depth:1","success":true,"request":{"action":"subscribe","args":["Depth:1"]}}
Example:

Example 1：{"action":"access","success":true}
Means successful login
Example 2：{"action":"unsubscribe","group":"futures/depth50:BTCUSDT","success":true,"request":{"action":"unsubscribe","args":["futures/depth50:BTCUSDT"]}}
Means successful cancellation of depth50 subscription for trading pair BTCUSDT
Example 3：{"action":"subscribe","group":"futures/depth50:BTCUSDT","success":true,"request":{"action":"subscribe","args":["futures/depth50:BTCUSDT"]}}
Means successful subscribe of depth50 subscription for trading pair BTCUSDT
Example 4：{"group":"futures/depth50:BTCUSDT","data":{"symbol":"BTCUSDT","way":2,"depths":[{"price":"30107.7","vol":"234"},{"price":"30107.8","vol":"1587"}]}}
Means the depth50 subscription of spot trading pair BTCUSDT, generates data, and returns it to the client
Failed Response Format
The format of the failed message returned by the BitMart server to the client.

Return success field is false

Failed Response Format

Copy Success{"action":"subscribe","group":"Depth:1","success":false,"error":"authentication is temporarily unavailable"}
Example 1：{"action":"subscribe","group":"futures/order","success":false,"error":"futures/order need authenication"}
Means you need to log in
Example 2：{"action":"access","success":false,"error":"access failed: openapi auth: apiKey 880d5edecs**** failed: openapi auth failed"}
Means login failed, your sign is wrong
Example 3：{"action":"subscribe","group":"sfutures/depth50:BTCUSDT","success":false,"request":{"action":"subscribe","args":["sfutures/depth50:BTCUSDT"]},"error":"group [sfutures/depth50:BTCUSDT] not exist"}
Means subscription failed, your parameter is invalid, this channel does not exist
Stay Connected And Limit
* If there is a network problem, the connection will be automatically disconnected, please set up the reconnection mechanism
How Stay Connected
WebSocket uses the Ping/Pong mechanism to maintain the connection. Once the connection is opened, a Ping frame is sent every N seconds, and the remote endpoint will return a Pong frame to keep responding. This is an approach to stay active. It helps to keep the connection open, especially if there is a short timeout proxy on an inactive connection.

If no data is returned after connecting to WebSocket, the link will be automatically disconnected after 20s. It is recommended that the user do the following:

After each message is received, the user sets a timer for N seconds (N<20).
If the timer is triggered (no new message is received within N seconds), send a ping frame or send a string 'ping'.
Expect for a text string 'pong' as a response. If not received within N seconds, please issue an error or reconnect.
We do not actively disconnect when there is a continuous message interaction between the two parties.
The following is the data format of ping: (Example in Java pseudocode)

Standard Ping frame
ws.send(new PingWebSocketFrame());

Ping Text
ws.send(new TextWebSocketFrame('{"action":"ping"}'));

Connection Limit
A maximum of 500 connections can be maintained between each IP and BitMart server.
Lifeless connection
Connection that do not send task subscription data within 5 seconds will be considered lifeless and the server will close the connection.

Subscription
Users can subscribe to one or more channels, and the total length of multiple channels cannot exceed 4096 bytes

Subscribe Message Format
{"action":"subscribe","args":["<topic>"]}

Parameter Instructions
action = subscribe
args = The content of the args array is the subscribed topic
topic is composed of <channel>:<filter>
channel is composed of business/name
filter can filter data, refer to the description of each channel for details
Example
Send message to BitMart server

{"action":"subscribe","args":["futures/klineBin1m:BTCUSDT"]}

The BitMart server returns the subscription result, success=true means the subscription is successful

{"action":"subscribe","group":"futures/klineBin1m:BTCUSDT","success":true,"request":{"action":"subscribe","args":["futures/klineBin1m:BTCUSDT"]}}

Unsubscribe
Cancel subscription to one or more channels

Unsubscribe Message Format
{"action": "unsubscribe", "args": ["<topic>"]}

Parameter Instruction
action = unsubscribe
args = The content of the args array is the subscribed topic
topic is composed of <channel>:<filter>
channel is composed of business/name
filter can filter data, refer to the description of each channel for details
Example
Send message to BitMart server

{"action": "unsubscribe", "args": ["futures/klineBin1m:BTCUSDT"]}

The BitMart server returns the subscription result, success=true means the subscription is successful

{"action":"unsubscribe","group":"futures/klineBin1m:BTCUSDT","success":true,"request":{"action":"unsubscribe","args":["futures/klineBin1m:BTCUSDT"]}}

【Public】Ticker Channel
Get the latest transaction price, bid one price, ask for one price, and 24 trading volumes of all perpetual contracts on the platform

Pushing Rules
No user login required
After subscribing, then the changes will be pushed
Sent once in 1 second after subscription
Request
Request

Copy Success{
  "action":"subscribe",
  "args":["futures/ticker:BTCUSDT"]
}
Message Format:

{"action":"subscribe","args":["<channel>:<symbol>"]}

actions: subscribe
channel: Channel name futures/ticker, fixed value
symbol: Trading pair, such as BTCUSDT
Response
Response

Copy Success{
    "data": {
        "symbol": "BTCUSDT",
        "last_price": "97153.6",
        "volume_24": "25502894",
        "range": "0.0016599204475393",
        "mark_price": "97153.7",
        "index_price": "97185.614",
        "ask_price": "97153.9",
        "ask_vol": "28",
        "bid_price": "97153.4",
        "bid_vol": "428"
    },
    "group": "futures/ticker:BTCUSDT"
}
Return data description:

Field	Type	Description
symbol	String	Symbol of the contract(like BTCUSDT)
last_price	String	Latest Price
volume_24	String	Volume of 24-hour transactions
range	String	Up or Down
mark_price	String	Mark Price
index_price	String	Index Price
ask_price	String	Sell depths first price
ask_vol	String	Sell depths first vol
bid_price	String	Buy depths first price
bid_vol	String	Buy depths first vol
【Public】Funding Rate Channel
Return funding Rate data

Pushing Rules
No user login required
After subscribing, the current data will be returned directly, and updates will be pushed every minute.
Request
Subscribe Request

Copy Success{
  "action":"subscribe",
  "args":["futures/fundingRate:BTCUSDT"]
}
Funding rate data Request

Copy Success{ 
  "action": "request", 
  "args":["futures/fundingRate:BTCUSDT"]
}
Message Format:

{"action": "<op>", "args": ["<channel:symbol>"]}

op: subscribe=Subscribe, You will receive a message that the subscription is successful, and then you will receive funding rate data pushed every minute. request=Single request for the latest funding rate data, You will receive a funding rate data immediately.
channel:Channel name, such asfutures/fundingRate
symbol: Trading pair, such asBTCUSDT
Response
Funding rate data

Copy Success{
    "data": {
        "symbol": "BTCUSDT",
        "fundingRate": "0.000098800809",
        "fundingTime": 1732525864000,
        "nextFundingRate": "0.0000947",
        "nextFundingTime": 1732550400000,
        "funding_upper_limit": "0.0375",
        "funding_lower_limit": "-0.0375",
        "ts": 1732525864601
    },
    "group": "futures/fundingRate:BTCUSDT"
}
Return data description:

Field	Type	Description
symbol	String	Symbol of the contract (like BTCUSDT)
fundingRate	String	Current funding rate
fundingTime	Long	Funding time of the upcoming settlement, Unix timestamp format in milliseconds
nextFundingRate	String	Forecasted funding rate for the next period
nextFundingTime	Long	Forecasted funding time for the next period, Unix timestamp format in milliseconds
funding_upper_limit	String	The upper limit of the predicted funding rate of the next cycle
funding_lower_limit	String	The lower limit of the predicted funding rate of the next cycle
ts	Long	Data return time, Unix timestamp format in milliseconds
【Public】Depth Channel
Get depth data

Pushing Rules
No user login required
After subscribing, then the changes will be pushed
Request
Request

Copy Success{
  "action":"subscribe",
  "args":["futures/depth20:BTCUSDT@200ms"]
}
Message Format:

{"action":"subscribe","args":["<channel:symbol><@speed>"]}

actions: subscribe
channel: Channel name, such as futures/depth20
symbol: Trading pair, such as BTCUSDT
speed: Update speed, support 200ms or 100ms
Parameters Channel Name List
Channel Name	Description
futures/depth5	5 Level Depth Channel
futures/depth20	20 Level Depth Channel
futures/depth50	50 Level Depth Channel
Response
Response

Copy Success{
    "group":"futures/depth20:BTCUSDT@200ms",
    "data":{
            "symbol":"BTCUSDT",
            "way":1,
            "depths":[
              {"price":"5","vol":"97"}
            ],
            "ms_t": 1542337219120
        }
}
Return data description:

Field	Type	Description
symbol	String	Symbol of the contract(like BTCUSDT)
way	Long	Trading side
-1=bid
-2=ask
depths	List	Array of depth details
ms_t	Long	Data push timestamp (in millisecond)
Instruction

Description of the depths details field:

Field	Type	Description
price	String	price
vol	String	volume
An example of the array of depths values: {"price":"20159.6","vol":"7284"}. price field is the price, and vol field is the quantity.
【Public】Depth-All Channel
Return depth data, each push is the full data

Pushing Rules
No user login required
After subscribing, then the changes will be pushed
Request
Request

Copy Success{
  "action":"subscribe",
  "args":["futures/depthAll20:BTCUSDT@200ms"]
}
Message Format:

{"action":"subscribe","args":["<channel:symbol><@speed>"]}

channel: Channel name, such asfutures/depthAll20
symbol: Trading pair, such asBTCUSDT
speed: Update speed, support 200ms or 100ms
Parameters Channel Name List

Channel Name	Description
futures/depthAll5	5 Level Depth Channel
futures/depthAll20	20 Level Depth Channel
futures/depthAll50	50 Level Depth Channel
Response
Response

Copy Success{
    "data": {
        "symbol": "BTCUSDT",
        "asks": [
            {
                "price": "70294.4",
                "vol": "455"
            }
        ],
        "bids": [
            {
                "price": "70293.9",
                "vol": "1856"
            }
        ],
        "ms_t": 1730399750402
    },
    "group": "futures/depthAll20:BTCUSDT@200ms"
}
Return data description:

Field	Type	Description
symbol	String	Symbol of the contract（like BTCUSDT）
asks	List	Asks Depth Array
bids	List	Bids Depth Array
ms_t	Long	Data push timestamp (in millisecond)
Instruction Description of the asks bids details field:

Field	Type	Description
price	String	price
vol	String	volume
An example of the array of depths values: {"price":"20159.6","vol":"7284"}. price field is the price, and vol field is the quantity.
【Public】Depth-Increase Channel
Return depth data, support the creation of a local full depth cache data

Pushing Rules
No user login required
After subscribing, the current data will be returned directly, and then the changes will be pushed
Request
Subscribe Request

Copy Success{
  "action":"subscribe",
  "args":["futures/depthIncrease20:BTCUSDT@200ms"]
}
Full depth snapshot data Request

Copy Success{ 
  "action": "request", 
  "args":["futures/depthIncrease20:BTCUSDT@200ms"]
}
Message Format:

{"action":"<op>","args":["<channel:symbol><@speed>"]}

op: subscribe=Subscribe, You will receive a message that the subscription is successful, and then you will receive incremental depth data pushed in real time. request=Single request for the latest depth snapshot, You will receive a full depth of data immediately.
channel:Channel name, such as futures/depthIncrease20
symbol: Trading pair, such as BTCUSDT
speed: Update speed, support 200ms or 100ms
Parameters Channel Name List

Channel Name	Description
futures/depthIncrease5	5 Level Depth Channel
futures/depthIncrease20	20 Level Depth Channel
futures/depthIncrease50	50 Level Depth Channel
Response
Full depth snapshot data

Copy Success{
    "data": {
        "symbol": "BTCUSDT",
        "asks": [
            {
                "price": "70391.6",
                "vol": "3550"
            }
        ],
        "bids": [
            {
                "price": "70391.2",
                "vol": "1335"
            }
        ],
        "ms_t": 1730400086184,
        "version": 980361,
        "type": "snapshot"
    },
    "group": "futures/depthIncrease20:BTCUSDT@200ms"
}
Incremental depth data

Copy Success{
    "data": {
        "symbol": "BTCUSDT",
        "asks": [
            {
                "price": "70395.3",
                "vol": "341"
            },
            {
                "price": "70395.4",
                "vol": "323"
            }
        ],
        "bids": [
            {
                "price": "70391.2",
                "vol": "0"
            },
            {
                "price": "70353.4",
                "vol": "11435"
            }
        ],
        "ms_t": 1730400086194,
        "version": 980362,
        "type": "update"
    },
    "group": "futures/depthIncrease20:BTCUSDT@200ms"
}
Return data description:

Field	Type	Description
symbol	String	Symbol of the contract (like BTCUSDT)
asks	List	Asks Depth Array
bids	List	Bids Depth Array
ms_t	Long	Data push timestamp (in millisecond)
version	Long	data version
type	String	data type
-snapshot=Full depth snapshot data
-update=Incremental depth data
Instruction

Description of the asks bids details field:

Field	Type	Description
price	String	price
vol	String	volume
An example of the array of depths values: {"price":"20159.6","vol":"7284"}. price field is the price, and vol field is the quantity.
How to correctly maintain a copy of OrderBook locally:
First, the client send a subscription request {"action": "subscribe", "args": ["futures/depthIncrease20:<symbol>"] }
After successful subscription, you will receive two types of messages, type=snapshot(full data)和type=update(update)
If a type=snapshot type message is received, update the deep snapshot content to thelocal cache. If there is no local cache, create one.
If a type=update message is received, update the data in the deep snapshot to local cache. The update rules are as follows:
4.1 If the field version number in the received new message is less than or equal to the version in the local cache(new version<=local version), this data can be discarded.
4.2 If the field version number in the new message received is equal to the version in the local cache plus 1(new version==local version+1), the quantity of the corresponding price will be updated to the local cache.
4.3 If the field version number in the new message received is greater than the version in the local cache plus 1(new version>local version+1), please obtain the latest depth snapshot from step 7 and overwrite the local cache.
The pending order volume in each returned message represents the absolute value of the current pending order volume at this price, rather than the relative change.
How to update local cache? Under the premise of 4.2:
6.1 New: If the same price is not already in the local cache, it means that it is a new pending order and needs to be added to the cache.
6.2 Modify or Remove: If the same price is already in the local cache, it means that the quantity has changed. If the quantity is 0, it will be directly removed from the cache. Otherwise, just change the quantity.
Request through request {"action": "request", "args": ["futures/depthIncrease20:<symbol>"] }to obtain the latest depth snapshot (type=snapshot in the message), and add the depth The content in the snapshot is overwritten to the local cache, and then the logic continues from step 2.
Abnormal Situation:
Because the depth snapshot has a limit on the number of price tiers, price tiers outside the initial snapshot and without quantity changes will not appear in the incremental depth update information. Therefore, even if all updates from the incremental depth are applied, these price brackets will not be visible in the local order book, so there may be some differences between the local order book and the real order book.
【Public】Individual Symbol Book Ticker Channel
Pushes any update to the best bid or ask's price or quantity in real-time for a specified symbol

Pushing Rules
No user login required
After subscribing, then the changes will be pushed
Real-time push
Request
Request

Copy Success{
  "action":"subscribe",
  "args":["futures/bookticker:BTCUSDT"]
}
Message Format:

{"action":"subscribe","args":["<channel:symbol>"]}

actions: subscribe
channel: Channel name, such as futures/bookticker
symbol: Trading pair, such as BTCUSDT
Response
Response

Copy Success{
    "data": {
        "symbol": "BTCUSDT",
        "best_bid_price": "97315",
        "best_bid_vol": "156",
        "best_ask_price": "97315.4",
        "best_ask_vol": "333",
        "ms_t": 1733891542244
    },
    "group": "futures/bookticker:BTCUSDT"
}
Return data description:

Field	Type	Description
symbol	String	Symbol of the contract(like BTCUSDT)
best_bid_price	String	Best bid price
best_bid_vol	String	Best bid volume
best_ask_price	String	Best ask price
best_ask_vol	String	Best ask volume
ms_t	Long	Data push timestamp (in millisecond)
【Public】Trade Channel
Get trade data

Pushing Rules
No user login required
After subscribing, then the changes will be pushed
Request
Request

Copy Success{
  "action":"subscribe",
  "args":["futures/trade:BTCUSDT"]
}
Message Format:

{"action":"subscribe","args":["<channel:symbol>","<channel:symbol>"]}

actions: subscribe
channel: Channel name futures/trade, fixed value
symbol: Trading pair, such as BTCUSDT
Response
Response

Copy Success{
  "group":"futures/trade:BTCUSDT",
  "data":[{
    "trade_id":1409495322,
    "symbol":"BTCUSDT",
    "deal_price":"117387.58",
    "deal_vol":"1445",
    "m":true,
    "created_at":"2023-02-24T07:54:11.124940968Z"
  }]
}

Return data description:

Field	Type	Description
symbol	String	symbol
deal_price	String	deal price
trade_id	Long	trade id
deal_vol	String	deal vol
way	Int	Trading type
-1=buy_open_long sell_open_short
-2=buy_open_long sell_close_long
-3=buy_close_short sell_open_short
-4=buy_close_short sell_close_long
-5=sell_open_short buy_open_long
-6=sell_open_short buy_close_short
-7=sell_close_long buy_open_long
-8=sell_close_long buy_close_short
m	Bool	-true=buyer is maker
-false=seller is maker
created_at	String	transaction create time(ms)
【Public】KlineBin Channel
Get individual contract K-line data

Pushing Rules
No user login required
After subscribing, then the changes will be pushed
Request
Request

Copy Success{"action":"subscribe","args":["futures/klineBin1m:BTCUSDT"]}
Message Format:

{"action":"subscribe","args":["<channel:symbol>","<channel:symbol>"]}

channel: Channel name, such as futures/klineBin1m
symbol: Trading pair, such as BTCUSDT
Parameters Channel Name List
Channel Name	Description
futures/klineBin1m	1-min klineBin Channel
futures/klineBin5m	5-min klineBin Channel
futures/klineBin15m	15-min klineBin Channel
futures/klineBin30m	30-min klineBin Channel
futures/klineBin1H	1-hour klineBin Channel
futures/klineBin2H	2-hour klineBin Channel
futures/klineBin4H	4-hour klineBin Channel
futures/klineBin1D	1-day klineBin Channel
futures/klineBin1W	1-week klineBin Channel
Response
Response

Copy Success{
    "group":"futures/klineBin1m:BTCUSDT",
    "data":{
            "symbol":"BTCUSDT",
            "o":"146.24",
            "h":"146.24",
            "l":"146.24",
            "c":"146.24",
            "v":"146",
            "ts":1700533801
        }
}
Return data description:

Field	Type	Description
symbol	String	Symbol of the contract(like BTCUSDT)
o	String	Opening Price
h	String	Highest Price
l	String	Lowest Price
c	String	Closing Price
v	String	Turnover
ts	Long	K-line timestamp（in second）
【Public】MarkPrice KlineBin Channel
Get individual contract K-line data

Pushing Rules
No user login required
After subscribing, then the changes will be pushed
Request
Request

Copy Success{"action":"subscribe","args":["futures/markPriceKlineBin1m:BTCUSDT"]}
Message Format:

{"action":"subscribe","args":["<channel:symbol>","<channel:symbol>"]}

channel: Channel name, such as futures/markPriceKlineBin1m
symbol: Trading pair, such as BTCUSDT
Parameters Channel Name List
Channel Name	Description
futures/markPriceKlineBin1m	1-min klineBin Channel
futures/markPriceKlineBin5m	5-min klineBin Channel
futures/markPriceKlineBin15m	15-min klineBin Channel
futures/markPriceKlineBin30m	30-min klineBin Channel
futures/markPriceKlineBin1H	1-hour klineBin Channel
futures/markPriceKlineBin2H	2-hour klineBin Channel
futures/markPriceKlineBin4H	4-hour klineBin Channel
futures/markPriceKlineBin1D	1-day klineBin Channel
futures/markPriceKlineBin1W	1-week klineBin Channel
Response
Response

Copy Success{
    "group":"futures/markPriceKlineBin1m:BTCUSDT",
    "data":{
            "symbol":"BTCUSDT",
            "o":"146.24",
            "h":"146.24",
            "l":"146.24",
            "c":"146.24",
            "v":"146",
            "ts":1700533801
        }
}
Return data description:

Field	Type	Description
symbol	String	Symbol of the contract(like BTCUSDT)
o	String	Opening Price
h	String	Highest Price
l	String	Lowest Price
c	String	Closing Price
v	String	Turnover
ts	Long	Data push timestamp (in second)
【Private】Login
Login Subscription Format
Request Format

Copy Success{"action":"access","args":["<API_KEY>","<timestamp>","<sign>","<dev>"]}
Please note that the following parameters are all of type String

API_KEY: The user's API key
timestamp: Timestamp, the unit is milliseconds, it will expire after 60 seconds
sign: Signature, sign=CryptoJS.HmacSHA256(timestamp + "#" + your_api_memo + "#" + "bitmart.WebSocket", your_api_secret_key)
dev: Device, web eg.
Example
Login Example

Copy Success{"action": "access", "args": ["80618e45710812162b04892c7ee5ead4a3cc3e56", "1589267764859", "3ceeb7e1b8cb165a975e28a2e2dfaca4d30b358873c0351c1a071d8c83314556","web"]}
Response

Copy Success{"action":"access","success":true}
Assume that the values of the API requested by the user is as follows:

timestamp=1589267764859
API_KEY = "80618e45710812162b04892c7ee5ead4a3cc3e56"
API_SECRET = "6c6c98544461bbe71db2bca4c6d7fd0021e0ba9efc215f9c6ad41852df9d9df9"
API_MEMO = "test001";
Ues Javascript create param sign: sign = CryptoJS.HmacSHA256(1589267764859 + "#" + test001 + "#" + "bitmart.WebSocket", '6c6c98544461bbe71db2bca4c6d7fd0021e0ba9efc215f9c6ad41852df9d9df9') = 3ceeb7e1b8cb165a975e28a2e2dfaca4d30b358873c0351c1a071d8c83314556

Ues Shell create param sign: sign = echo -n '1589267764859#test001#bitmart.WebSocket' | openssl dgst -sha256 -hmac "6c6c98544461bbe71db2bca4c6d7fd0021e0ba9efc215f9c6ad41852df9d9df9" (stdin)= 3ceeb7e1b8cb165a975e28a2e2dfaca4d30b358873c0351c1a071d8c83314556

The final login parameters are:

{"action": "access", "args": ["80618e45710812162b04892c7ee5ead4a3cc3e56", "1589267764859", "3ceeb7e1b8cb165a975e28a2e2dfaca4d30b358873c0351c1a071d8c83314556","web"]}

Note
1. If success field of return data is true, it indicates success
2. If the login fails, the link will be automatically disconnected
【Private】Assets Channel
Get asset balance change

Pushing Rules
User login required
After subscribing, then the changes will be pushed
Request
Request

Copy Success{
    "action": "subscribe",
    "args":["futures/asset:USDT", "futures/asset:BTC", "futures/asset:ETH"]
}
Message Format:

{"action":"subscribe","args":["<channel:currency>","<channel:currency>"]}

actions: subscribe
channel: Channel name futures/asset, fixed value
currency: Currency, such as BTC, asset types that support subscriptions are: USDT (U-native), BTC (coin-native), ETH (coin-native)
Response
Response

Copy Success{
  "group": "futures/asset:BTC",
  "data": {
    "currency": "BTC",
    "available_balance": "1000",
    "position_deposit": "1000",
    "frozen_balance": "1000"
  }
}
Return data description:

Field	Type	Description
currency	String	Currency
available_balance	String	Available Amount
position_deposit	String	Position Margin
frozen_balance	String	Transaction Frozen Amount
【Private】Position Channel
Get Position Data

Pushing Rules
User login required
After subscribing, then the changes will be pushed
10 seconds timed push
Request
Request

Copy Success{
    "action": "subscribe",
    "args":["futures/position"]
}
Message Format:

{"action":"subscribe","args":["<channel>"]}

actions: subscribe
channel: Channel name futures/position, fixed value
Response
Response

Copy Success{
  "group": "futures/position",
  "data": [
    {
      "symbol": "BTCUSDT",
      "hold_volume": "2000",
      "position_type": 1,
      "open_type": 1,
      "frozen_volume": "0",
      "close_volume": "0",
      "hold_avg_price": "19406.2092",
      "close_avg_price": "0",
      "open_avg_price": "19406.2092",
      "liquidate_price": "15621.998406",
      "create_time": 1662692862255,
      "update_time": 1662692862255,
      "position_mode": "hedge_mode"
    }
  ]
}
Return data description:

Field	Type	Description
symbol	String	Contract pair (e.g. BTCUSDT)
hold_volume	String	Number of positions
position_type	Int	Position type
-1=long
-2=short
open_type	Int	Open position type
-1=isolated
-2=cross
frozen_volume	String	Frozen volume
close_volume	String	Close volume
hold_avg_price	String	Average price of a position
close_avg_price	String	Average close price
open_avg_price	String	Average opening price
liquidate_price	String	Liquidation price
create_time	Long	Position created timestamp (ms)
update_time	Long	Position updated timestamp (ms)
position_mode	String	Position mode
-hedge_mode
-one_way_mode
【Private】Order Channel
Order Channel, which pushes immediately when the order status, transaction amount, etc. changes.

Pushing Rules
User login required
After subscribing, then the changes will be pushed
Request
Request

Copy Success{
  "action": "subscribe",
  "args": ["futures/order"]
}
Message Format:

{"action":"subscribe","args":["<channel>"]}

actions: subscribe
channel: Channel name futures/order, fixed value
Response
Response

Copy Success{
  "group": "futures/order",
  "data": [
    {
      "action": 3,
      "order": {
        "order_id": "220906179895578",
        "client_order_id": "BM1234",
        "price": "1",
        "size": "1000",
        "symbol": "BTCUSDT",
        "state": 2,
        "side": 1,
        "type": "limit",
        "leverage": "5",
        "open_type": "isolated",
        "deal_avg_price": "0",
        "deal_size": "0",
        "create_time": 1662368173000,
        "update_time": 1662368173000,
        "plan_order_id": "220901412155341",
        "last_trade": {
          "lastTradeID": 1247592391,
          "fillQty": "1",
          "fillPrice": "25667.2",
          "fee": "-0.00027",
          "feeCcy": "USDT"
        },
        "trigger_price": "-",
        "trigger_price_type": "-",
        "execution_price": "-",
        "activation_price_type": "-",
        "activation_price": "-",
        "callback_rate": "-",
        "position_mode": "hedge_mode"
      }
    }
  ]
}
Return data description:

Field	Type	Description
action	Int	Action
-1=match deal
-2=submit order
-3=cancel order
-4=liquidate cancel order
-5=adl cancel order
-6=part liquidate
-7=bankruptcy order
-8=passive adl match deal
-9=active adl match deal
symbol	String	Symbol of the contract
order_id	String	Order ID
client_order_id	String	Client-defined OrderId
side	Int	Order side
hedge mode
-1=buy_open_long
-2=buy_close_short
-3=sell_close_long
-4=sell_open_short
oneway mode
-1=buy
-2=buy(reduce only)
-3=sell(reduce only)
-4=sell
type	String	Order type
-limit
-market
-plan_order
-trailing_order
-take_profit
-stop_loss
leverage	String	Leverage order multipliers
open_type	String	Open type
-cross
-isolated
deal_avg_price	String	Average deal price
deal_size	String	Deal amount
price	String	Consignment price
state	Int	Order status
-1=status_approval
-2=status_check
-4=status_finish
create_time	Long	Order created timestamp (ms)
update_time	Long	Order updated timestamp (ms)
plan_order_id	String	Trigger plan order id
last_trade	object	recently trade info for this order，return null if not exist
trigger_price	String	Trigger price of TP/SL / plan order
trigger_price_type	String	Trigger price type of TP/SL / plan order
-last_price
-fair_price
execution_price	String	Execution price of TP/SL / plan order
activation_price	String	Activation price
activation_price_type	String	Activation price type
-last_price
-fair_price
callback_rate	String	Call back rate of trailing stop order
position_mode	String	Position mode
-hedge_mode
-one_way_mode
last_trade fields describe：

Parameter	Type	Description
lastTradeID	Long	recently trade id
fillQty	String	last trade deal vol
fillPrice	String	last trade deal price
fee	String	last trade fee
feeCcy	String	last trade fee coin name
Futures Affiliate Endpoints
Get Futures Rebate List(KEYED)
Used for API affiliates to query contract rebate records within a certain time range

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/affiliate/rebate-list

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/private/affiliate/rebate-list?page=1&size=10&currency=USDT
Field	Type	Required	Description
user_id	Long	No	user ID
page	Int	Yes	Page number
size	Int	Yes	Number of records per page
currency	String	Yes	query currency
rebate_start_time	Long	No	Query rebate start timestamp(in second)
rebate_end_time	Long	No	Query rebate end timestamp(in second)
register_start_time	Long	No	Query register start timestamp(in second)
register_end_time	Long	No	Query register end timestamp(in second)
Response Data
Response

Copy Success{
  "total": 2,
  "btc_rebate_sum": 0,
  "size": 10,
  "usdt_rebate_sum": 448.9697507148,
  "page": 1,
  "eth_rebate_sum": 0,
  "rebate_detail_page_data": [{
    "rebate_coin": "USDT",
    "trade_user_id": 4225149,
    "total_rebate_amount": 427.1825970576,
    "user_type":1
  }, {
    "rebate_coin": "USDT",
    "trade_user_id": 4225148,
    "total_rebate_amount": 21.7871536572,
    "user_type":1
  }]
}
Field	Type	Description
btc_rebate_sum	Decimal	Total BTC rebates
usdt_rebate_sum	Decimal	Total USDT rebates
eth_rebate_sum	Decimal	Total ETH rebates
rebate_detail_page_data	Object	Rebate details
rebate_coin	String	Currency
trade_user_id	Long	Trading user ID
total_rebate_amount	Decimal	Total commission for the user
user_type	Int	User type
-0=Indirect
-1=Direct
Get Futures Trade List(KEYED)
Used for API affiliates to query contract rebate records within a certain time range

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/affiliate/trade-list

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/private/affiliate/trade-list?user_id=123456&type=1&page=1&size=10
Field	Type	Required	Description
user_id	Long	Yes	userID
type	Int	Yes	Query type:
-1=U-based
-2=Coin-based
page	Int	Yes	Page number
size	Int	Yes	Number of records per page
start_time	Long	No	Query start timestamp(in second)
end_time	Long	No	Query end timestamp(in second)
Response Data
Response

Copy Success{
  "total": 60,
  "size": 10,
  "page": 1,
  "list": [{
    "leverage": 20.000000000000000000,
    "symbol": "BTCUSDT",
    "create_time": 1689933471000,
    "open_type": 2,
    "fee": 0.57162048,
    "deal_price": 29771.900000000000000000,
    "realised_profit": 0,
    "way": 1,
    "deal_vol": 32.000000000000000000,
    "select_copy_trade": 1,
    "user_type": 1,
    "user_id": 10048829,
    "category": 2
  }]
}
Field	Type	Description
user_id	Long	userID
user_type	Int	User Type:
-Direct User
-Indirect User
create_time	Long	Creation Time
symbol	String	symbol
leverage	Int	leverage
select_copy_trade	Int	Type:
1-Copy Trading
2-Non-Copy Trading
open_type	Int	Position Type:
-1=Isolated
-2=Cross
way	Int	Order Direction:
-1=Long
-2=Close Short
-3=Close Long
-4=Short
category	Int	Order Type:
-1=Limit Order
-2=Market Order
deal_price	Decimal	Average Deal Price
deal_vol	Decimal	Deal Volume
fee	Decimal	fee
realised_profit	Decimal	Realized Profit and Loss
Get Single User Rebate Data (KEYED)
Used by API affiliates to query contract rebate data of a single user within a given time range.

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/affiliate/rebate-user

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/private/affiliate/rebate-user?cid=1000000&start_time=1000000000&end_time=2000000000
Field	Type	Required	Description
cid	Long	Yes	User CID to query (Supports all agents and directly/indirectly invited users under your name.)
start_time	Long	Yes	Start timestamp of data query (in second)
end_time	Long	Yes	End timestamp of data query (in second)
Note
If the time range is filled in, end_time must be greater than the value of start_time, and the maximum query interval of start_time and end_time is 60 days
Response Data
Response

Copy Success{
  "code": "1000",
  "data": {
    "trading_vol_total": "483628.63308",
    "trading_fee": "287.910914",
    "back_rate": "90.00000000",
    "trading_vol": "483628.63308",
    "rebate": "259.1198226",
    "trading_fee_total": "287.910914",
    "rebate_total": "259.1198226",
    "cid": 166668888
  },
  "success": true,
  "requestId": "5f7fca16fbee4f74b3a9896d93f2c104",
  "message": "OK"
}
Field	Type	Description
cid	Long	User CID
back_rate	String	User rebate rate
trading_vol_total	String	User total trading volume
trading_fee_total	String	User total trading fee
rebate_total	String	User total rebate
trading_vol	String	User trading volume
trading_fee	String	User trading fee
rebate	String	User rebate
Get Single API User Rebate Data (KEYED)
Used by API affiliates to retrieve contract API rebate data for a single user over a given time range.

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/affiliate/rebate-api

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/private/affiliate/rebate-api?cid=1000000&start_time=1000000000&end_time=2000000000
Field	Type	Required	Description
cid	Long	Yes	User CID to query (Supports all agents and directly/indirectly invited users under your name.)
start_time	Long	Yes	Query start timestamp (in second)
end_time	Long	Yes	Query end timestamp (in second)
Note
If the time range is filled in, end_time must be greater than the value of start_time, and the maximum query interval of start_time and end_time is 60 days
Response Data
Response

Copy Success{
  "code": "1000",
  "data": {
    "api_trading_fee_total": "888",
    "api_rebate_total": "666"
  },
  "success": true,
  "requestId": "5f7fca16fbee4f74b3a9896d93f2c104",
  "message": "OK"
}
Field	Type	Description
api_trading_fee_total	String	API trading fee rebate
api_rebate_total	String	API rebate
GET Check If It Is An Invited User (KEYED)
Used for API This is suitable for agents to check whether a user is a user they invited.

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/affiliate/invite-check

Request Limit
See Detailed Rate Limit

Request Parameter
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/private/affiliate/invite-check?cid=1000000
Field	Type	Required	Description
cid	Long	Yes	User CID to Query
Response Data
Response

Copy Success{
  "code": "1000",
  "message": "OK",
  "success": true,
  "data": {"isInviteUser":true},
  "requestId": "215f9381064244ebb21fdb191ff8fa51",
  "trace": null
}
Field	Type	Description
isInviteUser	Boolean	Is this an invited user
-true= Yes
-false= No
Get Invited Customer List (KEYED)
Used by agents to query rebate information of invited users within a specified time range.

Request URL
GET https://api-cloud-v2.bitmart.com/contract/private/affiliate/rebate-inviteUser

Request Limit
See Detailed Rate Limit

Request Parameters
Request

Copy Successcurl https://api-cloud-v2.bitmart.com/contract/private/affiliate/rebate-inviteUser?start_time=1000000000&end_time=2000000000&page=1&size=10
Field	Type	Required	Description
cid	Long	No	User CID to query
start_time	Long	Yes	Query start timestamp (in second)
end_time	Long	Yes	Query end timestamp (in second)
page	Integer	Yes	Page number
size	Integer	Yes	Number of records per page
Note
If the time range is filled in, end_time must be greater than the value of start_time, and the maximum query interval of start_time and end_time is 60 days
The maximum size is 50 records. If the number exceeds 50, only 50 records will be retrieved.
Response Data
Response

Copy Success{
  "code": "1000",
  "message": "OK",
  "success": true,
  "data": {
    "list": [
      {
        "rebateTotal": "0",
        "tradingVolTotal": "0",
        "cashbackRate": "0.00000000",
        "tradingFeeTotal": "0",
        "backRate": "30.00000000",
        "cid": 100000000,
        "status": 1
      }
    ],
    "page": 1,
    "size": 10,
    "total": 10
  },
  "requestId": "d0ca45a64b1449a79a5773c705165a27",
  "trace": null
}

Field	Type	Description
rebateTotal	String	Cumulative Commission Rebate Amount (converted to USDT)
tradingVolTotal	String	Cumulative trading volume (converted to USDT)
cashbackRate	String	Cashback percentage
tradingFeeTotal	String	Total transaction fees (converted to USDT)
backRate	String	Rebate rate
cid	Long	User CID
status	Integer	Is the Rebate issued
-1= Yes
-0= No
Error Code
Restful Error Code
List of global HTTP return codes
HTTP	Description
404	Not Found-The requested interface could not be found
403	Forbidden-No permission to access the resource (KEY may not have permission, or it may be IP restrictions)
401	Unauthorized-Authentication failed (there are problems with the 3 header parameters, failed)
500	Internal Server Error-Server exception, BitMart service problem
Authentication Error Code
Example: httpStatus:200, body:{"code": 1000, "message": "OK", "trace": "12323-3243242-34334534-4353","data":{}}

error message	code error code	http status code
Not found	30000	404
Header X-BM-KEY is empty	30001	401
Header X-BM-KEY not found	30002	401
Header X-BM-KEY has frozen	30003	401
Header X-BM-SIGN is empty	30004	401
Header X-BM-SIGN is wrong	30005	401
Header X-BM-TIMESTAMP is empty	30006	401
Header X-BM-TIMESTAMP range. Within a minute	30007	401
Header X-BM-TIMESTAMP invalid format	30008	401
IP is forbidden. We recommend enabling IP whitelist for API trading. After that reauth your account	30010	403
Header X-BM-KEY over expire time	30011	403
Header X-BM-KEY is forbidden to request it	30012	403
Request too many requests	30013	429
Service unavailable	30014	503
Service maintenance, the function is temporarily unavailable	30016	200
Your account request is temporarily rejected due to violation of current limiting rules, please contact customer service	30017	418
Request Body requires JSON format	30018	503
You do not have the permissions to perform this operation. Please contact customer service or BD for assistance	30019	200
Futures V1 API has been deprecated. Please use Futures V2 API. You can view the change logs for upgrade	30030	200
This endpoint has been deprecated. You can view the change logs for upgrade	30031	200
Contract API Error Code
Example: httpStatus:400, body:{"code": 40001, "message":"out_trade_no not found", "trace":"8bynjk-nmoew-sd1221-csd-123" }

errMsg error message	code error code	http status code
OK	1000	200
Cloud account not found	40001	400
out_trade_no not found	40002	400
out_trade_no already existed	40003	400
Cloud account count limit	40004	400
Transfer vol precision error	40005	400
Invalid ip error	40006	400
Parse parameter error	40007	400
Check nonce error	40008	400
Check ver error	40009	400
Not found func error	40010	400
Invalid request	40011	400
System error	40012	400
Access too often" CLIENT_TIME_INVALID, "Please check your system time.	40013	400
This contract is offline	40014	400
This contract's exchange has been paused	40015	400
This order would trigger user position liquidate	40016	400
It is not possible to open and close simultaneously in the same position	40017	400
Your position is closed	40018	400
Your position is in liquidation delegating	40019	400
Your position volume is not enough	40020	400
The position is not exsit	40021	400
The position is not isolated	40022	400
The position would liquidate when sub margin	40023	400
The position would be warnning of liquidation when sub margin	40024	400
The position’s margin shouldn’t be lower than the base limit	40025	400
You cross margin position is in liquidation delegating	40026	400
You contract account available balance not enough	40027	400
Your plan order's count is more than system maximum limit.	40028	400
The order's leverage is too large.	40029	400
The order's leverage is too small.	40030	400
The deviation between current price and trigger price is too large.	40031	400
The plan order's life cycle is too long.	40032	400
The plan order's life cycle is too short.	40033	400
The Symbol is not exist	40034	400
The order is not exist	40035	400
The order status is invalid	40036	400
The order id is not exist	40037	400
The k-line step is invalid	40038	400
The timestamp is invalid	40039	400
The order leverage is invalid	40040	400
The order side is invalid	40041	400
The order type is invalid	40042	400
The order precision is invalid	40043	400
The order range is invalid	40044	400
The order open type is invalid	40045	400
The account is not opened futures	40046	403
Services is not available in you countries and areas	40047	403
ClientOrderId only allows a combination of numbers and letters	40048	403
The maximum length of clientOrderId cannot exceed 32	40049	403
Client OrderId duplicated with existing orders	40050	403
Insufficient balance	42000	200
