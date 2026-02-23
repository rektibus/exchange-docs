Get Started For Programmers
Welcome to the Lighter SDK and API Introduction. Here, we will go through everything from the system setup, to creating and cancelling all types of orders, to fetching exchange data. To keep up to date with Lighter's API, join this Telegram Channel or #api-updates on our Discord.

Setting up an API KEY
In order to get started using the Lighter API, you must first set up an API_KEY_PRIVATE_KEY, as you will need it to sign any transaction you want to make. You can find how to do it in the following example. The BASE_URL will reflect if your key is generated on testnet or mainnet (for mainnet, just change the BASE_URL in the example to https://mainnet.zklighter.elliot.ai). Note that you may also need to provide your ETH_PRIVATE_KEY.

You can create up to 252 API keys (3 <= API_KEY_INDEX <= 254). The 0 index is the one reserved for the desktop, 1 for the mobile PWA, and 2 is reserved for the mobile app. Finally, the 255 index can be used as a value for the api_key_index parameter of the apikeys method of the AccountApi for getting the data about all the API keys.

In case you do not know your ACCOUNT_INDEX, you can find it by querying the AccountApi for the data about your account, as shown in this example.

Account types
Lighter API users can operate under a Standard or Premium accounts. The Standard account is fee-free. Premium accounts pay 0.2 bps maker and 2 bps taker fees. Find out more in Account Types.

The Signer
In order to create a transaction (create/cancel/modify order), you need to use the SignerClient. Initialize with the following code:

Initialize SignerClient

 client = lighter.SignerClient(  
        url=BASE_URL,  
        api_private_keys={API_KEY_INDEX:PRIVATE_KEY},  
        account_index=ACCOUNT_INDEX
    )
The code for the signer can be found in the same repo, in the signer_client.py file. You may notice that it uses a binary for the signer: the code for it can be found in the lighter-go public repo, and you can compile it yourself using the justfile.

Nonce
When signing a transaction, you may need to provide a nonce (number used once). A nonce needs to be incremented each time you sign something. You can get the next nonce that you need to use using the TransactionApi’s next_nonce method or take care of incrementing it yourself. Note that each nonce is handled per API_KEY.

Signing a transaction
One can sign a transaction using the SignerClient’s sign_create_order, sign_modify_order, sign_cancel_order and its other similar methods. For actually pushing the transaction, you need to call send_tx or send_tx_batch using the TransactionApi. Here’s an example that includes such an operation.

Note that base_amount, price are to be passed as integers, and client_order_index is a unique (across all markets) identifier you provide for you to be able to reference this order later (e.g. if you want to cancel it).

The following values can be provided for the order_type parameter:

ORDER_TYPE_LIMIT
ORDER_TYPE_MARKET
ORDER_TYPE_STOP_LOSS
ORDER_TYPE_STOP_LOSS_LIMIT
ORDER_TYPE_TAKE_PROFIT
ORDER_TYPE_TAKE_PROFIT_LIMIT
ORDER_TYPE_TWAP
The following values can be provided for the time_in_force parameter:

ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL
ORDER_TIME_IN_FORCE_GOOD_TILL_TIME
ORDER_TIME_IN_FORCE_POST_ONLY
Signer Client Useful Wrapper Functions
The SignerClient provides several functions that sign and push a type of transaction. Here’s a list of some of them:

create_order - signs and pushes a create order transaction;
create_market_order - signs and pushes a create order transaction for a market order;
create_cancel_order - signs and pushes a cancel transaction for a certain order. Note that the order_index needs to equal the client_order_index of the order to cancel;
cancel_all_orders - signs and pushes a cancel all transactions. Note that, depending on the time_in_force provided, the transaction has different consequences:
ORDER_TIME_IN_FORCE_IMMEDIATE_OR_CANCEL - ImmediateCancelAll;
ORDER_TIME_IN_FORCE_GOOD_TILL_TIME - ScheduledCancelAll;
ORDER_TIME_IN_FORCE_POST_ONLY - AbortScheduledCancelAll.
create_auth_token_with_expiry - creates an auth token (useful for getting data using the Api and Ws methods)
API
The SDK provides API classes that make calling the Lighter API easier. Here are some of them and the most important of their methods:

AccountApi - provides account data
account - get account data either by l1_address or index
accounts_by_l1_address - get data about all the accounts (master account and subaccounts)
apikeys - get data about the api keys of an account (use api_key_index = 255 for getting data about all the api keys)
TransactionApi - provides transaction related data
next_nonce - get next nonce to be used for signing a transaction using a certain api key
send_tx - push a transaction
send_tx_batch - push several transactions at once
OrderApi - provides data about orders, trades and the orderbook
order_book_details - get data about a specific market’s orderbook
order_books - get data about all markets’ orderbooks
You can find the rest here. We also provide an example showing how to use some of these. For the methods that require an auth token, you can generate one using the create_auth_token_with_expiry method of the SignerClient (the same applies to the websockets auth).

WebSockets
Lighter also provides access to essential info using websockets. A simple version of an WsClient for subscribing to account and orderbook updates is implemented here. You can also take it as an example implementation of such a client.

To get access to more data, you will need to connect to the websockets without the provided WsClient. You can find the streams you can connect to, how to connect, and the data they provide in the websockets section.

Public Python SDK for Lighter:

https://github.com/elliottech/lighter-python

Public Go SDK for Lighter:

https://github.com/elliottech/lighter-go
API keys
You can use API keys to trade and manage your lighter account programmatically. Each API key will be assigned an index, ranging from 0 to 254 - indexes 0, and 1 are reserved for desktop and mobile interfaces.

Each internal account, whether that's a master account or a sub-account, will have its own separate API key index - and each comes with a public & private key, and its own nonce.

Permissions
API keys enable both write and read permissions, allowing you to query auth-gated REST endpoints and Websocket channel, but also send transactions and process withdrawals.

While it allows to process withdrawals, you should consider that only secure withdrawals can be executed without also providing the account's Ethereum private key - as they can only be sent to the same L1 address that created the account. On the other hand, Fast Withdrawals and Transfers can be sent to other L1 addresses and will require the wallet's private key.

Authentication
To interact with certain endpoints, you will need to generate an auth token using your API private key. You can do so using our GO SDK, or use the create_auth_token_with_expiry() function in our Python SDK. Each auth code can have a maximum expiry of 8 hours, and it uses the following structure: {expiry_unix}:{account_index}:{api_key_index}:{random_hex}.

Read-only Authentication
Using a canonical auth code, you can generate read-only auth tokens - those won't allow placing trades nor request withdrawals (essentially, you won't be able to sign transactions hence initialize a signer client), but you will be able to access auth-gated data via API. Each read-only auth code can have a maximum expiry of 10 years, and a minimum of 1 day. They will use the following structure: ro:{account_index}:{single|all}:{expiry_unix}:{random_hex}. You can generate one using the createToken endpoint, or via front-end.

How to create API keys programmatically
You can create new keys programmatically using either the Python SDK, or the GO SDK. While generating the API keys does not require your L1 private key, associating them with your Lighter account does. You can either do this via the SDKs, or interact with Lighter's smart contract directly using the ChangePubKey function (this is particularly helpful if you're running a multi-sig).

Nonce management
Each API key will have its own nonce, and the API servers require it to be increased by 1 for each transaction you submit. While the Python SDK handles nonce management on its own, you might want to manage it locally to handle more complex systems. Since some types of transactions may be subject to speed bumps based on your account type, and they are processed sequentially, you may want to use multiple API keys for the same account e.g. one for each type of order to always guarantee the fastest execution.

Rate Limits
We enforce rate limits on both REST API and WebSocket usage. These limits applies on both IP address and L1 wallet address. If you send transactions via Websocket, you will share the same rate limits the REST API uses.

REST API Endpoint Limits
The following limits apply to the https://mainnet.zklighter.elliot.ai/ base URL, different limits (listed further below) apply to https://explorer.elliot.ai/.

Premium Account users have limit of 24000 weighted REST API requests per minute window, while Standard Account users 60 per minute.

ThesendTx and sendTxBatch transaction types are the only types of transactions that can increase in quota (see Volume Quota ), which are used to create and modify orders. All other endpoints are have a set limit of tx per minute and do not increase with volume.

