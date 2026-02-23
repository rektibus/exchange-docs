ntroduction
ORANGEX api v1.0.0

Http request path: https://api.orangex.com/api/v1
Ws request path: wss://api.orangex.com/ws/api/v1
JSON-RPC
Authentication example
The API consists of public and private methods. The public methods do not require authentication. The private methods use OAuth 2.0 authentication. This means that a valid OAuth access token must be included in the request, which can be achived by calling method public/auth

When the token was assigned to the user, it should be passed along, with other request parameters, back to the server:

Connection type	Access token placement
Websocket	Inside request JSON parameters, as an access_token field
HTTP (REST)	Header Authorization: bearerToken`` value
Access scope

When asking for access token user can provide the required access level (called scope) which defines what type of functionality he/she wants to use, and whether requests are only going to check for some data or also to update them. Scopes are required and checked for private methods, so if you plan to use only public information you can stay with values assigned by default.

Scope	Description
account:read	Access to account methods - read only data.
account:read_write	Access to account methods - allows to manage account settings, add subaccounts, etc.
trade:read	Access to trade methods - read only data.
trade:read_write	Access to trade methods - required to create and modify orders.
wallet:read	Access to wallet methods - read only data.
wallet:read_write	Access to wallet methods - allows to withdraw, generate new deposit address, etc.
wallet:none, account:none, trade:none	Blocked access to specified functionality.
block_trade:read	Access to block_trade methods - reading info about block trades - read only data.
block_trade:read_write	Access to block_trade methods - required to create block trades.
NOTICE: Depending on choosing an authentication method (grant type) some scopes could be narrowed by the server or limited by user API key configured scope, e.g. when grant_type = client_credentials and scope = wallet:read_write could be modified by the server as scope = wallet:read.

The user shouldn't assume that requested values are blindly accepted and should verify assigned scoped.

Notifications
API users can subscribe to certain types of notifications. This means that they will receive JSON-RPC notification-messages from the server when certain events occur, such as changes to the index price or changes to the order book for a certain instrument.

The API methods public/subscribe and private/subscribe are used to set up a subscription. Since HTTP does not support the sending of messages from server to client, these methods are only availble when using the Websocket transport mechanism.

At the moment of subscription a "channel" must be specified. The channel determines the type of events that will be received. See [Subscriptions] for more details about the channels.

In accordance with the JSON-RPC specification, the format of a notification is that of a request message without an id field. The value of the method field will always be "subscription". The params field will always be an object with 2 members: channel and data. The value of the channel member is the name of the channel (a string). The value of the data member is an object that contains data that is specific for the channel.

Request messages
According to the JSON-RPC sepcification the requests must be JSON objects with the following fields.

Name	Type	Description
jsonrpc	string	The version of the JSON-RPC spec: "2.0"
id	integer or string	An identifier of the request. If it is included, then the response will contain the same identifier
method	string	The method to be invoked
params	object	The parameters values for the method. The field names must match with the expected parameter names. The parameters that are expected are described in the documentation for the methods, below.
Response messages
The JSON-RPC API always responds with a JSON object with the following fields.

Name	Type	Description
id	integer	This is the same id that was sent in the request.
result	any	If successful, the result of the API call. The format for the result is described with each method.
error	error object	Only present if there was an error invoking the method. The error object is described below.
usIn	integer	The timestamp when the requests was received (microseconds since the Unix epoch)
usOut	integer	The timestamp when the response was sent (microseconds since the Unix epoch)
usDiff	integer	The number of microseconds that was spent handling the request
Authentication
auth
Description

Retrieve an Oauth access token, to be used for authentication of 'private' requests.

Three methods of authentication are supported:

client_credentials - using the access key and access secret that can be found on the API page on the website
client_signature - using the access key that can be found on the API page on the website and user generated signature
The signature is generated by the following formula:
StringToSign = clientId + "\n" + Timestamp + "\n" + Nonce + "\n";
Signature = HEX_STRING( HMAC-SHA256( ClientSecret, StringToSign ));
refresh_token - using a refresh token that was received from an earlier invocation The response will contain an access token, expiration period (number of seconds that the token is valid) and a refresh token that can be used to get a new set of tokens.
Method

