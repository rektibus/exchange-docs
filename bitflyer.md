API Documentation
Service for Lightning FX has been terminated as of Thursday, March 28th, 2024.
Our new service, bitFlyer Crypto CFD, is available from same day.

The API of bitFlyer Crypto CFD is compatible with the API of Lightning FX, and the same API specifications as before can be used for trading.
- In the API "Market List," the "market_type" of bitFlyer Crypto CFD is "FX", succeeding the "market_type" of Lightning FX.
- The "product_code" for BTC-CFD/JPY used in each API will be FX_BTC_JPY, succeeding the "product_code" of FX BTC/JPY.
- A new API "Funding Rate" is newly introduced to obtain the funding rate transfer ratio.

The API specifications may be subject to change in the future to align with bitFlyer Crypto CFD.
Any changes to the API specifications will be announced in advance.

bitFlyer Lightning offers two styles of API, the HTTP API and Realtime API.

Regions
API functionality may be limited by region. Specific products, such as markets, may not be available in every region. Specific order pairs may be limited to a specific region as well.

Please note that samples are based on JP region.

bitFlyer USA: BTC_USD, BTC_JPY, ETH_BTC
bitFlyer Europe: BTC_EUR, BTC_JPY, ETH_BTC
HTTP API
Japan Endpoint URL: https://api.bitflyer.com/v1/ U.S. Endpoint URL: https://api.bitflyer.com/v1/ Europe Endpoint URL: https://api.bitflyer.com/v1/

For HTTP API, Public API does not require API Key, while Private API requires API Key authentication.

You can try out our API at the API Playground.

API Limits
Please be aware of the HTTP API usage limits described below.
When exceeding an API limit, future API requests will be blocked temporarily.
After being blocked, the maximum request limit will be temporarily be decreased.

Condition	Limitation
Same IP Address	500 queries per 5 minutes
Orders with volume <= 0.1	100 placements per minute**
Private APIs	500 queries per 5 minutes
Send a New Order
POST /v1/me/sendchildorder
Submit New Parent Order (Special order)
POST /v1/me/sendparentorder
Cancel All Orders
POST /v1/me/cancelallchildorders	300 queries per 5 minutes
** Exceeding this limit will enforce a temporary decreased limit of 10 times per minute for the duration of 1 hour

If we determine that orders are being repeatedly placed with the intent of increasing the load on the system, we may place restrictions on the user's API usage.

Authentication
bitFlyer Private APIs require authentication using an API Key and API Secret. They can be obtained by generating them on the developer's page.

The following HTTP request headers are required to properly authenticate a request:

ACCESS-KEY: API key issued by the developer's page
ACCESS-TIMESTAMP: The request's Unix Timestamp.
ACCESS-SIGN: Signature generated for each request with the following method.
The ACCESS-SIGN is the resulting HMAC-SHA256 hash of the ACCESS-TIMESTAMP, HTTP method, request path, and request body concatenated together as a character string, created using your API secret.

// Node.js sample
var request = require('request');
var crypto = require('crypto');

var key = '{{ YOUR API KEY }}';
var secret = '{{ YOUR API SECRET }}';

var timestamp = Date.now().toString();
var method = 'POST';
var path = '/v1/me/sendchildorder';
var body = JSON.stringify({
    product_code: 'BTC_JPY',
    child_order_type: 'LIMIT',
    side: 'BUY',
    price: 30000,
    size: 0.1
});

var text = timestamp + method + path + body;
var sign = crypto.createHmac('sha256', secret).update(text).digest('hex');

var options = {
    url: 'https://api.bitflyer.com' + path,
    method: method,
    body: body,
    headers: {
        'ACCESS-KEY': key,
        'ACCESS-TIMESTAMP': timestamp,
        'ACCESS-SIGN': sign,
        'Content-Type': 'application/json'
    }
};
request(options, function (err, response, payload) {
    console.log(payload);
});
API key permissions
When you set up an API key, you can set the permissions for each key. In order to access a list of the permissions held by the API key, please use the Get API permissions API.

API key permissions

Pagination
APIs that return many results can use query parameters to retrieve results within a specified range.

count: Specifies the number of results. If this is omitted, the value will be 100.
before: Obtains data having an id lower than the value specified for this parameter.
after: Obtains data having an id higher than the value specified for this parameter.
Two-factor Authentication
Since 2FA must be enabled for withdrawals, you will also need 2FA when using bitFlyer APIs. The authentication code is entered in the request parameters. If the code parameter is not included or is incorrect, the following error response will be returned.

Authenticate by including the verification code in the request as the code parameter.

{
   "status": -505,
   "error_message": "Two-factor authentication code is incorrect."
}
If you have enabled 2FA by email or SMS, a confirmation code will be sent. Please use the received confirmation code in your request.

HTTP Public API
Market List
Request
GET /v1/getmarkets
GET /v1/markets
GET /v1/getmarkets/usa
GET /v1/markets/usa
GET /v1/getmarkets/eu
GET /v1/markets/eu
Response
[
  {
    "product_code": "BTC_JPY",
    "market_type": "Spot"
  },
  {
    "product_code": "XRP_JPY",
    "market_type": "Spot"
  },
  {
    "product_code": "ETH_JPY",
    "market_type": "Spot"
  },
  {
    "product_code": "XLM_JPY",
    "market_type": "Spot"
  },
  {
    "product_code": "MONA_JPY",
    "market_type": "Spot"
  },
  {
    "product_code": "ETH_BTC",
    "market_type": "Spot"
  },
  {
    "product_code": "BCH_BTC",
    "market_type": "Spot"
  },
  {
    "product_code": "FX_BTC_JPY",
    "market_type": "FX"
  }
]
market_type: Spot or FX
Order Book
Request
GET /v1/getboard
GET /v1/board
Query parameters

