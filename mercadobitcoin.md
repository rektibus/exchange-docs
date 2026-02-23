Mercado Bitcoin API (v5.36.1)
Download OpenAPI specification:Download

API Support: contato@mercadobitcoin.com.br
URL: https://suporte.mercadobitcoin.com.br
Overview
Before using Mercado Bitcoin's APIs, please consult here the provisions of the APIs Terms of Service.

Endpoint
All requests is made with /api/v4 context (except /oauth2/token).

WebSocket API
If you are looking for WebSocket API documentation click here

Rate Limit
The default rate limit total: 500 requests/min.

Considering both private and public information. Each endpoint has its own rate limit, as described in the endpoints section. If you need to increase this number, please contact us via trade.support@mercadobitcoin.com.br.

Errors
Domain error examples
Our errors will have a pattern on every invalid request return

In them you will identify a mapping of information that will tell you the location of the error and the specific error, as well as a description to better describe the error.

DOMAIN = Error domain

e.g: TRADING(Trading services)

MODULE = Use case that is running

e.g: GET_ORDER(search endpoint of order by id)

ERROR = Specific error caused on request

e.g: ORDER_NOT_FOUND(id used for search does not exist in our base)

Response status code: 400

Response body payload

{
"code": "TRADING|GET_ORDER|ORDER_NOT_FOUND",
"message": "This order_id not found"
}
Possible errors return
Error	Description
API_UNAVAILABLE	API temporarily disabled
FORBIDDEN	Invalid login or password
INVALID_SYMBOL	{symbol} param does not exist or it's not on the BASE-QUOTE format, ex: BTC-BRL
INVALID_PARAMETER	Invalid parameter value
INSUFFICIENT_BALANCE	Insufficient balance to carry out the operation
ORDER_NOT_FOUND	This order_id not found
ADDRESS_NOT_REGISTERED	Address not registered or marked as trusted
PROBLEM_TRANSFERRING	Problem transferring digital currency
INVALID_ACCESS	Attempting to access a persistence method with a read-only key
ORDER_PROCESSED	This order have already been processed or canceled
INVALID_BANK_ACCOUNT	Bank account not registered or not marked as trusted
INVALID_WITHDRAWAL_VALUE	Withdrawal to savings account must be less than BRL 5000.00
WITHDRAWAL_AMOUNT_LIMIT	This amount exceeds the withdrawal limit of Reais for the last 24 hours
WITHDRAWAL_DIGITAL_AMOUNT_LIMIT	This amount exceeds the digital currency withdrawal limit for the last 24 hours
MINIMUM_WITHDRAWAL_AMOUNT	Minimum amount for withdrawals in Reais is R$ 50,00
MINIMUM_BITCOIN_TRANSFERS	Minimum value of Bitcoin transfers to external address is 0.001 BTC
MINIMUM_LITECOIN_TRANSFERS	Minimum value of Litecoin transfers to external address is 0.009 LTC
MIN_MAX_BITCOIN_EXCEEDED	Minimum or maximum amount of Bitcoin exceeded
MIN_MAX_LITECOIN_EXCEEDED	Minimum or maximum amount of Litecoin exceeded
MIN_MAX_BRL_EXCEEDED	Minimum unit price (BRL 0.01) or maximum exceeded
DUPLICATE_STATUS	Duplicate status
INVALID_STATUS_VALUE	Status value is invalid
INVALID_DECIMAL_PLACES	Invalid number of decimal places entered
PARAMETER_SIZE_LARGE	Parameter size larger than allowed
INVALID_TRANSFER_ID	Invalid transfer. The ID entered does not exist in your account.
MINIMUM_BCASH_TRANSFERS	Minimum value of transfers from BCash to external address is 0.001 BCH
MIN_MAX_BCASH_EXCEEDED	Minimum or maximum amount of BCash exceeded
MINIMUM_XRP_TRANSFERS	Minimum transfer value from XRP (Ripple) to external address is 10 XRP
MIN_MAX_XRP_EXCEEDED	Minimum or maximum amount of XRP exceeded
MINIMUM_ETHEREUM_TRANSFERS	Minimum transfer value from Ethereum to external address is 0.004 ETH
MIN_MAX_ETHEREUM_EXCEEDED	Minimum or maximum amount of Ethereum exceeded
INVALID_ADDRESS	Invalid address for transfer
REQUEST_RATE_EXCEEDED	Request rate exceeded the request limit in the range
REQUEST_DENIED	Request denied: high request rate or invalid request
REQUEST_BLOCKED	Requests temporarily blocked
ORDER_IN_PROCESSING	Your order is being processed, if there is any problem your balance will be reversed
ERROR_MONITOR_PRICE	Occurred unexpected error from monitor price
BALANCE_RESERVED_NOT_CANCELED	Balance reserved not canceled
ERROR_RESERVE_BALANCE	Occurred unexpected error from balance reserve
ERROR_LEGACY_PLACE_ORDER	Occurred unexpected error to create order
ERROR_PUBLISH_ORDER	Occurred unexpected error to publish order
INVALID_LIMIT_PRICE	Price Limit value must be less than the Stop Limit value
ORDER_DUPLICATE	There is already an order created
BALANCE_NOT_RESERVED	Balance not reserved
INVALID_MAX_LIMIT_PRICE	Limit price is higher than max value
INVALID_MIN_LIMIT_PRICE	Limit price is lower than min value
INVALID_MAX_QUANTITY	Quantity (volume) is higher than max value
INVALID_MIN_QUANTITY	Quantity (volume) is lower than min value
INVALID_PAIR	Base or Quote is invalid
INVALID_SIDE	Side must be sell on stoplimit orders
INVALID_STOP_PRICE	The param limitPrice cannot be higher than stopPrice
MISSING_FIELD	Param stopPrice cannot be empty in stoplimit orders
ASSET_NETWORKS_NOT_FOUND	The asset couldn't exist or there is no network active
INVALID_SYMBOL_NETWORK	Invalid symbol or invalid network
DEPOSIT_UNAVAILABLE	Deposit unavailable or disable for the symbol
Unauthorized error example
Response status code: 401