Weights per endpoint are the following:

/api/v1/sendTx, /api/v1/sendTxBatch, /api/v1/nextNonce
Per User: 6
/api/v1/publicPools,/api/v1/txFromL1TxHash
Per User: 50
/api/v1/accountInactiveOrders, /api/v1/deposit/latest
Per User: 100
/api/v1/apikeys
Per User: 150
/api/v1/transferFeeInfo
Per User: 500
/api/v1/trades, /api/v1/recentTrades
Per User: 600
/api/v1/changeAccountTier, /api/v1/tokens/create, /api/v1/tokens/revoke, /api/v1/airdrop/create, /api/v1/setAccountMetadata, /api/v1/notification/ack, /api/v1/createIntentAddress, /api/v1/fastwithdraw, /api/v1/referral/create, /api/v1/referral/use, /api/v1/referral/update, /api/v1/referral/kickback/update
Per User: 3000
Other endpoints not listed above are limited to:

Per User: 300
Standard Tier Rate Limit
Requests from a single IP address and L1 wallet address are capped at:

60 requests per minute under the Standard Account
Explorer REST API Endpoint Limits
The following limits apply to the https://explorer.elliot.ai/ Base URL.

Standard Users and Premium Users have the same limit of 90 weighted requests per minute window.

Weights per endpoint are the following:

/api/search
Per User: 3
/api/accounts/param/positions, /api/accounts/param/logs
Per User: 2
Other endpoints not listed above are limited to:

Per User: 1
WebSocket Limits
To prevent resource exhaustion, we enforce the following usage limits per IP:

Connections: 100
Subscriptions per connection: 100
Total Subscriptions: 1000
Max Connections Per Minute: 60 (not to be confused with channel subscriptions)
Max Messages Sent Per Minute: 200 (sendTx and sendBatchTx are not counted here, and follow the same limits as REST requests)
Max Inflight Messages: 50
Unique Accounts: 10
Additionally, every connection is automatically dropped after 24 hours. It's recommended to have proper reconnection logic, in addition to ping/pong logic.

Transaction Type Limits (per user)
These limits applied for only Standard Accounts.

Transaction Type	Limit
Default	40 requests / minute
L2Withdraw	2 requests / minute
L2UpdateLeverage	1 request / minute
L2CreateSubAccount	2 requests / minute
L2CreatePublicPool	2 requests / minute
L2ChangePubKey	2 requests / 10 seconds
L2Transfer	1 request / minute
Rate Limit Exceeding Behavior
If you exceed any rate limit:

You will receive an HTTP 429 Too Many Requests error.
For WebSocket connections, excessive messages may result in disconnection.
To avoid this, please ensure your clients are implementing proper backoff and retry strategies.

WebSocket
This page will help you get started with zkLighter WebSocket server.

Connection
URL: wss://mainnet.zklighter.elliot.ai/stream; wss://testnet.zklighter.elliot.ai/stream

You can directly connect to the WebSocket server using wscat:

Shell

wscat -c 'wss://mainnet.zklighter.elliot.ai/stream'
If you're connecting from a restricted region, you can still access read-only data:

Shell

wscat -c 'wss://mainnet.zklighter.elliot.ai/stream?readonly=true'
Send Tx
You can send transactions using the websocket as follows:

JSON

{
    "type": "jsonapi/sendtx",
    "data": {
        "tx_type": INTEGER,
        "tx_info": ...
    }
}
The tx_type options can be found in the SignerClient file, while tx_info can be generated using the sign methods in the SignerClient.

Example: ws_send_tx.py

Send Batch Tx
You can send batch transactions to execute up to 50 transactions in a single message.

JSON

{
    "type": "jsonapi/sendtxbatch",
    "data": {
        "tx_types": "[INTEGER]",
        "tx_infos": "[tx_info]"
    }
}
The tx_type options can be found in the SignerClient file, while tx_info can be generated using the sign methods in the SignerClient.

Example: ws_send_batch_tx.py

Types
We first need to define some types that appear often in the JSONs.

Transaction JSON
To decode event_info, you can refer to Data Structures.

JSON

Transaction = {
    "hash": STRING,
    "type": INTEGER,
    "info": STRING, // json object as string, attributes depending on the tx type
    "event_info": STRING, // json object as string, attributes depending on the tx type
    "status": INTEGER,
    "transaction_index": INTEGER,
    "l1_address": STRING,
    "account_index": INTEGER,
    "nonce": INTEGER,
    "expire_at": INTEGER,
    "block_height": INTEGER,
    "queued_at": INTEGER,
    "executed_at": INTEGER,
    "sequence_index": INTEGER,
    "parent_hash": STRING,
		"transaction_time": INTEGER
}
Example:

JSON

{
    "hash": "0xabc123456789def",
    "type": 15,
    "info": "{\"AccountIndex\":1,\"ApiKeyIndex\":2,\"MarketIndex\":3,\"Index\":404,\"ExpiredAt\":1700000000000,\"Nonce\":1234,\"Sig\":\"0xsigexample\"}",
    "event_info": "{\"a\":1,\"i\":404,\"u\":123,\"ae\":\"\"}",
    "status": 2,
    "transaction_index": 10,
    "l1_address": "0x123abc456def789",
    "account_index": 101,
    "nonce": 12345,
    "expire_at": 1700000000000,
    "block_height": 1500000,
    "queued_at": 1699999990000,
    "executed_at": 1700000000005,
    "sequence_index": 5678,
    "parent_hash": "0xparenthash123456",
		"transaction_time": INTEGER
}
Used in: Account Tx.

Order JSON
JSON

Order = {
    "order_index": INTEGER,
    "client_order_index": INTEGER,
    "order_id": STRING, // same as order_index but string
    "client_order_id": STRING, // same as client_order_index but string
    "market_index": INTEGER,
    "owner_account_index": INTEGER,
    "initial_base_amount": STRING,
    "price": STRING,
    "nonce": INTEGER,
    "remaining_base_amount": STRING,
    "is_ask": BOOL,
    "base_size": INTEGER,
    "base_price": INTEGER,
    "filled_base_amount": STRING,
    "filled_quote_amount": STRING,
    "side": STRING,
    "type": STRING,
    "time_in_force": STRING,
    "reduce_only": BOOL,
    "trigger_price": STRING,
    "order_expiry": INTEGER,
    "status": STRING,
    "trigger_status": STRING,
    "trigger_time": INTEGER,
    "parent_order_index": INTEGER,
    "parent_order_id": STRING,
    "to_trigger_order_id_0": STRING,
    "to_trigger_order_id_1": STRING,
    "to_cancel_order_id_0": STRING,
    "block_height": INTEGER,
    "timestamp": INTEGER,
		"created_at": INTEGER,
		"updated_at": INTEGER,
		"transaction_time": INTEGER
}
Used in: Account Market, Account All Orders, Account Orders.

Trade JSON
JSON

Trade = {
    "trade_id": INTEGER,
    "tx_hash": STRING,
    "type": STRING,
    "market_id": INTEGER,
    "size": STRING,
    "price": STRING,
    "usd_amount": STRING,
    "ask_id": INTEGER,
    "bid_id": INTEGER,
    "ask_account_id": INTEGER,
    "bid_account_id": INTEGER,
    "is_maker_ask": BOOLEAN,
    "block_height": INTEGER,
    "timestamp": INTEGER,
    "taker_fee": INTEGER (omitted when zero),
    "taker_position_size_before": STRING (omitted when empty),
    "taker_entry_quote_before": STRING (omitted when empty),
    "taker_initial_margin_fraction_before": INTEGER (omitted when zero),
    "taker_position_sign_changed": BOOL (omitted when false),
    "maker_fee": INTEGER (omitted when zero),
    "maker_position_size_before": STRING (omitted when empty),
    "maker_entry_quote_before": STRING (omitted when empty),
    "maker_initial_margin_fraction_before": INTEGER (omitted when zero),
    "maker_position_sign_changed": BOOL (omitted when false),
		"transaction_time": INTEGER,
}
Example:

JSON