product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
Response
{
  "mid_price": 33320,
  "bids": [
    {
      "price": 30000,
      "size": 0.1
    },
    {
      "price": 25570,
      "size": 3
    }
  ],
  "asks": [
    {
      "price": 36640,
      "size": 5
    },
    {
      "price": 36700,
      "size": 1.2
    }
  ]
}
Ticker
Request
GET /v1/getticker
GET /v1/ticker
Query parameters

product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.

Response
{
  "product_code": "BTC_JPY",
  "state": "RUNNING",
  "timestamp": "2015-07-08T02:50:59.97",
  "tick_id": 3579,
  "best_bid": 30000,
  "best_ask": 36640,
  "best_bid_size": 0.1,
  "best_ask_size": 5,
  "total_bid_depth": 15.13,
  "total_ask_depth": 20,
  "market_bid_size": 0,
  "market_ask_size": 0,
  "ltp": 31690,
  "volume": 16819.26,
  "volume_by_product": 6819.26
}
state: Please refer to Orderbook status
timestamp: Time in UTC
ltp: Final trade price
volume: 24-hour trade volume
market_bid_size: Market sell order volume under Itayose period
market_ask_size: Market buy order volume under Itayose period
Execution History
Request
GET /v1/getexecutions
GET /v1/executions
Query parameters

product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
count, before, after: See Pagination. As of December 19, 2018, the execution history obtainable through the before parameter will be limited to the most recent 31 days.
Response
[
  {
    "id": 39287,
    "side": "BUY",
    "price": 31690,
    "size": 27.04,
    "exec_date": "2015-07-08T02:43:34.823",
    "buy_child_order_acceptance_id": "JRF20150707-200203-452209",
    "sell_child_order_acceptance_id": "JRF20150708-024334-060234"
  },
  {
    "id": 39286,
    "side": "SELL",
    "price": 33170,
    "size": 0.36,
    "exec_date": "2015-07-08T02:43:34.72",
    "buy_child_order_acceptance_id": "JRF20150708-010230-400876",
    "sell_child_order_acceptance_id": "JRF20150708-024334-197755"
  }
]
Orderbook status
Request
GET /v1/getboardstate
Query parameters

product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.

Response
{
  "health": "NORMAL",
  "state": "RUNNING",
}

{
  "health": "NORMAL",
  "state": "MATURED",
  "data": {
    "special_quotation": 410897
  }
}
health: Operational status of the exchange. Will display one of the following results.
NORMAL: The exchange is operating.
BUSY: The exchange is experiencing high traffic.
VERY BUSY: The exchange is experiencing very heavy traffic.
SUPER BUSY: The exchange is experiencing extremely heavy traffic. There is a possibility that orders will fail or be processed after a delay.
NO ORDER: Orders can not be received.
STOP: The exchange has been stopped. Orders will not be accepted.
state: State of the order book. Displays one of the following:
RUNNING: Operating
CLOSED: Suspending
STARTING: Restarting
PREOPEN: Performing Itayose
CIRCUIT BREAK: Circuit breaker triggered
data: Additional information on the order book.
*These items may change or new items may be added in the future.

Exchange status
This will allow you to determine the current status of the exchange.

Request
GET /v1/gethealth
Query parameters

product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
Response
{
  "status": "NORMAL"
}
status: one of the following levels will be displayed
NORMAL: The exchange is operating.
BUSY: The exchange is experiencing high traffic.
VERY BUSY: The exchange is experiencing very heavy traffic.
SUPER BUSY: The exchange is experiencing extremely heavy traffic. There is a possibility that orders will fail or be processed after a delay.
STOP: The exchange has been stopped. Orders will not be accepted.
Funding rate
Obtain the next scheduled funding rate transfer ratio that will be collected or granted.

Request
GET /v1/getfundingrate
Query parameters

product_code: Within the "product_code" that you can obtain from the Market List, specify "FX" as "market_type". This cannot be omitted.
"FX" will remain as "market_type" for the time being after the launch of bitFlyer Crypto CFD on March 28th, 2024.

"FX_BTC_JPY" will remain as "product_code" for the time being after the launch of bitFlyer Crypto CFD on March 28th, 2024.

Response
{
  "current_funding_rate": -0.003750000000
  "next_funding_rate_settledate": "2024-04-15T13:00:00"
}
current_funding_rate: Funding rate transfer ratio that will be collected or granted, displayed in rate.
next_funding_rate_settledate: Timing of next funding rate collection or grant, displayed in UTC (Coordinated Universal Time).
Max leverage for corporate accounts
You can retrieve information on the max leverage for corporate accounts here. The following information is for clients with corporate accounts.

Request
GET /v1/getcorporateleverage
Response
{
    "current_max": 7.70,
    "current_startdate": "2021-04-27T15:00:00",
    "next_max": 7.65,
    "next_startdate": "2021-05-04T15:00:00"
}
current_max: The current max leverage.
current_startdate: The effective date/time from which the current max leverage applies.
next_max: The next applicable max leverage (no value is returned if it is yet to be determined).
next_startdate: The effective date/time from which the next max leverage will apply (no value is returned if it is yet to be determined).
Chat
Obtain the chat log.