Response body payload

{
"error": {
"code": 401,
"status": "Unauthorized",
"reason": "Access token is not active",
"message": "Access credentials are invalid"
}
}
Forbidden error example
Response status code: 403

Response body payload

{
"error": {
"code": 403,
"status": "Forbidden",
"message": "Access credentials are not sufficient to access this resource"
}
}
Internal server error example
Response status code: 500

Response body payload

{
"code": "API|INTERNAL_SERVER_ERROR",
"message": "An unexpected error has occurred"
}
Authentication
Client Credential
This is a Oauth2 client_credential flow.

It uses client id and secret to authenticate a user. These data are sent as parameters to the /oauth2/token endpoint.

The client_id refers to API key id and client_secret to API key secret.

You must generate an API key id and secret on MercadoBitcoin platform. Follow this link: Generate API token and secret

If the id and secret are valid, then the server issues an access token (access_token) and returns it in the response. The access token needs to be sent on every request in the Authorization header.

Bearer
Enter the token with the Bearer: prefix, e.g. "Bearer abcde12345".

Security Scheme Type	API Key
Header parameter name:	Authorization
Public Data
Get Fees From Asset

get
/{asset}/fees
Request for asset's withdraw fee (network fee charge)

Rate Limit: 1 requests/sec
path Parameters
asset
required
string
Instrument asset in the form BASE(e.g. USDC)

query Parameters
network	
string
Asset network. If not informed uses default network of the asset

Responses
200 Response
Response Schema: application/json
asset	
string
Selected instrument asset (equal to the requested one)

network	
string
Network of withdrawal

deposit_minimum	
string
Minimum asset quantity for deposit

deposit_confirmations_required	
string
Network confirmations required for confirm deposit

withdraw_minimum	
string
Minimum asset quantity for withdrawal

withdrawal_fee	
string
Fee value to cover the transaction costs (matching value with the field "tx_fee" of the POST/withdrawCoin endpoint)

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"asset": "USDC",
"network": "stellar",
"deposit_minimum": "0.004",
"deposit_confirmations_required": "3",
"withdraw_minimum": "0.001",
"withdrawal_fee": "0.01"
}
Get OrderBook

get
/{symbol}/orderbook
Get current orderbook (depth of market) for the instrument.

Rate Limit: 1 requests/sec
path Parameters
symbol
required
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)

query Parameters
limit	
string
Limit of orderbook response data per side (asks, bids). Max allowed 1000

Responses
200 Response
Response Schema: application/json
asks	
Array of strings
Array of Array of numbers (OrderbookItem) Array of arrays with two string elements - price and volume. It is sorted by price in asc order.

bids	
Array of strings
Array of Array of numbers (OrderbookItem) Array of arrays with two string elements - price and volume. It is sorted by price in asc order.

timestamp	
number
Timestamp when the orderbook was generated

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"asks": [
"1.0001",
"1.0001"
],
"bids": [
"1.0001",
"1.0001"
],
"timestamp": 0
}
List Trades

get
/{symbol}/trades
List trades (executions).

Rate Limit: 1 requests/sec
path Parameters
symbol
required
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)

query Parameters
tid	
integer
Trade id to find

since	
integer
Since trade id to find

from	
integer
Unix timestamp (UTC) of the leftmost required bar. {to} is required

to	
integer
Unix timestamp (UTC) of the rightmost required bar. {from} is required

limit	
integer
Limit of results. Max 1000

Responses
200 Response
Response Schema: application/json
Array ()
amount	
string
Amount of crypt transacted

date	
integer
Trade creation date

price	
string
Price of trade

tid	
integer
Trade id

type	
string
Type of trade(buy or sell)

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"amount": "1",
"date": 1629989121,
"price": "15000",
"tid": 2,
"type": "sell"
}
]
List Candles

get
/candles
Request for history bars (candles).

Rate Limit: 1 requests/sec
query Parameters
symbol
required
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)

resolution
required
string
1m, 15m, 1h, 3h, 1d, 1w, 1M(for months)

to
required
integer
Unix timestamp (UTC) of the rightmost required bar, including to. It can be in the future. In this case, the rightmost required bar is the latest available bar.

from	
integer
Unix timestamp (UTC) of the leftmost required bar

countback	
integer
Number of bars (higher priority than from) starting with to. If countback is set, from will be ignored.

Responses
200 Response
Response Schema: application/json
c	
Array of strings
Closing price (last trade) in the bucket interval

h	
Array of strings
Highest price during the bucket interval

l	
Array of strings
Lowest price during the bucket interval

o	
Array of strings
Opening price (first trade) in the bucket interval

t	
Array of integers
Bucket start time (UTC)

v	
Array of strings
Volume of trading activity during the bucket interval

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"c": [
"500.00000000",
"1000.00000000"
],
"h": [
"1000.00000000",
"1000.00000000"
],
"l": [
"500.00000000",
"300.00000000"
],
"o": [
"1000.00000000",
"300.00000000"
],
"t": [
1652119200,
1652187600
],
"v": [
"4.00000000",
"2.00000000"
]
}
List Symbols

get
/symbols
Get a list of all instruments.

Rate Limit: 1 requests/sec
query Parameters
symbols	
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL,LTC-BRL)

Responses
200 Response
Response Schema: application/json
base-currency	
Array of strings
Base of symbol

currency	
Array of strings
Quote of symbol

deposit-minimum	
Array of strings
Minimum value for deposit

description	
Array of strings
Description of a symbol. Will be displayed in the chart legend for this symbol.

exchange-listed	
Array of booleans
If is exchange listed

exchange-traded	
Array of booleans
This symbol is able to trade

minmovement	
Array of strings
Minimum price difference between two consecutive orders on the orderbook

pricescale	
Array of numbers
Number of decimal digits allowed for the symbol price. It's presented in the form of a scale. Example: 1000 means 3 decimal digits

