Firi Trading API (1.0.0)
Support: support@firi.com
This is the Trading API that enables our Market Makers.

Authorization
Some endpoints are public and do not require any form for authentication and authorization, and some are private which means that they require authentication and authorization. The private endpoints require an access key (See section about authentication for more information about access keys). The user can define the security levels of their access key(s)

Errors and problems
Error messages: Access control (Authorization/Authentication)
Error	Error description
ApiKeyNotFound	The request contains an access key that was not found in our systems
Expired Signature	The request contains an expired hmac encrypted secretKey. Make sure the timestamp was not made in the past and that the validity is sufficient
Invalid Signature	The hmac encrypted secretKey did not match with our hmac encryption of APIkey. PS! Timestamp and validity has to be strings
SecurityLevelTooLow	Try changing the security level of your access key, to the required security level.
Time
Provides current time as epoch. Recommended to use for the timestamp required for HMAC encryption of your secretKey

Get current timestamp in epoch
Responses
200 Successful Operation

get
/time
Response samples
200
Content type
application/json

Copy
{
"time": 0
}
History
Get history over all transactions
Direction is either end or start

Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
query Parameters
direction	
string
count	
integer <int32>
Responses
200 Successful Operation

get
/v2/history/transactions
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": "string",
"amount": "string",
"currency": "string",
"type": "string",
"date": "string",
"details": {}
}
]
Get history over transactions by year
Direction is either end or start.

year > 2017

Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
path Parameters
year
required
string
query Parameters
direction	
string
Responses
200 Successful Operation

get
/v2/history/transactions/{year}
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": "string",
"amount": "string",
"currency": "string",
"type": "string",
"date": "string",
"details": {}
}
]
Get history over transactions by month and year
Direction is either end or start.

12 >= month >= 1

year > 2017

Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
path Parameters
month
required
string
year
required
string
query Parameters
direction	
string
Responses
200 Successful Operation

get
/v2/history/transactions/{month}/{year}
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": "string",
"amount": "string",
"currency": "string",
"type": "string",
"date": "string",
"details": {}
}
]
Get history over all orders
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
query Parameters
type	
string
count	
integer <int32>
Responses
200 Successful Operation

get
/v2/history/orders
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": "string",
"market": "string",
"price": "string",
"price_currency": "string",
"amount": "string",
"amount_currency": "string",
"cost": "string",
"cost_currency": "string",
"side": "string",
"isMaker": true,
"date": "string"
}
]
Get history over orders defined by market
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
path Parameters
market
required
string
query Parameters
type	
string
count	
integer <int32>
Responses
200 Successful Operation

get
/v2/history/orders/{market}
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": "string",
"market": "string",
"price": "string",
"price_currency": "string",
"amount": "string",
"amount_currency": "string",
"cost": "string",
"cost_currency": "string",
"side": "string",
"isMaker": true,
"date": "string"
}
]
Market
Get history over a specific market
path Parameters
market
required
string
query Parameters
count	
integer <int32>
Responses
200 Successful Operation

get
/v1/markets/{market}/history
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"type": "string",
"amount": "string",
"price": "string",
"created_at": "string",
"total": "string"
}
]
Get history over a specific market
path Parameters
market
required
string
query Parameters
count	
integer <int32>
Responses
200 Successful Operation

get
/v2/markets/{market}/history
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"type": "string",
"amount": "string",
"price": "string",
"created_at": "string",
"total": "string"
}
]
Get orderbooks for a market
path Parameters
market
required
string
query Parameters
bids	
integer <int32>
asks	
integer <int32>
Responses
200 Successful Operation

get
/v2/markets/{market}/depth
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"bids": [
[]
],
"asks": [
[]
]
}
Get orderbooks for a market
path Parameters
market
required
string
query Parameters
bids	
integer <int32>
asks	
integer <int32>
Responses
200 Successful Operation

get
/v1/markets/{market}/depth
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"bids": [
[]
],
"asks": [
[]
]
}
Get info about specific market
path Parameters
market
required
string
Responses
200 Successful Operation

get
/v2/markets/{market}
Response samples
200
Content type
application/json

Copy
{
"id": "string",
"last": "string",
"high": "string",
"change": "string",
"low": "string",
"volume": "string"
}
Get info about specific market
path Parameters
market
required
string
Responses
200 Successful Operation

get
/v1/markets/{market}
Response samples
200
Content type
application/json

Copy
{
"id": "string",
"last": "string",
"high": "string",
"change": "string",
"low": "string",
"volume": "string"
}
Get available markets
Responses
200 Successful Operation

get
/v2/markets
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": "string",
"last": "string",
"high": "string",
"change": "string",
"low": "string",
"volume": "string"
}
]
Get available markets
Responses
200 Successful Operation

get
/v1/markets
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": "string",
"last": "string",
"high": "string",
"change": "string",
"low": "string",
"volume": "string"
}
]
Get ticker for specific market
path Parameters
market
required
string
Responses
200 Successful Operation

get
/v2/markets/{market}/ticker
Response samples
200
Content type
application/json

Copy
{
"bid": "string",
"ask": "string",
"spread": "string"
}
Get available tickers
Responses
200 Successful Operation

get
/v2/markets/tickers
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"market": "string",
"bid": "string",
"ask": "string",
"spread": "string"
}
]
Coin
Get information about the several different currencies we offer

Get a user's pending XRP withdraws
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/XRP/withdraw/pending
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"count": 0,
"pending": [
{}
]
}
Get a user's XRP address
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/XRP/address
Response samples
200
Content type
application/json