Request
GET /v1/getchats
GET /v1/getchats/usa
GET /v1/getchats/eu
Query parameters

from_date: This accesses a list of any new messages after this date. Defaults to the previous 5 days if left blank.
Response
[
  {
    "nickname": "User1234567",
    "message": "Hello world!",
    "date": "2016-02-16T10:58:08.833"
  },
  {
    "nickname": "TestUser",
    "message": "TestHello",
    "date": "2016-02-15T10:18:06.67"
  }
]
Please note this request will only pull the chat logs from Japan if you use /v1/getchats. Use /v1/getchats/usa and /v1/getchats/eu to pull their respective regional chat logs.

HTTP Private API
Authentication is required for requests using the Private API. See the Authentication section.

Get API Key Permissions
Returns a list of HTTP Private APIs that can be used with the API key provided in the header of the request.

Request
GET /v1/me/getpermissions
Response
[ "/v1/me/getpermissions",
  "/v1/me/getbalance",
  "/v1/me/getcollateral",
  "/v1/me/getchildorders",
  "/v1/me/getparentorders",
  "/v1/me/getparentorder",
  "/v1/me/getexecutions",
  "/v1/me/getpositions"
]
Get Account Asset Balance
Request
GET /v1/me/getbalance
Response
[
  {
    "currency_code": "JPY",
    "amount": 1024078,
    "available": 508000
  },
  {
    "currency_code": "BTC",
    "amount": 10.24,
    "available": 4.12
  },
  {
    "currency_code": "ETH",
    "amount": 20.48,
    "available": 16.38
  }
]
Get Margin Status
Request
GET /v1/me/getcollateral
Response
{
  "collateral": 100000,
  "open_position_pnl": -715,
  "require_collateral": 19857,
  "keep_rate": 5.000,
  "margin_call_amount": 1000000,
  "margin_call_due_date": "2021-09-01T08:00:00"
}
collateral: The amount deposited in JPY.
open_position_pnl: The profit or loss from valuation.
require_collateral: The current required margin.
keep_rate: The current maintenance margin.
margin_call_amount: The margin call.
margin_call_due_date: The margin call due date.
Request
GET /v1/me/getcollateralaccounts
Response
[
  {
    "currency_code": "JPY",
    "amount": 10000
  },
  {
    "currency_code": "BTC",
    "amount": 1.23
  }
]
Obtain the details of your margin deposits for each currency.

Get Crypto Assets Deposit Addresses
Get a crypto asset address for making deposits to your bitFlyer account.

Request
GET /v1/me/getaddresses
Response
[
  {
    "type": "NORMAL",
    "currency_code": "BTC",
    "address": "3AYrDq8zhF82NJ2ZaLwBMPmaNziaKPaxa7"
  },
  {
    "type": "NORMAL",
    "currency_code": "ETH",
    "address": "0x7fbB2CC24a3C0cd3789a44e9073381Ca6470853f"
  }
]
type: "NORMAL" for general deposit addresses.
currency_code: "BTC" for Bitcoin addresses and "ETH" for Ethereum addresses.
Get Crypto Assets Deposit History
Request
GET /v1/me/getcoinins
Query parameters

count, before, after: See Pagination.
Response
[
  {
    "id": 100,
    "order_id": "CDP20151227-024141-055555",
    "currency_code": "BTC",
    "amount": 0.00002,
    "address": "1WriteySQufKZ2pVuM1oMhPrTtTVFq35j",
    "tx_hash": "9f92ee65a176bb9545f7becb8706c50d07d4cee5ffca34d8be3ef11d411405ae",
    "status": "COMPLETED",
    "event_date": "2015-11-27T08:59:20.301"
  }
]
status: If the Bitcoin deposit is being processed, it will be listed as "PENDING". If the deposit has been completed, it will be listed as "COMPLETED".
Get Crypto Assets Transaction History
Request
GET /v1/me/getcoinouts
Query parameters

count, before, after: See Pagination.
Response
[
  {
    "id": 500,
    "order_id": "CWD20151224-014040-077777",
    "currency_code": "BTC",
    "amount": 0.1234,
    "address": "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa",
    "tx_hash": "724c07dfd4044abcb390b0412c3e707dd5c4f373f0a52b3bd295ce32b478c60a",
    "fee": 0.0005,
    "additional_fee": 0.0001,
    "status": "COMPLETED",
    "event_date": "2015-12-24T01:40:40.397"
  }
]
status: If remittance is being processed, it will be listed as "PENDING". If remittance has been completed, it will be listed as "COMPLETED".
Get Summary of Bank Accounts
Returns a summary of bank accounts registered to your account.

Request
GET /v1/me/getbankaccounts
Response
[
  {
    "id": 3402,
    "is_verified": true,
    "bank_name": "Wells Fargo",
    "branch_name": "1231234123",
    "account_type": "Checking",
    "account_number": "1111111",
    "account_name": "Name on Account"
  }
]
id: ID for the account designated for withdrawals.
is_verified: Will be return true if the account is verified and capable of sending money.
Get Cash Deposits
Request
GET /v1/me/getdeposits
Query parameters