session-regular	
Array of strings
Session that you can trade this symbol

symbol	
Array of strings
This is the name of the symbol. (Base - Quote)

timezone	
Array of strings
Timezone where symbol is trading

type	
Array of strings
Type of symbol

Enum: CRYPTO FAN_TOKEN DIGITAL_ASSET UTILITY_TOKEN DEFI

withdraw-minimum	
Array of strings
Minimum value for withdrawal

withdrawal-fee	
Array of strings
Withdrawal fee in mercado bitcoin

min-price	
Array of strings
Minimum price to place order

max-price	
Array of strings
Maximum price to place order

min-volume	
Array of strings
Minimum volume to place order

max-volume	
Array of strings
Maximum volume to place order

min-cost	
Array of strings
Minimum cost to place order

max-cost	
Array of strings
Maximum cost to place order

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"base-currency": [
"BTC"
],
"currency": [
"BRL"
],
"deposit-minimum": [
"0.00001"
],
"description": [
"Bitcoin"
],
"exchange-listed": [
true
],
"exchange-traded": [
true
],
"minmovement": [
"0.00000001"
],
"pricescale": [
100000000
],
"session-regular": [
"24x7"
],
"symbol": [
"BTC-BRL"
],
"timezone": [
"America/Sao_Paulo"
],
"type": [
"CRYPTO"
],
"withdraw-minimum": [
"0.0003"
],
"withdrawal-fee": [
"0.0002"
],
"min-price": [
"230000.00000000"
],
"max-price": [
"1571759.96784993"
],
"min-volume": [
"0.00000150"
],
"max-volume": [
"8.46076128"
],
"min-cost": [
"0.90000000"
],
"max-cost": [
"1000000.00000000"
]
}
List Tickers

get
/tickers
Get current prices of the instrument.

Rate Limit: 1 requests/sec
query Parameters
symbols
required
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL,LTC-BRL)

Responses
200 Response
Response Schema: application/json
Array ()
buy	
string
The last buy price.

date	
integer
Last update date in nanoseconds.

high	
string
The highest price

last	
string
The last price.

low	
string
The lowest price.

open	
string
The first price.

pair	
string
Pair name. It is equal to the requested one.

sell	
string
The last sell price.

vol	
string
The total volume.

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"buy": "160.00000005",
"date": 1636107279,
"high": "145.00000001",
"last": "144.07000004",
"low": "143.00000002",
"open": "143.00000007",
"pair": "BTC-BRL",
"sell": "145.00000006",
"vol": "84.00100003"
}
]
List Networks From Asset

get
/{asset}/networks
Retrieves the networks associated with a specific asset (networks available for withdrawal).Please note that assets in pre-listing or delisted status do not provide network information.

Rate Limit: 1 requests/sec
path Parameters
asset
required
string
Instrument asset in the form BASE(e.g. BTC)

Responses
200 Response
Response Schema: application/json
Array ()
coin	
string
Cryptocurrency ex BTC, XLM, ETH.

network	
string
Network of withdrawal

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"coin": "XLM",
"network": "stellar"
}
]
Account
List Accounts

get
/accounts
Get a list of accounts owned by the user. Usually, MercadoBitcoin works with only one default account.

Authorizations:
Bearer
Responses
200 Response
Response Schema: application/json
Array ()
currency	
string
Currency of the account.

currencySign	
string
CurrencySign of the account.

id	
string
Account identifier (accountId)

name	
string
Name of the account.

type	
string
Account type.

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"currency": "BRL",
"currencySign": "R$",
"id": "a322205ace882ef800553118e5000066",
"name": "Mercado Bitcoin",
"type": "live"
}
]
Internal Transfer

post
/accounts/{accountId}/{symbol}/transfers/internal
Transfer balance between accounts.

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

symbol
required
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)

Request Body schema: application/json
Request

amount	
string
recipient_account_id	
string
transaction_id	
string
Responses
200 Response
Response Schema: application/json
transfer_id	
string
Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"amount": "string",
"recipient_account_id": "string",
"transaction_id": "string"
}
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"transfer_id": "string"
}
List Balances

get
/accounts/{accountId}/balances
Get balances for all markets, including fiat, for an account

Rate Limit: 3 requests/sec
Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

Responses
200 Response
Response Schema: application/json
Array ()
available	
string
Available amount

on_hold	
string
On hold balance related to open orders

symbol	
string
Symbol.

total	
string
Total balance (available + on_hold)

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"available": "1000.00000050",
"on_hold": "300.00000300",
"symbol": "BRL",
"total": "1300.00000350"
}
]
Get Tier

get
/accounts/{accountId}/tier
Get tier tax

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

Responses
200 Response
Response Schema: application/json
Array ()
tier	
string
It's the tax tier of account.

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"tier": "13"
}
]
Get Trading Fees

get
/accounts/{accountId}/{symbol}/fees
Get your trading fees for each symbol

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

symbol
required
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)
Example:symbol=BTC-BRL

Responses
200 Response
Response Schema: application/json
base	
string
Base of the market

quote	
string
Quote of the market

maker_fee	
string
Your maker fee of the market

taker_fee	
string
Your taker fee of the market

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"base": "BTC",
"quote": "BRL",
"maker_fee": "0.00300000",
"taker_fee": "0.00700000"
}
List Positions

get
/accounts/{accountId}/positions
Get open positions (open orders) for an account.

Rate Limit: 1 requests/sec
Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

query Parameters
symbols	
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL,LTC-BRL)

Responses
200 Response
Response Schema: application/json
Array ()
avgPrice	
number
Simple average price of position trades.

category	
string
Type of orders

Type	Description
limit	limit order
post-only	post only order
stoplimit	stoplimit order
id	
string
Unique order identifier (orderId)

instrument	
string
Instrument symbol in the form BASE-QUOTE (e.g. "BTC-BRL").

qty	
string
Order quantity (volume)