{
    "trade_id": 401,
    "tx_hash": "0xabc123456789",
    "type": "buy",
    "market_id": 101,
    "size": "0.5",
    "price": "20000.00",
    "usd_amount": "10000.00",
    "ask_id": 501,
    "bid_id": 502,
    "ask_account_id": 123456,
    "bid_account_id": 654321,
    "is_maker_ask": true,
    "block_height": 1500000,
    "timestamp": 1700000000,
    "taker_position_size_before":"1.14880",
    "taker_entry_quote_before":"136130.046511",
    "taker_initial_margin_fraction_before":500,
    "maker_position_size_before":"-0.02594",
    "maker_entry_quote_before":"3075.396750",
    "maker_initial_margin_fraction_before":400,
		"transaction_time": INTEGER
}
Used in: Trade, Account All, Account Market, Account All Trades.

Position JSON
JSON

Position = {
    "market_id": INTEGER,
    "symbol": STRING,
    "initial_margin_fraction": STRING,
    "open_order_count": INTEGER,
    "pending_order_count": INTEGER,
    "position_tied_order_count": INTEGER,
    "sign": INTEGER,
    "position": STRING,
    "avg_entry_price": STRING,
    "position_value": STRING,
    "unrealized_pnl": STRING,
    "realized_pnl": STRING,
    "liquidation_price": STRING,
    "total_funding_paid_out": STRING (omitted when empty),
    "margin_mode": INT,
    "allocated_margin": STRING,
}
Example:

JSON

{
    "market_id": 101,
    "symbol": "BTC-USD",
    "initial_margin_fraction": "0.1",
    "open_order_count": 2,
    "pending_order_count": 1,
    "position_tied_order_count": 3,
    "sign": 1,
    "position": "0.5",
    "avg_entry_price": "20000.00",
    "position_value": "10000.00",
    "unrealized_pnl": "500.00",
    "realized_pnl": "100.00",
    "liquidation_price": "3024.66",
    "total_funding_paid_out": "34.2",
    "margin_mode": 1,
    "allocated_margin": "46342",
}
Used in: Account All, Account Market, Account All Positions.

PoolShares JSON
JSON

PoolShares = {
    "public_pool_index": INTEGER,
    "shares_amount": INTEGER,
    "entry_usdc": STRING
}
Example:

JSON

{
    "public_pool_index": 1,
    "shares_amount": 100,
    "entry_usdc": "1000.00"
}
Used in: Account All, Account All Positions.

Asset JSON
JSON

Asset = {
  "symbol": STRING,
  "asset_id": INTEGER,
  "balance": STRING,
  "locked_balance": STRING
}
Example:

JSON

Asset = {
      "symbol": "ETH",
      "asset_id": 1,
      "balance": "6691.4917",
      "locked_balance": "564.6135"
}
Used in: Account All Assets, Account Market, Account All.

Channels
To unsubscribe from a channel, use the following syntax:

JSON

{
    "type": "unsubscribe",
    "channel": STRING
}
Order Book
The order book channel sends the new ask and bid orders for the given market in batches, every 50ms. While the nonce is tied to Lighter's matching engine, the offset is tied to the API servers; hence, you can expect the offset to change drastically on reconnection if you're routed to a different server. Regardless, on each update the offset will increase, but it's not guaranteed to be continuous. Additionally, this channel sends a complete snapshot on subscription, but only state changes after that. To verify the continuity of the data, you can check that begin_nonce on the current update matches the nonce (i.e. last_nonce) of the previous update.

JSON

{
    "type": "subscribe",
    "channel": "order_book/{MARKET_INDEX}"
}
Example Subscription

JSON

{
    "type": "subscribe",
    "channel": "order_book/0"
}
Response Structure

JSON

{
    "channel": "order_book:{MARKET_INDEX}",
    "offset": INTEGER,
    "order_book": {
        "code": INTEGER,
        "asks": [
            {
                "price": STRING,
                "size": STRING
            }
        ],
        "bids": [
            {
                "price": STRING,
                "size": STRING
            }
        ],
      	"offset": INTEGER,
        "nonce": INTEGER,
				"begin_nonce": INTEGER
    },
		"timestamp": INTEGER,
    "type": "update/order_book"
}
Example Response

JSON

{
    "channel": "order_book:0",
    "offset": 41692864,
    "order_book": {
        "code": 0,
        "asks": [
            {
                "price": "3327.46",
                "size": "29.0915"
            }
        ],
        "bids": [
            {
                "price": "3338.80",
                "size": "10.2898"
            }
        ],
        "offset": 41692864,
				"nonce": 4037957053,
				"begin_nonce": 4037957034
    },
		"timestamp": 1766434222583,
    "type": "update/order_book"
}
Market Stats
The market stats channel sends the market stat data for a given market. current_funding_rate is an estimation of the upcoming funding payment, while funding_rate represents the last funding payment that occurred (at funding_timestamp).

JSON

{
    "type": "subscribe",
    "channel": "market_stats/{MARKET_INDEX}"
}
or

JSON

{
    "type": "subscribe",
    "channel": "market_stats/all"
}
Example Subscription

JSON

{
    "type": "subscribe",
    "channel": "market_stats/0"
}
Response Structure

JSON

{
    "channel": "market_stats:{MARKET_INDEX}",
    "market_stats": {
        "symbol": STRING,
        "market_id": INTEGER,
        "index_price": STRING,
        "mark_price": STRING,
        "open_interest": STRING,
        "open_interest_limit": STRING,
        "funding_clamp_small": STRING,
        "funding_clamp_big": STRING,
        "last_trade_price": STRING,
      	"current_funding_rate": STRING,
        "funding_rate": STRING,
        "funding_timestamp": INTEGER,
        "daily_base_token_volume": FLOAT,
        "daily_quote_token_volume": FLOAT,
        "daily_price_low": FLOAT,
        "daily_price_high": FLOAT,
        "daily_price_change": FLOAT
    },
    "type": "update/market_stats"
}
Example Response

JSON

{
   "channel":"market_stats:0",
   "market_stats":{
      "symbol":"ETH",
      "market_id":0,
      "index_price":"2965.30",
      "mark_price":"2963.63",
      "open_interest":"185926683.471886",
      "open_interest_limit":"72057594037927936.000000",
      "funding_clamp_small":"0.0500",
      "funding_clamp_big":"4.0000",
      "last_trade_price":"2963.67",
      "current_funding_rate":"-0.0005",
      "funding_rate":"0.0011",
      "funding_timestamp":1769187600001,
      "daily_base_token_volume":296009.9355,
      "daily_quote_token_volume":870882976.341333,
      "daily_price_low":2888.37,
      "daily_price_high":2984,
      "daily_price_change":0.830824189844348
   },
   "type":"update/market_stats"
}
Trade
The trade channel sends the new trade data for the given market.

JSON

{
    "type": "subscribe",
    "channel": "trade/{MARKET_INDEX}"
}
Example Subscription

JSON

{
    "type": "subscribe",
    "channel": "trade/0"
}
Response Structure

JSON

{
    "channel": "trade:{MARKET_INDEX}",
    "trades": [Trade]
    ],
    "type": "update/trade"
}
Example Response

JSON

{
    "channel": "trade:0",
    "trades": [
        {
            "trade_id": 14035051,
            "tx_hash": "189068ebc6b5c7e5efda96f92842a2fafd280990692e56899a98de8c4a12a38c",
            "type": "trade",
            "market_id": 0,
            "size": "0.1187",
            "price": "3335.65",
            "usd_amount": "13.67",
            "ask_id": 41720126,
            "bid_id": 41720037,
            "ask_account_id": 2304,
            "bid_account_id": 21504,
            "is_maker_ask": false,
            "block_height": 2204468,
            "timestamp": 1722339648
        }
    ],
    "type": "update/trade"
}
Account All
The account all channel sends specific account market data for all markets. On every new subscription message sent, you will reconnect and receive a new snapshot.

JSON

{
    "type": "subscribe",
    "channel": "account_all/{ACCOUNT_ID}"
}
Example Subscription

JSON

{
    "type": "subscribe",
    "channel": "account_all/1"
}
Response Structure

JSON