count, before, after: See Pagination.
Response
[
  {
    "id": 300,
    "order_id": "MDP20151014-101010-033333",
    "currency_code": "JPY",
    "amount": 10000,
    "status": "COMPLETED",
    "event_date": "2015-10-14T10:10:10.001"
  }
]
status: If the cash deposit is being processed, it will be listed as "PENDING". If the deposit has been completed, it will be listed as "COMPLETED".
Withdrawing Funds
Request
POST /v1/me/withdraw
Body parameters

{
  "currency_code": "JPY",
  "bank_account_id": 1234,
  "amount": 12000
}
currency_code: Required. Currently only compatible with "JPY" for Japanese accounts.
bank_account_id: Required. The id of the bank account.
amount: Required. The amount that you are canceling.
code: Two-factor authentication code. Reference the two-factor authentication section.
Additional fees apply for withdrawals. Please see the Fees and Taxes page for reference.

Response
{
  "message_id": "69476620-5056-4003-bcbe-42658a2b041b"
}
message_id: Transaction Message Receipt ID

Error Response:

{
  "status": -700,
  "error_message": "This account has not yet been authenticated",
  "data": null
}
If an error with a negative status value is returned, the cancellation has not been committed.

Get Deposit Cancellation History
Request
GET /v1/me/getwithdrawals
Query parameters

count, before, after: See Pagination.
message_id: Check the withdrawal status by specifying the receipt ID from the returned value from the withdrawal API.
Response
[
  {
    "id": 700,
    "order_id": "MWD20151020-090909-011111",
    "currency_code": "JPY",
    "amount": 12000,
    "status": "COMPLETED",
    "event_date": "2015-10-20T09:09:09.416"
  }
]
status: If the cancellation is being processed, it will be listed as "PENDING". If the cancellation has been completed, it will be listed as "COMPLETED".
Send a New Order
Request
POST /v1/me/sendchildorder
Body parameters

{
  "product_code": "BTC_JPY",
  "child_order_type": "LIMIT",
  "side": "BUY",
  "price": 30000,
  "size": 0.1,
  "minute_to_expire": 10000,
  "time_in_force": "GTC"
}
product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
child_order_type: Required. For limit orders, it will be "LIMIT". For market orders, "MARKET".
side: Required. For buy orders, "BUY". For sell orders, "SELL".
price: Specify the price. This is a required value if child_order_type has been set to "LIMIT".
size: Required. Specify the order quantity.
minute_to_expire: Specify the time in minutes until the expiration time. The maximum value is 43200 (30 days). If omitted, the value will be 43200 (30 days).
time_in_force: Specify any of the following execution conditions - "GTC", "IOC", or "FOK". If omitted, the value defaults to "GTC".
Response
If the parameters are correct, the status code will show 200 OK.

{
    "child_order_acceptance_id": "JRF20150707-050237-639234"
}
child_order_acceptance_id: This is the ID for the API. To specify the order to return, please use this instead of child_order_id. Please confirm the item is either Cancel Order or List Executions.
Cancel Order
Request
POST /v1/me/cancelchildorder
Body parameters

{
  "product_code": "BTC_JPY",
  "child_order_id": "JOR20150707-055555-022222"
}

{
  "product_code": "BTC_JPY",
  "child_order_acceptance_id": "JRF20150707-033333-099999"
}
product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
Please specify either child_order_id or child_order_acceptance_id

child_order_id: ID for the canceling order.
child_order_acceptance_id: Expects an ID from Send a New Order. When specified, the corresponding order will be cancelled.
Response
If the parameters are correct, the status code will show 200 OK.

Submit New Parent Order (Special order)
It is possible to place orders with logic more complicated than limit orders (LIMIT) and market orders (MARKET). Such orders are handled as parent orders. By using a special order, it is possible to place orders in response to market conditions or place multiple associated orders.

Please read about the types of special orders and their methods in the bitFlyer Lightning documentation on special orders.

Request
POST /v1/me/sendparentorder
Body parameters

{
  "order_method": "IFDOCO",
  "minute_to_expire": 10000,
  "time_in_force": "GTC",
  "parameters": [{
    "product_code": "BTC_JPY",
    "condition_type": "LIMIT",
    "side": "BUY",
    "price": 30000,
    "size": 0.1
  },
  {
    "product_code": "BTC_JPY",
    "condition_type": "LIMIT",
    "side": "SELL",
    "price": 32000,
    "size": 0.1
  },
  {
    "product_code": "BTC_JPY",
    "condition_type": "STOP_LIMIT",
    "side": "SELL",
    "price": 28800,
    "trigger_price": 29000,
    "size": 0.1
  }]
}
order_method: The order method. Please set it to one of the following values. If omitted, the value defaults to "SIMPLE".
"SIMPLE": A special order whereby one order is placed.
"IFD": Conducts an IFD order. In this method, you place two orders at once, and when the first order is completed, the second order is automatically placed.
"OCO": Conducts an OCO order. In this method, you place two orders at one, and when one of the orders is completed, the other order is automatically canceled.
"IFDOCO": Conducts an IFD-OCO order. In this method, once the first order is completed, an OCO order is automatically placed.
minute_to_expire: Specifies the time until the order expires in minutes. The maximum value is 43200 (30 days). If omitted, the value defaults to 43200 (30 days).
time_in_force: Specify any of the following execution conditions - "GTC", "IOC", or "FOK". If omitted, the value defaults to "GTC".
parameters: Required value. This is an array that specifies the parameters of the order to be placed. The required length of the array varies depending upon the specified order_method.
If "SIMPLE" has been specified, specify one parameter.
If "IFD" has been specified, specify two parameters. The first parameter is the parameter for the first order placed. The second parameter is the parameter for the order to be placed after the first order is completed.
If "OCO" has been specified, specify two parameters. Two orders are placed simultaneously based on these parameters.
If "IFDOCO" has been specified, specify three parameters. The first parameter is the parameter for the first order placed. After the order is complete, an OCO order is placed with the second and third parameters.
In the parameters, specify an array of objects with the following keys and values.