side	
string
Side of orders

Side	Description
buy	purchase order
sell	sales order
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"avgPrice": 380,
"category": "limit",
"id": "27",
"instrument": "BTC-BRL",
"qty": "0.001",
"side": "buy"
}
]
Wallet
Create Account

post
/accounts
Create new account to trade with.

Authorizations:
Bearer
Request Body schema: application/json
Request

name	
string
It's the name of account. Should have at least 3 characters.

Responses
200 Response
Response Schema: application/json
account_id	
string
name	
string
Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"name": "string"
}
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"account_id": "string",
"name": "string"
}
List Deposits

get
/accounts/{accountId}/wallet/{symbol}/deposits
List the deposits made by a user for a symbol. Fiat deposits not included.

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

symbol
required
string
Instrument asset in the form BASE (e.g. BTC)

query Parameters
limit	
string
Limit of results. Max 10

page	
string
Pagination of deposits

from	
string
Unix timestamp (UTC) for the time and date from where you want to list deposits

to	
string
Unix timestamp (UTC) for the time and date to where you want to list deposits

Responses
200 Response
Response Schema: application/json
Array ()
address	
string
Address of deposit

address_tag	
string
Secondary address identifier for coins like XRP.

amount	
string
Amount of deposit

coin	
string
Coin of deposit

confirmTimes	
string
Confirmations for deposit X / Y, X = Current, Y = Required ( For this coins: "BRL", "BTC", "LTC", "BCH", "XRP", "ETH", the current is not showed )

createdAt	
number
CreatedAt time of deposit

network	
string
Network of deposit

origin	
Array of strings
List of sender addresses

status	
string
Status of deposit

transaction_id	
string
TransactionId of operation on blockchain

transferType	
string
Type of transfer, internal or external

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"address": "nrM1Ke8UsuFktMsmKgfXvqZH2gTLkZxtTG",
"address_tag": 101742499,
"amount": 2.5,
"coin": "XLM",
"confirmTimes": "12 / 12",
"createdAt": 646415100,
"network": "stellar",
"origin": [
"klm3el7SusKftMSMkxfVvQZh5nTzkxTtPQ"
],
"status": 1,
"transaction_id": "e10e3ea123e99a4ec3999ca5ac2a57e23468e994e1b4tt324fe028bbf83548e577",
"transferType": "external"
}
]
Get Deposit Address

get
/accounts/{accountId}/wallet/{symbol}/deposits/addresses
Get the deposit addresses (wallet-in) and/or tag/memo. Deposits are only available for the main wallet when using multiwallet.

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

symbol
required
string
Instrument asset in the form BASE (e.g. BTC)

query Parameters
network	
string
Enum: "stellar" "ethereum"
Network of asset (for assets with more than one network), ignored if asset in present in one network only

Responses
200 Response
Response Schema: application/json
config	
object
Asset extra deposit config

addresses	
Array of objects (share.Addresses)
Array of addresses

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"config": {
"contract_address": "0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9"
},
"addresses": [
{
"hash": "string",
"extra": {},
"qrcode": {}
}
]
}
List Fiat Deposits

get
/accounts/{accountId}/wallet/fiat/{symbol}/deposits
List fiat deposits made by a user for a symbol. Only BRL supported.

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

symbol
required
string
Instrument asset in the form BASE (e.g. BRL)

query Parameters
limit	
string
Limit of results. Max 50. Default 10

page	
string
Pagination of deposits. Begins at 1

from	
string
Unix timestamp (UTC) for the time and date from where you want to list deposits. Filter by created_at field.

to	
string
Unix timestamp (UTC) for the time and date to where you want to list deposits. Filter by created_at field.

Responses
200 Response
Response Schema: application/json
Array ()
id	
integer
Fiat deposit identifier.

amount	
string
Amount of deposit

coin	
string
Coin of deposit

status	
string
Status of deposit

transferType	
string
Type of transfer. (e.g. pix)

source	
object
Information from source of fiat deposit

created_at	
number
Creation unix timestamp

updated_at	
number
Last update unix timestamp

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"id": 1234,
"amount": "10.5",
"coin": "BRL",
"status": "CREDITED",
"transferType": "pix",
"source": {
"bank_code": "208",
"bank_name": "BTG Pactual",
"account_branch": "0001",
"account_number": "0123432"
},
"created_at": 646415100,
"updated_at": 646415100
}
]
Withdraw Coin

post
/accounts/{accountId}/wallet/{symbol}/withdraw
Request for cryptocurrency or Brazilian Real currency transfer. So, if the coin field is filled with "BRL", a withdraw will be made to the informed banking account. If the coin field is filled with a cryptocurrency, a withdraw will be made to the informed wallet address.

IMPORTANT: It's only allowed the transfer to "reliable" destinations. The need to mark as safe a wallet address or banking account is a security measure. For cryptocurrency transfer, it's also needed email approval for the transfer. To mark a wallet address or banking account as "reliable", you need to have activates the "Two-Factor Authentication (2FA)" and have a "Security PIN". This feature is available for all users that have an active API Trade Key. You can configure reliable destinations at "Address Register" and/or "Banking Accounts".

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

symbol
required
string
Cryptocurrency or fiat, ex BTC, BRL, ETH.

Request Body schema: application/json
Request

account_ref	
integer
If your withdraw is fiat, inform id of bank account.

address	
string
If your withdraw is crypto, inform crypto wallet address.

description	
string
Description withdraw. (Maximum 30 characters)

destination_tag	
string
Destination address tag or MEMO if it is required

network	
string
Network withdraw. This parameter is required for crypto with multiple networks, otherwise must be empty. Check here for available networks for a specific crypto.

quantity	
string
Quantity for withdraw.

tx_fee	
string
If your withdraw is crypto, inform fee for pay. Check here for correct values.

Responses
200 Response
Response Schema: application/json
account	
string
Account of withdraw (if coin is fiat).

address	
string
Address of withdraw (if coin is crypto).