{
    "account": INTEGER,
    "assets": [Asset],
    "channel": "account_all:{ACCOUNT_ID}",
    "daily_trades_count": INTEGER,
    "daily_volume": INTEGER,
    "weekly_trades_count": INTEGER,
    "weekly_volume": INTEGER,
    "monthly_trades_count": INTEGER,
    "monthly_volume": INTEGER,
    "total_trades_count": INTEGER,
    "total_volume": INTEGER,
    "funding_histories": {
        "{MARKET_INDEX}": [
        {
          "timestamp": INTEGER,
          "market_id": INTEGER,
          "funding_id": INTEGER,
          "change": STRING,
          "rate": STRING,
          "position_size": STRING,
          "position_side": STRING
        }
      ]
    },
    "positions": {
        "{MARKET_INDEX}": [Position]
    },
    "shares": [PoolShares],
    "trades": {
        "{MARKET_INDEX}": [Trade]
    },
    "type": "update/account_all"
}
Example Response

JSON

{
   "account": 10,
   "assets": {
      "1": {
         "symbol":"ETH",
         "asset_id":1,
         "balance":"1",
         "locked_balance":"0.00000000"
      }
   },
    "channel": "account_all:10",
    "daily_trades_count": 123,
    "daily_volume": 234,
    "weekly_trades_count": 345,
    "weekly_volume": 456,
    "monthly_trades_count": 567,
    "monthly_volume": 678,
    "total_trades_count": 891,
    "total_volume": 912,
    "funding_histories": {
        "1": [
            {
                "timestamp": 1700000000,
                "market_id": 101,
                "funding_id": 2001,
                "change": "0.001",
                "rate": "0.0001",
                "position_size": "0.5",
                "position_side": "long"
            }
        ]
    },
    "positions": {
        "1": {
            "market_id": 101,
            "symbol": "BTC-USD",
            "initial_margin_fraction": "0.1",
            "open_order_count": 2,
            "pending_order_count": 1,
            "position_tied_order_count": 3,
            "sign": 1,
            "position": "0.5",
            "avg_entry_price": "20000.00",
            "position_value": "10000.00",
            "unrealized_pnl": "500.00",
            "realized_pnl": "100.00",
            "liquidation_price": "3024.66",
            "total_funding_paid_out": "34.2",
            "margin_mode": 1,
            "allocated_margin": "46342",
        }
    },
    "shares": [
        {
            "public_pool_index": 1,
            "shares_amount": 100,
            "entry_usdc": "1000.00"
        }
    ],
    "trades": {
        "1": [
            {
                "trade_id": 401,
                "tx_hash": "0xabc123456789",
                "type": "buy",
                "market_id": 101,
                "size": "0.5",
                "price": "20000.00",
                "usd_amount": "10000.00",
                "ask_id": 501,
                "bid_id": 502,
                "ask_account_id": 123456,
                "bid_account_id": 654321,
                "is_maker_ask": true,
                "block_height": 1500000,
                "timestamp": 1700000000,
                "taker_position_size_before":"1.14880",
                "taker_entry_quote_before":"136130.046511",
                "taker_initial_margin_fraction_before":500,
                "maker_position_size_before":"-0.02594",
                "maker_entry_quote_before":"3075.396750",
                "maker_initial_margin_fraction_before":400
            }
        ]
    },
    "type": "update/account"
}
Account Market
The account market channel sends specific account market data for a market. If {MARKET_ID} is a perpetual market, assets will return null, if {MARKET_ID} is a spot market, funding_history will return null.

JSON

{
    "type": "subscribe",
    "channel": "account_market/{MARKET_ID}/{ACCOUNT_ID}",
    "auth": "{AUTH_TOKEN}"
}
Example Subscription

JSON

{
    "type": "subscribe",
    "channel": "account_market/0/40",
    "auth": "{AUTH_TOKEN}"
}
Response Structure

JSON

{
    "account": INTEGER,
    "assets": [Asset],
    "channel": "account_market/{MARKET_ID}/{ACCOUNT_ID}",
    "funding_history": {
        "timestamp": INTEGER,
        "market_id": INTEGER,
        "funding_id": INTEGER,
        "change": STRING,
        "rate": STRING,
        "position_size": STRING,
        "position_side": STRING
        },
    "orders": [Order],
    "position": [Position],
    "trades": [Trade],
    "type": "update/account_market"
}
Account Stats
The account stats channel sends account stats data for the specific account.

JSON

{
    "type": "subscribe",
    "channel": "user_stats/{ACCOUNT_ID}"
}
Example Subscription

JSON

{
    "type": "subscribe",
    "channel": "user_stats/0"
}
Response Structure

JSON

{
    "channel": "user_stats:{ACCOUNT_ID}",
    "stats": {
        "collateral": STRING,
        "portfolio_value": STRING,
        "leverage": STRING,
        "available_balance": STRING,      
        "margin_usage": STRING,
        "buying_power": STRING,        
				"cross_stats":{
           "collateral": STRING,
           "portfolio_value": STRING,
           "leverage": STRING,
           "available_balance": STRING,
           "margin_usage": STRING,
           "buying_power": STRING
        },
        "total_stats":{
           "collateral": STRING,
           "portfolio_value": STRING,
           "leverage": STRING,
           "available_balance": STRING,
           "margin_usage": STRING,
           "buying_power": STRING
        }

    },
    "type": "update/user_stats"
}
Example Response

JSON

{
    "channel": "user_stats:10",
    "stats": {
        "collateral": "5000.00",
        "portfolio_value": "15000.00",
        "leverage": "3.0",
        "available_balance": "2000.00",
        "margin_usage": "0.80",
        "buying_power": "4000.00",
        "cross_stats":{
           "collateral":"0.000000",
           "portfolio_value":"0.000000",
           "leverage":"0.00",
           "available_balance":"0.000000",
           "margin_usage":"0.00",
           "buying_power":"0"
        },
        "total_stats":{
           "collateral":"0.000000",
           "portfolio_value":"0.000000",
           "leverage":"0.00",
           "available_balance":"0.000000",
           "margin_usage":"0.00",
           "buying_power":"0"
        }
    },
    "type": "update/user_stats"
}
Account Tx
This channel sends transactions related to a specific account.

JSON

{
    "type": "subscribe",
    "channel": "account_tx/{ACCOUNT_ID}",
    "auth": "{AUTH_TOKEN}"
}
Response Structure

JSON

{
    "channel": "account_tx:{ACCOUNT_ID}",
    "txs": [Account_tx],
    "type": "update/account_tx"
}
Account All Orders
The account all orders channel sends data about all the orders of an account.

JSON

{
    "type": "subscribe",
    "channel": "account_all_orders/{ACCOUNT_ID}",
    "auth": "{AUTH_TOKEN}"
}
Response Structure

JSON

{
    "channel": "account_all_orders:{ACCOUNT_ID}",
    "orders": {
        "{MARKET_INDEX}": [Order]
    },
    "type": "update/account_all_orders"
}
Height
Blockchain height updates

JSON

{
    "type": "subscribe",
    "channel": "height",
}
Response Structure

JSON

{
    "channel": "height",
    "height": INTEGER,
    "type": "update/height"
}
Pool data
Provides data about pool activities: trades, orders, positions, shares and funding histories.

JSON

{
    "type": "subscribe",
    "channel": "pool_data/{ACCOUNT_ID}",
    "auth": "{AUTH_TOKEN}"
}
Response Structure

JSON

{
    "channel": "pool_data:{ACCOUNT_ID}",
    "account": INTEGER,
    "trades": {
        "{MARKET_INDEX}": [Trade]
    },
    "orders": {
        "{MARKET_INDEX}": [Order]
    },
    "positions": {
        "{MARKET_INDEX}": Position
    },
    "shares": [PoolShares],
    "funding_histories": {
        "{MARKET_INDEX}": [PositionFunding]
    },
    "type": "subscribed/pool_data"
}
Pool info
Provides information about pools.

JSON

{
    "type": "subscribe",
    "channel": "pool_info/{ACCOUNT_ID}",
    "auth": "{AUTH_TOKEN}"
}
Response Structure

JSON

{
    "channel": "pool_info:{ACCOUNT_ID}",
    "pool_info": {
        "status": INTEGER,
        "operator_fee": STRING,
        "min_operator_share_rate": STRING,
        "total_shares": INTEGER,
        "operator_shares": INTEGER,
        "annual_percentage_yield": FLOAT,
        "daily_returns": [
            {
                "timestamp": INTEGER,
                "daily_return": FLOAT
            }
        ],
        "share_prices": [
            {
                "timestamp": INTEGER,
                "share_price": FLOAT
            }
        ]
    },
    "type": "subscribed/pool_info"
}
Notification
Provides notifications received by an account. Notifications can be of three kinds: liquidation, deleverage, or announcement. Each kind has a different content structure.