product_code: Required value. This is the product to be ordered. Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
condition_type: Required value. This is the execution condition for the order. Please set it to one of the following values.
"LIMIT": Limit order.
"MARKET": Market order.
"STOP": Stop order.
"STOP_LIMIT": Stop-limit order.
"TRAIL": Trailing stop order.
side: Required value. For buying orders, specify "BUY", for selling orders, specify "SELL".
size: Required value. Specify the order quantity.
price: Specify the price. This is a required value if condition_type has been set to "LIMIT" or "STOP_LIMIT".
trigger_price: Specify the trigger price for a stop order. This is a required value if condition_type has been set to "STOP" or "STOP_LIMIT".
offset: Specify the trail width of a trailing stop order as a positive integer. This is a required value if condition_type has been set to "TRAIL".
Response
If the parameters are correct, the status code will show 200 OK.

{
  "parent_order_acceptance_id": "JRF20150707-050237-639234"
}
parent_order_acceptance_id: This is the ID for the API. To specify the order to return, please use this instead of parent_order_id.
Cancel parent order
Parent orders can be canceled in the same manner as regular orders. If a parent order is canceled, the placed orders associated with that order will all be canceled.

Request
POST /v1/me/cancelparentorder
Body parameters

{
  "product_code": "BTC_JPY",
  "parent_order_id": "JCO20150925-055555-022222"
}

{
  "product_code": "BTC_JPY",
  "parent_order_acceptance_id": "JRF20150925-033333-099999"
}
product_code: Required. The product for the corresponding order. Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
Please specify only one between parent_order_id and parent_order_acceptance_id

parent_order_id: ID for the canceling order.
parent_order_acceptance_id: Expects an ID from Submit New Parent Order. When specified, the corresponding order will be cancelled.
Response
If the parameters are correct, the status code will show 200 OK.

Cancel All Orders
Cancel all existing orders for the corresponding product.

Request
POST /v1/me/cancelallchildorders
Body parameters

{
  "product_code": "BTC_JPY"
}
product_code: The product for the corresponding order. Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
Response
If the parameters are correct, the status code will show 200 OK.

List Orders
Request
GET /v1/me/getchildorders
Query parameters

product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
count, before, after: See Pagination. If either before or after is specified, ACTIVE orders will not be included in the result.
child_order_state: When specified, return only orders that match the specified value. If not specified, returns a concatenated list of ACTIVE and non-ACTIVE orders.
You can specify one of the following:
ACTIVE: Return open orders
COMPLETED: Return fully completed orders
CANCELED: Return orders that have been cancelled by the customer
EXPIRED: Return order that have been cancelled due to expiry
REJECTED: Return failed orders
child_order_id, child_order_acceptance_id: ID for the child order.
parent_order_id: If specified, a list of all orders associated with the parent order is obtained.
Response
[
  {
    "id": 138398,
    "child_order_id": "JOR20150707-084555-022523",
    "product_code": "BTC_JPY",
    "side": "BUY",
    "child_order_type": "LIMIT",
    "price": 30000,
    "average_price": 30000,
    "size": 0.1,
    "child_order_state": "COMPLETED",
    "expire_date": "2015-07-14T07:25:52",
    "child_order_date": "2015-07-07T08:45:53",
    "child_order_acceptance_id": "JRF20150707-084552-031927",
    "outstanding_size": 0,
    "cancel_size": 0,
    "executed_size": 0.1,
    "total_commission": 0,
    "time_in_force": "GTC"
  },
  {
    "id": 138397,
    "child_order_id": "JOR20150707-084549-022519",
    "product_code": "BTC_JPY",
    "side": "SELL",
    "child_order_type": "LIMIT",
    "price": 30000,
    "average_price": 0,
    "size": 0.1,
    "child_order_state": "CANCELED",
    "expire_date": "2015-07-14T07:25:47",
    "child_order_date": "2015-07-07T08:45:47",
    "child_order_acceptance_id": "JRF20150707-084547-396699",
    "outstanding_size": 0,
    "cancel_size": 0.1,
    "executed_size": 0,
    "total_commission": 0,
    "time_in_force": "GTC"
  }
]
Any order that has never been executed, and which is then invalidated, due to a cancellation, etc. will not be included in the list of orders. Although you can set child_order_state to CANCELED, EXPIRED, or REJECTED, even then, orders that have never been executed will not be included in the results.

id: This is the paging ID. If child_order_state is unspecified or set to ACTIVE, currently the response id for all open orders is set to the fixed value of 0. (If before or after is specified, orders that have never been executed are not included in the results.)
child_order_id: This is unique ID of the order.
List Parent Orders
Request
GET /v1/me/getparentorders
Query parameters