coin	
string
Cryptocurrency or fiat, ex BTC, BRL, ETH.

created_at	
string
CreatedAt time of transaction

description	
string
Description of withdraw.

destination_tag	
string
Destination of withdraw

fee	
string
Fee of withdrawal

id	
number
Id of withdrawal transaction

net_quantity	
string
NetQuantity for withdraw.

network	
string
Network of withdraw

quantity	
string
Quantity for withdraw.

status	
integer
Status of withdraw

Status	Description
1	open
2	done
3	canceled
tx	
string
Tx of coin

updated_at	
string
UpdatedAt time of transaction

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"account_ref": 1,
"address": "kasjdhaiucghajn1ekjhqwdkd",
"description": "description example",
"destination_tag": "string",
"network": "stellar",
"quantity": "2.5",
"tx_fee": "2"
}
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"account": "3",
"address": "bc1qs62xef6x0tyxsz87fya6le7htc6q5wayhqdzen",
"coin": "BTC",
"created_at": "1636047578",
"description": "description example",
"destination_tag": "100000044",
"fee": "0.001",
"id": 1,
"net_quantity": "1",
"network": "bitcoin",
"quantity": "2",
"status": 1,
"tx": "0.001",
"updated_at": "1636047578"
}
List Withdraw Coin

get
/accounts/{accountId}/wallet/{symbol}/withdraw
List withdraws by coin.

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

symbol
required
string
Instrument symbol in the form BASE or QUOTE

query Parameters
page	
integer
Pagination of withdraws

page_size	
integer
Pagination size of withdraws(max 50)

from	
integer
Unix timestamp (UTC) of the from required withdraw

Responses
200 Response
Response Schema: application/json
Array ()
account	
string
Account of withdraw (if coin is fiat).

address	
string
Address of withdraw (if coin is crypto).

coin	
string
Cryptocurrency or fiat, ex BTC, BRL, ETH.

created_at	
string
CreatedAt time of transaction

description	
string
Description of withdraw.

destination_tag	
string
Destination of withdraw

fee	
string
Fee of withdrawal

id	
number
Id of withdrawal transaction

net_quantity	
string
NetQuantity for withdraw.

network	
string
Network of withdraw

quantity	
string
Quantity for withdraw.

status	
integer
Status of withdraw

Status	Description
1	open
2	done
3	canceled
tx	
string
Tx of coin

updated_at	
string
UpdatedAt time of transaction

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"account": "3",
"address": "bc1qs62xef6x0tyxsz87fya6le7htc6q5wayhqdzen",
"coin": "BTC",
"created_at": "1636047578",
"description": "description example",
"destination_tag": "100000044",
"fee": "0.001",
"id": 1,
"net_quantity": "1",
"network": "bitcoin",
"quantity": "2",
"status": 1,
"tx": "0.001",
"updated_at": "1636047578"
}
]
Get Withdraw Coin

get
/accounts/{accountId}/wallet/{symbol}/withdraw/{withdrawId}
Get withdraw by coin and id.

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

symbol
required
string
Instrument symbol in the form BASE or QUOTE

withdrawId
required
string
Withdraw identifier to find

Responses
200 Response
Response Schema: application/json
account	
string
Account of withdraw (if coin is fiat).

address	
string
Address of withdraw (if coin is crypto).

coin	
string
Cryptocurrency or fiat, ex BTC, BRL, ETH.

created_at	
string
CreatedAt time of transaction

description	
string
Description of withdraw.

destination_tag	
string
Destination of withdraw

fee	
string
Fee of withdrawal

id	
number
Id of withdrawal transaction

net_quantity	
string
NetQuantity for withdraw.

network	
string
Network of withdraw

quantity	
string
Quantity for withdraw.

status	
integer
Status of withdraw

Status	Description
1	open
2	done
3	canceled
tx	
string
Tx of coin

updated_at	
string
UpdatedAt time of transaction

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"account": "3",
"address": "bc1qs62xef6x0tyxsz87fya6le7htc6q5wayhqdzen",
"coin": "BTC",
"created_at": "1636047578",
"description": "description example",
"destination_tag": "100000044",
"fee": "0.001",
"id": 1,
"net_quantity": "1",
"network": "bitcoin",
"quantity": "2",
"status": 1,
"tx": "0.001",
"updated_at": "1636047578"
}
Get Withdraw Limits

get
/accounts/{accountId}/wallet/withdraw/config/limits
Get fiat and crypto withdraw limits. The limit considers withdraws of the last 24 hours. If the value returned is 0, it means that is not possible to withdraw the asset.

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

query Parameters
symbols	
string
Symbols to filter. Ex.: BTC,LTC,SHIB,BRL

Responses
200 Response
Response Schema: application/json
symbol	
string
Keys in the form of symbols and values in the form of quantity

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"BTC": "0.00001000",
"ETH": "1.00000000"
}
Get BRL Withdraw Config

get
/accounts/{accountId}/wallet/withdraw/config/BRL
Get configurations of BRL cashout. The configurations includes limits and fees information.

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier.

Responses
200 Response
Response Schema: application/json
limit_min	
string
Minimum cashout value.

saving_limit_max	
string
Maximum cashout value of bank account type saving.

total_limit	
string
24 hours limit for fiat cashout.

used_limit	
string
24 hours limit for fiat cashout used.

fees	
Array of objects (Fees)
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"limit_min": "50",
"saving_limit_max": "5000",
"total_limit": "50000",
"used_limit": "5000",
"fees": [
{
"fixed_amount": "0.1",
"percentual": 2.9
}
]
}
List Withdraw Crypto Wallet Addresses

get
/accounts/{accountId}/wallet/withdraw/addresses
List blockchain addresses available for API wallet outs. The addresses are previously registered and confirmed by the user. To get this information, the wallet address must be registered into the Automated Wallet Out process and the request must be done using the same IP also registered at the Automated Wallet Out process.

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

Responses
200 Response
Response Schema: application/json
Array ()
asset	
string
Selected instrument asset (equal to the requested one)