JSON

{
    "type": "subscribe",
    "channel": "notification/{ACCOUNT_ID}",
    "auth": "{AUTH_TOKEN}"
}
Response Structure

JSON

{
    "channel": "notification:{ACCOUNT_ID}",
    "notifs": [
        {
            "id": STRING,
            "created_at": STRING,
            "updated_at": STRING,
            "kind": STRING,
            "account_index": INTEGER,
            "content": NotificationContent,
            "ack": BOOLEAN,
            "acked_at": STRING
        }
    ],
    "type": "subscribed/notification"
}
Liquidation Notification Content

JSON

{
    "id": STRING,
    "is_ask": BOOL,
    "usdc_amount": STRING,
    "size": STRING,
    "market_index": INTEGER,
    "price": STRING,
    "timestamp": INTEGER,
    "avg_price": STRING
}
Deleverage Notification Content

JSON

{
    "id": STRING,
    "usdc_amount": STRING,
    "size": STRING,
    "market_index": INTEGER,
    "settlement_price": STRING,
    "timestamp": INTEGER
}
Announcement Notification Content

JSON

{
    "title": STRING,
    "content": STRING, 
    "created_at": INTEGER
}
Example response

JSON

{
    "channel": "notification:12345",
    "notifs": [
        {
            "id": "notif_123",
            "created_at": "2024-01-15T10:30:00Z",
            "updated_at": "2024-01-15T10:30:00Z",
            "kind": "liquidation",
            "account_index": 12345,
            "content": {
                "id": "notif_123",
                "is_ask": false,
                "usdc_amount": "1500.50",
                "size": "0.500000",
                "market_index": 1,
                "price": "3000.00",
                "timestamp": 1705312200,
                "avg_price": "3000.00"
            },
            "ack": false,
            "acked_at": null
        },
        {
            "id": "notif_124",
            "created_at": "2024-01-15T11:00:00Z",
            "updated_at": "2024-01-15T11:00:00Z",
            "kind": "deleverage",
            "account_index": 12345,
            "content": {
                "id": "notif_124",
                "usdc_amount": "500.25",
                "size": "0.200000",
                "market_index": 1,
                "settlement_price": "2501.25",
                "timestamp": 1705314000
            },
            "ack": false,
            "acked_at": null
        }
    ],
    "type": "update/notification"
}
Account Orders
The account orders channel sends data about the orders of an account on a certain market.

JSON

{
    "type": "subscribe",
    "channel": "account_orders/{MARKET_INDEX}/{ACCOUNT_ID}",
    "auth": "{AUTH_TOKEN}"
}
Response Structure

JSON

{
    "account": {ACCOUNT_INDEX}, 
    "channel": "account_orders:{MARKET_INDEX}",
    "nonce": INTEGER,
    "orders": {
        "{MARKET_INDEX}": [Order] // the only present market index will be the one provided
    },
    "type": "update/account_orders"
}
Account All Trades
The account all trades channel sends data about all the trades of an account.

JSON

{
    "type": "subscribe",
    "channel": "account_all_trades/{ACCOUNT_ID}",
    "auth": "{AUTH_TOKEN}"
}
Response Structure

JSON

{
    "channel": "account_all_trades:{ACCOUNT_ID}",
    "trades": {
        "{MARKET_INDEX}": [Trade]
    },
    "total_volume": FLOAT,
    "monthly_volume": FLOAT,
    "weekly_volume": FLOAT,
    "daily_volume": FLOAT,
    "type": "update/account_all_trades"
}
Account All Positions
The account all orders channel sends data about all the orders of an account. auth is required, unless account_id pertains to a public pool.

JSON

{
    "type": "subscribe",
    "channel": "account_all_positions/{ACCOUNT_ID}",
    "auth": "{AUTH_TOKEN}"
}
Response Structure

JSON

{
    "channel": "account_all_positions:{ACCOUNT_ID}",
    "positions": {
        "{MARKET_INDEX}": Position
    },
    "shares": [PoolShares],
    "type": "update/account_all_positions"
}
Spot Market Stats
The spot market stats channel sends the market stat data for the given spot market.

JSON

{
    "type": "subscribe",
    "channel": "spot_market_stats/{MARKET_INDEX}"
}
or

JSON

{
    "type": "subscribe",
    "channel": "spot_market_stats/all"
}
Example Subscription

JSON

{
    "type": "subscribe",
    "channel": "spot_market_stats/2048"
}
Response Structure using all

JSON

{
    "channel": "spot_market_stats:all",
    "spot_market_stats": {
        "{MARKET_INDEX}": {
            "market_id": INTEGER,
            "mid_price": STRING,
            "last_trade_price": STRING,
            "daily_base_token_volume": FLOAT,
            "daily_quote_token_volume": FLOAT,
            "daily_price_low": FLOAT,
            "daily_price_high": FLOAT,
            "daily_price_change": FLOAT
        }
    },
    "type": "update/spot_market_stats"
}
Example Response using all

JSON

{
    "channel": "spot_market_stats:all",
    "spot_market_stats": {
        "2048": {
            "market_id": 2048,
            "mid_price": "3031.70",
            "last_trade_price": "3038.08",
            "daily_base_token_volume": 2181.5557,
            "daily_quote_token_volume": 6597016.394477,
            "daily_price_low": 2988,
            "daily_price_high": 3086.74,
            "daily_price_change": -0.015464392413892946
        }
    },
    "type": "update/spot_market_stats"
}
Response Structure using MARKET_INDEX

JSON

{
    "channel": "spot_market_stats:{MARKET_INDEX}",
    "spot_market_stats": {
        "market_id": INTEGER,
        "mid_price": STRING,
        "last_trade_price": STRING,
        "daily_base_token_volume": FLOAT,
        "daily_quote_token_volume": FLOAT,
        "daily_price_low": FLOAT,
        "daily_price_high": FLOAT,
        "daily_price_change": FLOAT
    },
    "type": "update/spot_market_stats"
}
Example Response using MARKET_INDEX

JSON

{
    "channel": "spot_market_stats:2048",
    "spot_market_stats": {
        "market_id": 2048,
        "mid_price": "3034.57",
        "last_trade_price": "3027.91",
        "daily_base_token_volume": 2589.4525,
        "daily_quote_token_volume": 7830586.177136,
        "daily_price_low": 2988,
        "daily_price_high": 3086.74,
        "daily_price_change": -0.004953404970576774
    },
    "type": "update/spot_market_stats"
}
Account All Assets
The account all assets channel sends specific account market data for all spot markets for a specific account. balance is in coin terms, not USDC (unless asset_index=3, in which case they coincide).

JSON

{
    "type": "subscribe",
    "channel": "account_all_assets/{ACCOUNT_ID}",
		"auth": "{AUTH_TOKEN}"
}
Example Subscription

JSON

{
    "type": "subscribe",
    "channel": "account_all_assets/1234",
  	"auth": "{AUTH_TOKEN}"
}
Response Structure

JSON

{
    "assets": {
      	"{ASSET_INDEX}": [Asset],
        "{ASSET_INDEX}": [Asset]
    },
    "channel": "account_all_assets:{ACCOUNT_ID}",
    "type": "update/account_all_assets"
}
Example Response

JSON

{
    "assets": {
        "1": {
            "symbol": "ETH",
            "asset_id": 1,
            "balance": "7.1072",
            "locked_balance": "0.0000"
        },
        "3": {
            "symbol": "USDC",
            "asset_id": 3,
            "balance": "6343.581906",
            "locked_balance": "297.000000"
        }
    },
    "channel": "account_all_assets:1234",
    "type": "update/account_all_assets"
}
riority Transactions
Priority Transactions offer a way to interact with the Lighter protocol directly via Ethereum directly. You can think of them as censorship-resistant operations - and use them to e.g. cancel all orders or withdraw your collateral. They can be executed via Lighter's proxy smart contract on Ethereum, which holds the platform's collateral: 0x3B4D794a66304F130a4Db8F2551B0070dfCf5ca7.