Copy
{
"address": "17SZQ346HUxfGamd6R2aBWBjlrsHP2B7i7"
}
Get a user's pending LTC withdraws
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/LTC/withdraw/pending
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"count": 0,
"pending": [
{}
]
}
Get a user's LTC address
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/LTC/address
Response samples
200
Content type
application/json

Copy
{
"address": "17SZQ346HUxfGamd6R2aBWBjlrsHP2B7i7"
}
Get a user's pending ETH withdraws
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/ETH/withdraw/pending
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"count": 0,
"pending": [
{}
]
}
Get a user's ETH address
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/ETH/address
Response samples
200
Content type
application/json

Copy
{
"address": "17SZQ346HUxfGamd6R2aBWBjlrsHP2B7i7"
}
Get a user's pending DAI withdraws
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/DAI/withdraw/pending
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"count": 0,
"pending": [
{}
]
}
Get a user's DAI address
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/DAI/address
Response samples
200
Content type
application/json

Copy
{
"address": "17SZQ346HUxfGamd6R2aBWBjlrsHP2B7i7"
}
Get a user's pending BTC withdraws
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/BTC/withdraw/pending
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"count": 0,
"pending": [
{}
]
}
Get address for BTC Wallet
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/BTC/address
Response samples
200
Content type
application/json

Copy
{
"address": "17SZQ346HUxfGamd6R2aBWBjlrsHP2B7i7"
}
Get a user's pending ADA withdraws
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/ADA/withdraw/pending
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"count": 0,
"pending": [
{}
]
}
Get address for ADA Wallet
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/ADA/address
Response samples
200
Content type
application/json

Copy
{
"address": "17SZQ346HUxfGamd6R2aBWBjlrsHP2B7i7"
}
Deposit
Provides a user's deposit address and deposit history

Get a user's history over deposits
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
query Parameters
count	
integer <int32>
before	
integer <int32>
Responses
200 Successful Operation

get
/v2/deposit/history
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"count": 0,
"transactions": [
{}
]
}
Get a user's deposit address
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/deposit/address
Response samples
200
Content type
application/json

Copy
{
"btc_address": "string",
"ltc_address": "string",
"eth_address": "string"
}
Order
Provides information about the a user's orders

Get orders
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v2/orders
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": 0,
"market": "string",
"type": "string",
"price": "string",
"amount": "string",
"remaining": "string",
"matched": "string",
"cancelled": "string",
"created_at": "string"
}
]
Create your order
Only "bid" and "ask" is supported as type at this time. Markets can be retrieved by the market operations. If you have trouble using HMAC authentication with this endpoint, see section 'POST requests and HMAC authentication'

Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Request Body schema: application/json
market
required
string
type
required
string
price
required
string
amount
required
string
Responses
201 Successful Operation

post
/v2/orders
Request samples
Payload
Content type
application/json

Copy
{
"market": "string",
"type": "string",
"price": "string",
"amount": "string"
}
Response samples
201
Content type
application/json

Copy
{
"id": 0
}
Delete your orders
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
204 Successful Operation

delete
/v2/orders
Get all active orders for a specific market
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
path Parameters
market
required
string
query Parameters
count	
integer <int32>
Responses
201 Successful Operation

get
/v2/orders/{market}
Response samples
201
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": 0,
"market": "string",
"type": "string",
"price": "string",
"amount": "string",
"remaining": "string",
"matched": "string",
"cancelled": "string",
"created_at": "string"
}
]
Get all filled and closed orders for a specific market
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
path Parameters
market
required
string
query Parameters
count	
integer <int32>
Responses
200 Successful Operation

get
/v2/orders/{market}/history
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": 0,
"market": "string",
"type": "string",
"price": "string",
"amount": "string",
"remaining": "string",
"matched": "string",
"cancelled": "string",
"created_at": "string"
}
]
Get all filled and closed orders
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
query Parameters
count	
integer <int32>
Responses
200 Successful Operation

get
/v2/orders/history
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": 0,
"market": "string",
"type": "string",
"price": "string",
"amount": "string",
"remaining": "string",
"matched": "string",
"cancelled": "string",
"created_at": "string"
}
]
Get order by orderId
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
path Parameters
orderID
required
integer <int64>
Responses
200 Successful Operation

get
/v2/order/{orderID}
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": 0,
"market": "string",
"type": "string",
"price": "string",
"amount": "string",
"remaining": "string",
"matched": "string",
"cancelled": "string",
"created_at": "string"
}
]
Delete your order by market and orderID, returns matched amount in cancelled order
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
path Parameters
orderID
required
integer <int64>
market
required
string
Responses
200 Successful Operation

delete
/v2/orders/{orderID}/{market}/detailed
Response samples
200
Content type
application/json

Copy
{
"matched": "string"
}
Delete your order by orderID, returns matched amount in cancelled order
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
path Parameters
orderID
required
integer <int64>
Responses
200 Successful Operation

delete
/v2/orders/{orderID}/detailed
Response samples
200
Content type
application/json

Copy
{
"matched": "string"
}
Delete your orders by market
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
path Parameters
marketOrMarketID
required
string
Responses
204 Successful Operation

delete
/v2/orders/{marketOrMarketID}
Balance
Check the balance for your wallets

Get balances of your wallets
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation

get
/v1/balances
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"currency": "string",
"balance": "string",
"hold": "string",
"available": "string"
}
]
Get balances of your wallets
Authorizations:
(HMAC_encrypted_secretKeyvaliditytimestampclientID) API-key
Responses
200 Successful Operation