address	
string
Crypto wallet address.

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"asset": "BTC",
"address": "bc1qs62xef6x0tyxsz87fya6le7htc6q5wayhqdzen"
}
]
List Withdraw Bank Accounts

get
/accounts/{accountId}/wallet/withdraw/bank-accounts
List bank accounts available for API cash outs

Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

Responses
200 Response
Response Schema: application/json
Array ()
account_ref	
integer
Bank account id informed for fiat withdrawal.

bank_code	
string
Bank code/number.

bank_name	
string
Bank name.

recipient_name	
string
Name of the withdrawal recipient entity.

recipient_tax_id	
string
Tax id of the withdrawal recipient entity.

account_branch	
string
Bank account branch.

account_number	
string
Account number.

account_type	
string
Account type. It can be CHECKING or SAVING

account_holder	
string
Joint account holder.

joint_account	
boolean
Indicates if it is a joint account

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"account_ref": 1,
"bank_code": "208",
"bank_name": "BTG Pactual",
"recipient_name": "Mercado Bitcoin",
"recipient_tax_id": "18.213.434.0001/35",
"account_branch": "0001",
"account_number": "0123432",
"account_type": "CHECKING",
"account_holder": "",
"joint_account": false
}
]
Trading
List orders

get
/accounts/{accountId}/{symbol}/orders
List orders from specific market (most recent first)

Rate Limit: 10 requests/sec
Authorizations:
Bearer
path Parameters
symbol
required
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)

accountId
required
string
Account identifier. Obtained from List Accounts

query Parameters
has_executions	
string
Filter for orders with or without execution
Example: has_executions=true

side	
string
Order side to be filtered
Enum: buy or sell

status	
string
Order status
Enum: created, working, cancelled, filled

id_from	
string
Filter for orders from the entered order ID
Example: id_from=5

id_to	
string
Filter for orders up to the entered order ID
Example: id_to=12

created_at_from	
string
Filter for orders created from the timestamp (UTC) entered
Example:created_at_from=1633538771

created_at_to	
string
Filter for orders created up to the timestamp (UTC) entered
Example:created_at_to=1633539132

executed_at_from	
string
Filter for orders executed from the timestamp (UTC) entered
Example:executed_at_from=1633538771

executed_at_to	
string
Filter for orders executed up to the timestamp (UTC) entered
Example:executed_at_to=1633539132

Responses
200 Response
Response Schema: application/json
Array ()
avgPrice	
number
Simple average price. For stoplimit orders with no limit order triggered the displayed value will be 0.00000000.

cost	
number
Cost used when placing the order (not considering fee application)

created_at	
number
Date of order creation timestamp (UTC)

executions	
Array of objects (Execution)
Executed order transactions

externalId	
string
External Identifier setted by client.

fee	
string
Charged volume by fee application

filledQty	
string
Filled quantity. For stoplimit orders with no limit order triggered the displayed value will be 0.00000000.

id	
string
Unique order identifier.

instrument	
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)

limitPrice	
number
Limit price used when placing the limit order (not considering fee application)

qty	
string
Volume used when placing the order (not considering fee application)

side	
string
String constants to describe an order side

Enum: buy sell

Side	Description
buy	purchase order
sell	sales order
status	
string
String constants to describe an order status.

Enum: created working cancelled filled

Status	Description
created	order is created and waiting to be processed
working	order is created but not fully executed yet
cancelled	order is cancelled
filled	order is fully executed
stopPrice	
number
Stop price trigger used when placing the stop limit order

triggerOrderId	
string
Limit order id created when stop price is achieved.

type	
string
String constants to describe an order type

Enum: market, limit, stoplimit and post-only

Type	Description
market	market order
limit	limit order
stoplimit	stoplimit order
post-only	post-only order
updated_at	
number
Date of last order update timestamp (UTC)

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
[
{
"avgPrice": 500,
"cost": 10000,
"created_at": 1636047578,
"executions": [
{}
],
"externalId": "1372183",
"fee": "0.003",
"filledQty": "0.001",
"id": "01HCDAA7YJ68ZJ0FTEPR7DYDS1",
"instrument": "BTC-BRL",
"limitPrice": 9997,
"qty": "0.01000000",
"side": "buy",
"status": "filled",
"stopPrice": 18000,
"triggerOrderId": "42",
"type": "limit",
"updated_at": 1636047578
}
]
Place order

post
/accounts/{accountId}/{symbol}/orders
Place a new order.

Rate Limit: 3 requests/sec
Authorizations:
Bearer
path Parameters
symbol
required
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)

accountId
required
string
Account identifier. Obtained from List Accounts

Request Body schema: application/json
Request

async	
boolean
Create an order asynchronously (default false)

If true the order status response can be created

cost	
number
Quote currency amount to be spent (used only for orders with type market and side buy)

externalId	
string
External customized order Id

limitPrice	
number
Limit price per base currency (used only for orders with type limit, post-only or stoplimit)

qty	
string
Order quantity (volume). Required only if cost is not set

side	
string
String constants to describe an order side

Enum: buy sell

Side	Description
buy	purchase order
sell	sales order
stopPrice	
number
Price that triggers a limit order creation (used only for orders with type stoplimit)

type	
string
String constants to describe an order type

Enum: market, limit, stoplimit and post-only

Type	Description
market	market order
limit	limit order
stoplimit	stoplimit order
post-only	post-only order
Responses
200 Response
Response Schema: application/json
orderId	
string
Unique alphanumeric order identifier

Request samples
Payload
Content type
application/json

Copy
Expand allCollapse all
{
"async": true,
"cost": 100,
"externalId": "134872873",
"limitPrice": 9997,
"qty": "0.001",
"side": "buy",
"stopPrice": 1000,
"type": "limit"
}
Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"orderId": "01H50SZYF0WZQY8Q3NCJ2HGD8G"
}
Cancel order