product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
count, before, after: See Pagination.
parent_order_state: When specified, return only orders that match the specified value. You must specify one of the following:
ACTIVE: Return open orders
COMPLETED: Return fully completed orders
CANCELED: Return orders that have been cancelled by the customer
EXPIRED: Return order that have been cancelled due to expiry
REJECTED: Return failed orders
Response
[
  {
    "id": 138398,
    "parent_order_id": "JCO20150707-084555-022523",
    "product_code": "BTC_JPY",
    "side": "BUY",
    "parent_order_type": "STOP",
    "price": 30000,
    "average_price": 30000,
    "size": 0.1,
    "parent_order_state": "COMPLETED",
    "expire_date": "2015-07-14T07:25:52",
    "parent_order_date": "2015-07-07T08:45:53",
    "parent_order_acceptance_id": "JRF20150707-084552-031927",
    "outstanding_size": 0,
    "cancel_size": 0,
    "executed_size": 0.1,
    "total_commission": 0
  },
  {
    "id": 138397,
    "parent_order_id": "JCO20150707-084549-022519",
    "product_code": "BTC_JPY",
    "side": "SELL",
    "parent_order_type": "IFD",
    "price": 30000,
    "average_price": 0,
    "size": 0.1,
    "parent_order_state": "CANCELED",
    "expire_date": "2015-07-14T07:25:47",
    "parent_order_date": "2015-07-07T08:45:47",
    "parent_order_acceptance_id": "JRF20150707-084547-396699",
    "outstanding_size": 0,
    "cancel_size": 0.1,
    "executed_size": 0,
    "total_commission": 0
  }
]
price and size values for parent orders with multiple associated orders are both reference values only.

To obtain the detailed parameters for individual orders, use the API to obtain the details of the parent order. To obtain a list of associated orders, use the API to obtain the order list.

Get Parent Order Details
Request
GET /v1/me/getparentorder
Query parameters

Please specify either parent_order_id or parent_order_acceptance_id.

parent_order_id: The ID of the parent order in question.
parent_order_acceptance_id: The acceptance ID for the API to place a new parent order. If specified, it returns the details of the parent order in question.
Response
{
  "id": 4242,
  "parent_order_id": "JCO20150925-046876-036161",
  "order_method": "IFDOCO",
  "expire_date": 10000,
  "parameters": [{
    "product_code": "BTC_JPY",
    "condition_type": "LIMIT",
    "side": "BUY",
    "price": 30000,
    "size": 0.1,
    "trigger_price": 0,
    "offset": 0
  }, {
    "product_code": "BTC_JPY",
    "condition_type": "LIMIT",
    "side": "SELL",
    "price": 32000,
    "size": 0.1,
    "trigger_price": 0,
    "offset": 0
  }, {
    "product_code": "BTC_JPY",
    "condition_type": "STOP_LIMIT",
    "side": "SELL",
    "price": 28800,
    "size": 0.1,
    "trigger_price": 29000,
    "offset": 0
  }],
  "parent_order_acceptance_id": "JRF20150925-060559-396699"
}
List Executions
Request
GET /v1/me/getexecutions
Query parameters

product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
count, before, after: See Pagination.
child_order_id: Optional. When specified, a list of stipulations related to the order will be displayed.
child_order_acceptance_id: Optional. Expects an ID from Send a New Order. When specified, a list of stipulations related to the corresponding order will be displayed.
Response
[
  {
    "id": 37233,
    "child_order_id": "JOR20150707-060559-021935",
    "side": "BUY",
    "price": 33470,
    "size": 0.01,
    "commission": 0,
    "exec_date": "2015-07-07T09:57:40.397",
    "child_order_acceptance_id": "JRF20150707-060559-396699"
  },
  {
    "id": 37232,
    "child_order_id": "JOR20150707-060426-021925",
    "side": "BUY",
    "price": 33470,
    "size": 0.01,
    "commission": 0,
    "exec_date": "2015-07-07T09:57:40.397",
    "child_order_acceptance_id": "JRF20150707-060559-396699"
  }
]
List Balance History
Request
GET /v1/me/getbalancehistory
Query parameters

currency_code: Please specify a currency code. If omitted, the value is set to JPY.
count, before, after: See Pagination.
Response
[
  {
    "id": 1000108,
    "trade_date": "2016-10-19T14:44:55.28",
    "event_date": "2016-10-19T05:44:55.28",
    "product_code": "BTC_USD",
    "currency_code": "USD",
    "trade_type": "SELL",
    "price": 9999.99,
    "amount": 99.99,
    "quantity": 99.99,
    "commission": 0,
    "balance": 9999999.99,
    "order_id": "JORYYYYMMDD‌-000000-000001X"
  },
  {
    "id": 1000107,
    "trade_date": "2016-10-19T14:41:35.23",
    "event_date": "2016-10-19T05:41:35.23",
    "product_code": "BTC_USD",
    "currency_code": "USD",
    "trade_type": "SELL",
    "price": 9999.99,
    "amount": 999.99,
    "quantity": 99.99,
    "commission": 0,
    "balance": 9999999.99,
    "order_id": "JORYYYYMMDD‌-000000-000000X"
  }
]
event_date: The transaction date in UTC.
trade_date: The transaction date in JST (UTC+9).
trade_type: The type of the transaction.
BUY: Purchases
SELL: Sales
DEPOSIT: Deposits of fiat or virtual currency
WITHDRAW: Withdrawals of fiat or virtual currency
FEE: Fees
POST_COLL: Margin deposits made
CANCEL_COLL: Margin withdrawals made
PAYMENT: Virtual currency transfers by means of Bitcoin Payments
TRANSFER: Other general currency transfers
Get Open Interest Summary
Request
GET /v1/me/getpositions
Query parameters