/public/auth
Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/public/auth",
  "params" : {
    "grant_type" : "client_credentials",
    "client_id" : "qpdskdfnaowpfewq",
    "client_secret" : "oqentgrfnfdwnveaef"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
grant_type	true	string	client_credentials client_signature refresh_token	Method of authentication
client_id	true	tring		Required for grant type client_credentials and client_signature
client_secret	true	string		Required for grant type client_credentials
refresh_token	true	string		Required for grant type refresh_token
signature	true	string		Required for grant type client_signature; it's a cryptographic signature calculated over provided fields using user secret key. The signature should be calculated as an HMAC (Hash-based Message Authentication Code) with SHA256 hash algorithm
nonce	true	string		Optional for grant type client_signature; delivers user generated initialization vector for the server token
timestamp	true	string		Required for grant type client_signature, provides time when request has been generated (milliseconds since the UNIX epoch)
The above command returns JSON structured like this (real example)

{
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1597127926021,
    "usOut": 1597127926052,
    "usDiff": 31,
    "result": {
        "access_token": "ba3avFNzfE",
        "token_type": "bearer",
        "refresh_token": "X9VtGUvsWvzPAjx63jzZnY+yTPTC8Ip8GYHSK29j0teOXcjsA=",
        "expires_in": 43199,
        "scope": "account:read_write block_trade:read_write trade:read_write wallet:read_write"
    }
}
Response

Name	Type	Description
result	object	
› access_token	string	
› expires_in	integer	Token lifetime in seconds
› refresh_token	string	Can be used to request a new token (with a new lifetime)
› scope	string	Type of the access for assigned token
› token_type	string	Authorization type, allowed value - bearer
logout
Method

/private/logout
Gracefully close websocket connection, when COD (Cancel On Disconnect) is enabled orders are not cancelled

This is a private method; it can only be used after authentication.

Parameters

This method takes no parameters

Response

This method has no response body

Wallet
Add withdraw address
Description

Add withdraw address
Method

/private/add_withdraw_address
Request example

{
    "jsonrpc":"2.0",
    "id":"450",
    "method":"/private/add_withdraw_address",
    "params":{
        "coin_type":"BTC",
        "main_chain":"BTC",
        "address":"2NBqqD5GRJ8wHy1PYyCXTe9ke5226FhavBz",
        "memo":"",
        "amount":"1.0999",
        "tfa":"123456",
        "source": "Other"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
coin_type	true	string		Coin type, i.e BTC ETH USDT
main_chain	true	string		Main chain, i.e ETH BTC
address	true	string		Address must be in the whitelist.
memo	false	string		Address memo or tag, required if it exists.
amount	true	string		Amount of funds to be withdrawn
tfa	true	string		TFA code
resource	true	string		Address source. eg: Other
The above command returns JSON structured like this (real example)

  {
    "id":"1",
    "jsonrpc":"2.0",
    "usIn":1590387640408,
    "usOut":1590387641134,
    "usDiff":726,
    "result":{
        "withdraw_id":"123000000001"
    }
}
Response

Name	Type	Enum	Description
result	object		
› withdraw_id	string		Withdraw record id.
Get Deposit Record
Description

Retrieve the latest users deposits
Method

/private/get_deposit_record
Request example

{
    "jsonrpc":"2.0",
    "id":"448",
    "method":"/private/get_deposit_record",
    "params":{
        "coin_type":"BTC"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
coin_type	true	string		Coin type, i.e BTC
The above command returns JSON structured like this (real example)

 {
    "id":"1",
    "jsonrpc":"2.0",
    "usIn":1590387640408,
    "usOut":1590387641134,
    "usDiff":726,
    "result":[
        {
            "id":"12300000001",
            "coin_type":"BTC",
            "token_code":"BTC",
            "main_chain":"BTC",
            "address":"2NBqqD5GRJ8wHy1PYyCXTe9ke5226FhavBz",
            "amount":"1.2345",
            "create_time":"1830268800000",
            "update_time":"1830268800000",
            "state":"deposit_confirmed",
            "tx_hash":"0xdbb8ed9ab6696c37e690b6208b55e7d56b152421ea8567576aa63d05fac0282b",
            "full_name":"Bitcoin"
        }
    ]
}
Response

Name	Type	Enum	Description
result	object		
› id	string		Withdraw record id.
› coin_type	string		Coin type, i.e BTC
› token_code	string		Token code, i.e USDT-ERC20
› main_chain	string		Main chain
› address	string		Address
› amount	string		Amount
› create_time	timestamp		
› update_time	timestamp		
› state	string	deposit_waiting_confirm, deposit_confirmed	
› tx_hash	string		Transaction hash
› full_name	string		Full name, i.e Bitcoin
Get Withdraw Record
Description

Retrieve the latest users withdrawals
Method

/private/get_withdraw_record
Request example

{
    "jsonrpc":"2.0",
    "id":"448",
    "method":"/private/get_withdraw_record",
    "params":{
        "coin_type":"BTC",
        "withdraw_id":"123000000001"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
coin_type	true	string		Coin type, i.e BTC
withdraw_id	false	string		
The above command returns JSON structured like this (real example)

 {
    "id":"1",
    "jsonrpc":"2.0",
    "usIn":1590387640408,
    "usOut":1590387641134,
    "usDiff":726,
    "result":[
        {
            "id":"12300000001",
            "coin_type":"BTC",
            "main_chain":"BTC",
            "address":"2NBqqD5GRJ8wHy1PYyCXTe9ke5226FhavBz",
            "amount":"1.2345",
            "create_time":"1830268800000",
            "update_time":"1830268800000",
            "state":"withdraw_init",
            "tx_hash":"0xdbb8ed9ab6696c37e690b6208b55e7d56b152421ea8567576aa63d05fac0282b",
            "full_name":"Bitcoin"
        }
    ]
}
Response

Name	Type	Enum	Description
result	object		
› id	string		Withdraw record id.
› coin_type	string		Coin type, i.e BTC
› main_chain	string		Main chain
› address	string		Address
› amount	string		Amount
› create_time	timestamp		
› update_time	timestamp		
› state	string	withdraw_init, withdraw_noticed_block_chain, withdraw_waiting_confirm, withdraw_confirmed, withdraw_faild , withdraw_auditing, withdraw_audit_reject	
› tx_hash	string		Transaction hash
› full_name	string		Full name, i.e Bitcoin
Get assets info
Description

Get assets info.
Method

/private/get_assets_info
Request example

{ 
    "jsonrpc":"2.0",
    "id": 1,
    "method": "/private/get_assets_info",
     "params":{
         "asset_type": ["ALL"]
     }
}
Request Parameters

Parameter	Required	Type	Enum	Description
asset_type	true	string array	ALL, SPOT,PERPETUAL, WALLET	Assets type.
coin_type	false	string array		CoinType。Only support WALLET, SPOT, MARGIN 。
The above command returns JSON structured like this (real example)

{
  "id": "1",
  "jsonrpc": "2.0",
  "usIn": 1607597828772,
  "usOut": 1607597829103,
  "usDiff": 331,
  "result": {
    "WALLET": {
      "total": "5578184962",
      "coupon": "0",
      "details": [
        {
          "available": "4999",
          "freeze": "0",
          "coin_type": "BTC",
          "current_mark_price": "38000"
        },
        {
          "available": "0",
          "freeze": "0",
          "coin_type": "ETH",
          "current_mark_price": "1600"
        },
        {
          "available": "5577199963",
          "freeze": "0",
          "coin_type": "USDT",
          "current_mark_price": "1"
        }
      ]
    },
    "SPOT": {
      "total": "281472.28536534",
      "net": "281472.28536534",
      "available": "281472.28536534",
      "details": [
        {
          "available": "9.99902",
          "freeze": "0",
          "total": "9.99902",
          "coin_type": "BTC",
          "current_mark_price": "18150.117"
        },
        {
          "available": "0",
          "freeze": "0",
          "total": "0",
          "coin_type": "ETH",
          "current_mark_price": "555.005"
        },
        {
          "available": "0",
          "freeze": "0",
          "total": "0",
          "coin_type": "USD",
          "current_mark_price": "0"
        },
        {
          "available": "99988.90248",
          "freeze": "0",
          "total": "99988.90248",
          "coin_type": "USDT",
          "current_mark_price": "1"
        }
      ]
    },
    "PERPETUAL": {
      "global_state": 0,
      "available_funds": "0",
      "available_withdraw_funds": "0",
      "total_pl": "0",
      "total_upl": "0",
      "position_rpl": "0",
      "total_upl_isolated": "0",
      "total_upl_cross": "0",
      "total_initial_margin_cross": "0",
      "total_initial_margin_isolated": "0",
      "total_variable_funds": "0",
      "total_margin_balance_isolated": "0",
      "total_margin_balance_cross": "0",
      "total_maintenance_margin_cross": "0",
      "total_wallet_balance_isolated": "0",
      "order_frozen": "0",
      "order_cross_frozen": "0",
      "order_isolated_frozen": "0",
      "bonus": 0,
      "bonus_max": 0
    }
  }
}
Response

Parameter	Type	Enum	Description
result	object array		
› WALLET	object		Wallet assets
› SPOT	object		Spot assets. Spot used to spot trading without leverage
› PERPETUAL	object		Perpetual assets.
Wallet assets fields（WALLET ）

Parameter	Type	Enum	Description
total	number		Total assets of wallet, equivalent to usdt
coupon	number		Coupon of wallet, equivalent to usdt
details	object array		Details of wallet assets
› coin_type	string		Coin
› available	number		Available assets, wallet balance
› freeze	number		Freezing assets
› current_mark_price	number		Mark Price, the unit is usdt
Spot asset field(SPOT)

Parameter	Type	Enum	Description
total	number		The total market value of all spot's assets, equivalent to usdt
available	number		The total market value of all available assets of spot, equivalent to usdt
details	object array		Asset details in single coin
› coin_type	string		Coin
› available	number		Available assets
› freeze	number		Freezing assets
› total	number		Total = Available + Freeze
› current_mark_price	number		Mark Price, the unit is usdt
Perpetual asset field（PERPETUAL ）

Parameter	Type	Enum	Description
wallet_balance	number		Total wallet balance.
available_funds	number		available funds
available_withdraw_funds	number		Transferable quantity
total_pl	number		Total profit and loss of trading area
total_upl	number		Unrealized profit and loss
position_rpl	number		Realized profit and loss
total_upl_isolated	number		Unrealized profit and loss of isolated
total_upl_cross	number		Unrealized profit and loss of cross
total_initial_margin_cross	number		Initial margin of cross
total_initial_margin_isolated	number		Initial margin of isolated
total_margin_balance_isolated	number		Total margin balance of isolated
total_margin_balance_cross	number		Total margin balance of cross
total_margin_balance	number		Total margin balance
total_maintenance_margin_cross	number		Maintenance margin of cross
total_wallet_balance_isolated	number		Total wallet balance of isolated
order_frozen	number		Frozen of order
order_cross_frozen	number		Frozen of cross order
order_isolated_frozen	number		Frozen of isolated order
bonus	number		Available bonus.
bonus_max	number		Upper limit of bonus.
Get coin config
Description

Get information of coins (available for deposit and withdraw)
Method

/public/get_coin_config
Request example

{
    "jsonrpc":"2.0",
    "id":"448",
    "method":"/public/get_coin_config",
    "params":{
        "coin_type": "ETH"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
coin_type	true	string		Coin type, i.e BTC
The above command returns JSON structured like this (real example)

{
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1672992305854,
    "usOut": 1672992305857,
    "usDiff": 3,
    "result": [
        {
            "enable": true,
            "coin_type": "USDT",
            "withdraw_status": true,
            "deposit_status": true,
            "full_name": "Tether",
            "token_config_list": [
                {
                    "token_code": "USDT-TRC20",
                    "main_chain": "TRX",
                    "main_chain_show": "TRX Tron(TRC20)",
                    "token_precision": 5,
                    "deposit_status": true,
                    "withdraw_status": true,
                    "most_withdraw_limit": "10000",
                    "least_withdraw_limit": "10",
                    "least_deposit_limit": "1",
                    "withdraw_fee": "1",
                    "token_address_regular": "^[T][a-km-zA-HJ-NP-Z1-9]{25,34}$",
                    "token_explore": "https://tronscan.org/#/transaction/{##}",
                    "token_confirmation": 36,
                    "token_memo_option": "0",
                    "deposit_memo_status": false,
                    "withdraw_memo_status": false,
                    "token_memo_status": false,
                    "withdraw_fee_extra_ratio": "0"
                },
                {
                    "token_code": "USDT-ERC20",
                    "main_chain": "ETH",
                    "main_chain_show": "ETH Ethereum(ERC20)",
                    "token_precision": 5,
                    "deposit_status": true,
                    "withdraw_status": true,
                    "most_withdraw_limit": "9999",
                    "least_withdraw_limit": "60",
                    "least_deposit_limit": "1",
                    "withdraw_fee": "10",
                    "token_address_regular": "^0x[a-fA-F0-9]{40}$",
                    "token_explore": "https://etherscan.io/tx/{##}",
                    "token_confirmation": 20,
                    "token_memo_option": "0",
                    "deposit_memo_status": false,
                    "withdraw_memo_status": false,
                    "token_memo_status": false,
                    "withdraw_fee_extra_ratio": "0"
                }
            ],
            "inner_transfer_config": {
                "least_withdraw_limit": "60",
                "withdraw_precision": 8
            }
        }
    ]
}
Response

Name	Type	Enum	Description
result	object array		
› enable	Boolean		Coin status.
› coin_type	String		Coin name.
› withdraw_status	Boolean		Withdrawal status.
› deposit_status	Boolean		Deposit status.
› token_config_list	object array		Chains config.
›› token_code	String		Uniquely identifies.
›› main_chain	String		Chain name.
›› token_precision	number		Coin precision of current chain.
›› withdraw_fee	number		Withdrawal fee.
›› deposit_status	Boolean		Deposit status of current chain.
›› withdraw_status	Boolean		Withdrawal status of current chain.
›› least_withdraw_limit	number		Minimum withdrawal amount.
›› least_deposit_limit	number		Minimum deposit amount.
›› token_address_regular	String		Regex matching rules for withdrawal addresses.
›› withdraw_memo_status	Boolean		Indicates whether memo is required when withdrawing coins.
› inner_transfer_config	object		Internal transfer configuration of the current coin.
›› least_withdraw_limit	number		Minimum withdrawal amount.
›› withdraw_precision	number		Withdraw precision.
Withdraw
Description

Submit a withdraw request.
client_signature auth type.
Method

/private/withdraw
Request example

{
    "jsonrpc":"2.0",
    "id":"448",
    "method":"/private/withdraw",
    "params":{
        "coin_type": "ETH",
        "main_chain": "ETH",
        "address": "address",
        "amount": "1",
        "memo": "-",
        "resource":"B",
        "toUserType":"personal",
        "toUserFirstName":"firstName",
        "toUserLastName":"lastName"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
coin_type	true	string		Coin type, i.e BTC
main_chain	true	string		Network.
address	true	string		Address
amount	true	Number		Amount
memo	false	String		Secondary address identifier for coins like XRP.
resource	false	String		When withdrawal amount exceeding 100W Won for Korean account and 1,000 EUR for non-Korean account, Travel Rule requirements are necessary in withdrawal requests. Ensure that the provided recipient type and name match what have registered with the receiving exchange. Failing to do so may cause an error.
Recipient Platform. Interface reference withdraw address resource. If target recipient platform is not found, please set as other.
toUserType	false	String	personal, legal	Type of recipient account. Individual KYC account set as personal, Corporate KYC account set as legal.
toUserFirstName	false	String		Individual type needed. Recipient’s first name.
toUserLastName	false	String		Individual type needed. Recipient’s last name.
toUserLegalName	false	String		Corporate type needed. Legal name of recipient’s corporate.
representativeFirstName	false	String		Corporate type needed. First name of representative of recipient’s corporate.
representativeLastName	false	String		Corporate type needed. Last name of representative of recipient’s corporate.
The above command returns JSON structured like this (real example)

{
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1618470601600,
    "usOut": 1618470602504,
    "usDiff": 904,
    "result": {
        "withdraw_id":123123
    }
}
Response

Name	Type	Enum	Description
result	object		
› withdraw_id	string		Withdraw record id.
Withdraw address resource
Description

Withdrawal address source platform
Method

/private/withdraw_address_resource
Request example

{
    "jsonrpc":"2.0",
    "id":"448",
    "method":"/private/withdraw_address_resource",
    "params":{}
}
The above command returns JSON structured like this (real example)

{
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1625541637418,
    "usOut": 1625541638285,
    "usDiff": 867,
    "result": {
        "resourceList": [
            "beeblock","basic-finance"
        ],
        "resourceEntityList": [
            {"vaspName":"Beeblock","entityId":"beeblock"},
            {"vaspName":"Basic-finance","entityId":"basic-finance"}
        ]
    }
}
Response

Name	Type	Enum	Description
result	object		
resourceList	list of String		
>	string		Address resource id
resourceEntityList	list of Object		
> vaspName	string		Address resource
> entityId	string		Address resource id
Inner Transfer
Description

Submit a inner transfer request.
Method

/private/inner_transfer
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/private/inner_transfer",
    "params":{
        "amount":"1",
        "coinType":"ETH",
        "innerWalletType":"uid",
        "innerWalletValue":"30487865"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
amount	true	BigDecimal		Amount, i.e 1
coinType	true	string		Short name of coin
innerWalletType	true	string		Receiver type, email,uid
innerWalletValue	true	Number		Info of receiver‘s email or uid
asset_type	false	String		Wallet account, WALLET, SPOT,PERPETUAL, Default WALLET
The above command returns JSON structured like this (real example)

{
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1655434905711,
    "usOut": 1655434906270,
    "usDiff": 559,
    "result": {
          "withdrawId":"123123",
    }
}
Response

Name	Enum	Description
withdrawId	String	Withdraw record id.
Asset Transfer
Description

Transfer assets between different asset areas.
Method

/private/submit_transfer
Request example

{ 
    "jsonrpc":"2.0",
    "id": 1,
    "method": "/private/submit_transfer",
     "params":{
        "coin_type":"ETH",
        "amount":"100",
        "from":"ETH",
        "to":"BTC"
     }
}
Parameters

Parameter	Required	Type	Enum	Description
coin_type	true	string		Coin type, i.e BTC
amount	true	Number		Amount
from	true	String	WALLET,SPOT,PERPETUAL	Source asset area.
to	true	String	WALLET,SPOT,PERPETUAL	Target asset area.
The above command returns JSON structured like this (real example)

 {
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1588745860741,
    "usOut": 1588745860991,
    "usDiff": 250,
    "result": "ok"
}
Response

Name	Type	Enum	Description
result	string		
Sub account Transfer
Description

Transfer funding assets between sub-account.
Sub-account can only transfer amount to main account.
Main-account can transfer amount between sub-account and sub-account , or between sub-account and main-account;
Method

/private/submit_transfer_between_subaccounts
Request example

{
    "id": "44",
    "method": "/private/submit_transfer_between_subaccounts",
    "params":
    {
        "sourceUid": "112505737061994496",
        "destinationUid": "108265251",
        "coinType": "USDT",
        "amount": "100"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
coin_type	true	string		Coin type, i.e BTC
amount	true	Number		Amount
sourceUid	true	Long		Source account uid.
destinationUid	true	Long		Target account uid.
The above command returns JSON structured like this (real example)

{
    "id": "44",
    "jsonrpc": "2.0",
    "usIn": 1675759149996,
    "usOut": 1675759150013,
    "usDiff": 17,
    "result": "ok"
}
Response

Name	Type	Enum	Description
result	string		
Trading
Buy
Description

Places a buy order for an instrument.
Asynchronous operation only means that the request is received. The specific order status can be obtained by subscribing or querying the order status.
Method

/private/buy
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/buy",
  "params": {
    "amount": "1",
    "type": "limit",
    "advanced": "iv",
    "reduce_only": false,
    "post_only": false,
    "time_in_force": "good_til_cancelled",
    "instrument_name": "BTC-USDT-PERPETUAL",
    "price": "90"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	String		Instrument name. eg: BTC-USDT-SPOT,BTC-USDT-PERPETAUL。
amount	true	number		Quantity at time of order
type	false	String	limit, market	The order type, default: limit.
price	false	number		The order price for limit order.
time_in_force	false	String	good_til_cancelled, fill_or_kill, immediate_or_cancel	Specifies how long the order remains in effect, default: good_til_cancelled.
post_only	false	Boolen		If true, the order is considered post-only, default: false.
reduce_only	false	Boolen		If true, the order is considered reduce-only which is intended to only reduce a current position. default: false.(Only for perpetuals).
condition_type	false	String	NORMAL, STOP, TRAILING, IF_TOUCHED	Condition sheet policy, the default is NORMAL.(Only for perpetuals).
trigger_price	false	Number		Trigger price. Available when condition_type is STOP or IF_TOUCHED. (Only for perpetuals).
trigger_price_type	false	Number		Trigger price type. 1 : mark_price, 2: last_price. (Only for perpetuals).
trail_price	false	Number		Tracking price change Delta. Available when condition_type is TRAILING. (Only for perpetuals).
market_amount_order	fasle	Boolen		Advanced order amount type, default: false. If set to true，then the amount field means USDT value. (Only for perpetuals)
stop_loss_price	false	Number		Stop loss price. (Only for perpetuals).
take_profit_price	false	Number		Take profit price. (Only for perpetuals).
stop_loss_type	false	Number		Stop loss price type. 1 : mark_price, 2: last_price. (Only for perpetuals).
take_profit_type	false	Number		Take profit price type. 1 : mark_price, 2: last_price. (Only for perpetuals).
position_side	true	String	BOTH,LONG,SHORT	Position Side. Default: BOTH.BOHT for One-way Mode. LONG and SHORT for Hedge mode.(Only for perpetuals).
custom_order_id	false	String		Client order id. Can only be string following the rule: ^[\.A-Z\:/a-z0-9_-]{1,36}$. Returned when querying an order .
The above command returns JSON structured like this (real example)

  {
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1590387640408,
    "usOut": 1590387641134,
    "usDiff": 726,
    "result": {
        "order": {
            "order_id": "77409325612535808"
        }
    }
}
Response

Name	Type	Enum	Description
result	object		Response data
› order	object		
›› order_id	string		order id
Sell
Description

Places a sell order for an instrument.
Asynchronous operation only means that the request is received. The specific order status can be obtained by subscribing or querying the order status.
Method

/private/sell
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/sell",
  "params": {
    "amount": "1",
    "type": "limit",
    "reduce_only": false,
    "post_only": false,
    "time_in_force": "good_til_cancelled",
    "instrument_name": "BTC-USDT-PERPETUAL",
    "price": "90"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	String		Instrument name. eg: BTC-USDT-SPOT,BTC-USDT-PERPETAUL。
amount	true	number		Quantity at time of order
type	false	String	limit, market	The order type, default: limit.
price	false	number		The order price for limit order.
time_in_force	false	String	good_til_cancelled, fill_or_kill, immediate_or_cancel	Specifies how long the order remains in effect, default: good_til_cancelled.
post_only	false	Boolen		If true, the order is considered post-only, default: false.
reduce_only	false	Boolen		If true, the order is considered reduce-only which is intended to only reduce a current position. default: false.(Only for perpetuals).
condition_type	false	String	NORMAL, STOP, TRAILING, IF_TOUCHED	Condition sheet policy, the default is NORMAL.(Only for perpetuals).
trigger_price	false	Number		Trigger price. Available when condition_type is STOP or IF_TOUCHED. (Only for perpetuals).
trigger_price_type	false	Number		Trigger price type. 1 : mark_price, 2: last_price. (Only for perpetuals).
trail_price	false	Number		Tracking price change Delta. Available when condition_type is TRAILING. (Only for perpetuals).
market_amount_order	fasle	Boolen		Advanced order amount type, default: false. If set to true，then the amount field means USDT value. (Only for perpetuals)
stop_loss_price	false	Number		Stop loss price. (Only for perpetuals).
take_profit_price	false	Number		Take profit price. (Only for perpetuals).
stop_loss_type	false	Number		Stop loss price type. 1 : mark_price, 2: last_price. (Only for perpetuals).
take_profit_type	false	Number		Take profit price type. 1 : mark_price, 2: last_price. (Only for perpetuals).
position_side	true	String	BOTH,LONG,SHORT	Position Side. Default: BOTH.BOHT for One-way Mode. LONG and SHORT for Hedge mode.(Only for perpetuals).
custom_order_id	false	String		Client order id. Can only be string following the rule: ^[\.A-Z\:/a-z0-9_-]{1,36}$. Returned when querying an order .
The above command returns JSON structured like this (real example)

  {
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1590387640408,
    "usOut": 1590387641134,
    "usDiff": 726,
    "result": {
        "order": {
            "order_id": "77409325612535808"
        }
    }
}
Response

Name	Type	Enum	Description
result	object		Response data
› order	object		
›› order_id	string		The order id.
Cancel by Id
Description

Cancel an order, specified by order id.
Asynchronous operation only means that the request is received. The specific order status can be obtained by subscribing or querying the order status.
Method

/private/cancel
Request example

{
  "jsonrpc": "2.0",
  "id": "3558",
  "method": "/private/cancel",
  "params": {
    "order_id": "77409325612535808"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
order_id	true	string		The order id.
The above command returns JSON structured like this (real example)

{
  "id": "3558",
  "jsonrpc": "2.0",
  "usIn": 1606288516328,
  "usOut": 1606288516343,
  "usDiff": 15,
  "result": {
    "order_id": "77409325612535808"
  }
}
Response

Name	Type	Enum	Description
result	object		
› order_id	string		The order id.
Cancel By Currency
Description

Cancel the order according to the trading area.
Asynchronous operation only means that the request is received. The specific order status can be obtained by subscribing or querying the order status.
Method

/private/cancel_all_by_currency
Request example

{
  "jsonrpc":"2.0",
  "id":"3558",
  "method":"/private/cancel_all_by_currency",
  "params":{
    "currency":"BTC"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
currrency	true	string	BTC, ETH, SPOT, PERPETUAL	The trading area.
kind	false	string	option, future, spot, margin, perpetual	The order kind.
The above command returns JSON structured like this (real example)

{
  "id":"3558",
  "jsonrpc":"2.0",
  "usIn":1606290888816,
  "usOut":1606290888830,
  "usDiff":14,
  "result":1
}
Response

Name	Type	Enum	Description
result	number		Number of cancelled orders.
Cancel By Instrument
Description

Cancels all orders by instrument.
Asynchronous operation only means that the request is received. The specific order status can be obtained by subscribing or querying the order status.
Method

/private/cancel_all_by_instrument
Request example

{
  "jsonrpc":"2.0",
  "id":"3558",
  "method":"/private/cancel_all_by_instrument",
  "params":{
    "instrument_name":"BTC-USDT-SPOT"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name. eg: BTC-USDT-SPOT,BTC-USDT-MARGIN,BTC-06JUN20,BTC-06JUN20-10000-C,BTC-USDT-PERPETAUL.
The above command returns JSON structured like this (real example)

{
  "id":"3558",
  "jsonrpc":"2.0",
  "usIn":1606290888816,
  "usOut":1606290888830,
  "usDiff":14,
  "result":1
}
Response

Name	Type	Enum	Description
result	number		Number of orders being cancelled.
Get positions
Description

Get the positions according to the trading area.
Only support for perpetuals, options and futures.
Method

/private/get_positions
Request example

 { 
    "jsonrpc":"2.0",
    "id": 1,
    "method": "/private/get_positions",
     "params":{
        "currency":"BTC",
        "kind": "option"
     }
}
Parameters

Parameter	Required	Type	Enum	Description
currrency	true	string	BTC, ETH, PERPETUAL	The trading area.
kind	false	string	option, future, spot, margin,perpetual	The order kind.
The above command returns JSON structured like this (real example)

{
  "id": "18",
  "jsonrpc": "2.0",
  "usIn": 1625563460761,
  "usOut": 1625563460770,
  "usDiff": 9,
  "result": [
    {
      "average_price": "33961.89",
      "delta": "-11.88",
      "direction": "sell",
      "floating_profit_loss": "-7711.98",
      "instrument_name": "BTC-24SEP21",
      "kind": "future",
      "currency": "BTC",
      "mark_price": "34611.05",
      "realized_profit_loss": "-11460.52",
      "size": "-11.88",
      "session_price": "33961.89",
      "total_profit_loss": "-7711.98",
      "vega": "0",
      "gamma": "0",
      "theta": "0",
      "zero_margin_size": "0",
      "version": "2091"
    }
  ]
}
Response

Name	Type	Enum	Description
result			
› pos_id	number		The position id.
› currency	string		The trading area.
› instrument_name	string		Instrument name.
› kind	string		The order kind.
› average_price	number		Average price of trades that built this position.
› size	number		Position size.
› direction	string	buy, sell	Direction
› leverage	number		Current available leverage for future position.
› mark_price	number		Current mark price for position's instrument.
› index_price	number		Current index price
› initial_margin	number		Initial margin
› maintenance_margin	number		Maintenance margin
› total_profit_loss	number		Profit or loss from position
› floating_profit_loss	number		floating profit or loss
› realized_profit_loss	number		Realized profit or loss
› total_rpl	number		Total floating profit or loss.
› delta	number		Only for options, Delta parameter
› version	number		Version
› variable_funds	number		Variable funds.
› liquid_price	number		Liquid price.
› margin	number		Margin.
› margin_balance	number		Margin balance.
› margin_balance_isolated	number		Margin balance of isolated.
› wallet_balance_isolated	number		Wallet balance of isolated.
› risk_level	number		Risk Level. The risk of margin is between 0% and 100%, the higher the value, the higher the risk of compulsory closing.
› roe	number		roe
› available_withdraw_funds	number		Transferable quantity
› margin_type	string	cross,isolated	Position margin type.
› stop_loss_price	number		Stop loss price. If the value is 0, it means not set.
› stop_loss_type	number		Stop loss price type.
› take_profit_price	number		Take profit price. If the value is 0, it means not set.
› take_profit_type	number		Take profit price type.
› traceType	number	0,1,2	Trace type. Only for perpetuals. 0: normal,1: trace trader, 2: trace follower
Close position
Description

Close the specified position.
Only support for perpetuals.
Method

/private/close_position
Request example

{
  "jsonrpc":"2.0",
  "id": "1662",
  "method": "/private/close_position",
  "params": {
    "instrument_name": "BTC-27NOV20-15000-C",
    "type": "limit",
    "price": "4500",
    "advanced": "usd"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name.
type	true	string	limit, market	The order type.
price	false	number		The order price for limit order.
amount	true	number		Quantity at time of order
pos_id	false	number		Position id. Support for perpetual multi position. Default: 0.
The above command returns JSON structured like this (real example)

{
  "id": "1662",
  "jsonrpc": "2.0",
  "usIn": 1606292314448,
  "usOut": 1606292314470,
  "usDiff": 22,
  "result": {
    "order": {
      "order_id": "77434881699745792"
    }
  }
}
Response

Response

Name	Type	Enum	Description
result	object		
› order	object		
›› order_id	string		The order id.
Get open order by Currency
Description

Get the open orders according to the trading area.
Method

/private/get_open_orders_by_currency
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/private/get_open_orders_by_currency",
    "params":{
        "currency":"SPOT"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
currency	true	string	BTC , ETH, SPOT, PERPETUAL	The trading area.
kind	false	string	margin, spot, option, future, perpetual	The order kind.
type	false	string	limit, market	The order type.
The above command returns JSON structured like this (real example)

{
  "id": "26",
  "jsonrpc": "2.0",
  "usIn": 1650524774836,
  "usOut": 1650524774939,
  "usDiff": 103,
  "result":
  [
    {
      "kind": "perpetual",
      "direction": "buy",
      "amount": "0.1",
      "price": "3020",
      "advanced": "usdt",
      "source": "api",
      "mmp": false,
      "version": 1,
      "order_id": "262959243277852672",
      "order_state": "open",
      "instrument_name": "ETH-USDT-PERPETUAL",
      "filled_amount": "0",
      "average_price": "0",
      "order_type": "limit",
      "time_in_force": "GTC",
      "post_only": false,
      "reduce_only": false,
      "condition_type": "NORMAL",
      "trigger_touch": false,
      "stop_loss_price": "0",
      "stop_loss_type": 1,
      "take_profit_price": "0",
      "take_profit_type": 1,
      "creation_timestamp": 1650524769151,
      "last_update_timestamp": 1650524769158
    }
  ]
}
Response

Name	Type	Enum	Description
result	array of object		
› order_id	string		The order id.
› order_state	string	open, filled, cancelled	The order state.
› instrument_name	string		Instrument name
› currency	string		The trading area.
› kind	string	option, future, spot, margin	The order kind.
› direction	string	buy, sell	The order direction.
› amount	Number		Order quantity.
› price	Number		The order price.
› filled_amount	Number		Filled amount of the order.
› average_price	Number		Average fill price of the order.
› iv	Number		Implied volatility in percent.For example, price=100, means implied volatility of 100%.
› advanced	string	usdt,iv	Advanced option order type, (Only for options).
› order_type	string	limit, market	The order type.
› time_in_force	string	good_til_cancelled, good_til_date, fill_or_kill, immediate_or_cancel	Specifies how long the order remains in effect.
› post_only	boolean		true for post-only orders only
› reduce_only	boolean		true for reduce-only orders only
› condition_type	String	NORMAL, STOP, TRAILING, IF_TOUCHED	Condition sheet policy, the default is NORMAL. Available when kind is future
› trigger_price	Number		Trigger price. Available when condition_type is STOP or IF_TOUCHED.
› trail_price	Number		Tracking price change Delta. Available when condition_type is TRAILING.
› creation_timestamp	string		Create time.
› last_update_timestamp	string		Last update time.
› version	Number		Order version.
› stop_loss_price	Number		Stop loss price. If the value is 0, it means not set.
› stop_loss_type	Number		Stop loss price type.
› take_profit_price	Number		Take profit price. If the value is 0, it means not set.
› take_profit_type	Number		Take profit price type.
› custom_order_id	String		Client order id.
Get open order by Instrument
Description

Get all open orders by instrument.
Method

/private/get_open_orders_by_instrument
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/private/get_open_orders_by_instrument",
    "params":{
        "instrument_name":"ETH-USDT-PERPETUAL"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name. eg: BTC-USDT-SPOT,BTC-USDT-MARGIN,BTC-06JUN20,BTC-06JUN20-10000-C,BTC-USDT-PERPETAUL。
type	false	string	limit, market	The order type.
The above command returns JSON structured like this (real example)

{
  "id": "26",
  "jsonrpc": "2.0",
  "usIn": 1650524774836,
  "usOut": 1650524774939,
  "usDiff": 103,
  "result":
  [
    {
      "kind": "perpetual",
      "direction": "buy",
      "amount": "0.1",
      "price": "3020",
      "advanced": "usdt",
      "source": "api",
      "mmp": false,
      "version": 1,
      "order_id": "262959243277852672",
      "order_state": "open",
      "instrument_name": "ETH-USDT-PERPETUAL",
      "filled_amount": "0",
      "average_price": "0",
      "order_type": "limit",
      "time_in_force": "GTC",
      "post_only": false,
      "reduce_only": false,
      "condition_type": "NORMAL",
      "trigger_touch": false,
      "stop_loss_price": "0",
      "stop_loss_type": 1,
      "take_profit_price": "0",
      "take_profit_type": 1,
      "creation_timestamp": 1650524769151,
      "last_update_timestamp": 1650524769158
    }
  ]
}
Response

Name	Type	Enum	Description
result	array of object		
› order_id	string		The order id.
› order_state	string	open, filled, cancelled	The order state.
› instrument_name	string		Instrument name
› currency	string		The trading area.
› kind	string	option, future, spot, margin	The order kind.
› direction	string	buy, sell	The order direction.
› amount	Number		Order quantity.
› price	Number		The order price.
› filled_amount	Number		Filled amount of the order.
› average_price	Number		Average fill price of the order.
› iv	Number		Implied volatility in percent.For example, price=100, means implied volatility of 100%.
› advanced	string	usdt,iv	Advanced option order type, (Only for options).
› order_type	string	limit, market	The order type.
› time_in_force	string	good_til_cancelled, good_til_date, fill_or_kill, immediate_or_cancel	Specifies how long the order remains in effect.
› post_only	boolean		true for post-only orders only
› reduce_only	boolean		true for reduce-only orders only
› condition_type	String	NORMAL, STOP, TRAILING, IF_TOUCHED	Condition sheet policy, the default is NORMAL. Available when kind is future
› trigger_price	Number		Trigger price. Available when condition_type is STOP or IF_TOUCHED.
› trail_price	Number		Tracking price change Delta. Available when condition_type is TRAILING.
› creation_timestamp	string		Create time.
› last_update_timestamp	string		Last update time.
› version	Number		Order version.
› stop_loss_price	Number		Stop loss price. If the value is 0, it means not set.
› stop_loss_type	Number		Stop loss price type.
› take_profit_price	Number		Take profit price. If the value is 0, it means not set.
› take_profit_type	Number		Take profit price type.
› custom_order_id	String		Client order id.
Get order history by Currency
Description

Get all complete orders by trading area.
Method

/private/get_order_history_by_currency
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/private/get_order_history_by_currency",
    "params":{
        "currency":"SPOT"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
currency	true	string	BTC ETH SPOT,BTC-USDT-PERPETAUL	The trading area.
kind	false	string	margin,spot,option,future, perpetual	The order type.
count	false	integer		Number of requested items, default - 20.
offset	false	integer		The default is 0. For example, if you query the second page and the quantity is 100, set offset = 100 and count = 100
The above command returns JSON structured like this (real example)

{
  "id": "230",
  "jsonrpc": "2.0",
  "usIn": 1650525112489,
  "usOut": 1650525112618,
  "usDiff": 129,
  "result":
  [
    {
      "currency": "PERPETUAL",
      "kind": "perpetual",
      "direction": "buy",
      "amount": "0.1",
      "price": "3020",
      "advanced": "usdt",
      "source": "api",
      "mmp": false,
      "version": 1,
      "order_id": "262959142199320576",
      "order_state": "canceled",
      "instrument_name": "ETH-USDT-PERPETUAL",
      "filled_amount": "0",
      "average_price": "0",
      "order_type": "limit",
      "time_in_force": "FOK",
      "post_only": false,
      "reduce_only": false,
      "condition_type": "NORMAL",
      "trigger_touch": false,
      "stop_loss_price": "0",
      "stop_loss_type": 1,
      "take_profit_price": "0",
      "take_profit_type": 1,
      "creation_timestamp": 1650524745053,
      "last_update_timestamp": 1650524745055
    }
  ]
}
Response

Name	Type	Enum	Description
result	array of object		
› order_id	string		The order id.
› order_state	string	open, filled, cancelled	The order state.
› instrument_name	string		Instrument name
› currency	string		The trading area.
› kind	string	option, future, spot, margin, perpetual	The order kind.
› direction	string	buy, sell	The order direction.
› amount	Number		Order quantity.
› price	Number		The order price.
› filled_amount	Number		Filled amount of the order.
› average_price	Number		Average fill price of the order.
› iv	Number		Implied volatility in percent.For example, price=100, means implied volatility of 100%.
› advanced	string	usdt,iv	Advanced option order type, (Only for options).
› order_type	string	limit, market	The order type.
› time_in_force	string	good_til_cancelled, good_til_date, fill_or_kill, immediate_or_cancel	Specifies how long the order remains in effect.
› post_only	boolean		true for post-only orders only
› reduce_only	boolean		true for reduce-only orders only
› condition_type	String	NORMAL, STOP, TRAILING, IF_TOUCHED	Condition sheet policy, the default is NORMAL. Available when kind is future
› trigger_price	Number		Trigger price. Available when condition_type is STOP or IF_TOUCHED.
› trail_price	Number		Tracking price change Delta. Available when condition_type is TRAILING.
› creation_timestamp	string		Create time.
› last_update_timestamp	string		Last update time.
› version	Number		Order version.
› stop_loss_price	Number		Stop loss price. If the value is 0, it means not set.
› stop_loss_type	Number		Stop loss price type.
› take_profit_price	Number		Take profit price. If the value is 0, it means not set.
› take_profit_type	Number		Take profit price type.
› custom_order_id	String		Client order id.
Get order history by Instrument
Description

Get all complete orders by instrument.
Method

/private/get_order_history_by_instrument
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/private/get_order_history_by_instrument",
    "params":{
        "instrument_name":"BTC-USD-SPOT",
        "count": 100
    }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name.
count	false	integer		Number of requested items, default - 20.
offset	false	integer		The default is 0. For example, if you query the second page and the quantity is 100, set offset = 100 and count = 100
The above command returns JSON structured like this (real example)

{
  "id":"1",
  "jsonrpc":"2.0",
  "usIn":1606296586819,
  "usOut":1606296586826,
  "usDiff":7,
  "result":[
    {
      "amount":"1",
      "advanced":"iv",
      "price":"12.00",
      "iv":"100",
      "direction":"buy",
      "version":6,
      "kind":"option",
      "currency":"BTC",
      "order_state":"open",
      "instrument_name":"BTC-27NOV20-22500-C",
      "time_in_force":"GTC",
      "last_update_timestamp":1606294066790,
      "filled_amount":"0",
      "average_price":"0.00",
      "order_id":"77442231437365248",
      "creation_timestamp":1606294066781,
      "order_type":"limit"
    },
    {
      "amount":"1",
      "advanced":"usdt",
      "price":"19000.00",
      "direction":"buy",
      "version":0,
      "kind":"future",
      "currency":"BTC",
      "order_state":"open",
      "instrument_name":"BTC-25DEC20",
      "time_in_force":"GTC",
      "last_update_timestamp":1606293747678,
      "filled_amount":"0",
      "average_price":"0.00",
      "order_id":"77440893005598720",
      "creation_timestamp":1606293747674,
      "order_type":"limit"
    }
  ]
}
Response

Name	Type	Enum	Description
result	array of object		
› order_id	string		The order id.
› order_state	string	open, filled, cancelled	The order state.
› instrument_name	string		Instrument name
› currency	string		The trading area.
› kind	string	option, future, spot, margin, perpetual	The order kind.
› direction	string	buy, sell	The order direction.
› amount	Number		Order quantity.
› price	Number		The order price.
› filled_amount	Number		Filled amount of the order.
› average_price	Number		Average fill price of the order.
› iv	Number		Implied volatility in percent.For example, price=100, means implied volatility of 100%.
› advanced	string	usdt,iv	Advanced option order type, (Only for options).
› order_type	string	limit, market	The order type.
› time_in_force	string	good_til_cancelled, good_til_date, fill_or_kill, immediate_or_cancel	Specifies how long the order remains in effect.
› post_only	boolean		true for post-only orders only
› reduce_only	boolean		true for reduce-only orders only
› condition_type	String	NORMAL, STOP, TRAILING, IF_TOUCHED	Condition sheet policy, the default is NORMAL. Available when kind is future
› trigger_price	Number		Trigger price. Available when condition_type is STOP or IF_TOUCHED.
› trail_price	Number		Tracking price change Delta. Available when condition_type is TRAILING.
› creation_timestamp	string		Create time.
› last_update_timestamp	string		Last update time.
› version	Number		Order version.
› stop_loss_price	Number		Stop loss price. If the value is 0, it means not set.
› stop_loss_type	Number		Stop loss price type.
› take_profit_price	Number		Take profit price. If the value is 0, it means not set.
› take_profit_type	Number		Take profit price type.
› custom_order_id	String		Client order id.
Get order state
Description

Get the order by id。
Method

/private/get_order_state
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/private/get_order_state",
    "params":{
        "order_id":"77451602670129152"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
order_id	true	string		The order id.
The above command returns JSON structured like this (real example)

{
  "id": "1",
  "jsonrpc": "2.0",
  "usIn": 1650525411885,
  "usOut": 1650525411902,
  "usDiff": 17,
  "result":
  {
    "currency": "PERPETUAL",
    "kind": "perpetual",
    "direction": "buy",
    "amount": "0.1",
    "price": "3020",
    "advanced": "usdt",
    "source": "api",
    "mmp": false,
    "version": 1,
    "order_id": "262959142199320576",
    "order_state": "canceled",
    "instrument_name": "ETH-USDT-PERPETUAL",
    "filled_amount": "0",
    "average_price": "0",
    "order_type": "limit",
    "time_in_force": "FOK",
    "post_only": false,
    "reduce_only": false,
    "condition_type": "NORMAL",
    "trigger_touch": false,
    "stop_loss_price": "0",
    "stop_loss_type": 1,
    "take_profit_price": "0",
    "take_profit_type": 1,
    "creation_timestamp": 1650524745053,
    "last_update_timestamp": 1650524745055
  }
}
Response

Name	Type	Enum	Description
result	array of object		
› order_id	string		The order id.
› order_state	string	open, filled, rejected, cancelled	The order state.
› instrument_name	string		Instrument name
› currency	string		The trading area.
› kind	string	option, future, spot, margin, perpetual	The order kind.
› direction	string	buy, sell	The order direction.
› amount	Number		Order quantity.
› price	Number		The order price.
› filled_amount	Number		Filled amount of the order.
› average_price	Number		Average fill price of the order.
› iv	Number		Implied volatility in percent.For example, price=100, means implied volatility of 100%.
› advanced	string	usdt,iv	Advanced option order type, (Only for options).
› order_type	string	limit, market	The order type.
› time_in_force	string	good_til_cancelled, good_til_date, fill_or_kill, immediate_or_cancel	Specifies how long the order remains in effect.
› post_only	boolean		true for post-only orders only
› reduce_only	boolean		true for reduce-only orders only
› condition_type	String	NORMAL, STOP, TRAILING, IF_TOUCHED	Condition sheet policy, the default is NORMAL. Available when kind is future
› trigger_price	Number		Trigger price. Available when condition_type is STOP or IF_TOUCHED.
› trail_price	Number		Tracking price change Delta. Available when condition_type is TRAILING.
› creation_timestamp	string		Create time.
› last_update_timestamp	string		Last update time.
› version	Number		Order version.
› stop_loss_price	Number		Stop loss price. If the value is 0, it means not set.
› stop_loss_type	Number		Stop loss price type.
› take_profit_price	Number		Take profit price. If the value is 0, it means not set.
› take_profit_type	Number		Take profit price type.
› custom_order_id	String		Client order id.
Get user trades by Currency
Description

Get user trades within given trading area.
Method

/private/get_user_trades_by_currency
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/private/get_user_trades_by_currency",
    "params":{
        "currency":"BTC"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
currency	true	string	BTC ETH SPOT, PERPETUAL	The trading area.
kind	false	string	margin,spot,option,future, perpetual	The order kind.
start_id	false	Number		The ID number of the first trade to be returned.
end_id	false	Number		The ID number of the last trade to be returned.
start_timestamp	false	Date		The trade time of the first trade to be returned.
end_timestamp	false	Date		The trade time of the last trade to be returned.
count	false	Number		Number of requested items, default - 20.
self_trade	false	boolean		If not set, query all.
sorting	false	string	asc desc	Direction of results sorting,default: desc.
The above command returns JSON structured like this (real example)

{
  "id": "1",
  "jsonrpc": "2.0",
  "usIn": 1650527520866,
  "usOut": 1650527520922,
  "usDiff": 56,
  "result": {
    "count": 3,
    "trades": [
      {
        "direction": "buy",
        "amount": "0.01",
        "price": "44000",
        "fee": "0.22",
        "timestamp": 1649909632028,
        "role": "taker",
        "trade_id": "19014109",
        "order_id": "260379171103793152",
        "instrument_name": "BTC-USDT-PERPETUAL",
        "order_type": "limit",
        "fee_use_coupon": false,
        "fee_coin_type": "USDT",
        "index_price": "0",
        "mark_price": "43999.95",
        "self_trade": false
      }
    ],
    "has_more": true
  }
}
Response

Parameter	Type	Enum	Description
result	object		
› has_more	boolean		
› trades	array of object		
›› amount	Number		Quantity of transactions
›› direction	string	buy, sell	The order direction.
›› fee	Number		User's fee in units of the specified fee_currency
›› fee_coin_type	string		The fee currency.
›› fee_use_coupon	boolean		Identifies whether the handling fee uses a coupon.
›› mark_price	Number		Mark Price at the moment of trade
›› instrument_name	string		Instrument name.
›› order_id	string		The order id.
›› order_type	string	limit,market	The order type
›› trade_id	string		Unique (per currency) trade identifier
›› price	Number		Price.
›› role	string	taker,maker	Role.
›› self_trade	Boolean		Indicates whether it is a self-transaction.
Get user trades by Instrument
Description

Get user trades within given instrument.
Method

/private/get_user_trades_by_instrument
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/private/get_user_trades_by_instrument",
    "params":{
        "instrument_name":"BTC-27NOV20-18500-C"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name. eg: BTC-USDT-SPOT,BTC-USDT-MARGIN,BTC-JUN0620,BTC-JUN0620-10000-C,BTC-USDT-PERPETAUL。
start_id	false	Number		The ID number of the first trade to be returned.
end_id	false	Number		The ID number of the last trade to be returned.
start_timestamp	false	Date		The trade time of the first trade to be returned.
end_timestamp	false	Date		The trade time of the last trade to be returned.
count	false	Number		Number of requested items, default - 20
self_trade	false	boolean		If not set, query all.
sorting	false	string	asc desc	Direction of results sorting,default: desc.
The above command returns JSON structured like this (real example)

{
  "id": "1",
  "jsonrpc": "2.0",
  "usIn": 1650527520866,
  "usOut": 1650527520922,
  "usDiff": 56,
  "result": {
    "count": 3,
    "trades": [
      {
        "direction": "buy",
        "amount": "0.01",
        "price": "44000",
        "fee": "0.22",
        "timestamp": 1649909632028,
        "role": "taker",
        "trade_id": "19014109",
        "order_id": "260379171103793152",
        "instrument_name": "BTC-USDT-PERPETUAL",
        "order_type": "limit",
        "fee_use_coupon": false,
        "fee_coin_type": "USDT",
        "index_price": "0",
        "mark_price": "43999.95",
        "self_trade": false
      }
    ],
    "has_more": true
  }
}
Response

Parameter	Type	Enum	Description
result	object		
› has_more	boolean		
› trades	array of object		
›› amount	Number		Quantity of transactions
›› direction	string	buy, sell	The order direction.
›› fee	Number		User's fee in units of the specified fee_currency
›› fee_coin_type	string		The fee currency.
›› fee_use_coupon	boolean		Identifies whether the handling fee uses a coupon.
›› mark_price	Number		Mark Price at the moment of trade
›› instrument_name	string		Instrument name.
›› order_id	string		The order id.
›› order_type	string	limit,market	The order type
›› trade_id	string		Unique (per currency) trade identifier
›› price	Number		Price.
›› role	string	taker,maker	Role.
›› self_trade	Boolean		Indicates whether it is a self-transaction.
Get user trades by Order
Description

Get user trades within given order id.
Method

/private/get_user_trades_by_order
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/private/get_user_trades_by_order",
    "params":{
        "order_id":"77770294733836288"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
order_id	true	string		The order id.
start_id	false	Number		The ID number of the first trade to be returned.
end_id	false	Number		The ID number of the last trade to be returned.
count	false	Number		Number of requested items, default - 20
sorting	false	string	asc desc	Direction of results sorting,default: desc.
The above command returns JSON structured like this (real example)

{
  "id": "1",
  "jsonrpc": "2.0",
  "usIn": 1650527520866,
  "usOut": 1650527520922,
  "usDiff": 56,
  "result": {
    "count": 3,
    "trades": [
      {
        "direction": "buy",
        "amount": "0.01",
        "price": "44000",
        "fee": "0.22",
        "timestamp": 1649909632028,
        "role": "taker",
        "trade_id": "19014109",
        "order_id": "260379171103793152",
        "instrument_name": "BTC-USDT-PERPETUAL",
        "order_type": "limit",
        "fee_use_coupon": false,
        "fee_coin_type": "USDT",
        "index_price": "0",
        "mark_price": "43999.95",
        "self_trade": false
      }
    ],
    "has_more": true
  }
}
Response

Parameter	Type	Enum	Description
result	object		
› has_more	boolean		
› trades	array of object		
›› amount	Number		Quantity of transactions
›› direction	string	buy, sell	The order direction.
›› fee	Number		User's fee in units of the specified fee_currency
›› fee_coin_type	string		The fee currency.
›› fee_use_coupon	boolean		Identifies whether the handling fee uses a coupon.
›› mark_price	Number		Mark Price at the moment of trade
›› instrument_name	string		Instrument name.
›› order_id	string		The order id.
›› order_type	string	limit,market	The order type
›› trade_id	string		Unique (per currency) trade identifier
›› price	Number		Price.
›› role	string	taker,maker	Role.
›› self_trade	Boolean		Indicates whether it is a self-transaction.
Get perpetual instrument config
Description

Get perpetual instrument config.
Method

/private/get_perpetual_user_config
Request example

 { 
    "jsonrpc":"2.0",
    "id": 1,
    "method": "/private/get_perpetual_user_config",
     "params":{
        "instrument_name":"BTC-USDT-PERPETUAL"
     }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		The instrument name. eg: BTC-USDT-PERPETUAL
The above command returns JSON structured like this (real example)

{
    "id":"1",
    "jsonrpc":"2.0",
    "usIn":1590387640408,
    "usOut":1590387641134,
    "usDiff":726,
    "result":{
        "margin_type":"Cross",
        "leverage":"10"
    }
}
Response

Name	Type	Enum	Description
result			
› margin_type	string	cross,isolated	Position margin type.
› leverage	number		Current available leverage for future position.
Modify perpetual instrument margin type
Description

Modify perpetual instrument margin type.
It can only be modified when the specified instrument has no orders and positions
Method

/private/adjust_perpetual_margin_type
Request example

 { 
    "jsonrpc":"2.0",
    "id": 1,
    "method": "/private/adjust_perpetual_margin_type",
     "params":{
        "instrument_name":"BTC-USDT-PERPETUAL",
      "margin_type": "cross"
     }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		The instrument name. eg: BTC-USDT-PERPETUAL
margin_type	true	string	cross,isolate	Margin type.
The above command returns JSON structured like this (real example)

{
    "id":"1",
    "jsonrpc":"2.0",
    "usIn":1590387640408,
    "usOut":1590387641134,
    "usDiff":726,
    "result": "ok"
}
Response

Name	Type	Enum	Description
result	string		
Modify perpetual instrument leverage
Description

Modify perpetual instrument leverage.
Method

/private/adjust_perpetual_leverage
Request example

 { 
    "jsonrpc":"2.0",
    "id": 1,
    "method": "/private/adjust_perpetual_leverage",
     "params":{
        "instrument_name":"BTC-USDT-PERPETUAL",
      "leverage": "20"
     }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		The instrument name. eg: BTC-USDT-PERPETUAL
leverage	true	Number		Leverage number.
The above command returns JSON structured like this (real example)

{
    "id":"1",
    "jsonrpc":"2.0",
    "usIn":1590387640408,
    "usOut":1590387641134,
    "usDiff":726,
    "result": "ok"
}
Response

Name	Type	Enum	Description
result	string		
MarketData
Get order book
Description

Retrieves the order book, along with other market values for a given instrument.
Method

/public/get_order_book
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/public/get_order_book",
    "params":{
        "instrument_name":"BTC-USDT-PERPETUAL"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name. eg: BTC-USDT-SPOT,BTC-USDT-MARGIN,BTC-JUN0620,BTC-JUN0620-10000-C,BTC-USDT-PERPETUAL。
depth	false	Number		Orders depth quantity. Not defined or 0 = full order book. Depth = 100 means 100 for each bid/ask side.
The above command returns JSON structured like this (real example)

{
  "id":"1",
  "jsonrpc":"2.0",
  "usIn":1606443462144,
  "usOut":1606443462149,
  "usDiff":5,
  "result":{
    "asks":[
      [
        "17400.0000",
        "14.000"
      ],
      [
        "17405.0000",
        "19.000"
      ]
    ],
    "bids":[
      [
        "17398.0000",
        "19.000"
      ],
      [
        "17396.0000",
        "18.000"
      ]
    ],
    "timestamp":"1606443462147",
    "version":119365
  }
}
Response

Parameter	Type	Enum	Description
result	object		
› timestamp	string		timestamp.
› version	number		version number.
› asks	object array		List of asks.
›› price	number		price,array[0].
›› size	number		size,array[1].
› bids	object array		List of bids.
›› price	number		price,array[0].
›› size	number		size,array[1].
Get ticker
Description

Get ticker for an instrument.
Method

/public/tickers
Request example

{
  "id": "16",
  "method": "/public/tickers",
  "params": {
    "instrument_name": "BTC-25DEC20-19000-C"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name. eg: BTC-USDT-SPOT,BTC-USDT-MARGIN,BTC-JUN0620,BTC-JUN0620-10000-C。
The above command returns JSON structured like this (real example)

spot or margin:
{
  "id":"1",
  "jsonrpc":"2.0",
  "usIn":1606448923178,
  "usOut":1606448923182,
  "usDiff":4,
  "result":[
    {
      "best_ask_amount":"0.18259",
      "best_ask_price":"17207.11",
      "best_bid_amount":"0.13125",
      "best_bid_price":"17204.79",
      "instrument_name":"BTC-USDT",
      "last_price":"17205.952",
      "mark_price":"17204.71038253",
      "state":"open",
      "stats":{
        "high":"19000",
        "low":"16091.759",
        "price_change":"-0.0944",
        "volume":"340.64608000000000002"
      },
      "timestamp":"1606448922809"
    }
  ]
}

future:
{
  "id":"1",
  "jsonrpc":"2.0",
  "usIn":1606448900092,
  "usOut":1606448900096,
  "usDiff":4,
  "result":[
    {
      "best_ask_amount":"14",
      "best_ask_price":"17399",
      "best_bid_amount":"18",
      "best_bid_price":"17394",
      "instrument_name":"BTC-25DEC20",
      "last_price":"17400",
      "mark_price":"17394.0339",
      "max_price":"17394.0339",
      "min_price":"17394.0339",
      "open_interest":"1",
      "state":"open",
      "stats":{
        "high":"17828",
        "low":"16451",
        "price_change":"-0.0110",
        "volume":"88698"
      },
      "timestamp":"1606448900013",
      "underlying_price":"17220.8375"
    }
  ]
}

option:
{
  "id": "1",
  "jsonrpc": "2.0",
  "usIn": 1606448952855,
  "usOut": 1606448952863,
  "usDiff": 8,
  "result": [
    {
      "best_ask_amount": "684",
      "best_ask_price": "103",
      "best_bid_amount": "2",
      "best_bid_price": "77",
      "instrument_name": "BTC-27NOV20-16000-P",
      "last_price": "0.0001135878084784",
      "mark_price": "2.7668",
      "max_price": "2.7668",
      "min_price": "2.7668",
      "open_interest": "0",
      "state": "open",
      "stats": {
        "high": "0.0001135878084784",
        "low": "0.0001135878084784",
        "price_change": "0.0000"
      },
      "timestamp": "1606448948618",
      "underlying_price": "17391.199",
      "ask_iv": "363.09",
      "bid_iv": "329.4",
      "mark_iv": "186.66",
      "greeks": {
        "delta": "-0.0121"
      }
    }
  ]
}
Response

Parameter	Type	Enum	Description
result	object array		
› best_ask_amount	number		It represents the requested order size of all best asks
› best_ask_price	number		The current best ask price
› best_bid_amount	number		It represents the requested order size of all best bids
› best_bid_price	number		The current best bid price
› instrument_name	number		Unique instrument identifier
› last_price	number		The price for the last trade
› mark_price	number		The mark price for the instrument
› max_price	number		The maximum price for the instrument
› min_price	number		The minimum price for the instrument
› open_interest	number		The total amount of outstanding contracts in the corresponding amount units
› state	number	open, closed	The state of the order book.
› stats	object		24-hour
› › high	number		Highest price during 24h
› › low	number		Lowest price during 24h
› › price_change	number		24-hour price change expressed as a percentage
› timestamp	timestamp		The timestamp (milliseconds since the Unix epoch)
› underlying_price	number		Underlying price for implied volatility calculations
› ask_iv	number		(Only for option) implied volatility for best ask
› bid_iv	number		(Only for option) implied volatility for best bid
› greeks	object		Only for options
› › delta	number		(Only for option) The delta value for the option
Get instruments
Description

Retrieves available trading instruments.
Method

/public/get_instruments
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/public/get_instruments",
    "params":{
       "currency": "SPOT"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
currency	true	string	BTC ETH SPOT	The trading area.
kind	false	string	margin,spot,option,future	The order kind.
The above command returns JSON structured like this (real example)


BTC or ETH currency
{
  "id": "1",
  "jsonrpc": "2.0",
  "usIn": 1606458143935,
  "usOut": 1606458143946,
  "usDiff": 11,
  "result": [
    {
      "base_currency": "USD",
      "contract_size": "1",
      "creation_timestamp": "1606361968520",
      "expiration_timestamp": "1608883200000",
      "instrument_name": "BTC-25DEC20",
      "is_active": true,
      "kind": "future",
      "leverage": 0,
      "maker_commission": "0.02",
      "min_trade_amount": "1",
      "option_type": "init",
      "quote_currency": "USD",
      "settlement_period": "month",
      "strike": "0",
      "taker_commission": "0.05",
      "tick_size": "1",
      "instr_multiple": "0.01"
    },
    {
      "base_currency": "USD",
      "contract_size": "1",
      "creation_timestamp": "1606362245048",
      "expiration_timestamp": "1607068800000",
      "instrument_name": "BTC-04DEC20-16500-C",
      "is_active": true,
      "kind": "option",
      "leverage": 0,
      "maker_commission": "0.4",
      "min_trade_amount": "1",
      "option_type": "call",
      "quote_currency": "USD",
      "settlement_period": "week",
      "strike": "16500",
      "taker_commission": "0.4",
      "tick_size": "1",
      "instr_multiple": "0.1"
    }
  ]
}
SPOT currency:
{
  "id":"1",
  "jsonrpc":"2.0",
  "usIn":1606458245947,
  "usOut":1606458245957,
  "usDiff":10,
  "result":[
    {
      "base_currency":"USDT",
      "contract_size":"0",
      "creation_timestamp":"1606361432728",
      "expiration_timestamp":"2114352000000",
      "instrument_name":"BTC-USDT-SPOT",
      "is_active":true,
      "kind":"spot",
      "leverage":0,
      "maker_commission":"0.001",
      "min_trade_amount":"0.00001",
      "option_type":"init",
      "quote_currency":"BTC",
      "strike":"0",
      "taker_commission":"0.001",
      "tick_size":"0.001"
    },
    {
      "base_currency":"USDT",
      "contract_size":"0",
      "creation_timestamp":"1606361432728",
      "expiration_timestamp":"2114352000000",
      "instrument_name":"BTC-USDT-MARGIN",
      "is_active":true,
      "kind":"margin",
      "leverage":0,
      "maker_commission":"0.001",
      "min_trade_amount":"0.00001",
      "option_type":"init",
      "quote_currency":"BTC",
      "strike":"0",
      "taker_commission":"0.001",
      "tick_size":"0.001"
    }
  ]
}

Response

Parameter	Type	Enum	Description
result	object array		
› base_currency	string		The base currency.
› contract_size	number		Contract size for instrument
› creation_timestamp	string		The time when the instrument was first created (milliseconds)
› expiration_timestamp	string		The time when the instrument will expire (milliseconds)
› instrument_name	string		Instrument name.
› show_name	string		Show name.
› is_active	boolean		Indicates if the instrument can currently be traded.
› kind	string	margin,spot,option,future	The order kind.
› leverage	integer		Maximal leverage for instrument.
› maker_commission	number		Maker commission for instrument. Spot and margin trading areas collect the currency according to a certain proportion of the amount of the currency obtained, while derivative trading areas collect usdt according to a certain proportion of the transaction amount
› taker_commission	number		Taker commission for instrument. Spot and margin trading areas collect the currency according to a certain proportion of the amount of the currency obtained, while derivative trading areas collect usdt according to a certain proportion of the transaction amount
› min_trade_amount	number		Minimum amount step for trading.
› min_qty	number		Minimum amount for trading.
› min_notional	number		Minimum baseCurrency for trading.
› tick_size	Long		Specifies minimal price change and, as follows, the number of decimal places for instrument prices.
› option_type	string	call, put	The option type.
› settlement_period	string	day, week, month, season	The settlement period.
› strike	Long		The strike value. (only for options)
Get kbar
Description

Get TradingView candle chart.
You can only request the 1500 most recent candles; otherwise, you will receive error code 5221.
Access requires authorization.
Method

/private/get_tradingview_chart_data
Request example

{
    "jsonrpc":"2.0",
    "id":1,
    "method":"/private/get_tradingview_chart_data",
    "params":{
      "instrument_name": "BTC-USDT",
      "start_timestamp": "1632360798",
      "end_timestamp": "1632648858",
      "resolution": "5"
    }
}
Parameters

Parameter	Required	Type	Enum	Description
start_timestamp	true	string		The earliest timestamp to return result for (seconds since the UNIX epoch).
end_timestamp	true	string		The most recent timestamp to return result for (seconds since the UNIX epoch).
instrument_name	true	string		Instrument name.Specially in SPOT currency, use symbol, eg: BTC-USDT-SPOT or BTC-USDT-MARGIN use BTC-USDT
resolution	true	string	1 3 5 10 15 30 60 120 180 240 360 720 D	Chart bars resolution given in full minutes or keyword 1D (only some specific resolutions are supported)
The above command returns JSON structured like this (real example)


{
  "id": "345",
  "jsonrpc": "2.0",
  "usIn": 1632649373914,
  "usOut": 1632649373923,
  "usDiff": 9,
  "result": [
    {
      "tick": 1632152400,
      "open": "43736.300",
      "high": "43841.500",
      "low": "43715.800",
      "close": "43768.900",
      "volume": "18.0000",
      "cost": "788049.634"
    },
    {
      "tick": 1632152700,
      "open": "43760.800",
      "high": "43830.300",
      "low": "43758.600",
      "close": "43815.100",
      "volume": "18.1200",
      "cost": "793734.494"
    }
  ]
}

Response

Parameter	Type	Enum	Description
result	object array		
› close	number		The close price for the candle
› cost	number		Cost data for the candle
› high	number		The highest price level for the candle
› low	number		The lowest price level for the candle
› open	number		The open price for the candle'
› tick	integer		The timestamp (seconds since the Unix epoch)
› volume	number		Volume data for the candle
Public ping
Description

Public ping
Method

/public/ping
Request example

{ 
    "jsonrpc":"2.0",
    "id": 1,
    "method": "/public/ping",
     "params":{}
}
Parameters

The above command returns JSON structured like this (real example)

{
  "id": "16",
  "jsonrpc": "2.0",
  "usIn": 1664112105289,
  "usOut": 1664112105290,
  "result":
  {}
}
Response

Name	Type	Enum	Description
result	string		
SubscriptionManagement
To keep the websocket connection connected, please send messages regularly to maintain the heartbeat connection. We recommend sending a request every 5 seconds. You can send a "PING" string or call the /public/ping command.

Private subscribe
Description

Subscribe to one or more channels.
The name of the channel determines what information will be provided, and in what form.

Method

/private/subscribe
Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/private/subscribe",
  "params" : {
    "channels":[
      "trades.BTC-14AUG20.raw",
      "trades.BTC-14AUG20.raw"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
channels	true	array		A list of channels to subscribe to.
The above command returns JSON structured like this (real example)


{ 
  "jsonrpc":"2.0",
  "id": 1,
  "method": "/private/subscribe",
   "params":{
       "channels":[
           "trades.BTC-14AUG20.raw",
           "trades.BTC-14AUG20.raw"
       ]
   }
}
Response

Name	Type	Enum	Description
result	array of string		A list of subscribed channels.
Private unsubscribe
Description

Unsubscribe from one or more channels.
Method

/private/unsubscribe
Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/private/unsubscribe",
  "params" : {
    "channels":[
      "trades.BTC-14AUG20.raw",
      "trades.BTC-14AUG20.raw"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
channels	true	array		A list of channels to unsubscribe from.
The above command returns JSON structured like this (real example)


{ 
  "jsonrpc":"2.0",
  "id": 1,
  "method": "/private/unsubscribe",
   "params":{
       "channels":[
           "trades.BTC-14AUG20.raw",
           "trades.BTC-14AUG20.raw"
       ]
   }
}
Response

Name	Type	Enum	Description
result	array of string		A list of unsubscribed channels.
Public subscribe
Description

Subscribe to one or more channels.
The name of the channel determines what information will be provided, and in what form.

Method

/public/subscribe
Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/public/subscribe",
  "params" : {
    "channels":[
      "trades.BTC-14AUG20.raw",
      "trades.BTC-14AUG20.raw"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
channels	true	array		A list of channels to subscribe to.
The above command returns JSON structured like this (real example)


{ 
  "jsonrpc":"2.0",
  "id": 1,
  "method": "/public/subscribe",
   "params":{
       "channels":[
           "trades.BTC-14AUG20.raw",
           "trades.BTC-14AUG20.raw"
       ]
   }
}
Response

Name	Type	Enum	Description
result	array of string		A list of unsubscribed channels.
Public unsubscribe
Description

Unsubscribe from one or more channels.
Method

/public/unsubscribe
Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/public/unsubscribe",
  "params" : {
    "channels":[
      "trades.BTC-14AUG20.raw",
      "trades.BTC-14AUG20.raw"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
channels	true	array		A list of channels to unsubscribe from.
The above command returns JSON structured like this (real example)


{ 
  "jsonrpc":"2.0",
  "id": 1,
  "method": "/public/unsubscribe",
   "params":{
       "channels":[
           "trades.BTC-14AUG20.raw",
           "trades.BTC-14AUG20.raw"
       ]
   }
}
Response

Name	Type	Enum	Description
result	array of string		A list of unsubscribed channels.
Subscriptions
book.{instrument_name}.{interval}
Description

Notifies about changes to the order book for a certain instrument.

How to manage a local order book correctly:

Open a WebSocket connection to server, then subscribe to the OrderBook data stream through the subscription channel book.{instrumentName}.raw, buffer the events received from the stream. Note the change_id of the first event you received, mark this as fisrtChangeId.

Get the orderbook snapshot by http endpoint /public/get_order_book.
If the version in the snapshot is strictly less than the fisrtChangeId - 1, retry taking the snapshot until version is greater than or equal to fisrtChangeId -1, mark the version field in the last snapshot data obtained as lastVersion.

Set your local order book to the snapshot. Its update ID is lastVersion. In the buffered events, discard any event where change_id is <= lastVersion of the snapshot.

Apply the update procedure below to all buffered events, and then to all subsequent events received.

If the event change_id is < lastVersion of your local order book, ignore the event.
If the event change_id > lastVersion + 1 of your local order book, something went wrong. Discard your local order book and restart the process from the beginning.
For each price level in bids and asks, set the new quantity in the order book:
If the price level does not exist in the order book, insert it with new quantity.
If the quantity is zero, remove the price level from the order book.
Set the order book lastVersion to the change_id in the processed event.
Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/public/subscribe",
  "params" : {
    "channels":[
      "book.BTC-USDT-PERPETUAL.raw"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name.Specially in SPOT currency, use symbol, eg: BTC-USDT-SPOT or BTC-USDT-MARGIN use BTC-USDT
interval	true	string	raw	Frequency of notifications. Events will be aggregated over this interval.
The above command returns JSON structured like this (real example)

{
  "params": {
    "data": {
      "timestamp": 1626056933600,
      "change_id": 1566764,
      "asks": [
        [
          "new",
          "34227.122",
          "0.00554"
        ],
        [
          "delete",
          "34235.679",
          "0"
        ]
      ],
      "bids": [
        [
          "delete",
          "34105.540",
          "0"
        ],
        [
          "delete",
          "34102.118",
          "0"
        ],
        [
          "new",
          "34209.912",
          "0.28236"
        ]
      ],
      "instrument_name": "BTC-USDT"
    },
    "channel": "book.BTC-USDT.raw"
  },
  "method": "subscription",
  "jsonrpc": "2.0"
}
Channel Response

Name	Type	Enum	Description
data	object		
› asks	array of [price, amount]		
› bids	array of [price, amount]		
› instrument_name	string		instrument name
› timestamp	integer		The timestamp of last change (milliseconds since the Unix epoch)
› change_id	integer		version number
chart.trades.{instrument_name}.{resolution}
Description

Publicly available market data used to generate a TradingView candle chart. During single resolution period, many events can be sent, each with updated values for the recent period.

NOTICE When there is no trade during the requested resolution period (e.g. 1 minute), then filling sample is generated which uses data from the last available trade candle (open and close values).

Request example

{
     "jsonrpc" : "2.0",
     "id" : 9929,
     "method" : "/public/subscribe",
     "params" : {
      "channels":[
        "chart.trades.BTC-14AUG20.5"
      ]
     }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name. Specially in SPOT currency, use symbol, eg: BTC-USDT-SPOT or BTC-USDT-MARGIN use BTC-USDT
resolution	true	string	1 3 5 10 15 30 60 120 180 240 360 720 1D	Chart bars resolution given in full minutes or keyword 1D (only some specific resolutions are supported)
The above command returns JSON structured like this (real example)

{
    "params": {
        "data": {
            "tick": 1597130400,
            "open": 11794.000,
            "high": 11794.000,
            "low": 11770.000,
            "close": 11770.000,
            "volume": 2.0000,
            "cost": 23540.000
        },
        "channel": "chart.trades.BTC-14AUG20.5"
    },
    "method": "subscription",
    "jsonrpc": "2.0"
}
Response
Name	Type	Enum	Description
data	object		
› close	number		The close price for the candle
› cost	number		Cost data for the candle
› high	number		The highest price level for the candle
› low	number		The lowest price level for the candle
› open	number		The open price for the candle'
› tick	integer		The timestamp (milliseconds since the Unix epoch)
› volume	number		Volume data for the candle
markprice.{kind}.{currency}
Description

Provides information about options and futures markprices

Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/public/subscribe",
  "params" : {
    "channels":[
      "markprice.perpetual.PERPETUAL"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
kind	true	string	perpetual, spot	Instrument kind
currency	true	string	SPOT, PERPETUAL	The currency symbol
The above command returns JSON structured like this (real example)

{
  "jsonrpc": "2.0",
  "method": "subscription",
  "params": {
    "channel": "markprice.perpetual.PERPETUAL",
    "data": [
      {
        "mut": "1597303073115",
        "instrument_name": "ETH-USDT-PERPETUAL",
        "mark_iv": "0.8341",
        "mark_price": "132.6479",
        "underlying_price": "391.3781",
        "underlying_index": "ETH-USDT"
      },
      {
        "mut": "1596959999594",
        "instrument_name": "ETH-USDT-PERPETUAL",
        "mark_iv": "0.9532",
        "mark_price": "0",
        "underlying_price": "380.3464"
      }
    ]
  }
}
Channel Response

Name	Type	Description
data	object	
› instrument_name	string	Instrument name
› mark_price	number	Current index price
› mark_iv	number	Current index iv
› mut	integer	The timestamp (milliseconds since the Unix epoch)
› underlying_price	number	Underlying price
› underlying_index	number	Underlying name
price_index.{index_name}
Description

Provides information about current value (price) for ORANGEX Index

Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/public/subscribe",
  "params" : {
    "channels":[
      "price_index.btc_usdt"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
index_name	true	string	btc_usdt eth_usdt	Index identifier, matches (base) cryptocurrency with quote currency
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "method": "subscription",
    "params": {
        "channel": "price_index.btc_usdt",
        "data": {
            "price": "11738.73",
            "index_name": "btc_usdt",
            "timestamp": 1597130683001
        }
    }
}
Response

Name	Type	Enum	Description
data	object		
› index_name	string		Index identifier, matches (base) cryptocurrency with quote currency
› price	number		Current index price
› timestamp	integer		The timestamp (milliseconds since the Unix epoch)
ticker.{instrument_name}.{interval}
Description

Key information about the instrument

Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/public/subscribe",
  "params" : {
    "channels":[
      "ticker.BTC-USDT.raw"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name.Specially in SPOT currency, use symbol, eg: BTC-USDT-SPOT or BTC-USDT-MARGIN use BTC-USDT
The above command returns JSON structured like this (real example)

{
    "params": {
        "data": {
            "max_price": null,
            "stats": {
                "low": "11733.145",
                "high": "12005.008",
                "price_change": "-0.0200",
                "volume": "344.84442"
            },
            "mark_price": "11737.221",
            "best_bid_amount": "0.01288",
            "state": "open",
            "best_ask_price": "11733.209",
            "last_price": "11733.145",
            "best_ask_amount": "0.01273",
            "min_price": null,
            "timestamp": "1597130649580",
            "best_bid_price": "11733.081",
            "instrument_name": "BTC-USDT"
        },
        "channel": "ticker.BTC-USDT.raw"
    },
    "method": "subscription",
    "jsonrpc": "2.0"
}
Response

Name	Type	Description
data	object	
› ask_iv	number	(Only for option) implied volatility for best ask
› best_ask_amount	number	It represents the requested order size of all best asks
› best_ask_price	number	The current best ask price, null if there aren't any asks
› best_bid_amount	number	It represents the requested order size of all best bids
› best_bid_price	number	The current best bid price, null if there aren't any bids
› bid_iv	number	(Only for option) implied volatility for best bid
› greeks	object	
› › delta	number	(Only for option) The delta value for the option
› index_price	number	Current index price
› instrument_name	string	Unique instrument identifier
› last_price	number	The price for the last trade
› mark_iv	number	(Only for option) implied volatility for mark price
› mark_price	number	The mark price for the instrument
› max_price	number	The maximum price for the future. Any buy orders you submit higher than this price, will be clamped to this maximum.
› min_price	number	The minimum price for the future. Any sell orders you submit lower than this price will be clamped to this minimum.
› open_interest	number	The total amount of outstanding contracts in the corresponding amount units. The minsize of futures and options is one contract.
› state	string	The state of the order book. Possible values are open and closed.
› stats	object	
› › high	number	highest price during 24h
› › low	number	lowest price during 24h
› › price_change	number	24-hour price change expressed as a percentage, null if there weren't any trades
› › volume	number	volume during last 24h in base currency
› timestamp	integer	The timestamp (milliseconds since the Unix epoch)
› underlying_index	number	Name of the underlying future, or index_price (options only)
› underlying_price	number	Underlying price for implied volatility calculations (options only)
trades.{instrument_name}.{interval}
Description

Get notifications about trades for an instrument.

Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/public/subscribe",
  "params" : {
    "channels":[
      "trades.BTC-USDT-PERPETUAL.raw"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name
interval	true	string	raw	Frequency of notifications. Events will be aggregated over this interval. The value raw means no aggregation will be applied
The above command returns JSON structured like this (real example)

{
  "jsonrpc":"2.0",
  "method":"subscription",
  "params":{
    "channel":"trades.BTC-USDT-SPOT.raw",
    "data":[
      {
        "timestamp":"1650529700650",
        "price":"39870",
        "amount":"0.00023",
        "iv":"0",
        "direction":"buy",
        "instrument_name":"BTC-USDT-SPOT",
        "trade_id":"18642753"
      }
    ]
  }
}
Response

Name	Type	Enum	Description
data	object		
› instrument_name	string		Unique instrument identifier
› trade_id	string		Unique (per currency) trade identifier
› timestamp	integer		The timestamp of the trade
› price	number		Price in base currency
› amount	number		Trade amount. The minsize of futures and options is one contract, while margin is measured in base currency(BTC, ETH, etc.).
› direction	string	buy, sell	Taker Direction
› iv	number		Option implied volatility for the price (Option only)
user.changes.{kind}.{currency}.{interval}
Description

Get notifications about changes in user's updates related to order, trades, etc. in instruments of a given kind and currency.

Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/private/subscribe",
  "params" : {
    "channels":[
      "user.changes.spot.SPOT.raw","user.changes.perpetual.PERPETUAL.raw"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
kind	true	string	spot ,perpetual	Instrument kind.
currency	true	string	SPOT ,PERPETUAL	The trading currency.
interval	true	string	raw	Frequency of notifications. Events will be aggregated over this interval. The value raw means no aggregation will be applied
The above command returns JSON structured like this (real example)

{
  "jsonrpc": "2.0",
  "method": "subscription",
  "params":
  {
    "channel": "user.changes.perpetual.PERPETUAL.raw",
    "data":
    {
      "orders":
      [
        {
          "currency": "PERPETUAL",
          "kind": "perpetual",
          "direction": "buy",
          "amount": "0.01",
          "price": "1000",
          "advanced": "usdt",
          "source": "api",
          "mmp": false,
          "rpl": "0",
          "version": 1,
          "order_id": "345521542966894593",
          "custom_order_id": "1234abc",
          "order_state": "open",
          "instrument_name": "ETH-USDT-PERPETUAL",
          "show_name": "ETHUSDT Perp",
          "filled_amount": "0",
          "average_price": "0",
          "order_type": "limit",
          "time_in_force": "GTC",
          "post_only": false,
          "reduce_only": false,
          "condition_type": "NORMAL",
          "trigger_touch": false,
          "trigger_price_type": 1,
          "stop_loss_price": "0",
          "stop_loss_type": 1,
          "take_profit_price": "0",
          "take_profit_type": 1,
          "creation_timestamp": 1670209155344,
          "last_update_timestamp": 1670209155360,
          "show_zero_rpl": false,
          "cascade_type": 0,
          "first_deal_time": 0,
          "position_side": "LONG"
        }
      ],
      "positions":
      [
        {
          "currency": "PERPETUAL",
          "kind": "perpetual",
          "size": "0.01",
          "direction": "buy",
          "leverage": "20",
          "margin": "0.64633",
          "version": "911779",
          "roe": "-0.009742",
          "traceType": 0,
          "pos_id": "1",
          "instrument_name": "ETH-USDT-PERPETUAL",
          "show_name": "ETHUSDT Perp",
          "average_price": "1293.29",
          "mark_price": "1292.66",
          "initial_margin": "0.646645",
          "maintenance_margin": "0.064633",
          "total_profit_loss": "0",
          "floating_profit_loss": "-0.0063",
          "liquid_price": "0",
          "margin_type": "cross",
          "risk_level": "0.002306",
          "available_withdraw_funds": "27.37056974",
          "order_id": "345532310033620992",
          "stop_loss_price": "0",
          "stop_loss_type": 1,
          "take_profit_price": "0",
          "take_profit_type": 1,
          "position_side": "LONG"
        }
      ],
      "trades":
      [
        {
            "direction": "buy",
            "amount": "0.01",
            "price": "1293.29",
            "fee": "0",
            "timestamp": 1670211722400,
            "role": "taker",
            "rpl": "0",
            "trade_id": "1637600273",
            "order_id": "345532310033620992",
            "instrument_name": "ETH-USDT-PERPETUAL",
            "show_name": "ETHUSDT Perp",
            "order_type": "market",
            "fee_use_coupon": false,
            "fee_coin_type": "USDT",
            "index_price": "0",
            "mark_price": "1292.66",
            "self_trade": false,
            "field1": false,
            "field2": 19154
        }
      ],
      "instrument_name": "ETH-USDT-PERPETUAL"
    }
  }
}
Response

Name	Type	Enum	Description
data	array of object		
› instrument_name	string		Unique instrument identifier
› orders	array of object		
›› order_id	string		Unique order identifier
›› amount	number		It represents the requested order size.
›› price	number		Price in base currency
›› trigger_price	number		Trigger price. Available when condition_type is STOP or IF_TOUCHED.
›› trail_price	number		Tracking price change Delta. Available when condition_type is TRAILING.
›› iv	string		Implied volatility in percent.For example, price=100, means implied volatility of 100%.
›› instrument_name	string		Unique instrument identifier
›› direction	string	buy, sell	Direction.
›› order_state	string	"open", "filled", "canceled"	order state.
›› order_type	string	limit market	order type, limit
›› filled_amount	number		Filled amount of the order.
›› average_price	number		Average fill price of the order
›› last_update_timestamp	integer		The timestamp (milliseconds since the Unix epoch)
›› creation_timestamp	integer		The timestamp (milliseconds since the Unix epoch)
›› version	string		The order version
›› kind	string		The order kind.
›› currency	string		The trading area.
›› condition_type	String		Condition sheet policy, the default is NORMAL. Available when kind is future
›› trigger_touch	boolean		Whether the stop order has been triggered
›› advanced	string	usdt iv	advanced type: usdt or iv (Only for options; field is omitted if not applicable).
›› time_in_force	string		Order time in force: "good_til_cancelled"
›› post_only	boolean		true for post-only orders only
›› reduce_only	boolean		true for reduce-only orders only
›› source	string		Order source
› stop_loss_type	Number		Stop loss price type.
› take_profit_price	Number		Take profit price. If the value is 0, it means not set.
› take_profit_type	Number		Take profit price type.
› position	array of object		
›› currency	string		The trading area.
›› instrument_name	string		Unique instrument identifier
›› kind	string		Instrument kind, "future" or "option"
›› average_price	number		Average price of trades that built this position
›› size	number		Position size.
›› direction	string	buy, sell , zero	Direction
›› leverage	number		Current available leverage for future position.
›› margin_type	string	cross,isolated	Position type.
›› risk_level	number		Risk Level. The risk of margin is between 0% and 100%, the higher the value, the higher the risk of compulsory closing.
›› roe	number		roe
›› available_withdraw_funds	number		Transferable quantity
›› floating_profit_loss	number		Floating profit or loss
›› realized_profit_loss	number		Realized profit or loss
›› total_rpl	number		Total realized profit or loss
›› total_profit_loss	number		Profit or loss from position
›› mark_price	number		Current mark price for position's instrument
›› index_price	number		Current mark price for index instrument
›› initial_margin	number		Initial margin
›› maintenance_margin	number		Maintenance margin
›› variable_funds	number		Variable funds.
›› liquid_price	number		Liquid price.
›› margin_balance	number		Margin balance.
›› margin_balance_isolated	number		Margin balance of isolated.
›› wallet_balance_isolated	number		Wallet balance of isolated.
›› version	string		The position version
›› delta	number		Delta parameter
›› stop_loss_price	number		Stop loss price. If the value is 0, it means not set.
›› stop_loss_type	number		Stop loss price type.
›› take_profit_price	number		Take profit price. If the value is 0, it means not set.
›› take_profit_type	number		Take profit price type.
›› traceType	number	0,1,2	Trace type. Only for perpetuals. 0: normal,1: trace trader, 2: trace follower
› trades	array of object		
›› trade_id	string		Unique (per currency) trade identifier
›› direction	string	buy,sell	Direction
›› amount	number		Trade amount.
›› fee	number		User's fee in units of the specified fee_currency
›› fee_coin_type	string		Fee Currency, i.e BTC, ETH
›› instrument_name	string		Unique instrument identifier
›› order_id	string		Id of the user order (maker or taker), i.e. subscriber's order id that took part in the trade
›› order_type	string	limit market	Order type.
›› price	number		Price in base currency
›› index_price	number		Index Price at the moment of trade
›› timestamp	integer		The timestamp of the trade
›› iv	number		Option implied volatility for the price (Option only)
›› custom_order_id	String		Client order id.
user.orders.{instrument_name}.raw
Description

Get notifications about changes in user's orders for given instrument.
Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/private/subscribe",
  "params" : {
    "channels":[
      "user.orders.BTC-14AUG20.raw"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name. eg: BTC-USDT-SPOT,BTC-USDT-MARGIN,BTC-JUN0620,BTC-JUN0620-10000-C,BTC-USDT-PERPETUAL。
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "method": "subscription",
    "params": {
        "channel": "user.orders.BTC-14AUG20.raw",
        "data": {
            "amount": "1",
            "price": "11895.00",
            "direction": "buy",
            "version": 0,
            "order_state": "filled",
            "instrument_name": "BTC-14AUG20",
            "time_in_force": "good_til_cancelled",
            "last_update_timestamp": 1597130534567,
            "filled_amount": "1",
            "average_price": "11770.00",
            "order_id": "39007591615041536",
            "creation_timestamp": 1597130534567,
            "order_type": "limit"
        }
    }
}
Response

Name	Type	Description
data	object	
› order_id	string	Unique order identifier
› amount	number	It represents the requested order size.
› price	number	Price in base currency
› trigger_price	number	Trigger price. Available when condition_type is STOP or IF_TOUCHED.
› trail_price	number	Tracking price change Delta. Available when condition_type is TRAILING.
› iv	string	Implied volatility in percent.For example, price=100, means implied volatility of 100%.
› instrument_name	string	Unique instrument identifier
› direction	string	Direction: buy, or sell
› order_state	string	order state, "open", "filled", "canceled"
› order_type	string	order type, limit
› filled_amount	Number	Filled amount of the order. The minsize of futures and options is one contract, while margin is measured in base currency(BTC, ETH, etc.).
› average_price	Number	Average fill price of the order
› last_update_timestamp	string	The timestamp (milliseconds since the Unix epoch)
› creation_timestamp	string	The timestamp (milliseconds since the Unix epoch)
› version	string	The order version
› kind	string	The order kind.
› currency	str ing	The trading area.
› condition_type	String	Condition sheet policy, the default is NORMAL. Available when kind is future
› trigger_touch	boolean	Whether the stop order has been triggered
› advanced	string	advanced type: usdt or iv (Only for options; field is omitted if not applicable).
› time_in_force	string	Order time in force: "good_til_cancelled"
› post_only	boolean	true for post-only orders only
› reduce_only	boolean	true for reduce-only orders only
› source	string	Order source
› stop_loss_price	Number	Stop loss price. If the value is 0, it means not set.
› stop_loss_type	Number	Stop loss price type.
› take_profit_price	Number	Take profit price. If the value is 0, it means not set.
› take_profit_type	Number	Take profit price type.
› custom_order_id	String	Client order id.
user.asset.{asset_type}
Description

Get the asset information of users in each trading area, including wallet assets.

Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/private/subscribe",
  "params" : {
    "channels":[
      "user.asset.MARGIN"
    ]
  }
}
The above command returns JSON structured like this (real example)

WALLET:
{
  "jsonrpc": "2.0",
  "method": "subscription",
  "params": {
    "channel": "user.asset.WALLET",
    "data": {
      "WALLET": {
        "total": "5578184962",
        "coupon": "0",
        "details": [
          {
            "available": "4999",
            "freeze": "0",
            "coin_type": "BTC",
            "current_mark_price": "38000"
          },
          {
            "available": "0",
            "freeze": "0",
            "coin_type": "ETH",
            "current_mark_price": "1600"
          },
          {
            "available": "980000",
            "freeze": "0",
            "coin_type": "USD",
            "current_mark_price": "1"
          },
          {
            "available": "5577199963",
            "freeze": "0",
            "coin_type": "USDT",
            "current_mark_price": "1"
          }
        ]
      }
    }
  }
}
SPOT:
{
  "jsonrpc": "2.0",
  "method": "subscription",
  "params": {
    "channel": "user.asset.SPOT",
    "data": {
      "SPOT": {
        "total": "281472.28536534",
        "net": "281472.28536534",
        "available": "281472.28536534",
        "details": [
          {
            "available": "9.99902",
            "freeze": "0",
            "total": "9.99902",
            "coin_type": "BTC",
            "current_mark_price": "18150.117"
          },
          {
            "available": "0",
            "freeze": "0",
            "total": "0",
            "coin_type": "ETH",
            "current_mark_price": "555.005"
          },
          {
            "available": "0",
            "freeze": "0",
            "total": "0",
            "coin_type": "USD",
            "current_mark_price": "0"
          },
          {
            "available": "99988.90248",
            "freeze": "0",
            "total": "99988.90248",
            "coin_type": "USDT",
            "current_mark_price": "1"
          }
        ]
      }
    }
  }
}
MARGIN:
{
  "jsonrpc": "2.0",
  "method": "subscription",
  "params": {
    "channel": "user.asset.MARGIN",
    "data": {
      "MARGIN": {
        "total": "609474.62536534",
        "net": "609474.62536534",
        "available": "609474.62536534",
        "borrowed": "0",
        "maintenance_margin": "0",
        "cushion_rate": "0",
        "interest_owed": "0",
        "details": [
          {
            "available": "29.99902",
            "freeze": "0",
            "borrowed": "0",
            "net": "29.99902",
            "total": "29.99902",
            "debt": "0",
            "canborrow": "302.21687432",
            "coin_type": "BTC",
            "interest_owed": "0",
            "max_transfer": "29.99902",
            "coin_leverage": "10",
            "daily_interest_rate": "0.01",
            "current_mark_price": "18150.117"
          },
          {
            "available": "0",
            "freeze": "0",
            "borrowed": "0",
            "net": "0",
            "total": "0",
            "debt": "0",
            "canborrow": "4392.57033984",
            "coin_type": "ETH",
            "interest_owed": "0",
            "max_transfer": "0",
            "coin_leverage": "5",
            "daily_interest_rate": "0.001",
            "current_mark_price": "555.005"
          },
          {
            "available": "64988.90248",
            "freeze": "0",
            "borrowed": "0",
            "net": "64988.90248",
            "total": "64988.90248",
            "debt": "0",
            "canborrow": "5485271.62828806",
            "coin_type": "USDT",
            "interest_owed": "0",
            "max_transfer": "64988.90248",
            "coin_leverage": "10",
            "daily_interest_rate": "0.01",
            "current_mark_price": "1"
          }
        ]
      }
    }
  }
}
option and future(BTC or ETH)
{
  "jsonrpc": "2.0",
  "method": "subscription",
  "params": {
    "channel": "user.asset.BTC",
    "data": {
      "BTC": {
        "currency": "BTC",
        "balance": "130824.29",
        "equity": "130824.29",
        "base_currency": "USD",
        "available_funds": "130824.29",
        "available_withdrawal_funds": "130824.29",
        "futures_pl": "0",
        "futures_session_rpl": "0",
        "futures_session_upl": "0",
        "initial_margin": "0",
        "maintenance_margin": "0",
        "margin_balance": "130824.29",
        "options_value": "0",
        "options_pl": "0",
        "options_session_rpl": "0",
        "options_session_upl": "0",
        "options_delta": "0",
        "options_gamma": "0",
        "options_theta": "0",
        "options_vega": "0",
        "session_funding": "0",
        "session_rpl": "0",
        "session_upl": "0",
        "delta_total": "0"
      }
    }
  }
}
perpetual
{
    "jsonrpc": "2.0",
    "method": "subscription",
    "params":
    {
        "channel": "user.asset.PERPETUAL",
        "data":
        {
            "PERPETUAL":
            {
                "bonus": "0",
                "global_state": 3,
                "available_funds": "102716.31684805",
                "wallet_balance": "107556.51446905",
                "available_withdraw_funds": "102716.31684805",
                "total_pl": "524.2",
                "total_upl": "524.2",
                "position_rpl": "0",
                "total_upl_isolated": "524.2",
                "total_upl_cross": "0",
                "total_initial_margin_cross": "0",
                "total_initial_margin_isolated": "4922.14",
                "total_margin_balance_isolated": "5364.397621",
                "total_margin_balance": "108080.71446905",
                "total_margin_balance_cross": "102716.31684805",
                "total_maintenance_margin_cross": "0",
                "total_wallet_balance_isolated": "4840.197621",
                "order_frozen": "0",
                "order_cross_frozen": "0",
                "order_isolated_frozen": "0",
                "risk_level": "0",
                "bonus_max": "140.20295713"
            }
        }
    }
}
Parameters

Parameter	Required	Type	Enum	Description
asset_type	true	Enum	BTC,ETH,MARGIN,SPOT,PERPETUAL	Asset type. The supported asset types can be obtained through get_assets_type method.
Response
Parameter	Type	Enum	Description
result	object array		
› WALLET	object		Wallet assets
› BTC	object		BTC derivatives trading area(BTC D.T.A) assets. (BTC D.T.A) used to trade BTC options and BTC futures
› ETH	object		ETH derivatives trading area(ETH D.T.A) assets. (ETH D.T.A) used to trade ETH options and ETH futures
› SPOT	object		Spot assets. Spot used to spot trading without leverage
› MARGIN	object		Margin assets. Margin used to spot trading without leverage
› PERPETUAL	object		Perpetual assets.
Wallet assets fields（WALLET ）

Parameter	Type	Enum	Description
total	number		Total assets of wallet, equivalent to usdt
coupon	number		Coupon of wallet, equivalent to usdt
details	object array		Details of wallet assets
› coin_type	string		Coin
› available	number		Available assets, wallet balance
› freeze	number		Freezing assets
› current_mark_price	number		Mark Price, the unit is usdt
Trading area asset fields for options and Futures(BTC D.T.A, ETH D.T.A)

Parameter	Type	Enum	Description
currency	enum	BTC,ETH	Trading area
base_currency	number		settlement coin
available_funds	number		available funds
available_withdrawal_funds	number		Transferable quantity
balance	number		Available balance
equity	number		Net assets of account
initial_margin	number		Initial margin
maintenance_margin	number		Maintenance margin
margin_balance	number		Margin balance
cushion_rate	number		Risk Level.
session_funding	number		Session funding
session_rpl	number		Realized profit and loss
session_upl	number		Unrealized profit and loss
futures_pl	number		Total profit and loss of futures
futures_session_rpl	number		Realized profit and loss of futures
futures_session_upl	number		Unrealized profit and loss of futures
options_value	number		Total value of options, sum(size*price)
options_pl	number		Total profit and loss of option
options_session_rpl	number		Realized profit and loss of option
options_session_upl	number		Unrealized profit and loss of option
options_delta	number		Delta of options
options_gamma	number		Gamma of options
options_theta	number		Theta of options
options_vega	number		Vega of options
delta_total	number		Total delta of trading area
total_pl	number		Total profit and loss of trading area
Spot asset field(SPOT)

Parameter	Type	Enum	Description
total	number		The total market value of all spot's assets, equivalent to usdt
available	number		The total market value of all available assets of spot, equivalent to usdt
details	object array		Asset details in single coin
› coin_type	string		Coin
› available	number		Available assets
› freeze	number		Freezing assets
› total	number		Total = Available + Freeze
› current_mark_price	number		Mark Price, the unit is usdt
Margin asset field(MARGIN)

Parameter	Type	Enum	*Description*
total	number		The total market value of all margin's assets, equivalent to usdt
available	number		The total market value of all available assets of margin, equivalent to usdt
net	number		The total market value of all net assets of margin, equivalent to usdt
borrowed	number		The total market value of all margin's loan balances, equivalent to usdt
interest_owed	number		Total interest payable in single coin
maintenance_margin	number		Maintenance margin
cushion_rate	number		Risk Level. The risk of margin is between 0% and 100%, the higher the value, the higher the risk of compulsory closing.
details	object array		Asset details in single coin
› coin_type	string		Coin
› available	number		Available assets
› freeze	number		Freezing assets
› borrowed	number		loan balances in single coin
›interest_owed	number		Interest payable in single coin
› net	number		Net = available + freeze - borrowed - interest_owed
› total	number		Total = available + freeze
› debt	number		Debt = borrowed + interest_owed
› max_transfer	number		Maximum transfer out quantity
› canborrow	number		Loanable quantity
› coin_leverage	number		Maximum leverage
› daily_interest_rate	number		Daily interest rate
› current_mark_price	number		Mark Price, the unit is usdt
Perpetual asset field（PERPETUAL ）

Parameter	Type	Enum	Description
wallet_balance	number		Total wallet balance.
available_funds	number		available funds
available_withdraw_funds	number		Transferable quantity
total_pl	number		Total profit and loss of trading area
total_upl	number		Unrealized profit and loss
position_rpl	number		Realized profit and loss
total_upl_isolated	number		Unrealized profit and loss of isolated
total_upl_cross	number		Unrealized profit and loss of cross
total_initial_margin_cross	number		Initial margin of cross
total_initial_margin_isolated	number		Initial margin of isolated
total_margin_balance_isolated	number		Total margin balance of isolated
total_margin_balance_cross	number		Total margin balance of cross
total_margin_balance	number		Total margin balance
total_maintenance_margin_cross	number		Maintenance margin of cross
total_wallet_balance_isolated	number		Total wallet balance of isolated
order_frozen	number		Frozen of order
order_cross_frozen	number		Frozen of cross order
order_isolated_frozen	number		Frozen of isolated order
bonus	number		Available bonus.
bonus_max	number		Upper limit of bonus.
user.trades.{instrument_name}.{interval}
Description

Get notifications about user's trades in an instrument.
Request example

{
  "jsonrpc" : "2.0",
  "id" : 1,
  "method" : "/private/subscribe",
  "params" : {
    "channels":[
      "user.trades.BTC-USDT-PERPETUAL.raw"
    ]
  }
}
Parameters

Parameter	Required	Type	Enum	Description
instrument_name	true	string		Instrument name. eg: BTC-USDT-SPOT,BTC-USDT-MARGIN,BTC-JUN0620,BTC-JUN0620-10000-C,BTC-USDT-PERPETUAL。
interval	true	string	raw	Frequency of notifications. Events will be aggregated over this interval. The value raw means no aggregation will be applied
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "method": "subscription",
    "params": {
        "channel": "user.trades.BTC-14AUG20.raw",
        "data": {
            "direction": "sell",
      "amount": "1",
      "price": "33000",
      "iv": "0",
      "fee": "0",
      "timestamp": 1626148488157,
      "trade_id": "1",
      "order_id": "160717710099746816",
      "instrument_name": "BTC-24SEP21",
      "order_type": "limit",
      "fee_coin_type": "USDT",
      "index_price": "33157.63"
        }
    }
}
Response

Name	Type	Enum	Description
data	array of object		
› trade_id	string		Unique (per currency) trade identifier
› direction	string	buy,sell	Direction
› amount	string		Trade amount.
› fee	string		User's fee in units of the specified fee_currency
› fee_coin_type	string		Fee Currency, i.e BTC, ETH
› instrument_name	string		Unique instrument identifier
› order_id	string		Id of the user order (maker or taker), i.e. subscriber's order id that took part in the trade
› order_type	string	limit market	Order type.
› price	string		Price in base currency
› index_price	string		Index Price at the moment of trade
› timestamp	number		The timestamp of the trade
› iv	string		Option implied volatility for the price (Option only)
CopyTrade
(Copy) Place order
Description

Places a buy order for an instrument.
Asynchronous operation only means that the request is received. The specific order status can be obtained by subscribing or querying the order status.
Method

/private/copyApi/trade/order/place
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/copy/trade/order/place",
  "params": {
    "portfolioId": 112,
    "amount": "1",
    "type": "limit",
    "direction": "buy",
    "instrumentName": "BTC-USDT-PERPETUAL",
    "price": "90"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
instrumentName	true	String		Instrument name. eg: BTC-USDT-PERPETUAL
direction	true	String	buy,sell	Order direction.
positionSide	true	String	LONG,SHORT	Position Side.
amount	true	number		The order amount.
type	false	String	limit, market	The order type, default: limit.
price	false	number		The order price for limit order
timeInForce	false	String	GTC, FOK, IOC	Specifies how long the order remains in effect, default: GTC.
postOnly	false	Boolen		If true, the order is considered post-only, default: false.
reduceOnly	false	Boolen		If true, the order is considered reduce-only which is intended to only reduce a current position. default: false.
conditionType	false	String	NORMAL, STOP, TRAILING, IF_TOUCHED	Condition sheet policy, the default is NORMAL.
triggerPrice	false	Number		Trigger price. Available when condition_type is STOP or IF_TOUCHED.
triggerPriceType	false	Number	1, 2	Trigger price type. 1 : mark_price, 2: last_price.
trailPrice	false	Number		Tracking price change Delta. Available when condition_type is TRAILING.
stopLossPrice	fasle	String		Stop loss price.
stopLossType	fasle	Number	1,2	Stop loss price type. 1 : mark_price, 2: last_price.
takeProfitPrice	fasle	String		Take profit price.
takeProfitType	fasle	Number	1,2	Take profit price type. 1 : mark_price, 2: last_price.
marketAmountOrder	false	boolean		Advanced order amount type, default: false. If set to true，then the amount field means USDT value.
customOrderId	false	String		Client order id. Can only be string following the rule: ^[.A-Z:/a-z0-9_-]{1,36}$. Returned when querying an order .
The above command returns JSON structured like this (real example)

  {
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1590387640408,
    "usOut": 1590387641134,
    "usDiff": 726,
    "result": {
        "orderId": "77409325612535808"
    }
}
Response

Name	Type	Enum	Description
result	object		Response data
› orderId	String		order id
(Copy) Get order state
Description

Get the order by id.
Method

/private/copyApi/trade/order/queryState
Request example

{
  "jsonrpc":"2.0",
  "id": "1662",
  "method": "/private/copy/trade/order/queryState",
  "params": {
    "portfolioId": 112,
    "orderId": 365533374317027328
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
orderId	true	string		The unique id of the order.
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1675069431765,
    "usOut": 1675069431782,
    "usDiff": 17,
    "result": [
        {
            "orderId": "365533374317027328",
            "customOrderId": "-",
            "orderState": "open",
            "instrumentName": "BTC-USDT-PERPETUAL",
            "showName": "BTCUSDT Perp",
            "direction": "buy",
            "amount": "0.01",
            "price": "20000",
            "filledAmount": "0",
            "averagePrice": "0",
            "orderType": "limit",
            "timeInForce": "GTC",
            "postOnly": false,
            "reduceOnly": false,
            "conditionType": "NORMAL",
            "triggerTouch": false,
            "triggerPriceType": 1,
            "stopLossPrice": "0",
            "stopLossType": 1,
            "takeProfitPrice": "0",
            "takeProfitType": 1,
            "createTime": 1674980347736,
            "updateTime": 1674980347777,
            "rpl": "0",
            "positionSide": "LONG"
        }
    ]
}
Response

Name	Type	Enum	Description
result	array of object		
› orderId	string		The unique id of the order.
› customOrderId	string		Client order id. Can only be string following the rule: ^[.A-Z:/a-z0-9_-]{1,36}$. Returned when querying an order.
› orderState	string	open, filled, cancelled	The order state.
› direction	string	buy, sell	The order direction.
› instrumentName	string		Instrument name. eg: BTC-USDT-PERPETUAL
› positionSide	string	LONG, SHORT	Position Side.
› amount	number		Order quantity.
› filledAmount	number		Filled amount of the order.
› price	number		The order price.
› averagePrice	number		Average fill price of the order.
› orderType	string	limit, market	The order type.
› timeInForce	string	GTC, IOC, FOK	The order type.
› postOnly	Boolean		If true, the order is considered post-only.
› reduceOnly	Boolean		If true, the order is considered reduce-only which is intended to only reduce a current position.
› conditionType	string	NORMAL, STOP, TRAILING, IF_TOUCHED	Condition sheet policy, the default is NORMAL.
› triggerTouch	Boolean		Whether the trigger price is triggered.
› triggerPrice	number		Trigger price. Available when condition_type is STOP or IF_TOUCHED.
› triggerPriceType	string	1,2	Trigger price. 1 : mark_price, 2: last_price.
› trailPrice	number		Tracking price change Delta. Available when condition_type is TRAILING.
› stopLossPrice	number		Stop loss price.
› stopLossType	number	1,2	Stop loss price type. 1 : mark_price, 2: last_price.
› takeProfitPrice	number		Take profit price.
› takeProfitType	number	1,2	Take profit price type. 1 : mark_price, 2: last_price.
› rpl	number		Realized profit or loss.
› positionSide	string	LONG, SHORT	Position Side.
› createTime	timestamp		Create time.
› updateTime	timestamp		Last update time.
(Copy) Get open order
Description

Get open order.
Method

/private/copyApi/trade/order/queryOpen
Request example

{
  "jsonrpc":"2.0",
  "id": "1662",
  "method": "/private/copy/trade/order/queryOpen",
  "params": {
    "portfolioId": 112
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
instrumentName	false	string		The instrument name. eg: BTC-USDT-PERPETUAL.
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1675069431765,
    "usOut": 1675069431782,
    "usDiff": 17,
    "result": [
        {
            "orderId": "365533374317027328",
            "customOrderId": "-",
            "orderState": "open",
            "instrumentName": "BTC-USDT-PERPETUAL",
            "showName": "BTCUSDT Perp",
            "direction": "buy",
            "amount": "0.01",
            "price": "20000",
            "filledAmount": "0",
            "averagePrice": "0",
            "orderType": "limit",
            "timeInForce": "GTC",
            "postOnly": false,
            "reduceOnly": false,
            "conditionType": "NORMAL",
            "triggerTouch": false,
            "triggerPriceType": 1,
            "stopLossPrice": "0",
            "stopLossType": 1,
            "takeProfitPrice": "0",
            "takeProfitType": 1,
            "createTime": 1674980347736,
            "updateTime": 1674980347777,
            "rpl": "0",
            "positionSide": "LONG"
        }
    ]
}
Response

Name	Type	Enum	Description
result	array of object		
› orderId	string		The unique id of the order.
› customOrderId	string		Client order id. Can only be string following the rule: ^[.A-Z:/a-z0-9_-]{1,36}$. Returned when querying an order.
› orderState	string	open, filled, cancelled	The order state.
› direction	string	buy, sell	The order direction.
› instrumentName	string		Instrument name. eg: BTC-USDT-PERPETUAL
› positionSide	string	LONG, SHORT	Position Side.
› amount	number		Order quantity.
› filledAmount	number		Filled amount of the order.
› price	number		The order price.
› averagePrice	number		Average fill price of the order.
› orderType	string	limit, market	The order type.
› timeInForce	string	GTC, IOC, FOK	The order type.
› postOnly	Boolean		If true, the order is considered post-only.
› reduceOnly	Boolean		If true, the order is considered reduce-only which is intended to only reduce a current position.
› conditionType	string	NORMAL, STOP, TRAILING, IF_TOUCHED	Condition sheet policy, the default is NORMAL.
› triggerTouch	Boolean		Whether the trigger price is triggered.
› triggerPrice	number		Trigger price. Available when condition_type is STOP or IF_TOUCHED.
› triggerPriceType	string	1,2	Trigger price. 1 : mark_price, 2: last_price.
› trailPrice	number		Tracking price change Delta. Available when condition_type is TRAILING.
› stopLossPrice	number		Stop loss price.
› stopLossType	number	1,2	Stop loss price type. 1 : mark_price, 2: last_price.
› takeProfitPrice	number		Take profit price.
› takeProfitType	number	1,2	Take profit price type. 1 : mark_price, 2: last_price.
› rpl	number		Realized profit or loss.
› positionSide	string	LONG, SHORT	Position Side.
› createTime	timestamp		Create time.
› updateTime	timestamp		Last update time.
(Copy) Cancel by Id
Description

Cancel an order, specified by order id.
Asynchronous operation only means that the request is received. The specific order status can be obtained by subscribing or querying the order status.
Method

/private/copyApi/trade/order/cancel
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/copy/trade/order/cancel",
  "params": {
    "portfolioId": 112,
    "orderId": "1233",
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
orderId	true	Long		The order id.
The above command returns JSON structured like this (real example)

  {
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1590387640408,
    "usOut": 1590387641134,
    "usDiff": 726,
    "result": {
        "orderId": "77409325612535808"
    }
}
Response

Name	Type	Enum	Description
result	object		Response data
› orderId	String		order id
(Copy) Cancel By Instrument
Description

Cancels all orders by instrument. If the instrument is not transmitted, the order of all instrument will be cancelled.
Asynchronous operation only means that the request is received. The specific order status can be obtained by subscribing or querying the order status.
Method

/private/copyApi/trade/order/cancelAll
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/copy/trade/order/cancelAll",
  "params": {
    "portfolioId": 112,
    "instrumentName": "BTC-USDT-PERPETUAL"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
instrumentName	false	String		Instrument name. eg: BTC-USDT-PERPETUAL.
The above command returns JSON structured like this (real example)

  {
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1590387640408,
    "usOut": 1590387641134,
    "usDiff": 726,
    "result": {
        "cancelOrderNum": 10
    }
}
Response

Name	Type	Enum	Description
result	object		Response data
› cancelOrderNum	Integer		Number of cancelled orders.
(Copy) Edit order
Description

Edit order.
Method

/private/copyApi/trade/order/edit
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/copy/trade/order/edit",
  "params": {
    "portfolioId": 112,
    "orderId": "123",
    "amount": 123,
    "price": 1000,
    "triggerPrice": "1100",
    "triggerPriceType": 1
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
orderId	true	String		The unique id of the order.
amount	true	Number		Quantity at time of order.
price	false	Number		The order price for limit order.
triggerPrice	false	Number		Trigger price. Available when condition_type is STOP or IF_TOUCHED.
triggerPriceType	false	Integer	1,2	Trigger price type. 1 : mark_price, 2: last_price.
The above command returns JSON structured like this (real example)

  {
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1590387640408,
    "usOut": 1590387641134,
    "usDiff": 726,
    "result": {
        "orderId": "77409325612535808"
    }
}
Response

Name	Type	Enum	Description
result	object		Response data
› orderId	String		order id
(Copy) Order TP/SL
Description

Set TP/SL for order.
Method

/private/copyApi/trade/order/tpsl
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/copy/trade/order/tpsl",
  "params": {
    "portfolioId": 112,
    "orderId":"302573834064191488",
    "stopLossPrice": "1900",
    "stopLossType": "1",
    "takeProfitPrice": "2100",
    "takeProfitType": "1"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
orderId	true	String		The unique id of the order.
stopLossPrice	false	Number		Stop loss price. If you want to cancel the stop loss, please set stopLossPrice to 0.
stopLossType	false	Number	1, 2	Stop loss price type. 1 : mark_price, 2: last_price.
takeProfitPrice	false	Number		Take profit price. If you want to cancel the take profit, please set takeProfitPrice to 0.
takeProfitType	false	Number	1, 2	Take profit price type. 1 : mark_price, 2: last_price.
The above command returns JSON structured like this (real example)

  {
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1590387640408,
    "usOut": 1590387641134,
    "usDiff": 726,
    "result": {
        "orderId": "77409325612535808"
    }
}
Response

Name	Type	Enum	Description
result	object		Response data
› orderId	String		order id
(Copy) Get order tpsl detail
Description

Get TP/SL detail of the order.
Method

/private/copyApi/trade/order/queryTpsl
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/copy/trade/order/queryTpsl",
  "params": {
    "portfolioId": 112,
    "orderId":"302573834064191488"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
orderId	true	string		The unique id of the order.
The above command returns JSON structured like this (real example)

{
    "id": "1",
    "jsonrpc": "2.0",
    "usIn": 1636361022270,
    "usOut": 1636361022390,
    "usDiff": 120,
    "result": {
        "amount": "0.1",
        "filled": "0",
        "direction": "buy",
        "orderId": 203552148811681792,
        "instrumentName": "BTC-USDT-PERPETUAL",
        "trigger": true,
        "reduceOnly": false,
        "takeProfitOrder": {
            "amount": "0",
            "filled": "0",
            "direction": "sell",
            "trigger": false,
            "triggerPrice": "70000",
            "triggerPriceType": 1,
            "reduceOnly": true
        },
        "stopLossOrder": {
            "amount": "0",
            "filled": "0",
            "direction": "sell",
            "trigger": false,
            "triggerPrice": "60000",
            "triggerPriceType": 1,
            "reduceOnly": true
        }
    }
}
Response

Name	Type	Enum	Description
result	array of object		
› orderId	string		The unique id of the order.
› instrumentName	string		Instrument name. eg: BTC-USDT-PERPETUAL
› direction	string	buy, sell	Order direction.
› amount	string		Order quantity.
› filledAmount	string		Filled amount of the order.
› trigger	boolean		Whether the trigger price is triggered.
› reduceOnly	boolean		true for reduce-only orders only
› takeProfitOrder			The details of take profit order .
›› orderId	string		The unique id of take profit order.
›› direction	string	buy, sell	Order direction of take profit order.
›› amount	string		Order quantity of take profit order.
›› filledAmount	string		Filled amount of take profit order.
›› trigger	boolean		Whether take profit price is triggered.
›› triggerPrice			Take profit price.
›› triggerPriceType			Take profit price type. 1 : mark_price, 2: last_price.
› stopLossOrder			The details of stop loss order .
›› orderId	string		The unique id of stop loss order.
›› direction	string	buy, sell	Order direction of stop loss order.
›› amount	string		Order quantity of stop loss order.
›› filledAmount	string		Filled amount of stop loss order.
›› trigger	boolean		Whether take stop loss is triggered.
›› triggerPrice			Stop loss price.
›› triggerPriceType			Stop loss price type. 1 : mark_price, 2: last_price.
(Copy) Modify leverage
Description

Modify perpetual instrument leverage.
Method

/private/copyApi/trade/position/changeLeverage
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/copy/trade/position/changeLeverage",
  "params": {
    "portfolioId": 112,
    "instrumentName":"BTC-USDT-PERPETUAL",
    "leverage": 10
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
instrumentName	true	String		The instrument name. eg: BTC-USDT-PERPETUAL.
leverage	true	Integer		Leverage number.
The above command returns JSON structured like this (real example)

{
  "id": "18",
  "jsonrpc": "2.0",
  "usIn": 1625563460761,
  "usOut": 1625563460770,
  "usDiff": 9,
  "result": {}
}
Response

Name	Type	Enum	Description
result			
(Copy) Change margin
Description

Change margin for isolated position.
Method

/private/copyApi/trade/position/changeMargin
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/copy/trade/position/changeMargin",
  "params": {
    "portfolioId": 112,
    "instrumentName":"BTC-USDT-PERPETUAL",
    "positionSide": "LONG",
    "amount": "-10"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
instrumentName	true	String		The instrument name. eg: BTC-USDT-PERPETUAL.
positionSide	true	String	LONG, SHORT	Position Side.
amount	true	Number		Change amount.
The above command returns JSON structured like this (real example)

{
  "id": "18",
  "jsonrpc": "2.0",
  "usIn": 1625563460761,
  "usOut": 1625563460770,
  "usDiff": 9,
  "result": {}
}
Response

Name	Type	Enum	Description
result			
(Copy) Modify margin type
Description

Modify perpetual instrument margin type.
It can only be modified when the specified instrument has no orders and positions.
Method

/private/copyApi/trade/position/changeMarginType
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/copy/trade/position/changeMarginType",
  "params": {
    "portfolioId": 112,
    "instrumentName":"BTC-USDT-PERPETUAL",
    "marginType": "isolate"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
instrumentName	true	String		The instrument name. eg: BTC-USDT-PERPETUAL.
marginType	true	String	isolate,cross	Margin type.
The above command returns JSON structured like this (real example)

{
  "id": "18",
  "jsonrpc": "2.0",
  "usIn": 1625563460761,
  "usOut": 1625563460770,
  "usDiff": 9,
  "result": {}
}
Response

Name	Type	Enum	Description
result			
(Copy) Get position
Description

Get position.
Method

/private/copyApi/trade/position/query
Request example

{
  "jsonrpc":"2.0",
  "id": "1662",
  "method": "/private/copy/trade/position/query",
  "params": {
    "portfolioId": 112
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
instrumentName	false	string		The instrument name. eg: BTC-USDT-PERPETUAL.
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1675069431765,
    "usOut": 1675069431782,
    "usDiff": 17,
    "result": [
        {
            "instrumentName": "ETH-USDT-PERPETUAL",
            "positionSide": "SHORT",
            "size": "-0.06",
            "marginType": "isolate",
            "entryPrice": "1620.95",
            "liquidPrice": "1693.57960199",
            "markPrice": "1619.6",
            "leverage": "20",
            "margin": "4.86585",
            "initialMargin": "4.86285",
            "maintenanceMargin": "0.48588",
            "availableWithdrawFunds": "0.084",
            "realizedProfitLoss": "0",
            "floatingProfitLoss": "0.081",
            "roe": "0.016656",
            "riskLevel": "0.09822"
        },
        {
            "instrumentName": "ETH-USDT-PERPETUAL",
            "positionSide": "LONG",
            "size": "0.62",
            "marginType": "isolate",
            "entryPrice": "1609.55403226",
            "liquidPrice": "1534.56512401",
            "markPrice": "1619.6",
            "leverage": "20",
            "margin": "51.250275",
            "initialMargin": "49.896175",
            "maintenanceMargin": "5.02076",
            "availableWithdrawFunds": "7.5826",
            "realizedProfitLoss": "0",
            "floatingProfitLoss": "6.2285",
            "stopLossPrice": "1569.35",
            "stopLossType": 2,
            "takeProfitPrice": "2000",
            "takeProfitType": 2,
            "roe": "0.124829",
            "riskLevel": "0.087349"
        }
    ]
}
Name	Type	Enum	Description
result	array of object		
› instrumentName	string		Instrument name. eg: BTC-USDT-PERPETUAL
› positionSide	string	LONG, SHORT	Position Side.
› size	number		Position quantity.
› marginType	string	isolate,cross	Margin type.
› entryPrice	number		Average entry price.
› liquidPrice	number		Liquid price.
› markPrice	number		Current mark price for position's instrument.
› leverage	number		Current leverage for the position.
› margin	number		Margin.
› initialMargin	number		Initial margin.
› maintenanceMargin	number		Maintenance margin.
› availableWithdrawFunds	number		Transferable quantity.
› realizedProfitLoss	number		Realized profit or loss.
› floatingProfitLoss	number		Floating profit or loss.
› stopLossPrice	number		Stop loss price.
› stopLossType	number	1,2	Stop loss price type. 1 : mark_price, 2: last_price.
› takeProfitPrice	number		Take profit price.
› takeProfitType	number	1,2	Take profit price type. 1 : mark_price, 2: last_price.
(Copy) Close position
Description

Close the specified position.
Method

/private/copyApi/trade/position/close
Request example

{
  "jsonrpc":"2.0",
  "id": "1662",
  "method": "/private/copy/trade/position/close",
  "params": {
    "portfolioId": 112,
    "instrumentName": "BTC-USDT-PERPETUAL",
    "portfolioId": 112,
    "type": "limit",
    "price": "4500",
    "amount": "0.1"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
instrumentName	true	string		The instrument name. eg: BTC-USDT-PERPETUAL.
type	true	string	limit, market	The order type.
price	false	number		The order price for limit order.
amount	true	number		The order amount.
positionSide	true	String	LONG, SHORT	Position Side.
The above command returns JSON structured like this (real example)

{
  "id": "1662",
  "jsonrpc": "2.0",
  "usIn": 1606292314448,
  "usOut": 1606292314470,
  "usDiff": 22,
  "result": {

  }
}
Response

Name	Type	Enum	Description
result	object		
(Copy) Close all positions
Description

Close all position for the portfolio.
Method

/private/copyApi/trade/position/closeAll
Request example

{
  "jsonrpc":"2.0",
  "id": "1662",
  "method": "/private/copy/trade/position/closeAll",
  "params": {
    "portfolioId": 112
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1674028215933,
    "usOut": 1674028215987,
    "usDiff": 54,
    "result": {
        "totalClosePosition": 3
    }
}
Response

Name	Type	Enum	Description
result	object		
› totalClosePosition	object		The number of positions.
(Copy) Get copier info
Description

Get information about the copier currently following you.
Method

/private/copyApi/asset/queryCurrentCopierInfo
Request example

{
  "jsonrpc":"2.0",
  "id": "1662",
  "method": "/private/copyApi/asset/queryCurrentCopierInfo",
  "params": {
    "portfolioId": 112
  }
}
Parameters

Parameter	Required	Type	Enum	Description
portfolioId	true	Long		The unique id of the portfolio.
The above command returns JSON structured like this (real example)

{
  "id": "1764248498040",
  "jsonrpc": "2.0",
  "usIn": 1764248498153,
  "usOut": 1764248498306,
  "usDiff": 153,
  "result": [
    {
      "copierAssetUserId": "538415169371504641",
      "copierUid": 153501684,
      "portfolioName": "test-ts",
      "baseCurrency": "USDT",
      "startTime": "1716198579648",
      "initialCopierAmount": "100",
      "latestAmount": "0",
      "pnl": "0",
      "gainAndLoss": "999",
      "profitSharing": "0",
      "profitShared": "0"
    }
  ]
}
Response

Name	Type	Enum	Description
result	array of object		
› copierAssetUserId	string		Copy ID.
› copierUid	number		Copier's UID.
› portfolioName	string		Portfolio Name.
› baseCurrency	string		Assets.
› startTime	timestamp		Copy time
› initialCopierAmount	number		Initial Amount.
› latestAmount	number		Latest Amount. The latest amount is the last snapshot of the copy trader’s margin balance which contains unrealized pnl.
› pnl	number		PNL. Copy PNL = Latest Amount - Initial Amount - Accumulated Deposit
› gainAndLoss	number		Gain and Loss. Copy Gain and Loss = {Latest Amount / (Initial Amount + Accumulated Deposit) -1}
› profitSharing	number		Unrealized Profit Sharing. Calculated according to the current revenue of the copy trader. Data is used as reference only.
› profitShared	number		Realized Profit Sharing.
Convert
Query wallet support convert currency
Description

Query wallet support convert currency
Method

post
/public/convertApi/getWalletCoinList
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/public/convertApi/getWalletCoinList",
  "params": {
    "walletType": "SPOT"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
walletType	true	String	PERPETUAL，SPOT	wallet Type.
The above command returns JSON structured like this (real example)

{
  "id": "972",
  "jsonrpc": "2.0",
  "usIn": 1681959879126,
  "usOut": 1681959879129,
  "usDiff": 3,
  "result": [
    "BTC",
    "ETH",
    "TRX",
    "USDT"
  ]
}
Response

Name	Type	Enum	Description
result	List		Response data
Get the convert price between currency
Description

Get the convert price between currency
Method

post
/public/convertApi/getConvertPrice
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/public/convertApi/getConvertPrice",
  "params": {
    "from": "USDT",
    "to": "BTC"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
from	true	String		User spends coin.
to	true	String		User receives coin.
The above command returns JSON structured like this (real example)

{
  "id": "1",
  "jsonrpc": "2.0",
  "usIn": 1681960193742,
  "usOut": 1681960193755,
  "usDiff": 13,
  "result": {
    "price": "0.0000333000333",
    "inversePrice": "30030"
  }
}
Response

Name	Type	Enum	Description
result	object		Response data
› price	BigDecimal		exchange price
› inversePrice	BigDecimal		inverse price
Initiate convert
Description

Initiate convert
Method

post
/private/convertApi/initiateConvert
Request example

{
  "jsonrpc": "2.0",
  "id": "972",
  "method": "/private/convertApi/initiateConvert",
  "params": {
    "walletType": "SPOT",
    "from": "USDT",
    "to": "BTC",
    "convertAmount": "10.001"
  }
}
Parameters

Parameter	Required	Type	Enum	Description
walletType	true	String	PERPETUAL，SPOT	wallet Type.
from	true	String		User spends coin.
to	true	String		User receives coin.
convertAmount	true	BigDecimal		User convert amount.
The above command returns JSON structured like this (real example)

{
  "id": "1",
  "jsonrpc": "2.0",
  "usIn": 1681897739865,
  "usOut": 1681897739892,
  "usDiff": 27,
  "result": {
    "toAmount": "0.00068277",
    "price": "0.0000341387787125",
    "inversePrice": "29292.201939",
    "orderId": "394547019944431616"
  }
}
Response

Name	Type	Enum	Description
result	object		Response data
› toAmount	BigDecimal		user actually got amount
› price	BigDecimal		exchange price
› inversePrice	BigDecimal		inverse price
› orderId	String		order Id
Get convert records
Description

Get convert records
Method

post
/private/convertApi/getConvertRecordList
Request example

{
  "jsonrpc":"2.0",
  "id":1,
  "method":"/private/convertApi/getConvertRecordList",
  "params":{
    "currentPage":1,
    "pageSize":10,
    "params":{
      "status":"0",
      "startTime":"1681889369",
      "endTime":"1681889369",
      "coinType":"USDT",
      "orderId": "369154217945075714"
    }
  }
}
Parameters

Parameter	Required	Type	Enum	Description
currentPage	false	Integer		current page
pageSize	false	Integer		page size
params	false	object		
› status	false	Integer	PROCESSING(0),SUCCESS(1),FAIL(2)	order status
› startTime	false	Date		start time
› endTime	false	Date		end time
› coinType	false	String		coin type
› orderId	false	Long		order id
The above command returns JSON structured like this (real example)

{
  "id": "1",
  "jsonrpc": "2.0",
  "usIn": 1681898422981,
  "usOut": 1681898422991,
  "usDiff": 10,
  "result": {
    "count": 10,
    "total": 1,
    "totalPage": 1,
    "offset": 1,
    "data": [
      {
        "fromAmount": "20",
        "fromCoin": "USDT",
        "toAmount": "0.00068277",
        "toCoin": "BTC",
        "status": 1,
        "createTime": "1681897739884",
        "assetType": "SPOT",
        "realPrice": "0.0000341387787125",
        "inversePrice": "29292.201939",
        "orderId": "369154217945075714"
      }
    ]
  }
}
Response

Name	Type	Enum	Description
count	Long		Number of data per page
total	Long		total data number
totalPage	Long		total pages
offset	Long		current page
result	object		Response data
› assetType	String		user asset Type
› fromAmount	BigDecimal		User spends coin amount
› fromCoin	String		User spends coin type
› toAmount	BigDecimal		user actually got amount
› toCoin	String		user receives coin type
› realPrice	BigDecimal		exchange price
› inversePrice	BigDecimal		inverse price
› status	Int	PROCESSING(0),SUCCESS(1),FAIL(2)	order status
› createTime	Date		order create time
› orderId	String		order id
CMC
Spot summary
Description

Spot summary.
Method

/public/cmc_spot_summary
Request example

https://api.orangex.com/api/v1/public/cmc_spot_summary
Parameters

The above command returns JSON structured like this (real example)

{
  "jsonrpc": "2.0",
  "usIn": 1640013201423,
  "usOut": 1640013201433,
  "usDiff": 10,
  "result": [
    {
      "trading_pairs": "BTC-USDT",
      "last_price": "46151.605",
      "lowest_ask": "46155.81",
      "highest_bid": "48698.516",
      "base_volume": "399.72262999999999997",
      "quote_volume": "18476628.30808085",
      "price_change_percent_24h": "-0.035",
      "highest_price_24h": "47824.176",
      "lowest_price_24h": "46151.605"
    }
  ]
}

Response

Name	Type	Enum	Description
result	Array of object		
› trading_pairs	string		Identifier of a ticker with delimiter to separate base/quote, eg. BTC-USDT (Price of BTC is quoted in USDT).
› last_price	decimal		Last transacted price of base currency based on given quote currency.
› lowest_ask	decimal		Last transacted price of base currency based on given quote currency.
› highest_bid	decimal		Highest bid price of base currency based on given quote currency.
› base_volume	decimal		24-hr volume of market pair denoted in BASE currency.
› quote_volume	decimal		24-hr volume of market pair denoted in QUOTE currency.
› price_change_percent_24h	decimal		24-hr % price change of market pai.
› highest_price_24h	decimal		Highest price of base currency based on given quote currency in the last 24-hrs.
› lowest_price_24h	decimal		Lowest price of base currency based on given quote currency in the last 24-hrs.
Spot ticker
Description

Spot ticker.
Method

/public/cmc_spot_ticker
Request example

https://api.orangex.com/api/v1/public/cmc_spot_ticker
Parameters

The above command returns JSON structured like this (real example)

{
  "jsonrpc": "2.0",
  "usIn": 1640013063339,
  "usOut": 1640013063353,
  "usDiff": 14,
  "result": {
    "BTC-USDT": {
      "last_price": "46013.235",
      "quote_volume": "18417965.89790487",
      "base_volume": "398.44799000000000003",
      "isFrozen": "0"
    }
  }
}
Response

Name	Type	Enum	Description
result	object		
› pair	object		
›› base_volume	decimal		24-hour trading volume denoted in BASE currency.
›› last_price	decimal		Last transacted price of base currency based on given quote currency.
›› quote_volume	decimal		24 hour trading volume denoted in QUOTE currency.
›› isFrozen	string		Indicates if the market is currently enabled (0) or disabled (1).
Spot orderbook
Description

Get orderbook within given instrument.
Method

/public/cmc_spot_orderbook
Request example

https://api.orangex.com/api/v1/public/cmc_spot_orderbook?market_pair=BTC-USDT&depth=100
Parameters

Parameter	Required	Type	Enum	Description
market_pair	true	string		A pair such as “LTC-BTC”
depth	false	string		Orders depth quantity. Not defined or 0 = full order book. Depth = 100 means 50 for each bid/ask side.
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1640007375093,
    "usOut": 1640007375098,
    "usDiff": 5,
    "result": {
        "timestamp": 1640007375097,
        "bids": [
            [
                "32101.57600000",
                "0.22663000"
            ]
        ],
        "asks": [
            [
                "45935.28900000",
                "0.08829000"
            ]
        ],
        "ticker_id": "BTC-USDT"
    }
}
Response

Name	Type	Enum	Description
result	object		
› timestamp	timestamp		Unix timestamp in milliseconds for when the last updated time occurred.
› ticker_id	string		A pair such as "BTC-ETH"
› bids	decimal		An array containing 2 elements. The offer price and quantity for each bid order
› asks	decimal		An array containing 2 elements. The ask price and quantity for each ask order.
Market trades
Description

Get market trades within given instrument.
Method

/public/cmc_market_trades
Request example

https://api.orangex.com/api/v1/public/cmc_market_trades?market_pair=BTC-USDT
Parameters

Parameter	Required	Type	Enum	Description
market_pair	true	string		A pair such as “LTC-BTC”,"BTC-USDT-PERPETUAL"
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1640010582612,
    "usOut": 1640010583370,
    "usDiff": 758,
    "result": [
        {
            "trade_id": 1847753,
            "price": "45617.827",
            "base_volume": "0.08674",
            "quote_volume": "3956.89031398",
            "timestamp": 1640010564816,
            "type": "sell"
        }
    ]
}
Response

Name	Type	Enum	Description
result	object		
› trade_id	integer		A unique ID associated with the trade for the currency pair transaction
› price	decimal		Last transacted price of base currency based on given quote currency
› base_volume	decimal		Transaction amount in BASE currency.
› quote_volume	decimal		Transaction amount in QUOTE currency
› timestamp	timestamp		Unix timestamp in milliseconds for when the transaction occurred.
› type	string	buy,sell	Used to determine whether or not the transaction originated as a buy or sell. Buy – Identifies an ask was removed from the order book.Sell – Identifies a bid was removed from the order book.
Contract
Description

Contracts.
Method

/public/cmc_contracts
Request example

https://api.orangex.com/api/v1/public/cmc_contracts
Parameters

The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1640014365071,
    "usOut": 1640014365187,
    "usDiff": 116,
    "result": [
        {
            "ticker_id": "ETH-25MAR22",
            "base_currency": "ETH",
            "quote_currency": "USDT",
            "last_price": "4159.61169",
            "base_volume": "0",
            "quote_volume": "0",
            "high": "4159.61169",
            "low": "4159.61169",
            "product_type": "future",
            "open_interest": "0",
            "index_price": "3990.09",
            "creation_timestamp": 1635299213113,
            "expiry_timestamp": 1648195200000,
            "contract_type": "Quanto",
            "contract_price": "4159.61169",
            "contract_price_currency": "USDT"
        }
    ]
}

Response

Name	Type	Enum	Description
result	Array of object		
› ticker_id	string		Identifier of a ticker with delimiter to separate base/quote, eg. BTC-USDT-PERPEUR.
› base_currency	string		Symbol/currency code of base pair, eg. BTC.
› quote_currency	string		Symbol/currency code of quote pair, eg. USDT.
› last_price	decimal		Last transacted price of base currency based on given quote currency.
› base_volume	decimal		24 hour trading volume in BASE currency.
› quote_volume	decimal		24 hour trading volume in QUOTE currency.
› bid	decimal		Current highest bid price.
› ask	decimal		Current lowest ask price.
› high	decimal		Rolling 24-hour highest transaction price.
› low	decimal		Rolling 24-hour lowest transaction price.
› product_type	string		Futures, Perpetual, Options.
› open_interest	decimal		The number of outstanding derivatives contracts that have not been settled.
› open_interest_usd	decimal		The sum of the Open Positions (long or short) in USD Value of the contract.
› index_price	decimal		Last calculated index price for underlying of contract.
› creation_timestamp	Long		Start date of derivative (not needed for perpetual swaps).
› expiry_timestamp	Long		End date of derivative (not needed for perpetual swaps).
› funding_rate	decimal		Current funding rate.
› next_funding_rate_timestamp	Long		Timestamp of the next funding rate change.
› contract_type	string		Describes the type of contract - Vanilla, Inverse or Quanto?.
› contract_price	decimal		Describes the price per contract.
› contract_price_currency	string		Describes the currency which the contract is priced in (e.g. USD, EUR, BTC, USDT)
› taker_fee	decimal		Fees for filling a “maker” order
› maker_fee	decimal		Fees for filling a “taker” order
Contract orderbook
Description

Get orderbook within given instrument.
Method

/public/cmc_contract_orderbook
Request example

https://api.orangex.com/api/v1/public/cmc_contract_orderbook?market_pair=BTC-USDT-PERPETUAL&depth=2
Parameters

Parameter	Required	Type	Enum	Description
market_pair	true	string		A pair such as “LTC-BTC”
depth	false	string		Orders depth quantity. Not defined or 0 = full order book. Depth = 100 means 50 for each bid/ask side.
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1640010417114,
    "usOut": 1640010417118,
    "usDiff": 4,
    "result": {
        "timestamp": 1640010417116,
        "bids": [
            [
                "45883.20000000",
                "7.18000000"
            ]
        ],
        "asks": [
            [
                "57294.80000000",
                "2.74000000"
            ]
        ],
        "ticker_id": "BTC-USDT-PERPETUAL"
    }
}
Response

Name	Type	Enum	Description
result	object		
› timestamp	timestamp		Unix timestamp in milliseconds for when the last updated time occurred.
› ticker_id	string		A pair such as "BTC-ETH"
› bids	decimal		An array containing 2 elements. The offer price and quantity for each bid order
› asks	decimal		An array containing 2 elements. The ask price and quantity for each ask order.
CoinGecko
Pairs
Description

The /pairs endpoint provides a summary on cryptoasset trading pairs available on the exchange
Method

/public/coin_gecko_spot_pairs
Request example

https://api.orangex.com/api/v1/public/coin_gecko_spot_pairs
Parameters

The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1640011515216,
    "usOut": 1640011515221,
    "usDiff": 5,
    "result": [
        {
            "ticker_id": "BTC-USDT",
            "base": "BTC",
            "target": "USDT"
        }
    ]
}

Response

Name	Type	Enum	Description
result	object	Identifier of a ticker with delimiter to separate base/target, eg. BTC-ETH	
› ticker_id	string		
› base	string		Symbol/currency code of a the base cryptoasset, eg. BTC
› target	string		Symbol/currency code of the target cryptoasset, eg. ETH,USDT
Spot tickers
Description

Spot tickers.
Method

/public/coin_gecko_spot_ticker
Request example

https://api.orangex.com/api/v1/public/coin_gecko_spot_ticker
Parameters

The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1640013944756,
    "usOut": 1640013944763,
    "usDiff": 7,
    "result": [
        {
            "ticker_id": "BTC-USDT",
            "base_currency": "BTC",
            "target_currency": "USDT",
            "last_price": "46192.975",
            "base_volume": "405.65935000000000002",
            "target_volume": "18750771.58411256",
            "bid": "48698.516",
            "ask": "46268.522",
            "high": "47824.176",
            "low": "45481.536"
        }
    ]
}

Response

Name	Type	Enum	Description
result	Array of object		
› ticker_id	string		Identifier of a ticker with delimiter to separate base/target, eg. BTC-USDT.
› base_currency	string		Symbol/currency code of base pair, eg. BTC.
› target_currency	decimal		Symbol/currency code of target pair, eg. ETH.
› last_price	decimal		Last transacted price of base currency based on given target currency.
› base_volume	decimal		24 hour trading volume in base pair volume.
› target_volume	decimal		24 hour trading volume in target pair volume.
› bid	decimal		Current highest bid price.
› ask	decimal		Current lowest ask price.
› high	decimal		Rolling 24-hours highest transaction price.
› low	decimal		Rolling 24-hours lowest transaction price.
Spot orderbooks
Description

Get orderbook within given spot pair.
Method

/public/coin_gecko_spot_orderbook
Request example

https://api.orangex.com/api/v1/public/coin_gecko_spot_orderbook?ticker_id=BTC-USDT&depth=100
Parameters

Parameter	Required	Type	Enum	Description
ticker_id	true	string		A pair such as “LTC-BTC”
depth	false	string		Orders depth quantity. Not defined or 0 = full order book. Depth = 100 means 50 for each bid/ask side.
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1640007375093,
    "usOut": 1640007375098,
    "usDiff": 5,
    "result": {
        "timestamp": 1640007375097,
        "bids": [
            [
                "32101.57600000",
                "0.22663000"
            ]
        ],
        "asks": [
            [
                "45935.28900000",
                "0.08829000"
            ]
        ],
        "ticker_id": "BTC-USDT"
    }
}
Response

Name	Type	Enum	Description
result	object		
› timestamp	timestamp		Unix timestamp in milliseconds for when the last updated time occurred.
› ticker_id	string		A pair such as "BTC-ETH"
› bids	decimal		An array containing 2 elements. The offer price and quantity for each bid order
› asks	decimal		An array containing 2 elements. The ask price and quantity for each ask order.
History trades
Description

Get market trades within given instrument.
Method

/public/coin_gecko_market_trades
Request example

https://api.orangex.com/api/v1/public/coin_gecko_market_trades?ticker_id=BTC-USDT&type=buy&limit=10&start_time=1640011101596&end_time=1640011101596
Parameters

Parameter	Required	Type	Enum	Description
ticker_id	true	string		A pair such as “LTC-BTC”,"BTC-USDT-PERPETUAL"
type	false	string	buy,sell	To indicate nature of trade - buy/sell
limit	false	string		Number of historical trades to retrieve from time of query. [0, 200, 500...]. 0 returns full history.
start_time	false	date		Start time from which to query historical trades from
end_time	false	date		End time for historical trades query
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1640011141970,
    "usOut": 1640011142136,
    "usDiff": 166,
    "result": [
        {
            "trade_id": 1847919,
            "price": "45869.323",
            "base_volume": "0.05117",
            "target_volume": "2347.13325791",
            "trade_timestamp": 1640011101596,
            "type": "buy"
        }
    ]
}
Response

Name	Type	Enum	Description
result	object		
› trade_id	integer		A unique ID associated with the trade for the currency pair transaction
› price	decimal		Transaction price in base pair volume.
› base_volume	decimal		Transaction amount in base pair volume.
› target_volume	decimal		Transaction amount in target pair volume
› timestamp	timestamp		Unix timestamp in milliseconds for when the transaction occurred.
› type	string	buy,sell	Used to determine whether or not the transaction originated as a buy or sell. Buy – Identifies an ask was removed from the order book.Sell – Identifies a bid was removed from the order book.
Contracts
Description

Contracts.
Method

/public/coin_gecko_contracts
Request example

https://api.orangex.com/api/v1/public/coin_gecko_contracts
Parameters

The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1640014583640,
    "usOut": 1640014583666,
    "usDiff": 26,
    "result": [
        {
            "ticker_id": "BTC-USDT-PERPETUAL",
            "base_currency": "BTC",
            "target_currency": "BTC",
            "last_price": "47670.7",
            "base_volume": "5.35",
            "target_volume": "273052.8771766",
            "bid": "47936.8",
            "ask": "57294.8",
            "high": "57294.8",
            "low": "45000",
            "product_type": "perpetual",
            "open_interest": "297.63",
            "index_price": "46120.44848773",
            "index_name": "BTC-USDT",
            "index_currency": "BTC",
            "start_timestamp": 1635246428154,
            "funding_rate": "0.0001",
            "next_funding_rate_timestamp": 1440000,
            "contract_type": "Quanto",
            "contract_price": "47670.7",
            "contract_price_currency": "BTC"
        }
    ]
}

Response

Name	Type	Enum	Description
result	Array of object		
› ticker_id	string		Identifier of a ticker with delimiter to separate base/quote, eg. BTC-USDT-PERPEUR.
› base_currency	string		Symbol/currency code of base pair, eg. BTC.
› target_currency	string		Symbol/currency code of quote pair, eg. USDT.
› last_price	decimal		Last transacted price of base currency based on given quote currency.
› base_volume	decimal		24 hour trading volume in BASE currency.
› target_volume	decimal		24 hour trading volume in QUOTE currency.
› bid	decimal		Current highest bid price.
› ask	decimal		Current lowest ask price.
› high	decimal		Rolling 24-hour highest transaction price.
› low	decimal		Rolling 24-hour lowest transaction price.
› product_type	string		Futures, Perpetual, Options.
› open_interest	decimal		The number of outstanding derivatives contracts that have not been settled.
› index_price	decimal		Last calculated index price for underlying of contract.
› index_name	string		Name of the underlying index if any.
› index_currency	decimal		Underlying currency for index
› start_timestamp	Long		Start date of derivative (not needed for perpetual swaps).
› end_timestamp	Long		End date of derivative (not needed for perpetual swaps).
› funding_rate	decimal		Current funding rate.
› next_funding_rate	decimal		Upcoming predicted funding rate.
› next_funding_rate_timestamp	Long		Timestamp of the next funding rate change.
› contract_type	string		Describes the type of contract - Vanilla, Inverse or Quanto?.
› contract_price	decimal		Describes the price per contract.
› contract_price_currency	string		Describes the currency which the contract is priced in (e.g. USD, EUR, BTC, USDT)
Contract orderbooks
Description

Get orderbook within given instrument.
Method

/public/coin_gecko_contract_orderbook
Request example

https://api.orangex.com/api/v1/public/coin_gecko_contract_orderbook?ticker_id=BTC-USDT-PERPETUAL&depth=10
Parameters

Parameter	Required	Type	Enum	Description
ticker_id	true	string		A pair such as “BTC-USDT-PERPETUAL”
depth	false	string		Orders depth quantity. Not defined or 0 = full order book. Depth = 100 means 50 for each bid/ask side.
The above command returns JSON structured like this (real example)

{
    "jsonrpc": "2.0",
    "usIn": 1640007375093,
    "usOut": 1640007375098,
    "usDiff": 5,
    "result": {
        "timestamp": 1640007375097,
        "bids": [
            [
                "32101.57600000",
                "0.22663000"
            ]
        ],
        "asks": [
            [
                "45935.28900000",
                "0.08829000"
            ]
        ],
        "ticker_id": "BTC-USDT-PERPETUAL"
    }
}
Response

Name	Type	Enum	Description
result	object		
› timestamp	timestamp		Unix timestamp in milliseconds for when the last updated time occurred.
› ticker_id	string		A pair such as "BTC-ETH"
› bids	decimal		An array containing 2 elements. The offer price and quantity for each bid order
› asks	decimal		An array containing 2 elements. The ask price and quantity for each ask order.