Read functions:

desertMode: boolean, set to False unless desert mode gets activated.
getPendingBalance: the pending balance for a certain layer 1 account, you can find a complete list of asset IDs via the assetDetails endpoint.
getPendingBalanceLegacy: the pending balance for a certain layer 1 account before the spot upgrade. In this case, it can only be a USDC value.
lastAccountIndex: the highest account index assigned. Only accounts that deposit get assigned an account index, so that would represent the total number of wallets on the exchange.
tokenToAssetIndex: match an ERC20 contract address to its corresponding asset_index on the Lighter protocol
Most have been left out, but you can check out all functions on Ethereum block explorers, e.g. Etherscan.

Write functions:

activateDesertMode
burnShares: allows you to burn shares of a Public Pool.
cancelAllorders: cancels all open orders on Lighter for the specified account index.
cancelOustandingDepositsForDesertMode
changePubKey: assign a newly created api key to an account index. Each key is tied to a single account index (if you use sub-accounts, you'll need to create new ones).
deposit: deposit assets to the platform. See Deposits, Transfers and Withdrawals for more details.
depositBatch: deposit to multiple addresses.
transferERC20: transfer non-ETH spot assets between addresses.
transferETH: transfer mainnet ETH between addresses.
withdraw: withdraw assets from the platform. See Deposits, Transfers and Withdrawals for more details.
withdrawPendingBalance: claim an existing secure withdrawal. Whenever the gas isn't too steep in price, withdrawals will be claimed by the platform on the users' behalf.
withdrawPendingBalanceLegacy: claim an existing secure withdrawal that was requested before the addition of spot assets to the protocol.
Unlisted functions are reserved for the governor (a multi-sig controlled by the protocol) to manage markets and the protocol's settings. If you specify an account_index, you should sign with the wallet that controls said index.

Manage Public Pools
Something to keep in mind is that Lighter considers Public Pools as a special type of Subaccount, where multiple users in addition to its owner can deposit in exchange for pool shares. Hence, you can trade on it via API as you would with a subaccount. Users can participate in Public Pools by creating and modifying them (on a whitelist basis), but also mint and burn shares via API. The corresponding transaction types are:

TxTypeL2CreatePublicPool (10)
TxTypeL2UpdatePublic Pool (11)
TxL2TypeMintShares (18)
TxL2TypeBurnShares (19)
In the hyperlinks, you can find the corresponding examples on the Python SDK using wrapper functions.

You can monitor your shares using the account endpoint, the publicPoolsMetadata endpoint, or any Websocket channel that contains the PoolShares JSON. Note that entry_usdc represents the USDC used to acquire pool shares - if you're looking to get an accurate price per share to date, you can query the publicPoolsMetadata endpoint using account_id plus one. Staking pools are to be considered similar to public pools in structure, wth principal_amount representing the number of coins staked.

This is what a request to fetch LLP's (281474976710654) metadata would look like:

Shell

curl --request GET \
     --url 'https://mainnet.zklighter.elliot.ai/api/v1/publicPoolsMetadata?index=281474976710655&limit=1' \
     --header 'accept: application/json'
The response will look like this:

JSON

{
  "code": 200,
  "public_pools": [
    {
      "code": 0,
      "account_index": 281474976710654,
      "created_at": 1737098583,
      "master_account_index": 1,
      "account_type": 3,
      "name": "Lighter Liquidity Provider (LLP)",
      "l1_address": "0x0000000000000000000000000000000000000000",
      "annual_percentage_yield": 30.733724772746875,
      "sharpe_ratio": 5.004736993685667,
      "status": 0,
      "operator_fee": "0.0000",
      "total_asset_value": "693552603.614245",
      "total_shares": 208742636824
    }
  ]
}
If you provide auth, you can fetch your account's data as well from this endpoint without having to query the account one.

To obtain price_per_share you can then simply calculate total_asset_value/total_shares.


Multi-signature and smart wallets
In the case of multi-signature and smart wallets, you can still access the front-end by signing with your api key with a priority transaction (i.e. using ethereum's priority transactions). To do this, make sure to tick the box shown in the authentication modal.


While most features are available these type of wallts, there are some key differences if you're interacting with them through API. Specifically, functions that require your Ethereum private key as an argument won't be available (e.g. changing public key, and signing a transfer). While you can change public key via priority transactions, you cannot perform a transfer that way - making a secure withdrawal the only way to withdraw funds off the platform.
Create accounts programmatically
To create a Lighter account, you can simply deposit some assets to Lighter using the procedure here. The crediting on mainnet takes a few minutes, after which a master account index gets generated, allowing you to interact with the exchange without ever needing to touch the front-end. If you're using other EVM-compatible chains routed via CCTP, deposits will take around 15-20 minutes to get credited.

Once the account is created, you can verify the assigned account_index querying addressToAccountIndex (0xabf6a038) on Lighter's Ethereum contract, or using the account or accountsByL1Address endpoints.

You can refer to this documentation to then generate API keys in a programmatic way.

Data Structures, Constants and Errors
Data and Event Structures
Go

type Order struct {
	OrderIndex           int64  `json:"i"`
	ClientOrderIndex     int64  `json:"u"`
	OwnerAccountId       int64  `json:"a"`
	InitialBaseAmount    int64  `json:"is"`
	Price                uint32 `json:"p"`
	RemainingBaseAmount  int64  `json:"rs"`
	IsAsk                uint8  `json:"ia"`
	Type                 uint8  `json:"ot"`
	TimeInForce          uint8  `json:"f"`
	ReduceOnly           uint8  `json:"ro"`
	TriggerPrice         uint32 `json:"tp"`
	Expiry               int64  `json:"e"`
	Status               uint8  `json:"st"`
	TriggerStatus        uint8  `json:"ts"`
	ToTriggerOrderIndex0 int64  `json:"t0"`
	ToTriggerOrderIndex1 int64  `json:"t1"`
	ToCancelOrderIndex0  int64  `json:"c0"`
}

type OrderExecution struct {
	MarketId   int16  `json:"m"`
	Trade      *Trade `json:"t"`
	MakerOrder *Order `json:"mo"`
	TakerOrder *Order `json:"to"`
	AppError string `json:"ae"`
}

type CancelOrder struct {
	AccountId        int64 `json:"a"`
	OrderIndex       int64 `json:"i"`
	ClientOrderIndex int64 `json:"u"`
	AppError string `json:"ae"`
}

type ModifyOrder struct {
	MarketId uint8  `json:"m"`
	OldOrder *Order `json:"oo"`
	NewOrder *Order `json:"no"`
	AppError string `json:"ae"`
}


type Trade struct {
	Price    uint32 `json:"p"`
	Size     int64  `json:"s"`
	TakerFee int32  `json:"tf"`
	MakerFee int32  `json:"mf"`
}

// Order Status
const (
  InProgressOrder  = iota // In register
  PendingOrder            // Pending to be triggered
  ActiveLimitOrder        // Active limit order
  FilledOrder // 3
  CanceledOrder // 4
  CanceledOrder_PostOnly // 5
  CanceledOrder_ReduceOnly // 6
  CanceledOrder_PositionNotAllowed // 7
  CanceledOrder_MarginNotAllowed // 8 
  CanceledOrder_TooMuchSlippage // 9 
  CanceledOrder_NotEnoughLiquidity // 10
  CanceledOrder_SelfTrade // 11
  CanceledOrder_Expired // 12
  CanceledOrder_OCO // 13
  CanceledOrder_Child // 14
  CanceledOrder_Liquidation // 15
  CanceledOrder_InvalidBalance // 16

Constants
Go

TxTypeL2ChangePubKey     = 8
TxTypeL2CreateSubAccount = 9
TxTypeL2CreatePublicPool = 10
TxTypeL2UpdatePublicPool = 11
TxTypeL2Transfer         = 12
TxTypeL2Withdraw         = 13
TxTypeL2CreateOrder      = 14
TxTypeL2CancelOrder      = 15
TxTypeL2CancelAllOrders  = 16
TxTypeL2ModifyOrder      = 17
TxTypeL2MintShares       = 18
TxTypeL2BurnShares       = 19
TxTypeL2UpdateLeverage   = 20
TxTypeL2CreateGroupedOrders = 28
TxTypeL2UpdateMargin        = 29
TxTypeL1BurnShares          = 30
See all constants here: https://github.com/elliottech/lighter-go/blob/37514ad5630052c162fa0745ac59ae47ff33d148/types/txtypes/constants.go

Transaction Status Mapping
Go

0: Failed
1: Pending
2: Executed
3: Pending - Final State
Error Codes
Go

// Tx
	AppErrTxNotFound                         = NewBusinessError(21500, "transaction not found")
	AppErrInvalidTxInfo                      = NewBusinessError(21501, "invalid tx info")
	AppErrMarshalTxFailed                    = NewBusinessError(21502, "marshal tx failed")
	AppErrMarshalEventsFailed                = NewBusinessError(21503, "marshal event failed")
	AppErrFailToL1Signature                  = NewBusinessError(21504, "fail to l1 signature")
	AppErrUnsupportedTxType                  = NewBusinessError(21505, "unsupported tx type")
	AppErrTooManyTxs                         = NewBusinessError(21506, "too many pending txs. Please try again later")
	AppErrAccountBelowMaintenanceMargin      = NewBusinessError(21507, "account is below maintenance margin, can't execute transaction")
	AppErrAccountBelowInitialMargin          = NewBusinessError(21508, "account is below initial margin, can't execute transaction")
	AppErrInvalidTxTypeForAccount            = NewBusinessError(21511, "invalid tx type for account")
	AppErrInvalidL1RequestId                 = NewBusinessError(21512, "invalid l1 request id")
	AppErrTxInfoTxTypeLengthMismatch         = NewBusinessError(21513, "TxInfos and TxTypes should have the same length")
	AppErrMaxBatchTx                         = NewBusinessError(21514, "maximum 50 transactions allowed per batch")
	AppErrCannotCreateTxOnAsset              = NewBusinessError(21515, "transaction is not allowed")
	AppErrTreasuryOutgoingTransferNotAllowed = NewBusinessError(21516, "outgoing transfers from treasury account are not allowed")

	// OrderBook
	AppErrInactiveCancel             = NewBusinessError(21600, "given order is not an active limit order")
	AppErrOrderBookFull              = NewBusinessError(21601, "order book is full")
	AppErrInvalidMarketIndex         = NewBusinessError(21602, "invalid market index")
	AppErrInvalidMinAmountsForMarket = NewBusinessError(21603, "invalid min amounts for market")
	// 21604 deprecated
	AppErrInvalidMarketStatus           = NewBusinessError(21605, "invalid market status")
	AppErrMarketAlreadyExist            = NewBusinessError(21606, "market already exist for given index")
	AppErrInvalidMarketFees             = NewBusinessError(21607, "invalid market fees")
	AppErrInvalidQuoteMultiplier        = NewBusinessError(21608, "invalid quote multiplier")
	AppErrInvalidInterestRate           = NewBusinessError(21611, "invalid interest rate")
	AppErrInvalidOpenInterest           = NewBusinessError(21612, "invalid open interest")
	AppErrInvalidMarginMode             = NewBusinessError(21613, "invalid margin mode")
	AppErrNoPositionFound               = NewBusinessError(21614, "no position found")
	AppErrInvalidUpdateMarginDirection  = NewBusinessError(21615, "invalid update margin direction")
	AppErrAssetNotExist                 = NewBusinessError(21616, "asset does not exists for given index")
	AppErrInvalidCreateMarketParameters = NewBusinessError(21617, "invalid create market parameters")
	AppErrInvalidOrderTypeForMarket     = NewBusinessError(21618, "invalid order type for market")
	AppErrInvalidMarketType             = NewBusinessError(21619, "invalid market type")
	AppErrInvalidFundingClamp           = NewBusinessError(21620, "invalid funding clamp")
	AppErrInvalidPerpsMarketIndex       = NewBusinessError(21621, "invalid perps market index")
	AppErrInvalidOrderQuoteLimit        = NewBusinessError(21622, "invalid order quote limit")
	AppErrInvalidOpenInterestLimit      = NewBusinessError(21623, "invalid open interest limit")
	AppErrInvalidMinBaseAmount          = NewBusinessError(21624, "invalid min base amount")
	AppErrInvalidMinQuoteAmount         = NewBusinessError(21625, "invalid min quote amount")
	AppErrInvalidMarginFraction         = NewBusinessError(21626, "invalid margin fraction")

	// Order
	AppErrInvalidOrderIndex                        = NewBusinessError(21700, "invalid order index")
	AppErrInvalidBaseAmount                        = NewBusinessError(21701, "invalid base amount")
	AppErrInvalidPrice                             = NewBusinessError(21702, "invalid price")
	AppErrInvalidIsAsk                             = NewBusinessError(21703, "invalid isAsk")
	AppErrInvalidOrderType                         = NewBusinessError(21704, "invalid OrderType")
	AppErrInvalidOrderTimeInForce                  = NewBusinessError(21705, "invalid OrderTimeInForce")
	AppErrInvalidOrderAmount                       = NewBusinessError(21706, "invalid order base or quote amount")
	AppErrInvalidOrderOwner                        = NewBusinessError(21707, "account is not owner of the order")
	AppErrEmptyOrder                               = NewBusinessError(21708, "order is empty")
	AppErrInactiveOrder                            = NewBusinessError(21709, "order is inactive")
	AppErrUnsupportedOrderType                     = NewBusinessError(21710, "unsupported order type")
	AppErrInvalidOrderExpiry                       = NewBusinessError(21711, "invalid expiry")
	AppErrAccountHasAQueuedCancelAllOrdersRequest  = NewBusinessError(21712, "account has a queued cancel all orders request")
	AppErrInvalidCancelAllTimeInForce              = NewBusinessError(21713, "invalid cancel all time in force")
	AppErrInvalidCancelAllTime                     = NewBusinessError(21714, "invalid cancel all time")
	AppErrInctiveOrder                             = NewBusinessError(21715, "given order is not an active order")
	AppErrOrderNotExpired                          = NewBusinessError(21716, "order is not expired")
	AppErrMaxOrdersPerAccount                      = NewBusinessError(21717, "maximum active limit order count reached")
	AppErrMaxOrdersPerAccountPerMarket             = NewBusinessError(21718, "maximum active limit order count per market reached")
	AppErrMaxPendingOrdersPerAccount               = NewBusinessError(21719, "maximum pending order count reached")
	AppErrMaxPendingOrdersPerAccountPerMarket      = NewBusinessError(21720, "maximum pending order count per market reached")
	AppErrMaxTWAPOrdersInExchange                  = NewBusinessError(21721, "maximum twap order count reached")
	AppErrMaxConditionalOrdersInExchange           = NewBusinessError(21722, "maximum conditional order count reached")
	AppErrInvalidAccountHealth                     = NewBusinessError(21723, "invalid account health")
	AppErrInvalidLiquidationSize                   = NewBusinessError(21724, "invalid liquidation size")
	AppErrInvalidLiquidationPrice                  = NewBusinessError(21725, "invalid liquidation price")
	AppErrInsuranceFundCannotBePartiallyLiquidated = NewBusinessError(21726, "insurance fund cannot be partially liquidated")
	AppErrInvalidClientOrderIndex                  = NewBusinessError(21727, "invalid client order index")
	AppErrClientOrderIndexExists                   = NewBusinessError(21728, "client order index already exists")
	AppErrInvalidOrderTriggerPrice                 = NewBusinessError(21729, "invalid order trigger price")
	AppOrderStatusIsNotPending                     = NewBusinessError(21730, "order status is not pending")
	AppPendingOrderCanNotBeTriggered               = NewBusinessError(21731, "order can not be triggered")
	AppReduceOnlyIncreasesPosition                 = NewBusinessError(21732, "reduce only increases position")
	AppErrFatFingerPrice                           = NewBusinessError(21733, "order price flagged as an accidental price")
	AppErrPriceTooFarFromMarkPrice                 = NewBusinessError(21734, "limit order price is too far from the mark price")
	AppErrPriceTooFarFromTrigger                   = NewBusinessError(21735, "SL/TP order price is too far from the trigger price")
	AppErrInvalidOrderTriggerStatus                = NewBusinessError(21736, "invalid order trigger status")
	AppErrInvalidOrderStatus                       = NewBusinessError(21737, "invalid order status")
	AppErrInvalidReduceOnlyDirection               = NewBusinessError(21738, "invalid reduce only direction")
	AppErrNotEnoughOrderMargin                     = NewBusinessError(21739, "not enough margin to create the order")
	AppErrInvalidReduceOnlyMode                    = NewBusinessError(21740, "invalid reduce only mode")
	AppErrInvalidGroupingType                      = NewBusinessError(21741, "invalid grouping type")
	AppErrInvalidOrderGroupSize                    = NewBusinessError(21742, "invalid order group size")
	AppErrInvalidOrderInfo                         = NewBusinessError(21743, "invalid order info")
	AppErrInvalidAccountTypeForSpotMarket          = NewBusinessError(21744, "pools are not allowed to trade in spot markets")
	AppErrInvalidMarketTypeForL1Order              = NewBusinessError(21745, "only perps markets are allowed for L1 orders")

	// Asset
	AppErrInvalidAssetIndex          = NewBusinessError(21801, "invalid asset index")
	AppErrInvalidAssetMarginMode     = NewBusinessError(21802, "invalid asset margin mode")
	AppErrAssetAlreadyExists         = NewBusinessError(21803, "asset already exists for given index")
	AppErrAssetDoesNotExists         = NewBusinessError(21804, "asset does not exist for given index")
	AppErrOnlyUSDCTransferSupported  = NewBusinessError(21805, "only usdc transfer supported")
	AppErrInvalidExtensionMultiplier = NewBusinessError(21806, "invalid extension multiplier")
	AppErrInvalidMinTransferAmount   = NewBusinessError(21807, "invalid min transfer amount")
	AppErrInvalidMinWithdrawalAmount = NewBusinessError(21808, "invalid min withdrawal amount")
	AppErrAssetNotFound              = NewBusinessError(21809, "asset not found")

	// Deleverage
	AppErrDeleverageAgainstItself                 = NewBusinessError(21901, "deleverage against itself")
	AppErrDeleverageDoesNotMatchLiquidationStatus = NewBusinessError(21902, "deleverage does not match liquidation status")
	AppErrDeleverageWithOpenOrders                = NewBusinessError(21903, "deleverage with open orders")
	AppErrInvalidDeleverageSize                   = NewBusinessError(21904, "invalid deleverage size")
	AppErrInvalidDeleveragePrice                  = NewBusinessError(21905, "invalid deleverage price")
	AppErrInvalidDeleverageSide                   = NewBusinessError(21906, "invalid deleverage side")

	// Candlestick
	AppErrInvalidTimestamps     = NewBusinessError(22400, "invalid timestamps: end_timestamp must be greater than start_timestamp")
	AppErrInvalidTimestamp      = NewBusinessError(22401, "invalid timestamp: timestamp must be greater than 0 and less than year 2286")
	AppErrInvalidResolution     = NewBusinessError(22402, "invalid resolution: resolution unsupported")
	AppErrTimeRangeExceedsLimit = NewBusinessError(22403, "time range exceeds maximum allowed range for the specified resolution")

	// RateLimit
	AppErrTooManyRequest           = NewBusinessError(23000, "Too Many Requests!")
	AppErrTooManySubscriptions     = NewBusinessError(23001, "Too Many Subscriptions!")
	AppErrTooManyDifferentAccounts = NewBusinessError(23002, "Too Many Different Accounts!")
	AppErrTooManyConnections       = NewBusinessError(23003, "Too Many Connections!")
	AppErrTooManyL2Withdrawals     = NewBusinessError(23004, "Too Many L2 Withdrawal Requests!")

	// General Errors
	AppErrNotFound = NewBusinessError(29404, "not found")
	AppErrInternal = NewBusinessError(29500, "internal server error")
	AppTimeout     = NewBusinessError(29501, "process timeout")

	// Websocket
	AppErrWebsocketInvalidJson        = NewBusinessError(30000, "Invalid Json")
	AppErrWebsocketInvalidType        = NewBusinessError(30001, "Invalid Type")
	AppErrWebsocketNotSubscribed      = NewBusinessError(30002, "Not Subscribed to ")
	AppErrWebsocketAlreadySubscribed  = NewBusinessError(30003, "Already Subscribed to ")
	AppErrWebsocketFetchFailed        = NewBusinessError(30004, "Failed to fetch ")
	AppErrWebsocketInvalidChannel     = NewBusinessError(30005, "Invalid Channel")
	AppErrWebsocketNotSupported       = NewBusinessError(30006, "Operation isn't supported ")
	AppErrWebsocketInvalidData        = NewBusinessError(30007, "Invalid Data")
	AppErrWebsocketInvalidAccountType = NewBusinessError(30008, "Invalid account type")
	AppErrWebsocketRateLimit          = NewBusinessError(30009, "Too Many Websocket Messages!")
	AppErrWebsocketTooManyInflight    = NewBusinessError(30010, "Too Many Inflight Messages!")
	AppErrWebsocketFailedToConnect    = NewBusinessError(30011, "Failed to connect")
	AppErrWebsocketFailedToSubscribe  = NewBusinessError(30012, "Failed to subscribe")

	// Referral
	AppErrReferralAlreadyExists      = NewBusinessError(41001, "Referral code already exists")
	AppErrReferralExpired            = NewBusinessError(41002, "Referral code is expired")
	AppErrReferralAlreadyUsed        = NewBusinessError(41003, "Referral code already used")
	AppErrReferralUserHasAccess      = NewBusinessError(41004, "User can already access")
	AppErrReferralUserCantInvite     = NewBusinessError(41005, "User can't invite")
	AppErrReferralInvalid            = NewBusinessError(41006, "Invalid referral code")
	AppErrReferralRequired           = NewBusinessError(41007, "Referral code is required")
	AppErrReferralKickbackUpdate     = NewBusinessError(41008, "Kickback can only be updated once per week")
	AppErrReferralCodeAlreadyUpdated = NewBusinessError(41009, "Referral code has already been updated once, cannot update again")
	AppErrReferralCodeInvalid        = NewBusinessError(41010, "Referral code must be 4-14 characters and contain only uppercase letters (A-Z) and numbers (0-9)")
	AppErrReferralOnlyMainAccount    = NewBusinessError(41011, "only main account index is valid, please use the main account")
	AppErrReferralCannotUseOwnCode   = NewBusinessError(41012, "cannot use your own referral code")

	// Read Only API Token
	AppErrAPITokenExpiryBeforeMinAllowed   = NewBusinessError(61001, "api token expiry is before minimum allowed expiry of 1 day")
	AppErrAPITokenExpiryAfterMaxAllowed    = NewBusinessError(61002, "api token expiry is after maximum allowed expiry of 10 years")
	AppErrAPITokenMaxTokensExceeded        = NewBusinessError(61003, "maximum number of 10 api tokens for the account exceeded")
	AppErrAPITokenCustomScopesNotSupported = NewBusinessError(61004, "custom scopes for api tokens are not supported yet")
	AppErrAPITokenNotFound                 = NewBusinessError(61005, "api token not found or does not belong to this account")
	AppErrAPITokenAlreadyRevoked           = NewBusinessError(61006, "api token has already been revoked")
	AppErrAPITokenNameEmpty                = NewBusinessError(61007, "api token name cannot be empty")
	AppErrAPITokenNameTooLong              = NewBusinessError(61008, "api token name cannot exceed 50 characters")
	AppErrAPITokenNameInvalidChars         = NewBusinessError(61009, "api token name can only contain letters, numbers, spaces, hyphens, underscores, and periods")

	// Tier Change
	AppErrTierChangeInProgress       = NewBusinessError(62001, "tier change already in progress")
	AppErrTierChangeInvalidTier      = NewBusinessError(62002, "invalid tier")
	AppErrTierChangeSameTier         = NewBusinessError(62003, "account already part of requested tier")
	AppErrTierChangeHasOpenPositions = NewBusinessError(62004, "account has open positions")
	AppErrTierChangeHasOpenOrders    = NewBusinessError(62005, "account has open orders")
	AppErrTierChangeTooManyRequest   = NewBusinessError(62006, "too frequent tier change request")

https://apidocs.lighter.xyz/reference/status