delete
/accounts/{accountId}/{symbol}/orders/{orderId}
Cancel an existing order.

Rate Limit: 3 requests/sec
Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

symbol
required
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)

orderId
required
string
Unique order identifier

query Parameters
async	
boolean
Cancel an order asynchronously (default true)

If false the order status response will be polled until is cancelled

Responses
200 Response
Response Schema: application/json
status	
string
If the option async was set to true you order may or may not be canceled. If not, you will receive the following message.

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"status": "queued_to_cancel"
}
Get orders

get
/accounts/{accountId}/{symbol}/orders/{orderId}
Get unique order by identifier

Rate Limit: 1 requests/sec
Authorizations:
Bearer
path Parameters
symbol
required
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)

accountId
required
string
Account identifier. Obtained from List Accounts

orderId
required
string
Unique order identifier

Responses
200 Response
Response Schema: application/json
avgPrice	
number
Simple average price. For stoplimit orders with no limit order triggered the displayed value will be 0.00000000.

cost	
number
Cost used when placing the order (not considering fee application)

created_at	
number
Date of order creation timestamp (UTC)

executions	
Array of objects (Execution)
Executed order transactions

externalId	
string
External Identifier setted by client.

fee	
string
Charged volume by fee application

filledQty	
string
Filled quantity. For stoplimit orders with no limit order triggered the displayed value will be 0.00000000.

id	
string
Unique order identifier.

instrument	
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)

limitPrice	
number
Limit price used when placing the limit order (not considering fee application)

qty	
string
Volume used when placing the order (not considering fee application)

side	
string
String constants to describe an order side

Enum: buy sell

Side	Description
buy	purchase order
sell	sales order
status	
string
String constants to describe an order status.

Enum: created working cancelled filled

Status	Description
created	order is created and waiting to be processed
working	order is created but not fully executed yet
cancelled	order is cancelled
filled	order is fully executed
stopPrice	
number
Stop price trigger used when placing the stop limit order

triggerOrderId	
string
Limit order id created when stop price is achieved.

type	
string
String constants to describe an order type

Enum: market, limit, stoplimit and post-only

Type	Description
market	market order
limit	limit order
stoplimit	stoplimit order
post-only	post-only order
updated_at	
number
Date of last order update timestamp (UTC)

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"avgPrice": 500,
"cost": 10000,
"created_at": 1636047578,
"executions": [
{
"executed_at": 1634731027,
"fee_rate": "0.70000000",
"id": "16",
"instrument": "BTC-BRL",
"price": 500,
"qty": "0.001",
"side": "buy",
"liquidity": "maker"
}
],
"externalId": "1372183",
"fee": "0.003",
"filledQty": "0.001",
"id": "01HCDAA7YJ68ZJ0FTEPR7DYDS1",
"instrument": "BTC-BRL",
"limitPrice": 9997,
"qty": "0.01000000",
"side": "buy",
"status": "filled",
"stopPrice": 18000,
"triggerOrderId": "42",
"type": "limit",
"updated_at": 1636047578
}
Cancel all open orders

delete
/accounts/{accountId}/cancel_all_open_orders
Cancel all open orders for an account.

Rate Limit: 1 requests/min
Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

query Parameters
has_executions	
boolean
Filter for orders with or without execution

symbol	
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)
Example:symbol=BTC-BRL

Responses
200 Response
Response Schema: application/json
crypto	
string
Crypto symbol

fiat	
string
Fiat symbol

order_id	
string
Unique order identifier

order_type	
string
String constants to describe an order type

Enum: limit, stoplimit and post-only

Type	Description
limit	limit order
stoplimit	stoplimit order
post-only	post-only order
side	
string
String constants to describe an order side

Enum: BID and ASK

Side	Description
BID	purchase (buy) order
ASK	sales (sell) order
status	
string
Status of request (not order status)

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"crypto": "BTC",
"fiat": "BRL",
"order_id": "27",
"order_type": "limit",
"side": "BID",
"status": "queued_to_cancel"
}
List all orders

get
/accounts/{accountId}/orders
List orders from all markets (most recent first)

Rate Limit: 3 requests/sec
Authorizations:
Bearer
path Parameters
accountId
required
string
Account identifier. Obtained from List Accounts

query Parameters
has_executions	
string
Filter for orders with or without execution
Example: has_executions=true

symbol	
string
Instrument symbol in the form BASE-QUOTE(e.g. BTC-BRL)
Example:symbol=BTC-BRL

status	
string
Order status
Example: status=created,working,cancelled,filled

size	
string
Size quantity of orders to find
Example: size=1

Responses
200 Response
Response Schema: application/json
items	
Array of objects (Orders)
Items. List of orders

Response samples
200
Content type
application/json

Copy
Expand allCollapse all
{
"items": [
{
"created_at": 1636047578,
"filledQty": "0.001",
"id": "01HCDAA7YJ68ZJ0FTEPR7DYDS1",
"instrument": "BTC-BRL",
"limitPrice": 9997,
"qty": "0.001",
"side": "buy",
"status": "filled",
"stopPrice": 18000,
"triggerOrderId": "42",
"type": "limit",
"updated_at": 1636047578,
"external_id": "external-id-informed-by-user"
}
]
}
Authorize
Authorize user to access following Oauth2 pattern (client_credentials flow)

post
/oauth2/token
ClientId and ClientSecret authentication.

Request Body schema: application/x-www-form-urlencoded
grant_type
required
string
Should be always: client_credentials

scope
required
string
For now, should be: global

client_id
required
string
Credential client id

client_secret
required
string
Credential client secret

Responses
200 Response
Response Schema: application/json
access_token	
string
Access token acts as a session ID that the application uses for making requests. This token should be protected as if it were user credentials.

expires_in	
integer
The time in seconds that the token will remain valid.

scope	
string
The scope witch the token is valid.

token_type	
string
The token type.

401 Unauthorized
Response Schema: application/json
code	
string
The internal error code.

data	
object
Response samples
200401
Content type
application/json