product_code: Currently supports bitFlyer Crypto CFD.
Response
[
  {
    "product_code": "FX_BTC_JPY",
    "side": "BUY",
    "price": 36000,
    "size": 10,
    "commission": 0,
    "swap_point_accumulate": -35,
    "require_collateral": 120000,
    "open_date": "2015-11-03T10:04:45.011",
    "leverage": 3,
    "pnl": 965,
    "sfd": -0.5
  }
]
Get Margin Change History
Request
GET /v1/me/getcollateralhistory
Query parameters

count, before, after: See Pagination.
Response
[
  {
    "id": 4995,
    "currency_code": "JPY",
    "change": -6,
    "amount": -6,
    "reason_code": "CLEARING_COLL",
    "date": "2017-05-18T02:37:41.327"
  },
  {
    "id": 4994,
    "currency_code": "JPY",
    "change": 2083698,
    "amount": 0,
    "reason_code": "EXCHANGE_COLL",
    "date": "2017-04-28T03:05:07.493"
  },
  {
    "id": 4993,
    "currency_code": "BTC",
    "change": -14.69001618,
    "amount": 34.97163164,
    "reason_code": "EXCHANGE_COLL",
    "date": "2017-04-28T03:05:07.493"
  }
]
change: The amount of change to the margin deposit.
amount: The margin deposit balance after the change
Get Trading Commission
Request
GET /v1/me/gettradingcommission
Query parameters

product_code: Please specify a product_code, as obtained from the Market List. Please refer to the Regions to check available products in each region.
Response
{
  "commission_rate": 0.001
}





















Overview
Realtime API

bitFlyer supports 2 protocols for real-time updates.

Socket.IO 2.0 (WebSocket)
JSON-RPC 2.0 over WebSocket
The Realtime API is divided into Public Channels that do not require API key authentication and Private Channels that require authentication.

Important Technical Notes
You can receive information from the Realtime API from the time you start your subscription. The situations listed below may result in loss of connection. Information that was generated in the period prior to reconnection can not be received retroactively.

Maintenance, outages, etc. of our system
Maintenance, communication or route failure, etc. by your network equipment or network provider
Please fully understand the following characteristics of the WebSocket protocol when using the Realtime API :

Messages will be delivered one by one and the order of message delivery is guaranteed for a given connection.
While a message with a large data size is being delivered, subsequent messages may be delayed depending on the line speed etc. (we recommend not subscribing to unnecessary channels)
If delay or packet loss occurs due to factors such as line quality, subsequent messages will also be delayed, and eventually ping responses will time out and the connection will be lost.





Socket.IO 2.0 (WebSocket)
Realtime API

📘
For more detailed information on Socket.IO please refer to the Socket.IO official site.

Endpoint

https://io.lightstream.bitflyer.com
🚧
* websocket Only websocket requests are supported by this endpoint. Many clients must state this explicity.
A TLS 1.2 compliant client, and in some cases explicit configuration, is required in order to connect.
Methods
auth - Make an authentication request
io.Socket#emit("auth", { /* (Auth Params) */ }, callbackFn)
(Auth Params) Please reference the Authentication page for more information.
callbackFn A callback method executed after the authentiction request. The first argument to the callback contains information on any errors that occured during the authentication process
subscribe - Subscribe to a channel
io.Socket#emit("subscribe", "(Channel Name)"[, callbackFn])
unsubscribe - Unsubscribe from a channel
io.Socket#emit("unsubscribe", "(Channel Name)"[, callbackFn])
Events
(Channel Name) - The message will be delivered to the subscribed channel
Usage Example
JavaScript
Java

// Node.js (JavaScript)
const crypto = require("crypto");
const io = require("socket.io-client");

const key = "{{ YOUR API KEY }}";
const secret = "{{ YOUR API SECRET }}";

const publicChannels = ["lightning_executions_BTC_JPY"];
const privateChannels = ["child_order_events", "parent_order_events"];

const socket = io("https://io.lightstream.bitflyer.com", {
    transports: ["websocket"] // specify explicitly
});