Copy
Expand allCollapse all
{
"access_token": "some.valid.jwt",
"expires_in": 3599,
"scope": "global",
"token_type": "bearer"
}


























MercadoBitcoin Websockets API v0.0.4
Overview
WebSockets API offers real-time market data updates. WebSockets is a bidirectional protocol offering fastest real-time data, helping you build real-time applications.

REST API
If you are looking for REST API, click here

General considerations
All messages are encoded in JSON format
Timestamps should not be considered unique.
Use REST API to fetch available markets to be subscribed.
Do a reconnection if a connection is closed.
Connection details
A User-Agent header SHOULD be sent to pass security restrictions

If a connection is made and no message is sent in 5 seconds, the current connection is closed.

A Origin header can be sent, so we can identify you

Production
URL	Scheme	Path	Description
ws.mercadobitcoin.net	wss	/ws	Production server
Errors
A list of errors can be found here

Example of API clients







General Messages
ping
To verify if a server is online, the client can send a ping message to the server.

The server answers with a pong.

Payload
Name	Type	Description
type	string	Message request type (ping)
Example
subscribe
Subscribe to a topic. An answer is provided with the request subscription data.

Payload
Name	Type	Description
type	string	Message request type (subscribe)
subscription	object	Subscription details
└ id	string	Available market (e.g BRLBTC)
└ name	string	Subscription type (e.g orderbook), possible values: ticker, orderbook, trades
└ limit	integer	Available only for orderbook. Limits the book depth. Possible values: 10, 20, 50, 100, 200
Examples
unsubscribe
Unsubscribe to a topic. The client should send the same information provided on subscription. An answer is provided with the request subscription data.

Payload
Name	Type	Description
type	string	Message request type (subscribe)
subscription	object	Subscription details
└ id	string	Available market (e.g BRLBTC)
└ name	string	Subscription type (e.g orderbook), possible values: ticker, orderbook, trades
└ limit	integer	Available only for orderbook. Limits the book depth. Possible values: 10, 20, 50, 100, 200




General Messages
ping
To verify if a server is online, the client can send a ping message to the server.

The server answers with a pong.

Payload
Name	Type	Description
type	string	Message request type (ping)
Example
subscribe
Subscribe to a topic. An answer is provided with the request subscription data.

Payload
Name	Type	Description
type	string	Message request type (subscribe)
subscription	object	Subscription details
└ id	string	Available market (e.g BRLBTC)
└ name	string	Subscription type (e.g orderbook), possible values: ticker, orderbook, trades
└ limit	integer	Available only for orderbook. Limits the book depth. Possible values: 10, 20, 50, 100, 200
Examples
unsubscribe
Unsubscribe to a topic. The client should send the same information provided on subscription. An answer is provided with the request subscription data.

Payload
Name	Type	Description
type	string	Message request type (subscribe)
subscription	object	Subscription details
└ id	string	Available market (e.g BRLBTC)
└ name	string	Subscription type (e.g orderbook), possible values: ticker, orderbook, trades
└ limit	integer	Available only for orderbook. Limits the book depth. Possible values: 10, 20, 50, 100, 200





Public Messages
Websocket messages are sent as string

Messages follow the payload:

Name	Type	Description
type	string	Event type (e.g orderbook)
ts	integer	Unix timestamp in nanoseconds. Represents the time when a message is sent from server.
id	string	Market
limit	integer	Orderbook depth limit. Available only for orderbook events.
data	object	Event data
You can use the message timestamp and the data timestamp to measure lag.

ticker
Last 24h trading information.

Payload
Name	Type	Description
type	string	Event type ticker
ts	integer	Unix timestamp in nanoseconds. Represents the time when a message is sent from server.
id	string	Market
data	object	Event data
└ high	string	High price
└ low	string	Low price
└ last	string	Last price
└ buy	string	Buy price
└ sell	string	Sell price
└ open	string	Open price
└ vol	string	Volume
└ date	integer	Unix timestamp representing the time when the ticker is generated
Example
trades
Last executed trade.

Payload
Name	Type	Description
type	string	Event type trade
ts	integer	Unix timestamp in nanoseconds. Represents the time when a message is sent from server.
id	string	Market
data	object	Event data
└ tid	integer	Trade ID
└ date	integer	Unix timestamp when a trade is executed.
└ type	string	Trade side, buy or sell
└ price	float	Trade price
└ amount	float	Trade volume
Example
{
  "type": "trade",
  "id": "BRLBTC",
  "ts": 1607685693917511270,
  "data": {
    "tid": 8522200,
    "date": 1613000055,
    "type": "sell",
    "price": 244500.03022,
    "amount": 0.00052
  }
}
orderbook
Trading orderbook.

A limit parameter is given to restrict the depth.

Possible values for limit:

10
20
50
100
200
Payload
Name	Type	Description
type	string	Event type orderbook
ts	integer	Unix timestamp in nanoseconds. Represents the time when a message is sent from server.
id	string	Market
data	object	Event data
└ timestamp	object	Unix timestamp in nanoseconds when the orderbook is generated.
└ ask	object	Ask side
 └ array	array	Array of values
  └ volume	float	Volume
  └ price	float	Price
└ bid	object	Bid side
 └ array	array	Array of values
  └ volume	float	Volume
  └ price	float	Price
Example
{
  "type": "orderbook",
  "id": "BRLBTC",
  "ts": 1607685456412989154,
  "data": {
    "asks": [
      [
        12221,
        7
      ],
      [
        13469,
        2
      ],
      [
        14019,
        5
      ]
    ],
    "bids": [
      [
        10000,
        100
      ]
    ],
    "timestamp": 1607685456412989154
  }
}





Errors
The API returns errors in the following format:

{
  "type": "error",
  "message": "<message>"
}
Error List
Message	Description
unknown message type	Message type is unknown
unexpected end of JSON input	JSON is invalid
already subscribed	Subscription to topic already exists
not subscribed	Subscription not exists when trying to unsubscribe