// connection handling
socket.on("connect", () => {
    // subscribe to the Public Channels
    for (const ch of publicChannels) {
        socket.emit("subscribe", ch, err => {
            if (err) {
                console.error(ch, "Subscribe Error:", err);
                return;
            }
            console.log(ch, "Subscribed.");
        });
    }

    // authentication parameters
    const now = Date.now();
    const nonce = crypto.randomBytes(16).toString("hex");
    const sign = crypto.createHmac("sha256", secret).update(`${now}${nonce}`).digest("hex");

    // request auth



JSON-RPC 2.0 over WebSocket
Realtime API

📘
The transmission contents of this connection protocol conform to the JSON-RPC 2.0 Specification.

Endpoint

wss://ws.lightstream.bitflyer.com/json-rpc
🚧
Supports batch requests as defined in JSON-RPC 2.0. Requests are processed in order, starting from the beginning of the array.
A TLS 1.2 compliant client, and in some cases explicit configuration, is required in order to connect.
Server Methods
auth - Make an authentication request
params: Please refer to the Authentication page for details
Returns true if authentication is successful (please confirm)
subscribe - Subscribe to a channel
params: { channel: "(Channel Name)" }
Returns true if the subscription starts.
unsubscribe - Unsubscribe from a channel
params: { channel: "(Channel Name)" }
Returns true if the subscription ends.
Client Methods
channelMessage - The message will be delivered to the subscribed channel
Usage Example
JavaScript
C#
Ruby

// Node.js (JavaScript)
const crypto = require("crypto");
const RPCClient = require("jsonrpc2-ws").Client;

const key = "{{ YOUR API KEY }}";
const secret = "{{ YOUR API SECRET }}";

const publicChannels = ["lightning_executions_BTC_JPY"];
const privateChannels = ["child_order_events", "parent_order_events"];

const client = new RPCClient("wss://ws.lightstream.bitflyer.com/json-rpc", { protocols: undefined });

// connection handling
client.on("connected", async () => {
    // subscribe to the Public Channels
    for (const channel of publicChannels) {
        try {
            await client.call("subscribe", { channel });
        } catch (e) {
            console.log(channel, "Subscribe Error:", e);
            continue;
        }
        console.log(channel, "Subscribed.");
    }

    // authentication parameters
    const now = Date.now();
    const nonce = crypto.randomBytes(16).toString("hex");
    const sign = crypto.createHmac("sha256", secret).update(`${now}${nonce}`).digest("hex");

    // request auth


https://www.jsonrpc.org/specification


API Limits
Realtime API

The Realtime API does not have a uniform limit, but we may restrict or prohibit connections by IP address or account in the following situations:

If a large number of API errors occur repeatedly over an extended period of time
If you connect and disconnect repeatedly and with high frequency even though a connection was correctly established
If we determine that you are repeatedly burdening the system or acting improperly
📘
With the Realtime API it is possible to subscribe to multiple channels over a single TCP connection. Once you have established a connection you do not have to disconnect each time you receive data. Data will continue to be delivered until you disconnect.



Order Book
Realtime Public Channel

Channel Name

lightning_board_snapshot_{product_code}
{product_code} can be obtained from the market list. It cannot be an alias.

BTC/JPY (Spot): lightning_board_snapshot_BTC_JPY
bitFlyer Crypto CFD: lightning_board_snapshot_FX_BTC_JPY
ETH/BTC: lightning_board_snapshot_ETH_BTC
Message Content
Sends out a snapshot of the order book.

Message frequency is limited for rational reasons such as delivery efficiency.
Please use Order Book Updates to retrieve information every time there is an update.
The order of the asks and bids arrays is not guaranteed, so sort as necessary.
JSON

{
  "mid_price": 33320,
  "bids": [
    {
      "price": 30000,
      "size": 0.1
    },
    {
      "price": 25570,
      "size": 3
    }
  ],
  "asks": [
    {
      "price": 36640,
      "size": 5
    },
    {
      "price": 36700,
      "size": 1.2
    }
  ]
}



Order Book Updates
Realtime Public Channel

Channel Name

lightning_board_{product_code}
{product_code} can be obtained from the market list. It cannot be an alias.

BTC/JPY (Spot): lightning_board_BTC_JPY
bitFlyer Crypto CFD: lightning_board_FX_BTC_JPY
ETH/BTC: lightning_board_ETH_BTC
Message Content
Whenever the order book is updated the difference is sent out.

size is the total amount of the order given the price.
When the order for the given price disappears from the order book due to execution or expiration, it will be returned as size: 0.
When the market order is executed during an Itayose, it will return a difference of price: 0.
JSON

{
  "mid_price": 35625,
  "bids": [
    {
      "price": 33350,
      "size": 1
    }
  ],
  "asks": []
}





Ticker
Realtime Public Channel

Channel Name

lightning_ticker_{product_code}
{product_code} can be obtained from the market list. It cannot be an alias.

BTC/JPY (Spot): lightning_ticker_BTC_JPY
bitFlyer Crypto CFD: lightning_ticker_FX_BTC_JPY
ETH/BTC: lightning_ticker_ETH_BTC
Message Content
Sent out when there is an update to the Ticker.

Message frequency is limited for rational reasons such as delivery efficiency.
To get the latest final transaction price as accurately as possible, please use the Executions channel.
JSON

{
  "product_code": "BTC_JPY",
  "timestamp": "2019-04-11T05:14:12.3739915Z",
  "state": "RUNNING",
  "tick_id": 25965446,
  "best_bid": 580006,
  "best_ask": 580771,
  "best_bid_size": 2.00000013,
  "best_ask_size": 0.4,
  "total_bid_depth": 1581.64414981,
  "total_ask_depth": 1415.32079982,
  "market_bid_size": 0,
  "market_ask_size": 0,
  "ltp": 580790,
  "volume": 6703.96837634,
  "volume_by_product": 6703.96837634
}
timestamp: Time in ISO format
ltp: Last trade price
volume: 24-hour trade volume



Executions
Realtime Public Channel

Channel Name

lightning_executions_{product_code}
{product_code} can be obtained from the market list. It cannot be an alias.

BTC/JPY (Spot): lightning_executions_BTC_JPY
bitFlyer Crypto CFD: lightning_executions_FX_BTC_JPY
ETH/BTC: lightning_executions_ETH_BTC
Message Content
Sent out each time there is an execution.

JSON

[
  {
    "id": 39361,
    "side": "SELL",
    "price": 35100,
    "size": 0.01,
    "exec_date": "2015-07-07T10:44:33.547Z",
    "buy_child_order_acceptance_id": "JRF20150707-014356-184990",
    "sell_child_order_acceptance_id": "JRF20150707-104433-186048"
  }
]
side: Trading type of the order (taker) that executed this fill. If it is executed during an Itayose, it will be an empty string.

